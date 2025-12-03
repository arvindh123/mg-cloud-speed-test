import json
import os
from pathlib import Path
from urllib.parse import urlparse

import matplotlib.pyplot as plt

# Scenarios and colors
SCENARIOS = [
    ("Without CF (DO LB)", "Without-CF-Proxy-Direct-DO-LB"),
    ("With CF Proxy", "With-CF-Proxy"),
    ("With CF Proxy + CF Tunnel", "With-CF-Proxy-CF-Tunnel"),
]
COLORS = {
    "Without CF (DO LB)": "#1f77b4",
    "With CF Proxy": "#ff7f0e",
    "With CF Proxy + CF Tunnel": "#2ca02c",
}

# Location helpers
LOC_DISPLAY = {
    "frankfurt": "Frankfurt",
    "frankfurth": "Frankfurt",
    "london": "London",
    "san-francisco": "San Francisco",
    "san-fransico": "San Francisco",
    "san-franscisco": "San Francisco",
    "sao-paulo": "São Paulo",
    "sydney": "Sydney",
    "tokyo": "Tokyo",
    "washington-dc": "Washington, DC",
}
LOC_ORDER = [
    "frankfurt",
    "frankfurth",
    "london",
    "san-francisco",
    "san-fransico",
    "san-franscisco",
    "sao-paulo",
    "sydney",
    "tokyo",
    "washington-dc",
]


def norm_loc(raw: str) -> str:
    return {
        "frankfurt": "frankfurt",
        "frankfurth": "frankfurt",
        "london": "london",
        "san-francisco": "san-francisco",
        "san-fransico": "san-francisco",
        "san-franscisco": "san-francisco",
        "sao-paulo": "sao-paulo",
        "sydney": "sydney",
        "tokyo": "tokyo",
        "washington-dc": "washington-dc",
    }.get(raw, raw)


def load_har_data():
    data = {}  # url -> (scenario, loc) -> metrics
    summary = {}  # scenario -> loc -> (reqs, size_bytes, fully_loaded_ms)
    urls = set()

    for scenario_label, folder in SCENARIOS:
        for path in sorted(Path(folder).glob("profile-page-*.json")):
            raw_loc = path.name.split("profile-page-", 1)[1].rsplit(".", 1)[0]
            loc = norm_loc(raw_loc)
            har = json.loads(path.read_text())
            entries = har.get("log", {}).get("entries", [])
            reqs = len(entries)
            size = sum(
                e.get("response", {}).get("content", {}).get("size", 0) or 0
                for e in entries
                if isinstance(
                    e.get("response", {}).get("content", {}).get("size"), (int, float)
                )
            )
            load = (
                har.get("log", {})
                .get("pages", [{}])[0]
                .get("pageTimings", {})
                .get("_fullyLoaded")
            )
            summary.setdefault(scenario_label, {})[loc] = (reqs, size, load)

            for e in entries:
                req = e.get("request", {})
                url = req.get("url")
                if not url:
                    continue
                urls.add(url)
                resp = e.get("response", {})
                content = resp.get("content", {})
                hdrs = {h["name"].lower(): h["value"] for h in resp.get("headers", [])}
                t = e.get("timings", {})
                data.setdefault(url, {})[(scenario_label, loc)] = {
                    "dns": t.get("dns"),
                    "connect": t.get("connect"),
                    "ssl": t.get("ssl"),
                    "wait": t.get("wait"),
                    "receive": t.get("receive"),
                    "blocked": t.get("blocked"),
                    "status": resp.get("status"),
                    "mime": content.get("mimeType", ""),
                    "size": content.get("size", ""),
                    "cf_ray": hdrs.get("cf-ray", ""),
                }
    return data, summary, urls


def plot_grouped(metric_by_scenario, ylabel, title, out_path):
    x = range(len(LOC_ORDER))
    regions = [LOC_DISPLAY.get(loc, loc).replace("Washington, DC", "Washington DC") for loc in LOC_ORDER]
    width = 0.25
    fig, ax = plt.subplots(figsize=(11, 5))
    for idx, scenario in enumerate(SCENARIOS):
        label = scenario[0]
        offsets = [xi + (idx - 1) * width for xi in x]
        ax.bar(offsets, metric_by_scenario[label], width, label=label, color=COLORS[label])
    ax.set_xticks([xi for xi in x])
    ax.set_xticklabels(regions, rotation=20, ha="right")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_path, dpi=200)
    plt.close(fig)


def ensure_clean_dir(path: Path):
    if path.exists():
        for f in path.glob("*.png"):
            f.unlink()
        if (path / "index.html").exists():
            (path / "index.html").unlink()
    else:
        path.mkdir(parents=True)


def main():
    data, summary, urls = load_har_data()
    out_dir = Path("docs/profile-page")
    ensure_clean_dir(out_dir)

    # Summary load-time chart
    load_chart = {
        scenario: [
            (summary.get(scenario, {}).get(loc, (0, 0, 0))[2] or 0) / 1000
            for loc in LOC_ORDER
        ]
        for scenario, _ in SCENARIOS
    }
    plot_grouped(
        load_chart,
        "Seconds",
        "Page Load Time (_fullyLoaded) by Region",
        out_dir / "summary_load_time.png",
    )

    # Per-URL charts by metric
    metrics = [
        ("dns", "DNS (ms)"),
        ("connect", "Connect (ms)"),
        ("ssl", "SSL (ms)"),
        ("wait", "Wait/TTFB (ms)"),
        ("receive", "Content download (ms)"),
    ]

    html = [
        "<html><head><title>Profile Page Chart Pack</title></head><body>",
        "<h1>Profile Page Chart Pack</h1>",
        "<p>Scenarios: Without CF (DO LB), With CF Proxy, With CF Proxy + CF Tunnel.</p>",
        '<div><h2>Summary</h2><img src="summary_load_time.png" width="900"></div>',
        "<h2>Per-request metrics</h2>",
    ]

    for url in sorted(urls):
        parsed = urlparse(url)
        path = parsed.path
        if parsed.query:
            path += "?" + parsed.query
        safe = (
            path.replace("/", "_")
            .replace("?", "_")
            .replace(":", "_")
            .replace("%", "_")
            .strip("_")
        )
        html.append(f"<h3>{path}</h3>")

        for metric_key, metric_label in metrics:
            # For DNS/Connect/SSL, only draw if every scenario/region has a value
            if metric_key in {"dns", "connect", "ssl"}:
                complete = True
                for scenario, _ in SCENARIOS:
                    for loc in LOC_ORDER:
                        entry = data.get(url, {}).get((scenario, loc))
                        if not entry or entry.get(metric_key) is None:
                            complete = False
                            break
                    if not complete:
                        break
                if not complete:
                    continue

            metric_vals = {
                scenario: [
                    data.get(url, {}).get((scenario, loc), {}).get(metric_key, 0) or 0
                    for loc in LOC_ORDER
                ]
                for scenario, _ in SCENARIOS
            }

            title_suffix = ""
            if metric_key == "receive":
                sizes = []
                for scenario, _ in SCENARIOS:
                    size_val = None
                    for loc in LOC_ORDER:
                        entry = data.get(url, {}).get((scenario, loc))
                        if entry and entry.get("size") not in (None, ""):
                            size_val = entry["size"]
                            break
                    sizes.append(f"{scenario}: {size_val if size_val is not None else 'n/a'} bytes")
                title_suffix = " (" + "; ".join(sizes) + ")"
            filename = f"{safe}_{metric_key}.png"
            plot_grouped(
                metric_vals,
                metric_label,
                f"{metric_label} by Region: {path}{title_suffix}",
                out_dir / filename,
            )
            html.append(f'<div><p>{metric_label}</p><img src="{filename}" width="900"></div>')

    html.append("</body></html>")
    (out_dir / "index.html").write_text("\n".join(html))
    print(f"Charts written to {out_dir} and index.html generated.")


if __name__ == "__main__":
    main()

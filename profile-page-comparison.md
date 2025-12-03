## HAR comparison: Without CF vs CF Proxy vs CF Proxy + CF Tunnel (profile page)

Scenarios:
- Without CF (DO LB): direct to DigitalOcean Frankfurt (Kubernetes, DO LB + ingress-nginx)
- With CF Proxy: Cloudflare proxy in front of the same origin
- With CF Proxy + CF Tunnel: Cloudflare proxy plus CF Tunnel to origin

Summary by scenario/location:

| Scenario | Location | Requests | Page size (KB) | Load time (s, `_fullyLoaded`) | CF-ray edge |
|---|---|---:|---:|---:|---|
| Without CF (DO LB) | Frankfurt | 31 | 1369.84 | 1.361 | — |
| With CF Proxy | Frankfurt | 34 | 1380.48 | 1.105 | FRA |
| With CF Proxy + CF Tunnel | Frankfurt | 34 | 1380.48 | 0.804 | FRA |
| Without CF (DO LB) | London | 29 | 1244.90 | 1.630 | — |
| With CF Proxy | London | 34 | 1380.67 | 3.602 | LHR |
| With CF Proxy + CF Tunnel | London | 34 | 1380.47 | 1.287 | LHR |
| Without CF (DO LB) | San Francisco | 31 | 1369.84 | 2.968 | — |
| With CF Proxy | San Francisco | 36 | 1400.64 | 3.410 | SJC |
| With CF Proxy + CF Tunnel | San Francisco | 36 | 1400.45 | 4.092 | SJC |
| Without CF (DO LB) | São Paulo | 31 | 1369.84 | 3.508 | — |
| With CF Proxy | São Paulo | 34 | 1275.52 | 3.579 | GRU |
| With CF Proxy + CF Tunnel | São Paulo | 34 | 1275.66 | 2.672 | GRU |
| Without CF (DO LB) | Sydney | 31 | 1369.84 | 4.671 | — |
| With CF Proxy | Sydney | 36 | 1400.57 | 4.401 | SYD |
| With CF Proxy + CF Tunnel | Sydney | 36 | 1400.48 | 2.939 | SYD |
| Without CF (DO LB) | Tokyo | 31 | 1369.84 | 4.032 | — |
| With CF Proxy | Tokyo | 36 | 1400.40 | 4.313 | NRT |
| With CF Proxy + CF Tunnel | Tokyo | 36 | 1400.64 | 2.323 | NRT |
| Without CF (DO LB) | Washington, DC | 31 | 1369.84 | 4.361 | — |
| With CF Proxy | Washington, DC | 34 | 1275.57 | 1.719 | IAD |
| With CF Proxy + CF Tunnel | Washington, DC | 34 | 1275.65 | 3.363 | IAD |

Mermaid bar chart – `_fullyLoaded` load time by region:

```mermaid
bar
  title Load time (s) by region and scenario
  xaxis Region
  yaxis Load time (s)
  series
    title Without CF (DO LB)
    data 1.361 1.630 2.968 3.508 4.671 4.032 4.361
  series
    title With CF Proxy
    data 1.105 3.602 3.410 3.579 4.401 4.313 1.719
  series
    title With CF Proxy + CF Tunnel
    data 0.804 1.287 4.092 2.672 2.939 2.323 3.363
  categories Frankfurt,London,San Francisco,São Paulo,Sydney,Tokyo,Washington, DC
```

### /_next/static/chunks/0f9dcbb3-4ea2e6533b43a41b.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 191.88 | 95.95 | 0.19 | 200 | application/javascript | 69536 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 11.12 | 2.15 | 0.50 | 200 | application/javascript | 69536 | 9a84227a388edc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.70 | 0.76 | 0.88 | 200 | application/javascript | 69536 | 9a84a8f0086ee866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 66.63 | 59.86 | 0.36 | 200 | application/javascript | 69536 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 34.42 | 2.45 | 0.43 | 200 | application/javascript | 69536 | 9a8450feadf86412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.07 | 3.24 | 0.18 | 200 | application/javascript | 69536 | 9a84a99fcd7588ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 160.30 | 20.15 | 0.24 | 200 | application/javascript | 69536 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 173.90 | 1.01 | 0.32 | 200 | application/javascript | 69536 | 9a845fd90b24cb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 14.04 | 4.50 | 1.81 | 200 | application/javascript | 69536 | 9a84aca71eda33fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 208.50 | 19.08 | 0.26 | 200 | application/javascript | 69536 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 208.42 | 1.73 | 0.24 | 200 | application/javascript | 69536 | 9a84636efd3b2788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.01 | 2.16 | 3.14 | 200 | application/javascript | 69536 | 9a84afa2ed96bc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 302.16 | 28.96 | 0.26 | 200 | application/javascript | 69536 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 307.71 | 1.05 | 0.25 | 200 | application/javascript | 69536 | 9a846146192ea959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 5.27 | 3.67 | 1.45 | 200 | application/javascript | 69536 | 9a84ae1ab9b2e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 243.50 | 21.00 | 0.30 | 200 | application/javascript | 69536 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 255.88 | 1.01 | 1.39 | 200 | application/javascript | 69536 | 9a841d85cf4de382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.13 | 0.85 | 0.23 | 200 | application/javascript | 69536 | 9a84a846db3fb200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 102.27 | 9.78 | 0.29 | 200 | application/javascript | 69536 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 11.33 | 1.51 | 0.17 | 200 | application/javascript | 69536 | 9a845e8aa9188c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.67 | 2.78 | 0.62 | 200 | application/javascript | 69536 | 9a84aa811c7faf04-IAD |

### /_next/static/chunks/2065e367-738d69ba223595b9.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 15.01 | 75.23 | 0.43 | 200 | application/javascript | 157100 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 8.89 | 2.28 | 0.43 | 200 | application/javascript | 157100 | 9a84227a38b1dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 12.96 | 2.76 | 0.28 | 200 | application/javascript | 157100 | 9a84a8f0089fe866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 60.78 | 186.02 | 0.37 | 200 | application/javascript | 157100 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 44.48 | 2.61 | 2.62 | 200 | application/javascript | 157100 | 9a8450feee1e6412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.31 | 2.39 | 0.29 | 200 | application/javascript | 157100 | 9a84a99fdd8388ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 333.67 | 186.18 | 0.30 | 200 | application/javascript | 157100 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 171.48 | 8.13 | 0.20 | 200 | application/javascript | 157100 | 9a845fd92b5dcb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.57 | 4.08 | 4.26 | 200 | application/javascript | 157100 | 9a84aca73f3233fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 210.64 | 39.74 | 0.26 | 200 | application/javascript | 157100 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 210.95 | 2.14 | 0.36 | 200 | application/javascript | 157100 | 9a84636f0d522788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.60 | 1.78 | 0.29 | 200 | application/javascript | 157100 | 9a84afa2edb0bc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 304.69 | 67.57 | 0.27 | 200 | application/javascript | 157100 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 314.82 | 2.31 | 0.28 | 200 | application/javascript | 157100 | 9a846146393da959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.12 | 6.42 | 1.21 | 200 | application/javascript | 157100 | 9a84ae1ac9cce7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 253.11 | 58.34 | 0.22 | 200 | application/javascript | 157100 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 246.02 | 2.33 | 0.18 | 200 | application/javascript | 157100 | 9a841d85df87e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.58 | 2.34 | 1.07 | 200 | application/javascript | 157100 | 9a84a846db50b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 106.08 | 23.59 | 1.51 | 200 | application/javascript | 157100 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 21.76 | 3.36 | 0.29 | 200 | application/javascript | 157100 | 9a845e8aa9448c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.20 | 7.25 | 0.24 | 200 | application/javascript | 157100 | 9a84aa811c93af04-IAD |

### /_next/static/chunks/28214-f7bd4fbe2e13f9bd.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 8.15 | 0.33 | 0.34 | 200 | application/javascript | 11457 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 9.14 | 0.44 | 0.26 | 200 | application/javascript | 11457 | 9a84227a58e9dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.79 | 0.49 | 0.29 | 200 | application/javascript | 11457 | 9a84a8f028ebe866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 19.34 | 3.76 | 0.49 | 200 | application/javascript | 11457 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 34.13 | 0.43 | 0.53 | 200 | application/javascript | 11457 | 9a8450ff2e3d6412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.81 | 0.51 | 0.20 | 200 | application/javascript | 11457 | 9a84a99fedd688ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 206.37 | 0.33 | 0.26 | 200 | application/javascript | 11457 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 484.48 | 1.82 | 0.26 | 200 | application/javascript | 11457 | 9a845fda7dafcb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.89 | 0.30 | 0.68 | 200 | application/javascript | 11457 | 9a84aca74f6c33fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 206.05 | 0.92 | 0.25 | 200 | application/javascript | 11457 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 208.34 | 0.39 | 0.28 | 200 | application/javascript | 11457 | 9a8463706f9e2788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.28 | 0.38 | 0.24 | 200 | application/javascript | 11457 | 9a84afa30de2bc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 303.26 | 0.33 | 0.23 | 200 | application/javascript | 11457 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 301.96 | 0.39 | 0.83 | 200 | application/javascript | 11457 | 9a8461483a35a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.77 | 2.13 | 1.72 | 200 | application/javascript | 11457 | 9a84ae1aea13e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 246.69 | 0.33 | 0.20 | 200 | application/javascript | 11457 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 255.69 | 0.43 | 0.20 | 200 | application/javascript | 11457 | 9a841d877b16e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.86 | 0.42 | 1.74 | 200 | application/javascript | 11457 | 9a84a846fb64b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 102.98 | 0.72 | 0.25 | 200 | application/javascript | 11457 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 21.24 | 0.52 | 0.48 | 200 | application/javascript | 11457 | 9a845e8ad9d28c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 14.06 | 0.33 | 0.51 | 200 | application/javascript | 11457 | 9a84aa813d16af04-IAD |

### /_next/static/chunks/28381-f69fef083c6248e7.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 7.60 | 0.39 | 0.25 | 200 | application/javascript | 23076 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 7.73 | 0.42 | 0.20 | 200 | application/javascript | 23076 | 9a84227a58ecdc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.62 | 0.94 | 1.28 | 200 | application/javascript | 23076 | 9a84a8f028f8e866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 22.24 | 0.55 | 0.34 | 200 | application/javascript | 23076 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 32.71 | 0.75 | 1.47 | 200 | application/javascript | 23076 | 9a8450ff3e4c6412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.52 | 0.79 | 1.96 | 200 | application/javascript | 23076 | 9a84a99ffdf288ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 166.28 | 8.78 | 0.23 | 200 | application/javascript | 23076 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 176.61 | 0.47 | 0.24 | 200 | application/javascript | 23076 | 9a845fdb3eebcb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.25 | 2.19 | 0.62 | 200 | application/javascript | 23076 | 9a84aca74f6f33fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 206.29 | 2.55 | 0.26 | 200 | application/javascript | 23076 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 208.52 | 0.40 | 0.17 | 200 | application/javascript | 23076 | 9a8463709fdd2788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.86 | 0.44 | 0.26 | 200 | application/javascript | 23076 | 9a84afa30de3bc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 303.02 | 3.27 | 0.23 | 200 | application/javascript | 23076 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 303.05 | 0.44 | 0.39 | 200 | application/javascript | 23076 | 9a8461483a36a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.27 | 0.37 | 1.23 | 200 | application/javascript | 23076 | 9a84ae1aea15e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 243.23 | 3.00 | 0.23 | 200 | application/javascript | 23076 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 255.06 | 1.37 | 0.40 | 200 | application/javascript | 23076 | 9a841d88ee28e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.44 | 1.76 | 1.02 | 200 | application/javascript | 23076 | 9a84a846fb69b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 108.25 | 1.12 | 0.23 | 200 | application/javascript | 23076 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 19.99 | 1.87 | 0.22 | 200 | application/javascript | 23076 | 9a845e8aea228c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 12.93 | 3.09 | 0.36 | 200 | application/javascript | 23076 | 9a84aa813d20af04-IAD |

### /_next/static/chunks/28743-4a3deeebaf794acf.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 124.62 | 86.05 | 0.22 | 200 | application/javascript | 9506 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 19.75 | 0.56 | 0.50 | 200 | application/javascript | 9506 | 9a84227a58e5dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 11.52 | 0.38 | 0.34 | 200 | application/javascript | 9506 | 9a84a8f028e8e866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 56.93 | 0.39 | 0.96 | 200 | application/javascript | 9506 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 36.95 | 0.37 | 0.50 | 200 | application/javascript | 9506 | 9a8450ff2e3c6412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.35 | 0.49 | 0.23 | 200 | application/javascript | 9506 | 9a84a99fedcd88ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 197.93 | 0.35 | 0.26 | 200 | application/javascript | 9506 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 6.76 | 0.39 | 0.24 | 200 | application/javascript | 9506 | 9a845fda6d98cb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.15 | 0.56 | 0.92 | 200 | application/javascript | 9506 | 9a84aca74f6b33fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 208.19 | 0.87 | 0.26 | 200 | application/javascript | 9506 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 210.94 | 0.40 | 0.30 | 200 | application/javascript | 9506 | 9a8463706f942788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.19 | 0.34 | 0.23 | 200 | application/javascript | 9506 | 9a84afa30ddebc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 305.45 | 0.35 | 0.21 | 200 | application/javascript | 9506 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 299.82 | 0.42 | 0.33 | 200 | application/javascript | 9506 | 9a8461482a32a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.23 | 0.36 | 1.79 | 200 | application/javascript | 9506 | 9a84ae1aea12e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 249.48 | 0.45 | 0.26 | 200 | application/javascript | 9506 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 255.15 | 0.35 | 0.36 | 200 | application/javascript | 9506 | 9a841d876b01e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.12 | 0.45 | 1.21 | 200 | application/javascript | 9506 | 9a84a846fb63b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 104.20 | 1.04 | 0.35 | 200 | application/javascript | 9506 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 16.08 | 2.73 | 1.21 | 200 | application/javascript | 9506 | 9a845e8ad9c98c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 13.51 | 0.36 | 0.76 | 200 | application/javascript | 9506 | 9a84aa813d13af04-IAD |

### /_next/static/chunks/38874-526f584e6aadcd4b.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 6.50 | 0.35 | 0.18 | 200 | application/javascript | 8565 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 9.19 | 0.44 | 0.40 | 200 | application/javascript | 8565 | 9a84227a48d0dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.24 | 1.82 | 0.17 | 200 | application/javascript | 8565 | 9a84a8f018c7e866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 36.76 | 0.44 | 0.26 | 200 | application/javascript | 8565 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 30.89 | 0.45 | 0.26 | 200 | application/javascript | 8565 | 9a8450feee256412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.73 | 0.46 | 1.70 | 200 | application/javascript | 8565 | 9a84a99fedc488ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 332.85 | 6.73 | 0.35 | 200 | application/javascript | 8565 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 180.59 | 0.33 | 2.47 | 200 | application/javascript | 8565 | 9a845fda4d59cb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.14 | 0.33 | 1.47 | 200 | application/javascript | 8565 | 9a84aca73f3933fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 206.12 | 0.31 | 0.28 | 200 | application/javascript | 8565 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 209.18 | 5.67 | 1.66 | 200 | application/javascript | 8565 | 9a8463706f8f2788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.79 | 0.39 | 0.16 | 200 | application/javascript | 8565 | 9a84afa2fdcabc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 301.50 | 1.25 | 0.24 | 200 | application/javascript | 8565 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 300.67 | 0.48 | 0.19 | 200 | application/javascript | 8565 | 9a8461481a25a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 12.32 | 0.98 | 0.90 | 200 | application/javascript | 8565 | 9a84ae1ac9d7e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 242.59 | 0.34 | 0.22 | 200 | application/javascript | 8565 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 253.65 | 0.49 | 1.43 | 200 | application/javascript | 8565 | 9a841d876afae382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.13 | 0.35 | 0.71 | 200 | application/javascript | 8565 | 9a84a846eb58b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 102.17 | 0.36 | 0.23 | 200 | application/javascript | 8565 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 23.09 | 0.55 | 2.93 | 200 | application/javascript | 8565 | 9a845e8ad9c38c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 12.60 | 0.92 | 2.90 | 200 | application/javascript | 8565 | 9a84aa813d0faf04-IAD |

### /_next/static/chunks/40867-24b106b5648edbf1.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 8.03 | 1.16 | 0.44 | 200 | application/javascript | 31882 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 7.96 | 0.42 | 1.12 | 200 | application/javascript | 31882 | 9a84227a3886dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.52 | 0.43 | 1.28 | 200 | application/javascript | 31882 | 9a84a8eff867e866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 111.47 | 0.58 | 0.71 | 200 | application/javascript | 31882 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 43.27 | 0.51 | 0.38 | 200 | application/javascript | 31882 | 9a8450fe7dbc6412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.90 | 0.51 | 0.36 | 200 | application/javascript | 31882 | 9a84a99fbd5b88ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 445.58 | 104.52 | 0.58 | 200 | application/javascript | 31882 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 180.23 | 1.51 | 1.55 | 200 | application/javascript | 31882 | 9a845fd7f936cb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 12.67 | 1.87 | 1.65 | 200 | application/javascript | 31882 | 9a84aca71ed633fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 220.44 | 3.36 | 0.58 | 200 | application/javascript | 31882 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 213.81 | 0.52 | 0.23 | 200 | application/javascript | 31882 | 9a84636dbadd2788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.33 | 1.25 | 1.46 | 200 | application/javascript | 31882 | 9a84afa2dd84bc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 339.23 | 7.53 | 0.56 | 200 | application/javascript | 31882 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 310.96 | 0.86 | 0.87 | 200 | application/javascript | 31882 | 9a8461443877a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.59 | 1.00 | 3.28 | 200 | application/javascript | 31882 | 9a84ae1ab9b0e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 286.68 | 8.78 | 0.29 | 200 | application/javascript | 31882 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 245.17 | 0.50 | 0.33 | 200 | application/javascript | 31882 | 9a841d845c18e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.71 | 0.40 | 2.21 | 200 | application/javascript | 31882 | 9a84a846cb3cb200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 121.45 | 5.04 | 0.30 | 200 | application/javascript | 31882 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 11.15 | 0.94 | 0.20 | 200 | application/javascript | 31882 | 9a845e8a98f78c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.33 | 0.51 | 0.20 | 200 | application/javascript | 31882 | 9a84aa810c5aaf04-IAD |

### /_next/static/chunks/43423-49ad8b8120df9a57.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 15.45 | 0.34 | 0.50 | 200 | application/javascript | 25366 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 8.47 | 0.47 | 0.73 | 200 | application/javascript | 25366 | 9a84227a38a0dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 13.35 | 0.40 | 0.82 | 200 | application/javascript | 25366 | 9a84a8f00870e866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 18.92 | 4.12 | 0.47 | 200 | application/javascript | 25366 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 32.75 | 0.81 | 0.34 | 200 | application/javascript | 25366 | 9a8450feadfb6412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.96 | 0.49 | 1.97 | 200 | application/javascript | 25366 | 9a84a99fdd8088ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 157.75 | 5.07 | 0.52 | 200 | application/javascript | 25366 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 185.62 | 0.85 | 0.47 | 200 | application/javascript | 25366 | 9a845fd91b45cb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 11.19 | 0.71 | 0.56 | 200 | application/javascript | 25366 | 9a84aca71edc33fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 221.31 | 7.80 | 0.22 | 200 | application/javascript | 25366 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 211.40 | 0.46 | 1.23 | 200 | application/javascript | 25366 | 9a84636f0d4c2788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.69 | 0.48 | 1.00 | 200 | application/javascript | 25366 | 9a84afa2ed9bbc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 303.88 | 5.50 | 0.24 | 200 | application/javascript | 25366 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 313.35 | 0.48 | 3.80 | 200 | application/javascript | 25366 | 9a846146393aa959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.63 | 0.37 | 0.29 | 200 | application/javascript | 25366 | 9a84ae1ab9b3e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 263.33 | 3.10 | 0.23 | 200 | application/javascript | 25366 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 684.84 | 1.91 | 0.28 | 200 | application/javascript | 25366 | 9a841d85cf50e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.96 | 0.47 | 0.74 | 200 | application/javascript | 25366 | 9a84a846db44b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 110.97 | 3.16 | 0.21 | 200 | application/javascript | 25366 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 16.63 | 0.57 | 1.11 | 200 | application/javascript | 25366 | 9a845e8aa9418c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.74 | 1.35 | 0.18 | 200 | application/javascript | 25366 | 9a84aa811c84af04-IAD |

### /_next/static/chunks/65264-dc11e68888cdad2a.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 9.40 | 10.50 | 0.54 | 200 | application/javascript | 172276 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 8.96 | 2.14 | 0.84 | 200 | application/javascript | 172276 | 9a84227a286edc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.59 | 7.97 | 0.69 | 200 | application/javascript | 172276 | 9a84a8efe846e866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 18.81 | 8.87 | 0.56 | 200 | application/javascript | 172276 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 32.30 | 1.87 | 0.54 | 200 | application/javascript | 172276 | 9a8450fe6db46412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.69 | 2.72 | 0.74 | 200 | application/javascript | 172276 | 9a84a99fbd5788ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 163.07 | 54.12 | 0.66 | 200 | application/javascript | 172276 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 505.16 | 172.23 | 1.57 | 200 | application/javascript | 172276 | 9a845fd7f933cb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.60 | 2.11 | 0.54 | 200 | application/javascript | 172276 | 9a84aca70e8533fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 226.90 | 65.41 | 0.66 | 200 | application/javascript | 172276 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 211.56 | 6.21 | 0.50 | 200 | application/javascript | 172276 | 9a84636daacd2788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.23 | 2.37 | 0.60 | 200 | application/javascript | 172276 | 9a84afa2cd75bc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 401.35 | 62.02 | 0.62 | 200 | application/javascript | 172276 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 314.00 | 3.38 | 0.92 | 200 | application/javascript | 172276 | 9a8461443874a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.12 | 3.22 | 0.94 | 200 | application/javascript | 172276 | 9a84ae1aa9a3e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 322.65 | 49.29 | 0.46 | 200 | application/javascript | 172276 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 247.76 | 3.76 | 0.51 | 200 | application/javascript | 172276 | 9a841d844bfbe382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.33 | 2.16 | 0.39 | 200 | application/javascript | 172276 | 9a84a846cb30b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 117.48 | 35.85 | 0.50 | 200 | application/javascript | 172276 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 13.54 | 2.14 | 0.19 | 200 | application/javascript | 172276 | 9a845e8a98e28c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.63 | 1.63 | 0.51 | 200 | application/javascript | 172276 | 9a84aa810c44af04-IAD |

### /_next/static/chunks/72283-44c31ff2dbd0a071.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 179.65 | 1.56 | 0.78 | 200 | application/javascript | 33960 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 7.29 | 0.85 | 1.17 | 200 | application/javascript | 33960 | 9a84227a48c7dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.57 | 1.29 | 0.21 | 200 | application/javascript | 33960 | 9a84a8f018b4e866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 33.53 | 0.87 | 1.13 | 200 | application/javascript | 33960 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 33.28 | 1.67 | 1.28 | 200 | application/javascript | 33960 | 9a8450feee236412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.46 | 0.56 | 0.29 | 200 | application/javascript | 33960 | 9a84a99fddac88ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 161.38 | 8.24 | 0.24 | 200 | application/javascript | 33960 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 171.81 | 2.00 | 0.22 | 200 | application/javascript | 33960 | 9a845fda2d16cb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.46 | 1.56 | 4.08 | 200 | application/javascript | 33960 | 9a84aca73f3533fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 224.81 | 6.46 | 0.22 | 200 | application/javascript | 33960 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 208.87 | 0.54 | 0.25 | 200 | application/javascript | 33960 | 9a84636f4db12788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.76 | 0.81 | 0.41 | 200 | application/javascript | 33960 | 9a84afa2fdc1bc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 304.54 | 6.85 | 0.30 | 200 | application/javascript | 33960 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 299.83 | 0.53 | 0.55 | 200 | application/javascript | 33960 | 9a8461463940a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.86 | 1.10 | 1.08 | 200 | application/javascript | 33960 | 9a84ae1ac9d3e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 270.33 | 4.81 | 0.26 | 200 | application/javascript | 33960 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 237.42 | 0.48 | 0.22 | 200 | application/javascript | 33960 | 9a841d85ffd3e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.62 | 1.87 | 0.18 | 200 | application/javascript | 33960 | 9a84a846db52b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 107.83 | 2.06 | 0.32 | 200 | application/javascript | 33960 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 13.80 | 0.70 | 0.24 | 200 | application/javascript | 33960 | 9a845e8ab9818c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.99 | 1.44 | 0.62 | 200 | application/javascript | 33960 | 9a84aa812cc6af04-IAD |

### /_next/static/chunks/75245-4381628e6d93ed7c.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 59.90 | 2.67 | 0.20 | 200 | application/javascript | 83664 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 9.85 | 1.68 | 0.38 | 200 | application/javascript | 83664 | 9a84227a48d1dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 12.13 | 2.08 | 0.39 | 200 | application/javascript | 83664 | 9a84a8f028e5e866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 176.72 | 8.28 | 0.27 | 200 | application/javascript | 83664 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 33.39 | 1.78 | 0.58 | 200 | application/javascript | 83664 | 9a8450ff2e3b6412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.82 | 1.45 | 0.20 | 200 | application/javascript | 83664 | 9a84a99fedc688ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 167.97 | 14.57 | 0.61 | 200 | application/javascript | 83664 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 176.68 | 1.65 | 0.76 | 200 | application/javascript | 83664 | 9a845fda4d5acb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.64 | 3.14 | 2.91 | 200 | application/javascript | 83664 | 9a84aca74f6833fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 207.78 | 13.74 | 0.25 | 200 | application/javascript | 83664 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 208.25 | 41.58 | 1.61 | 200 | application/javascript | 83664 | 9a8463706f922788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.48 | 1.58 | 0.89 | 200 | application/javascript | 83664 | 9a84afa30ddcbc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 301.93 | 16.98 | 0.22 | 200 | application/javascript | 83664 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 319.42 | 0.86 | 0.21 | 200 | application/javascript | 83664 | 9a8461482a26a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.08 | 1.06 | 4.64 | 200 | application/javascript | 83664 | 9a84ae1aea11e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 248.00 | 13.13 | 0.27 | 200 | application/javascript | 83664 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 238.34 | 1.89 | 1.33 | 200 | application/javascript | 83664 | 9a841d876afee382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.40 | 1.53 | 0.50 | 200 | application/javascript | 83664 | 9a84a846eb5ab200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 104.75 | 6.92 | 0.44 | 200 | application/javascript | 83664 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 16.74 | 2.16 | 1.25 | 200 | application/javascript | 83664 | 9a845e8ad9c88c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.95 | 6.33 | 1.57 | 200 | application/javascript | 83664 | 9a84aa813d10af04-IAD |

### /_next/static/chunks/87524-df2a52a55c85cce2.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 9.43 | 1.13 | 0.27 | 200 | application/javascript | 48368 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 9.77 | 0.87 | 0.38 | 200 | application/javascript | 48368 | 9a84227a38b4dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.00 | 1.96 | 0.18 | 200 | application/javascript | 48368 | 9a84a8f018afe866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 33.37 | 4.22 | 0.36 | 200 | application/javascript | 48368 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 32.82 | 2.30 | 1.39 | 200 | application/javascript | 48368 | 9a8450feee226412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.18 | 1.04 | 0.40 | 200 | application/javascript | 48368 | 9a84a99fddab88ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 159.91 | 8.94 | 0.27 | 200 | application/javascript | 48368 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 185.40 | 0.70 | 0.18 | 200 | application/javascript | 48368 | 9a845fd93b9fcb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.26 | 3.61 | 4.15 | 200 | application/javascript | 48368 | 9a84aca73f3433fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 223.22 | 8.91 | 0.32 | 200 | application/javascript | 48368 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 208.31 | 4.41 | 0.20 | 200 | application/javascript | 48368 | 9a84636f1d622788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.85 | 1.00 | 0.31 | 200 | application/javascript | 48368 | 9a84afa2edb2bc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 321.21 | 15.74 | 0.32 | 200 | application/javascript | 48368 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 300.83 | 0.67 | 0.31 | 200 | application/javascript | 48368 | 9a846146393ea959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.98 | 2.65 | 1.18 | 200 | application/javascript | 48368 | 9a84ae1ac9d1e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 264.05 | 7.41 | 0.23 | 200 | application/javascript | 48368 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 240.10 | 0.72 | 0.17 | 200 | application/javascript | 48368 | 9a841d85df8de382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 5.95 | 2.60 | 1.27 | 200 | application/javascript | 48368 | 9a84a846db51b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 107.59 | 3.99 | 0.31 | 200 | application/javascript | 48368 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 15.34 | 1.18 | 0.27 | 200 | application/javascript | 48368 | 9a845e8ab96a8c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 12.46 | 1.93 | 0.68 | 200 | application/javascript | 48368 | 9a84aa812cc0af04-IAD |

### /_next/static/chunks/ad6b4c6d-bd23cbb78334428b.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 91.03 | 111.13 | 0.65 | 200 | application/javascript | 173026 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 7.60 | 3.91 | 0.25 | 200 | application/javascript | 173026 | 9a84227a1859dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.87 | 2.48 | 0.26 | 200 | application/javascript | 173026 | 9a84a8efe830e866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 21.32 | 40.39 | 0.65 | 200 | application/javascript | 173026 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 60.59 | 18.60 | 0.55 | 200 | application/javascript | 173026 | 9a8450fe6db36412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.89 | 2.35 | 0.38 | 200 | application/javascript | 173026 | 9a84a99fbd3c88ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 164.84 | 68.13 | 0.72 | 200 | application/javascript | 173026 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 185.94 | 4.17 | 1.46 | 200 | application/javascript | 173026 | 9a845fd7f932cb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.33 | 3.43 | 0.58 | 200 | application/javascript | 173026 | 9a84aca6fe7433fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 224.00 | 97.33 | 0.70 | 200 | application/javascript | 173026 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 210.78 | 14.40 | 0.52 | 200 | application/javascript | 173026 | 9a84636daacc2788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.35 | 4.02 | 0.37 | 200 | application/javascript | 173026 | 9a84afa2cd63bc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 303.39 | 97.74 | 0.69 | 200 | application/javascript | 173026 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 312.19 | 4.97 | 0.86 | 200 | application/javascript | 173026 | 9a8461443872a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.37 | 5.06 | 0.33 | 200 | application/javascript | 173026 | 9a84ae1aa99fe7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 250.17 | 60.67 | 0.50 | 200 | application/javascript | 173026 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 241.41 | 2.23 | 0.54 | 200 | application/javascript | 173026 | 9a841d844bfae382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.25 | 3.27 | 0.28 | 200 | application/javascript | 173026 | 9a84a846bb26b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 105.50 | 34.69 | 0.54 | 200 | application/javascript | 173026 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 14.49 | 1.87 | 0.34 | 200 | application/javascript | 173026 | 9a845e8a88bf8c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 13.07 | 1.79 | 0.30 | 200 | application/javascript | 173026 | 9a84aa80fc31af04-IAD |

### /_next/static/chunks/app/%5Blocale%5D/(app)/layout-b4d9c5a0442100bf.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 8.33 | 0.47 | 0.43 | 200 | application/javascript | 20176 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 7.26 | 0.45 | 0.93 | 200 | application/javascript | 20176 | 9a84227a3888dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.63 | 0.53 | 1.38 | 200 | application/javascript | 20176 | 9a84a8eff868e866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 59.37 | 5.43 | 0.33 | 200 | application/javascript | 20176 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 43.68 | 0.52 | 0.32 | 200 | application/javascript | 20176 | 9a8450fe9de56412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.44 | 2.35 | 1.50 | 200 | application/javascript | 20176 | 9a84a99fcd7088ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 158.68 | 4.23 | 0.56 | 200 | application/javascript | 20176 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 169.35 | 0.51 | 0.23 | 200 | application/javascript | 20176 | 9a845fd7f939cb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 11.34 | 1.02 | 1.23 | 200 | application/javascript | 20176 | 9a84aca71ed933fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 275.22 | 7.79 | 0.31 | 200 | application/javascript | 20176 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 214.04 | 0.43 | 0.30 | 200 | application/javascript | 20176 | 9a84636dfb432788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.13 | 0.45 | 1.89 | 200 | application/javascript | 20176 | 9a84afa2dd91bc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 307.49 | 3.81 | 0.53 | 200 | application/javascript | 20176 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 320.54 | 0.78 | 0.84 | 200 | application/javascript | 20176 | 9a8461443878a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.74 | 0.39 | 2.56 | 200 | application/javascript | 20176 | 9a84ae1ab9b1e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 295.10 | 2.97 | 0.28 | 200 | application/javascript | 20176 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 255.66 | 1.11 | 0.33 | 200 | application/javascript | 20176 | 9a841d845c27e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 5.92 | 0.51 | 2.32 | 200 | application/javascript | 20176 | 9a84a846cb3eb200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 114.49 | 1.50 | 0.33 | 200 | application/javascript | 20176 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 12.64 | 2.69 | 1.25 | 200 | application/javascript | 20176 | 9a845e8aa9148c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.94 | 2.47 | 1.12 | 200 | application/javascript | 20176 | 9a84aa810c79af04-IAD |

### /_next/static/chunks/app/%5Blocale%5D/(auth)/login/page-db91e715f9db634b.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 84.82 | 0.46 | 0.43 | 200 | application/javascript | 6428 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 9.12 | 0.70 | 1.21 | 200 | application/javascript | 6428 | 9a84227a58f8dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 11.51 | 0.36 | 0.38 | 200 | application/javascript | 6428 | 9a84a8f028fce866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 29.37 | 0.66 | 0.26 | 200 | application/javascript | 6428 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 32.71 | 0.64 | 0.37 | 200 | application/javascript | 6428 | 9a8450ff3e4e6412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.66 | 0.69 | 1.82 | 200 | application/javascript | 6428 | 9a84a99ffdf488ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 160.36 | 0.33 | 0.20 | 200 | application/javascript | 6428 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 170.32 | 0.35 | 0.47 | 200 | application/javascript | 6428 | 9a845fdb6f31cb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.52 | 0.38 | 0.49 | 200 | application/javascript | 6428 | 9a84aca74f7133fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 206.94 | 0.37 | 0.31 | 200 | application/javascript | 6428 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 210.67 | 0.37 | 0.27 | 200 | application/javascript | 6428 | 9a8463719a112788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.49 | 0.39 | 0.17 | 200 | application/javascript | 6428 | 9a84afa30de5bc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 303.87 | 0.36 | 0.26 | 200 | application/javascript | 6428 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 300.59 | 0.51 | 0.26 | 200 | application/javascript | 6428 | 9a846149fadba959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.78 | 0.26 | 0.41 | 200 | application/javascript | 6428 | 9a84ae1aea16e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 291.83 | 1.07 | 0.34 | 200 | application/javascript | 6428 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 238.73 | 0.46 | 0.33 | 200 | application/javascript | 6428 | 9a841d88fe44e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.10 | 1.15 | 3.51 | 200 | application/javascript | 6428 | 9a84a846fb6cb200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 102.14 | 0.44 | 0.98 | 200 | application/javascript | 6428 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 15.91 | 0.32 | 1.28 | 200 | application/javascript | 6428 | 9a845e8afa4b8c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 12.39 | 1.82 | 1.14 | 200 | application/javascript | 6428 | 9a84aa815d64af04-IAD |

### /_next/static/chunks/app/%5Blocale%5D/error-c58756f7ba7b9f2b.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 125.50 | 4.15 | 0.37 | 200 | application/javascript | 10308 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 10.06 | 0.50 | 0.47 | 200 | application/javascript | 10308 | 9a84227a58fddc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 11.31 | 0.59 | 1.24 | 200 | application/javascript | 10308 | 9a84a8f0392ee866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 123.46 | 2.74 | 0.35 | 200 | application/javascript | 10308 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 33.34 | 0.42 | 0.69 | 200 | application/javascript | 10308 | 9a8450ff5e656412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.67 | 0.62 | 0.86 | 200 | application/javascript | 10308 | 9a84a99ffdf588ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 166.66 | 0.37 | 0.23 | 200 | application/javascript | 10308 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 174.90 | 0.42 | 0.34 | 200 | application/javascript | 10308 | 9a845fdb6f32cb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 11.18 | 0.67 | 1.36 | 200 | application/javascript | 10308 | 9a84aca76f9733fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 206.75 | 0.31 | 0.20 | 200 | application/javascript | 10308 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 212.30 | 0.42 | 0.22 | 200 | application/javascript | 10308 | 9a846371ba322788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.26 | 0.35 | 0.33 | 200 | application/javascript | 10308 | 9a84afa31df5bc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 302.56 | 0.33 | 0.19 | 200 | application/javascript | 10308 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 305.61 | 0.53 | 0.25 | 200 | application/javascript | 10308 | 9a84614a0ae7a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.44 | 0.36 | 0.68 | 200 | application/javascript | 10308 | 9a84ae1afa28e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 243.44 | 1.09 | 0.25 | 200 | application/javascript | 10308 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 241.28 | 2.01 | 0.24 | 200 | application/javascript | 10308 | 9a841d88fe5ce382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.65 | 0.64 | 3.44 | 200 | application/javascript | 10308 | 9a84a846fb6db200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 103.74 | 0.47 | 0.38 | 200 | application/javascript | 10308 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 16.32 | 0.32 | 0.30 | 200 | application/javascript | 10308 | 9a845e8afa4e8c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 13.16 | 0.73 | 1.02 | 200 | application/javascript | 10308 | 9a84aa815d6baf04-IAD |

### /_next/static/chunks/app/%5Blocale%5D/layout-df215d4a79c4add9.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 54.39 | 0.41 | 0.27 | 200 | application/javascript | 10734 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 10.83 | 0.32 | 0.45 | 200 | application/javascript | 10734 | 9a84227a48cfdc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.01 | 0.36 | 0.17 | 200 | application/javascript | 10734 | 9a84a8f018bae866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 29.07 | 4.04 | 0.25 | 200 | application/javascript | 10734 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 44.67 | 0.36 | 0.81 | 200 | application/javascript | 10734 | 9a8450feee246412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.51 | 0.50 | 1.97 | 200 | application/javascript | 10734 | 9a84a99fedc188ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 158.01 | 0.88 | 0.22 | 200 | application/javascript | 10734 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 190.23 | 0.40 | 0.25 | 200 | application/javascript | 10734 | 9a845fda3d2acb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.91 | 0.36 | 1.79 | 200 | application/javascript | 10734 | 9a84aca73f3733fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 206.89 | 0.42 | 0.31 | 200 | application/javascript | 10734 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 209.46 | 0.47 | 0.26 | 200 | application/javascript | 10734 | 9a8463704f6c2788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.30 | 0.53 | 0.28 | 200 | application/javascript | 10734 | 9a84afa2fdc2bc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 310.42 | 1.15 | 0.28 | 200 | application/javascript | 10734 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 342.79 | 0.37 | 0.25 | 200 | application/javascript | 10734 | 9a8461480a1fa959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.67 | 1.03 | 0.99 | 200 | application/javascript | 10734 | 9a84ae1ac9d5e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 243.02 | 0.51 | 0.30 | 200 | application/javascript | 10734 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 253.25 | 0.42 | 0.27 | 200 | application/javascript | 10734 | 9a841d875ae5e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.91 | 0.39 | 1.88 | 200 | application/javascript | 10734 | 9a84a846eb56b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 102.83 | 0.51 | 1.57 | 200 | application/javascript | 10734 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 11.97 | 0.47 | 7.31 | 200 | application/javascript | 10734 | 9a845e8ad9c08c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.62 | 1.04 | 0.65 | 200 | application/javascript | 10734 | 9a84aa812cc7af04-IAD |

### /_next/static/chunks/app/%5Blocale%5D/loading-98f017f93adc0ad2.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 14.22 | 0.47 | 0.48 | 200 | application/javascript | 4659 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 8.96 | 0.23 | 0.20 | 200 | application/javascript | 4659 | 9a84227a38a4dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.31 | 0.31 | 0.22 | 200 | application/javascript | 4659 | 9a84a8f00872e866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 18.42 | 3.86 | 0.54 | 200 | application/javascript | 4659 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 32.64 | 0.48 | 0.25 | 200 | application/javascript | 4659 | 9a8450febe066412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.88 | 0.42 | 1.16 | 200 | application/javascript | 4659 | 9a84a99fdd8288ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 175.74 | 0.31 | 0.29 | 200 | application/javascript | 4659 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 175.34 | 0.36 | 0.22 | 200 | application/javascript | 4659 | 9a845fd91b4acb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 11.84 | 1.34 | 0.61 | 200 | application/javascript | 4659 | 9a84aca72ef033fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 221.53 | 0.31 | 0.21 | 200 | application/javascript | 4659 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 212.01 | 0.33 | 0.22 | 200 | application/javascript | 4659 | 9a84636f0d4e2788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 12.94 | 0.30 | 0.28 | 200 | application/javascript | 4659 | 9a84afa2ed9cbc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 302.38 | 0.29 | 0.25 | 200 | application/javascript | 4659 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 316.34 | 0.31 | 2.35 | 200 | application/javascript | 4659 | 9a846146393ba959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.21 | 0.30 | 0.24 | 200 | application/javascript | 4659 | 9a84ae1ab9b4e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 241.94 | 0.33 | 0.26 | 200 | application/javascript | 4659 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 249.15 | 0.34 | 0.19 | 200 | application/javascript | 4659 | 9a841d85df7de382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.07 | 0.39 | 0.23 | 200 | application/javascript | 4659 | 9a84a846db45b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 102.60 | 0.40 | 0.29 | 200 | application/javascript | 4659 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 15.71 | 0.46 | 0.36 | 200 | application/javascript | 4659 | 9a845e8aa9428c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 17.83 | 0.40 | 0.18 | 200 | application/javascript | 4659 | 9a84aa811c8aaf04-IAD |

### /_next/static/chunks/main-app-3267ec133fe45348.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 9.64 | 0.24 | 0.48 | 200 | application/javascript | 572 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 9.43 | 0.29 | 0.17 | 200 | application/javascript | 572 | 9a84227a2871dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.32 | 7.12 | 0.20 | 200 | application/javascript | 572 | 9a84a8eff84ae866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 17.17 | 0.91 | 0.59 | 200 | application/javascript | 572 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 35.19 | 0.55 | 0.85 | 200 | application/javascript | 572 | 9a8450fe6dba6412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.63 | 0.30 | 0.42 | 200 | application/javascript | 572 | 9a84a99fbd5988ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 158.04 | 0.29 | 0.63 | 200 | application/javascript | 572 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 179.55 | 0.32 | 1.57 | 200 | application/javascript | 572 | 9a845fd7f934cb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 12.34 | 1.08 | 1.58 | 200 | application/javascript | 572 | 9a84aca70e8c33fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 206.84 | 0.44 | 0.63 | 200 | application/javascript | 572 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 212.57 | 0.34 | 0.28 | 200 | application/javascript | 572 | 9a84636dbad62788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.87 | 0.25 | 0.19 | 200 | application/javascript | 572 | 9a84afa2cd79bc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 301.13 | 0.35 | 0.59 | 200 | application/javascript | 572 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 313.42 | 0.28 | 0.90 | 200 | application/javascript | 572 | 9a8461443876a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.14 | 0.39 | 0.23 | 200 | application/javascript | 572 | 9a84ae1aa9a4e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 242.72 | 0.38 | 0.44 | 200 | application/javascript | 572 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 241.58 | 3.14 | 0.34 | 200 | application/javascript | 572 | 9a841d844c15e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.08 | 0.29 | 0.41 | 200 | application/javascript | 572 | 9a84a846cb32b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 103.97 | 1.36 | 0.47 | 200 | application/javascript | 572 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 12.49 | 0.29 | 0.27 | 200 | application/javascript | 572 | 9a845e8a98f48c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 11.42 | 0.32 | 0.21 | 200 | application/javascript | 572 | 9a84aa810c4baf04-IAD |

### /_next/static/chunks/webpack-b80cd65c35b59642.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 88.55 | 0.82 | 4.98 | 200 | application/javascript | 43159 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 8.49 | 0.76 | 4.97 | 200 | application/javascript | 43159 | 9a84227a1856dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.31 | 1.63 | 5.31 | 200 | application/javascript | 43159 | 9a84a8efe823e866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 176.44 | 2.53 | 3.39 | 200 | application/javascript | 43159 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 36.87 | 1.24 | 0.57 | 200 | application/javascript | 43159 | 9a8450fe2d886412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.88 | 0.99 | 0.65 | 200 | application/javascript | 43159 | 9a84a99fad2588ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 386.16 | 74.17 | 0.17 | 200 | application/javascript | 43159 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 177.47 | 3.40 | 0.20 | 200 | application/javascript | 43159 | 9a845fd6def2cb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.17 | 2.54 | 4.17 | 200 | application/javascript | 43159 | 9a84aca6fe7233fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 578.73 | 41.02 | 2.60 | 200 | application/javascript | 43159 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 211.06 | 36.93 | 0.33 | 200 | application/javascript | 43159 | 9a84636c6ff12788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.65 | 1.31 | 4.54 | 200 | application/javascript | 43159 | 9a84afa2cd5fbc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 629.30 | 98.06 | 0.23 | 200 | application/javascript | 43159 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 302.97 | 0.65 | 2.84 | 200 | application/javascript | 43159 | 9a8461424fd6a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.67 | 1.87 | 4.48 | 200 | application/javascript | 43159 | 9a84ae1aa99ce7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 704.28 | 38.89 | 1.66 | 200 | application/javascript | 43159 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 249.14 | 1.12 | 0.86 | 200 | application/javascript | 43159 | 9a841d82c824e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.40 | 1.55 | 4.69 | 200 | application/javascript | 43159 | 9a84a846bb22b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 333.64 | 26.30 | 2.71 | 200 | application/javascript | 43159 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 12.64 | 0.98 | 1.65 | 200 | application/javascript | 43159 | 9a845e8a88a18c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 15.65 | 0.69 | 3.59 | 200 | application/javascript | 43159 | 9a84aa80ec15af04-IAD |

### /_next/static/css/abf98b2abcdbd573.css (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 7.02 | 3.49 | 0.49 | 200 | text/css | 123936 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.08 | 0.90 | 0.70 | 200 | text/css | 123936 | 9a84227d0f70dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.08 | 0.96 | 0.50 | 200 | text/css | 123936 | 9a84a8f1dc95e866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 44.22 | 4.01 | 1.01 | 200 | text/css | 123936 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.11 | 1.11 | 0.72 | 200 | text/css | 123936 | 9a8451118c796412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.09 | 1.15 | 1.28 | 200 | text/css | 123936 | 9a84a9a2ab4b88ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 174.48 | 9.01 | 0.45 | 200 | text/css | 123936 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.11 | 0.99 | 0.62 | 200 | text/css | 123936 | 9a845fe08ffecb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.10 | 1.56 | 0.52 | 200 | text/css | 123936 | 9a84acac494d33fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 208.39 | 12.65 | 0.50 | 200 | text/css | 123936 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.11 | 1.06 | 0.71 | 200 | text/css | 123936 | 9a84636c5fd52788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.11 | 4.18 | 1.40 | 200 | text/css | 123936 | 9a84afa2ad34bc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 299.45 | 16.91 | 0.50 | 200 | text/css | 123936 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.11 | 1.50 | 0.68 | 200 | text/css | 123936 | 9a84614ebc88a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.11 | 1.62 | 0.71 | 200 | text/css | 123936 | 9a84ae201f2ce7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 244.44 | 15.89 | 0.53 | 200 | text/css | 123936 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.09 | 1.64 | 0.67 | 200 | text/css | 123936 | 9a841d8d9893e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.09 | 1.69 | 0.68 | 200 | text/css | 123936 | 9a84a84adff3b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 103.41 | 8.57 | 0.63 | 200 | text/css | 123936 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.09 | 1.38 | 1.01 | 200 | text/css | 123936 | 9a845e8a68608c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.11 | 1.22 | 4.01 | 200 | text/css | 123936 | 9a84aa80dbd0af04-IAD |

### /_next/static/css/e771c44a50dae3b6.css (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 6.30 | 0.35 | 0.28 | 200 | text/css | 4004 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.09 | 0.35 | 0.51 | 200 | text/css | 4004 | 9a84227d0f71dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.07 | 0.29 | 0.29 | 200 | text/css | 4004 | 9a84a8f1dc96e866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 40.40 | 3.66 | 0.87 | 200 | text/css | 4004 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.12 | 0.37 | 0.50 | 200 | text/css | 4004 | 9a8451118c7a6412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.10 | 0.75 | 1.06 | 200 | text/css | 4004 | 9a84a9a2ab4e88ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 183.65 | 0.27 | 0.28 | 200 | text/css | 4004 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.11 | 0.38 | 0.40 | 200 | text/css | 4004 | 9a845fe08fffcb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.08 | 0.31 | 0.31 | 200 | text/css | 4004 | 9a84acac494f33fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 206.98 | 0.37 | 0.30 | 200 | text/css | 4004 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.08 | 0.35 | 0.79 | 200 | text/css | 4004 | 9a84636c5fd82788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.08 | 0.40 | 1.30 | 200 | text/css | 4004 | 9a84afa2ad37bc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 297.45 | 0.38 | 0.29 | 200 | text/css | 4004 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.07 | 0.28 | 0.47 | 200 | text/css | 4004 | 9a84614ebc8aa959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.07 | 0.32 | 0.51 | 200 | text/css | 4004 | 9a84ae201f2de7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 242.57 | 0.39 | 0.33 | 200 | text/css | 4004 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.08 | 0.41 | 1.21 | 200 | text/css | 4004 | 9a841d8d9896e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.08 | 0.32 | 0.42 | 200 | text/css | 4004 | 9a84a84adff4b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 100.38 | 3.38 | 0.32 | 200 | text/css | 4004 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.09 | 0.37 | 0.87 | 200 | text/css | 4004 | 9a845e8a68648c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.09 | 0.38 | 3.83 | 200 | text/css | 4004 | 9a84aa80dbd3af04-IAD |

### /_next/static/media/739c2d8941231bb4-s.p.woff2 (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 5.84 | 1.76 | 2.32 | 200 | font/woff2 | 32752 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 4.39 | 0.59 | 1.16 | 200 | font/woff2 | 32752 | 9a84227a1849dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.42 | 0.41 | 1.05 | 200 | font/woff2 | 32752 | 9a84a8efe80ee866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 37.03 | 6.79 | 1.31 | 200 | font/woff2 | 32752 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 39.04 | 1.45 | 1.23 | 200 | font/woff2 | 32752 | 9a8450fe2d846412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.30 | 0.53 | 1.22 | 200 | font/woff2 | 32752 | 9a84a99fad1f88ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 165.40 | 137.71 | 0.72 | 200 | font/woff2 | 32752 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 169.27 | 6.53 | 0.80 | 200 | font/woff2 | 32752 | 9a845fd6deedcb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.46 | 0.48 | 1.05 | 200 | font/woff2 | 32752 | 9a84aca6fe6733fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 362.25 | 153.53 | 1.12 | 200 | font/woff2 | 32752 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 209.68 | 0.41 | 1.03 | 200 | font/woff2 | 32752 | 9a84636c6fed2788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.41 | 0.46 | 1.05 | 200 | font/woff2 | 32752 | 9a84afa2bd4cbc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 741.28 | 116.35 | 0.75 | 200 | font/woff2 | 32752 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 301.73 | 0.84 | 1.12 | 200 | font/woff2 | 32752 | 9a8461424fd4a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 2.69 | 0.44 | 1.22 | 200 | font/woff2 | 32752 | 9a84ae1aa990e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 535.93 | 154.04 | 1.06 | 200 | font/woff2 | 32752 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 255.14 | 0.55 | 1.03 | 200 | font/woff2 | 32752 | 9a841d82b810e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 4.54 | 0.47 | 1.62 | 200 | font/woff2 | 32752 | 9a84a846bb1cb200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 254.21 | 47.86 | 1.23 | 200 | font/woff2 | 32752 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 17.15 | 0.83 | 1.12 | 200 | font/woff2 | 32752 | 9a845e8a788a8c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 12.13 | 0.57 | 4.22 | 200 | font/woff2 | 32752 | 9a84aa80ec07af04-IAD |

### /_next/static/media/authLogo.59ea595a.svg (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 6.38 | 0.38 | 0.30 | 200 | image/svg+xml | 16549 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 9.66 | 0.35 | 0.29 | 200 | image/svg+xml | 16549 | 9a84227a1858dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.29 | 0.51 | 0.23 | 200 | image/svg+xml | 16549 | 9a84a8efe829e866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 19.61 | 0.45 | 0.78 | 200 | image/svg+xml | 16549 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 40.13 | 0.60 | 0.62 | 200 | image/svg+xml | 16549 | 9a8450fe6daf6412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.13 | 0.50 | 0.32 | 200 | image/svg+xml | 16549 | 9a84a99fbd3b88ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 159.82 | 2.08 | 0.28 | 200 | image/svg+xml | 16549 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 202.77 | 1.60 | 1.51 | 200 | image/svg+xml | 16549 | 9a845fd7f931cb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.84 | 1.32 | 0.62 | 200 | image/svg+xml | 16549 | 9a84aca6fe7333fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 206.52 | 7.32 | 0.77 | 200 | image/svg+xml | 16549 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 209.99 | 0.51 | 0.58 | 200 | image/svg+xml | 16549 | 9a84636daac72788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.60 | 0.45 | 0.35 | 200 | image/svg+xml | 16549 | 9a84afa2cd61bc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 302.96 | 4.77 | 0.24 | 200 | image/svg+xml | 16549 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 303.40 | 0.50 | 0.26 | 200 | image/svg+xml | 16549 | 9a846144386fa959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.68 | 0.36 | 0.37 | 200 | image/svg+xml | 16549 | 9a84ae1aa99de7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 242.39 | 7.59 | 0.56 | 200 | image/svg+xml | 16549 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 240.39 | 0.56 | 0.57 | 200 | image/svg+xml | 16549 | 9a841d844bf4e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 6.67 | 0.38 | 0.24 | 200 | image/svg+xml | 16549 | 9a84a846bb25b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 101.20 | 2.52 | 0.62 | 200 | image/svg+xml | 16549 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 13.26 | 0.94 | 0.41 | 200 | image/svg+xml | 16549 | 9a845e8a88bc8c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 11.91 | 0.71 | 0.36 | 200 | image/svg+xml | 16549 | 9a84aa80fc2baf04-IAD |

### /_next/static/media/e4af272ccee01ff0-s.p.woff2 (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 6.71 | 4.05 | 3.91 | 200 | font/woff2 | 48432 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 5.51 | 0.88 | 1.01 | 200 | font/woff2 | 48432 | 9a84227a184adc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.16 | 0.57 | 0.89 | 200 | font/woff2 | 48432 | 9a84a8efe811e866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 18.01 | 18.49 | 1.12 | 200 | font/woff2 | 48432 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 30.80 | 0.95 | 1.04 | 200 | font/woff2 | 48432 | 9a8450fe2d876412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.19 | 2.86 | 1.05 | 200 | font/woff2 | 48432 | 9a84a99fad2488ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 311.90 | 133.30 | 0.63 | 200 | font/woff2 | 48432 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 183.46 | 1.41 | 0.67 | 200 | font/woff2 | 48432 | 9a845fd6deefcb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 5.80 | 2.52 | 1.11 | 200 | font/woff2 | 48432 | 9a84aca6fe6c33fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 216.29 | 246.96 | 1.27 | 200 | font/woff2 | 48432 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 207.87 | 0.63 | 0.85 | 200 | font/woff2 | 48432 | 9a84636c6fee2788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.36 | 0.85 | 1.46 | 200 | font/woff2 | 48432 | 9a84afa2bd51bc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 309.01 | 293.40 | 0.68 | 200 | font/woff2 | 48432 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 300.36 | 2.59 | 1.25 | 200 | font/woff2 | 48432 | 9a8461424fd5a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 3.76 | 1.55 | 1.07 | 200 | font/woff2 | 48432 | 9a84ae1aa991e7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 318.88 | 203.37 | 0.87 | 200 | font/woff2 | 48432 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 245.44 | 5.31 | 0.86 | 200 | font/woff2 | 48432 | 9a841d82b819e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 5.26 | 0.73 | 1.20 | 200 | font/woff2 | 48432 | 9a84a846bb1db200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 104.11 | 138.73 | 1.01 | 200 | font/woff2 | 48432 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 13.20 | 0.67 | 1.10 | 200 | font/woff2 | 48432 | 9a845e8a788c8c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 12.93 | 0.85 | 4.12 | 200 | font/woff2 | 48432 | 9a84aa80ec0baf04-IAD |

### /cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.48787175522499493:1764780765:ffx7zC-Wk64FNnKGFpWIfxjLgt-MkY_KjrUz5sb6OQ0/9a84a8ee2bf0e866 (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 28.89 | 0.33 | 0.24 | 200 | text/plain | 0 | 9a84a8f18bf1e866-FRA |
| London | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| San Francisco | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| São Paulo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Sydney | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Tokyo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |

### /cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.48787175522499493:1764780765:ffx7zC-Wk64FNnKGFpWIfxjLgt-MkY_KjrUz5sb6OQ0/9a84a99d1f5e88ef (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| London | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 15.00 | 0.31 | 0.44 | 200 | text/plain | 0 | 9a84a9a1c98d88ef-LHR |
| San Francisco | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| São Paulo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Sydney | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Tokyo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |

### /cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.48787175522499493:1764780765:ffx7zC-Wk64FNnKGFpWIfxjLgt-MkY_KjrUz5sb6OQ0/9a84aa7d488eaf04 (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| London | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| San Francisco | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| São Paulo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Sydney | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Tokyo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 27.73 | 0.37 | 0.31 | 200 | text/plain | 0 | 9a84aa8c3f03af04-IAD |

### /cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.48787175522499493:1764780765:ffx7zC-Wk64FNnKGFpWIfxjLgt-MkY_KjrUz5sb6OQ0/9a84ac990da533fc (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| London | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| San Francisco | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 14.63 | 0.32 | 0.33 | 200 | text/plain | 0 | 9a84acaa6d3f33fc-SJC |
| São Paulo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Sydney | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Tokyo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |

### /cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.48787175522499493:1764780765:ffx7zC-Wk64FNnKGFpWIfxjLgt-MkY_KjrUz5sb6OQ0/9a84ae176e7be7ec (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| London | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| San Francisco | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| São Paulo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Sydney | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 11.05 | 0.29 | 0.22 | 200 | text/plain | 0 | 9a84ae1c9ba1e7ec-SYD |
| Tokyo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |

### /cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.48787175522499493:1764780765:ffx7zC-Wk64FNnKGFpWIfxjLgt-MkY_KjrUz5sb6OQ0/9a84af9fcfdcbc64 (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| London | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| San Francisco | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| São Paulo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 25.80 | 0.83 | 0.24 | 200 | text/plain | 0 | 9a84afa4c951bc64-GRU |
| Sydney | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Tokyo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |

### /cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.7589308712729556:1764777276:Dq0c_wZGRrMPY-hSCmoqTpc1FCC57z162N2iJ5FrXxA/9a8450fcfc5c6412 (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| London | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 18.75 | 0.34 | 0.31 | 200 | text/plain | 0 | 9a8451108b9b6412-LHR |
| London | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| San Francisco | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| São Paulo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Sydney | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Tokyo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |

### /cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.7589308712729556:1764777276:Dq0c_wZGRrMPY-hSCmoqTpc1FCC57z162N2iJ5FrXxA/9a845e879fb08c9d (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| London | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| San Francisco | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| São Paulo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Sydney | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Tokyo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 19.92 | 0.28 | 0.26 | 200 | text/plain | 0 | 9a845e8cc80b8c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |

### /cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.7589308712729556:1764777276:Dq0c_wZGRrMPY-hSCmoqTpc1FCC57z162N2iJ5FrXxA/9a845fd4eb3dcb6f (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| London | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| San Francisco | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 13.37 | 0.31 | 0.25 | 200 | text/plain | 0 | 9a845fdc286ccb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| São Paulo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Sydney | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Tokyo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |

### /cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.7589308712729556:1764777276:Dq0c_wZGRrMPY-hSCmoqTpc1FCC57z162N2iJ5FrXxA/9a84613e8e87a959 (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| London | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| San Francisco | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| São Paulo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Sydney | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 13.84 | 0.35 | 0.39 | 200 | text/plain | 0 | 9a84614afb4ca959-SYD |
| Sydney | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Tokyo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |

### /cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.7589308712729556:1764777276:Dq0c_wZGRrMPY-hSCmoqTpc1FCC57z162N2iJ5FrXxA/9a846369db3f2788 (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| London | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| San Francisco | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| São Paulo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 20.84 | 0.30 | 0.26 | 200 | text/plain | 0 | 9a846372bc002788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Sydney | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Tokyo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |

### /cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.7589308712729556:1764777276:Dq0c_wZGRrMPY-hSCmoqTpc1FCC57z162N2iJ5FrXxA/9a84a843eef8b200 (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| London | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| San Francisco | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| São Paulo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Sydney | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Tokyo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 16.26 | 0.36 | 0.27 | 200 | text/plain | 0 | 9a84a848ad5fb200-NRT |
| Washington, DC | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |

### /cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.8728646934432264:1764773104:DtYlidy7pVfTfqpJpqLPuAHLQwgBG9mSsl1bPMKbTUA/9a841d7ff9ace382 (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| London | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| San Francisco | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| São Paulo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Sydney | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Tokyo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 13.07 | 0.31 | 0.32 | 200 | text/plain | 0 | 9a841d89d875e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |

### /cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.8728646934432264:1764773104:DtYlidy7pVfTfqpJpqLPuAHLQwgBG9mSsl1bPMKbTUA/9a8422782bfcdc58 (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 15.87 | 0.31 | 0.32 | 200 | text/plain | 0 | 9a84227bdc30dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| London | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| San Francisco | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| São Paulo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Sydney | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Tokyo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |

### /cdn-cgi/challenge-platform/h/b/scripts/jsd/13c98df4ef2d/main.js (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 17.74 | 0.49 | 0.45 | 200 | application/javascript | 9972 | 9a84227aea36dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.04 | 0.56 | 0.20 | 200 | application/javascript | 9978 | 9a84a8f0da83e866-FRA |
| London | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 14.30 | 0.62 | 0.27 | 200 | application/javascript | 10164 | 9a84510fbaf56412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 11.24 | 0.66 | 0.26 | 200 | application/javascript | 9965 | 9a84a9a0f82288ef-LHR |
| San Francisco | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 6.44 | 0.50 | 0.22 | 200 | application/javascript | 10164 | 9a845fdb7f63cb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 32.76 | 0.43 | 0.19 | 200 | application/javascript | 9974 | 9a84aca96b6233fc-SJC |
| São Paulo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 9.69 | 0.34 | 0.18 | 200 | application/javascript | 9978 | 9a846371ea792788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 12.24 | 0.39 | 0.16 | 200 | application/javascript | 10121 | 9a84afa40f93bc64-GRU |
| Sydney | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 9.50 | 0.49 | 0.24 | 200 | application/javascript | 10093 | 9a84614a3af8a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.37 | 0.39 | 0.19 | 200 | application/javascript | 10006 | 9a84ae1beb03e7ec-SYD |
| Tokyo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 11.70 | 0.46 | 0.21 | 200 | application/javascript | 9958 | 9a841d891e95e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.58 | 0.41 | 0.21 | 200 | application/javascript | 10164 | 9a84a847cc6bb200-NRT |
| Washington, DC | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 13.86 | 0.70 | 0.24 | 200 | application/javascript | 10033 | 9a845e8bfd8d8c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.76 | 0.68 | 0.26 | 200 | application/javascript | 10118 | 9a84aa8b7c92af04-IAD |

### /cdn-cgi/challenge-platform/scripts/jsd/main.js (302)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 14.86 | 0.00 | 0.35 | 302 |  | 0 | 9a84227ab9d2dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 15.56 | 0.00 | 0.28 | 302 |  | 0 | 9a84a8f0ba50e866-FRA |
| London | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 18.04 | 0.00 | 0.40 | 302 |  | 0 | 9a84510f9adb6412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 38.33 | 0.00 | 0.34 | 302 |  | 0 | 9a84a9a0bf9e88ef-LHR |
| San Francisco | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 12.19 | 0.00 | 0.20 | 302 |  | 0 | 9a845fdb6f3acb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 14.69 | 0.00 | 0.30 | 302 |  | 0 | 9a84aca94af633fc-SJC |
| São Paulo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 28.33 | 0.00 | 0.22 | 302 |  | 0 | 9a846371ba3c2788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 16.69 | 0.00 | 0.29 | 302 |  | 0 | 9a84afa3ef51bc64-GRU |
| Sydney | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 14.59 | 0.00 | 0.23 | 302 |  | 0 | 9a84614a1aeaa959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 20.94 | 0.00 | 0.22 | 302 |  | 0 | 9a84ae1bbadae7ec-SYD |
| Tokyo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 14.46 | 0.00 | 0.19 | 302 |  | 0 | 9a841d88fe61e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 15.49 | 0.00 | 0.27 | 302 |  | 0 | 9a84a847ac46b200-NRT |
| Washington, DC | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 47.28 | 0.00 | 0.23 | 302 |  | 0 | 9a845e8bac7a8c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 22.47 | 0.00 | 0.33 | 302 |  | 0 | 9a84aa8b4c16af04-IAD |

### /cdn-cgi/rum (204)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| London | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| San Francisco | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 4.00 | 0.20 | 0.20 | 204 | text/plain | 0 | 9a845fdd8ac4cb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 4.53 | 0.25 | 0.18 | 204 | text/plain | 0 | 9a84aca95b1033fc-SJC |
| São Paulo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 7.33 | 0.20 | 0.16 | 204 | text/plain | 0 | 9a8463730c9b2788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 4.92 | 0.23 | 0.17 | 204 | text/plain | 0 | 9a84afa3ef64bc64-GRU |
| Sydney | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 5.47 | 0.28 | 0.17 | 204 | text/plain | 0 | 9a84614c0b93a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 2.91 | 0.22 | 0.17 | 204 | text/plain | 0 | 9a84ae1bcaeae7ec-SYD |
| Tokyo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 4.36 | 0.20 | 0.19 | 204 | text/plain | 0 | 9a841d8a8a23e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 5.15 | 0.26 | 0.25 | 204 | text/plain | 0 | 9a84a847bc57b200-NRT |
| Washington, DC | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 4.83 | 0.25 | 0.22 | 204 | text/plain | 0 | 9a845e8bbcb18c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 5.76 | 0.36 | 0.20 | 204 | text/plain | 0 | 9a84aa8b5c38af04-IAD |

### /en/login?callbackUrl=%2Fen%2Fprofile (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 121.12 | 104.02 | 0.21 | 200 | text/html | 75808 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 303.50 | 35.58 | 0.27 | 200 | text/html | 76727 | 9a8422782bfcdc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 270.00 | 92.82 | 0.31 | 200 | text/html | 76727 | 9a84a8ee2bf0e866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 259.14 | 682.18 | 0.35 | 200 | text/html | 75808 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 188.32 | 2781.79 | 0.28 | 200 | text/html | 76727 | 9a8450fcfc5c6412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 405.70 | 100.65 | 0.26 | 200 | text/html | 76727 | 9a84a99d1f5e88ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 373.69 | 228.67 | 0.26 | 200 | text/html | 75808 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 303.25 | 132.37 | 0.31 | 200 | text/html | 77231 | 9a845fd4eb3dcb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 2226.51 | 313.48 | 0.31 | 200 | text/html | 77231 | 9a84ac990da533fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 393.11 | 201.61 | 0.30 | 200 | text/html | 75808 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 401.53 | 127.09 | 0.31 | 200 | text/html | 77231 | 9a846369db3f2788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 470.66 | 111.36 | 0.33 | 200 | text/html | 77231 | 9a84af9fcfdcbc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 433.66 | 328.57 | 0.27 | 200 | text/html | 75808 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 597.34 | 131.27 | 0.26 | 200 | text/html | 77231 | 9a84613e8e87a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 512.56 | 120.64 | 0.28 | 200 | text/html | 77231 | 9a84ae176e7be7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 553.80 | 440.29 | 0.31 | 200 | text/html | 75808 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 440.30 | 134.16 | 0.28 | 200 | text/html | 77188 | 9a841d7ff9ace382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 442.20 | 33.87 | 0.32 | 200 | text/html | 77231 | 9a84a843eef8b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 585.28 | 2185.11 | 0.29 | 200 | text/html | 75808 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 460.66 | 93.39 | 0.33 | 200 | text/html | 77231 | 9a845e879fb08c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 576.40 | 1607.96 | 0.36 | 200 | text/html | 77231 | 9a84aa7d488eaf04-IAD |

### /en/profile (307)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 73.21 | 16.62 | 14.08 | 7.66 | 0.00 | 0.00 | 307 |  | 0 | — |
| Frankfurt | With CF Proxy | 26.62 | 14.43 | 12.92 | 51.25 | 0.00 | 0.00 | 307 |  | 0 | 9a8422779a8adc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 28.38 | 19.27 | 33.76 | 0.00 | 0.00 | 307 |  | 0 | 9a84a8edbad3e866-FRA |
| London | Without CF (DO LB) | 31.87 | 56.28 | 42.39 | 29.77 | 0.00 | 0.00 | 307 |  | 0 | — |
| London | With CF Proxy | 11.59 | 26.85 | 25.05 | 105.48 | 0.00 | 0.00 | 307 |  | 0 | 9a8450fbfba96412-LHR |
| London | With CF Proxy + CF Tunnel | 5.56 | 15.21 | 13.31 | 115.39 | 0.00 | 0.00 | 307 |  | 0 | 9a84a99c0cf788ef-LHR |
| San Francisco | Without CF (DO LB) | 22.11 | 322.45 | 168.69 | 160.74 | 0.00 | 0.00 | 307 |  | 0 | — |
| San Francisco | With CF Proxy | 4.74 | 18.12 | 16.62 | 630.23 | 0.00 | 0.00 | 307 |  | 0 | 9a845fcc9d45cb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 22.77 | 21.37 | 19.42 | 567.20 | 0.00 | 0.00 | 307 |  | 0 | 9a84ac942d7333fc-SJC |
| São Paulo | Without CF (DO LB) | 10.61 | 426.92 | 225.10 | 207.33 | 0.00 | 0.00 | 307 |  | 0 | — |
| São Paulo | With CF Proxy | 4.51 | 19.83 | 16.07 | 769.88 | 0.00 | 0.00 | 307 |  | 0 | 9a8463608a502788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 7.35 | 18.31 | 15.82 | 614.66 | 0.00 | 0.00 | 307 |  | 0 | 9a84af980a78bc64-GRU |
| Sydney | Without CF (DO LB) | 48.87 | 593.41 | 305.43 | 298.70 | 0.00 | 0.00 | 307 |  | 0 | — |
| Sydney | With CF Proxy | 49.56 | 15.39 | 13.97 | 1291.14 | 0.00 | 0.00 | 307 |  | 0 | 9a8461344aa2a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 51.42 | 21.95 | 17.84 | 902.32 | 0.00 | 0.00 | 307 |  | 0 | 9a84ae0f9e17e7ec-SYD |
| Tokyo | Without CF (DO LB) | 5.23 | 488.07 | 249.73 | 251.33 | 0.00 | 0.00 | 307 |  | 0 | — |
| Tokyo | With CF Proxy | 5.44 | 17.76 | 15.98 | 982.23 | 0.00 | 0.00 | 307 |  | 0 | 9a841d73ff40e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 14.36 | 13.07 | 691.63 | 0.00 | 0.00 | 307 |  | 0 | 9a84a83dadc7b200-NRT |
| Washington, DC | Without CF (DO LB) | 206.65 | 235.74 | 138.53 | 113.14 | 0.00 | 0.00 | 307 |  | 0 | — |
| Washington, DC | With CF Proxy | 96.13 | 14.85 | 13.17 | 434.02 | 0.00 | 0.00 | 307 |  | 0 | 9a845e840bf68c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 6.70 | 16.79 | 15.47 | 300.05 | 0.00 | 0.00 | 307 |  | 0 | 9a84aa7aa8d0af04-IAD |

### /favicon.ico (404)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 296.63 | 313.44 | 0.21 | 404 | text/html | 29480 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 338.80 | 190.78 | 0.28 | 404 | text/html | 29480 | 9a84227aea41dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 166.71 | 111.83 | 0.24 | 404 | text/html | 29480 | 9a84a8f0ca64e866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 128.99 | 392.05 | 0.31 | 404 | text/html | 29480 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 313.31 | 104.14 | 0.28 | 404 | text/html | 29480 | 9a84510f9ae96412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 303.78 | 204.79 | 0.24 | 404 | text/html | 29480 | 9a84a9a0cfc988ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 236.14 | 203.20 | 0.20 | 404 | text/html | 29480 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 480.23 | 197.87 | 0.30 | 404 | text/html | 29480 | 9a845fdd8ac5cb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 473.65 | 190.44 | 0.24 | 404 | text/html | 29480 | 9a84aca95b1433fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 286.53 | 296.72 | 0.20 | 404 | text/html | 29480 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 392.53 | 191.43 | 0.27 | 404 | text/html | 29480 | 9a8463731c9c2788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 428.00 | 297.83 | 0.65 | 404 | text/html | 29480 | 9a84afa3ff8fbc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 424.20 | 299.44 | 0.23 | 404 | text/html | 29480 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 433.25 | 108.04 | 0.28 | 404 | text/html | 29480 | 9a84614c0b94a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 694.25 | 217.90 | 0.21 | 404 | text/html | 29480 | 9a84ae1bcaece7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 262.61 | 289.30 | 0.21 | 404 | text/html | 29480 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 492.48 | 187.73 | 0.36 | 404 | text/html | 29480 | 9a841d8a8a29e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 503.78 | 189.57 | 0.27 | 404 | text/html | 29480 | 9a84a847bc58b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 174.52 | 303.79 | 0.22 | 404 | text/html | 29480 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 182.01 | 190.59 | 0.27 | 404 | text/html | 29480 | 9a845e8bbccc8c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 418.91 | 242.91 | 0.35 | 404 | text/html | 29480 | 9a84aa8b5c3faf04-IAD |

### /login?callbackUrl=%2Fen%2Fprofile (307)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 14.93 | 0.00 | 0.35 | 307 |  | 0 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 35.44 | 0.00 | 0.29 | 307 |  | 0 | 9a842277eb30dc58-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 35.91 | 0.00 | 0.33 | 307 |  | 0 | 9a84a8edeb5de866-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 38.61 | 0.00 | 0.32 | 307 |  | 0 | — |
| London | With CF Proxy | 0.00 | 0.00 | 0.00 | 50.01 | 0.00 | 0.33 | 307 |  | 0 | 9a8450fcac176412-LHR |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 48.67 | 0.00 | 0.33 | 307 |  | 0 | 9a84a99ccea988ef-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 195.68 | 0.00 | 0.33 | 307 |  | 0 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 693.02 | 0.00 | 0.30 | 307 |  | 0 | 9a845fd08bbdcb6f-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 203.68 | 0.00 | 0.31 | 307 |  | 0 | 9a84ac97bba933fc-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 334.77 | 0.00 | 0.37 | 307 |  | 0 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 718.49 | 0.00 | 0.30 | 307 |  | 0 | 9a8463655b992788-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 624.61 | 0.00 | 0.33 | 307 |  | 0 | 9a84af9bd97dbc64-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 309.87 | 0.00 | 0.32 | 307 |  | 0 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 344.18 | 0.00 | 0.30 | 307 |  | 0 | 9a84613c5dc6a959-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 344.40 | 0.00 | 0.41 | 307 |  | 0 | 9a84ae153c1fe7ec-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 254.72 | 0.00 | 0.42 | 307 |  | 0 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 929.83 | 0.00 | 0.43 | 307 |  | 0 | 9a841d7a2cf9e382-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 310.58 | 0.00 | 0.30 | 307 |  | 0 | 9a84a841fbe3b200-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 171.42 | 0.00 | 0.33 | 307 |  | 0 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 129.69 | 0.00 | 0.30 | 307 |  | 0 | 9a845e86bcf98c9d-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 117.24 | 0.00 | 0.33 | 307 |  | 0 | 9a84aa7c8e9daf04-IAD |

### /beacon.min.js/vcd15cbe7772f49c399c6a5babf22c1241717689176015 (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| Frankfurt | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| London | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | — | — | — | — | — | — | — | — | — | — |
| San Francisco | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| San Francisco | With CF Proxy | 0.42 | 22.66 | 21.36 | 15.77 | 0.65 | 1.27 | 200 | text/javascript | 19948 | 9a845fd81de9c487-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 3.66 | 18.72 | 16.55 | 21.47 | 0.50 | 0.27 | 200 | text/javascript | 19948 | 9a84aca90a2049ec-SJC |
| São Paulo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| São Paulo | With CF Proxy | 1.34 | 26.72 | 23.43 | 18.30 | 0.62 | 0.47 | 200 | text/javascript | 19948 | 9a84636ddda0f245-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 1.47 | 20.25 | 17.88 | 14.16 | 0.47 | 0.26 | 200 | text/javascript | 19948 | 9a84afa3b816c6a6-GRU |
| Sydney | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Sydney | With CF Proxy | 0.90 | 16.92 | 15.70 | 19.90 | 0.49 | 0.55 | 200 | text/javascript | 19948 | 9a8461445ba1a974-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.98 | 22.05 | 20.69 | 10.48 | 0.50 | 0.25 | 200 | text/javascript | 19948 | 9a84ae1b9af30fc3-SYD |
| Tokyo | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Tokyo | With CF Proxy | 0.47 | 23.70 | 21.55 | 15.68 | 0.58 | 0.26 | 200 | text/javascript | 19948 | 9a841d846807dfc5-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 1.08 | 21.50 | 19.85 | 14.22 | 0.57 | 0.31 | 200 | text/javascript | 19948 | 9a84a8477f01b012-NRT |
| Washington, DC | Without CF (DO LB) | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | With CF Proxy | 2.71 | 25.14 | 23.72 | 15.96 | 0.50 | 0.26 | 200 | text/javascript | 19948 | 9a845e8b8f1d7b5f-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 1.25 | 26.91 | 25.60 | 22.83 | 0.67 | 0.60 | 200 | text/javascript | 19948 | 9a84aa8b1ce79c3c-IAD |

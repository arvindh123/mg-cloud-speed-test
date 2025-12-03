## HAR summary: With-CF-Proxy-CF-Tunnel (`profile-page-*.json`)

Context:
- Tool: https://tools.pingdom.com/
- Source: `profile-page-*.json` (times in ms; content download = HAR `receive`)
- CF proxy + CF Tunnel in front of DigitalOcean Frankfurt (Kubernetes, DO LB + ingress-nginx).
- Requests include profile redirect chain, Next.js assets, favicon, Cloudflare challenge/telemetry files.
- Auth: unauthenticated -> redirects to login (200 login page); no session token present.
- Tables include MIME type, response size (bytes), cf-ray; `—` indicates the request is absent. Performance grade is not present in these HARs.

Summary (per location):

| Location | Requests | Page size (KB) | Load time (s, `_fullyLoaded`) | CF-ray (edge) | Performance grade |
|---|---:|---:|---:|---|---|
| Frankfurt | 34 | 1380.48 | 0.804 | FRA | n/a |
| London | 34 | 1380.47 | 1.287 | LHR | n/a |
| San Francisco | 36 | 1400.45 | 4.092 | SJC | n/a |
| São Paulo | 34 | 1275.66 | 2.672 | GRU | n/a |
| Sydney | 36 | 1400.48 | 2.939 | SYD | n/a |
| Tokyo | 36 | 1400.64 | 2.323 | NRT | n/a |
| Washington, DC | 34 | 1275.65 | 3.363 | IAD | n/a |

### GET `/en/profile` (307)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 28.38 | 19.27 | 33.76 | 0.00 | 0.00 | 307 |  | 0 | 9a84a8edbad3e866-FRA |
| London | 5.56 | 15.21 | 13.31 | 115.39 | 0.00 | 0.00 | 307 |  | 0 | 9a84a99c0cf788ef-LHR |
| San Francisco | 22.77 | 21.37 | 19.42 | 567.20 | 0.00 | 0.00 | 307 |  | 0 | 9a84ac942d7333fc-SJC |
| São Paulo | 7.35 | 18.31 | 15.82 | 614.66 | 0.00 | 0.00 | 307 |  | 0 | 9a84af980a78bc64-GRU |
| Sydney | 51.42 | 21.95 | 17.84 | 902.32 | 0.00 | 0.00 | 307 |  | 0 | 9a84ae0f9e17e7ec-SYD |
| Tokyo | 0.00 | 14.36 | 13.07 | 691.63 | 0.00 | 0.00 | 307 |  | 0 | 9a84a83dadc7b200-NRT |
| Washington, DC | 6.70 | 16.79 | 15.47 | 300.05 | 0.00 | 0.00 | 307 |  | 0 | 9a84aa7aa8d0af04-IAD |

### GET `/login?callbackUrl=%2Fen%2Fprofile` (307)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 35.91 | 0.00 | 0.33 | 307 |  | 0 | 9a84a8edeb5de866-FRA |
| London | 0.00 | 0.00 | 0.00 | 48.67 | 0.00 | 0.33 | 307 |  | 0 | 9a84a99ccea988ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 203.68 | 0.00 | 0.31 | 307 |  | 0 | 9a84ac97bba933fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 624.61 | 0.00 | 0.33 | 307 |  | 0 | 9a84af9bd97dbc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 344.40 | 0.00 | 0.41 | 307 |  | 0 | 9a84ae153c1fe7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 310.58 | 0.00 | 0.30 | 307 |  | 0 | 9a84a841fbe3b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 117.24 | 0.00 | 0.33 | 307 |  | 0 | 9a84aa7c8e9daf04-IAD |

### GET `/_next/static/css/e771c44a50dae3b6.css` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 0.07 | 0.29 | 0.29 | 200 | text/css | 4004 | 9a84a8f1dc96e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 0.10 | 0.75 | 1.06 | 200 | text/css | 4004 | 9a84a9a2ab4e88ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 0.08 | 0.31 | 0.31 | 200 | text/css | 4004 | 9a84acac494f33fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 0.08 | 0.40 | 1.30 | 200 | text/css | 4004 | 9a84afa2ad37bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 0.07 | 0.32 | 0.51 | 200 | text/css | 4004 | 9a84ae201f2de7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 0.08 | 0.32 | 0.42 | 200 | text/css | 4004 | 9a84a84adff4b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 0.09 | 0.38 | 3.83 | 200 | text/css | 4004 | 9a84aa80dbd3af04-IAD |

### GET `/_next/static/css/abf98b2abcdbd573.css` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 0.08 | 0.96 | 0.50 | 200 | text/css | 123936 | 9a84a8f1dc95e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 0.09 | 1.15 | 1.28 | 200 | text/css | 123936 | 9a84a9a2ab4b88ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 0.10 | 1.56 | 0.52 | 200 | text/css | 123936 | 9a84acac494d33fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 0.11 | 4.18 | 1.40 | 200 | text/css | 123936 | 9a84afa2ad34bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 0.11 | 1.62 | 0.71 | 200 | text/css | 123936 | 9a84ae201f2ce7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 0.09 | 1.69 | 0.68 | 200 | text/css | 123936 | 9a84a84adff3b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 0.11 | 1.22 | 4.01 | 200 | text/css | 123936 | 9a84aa80dbd0af04-IAD |

### GET `/_next/static/media/739c2d8941231bb4-s.p.woff2` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 8.42 | 0.41 | 1.05 | 200 | font/woff2 | 32752 | 9a84a8efe80ee866-FRA |
| London | 0.00 | 0.00 | 0.00 | 9.30 | 0.53 | 1.22 | 200 | font/woff2 | 32752 | 9a84a99fad1f88ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 7.46 | 0.48 | 1.05 | 200 | font/woff2 | 32752 | 9a84aca6fe6733fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 8.41 | 0.46 | 1.05 | 200 | font/woff2 | 32752 | 9a84afa2bd4cbc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 2.69 | 0.44 | 1.22 | 200 | font/woff2 | 32752 | 9a84ae1aa990e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 4.54 | 0.47 | 1.62 | 200 | font/woff2 | 32752 | 9a84a846bb1cb200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 12.13 | 0.57 | 4.22 | 200 | font/woff2 | 32752 | 9a84aa80ec07af04-IAD |

### GET `/_next/static/media/e4af272ccee01ff0-s.p.woff2` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.16 | 0.57 | 0.89 | 200 | font/woff2 | 48432 | 9a84a8efe811e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 8.19 | 2.86 | 1.05 | 200 | font/woff2 | 48432 | 9a84a99fad2488ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 5.80 | 2.52 | 1.11 | 200 | font/woff2 | 48432 | 9a84aca6fe6c33fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 7.36 | 0.85 | 1.46 | 200 | font/woff2 | 48432 | 9a84afa2bd51bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 3.76 | 1.55 | 1.07 | 200 | font/woff2 | 48432 | 9a84ae1aa991e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 5.26 | 0.73 | 1.20 | 200 | font/woff2 | 48432 | 9a84a846bb1db200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 12.93 | 0.85 | 4.12 | 200 | font/woff2 | 48432 | 9a84aa80ec0baf04-IAD |

### GET `/_next/static/chunks/webpack-b80cd65c35b59642.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.31 | 1.63 | 5.31 | 200 | application/javascript | 43159 | 9a84a8efe823e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 9.88 | 0.99 | 0.65 | 200 | application/javascript | 43159 | 9a84a99fad2588ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 9.17 | 2.54 | 4.17 | 200 | application/javascript | 43159 | 9a84aca6fe7233fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 10.65 | 1.31 | 4.54 | 200 | application/javascript | 43159 | 9a84afa2cd5fbc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 6.67 | 1.87 | 4.48 | 200 | application/javascript | 43159 | 9a84ae1aa99ce7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 6.40 | 1.55 | 4.69 | 200 | application/javascript | 43159 | 9a84a846bb22b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 15.65 | 0.69 | 3.59 | 200 | application/javascript | 43159 | 9a84aa80ec15af04-IAD |

### GET `/_next/static/media/authLogo.59ea595a.svg` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 10.29 | 0.51 | 0.23 | 200 | image/svg+xml | 16549 | 9a84a8efe829e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 9.13 | 0.50 | 0.32 | 200 | image/svg+xml | 16549 | 9a84a99fbd3b88ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 9.84 | 1.32 | 0.62 | 200 | image/svg+xml | 16549 | 9a84aca6fe7333fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 9.60 | 0.45 | 0.35 | 200 | image/svg+xml | 16549 | 9a84afa2cd61bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 7.68 | 0.36 | 0.37 | 200 | image/svg+xml | 16549 | 9a84ae1aa99de7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 6.67 | 0.38 | 0.24 | 200 | image/svg+xml | 16549 | 9a84a846bb25b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 11.91 | 0.71 | 0.36 | 200 | image/svg+xml | 16549 | 9a84aa80fc2baf04-IAD |

### GET `/_next/static/chunks/ad6b4c6d-bd23cbb78334428b.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 10.87 | 2.48 | 0.26 | 200 | application/javascript | 173026 | 9a84a8efe830e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 9.89 | 2.35 | 0.38 | 200 | application/javascript | 173026 | 9a84a99fbd3c88ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 10.33 | 3.43 | 0.58 | 200 | application/javascript | 173026 | 9a84aca6fe7433fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 8.35 | 4.02 | 0.37 | 200 | application/javascript | 173026 | 9a84afa2cd63bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 7.37 | 5.06 | 0.33 | 200 | application/javascript | 173026 | 9a84ae1aa99fe7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 7.25 | 3.27 | 0.28 | 200 | application/javascript | 173026 | 9a84a846bb26b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 13.07 | 1.79 | 0.30 | 200 | application/javascript | 173026 | 9a84aa80fc31af04-IAD |

### GET `/_next/static/chunks/main-app-3267ec133fe45348.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.32 | 7.12 | 0.20 | 200 | application/javascript | 572 | 9a84a8eff84ae866-FRA |
| London | 0.00 | 0.00 | 0.00 | 9.63 | 0.30 | 0.42 | 200 | application/javascript | 572 | 9a84a99fbd5988ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 12.34 | 1.08 | 1.58 | 200 | application/javascript | 572 | 9a84aca70e8c33fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 9.87 | 0.25 | 0.19 | 200 | application/javascript | 572 | 9a84afa2cd79bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 7.14 | 0.39 | 0.23 | 200 | application/javascript | 572 | 9a84ae1aa9a4e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 8.08 | 0.29 | 0.41 | 200 | application/javascript | 572 | 9a84a846cb32b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 11.42 | 0.32 | 0.21 | 200 | application/javascript | 572 | 9a84aa810c4baf04-IAD |

### GET `/_next/static/chunks/65264-dc11e68888cdad2a.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 8.59 | 7.97 | 0.69 | 200 | application/javascript | 172276 | 9a84a8efe846e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 8.69 | 2.72 | 0.74 | 200 | application/javascript | 172276 | 9a84a99fbd5788ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 7.60 | 2.11 | 0.54 | 200 | application/javascript | 172276 | 9a84aca70e8533fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 9.23 | 2.37 | 0.60 | 200 | application/javascript | 172276 | 9a84afa2cd75bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 6.12 | 3.22 | 0.94 | 200 | application/javascript | 172276 | 9a84ae1aa9a3e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 7.33 | 2.16 | 0.39 | 200 | application/javascript | 172276 | 9a84a846cb30b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 8.63 | 1.63 | 0.51 | 200 | application/javascript | 172276 | 9a84aa810c44af04-IAD |

### GET `/_next/static/chunks/40867-24b106b5648edbf1.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.52 | 0.43 | 1.28 | 200 | application/javascript | 31882 | 9a84a8eff867e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 7.90 | 0.51 | 0.36 | 200 | application/javascript | 31882 | 9a84a99fbd5b88ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 12.67 | 1.87 | 1.65 | 200 | application/javascript | 31882 | 9a84aca71ed633fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 8.33 | 1.25 | 1.46 | 200 | application/javascript | 31882 | 9a84afa2dd84bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 6.59 | 1.00 | 3.28 | 200 | application/javascript | 31882 | 9a84ae1ab9b0e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 6.71 | 0.40 | 2.21 | 200 | application/javascript | 31882 | 9a84a846cb3cb200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 10.33 | 0.51 | 0.20 | 200 | application/javascript | 31882 | 9a84aa810c5aaf04-IAD |

### GET `/_next/static/chunks/app/%5Blocale%5D/(app)/layout-b4d9c5a0442100bf.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.63 | 0.53 | 1.38 | 200 | application/javascript | 20176 | 9a84a8eff868e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 10.44 | 2.35 | 1.50 | 200 | application/javascript | 20176 | 9a84a99fcd7088ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 11.34 | 1.02 | 1.23 | 200 | application/javascript | 20176 | 9a84aca71ed933fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 7.13 | 0.45 | 1.89 | 200 | application/javascript | 20176 | 9a84afa2dd91bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 7.74 | 0.39 | 2.56 | 200 | application/javascript | 20176 | 9a84ae1ab9b1e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 5.92 | 0.51 | 2.32 | 200 | application/javascript | 20176 | 9a84a846cb3eb200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 10.94 | 2.47 | 1.12 | 200 | application/javascript | 20176 | 9a84aa810c79af04-IAD |

### GET `/_next/static/chunks/0f9dcbb3-4ea2e6533b43a41b.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 8.70 | 0.76 | 0.88 | 200 | application/javascript | 69536 | 9a84a8f0086ee866-FRA |
| London | 0.00 | 0.00 | 0.00 | 9.07 | 3.24 | 0.18 | 200 | application/javascript | 69536 | 9a84a99fcd7588ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 14.04 | 4.50 | 1.81 | 200 | application/javascript | 69536 | 9a84aca71eda33fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 10.01 | 2.16 | 3.14 | 200 | application/javascript | 69536 | 9a84afa2ed96bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 5.27 | 3.67 | 1.45 | 200 | application/javascript | 69536 | 9a84ae1ab9b2e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 7.13 | 0.85 | 0.23 | 200 | application/javascript | 69536 | 9a84a846db3fb200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 9.67 | 2.78 | 0.62 | 200 | application/javascript | 69536 | 9a84aa811c7faf04-IAD |

### GET `/_next/static/chunks/app/%5Blocale%5D/loading-98f017f93adc0ad2.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 10.31 | 0.31 | 0.22 | 200 | application/javascript | 4659 | 9a84a8f00872e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 8.88 | 0.42 | 1.16 | 200 | application/javascript | 4659 | 9a84a99fdd8288ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 11.84 | 1.34 | 0.61 | 200 | application/javascript | 4659 | 9a84aca72ef033fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 12.94 | 0.30 | 0.28 | 200 | application/javascript | 4659 | 9a84afa2ed9cbc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 6.21 | 0.30 | 0.24 | 200 | application/javascript | 4659 | 9a84ae1ab9b4e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 6.07 | 0.39 | 0.23 | 200 | application/javascript | 4659 | 9a84a846db45b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 17.83 | 0.40 | 0.18 | 200 | application/javascript | 4659 | 9a84aa811c8aaf04-IAD |

### GET `/_next/static/chunks/43423-49ad8b8120df9a57.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 13.35 | 0.40 | 0.82 | 200 | application/javascript | 25366 | 9a84a8f00870e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 9.96 | 0.49 | 1.97 | 200 | application/javascript | 25366 | 9a84a99fdd8088ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 11.19 | 0.71 | 0.56 | 200 | application/javascript | 25366 | 9a84aca71edc33fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 10.69 | 0.48 | 1.00 | 200 | application/javascript | 25366 | 9a84afa2ed9bbc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 7.63 | 0.37 | 0.29 | 200 | application/javascript | 25366 | 9a84ae1ab9b3e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 6.96 | 0.47 | 0.74 | 200 | application/javascript | 25366 | 9a84a846db44b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 9.74 | 1.35 | 0.18 | 200 | application/javascript | 25366 | 9a84aa811c84af04-IAD |

### GET `/_next/static/chunks/app/%5Blocale%5D/layout-df215d4a79c4add9.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 8.01 | 0.36 | 0.17 | 200 | application/javascript | 10734 | 9a84a8f018bae866-FRA |
| London | 0.00 | 0.00 | 0.00 | 10.51 | 0.50 | 1.97 | 200 | application/javascript | 10734 | 9a84a99fedc188ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 10.91 | 0.36 | 1.79 | 200 | application/javascript | 10734 | 9a84aca73f3733fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 9.30 | 0.53 | 0.28 | 200 | application/javascript | 10734 | 9a84afa2fdc2bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 7.67 | 1.03 | 0.99 | 200 | application/javascript | 10734 | 9a84ae1ac9d5e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 6.91 | 0.39 | 1.88 | 200 | application/javascript | 10734 | 9a84a846eb56b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 9.62 | 1.04 | 0.65 | 200 | application/javascript | 10734 | 9a84aa812cc7af04-IAD |

### GET `/_next/static/chunks/72283-44c31ff2dbd0a071.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 8.57 | 1.29 | 0.21 | 200 | application/javascript | 33960 | 9a84a8f018b4e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 9.46 | 0.56 | 0.29 | 200 | application/javascript | 33960 | 9a84a99fddac88ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 10.46 | 1.56 | 4.08 | 200 | application/javascript | 33960 | 9a84aca73f3533fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 8.76 | 0.81 | 0.41 | 200 | application/javascript | 33960 | 9a84afa2fdc1bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 8.86 | 1.10 | 1.08 | 200 | application/javascript | 33960 | 9a84ae1ac9d3e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 6.62 | 1.87 | 0.18 | 200 | application/javascript | 33960 | 9a84a846db52b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 9.99 | 1.44 | 0.62 | 200 | application/javascript | 33960 | 9a84aa812cc6af04-IAD |

### GET `/_next/static/chunks/87524-df2a52a55c85cce2.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 10.00 | 1.96 | 0.18 | 200 | application/javascript | 48368 | 9a84a8f018afe866-FRA |
| London | 0.00 | 0.00 | 0.00 | 7.18 | 1.04 | 0.40 | 200 | application/javascript | 48368 | 9a84a99fddab88ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 8.26 | 3.61 | 4.15 | 200 | application/javascript | 48368 | 9a84aca73f3433fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 9.85 | 1.00 | 0.31 | 200 | application/javascript | 48368 | 9a84afa2edb2bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 6.98 | 2.65 | 1.18 | 200 | application/javascript | 48368 | 9a84ae1ac9d1e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 5.95 | 2.60 | 1.27 | 200 | application/javascript | 48368 | 9a84a846db51b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 12.46 | 1.93 | 0.68 | 200 | application/javascript | 48368 | 9a84aa812cc0af04-IAD |

### GET `/_next/static/chunks/2065e367-738d69ba223595b9.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 12.96 | 2.76 | 0.28 | 200 | application/javascript | 157100 | 9a84a8f0089fe866-FRA |
| London | 0.00 | 0.00 | 0.00 | 10.31 | 2.39 | 0.29 | 200 | application/javascript | 157100 | 9a84a99fdd8388ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 8.57 | 4.08 | 4.26 | 200 | application/javascript | 157100 | 9a84aca73f3233fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 10.60 | 1.78 | 0.29 | 200 | application/javascript | 157100 | 9a84afa2edb0bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 8.12 | 6.42 | 1.21 | 200 | application/javascript | 157100 | 9a84ae1ac9cce7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 7.58 | 2.34 | 1.07 | 200 | application/javascript | 157100 | 9a84a846db50b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 10.20 | 7.25 | 0.24 | 200 | application/javascript | 157100 | 9a84aa811c93af04-IAD |

### GET `/_next/static/chunks/38874-526f584e6aadcd4b.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.24 | 1.82 | 0.17 | 200 | application/javascript | 8565 | 9a84a8f018c7e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 9.73 | 0.46 | 1.70 | 200 | application/javascript | 8565 | 9a84a99fedc488ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 9.14 | 0.33 | 1.47 | 200 | application/javascript | 8565 | 9a84aca73f3933fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 8.79 | 0.39 | 0.16 | 200 | application/javascript | 8565 | 9a84afa2fdcabc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 12.32 | 0.98 | 0.90 | 200 | application/javascript | 8565 | 9a84ae1ac9d7e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 6.13 | 0.35 | 0.71 | 200 | application/javascript | 8565 | 9a84a846eb58b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 12.60 | 0.92 | 2.90 | 200 | application/javascript | 8565 | 9a84aa813d0faf04-IAD |

### GET `/_next/static/chunks/28214-f7bd4fbe2e13f9bd.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 10.79 | 0.49 | 0.29 | 200 | application/javascript | 11457 | 9a84a8f028ebe866-FRA |
| London | 0.00 | 0.00 | 0.00 | 8.81 | 0.51 | 0.20 | 200 | application/javascript | 11457 | 9a84a99fedd688ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 10.89 | 0.30 | 0.68 | 200 | application/javascript | 11457 | 9a84aca74f6c33fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 9.28 | 0.38 | 0.24 | 200 | application/javascript | 11457 | 9a84afa30de2bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 6.77 | 2.13 | 1.72 | 200 | application/javascript | 11457 | 9a84ae1aea13e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 6.86 | 0.42 | 1.74 | 200 | application/javascript | 11457 | 9a84a846fb64b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 14.06 | 0.33 | 0.51 | 200 | application/javascript | 11457 | 9a84aa813d16af04-IAD |

### GET `/_next/static/chunks/28743-4a3deeebaf794acf.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 11.52 | 0.38 | 0.34 | 200 | application/javascript | 9506 | 9a84a8f028e8e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 9.35 | 0.49 | 0.23 | 200 | application/javascript | 9506 | 9a84a99fedcd88ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 10.15 | 0.56 | 0.92 | 200 | application/javascript | 9506 | 9a84aca74f6b33fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 9.19 | 0.34 | 0.23 | 200 | application/javascript | 9506 | 9a84afa30ddebc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 6.23 | 0.36 | 1.79 | 200 | application/javascript | 9506 | 9a84ae1aea12e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 6.12 | 0.45 | 1.21 | 200 | application/javascript | 9506 | 9a84a846fb63b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 13.51 | 0.36 | 0.76 | 200 | application/javascript | 9506 | 9a84aa813d13af04-IAD |

### GET `/_next/static/chunks/28381-f69fef083c6248e7.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.62 | 0.94 | 1.28 | 200 | application/javascript | 23076 | 9a84a8f028f8e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 8.52 | 0.79 | 1.96 | 200 | application/javascript | 23076 | 9a84a99ffdf288ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 9.25 | 2.19 | 0.62 | 200 | application/javascript | 23076 | 9a84aca74f6f33fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 9.86 | 0.44 | 0.26 | 200 | application/javascript | 23076 | 9a84afa30de3bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 7.27 | 0.37 | 1.23 | 200 | application/javascript | 23076 | 9a84ae1aea15e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 6.44 | 1.76 | 1.02 | 200 | application/javascript | 23076 | 9a84a846fb69b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 12.93 | 3.09 | 0.36 | 200 | application/javascript | 23076 | 9a84aa813d20af04-IAD |

### GET `/_next/static/chunks/75245-4381628e6d93ed7c.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 12.13 | 2.08 | 0.39 | 200 | application/javascript | 83664 | 9a84a8f028e5e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 7.82 | 1.45 | 0.20 | 200 | application/javascript | 83664 | 9a84a99fedc688ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 8.64 | 3.14 | 2.91 | 200 | application/javascript | 83664 | 9a84aca74f6833fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 8.48 | 1.58 | 0.89 | 200 | application/javascript | 83664 | 9a84afa30ddcbc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 8.08 | 1.06 | 4.64 | 200 | application/javascript | 83664 | 9a84ae1aea11e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 7.40 | 1.53 | 0.50 | 200 | application/javascript | 83664 | 9a84a846eb5ab200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 9.95 | 6.33 | 1.57 | 200 | application/javascript | 83664 | 9a84aa813d10af04-IAD |

### GET `/_next/static/chunks/app/%5Blocale%5D/(auth)/login/page-db91e715f9db634b.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 11.51 | 0.36 | 0.38 | 200 | application/javascript | 6428 | 9a84a8f028fce866-FRA |
| London | 0.00 | 0.00 | 0.00 | 9.66 | 0.69 | 1.82 | 200 | application/javascript | 6428 | 9a84a99ffdf488ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 9.52 | 0.38 | 0.49 | 200 | application/javascript | 6428 | 9a84aca74f7133fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 7.49 | 0.39 | 0.17 | 200 | application/javascript | 6428 | 9a84afa30de5bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 6.78 | 0.26 | 0.41 | 200 | application/javascript | 6428 | 9a84ae1aea16e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 7.10 | 1.15 | 3.51 | 200 | application/javascript | 6428 | 9a84a846fb6cb200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 12.39 | 1.82 | 1.14 | 200 | application/javascript | 6428 | 9a84aa815d64af04-IAD |

### GET `/_next/static/chunks/app/%5Blocale%5D/error-c58756f7ba7b9f2b.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 11.31 | 0.59 | 1.24 | 200 | application/javascript | 10308 | 9a84a8f0392ee866-FRA |
| London | 0.00 | 0.00 | 0.00 | 10.67 | 0.62 | 0.86 | 200 | application/javascript | 10308 | 9a84a99ffdf588ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 11.18 | 0.67 | 1.36 | 200 | application/javascript | 10308 | 9a84aca76f9733fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 10.26 | 0.35 | 0.33 | 200 | application/javascript | 10308 | 9a84afa31df5bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 6.44 | 0.36 | 0.68 | 200 | application/javascript | 10308 | 9a84ae1afa28e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 7.65 | 0.64 | 3.44 | 200 | application/javascript | 10308 | 9a84a846fb6db200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 13.16 | 0.73 | 1.02 | 200 | application/javascript | 10308 | 9a84aa815d6baf04-IAD |

### GET `/en/login?callbackUrl=%2Fen%2Fprofile` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 270.00 | 92.82 | 0.31 | 200 | text/html | 76727 | 9a84a8ee2bf0e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 405.70 | 100.65 | 0.26 | 200 | text/html | 76727 | 9a84a99d1f5e88ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 2226.51 | 313.48 | 0.31 | 200 | text/html | 77231 | 9a84ac990da533fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 470.66 | 111.36 | 0.33 | 200 | text/html | 77231 | 9a84af9fcfdcbc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 512.56 | 120.64 | 0.28 | 200 | text/html | 77231 | 9a84ae176e7be7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 442.20 | 33.87 | 0.32 | 200 | text/html | 77231 | 9a84a843eef8b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 576.40 | 1607.96 | 0.36 | 200 | text/html | 77231 | 9a84aa7d488eaf04-IAD |

### GET `/cdn-cgi/challenge-platform/scripts/jsd/main.js` (302)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 15.56 | 0.00 | 0.28 | 302 |  | 0 | 9a84a8f0ba50e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 38.33 | 0.00 | 0.34 | 302 |  | 0 | 9a84a9a0bf9e88ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 14.69 | 0.00 | 0.30 | 302 |  | 0 | 9a84aca94af633fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 16.69 | 0.00 | 0.29 | 302 |  | 0 | 9a84afa3ef51bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 20.94 | 0.00 | 0.22 | 302 |  | 0 | 9a84ae1bbadae7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 15.49 | 0.00 | 0.27 | 302 |  | 0 | 9a84a847ac46b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 22.47 | 0.00 | 0.33 | 302 |  | 0 | 9a84aa8b4c16af04-IAD |

### GET `/cdn-cgi/challenge-platform/h/b/scripts/jsd/13c98df4ef2d/main.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.04 | 0.56 | 0.20 | 200 | application/javascript | 9978 | 9a84a8f0da83e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 11.24 | 0.66 | 0.26 | 200 | application/javascript | 9965 | 9a84a9a0f82288ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 32.76 | 0.43 | 0.19 | 200 | application/javascript | 9974 | 9a84aca96b6233fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 12.24 | 0.39 | 0.16 | 200 | application/javascript | 10121 | 9a84afa40f93bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 9.37 | 0.39 | 0.19 | 200 | application/javascript | 10006 | 9a84ae1beb03e7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 7.58 | 0.41 | 0.21 | 200 | application/javascript | 10164 | 9a84a847cc6bb200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 8.76 | 0.68 | 0.26 | 200 | application/javascript | 10118 | 9a84aa8b7c92af04-IAD |

### POST `/cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.48787175522499493:1764780765:ffx7zC-Wk64FNnKGFpWIfxjLgt-MkY_KjrUz5sb6OQ0/9a84a8ee2bf0e866` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 28.89 | 0.33 | 0.24 | 200 | text/plain | 0 | 9a84a8f18bf1e866-FRA |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | — | — | — | — | — | — | — | — | — | — |
| São Paulo | — | — | — | — | — | — | — | — | — | — |
| Sydney | — | — | — | — | — | — | — | — | — | — |
| Tokyo | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | — | — | — | — | — | — | — | — | — | — |

### GET `/favicon.ico` (404)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 166.71 | 111.83 | 0.24 | 404 | text/html | 29480 | 9a84a8f0ca64e866-FRA |
| London | 0.00 | 0.00 | 0.00 | 303.78 | 204.79 | 0.24 | 404 | text/html | 29480 | 9a84a9a0cfc988ef-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 473.65 | 190.44 | 0.24 | 404 | text/html | 29480 | 9a84aca95b1433fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 428.00 | 297.83 | 0.65 | 404 | text/html | 29480 | 9a84afa3ff8fbc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 694.25 | 217.90 | 0.21 | 404 | text/html | 29480 | 9a84ae1bcaece7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 503.78 | 189.57 | 0.27 | 404 | text/html | 29480 | 9a84a847bc58b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 418.91 | 242.91 | 0.35 | 404 | text/html | 29480 | 9a84aa8b5c3faf04-IAD |

### POST `/cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.48787175522499493:1764780765:ffx7zC-Wk64FNnKGFpWIfxjLgt-MkY_KjrUz5sb6OQ0/9a84a99d1f5e88ef` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | — | — | — | — | — | — | — | — | — | — |
| London | 0.00 | 0.00 | 0.00 | 15.00 | 0.31 | 0.44 | 200 | text/plain | 0 | 9a84a9a1c98d88ef-LHR |
| San Francisco | — | — | — | — | — | — | — | — | — | — |
| São Paulo | — | — | — | — | — | — | — | — | — | — |
| Sydney | — | — | — | — | — | — | — | — | — | — |
| Tokyo | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | — | — | — | — | — | — | — | — | — | — |

### GET `/beacon.min.js/vcd15cbe7772f49c399c6a5babf22c1241717689176015` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | — | — | — | — | — | — | — | — | — | — |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | 3.66 | 18.72 | 16.55 | 21.47 | 0.50 | 0.27 | 200 | text/javascript | 19948 | 9a84aca90a2049ec-SJC |
| São Paulo | 1.47 | 20.25 | 17.88 | 14.16 | 0.47 | 0.26 | 200 | text/javascript | 19948 | 9a84afa3b816c6a6-GRU |
| Sydney | 0.98 | 22.05 | 20.69 | 10.48 | 0.50 | 0.25 | 200 | text/javascript | 19948 | 9a84ae1b9af30fc3-SYD |
| Tokyo | 1.08 | 21.50 | 19.85 | 14.22 | 0.57 | 0.31 | 200 | text/javascript | 19948 | 9a84a8477f01b012-NRT |
| Washington, DC | 1.25 | 26.91 | 25.60 | 22.83 | 0.67 | 0.60 | 200 | text/javascript | 19948 | 9a84aa8b1ce79c3c-IAD |

### POST `/cdn-cgi/rum` (204)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | — | — | — | — | — | — | — | — | — | — |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | 0.00 | 0.00 | 0.00 | 4.53 | 0.25 | 0.18 | 204 | text/plain | 0 | 9a84aca95b1033fc-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 4.92 | 0.23 | 0.17 | 204 | text/plain | 0 | 9a84afa3ef64bc64-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 2.91 | 0.22 | 0.17 | 204 | text/plain | 0 | 9a84ae1bcaeae7ec-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 5.15 | 0.26 | 0.25 | 204 | text/plain | 0 | 9a84a847bc57b200-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 5.76 | 0.36 | 0.20 | 204 | text/plain | 0 | 9a84aa8b5c38af04-IAD |

### POST `/cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.48787175522499493:1764780765:ffx7zC-Wk64FNnKGFpWIfxjLgt-MkY_KjrUz5sb6OQ0/9a84ac990da533fc` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | — | — | — | — | — | — | — | — | — | — |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | 0.00 | 0.00 | 0.00 | 14.63 | 0.32 | 0.33 | 200 | text/plain | 0 | 9a84acaa6d3f33fc-SJC |
| São Paulo | — | — | — | — | — | — | — | — | — | — |
| Sydney | — | — | — | — | — | — | — | — | — | — |
| Tokyo | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | — | — | — | — | — | — | — | — | — | — |

### POST `/cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.48787175522499493:1764780765:ffx7zC-Wk64FNnKGFpWIfxjLgt-MkY_KjrUz5sb6OQ0/9a84af9fcfdcbc64` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | — | — | — | — | — | — | — | — | — | — |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | — | — | — | — | — | — | — | — | — | — |
| São Paulo | 0.00 | 0.00 | 0.00 | 25.80 | 0.83 | 0.24 | 200 | text/plain | 0 | 9a84afa4c951bc64-GRU |
| Sydney | — | — | — | — | — | — | — | — | — | — |
| Tokyo | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | — | — | — | — | — | — | — | — | — | — |

### POST `/cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.48787175522499493:1764780765:ffx7zC-Wk64FNnKGFpWIfxjLgt-MkY_KjrUz5sb6OQ0/9a84ae176e7be7ec` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | — | — | — | — | — | — | — | — | — | — |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | — | — | — | — | — | — | — | — | — | — |
| São Paulo | — | — | — | — | — | — | — | — | — | — |
| Sydney | 0.00 | 0.00 | 0.00 | 11.05 | 0.29 | 0.22 | 200 | text/plain | 0 | 9a84ae1c9ba1e7ec-SYD |
| Tokyo | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | — | — | — | — | — | — | — | — | — | — |

### POST `/cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.7589308712729556:1764777276:Dq0c_wZGRrMPY-hSCmoqTpc1FCC57z162N2iJ5FrXxA/9a84a843eef8b200` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | — | — | — | — | — | — | — | — | — | — |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | — | — | — | — | — | — | — | — | — | — |
| São Paulo | — | — | — | — | — | — | — | — | — | — |
| Sydney | — | — | — | — | — | — | — | — | — | — |
| Tokyo | 0.00 | 0.00 | 0.00 | 16.26 | 0.36 | 0.27 | 200 | text/plain | 0 | 9a84a848ad5fb200-NRT |
| Washington, DC | — | — | — | — | — | — | — | — | — | — |

### POST `/cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.48787175522499493:1764780765:ffx7zC-Wk64FNnKGFpWIfxjLgt-MkY_KjrUz5sb6OQ0/9a84aa7d488eaf04` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | — | — | — | — | — | — | — | — | — | — |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | — | — | — | — | — | — | — | — | — | — |
| São Paulo | — | — | — | — | — | — | — | — | — | — |
| Sydney | — | — | — | — | — | — | — | — | — | — |
| Tokyo | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | 0.00 | 0.00 | 0.00 | 27.73 | 0.37 | 0.31 | 200 | text/plain | 0 | 9a84aa8c3f03af04-IAD |

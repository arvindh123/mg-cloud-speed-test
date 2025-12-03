## HAR summary: With-CF-Proxy-CF-Tunnel (`api-users-health -*.json`)

Context:
- Tool: https://tools.pingdom.com/
- Source: `api-users-health -*.json` (times in ms; content download = HAR `receive`)
- CF proxy + CF Tunnel in front of DigitalOcean Frankfurt (Kubernetes, DO LB + ingress-nginx).
- Requests captured (6 per location).
- Auth: no bearer token; `/api/users/health` returns 401 JSON {"error":"","message":"missing or invalid bearer user token"}; static assets 200; favicon 404.
- Tables include MIME type, response size (bytes), cf-ray.

Summary (per location):

| Location | Requests | Page size (KB) | Load time (s, `_fullyLoaded`) | CF-ray (edge) | Performance grade |
|---|---:|---:|---:|---|---|
| Frankfurt | 6 | 233.07 | 0.468 | FRA | n/a |
| London | 6 | 233.07 | 2.206 | LHR | n/a |
| San Francisco | 6 | 233.07 | 1.057 | SJC | n/a |
| São Paulo | 6 | 233.07 | 1.165 | GRU | n/a |
| Sydney | 6 | 233.07 | 1.690 | SYD | n/a |
| Tokyo | 6 | 233.07 | 1.988 | NRT | n/a |
| Washington, DC | 6 | 233.07 | 0.875 | IAD | n/a |

### GET `/api/users/health` (401)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 8.53 | 13.21 | 11.89 | 25.22 | 0.88 | 0.00 | 401 | application/json | 62 | 9a849f661923bbe5-FRA |
| London | 39.20 | 17.42 | 15.40 | 69.57 | 1.07 | 0.00 | 401 | application/json | 62 | 9a84a07d2c944e3b-LHR |
| San Francisco | 24.10 | 15.87 | 13.87 | 535.72 | 0.85 | 0.00 | 401 | application/json | 62 | 9a84a20cab3349d2-SJC |
| São Paulo | 23.73 | 17.37 | 13.49 | 603.75 | 0.84 | 0.00 | 401 | application/json | 62 | 9a84a46b9a14f181-GRU |
| Sydney | 90.35 | 12.42 | 10.99 | 901.92 | 0.95 | 0.00 | 401 | application/json | 62 | 9a84a3715d4fa7f6-SYD |
| Tokyo | 0.28 | 14.90 | 12.90 | 749.27 | 0.89 | 0.00 | 401 | application/json | 62 | 9a849ebdfe94d758-NRT |
| Washington, DC | 6.03 | 14.35 | 12.83 | 304.28 | 1.03 | 0.00 | 401 | application/json | 62 | 9a84a153ac7264aa-IAD |

### GET `/_next/static/css/e771c44a50dae3b6.css` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 0.07 | 0.36 | 0.57 | 200 | text/css | 4004 | 9a849f67ba62bbe5-FRA |
| London | 0.00 | 0.00 | 0.00 | 0.13 | 0.64 | 0.87 | 200 | text/css | 4004 | 9a84a07f69794e3b-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 0.11 | 0.72 | 0.57 | 200 | text/css | 4004 | 9a84a2126ddf49d2-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 0.12 | 0.40 | 0.83 | 200 | text/css | 4004 | 9a84a471ef19f181-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 0.12 | 0.54 | 0.77 | 200 | text/css | 4004 | 9a84a37a0f30a7f6-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 0.07 | 0.27 | 0.80 | 200 | text/css | 4004 | 9a849ec92b01d758-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 0.09 | 0.54 | 0.85 | 200 | text/css | 4004 | 9a84a1584fe764aa-IAD |

### GET `/_next/static/css/abf98b2abcdbd573.css` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 0.14 | 2.29 | 0.71 | 200 | text/css | 123936 | 9a849f67ba60bbe5-FRA |
| London | 0.00 | 0.00 | 0.00 | 0.08 | 1.20 | 1.01 | 200 | text/css | 123936 | 9a84a07f69774e3b-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 0.08 | 0.98 | 0.70 | 200 | text/css | 123936 | 9a84a2126dde49d2-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 0.09 | 0.88 | 0.93 | 200 | text/css | 123936 | 9a84a471ef17f181-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 0.07 | 0.99 | 0.87 | 200 | text/css | 123936 | 9a84a37a0f2fa7f6-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 0.13 | 1.18 | 0.93 | 200 | text/css | 123936 | 9a849ec92affd758-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 0.16 | 3.98 | 1.01 | 200 | text/css | 123936 | 9a84a1584fe364aa-IAD |

### GET `/_next/static/media/739c2d8941231bb4-s.p.woff2` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.61 | 1.08 | 0.91 | 200 | font/woff2 | 32752 | 9a849f67ba66bbe5-FRA |
| London | 0.00 | 0.00 | 0.00 | 9.62 | 0.92 | 1.23 | 200 | font/woff2 | 32752 | 9a84a07f698c4e3b-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 8.77 | 0.43 | 0.91 | 200 | font/woff2 | 32752 | 9a84a2126de949d2-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 11.42 | 1.89 | 1.05 | 200 | font/woff2 | 32752 | 9a84a471ff29f181-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 7.03 | 0.50 | 1.18 | 200 | font/woff2 | 32752 | 9a84a37a0f31a7f6-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 5.99 | 0.38 | 1.09 | 200 | font/woff2 | 32752 | 9a849ec93b06d758-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 20.07 | 0.55 | 1.17 | 200 | font/woff2 | 32752 | 9a84a1584ff564aa-IAD |

### GET `/_next/static/media/e4af272ccee01ff0-s.p.woff2` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.95 | 0.91 | 0.82 | 200 | font/woff2 | 48432 | 9a849f67ba68bbe5-FRA |
| London | 0.00 | 0.00 | 0.00 | 10.77 | 0.73 | 1.15 | 200 | font/woff2 | 48432 | 9a84a07f698e4e3b-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 7.31 | 2.12 | 0.82 | 200 | font/woff2 | 48432 | 9a84a2126dea49d2-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 10.57 | 1.43 | 1.02 | 200 | font/woff2 | 48432 | 9a84a471ff2cf181-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 7.77 | 0.72 | 0.98 | 200 | font/woff2 | 48432 | 9a84a37a0f32a7f6-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 7.02 | 0.60 | 1.04 | 200 | font/woff2 | 48432 | 9a849ec93b07d758-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 21.11 | 0.81 | 1.14 | 200 | font/woff2 | 48432 | 9a84a1585ff764aa-IAD |

### GET `/favicon.ico` (404)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 206.29 | 194.01 | 0.27 | 404 | text/html | 29480 | 9a849f66696abbe5-FRA |
| London | 0.00 | 0.00 | 0.00 | 258.32 | 1790.05 | 0.29 | 404 | text/html | 29480 | 9a84a07dcdff4e3b-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 334.27 | 100.82 | 0.34 | 404 | text/html | 29480 | 9a84a210499d49d2-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 381.79 | 107.37 | 0.25 | 404 | text/html | 29480 | 9a84a46f8a16f181-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 483.07 | 191.46 | 0.32 | 404 | text/html | 29480 | 9a84a3770e93a7f6-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 1027.48 | 182.83 | 0.27 | 404 | text/html | 29480 | 9a849ec2cbf3d758-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 429.76 | 107.54 | 0.33 | 404 | text/html | 29480 | 9a84a155994864aa-IAD |

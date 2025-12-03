## HAR summary: With-CF-Proxy (`api-users-health -*.json`)

Context:
- Tool: https://tools.pingdom.com/
- Source: `api-users-health -*.json` (times in ms; content download = HAR `receive`)
- CF proxy enabled in front of DigitalOcean Frankfurt (Kubernetes, DO LB + ingress-nginx).
- Requests captured (6 for most locations; London file only has the API request).
- Auth: no bearer token; `/api/users/health` returns 401 JSON {"error":"","message":"missing or invalid bearer user token"}; static assets 200; favicon 404.
- Tables include MIME type, response size (bytes), cf-ray, and `—` where a request is absent in a location.

Summary (per location):

| Location | Requests | Page size (KB) | Load time (s, `_fullyLoaded`) | CF-ray (edge) | Performance grade |
|---|---:|---:|---:|---|---|
| Frankfurt | 6 | 233.07 | 0.461 | FRA | n/a |
| London | 1 | 0.06 | 0.161 | LHR | n/a |
| San Francisco | 6 | 233.07 | 1.214 | SJC | n/a |
| São Paulo | 6 | 233.07 | 3.658 | GRU | n/a |
| Sydney | 6 | 233.07 | 1.923 | SYD | n/a |
| Tokyo | 6 | 233.07 | 2.232 | NRT | n/a |
| Washington, DC | 6 | 233.07 | 1.076 | IAD | n/a |

### GET `/api/users/health` (401)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 6.65 | 13.41 | 12.39 | 38.98 | 8.77 | 0.00 | 401 | application/json | 62 | 9a846aa9a88bd28a-FRA |
| London | 38.11 | 16.41 | 14.70 | 94.34 | 1.04 | 0.00 | 401 | application/json | 62 | 9a846c9a0e785016-LHR |
| San Francisco | 15.05 | 15.02 | 13.14 | 640.19 | 0.91 | 0.00 | 401 | application/json | 62 | 9a846fc1bc53fc54-SJC |
| São Paulo | 13.74 | 21.89 | 15.96 | 720.74 | 0.89 | 0.00 | 401 | application/json | 62 | 9a84718b19edf198-GRU |
| Sydney | 15.63 | 14.52 | 13.14 | 1209.48 | 0.97 | 0.00 | 401 | application/json | 62 | 9a8470a3bce8e7c8-SYD |
| Tokyo | 2.72 | 27.78 | 18.11 | 992.78 | 0.83 | 0.00 | 401 | application/json | 62 | 9a8469949c5c9d71-NRT |
| Washington, DC | 31.52 | 15.31 | 13.85 | 434.89 | 0.90 | 0.00 | 401 | application/json | 62 | 9a846d673da4c95e-IAD |

### GET `/_next/static/css/abf98b2abcdbd573.css` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 0.19 | 1.02 | 0.77 | 200 | text/css | 123936 | 9a846aab3d37d28a-FRA |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | 0.00 | 0.00 | 0.00 | 0.17 | 1.01 | 0.77 | 200 | text/css | 123936 | 9a846fc86dc3fc54-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 0.17 | 0.93 | 1.04 | 200 | text/css | 123936 | 9a8471920c91f198-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 0.11 | 1.59 | 0.76 | 200 | text/css | 123936 | 9a8470aeee3ee7c8-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 0.07 | 0.92 | 0.85 | 200 | text/css | 123936 | 9a84699d6e369d71-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 0.13 | 3.36 | 0.81 | 200 | text/css | 123936 | 9a846d6c695fc95e-IAD |

### GET `/_next/static/css/e771c44a50dae3b6.css` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 0.08 | 1.28 | 0.67 | 200 | text/css | 4004 | 9a846aab3d3bd28a-FRA |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | 0.00 | 0.00 | 0.00 | 0.09 | 0.29 | 0.68 | 200 | text/css | 4004 | 9a846fc86dc4fc54-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 0.08 | 0.31 | 0.92 | 200 | text/css | 4004 | 9a8471920c94f198-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 0.15 | 1.32 | 0.68 | 200 | text/css | 4004 | 9a8470aeee40e7c8-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 0.14 | 0.52 | 0.74 | 200 | text/css | 4004 | 9a84699d6e389d71-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 0.11 | 0.77 | 0.71 | 200 | text/css | 4004 | 9a846d6c6960c95e-IAD |

### GET `/_next/static/media/739c2d8941231bb4-s.p.woff2` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 7.06 | 1.13 | 0.99 | 200 | font/woff2 | 32752 | 9a846aab3d4fd28a-FRA |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | 0.00 | 0.00 | 0.00 | 8.50 | 0.39 | 0.93 | 200 | font/woff2 | 32752 | 9a846fc87dccfc54-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 7.78 | 0.55 | 1.35 | 200 | font/woff2 | 32752 | 9a8471920cabf198-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 7.33 | 0.77 | 1.11 | 200 | font/woff2 | 32752 | 9a8470aeee41e7c8-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 6.85 | 0.45 | 1.10 | 200 | font/woff2 | 32752 | 9a84699d6e449d71-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 10.26 | 0.92 | 1.06 | 200 | font/woff2 | 32752 | 9a846d6c6968c95e-IAD |

### GET `/_next/static/media/e4af272ccee01ff0-s.p.woff2` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 7.27 | 1.12 | 0.89 | 200 | font/woff2 | 48432 | 9a846aab3d52d28a-FRA |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | 0.00 | 0.00 | 0.00 | 8.04 | 2.12 | 0.89 | 200 | font/woff2 | 48432 | 9a846fc87dcefc54-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 8.53 | 2.01 | 1.14 | 200 | font/woff2 | 48432 | 9a8471920cacf198-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 6.64 | 1.13 | 0.87 | 200 | font/woff2 | 48432 | 9a8470aefe42e7c8-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 8.01 | 0.53 | 0.93 | 200 | font/woff2 | 48432 | 9a84699d6e459d71-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 11.42 | 1.58 | 0.90 | 200 | font/woff2 | 48432 | 9a846d6c696bc95e-IAD |

### GET `/favicon.ico` (404)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 193.10 | 186.43 | 0.26 | 404 | text/html | 29480 | 9a846aaa09a9d28a-FRA |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | 0.00 | 0.00 | 0.00 | 400.93 | 104.20 | 0.83 | 404 | text/html | 29480 | 9a846fc5fa66fc54-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 369.79 | 2507.70 | 0.25 | 404 | text/html | 29480 | 9a84718fb92cf198-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 572.43 | 99.73 | 0.25 | 404 | text/html | 29480 | 9a8470ab5b42e7c8-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 410.26 | 791.23 | 0.24 | 404 | text/html | 29480 | 9a84699ad9689d71-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 385.34 | 197.97 | 0.25 | 404 | text/html | 29480 | 9a846d6a0bd7c95e-IAD |

## HAR summary: Without-CF-Proxy-Direct-DO-LB (`api-users-health -*.json`)

Context:
- Tool: https://tools.pingdom.com/
- Source: `api-users-health -*.json` (times in ms; content download = HAR `receive`)
- Hosting: DigitalOcean Frankfurt (Kubernetes) behind a DO load balancer with ingress-nginx
- Requests captured (6): `/api/users/health`, two CSS bundles, two font files, `/favicon.ico`
- Auth: no bearer token supplied; `/api/users/health` returns 401 JSON `{"error":"","message":"missing or invalid bearer user token"}` at the transport layer (no authn/authz downstream). Static assets return 200; `favicon.ico` returns 404.
- Tables include MIME type and response content size (bytes).
- Pingdom “performance grade” is not stored in these HARs (n/a below).

Summary (per location):

| Location | Requests | Page size (KB) | Load time (s, `_fullyLoaded`) | Performance grade |
|---|---:|---:|---:|---|
| Frankfurt | 6 | 233.07 | 0.374 | n/a |
| London | 6 | 233.07 | 0.467 | n/a |
| San Francisco | 6 | 233.07 | 1.305 | n/a |
| São Paulo | 6 | 233.07 | 1.605 | n/a |
| Sydney | 6 | 233.07 | 2.132 | n/a |
| Tokyo | 6 | 233.07 | 1.820 | n/a |
| Washington, DC | 6 | 233.07 | 0.852 | n/a |

### GET `/api/users/health` (401)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 7.62 | 13.57 | 12.74 | 8.25 | 7.22 | 0.00 | 401 | application/json | 62 |
| London | 7.46 | 47.36 | 31.71 | 18.71 | 14.73 | 0.00 | 401 | application/json | 62 |
| San Francisco | 0.30 | 314.27 | 163.18 | 156.88 | 0.80 | 0.00 | 401 | application/json | 62 |
| São Paulo | 17.96 | 406.16 | 208.77 | 199.70 | 0.91 | 0.00 | 401 | application/json | 62 |
| Sydney | 59.91 | 591.24 | 303.62 | 301.96 | 0.84 | 0.00 | 401 | application/json | 62 |
| Tokyo | 9.76 | 494.91 | 256.31 | 243.92 | 0.90 | 0.00 | 401 | application/json | 62 |
| Washington, DC | 28.46 | 221.82 | 107.38 | 97.70 | 0.88 | 0.00 | 401 | application/json | 62 |

### GET `/favicon.ico` (404)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 30.07 | 291.08 | 0.31 | 404 | text/html | 29480 |
| London | 0.00 | 0.00 | 0.00 | 53.06 | 309.52 | 0.31 | 404 | text/html | 29480 |
| San Francisco | 0.00 | 0.00 | 0.00 | 258.04 | 554.55 | 0.26 | 404 | text/html | 29480 |
| São Paulo | 0.00 | 0.00 | 0.00 | 296.28 | 673.11 | 0.30 | 404 | text/html | 29480 |
| Sydney | 0.00 | 0.00 | 0.00 | 315.12 | 209.26 | 0.39 | 404 | text/html | 29480 |
| Tokyo | 0.00 | 0.00 | 0.00 | 266.22 | 233.19 | 0.47 | 404 | text/html | 29480 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 119.40 | 340.85 | 0.26 | 404 | text/html | 29480 |

### GET `/_next/static/css/abf98b2abcdbd573.css` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 13.06 | 2.34 | 0.62 | 200 | text/css | 123936 |
| London | 0.00 | 0.00 | 0.00 | 55.39 | 4.65 | 0.80 | 200 | text/css | 123936 |
| San Francisco | 0.00 | 0.00 | 0.00 | 428.91 | 101.66 | 0.52 | 200 | text/css | 123936 |
| São Paulo | 0.00 | 0.00 | 0.00 | 298.37 | 372.38 | 0.62 | 200 | text/css | 123936 |
| Sydney | 0.00 | 0.00 | 0.00 | 408.18 | 327.44 | 0.71 | 200 | text/css | 123936 |
| Tokyo | 0.00 | 0.00 | 0.00 | 510.04 | 267.17 | 0.63 | 200 | text/css | 123936 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 298.74 | 26.06 | 0.66 | 200 | text/css | 123936 |

### GET `/_next/static/css/e771c44a50dae3b6.css` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 10.59 | 0.41 | 0.53 | 200 | text/css | 4004 |
| London | 0.00 | 0.00 | 0.00 | 46.91 | 0.35 | 0.72 | 200 | text/css | 4004 |
| San Francisco | 0.00 | 0.00 | 0.00 | 157.62 | 2.04 | 0.44 | 200 | text/css | 4004 |
| São Paulo | 0.00 | 0.00 | 0.00 | 229.54 | 0.50 | 0.53 | 200 | text/css | 4004 |
| Sydney | 0.00 | 0.00 | 0.00 | 296.60 | 0.47 | 0.61 | 200 | text/css | 4004 |
| Tokyo | 0.00 | 0.00 | 0.00 | 352.23 | 0.43 | 0.54 | 200 | text/css | 4004 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 129.86 | 0.46 | 0.59 | 200 | text/css | 4004 |

### GET `/_next/static/media/739c2d8941231bb4-s.p.woff2` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.08 | 0.89 | 0.84 | 200 | font/woff2 | 32752 |
| London | 0.00 | 0.00 | 0.00 | 47.88 | 7.35 | 1.18 | 200 | font/woff2 | 32752 |
| San Francisco | 0.00 | 0.00 | 0.00 | 402.13 | 85.35 | 0.81 | 200 | font/woff2 | 32752 |
| São Paulo | 0.00 | 0.00 | 0.00 | 257.07 | 277.62 | 0.87 | 200 | font/woff2 | 32752 |
| Sydney | 0.00 | 0.00 | 0.00 | 747.62 | 100.65 | 0.94 | 200 | font/woff2 | 32752 |
| Tokyo | 0.00 | 0.00 | 0.00 | 254.07 | 255.76 | 0.89 | 200 | font/woff2 | 32752 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 103.95 | 105.02 | 0.90 | 200 | font/woff2 | 32752 |

### GET `/_next/static/media/e4af272ccee01ff0-s.p.woff2` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 13.29 | 0.97 | 0.71 | 200 | font/woff2 | 48432 |
| London | 0.00 | 0.00 | 0.00 | 25.71 | 20.35 | 0.94 | 200 | font/woff2 | 48432 |
| San Francisco | 0.00 | 0.00 | 0.00 | 170.34 | 215.41 | 0.63 | 200 | font/woff2 | 48432 |
| São Paulo | 0.00 | 0.00 | 0.00 | 391.94 | 224.70 | 0.72 | 200 | font/woff2 | 48432 |
| Sydney | 0.00 | 0.00 | 0.00 | 320.32 | 328.14 | 0.86 | 200 | font/woff2 | 48432 |
| Tokyo | 0.00 | 0.00 | 0.00 | 520.94 | 194.40 | 0.74 | 200 | font/woff2 | 48432 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 215.39 | 83.14 | 0.73 | 200 | font/woff2 | 48432 |

Notes:
- Wait/TTFB climbs with distance from Frankfurt across all assets; static files re-use connections (DNS/connect/SSL at 0).
- Favicon requests consistently 404; health endpoint consistently 401 due to missing bearer token.

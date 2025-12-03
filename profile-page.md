## HAR summary: Without-CF-Proxy-Direct-DO-LB (`profile-page-*.json`)

Context:
- Tool: https://tools.pingdom.com/
- Source: `profile-page-*.json` (times in ms; content download = HAR `receive`)
- Hosting: DigitalOcean Frankfurt (Kubernetes) behind a DO load balancer with ingress-nginx
- Requests captured (29): profile page redirect chain plus Next.js assets and favicon
- Auth: `/en/profile` -> 307 to `/login?callbackUrl=/en/profile` -> 307 to `/en/login?callbackUrl=%2Fen%2Fprofile` (200 login page); no session token present.
- Tables include MIME type and response content size (bytes); Pingdom “performance grade” is not stored in these HARs.

Summary (per location):

| Location | Requests | Page size (KB) | Load time (s, `_fullyLoaded`) | Performance grade |
|---|---:|---:|---:|---|
| Frankfurt | 31 | 1369.84 | 1.361 | n/a |
| London | 29 | 1244.90 | 1.630 | n/a |
| San Francisco | 31 | 1369.84 | 2.968 | n/a |
| São Paulo | 31 | 1369.84 | 3.508 | n/a |
| Sydney | 31 | 1369.84 | 4.671 | n/a |
| Tokyo | 31 | 1369.84 | 4.032 | n/a |
| Washington, DC | 31 | 1369.84 | 4.361 | n/a |

### GET `/en/profile` (307)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 73.21 | 16.62 | 14.08 | 7.66 | 0.00 | 0.00 | 307 |  | 0 |
| London | 31.87 | 56.28 | 42.39 | 29.77 | 0.00 | 0.00 | 307 |  | 0 |
| San Francisco | 22.11 | 322.45 | 168.69 | 160.74 | 0.00 | 0.00 | 307 |  | 0 |
| São Paulo | 10.61 | 426.92 | 225.10 | 207.33 | 0.00 | 0.00 | 307 |  | 0 |
| Sydney | 48.87 | 593.41 | 305.43 | 298.70 | 0.00 | 0.00 | 307 |  | 0 |
| Tokyo | 5.23 | 488.07 | 249.73 | 251.33 | 0.00 | 0.00 | 307 |  | 0 |
| Washington, DC | 206.65 | 235.74 | 138.53 | 113.14 | 0.00 | 0.00 | 307 |  | 0 |

### GET `/login?callbackUrl=%2Fen%2Fprofile` (307)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 14.93 | 0.00 | 0.35 | 307 |  | 0 |
| London | 0.00 | 0.00 | 0.00 | 38.61 | 0.00 | 0.32 | 307 |  | 0 |
| San Francisco | 0.00 | 0.00 | 0.00 | 195.68 | 0.00 | 0.33 | 307 |  | 0 |
| São Paulo | 0.00 | 0.00 | 0.00 | 334.77 | 0.00 | 0.37 | 307 |  | 0 |
| Sydney | 0.00 | 0.00 | 0.00 | 309.87 | 0.00 | 0.32 | 307 |  | 0 |
| Tokyo | 0.00 | 0.00 | 0.00 | 254.72 | 0.00 | 0.42 | 307 |  | 0 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 171.42 | 0.00 | 0.33 | 307 |  | 0 |

### GET `/en/login?callbackUrl=%2Fen%2Fprofile` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 121.12 | 104.02 | 0.21 | 200 | text/html | 75808 |
| London | 0.00 | 0.00 | 0.00 | 259.14 | 682.18 | 0.35 | 200 | text/html | 75808 |
| San Francisco | 0.00 | 0.00 | 0.00 | 373.69 | 228.67 | 0.26 | 200 | text/html | 75808 |
| São Paulo | 0.00 | 0.00 | 0.00 | 393.11 | 201.61 | 0.30 | 200 | text/html | 75808 |
| Sydney | 0.00 | 0.00 | 0.00 | 433.66 | 328.57 | 0.27 | 200 | text/html | 75808 |
| Tokyo | 0.00 | 0.00 | 0.00 | 553.80 | 440.29 | 0.31 | 200 | text/html | 75808 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 585.28 | 2185.11 | 0.29 | 200 | text/html | 75808 |

### GET `/_next/static/media/739c2d8941231bb4-s.p.woff2` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 5.84 | 1.76 | 2.32 | 200 | font/woff2 | 32752 |
| London | 0.00 | 0.00 | 0.00 | 37.03 | 6.79 | 1.31 | 200 | font/woff2 | 32752 |
| San Francisco | 0.00 | 0.00 | 0.00 | 165.40 | 137.71 | 0.72 | 200 | font/woff2 | 32752 |
| São Paulo | 0.00 | 0.00 | 0.00 | 362.25 | 153.53 | 1.12 | 200 | font/woff2 | 32752 |
| Sydney | 0.00 | 0.00 | 0.00 | 741.28 | 116.35 | 0.75 | 200 | font/woff2 | 32752 |
| Tokyo | 0.00 | 0.00 | 0.00 | 535.93 | 154.04 | 1.06 | 200 | font/woff2 | 32752 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 254.21 | 47.86 | 1.23 | 200 | font/woff2 | 32752 |

### GET `/_next/static/media/e4af272ccee01ff0-s.p.woff2` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 6.71 | 4.05 | 3.91 | 200 | font/woff2 | 48432 |
| London | 0.00 | 0.00 | 0.00 | 18.01 | 18.49 | 1.12 | 200 | font/woff2 | 48432 |
| San Francisco | 0.00 | 0.00 | 0.00 | 311.90 | 133.30 | 0.63 | 200 | font/woff2 | 48432 |
| São Paulo | 0.00 | 0.00 | 0.00 | 216.29 | 246.96 | 1.27 | 200 | font/woff2 | 48432 |
| Sydney | 0.00 | 0.00 | 0.00 | 309.01 | 293.40 | 0.68 | 200 | font/woff2 | 48432 |
| Tokyo | 0.00 | 0.00 | 0.00 | 318.88 | 203.37 | 0.87 | 200 | font/woff2 | 48432 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 104.11 | 138.73 | 1.01 | 200 | font/woff2 | 48432 |

### GET `/_next/static/css/abf98b2abcdbd573.css` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 7.02 | 3.49 | 0.49 | 200 | text/css | 123936 |
| London | 0.00 | 0.00 | 0.00 | 44.22 | 4.01 | 1.01 | 200 | text/css | 123936 |
| San Francisco | 0.00 | 0.00 | 0.00 | 174.48 | 9.01 | 0.45 | 200 | text/css | 123936 |
| São Paulo | 0.00 | 0.00 | 0.00 | 208.39 | 12.65 | 0.50 | 200 | text/css | 123936 |
| Sydney | 0.00 | 0.00 | 0.00 | 299.45 | 16.91 | 0.50 | 200 | text/css | 123936 |
| Tokyo | 0.00 | 0.00 | 0.00 | 244.44 | 15.89 | 0.53 | 200 | text/css | 123936 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 103.41 | 8.57 | 0.63 | 200 | text/css | 123936 |

### GET `/_next/static/chunks/webpack-b80cd65c35b59642.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 88.55 | 0.82 | 4.98 | 200 | application/javascript | 43159 |
| London | 0.00 | 0.00 | 0.00 | 176.44 | 2.53 | 3.39 | 200 | application/javascript | 43159 |
| San Francisco | 0.00 | 0.00 | 0.00 | 386.16 | 74.17 | 0.17 | 200 | application/javascript | 43159 |
| São Paulo | 0.00 | 0.00 | 0.00 | 578.73 | 41.02 | 2.60 | 200 | application/javascript | 43159 |
| Sydney | 0.00 | 0.00 | 0.00 | 629.30 | 98.06 | 0.23 | 200 | application/javascript | 43159 |
| Tokyo | 0.00 | 0.00 | 0.00 | 704.28 | 38.89 | 1.66 | 200 | application/javascript | 43159 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 333.64 | 26.30 | 2.71 | 200 | application/javascript | 43159 |

### GET `/_next/static/css/e771c44a50dae3b6.css` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 6.30 | 0.35 | 0.28 | 200 | text/css | 4004 |
| London | 0.00 | 0.00 | 0.00 | 40.40 | 3.66 | 0.87 | 200 | text/css | 4004 |
| San Francisco | 0.00 | 0.00 | 0.00 | 183.65 | 0.27 | 0.28 | 200 | text/css | 4004 |
| São Paulo | 0.00 | 0.00 | 0.00 | 206.98 | 0.37 | 0.30 | 200 | text/css | 4004 |
| Sydney | 0.00 | 0.00 | 0.00 | 297.45 | 0.38 | 0.29 | 200 | text/css | 4004 |
| Tokyo | 0.00 | 0.00 | 0.00 | 242.57 | 0.39 | 0.33 | 200 | text/css | 4004 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 100.38 | 3.38 | 0.32 | 200 | text/css | 4004 |

### GET `/_next/static/media/authLogo.59ea595a.svg` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 6.38 | 0.38 | 0.30 | 200 | image/svg+xml | 16549 |
| London | 0.00 | 0.00 | 0.00 | 19.61 | 0.45 | 0.78 | 200 | image/svg+xml | 16549 |
| San Francisco | 0.00 | 0.00 | 0.00 | 159.82 | 2.08 | 0.28 | 200 | image/svg+xml | 16549 |
| São Paulo | 0.00 | 0.00 | 0.00 | 206.52 | 7.32 | 0.77 | 200 | image/svg+xml | 16549 |
| Sydney | 0.00 | 0.00 | 0.00 | 302.96 | 4.77 | 0.24 | 200 | image/svg+xml | 16549 |
| Tokyo | 0.00 | 0.00 | 0.00 | 242.39 | 7.59 | 0.56 | 200 | image/svg+xml | 16549 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 101.20 | 2.52 | 0.62 | 200 | image/svg+xml | 16549 |

### GET `/_next/static/chunks/app/%5Blocale%5D/(app)/layout-b4d9c5a0442100bf.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 8.33 | 0.47 | 0.43 | 200 | application/javascript | 20176 |
| London | 0.00 | 0.00 | 0.00 | 59.37 | 5.43 | 0.33 | 200 | application/javascript | 20176 |
| San Francisco | 0.00 | 0.00 | 0.00 | 158.68 | 4.23 | 0.56 | 200 | application/javascript | 20176 |
| São Paulo | 0.00 | 0.00 | 0.00 | 275.22 | 7.79 | 0.31 | 200 | application/javascript | 20176 |
| Sydney | 0.00 | 0.00 | 0.00 | 307.49 | 3.81 | 0.53 | 200 | application/javascript | 20176 |
| Tokyo | 0.00 | 0.00 | 0.00 | 295.10 | 2.97 | 0.28 | 200 | application/javascript | 20176 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 114.49 | 1.50 | 0.33 | 200 | application/javascript | 20176 |

### GET `/_next/static/chunks/40867-24b106b5648edbf1.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 8.03 | 1.16 | 0.44 | 200 | application/javascript | 31882 |
| London | 0.00 | 0.00 | 0.00 | 111.47 | 0.58 | 0.71 | 200 | application/javascript | 31882 |
| San Francisco | 0.00 | 0.00 | 0.00 | 445.58 | 104.52 | 0.58 | 200 | application/javascript | 31882 |
| São Paulo | 0.00 | 0.00 | 0.00 | 220.44 | 3.36 | 0.58 | 200 | application/javascript | 31882 |
| Sydney | 0.00 | 0.00 | 0.00 | 339.23 | 7.53 | 0.56 | 200 | application/javascript | 31882 |
| Tokyo | 0.00 | 0.00 | 0.00 | 286.68 | 8.78 | 0.29 | 200 | application/javascript | 31882 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 121.45 | 5.04 | 0.30 | 200 | application/javascript | 31882 |

### GET `/_next/static/chunks/main-app-3267ec133fe45348.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.64 | 0.24 | 0.48 | 200 | application/javascript | 572 |
| London | 0.00 | 0.00 | 0.00 | 17.17 | 0.91 | 0.59 | 200 | application/javascript | 572 |
| San Francisco | 0.00 | 0.00 | 0.00 | 158.04 | 0.29 | 0.63 | 200 | application/javascript | 572 |
| São Paulo | 0.00 | 0.00 | 0.00 | 206.84 | 0.44 | 0.63 | 200 | application/javascript | 572 |
| Sydney | 0.00 | 0.00 | 0.00 | 301.13 | 0.35 | 0.59 | 200 | application/javascript | 572 |
| Tokyo | 0.00 | 0.00 | 0.00 | 242.72 | 0.38 | 0.44 | 200 | application/javascript | 572 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 103.97 | 1.36 | 0.47 | 200 | application/javascript | 572 |

### GET `/_next/static/chunks/65264-dc11e68888cdad2a.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.40 | 10.50 | 0.54 | 200 | application/javascript | 172276 |
| London | 0.00 | 0.00 | 0.00 | 18.81 | 8.87 | 0.56 | 200 | application/javascript | 172276 |
| San Francisco | 0.00 | 0.00 | 0.00 | 163.07 | 54.12 | 0.66 | 200 | application/javascript | 172276 |
| São Paulo | 0.00 | 0.00 | 0.00 | 226.90 | 65.41 | 0.66 | 200 | application/javascript | 172276 |
| Sydney | 0.00 | 0.00 | 0.00 | 401.35 | 62.02 | 0.62 | 200 | application/javascript | 172276 |
| Tokyo | 0.00 | 0.00 | 0.00 | 322.65 | 49.29 | 0.46 | 200 | application/javascript | 172276 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 117.48 | 35.85 | 0.50 | 200 | application/javascript | 172276 |

### GET `/_next/static/chunks/app/%5Blocale%5D/loading-98f017f93adc0ad2.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 14.22 | 0.47 | 0.48 | 200 | application/javascript | 4659 |
| London | 0.00 | 0.00 | 0.00 | 18.42 | 3.86 | 0.54 | 200 | application/javascript | 4659 |
| San Francisco | 0.00 | 0.00 | 0.00 | 175.74 | 0.31 | 0.29 | 200 | application/javascript | 4659 |
| São Paulo | 0.00 | 0.00 | 0.00 | 221.53 | 0.31 | 0.21 | 200 | application/javascript | 4659 |
| Sydney | 0.00 | 0.00 | 0.00 | 302.38 | 0.29 | 0.25 | 200 | application/javascript | 4659 |
| Tokyo | 0.00 | 0.00 | 0.00 | 241.94 | 0.33 | 0.26 | 200 | application/javascript | 4659 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 102.60 | 0.40 | 0.29 | 200 | application/javascript | 4659 |

### GET `/_next/static/chunks/43423-49ad8b8120df9a57.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 15.45 | 0.34 | 0.50 | 200 | application/javascript | 25366 |
| London | 0.00 | 0.00 | 0.00 | 18.92 | 4.12 | 0.47 | 200 | application/javascript | 25366 |
| San Francisco | 0.00 | 0.00 | 0.00 | 157.75 | 5.07 | 0.52 | 200 | application/javascript | 25366 |
| São Paulo | 0.00 | 0.00 | 0.00 | 221.31 | 7.80 | 0.22 | 200 | application/javascript | 25366 |
| Sydney | 0.00 | 0.00 | 0.00 | 303.88 | 5.50 | 0.24 | 200 | application/javascript | 25366 |
| Tokyo | 0.00 | 0.00 | 0.00 | 263.33 | 3.10 | 0.23 | 200 | application/javascript | 25366 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 110.97 | 3.16 | 0.21 | 200 | application/javascript | 25366 |

### GET `/_next/static/chunks/87524-df2a52a55c85cce2.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.43 | 1.13 | 0.27 | 200 | application/javascript | 48368 |
| London | 0.00 | 0.00 | 0.00 | 33.37 | 4.22 | 0.36 | 200 | application/javascript | 48368 |
| San Francisco | 0.00 | 0.00 | 0.00 | 159.91 | 8.94 | 0.27 | 200 | application/javascript | 48368 |
| São Paulo | 0.00 | 0.00 | 0.00 | 223.22 | 8.91 | 0.32 | 200 | application/javascript | 48368 |
| Sydney | 0.00 | 0.00 | 0.00 | 321.21 | 15.74 | 0.32 | 200 | application/javascript | 48368 |
| Tokyo | 0.00 | 0.00 | 0.00 | 264.05 | 7.41 | 0.23 | 200 | application/javascript | 48368 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 107.59 | 3.99 | 0.31 | 200 | application/javascript | 48368 |

### GET `/_next/static/chunks/38874-526f584e6aadcd4b.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 6.50 | 0.35 | 0.18 | 200 | application/javascript | 8565 |
| London | 0.00 | 0.00 | 0.00 | 36.76 | 0.44 | 0.26 | 200 | application/javascript | 8565 |
| San Francisco | 0.00 | 0.00 | 0.00 | 332.85 | 6.73 | 0.35 | 200 | application/javascript | 8565 |
| São Paulo | 0.00 | 0.00 | 0.00 | 206.12 | 0.31 | 0.28 | 200 | application/javascript | 8565 |
| Sydney | 0.00 | 0.00 | 0.00 | 301.50 | 1.25 | 0.24 | 200 | application/javascript | 8565 |
| Tokyo | 0.00 | 0.00 | 0.00 | 242.59 | 0.34 | 0.22 | 200 | application/javascript | 8565 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 102.17 | 0.36 | 0.23 | 200 | application/javascript | 8565 |

### GET `/_next/static/chunks/app/%5Blocale%5D/layout-df215d4a79c4add9.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 54.39 | 0.41 | 0.27 | 200 | application/javascript | 10734 |
| London | 0.00 | 0.00 | 0.00 | 29.07 | 4.04 | 0.25 | 200 | application/javascript | 10734 |
| San Francisco | 0.00 | 0.00 | 0.00 | 158.01 | 0.88 | 0.22 | 200 | application/javascript | 10734 |
| São Paulo | 0.00 | 0.00 | 0.00 | 206.89 | 0.42 | 0.31 | 200 | application/javascript | 10734 |
| Sydney | 0.00 | 0.00 | 0.00 | 310.42 | 1.15 | 0.28 | 200 | application/javascript | 10734 |
| Tokyo | 0.00 | 0.00 | 0.00 | 243.02 | 0.51 | 0.30 | 200 | application/javascript | 10734 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 102.83 | 0.51 | 1.57 | 200 | application/javascript | 10734 |

### GET `/_next/static/chunks/2065e367-738d69ba223595b9.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 15.01 | 75.23 | 0.43 | 200 | application/javascript | 157100 |
| London | 0.00 | 0.00 | 0.00 | 60.78 | 186.02 | 0.37 | 200 | application/javascript | 157100 |
| San Francisco | 0.00 | 0.00 | 0.00 | 333.67 | 186.18 | 0.30 | 200 | application/javascript | 157100 |
| São Paulo | 0.00 | 0.00 | 0.00 | 210.64 | 39.74 | 0.26 | 200 | application/javascript | 157100 |
| Sydney | 0.00 | 0.00 | 0.00 | 304.69 | 67.57 | 0.27 | 200 | application/javascript | 157100 |
| Tokyo | 0.00 | 0.00 | 0.00 | 253.11 | 58.34 | 0.22 | 200 | application/javascript | 157100 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 106.08 | 23.59 | 1.51 | 200 | application/javascript | 157100 |

### GET `/_next/static/chunks/75245-4381628e6d93ed7c.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 59.90 | 2.67 | 0.20 | 200 | application/javascript | 83664 |
| London | 0.00 | 0.00 | 0.00 | 176.72 | 8.28 | 0.27 | 200 | application/javascript | 83664 |
| San Francisco | 0.00 | 0.00 | 0.00 | 167.97 | 14.57 | 0.61 | 200 | application/javascript | 83664 |
| São Paulo | 0.00 | 0.00 | 0.00 | 207.78 | 13.74 | 0.25 | 200 | application/javascript | 83664 |
| Sydney | 0.00 | 0.00 | 0.00 | 301.93 | 16.98 | 0.22 | 200 | application/javascript | 83664 |
| Tokyo | 0.00 | 0.00 | 0.00 | 248.00 | 13.13 | 0.27 | 200 | application/javascript | 83664 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 104.75 | 6.92 | 0.44 | 200 | application/javascript | 83664 |

### GET `/_next/static/chunks/28381-f69fef083c6248e7.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 7.60 | 0.39 | 0.25 | 200 | application/javascript | 23076 |
| London | 0.00 | 0.00 | 0.00 | 22.24 | 0.55 | 0.34 | 200 | application/javascript | 23076 |
| San Francisco | 0.00 | 0.00 | 0.00 | 166.28 | 8.78 | 0.23 | 200 | application/javascript | 23076 |
| São Paulo | 0.00 | 0.00 | 0.00 | 206.29 | 2.55 | 0.26 | 200 | application/javascript | 23076 |
| Sydney | 0.00 | 0.00 | 0.00 | 303.02 | 3.27 | 0.23 | 200 | application/javascript | 23076 |
| Tokyo | 0.00 | 0.00 | 0.00 | 243.23 | 3.00 | 0.23 | 200 | application/javascript | 23076 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 108.25 | 1.12 | 0.23 | 200 | application/javascript | 23076 |

### GET `/_next/static/chunks/28214-f7bd4fbe2e13f9bd.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 8.15 | 0.33 | 0.34 | 200 | application/javascript | 11457 |
| London | 0.00 | 0.00 | 0.00 | 19.34 | 3.76 | 0.49 | 200 | application/javascript | 11457 |
| San Francisco | 0.00 | 0.00 | 0.00 | 206.37 | 0.33 | 0.26 | 200 | application/javascript | 11457 |
| São Paulo | 0.00 | 0.00 | 0.00 | 206.05 | 0.92 | 0.25 | 200 | application/javascript | 11457 |
| Sydney | 0.00 | 0.00 | 0.00 | 303.26 | 0.33 | 0.23 | 200 | application/javascript | 11457 |
| Tokyo | 0.00 | 0.00 | 0.00 | 246.69 | 0.33 | 0.20 | 200 | application/javascript | 11457 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 102.98 | 0.72 | 0.25 | 200 | application/javascript | 11457 |

### GET `/_next/static/chunks/app/%5Blocale%5D/(auth)/login/page-db91e715f9db634b.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 84.82 | 0.46 | 0.43 | 200 | application/javascript | 6428 |
| London | 0.00 | 0.00 | 0.00 | 29.37 | 0.66 | 0.26 | 200 | application/javascript | 6428 |
| San Francisco | 0.00 | 0.00 | 0.00 | 160.36 | 0.33 | 0.20 | 200 | application/javascript | 6428 |
| São Paulo | 0.00 | 0.00 | 0.00 | 206.94 | 0.37 | 0.31 | 200 | application/javascript | 6428 |
| Sydney | 0.00 | 0.00 | 0.00 | 303.87 | 0.36 | 0.26 | 200 | application/javascript | 6428 |
| Tokyo | 0.00 | 0.00 | 0.00 | 291.83 | 1.07 | 0.34 | 200 | application/javascript | 6428 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 102.14 | 0.44 | 0.98 | 200 | application/javascript | 6428 |

### GET `/_next/static/chunks/ad6b4c6d-bd23cbb78334428b.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 91.03 | 111.13 | 0.65 | 200 | application/javascript | 173026 |
| London | 0.00 | 0.00 | 0.00 | 21.32 | 40.39 | 0.65 | 200 | application/javascript | 173026 |
| San Francisco | 0.00 | 0.00 | 0.00 | 164.84 | 68.13 | 0.72 | 200 | application/javascript | 173026 |
| São Paulo | 0.00 | 0.00 | 0.00 | 224.00 | 97.33 | 0.70 | 200 | application/javascript | 173026 |
| Sydney | 0.00 | 0.00 | 0.00 | 303.39 | 97.74 | 0.69 | 200 | application/javascript | 173026 |
| Tokyo | 0.00 | 0.00 | 0.00 | 250.17 | 60.67 | 0.50 | 200 | application/javascript | 173026 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 105.50 | 34.69 | 0.54 | 200 | application/javascript | 173026 |

### GET `/_next/static/chunks/72283-44c31ff2dbd0a071.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 179.65 | 1.56 | 0.78 | 200 | application/javascript | 33960 |
| London | 0.00 | 0.00 | 0.00 | 33.53 | 0.87 | 1.13 | 200 | application/javascript | 33960 |
| San Francisco | 0.00 | 0.00 | 0.00 | 161.38 | 8.24 | 0.24 | 200 | application/javascript | 33960 |
| São Paulo | 0.00 | 0.00 | 0.00 | 224.81 | 6.46 | 0.22 | 200 | application/javascript | 33960 |
| Sydney | 0.00 | 0.00 | 0.00 | 304.54 | 6.85 | 0.30 | 200 | application/javascript | 33960 |
| Tokyo | 0.00 | 0.00 | 0.00 | 270.33 | 4.81 | 0.26 | 200 | application/javascript | 33960 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 107.83 | 2.06 | 0.32 | 200 | application/javascript | 33960 |

### GET `/_next/static/chunks/app/%5Blocale%5D/error-c58756f7ba7b9f2b.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 125.50 | 4.15 | 0.37 | 200 | application/javascript | 10308 |
| London | 0.00 | 0.00 | 0.00 | 123.46 | 2.74 | 0.35 | 200 | application/javascript | 10308 |
| San Francisco | 0.00 | 0.00 | 0.00 | 166.66 | 0.37 | 0.23 | 200 | application/javascript | 10308 |
| São Paulo | 0.00 | 0.00 | 0.00 | 206.75 | 0.31 | 0.20 | 200 | application/javascript | 10308 |
| Sydney | 0.00 | 0.00 | 0.00 | 302.56 | 0.33 | 0.19 | 200 | application/javascript | 10308 |
| Tokyo | 0.00 | 0.00 | 0.00 | 243.44 | 1.09 | 0.25 | 200 | application/javascript | 10308 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 103.74 | 0.47 | 0.38 | 200 | application/javascript | 10308 |

### GET `/_next/static/chunks/0f9dcbb3-4ea2e6533b43a41b.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 191.88 | 95.95 | 0.19 | 200 | application/javascript | 69536 |
| London | 0.00 | 0.00 | 0.00 | 66.63 | 59.86 | 0.36 | 200 | application/javascript | 69536 |
| San Francisco | 0.00 | 0.00 | 0.00 | 160.30 | 20.15 | 0.24 | 200 | application/javascript | 69536 |
| São Paulo | 0.00 | 0.00 | 0.00 | 208.50 | 19.08 | 0.26 | 200 | application/javascript | 69536 |
| Sydney | 0.00 | 0.00 | 0.00 | 302.16 | 28.96 | 0.26 | 200 | application/javascript | 69536 |
| Tokyo | 0.00 | 0.00 | 0.00 | 243.50 | 21.00 | 0.30 | 200 | application/javascript | 69536 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 102.27 | 9.78 | 0.29 | 200 | application/javascript | 69536 |

### GET `/_next/static/chunks/28743-4a3deeebaf794acf.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 124.62 | 86.05 | 0.22 | 200 | application/javascript | 9506 |
| London | 0.00 | 0.00 | 0.00 | 56.93 | 0.39 | 0.96 | 200 | application/javascript | 9506 |
| San Francisco | 0.00 | 0.00 | 0.00 | 197.93 | 0.35 | 0.26 | 200 | application/javascript | 9506 |
| São Paulo | 0.00 | 0.00 | 0.00 | 208.19 | 0.87 | 0.26 | 200 | application/javascript | 9506 |
| Sydney | 0.00 | 0.00 | 0.00 | 305.45 | 0.35 | 0.21 | 200 | application/javascript | 9506 |
| Tokyo | 0.00 | 0.00 | 0.00 | 249.48 | 0.45 | 0.26 | 200 | application/javascript | 9506 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 104.20 | 1.04 | 0.35 | 200 | application/javascript | 9506 |

### GET `/favicon.ico` (404)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Frankfurt | 0.00 | 0.00 | 0.00 | 296.63 | 313.44 | 0.21 | 404 | text/html | 29480 |
| London | 0.00 | 0.00 | 0.00 | 128.99 | 392.05 | 0.31 | 404 | text/html | 29480 |
| San Francisco | 0.00 | 0.00 | 0.00 | 236.14 | 203.20 | 0.20 | 404 | text/html | 29480 |
| São Paulo | 0.00 | 0.00 | 0.00 | 286.53 | 296.72 | 0.20 | 404 | text/html | 29480 |
| Sydney | 0.00 | 0.00 | 0.00 | 424.20 | 299.44 | 0.23 | 404 | text/html | 29480 |
| Tokyo | 0.00 | 0.00 | 0.00 | 262.61 | 289.30 | 0.21 | 404 | text/html | 29480 |
| Washington, DC | 0.00 | 0.00 | 0.00 | 174.52 | 303.79 | 0.22 | 404 | text/html | 29480 |

Notes:
- `/en/profile` redirects to login because no session token; final `/en/login?callbackUrl=%2Fen%2Fprofile` serves the login page (200).
- Wait/TTFB rises with distance from Frankfurt; most assets reuse existing connections (DNS/connect/SSL = 0).
- `favicon.ico` consistently returns 404.

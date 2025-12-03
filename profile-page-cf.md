## HAR summary: With-CF-Proxy (`profile-page-*.json`)

Context:
- Tool: https://tools.pingdom.com/
- Source: `profile-page-*.json` (times in ms; content download = HAR `receive`)
- CF proxy enabled in front of DigitalOcean Frankfurt (Kubernetes, DO LB + ingress-nginx).
- Requests include profile redirect chain, Next.js assets, favicon, and Cloudflare challenge/telemetry files.
- Auth: unauthenticated -> redirects to login (200 login page); no session token present.
- Tables include MIME type, response size (bytes), cf-ray; `—` indicates the request is absent. Performance grade is not present in these HARs.

Summary (per location):

| Location | Requests | Page size (KB) | Load time (s, `_fullyLoaded`) | CF-ray (edge) | Performance grade |
|---|---:|---:|---:|---|---|
| Frankfurt | 34 | 1380.48 | 1.105 | FRA | n/a |
| London | 34 | 1380.67 | 3.602 | LHR | n/a |
| San Francisco | 36 | 1400.64 | 3.410 | SJC | n/a |
| São Paulo | 34 | 1275.52 | 3.579 | GRU | n/a |
| Sydney | 36 | 1400.57 | 4.401 | SYD | n/a |
| Tokyo | 36 | 1400.40 | 4.313 | NRT | n/a |
| Washington, DC | 34 | 1275.57 | 1.719 | IAD | n/a |

### GET `/en/profile` (307)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 26.62 | 14.43 | 12.92 | 51.25 | 0.00 | 0.00 | 307 |  | 0 | 9a8422779a8adc58-FRA |
| London | 11.59 | 26.85 | 25.05 | 105.48 | 0.00 | 0.00 | 307 |  | 0 | 9a8450fbfba96412-LHR |
| San Francisco | 4.74 | 18.12 | 16.62 | 630.23 | 0.00 | 0.00 | 307 |  | 0 | 9a845fcc9d45cb6f-SJC |
| São Paulo | 4.51 | 19.83 | 16.07 | 769.88 | 0.00 | 0.00 | 307 |  | 0 | 9a8463608a502788-GRU |
| Sydney | 49.56 | 15.39 | 13.97 | 1291.14 | 0.00 | 0.00 | 307 |  | 0 | 9a8461344aa2a959-SYD |
| Tokyo | 5.44 | 17.76 | 15.98 | 982.23 | 0.00 | 0.00 | 307 |  | 0 | 9a841d73ff40e382-NRT |
| Washington, DC | 96.13 | 14.85 | 13.17 | 434.02 | 0.00 | 0.00 | 307 |  | 0 | 9a845e840bf68c9d-IAD |

### GET `/login?callbackUrl=%2Fen%2Fprofile` (307)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 35.44 | 0.00 | 0.29 | 307 |  | 0 | 9a842277eb30dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 50.01 | 0.00 | 0.33 | 307 |  | 0 | 9a8450fcac176412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 693.02 | 0.00 | 0.30 | 307 |  | 0 | 9a845fd08bbdcb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 718.49 | 0.00 | 0.30 | 307 |  | 0 | 9a8463655b992788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 344.18 | 0.00 | 0.30 | 307 |  | 0 | 9a84613c5dc6a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 929.83 | 0.00 | 0.43 | 307 |  | 0 | 9a841d7a2cf9e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 129.69 | 0.00 | 0.30 | 307 |  | 0 | 9a845e86bcf98c9d-IAD |

### GET `/_next/static/css/e771c44a50dae3b6.css` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 0.09 | 0.35 | 0.51 | 200 | text/css | 4004 | 9a84227d0f71dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 0.12 | 0.37 | 0.50 | 200 | text/css | 4004 | 9a8451118c7a6412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 0.11 | 0.38 | 0.40 | 200 | text/css | 4004 | 9a845fe08fffcb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 0.08 | 0.35 | 0.79 | 200 | text/css | 4004 | 9a84636c5fd82788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 0.07 | 0.28 | 0.47 | 200 | text/css | 4004 | 9a84614ebc8aa959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 0.08 | 0.41 | 1.21 | 200 | text/css | 4004 | 9a841d8d9896e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 0.09 | 0.37 | 0.87 | 200 | text/css | 4004 | 9a845e8a68648c9d-IAD |

### GET `/_next/static/css/abf98b2abcdbd573.css` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 0.08 | 0.90 | 0.70 | 200 | text/css | 123936 | 9a84227d0f70dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 0.11 | 1.11 | 0.72 | 200 | text/css | 123936 | 9a8451118c796412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 0.11 | 0.99 | 0.62 | 200 | text/css | 123936 | 9a845fe08ffecb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 0.11 | 1.06 | 0.71 | 200 | text/css | 123936 | 9a84636c5fd52788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 0.11 | 1.50 | 0.68 | 200 | text/css | 123936 | 9a84614ebc88a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 0.09 | 1.64 | 0.67 | 200 | text/css | 123936 | 9a841d8d9893e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 0.09 | 1.38 | 1.01 | 200 | text/css | 123936 | 9a845e8a68608c9d-IAD |

### GET `/_next/static/media/739c2d8941231bb4-s.p.woff2` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 4.39 | 0.59 | 1.16 | 200 | font/woff2 | 32752 | 9a84227a1849dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 39.04 | 1.45 | 1.23 | 200 | font/woff2 | 32752 | 9a8450fe2d846412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 169.27 | 6.53 | 0.80 | 200 | font/woff2 | 32752 | 9a845fd6deedcb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 209.68 | 0.41 | 1.03 | 200 | font/woff2 | 32752 | 9a84636c6fed2788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 301.73 | 0.84 | 1.12 | 200 | font/woff2 | 32752 | 9a8461424fd4a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 255.14 | 0.55 | 1.03 | 200 | font/woff2 | 32752 | 9a841d82b810e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 17.15 | 0.83 | 1.12 | 200 | font/woff2 | 32752 | 9a845e8a788a8c9d-IAD |

### GET `/_next/static/media/e4af272ccee01ff0-s.p.woff2` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 5.51 | 0.88 | 1.01 | 200 | font/woff2 | 48432 | 9a84227a184adc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 30.80 | 0.95 | 1.04 | 200 | font/woff2 | 48432 | 9a8450fe2d876412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 183.46 | 1.41 | 0.67 | 200 | font/woff2 | 48432 | 9a845fd6deefcb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 207.87 | 0.63 | 0.85 | 200 | font/woff2 | 48432 | 9a84636c6fee2788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 300.36 | 2.59 | 1.25 | 200 | font/woff2 | 48432 | 9a8461424fd5a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 245.44 | 5.31 | 0.86 | 200 | font/woff2 | 48432 | 9a841d82b819e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 13.20 | 0.67 | 1.10 | 200 | font/woff2 | 48432 | 9a845e8a788c8c9d-IAD |

### GET `/_next/static/chunks/webpack-b80cd65c35b59642.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 8.49 | 0.76 | 4.97 | 200 | application/javascript | 43159 | 9a84227a1856dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 36.87 | 1.24 | 0.57 | 200 | application/javascript | 43159 | 9a8450fe2d886412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 177.47 | 3.40 | 0.20 | 200 | application/javascript | 43159 | 9a845fd6def2cb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 211.06 | 36.93 | 0.33 | 200 | application/javascript | 43159 | 9a84636c6ff12788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 302.97 | 0.65 | 2.84 | 200 | application/javascript | 43159 | 9a8461424fd6a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 249.14 | 1.12 | 0.86 | 200 | application/javascript | 43159 | 9a841d82c824e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 12.64 | 0.98 | 1.65 | 200 | application/javascript | 43159 | 9a845e8a88a18c9d-IAD |

### GET `/_next/static/media/authLogo.59ea595a.svg` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.66 | 0.35 | 0.29 | 200 | image/svg+xml | 16549 | 9a84227a1858dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 40.13 | 0.60 | 0.62 | 200 | image/svg+xml | 16549 | 9a8450fe6daf6412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 202.77 | 1.60 | 1.51 | 200 | image/svg+xml | 16549 | 9a845fd7f931cb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 209.99 | 0.51 | 0.58 | 200 | image/svg+xml | 16549 | 9a84636daac72788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 303.40 | 0.50 | 0.26 | 200 | image/svg+xml | 16549 | 9a846144386fa959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 240.39 | 0.56 | 0.57 | 200 | image/svg+xml | 16549 | 9a841d844bf4e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 13.26 | 0.94 | 0.41 | 200 | image/svg+xml | 16549 | 9a845e8a88bc8c9d-IAD |

### GET `/_next/static/chunks/ad6b4c6d-bd23cbb78334428b.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 7.60 | 3.91 | 0.25 | 200 | application/javascript | 173026 | 9a84227a1859dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 60.59 | 18.60 | 0.55 | 200 | application/javascript | 173026 | 9a8450fe6db36412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 185.94 | 4.17 | 1.46 | 200 | application/javascript | 173026 | 9a845fd7f932cb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 210.78 | 14.40 | 0.52 | 200 | application/javascript | 173026 | 9a84636daacc2788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 312.19 | 4.97 | 0.86 | 200 | application/javascript | 173026 | 9a8461443872a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 241.41 | 2.23 | 0.54 | 200 | application/javascript | 173026 | 9a841d844bfae382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 14.49 | 1.87 | 0.34 | 200 | application/javascript | 173026 | 9a845e8a88bf8c9d-IAD |

### GET `/_next/static/chunks/main-app-3267ec133fe45348.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.43 | 0.29 | 0.17 | 200 | application/javascript | 572 | 9a84227a2871dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 35.19 | 0.55 | 0.85 | 200 | application/javascript | 572 | 9a8450fe6dba6412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 179.55 | 0.32 | 1.57 | 200 | application/javascript | 572 | 9a845fd7f934cb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 212.57 | 0.34 | 0.28 | 200 | application/javascript | 572 | 9a84636dbad62788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 313.42 | 0.28 | 0.90 | 200 | application/javascript | 572 | 9a8461443876a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 241.58 | 3.14 | 0.34 | 200 | application/javascript | 572 | 9a841d844c15e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 12.49 | 0.29 | 0.27 | 200 | application/javascript | 572 | 9a845e8a98f48c9d-IAD |

### GET `/_next/static/chunks/65264-dc11e68888cdad2a.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 8.96 | 2.14 | 0.84 | 200 | application/javascript | 172276 | 9a84227a286edc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 32.30 | 1.87 | 0.54 | 200 | application/javascript | 172276 | 9a8450fe6db46412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 505.16 | 172.23 | 1.57 | 200 | application/javascript | 172276 | 9a845fd7f933cb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 211.56 | 6.21 | 0.50 | 200 | application/javascript | 172276 | 9a84636daacd2788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 314.00 | 3.38 | 0.92 | 200 | application/javascript | 172276 | 9a8461443874a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 247.76 | 3.76 | 0.51 | 200 | application/javascript | 172276 | 9a841d844bfbe382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 13.54 | 2.14 | 0.19 | 200 | application/javascript | 172276 | 9a845e8a98e28c9d-IAD |

### GET `/_next/static/chunks/app/%5Blocale%5D/(app)/layout-b4d9c5a0442100bf.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 7.26 | 0.45 | 0.93 | 200 | application/javascript | 20176 | 9a84227a3888dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 43.68 | 0.52 | 0.32 | 200 | application/javascript | 20176 | 9a8450fe9de56412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 169.35 | 0.51 | 0.23 | 200 | application/javascript | 20176 | 9a845fd7f939cb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 214.04 | 0.43 | 0.30 | 200 | application/javascript | 20176 | 9a84636dfb432788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 320.54 | 0.78 | 0.84 | 200 | application/javascript | 20176 | 9a8461443878a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 255.66 | 1.11 | 0.33 | 200 | application/javascript | 20176 | 9a841d845c27e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 12.64 | 2.69 | 1.25 | 200 | application/javascript | 20176 | 9a845e8aa9148c9d-IAD |

### GET `/_next/static/chunks/40867-24b106b5648edbf1.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 7.96 | 0.42 | 1.12 | 200 | application/javascript | 31882 | 9a84227a3886dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 43.27 | 0.51 | 0.38 | 200 | application/javascript | 31882 | 9a8450fe7dbc6412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 180.23 | 1.51 | 1.55 | 200 | application/javascript | 31882 | 9a845fd7f936cb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 213.81 | 0.52 | 0.23 | 200 | application/javascript | 31882 | 9a84636dbadd2788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 310.96 | 0.86 | 0.87 | 200 | application/javascript | 31882 | 9a8461443877a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 245.17 | 0.50 | 0.33 | 200 | application/javascript | 31882 | 9a841d845c18e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 11.15 | 0.94 | 0.20 | 200 | application/javascript | 31882 | 9a845e8a98f78c9d-IAD |

### GET `/en/login?callbackUrl=%2Fen%2Fprofile` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 303.50 | 35.58 | 0.27 | 200 | text/html | 76727 | 9a8422782bfcdc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 188.32 | 2781.79 | 0.28 | 200 | text/html | 76727 | 9a8450fcfc5c6412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 303.25 | 132.37 | 0.31 | 200 | text/html | 77231 | 9a845fd4eb3dcb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 401.53 | 127.09 | 0.31 | 200 | text/html | 77231 | 9a846369db3f2788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 597.34 | 131.27 | 0.26 | 200 | text/html | 77231 | 9a84613e8e87a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 440.30 | 134.16 | 0.28 | 200 | text/html | 77188 | 9a841d7ff9ace382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 460.66 | 93.39 | 0.33 | 200 | text/html | 77231 | 9a845e879fb08c9d-IAD |

### GET `/_next/static/chunks/43423-49ad8b8120df9a57.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 8.47 | 0.47 | 0.73 | 200 | application/javascript | 25366 | 9a84227a38a0dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 32.75 | 0.81 | 0.34 | 200 | application/javascript | 25366 | 9a8450feadfb6412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 185.62 | 0.85 | 0.47 | 200 | application/javascript | 25366 | 9a845fd91b45cb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 211.40 | 0.46 | 1.23 | 200 | application/javascript | 25366 | 9a84636f0d4c2788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 313.35 | 0.48 | 3.80 | 200 | application/javascript | 25366 | 9a846146393aa959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 684.84 | 1.91 | 0.28 | 200 | application/javascript | 25366 | 9a841d85cf50e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 16.63 | 0.57 | 1.11 | 200 | application/javascript | 25366 | 9a845e8aa9418c9d-IAD |

### GET `/_next/static/chunks/app/%5Blocale%5D/loading-98f017f93adc0ad2.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 8.96 | 0.23 | 0.20 | 200 | application/javascript | 4659 | 9a84227a38a4dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 32.64 | 0.48 | 0.25 | 200 | application/javascript | 4659 | 9a8450febe066412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 175.34 | 0.36 | 0.22 | 200 | application/javascript | 4659 | 9a845fd91b4acb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 212.01 | 0.33 | 0.22 | 200 | application/javascript | 4659 | 9a84636f0d4e2788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 316.34 | 0.31 | 2.35 | 200 | application/javascript | 4659 | 9a846146393ba959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 249.15 | 0.34 | 0.19 | 200 | application/javascript | 4659 | 9a841d85df7de382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 15.71 | 0.46 | 0.36 | 200 | application/javascript | 4659 | 9a845e8aa9428c9d-IAD |

### GET `/_next/static/chunks/0f9dcbb3-4ea2e6533b43a41b.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 11.12 | 2.15 | 0.50 | 200 | application/javascript | 69536 | 9a84227a388edc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 34.42 | 2.45 | 0.43 | 200 | application/javascript | 69536 | 9a8450feadf86412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 173.90 | 1.01 | 0.32 | 200 | application/javascript | 69536 | 9a845fd90b24cb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 208.42 | 1.73 | 0.24 | 200 | application/javascript | 69536 | 9a84636efd3b2788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 307.71 | 1.05 | 0.25 | 200 | application/javascript | 69536 | 9a846146192ea959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 255.88 | 1.01 | 1.39 | 200 | application/javascript | 69536 | 9a841d85cf4de382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 11.33 | 1.51 | 0.17 | 200 | application/javascript | 69536 | 9a845e8aa9188c9d-IAD |

### GET `/_next/static/chunks/87524-df2a52a55c85cce2.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.77 | 0.87 | 0.38 | 200 | application/javascript | 48368 | 9a84227a38b4dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 32.82 | 2.30 | 1.39 | 200 | application/javascript | 48368 | 9a8450feee226412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 185.40 | 0.70 | 0.18 | 200 | application/javascript | 48368 | 9a845fd93b9fcb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 208.31 | 4.41 | 0.20 | 200 | application/javascript | 48368 | 9a84636f1d622788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 300.83 | 0.67 | 0.31 | 200 | application/javascript | 48368 | 9a846146393ea959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 240.10 | 0.72 | 0.17 | 200 | application/javascript | 48368 | 9a841d85df8de382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 15.34 | 1.18 | 0.27 | 200 | application/javascript | 48368 | 9a845e8ab96a8c9d-IAD |

### GET `/_next/static/chunks/2065e367-738d69ba223595b9.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 8.89 | 2.28 | 0.43 | 200 | application/javascript | 157100 | 9a84227a38b1dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 44.48 | 2.61 | 2.62 | 200 | application/javascript | 157100 | 9a8450feee1e6412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 171.48 | 8.13 | 0.20 | 200 | application/javascript | 157100 | 9a845fd92b5dcb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 210.95 | 2.14 | 0.36 | 200 | application/javascript | 157100 | 9a84636f0d522788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 314.82 | 2.31 | 0.28 | 200 | application/javascript | 157100 | 9a846146393da959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 246.02 | 2.33 | 0.18 | 200 | application/javascript | 157100 | 9a841d85df87e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 21.76 | 3.36 | 0.29 | 200 | application/javascript | 157100 | 9a845e8aa9448c9d-IAD |

### GET `/_next/static/chunks/72283-44c31ff2dbd0a071.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 7.29 | 0.85 | 1.17 | 200 | application/javascript | 33960 | 9a84227a48c7dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 33.28 | 1.67 | 1.28 | 200 | application/javascript | 33960 | 9a8450feee236412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 171.81 | 2.00 | 0.22 | 200 | application/javascript | 33960 | 9a845fda2d16cb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 208.87 | 0.54 | 0.25 | 200 | application/javascript | 33960 | 9a84636f4db12788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 299.83 | 0.53 | 0.55 | 200 | application/javascript | 33960 | 9a8461463940a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 237.42 | 0.48 | 0.22 | 200 | application/javascript | 33960 | 9a841d85ffd3e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 13.80 | 0.70 | 0.24 | 200 | application/javascript | 33960 | 9a845e8ab9818c9d-IAD |

### GET `/_next/static/chunks/38874-526f584e6aadcd4b.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.19 | 0.44 | 0.40 | 200 | application/javascript | 8565 | 9a84227a48d0dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 30.89 | 0.45 | 0.26 | 200 | application/javascript | 8565 | 9a8450feee256412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 180.59 | 0.33 | 2.47 | 200 | application/javascript | 8565 | 9a845fda4d59cb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 209.18 | 5.67 | 1.66 | 200 | application/javascript | 8565 | 9a8463706f8f2788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 300.67 | 0.48 | 0.19 | 200 | application/javascript | 8565 | 9a8461481a25a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 253.65 | 0.49 | 1.43 | 200 | application/javascript | 8565 | 9a841d876afae382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 23.09 | 0.55 | 2.93 | 200 | application/javascript | 8565 | 9a845e8ad9c38c9d-IAD |

### GET `/_next/static/chunks/app/%5Blocale%5D/layout-df215d4a79c4add9.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 10.83 | 0.32 | 0.45 | 200 | application/javascript | 10734 | 9a84227a48cfdc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 44.67 | 0.36 | 0.81 | 200 | application/javascript | 10734 | 9a8450feee246412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 190.23 | 0.40 | 0.25 | 200 | application/javascript | 10734 | 9a845fda3d2acb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 209.46 | 0.47 | 0.26 | 200 | application/javascript | 10734 | 9a8463704f6c2788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 342.79 | 0.37 | 0.25 | 200 | application/javascript | 10734 | 9a8461480a1fa959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 253.25 | 0.42 | 0.27 | 200 | application/javascript | 10734 | 9a841d875ae5e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 11.97 | 0.47 | 7.31 | 200 | application/javascript | 10734 | 9a845e8ad9c08c9d-IAD |

### GET `/_next/static/chunks/75245-4381628e6d93ed7c.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.85 | 1.68 | 0.38 | 200 | application/javascript | 83664 | 9a84227a48d1dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 33.39 | 1.78 | 0.58 | 200 | application/javascript | 83664 | 9a8450ff2e3b6412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 176.68 | 1.65 | 0.76 | 200 | application/javascript | 83664 | 9a845fda4d5acb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 208.25 | 41.58 | 1.61 | 200 | application/javascript | 83664 | 9a8463706f922788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 319.42 | 0.86 | 0.21 | 200 | application/javascript | 83664 | 9a8461482a26a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 238.34 | 1.89 | 1.33 | 200 | application/javascript | 83664 | 9a841d876afee382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 16.74 | 2.16 | 1.25 | 200 | application/javascript | 83664 | 9a845e8ad9c88c9d-IAD |

### GET `/_next/static/chunks/28214-f7bd4fbe2e13f9bd.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.14 | 0.44 | 0.26 | 200 | application/javascript | 11457 | 9a84227a58e9dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 34.13 | 0.43 | 0.53 | 200 | application/javascript | 11457 | 9a8450ff2e3d6412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 484.48 | 1.82 | 0.26 | 200 | application/javascript | 11457 | 9a845fda7dafcb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 208.34 | 0.39 | 0.28 | 200 | application/javascript | 11457 | 9a8463706f9e2788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 301.96 | 0.39 | 0.83 | 200 | application/javascript | 11457 | 9a8461483a35a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 255.69 | 0.43 | 0.20 | 200 | application/javascript | 11457 | 9a841d877b16e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 21.24 | 0.52 | 0.48 | 200 | application/javascript | 11457 | 9a845e8ad9d28c9d-IAD |

### GET `/_next/static/chunks/28381-f69fef083c6248e7.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 7.73 | 0.42 | 0.20 | 200 | application/javascript | 23076 | 9a84227a58ecdc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 32.71 | 0.75 | 1.47 | 200 | application/javascript | 23076 | 9a8450ff3e4c6412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 176.61 | 0.47 | 0.24 | 200 | application/javascript | 23076 | 9a845fdb3eebcb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 208.52 | 0.40 | 0.17 | 200 | application/javascript | 23076 | 9a8463709fdd2788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 303.05 | 0.44 | 0.39 | 200 | application/javascript | 23076 | 9a8461483a36a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 255.06 | 1.37 | 0.40 | 200 | application/javascript | 23076 | 9a841d88ee28e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 19.99 | 1.87 | 0.22 | 200 | application/javascript | 23076 | 9a845e8aea228c9d-IAD |

### GET `/_next/static/chunks/app/%5Blocale%5D/(auth)/login/page-db91e715f9db634b.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 9.12 | 0.70 | 1.21 | 200 | application/javascript | 6428 | 9a84227a58f8dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 32.71 | 0.64 | 0.37 | 200 | application/javascript | 6428 | 9a8450ff3e4e6412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 170.32 | 0.35 | 0.47 | 200 | application/javascript | 6428 | 9a845fdb6f31cb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 210.67 | 0.37 | 0.27 | 200 | application/javascript | 6428 | 9a8463719a112788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 300.59 | 0.51 | 0.26 | 200 | application/javascript | 6428 | 9a846149fadba959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 238.73 | 0.46 | 0.33 | 200 | application/javascript | 6428 | 9a841d88fe44e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 15.91 | 0.32 | 1.28 | 200 | application/javascript | 6428 | 9a845e8afa4b8c9d-IAD |

### GET `/_next/static/chunks/app/%5Blocale%5D/error-c58756f7ba7b9f2b.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 10.06 | 0.50 | 0.47 | 200 | application/javascript | 10308 | 9a84227a58fddc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 33.34 | 0.42 | 0.69 | 200 | application/javascript | 10308 | 9a8450ff5e656412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 174.90 | 0.42 | 0.34 | 200 | application/javascript | 10308 | 9a845fdb6f32cb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 212.30 | 0.42 | 0.22 | 200 | application/javascript | 10308 | 9a846371ba322788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 305.61 | 0.53 | 0.25 | 200 | application/javascript | 10308 | 9a84614a0ae7a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 241.28 | 2.01 | 0.24 | 200 | application/javascript | 10308 | 9a841d88fe5ce382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 16.32 | 0.32 | 0.30 | 200 | application/javascript | 10308 | 9a845e8afa4e8c9d-IAD |

### GET `/_next/static/chunks/28743-4a3deeebaf794acf.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 19.75 | 0.56 | 0.50 | 200 | application/javascript | 9506 | 9a84227a58e5dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 36.95 | 0.37 | 0.50 | 200 | application/javascript | 9506 | 9a8450ff2e3c6412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 6.76 | 0.39 | 0.24 | 200 | application/javascript | 9506 | 9a845fda6d98cb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 210.94 | 0.40 | 0.30 | 200 | application/javascript | 9506 | 9a8463706f942788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 299.82 | 0.42 | 0.33 | 200 | application/javascript | 9506 | 9a8461482a32a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 255.15 | 0.35 | 0.36 | 200 | application/javascript | 9506 | 9a841d876b01e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 16.08 | 2.73 | 1.21 | 200 | application/javascript | 9506 | 9a845e8ad9c98c9d-IAD |

### GET `/cdn-cgi/challenge-platform/scripts/jsd/main.js` (302)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 14.86 | 0.00 | 0.35 | 302 |  | 0 | 9a84227ab9d2dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 18.04 | 0.00 | 0.40 | 302 |  | 0 | 9a84510f9adb6412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 12.19 | 0.00 | 0.20 | 302 |  | 0 | 9a845fdb6f3acb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 28.33 | 0.00 | 0.22 | 302 |  | 0 | 9a846371ba3c2788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 14.59 | 0.00 | 0.23 | 302 |  | 0 | 9a84614a1aeaa959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 14.46 | 0.00 | 0.19 | 302 |  | 0 | 9a841d88fe61e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 47.28 | 0.00 | 0.23 | 302 |  | 0 | 9a845e8bac7a8c9d-IAD |

### GET `/cdn-cgi/challenge-platform/h/b/scripts/jsd/13c98df4ef2d/main.js` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 17.74 | 0.49 | 0.45 | 200 | application/javascript | 9972 | 9a84227aea36dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 14.30 | 0.62 | 0.27 | 200 | application/javascript | 10164 | 9a84510fbaf56412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 6.44 | 0.50 | 0.22 | 200 | application/javascript | 10164 | 9a845fdb7f63cb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 9.69 | 0.34 | 0.18 | 200 | application/javascript | 9978 | 9a846371ea792788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 9.50 | 0.49 | 0.24 | 200 | application/javascript | 10093 | 9a84614a3af8a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 11.70 | 0.46 | 0.21 | 200 | application/javascript | 9958 | 9a841d891e95e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 13.86 | 0.70 | 0.24 | 200 | application/javascript | 10033 | 9a845e8bfd8d8c9d-IAD |

### POST `/cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.8728646934432264:1764773104:DtYlidy7pVfTfqpJpqLPuAHLQwgBG9mSsl1bPMKbTUA/9a8422782bfcdc58` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 15.87 | 0.31 | 0.32 | 200 | text/plain | 0 | 9a84227bdc30dc58-FRA |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | — | — | — | — | — | — | — | — | — | — |
| São Paulo | — | — | — | — | — | — | — | — | — | — |
| Sydney | — | — | — | — | — | — | — | — | — | — |
| Tokyo | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | — | — | — | — | — | — | — | — | — | — |

### GET `/favicon.ico` (404)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | 0.00 | 0.00 | 0.00 | 338.80 | 190.78 | 0.28 | 404 | text/html | 29480 | 9a84227aea41dc58-FRA |
| London | 0.00 | 0.00 | 0.00 | 313.31 | 104.14 | 0.28 | 404 | text/html | 29480 | 9a84510f9ae96412-LHR |
| San Francisco | 0.00 | 0.00 | 0.00 | 480.23 | 197.87 | 0.30 | 404 | text/html | 29480 | 9a845fdd8ac5cb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 392.53 | 191.43 | 0.27 | 404 | text/html | 29480 | 9a8463731c9c2788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 433.25 | 108.04 | 0.28 | 404 | text/html | 29480 | 9a84614c0b94a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 492.48 | 187.73 | 0.36 | 404 | text/html | 29480 | 9a841d8a8a29e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 182.01 | 190.59 | 0.27 | 404 | text/html | 29480 | 9a845e8bbccc8c9d-IAD |

### POST `/cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.7589308712729556:1764777276:Dq0c_wZGRrMPY-hSCmoqTpc1FCC57z162N2iJ5FrXxA/9a8450fcfc5c6412` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | — | — | — | — | — | — | — | — | — | — |
| London | 0.00 | 0.00 | 0.00 | 18.75 | 0.34 | 0.31 | 200 | text/plain | 0 | 9a8451108b9b6412-LHR |
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
| San Francisco | 0.42 | 22.66 | 21.36 | 15.77 | 0.65 | 1.27 | 200 | text/javascript | 19948 | 9a845fd81de9c487-SJC |
| São Paulo | 1.34 | 26.72 | 23.43 | 18.30 | 0.62 | 0.47 | 200 | text/javascript | 19948 | 9a84636ddda0f245-GRU |
| Sydney | 0.90 | 16.92 | 15.70 | 19.90 | 0.49 | 0.55 | 200 | text/javascript | 19948 | 9a8461445ba1a974-SYD |
| Tokyo | 0.47 | 23.70 | 21.55 | 15.68 | 0.58 | 0.26 | 200 | text/javascript | 19948 | 9a841d846807dfc5-NRT |
| Washington, DC | 2.71 | 25.14 | 23.72 | 15.96 | 0.50 | 0.26 | 200 | text/javascript | 19948 | 9a845e8b8f1d7b5f-IAD |

### POST `/cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.7589308712729556:1764777276:Dq0c_wZGRrMPY-hSCmoqTpc1FCC57z162N2iJ5FrXxA/9a845fd4eb3dcb6f` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | — | — | — | — | — | — | — | — | — | — |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | 0.00 | 0.00 | 0.00 | 13.37 | 0.31 | 0.25 | 200 | text/plain | 0 | 9a845fdc286ccb6f-SJC |
| São Paulo | — | — | — | — | — | — | — | — | — | — |
| Sydney | — | — | — | — | — | — | — | — | — | — |
| Tokyo | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | — | — | — | — | — | — | — | — | — | — |

### POST `/cdn-cgi/rum` (204)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | — | — | — | — | — | — | — | — | — | — |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | 0.00 | 0.00 | 0.00 | 4.00 | 0.20 | 0.20 | 204 | text/plain | 0 | 9a845fdd8ac4cb6f-SJC |
| São Paulo | 0.00 | 0.00 | 0.00 | 7.33 | 0.20 | 0.16 | 204 | text/plain | 0 | 9a8463730c9b2788-GRU |
| Sydney | 0.00 | 0.00 | 0.00 | 5.47 | 0.28 | 0.17 | 204 | text/plain | 0 | 9a84614c0b93a959-SYD |
| Tokyo | 0.00 | 0.00 | 0.00 | 4.36 | 0.20 | 0.19 | 204 | text/plain | 0 | 9a841d8a8a23e382-NRT |
| Washington, DC | 0.00 | 0.00 | 0.00 | 4.83 | 0.25 | 0.22 | 204 | text/plain | 0 | 9a845e8bbcb18c9d-IAD |

### POST `/cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.7589308712729556:1764777276:Dq0c_wZGRrMPY-hSCmoqTpc1FCC57z162N2iJ5FrXxA/9a846369db3f2788` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | — | — | — | — | — | — | — | — | — | — |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | — | — | — | — | — | — | — | — | — | — |
| São Paulo | 0.00 | 0.00 | 0.00 | 20.84 | 0.30 | 0.26 | 200 | text/plain | 0 | 9a846372bc002788-GRU |
| Sydney | — | — | — | — | — | — | — | — | — | — |
| Tokyo | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | — | — | — | — | — | — | — | — | — | — |

### POST `/cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.7589308712729556:1764777276:Dq0c_wZGRrMPY-hSCmoqTpc1FCC57z162N2iJ5FrXxA/9a84613e8e87a959` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | — | — | — | — | — | — | — | — | — | — |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | — | — | — | — | — | — | — | — | — | — |
| São Paulo | — | — | — | — | — | — | — | — | — | — |
| Sydney | 0.00 | 0.00 | 0.00 | 13.84 | 0.35 | 0.39 | 200 | text/plain | 0 | 9a84614afb4ca959-SYD |
| Tokyo | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | — | — | — | — | — | — | — | — | — | — |

### POST `/cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.8728646934432264:1764773104:DtYlidy7pVfTfqpJpqLPuAHLQwgBG9mSsl1bPMKbTUA/9a841d7ff9ace382` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | — | — | — | — | — | — | — | — | — | — |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | — | — | — | — | — | — | — | — | — | — |
| São Paulo | — | — | — | — | — | — | — | — | — | — |
| Sydney | — | — | — | — | — | — | — | — | — | — |
| Tokyo | 0.00 | 0.00 | 0.00 | 13.07 | 0.31 | 0.32 | 200 | text/plain | 0 | 9a841d89d875e382-NRT |
| Washington, DC | — | — | — | — | — | — | — | — | — | — |

### POST `/cdn-cgi/challenge-platform/h/b/jsd/oneshot/13c98df4ef2d/0.7589308712729556:1764777276:Dq0c_wZGRrMPY-hSCmoqTpc1FCC57z162N2iJ5FrXxA/9a845e879fb08c9d` (200)

| Location | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | — | — | — | — | — | — | — | — | — | — |
| London | — | — | — | — | — | — | — | — | — | — |
| San Francisco | — | — | — | — | — | — | — | — | — | — |
| São Paulo | — | — | — | — | — | — | — | — | — | — |
| Sydney | — | — | — | — | — | — | — | — | — | — |
| Tokyo | — | — | — | — | — | — | — | — | — | — |
| Washington, DC | 0.00 | 0.00 | 0.00 | 19.92 | 0.28 | 0.26 | 200 | text/plain | 0 | 9a845e8cc80b8c9d-IAD |

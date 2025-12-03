## HAR comparison: Without CF vs CF Proxy vs CF Proxy + CF Tunnel (api-users-health)

Scenarios:
- Without CF (DO LB): direct to DigitalOcean Frankfurt (Kubernetes, DO LB + ingress-nginx)
- With CF Proxy: Cloudflare proxy in front of the same origin
- With CF Proxy + CF Tunnel: Cloudflare proxy plus CF Tunnel to origin

Summary by scenario/location:

| Scenario | Location | Requests | Page size (KB) | Load time (s, `_fullyLoaded`) | CF-ray edge |
|---|---|---:|---:|---:|---|
| Without CF (DO LB) | Frankfurt | 6 | 233.07 | 0.374 | — |
| With CF Proxy | Frankfurt | 6 | 233.07 | 0.461 | FRA |
| With CF Proxy + CF Tunnel | Frankfurt | 6 | 233.07 | 0.468 | FRA |
| Without CF (DO LB) | London | 6 | 233.07 | 0.467 | — |
| With CF Proxy | London | 1 | 0.06 | 0.161 | LHR |
| With CF Proxy + CF Tunnel | London | 6 | 233.07 | 2.206 | LHR |
| Without CF (DO LB) | San Francisco | 6 | 233.07 | 1.305 | — |
| With CF Proxy | San Francisco | 6 | 233.07 | 1.214 | SJC |
| With CF Proxy + CF Tunnel | San Francisco | 6 | 233.07 | 1.057 | SJC |
| Without CF (DO LB) | São Paulo | 6 | 233.07 | 1.605 | — |
| With CF Proxy | São Paulo | 6 | 233.07 | 3.658 | GRU |
| With CF Proxy + CF Tunnel | São Paulo | 6 | 233.07 | 1.165 | GRU |
| Without CF (DO LB) | Sydney | 6 | 233.07 | 2.132 | — |
| With CF Proxy | Sydney | 6 | 233.07 | 1.923 | SYD |
| With CF Proxy + CF Tunnel | Sydney | 6 | 233.07 | 1.690 | SYD |
| Without CF (DO LB) | Tokyo | 6 | 233.07 | 1.820 | — |
| With CF Proxy | Tokyo | 6 | 233.07 | 2.232 | NRT |
| With CF Proxy + CF Tunnel | Tokyo | 6 | 233.07 | 1.988 | NRT |
| Without CF (DO LB) | Washington, DC | 6 | 233.07 | 0.852 | — |
| With CF Proxy | Washington, DC | 6 | 233.07 | 1.076 | IAD |
| With CF Proxy + CF Tunnel | Washington, DC | 6 | 233.07 | 0.875 | IAD |

### /_next/static/css/abf98b2abcdbd573.css (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 13.06 | 2.34 | 0.62 | 200 | text/css | 123936 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.19 | 1.02 | 0.77 | 200 | text/css | 123936 | 9a846aab3d37d28a-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.14 | 2.29 | 0.71 | 200 | text/css | 123936 | 9a849f67ba60bbe5-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 55.39 | 4.65 | 0.80 | 200 | text/css | 123936 | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.08 | 1.20 | 1.01 | 200 | text/css | 123936 | 9a84a07f69774e3b-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 428.91 | 101.66 | 0.52 | 200 | text/css | 123936 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.17 | 1.01 | 0.77 | 200 | text/css | 123936 | 9a846fc86dc3fc54-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.08 | 0.98 | 0.70 | 200 | text/css | 123936 | 9a84a2126dde49d2-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 298.37 | 372.38 | 0.62 | 200 | text/css | 123936 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.17 | 0.93 | 1.04 | 200 | text/css | 123936 | 9a8471920c91f198-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.09 | 0.88 | 0.93 | 200 | text/css | 123936 | 9a84a471ef17f181-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 408.18 | 327.44 | 0.71 | 200 | text/css | 123936 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.11 | 1.59 | 0.76 | 200 | text/css | 123936 | 9a8470aeee3ee7c8-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.07 | 0.99 | 0.87 | 200 | text/css | 123936 | 9a84a37a0f2fa7f6-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 510.04 | 267.17 | 0.63 | 200 | text/css | 123936 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.07 | 0.92 | 0.85 | 200 | text/css | 123936 | 9a84699d6e369d71-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.13 | 1.18 | 0.93 | 200 | text/css | 123936 | 9a849ec92affd758-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 298.74 | 26.06 | 0.66 | 200 | text/css | 123936 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.13 | 3.36 | 0.81 | 200 | text/css | 123936 | 9a846d6c695fc95e-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.16 | 3.98 | 1.01 | 200 | text/css | 123936 | 9a84a1584fe364aa-IAD |

### /_next/static/css/e771c44a50dae3b6.css (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 10.59 | 0.41 | 0.53 | 200 | text/css | 4004 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.08 | 1.28 | 0.67 | 200 | text/css | 4004 | 9a846aab3d3bd28a-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.07 | 0.36 | 0.57 | 200 | text/css | 4004 | 9a849f67ba62bbe5-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 46.91 | 0.35 | 0.72 | 200 | text/css | 4004 | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.13 | 0.64 | 0.87 | 200 | text/css | 4004 | 9a84a07f69794e3b-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 157.62 | 2.04 | 0.44 | 200 | text/css | 4004 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.09 | 0.29 | 0.68 | 200 | text/css | 4004 | 9a846fc86dc4fc54-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.11 | 0.72 | 0.57 | 200 | text/css | 4004 | 9a84a2126ddf49d2-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 229.54 | 0.50 | 0.53 | 200 | text/css | 4004 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.08 | 0.31 | 0.92 | 200 | text/css | 4004 | 9a8471920c94f198-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.12 | 0.40 | 0.83 | 200 | text/css | 4004 | 9a84a471ef19f181-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 296.60 | 0.47 | 0.61 | 200 | text/css | 4004 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.15 | 1.32 | 0.68 | 200 | text/css | 4004 | 9a8470aeee40e7c8-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.12 | 0.54 | 0.77 | 200 | text/css | 4004 | 9a84a37a0f30a7f6-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 352.23 | 0.43 | 0.54 | 200 | text/css | 4004 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.14 | 0.52 | 0.74 | 200 | text/css | 4004 | 9a84699d6e389d71-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.07 | 0.27 | 0.80 | 200 | text/css | 4004 | 9a849ec92b01d758-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 129.86 | 0.46 | 0.59 | 200 | text/css | 4004 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 0.11 | 0.77 | 0.71 | 200 | text/css | 4004 | 9a846d6c6960c95e-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 0.09 | 0.54 | 0.85 | 200 | text/css | 4004 | 9a84a1584fe764aa-IAD |

### /_next/static/media/739c2d8941231bb4-s.p.woff2 (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 9.08 | 0.89 | 0.84 | 200 | font/woff2 | 32752 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 7.06 | 1.13 | 0.99 | 200 | font/woff2 | 32752 | 9a846aab3d4fd28a-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.61 | 1.08 | 0.91 | 200 | font/woff2 | 32752 | 9a849f67ba66bbe5-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 47.88 | 7.35 | 1.18 | 200 | font/woff2 | 32752 | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.62 | 0.92 | 1.23 | 200 | font/woff2 | 32752 | 9a84a07f698c4e3b-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 402.13 | 85.35 | 0.81 | 200 | font/woff2 | 32752 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 8.50 | 0.39 | 0.93 | 200 | font/woff2 | 32752 | 9a846fc87dccfc54-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 8.77 | 0.43 | 0.91 | 200 | font/woff2 | 32752 | 9a84a2126de949d2-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 257.07 | 277.62 | 0.87 | 200 | font/woff2 | 32752 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 7.78 | 0.55 | 1.35 | 200 | font/woff2 | 32752 | 9a8471920cabf198-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 11.42 | 1.89 | 1.05 | 200 | font/woff2 | 32752 | 9a84a471ff29f181-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 747.62 | 100.65 | 0.94 | 200 | font/woff2 | 32752 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 7.33 | 0.77 | 1.11 | 200 | font/woff2 | 32752 | 9a8470aeee41e7c8-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.03 | 0.50 | 1.18 | 200 | font/woff2 | 32752 | 9a84a37a0f31a7f6-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 254.07 | 255.76 | 0.89 | 200 | font/woff2 | 32752 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 6.85 | 0.45 | 1.10 | 200 | font/woff2 | 32752 | 9a84699d6e449d71-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 5.99 | 0.38 | 1.09 | 200 | font/woff2 | 32752 | 9a849ec93b06d758-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 103.95 | 105.02 | 0.90 | 200 | font/woff2 | 32752 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 10.26 | 0.92 | 1.06 | 200 | font/woff2 | 32752 | 9a846d6c6968c95e-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 20.07 | 0.55 | 1.17 | 200 | font/woff2 | 32752 | 9a84a1584ff564aa-IAD |

### /_next/static/media/e4af272ccee01ff0-s.p.woff2 (200)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 13.29 | 0.97 | 0.71 | 200 | font/woff2 | 48432 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 7.27 | 1.12 | 0.89 | 200 | font/woff2 | 48432 | 9a846aab3d52d28a-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 9.95 | 0.91 | 0.82 | 200 | font/woff2 | 48432 | 9a849f67ba68bbe5-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 25.71 | 20.35 | 0.94 | 200 | font/woff2 | 48432 | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.77 | 0.73 | 1.15 | 200 | font/woff2 | 48432 | 9a84a07f698e4e3b-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 170.34 | 215.41 | 0.63 | 200 | font/woff2 | 48432 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 8.04 | 2.12 | 0.89 | 200 | font/woff2 | 48432 | 9a846fc87dcefc54-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.31 | 2.12 | 0.82 | 200 | font/woff2 | 48432 | 9a84a2126dea49d2-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 391.94 | 224.70 | 0.72 | 200 | font/woff2 | 48432 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 8.53 | 2.01 | 1.14 | 200 | font/woff2 | 48432 | 9a8471920cacf198-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 10.57 | 1.43 | 1.02 | 200 | font/woff2 | 48432 | 9a84a471ff2cf181-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 320.32 | 328.14 | 0.86 | 200 | font/woff2 | 48432 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 6.64 | 1.13 | 0.87 | 200 | font/woff2 | 48432 | 9a8470aefe42e7c8-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.77 | 0.72 | 0.98 | 200 | font/woff2 | 48432 | 9a84a37a0f32a7f6-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 520.94 | 194.40 | 0.74 | 200 | font/woff2 | 48432 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 8.01 | 0.53 | 0.93 | 200 | font/woff2 | 48432 | 9a84699d6e459d71-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 7.02 | 0.60 | 1.04 | 200 | font/woff2 | 48432 | 9a849ec93b07d758-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 215.39 | 83.14 | 0.73 | 200 | font/woff2 | 48432 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 11.42 | 1.58 | 0.90 | 200 | font/woff2 | 48432 | 9a846d6c696bc95e-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 21.11 | 0.81 | 1.14 | 200 | font/woff2 | 48432 | 9a84a1585ff764aa-IAD |

### /api/users/health (401)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 7.62 | 13.57 | 12.74 | 8.25 | 7.22 | 0.00 | 401 | application/json | 62 | — |
| Frankfurt | With CF Proxy | 6.65 | 13.41 | 12.39 | 38.98 | 8.77 | 0.00 | 401 | application/json | 62 | 9a846aa9a88bd28a-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 8.53 | 13.21 | 11.89 | 25.22 | 0.88 | 0.00 | 401 | application/json | 62 | 9a849f661923bbe5-FRA |
| London | Without CF (DO LB) | 7.46 | 47.36 | 31.71 | 18.71 | 14.73 | 0.00 | 401 | application/json | 62 | — |
| London | With CF Proxy | 38.11 | 16.41 | 14.70 | 94.34 | 1.04 | 0.00 | 401 | application/json | 62 | 9a846c9a0e785016-LHR |
| London | With CF Proxy + CF Tunnel | 39.20 | 17.42 | 15.40 | 69.57 | 1.07 | 0.00 | 401 | application/json | 62 | 9a84a07d2c944e3b-LHR |
| San Francisco | Without CF (DO LB) | 0.30 | 314.27 | 163.18 | 156.88 | 0.80 | 0.00 | 401 | application/json | 62 | — |
| San Francisco | With CF Proxy | 15.05 | 15.02 | 13.14 | 640.19 | 0.91 | 0.00 | 401 | application/json | 62 | 9a846fc1bc53fc54-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 24.10 | 15.87 | 13.87 | 535.72 | 0.85 | 0.00 | 401 | application/json | 62 | 9a84a20cab3349d2-SJC |
| São Paulo | Without CF (DO LB) | 17.96 | 406.16 | 208.77 | 199.70 | 0.91 | 0.00 | 401 | application/json | 62 | — |
| São Paulo | With CF Proxy | 13.74 | 21.89 | 15.96 | 720.74 | 0.89 | 0.00 | 401 | application/json | 62 | 9a84718b19edf198-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 23.73 | 17.37 | 13.49 | 603.75 | 0.84 | 0.00 | 401 | application/json | 62 | 9a84a46b9a14f181-GRU |
| Sydney | Without CF (DO LB) | 59.91 | 591.24 | 303.62 | 301.96 | 0.84 | 0.00 | 401 | application/json | 62 | — |
| Sydney | With CF Proxy | 15.63 | 14.52 | 13.14 | 1209.48 | 0.97 | 0.00 | 401 | application/json | 62 | 9a8470a3bce8e7c8-SYD |
| Sydney | With CF Proxy + CF Tunnel | 90.35 | 12.42 | 10.99 | 901.92 | 0.95 | 0.00 | 401 | application/json | 62 | 9a84a3715d4fa7f6-SYD |
| Tokyo | Without CF (DO LB) | 9.76 | 494.91 | 256.31 | 243.92 | 0.90 | 0.00 | 401 | application/json | 62 | — |
| Tokyo | With CF Proxy | 2.72 | 27.78 | 18.11 | 992.78 | 0.83 | 0.00 | 401 | application/json | 62 | 9a8469949c5c9d71-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.28 | 14.90 | 12.90 | 749.27 | 0.89 | 0.00 | 401 | application/json | 62 | 9a849ebdfe94d758-NRT |
| Washington, DC | Without CF (DO LB) | 28.46 | 221.82 | 107.38 | 97.70 | 0.88 | 0.00 | 401 | application/json | 62 | — |
| Washington, DC | With CF Proxy | 31.52 | 15.31 | 13.85 | 434.89 | 0.90 | 0.00 | 401 | application/json | 62 | 9a846d673da4c95e-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 6.03 | 14.35 | 12.83 | 304.28 | 1.03 | 0.00 | 401 | application/json | 62 | 9a84a153ac7264aa-IAD |

### /favicon.ico (404)

| Location | Scenario | DNS (ms) | Connect (ms) | SSL (ms) | Wait/TTFB (ms) | Content download (ms) | Blocked (ms) | Status | MIME type | Body size (bytes) | CF-ray |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| Frankfurt | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 30.07 | 291.08 | 0.31 | 404 | text/html | 29480 | — |
| Frankfurt | With CF Proxy | 0.00 | 0.00 | 0.00 | 193.10 | 186.43 | 0.26 | 404 | text/html | 29480 | 9a846aaa09a9d28a-FRA |
| Frankfurt | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 206.29 | 194.01 | 0.27 | 404 | text/html | 29480 | 9a849f66696abbe5-FRA |
| London | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 53.06 | 309.52 | 0.31 | 404 | text/html | 29480 | — |
| London | With CF Proxy | — | — | — | — | — | — | — | — | — | — |
| London | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 258.32 | 1790.05 | 0.29 | 404 | text/html | 29480 | 9a84a07dcdff4e3b-LHR |
| San Francisco | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 258.04 | 554.55 | 0.26 | 404 | text/html | 29480 | — |
| San Francisco | With CF Proxy | 0.00 | 0.00 | 0.00 | 400.93 | 104.20 | 0.83 | 404 | text/html | 29480 | 9a846fc5fa66fc54-SJC |
| San Francisco | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 334.27 | 100.82 | 0.34 | 404 | text/html | 29480 | 9a84a210499d49d2-SJC |
| São Paulo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 296.28 | 673.11 | 0.30 | 404 | text/html | 29480 | — |
| São Paulo | With CF Proxy | 0.00 | 0.00 | 0.00 | 369.79 | 2507.70 | 0.25 | 404 | text/html | 29480 | 9a84718fb92cf198-GRU |
| São Paulo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 381.79 | 107.37 | 0.25 | 404 | text/html | 29480 | 9a84a46f8a16f181-GRU |
| Sydney | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 315.12 | 209.26 | 0.39 | 404 | text/html | 29480 | — |
| Sydney | With CF Proxy | 0.00 | 0.00 | 0.00 | 572.43 | 99.73 | 0.25 | 404 | text/html | 29480 | 9a8470ab5b42e7c8-SYD |
| Sydney | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 483.07 | 191.46 | 0.32 | 404 | text/html | 29480 | 9a84a3770e93a7f6-SYD |
| Tokyo | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 266.22 | 233.19 | 0.47 | 404 | text/html | 29480 | — |
| Tokyo | With CF Proxy | 0.00 | 0.00 | 0.00 | 410.26 | 791.23 | 0.24 | 404 | text/html | 29480 | 9a84699ad9689d71-NRT |
| Tokyo | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 1027.48 | 182.83 | 0.27 | 404 | text/html | 29480 | 9a849ec2cbf3d758-NRT |
| Washington, DC | Without CF (DO LB) | 0.00 | 0.00 | 0.00 | 119.40 | 340.85 | 0.26 | 404 | text/html | 29480 | — |
| Washington, DC | With CF Proxy | 0.00 | 0.00 | 0.00 | 385.34 | 197.97 | 0.25 | 404 | text/html | 29480 | 9a846d6a0bd7c95e-IAD |
| Washington, DC | With CF Proxy + CF Tunnel | 0.00 | 0.00 | 0.00 | 429.76 | 107.54 | 0.33 | 404 | text/html | 29480 | 9a84a155994864aa-IAD |

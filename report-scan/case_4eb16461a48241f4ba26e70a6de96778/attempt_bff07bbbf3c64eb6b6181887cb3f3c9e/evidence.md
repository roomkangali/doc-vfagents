# Original-location index

Coordinates and opaque Evidence IDs are retained; Evidence blobs and target bytes are private. A coordinate check does not establish vulnerability semantics.

## F1 / A02

- Original locations: app.asar:src/renderer/pages/index.html:offset 6800 \| app.asar:src/main/preload.js:offset 350 \| app.asar:src/main/main.js:offset 24850 \| app.asar:src/main/main.js:offset 25200 \| app.asar:src/renderer/pages/xss-rce-direct.html \| app.asar:src/renderer/pages/xss-rce-direct.html:offset 3300 \| app.asar:src/renderer/pages/xss-rce-direct.html:offset 5800 \| app.asar:src/renderer/js/xss-rce-direct.js:offset 2905
- Evidence IDs: E3 \| E4 \| E5 \| E6 \| E7 \| E8
- Citation count in private audit: 8
- Candidate ref: `c82a9387466cb838ba510c70d1b1e7a2b2aa40b9cfa638f3a2f16fbd978eca3c`; decision ref: `70fdfda212932fd58439ee92eb43713bdee01eb47f682569ed6bc4ca687b7c18`

## F2 / A01

- Original locations: app.asar:src/renderer/pages/xss-system-api.html:offset 2597 \| app.asar:src/renderer/pages/xss-system-api.html:offset 4746 \| app.asar:src/renderer/js/xss-system-api.js:offset 2257 \| app.asar:src/main/preload-xss-bridged.js:offset 520 \| app.asar:src/main/main.js:offset 28036 \| app.asar:src/main/main.js:offset 30634 \| app.asar:src/main/observability.js:offset 5152
- Evidence IDs: E9 \| E10 \| E11 \| E12 \| E13 \| E14 \| E15
- Citation count in private audit: 7
- Candidate ref: `5fa22bce5988b616e01fd8c0281f21025a8815dc97e07e8ec0310992a384b660`; decision ref: `67ca6999e7a247e70b3595547452821b1015e72579553c5b119324249c0eb88b`

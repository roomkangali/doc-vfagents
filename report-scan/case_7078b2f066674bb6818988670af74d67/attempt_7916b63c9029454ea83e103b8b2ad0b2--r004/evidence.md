# Original-location index

Coordinates and opaque Evidence IDs are retained; Evidence blobs and target bytes are private. A coordinate check does not establish vulnerability semantics.

## F1 / A01

- Original locations: app.asar:src/renderer/pages/xss-system-api.html \| app.asar:src/renderer/pages/xss-system-api.html:offset 4096 \| app.asar:src/renderer/js/xss-system-api.js:offset 1962 \| app.asar:src/main/preload-xss-bridged.js:offset 473 \| app.asar:src/main/main.js:offset 27814 \| app.asar:src/main/main.js:offset 30541
- Evidence IDs: E5 \| E6 \| E7 \| E8 \| E9 \| E10
- Citation count in private audit: 6
- Candidate ref: `578a653580f0f214c660999b352a0098191cc6e14a6d436595696d40a6a69317`; decision ref: `163f82805f08a1031d88f41a04b01ac6b9fcb0f39d6dc9ad8cca20c0856b0d4e`

## F2 / A02

- Original locations: app.asar:src/renderer/pages/xss-rce-direct.html \| app.asar:src/renderer/pages/xss-rce-direct.html:offset 3200 \| app.asar:src/renderer/pages/xss-rce-direct.html:offset 5800 \| app.asar:src/renderer/js/xss-rce-direct.js:offset 2624 \| app.asar:src/main/main.js:offset 24791 \| app.asar:src/main/main.js:offset 24900 \| app.asar:src/main/main.js:offset 25350 \| app.asar:package.json:offset 650
- Evidence IDs: E11 \| E12 \| E13 \| E14 \| E15
- Citation count in private audit: 8
- Candidate ref: `55e5477da5e74607359d6fced046c9d979245344c7f816b36a9778cdb0b9e962`; decision ref: `e9c87a9a13b5f7f87f896b02ee3fff589ada44896cfcc1ae8a76f3f04634132e`

## F3 / A03

- Original locations: app.asar:src/renderer/pages/xss-no-priv.html \| app.asar:src/renderer/js/xss-no-priv.js:offset 2484 \| app.asar:src/renderer/js/xss-no-priv.js:offset 2898 \| app.asar:src/renderer/js/xss-no-priv.js:offset 3189 \| app.asar:src/renderer/js/xss-no-priv.js:offset 3251 \| app.asar:src/main/preload-xss-contained.js \| app.asar:src/main/main.js:offset 31342 \| app.asar:src/main/main.js:offset 31409 \| app.asar:src/main/main.js:offset 31432 \| app.asar:src/main/main.js:offset 31464 \| app.asar:src/main/main.js:offset 31855
- Evidence IDs: E16 \| E17 \| E18 \| E19
- Citation count in private audit: 11
- Candidate ref: `78d9f08a5d2684c5d0f726f6685e788cc18d8e27afde457b11324fe5c1489823`; decision ref: `10607bf2d585378ef69543b99f58b31f5ebfb195a64332554407729c5f53f776`

## F4 / A01

- Original locations: app.asar:src/renderer/pages/xss-system-api.html:offset 2649 \| app.asar:src/renderer/js/xss-system-api.js:offset 2257 \| app.asar:src/main/preload-xss-bridged.js:offset 473 \| app.asar:src/main/main.js:offset 27879 \| app.asar:src/main/main.js:offset 30634 \| app.asar:src/main/observability.js:offset 5152
- Evidence IDs: E20 \| E21 \| E22 \| E23 \| E24
- Citation count in private audit: 6
- Candidate ref: `a67aa8ed8026429ccdbc22d461d078ffdac528a09e4e2a1384529139d52deaf8`; decision ref: `58a01923e8de39da0dfea9a3db7662154664c5e70b960b1bfb8145a2b4bb8232`

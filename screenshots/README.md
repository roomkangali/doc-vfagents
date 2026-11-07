# VFA CLI screenshots

These two original PNG captures show VFA v1.0.000 opening a **saved, completed** host/WebAssembly case on 7 November 2026. They were not captured during the scan. They illustrate the operator interface; the [case audit](../claim-audit.csv), [selected report summary](../report-scan/case_35ba4dd3e5e6435c9e07b0efbfa90ca1/attempt_b7c03e843a2e4fe4aff6b4d0427d9e3f--r002/report.md), and [workflow register](../workflow-candidates.csv) carry the underlying research record.

- [Finding and reviewer counterevidence](wasm-finding-review.png) displays Finding F1 with its `static_path` basis and a counterexample considered by the reviewer.
- [PoC execution status](wasm-poc-status.png) displays zero executed tests for the same Finding. A recorded operator procedure does not establish a runtime effect.

The [manifest](manifest.json) records the source capture hash, published image hash, case and attempt/export identity, UTC capture time, and UI version. The two published images are byte-identical to the selected captures. Other captures, including one that shows target bytes and others that show local filesystem paths, are not distributed.

# Coverage and proof gaps

Export state: **partial**. This projection includes only author-audited Finding rows, not the full VFA coverage ledger.

- **F1** (`A01`): No Electron/browser/script execution was permitted, so event-handler execution from innerHTML, IPC round-trip, OS command output, and platform-specific runtime behavior remain unobserved. The full HTML bytes show no CSP declaration, but response-header CSP is not applicable to the local file in the static ASAR and was not runtime-checked.

- **F2** (`A02`): Static bytes establish the source-to-sink and Node-enabled configuration, but Electron was not run. Runtime execution of a harmless injected event-handler payload, actual availability of require() in Electron 40.2.1, and whether any response-header CSP is applied outside the ASAR remain untested.

- **F3** (`A03`): Electron/browser execution was forbidden and not performed. Static bytes establish the source, sink, page data, and declared guards, but do not observe an event-handler payload executing or verify effective runtime preferences/CSP headers. No remote or cross-user delivery mechanism was established.

- **F4** (`A01`): A scoped work item must invoke the bundle adapter before member-content evidence exists.; No Electron runtime or deep package adapter was used.; At intake, no discovery or validation had run; generic read-only navigation is available for scheduled investigation. Specialized adapters may add depth where applicable.; Bounded generic navigation only; no framework or vulnerability conclusion. Gap: bounded result incomplete; path must be a bounded relative POSIX path; this case has not authorized automatic bounded local proof; No exact authored source fixture claim gate applies.; Candidate is not a supported, target-bound static claim.

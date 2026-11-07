# Author-audited Finding entries

Original VFA statuses and later author audit are distinct. These are summaries, not complete original exports.

## F1 — ric-wasm-execute-stack-selector-overwrite-to-host-eval

- Path group: `W01`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: Host input reaches execute; WABT shows a copy across the object selector and call_indirect table index 3 bound to the eval-backed import. This is a static conditional path, not observed JavaScript execution.
- Reviewer counterevidence: Function 7 initializes the selector to only 1 or 2, and WebAssembly linear-memory accesses trap outside the memory. For n >= 512 function 13 calls the host copyWithin helper, which is heap-bounded. These controls do not protect the object boundary at +68: initialization precedes the copy, the 72-byte candidate stays within linear memory and takes the module's small-copy path, and function 8 later reloads the overwritten selector. The host source does not authenticate /api/execute or impose a message-length cap. No runtime was executed, so Express decoding of embedded control bytes and the exact harmless JavaScript payload remain unverified.
- Negative control: The same-length selector-1 input follows the same route and copy but invokes the legitimate table target, produces no marker, and returns or transforms data without entering _emscripten_run_script.
- PoC: `published`, execution `not_run`; runtime `not_performed`

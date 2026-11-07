# Author-audited Finding entries

Original VFA statuses and later author audit are distinct. These are summaries, not complete original exports.

## F1 — dvea-bridged-xss-command-execution

- Path group: `A01`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: The local bridged page assigns form input to innerHTML; its preload exposes runCommand and main handles it with exec. Static conditional chain only; no Electron run.
- Reviewer counterevidence: The Bridged BrowserWindow uses sandbox:true, contextIsolation:true, nodeIntegration:false and prevents will-navigate. Those controls restrict direct Node access and navigation, but do not constrain the explicitly exposed systemAPI.runCommand or the main-process exec handler. The sibling Contained preload exposes no privileged API, but it is a different window/control, not a defeater for this path.
- Negative control: Submitting the same event-handler structure with only a DOM-marker action and no systemAPI call should mark the DOM but produce no bridge response and no OS-command output.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F2 — owned-innerhtml-nodeintegration-rce

- Path group: `A02`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: The owned page assigns form input to innerHTML in a Node-integrated, unsandboxed window. Static conditional Node access only; effective runtime exposure not observed.
- Reviewer counterevidence: The main process installs will-navigate and always calls preventDefault(), constraining the privileged configuration to the bundled lab page. The Owned window specifies preload:undefined, so there is no separate preload bridge. Those controls reduce cross-page exposure but do not sanitize xssInput3 or remove Node from the current document. No setWindowOpenHandler review or runtime Electron execution was performed.
- Negative control: Submitting the same payload as encoded text, or replacing the innerHTML assignment with textContent while keeping the same form path, displays literal markup and produces no Node-derived output.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F3 — dvea-contained-dom-xss-renderer-data

- Path group: `A03`; VFA status: `confirmed`; author audit: `needs_correction`
- Audit rationale: The local innerHTML sink can interpret active markup, but this is the intended contained control: no preload exposure, Node integration, or navigation escape is shown. Count only local DOM/data behavior, not privileged compromise.
- Reviewer counterevidence: The original contained preload imports ipcRenderer only to self-report isolation and exposes nothing through contextBridge. The creating main-process function selects that preload, enables sandbox and contextIsolation, disables nodeIntegration, and prevents all will-navigate events. These controls defeat the broader XSS-to-OS hypothesis but do not prevent same-renderer DOM/storage access.
- Negative control: Submitting an entity-escaped look-alike such as &lt;img src=x onerror=...&gt; follows the same form and innerHTML assignment but yields inert text and does not add the token/storage value to #attacker-log.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F4 — dvea-bridged-xss-command-execution

- Path group: `A01`; VFA status: `inconclusive`; author audit: `needs_correction`
- Audit rationale: Duplicate of primary F1 at the same bridged window, IPC and exec sink. The extra inconclusive Finding must not become another unique vulnerability.
- Reviewer counterevidence: The Bridged BrowserWindow is sandboxed, context-isolated, has Node integration disabled, and cancels navigation; those controls limit direct Node access and privilege carryover. The only inspected response-header hook merely observes CSP and returns callback({cancel:false}); it does not inject a policy. A contained sibling preload exposes no bridge, demonstrating a safer design, but it is not the preload used by this window.
- Negative control: Submitting plain text through the same form changes only xssOutput2 and does not invoke bridge-run-command; the contained sibling's equivalent injection has no window.systemAPI.runCommand capability.
- PoC: `draft_only`, execution `not_run`; runtime `not recorded`

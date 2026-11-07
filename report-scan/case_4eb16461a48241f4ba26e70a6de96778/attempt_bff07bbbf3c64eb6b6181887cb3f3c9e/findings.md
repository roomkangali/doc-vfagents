# Author-audited Finding entries

Original VFA statuses and later author audit are distinct. These are summaries, not complete original exports.

## F1 — owned-window-innerhtml-nodeintegration-rce

- Path group: `A02`; VFA status: `inconclusive`; author audit: `needs_correction`
- Audit rationale: Same owned-window source, sink, configuration, and effect as primary F2. Preserve its earlier inconclusive verdict but do not count another path.
- Reviewer counterevidence: The main process installs a will-navigate handler that always calls preventDefault, limiting privilege carry-over to another document, and the Owned window has no preload bridge. Those controls do not sanitize xssInput3 or prevent event-handler markup from executing in the already loaded Node-enabled document. The entry requires the user to open the challenge and submit input; no remote delivery route was established.
- Negative control: Submitting inert markup such as <span data-vfa-control='1'>control</span> through the same form changes xssOutput3 markup but does not write a Node-derived value to attacker-log or invoke require.
- PoC: `draft_only`, execution `not_run`; runtime `not recorded`

## F2 — bridged-window-xss-preload-command-exec

- Path group: `A01`; VFA status: `inconclusive`; author audit: `needs_correction`
- Audit rationale: Same bridged-window source, IPC, exec sink, and effect as primary F1. Preserve its earlier inconclusive verdict but do not count another path.
- Reviewer counterevidence: The same window is configured with sandbox:true, contextIsolation:true, nodeIntegration:false and blocks will-navigate; these are meaningful containment controls and rule out direct renderer require/process access and navigation-based privilege carryover. They do not defeat the same-document innerHTML path because the preload deliberately exposes runCommand. The only CSP-related package hook found observes response/meta policies and calls callback({cancel:false}); it does not inject a CSP. A separate contained window exposes no privileged bridge, but that is a different window/control.
- Negative control: Submitting the same marker as plain text without active HTML/event-handler syntax should render text only and must not invoke bridge-run-command or produce command output.
- PoC: `draft_only`, execution `not_run`; runtime `not recorded`

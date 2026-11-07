# Coverage and proof gaps

Export state: **complete**. This projection includes only author-audited Finding rows, not the full VFA coverage ledger.

- **F1** (`S01`): No runtime request was executed by instruction. The exact response fields and adapter behavior for a boolean payload remain to be confirmed; multi-statement effects are unproven.

- **F2** (`S02`): Static source establishes routing, missing local/global ownership guard, and sensitive rendering. Runtime confirmation is intentionally not performed; exact deployed authentication middleware outside this frozen source and whether an attacker can learn a valid order id remain unobserved. Identifier opacity would affect exploitability, not the missing authorization invariant.

- **F3** (`S03`): No application execution is authorized, so the exact database interleaving has not been observed. A reviewer/proof planner should verify two concurrent requests can both read "available" before either status save commits. Any downstream ability to create two orders from the duplicate reservations belongs to the separately assigned orders path and is not claimed here.

- **F4** (`S04`): No application execution was permitted. Confirm framework-default CSRF behavior and whether any external reverse proxy adds authorization; neither is visible in this target path.

- **F5** (`S05`): No runtime request was executed. External authorization outside the frozen source is unknown, and database recovery/cascade effects are not established.

- **F6** (`S06`): No runtime request was executed. External middleware or deployment-layer authorization is not represented in the frozen source and remains unknown.

- **F7** (`S07`): The operator forbids running the application, so no browser execution is observed. A reviewer should confirm effective CSP and deployed Rails rendering behavior; the static source directly shows the escaping bypass.

- **F8** (`S08`): At intake, no discovery or validation had run; generic read-only navigation is available for scheduled investigation. Specialized adapters may add depth where applicable.; Paged lexical search; skipped files/lines and unfinished pages remain visible.; this case has not authorized automatic bounded local proof; Adjudicator did not propose confirmation.; Adjudicator did not propose a static confirmation.

- **F9** (`S09`): No application execution is permitted, so effective cookie SameSite behavior and any upstream Origin/Fetch-Metadata enforcement are unobserved. The GET route is especially relevant because top-level cross-site GET navigation commonly carries Lax cookies.

- **F10** (`S10`): No runtime proof was run, as requested. The exact shell used by Ruby system and deployed process privileges are not observed, although single-string system with metacharacter-containing interpolation is a direct static command-execution path.

- **F11** (`S11`): At intake, no discovery or validation had run; generic read-only navigation is available for scheduled investigation. Specialized adapters may add depth where applicable.; Paged lexical search; skipped files/lines and unfinished pages remain visible.; source path is not an in-scope regular file; this case has not authorized automatic bounded local proof; Role reported blocked: The frozen source proves the local GET-to-lookup-to-destroy chain, but it does not prove the browser will attach the victim's authenticated session on the alleged cross-site top-level GET, because effective SameSite/session-cookie settings and any deployment-level origin enforcement are not established. No runtime observation is allowed. The inspected review index also does not expose review IDs, so attacker acquisition of a victim-owned ID remains an unestablished prerequisite. These are missin; Independent skeptical review was unavailable or incomplete.; Adjudicator did not propose confirmation.; Adjudicator did not propose a static confirmation.

- **F12** (`S12`): No runtime request was made. Deployment DNS, network egress, metadata-service protections, wget version/protocol behavior, redirect policy, and whether a non-image blob can be directly retrieved are unobserved.

- **F13** (`S13`): At intake, no discovery or validation had run; generic read-only navigation is available for scheduled investigation. Specialized adapters may add depth where applicable.; Paged lexical search; skipped files/lines and unfinished pages remain visible.; this case has not authorized automatic bounded local proof; Role reported blocked: The critical transformation and protection edges are not established: the frozen target pins Devise 4.9.4 at Gemfile.lock:107 but does not contain that dependency's sanitizer or update_without_password implementation. Therefore the evidence does not show whether account_update defaults include email/password/password_confirmation after the application's permit call, whether permit appends or replaces those defaults in this version, whether update_without_password persists those attributes under ; Independent skeptical review was unavailable or incomplete.; Adjudicator did not propose confirmation.; Adjudicator did not propose a static confirmation.

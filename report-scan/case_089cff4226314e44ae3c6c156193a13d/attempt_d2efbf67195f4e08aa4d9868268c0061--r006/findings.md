# Author-audited Finding entries

Original VFA statuses and later author audit are distinct. These are summaries, not complete original exports.

## F1 — zipslip-exported-activity-unconfined-entry

- Path group: `D01`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: Exported ZipSlipActivity reads zip_path and writes archive entry names without confinement. A readable supplied archive and writable resolved path are prerequisites.
- Reviewer counterevidence: When zip_path is absent, onCreate uses createDemoZip(), whose only entry is fixed as readme.txt. Android app sandboxing also limits the ultimate writable scope. Neither condition confines entry names for a supplied readable archive, and no canonical-path, prefix, or descriptor-relative guard appears in the inspected unzip flow.
- Negative control: A same-path ZIP containing only readme.txt should write solely to cache/unzipped/readme.txt; launching without zip_path should select the internally generated benign readme.txt archive.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F2 — insecure-file-ui-path-traversal-read

- Path group: `D02`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: The local UI filename reaches FileInputStream under getFilesDir without canonical confinement. The inspected handler does not accept an external filename Intent extra.
- Reviewer counterevidence: The UI handler rejects an empty filename, and read failures are caught rather than crashing. The inspected onCreate and lambda path does not read an Intent extra, so an external application cannot be said from these bytes alone to choose the path programmatically. No final-object confinement guard was observed.
- Negative control: A simple in-root filename opens only the benign getFilesDir() marker; a canonicalized implementation rejecting paths whose canonical target is outside getFilesDir() would return an error for the traversal input.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F3 — sql-search-unparameterized-rawquery

- Path group: `D03`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: The local search UI concatenates text into rawQuery without selectionArgs. Query manipulation is supported statically; external-app injection is not established.
- Reviewer counterevidence: The click handler rejects an empty query, and performVulnerableSearch catches exceptions; neither preserves the scalar-value invariant. rawQuery receives null selectionArgs. No same-path parameterized query or input sanitizer was found in the inspected class. The external-app aspect is narrower than direct intent injection: export permits activity launch, but the inspected path sources the SQL value from the UI EditText.
- Negative control: Entering admin follows the same button and rawQuery path but contains no SQL metacharacter; it should display only the admin row. An empty string is a blocked control because the length guard should prevent performVulnerableSearch.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F4 — insecure-file-world-readable-secret

- Path group: `D04`; VFA status: `inconclusive`; author audit: `unresolved`
- Audit rationale: Manifest targetSdkVersion 34 and Android runtime policy may reject legacy world-readable mode; static calls alone do not establish cross-app readability.
- Reviewer counterevidence: The method wraps the whole sequence in an exception handler. The shipped manifest observation reports targetSdkVersion 34, which is a material guard question for legacy MODE_WORLD_READABLE behavior. The static target does not show another app successfully opening the file, and the file's parent app-data directory may remain inaccessible despite a leaf permission change.
- Negative control: The same target-SDK-34 build reports a SecurityException or the separate app receives access denied; a MODE_PRIVATE file must also remain unreadable.
- PoC: `draft_only`, execution `not_run`; runtime `not recorded`

## F5 — intent-redirection-exported-nested-intent-launch

- Path group: `D05`; VFA status: `inconclusive`; author audit: `needs_correction`
- Audit rationale: Exported handler launches a non-null nested Intent without a destination allowlist, but no privileged destination or permission bypass is established. Narrow the effect to nested launch.
- Reviewer counterevidence: The method rejects a missing/null forward_intent and Android will still apply destination resolution and platform launch rules. No shipped manifest permission protects the entry, and no same-path code-level caller check or destination allowlist appears before startActivity. The provider is static and did not execute the APK.
- Negative control: The same outer launch without forward_intent follows the observed null branch, displays the instruction message, and does not call startActivity; a controlled safe build with a destination allowlist should reject a non-allowlisted nested Intent.
- PoC: `draft_only`, execution `not_run`; runtime `not recorded`

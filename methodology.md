# Case selection and audit method

## Selection and provenance

This is a purposive development case series, not a held-out benchmark or a matched comparison with other agent CLIs. The [attempt register](attempts.csv) contains all 147 retained attempts for seven frozen target identities, including stopped and failed attempts: 303 export revisions and 16 attempts without an export. The latest attempt using each route's frozen question is primary, even when its latest export is partial. An earlier complete attempt with the same question is a separate companion for ASAR only. A resumed run remains one attempt; a re-export is a revision, not another scan.

Question and read-only authorization fields are in `attempts.csv`. One historical question contained an absolute local path. That path is replaced with `[private local path]`; `question_original_sha256` identifies the original private question text. Two distinct authorization phrasings and several component labels were normalized for this archive. `authorization_statement_original_sha256` identifies the original wording, while the recorded component hashes preserve component identity. These display changes do not alter the retained scan records or their case and attempt IDs. The selected [report summaries](report-scan/) retain the original report JSON digest but are not byte-identical VFA exports. `workflow-attempts.csv` and `workflow-candidates.csv` derive chronology from the retained journal. A timestamp for a partial export is a bound, not a completed-report time.

## Units and author audit

A Finding entry is one row in an export. A candidate is a proposed claim before a canonical decision. A path group is the author's grouping of entries by root cause, sensitive operation, and security effect. Two entries can share a group when different commands or sources converge on the same operation and effect; different operations or effects remain separate. Grouping does not alter the VFA verdict in the original export. The [claim audit](claim-audit.csv) records each entry's original status, author label, path group, rationale, reviewer counterevidence, negative control, proof gap, and PoC state.

The author applied these labels to the qualified static claim in each row:

- `supported`: the recorded original location, controlled input, guard, sensitive operation, and stated effect form a coherent static path under the stated prerequisites. This is not an observed exploit.
- `needs_correction`: a supported core exists, but the stated scope, impact, proof, or duplicate count needs a material correction. The correction is recorded in the row rationale.
- `unresolved`: a concrete prerequisite, reachability step, or observation is missing, so the static claim cannot be accepted at the stated scope.
- `unsupported`: contradictory evidence defeats the claim. No selected entry received this label.

A path group is counted as conditionally supported if it contains at least one `supported` entry. This rule yields 34 groups and 26 conditionally supported groups from 42 Finding entries; five groups mix `supported` and `needs_correction`, while two groups contain only `needs_correction`. These are descriptive counts, not a precision, recall, or exploit-success metric. The author audit was AI-assisted and non-blinded; it was not an independent external vulnerability review. The separately scheduled VFA reviewer is a distinct work item within VFA, not an external human reviewer.

The author checked cited original coordinates and retained Evidence hashes in the selected exports. The 314 positive historical citation/hash checks establish reference integrity at the checked locations. They do not prove the source-to-sink reasoning or runtime effect. The separate [directed checker study](evidence-contract/) contains 86 current-code mutation cases; it is not a re-run of the historical scans.

## Distribution and replay boundary

The public report summaries index original coordinates, Evidence IDs, Findings, Coverage gaps, and PoC states without distributing target excerpts or original runnable proofs. The original scan reports, state, journal, checker inputs, and raw results are retained outside this repository. These tables support count and provenance inspection, but they do not permit independent full replay. No target program or PoC was executed as part of this dossier preparation.

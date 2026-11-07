# Author-audited Finding entries

Original VFA statuses and later author audit are distinct. These are summaries, not complete original exports.

## F1 — elf-logit-second-stage-format-string

- Path group: `E01`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: Disassembly at 0x400aeb shows fprintf receiving an actor-influenced formatted buffer as its format argument. Static format interpretation is established; runtime output and stronger effects are not.
- Reviewer counterevidence: parser limits each fgets read to 0x7f bytes, logit limits snprintf output to 0x800 bytes, parser requires a previously nonempty username, and main selects /dev/null as output when no argument is supplied. These controls reduce overflow/output visibility but do not defeat the same-path format-authority violation because fprintf still receives the completed actor-influenced buffer as its format operand. Static analysis does not establish service exposure, libc behavior for a chosen directive, or a runtime memory disclosure/write.
- Negative control: With the same `--test` invocation and protocol sequence, an alphanumeric login marker containing no `%` is printed literally; as an additional blocked-output control, omitting `--test` should leave the log stream directed to /dev/null even though the sink remains reached.
- PoC: `published`, execution `not_run`; runtime `not_performed`

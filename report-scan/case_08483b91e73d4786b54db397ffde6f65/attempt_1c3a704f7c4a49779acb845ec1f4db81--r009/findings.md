# Author-audited Finding entries

Original VFA statuses and later author audit are distinct. These are summaries, not complete original exports.

## F1 — trun-function3-stack-overflow

- Path group: `P01`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: TRUN reaches Function3 strcpy into a 2008-byte stack local without a matching bound. Static out-of-bounds write only.
- Reviewer counterevidence: recv itself is capped at the allocated 0x1000-byte input buffer, and TRUN without a dot never calls Function3. Short, NUL-terminated TRUN commands that fit in 2008 bytes traverse the same call safely. No dominating length check against 2008 was observed before the call.
- Negative control: A short NUL-terminated 'TRUN .SAFE' command reaches the same Function3 strcpy but fits within the 2008-byte local and should return the normal TRUN completion response if runtime prerequisites are met.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F2 — gmon-lter-function3-stack-overflow-variants

- Path group: `P02`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: GMON and LTER have distinct entry guards but converge on the same Function3 strcpy and stack-write effect. Retain both source variants in one sink/effect group.
- Reviewer counterevidence: GMON without '/' or with length at most 0xf6e does not call Function3; LTER without '.' does not call it. Short dot-bearing LTER is a same-path safe control. No length guard at or below 2007 dominates either admitted call.
- Negative control: A short NUL-terminated 'LTER .SAFE' reaches the same Function3 call but fits; a NUL-terminated GMON input at or below 0xf6e with '/' should not call Function3.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F3 — gmon-lter-function3-stack-overflow-variants

- Path group: `P02`; VFA status: `inconclusive`; author audit: `needs_correction`
- Audit rationale: Repeats F2 GMON and LTER variants at the same Function3 sink. Its inconclusive VFA status remains recorded, but it is not a second path.
- Reviewer counterevidence: GMON without '/' or at length <=0xf6e and LTER without '.' do not reach Function3; short dot-bearing LTER is a same-path safe control.
- Negative control: Short 'LTER .SAFE' reaches the same sink and fits; GMON with '/' at or below 0xf6e does not call Function3.
- PoC: `draft_only`, execution `not_run`; runtime `not recorded`

## F4 — vulnserver-kstet-function2-stack-overflow

- Path group: `P03`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: KSTET reaches Function2 strcpy into a 72-byte stack local; the fixed 100-byte intermediate is not an adequate bound for that destination.
- Reviewer counterevidence: The KSTET caller allocates exactly 100 bytes and uses strncpy with count 100, so that first destination is not overrun by the fixed-count copy. For an input of at most 71 non-NUL bytes total, zero padding supplies a terminator and _Function2's 72-byte stack destination can hold the string plus NUL. No callee-side bound check was observed.
- Negative control: A KSTET input containing at most 71 non-NUL bytes total follows the same branch, is NUL-padded by strncpy, and fits the 72-byte stack array including the terminator.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F5 — vulnserver-gter-function1-stack-overflow

- Path group: `P04`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: GTER reaches Function1 strcpy into a 152-byte stack local; the fixed 180-byte intermediate is not an adequate bound for that destination.
- Reviewer counterevidence: The GTER caller allocates exactly 0xb4 bytes and uses strncpy with count 0xb4, so that first destination is not overrun by the fixed-count copy. For an input of at most 151 non-NUL bytes total, strncpy zero-padding supplies a terminator and _Function1's 152-byte stack destination can hold the string plus NUL. No callee-side bound check was observed.
- Negative control: A GTER input containing at most 151 non-NUL bytes total follows the same branch, is NUL-padded by strncpy, and fits the 152-byte stack array including the terminator.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F6 — vulnserver-trun-function3-stack-overflow

- Path group: `P01`; VFA status: `confirmed`; author audit: `needs_correction`
- Audit rationale: Repeats F1 TRUN input, Function3 strcpy sink, and stack-write effect. Keep the additional Evidence as corroboration.
- Reviewer counterevidence: A first request shorter than 0x1000 is followed by zeros from the handler's initial memset, so a bounded short TRUN string is terminated; strncpy also caps the intermediate copy at 3000. Those controls prevent unlimited source reads but do not protect the smaller 2008-byte Function3 destination. TCP segmentation and later-request stale bytes remain runtime variables.
- Negative control: A first-request TRUN string of at most 2007 non-NUL bytes total, still containing '.', follows the same dispatch and helper path but fits local_7dc including its NUL terminator.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F7 — vulnserver-gmon-threshold-function3-stack-overflow

- Path group: `P02`; VFA status: `confirmed`; author audit: `needs_correction`
- Audit rationale: GMON is already covered by F2 at Function3. Additionally, the published F7 reproducer failed its recorded Python syntax check; do not call it syntax-valid.
- Reviewer counterevidence: The slash scan and >0xf6e check restrict reachability, and a first recv shorter than 4096 is NUL-terminated by the buffer's prior zero fill. Neither is protective: the length threshold itself implies at least 3951 source bytes versus a 2008-byte destination. A GMON message of length 3950 or less does not call the helper.
- Negative control: A 3950-byte first-request GMON string containing '/' follows the same prefix and slash scan but fails the strict >0xf6e threshold and therefore does not call _Function3.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F8 — vulnserver-lter-function3-stack-overflow

- Path group: `P02`; VFA status: `inconclusive`; author audit: `needs_correction`
- Audit rationale: LTER is already covered by F2 at Function3. Its inconclusive adjudication does not create another distinct sink/effect.
- Reviewer counterevidence: For a first recv shorter than 4096, the initial zero fill supplies termination, and the intermediate allocation is 4096 bytes. These controls can keep the transform in its own buffer for the bounded test, but they do not reconcile that string with Function3's 2008-byte destination. An exact 4096-byte unterminated receive may create an earlier read/write issue, but that distinct condition is not required for this claim.
- Negative control: A 2007-byte first-request LTER string with the same prefix and period follows the same transform, scan, and helper call while fitting the 2008-byte destination including NUL.
- PoC: `draft_only`, execution `not_run`; runtime `not recorded`

## F9 — hter-function4-stack-overflow

- Path group: `P05`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: HTER decodes input before Function4 strcpy into a 1016-byte stack local. Static out-of-bounds write only.
- Reviewer counterevidence: For a recv shorter than 0x1000, the initially zeroed command buffer supplies a terminator; decoding two characters into one byte means the 0x800-byte heap buffer is large enough for the maximum normally terminated command. Decoded zero bytes also terminate strcpy early. These controls do not protect _Function4 when the attacker uses more than 1015 nonzero decoded bytes. A full 0x1000-byte recv has no inserted terminator and may make the decoder read beyond the command allocation, but that separate conditional behavior is not needed for this claim.
- Negative control: The same HTER route with 1015 decoded nonzero bytes leaves the next zeroed heap byte as the terminator, so strcpy copies exactly 1016 bytes including NUL and stays within local_3fc[1016].
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F10 — vulnserver-full-recv-gmon-unterminated-strlen-oob-read

- Path group: `P06`; VFA status: `inconclusive`; author audit: `unresolved`
- Audit rationale: A full 4096-byte non-NUL receive can remove the zero terminator before GMON strlen; the record does not observe the exact out-of-bounds access or resulting fault.
- Reviewer counterevidence: The receive buffer is zeroed before the receive loop, fixed-width strncmp dispatch reads only 4-6 bytes, the GMON slash search is bounded by local_10 (0x1000), and recv results below 1 close the connection. These controls protect short first receives and the prefix checks, but no observed instruction reserves space, rejects recv_count == 0x1000, or appends a NUL before strlen. Buffer reuse on later loop iterations is a separate complication and was not needed for this first-request candidate.
- Negative control: On a fresh connection, a 4095-byte otherwise identical non-NUL GMON request leaves byte 4095 as zero from the initial memset, so strlen remains within the allocation and the out-of-bounds-read observation should be absent.
- PoC: `draft_only`, execution `not_run`; runtime `not recorded`

## F11 — vulnserver-hter-function4-stack-overflow

- Path group: `P05`; VFA status: `confirmed`; author audit: `needs_correction`
- Audit rationale: Repeats F9 HTER decode, Function4 strcpy sink, and stack-write effect. Keep its Evidence, not another count.
- Reviewer counterevidence: ConnectionHandler allocates and zeroes 0x800 bytes for decoded HTER data, and on a normally NUL-terminated receive buffer the pairwise decoder cannot exceed that heap allocation. This is not a same-path defense for Function4: its stack destination is only 1,016 bytes and strcpy has no length argument. The separate full-size-recv/no-NUL case was not needed for this claim.
- Negative control: The same HTER framing with 1,015 '41' pairs yields 1,015 decoded 'A' bytes plus one NUL, exactly fitting local_3fc[1016], and should return normally absent an independent defect.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F12 — vulnserver-full-recv-lter-unterminated-transform-oob

- Path group: `P07`; VFA status: `inconclusive`; author audit: `unresolved`
- Audit rationale: A full non-NUL receive can let the LTER transform cross a buffer edge; exact read/write behavior and fault remain unobserved. This is a different sink from Function3.
- Reviewer counterevidence: The receive buffer is initially zeroed, LTER dispatch uses a fixed five-byte strncmp, the destination is also zeroed, and the later dot scan has an explicit index < 0x1000 bound. Those controls make a fresh 4095-byte request safely terminated by the untouched final zero and bound the later scan, but the transform itself has no capacity comparison and a 4096-byte receive overwrites every initialized zero.
- Negative control: On a fresh connection, a 4095-byte otherwise identical LTER request leaves local_14[4095] zero from the initial memset, so the transform stops before either allocation boundary and no out-of-bounds access is observed.
- PoC: `draft_only`, execution `not_run`; runtime `not recorded`

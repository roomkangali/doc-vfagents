# Author-audited Finding entries

Original VFA statuses and later author audit are distinct. These are summaries, not complete original exports.

## F1 — reports-export-shell-command-injection

- Path group: `M01`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: IL and decompiled body show user title concatenated into /bin/sh -c and Process.Start. Deployment of the controller and shell availability are untested prerequisites.
- Reviewer counterevidence: The executable and base command are fixed, and the input is placed between double quotes. Those constraints narrow the primitive but do not neutralize shell command substitution or quote termination. The frozen DLL does not establish endpoint registration, global authorization, input binding, /bin/sh availability, or process-start policy; any of those could prevent a remote trigger.
- Negative control: A same-path plain title such as VFA_SAFE_TEXT returns only the literal echoed text and performs no additional shell expansion; if the route is blocked or /bin/sh is unavailable, neither input launches and the reachability prerequisite is disproved.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F2 — checkout-place-client-unit-price-controls-persisted-total

- Path group: `M02`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: Place multiplies DTO UnitPrice by Quantity and saves Order.Total; the server product lookup supplies Name but not Price. Billing consequences remain conditional.
- Reviewer counterevidence: The method does perform a server-side Products.Find lookup using ProductId and uses the Product.Name (or 'unknown') for Order.Item, which is a guarded look-alike for server-derived product data. However, the complete decompiled Place body does not read Product.Price; the Product model has a Price property, and the caller DTO's UnitPrice is used directly. Unknown global MVC filters, model validators, database constraints, authentication, and downstream recalculation remain possible external defeaters because dependencies and host configuration were not inspected or executed.
- Negative control: With the same ProductId and Quantity but UnitPrice exactly equal to the server-side Product.Price, the action follows the same path and stores Product.Price*2; if a global guard exists, the mismatched positive should instead be rejected or normalized while this control succeeds.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F3 — invoices-download-path-confinement

- Path group: `M03`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: Download combines Root with caller name and reads the result without canonical containment. Fixed-control DLL adds a root-prefix check, but was not supplied to VFA.
- Reviewer counterevidence: File.Exists gates the read and missing paths return NotFound, but existence is not confinement. No same-body canonical-path or root-containment check was observed. A global authorization filter, route restriction, trusted-only caller, runtime path policy, or deployment filesystem confinement could defeat or narrow the actor claim and was not established by the frozen DLL inspection.
- Negative control: The same action with 'inv-1001.txt' should return only the seeded in-root invoice; a nonexistent traversal target should take the NotFound branch. If routing or authorization blocks both inputs, the actor/reachability premise is not established.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F4 — import-xml-external-entity-resolution

- Path group: `M04`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: XML action configures DTD parsing and XmlUrlResolver before XmlDocument.Load. External entity effects depend on deployed host/resolver access.
- Reviewer counterevidence: The frozen DLL does not establish that the containing host registers controllers, exposes POST /import/xml to the stated actor, omits a global authorization gate, or permits the resolver to access a chosen URI. Runtime policy, container isolation, URI scheme restrictions, or an upstream request filter could prevent the downstream effect. The inspected method nevertheless contains no same-path Prohibit/null-resolver guard; both resolver assignments are explicit in its original CIL.
- Negative control: A plain body such as <root>safe</root> follows the same action and returns only safe. A genuinely guarded look-alike configured with DtdProcessing.Prohibit and XmlResolver=null should reject the DOCTYPE or leave the external entity unresolved; no such target method was established here.
- PoC: `published`, execution `not_run`; runtime `not_performed`

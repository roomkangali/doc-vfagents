# Author-audited Finding entries

Original VFA statuses and later author audit are distinct. These are summaries, not complete original exports.

## F1 — products-search-sqli

- Path group: `S01`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: The active find_by_sql interpolates the request term; the adjacent parameterized example is commented out. Predicate manipulation is the supported effect, not stacked statements.
- Reviewer counterevidence: A safe placeholder-based Product.where query is present immediately above the sink, but it is commented out and therefore does not protect the active find_by_sql call. Rails/ActiveRecord may constrain stacked statements, so this evidence supports predicate manipulation and row disclosure, not arbitrary write or code execution.
- Negative control: Replace the active line with the shown placeholder-based Product.where form and supply the same term; it remains a bound LIKE value and cannot change predicate structure.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F2 — orders-view-unscoped-idor-sensitive-financial-disclosure

- Path group: `S02`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: The routed view uses global Order.find and renders financial fields; sibling order actions use current_user.orders.find as a meaningful negative control.
- Reviewer counterevidence: The other order workflow actions use current_user.cart and current_user.orders; in particular get_check and create scope session[:order_id] through current_user.orders.find, showing a same-controller ownership control. That control is absent from view, which uses global Order.find. Rails' default CSRF protection is irrelevant to this read-only GET disclosure.
- Negative control: After replacing Order.find(params[:id]) with current_user.orders.find(params[:id]) and requiring authentication, user A receives the order while no-session and user-B requests are denied or uniformly not found; a nonexistent id is also not disclosed.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F3 — cart-add-toctou-duplicate-reservation

- Path group: `S03`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: The availability read, cart-item creation, and product status update have no shared transaction or lock. This supports a possible concurrent interleaving only; no duplicate was observed.
- Reviewer counterevidence: All cart actions require authentication, add always selects current_user.cart, remove resolves cart_item through current_user.cart, and a sequential second add after status becomes in_cart takes the rejection branch. These controls prevent unauthenticated use and direct cross-cart removal, but they do not make the availability check and writes atomic. The schema has only separate non-unique indexes on cart_id and product_id.
- Negative control: Send the same two authenticated add requests sequentially after the first completes; the second should follow the "Gem cannot be added" branch and create no second cart_item.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F4 — products-unauthenticated-create

- Path group: `S04`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: The create route and save have no authentication or role guard. Strong parameters limit fields but do not authorize callers.
- Reviewer counterevidence: product_params is an effective field allowlist and excludes status/secret, but it does not check identity or role. Rails CSRF protection may block a cross-site forged POST, but it is not caller authorization and public form/session token availability has not been runtime-tested.
- Negative control: Add authenticate_user! plus an administrator-role check before create; the same anonymous request is rejected before Product.new/save.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F5 — products-unauthenticated-destroy

- Path group: `S05`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: The destroy route reaches Product.find and destroy! without an authentication or role guard; CSRF protection is a separate boundary.
- Reviewer counterevidence: The callback requires an existing id and Rails CSRF protection may resist cross-site forgery, but neither is caller authorization; no current-user scope, role check, or policy precedes destroy!.
- Negative control: Add authenticate_user! and an administrator policy before set_product/destroy; the same anonymous DELETE is rejected and the row remains.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F6 — products-unauthenticated-update

- Path group: `S06`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: The update route reaches Product.find and update without an authentication or role guard; strong parameters narrow mutable fields.
- Reviewer counterevidence: The callback centralizes lookup and product_params restricts mutable fields; neither scopes by current_user nor checks a role. Rails CSRF protection may block cross-site forgery but not a direct unauthorized caller with a valid token/session.
- Negative control: Add authenticate_user! and an administrator policy before set_product/update; the same anonymous request is rejected and the record remains unchanged.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F7 — reviews-stored-xss-html-safe

- Path group: `S07`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: An authenticated user controls review body; the public view renders body.html_safe. The shipped CSP initializer is commented out; browser execution remains unobserved.
- Reviewer counterevidence: Creation requires user_signed_in? and binds the new review to current_user. The model validates rating range and body presence. These controls restrict record creation and shape but do not sanitize body HTML or protect the public render sink.
- Negative control: A same-path plain-text review or the same payload rendered with normal ERB escaping should display literal markup and must not set the DOM marker.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F8 — cart-add-bypasses-secret-product-filter

- Path group: `S08`; VFA status: `inconclusive`; author audit: `unresolved`
- Audit rationale: The cart action omits the index secret filter, but no available secret product or confidentiality rule is established. The existence and security meaning of the hidden state remain open.
- Reviewer counterevidence: The cart endpoint requires authentication, binds the new item to current_user.cart, and rejects products whose status is not available. The source tree contains no seed file proving that an available secret product exists, and the meaning of secret could be presentation-only rather than an authorization boundary. Separately assigned product routes may expose the same record and must be assessed independently.
- Negative control: A non-secret available product follows the same add/cart path and is both listed and rendered; a secret product with status other than available is rejected by the existing status guard.
- PoC: `draft_only`, execution `not_run`; runtime `not recorded`

## F9 — reviews-create-csrf-get-and-token-skip

- Path group: `S09`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: GET /reviews/create is state-changing and verification is skipped. Authentication and owner scoping remain effective; cross-site browser delivery was not tested.
- Reviewer counterevidence: The action requires user_signed_in?, and the record is built through current_user.reviews, so anonymous requests do not create a review and the record is attributed only to the authenticated victim. Rating range/body-presence validation limits shape, not request intent.
- Negative control: The same request while logged out must redirect without creation; after removing the GET route and token skip, a tokenless cross-site request must be rejected without creating a record.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F10 — user-avatar-url-shell-command-injection

- Path group: `S10`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: The authenticated account-update path inserts avatar_url into a single-string shell command. This supports conditional command interpretation, not an observed command run.
- Reviewer counterevidence: The Devise registration flow is an authenticated account-update surface, and blank avatar_url values are rejected at both controller presence and model blankness checks. Those controls reduce reachability but do not neutralize shell metacharacters in a nonblank URL. The ordinary database update is delegated to super only after import_avatar_from_url has already executed.
- Negative control: On the same authenticated update path, a metacharacter-free URL such as `https://example.invalid/image.jpg` should only form the wget invocation and should not create the marker; a blank avatar_url should avoid import_avatar_from_url entirely.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F11 — reviews-destroy-get-csrf

- Path group: `S11`; VFA status: `inconclusive`; author audit: `unresolved`
- Audit rationale: GET destruction is present, but the action scopes lookup to current_user.reviews and effective victim-cookie/browser delivery was not observed.
- Reviewer counterevidence: The lookup is correctly scoped through current_user.reviews, so an authenticated user cannot use this action to delete another user's review. An unauthenticated request is expected to fail or error because current_user is absent. These facts narrow the impact but do not establish intent for the victim's own deletion.
- Negative control: A different user's review ID must not be deleted because the scoped lookup should fail; after conversion to a token-protected DELETE/POST route, a tokenless cross-site request must not delete the victim's review.
- PoC: `draft_only`, execution `not_run`; runtime `not recorded`

## F12 — user-avatar-url-unrestricted-server-fetch-ssrf

- Path group: `S12`; VFA status: `confirmed`; author audit: `supported`
- Audit rationale: The same authenticated avatar URL reaches server-side wget without a destination allowlist. This is a distinct outbound-request effect from S10; network reachability is not observed.
- Reviewer counterevidence: The actor must reach an authenticated Devise account-update flow, and a blank value is rejected. The layout renders the result as an image, which may not visibly display non-image response bodies. These constraints do not restrict the server-side destination or prevent response persistence.
- Negative control: A metacharacter-free benign external test URL exercises the same fetch path but contacts only that nominated host; with an effective private/link-local destination guard added, the loopback URL should be rejected before wget runs.
- PoC: `published`, execution `not_run`; runtime `not_performed`

## F13 — devise-account-update-without-current-password

- Path group: `S13`; VFA status: `inconclusive`; author audit: `unresolved`
- Audit rationale: The override calls update_without_password, but the effective Devise parameter allowlist and credential-update behavior have not been established from this record.
- Reviewer counterevidence: The rendered edit form exposes only profile fields and hides email as readonly, so ordinary UI use does not present password controls; however a client can craft request parameters. Strong parameters may defeat the claim if Devise's effective account_update allowlist excludes email/password or the method applies an independent reauthentication guard. Avatar_url-present updates call super instead, so this hypothesis is limited to the no-avatar_url branch.
- Negative control: The same credential-change parameters through the superclass update_resource path, or a modified override using update_with_password, fail without the correct current_password.
- PoC: `draft_only`, execution `not_run`; runtime `not recorded`

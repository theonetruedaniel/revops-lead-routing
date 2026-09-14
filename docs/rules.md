# Routing policy for this sample

These rules define the synthetic work sample. They are not an export of an employer's production configuration.

## Order of decisions

1. Normalize event ID whitespace and email whitespace/case. A repeated nonempty event ID produces `duplicate_event`, even when its payload changes. Record first-seen nonempty event IDs before validating the payload.
2. Missing event ID or an email that fails a basic format check produces `manual_review`. The format check does not establish deliverability.
3. A previously seen normalized email produces `existing_contact`. No second sequence is assigned. The first valid identity is retained even if later qualification sends it to review.
4. An unsupported source produces `manual_review`. Supported sources are `facebook`, `app_install` and `website`.
5. Explicit `website_fit=fail` produces `disqualified`, including when traffic is unknown.
6. Unknown fit or traffic other than a nonnegative integer produces `manual_review`.
7. A passing fit and valid traffic qualify for the corresponding sequence below.

## Traffic tiers

| Monthly visits | Sequence | Owner queue |
|---|---|---|
| 0 through 499 | starter | sales_queue |
| 500 through 1,999 | growth | sales_queue |
| 2,000 through 4,999 | scale | sales_queue |
| 5,000 or more | strategic | strategic_queue |

Review cases use `review_queue`. Existing contacts use `existing_owner` as a placeholder; duplicate events and disqualified leads use `none`. All nonqualified rows have sequence `none`.

Input order determines the first event and contact. Each invocation starts with empty deduplication state. Updating a contact after new enrichment is outside this sample's scope.

## Verification approach

`data/expected.csv` contains independently specified outcomes, including traffic boundaries and competing signals. `verify_sample.py` compares the generated output by case order, identifier, decision, sequence and owner. `test_routing.py` probes boundaries and malformed values beyond the CSV examples.

Edit a traffic value across a boundary, rerun the router and then run verification: an unchanged expectation should fail. Update expectations only when intentionally changing the policy or fixture, with an explanation of the business reason.

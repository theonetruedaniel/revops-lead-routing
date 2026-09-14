# Sample verification

Synthetic data only; this measures agreement with the demo rules.

Rows compared: 24. Mismatches: 0.

| Case | Expected decision / sequence | Actual decision / sequence | Match |
|---|---|---|---|
| 01 | qualified / starter | qualified / starter | PASS |
| 02 | qualified / starter | qualified / starter | PASS |
| 03 | qualified / growth | qualified / growth | PASS |
| 04 | qualified / growth | qualified / growth | PASS |
| 05 | qualified / scale | qualified / scale | PASS |
| 06 | qualified / scale | qualified / scale | PASS |
| 07 | qualified / strategic | qualified / strategic | PASS |
| 08 | qualified / strategic | qualified / strategic | PASS |
| 09 | disqualified / none | disqualified / none | PASS |
| 10 | manual_review / none | manual_review / none | PASS |
| 11 | manual_review / none | manual_review / none | PASS |
| 12 | manual_review / none | manual_review / none | PASS |
| 13 | manual_review / none | manual_review / none | PASS |
| 14 | manual_review / none | manual_review / none | PASS |
| 15 | manual_review / none | manual_review / none | PASS |
| 16 | manual_review / none | manual_review / none | PASS |
| 17 | duplicate_event / none | duplicate_event / none | PASS |
| 18 | existing_contact / none | existing_contact / none | PASS |
| 19 | manual_review / none | manual_review / none | PASS |
| 20 | manual_review / none | manual_review / none | PASS |
| 21 | disqualified / none | disqualified / none | PASS |
| 22 | qualified / starter | qualified / starter | PASS |
| 23 | qualified / growth | qualified / growth | PASS |
| 24 | qualified / scale | qualified / scale | PASS |

Owner assignment is also checked against expected.csv. No CRM writes, messages or enrichment calls occur.

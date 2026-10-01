# RevOps lead routing: an inspectable work sample

**24 fictional intake rows → documented decisions → checked results.**

This small Python project demonstrates how I translate lead qualification requirements into routing rules, handle incomplete data and verify the output. It reconstructs a narrow part of workflows I worked on at AdScale, using synthetic data and illustrative policies.

**Daniel Abrams** · [Portfolio](https://theonetruedaniel.github.io/) · [LinkedIn](https://www.linkedin.com/in/danielmabrams/)

## Review in two minutes

1. Read the [routing rules](docs/rules.md).
2. Compare the [fictional inputs](data/leads.csv) with the [hand-authored expectations](data/expected.csv).
3. Inspect [actual output](results/actual.csv) and the [row-by-row verification](results/verification.md).

The sample covers Facebook, app-install and website intake; traffic tiers; failed fit; missing enrichment; event replay; and normalized contact deduplication. It outputs queue and sequence labels only. It performs no CRM writes, enrichment requests or outreach.

## Run it

Use Python 3.10 or newer. No packages or credentials are needed.

```sh
python route_leads.py
python verify_sample.py
python -m unittest -v
```

Run these commands from the repository directory. The first two regenerate the CSV and Markdown results. Verification exits with a nonzero status if the output differs from the expected decisions, sequences or owners.

## Example decisions

| Input | Result |
|---|---|
| Fit passes; 499 visits/month | Starter sequence, sales queue |
| Fit passes; 500 visits/month | Growth sequence, sales queue |
| Fit passes; 5,000 visits/month | Strategic sequence, strategic queue |
| Fit fails; 9,000 visits/month | Disqualified; no sequence |
| Traffic unknown | Manual review; no sequence |
| Replayed event identifier | Duplicate event; no second route |

## What this demonstrates

- Translating a business process into explicit, ordered rules.
- Preserving uncertainty instead of inventing missing enrichment.
- Checking boundary values and preventing repeated routing within a batch.
- Keeping expected outcomes independent from the implementation.

The initial local run matched **24/24** expected outcomes and passed **8 test methods** covering multiple cases. Those results measure this synthetic sample's behavior, not conversion rates or production reliability.

## Scope and authorship

My AdScale experience supplies the workflow context: webhook intake, traffic enrichment, website-fit review and conditional HubSpot follow-up. I defined this work sample's requirements and reviewed it with AI assistance for implementation, tests and documentation. This repository contains no AdScale source code or customer data.

The exact historical traffic-boundary handling is unconfirmed. These interval definitions, queue names, sequence labels and decision precedence are illustrative. Website fit is a supplied synthetic label; the script does not run an AI assessment. This compact example does not implement phone/country inference, intent scoring or the full multi-agent workflow.

Deduplication is in-memory and batch-local. The first valid contact identity reserves its position, including a contact sent to review; subsequent records do not re-enroll it. A production system would need persistent idempotency, update handling, access control and real provider verification.

Related: [interactive workflow reconstruction](https://theonetruedaniel.github.io/lead-lab/) · [case study](https://gamma.app/docs/q5fun7ugwjj0g9n). The hosted reconstruction is a separate demo with its own illustrative rules.

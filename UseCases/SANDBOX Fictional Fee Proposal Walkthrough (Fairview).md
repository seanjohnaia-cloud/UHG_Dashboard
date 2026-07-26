---
id: SANDBOX-FEE-01
title: Fictional Fee Proposal Walkthrough (Fairview)
status: fictional_sandbox
layer: sandbox
source: UC-001 Incomplete Fee Proposal (method reference, not data)
governed_by: none — non-authoritative, fictional
requested_activity: prepare_grace_architectural_fee_proposal
---

# Fictional Fee Proposal Walkthrough (Fairview)

## Why this exists

Real UC-001 (Muncie) is the actual UHG Fee Proposal exercise, and it is genuinely stuck: readiness is `deficient_but_actionable` and several fields remain open (see `02_Records/UC-001 Incomplete Fee Proposal/readiness-assessment.md`). There isn't enough real project data to walk a Fee Proposal act all the way through and see the whole shape of it.

Fairview is the vault's existing fictional specimen (`fixture_status: fictional_specimen` in `05_Dashboard/test_runs/fairview_project_home_fixture.json`) — already used as the non-authoritative stand-in project for both dashboards. This sandbox reuses it to run the Fee Proposal act to completion, so the *process* can be worked out before real data exists to run it on Muncie or any other project.

**This produces no authority, no client-facing content, and no governed record.** It is a working sandbox for Sean to think through what a Fee Proposal act actually requires.

## Method

Same required-outputs contract as UC-001 (see `UseCases/UC-001 Incomplete Fee Proposal.md`):

- proposal draft
- assumption records
- information-gap records
- risk records
- clarification requests
- readiness assessment

Same governing discipline: extracted values stay `extracted` until validated, inferred positions are assumptions not facts, missing information is a gap record not a blank field, evidence stays traceable.

## What's already known (from the Fairview fixture)

Pulled from `05_Dashboard/test_runs/fairview_project_home_fixture.json` — this is the PAC/origin layer, already populated:

- Project: Fairview Urgent Care, 4210 Preston Commons Blvd, Fairview, TX 75069
- Type / asset: Remodel / Renovation, Urgent Care
- Scope: interior remodel of 1,800 SF retail space into a UHG-branded clinic; no footprint expansion
- Existing S.F. 1,800 / New S.F. 0
- Owner-provided cost of work (AFC): $850,000
- Compensation basis anticipated: Stipulated sum
- Schedule: construction commencement 2026-10-01, substantial completion 2027-02-01, estimated occupancy 2027-03-01
- Consultants: mechanical/electrical/structural not specified by Owner — Basic Services per Article 2.3, to be engaged by Architect
- Owner consultants: none identified at this stage

## What the act still needs

See `information-gaps.md` in this record folder — this is the actual content of the exercise. Everything above is already known; the Fee Proposal act is about producing the values below, not looking them up.

## Records

```text
02_Records/SANDBOX Fictional Fee Proposal Walkthrough (Fairview)/
    readiness-assessment.md
    information-gaps.md
    assumptions.md
    risk-records.md
    clarification-requests.md
    proposal-draft.md
```

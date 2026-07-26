---
record_type: readiness_assessment
status: deficient_but_actionable
use_case: SANDBOX-FEE-01
experiment_focus: Fairview Urgent Care (fictional)
requested_activity: prepare_grace_architectural_fee_proposal
workflow_position: fee_proposal_walkthrough
readiness_status: deficient_but_actionable
service_order_required_now: false
---

# Fairview Fictional Fee Proposal — Readiness Assessment

## Independent State Fields

- `requested_activity`: `prepare_grace_architectural_fee_proposal`
- `workflow_position`: `fee_proposal_walkthrough`
- `readiness_status`: `deficient_but_actionable`
- `service_order_required_now`: `false`

## Assessment

Fairview has a complete PAC/origin layer (project info, scope, square footage, AFC, schedule, basic-services consultants) — see the source fixture. It does not yet have any of the Fee Proposal act's own output content: no proposed fee, no phase breakdown, no Schedule E/F classification, no project/S.O. number, no assigned PM or Architect's Project Representative.

This mirrors real UC-001's structure exactly (Grace-only architectural fee proposal, no Service Order today) but starts from a complete origin record instead of an incomplete client email — the deficiency here is entirely in the fee-proposal output layer, not the source layer.

## Remaining Deficiencies

See `information-gaps.md` for the full list. In brief: proposed fee amount/basis, phase-by-phase fee split, Schedule E/F routing decision, project/S.O. number, PM assignment, Architect's Project Representative, certificate of insurance, consultant fee inputs, reimbursables.

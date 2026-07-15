---
id: UC-001
title: Incomplete Fee Proposal
status: first_executable_slice
layer: operational
source: ../Pii Founding Prompt.md
governed_by: UC-000
requested_activity: prepare_fee_proposal
---

# UC-001 Incomplete Fee Proposal

## Use Case

Prepare a fee proposal from an incomplete project request.

## Input

A real client email with partial scope and no completed service order.

## Required Outputs

Pii must produce:

- proposal draft;
- assumption records;
- information-gap records;
- risk records;
- clarification requests;
- readiness assessment.

## Required State Distinction

Workflow position and information readiness are recorded independently.

The same project can simultaneously have:

```yaml
requested_activity: prepare_fee_proposal
readiness_status: deficient
```

## Governing Constraints

Pii must:

- preserve the client email as a source;
- extract possible project information without making it authoritative;
- record AI-extracted values as `extracted` until human validation;
- record inferred working positions as assumptions, not facts;
- record missing required information as gap records, not blank fields;
- record conflicts as conflict records, not merged records;
- maintain evidence references for every assertion used in the proposal;
- log state transitions with from, to, date, actor, reason, and evidence.

## Smallest Executable Slice

The first implementation should process one real incomplete email end to end and create the minimum operational records necessary to produce the required outputs.

## Stop Condition

When UC-001 works end to end, stop and report:

- what entities reality forced into existence;
- what the founding assumptions got wrong;
- what should be proposed next.

---
record_type: workflow_model_note
status: active_model_candidate
use_case: UC-001
model_scope: recurring_all_projects
---

# SO Matrix Role in Pii

## Core Classification

The SO Development Matrix is not merely a Muncie source file. It is a **working standard exercise** that should become part of Pii's recurring project-intake/proposal workflow.

It is a bridge artifact between:

1. executed contract requirements;
2. material received from UHG;
3. the specific client request/email;
4. project-type deliverables;
5. fee schedule basis;
6. SLA/schedule framework.

## User Explanation

The matrix was sent to the team as a working document. The standard exercise is to scrub contractual requirements against the material received from UHG and the request of the email.

In the Muncie case, because the request was only for a fee proposal for architectural services, the matrix pulled forward:

- deliverables for that Project Type;
- fees from the appropriate schedule;
- SLA framework in order to evaluate the schedule.

## What This Means Architecturally

This reveals that Pii needs a recurring workflow step:

```text
Request Intake → Contract Scrub → Project-Type Deliverables → Fee Basis → SLA/Schedule Evaluation → Proposal Readiness
```

But under the founding prompt, we should not over-abstract yet. For UC-001, the matrix should be implemented as a concrete Muncie workflow artifact first.

## Emerging Entity Candidates

These are candidates, not accepted abstractions yet:

| Candidate Entity | Why Reality Introduced It | Status |
|---|---|---|
| Contract Requirement | The matrix scrubs against executed requirements. | candidate |
| Received Material | UHG materials must be checked against the email and contract. | candidate |
| Request Scope | The email defines the requested activity and scope frame. | candidate |
| Project Type | Deliverables are pulled by project type. | candidate |
| Deliverable Set | Fee proposal depends on selected deliverables. | candidate |
| Fee Schedule Basis | Fee comes from appropriate schedule, not invention. | candidate |
| SLA Framework | Schedule evaluation is contract-linked. | candidate |
| Proposal Readiness | Matrix helps determine whether pricing can proceed or remains deficient. | already_active |

## Current Muncie Boundary

For now, Pii should use the Muncie SO Matrix to understand how a human expert performs the contract scrub for one project.

Do not generalize this into a universal module until the Muncie slice executes end to end.

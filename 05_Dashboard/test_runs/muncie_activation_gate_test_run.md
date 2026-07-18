---
record_type: activation_gate_dashboard_test_run
status: recorded
use_case: UC-001
project: Muncie Family Physicians / IN125
expected_startup_state: startup_blocked
source_dataset: 05_Dashboard/test_runs/muncie_activation_gate_test_run.json
created_date: 2026-07-15
---

# Muncie Activation Gate Dashboard Test Run

## Purpose

Use Muncie Family Physicians / IN125 as the first real project specimen for the approved Activation Gate Dashboard v0.

This test does not change canonical gate structure. It applies the approved fourteen gates to known Muncie records.

## Result

```text
startup_blocked
```

## Why

Muncie is not activation-ready. It is in post-proposal scope negotiation after UHG requested a reduced-AOR discussion.

The fee proposal exercise was actionable, but startup is blocked because authority, NTP/equivalent authorization, accountable ownership, project number/SO, startup-ready scope, fee approval, schedule baseline, risk review, consultant routing, billing path, and firm approval-path governance are not sufficiently confirmed.

## Confirmed Gates

| Gate | Basis |
|---|---|
| A-GATE-001 | Acceptance status is known as not approved / pending post-proposal scope negotiation. |
| A-GATE-009 | Contract path context is identified as UHG MSA / Service Order framework, though no Service Order exists yet. |
| A-GATE-013 | All fourteen gates were evaluated in this test run. |

## Blocking Gates

| Gate | Reason |
|---|---|
| A-GATE-002 | Acceptance authority not confirmed; user is Admin Team, not Clinical/PIC, and cannot commit scope/fee reduction. |
| A-GATE-003 | No NTP, Service Order, PO, or equivalent authorization confirmed. |
| A-GATE-004 | Accountable Clinical/PIC ownership for startup/reduced-AOR response is not confirmed. |
| A-GATE-005 | Project number / S.O. number remains missing. |
| A-GATE-006 | Scope baseline not startup-sufficient; reduced-AOR/direct-to-90% path unresolved. |
| A-GATE-007 | Fee basis not approved for startup; UHG requested review of scope and fees. |
| A-GATE-008 | Schedule baseline not confirmed for reduced-AOR/direct-to-90% path. |
| A-GATE-010 | Insurance/risk requirement relevance not reviewed for startup condition. |
| A-GATE-011 | Consultant/additional-service triggers acknowledged but unresolved/routed incompletely. |
| A-GATE-012 | Billing path not startup-viable/confirmed. |
| A-GATE-014 | Firm approval-path governance not satisfied; constitutional dependency remains open. |

## Decision Records / Overrides

No overrides were recorded for this test run.

Therefore blocked gates remain blocked and the output state is:

```text
startup_blocked
```

## Evidence Sources

- `02_Records/UC-001 Incomplete Fee Proposal/readiness-assessment.md`
- `02_Records/UC-001 Incomplete Fee Proposal/muncie-service-order-preparation-record.md`
- `02_Records/UC-001 Incomplete Fee Proposal/authority-and-response-governance.md`
- `02_Records/UC-001 Incomplete Fee Proposal/post-proposal-review-analysis-reduced-aor.md`
- `02_Records/UC-001 Incomplete Fee Proposal/client-sent-output-analysis-muncie.md`

## Dashboard Lesson

The Muncie test confirms why the dashboard cannot treat proposal actionability as startup readiness.

```text
fee proposal exercise actionable ≠ activation/startup authorized
```

The first real project specimen therefore validates the dashboard's need for distinct states and override records.

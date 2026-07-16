---
record_type: activation_gate_conditions
status: approved
implementation_status: not_implemented
classification: addition
source_context:
  - 00_Source/PAC/Working Drafts/PAC_Canonical_Data_Model_v1.1.md
  - user_review_revision_2026-07-15
  - governance_approval_2026-07-15
developmental_structure_change: true
framework_b_signal_source: gate_overrides_are_live_project_risk_signals
---

# Activation Gate Conditions

## Governance Decision

| Field | Value |
|---|---|
| Decision Date | 2026-07-15 |
| Reviewer | User / Grace governance review, informed by Claude review pass |
| Decision | Approved |
| Classification | Addition — new canonical artifact; no existing canon replaced or retired |
| Implementation Status | Not implemented — approval canonizes the requirement, not dashboard logic |
| Rationale | Fourteen gate conditions confirmed against project reality; blocking-by-default with Decision Record override confirmed as the deterministic rule; output states confirmed including `startup_ready_with_recorded_risk` as a permanently distinct state. |

## Purpose

This draft defines the missing gate logic between PAC and downstream LCW / Startup activity.

PAC boundary holds as drafted:

```text
PAC answers: what did the origin instrument state?
```

Activation answers a different question:

```text
Is Grace permitted, authorized, and organized to begin?
```

The UHG lesson does not require expanding PAC. It exposes the need for explicit **Activation gate logic**.

## Layer Distinction

| Layer | Question Answered | Epistemic Category |
|---|---|---|
| PAC | What did the origin instrument state? | Captured origin data |
| Activation | Is the firm permitted and organized to begin? | Confirmed condition |
| LCW Startup / Downstream Sections | How is the project staffed, coordinated, configured, and executed? | Operational truth / working record |

## Deterministic Gate Rule

All Activation gate conditions are **blocking by default**.

A block may be overridden only when an accountable human records a Decision Record that states:

1. who authorized the override;
2. what gate condition was overridden;
3. the rationale;
4. the accepted risk;
5. any mitigation or follow-up requirement;
6. date/time of decision;
7. source/evidence supporting the decision.

A "warn" condition is therefore not a separate gate type. It is:

```text
blocking condition + accountable override + recorded rationale/accepted risk
```

This prevents ambiguous gate outcomes and preserves traceability.

## Framework B Signal Link

Gate overrides are a defined signal source for Framework B.

Proceeding under qualified or unresolved conditions is not invisible drift. It becomes captured project intelligence:

```text
Activation gate override
→ Decision Record
→ accepted risk / deviation / friction signal
→ Framework B live-project intelligence input
```

## Activation Gate Table

| # | Gate Condition | Source PAC Field / Signal | Confirmation Mechanism | Default Gate Result | Override / Routing |
|---|---|---|---|---|---|
| A-GATE-001 | Acceptance status known | PAC 9.2 Acceptance Block | Confirm proposal/approval instrument shows approved, pending, revision required, or not approved | Blocks if unknown | Override requires Decision Record; no Startup should proceed with unknown acceptance unless explicitly authorized. |
| A-GATE-002 | Acceptance authority confirmed | PAC 9.3 Authorization Confirmation Status | Confirm signer/approver had authority under client and firm process | Blocks if unconfirmed | UHG failure mode: apparent movement without confirmed authority. Override becomes Framework B risk signal. |
| A-GATE-003 | NTP / equivalent authorization event confirmed | Acceptance Block + client communication | Written NTP, approved proposal, executed agreement, Service Order, PO, or other accepted authorization path | Blocks if absent | Exact acceptable instrument may vary by client/project; override must state accepted authorization basis. |
| A-GATE-004 | Project ownership assigned | PAC project identity + internal routing | PIC/PM/accountable owner assigned for Activation | Blocks if unassigned | This is not full staffing; it establishes accountable ownership before downstream team assembly. |
| A-GATE-005 | Project number / activation identifier created or provisional identifier approved | PAC project name/client/location | Internal project number, activation record, or approved provisional identifier exists | Blocks if neither created nor provisionally approved | Override must state why work may proceed without final identifier and how tracking/billing will be protected. |
| A-GATE-006 | Scope baseline sufficient for startup or explicitly qualified | PAC 4.1 Project Description + 4.4 Scope Clarity Status | Confirm scope clarity is sufficient, or unresolved gaps are named and accepted | Blocks if insufficient/unassessed | Override records accepted scope ambiguity and required follow-up. |
| A-GATE-007 | Fee basis approved and aligned with authorization instrument | PAC 6.1 Professional Fee + 6.2 Fee Breakdown | Confirm approved fee basis matches acceptance/NTP/Service Order/PO or other authorization | Blocks if unapproved/misaligned | Critical for fee-reduction or scope-revision situations; override must name authorized approver. |
| A-GATE-008 | Schedule baseline acknowledged and confidence classified | PAC 7.1 Schedule + 7.2 Schedule Confidence | Confirm schedule status: contractual, illustrative, preliminary, owner-dependent, or incomplete | Blocks if unassessed | Override records schedule uncertainty and downstream impact. |
| A-GATE-009 | Required contract path identified | PAC 8.1 Form of Agreement | Confirm AIA / owner form / MSA / Service Order / custom path / pending legal form | Blocks if unidentified | Prevents work beginning under wrong contractual assumption. |
| A-GATE-010 | Insurance / risk requirement reviewed for startup relevance | PAC 8.2 Insurance Requirements | Confirm requirements are stated, not applicable, or risk-reviewed if incomplete | Blocks if relevant and unreviewed | Especially important for public, institutional, clinical, or special-risk work. |
| A-GATE-011 | Unresolved consultant / additional-service triggers acknowledged and routed | PAC 5.2 Additional Services + 5.3 Programming + 5.4 Record Drawings | Identify any consultant/additional-service signals and route to Section B responsibility mapping before they are dropped | Blocks if triggers are present and unrouted | PAC signals need; Section B assigns parties/responsibilities. Override records accepted coordination risk. |
| A-GATE-012 | Billing path viable | PAC 6.4 Billing Schedule | Confirm billing schedule or approved provisional billing logic sufficient for setup | Blocks if unassessed/insufficient | Override must state how accounting/project setup can proceed without full billing clarity. |
| A-GATE-013 | All gate conditions evaluated | Activation gate table | Confirm no gate condition remains unassessed | Blocks if any condition is unassessed | Readiness flags are aggregate T-output, not a gate condition. |
| A-GATE-014 | Approval-path governance satisfied | Firm constitutional/process layer | Confirm required internal approval path was followed | Blocks if unsatisfied | This is inherited governance/process knowledge, not a project-origin PAC field. Reroute to constitutional/process layer for review. Open dependency logged at `01_Requirements/Pending Constitutional Item - Firm Approval Path Governance.md`. |

## A-GATE-013 Rationale Trail

The proposed "startup readiness flags generated" condition was rejected as circular because readiness flags are the aggregate output of gate evaluation. A gate cannot require its own output as an input condition.

Therefore A-GATE-013 is a completeness condition instead:

```text
All gate conditions evaluated; none unassessed.
```

The resulting readiness flags remain downstream transformation outputs.

## Startup Readiness Flags

Startup readiness flags are not independent gate conditions. They are transformation outputs derived from the gate evaluation.

```text
all gates green → startup_ready
one or more gates overridden → startup_ready_with_recorded_risk
one or more gates blocked/no override → startup_blocked
one or more gates unassessed → startup_unassessed / incomplete
```

These flags are downstream T outputs and must not be written back into PAC as origin truth.

## Condensed Activation Logic

Section A Activation may open only when:

1. acceptance status is known;
2. acceptance authority is confirmed;
3. NTP/equivalent authorization exists;
4. accountable PIC/PM ownership exists;
5. fee/scope/schedule are approved, or explicitly qualified by Decision Record;
6. every gate is evaluated;
7. any unresolved condition is either blocking or consciously overridden with lineage;
8. firm approval-path governance has been satisfied.

## Routing Notes

| Item | Correct Layer | Reason |
|---|---|---|
| Authority to approve | Activation | PAC captures apparent acceptance; Activation confirms authority. |
| NTP / acceptance condition | Split | PAC records stated condition; Activation records confirmed authorization event. |
| PIC / team ownership | Activation | Accountability assignment precedes full team assembly. |
| Consultant responsibility | Section B, signaled/routed by Activation | PAC Additional Services may signal need; Section B assigns actual parties/responsibilities. |
| Scope/fee approval path | Constitutional / firm process layer | Inherited governance/process knowledge, not project-specific PAC origin data. |

## Governing Conclusion

PAC boundary holds as drafted.

The UHG lesson does not expand PAC. It requires explicit Activation gate logic and an override-with-Decision-Record rule so that proceeding under qualified conditions becomes captured intelligence rather than invisible drift.

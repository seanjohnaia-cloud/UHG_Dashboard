---
record_type: service_order_preparation_record
status: draft_field_truth_record
use_case: UC-001
experiment_focus: Muncie Family Physicians
requested_activity: prepare_fee_proposal
first_act: service_order_preparation
readiness_status: deficient
---

# Muncie Service Order Preparation Record — Draft

> This is the first LCD-style data record for the Muncie experiment. It records field truth states. It does not complete the Service Order and does not invent missing information.

## Field Truth State Legend

Allowed states from Pii founding prompt:

```text
provided, extracted, validated, assumed, missing, conflict, deferred, unknown, not-required
```

## Project Identity

| Field | Value | State | Evidence / Basis |
|---|---|---|---|
| Project Name | Muncie Family Physicians | extracted | LCD Workbook `Life Cycle Data Worksheet` row 2; Muncie PDF title block also visible |
| Project Location | unknown / incomplete | missing | LCD says from Initial Information; no clean Service Order location value preserved yet |
| Project Number / S.O. Number | unknown | missing | LCD says must be requested / CBRE PM provides SO number |
| Project Start Date | 2026-07-06 | extracted | LCD `Life Cycle Data Worksheet` row 2 |
| Project Group | unknown | missing | LCD select field blank |
| Project Manager | unknown | missing | LCD select field blank |
| Project Leader | unknown | missing | LCD select field blank |
| UHG DE Regional Rep. | unknown | missing | LCD says from Initial Information |
| UHG Regional PM Rep. | unknown | missing | LCD says from Initial Information |

## Request / Activity

| Field | Value | State | Evidence / Basis |
|---|---|---|---|
| Requested Activity | prepare fee proposal | provided | Client email asks for pricing/fee proposal |
| Active Project Scope | Muncie only | validated | User directed to ignore Russiaville for the experiment |
| Workflow Position | proposal requested / service order preparation | extracted | Client email + user clarification that Service Order preparation is first ACT |
| Information Readiness | deficient | validated | Missing MSA fee basis details, SO number, schedule, project location, reps, consultant responsibilities, etc. |

## Classification / Compensation

| Field | Value | State | Evidence / Basis |
|---|---|---|---|
| Project Type | Small Remodel | extracted | SO Matrix `Muncie Family Physicians` row 5 |
| Special Type | one-off / small project fee exercise | extracted | Client email asks one-off treatment; PM response says hammer out small project fees |
| Compensation Method | Grace-only architectural fee proposal; intended output shows proposed fee $27,950 against per-contract comparison $34,760 | extracted | Client-sent Muncie PDF shows proposed total $27,950 and per-contract total $34,760; requires user validation before final proposal |
| Fee Schedule Basis | Schedule F — Clinic Project Size (0-2,500 SF) | extracted | SO Matrix rows 2-3 |
| Architectural Services Only | yes — Grace proposal only for current exercise | validated | UHG PM response: "Grace’s proposal only – no MEP at this time" |

## Scope / Project Material

| Field | Value | State | Evidence / Basis |
|---|---|---|---|
| Approximate Area | ~250 SF | provided | Client email |
| Research Scope | supply storage / ambient drug study room, cabinets, shelving, power/data, LVT, security | extracted | Email + Muncie PDF notes |
| Imaging/X-Ray Scope | RSI layout, Carmel machine relocation, direct dressing connection, lead-wall confirmation pending | extracted | Email + Muncie PDF notes |
| Floor Plans | preserved | validated | Muncie PDF preserved and hash-verified |
| Existing/New SF split | unknown | missing | LCD fields require existing/new SF; not resolved |
| Scope Description | partial | extracted | Email and plan notes provide partial scope but not final SO-ready narrative |

## Schedule / SLA

| Field | Value | State | Evidence / Basis |
|---|---|---|---|
| Service Order Submittal Date | unknown | missing | LCD Design Schedule field blank |
| Service Order Approval Date | unknown | missing | LCD Design Schedule field blank |
| Design Start Date | unknown / date of PO | missing | LCD says Design Start Date = Date of Purchase Order |
| Design Completion Date | unknown | missing | LCD says from Design Schedule |
| Construction Start Date | unknown | missing | LCD says from Initial Information |
| Substantial Completion Date | unknown | missing | LCD says from Initial Information |
| SLA Framework | available but not applied | extracted | LCD Design Schedule has SLA framework by project type |

## Consultant / Responsibility Boundaries

| Field | Value | State | Evidence / Basis |
|---|---|---|---|
| MEP Consultant Required | not for current fee exercise; likely required later | deferred | UHG PM response: "Grace’s proposal only – no MEP at this time" and "agreed some will be required". Do not contact Salas O'Brien now. |
| Structural Consultant Required | unknown | missing | Not evidenced yet |
| Civil Consultant Required | likely not required but not validated | unknown | Not evidenced yet |
| RSI Role | unknown | missing | Email/PDF says RSI to provide/confirm; responsibility not defined |
| Security / Access Control Responsibility | unknown | missing | Punch door security requested; responsible party not defined |
| Medical Equipment Responsibility | unknown | missing | X-ray equipment relocating; AHN owns equipment; responsibility not defined |
| IT/Low Voltage Responsibility | unknown | missing | Power/data and security imply coordination; not defined |

## Output Readiness

| Output | Status | Reason |
|---|---|---|
| Final Fee Proposal | not ready | Fee basis, project type, schedule, consultant responsibilities, and missing fields unresolved |
| Deficient-Readiness Response | ready | Enough evidence to request clarifications and frame proposal path |
| Service Order Draft | not required today / deferred | UHG PM response: "No Service Order today"; current activity is to hammer out small project fees |
| LCD Data Record | started | This file is the first draft field truth record |

## Next Required Source Extraction

To advance this record, extract the **Muncie SO Development Matrix** access layer and compare it against this LCD field map.

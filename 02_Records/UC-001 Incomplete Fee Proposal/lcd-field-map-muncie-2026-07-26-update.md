---
record_type: lcd_field_map
status: draft_extracted_from_lcd_access_layer
use_case: UC-001
experiment_focus: Muncie Family Physicians
source_id: SRC-WORKFLOW-LCD-WORKBOOK
supersedes_in_time: lcd-field-map-muncie.md (does not overwrite; that record stands as the pre-negotiation field map)
---

# LCD Field Map — Muncie (Update)

> Same field structure as `lcd-field-map-muncie.md`. This pass compares that map against everything received since: the 2026-07-15 and 2026-07-22 SO Development Matrices, and Sandy Goodman's 2026-07-23/26 email on permits and meetings. Adds a Stage column per Sean's request — data needs to be trackable as it matures, not just as present/missing.

## Stage Legend

- `initial` — first raw value received, as-stated, not yet reconciled against anything else
- `developmental` — value has been revised at least once through negotiation; not yet accepted/final
- `final` — confirmed/accepted, ready to populate the actual Service Order
- `missing` — still not provided (unchanged from the original field map)

## 1. Project Identity — unchanged since original map

| LCD Label | Status | Stage | Evidence / Date Received |
|---|---|---|---|
| Project Name | extracted: `Muncie Family Physicians` | final | LCD Life Cycle Data Worksheet row 2 |
| Project Location | missing | — | Still no clean location value preserved |
| Project Number / S.O. Number | missing | — | Must be requested per CBRE PM (Service Order row 2) |
| Project Start Date | extracted: `2026-07-06` | final | LCD row 2 |
| Project Group / Manager / Leader | missing | — | LCD select fields blank |
| UHG DE Regional Rep. | candidate: Shannon Dupras (unconfirmed role match) | developmental | Named sender/recipient in 2026-07-23 email thread; role title on the LCD-W field is "UHG DE Regional Rep." — not yet confirmed this is the same role as Shannon's actual title "Design Manager, Midwest Region" |
| UHG Regional PM Rep. | unknown | missing | Eric Dietz cc'd/addressed in the thread; role match not confirmed |

## 2. Classification / Fee Basis — materially updated

| LCD Label | Status | Stage | Evidence / Date Received |
|---|---|---|---|
| Project Type | extracted: Small Remodel | final | SO Matrix, both dates |
| Special Type | one-off / small project fee exercise | final | Original client email; consistent across both matrix dates |
| Fee Schedule Basis | Schedule F — Clinic Project Size (0-2,500 SF) | final | SO Matrix rows 2-3, confirmed both dates and matches Russiaville's identical classification |
| Compensation — per-Contract baseline | $34,760.00 | final | Fixed by classification; unchanged across both matrix dates |
| Compensation — proposed (initial pass) | $27,950.00 | developmental (superseded) | 2026-07-15 client-sent artifact; see `so-matrix-fee-basis-analysis-muncie.md` |
| Compensation — proposed (post-scope-reduction) | $23,650.00 | developmental | 2026-07-22 SO Matrix, produced after collaborative scope reduction with UHG Design Experience per Sean's 2026-07-26 explanation. Not yet marked `final` — no confirmation on file that UHG has accepted this figure. |
| Additional Services basis (permitting) | Permit application + review-comment response **included** in fee, folded into CA hours allowance | final | Sandy Goodman email, received 2026-07-26 (thread dated 2026-07-23) |
| Reimbursable Expenses | Permit fees billed as reimbursable | final | Same email |

## 3. Scope / Area — unchanged since original map

| LCD Label | Status | Stage | Evidence / Date Received |
|---|---|---|---|
| Scope Description | partial | developmental | Email + Muncie PDF notes; not yet SO-ready narrative |
| Project S.F. | conflicting fragments (~250sf email vs 171.12/408.62sf extraction) | missing (conflict) | Unreconciled — carried forward unchanged |
| Existing/New S.F. split | missing | — | LCD rows 24-25 |
| Sustainability Objectives / Certification Required | missing | — | LCD rows 26, 29 |

## 4. Schedule / SLA — meeting assumptions now known; dates still missing

| LCD Label | Status | Stage | Evidence / Date Received |
|---|---|---|---|
| Design Start / Completion, Construction Start, Substantial Completion Dates | missing | — | Unchanged — LCD rows 32-35 |
| Service Order Submittal / Approval Date | missing | — | Unchanged |
| SLA / working-day framework | extracted, both matrix dates | final | 2026-07-22 SO Matrix: Site Due Diligence 2 days, SD Documents 5, Construction Documents 12 — reduced from original SLA per the same negotiation |
| **Meeting scope (new)** — existing-conditions site survey | 1 combined trip (Muncie + Russiaville same day) | final | Sandy Goodman email, 2026-07-26 |
| **Meeting scope (new)** — SD meeting | Virtual | final | Same email |
| **Meeting scope (new)** — check-ins | Weekly, virtual, as needed | final | Same email |
| **Meeting scope (new)** — construction-phase site visits | 3 combined trips (both sites same day) | final | Same email |

## 5. Consultants / Owner Consultants — unchanged since original map

| LCD Label | Status | Stage | Evidence / Date Received |
|---|---|---|---|
| Mechanical / Electrical / Structural | missing/select | — | Unchanged |
| Owner Consultants / Contractors (RSI, security, IT, medical equipment) | likely relevant, not validated | — | Unchanged from original map |

## 6. Service Order Output Requirements — new since original map

| LCD / Service Order Label | Status | Stage | Evidence / Date Received |
|---|---|---|---|
| Article 2 Feasibility Phase Exceptions | Feasibility fully excepted (all 5 Feasibility lines $0 both matrix dates) | final | SO Matrix, both dates |
| Article 4.1 Compensation, 3-bucket rollup | Feasibility $0 · SD-DD $7,370 · CD-Closeout $16,280 (sums to $23,650) | developmental | Derived from 2026-07-22 SO Matrix; same acceptance caveat as the total above |
| Article 4.3 Reimbursable Expenses | Permit fees | final | Sandy Goodman email |
| Article 7 Attachment — Project Scope Document | **does not exist as its own artifact** | missing | Needs to be produced — this is "the limited scope document" |
| Article 6 Party Representatives | Candidate names known (Shannon Dupras, Eric Dietz, Sandy Goodman); role assignment not confirmed | developmental | Same email thread |

## Open Items for Design Experience — carried into 04_Output draft

Everything still marked `missing` above is a real candidate for the clarification response to UHG Design Experience: Project Location, S.O. Number, PM/Project Leader assignment, exact Commencement/Substantial Completion dates, Existing/New SF split (and resolving the SF conflict), Article 6 role-to-name confirmation, Sustainability Objectives, Certification Required, and consultant (MEP/structural, RSI, security, IT) responsibility assignment. See `04_Output/UC-001 Incomplete Fee Proposal/design-experience-clarification-draft-2026-07-26.md`.

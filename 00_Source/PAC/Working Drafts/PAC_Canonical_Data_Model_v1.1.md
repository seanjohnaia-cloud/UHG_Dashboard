# PAC — PROPOSAL / APPROVAL / CAPTURE STRUCTURE
**Canonical Data Model — LCW Layer 0 · v1.1**

---

## 0. Purpose

This structure defines **all data captured at project inception, prior to Startup**.

It is derived from the Fee Proposal and Approval process and represents the earliest formal project record.

PAC is the first authoritative data layer for:

- Project identity
- Initial scope definition
- Financial structure
- Schedule baseline
- Service structure
- Approval status

It is the root population source for the Life Cycle Workbook (LCW).

---

## 1. Core Function

PAC exists to answer one question:

> **What is known, approved, and structurally defined before operational startup begins?**

PAC is not meant to capture everything required to run the project. It is meant to capture the **origin dataset** that establishes the project before activation, staffing, consultant coordination, system setup, and design development begin.

---

## 2. Data Capture Rule

PAC data falls into three categories:

| Code | Category | Definition |
|---|---|---|
| **O** | Origin Data | First authoritative project definition, captured directly from the approved proposal or approval instrument |
| **V** | Validation Data | May exist in the proposal but requires later confirmation before it can be treated as operational truth |
| **T** | Transformation Data | Not entered as origin truth; later derived from PAC for budgeting, scheduling, reporting, or tool population |

---

## 3. Project Identity

| # | Field | Class | Definition / Role |
|---|---|---|---|
| 3.1 | Proposal Date | O | Predesign baseline start · duration-to-approval tracking · earliest formal project timestamp |
| 3.2 | Client Entity (Company Name) | O | Legal client entity associated with the proposal |
| 3.3 | Client Contact (Attn:) | V | May not be final decision-maker or day-to-day contact. Requires later confirmation |
| 3.4 | Client Address | V | May differ from project address. Requires validation before operational use |
| 3.5 | Project Name | O | Primary project identifier |
| 3.6 | Project Type | O | New Construction / Addition / Renovation / Interior Renovation / Expansion / Adaptive Reuse |
| 3.7 | Market Sector | O | Classification · search and filtering · sector-based analytics · LLM conditional logic |
| 3.8 | Project Location (City / State) | O | Regional, jurisdictional, and reporting placement |
| 3.9 | Project Address (Physical) | O | Jurisdiction · code path initiation · site-based workflows · mapping and logistics |

---

## 4. Project Definition

| # | Field | Class | Definition / Role |
|---|---|---|---|
| 4.1 | Project Description | O | Initial narrative of scope, intent, character, known work type. Baseline reference for later scope comparison |
| 4.2 | Estimated Gross Square Footage | O | Range or approximate. Early code search logic · modeling assumptions · scope framing · fee and effort evaluation |
| 4.3 | Estimated Construction Cost | O | Total cost, cost/SF, or budget target basis. Initial financial baseline for fee calculation, cost alignment, budget expectation |
| 4.4 | Scope Clarity Status | V | Interpretive flag on the narrative: Clear / Partial / Conceptual / Likely Incomplete / Likely Misaligned. A validation condition attached to origin narrative, not origin truth itself |

---

## 5. Services Structure

| # | Field | Class | Definition / Role |
|---|---|---|---|
| 5.1 | Basic Services | O | Included core services and phases. Establishes scope inclusion, standard workflow population, phase-based downstream routing |
| 5.2 | Additional Services | O | Optional services and special scope. Triggers: specialty consultants, additional workflows, expanded fee conditions, special review |
| 5.3 | Programming | O if explicit / V if implied | Its own service category. Never assumed from project definition language |
| 5.4 | Record Drawings | O if included | Defined service type. Kept separate from core design phases |

---

## 6. Financial Structure

| # | Field | Class | Definition / Role |
|---|---|---|---|
| 6.1 | Professional Fee | O | Percentage of construction cost / lump sum / hybrid. The core fee basis |
| 6.2 | Fee Breakdown by Phase (%) | O | Distribution of fee across phases. Required for production budgeting, forecasting, downstream fee transformation, phase billing logic |
| 6.3 | Reimbursable Expenses | O if defined / V if unclear | Proposal-defined reimbursables |
| 6.4 | Billing Schedule | O if defined / V if incomplete | Initial billing logic tied to phase or milestone structure |

---

## 7. Schedule Structure

| # | Field | Class | Definition / Role |
|---|---|---|---|
| 7.1 | Project Schedule by Phase | O | First phase start, final phase end, phase durations, milestone sequencing. First formal project time structure |
| 7.2 | Schedule Confidence Status | V | Contractual / Illustrative / Preliminary / Owner-dependent / Incomplete. Prevents false precision downstream |

---

## 8. Contract Structure

| # | Field | Class | Definition / Role |
|---|---|---|---|
| 8.1 | Form of Agreement | O | AIA-based / owner-generated / custom / pending legal form |
| 8.2 | Professional Liability Insurance Requirements | O if stated / V if referenced-undefined | Especially relevant for public work, institutional clients, special risk or compliance |

---

## 9. Authorization + Control

| # | Field | Class | Definition / Role |
|---|---|---|---|
| 9.1 | Signature Block | O | Proposal author · originating office or team · point of authorship |
| 9.2 | Acceptance Block | O — **Critical Control Field** | Approved / Not Approved / Pending / Revision Required |
| 9.3 | Authorization Confirmation Status | V | Apparent approval may still require confirmation depending on process, client type, or contract path |

> **Rule:** No project proceeds into Startup without acceptance status being known. Acceptance is not administrative — it is the control condition that permits downstream activation.

---

## 10. PAC Data Classification Summary

### 10.1 True Origin Data (O)
Treated as PAC origin truth unless formally superseded:

Proposal Date · Client Entity · Project Name · Project Type · Market Sector · Project Location · Project Address · Project Description · Estimated GSF · Estimated Construction Cost · Professional Fee Basis · Fee Breakdown by Phase · Basic Services · Additional Services · Schedule by Phase · Form of Agreement · Acceptance Status

### 10.2 Validation Required (V)
May appear in PAC but require confirmation before operational use:

Client Contact · Client Address · Authorization Confirmation · Scope Clarity · Schedule Confidence · Insurance Requirement Completeness · Billing Completeness · Narrative Alignment to Actual Startup Conditions

### 10.3 Transformation Data (T)
Not PAC origin fields — derived later from PAC:

Fee dollars by phase · Internal production budget allocations · Schedule formatting (Gantt/dashboards) · Proposal-to-approval duration metrics · Fee-to-area ratios · Early cost density comparisons · Startup readiness flags

---

## 11. What PAC Does Not Contain

PAC is intentionally limited. The following are captured later in the LCW or related systems:

| Category | Excluded Content |
|---|---|
| Internal Resourcing | PIC, PM, PA, team staffing, responsibility assignments |
| Consultant Identity | Consultant firms, contacts, emails, proposal requests, scope mapping |
| Operational Setup | Revit version, folder structures, platforms, file locations, collaboration environments |
| Design Inputs | Program detail, room lists, code analysis, site verification, existing conditions, utilities |
| System Inputs | Model setup, naming conventions, file uploads, standards deployment |
| Project Intelligence Inputs | Friction points, deviations, startup failures, missing data conditions, process observations, lessons learned |

These emerge later and must not be confused with origin capture.

---

## 12. Structural Role in LCW

### PAC = LCW Section 0 — Origin Layer (Immutable Starting Point)

PAC populates Section 0 of the LCW and remains preserved as the initial dataset. It is not continuously edited as operational knowledge increases.

If a PAC field is later found to be wrong, the correction is recorded in a way that preserves the distinction between:

- What was originally stated
- What was later validated
- What became operational truth

### Downstream LCW Sections

| Section | Name | Role |
|---|---|---|
| **0** | PAC | Origin layer — this document |
| **A** | Activation | Project number, authorization, activation control |
| **B** | Team + Responsibility | Internal, consultant, and owner parties |
| **C** | Financial Modeling | Transforms PAC fee and budget data into operational financial structures |
| **D** | Operational Alignment | Standards, deliverables, milestones, coordination expectations |
| **E** | System Setup | Platforms, file structures, model environment, operational configuration |
| **F** | Design Inputs | Required conditions: program, site, regulatory, systems |

*Project Intelligence (observations, deviations, process gaps) sits outside the LCW sections and feeds DIF Framework B.*

---

## 13. PAC-to-LCW Routing Logic

| Condition | Routing |
|---|---|
| Field defines the project at origin | Store in PAC (Section 0) |
| Field confirms whether PAC is operationally reliable | Store as validation against PAC, downstream |
| Field is calculated or reformatted from PAC | Store as transformation output — never written back as PAC truth |
| Field emerges only after startup begins | Store in the appropriate LCW section (A–F), never PAC |

---

## 14. Governing Rules

| Rule | Statement |
|---|---|
| **1 — PAC is captured once** | Created once from the approved proposal/approval source |
| **2 — PAC is preserved** | An origin layer, not a live working worksheet |
| **3 — Validation does not overwrite origin** | Later clarification must not erase what PAC originally said |
| **4 — Derived data is not origin data** | Calculated values remain visibly downstream from PAC |
| **5 — Startup cannot substitute for PAC** | If PAC was not captured, later startup entry must not pretend to be origin truth |

---

## Final Statement

PAC is not just a document. It is the origin dataset from which the project is first constructed. Its role is not to run the project. Its role is to ensure that the project begins with a stable, classifiable, and recoverable starting point.

> **One line:** If PAC is captured correctly once, everything else becomes population, validation, or transformation — not re-entry.

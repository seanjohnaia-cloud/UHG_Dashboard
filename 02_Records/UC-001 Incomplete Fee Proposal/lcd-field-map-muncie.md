---
record_type: lcd_field_map
status: draft_extracted_from_lcd_access_layer
use_case: UC-001
experiment_focus: Muncie Family Physicians
source_id: SRC-WORKFLOW-LCD-WORKBOOK
---

# LCD Field Map — Muncie Service Order Preparation

> Draft field map derived from the LCD Workbook access layer. This is not a final data model. It identifies the smallest fields reality is asking for during Service Order preparation.

## Why LCD Matters Here

The LCD Workbook is the user's attempt to manage the project **as data**. For UC-001, it becomes the first field substrate for the first ACT:

```text
Service Order Preparation
```

## Active LCD Sheets

| Sheet | Role in First ACT |
|---|---|
| Life Cycle Data Worksheet | Primary data capture surface for project identity, status, scope, budget, schedule, consultants, and owner reps. |
| Service Order | Output/form structure for AIA B221 Service Order. Pulls from Life Cycle Data Worksheet. |
| Compensation | Fee/compensation basis and consultant/additional service compensation structure. |
| Design Schedule | SLA/schedule framework and milestone surface. |
| Project Tracking Report | Later tracking/reporting surface; not first focus unless readiness/risk requires it. |

## Minimum Data Groups Forced by LCD

### 1. Project Identity

| LCD Label | Current Muncie Status | Evidence / Note |
|---|---|---|
| Project Name | provided/extracted: `Muncie Family Physicians` | LCD `Life Cycle Data Worksheet` row 2 |
| Project Location | missing / from Initial Information | LCD row 3; email and PDF have partial/location-related clues but no clean Service Order location record yet |
| Project Number / S.O. Number | missing / must be requested | LCD row 3; Service Order row 2 says provided by CBRE PM |
| Project Start Date | extracted from LCD: `2026-07-06` | LCD row 2 |
| Project Group | missing/select | LCD row 5 |
| Project Manager | missing/select | LCD row 5 |
| Project Leader | missing/select | LCD row 6 |
| UHG DE Regional Rep. | missing/from Initial Information | LCD row 7 |
| UHG Regional PM Rep. | missing/from Initial Information | LCD row 8 |

### 2. Classification / Fee Basis

| LCD Label | Current Muncie Status | Evidence / Note |
|---|---|---|
| Project Type | missing/select | LCD row 6; SO Matrix expected to scrub project type |
| Special Type | likely relevant: `One-off`, but not validated | Client email asks one-off treatment; LCD row 7 lists One-off as special type option |
| Compensation | missing/select | Client email asks lump-sum/base minimum; LCD row 8 / Compensation sheet |
| Compensation categories | extracted options include Schedule E, Schedule F, Percentage Fee, Stipulated Fee, Negotiated Fee | LCD rows 3-8; Compensation sheet rows 3-12 |

### 3. Scope / Area

| LCD Label | Current Muncie Status | Evidence / Note |
|---|---|---|
| Scope Description | partially provided, needs refinement | Email and Muncie PDF notes |
| Project S.F. | email says `~250sf`; PDF extraction also shows `171.12 sf` and `408.62 sf` fragments requiring reconciliation | Email + Muncie PDF visual/extracted observations |
| Existing S.F. / New S.F. / Conditions Reused | missing/TBD | LCD rows 24-25 |
| Project Sustainability Objectives | missing/from Initial Information | LCD row 26 |
| Certification Required | missing/select | LCD row 29 |

### 4. Schedule / SLA

| LCD Label | Current Muncie Status | Evidence / Note |
|---|---|---|
| Design Start Date | missing; LCD says date of PO | LCD row 32 |
| Design Completion Date | missing/from Design Schedule | LCD row 33 |
| Construction Start Date | missing/from Initial Information | LCD row 34 |
| Substantial Completion Date | missing/from Initial Information | LCD row 35 |
| Service Order Submittal Date | missing | Design Schedule row 18 |
| Service Order Approval Date | missing | Design Schedule row 19 |
| SLA Framework | available in LCD Design Schedule, but not yet applied to Muncie | Design Schedule rows 1-15 |

### 5. Consultants / Owner Consultants

| LCD Label | Current Muncie Status | Evidence / Note |
|---|---|---|
| Mechanical / Electrical / Structural | missing/select | LCD rows 38-42; Muncie scope includes MEP/power/data/x-ray/security implications |
| Supplemental Consulting Services | missing/select | LCD rows 37-44 |
| Owner Consultants / Contractors | likely relevant but not validated | LCD rows 44-50; Exhibit A lists owner consultants; email/PDF references RSI/security/customer-provided cabinets |
| Security, IT/Low Voltage, Medical Equipment | likely relevant but not validated | LCD owner consultant list rows 38-42 |

### 6. Service Order Output Requirements

| LCD / Service Order Label | Current Muncie Status | Evidence / Note |
|---|---|---|
| Service Order Date | missing; LCD suggests date of Project Engagement Meeting | Service Order row 3 |
| Owner | template-provided: United HealthCare Services, Inc. | Service Order rows 5-7 |
| Architect | template-provided but has legal/state verification note | Service Order rows 8-12 |
| Project Description | linked from LCD Scope Description | Service Order row 16 |
| Initial Information attachment | required as Project Scope Document / Project Design Schedule | Service Order rows 23-25 |
| Compensation | from Exhibits E or F | Service Order row 15 / row 17+ |
| Additional/Reimbursable Expenses | referenced as Attachment X if applicable | Service Order rows 25-28 |

## Immediate Muncie Data Problem

The LCD gives us the shape of the data record, but Muncie still lacks enough validated values to complete the Service Order.

Therefore the first Pii behavior should be:

```text
Create a Muncie Service Order Preparation Record that can hold provided/extracted/assumed/missing/conflict states per field.
```

Do not turn blanks into guesses.

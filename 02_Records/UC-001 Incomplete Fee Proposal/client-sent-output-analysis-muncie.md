---
record_type: intended_output_analysis
status: draft_from_client_sent_artifact
use_case: UC-001
experiment_focus: Muncie Family Physicians
source_id: client_sent_muncie_pdf
---

# Muncie Client-Sent Artifact — Intended Output Analysis

> Analysis of the artifact actually sent/used after UHG clarified no formal Service Order was needed. This supersedes the earlier workbook-only candidate as evidence of the intended output format and fee value.

## Source

```text
00_Source/Project Requests/UC-001 Incomplete Fee Proposal/Client-Sent Artifacts/Muncie/original/SO Development Matrix_Muncie.pdf
```

Extracted text:

```text
00_Source/Project Requests/UC-001 Incomplete Fee Proposal/Client-Sent Artifacts/Muncie/extracted/SO Development Matrix_Muncie-text.md
```

## Intended Output Type

The client-sent artifact is a **Service Order Development Matrix PDF**, not a formal Service Order and not a narrative proposal letter.

It provides the requested data after UHG clarified:

- Grace proposal only;
- no MEP fee at this time;
- no Service Order today;
- purpose is small project fee evaluation.

## Key Difference from Workbook Extraction

The earlier XLSX access layer exposed the workbook's formula/candidate contract total of:

```text
$34,760
```

The client-sent PDF shows both:

```text
per Contract Total: $34,760.00
Proposed Total: $27,950.00
```

Therefore, the **intended output value** appears to be:

```text
$27,950.00 proposed Grace architectural fee
```

while `$34,760.00` remains the contract/schedule reference comparison.

## Proposed Fee Rows in Client-Sent PDF

| Deliverable / Phase | Required | Per Contract | Proposed |
|---|---|---:|---:|
| Feasibility Kick-off | blank | $1,100 | $0 |
| Feasibility Scope Interview | blank | $3,300 | $0 |
| Feasibility Scenario Development | blank | $1,650 | $0 |
| Feasibility Preliminary Programming | blank | $3,850 | $0 |
| Feasibility Utilization Analyses | blank | $3,300 | $0 |
| SD Site Due Diligence | YES | $6,050 | $3,300 |
| SD Programming | blank | $4,950 | $0 |
| SD Preliminary Floor Plan | YES | $1,650 | $900 |
| SD Schematic Design Documents | YES | $6,050 | $3,850 |
| Design Development Phase | YES | $4,950 | $4,800 |
| Construction Development Phase | YES | $6,050 | $6,050 |
| Permitting | YES | $1,980 | $1,500 |
| Bidding | YES | $1,980 | $1,500 |
| Construction Phase | YES | $6,050 | $6,050 |
| **Total** |  | **$34,760** | **$27,950** |

## Schedule Notes in Client-Sent PDF

| Phase | Contract Days | Proposed Days |
|---|---:|---:|
| Project Kick-off | 1 | 1 |
| Scope Review | 1 | 1 |
| Site Due Diligence | 5 | 1 |
| Preliminary Floor Plan | 5 | 5 |
| Schematic Design Documents | 10 | 5 |
| Design Development Documents | 10 | 10 |
| Construction Documents | 15 | 15** |
| Permitting/Bidding | 15 | 15 |

Footnotes preserved:

```text
*Fee assumes ACAD Backgrounds of the existing space are available for use
**During the CD phase, the AE team will need a minimum of 15 business to coordinate with site specific imaging equipment vendor drawings to be provided when required of the schedule.
```

## Missing from Intended Output

The artifact contains fee/schedule data, but it does not provide a complete narrative scope / statement of understanding.

User's gold standard requires a scope section so the output becomes:

```text
Your request + our response = complete statement of understanding
```

## Pii Design Consequence

Future proposal output should not be only a fee matrix. It should include:

1. Request Summary — what UHG asked for.
2. Scope Understanding — what Grace understands the project to include.
3. Response / Fee Matrix — how Grace proposes to price/respond.
4. Assumptions and Exclusions — what is included/excluded, including no MEP at this time.
5. Schedule / SLA Understanding — proposed time frame and constraints.
6. Carry-forward Note — if approved, this can become the Service Order basis later.

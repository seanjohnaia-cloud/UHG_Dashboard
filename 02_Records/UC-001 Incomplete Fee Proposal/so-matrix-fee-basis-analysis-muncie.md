---
record_type: so_matrix_fee_basis_analysis
status: draft_extracted_for_user_validation
use_case: UC-001
experiment_focus: Muncie Family Physicians
source_id: SRC-UC001-SO-MATRIX-MUNCIE-001
source_access_layer: 00_Source/Project Requests/UC-001 Incomplete Fee Proposal/Muncie/SO Development Matrix/extracted/Muncie_Family_Physicians.md
---

# Muncie SO Matrix — Fee Basis Analysis

> Draft analysis from the extracted SO Development Matrix access layer. This does not finalize the fee proposal. It identifies the fee basis and candidate fee logic visible in the matrix.

## Source Position

- Source/work-product: `SO Development Matrix_Muncie.xlsx`
- Sheet: `Muncie Family Physicians`
- Classification: user-generated working standard exercise sent to team
- Current PM direction: Grace architectural proposal only; no MEP fee; no formal Service Order today

## Matrix Structure Observed

The matrix contains three working lanes:

1. **Contractural Requirements (Deliverables)**
2. **Schedule F Fees and Proposed Adjustments**
3. **Contractural Time Frames / Proposed Project Schedule**

The spelling `Contractural` is preserved from the workbook extraction.

## Project / Fee Classification Extracted

| Field | Extracted Value | Evidence |
|---|---|---|
| Project / Sheet | Muncie Family Physicians | Row 20 |
| Project class | Small Remodel | Row 5 |
| Fee schedule | Schedule F Fees and Proposed Adjustments | Row 2 |
| Size category | Clinic Project Size (0-2,500SF) | Row 3 |
| Schedule framework | SLA Framework (Working Days) | Row 3 |

## Deliverable / Fee Rows Extracted

| Row | Deliverable / Phase | Required? | Contract Fee | Proposed Adjustment |
|---:|---|---|---:|---:|
| 5 | 4.2.3.1 A Feasibility: Feasibility Kick-off | X | 1,100 | 0 |
| 6 | 4.2.3.1 B Feasibility: Feasibility Scope Interview | X | 3,300 | 0 |
| 7 | 4.2.3.1 D Feasibility: Scenario Development | X | 1,650 | 0 |
| 8 | 4.2.3.1 C Feasibility: Preliminary Programming | X | 3,850 | 0 |
| 9 | 4.2.3.1 E Feasibility: Utilization Analyses | X | 3,300 | 0 |
| 10 | 4.2.3.2 A Schematic Design Phase: Site Due Diligence | blank | 6,050 | blank |
| 11 | 4.2.3.2 B Schematic Design Phase: Programming | X | 4,950 | 0 |
| 12 | 4.2.3.2 D Schematic Design Phase: Preliminary Floor Plan | blank | 1,650 | blank |
| 13 | 4.2.3.2 E Schematic Design Phase: Schematic Design Documents | blank | 6,050 | blank |
| 14 | 4.2.3.3 Design Development Phase | blank | 4,950 | blank |
| 15 | 4.2.3.4 Construction Development Phase | blank | 6,050 | blank |
| 16 | 4.2.3.5 A Preconstruction, Bidding and Permitting Phase: Permitting | blank | 1,980 | blank |
| 17 | 4.2.3.5 B Preconstruction, Bidding and Permitting Phase: Bidding | blank | 1,980 | blank |
| 18 | 4.2.3.6 Construction Phase | blank | 6,050 | blank |

## Candidate Fee Total Observed

The workbook total row shows:

```text
Muncie Family Physicians | Total: | 34760
```

The formula view shows:

```excel
=SUM(D12:D18,D10)
```

That means the visible total is summing the contract fee values for:

- Site Due Diligence — 6,050
- Preliminary Floor Plan — 1,650
- Schematic Design Documents — 6,050
- Design Development Phase — 4,950
- Construction Development Phase — 6,050
- Permitting — 1,980
- Bidding — 1,980
- Construction Phase — 6,050

Candidate total:

```text
$34,760
```

## Important Interpretation Boundary

The matrix also marks several early feasibility/programming rows with `X` and proposed adjustment `0`. This appears to distinguish tasks considered required/reviewed from the fee total currently being proposed, but that interpretation must be validated by the user before final proposal language is generated.

Do not assume that `X` means included in the $34,760 total. The workbook's actual total formula excludes rows 5-9 and row 11, and includes row 10 plus rows 12-18.

## Schedule/SLA Extracted

| Phase | Contract Days | Proposed Days |
|---|---:|---:|
| Project Kick-off | 1 | 1 |
| Scope Review | 1 | 1 |
| Site Due Diligence | 5 | 1 |
| Preliminary Floor Plan | 5 | 5 |
| Schematic Design Documents | 10 | 5 |
| Design Development Documents | 10 | 10 |
| Construction Documents | 15 | 15 |
| Permitting/Bidding | 15 | 15 |

## Current Working Conclusion

For the current Grace-only / no-MEP / no-Service-Order-today exercise, the SO Matrix provides a candidate contract-derived fee basis:

```text
Small Remodel, Clinic Project Size 0-2,500 SF, Schedule F, candidate fee total $34,760 before any further user-approved adjustment.
```

This is ready for user validation before it becomes proposal language.

# Fee Proposal Walkthrough — Handoff

Status: draft / in progress. This file will be updated at commit time to reflect final state before these files land in git history.

## What this thread is

Two related pieces of work, both under the "figure out what a Fee Proposal act actually requires" umbrella:

1. **Fictional Fairview walkthrough** (`02_Records/SANDBOX Fictional Fee Proposal Walkthrough (Fairview)/`, overview at `UseCases/SANDBOX Fictional Fee Proposal Walkthrough (Fairview).md`) — a non-authoritative sandbox using the vault's existing fictional specimen (Fairview) to work the Fee Proposal act to completion, since real Muncie data was insufficient to do that. Mirrors real UC-001's required-outputs contract (proposal draft, assumptions, gaps, risks, clarifications, readiness).
2. **Real UC-001 additions** (`02_Records/UC-001 Incomplete Fee Proposal/`) — while grounding the fictional walkthrough in real mechanism, two real gaps got filled in: a newer Muncie SO Development Matrix (2026-07-22) and a first-ever Russiaville fee-basis analysis.

## Key finding: the fee mechanism

UHG project fees are **not** computed via the generic AIA lump-sum-with-standard-phase-percentages model. They're built off the UHG contract's **Schedule F deliverable matrix** — a fixed per-deliverable rate table keyed by classification (project type × size tier), with a PM Required/Proposed call on each line. Two real Grace document templates exist (`00_Source/Proposal Template.docx` = Negotiated Fee/AIA B101-2017; `00_Source/Proposal Template_Hourly Rate.dotx` = Hourly/NTE/AIA B104-2017) — for a UHG project, the matrix produces the fee, and the Negotiated Fee template supplies the surrounding letter structure once the matrix total exists.

## Fairview sandbox — current state

In `02_Records/SANDBOX Fictional Fee Proposal Walkthrough (Fairview)/`:

- `readiness-assessment.md`, `information-gaps.md` — resolved: Schedule F routing (confirmed two ways), which template applies (Negotiated Fee), phase-breakdown mechanism (deliverable matrix, not % split).
- `so-development-matrix.md` — **open**: the 14-line Schedule F deliverable table is populated with per-Contract rates (same as Muncie/Russiaville, same classification tier) but **Required and Proposed columns are blank**. This is the next thing to fill in — same two judgment calls Sean already made on Muncie/Russiaville.
- `proposal-draft.md` — skeleton follows the real Negotiated Fee template structure; fee section points at the matrix and is empty until the matrix is filled in.
- `assumptions.md`, `risk-records.md`, `clarification-requests.md` — still templates, not started.

## Real UC-001 additions (this session)

- Preserved a new real Muncie artifact: `00_Source/Project Requests/UC-001 Incomplete Fee Proposal/Client-Sent Artifacts/Muncie 2026-07-22 Reduced AOR/` (original PDF + extracted text + provenance, sha256 `8e818737f9088a98514f37672717d0c28744615d841d13424d0448a48ef06210`). Does not overwrite the existing 2026-07-15 preserved version.
- `02_Records/UC-001 Incomplete Fee Proposal/so-matrix-fee-basis-analysis-muncie-2026-07-22-update.md` — line-by-line delta vs the 2026-07-15 matrix. Total dropped $27,950 → $23,650. Pattern (DD Phase/Permitting/Bidding/Prelim Floor Plan zeroed, Construction Development Phase nearly doubled) matches the already-recorded reduced-AOR scope direction.
- `02_Records/UC-001 Incomplete Fee Proposal/so-matrix-fee-basis-analysis-russiaville.md` — first fee-basis analysis for Russiaville (none existed before). Same classification/per-Contract total as Muncie; Proposed total $23,870; Required/Proposed pattern is internally consistent (unlike Muncie's, where a non-Required line still gets a nonzero Proposed fee).

**Open, unresolved by design**: `readiness-assessment.md` in the real UC-001 folder still cites $27,950 as "the intended output value" — that's now stale against the 2026-07-22 $23,650 figure. Whether $23,650 is the new intended output, an interim position, or still moving is Sean's call, not inferred here. `readiness-assessment.md` was deliberately not edited.

## Uncommitted files (as of this session)

```
?? 00_Source/Project Requests/UC-001 Incomplete Fee Proposal/Client-Sent Artifacts/Muncie 2026-07-22 Reduced AOR/
?? 00_Source/Proposal Template.docx
?? 00_Source/Proposal Template_Hourly Rate.dotx
?? 02_Records/SANDBOX Fictional Fee Proposal Walkthrough (Fairview)/
?? 02_Records/UC-001 Incomplete Fee Proposal/so-matrix-fee-basis-analysis-muncie-2026-07-22-update.md
?? 02_Records/UC-001 Incomplete Fee Proposal/so-matrix-fee-basis-analysis-russiaville.md
?? UseCases/SANDBOX Fictional Fee Proposal Walkthrough (Fairview).md
```

Also present but **not part of this thread** — appears to be concurrent Hermes work, untouched by this session:

```
 M pii_team_dashboard/prototype/index.html
?? pii_team_dashboard/prototype_v2_draft/
```

## Next steps

1. Fill in `so-development-matrix.md`'s Required/Proposed columns for Fairview (fictional judgment call).
2. Reconcile `proposal-draft.md`'s fee section once the matrix total exists.
3. Sean's call on the real Muncie $27,950 vs $23,650 question, and whether `readiness-assessment.md` needs a revision pass.
4. Commit — this file gets a final pass first.

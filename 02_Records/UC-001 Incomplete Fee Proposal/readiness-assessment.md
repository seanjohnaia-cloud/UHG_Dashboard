---
record_type: readiness_assessment
status: deficient_but_narrowed
use_case: UC-001
experiment_focus: Muncie Family Physicians
requested_activity: prepare_grace_architectural_fee_proposal
workflow_position: small_project_fee_exercise
readiness_status: deficient_but_actionable
service_order_required_now: false
mep_fee_required_now: false
---

# UC-001 Muncie Readiness Assessment

## Independent State Fields

- `requested_activity`: `prepare_grace_architectural_fee_proposal`
- `workflow_position`: `small_project_fee_exercise`
- `readiness_status`: `deficient_but_actionable`
- `service_order_required_now`: `false`
- `mep_fee_required_now`: `false`

## Assessment

The Muncie request is now narrower and more actionable than before.

UHG has clarified that the immediate need is **Grace's proposal only**, not MEP consultant pricing and not a formal Service Order today. The purpose is to hammer out small project fees.

The project is still not complete enough for a final contractual Service Order, but it is actionable enough to prepare a Grace-only architectural fee proposal using the contract language and the LCD/SO Matrix workflow.

## New PM Response Basis

Preserved response:

```text
03_Communications/UC-001 Muncie/incoming-pm-response-001-grace-only-no-so.md
```

Key answers:

1. Grace proposal only for now.
2. No MEP fee at this time.
3. MEP will likely be required later.
4. No Service Order today.
5. Current task is to hammer out small project fees.

## Client-Sent Intended Output Extracted

The actual client-sent Muncie PDF shows the intended no-Service-Order output after UHG's clarification:

```text
Per-contract comparison total: $34,760.00
Proposed adjusted Grace architectural fee: $27,950.00
```

Analysis record:

```text
02_Records/UC-001 Incomplete Fee Proposal/client-sent-output-analysis-muncie.md
```

This supersedes the earlier workbook-only `$34,760` candidate as the intended output value. `$34,760` remains the contract/schedule comparison basis; `$27,950` is the proposed fee visible in the sent artifact.

## SO Matrix Fee Basis Extracted

The Muncie SO Development Matrix workbook provided the draft fee-basis candidate and contract comparison:

```text
Small Remodel
Schedule F
Clinic Project Size (0-2,500 SF)
Contract comparison total: $34,760
```

Analysis record:

```text
02_Records/UC-001 Incomplete Fee Proposal/so-matrix-fee-basis-analysis-muncie.md
```

## Current Recommendation

Proceed with a **Grace-only Muncie architectural fee proposal exercise**:

1. exclude MEP consultant fees from this response;
2. note that MEP appears likely required later but is not included at this stage;
3. do not prepare a formal Service Order today;
4. use contract language, fee schedule, LCD, and SO Matrix to develop the small-project fee basis;
5. preserve unresolved assumptions/gaps separately.

## Time-to-Response Note

A separate timeline analysis records that the request was received on 2026-07-02 and responded to on 2026-07-09, with the office off on Friday 2026-07-03 for the Fourth of July holiday. Work began on 2026-07-06; the user built the matrix, asked UHG questions, and issued the internal assessment that day. The team then took three days to accumulate the actual budget/fee.

Record:

```text
02_Records/UC-001 Incomplete Fee Proposal/time-to-response-analysis.md
```

## Latest State — Post-Proposal Scope Negotiation

UHG has now responded after internal review and requested a call to discuss proposed scopes and associated fees. They are considering a reduced AOR scope focused primarily on site due diligence followed by advancement directly to a 90% CD set for review and final comments.

Preserved source:

```text
03_Communications/UC-001 Muncie/incoming-uhg-review-request-002-reduced-aor-call.md
```

Analysis and call prep:

```text
02_Records/UC-001 Incomplete Fee Proposal/post-proposal-review-analysis-reduced-aor.md
04_Output/UC-001 Incomplete Fee Proposal/reduced-aor-call-prep-agenda.md
```

Current workflow state is now:

```text
post_proposal_scope_negotiation
```

The next correct action is to prepare for the call and clarify reduced-AOR scope before revising fee/schedule.

However, because the user is on the UHG Admin Team, not the Clinical Projects team or PIC, the immediate response posture should be **acknowledgement/coordination only** until the proper internal team/PIC approves any scope or fee position.

Governance record:

```text
02_Records/UC-001 Incomplete Fee Proposal/authority-and-response-governance.md
```

## Remaining Deficiencies

The clarification and SO Matrix extraction removed several blockers, but these remain unresolved:

- user validation that the extracted `$27,950` proposed fee and `$34,760` contract comparison are the intended output values;
- Section 4.3 / one-off language still needs to be checked against the executed contract before final wording;
- interpretation of SO Matrix `X` rows and proposed `0` adjustments needs user validation;
- clean project location / SO number / formal representative fields remain missing but are not required for today's no-SO fee exercise;
- final MEP/security/x-ray responsibility boundaries remain deferred for later project execution.

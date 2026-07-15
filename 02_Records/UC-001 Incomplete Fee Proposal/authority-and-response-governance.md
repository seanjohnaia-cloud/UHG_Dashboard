---
record_type: authority_and_response_governance
status: active
use_case: UC-001
thread_state: post_proposal_scope_negotiation
---

# Authority and Response Governance — Reduced AOR Request

## User Constraint / Role Reality

The user clarified a critical governance constraint:

- User is on the **UHG Admin Team**.
- Administrative Projects and Clinical Projects are handled by different teams.
- The user may have more available time and could respond quickly.
- However, responding substantively now would not be prudent because:
  - the user is **not on the Clinical Projects team**;
  - the user is **not the PIC**;
  - the user cannot agree to a reduction in fee without approval.

## Governance Meaning

The constraint is not a workload issue. It is an **authority boundary**.

Pii must distinguish:

```text
ability_to_respond_now ≠ authority_to_commit_scope_or_fee
```

## Current Permitted Response Posture

The user can likely:

- acknowledge receipt;
- coordinate availability;
- preserve the issue for internal review;
- route the request to the proper team/PIC;
- prepare internal analysis and call questions.

The user should not independently:

- agree to a reduced AOR scope;
- agree to reduce the fee;
- commit to direct-to-90% CD delivery;
- represent that Grace accepts UHG's reduced-scope approach;
- speak for the Clinical Projects team or PIC.

## Required Internal Approval Before Substantive Commitment

Before Grace provides a substantive response on reduced scope/fee, Pii should require:

1. Clinical Projects team review;
2. PIC review/approval;
3. confirmation of who is authorized to speak on scope/fee;
4. confirmation of whether the current submitted fee can be reduced, reframed, or must remain as-is;
5. agreement on meeting posture before the UHG call.

## Updated Workflow State

The latest UHG email creates urgency, but the correct next state is not immediate client commitment.

Correct state:

```text
internal_authority_review_required_before_substantive_client_response
```

## Pii Lesson

Response-time pressure must be balanced against authority and governance.

A faster response is not better if it creates unauthorized scope/fee commitments.

For future tracking, Pii should capture:

```text
can_acknowledge_now: true/false
authorized_to_commit_scope: true/false
authorized_to_commit_fee: true/false
required_internal_approvers
approval_received_at
client_response_type: acknowledgement | coordination | substantive commitment
```

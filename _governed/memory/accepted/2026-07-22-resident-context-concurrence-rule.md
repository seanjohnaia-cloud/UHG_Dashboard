---
layer: memory
status: accepted
proposal_type: constitutional_rule_candidate
target_layer: decisions
source:
  - "_governed/raw/2026-07-22-session-capture-context-architecture-multiagent-control-system.md"
  - "_governed/synthesis/concepts/pii-tiered-context-architecture.md"
derived_by: hermes
confidence: high
uncertainty: "Boundary definition is unsettled: which synthesis pages count as 'resident/state context' (loaded per query / per project touch) vs. ordinary deep-tier synthesis. The rule's scope depends on a tier-classification convention that does not yet exist. Cadence (weekly?) and who counts as the concurring human (PM? designated reviewer?) are also open."
review_after: 2026-08-05
accepted_by: Sean Johnson
accepted_on: 2026-07-22
enacted_by_decision: "_governed/decisions/2026-07-22-resident-context-concurrence-rule.md"
supersedes: "_governed/memory/superseded/2026-07-22-resident-context-concurrence-rule-pending-draft.md"
admissibility: initiating
verification:
  status: unverified
  verified_by: null
  verified_on: null
  method: null
---

# Proposed rule: synthesis serving as resident/state context requires human concurrence on updates

## Claim

Any synthesis page that is loaded as resident or state-tier context (i.e., injected into every query or every project touch) is load-bearing regardless of its layer label. Updates to such pages may be **drafted** by AI (scrub + proposed revisions with diffs, consequence ranking, and pre-attached provenance) but may not take effect until a human concurs. Automated, ungated updates to load-bearing context are model output promoted to ground truth and are prohibited in effect even where permitted in form.

## Why this rises above ordinary synthesis rules

The existing constitution treats synthesis as freely AI-maintainable because it is non-authoritative. This session identified the gap: a synthesis page that hydrates every query functions as ground truth for all downstream reasoning regardless of its non-authoritative label. A wrong sentence in an obscure synthesis page misleads one lookup; a wrong sentence in the state tier poisons every query until noticed.

## Origin

User correction, 2026-07-22 session: automated current-state updates rejected where worker-entered data reaches the state layer without review. Required flow: AI scrubs/proposes → PM + AI process → human concurs. "That is the safeguard and the accountability rolled into one." The gate additionally emits accountability metrics (review latency, streaks, dialogue effectiveness) — see the control-system pending proposal filed alongside this one.

## Not enacted

This proposal binds nothing until a human authors an accepted decision record. Until then, agents should treat it as a candidate norm and behave conservatively (propose, don't auto-update state-tier pages).


## Acceptance note (2026-07-22)

Accepted under an open human review window. Authority is expressed through the decision record at `_governed/decisions/2026-07-22-resident-context-concurrence-rule.md`; this accepted-memory record carries the durable claim. The original pending draft is preserved with lineage at `memory/superseded/2026-07-22-resident-context-concurrence-rule-pending-draft.md`.
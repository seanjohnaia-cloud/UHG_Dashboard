---
layer: decision
status: accepted
source:
  - "_governed/raw/2026-07-22-session-capture-context-architecture-multiagent-control-system.md"
  - "_governed/raw/2026-07-22-chat-archive-context-architecture-session.md"
  - "_governed/memory/pending/2026-07-22-resident-context-concurrence-rule.md (promoted; superseded lineage at memory/superseded/)"
decided_by: Sean Johnson
decision_date: 2026-07-22
supersedes: null
admissibility: supporting
verification:
  status: verified
  verified_by: Sean Johnson
  verified_on: 2026-07-22
  method: "Human review under open review window (.review-open), following live-session development and explicit boundary-option selection."
---

# Decision: Synthesis serving as resident/state context requires human concurrence on updates

## Rule

Any synthesis page that is loaded as **resident or state-tier context** — injected into every query or every project touch — is load-bearing regardless of its non-authoritative layer label. Updates to such pages:

1. **May be drafted by AI**: automated scrub of worker-entered data, proposed revisions presented as field-level diffs with consequence ranking and pre-attached provenance.
2. **Must be processed by PM + AI** and **take effect only on human concurrence.**
3. Between reviews, unreviewed proposed deltas must be **visibly flagged** in any context that loads the page (concurred state + flagged staleness; silent staleness is prohibited).

Automated, ungated updates to load-bearing context are model output promoted to ground truth and are prohibited in effect even where permitted in form.

## Boundary (interim — option a, selected by decider)

A page counts as resident/state-tier context **iff it is listed as such in the project's `_governed/index.md`**. Pages so listed are tagged in their frontmatter as they are touched. This is an enforceable interim convention; a formal tier-classification convention is a named follow-up and may refine this boundary via a superseding decision — it does not weaken the rule in the meantime.

## Accountability metrics (part of the rule's intent, per decider)

The gate emits its own telemetry: weekly processing compliance (who is not processing their updates), review latency **and depth**, consecutive no-comment approval streaks, and dialogue effectiveness measured by outcome (comment-to-revision rate), not volume. Concurrence is the safeguard and the accountability rolled into one.

## Lineage

Proposed in-session 2026-07-22 (user correction of an AI framing that would have allowed agent-maintained current-state pages); filed as pending memory the same day; accepted under an open review window the same day with boundary option (a). The pending draft is preserved at `memory/superseded/` with pointer frontmatter; the accepted memory record lives at `memory/accepted/2026-07-22-resident-context-concurrence-rule.md`.

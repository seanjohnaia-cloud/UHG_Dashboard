---
layer: memory
status: superseded
proposal_type: pattern_candidate
target_layer: decisions
source:
  - "_governed/raw/2026-07-22-session-capture-context-architecture-multiagent-control-system.md"
  - "_governed/synthesis/concepts/pii-tiered-context-architecture.md"
  - "_governed/synthesis/concepts/pii-integrity-first-context-economy.md"
derived_by: hermes
confidence: medium
uncertainty: "Untested design, not implementation. Open: session-state artifact for conversational continuity; human-declared per-session context mode; concrete proposal-format/triage specs for the gate; audit sampling parameters; whether the single-pen rule survives real multi-agent operation. Claimed as Pii-generic core, but developed in one specimen project (UHG_Dashboard) — the generalization test has not been run against a second project."
supersedes: null
superseded_by: "_governed/memory/accepted/2026-07-22-tiered-context-control-system-pattern.md"
superseded_on: 2026-07-22
superseded_reason: "Promoted to accepted memory via _governed/decisions/2026-07-22-tiered-context-control-system-pattern.md under open review window."
review_after: 2026-08-05
admissibility: initiating
verification:
  status: unverified
  verified_by: null
  verified_on: null
  method: null
---

# Proposed pattern: the tiered-context / concurrence-gate control system (Pii-generic core candidate)

## Claim

The following five-layer stack is proposed as a **Pii-generic core pattern** (tier 1 of the 3-tier field schema), not a UHG-specific overlay:

```text
1. Tiered context        — resident / state / deep / archival, mapped onto _governed/ layers;
                           deterministic loading driven by metadata; depth escalation triggered
                           by structure (conflict/assumed states, decision citations), never by
                           model confidence
2. Concurrence gate      — AI scrubs and proposes state-tier revisions (diffs, consequence
                           ranking, provenance pre-attached, staleness flags); PM + AI process;
                           human concurs; nothing load-bearing updates ungated
3. Gate-health metrics   — no-comment approval streaks; dialogue effectiveness by outcome
                           (comment-to-revision rate), not volume; review latency AND depth
4. Reality audit         — designated QC person verifies screen-vs-reality, human to human;
                           measures correspondence, which no internal (coherence) check reaches;
                           risk-weighted sampling (assumed fields, long streaks, recent revisions)
5. Feedback              — audit findings re-enter as raw/ records, drive conflict states, and
                           flow through the same pending→concur pipeline
```

Each layer watches the layer below; the top layer is a human in the field.

Supporting multi-agent rules proposed with it: partition agents by governed layer (scoping/map, workers/pre-scoped bundles, orchestrator/continuity), governed handoffs carrying PI metadata (no provenance laundering), and the **single-pen rule** — only the orchestrator writes to `pending/`, with the worker chain in provenance.

## Origin

2026-07-22 session (user + Hermes), developed from the user's realization that multi-agent architecture is fundamentally context partitioning for continuity, the integrity-first requirement ("project integrity nothing else right now"), the concurrence correction, and the user's embedded-metrics + human-to-human audit scheme. Design lineage is preserved in the Instance 2 Exchange Development Extraction.

## Not enacted

No tooling, dashboard, or agent behavior should assume this pattern until a decision record accepts it (in whole or narrowed). The two synthesis pages carry the full articulation; this proposal exists so the pattern enters the governed promotion pipeline rather than living only in synthesis.

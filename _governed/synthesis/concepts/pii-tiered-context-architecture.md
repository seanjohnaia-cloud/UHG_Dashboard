---
layer: synthesis
status: draft
source:
  - "_governed/raw/2026-07-22-session-capture-context-architecture-multiagent-control-system.md"
  - "_governed/extractions/exchange-development/2026-07-22-exchange-development-extraction-v0.1-instance-2-context-architecture-control-system.md"
confidence: medium
updated: 2026-07-22
admissibility: initiating
verification:
  status: unverified
  verified_by: null
  verified_on: null
  method: null
---

# Pii Tiered Context Architecture (System Level)

Non-authoritative synthesis. Design reasoning from the 2026-07-22 session; nothing here is tested implementation or accepted structure. Candidate rules are flagged as such and belong in `memory/pending/` → decision review before enactment.

## Problem statement

A single agent's context window is a structural roadblock to continuity: each query forces re-remembering the project, most tokens go to rehydration rather than reasoning, and continuity dies when windows fill. The industry's answers (multi-agent for capacity, iceberg loading, cost-tier routing) optimize for **cost**. Pii requires optimization for **integrity** — the right context, with the right standing, every query — with economy falling out of the same structure.

## The four context tiers

| Tier | Contents | Load policy | Cost |
|---|---|---|---|
| **Resident** | Constitution/AGENTS.md, `index.md`, layer schemas | Every query | Tiny, stable |
| **State** | Field truth states, statuses, pending chain, current-state synthesis pages | Every project touch | Small — day-to-day operations live here |
| **Deep** | Full synthesis pages, decision records, extractions | Per question, scoped by citations | Medium |
| **Archival** | `raw/`, `superseded/`, full lineage | Research/audit only | Heavy, rare |

The tiers are not new structure — they are the existing `_governed/` layers reinterpreted as a context-loading policy. Governance metadata (status, supersession, admissibility) is what makes deterministic tier loading possible at all.

### Capability honesty boundary

- **Reliable now:** deterministic tier loading driven by machine-readable metadata (bookkeeping — no model judgment involved).
- **Not reliable now:** the model judging what depth a query needs. Models are poor at knowing what they don't know; the failure mode is confidently answering deep questions from shallow context.

### Candidate rule — structure-triggered depth escalation

Depth escalation is triggered by **structure, not model confidence**: a field state of `conflict` or `assumed`, or a citation to a decision record, forces the deep load. Metadata decides context depth; the agent's self-assessed recall does not. The human remains the only party entitled to say "general context is enough" when structure says otherwise.

### Prerequisite

The state tier only works if current-state pages are maintained. A stale state tier produces confidently wrong context at every query — which is why state-tier updates are gated (below), and why staleness must be **visible**: between reviews, queries see concurred state plus flagged unreviewed deltas, never silent staleness.

## Multi-agent as context partitioning

Motivation reframed from the standard capacity/expertise arguments: multi-agent exists so that **no single window must reconstruct the whole project per query**. Partition by governed layer, not by topic (topics interlock; layers have genuinely different context requirements):

- **Scoping/retrieval agent** — holds only the map (index, schemas, statuses). Job: "which records does this query need?"
- **Worker agents** — receive pre-scoped bundles; deep but narrow context; disposable afterward.
- **Orchestrator/session agent** — holds conversational continuity and the pending chain; never the full corpus.

Continuity splits into two problems: **project continuity** (externalized in `_governed/`, solved by scoped retrieval) and **conversational continuity** (model-native working context; open question whether a lightweight non-authoritative session-state artifact should exist).

### Governed handoffs

Ungoverned multi-agent pipelines launder provenance: each hop turns "claim with sources" into "the upstream agent said so" — circular provenance at machine speed (Authority Rule 8). Therefore inter-agent handoffs must carry PI metadata (source refs, confidence, admissibility), not bare content.

### Candidate rule — single pen

Workers return candidates **to the orchestrator**; only the orchestrator writes to `memory/pending/`, recording itself as `derived_by` with the worker chain in provenance. One writer, many thinkers. (A proposer/critic debate step *before* the pen writes is constitutionally free — it happens entirely in working context.)

### Retrieval caveat

If the Pii Console gains semantic/vector search, PI metadata must survive retrieval: filter or rank by status/supersession/admissibility, never similarity alone. A vector store returns superseded and current records as equally good neighbors; plain RAG over `_governed/` is a governance bug.

## The concurrence gate

State-tier content is load-bearing regardless of layer label: a wrong sentence in resident/state context poisons every query until noticed. Therefore (candidate constitutional rule): **synthesis that serves as resident/state context requires human concurrence on updates.**

Flow: workers (humans) enter data → AI scrubs and drafts proposed revisions → PM + AI process → **human concurs** → state tier updates. The gate is safeguard and accountability in one, and it emits metrics natively.

The gate's real failure mode is rubber-stamping, not skipping. The AI owes the gate, to keep concurrence cheap enough to stay real:

1. **Diffs, never documents** — field-level deltas with source ("X: `assumed` → `validated`, source: client email 7/21"), not rewritten pages.
2. **Consequence ranking** — triage what matters this week vs. batch-concurrable routine.
3. **Provenance pre-attached** — review is judgment, not investigation.
4. **Honest staleness signal** — unreviewed deltas visibly flagged in query context.

Human-side obligations: explicit corrections, decisions landed as records, worker-entry stream reaching the AI in structured form.

## The control system (assembled)

```text
tiered context                 (economy)
  → human concurrence gate       (authority)
    → streak / dialogue metrics    (gate health)
      → print-to-reality audit       (ground truth)
        → findings re-enter as records (feedback)
```

- **Gate-health metrics:** consecutive no-comment approval streaks (rubber-stamp detector — deliberately ambiguous alone); effective vs. non-effective dialogue measured by *outcome* (comment-to-revision rate; did gate corrections reduce audit misses), not volume; review latency **and depth** (a queue cleared in 90 seconds is a worse sign than one cleared slowly).
- **Reality audit:** a designated QC person prints what the screen claims and verifies it against reality — human-to-human. This measures **correspondence** (record vs. world), which no internal check reaches; internal checks verify only **coherence** (record vs. record). Sampling should be risk-weighted: oversample `assumed` fields, long-streak approvals, and anything downstream of recent process revisions.
- **Discrepancy localization:** layer separation lets one audit finding be attributed to source (worker entry), scrub (AI), gate (reviewer), or view (display) — four different fixes from the same finding.
- **Feedback:** audit findings land as `raw/` records, drive `conflict` field states, and flow through the same pending→concur pipeline. Audits that don't re-enter the system are theater; audits that do are the system's immune memory.

## Open questions

- Session-state scratch artifact for conversational continuity (shape, standing, lifecycle).
- Human-declared per-session context mode (day-to-day vs. research), Centerline-style.
- Reasoning-architecture selection per Pii task class (CoT/ToT/debate mapping).
- Concrete proposal-format and triage-rank specifications for the gate.
- Audit sampling parameters and cadence.

## Standing

Draft synthesis; cites the raw session record and Instance 2 extraction. The two candidate rules (resident-context concurrence; single pen) and the control-system pattern are proposed in `memory/pending/` and are not enacted. Client-overlay note: this page describes candidate **Pii-generic core** architecture, not UHG-specific overlay; UHG_Dashboard is the specimen project where it was developed.

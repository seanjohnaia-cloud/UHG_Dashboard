---
layer: extraction
extraction_type: exchange-development
version: v0.1
instance: 2
captured_at: 2026-07-22
source_type: session
source_ref: "_governed/raw/2026-07-22-session-capture-context-architecture-multiagent-control-system.md (direct session record; Hermes observed this exchange first-hand)"
captured_by: hermes (at explicit user direction, in-session)
admissibility: initiating
verification:
  status: unverified
  verified_by: null
  verified_on: null
  method: null
---

# Exchange Development Extraction — Instance 2

**Subject:** Tiered Context Architecture, Multi-Agent Partitioning, and the Human-Concurrence Control System

**Participants:**

- Human Designer (Sean Johnson)
- AI Design Collaborator (Hermes)

**Provenance note:** Unlike Instance 1 (which captured the user's narration of a prior exchange), this record is drawn from a session Hermes observed first-hand. The evidentiary chain runs through direct session logs preserved in the cited raw record. This makes Instance 2 the stronger provenance specimen of the two for evaluating the sub-type.

---

## Exchange 001

### Initiation (Human)

Tree of Thoughts, from an external course: agents branching like a chess player evaluating moves.

### AI Interpretation

Sharpened the analogy — chess engines *prune* and discard; Pii preserves abandoned branches as supersession lineage. Posed the tension: ToT branches as ephemeral working context vs. ToT traces as decision-record raw material.

### Human Response

Redirected to the broader point rather than the technique.

### Emergent Insight

Rejected reasoning branches are evidence in Pii, exhaust in standard agentic practice.

---

## Exchange 002

### Initiation (Human)

> there are different architectures for different reasoning functions

### AI Interpretation

Built the taxonomy (CoT / ToT / GoT / ReAct / Reflexion / Debate) and proposed the meta-rule: architecture selection is itself a reasoning decision. Mapped architectures onto existing Pii structures (workflow execution, design alternatives, synthesis, federation).

### Human Response

"Exactly" — confirmed, then pivoted to the source course for shared ground.

### Architectural Consequence

Opened the question of whether Pii should specify reasoning architecture per task class. (Left open.)

---

## Exchange 003

### Initiation (AI, from course ingestion)

Flagged three course sections as constitutionally loaded: storage-shaped vs. authority-shaped memory taxonomies; self-modifying agents as ungated accepted-memory writes; RAG similarity search as authority-blind (superseded and current records are equally good neighbors).

### Human Response

Selected multi-agent systems as the thread to develop.

### Emergent Insight

Plain RAG over `_governed/` would be a governance bug: PI metadata must survive retrieval.

---

## Exchange 004

### Initiation (AI)

Critique of course multi-agent topologies: inter-agent handoffs launder provenance; governed handoffs must carry PI metadata. Proposed the single-pen rule (workers return candidates; only the orchestrator writes to `pending/`) and identified Pii → Risk Management → DIF as a bordered-pipeline topology absent from the course.

### Human Response — reframing

> to me its a structural thing how much context can 1 agent hold and that becomes a major road block to continuity… limit what one agent has to "re-remember" as each querry comes in

### Emergent Insight

**Multi-agent as context partitioning, not skill partitioning.** The human's motivation was continuity economics, not expertise division — a motivation the course does not name.

### Architectural Consequence

Partition by governed layer, not topic: scoping agent (map only) / workers (pre-scoped bundles) / orchestrator (continuity + pending chain, never full corpus). Project continuity vs. conversational continuity separated as distinct problems.

---

## Exchange 005

### Initiation (Human)

> i need to know it can do what i think it can do and not what i "want" it to do. i need project integrity nothing else right now.

Plus the human context-mode analogy: day-to-day operations vs. researching an 8-year-old project require different context depths; "there are economies we have not explored within the architecture."

### AI Interpretation

The tiered context model (resident / state / deep / archival), mapped onto existing `_governed/` layers. Capability honesty line: deterministic tier loading is reliable today; model-judged depth selection is not. Proposed the integrity rule: **depth escalation triggered by structure (field states, citations), not model confidence.**

### Emergent Insight

Industry optimizes context for cost; Pii optimizes for integrity, and economy falls out of the same structure. Admissibility and relevance are the same computation run for different purposes.

---

## Exchange 006 — [COURSE CORRECTION]

### Initiation (Human)

Rejected automated state-tier updates where worker-entered data bypasses review. Required flow: AI scrubs and proposes → PM + AI process → **human concurs**. "That is the safeguard and the accountability rolled into one." Introduced the gate as a metric source (weekly processing compliance) and asked the AI directly what is hard, labor-intensive, and in need of improvement — "this only works with your active participation."

### AI Response

Acknowledged the near-slip: resident-loading synthesis is load-bearing regardless of layer label; an unreviewed auto-update is model output promoted to load-bearing status. Named the real failure mode — **gates die by rubber-stamping, not by being skipped** — and accepted the labor burden as primarily the AI's: diffs not documents, consequence ranking, provenance pre-attached, honest staleness signaling. Pushed back on compliance-metrics-as-endpoint (measure latency and depth; fast-cleared queues are a warning sign).

### Emergent Insight

Concurrence must be made cheap enough to stay real; proposal format and triage design are integrity engineering.

### Architectural Consequence

Candidate constitutional rule identified (not filed as decision): synthesis serving as resident context requires human concurrence on updates.

---

## Exchange 007

### Initiation (Human)

Embedded synthesis metrics: effective vs. non-effective dialogue; consecutive no-comment approval streaks; and the anchor —

> how accurate is what a designated QC person prints off the screen to reality? a human to human audit.

### AI Interpretation

The three metrics triangulate: streaks detect rubber-stamping but are ambiguous alone; the reality audit disambiguates. The audit measures **correspondence** (record vs. world), which no internal check can reach — internal checks only verify **coherence** (record vs. record). Layer separation localizes discrepancies to source/scrub/gate/view. Cautions: Goodhart on dialogue metrics (measure comment-to-revision outcome, not volume); audit findings must re-enter as governed records or the audit is theater.

### Emergent Insight

A human in the field with a printout is the only ground-truth anchor in the architecture — the user's professional QA/QC field-verification practice applied to an information system.

---

## Exchange 008 — Assembly

### Initiation (AI)

Named the accumulated design a control system:

```text
tiered context → concurrence gate → gate-health metrics → reality audit → findings re-enter as records
```

Each layer watches the layer below; the top layer is a human in the field.

### Human Response

> were ready lets definitly capture this at the system architectural level and the philosophical level as well. i think this is very close to being something real

---

## Design Lineage

**Originated primarily from the Human this session:**

- Architectures-per-reasoning-function realization.
- Multi-agent as a continuity/context problem ("re-remember").
- Integrity before economy; capability honesty demand.
- Human context-mode analogy (hyper vs. general context).
- The human concurrence gate as safeguard + accountability + metric.
- Effective/non-effective dialogue metrics; approval-streak metric.
- The human-to-human print-to-reality audit.

**Originated primarily through AI synthesis:**

- Architecture-selection-as-reasoning-decision meta-rule.
- Provenance laundering critique of ungoverned multi-agent handoffs.
- Single-pen rule; bordered-pipeline as fifth topology.
- Layer-based (not topic-based) context partitioning.
- Four-tier context model mapped to `_governed/` layers.
- Structure-triggered depth escalation rule.
- Rubber-stamp failure mode; diffs/triage/provenance/staleness obligations.
- Coherence vs. correspondence distinction; discrepancy localization.
- Audit-findings-as-immune-memory feedback requirement.

**Emerged collaboratively:**

- Governance structure doubling as context-economy structure.
- Admissibility and relevance as the same computation.
- The five-layer control system as an assembled whole.
- Concurrence-cost engineering as integrity engineering.

---

## Unresolved Questions

- Does the orchestrator need a lightweight non-authoritative session-state artifact for conversational continuity across window resets?
- Should the human declare a per-session context mode (day-to-day vs. research), Centerline-style?
- Should Pii specify reasoning architecture per task class?
- What are the concrete proposal-format and triage-rank specifications that keep concurrence cheap?
- Risk-weighted audit sampling parameters.

---

## Standing of this record

This is the **second provisional instance** of the Exchange Development Extraction sub-type, filed at explicit user direction to strengthen the ratification case described in Instance 1 (`2026-07-22-exchange-development-extraction-v0.1-pii-information-architecture.md`). Per Authority Rule 9, this record is preservation, not authority. The sub-type remains candidate/provisional: no decision record has yet formalized its triggers, schema, or filing conventions. Two instances now exist as schema examples — one narrated-source (Instance 1), one direct-session (Instance 2) — giving a future ratification review both provenance variants to evaluate. No further instances should be treated as routine practice until that decision record exists.

# Governed Layer Index — Pii UHG Dashboard

Status: initialized (bootstrapped 2026-07-22)

This project inherits its governance pattern from the production PI environment at `C:\Obsidian\My Projects\PI v1\`. It is a separate Pii project instance: its `_governed/` layer is its own, scoped to the UHG Dashboard engagement (client overlay + dashboard build), not the abstract Pii/DIF architecture itself.

## Layers

- `raw/` — append-only source records (session captures, client communications, site/workflow facts)
- `extractions/` — preservation records from source material, including structured extraction sub-types (see below)
- `memory/pending/` — AI/user proposed durable memory awaiting review
- `memory/accepted/` — human-gated durable memory
- `memory/superseded/` — retired memory with lineage
- `synthesis/` — WikiLLM living wiki; non-authoritative synthesis
- `decisions/` — authority-bearing design/process decision records
- `index.md` — this file

## Extraction sub-types in use

- **Exchange Development Extraction** (`extractions/exchange-development/`) — captures the reciprocal development of ideas between human and AI across a session (who initiated, how the other party interpreted/extended it, what emerged, what changed architecturally) rather than only the resulting conclusions. Instances: `2026-07-22-exchange-development-extraction-v0.1-pii-information-architecture.md` (Instance 1, narrated-source provenance) and `2026-07-22-exchange-development-extraction-v0.1-instance-2-context-architecture-control-system.md` (Instance 2, direct-session provenance, filed at explicit user direction to strengthen the ratification case). This sub-type is candidate/provisional — it has not yet been ratified as a permanent artifact class via a decision record. Treat its existence and schema as `initiating`, not `supporting`, until reviewed.

## Raw source records

- `raw/2026-07-22-session-capture-context-architecture-multiagent-control-system.md` — direct session record: tiered-context architecture, multi-agent context partitioning, human-concurrence gate, gate-health metrics, human-to-human reality audit, and the assembled control system. Append-only.

## Synthesis pages in use

- `synthesis/concepts/pii-console-team-side-architecture.md` — draft synthesis of the Pii Console (internal, team-side) system: Sonar Bunker graph + Amber Command console, launch-context inheritance from Centerline, stable-node/multi-view graph model, and the explicit exclusion of Institutional Learning (DIF-only). Non-authoritative; open questions listed in the page itself.
- `synthesis/concepts/pii-tiered-context-architecture.md` — draft, system level: four context tiers mapped onto `_governed/` layers, structure-triggered depth escalation, multi-agent partitioning by layer, single-pen rule, concurrence gate, and the five-layer control system. Non-authoritative.
- `synthesis/concepts/pii-integrity-first-context-economy.md` — draft, philosophical level: integrity precedes economy, admissibility ≡ relevance, coherence vs. correspondence, gates die by rubber-stamping, findings must re-enter. Non-authoritative.

## Pending memory proposals

- `memory/pending/2026-07-22-resident-context-concurrence-rule.md` — candidate constitutional rule: synthesis serving as resident/state context requires human concurrence on updates.
- `memory/pending/2026-07-22-tiered-context-control-system-pattern.md` — candidate Pii-generic core pattern: the five-layer tiered-context / concurrence-gate control system, plus supporting multi-agent rules.

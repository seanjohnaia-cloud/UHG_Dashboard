# Governed Layer Index — Pii UHG Dashboard

Status: active (bootstrapped 2026-07-22; first review window exercised 2026-07-22)

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

## Context tiers (per accepted decisions of 2026-07-22)

Pages listed in this index are classified for context loading per `decisions/2026-07-22-tiered-context-control-system-pattern.md`. Interim boundary rule (per `decisions/2026-07-22-resident-context-concurrence-rule.md`): a page is resident/state-tier **iff listed as such here**; such pages require human concurrence on updates.

- **Resident tier:** `AGENTS.md` (project root), this `index.md`.
- **State tier:** *(none yet — current-state synthesis pages will be listed here as they are created and tagged).*
- All other synthesis/extraction/decision content is deep tier; `raw/` and `memory/superseded/` are archival tier.

## Extraction sub-types in use

- **Exchange Development Extraction** (`extractions/exchange-development/`) — **ratified standing artifact class** per `decisions/2026-07-22-ratify-exchange-development-extraction.md` (triggers, schema, filing rules defined there). Captures the reciprocal development of ideas between human and AI across a session (who initiated, how the other party interpreted/extended it, what emerged, what changed architecturally) rather than only the resulting conclusions. Records remain preservation, not authority (Authority Rule 9). Instances: Instance 1 `2026-07-22-exchange-development-extraction-v0.1-pii-information-architecture.md` (narrated-source provenance); Instance 2 `2026-07-22-exchange-development-extraction-v0.1-instance-2-context-architecture-control-system.md` (direct-session provenance). The provisional-standing notes inside both instances are superseded by the ratification decision (left visible in place, per Authority Rule 6).

## Raw source records

- `raw/2026-07-22-session-capture-context-architecture-multiagent-control-system.md` — direct session record: tiered-context architecture, multi-agent context partitioning, human-concurrence gate, gate-health metrics, human-to-human reality audit, and the assembled control system. Append-only.
- `raw/2026-07-22-chat-archive-context-architecture-session.md` — turn-by-turn chat archive of the same session (user turns verbatim; AI turns condensed and marked). Companion shape to the structured capture above. Append-only.

## Synthesis pages in use

- `synthesis/concepts/pii-console-team-side-architecture.md` — draft synthesis of the Pii Console (internal, team-side) system: Sonar Bunker graph + Amber Command console, launch-context inheritance from Centerline, stable-node/multi-view graph model, and the explicit exclusion of Institutional Learning (DIF-only). Non-authoritative; open questions listed in the page itself.
- `synthesis/concepts/pii-tiered-context-architecture.md` — system level: four context tiers mapped onto `_governed/` layers, structure-triggered depth escalation, multi-agent partitioning by layer, single-pen rule, concurrence gate, and the five-layer control system. Non-authoritative; its candidate rules are now enacted via the decisions of 2026-07-22.
- `synthesis/concepts/pii-integrity-first-context-economy.md` — philosophical level: integrity precedes economy, admissibility ≡ relevance, coherence vs. correspondence, gates die by rubber-stamping, findings must re-enter. Non-authoritative.

## Accepted memory

- `memory/accepted/2026-07-22-resident-context-concurrence-rule.md` — synthesis serving as resident/state context requires human concurrence on updates. Enacted via `decisions/2026-07-22-resident-context-concurrence-rule.md` (interim boundary: index-listing). Pending draft preserved in `memory/superseded/`.
- `memory/accepted/2026-07-22-tiered-context-control-system-pattern.md` — the five-layer tiered-context / concurrence-gate control system plus supporting multi-agent rules (layer partitioning, governed handoffs, single-pen). Accepted **narrowed**: candidate Pii-generic core pending the second-project generalization test (Dunham / LPSO / LUC); binds this project, does not bind Pii core schema. Enacted via `decisions/2026-07-22-tiered-context-control-system-pattern.md`. Pending draft preserved in `memory/superseded/`.

## Pending memory proposals

- *(none — queue cleared at the 2026-07-22 review window)*

## Decision records

- `decisions/2026-07-22-candidate-operational-data-layer-wikillm-pattern.md` — **candidate, not accepted**: new operational data layer distinct from synthesis. Blocked on two open questions (approval-gate/Elevate mechanics; Extract/Absorb/Elevate/Quarantine behavior).
- `decisions/2026-07-22-resident-context-concurrence-rule.md` — **accepted**.
- `decisions/2026-07-22-tiered-context-control-system-pattern.md` — **accepted (narrowed)**.
- `decisions/2026-07-22-ratify-exchange-development-extraction.md` — **accepted**.

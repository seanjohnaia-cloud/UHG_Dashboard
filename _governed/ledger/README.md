# Ledger — Current Operational Truth with Lineage

Established by `_governed/decisions/2026-07-22-candidate-operational-data-layer-wikillm-pattern.md` (accepted 2026-07-22).

## Definition

The ledger is the project's **current operational truth with lineage** — the single place where live, canonical, per-project field values reside: budget figures, schedule dates, compensation terms, consultant assignments, PAC/LCD-W field instances. Like an accounting ledger: entries are corrected by new lineaged entries, never by silent erasure (Authority Rule 6 supersession at field grain); the current balance is always readable; the history of every value is always reconstructible.

## Where it sits among the layers

| Layer | Answers |
|---|---|
| `raw/` | what was received (append-only evidence) |
| `synthesis/` | what we think it means (non-authoritative) |
| `decisions/` | what was ruled (authority) |
| **`ledger/`** | **what currently is** (mutable-with-approval operational state) |

In tiered-context terms (per `decisions/2026-07-22-tiered-context-control-system-pattern.md`), the ledger is the **permanent home of the state tier**: ledger content loads on every project touch and is therefore load-bearing, governed by the concurrence rule (`decisions/2026-07-22-resident-context-concurrence-rule.md`).

**Naming note:** deliberately not called "operations" — that term belongs to the process-centric Contract → Operations → Institutional Learning stack, a process taxonomy, not a data store.

## Rules of operation

1. **Field-level records, three-tier schema** — Pii-generic core fields / client-contract overlay fields (UHG LCD-W is the first overlay) / per-project instance values. Every field carries its own provenance, state, and dependents list.
2. **Hybrid format** — structured YAML frontmatter per field record (machine-resolvable dependencies, provenance, field truth state) + markdown body (human-readable context and audit trail).
3. **Mutable with approval only** — changes enter as proposals (a PM's **Elevate**, or AI scrub output) into `memory/pending/`; they take effect on **human concurrence**, never on proposal. Elevate is intake, not approval.
4. **Field truth states apply** — `provided`, `extracted`, `validated`, `assumed`, `missing`, `conflict`, `deferred`, `unknown`, `not_required`. `conflict`/`assumed` trigger mandatory depth escalation per the control-system decision.
5. **Single source, many lenses** — Pii Console modules read/write against this layer only; no module holds its own copy. An approved change is visible to every dependent module by construction.
6. **Lineage always** — a corrected value supersedes visibly; prior approved values are never silently lost.

## Status

Layer established, currently empty. First entries should come from the active UHG slice (Service Order / LCD-W field instances) through the Extract → pending → concurrence path.

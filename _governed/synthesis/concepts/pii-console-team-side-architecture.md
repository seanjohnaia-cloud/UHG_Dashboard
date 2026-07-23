---
layer: synthesis
status: draft
source:
  - session discussion, 2026-07-22, Pii UHG Dashboard project (Hermes session)
  - _governed/extractions/exchange-development/2026-07-22-exchange-development-extraction-v0.1-pii-information-architecture.md
  - sketches/001-amber-console/, sketches/002-sonar-bunker/, sketches/003-patchbay-modular/ (disposable HTML comparison sketches)
  - C:\Obsidian\My Projects\PI v1\_governed\raw\2026-07-20-centerline-deferred-from-pii-synthesis.md
confidence: medium
admissibility: initiating
verification:
  status: unverified
  verified_by: null
  verified_on: null
  method: null
updated: 2026-07-22
---

# Pii Console — Team-Side Architecture (Concept)

## Status

Draft synthesis from a single design session. Non-authoritative — this describes an emerging shared understanding, not a decision. No decision record exists yet ratifying this architecture. Treat as citable working context, not as settled system design.

## Scope boundary: Pii Console vs. the existing Streamlit dashboard

Two separate systems, deliberately not merged:

- **`05_Dashboard/*` (existing Streamlit app — `project_home_dashboard.py`, LCD/Metrics/Contracts pages)** is the client/deliverable-facing tool. It stays as-is. It is out of scope for the redesign discussed in this session.
- **Pii Console (new, net-new build, not Streamlit)** is internal, team-side. It is the firm's own operational view of a project — process-centric, phase-as-metadata, full visibility into gaps/risk/flags that would not be shown raw to the client.

The original complaint that motivated this discussion — Streamlit's widget-driven layout collapsing "Appearance" back into generic PM-SaaS visual grammar — applies to the client-facing tool. Pii Console sidesteps the problem by not being built on Streamlit at all, and by not needing to match client-facing constraints.

A client-facing redesign (if wanted later) is a separate, later design conversation with its own audience and its own client-overlay boundary considerations (see `PI v1`'s `pii-client-overlay-boundary.md` synthesis for the general pattern this project inherits).

## Launch context: inherited from Centerline, not re-derived

Pii Console is launched **from inside Centerline**, already scoped to a specific project — the launch itself is the context-setting event, analogous to a terminal inheriting its working directory. The launch triggers preloading of that project's data files and Statement of Understanding.

Consequence: **Pii Console does not need a portfolio-level zoom step.** There is no "which project am I in" navigation inside Pii Console itself — that question is answered before Pii Console opens. This significantly simplifies the graph model discussed below (see "Rejected: two-level zoom").

Noted dependency: Centerline is currently kept **outside** Pii governance/synthesis as a separate test environment (per the PI v1 raw record `2026-07-20-centerline-deferred-from-pii-synthesis.md`, ~1 year horizon before IT integration consideration). This session establishes that Pii Console *consumes* a launch/context handoff from Centerline as a real integration point, even though Centerline itself remains outside `_governed/`. This dependency should be tracked explicitly rather than assumed away — it is a seam between an ungoverned environment and a governed one.

## Two-screen model

1. **Sonar Bunker (landing/navigation screen).** A force-directed graph, amber-recolored from the original green sketch. Nodes = **modules** for the current (already-scoped) project — Budget, Schedule, Compensation, Consultants, Contracts, etc. Clicking a module node navigates into that module's console.
2. **Amber Command (per-module console).** The module's working screen: central dialogue/status display, a Perspective bank (toggle switches + amplitude knobs) for tuning which lens(es) of data are emphasized, a quick-glance gauge cluster, and the Extract / Absorb / Elevate / Quarantine function strip (mapping onto the governed pipeline: raw → synthesis → decision, plus a hold/flag state).

Both screens originated as disposable comparison sketches (`sketches/001-amber-console/`, `sketches/002-sonar-bunker/`) and are not yet implementation-grade code.

## Graph model: stable nodes, multiple clustering views

Modules are **one stable node set** with a persistent identity regardless of how they're currently arranged. A "view" is a clustering function applied to that same node set — not a separate dataset and not a separate graph.

Two views were the earliest candidates:

- **Contract-structure view** — clusters/colors nodes by phase or contract deliverable grouping (SD, DD, CD, etc.)
- **Process (Operations) view** — clusters nodes by the firm's actual recurring operational categories, independent of contract phase

The set of views is explicitly **open-ended** — "whatever else develops" (e.g. a future risk-exposure view, a consultant-assignment view) should be addable as a new clustering function without redesigning the node model. This requires each module/node to carry enough relationship metadata (phase, process category, contract line, consultant, etc.) that any clustering view can be computed from the same underlying records — no view-specific structure should be baked into the node itself.

**Correction (2026-07-22, same session):** an earlier draft of this note characterized "keep as close to current state as possible" as a UI/animation preference (re-layout continuity, preserved pan/zoom on view switch). The user corrected this: the actual concern is **project data integrity**, not view-transition smoothness.

There is **one canonical data set per project**. A module is not an independent copy or a projection with its own state — it is a lens onto shared underlying data. If a value is modified and approved through one module/view, every other module that depends on that same underlying data must reflect the update immediately, because all views read the same source of truth rather than parallel copies that could drift out of sync. Whatever path a user takes to reach or change a piece of data, the result is identical everywhere that data is used.

This makes "Pii understands the relationships" a hard requirement rather than a UX nicety: Pii must maintain an explicit dependency/reference structure — which fields in which modules read which underlying data — so that an approved change propagates correctly to every dependent module, not merely to whatever screen is currently open.

Consequence for the graph model: edges between modules should be understood as (at least in part) **actual data-dependency edges** — e.g. Budget reads Compensation's approved figures; Schedule reads Design Milestone dates that Contracts also references — not only "this process is active on this project" or clustering-relationship edges. The clustering/view mechanism described above is a separate concern (how nodes are visually arranged) from this integrity requirement (what data a node's approved state actually feeds).

Re-layout/animation continuity on view switch may still be a reasonable UI choice, but it is not what "keep as close to current state as possible" was about, and should not be conflated with the data-integrity requirement above.

Phase/contract state also renders as node color/ring in the process view (and vice versa) — both lenses stay visible as different visual channels (position vs. color) rather than one lens hiding the other behind a toggle. This directly demonstrates the project's stated principle that phases are contract/invoicing metadata, not the organizing structure of how the firm actually works — the same data is reachable however you approach it.

### Rejected: two-level portfolio/project zoom

An earlier direction in this session proposed a two-level graph (portfolio graph of projects → zoom into a project graph of processes). This was superseded once launch-context inheritance from Centerline was established: since Pii Console always opens already-scoped to one project, a portfolio level inside Pii Console itself is unnecessary. Recorded here so the reasoning isn't lost if it resurfaces.

## Explicit non-scope: Institutional Learning

Institutional Learning (in the Contract → Operations → Institutional Learning stack from Exchange 005 of the exchange-development extraction) is **explicitly excluded** from the Pii Console graph and console. That is a DIF function, not a Pii function. No "lesson" or accumulated-knowledge node type should appear in this graph. This boundary was stated directly by the user and should not be re-derived or softened in later synthesis without an explicit decision to revisit it.

## Open questions

- **Single-source-of-truth data model.** What is the actual storage/reference architecture that makes "one data set, many lenses" real rather than aspirational — e.g. a single project data store keyed by field, with modules as read/write views into named fields, versus per-module stores with a sync layer? What triggers propagation on an approved change (write-through immediately, or a batched reconciliation step gated by the Extract/Absorb/Elevate pipeline)? This is now a hard integrity requirement (see correction above), not a UI preference, and needs its own design pass before implementation.
- What do Extract / Absorb / Elevate / Quarantine concretely *do* when clicked — is this a UI action that files a `_governed/` record, a navigation to a filing form, or something else? Not yet defined. Likely connects to the propagation question above: does "Elevate" gate when a change becomes visible to dependent modules?
- Is the graph populated from real UHG_Dashboard project data (configs under `05_Dashboard/dashboard_configs/`, contract/SOW records) now, or does a mockup ship first with live data wired in later?
- What is "module" precisely, relative to the existing `module_registry.py` / `MODULE_REGISTRY` concept in the Streamlit implementation plan (`.hermes/plans/2026-07-18_082258-...`)? Are Pii Console modules the same catalog, a superset, or a deliberately distinct concept scoped only to team-side process categories?
- What relationship/clustering metadata schema does each module need to carry to support arbitrary future views without redesign? (Note: this is now distinct from the data-dependency edges described above — clustering metadata is about visual arrangement, dependency edges are about actual data propagation.)
- Technical approach for the force-directed graph itself (D3.js, vis-network, or other) — not yet chosen; noted in-session that Obsidian's own graph view cannot be embedded (no public embed API) but a similarly-styled custom graph is buildable against real vault/project data.

## Standing of this record

This is synthesis, not decision. It should not be treated as settled system design. Promote specific claims here into a decision record only once the open questions above are resolved and a human explicitly ratifies the architecture (or the parts of it that are ready).

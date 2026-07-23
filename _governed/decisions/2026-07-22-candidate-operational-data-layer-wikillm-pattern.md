---
layer: decision
status: accepted
source:
  - session discussion, 2026-07-22, Pii UHG Dashboard project (Hermes session)
  - _governed/synthesis/concepts/pii-console-team-side-architecture.md
  - C:\Obsidian\My Projects\PI v1\AGENTS.md (WikiLLM Rules, Layer Model)
  - C:\Obsidian\My Projects\PI v1\_governed\synthesis\concepts\governed-wikillm.md
  - _governed/raw/2026-07-22-session-addendum-operational-layer-questions-resolved.md (Q2/Q3/Q4 + function-strip resolutions)
decided_by: Sean Johnson
decision_date: 2026-07-22
admissibility: supporting
verification:
  status: verified
  verified_by: Sean Johnson
  verified_on: 2026-07-22
  method: "Human review under open review window (.review-open), second window of 2026-07-22, after all design questions were resolved in-session (see raw addendum of this date)."
supersedes: null
---

# Candidate: A new operational data layer, distinct from synthesis, patterned on WikiLLM

## What this decision would do

Add a new layer to this project's `_governed/` structure — named **`ledger/`** (resolved 2026-07-22, see Q4 below) — that holds the **live, canonical, per-project operational data** that Pii Console's modules read and write (Budget figures, Schedule dates, Compensation terms, Consultant assignments, etc.). This layer would be:

- **Structured and interlinked like WikiLLM** — relationship-aware, cross-referenced, so Pii can trace which fields in which modules depend on which other fields (the data-dependency requirement established in the architecture synthesis above).
- **NOT part of `_governed/synthesis/`.** Synthesis stays exactly as constitutionally defined: non-authoritative, `admissibility: initiating` always, safe for interpretation/commentary/uncertainty. This new layer is explicitly not that — it needs to be able to reach a `supporting` admissibility state once approved, because modules operationally depend on its values being trustworthy, not merely "someone's synthesis of the truth."
- **Mutable-with-approval, not append-only.** Unlike `raw/` (append-only source evidence), this layer represents *current state* — a Budget figure that gets corrected is corrected, not merely appended-to. But every change must preserve lineage (supersession, per existing Authority Rule 6) so prior approved values are never silently lost.
- **The propagation mechanism for "one data set, many lenses."** Modules in Pii Console do not hold their own copies of data — they read/write against this layer. An approved change here is, by construction, visible to every dependent module immediately, because there is only one place the value lives.

## Relationship to WikiLLM as a pattern, not a single instance

This proposal reframes "WikiLLM" as a **reusable architectural pattern** (interlinked pages/records, relationship-aware, living document structure) that can be instantiated at more than one authority tier — not as a single folder that serves every purpose:

- `_governed/synthesis/` — WikiLLM pattern, **non-authoritative** tier (existing, unchanged)
- `_governed/operations/` (proposed) — WikiLLM pattern, **operational/authoritative-once-approved** tier (new)
- Per the user's broader framing in this session: each Pii project would have its own instance of this operational layer; each DIF spoke would have its own separate instance at the DIF side; Risk Management continues to mediate between Pii-side and DIF-side material exactly as already established (see PI v1's `risk-management-layer.md` synthesis) — this decision does not change that mediation role, only clarifies that "single source of truth" data storage is a distinct concern from synthesis.

## Why this needs to be a decision, not synthesis

Adding a new layer changes the `_governed/` layer model itself (per this project's `AGENTS.md` and the inherited PI v1 constitution). Per Authority Rule 5, decision records are authority-bearing and must not be created as if synthesis or model confidence were authority. This candidate is filed for human review — it is not yet acted on. No `_governed/operations/` directory has been created; no `AGENTS.md`/`index.md` layer model text has been changed to reflect it. Those changes should follow only if this decision is accepted.

## Open design questions (to resolve before/at acceptance, not decided here)

1. ~~**Field-level vs. record-level.**~~ **RESOLVED 2026-07-22 (in-session, pending formal ratification):** Field-level, every PAC/LCD-W field individually tracked with its own provenance and dependents list — no coarser grouping. The schema is not invented from scratch: **PAC** (Layer 0 startup/intake data) and **LCD-W** (expanded data model) are the real existing field structures this layer is built on. Full field-level was chosen explicitly because "Pii understands the relationships" requires exact tracking, not approximation.

   **Refinement (same session):** the LCD-W present in this repo is shaped by the UHG project's contractual requirements (B121 service orders, UHG DE/PM representative fields, Schedule E/F compensation routing, etc.) and must not be mistaken for Pii's generic schema. Other projects are already anticipated — Dunham School Dining Hall Expansion, Livingston Parish Sheriff's Office (LPSO) Work Release Renovations, Living Unified Community (LUC) — with different clients, different contract forms, and structurally different field needs. The field model is therefore three-tier:

   - **Pii-generic core** — fields every project carries regardless of client (name, scope, budget/COW, schedule milestones, consultants, compensation basis, ...). This is the generic LCD-W sense.
   - **Client/contract overlay** — contract-derived fields added/constrained per engagement (UHG's binding LCW/LCD is the first overlay; Dunham/LPSO/LUC would each get their own). Overlay fields are additive, explicitly marked as contract-derived, and never silently promoted into the generic core.
   - **Per-project instance data** — actual values, field-level tracked as resolved above.

   Field-level dependency tracking applies to whichever fields exist on a given project; *which* fields exist is core + overlay, not one fixed catalog. When work on UHG (or any engagement) reveals a useful field, it must be triaged — generic Pii pattern (candidate for promotion to core) vs. contract-specific (stays in that client's overlay) — consistent with the established client-overlay boundary rule in the parent PI environment.
2. ~~**Approval gate mechanics.**~~ **RESOLVED 2026-07-22 (in-session, pending formal ratification; source: raw addendum of this date):** Elevate is **not** the approval event. Elevate is a PM's direct proposal intake — it files a proposed improvement into `memory/pending/`. Approval is the separate human concurrence gate, now enacted as `decisions/2026-07-22-resident-context-concurrence-rule.md`. Proposal and approval are deliberately never the same action: collapsing them would fold the single-pen/human-gate structure into one click. A change becomes visible to dependent modules only on concurrence.
3. ~~**Format.**~~ **RESOLVED 2026-07-22 (in-session, pending formal ratification):** Hybrid — structured YAML frontmatter per field record (machine-resolvable dependency/provenance/state data, required for "Pii understands the relationships") with a markdown body carrying human-readable context and audit trail. Matches the rest of `_governed/` for git-diffability and human review while supporting programmatic dependency resolution.
4. ~~**Naming.**~~ **RESOLVED 2026-07-22 (in-session, pending formal ratification):** **`ledger/`** — accepted by the decider conditional on a clear definition and context, which is hereby recorded:

   **Definition:** The ledger is the project's **current operational truth with lineage** — the single place where live, canonical, per-project field values (budget figures, schedule dates, compensation terms, consultant assignments, PAC/LCD-W field instances) reside. Like an accounting ledger: entries are corrected by new lineaged entries, never by silent erasure (Authority Rule 6 supersession applies at field grain); the current balance is always readable; the history of every value is always reconstructible.

   **Context / disambiguation:** `ledger/` is deliberately NOT named "operations" — "Operations" in this project refers to the process-centric Contract→Operations→Institutional Learning stack (Exchange 005 of the Instance 1 extraction), a process taxonomy, not a data store. The ledger relates to the other layers as: `raw/` is what was received (append-only evidence); `synthesis/` is what we think it means (non-authoritative); `decisions/` is what was ruled (authority); **`ledger/` is what currently is** (mutable-with-approval operational state, approvable to `supporting` admissibility). In tiered-context terms (per the accepted control-system decision of this date), the ledger is the permanent home of the **state tier**.
5. **Admissibility lifecycle.** What specifically triggers a field moving from `unverified`/pending to `verified`/`supporting` — human sign-off equivalent to existing decision-record ratification, or a lighter per-field approval suited to high-frequency data entry (e.g. a PM approving a schedule date) that shouldn't require full decision-record ceremony for every field? Likely the same answer as #2 above.

## RESOLVED 2026-07-22: the function strip is Extract / Absorb / Elevate / Archive

Answered in-session by the decider (source: raw addendum of this date); pending formal ratification with the rest of this record.

- **Extract** — gleans information from pasted chats or artifacts as topics/major concepts *with context*. Governed mapping: produces preservation records (`raw/` → `extractions/`).
- **Absorb** — receives an artifact created **outside** the framework environment. Admission, not endorsement: the artifact lands in `raw/` with provenance disclosing external origin, then its data must be extracted and sorted/discussed (Extract + triage dialogue) before any of it reaches ledger or synthesis standing.
- **Elevate** — a PM's direct option to propose an improvement to the system. Files into `memory/pending/`; approval remains the separate concurrence gate (see resolved Q2).
- **Archive** — records dialogue as close to word-for-word as achievable, each exchange from both standpoints, human and AI. Governed mapping: append-only chat-archive records in `raw/` (first specimens: the 2026-07-22 chat archive and session addendum).

**Quarantine is struck.** The decider does not know what it is; it entered the earlier session's record without source backing — a synthesis-drift catch, preserved here deliberately as evidence that the record-vs-reality check works (the correspondence failure mode identified in the control-system decision of this date, caught at the gate before any audit function exists). If a quarantine-like hold state ("admitted but not yet trustworthy; withhold from propagation") is ever wanted, it is already expressible through admissibility/verification states and should be proposed on its own merits, not retained because a UI strip once used the word.

## Standing of this record

**ACCEPTED 2026-07-22** under an open human review window (the second window of this date), by Sean Johnson. All design questions were resolved prior to acceptance — see the resolution annotations above and the raw addendum they cite. Enactment actions taken with acceptance: `_governed/ledger/` created with `ledger/README.md` carrying the definition and disambiguation; `index.md` and project `AGENTS.md` layer models amended to include the ledger layer. The candidate-era text below is preserved unchanged as lineage.

**Status note (2026-07-22, post-docket, pre-acceptance):** All five numbered design questions and the function-strip question were resolved in-session (Q1 field-level three-tier schema; Q2 Elevate≠approval; Q3 hybrid format; Q4 `ledger/` with definition; Q5 folded into Q2's concurrence-gate answer — per-field approval IS the gate event, with formal decision-record ceremony reserved for schema/structure changes rather than routine field concurrence). Nothing blocked acceptance; ratified at the window recorded in this record's frontmatter.

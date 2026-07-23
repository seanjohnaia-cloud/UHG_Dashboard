---
layer: decision
status: candidate
source:
  - session discussion, 2026-07-22, Pii UHG Dashboard project (Hermes session)
  - _governed/synthesis/concepts/pii-console-team-side-architecture.md
  - C:\Obsidian\My Projects\PI v1\AGENTS.md (WikiLLM Rules, Layer Model)
  - C:\Obsidian\My Projects\PI v1\_governed\synthesis\concepts\governed-wikillm.md
decided_by: null
decision_date: null
admissibility: initiating
verification:
  status: unverified
  verified_by: null
  verified_on: null
  method: null
supersedes: null
---

# Candidate: A new operational data layer, distinct from synthesis, patterned on WikiLLM

## What this decision would do

Add a new layer to this project's `_governed/` structure — tentatively named `operations/` — that holds the **live, canonical, per-project operational data** that Pii Console's modules read and write (Budget figures, Schedule dates, Compensation terms, Consultant assignments, etc.). This layer would be:

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
2. **Approval gate mechanics.** Does "Elevate" (from the Extract/Absorb/Elevate/Quarantine function strip) correspond to the approval event that makes a change visible to dependent modules? Or is there a separate approval step distinct from that UI action? **Still open** — asked directly in-session (2026-07-22) and not yet answered; do not assume an answer. This blocks resolving what Extract/Absorb/Elevate/Quarantine concretely do (see below) and should be resolved together with it.
3. **Format.** Markdown-with-frontmatter (matching the rest of `_governed/`, human-readable, git-diffable) vs. structured data (JSON/YAML) optimized for programmatic dependency resolution — or a hybrid (structured data as the operational store, markdown as a human-readable rendering/audit trail of it).
4. **Naming.** `operations/` risks collision with the "Operations" term already used for the process-centric Contract→Operations→Institutional Learning stack (Exchange 005). Consider alternatives: `state/`, `ledger/`, `live/`, `working-data/` — something that reads clearly as "the mutable operational truth," distinct from the process-taxonomy sense of "Operations."
5. **Admissibility lifecycle.** What specifically triggers a field moving from `unverified`/pending to `verified`/`supporting` — human sign-off equivalent to existing decision-record ratification, or a lighter per-field approval suited to high-frequency data entry (e.g. a PM approving a schedule date) that shouldn't require full decision-record ceremony for every field? Likely the same answer as #2 above.

## Still open: what do Extract / Absorb / Elevate / Quarantine concretely do?

Asked directly in-session (2026-07-22); not yet answered. This is the other blocking question alongside #2 above — both concern what actually happens to a field's data at each step of that function strip (does clicking Elevate change a field's admissibility/visibility state? does Extract pull a value from `raw/`? does Quarantine hold a field's value back from propagation?). No behavior should be assumed or implemented for these four functions until this is answered.

## Standing of this record

Candidate. Not accepted, not acted on. Requires explicit human decision (`decided_by`, `decision_date`, `verification.status: verified`) before any implementation work creates the layer or before `AGENTS.md`/`index.md` are amended to reflect it.

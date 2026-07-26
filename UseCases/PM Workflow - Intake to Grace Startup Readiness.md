---
id: WORKFLOW-001
title: PM Workflow — Intake to Grace Startup Readiness
status: draft
layer: process_definition
source:
  - PI v1/_governed/synthesis/concepts/pac-project-start.md
  - PI v1/_governed/synthesis/concepts/grace-startup-a-f-requirements.md
  - This session's real UC-001 Muncie/Russiaville working method (2026-07-26)
  - "PM best practices" framework — source document not yet identified, see Stage 3
governed_by: none — draft process definition, not yet a ratified Pii schema
---

# PM Workflow — Intake to Grace Startup Readiness

> This is the human-facing workflow: what a PM actually does, in order, from first receiving a project through Grace startup readiness. It is the same shape as this session's real Muncie/Russiaville work, generalized. Draft — not yet a ratified Pii process.

## The five stages

```text
Stage 0 — Ingest initial project data
Stage 1 — Review against LCD-W, reconcile
Stage 2 — Produce base Statement of Understanding
Stage 3 — Apply PM best practices (lens, carried throughout — not a separate step)
Stage 4 — PAC / Grace Startup A–F readiness
```

Stage 3 is not sequential — it's a lens applied across Stages 0–4, per the source framework's own framing ("carried, every module, by one identity: the Accountable Owner").

---

## Stage 0 — Ingest initial project data

The PM brings data in through one of two paths (both first-class, neither a fallback for the other):

- **Upload as artifact** — a document is deposited: contract, matrix, PDD, email, floor plan.
- **Create through dialogue** — the PM talks through the project, and that dialogue is itself the source material.

Every ingested item gets **preserved with date of receipt** before anything else happens — this is provenance, not optional bookkeeping. See this session's pattern: `00_Source/.../original/` + `extracted/` + `provenance.md` (with sha256), for every real artifact brought in.

**Output of this stage:** one or more preserved source records, each dated and hashed, none yet interpreted.

## Stage 1 — Review against LCD-W, reconcile

Take the preserved source material and compare it field-by-field against the LCD-W's actual structure (`00_Source/Workflow/LCD Workbook/extracted/Life_Cycle_Data_Worksheet.md` — Project Identity, Classification/Fee Basis, Scope/Area, Schedule/SLA, Consultants, Service Order Output Requirements).

For each LCD-W field:

- Fill in what's known, with a **Stage** marker: `initial` (first raw value, unreconciled) → `developmental` (revised through negotiation, not yet accepted) → `final` (confirmed, ready to use).
- Highlight what's still missing — this becomes the literal content of the clarification response to the client (see this session's `design-experience-clarification-draft-2026-07-26.md` as the concrete example of that output).
- Where two sources conflict (e.g., Muncie's unreconciled square-footage figures), record it as a conflict, not a guess.

**Output of this stage:** an LCD field map per project (this session's `lcd-field-map-*.md` pattern), plus a clarification draft listing genuine gaps.

## Stage 2 — Produce base Statement of Understanding

Once enough of the LCD-W is populated to say something coherent, synthesize a **base Statement of Understanding** — a plain narrative of what's currently known, phrased so a human can sanity-check it at a glance. This is distinct from:

- the **client-facing** "current statement of understanding" (what `05_Dashboard`'s Overview page renders — polished, external-facing);
- the **field-level truth record** (the LCD field map — structured, internal, granular).

**Per Sean's direction (2026-07-26): the SoU is not a scratch artifact — it becomes the project record.** It has its own dedicated location, is revised in place rather than replaced, and carries a revision log (date, author, what changed) plus tracked metrics (count of fields at each Stage from Stage 1, count of open items, current fee/negotiation status). Location: `06_Statement of Understanding/<use-case>/<project>/SoU-<project>.md` — see `06_Statement of Understanding/UC-001 Incomplete Fee Proposal/Muncie/SoU-Muncie.md` and the parallel Russiaville file as the working examples.

The SoU is re-revised (new revision-log row, not a silent edit) whenever a Stage 1 field moves between Stages, or whenever new source material changes the picture — not on a schedule.

**Output of this stage:** a versioned narrative project record, distinct from both the client-facing dashboard summary and the raw field map, that the PM can point to as "the current understanding," with a visible history of how that understanding changed.

## Stage 3 — PM best practices (lens across all stages)

Source: Grace's own **PM Academy** curriculum — Module 1 "The Role of the Project Manager" and the Onsite #1 "Leadership Outcomes" / "PM Responsibilities" maps, preserved 2026-07-26 at `00_Source/PM Academy/`.

**Who the PM is:** the Accountable Owner — the one person answerable for the outcome, not just the tasks. Growing past three habits: the Coordinator (tracks tasks), the Designer (chases the drawing), the Pleaser (says yes to everything).

**Why the role exists:**

```text
VALUE = PERFORMANCE × EXPERIENCE
```

It multiplies, not adds. Performance = did we do the work well (technical quality, value for scope/fees, schedule adherence). Experience = what was it like to work with us (responsiveness, proactiveness, clear communication). Three roles overlap at the PM's position: PA owns the discipline answer ("makes it great"), PIC owns the client relationship and firm's risk, PM owns whether it all comes together ("you make it real").

**Three core behaviors, each triggered by a specific failure mode:**

| Trigger | Behavior | What it means | Concentration |
|---|---|---|---|
| People get out of sync | **Establish Clarity** | Define scope, fee, schedule & contract. Run the kickoff. Nothing advances on assumption. | Front of project |
| Work races ahead of decisions | **Control Advancement** | Manage coordination, budget & schedule. Surface variances early — not at the deadline. | Through the middle |
| Important things get sacrificed under pressure | **Protect Integrity** | Hold QA gates, price every change, protect quality and the fee. | Throughout |

**Five outcomes these compound into** (not additive):

1. Defined Scope & Aligned Commitments — scope, fee, schedule & contract settled before the team starts.
2. Controlled, Predictable Delivery — budgets, schedules & assignments actively managed; variances surfaced early.
3. Protected Design & Technical Integrity — code, coordination, BIM, constructability & QA guarded.
4. Sustained Financial Health — utilization & efficient execution protected.
5. Developed Teams & Collaborative Leadership — leads the workflow, leverages SMEs, delegates & grows others.

**The full operational checklist** behind these outcomes — every item a PM owns before a phase can close, by phase and by stream (Client Experience / Team Leadership / Business Management) — is preserved at `00_Source/PM Academy/Onsite 1 - PM Responsibilities Map/`. This is the concrete content behind Stages 0–4 of this workflow: e.g. its Pursuit & Contracting / Business Management items ("Fee estimate completed," "Proposal submitted," "Contract executed," "Go/No-Go completed & logged," "Project number opened") are the same ground this session's real Muncie/Russiaville work has been walking manually.

**Closing prompt, worth carrying into every stage above:** "Is there a decision my project depends on that nobody owns? That's your work."

## Stage 4 — PAC / Grace Startup A–F readiness

Once Stage 2's Statement of Understanding is stable, determine what Grace itself needs to actually start the project. This is PAC Layer 0 feeding six startup sections (per `grace-startup-a-f-requirements.md`):

| Section | Purpose |
|---|---|
| **A** — Activation / Project Number | Confirm the project may be activated; administrative identifiers/control conditions in place (includes the 14 Activation gates) |
| **B** — Team + Responsibility | PM, PIC, architecture/interiors team, consultants, owner contacts, responsibility boundaries |
| **C** — Financial Modeling | Transform proposal-level fee/budget into operating financial structure — fee breakdown by phase, production budget, staffing hours |
| **D** — Operational Alignment | Deliverables, milestones, schedule tracking, standards, coordination expectations |
| **E** — System Setup | Revit/BIM setup, cloud project setup, team/consultant access, folder structures |
| **F** — Programming / Predesign | Room lists, area requirements, site inputs, code/jurisdiction, unresolved assumptions |

PAC's rule applies throughout: **origin data captured once, never silently overwritten by downstream validation or transformation.** Section C's financial model doesn't rewrite PAC's origin fee data; it transforms it.

**Output of this stage:** PAC sufficiency confirmed or gaps named per section, ready for activation.

---

## Applied to Muncie / Russiaville right now

Both projects have completed Stage 0–2: LCD field maps exist and are actively reconciled (`lcd-field-map-muncie-2026-07-26-update.md`, `lcd-field-map-russiaville.md`), a clarification draft is ready to send, and both now have a Revision 1 Statement of Understanding on file (`06_Statement of Understanding/UC-001 Incomplete Fee Proposal/`). Stage 4 (PAC/A–F) hasn't started — Section A alone needs a Project Number, which is still an open gap in both field maps and both SoUs.

## Open questions

- Where does Stage 4 (PAC/A–F) actually get tracked for a real project — a new record type, or an extension of the existing field-map pattern?
- Does every SoU revision need its own dated file (matching this session's pattern for SO Matrix updates), or is in-place revision with a log table sufficient? Currently using in-place revision per Sean's direction; revisit if revision history gets long enough to make diffing hard.

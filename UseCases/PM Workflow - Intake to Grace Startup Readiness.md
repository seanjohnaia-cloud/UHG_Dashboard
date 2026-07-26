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

The base SoU is the PM-facing synthesis in between: "here is the project as we currently understand it, here's what's still open." It should read like `reconstructed_context()` in the dashboard code, but produced earlier, internally, and explicitly re-generated as Stage 1 fields move from `developmental` to `final`.

**Output of this stage:** a short narrative artifact the PM can use to align the team, or to sanity-check before advancing to Stage 4.

## Stage 3 — PM best practices (lens across all stages)

From the framework image provided 2026-07-26 — **source document not yet identified; the labels below are exactly what's visible, not elaborated beyond that.**

Three core behaviors:

- Establishing Clarity
- Controlling Advancement
- Protecting Integrity

Five target outcomes these compound into:

```text
Defined scope & aligned commitments
→ Controlled, predictable delivery
→ Protected design & technical integrity
→ Sustained financial health
→ Developed teams & leadership
```

Carried by one identity: **the Accountable Owner** (maps to PAC Section A's "PIC/PM or accountable owner").

**This stage needs a real source document before it can be more than labels.** Once identified, it should be preserved (`00_Source/`) and extracted the same way the Proposal Templates were, so this workflow can cite specifics rather than a summary image.

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

Both projects are currently mid-Stage-1/2: LCD field maps exist and are being actively reconciled (`lcd-field-map-muncie-2026-07-26-update.md`, `lcd-field-map-russiaville.md`), a clarification draft is ready to send, but the base Statement of Understanding hasn't been formally produced yet, and Stage 4 (PAC/A–F) hasn't started — Section A alone needs a Project Number, which is still an open gap in both field maps.

## Open questions

- What is the source document for Stage 3's framework? Needs identification and preservation before this stage can be more than four labels.
- Does the base Statement of Understanding (Stage 2) get its own file per project, or does it live inside the LCD field map as a rendered summary?
- Where does Stage 4 (PAC/A–F) actually get tracked for a real project — a new record type, or an extension of the existing field-map pattern?

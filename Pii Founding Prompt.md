# Pii — Founding Prompt

**Version 1.0 — Frozen.** This document is under source control. It is not edited during implementation. Improvements are submitted as amendment proposals per Layer 1 governance.

You are the development agent for **Pii (Project Intelligence)**, an operational platform for architectural practice. Your mandate is to build the operational layer only. The governing rules below are settled and are not yours to redesign.

## What Pii is

Pii helps architects operate projects where information is incomplete, fragmented, and arrives out of sequence. It does not force projects into an ideal workflow. It preserves reality and makes imperfect information operational: the system must always know what is known, what is assumed, what is missing, what conflicts, and on what basis work is proceeding.

Pii is evidence-centric. Contracts, emails, meeting notes, and drawings are not the record — they are **sources** that produce and support canonical records. Every assertion in a canonical record must trace back to its supporting evidence.

## The three layers (your mandate is Layer 2)

- **Layer 1 — Constitutional.** Defines how knowledge becomes trusted: extraction, provenance, validation, governance, canonization, improvement. This layer exists outside this codebase and governs it. You consume its rules; you never redefine them. If building Pii reveals a defect in Layer 1, write an **amendment proposal** — never amend directly.
- **Layer 2 — Operational (Pii).** What you are building: intake, requirements, PAC interview, proposal generation, dashboards.
- **Layer 3 — Implementation.** The tools: this repo, Obsidian vault (markdown + YAML frontmatter), Git, the dashboard.

## Development principles

1. **Operational emergence.** Do not introduce a new entity, register, workflow, or state unless an existing use case requires it. Architecture follows demonstrated need.
2. **Constitutional carve-out.** Records mandated by Layer 1 are exempt from principle 1 and must always be present: source preservation (verbatim source text), provenance, transition history, validation records, evidence references. These exist by governance, not by use-case demand. Never strip them as unnecessary.
3. **Define origin once.** Every piece of project information has one authoritative record. Sources reference it; nothing is duplicated or silently merged. Conflicting sources become conflict records, never merged records.
4. **Never invent missing information.** Inferences are recorded as assumptions, never as facts. Missing information becomes a gap record with reason, impact, owner, and resolution path — never an empty field, never a guessed value.
5. **Two state systems.** Requirement lifecycle: extracted → validated → activated → satisfied (exceptions: missing, conflict, superseded, not-applicable). Field truth states: provided, extracted, validated, assumed, missing, conflict, deferred, unknown, not-required. Lifecycle is derived from field truth states. AI-extracted values enter as `extracted` and become authoritative only after human validation. Every state transition is logged: from, to, date, actor, reason, evidence.

## Development Rule — Smallest Executable Slice

Always build the smallest complete use case that exercises the architecture end to end. Prefer one functioning workflow over multiple partially implemented abstractions. Every completed use case becomes both a regression test for future development and evidence that the architecture is grounded in reality.

## Use Cases Are First-Class Artifacts

Use cases live in `/UseCases` as permanent architectural artifacts (`UC-000 Accept Reality.md`, `UC-001 Incomplete Fee Proposal.md`, ...). Future development begins by implementing existing use cases before introducing new abstractions.

## Principle — Reality Is the Architect

Pii does not discover its architecture through speculation. Reality determines the architecture. Use cases reveal entities. Entities reveal workflows. Workflows reveal abstractions. Abstractions are accepted only after successful execution.

## Use Case 000 — Accept Reality (governs all use cases)

Pii faithfully represents the project as received, regardless of completeness, sequence, or quality. Success criteria: preserve every source; record every gap; record every assumption; record the basis for proceeding; never invent missing information; never force a project into an ideal workflow.

## Your first task — Use Case 001

**Prepare a fee proposal from an incomplete project request.**

Input: a real client email with partial scope, no completed service order.
Required outputs: proposal draft, assumption records, information-gap records, risk records, clarification requests, and a readiness assessment (workflow position and information readiness are recorded independently — both can be true at once: `requested_activity: prepare_fee_proposal`, `readiness_status: deficient`).

Build only what this use case requires. When it works end to end, stop and report: what entities reality forced into existence, what the founding assumptions got wrong, and what you propose next.

## Scope boundary

Pii owns procurement, contracting, project activation, and design. Centerline owns bidding, construction, closeout, and warranty. Pii hands a structured project record downstream; it does not replace execution systems.

# UHG Dashboard — Agent Instructions

## Purpose

This project is the Pii UHG Dashboard build: a client-facing dashboard/tooling engagement for UHG, and a proving ground for Pii project-intelligence patterns applied to a real client overlay.

Agents may help preserve, organize, synthesize, and propose project knowledge, but they do not create project authority by remembering, repeating, or summarizing information.

Core rule:

> Project Intelligence is the governed memory and authority layer through which humans and machines determine what project information may be trusted, for what purpose, and with what standing.

This project inherits its governance pattern from the production PI environment at `C:\Obsidian\My Projects\PI v1\`. It is a **separate Pii project instance**, not part of that environment: its `_governed/` layer is its own. Where this file and the PI v1 constitution differ, the PI v1 constitution is the reference pattern; project-specific rules below are additive.

## Layer Model

```text
_governed/
├── raw/                  # append-only source records (sessions, client comms, workflow facts)
├── extractions/          # preservation records from source material
│   └── exchange-development/  # candidate sub-type: reciprocal human/AI idea development (see index.md)
├── memory/
│   ├── pending/          # AI/user proposed durable memory awaiting review
│   ├── accepted/         # human-gated durable memory
│   └── superseded/       # retired memory with lineage
├── synthesis/            # WikiLLM living wiki; non-authoritative synthesis
├── decisions/            # authority-bearing design/process decision records
└── index.md              # governed layer map
```

Existing notes and code outside `_governed/` (dashboard modules, requirements docs, client communications folders) are working artifacts and source material. They may be cited as source evidence, but they are not automatically accepted memory or authority-bearing records.

## Authority Rules

1. **Raw source records are append-only.** Do not edit existing files in `_governed/raw/`. If a source was captured incorrectly, surface the issue for human correction.
2. **WikiLLM lives in `_governed/synthesis/`.** Synthesis may be revised, cross-linked, and maintained, but it does not bind authority.
3. **AI proposals go to `_governed/memory/pending/`.** Durable memory proposed by an agent must include provenance and uncertainty.
4. **Accepted memory requires human review.** Do not write directly to `_governed/memory/accepted/` unless a human-governed review workflow explicitly permits it.
5. **Decision records are authority-bearing.** Do not create or modify `_governed/decisions/` as if synthesis or model confidence were authority.
6. **Supersession must remain visible.** Do not delete superseded records; move or mark them with lineage.
7. **Model-native memory is working context, never project record.** Information stored, inferred, consolidated, or recalled by a model has no independent constitutional standing.
8. **Unverified material may initiate verification work but may not support another constitutional claim.** Avoid circular provenance.
9. **Extraction sub-types (e.g. Exchange Development Extraction) are preservation, not authority.** They may be cited as source evidence for later synthesis or decision records, but they do not themselves decide anything. A new extraction sub-type becomes a durable artifact class only once a decision record ratifies it.

## Required Frontmatter Patterns

Same patterns as PI v1 (`admissibility` / `verification` fields required on all non-raw records). See `C:\Obsidian\My Projects\PI v1\_governed\decisions\2026-07-19-admissibility-and-verification-as-explicit-pi-fields.md` for the canonical definitions.

## Agent Conduct

- Gather context before editing.
- Prefer preserving source material before synthesizing it.
- Do not silently promote working notes, summaries, or model memory into accepted memory.
- Do not collapse source, extraction, synthesis, memory, and decision layers.
- When uncertain whether something is authoritative, mark it as candidate/proposed and ask for review.
- Do not commit, push, or rewrite history unless the user explicitly asks.

## Maintenance Principle

The system should perform bookkeeping; humans exercise judgment at constitutional gates.

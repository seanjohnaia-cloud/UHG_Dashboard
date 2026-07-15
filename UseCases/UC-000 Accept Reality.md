---
id: UC-000
title: Accept Reality
status: frozen_governing_use_case
layer: operational
governs: all_use_cases
source: ../Pii Founding Prompt.md
---

# UC-000 Accept Reality

## Purpose

Pii faithfully represents the project as received, regardless of completeness, sequence, or quality.

This use case governs all later use cases.

## Success Criteria

Pii must:

- preserve every source;
- record every gap;
- record every assumption;
- record the basis for proceeding;
- never invent missing information;
- never force a project into an ideal workflow.

## Constitutional Carve-Out Records

The following records must exist when applicable because Layer 1 governance requires them, not because a later operational workflow first demanded them:

- source preservation / verbatim source text;
- provenance;
- transition history;
- validation records;
- evidence references.

## Implementation Boundary

This use case does not authorize broad architecture. It defines the required behavior that every executable slice must satisfy.

## Regression Role

Every future use case must be tested against UC-000. If a workflow succeeds by inventing, smoothing, silently merging, or forcing sequence, it fails UC-000.

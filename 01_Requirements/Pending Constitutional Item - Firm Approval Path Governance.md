---
record_type: pending_constitutional_layer_item
status: open
source_requirement: 01_Requirements/Activation Gate Conditions.md
related_gate: A-GATE-014
created_date: 2026-07-15
classification: dependency
---

# Pending Constitutional Item — Firm Approval-Path Governance

## Dependency

A-GATE-014 in the approved Activation Gate Conditions requires:

```text
Approval-path governance satisfied
```

The gate correctly routes this to the firm constitutional/process layer rather than treating it as project-origin PAC data.

However, the corresponding constitutional/process record does not yet exist in this Pii/UHG Dashboard structure.

## Why This Remains Open

The activation gate can reference inherited firm approval-path governance, but the system should not assume that governance is defined merely because the gate points to it.

Until the constitutional/process record exists, A-GATE-014 has an explicit dependency:

```text
Define the firm approval path that governs who may approve scope, fee, fee reductions, NTP acceptance, and project-start authorization.
```

## Status

```text
open_dependency
```

## Required Future Review

Create or identify the constitutional/process-layer artifact that defines:

1. who can approve project startup;
2. who can approve scope changes;
3. who can approve fee reductions;
4. who can approve proceeding under unresolved gate conditions;
5. how approval authority differs by project type, client, team, PIC, or contract path;
6. how Decision Records are reviewed and retained.

## Relationship to Activation Gate Conditions

A-GATE-014 remains valid and approved, but this dependency must stay visible until the constitutional/process layer is defined.

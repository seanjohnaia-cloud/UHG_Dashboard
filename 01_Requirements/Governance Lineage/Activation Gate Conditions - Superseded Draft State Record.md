---
record_type: superseded_state_record
status: preserved_lineage_summary
subject: Activation Gate Conditions
superseded_state: draft_for_review
current_state: approved
created_date: 2026-07-15
recovery_note: original draft file was renamed before commit; exact draft state is recoverable from session transcript/tool output, not from git history alone
---

# Activation Gate Conditions — Superseded Draft State Record

## Why This Record Exists

During governance promotion, the file:

```text
01_Requirements/Activation Gate Conditions - Draft for Review.md
```

was renamed/promoted to:

```text
01_Requirements/Activation Gate Conditions.md
```

A later provenance check noted that because the draft file had not yet been committed before the rename, git history alone does not preserve the original draft path/state.

This record preserves the superseded-state lineage so approval does not erase the fact that the artifact passed through a draft-for-review state.

## Recovery Path

| Recovery Source | Status |
|---|---|
| Git history | Not sufficient for pre-approval draft state because the draft was renamed before commit. |
| Hermes session transcript / tool output | Contains the draft creation and subsequent promotion patches. |
| This lineage record | Preserves the key draft-state metadata and transition facts inside the vault. |

## Superseded Draft State

The superseded draft state was characterized by:

```yaml
record_type: activation_gate_conditions
status: draft_for_review
implementation_status: not_implemented
developmental_structure_change: true
framework_b_signal_source: gate_overrides_are_live_project_risk_signals
```

The draft contained the same core Activation gate structure later approved:

- PAC boundary holds;
- Activation answers whether Grace is permitted, authorized, and organized to begin;
- all gates block by default;
- overrides require Decision Records;
- overrides feed Framework B as live-project risk/friction signals;
- A-GATE-013 is completeness evaluation, not readiness-flag generation;
- consultant/additional-service triggers are merged/routed;
- A-GATE-014 reroutes approval-path governance to constitutional/process layer.

## Promotion Event

The artifact was promoted on 2026-07-15 after governance review.

Promotion changed the artifact state from:

```text
draft_for_review
```

to:

```text
approved
```

and classified the artifact as:

```text
addition — new canonical artifact; no existing canon replaced or retired
```

Implementation remained:

```text
not_implemented
```

## Provenance Conclusion

The substantive lineage is intact. This record closes the small provenance gap created by renaming an uncommitted draft artifact before the approved version was committed.

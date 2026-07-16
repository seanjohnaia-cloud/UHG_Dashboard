---
record_type: dashboard_build_brief
status: approved_requirement_brief
implementation_status: not_implemented
source_requirement: 01_Requirements/Activation Gate Conditions.md
created_date: 2026-07-15
---

# Dashboard Build Brief — Activation Gate Behavior

## Primary Implementation Instruction

Build the override flow first, not last.

Rendering the fourteen gates is straightforward. The Decision Record capture at the moment of override is the mechanism that makes the dashboard honest.

If the implementation allows a blocked condition to be bypassed without capturing a Decision Record, the dashboard fails its governance purpose.

## Behavioral Spec

The dashboard must implement:

1. fourteen Activation gates;
2. blocking-by-default logic;
3. one override mechanism;
4. required Decision Record capture at override time;
5. four output states:
   - `startup_ready`
   - `startup_ready_with_recorded_risk`
   - `startup_blocked`
   - `startup_unassessed` / `incomplete`
6. explicit preservation that `startup_ready_with_recorded_risk` can never masquerade as clean green.

## Override Flow Requirement

When a user attempts to proceed past a blocked gate, the dashboard must require:

- accountable human;
- gate condition being overridden;
- rationale;
- accepted risk;
- mitigation/follow-up;
- date/time;
- source/evidence.

The resulting Decision Record must be available as a Framework B signal source.

## Implementation Warning

Do not treat overrides as UI exceptions or comments. Overrides are governed project intelligence.

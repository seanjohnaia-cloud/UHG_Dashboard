---
layer: decision
status: accepted
source:
  - "C:/Obsidian/My Projects/PI v1/_governed/decisions/2026-07-26-ratify-accountable-owner-operating-principles.md"
  - "C:/Obsidian/My Projects/PI v1/_governed/synthesis/concepts/pii-accountable-owner-operating-principles.md"
  - "C:/Obsidian/My Projects/PI v1/AGENTS.md#accountable-owner-operating-principles"
  - "UHG_Dashboard/00_Source/PM Academy/Module 1 - Role of the Project Manager/extracted/role-at-a-glance-text.md"
  - "UHG_Dashboard/00_Source/PM Academy/Onsite 1 - PM Responsibilities Map/extracted/pm-responsibilities-map-text.md"
  - "UHG_Dashboard/00_Source/PM Academy/Onsite 1 - Leadership Outcomes Map/extracted/leadership-outcomes-map-text.md"
decided_by: Sean Johnson
decision_date: 2026-07-26
admissibility: supporting
verification:
  status: verified
  verified_by: Sean Johnson
  verified_on: 2026-07-26
  method: "Human review window approval (.review-open present) in UHG_Dashboard; user instructed adoption of PI v1 principles into this Pii instance."
supersedes: null
---

# Decision: adopt Accountable Owner operating principles for this Pii instance

> Authored during an open human review window (`_governed/.review-open` present) and approved by Sean Johnson on 2026-07-26. Authority-bearing for the UHG_Dashboard Pii instance.

## Decision

UHG_Dashboard adopts, by reference and local enactment, the Accountable Owner Operating Principles ratified in the production PI v1 environment by `C:/Obsidian/My Projects/PI v1/_governed/decisions/2026-07-26-ratify-accountable-owner-operating-principles.md`.

The principles are binding for agents acting as a PM's extension in this UHG/Pii project instance:

1. **Establish Clarity.** Treat scope/fee/schedule/contract ambiguity as blocking advancement by default — the same posture as PAC's Activation gates, applied earlier, at first contact with ambiguity rather than only at formal Activation.
2. **Control Advancement.** Track field-Stage age (how long a field has sat at `developmental` or `missing`, per the `initial`/`developmental`/`final`/`missing` model), not just current Stage. Surface fields stuck in non-final states as variance signals before deadline pressure exposes them.
3. **Protect Integrity.** Any field that has reached `final` Stage requires an explicit change record if edited again, including what changed, why, and cost/schedule impact where applicable. Agents must never silently overwrite a `final`-Stage field.
4. **Accountable Owner.** Every gap record, risk record, and open item carries an accountable-owner field, not just the project as a whole. Agents should be able to surface, on request, every open item with no assigned owner.

## What this enacts

This decision adds the four principles to `UHG_Dashboard/AGENTS.md` under a new `Accountable Owner Operating Principles` section. That makes the behavior binding for agents operating in this project instance.

## Scope

This is an adoption decision for UHG_Dashboard as a Pii project instance. It does not modify PI v1, and it does not create a new generic Pii core decision beyond the already-ratified PI v1 source decision. Where this UHG instance and PI v1 differ, `AGENTS.md` remains clear that PI v1 is the reference pattern and UHG-specific rules are additive.

## Standing

`status: accepted`, `admissibility: supporting`. Authority-bearing for UHG_Dashboard per this project's established review-window mechanism.

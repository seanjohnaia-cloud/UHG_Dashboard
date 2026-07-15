---
status: working_extraction_not_canonical
source_id: SRC-CONTRACT-EXHIBIT-A
use_case: UC-001
purpose: initial_contract_constraints_for_incomplete_fee_proposal
---

# UC-001 Contract Requirement Seed — Exhibit A

> Working extraction only. These are not canonical requirement records yet. Each item must become a governed requirement record only when the UC-001 workflow needs it and evidence/validation are attached.

## Why this exists

UC-001 asks Pii to prepare a fee proposal from an incomplete project request. Exhibit A establishes contract constraints that the proposal workflow must respect before seeing a specific request.

## Evidence-Backed Candidate Constraints

### CR-001 — Service Order is project-specific authority container

- Evidence: `00_Source/Contract/Exhibit A - Scope of Work/extracted-text.md#L253-L259`
- Source text: “The Architect shall provide an individual Service Order for each project... The Service Order will indicate project-specific scope of services, compensation, and schedule for performing the services.”
- Working implication for Pii: proposal output must distinguish scope, compensation/fee, and schedule, even when deficient.
- State: `extracted`

### CR-002 — Purchase Order authorizes proceeding

- Evidence: `00_Source/Contract/Exhibit A - Scope of Work/extracted-text.md#L261-L263`
- Source text: “Receipt of a Purchase Order (PO)... will act as authorization to proceed with Design Services for a specific project.”
- Working implication for Pii: readiness to draft a proposal is independent from authorization to proceed.
- State: `extracted`

### CR-003 — Scope, fees, and schedules are coordinated with Owner / Designated Representative

- Evidence: `00_Source/Contract/Exhibit A - Scope of Work/extracted-text.md#L265-L267`
- Source text: “Scope, fees and schedules for individual work efforts shall be coordinated with the Owner or its Designated Representative.”
- Working implication for Pii: clarification requests must identify which missing facts affect scope, fee, and schedule coordination.
- State: `extracted`

### CR-004 — Proposal accuracy requires sufficient discussion of location and scope

- Evidence: `00_Source/Contract/Exhibit A - Scope of Work/extracted-text.md#L163-L169`
- Source text: “Ensure that sufficient discussions of the project location and scope have been completed to ensure proposal accuracy...”
- Working implication for Pii: insufficient location/scope information becomes gap/risk records, not guessed values.
- State: `extracted`

### CR-005 — Proposal preparation is a standard administrative function, not separately charged

- Evidence: `00_Source/Contract/Exhibit A - Scope of Work/extracted-text.md#L107-L115`
- Source text: “The Architect shall not charge additional fees for standard administrative functions, including... Proposal Preparations.”
- Working implication for Pii: the proposal workflow should not treat its own preparation as a fee item unless a separate, explicit written basis exists.
- State: `extracted`

### CR-006 — Deliverables may be requested out of sequence

- Evidence: `00_Source/Contract/Exhibit A - Scope of Work/extracted-text.md#L337-L339`
- Source text: “The Architect shall provide deliverables even when requested out of sequence.”
- Working implication for Pii: workflow position and information readiness must be tracked independently.
- State: `extracted`

### CR-007 — Changes require written approval before proceeding

- Evidence: `00_Source/Contract/Exhibit A - Scope of Work/extracted-text.md#L977-L979`
- Source text: “The Architect must obtain written approval... for any changes to the scope, schedule or budget... before proceeding...”
- Working implication for Pii: assumptions may support proposal drafting but cannot authorize changed scope/schedule/budget.
- State: `extracted`

## First Slice Consequence

The first executable Pii slice should not try to model the whole contract. It should take one incomplete project request and produce:

1. preserved source record
2. extracted facts as `extracted`
3. assumptions as assumptions
4. gaps with reason/impact/owner/resolution path
5. risks caused by proceeding under deficiency
6. clarification requests
7. proposal draft with evidence references
8. readiness assessment:
   - `requested_activity: prepare_fee_proposal`
   - `workflow_position: proposal_requested`
   - `readiness_status: deficient`

## Open Dependency

Need the real incomplete client email / project request before creating the first executable UC-001 project record.

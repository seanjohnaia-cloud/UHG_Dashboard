---
layer: synthesis
status: draft
source:
  - ".hermes/desktop-attachments/DIF_Hermes_Full_Architecture_Chain.md (user-provided attached context, 2026-07-26)"
  - ".hermes/desktop-attachments/DIF_Hermes_Slice1_Handoff_1.md (user-provided attached context, 2026-07-26)"
  - ".hermes/desktop-attachments/DIF Architecture.txt (GPT summary provided by user, 2026-07-26)"
  - "Hermes review in current session, 2026-07-26"
confidence: high
updated: 2026-07-26
admissibility: initiating
verification:
  status: unverified
  verified_by: null
  verified_on: null
  method: null
---

# Build Architecture Analysis — Project Intelligence Implementation Architecture, Volume I

Non-authoritative synthesis/specification. This document merges the full DIF/Hermes/Pii architecture chain, the Slice 1 implementation handoff, the GPT-proposed architecture-document outline, and Hermes review comments into a builder-facing analysis. It is **not** a raw transcript, not an extraction record, and not an authority-bearing decision. It should become `v1.0` or be treated as canonized only if a human-governed review process later accepts it through an appropriate decision record.

## 1. Purpose

This document records the implementation architecture that emerged from the July 26, 2026 DIF / Hermes / Pii design chain. Its purpose is to convert the discovered constitutional architecture into a build-ready Slice 1 analysis without collapsing preservation, synthesis, and authority.

The immediate build question is:

> How should Hermes process an incomplete client request into governed Slice 1 operational records without turning unknowns into facts?

The intended answer is a small executable slice:

```text
Client request
      ↓
Source record
      ↓
Initial Conditions baseline
      ├── Known facts
      ├── Assumption records
      ├── Constraint records
      └── Clarification records
              ↓
Proposal preparation support
              ↓
Selective Knowledge Candidate creation, only when reusable learning emerges
```

## 2. Standing and governance status

This document should be read as **candidate implementation synthesis**. It may guide schema design and engineering discussion, but it does not itself create authority.

Recommended standing language:

```text
Status: Candidate Architecture Specification
Standing: Non-authoritative synthesis pending human review
Version: v0.9 candidate
```

Do **not** label the architecture `Canonized` or `v1.0` merely because it is well-formed. In the Pii/DIF governance model, authority requires a human/delegated review act captured through the governed decision layer.

### Corrected Hermes authority language

The GPT summary proposed: "Hermes is the only authority permitted to admit information into the DIF." That wording is constitutionally too strong.

Use this instead:

> **Hermes is the controlled admission and publication mechanism. Human-governed review supplies authority. The DIF records the authoritative result.**

Hermes may be the only service/process permitted to execute admission mechanics, but Hermes does not create authority by itself.

## 3. Source chain and artifact separation

The architecture should be preserved through distinct artifact classes:

| Artifact | Purpose | Standing |
|---|---|---|
| Chat Exchange Archive | Preserves the actual exchange/source history | Raw / append-only source if filed |
| Chat Extraction / Architecture Chain | Preserves reasoning, moves, unresolved questions, and decision candidates | Extraction / preservation, not authority |
| Build Architecture Analysis | Converts the chain into a builder-facing synthesis/spec | Non-authoritative synthesis unless accepted by decision |
| Decision Record | Accepts, narrows, rejects, or supersedes architecture claims | Authority-bearing |

The GPT summary is correct that the useful build artifact should not read like a chat transcript. Its mistake is treating an architecture document's clean form as enough to make it canonized.

## 4. Core invariants

These invariants should be treated as Slice 1 design constraints:

1. **Raw capture is not knowledge.** Capture preserves material without admitting it as institutional truth.
2. **Workspace is retrieval scope, not canonical project record.** AnythingLLM-style workspace membership does not prove approval, verification, or authority.
3. **The vector database is not the DIF.** It is a rebuildable retrieval projection of selected governed content.
4. **Canonized does not equal published.** A record may be authoritative while withheld from a retrieval environment because of confidentiality, privilege, access restrictions, review timing, or scope.
5. **Operational visibility and analytical visibility are separate.** Project-scoped operational approval does not grant cross-project comparison rights.
6. **Hermes executes governed admission; it does not create authority.** Hermes proposes, structures, validates, publishes approved copies, and preserves lineage.
7. **Unknowns remain visible as unknowns.** Missing or uncertain project-start facts become assumptions or clarifications, not synthetic facts.
8. **Relationships are governed records.** Relationship status and verification matter; a linked source does not automatically resolve, validate, or confirm a record.
9. **Retrieval comes after governance.** Slice 1 should prove operational truth handling before vector publication or AnythingLLM integration.

## 5. Architectural decisions carried forward as candidate build assumptions

These are stable enough to guide implementation, but still need formal acceptance if they are to bind future work as architecture.

### 5.1 DIF / retrieval separation

The authoritative environment and retrieval environment are distinct:

```text
Capture Store
      ↓
Governance Registry / DIF
      ↓
Canonical governed records
      ↓
Retrieval publication service
      ↓
Vector / keyword / SQL indexes
      ↓
AnythingLLM or equivalent retrieval UI
```

The retrieval store should be disposable: it must be possible to delete and rebuild it from the canonical DIF without losing institutional knowledge.

### 5.2 Governance envelope plus typed evidence

The system should use one constitutional lifecycle with multiple evidentiary schemas:

- shared envelope for provenance, review state, confidentiality, publication state, and authority;
- typed detail tables for assumptions, constraints, clarifications, issues, decisions, risks, actions, changes, gates, and Framework A findings.

Implementation principle:

> **Normalize governance metadata. Preserve domain-specific evidence.**

### 5.3 Slice activation through use cases

The full vocabulary may be architecturally recognized before it is physically implemented. A record type earns implementation only when:

1. a real use case produces it;
2. it cannot be represented honestly by an existing type;
3. its fields support an actual decision or workflow;
4. someone is responsible for maintaining it;
5. its lifecycle and relationships are understood.

This prevents the database from becoming a speculative ontology rather than a working governed system.

## 6. Framework B count correction

Use the following language to avoid ambiguity:

> **Framework B has nine typed operational record types, supported by two baseline/source structures.**

Supporting structures:

1. Sources
2. Initial Conditions

Nine typed operational record types:

1. Assumptions
2. Constraints
3. Clarifications
4. Issues
5. Decisions
6. Risks
7. Actions
8. Changes
9. Review Gates

Therefore the count is:

- **9 typed operational record types**
- **11 total Framework B operational structures if Sources and Initial Conditions are included**

Roadmap / Intended Process and Project Log remain operational-only baseline/source structures unless a future use case proves they require structured implementation.

## 7. Slice 1 scope

Slice 1 should implement only the records needed to accept incomplete project-start reality:

- Sources
- Initial Conditions
- Assumptions
- Constraints
- Clarifications
- Relationship Registry
- Relationship Endpoint Rules
- Record Relationships
- Minimal Knowledge Candidates
- Candidate Source Snapshots
- Record Events / Audit Log

### Explicitly deferred from Slice 1

Do not implement yet:

- Issues
- Decisions
- Risks
- Actions
- Changes
- Review Gates
- Framework A cross-project projections
- Canonical object hierarchy
- Retrieval publications
- Vector chunks / embedding profiles
- AnythingLLM integration

These are specified concepts, not Slice 1 tables, until activated by a real use case.

## 8. Slice 1 table set — recommended physical build list

### 8.1 `projects`

Minimal project identity table, if not already provided elsewhere.

```text
projects
--------
project_id, project_code, project_name, project_status, created_at, updated_at
```

### 8.2 `sources`

Preserves the actual received request, artifact, communication, or exchange.

```text
sources
-------
source_id, project_id, source_type, title, source_location, source_version,
source_checksum, received_at, received_from, captured_by, confidentiality_class,
access_policy, created_at, updated_at
```

### 8.3 `initial_conditions`

Baseline metadata and generated project-start summary. Assumptions and constraints should not live here as authoritative long text; they should render from structured records.

```text
initial_conditions
------------------
initial_conditions_id, project_id, baseline_title, baseline_status, effective_at,
request_summary, known_scope, known_deliverables, known_schedule, known_budget,
known_participants, information_completeness, confidence_summary, prepared_by,
reviewed_by, version, supersedes_id, rendered_from_version, rendered_at,
render_status, created_at, updated_at
```

Implementation note: consider splitting rendered prose into an `initial_condition_renders` table if manual editing of generated summary fields becomes a contamination risk.

### 8.4 `framework_b_assumptions`

```text
framework_b_assumptions
-----------------------
assumption_id, project_id, assumption_title, assumption_statement, assumption_status,
basis, reason_required, confidence_level, identified_at, identified_by, owner,
validation_method, validation_due_at, validated_at, validated_by, validation_result,
effect_if_false, created_at, updated_at
```

Suggested statuses:

```text
PROPOSED, ACTIVE, VALIDATED, DISPROVED, OVERDUE_FOR_REVIEW, SUPERSEDED, EXPIRED
```

Governance rule: assumptions require review dates by default, but do not silently expire unless an explicit expiration condition/date exists.

### 8.5 `framework_b_constraints`

```text
framework_b_constraints
-----------------------
constraint_id, project_id, constraint_title, constraint_statement, constraint_type,
constraint_status, source_authority, effective_at, scope_effect, schedule_effect,
budget_effect, quality_effect, confirmed_at, confirmed_by, created_at, updated_at
```

Suggested statuses:

```text
CONFIRMED, PROVISIONAL, DISPUTED, REMOVED, SUPERSEDED
```

Governance rule: constraints require source authority. Temporary or provisional constraints may need review dates case-by-case, but not universally.

### 8.6 `framework_b_clarifications`

```text
framework_b_clarifications
--------------------------
clarification_id, project_id, clarification_title, question, context,
clarification_status, raised_at, raised_by, directed_to, blocking, priority,
response_required_by, response, response_authority, responded_at,
ambiguity_category, recurrence_count, created_at, updated_at
```

Suggested statuses:

```text
OPEN, ASSIGNED, UNDER_REVIEW, ANSWERED, CONFIRMED, SUPERSEDED, CLOSED
```

Governance rule: raising a clarification does not require source verification. Verification belongs on the response/resolution relationship.

### 8.7 `knowledge_candidates`

Minimal Slice 1 candidate layer. Candidate creation is selective, not automatic.

```text
knowledge_candidates
--------------------
candidate_id, project_id, record_family, record_type, source_record_type,
source_record_id, source_record_version, candidate_title, candidate_statement,
governance_status, proposed_by, proposed_at, confidentiality_class,
publication_eligible, reviewed_by, reviewed_at, review_notes, created_at, updated_at
```

Important: this table should not become the operational record store. It records proposed knowledge candidates derived from operational evidence.

### 8.8 `candidate_source_snapshots`

Required to preserve exactly what Hermes evaluated when a candidate was created.

```text
candidate_source_snapshots
--------------------------
snapshot_id, candidate_id, source_record_type, source_record_id,
source_record_version, snapshot_json, snapshot_checksum, captured_at
```

Rationale: if the source operational record changes later, the evidence underlying the candidate review must remain reconstructible. This is the database form of "no silent overwrite."

### 8.9 `record_events`

Governed systems need event history from Slice 1, not just `updated_at`.

```text
record_events
-------------
event_id, record_type, record_id, event_type, event_at, event_by,
previous_status, new_status, reason, source_id, metadata_json
```

Example event types:

```text
SOURCE_CAPTURED
INITIAL_CONDITIONS_RENDERED
ASSUMPTION_CREATED
ASSUMPTION_STATUS_CHANGED
CONSTRAINT_CREATED
CONSTRAINT_CONFIRMED
CLARIFICATION_RAISED
RELATIONSHIP_PROPOSED
RELATIONSHIP_ACTIVATED
RELATIONSHIP_VERIFIED
CANDIDATE_CREATED
REVIEW_REQUESTED
REVIEW_COMPLETED
```

## 9. Relationship model

Relationships should be first-class governed records, not scattered `related_*_id` columns.

### 9.1 Registry and canonical edge storage

The registry defines relationship vocabulary and inverse behavior. `record_relationships` stores only one canonical edge per fact. Inverse relationships are generated for display/query traversal, not duplicated as stored facts.

Add an explicit storage-direction field to avoid double-facts:

```text
relationship_type_registry
--------------------------
relationship_type_code, display_name, inverse_relationship_type,
canonical_storage_direction, requires_verification, description,
is_active, schema_version, default_cardinality_note
```

Avoid storing both:

```text
SOURCE 001 SUPPORTS ASSUMPTION 004
ASSUMPTION 004 SUPPORTED_BY SOURCE 001
```

Those are the same semantic fact.

### 9.2 Endpoint-specific cardinality

`relationship_endpoint_rules` should be the enforced source of truth for cardinality. A single cardinality field on the relationship type is too coarse.

```text
relationship_endpoint_rules
---------------------------
rule_id, relationship_type_code, from_record_type, to_record_type,
from_cardinality, to_cardinality, requires_verification_override,
allowed_statuses, is_primary_authority_allowed, schema_version, is_active
```

Recommendation: remove `cardinality_rule` from `relationship_type_registry` or retain it only as a non-enforced human-readable default note.

### 9.3 Record relationships

```text
record_relationships
--------------------
relationship_id, from_record_type, from_record_id, relationship_type,
to_record_type, to_record_id, relationship_status, created_at, created_by,
valid_from, valid_to, notes, metadata_json
```

Recommendation: omit `is_bidirectional` from individual relationship records. Bidirectional/inverse behavior belongs in the registry, not per-edge, to avoid semantic drift.

### 9.4 Relationship statuses

Resolve the open question by adding `ACTIVE`:

```text
PROPOSED
ACTIVE
VERIFIED
REJECTED
SUPERSEDED
REVOKED
```

Rules:

- If `requires_verification = false`, a new relationship may default to `ACTIVE`.
- If `requires_verification = true`, a new relationship defaults to `PROPOSED`.
- Only `ACTIVE` or `VERIFIED` relationships should produce operative downstream effects.
- Only `VERIFIED` relationships should trigger lifecycle transitions that require verification.

Examples:

```text
SOURCE DERIVED_FROM relationship, requires_verification=false → ACTIVE
SOURCE RESOLVES CLARIFICATION, requires_verification=true → PROPOSED until verified
SOURCE VALIDATES ASSUMPTION, requires_verification=true → PROPOSED until verified
```

### 9.5 Slice 1 relationship vocabulary

Scope the registry down to Slice 1 only. Relationship concepts should earn inclusion the same way record types do.

Include:

- DERIVED_FROM / SOURCE_OF
- SUPPORTED_BY / SUPPORTS
- CONTRADICTED_BY / CONTRADICTS
- CLARIFIES / CLARIFIED_BY
- RESOLVED_BY / RESOLVES
- VALIDATES / VALIDATED_BY
- INVALIDATES / INVALIDATED_BY
- ESTABLISHED_BY / ESTABLISHES
- SUPERSEDES / SUPERSEDED_BY
- CREATES / CREATED_BY

Explicitly exclude until later slices:

- MITIGATES
- MATERIALIZED_AS
- DEPENDS_ON
- BLOCKS
- REQUIRES
- IMPLEMENTS
- AFFECTS

## 10. Hermes processing pipeline — Slice 1

The Slice 1 Hermes pipeline should be limited and testable:

```text
1. Source intake
   - preserve received artifact/request/exchange
   - compute checksum/version
   - classify confidentiality/access policy

2. Source validation
   - verify source identity/location/checksum
   - record capture event

3. Initial Conditions generation
   - identify known facts
   - generate baseline summary/render
   - record incompleteness and confidence summary

4. Assumption extraction
   - identify claims required for work to proceed but not yet verified
   - create individually trackable assumption records

5. Constraint extraction
   - identify externally imposed limits or requirements
   - attach source authority and effects

6. Clarification extraction
   - identify questions/ambiguities requiring response or interpretation
   - preserve unresolved ambiguity without forcing closure

7. Relationship proposal/activation
   - create source/record relationships
   - default status based on verification requirement
   - prevent unsupported lifecycle transitions

8. Knowledge Candidate creation
   - only when reusable learning emerges
   - preserve source snapshot
   - do not auto-promote operational records into institutional knowledge

9. Audit/event logging
   - record status changes, relationship events, candidate creation, and review actions
```

## 11. Validation rules for implementation

The first implementation should enforce these rules before adding retrieval:

1. No assumed fact may appear in the baseline as fact without a corresponding assumption record.
2. No constraint may become `CONFIRMED` without source authority.
3. No clarification may become `ANSWERED` or `CONFIRMED` solely because a source is linked; the resolution relationship must be operative and verified when required.
4. No knowledge candidate may be created without a source record reference and source snapshot.
5. No relationship requiring verification may trigger lifecycle changes while still `PROPOSED`.
6. No vector publication or AnythingLLM ingestion occurs in Slice 1.
7. No cross-project analytical projection occurs in Slice 1.
8. No deferred record type may appear as an implemented table until activated by a real use case.
9. Initial Conditions prose must be reproducible from structured records or explicitly marked as a rendered summary.
10. Every status transition should emit a `record_events` row.

## 12. Deferred roadmap

Recommended implementation sequence:

1. **Slice 1 — Accept Reality**
   - Sources, Initial Conditions, Assumptions, Constraints, Clarifications, Relationships, minimal Knowledge Candidates.
   - Prove that Hermes does not manufacture completeness.

2. **Slice 2 — Govern Decisions**
   - Add Decisions and Actions.
   - Prove authority, rationale, ownership, and verification of completion.

3. **Slice 3 — Manage Project Instability**
   - Add Risks, Issues, and Changes.
   - Prove risk materialization, issue/change linkage, and preserved history.

4. **Slice 4 — Control Phase Progression**
   - Add Gates, Exceptions, Approval relationships.
   - Prove evidence-based progression and visible exceptions.

5. **Slice 5 — Publish Governed Intelligence**
   - Add canonical objects, publication eligibility, retrieval projections, vector publication, AnythingLLM integration.
   - Prove retrieval is a governed projection, not a source of truth.

## 13. Resolved build clarifications

These are the recommended resolutions to the open questions carried in the architecture chain.

### 13.1 Cardinality source of truth

`relationship_endpoint_rules` is authoritative for enforcement. `relationship_type_registry` should not enforce universal cardinality.

### 13.2 Default relationship status

```text
requires_verification = true  → default relationship_status = PROPOSED
requires_verification = false → default relationship_status = ACTIVE
```

### 13.3 Slice 1 relationship registry scope

The registry should include only Slice 1 relationship types. Deferred verbs should be absent, not merely inactive, so Hermes cannot reach for undefined concepts.

### 13.4 Framework B count

Use: "nine typed operational record types + two supporting structures = eleven total Framework B operational structures."

### 13.5 Source snapshots

Candidate source snapshots are required in Slice 1.

### 13.6 Event log

A record/audit event table is required in Slice 1.

### 13.7 Initial Conditions prose

Initial Conditions readable text is a rendered baseline view, not the granular source of truth.

## 14. Highest-risk implementation traps

### 14.1 Building retrieval too early

AnythingLLM/vector integration should not be part of Slice 1. If retrieval arrives before governance behavior is proven, the system may recreate the contamination problem it is designed to prevent.

### 14.2 Letting Hermes become authority

Hermes should structure, propose, validate, log, and publish approved copies. It should not be described or implemented as the source of approval authority.

### 14.3 Overbuilding Framework B

Issues, Decisions, Risks, Actions, Changes, and Review Gates are important, but building them before a use case requires them undermines the emergence principle.

### 14.4 Treating links as lifecycle transitions

A relationship record can exist before it is operative. Example:

```text
Clarification OPEN
Source linked via RESOLVED_BY relationship
Relationship status PROPOSED
No lifecycle transition yet

Authorized verifier confirms the relationship
Relationship status VERIFIED
Clarification may transition to ANSWERED or CONFIRMED
```

### 14.5 Duplicating inverse edges

Store one canonical edge and generate inverse views. Do not store the same semantic fact twice.

## 15. Recommended builder handoff statement

A concise handoff to an engineer should say:

> Build Slice 1 of the Project Intelligence implementation architecture. The system must preserve an incomplete client request as a Source, generate Initial Conditions as a reproducible baseline view, extract Assumptions, Constraints, and Clarifications as individually governed operational records, create first-class relationships with endpoint-specific validation and status semantics, log all status changes/events, and create Knowledge Candidates only selectively with source snapshots. Do not implement vector publication, AnythingLLM ingestion, cross-project projections, or deferred Framework B record types in this slice.

## 16. Milestone statement

This architecture chain marks the transition of Project Intelligence from constitutional discovery into implementation engineering. Future work should prioritize implementation, validation, and incremental activation rather than introducing new core concepts.

The first proof is deliberately narrow:

> Given an incomplete client request, can Hermes preserve what was received, distinguish facts from assumptions, constraints, and clarifications, maintain relationship standing, and avoid turning uncertainty into institutional truth?

If Slice 1 proves that, the foundation is sound enough to activate later slices.

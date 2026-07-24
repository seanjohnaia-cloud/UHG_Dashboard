---
layer: memory
status: superseded
proposal_type: extraction_schema_candidate
target_layer: decisions
source:
  - "pii_team_dashboard/server/governed_writer.py (write_extraction(), running code since 2026-07-24 / Checkpoint 2)"
  - "pii_team_dashboard/open-questions.md (item 1, flagged 2026-07-24)"
  - "_governed/decisions/2026-07-22-ratify-exchange-development-extraction.md (sibling precedent; deliberately not reused, see Claim)"
  - "_governed/decisions/2026-07-22-candidate-operational-data-layer-wikillm-pattern.md (RESOLVED 2026-07-22 function-strip mapping: Extract -> raw/ -> extractions/)"
derived_by: "claude-code (Checkpoint 3 follow-up, at explicit user direction)"
confidence: medium
uncertainty: "Whether `extraction_type: general` is the right name, whether `status` needs values beyond `draft`, and whether a single extraction should be allowed to cite more than one raw source are all open -- see Open sub-questions below. The schema has been exercised by isolated tests and one live HTTP round trip (Checkpoint 2 verification, since deleted) but not yet by any real captured content."
admissibility: initiating
verification:
  status: unverified
  verified_by: null
  verified_on: null
  method: null
supersedes: null
superseded_by: "_governed/decisions/2026-07-24-ratify-generic-extraction-schema.md"
superseded_on: 2026-07-24
superseded_reason: "Promoted to accepted decision via _governed/decisions/2026-07-24-ratify-generic-extraction-schema.md under open review window; all three open sub-questions resolved by the decider."
review_after: 2026-08-24
---

# Proposed: frontmatter schema for generic (non-exchange-development) extraction records

## Claim

Ratify a minimal frontmatter schema for extraction records produced by the plain
Extract action — gleaning topics/major concepts *with context* from pasted material
or an already-captured raw record — as its own extraction sub-type, distinct from
and lighter-weight than the ratified Exchange Development Extraction sub-type.

```yaml
---
layer: extraction
extraction_type: general
status: draft
source:
  - <raw/ path this was extracted from>
captured_by: <agent or human>
captured_at: YYYY-MM-DD
admissibility: initiating
verification:
  status: unverified
  verified_by: null
  verified_on: null
  method: null
---
```

Body: a title, `Extracted from: \`<raw_ref>\``, an optional `## Topics / concepts`
list, an optional `## Context` section, and a fixed preservation-only disclaimer
("citable as source evidence for later synthesis or decision records; does not itself
decide anything").

This is already the schema `server/governed_writer.py::write_extraction()` has been
producing since Checkpoint 2 (2026-07-24) — it was written in code before being filed
here, flagged the same day as an unratified inference in `open-questions.md` item 1.
This proposal is that ratification step, not new design.

## Why a separate, lighter schema — not the exchange-development shape

Exchange Development Extraction (`decisions/2026-07-22-ratify-exchange-development-extraction.md`)
captures reciprocal architectural development between human and AI: a numbered
Initiation/Interpretation/Response/Emergent Insight/Architectural Consequence
structure, plus Design Lineage and Unresolved Questions sections. It exists for a
narrow, specific situation — sessions where ideas were materially shaped by both
parties in alternation.

Plain Extract, per its ratified governed mapping (`decisions/2026-07-22-candidate-operational-data-layer-wikillm-pattern.md`,
"RESOLVED 2026-07-22: the function strip"), is a much lighter, general-purpose action:
glean topics/concepts with context from pasted chat or an artifact. Routing every plain
extraction through the 5-part Exchange structure would misrepresent single-directional
or routine captures as reciprocal architectural development, and would make Extract too
heavyweight for a button meant to be pressed often. These should remain two distinct
extraction sub-types under `extractions/`, not one schema stretched to cover both.

## Relationship to Authority Rule 9

Authority Rule 9: "Extraction sub-types (e.g. Exchange Development Extraction) are
preservation, not authority... A new extraction sub-type becomes a durable artifact
class only once a decision record ratifies it." This proposal is that ratifying step
for the `general` sub-type, paralleling the exchange-development ratification.

## Open sub-questions for reviewer

1. Is `extraction_type: general` the right name, or something more descriptive (e.g.
   `topic-glean`, `plain`)?
2. Should `status` carry values beyond `draft` (e.g. `draft | reviewed | superseded`),
   or does that belong to a later governance-review workflow rather than this schema?
3. Should `source` support more than one raw record per extraction (e.g. drawn from
   several pasted fragments in one session)? Current code supports exactly one
   `raw_ref` per Extract call.

## Not enacted

This proposal binds nothing until a human authors an accepted decision record. Until
then, `server/governed_writer.py` continues operating on this schema as a
documented-but-unratified inference (`open-questions.md` item 1), and agents should
not extend or rely on this schema being final.

## Origin

Flagged in code comments and `open-questions.md` at Checkpoint 2 (2026-07-24). Filed
here at explicit user direction as a Checkpoint 3 follow-up (2026-07-24), after the
user declined to let it sit unratified while more gets built on top of it. No
`_governed/.review-open` window is currently open (checked before filing); this
proposal awaits one.

---
layer: decision
status: accepted
source:
  - "_governed/memory/pending/2026-07-24-generic-extraction-frontmatter-schema.md (promoted; superseded lineage at memory/superseded/)"
  - "pii_team_dashboard/server/governed_writer.py (write_extraction()/extract(), code updated to match this decision)"
  - "_governed/decisions/2026-07-22-ratify-exchange-development-extraction.md (sibling precedent)"
decided_by: Sean Johnson
decision_date: 2026-07-24
admissibility: supporting
verification:
  status: verified
  verified_by: Sean Johnson
  verified_on: 2026-07-24
  method: "Human review under open review window (.review-open present), direct conversation with Claude Code, 2026-07-24."
supersedes: null
---

# Decision: ratify the `topic-glean` generic extraction schema

## What this ratifies

The frontmatter schema for extraction records produced by the plain Extract
action — gleaning topics/major concepts *with context* from pasted material or
already-captured raw records — as its own extraction sub-type, distinct from
and lighter-weight than the ratified Exchange Development Extraction sub-type
(`decisions/2026-07-22-ratify-exchange-development-extraction.md`).

This enacts `_governed/memory/pending/2026-07-24-generic-extraction-frontmatter-schema.md`
(preserved at `memory/superseded/2026-07-24-generic-extraction-frontmatter-schema-pending-draft.md`),
resolved as follows.

## Decisions on the three open sub-questions

1. **Naming — resolved: `topic-glean`, not `general`.** Matches the vocabulary
   already used by this project's own action-strip data for Extract ("glean
   topics/major concepts with context"), rather than introducing a new term.
2. **Status — resolved: three values, `draft | reviewed | superseded`.**
   Decider's stated reason: ongoing metrics/metadata will be pulled from this
   layer, which requires a status field with more than one value to be
   meaningful. `draft` is set on capture; `reviewed` and `superseded`
   transitions are NOT mechanized by this decision (see "Explicitly not
   decided here") — only the vocabulary is ratified.
3. **Multi-source — resolved: yes, `source` supports more than one raw
   record.** Decider's stated reason: reinforces project integrity — an
   extraction genuinely drawn from several captured fragments should say so,
   rather than being forced to pick one and lose the rest.

## Ratified schema

```yaml
---
layer: extraction
extraction_type: topic-glean
status: draft
source:
  - <raw/ path this was extracted from>
  - <additional raw/ paths, if this extraction draws on more than one>
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

Body: a title, `Extracted from: <raw_ref>` (one or more, comma-separated), an
optional `## Topics / concepts` list, an optional `## Context` section, and a
fixed preservation-only disclaimer ("citable as source evidence for later
synthesis or decision records; does not itself decide anything").

`pii_team_dashboard/server/governed_writer.py` is updated to produce exactly
this schema as part of this decision landing (same session).

## Relationship to Authority Rule 9

Authority Rule 9: "Extraction sub-types (e.g. Exchange Development Extraction)
are preservation, not authority... A new extraction sub-type becomes a durable
artifact class only once a decision record ratifies it." This record is that
ratifying step for `topic-glean`, paralleling the exchange-development
ratification.

## Explicitly not decided here

- The mechanism/trigger for transitioning `status` from `draft` to `reviewed`
  or `superseded` — who sets it, when, through what interface. Only the
  vocabulary is ratified here; the workflow is a future decision.
- Whether an extraction can be regenerated/re-run against an updated raw
  source (versioning of extractions themselves) is not addressed.

## Standing of this record

**ACCEPTED 2026-07-24** under an open human review window (`.review-open`
present), decided by Sean Johnson in direct conversation with Claude Code.
Enactment actions taken with acceptance: this record created; the candidate
pending draft moved to `memory/superseded/` with lineage; `governed_writer.py`
updated to match; `open-questions.md` item 1 marked resolved;
`_governed/index.md` updated.

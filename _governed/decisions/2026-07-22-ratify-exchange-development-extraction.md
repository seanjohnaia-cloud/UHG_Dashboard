---
layer: decision
status: accepted
source:
  - "_governed/extractions/exchange-development/2026-07-22-exchange-development-extraction-v0.1-pii-information-architecture.md (Instance 1, narrated-source provenance)"
  - "_governed/extractions/exchange-development/2026-07-22-exchange-development-extraction-v0.1-instance-2-context-architecture-control-system.md (Instance 2, direct-session provenance)"
  - "_governed/raw/2026-07-22-chat-archive-context-architecture-session.md"
decided_by: Sean Johnson
decision_date: 2026-07-22
supersedes: null
admissibility: supporting
verification:
  status: verified
  verified_by: Sean Johnson
  verified_on: 2026-07-22
  method: "Human review under open review window (.review-open), with both provenance-variant instances available as schema examples."
---

# Decision: Ratify the Exchange Development Extraction as a standing artifact class

## What this ratifies

The **Exchange Development Extraction** (`extractions/exchange-development/`) is promoted from candidate/provisional to a **standing extraction sub-type** in this project's governed layer. It preserves the reciprocal development of ideas between human and AI — who initiated each move, how the other party interpreted or extended it, what emerged, what changed architecturally — rather than only resulting conclusions. Rationale (from Instance 1): interaction itself is institutional knowledge; the Chat Archive tells you what happened, the Extraction tells you what was learned, the Exchange Development Extraction tells a future collaborator how the architecture evolved.

## Capture triggers

File an Exchange Development Extraction when a session produces **reciprocal architectural development** — ideas materially shaped by both parties in alternation, where design lineage (who originated what) would be lost by conclusion-only extraction. Not every session qualifies; routine execution, single-direction instruction, or pure Q&A sessions do not. Time-sensitivity remains a legitimate reason to capture in-session rather than waiting for END OF CHAT.

## Required frontmatter

```yaml
layer: extraction
extraction_type: exchange-development
version: v0.1            # schema version, not instance version
instance: <n>            # sequential within the project
captured_at: YYYY-MM-DD
source_type: session
source_ref: "<source; state explicitly whether provenance is direct-session or narrated/reconstructed>"
captured_by: <agent> (at explicit user direction)
admissibility: initiating
verification: {status: unverified, verified_by: null, verified_on: null, method: null}
```

## Required body structure

Numbered Exchange sections (Initiation / Interpretation / Response / Emergent Insight / Architectural Consequence, marking course corrections), followed by **Design Lineage** (originated-human / originated-AI / emerged-collaboratively), **Unresolved Questions**, and a **Standing** note. Sequence is content; preserve corrections and rejected directions.

## Filing and provenance rules

- Filed under `_governed/extractions/exchange-development/`, date-prefixed.
- Provenance variant must be disclosed: direct-session observation vs. narrated reconstruction (both are valid; the record must say which).
- Per Authority Rule 9 (unchanged by this decision): these records are **preservation, not authority** — citable as source evidence, never authority-bearing themselves.

## Lineage

Sub-type proposed and first instantiated 2026-07-22 (Instance 1, narrated-source); second instance filed the same day at explicit user direction to strengthen this ratification case (Instance 2, direct-session). Both instances predate this decision and stand as the schema examples it ratifies. This decision fulfils the ratification path described in Instance 1's standing note and in `index.md`; those standing notes are superseded by this record (visible in place, per Authority Rule 6 — the notes remain in the frozen extractions; this decision is the correction of record).

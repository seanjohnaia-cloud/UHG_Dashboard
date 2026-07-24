# Open Questions — Pii Team Dashboard server work

Status: working tracking note, non-authoritative. This is not a `_governed/` record and
creates no authority itself — it exists so schema/mechanism choices made under time
pressure to keep the `server/` write path working don't quietly become de facto
standards through repetition, and so a third unratified item doesn't open before the
first two are resolved or explicitly batched into a decision record.

Rule for this file: before adding a new inferred schema or mechanism to `server/`
code, check here first. If two items are already open, resolve or explicitly defer
one before adding a third.

## Open

### 1. In-console concurrence/approval affordance

- **Where:** not built. `prototype/index.html` has no approve/reject UI, and none of
  `server/`'s code can write to `_governed/ledger/`.
- **What's unratified:** the working agreement (2026-07-24) selected option (b) for
  ledger concurrence — it happens entirely outside the dashboard; the console is a
  read-side view of the result only. The agreement explicitly named a fallback: if
  routine field-level concurrence proves too high-friction under option (b), option
  (a) — an in-console approve/reject affordance with role gating and an explicit
  concurrence-event record — should be filed as its own governed decision record
  before anything is built, not backed into via the server or the UI.
- **Flagged:** 2026-07-24 (working agreement, restated at Checkpoint 2 approval).
- **Resolution path:** stays closed/deferred unless someone observes real friction with
  option (b) in practice, at which point it becomes a decision-record proposal, not a
  code change.

## Resolved / not currently open

### Generic extraction frontmatter schema — RESOLVED 2026-07-24

Filed as a candidate proposal 2026-07-24 (Checkpoint 3 follow-up), reviewed and
**accepted the same day** by Sean Johnson under an open review window
(`_governed/.review-open`). Ratified as `decisions/2026-07-24-ratify-generic-extraction-schema.md`:

- `extraction_type: topic-glean` (not `general`) — matches existing Extract
  action vocabulary.
- `status: draft | reviewed | superseded` — three values, needed for ongoing
  metrics/metadata pulls. Note: only the vocabulary is ratified; the decision
  explicitly does not specify what mechanism transitions a record from
  `draft` to `reviewed`/`superseded` — that remains a future question, not
  reopened here.
- `source` supports multiple raw records per extraction (multi-source),
  reasoned as reinforcing project integrity.

`governed_writer.py::write_extraction()`/`extract()` updated and verified
(isolated + live HTTP) to match. Pending draft preserved with lineage at
`_governed/memory/superseded/2026-07-24-generic-extraction-frontmatter-schema-pending-draft.md`.

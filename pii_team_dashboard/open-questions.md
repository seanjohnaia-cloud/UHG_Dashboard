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

### 1. Generic extraction frontmatter schema (`extraction_type: general`)

- **Where:** `server/governed_writer.py`, `write_extraction()`.
- **What's unratified:** `2026-07-22-ratify-exchange-development-extraction.md` ratifies
  a frontmatter schema for the *exchange-development* extraction sub-type only. No
  decision record defines a schema for a plain/general extraction (topics/concepts
  gleaned from pasted material, per the Extract action's governed mapping). The
  `extraction_type: general` shape in `write_extraction()` — `layer / extraction_type /
  status / source / captured_by / captured_at / admissibility / verification` — is this
  codebase's own reasonable inference, modeled on the ratified raw-record and
  exchange-development patterns, not a cited standard.
- **Flagged:** 2026-07-24 (Checkpoint 2).
- **Resolution path:** either ratify a generic extraction schema via its own decision
  record, or determine that Extract's plain output should use a different shape
  entirely (e.g. folded into the exchange-development schema, or something narrower).

### 2. In-console concurrence/approval affordance

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

*(none yet — this file was created 2026-07-24 alongside Checkpoint 3)*

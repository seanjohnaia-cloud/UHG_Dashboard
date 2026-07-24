# Pii Team Dashboard — Handoff

## What this is

This is the Grace/team-side **Pii Console / Pii Team Dashboard** proof. It is an internal project-intelligence command-center spine for project startup, readiness, gaps, governance routing, and module-level operational state.

It is intentionally separate from `05_Dashboard/`, which remains the client-facing Streamlit dashboard for the UHG contractual/LCD deliverable surface.

## What was built

Current committed artifacts under `pii_team_dashboard/` include:

- `data/project-context.seed.json` — scoped launch / Centerline-style project handoff assumptions.
- `data/module-catalog.seed.json` — 12 stable team-side module nodes.
- `data/views.seed.json` — alternate clustering/lens definitions over the same module set.
- `data/dependency-edges.seed.json` — dependency edges for shared-field propagation and downstream readiness effects.
- `data/field-registry.seed.json` — canonical field spine, truth states, blocking effects, and field metadata.
- `data/module-field-map.seed.json` — module permissions over canonical fields.
- `data/action-strip.seed.json` — Extract / Absorb / Elevate / Archive action model.
- `data/state-transition.seed.json` — operational bridge for candidate field state, gaps, conflicts, proposals, concurrence candidates, archive pointers, and propagation events.
- `data/readiness-state.seed.json` — readiness dimensions, state rollups, module profiles, and dashboard posture rules.
- `fixtures/uhg-startup-state.sample.json` — synthetic mixed-readiness startup fixture.
- `prototype/index.html` — self-contained static console proof rendering the fixture against the spine.
- `server/governed_reader.py`, `server/serve.py` — read-only local dev server exposing the real `_governed/ledger/`, `memory/pending/`, and `decisions/` layers as JSON (`/api/state` etc.), separate from and additional to the seed/fixture prototype above. Never writes.
- `server/governed_writer.py` — write-side for Extract / Absorb / Archive (→ `raw/` / `extractions/`, append-only by construction) and Elevate (→ `memory/pending/` only, proposal never approval; cannot write `ledger/`). Exposed via `POST /api/actions/{extract,absorb,archive,elevate}` in `serve.py`. Not yet wired to any button in `prototype/index.html` — that page's display contract is intentionally untouched by this work.
- `server/governed-client.js` — thin fetch wrapper for the read API; not loaded by any page yet.
- `open-questions.md` — running list of schema/mechanism choices made to keep the server work moving that are not backed by a governed decision record. Check it before adding a new inferred schema so a third unratified item doesn't open quietly.

## Synthetic vs. real

The fixture is **synthetic only**. It is not real UHG project state, not client record, not accepted memory, and not authority.

The current seed files are **non-authoritative implementation artifacts**. They model structure and behavior for prototype/spine testing. They do not create governed project truth.

Readiness is **dashboard state, not authority**. A ready/blocked/qualified badge describes scoped operating posture only. Human concurrence and governed records remain the authority boundary.

## What not to touch

- Do **not** touch `05_Dashboard/` for this workstream.
- Do **not** collapse the Pii Console into the client-facing Streamlit dashboard.
- Do **not** treat fixture data as real UHG state.
- Do **not** promote extracted/candidate/proposed/readiness state into current truth without human concurrence.
- Do **not** reintroduce Quarantine as an action-strip function; unresolved state is represented through field truth, admissibility, verification, gaps/conflicts, and Archive/source preservation.

## How to verify

Run focused ad-hoc verification against the relevant artifact rather than treating this as a full application test suite.

Useful checks:

```bash
python3 -m json.tool pii_team_dashboard/data/state-transition.seed.json >/tmp/state-transition.verify.json
python3 -m json.tool pii_team_dashboard/data/readiness-state.seed.json >/tmp/readiness-state.verify.json
python3 -m json.tool pii_team_dashboard/fixtures/uhg-startup-state.sample.json >/tmp/uhg-startup-state.verify.json
```

For the static prototype, verify that:

- `pii_team_dashboard/prototype/index.html` exists.
- It embeds or references the synthetic fixture/spine concepts.
- It contains all 12 module IDs/labels.
- It contains Extract / Absorb / Elevate / Archive.
- It labels the fixture as synthetic/non-authoritative.
- It states that readiness is dashboard state, not authority.
- It does not reference `05_Dashboard`.

## Dev environment notes

- `server/*.py` requires PyYAML (`import yaml`). On this machine, the `python` on PATH (Hermes venv) has it; the Windows Store `python3` does not. If a future session runs the server from a different shell and gets `ModuleNotFoundError: No module named 'yaml'`, that's the venv split, not a broken server.
- Run: `python server/serve.py [port]` from `pii_team_dashboard/`. Serves the existing static prototype unchanged at `/prototype/index.html` plus the governed-state API at `/api/*` (see `serve.py`'s module docstring for the full route list).

## Next intended work

Recommended next steps:

1. Interaction polish for the static console proof.
2. Dependency highlighting between modules and shared fields.
3. Readiness filtering by dimension/state/module.
4. Better selected-module field selection and record drill-down.
5. Live data adapter: **underway**, not "later" — `server/` (Checkpoints 1–3, see `open-questions.md` for what's still unratified) now reads real `ledger/`/`pending/`/`decisions/` state and can write Extract/Absorb/Archive/Elevate records. Not yet wired into `prototype/index.html`; that integration is a deliberately separate, explicitly-flagged step per the current working agreement, not an oversight.

Do not start live-data *integration into the console UI* until the synthetic proof and governance semantics are comfortable — the adapter itself existing under `server/` is not the same thing as wiring it into `index.html`, and the latter has not happened.

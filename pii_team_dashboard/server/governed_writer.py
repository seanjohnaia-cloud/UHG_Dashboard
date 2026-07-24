"""Write-side for the console actions that don't require human concurrence to file:
Extract, Absorb, Archive (Checkpoint 2), and Elevate (Checkpoint 3).

Scope: writes ONLY to _governed/raw/, _governed/extractions/, and (Elevate only)
_governed/memory/pending/. NEVER writes to _governed/ledger/ or _governed/decisions/.
Ledger changes require a human concurrence event that happens outside this API, per
the resident-context concurrence rule -- nothing in this module, and no console
button behind it, may promote a pending/ proposal into ledger/ current truth.

Append-only by construction, not just convention: every write target path is produced by
_unique_path(), which only ever returns a path that does not yet exist. No function in
this module ever opens an existing file for writing. Existing records are therefore
structurally unreachable for edits. All writes additionally serialize through
_WRITE_LOCK so concurrent requests (ThreadingHTTPServer) can't race two writers onto
the same unique path -- the single-pen rule enforced in-process, not just by convention.

Single-pen rule (per the tiered-context-control-system decision): this backend is the
designated pen for dashboard-originated memory/pending/ writes. Every pending record
this module creates is named with a `pii-console-` prefix and carries `derived_by`
identifying dashboard origin, so provenance is unambiguous from the record itself if
other pens (e.g. a Hermes-side session) also write to pending/ under a different,
equally-identifiable naming convention.

Governed mapping (per decisions/2026-07-22-candidate-operational-data-layer-wikillm-pattern.md,
"RESOLVED 2026-07-22: the function strip"):
  - Extract  -- gleans topics/concepts *with context* from pasted chat or one or more
                already-captured artifacts. Produces a raw/ record (only if fresh source
                text was given) plus a `topic-glean` extractions/ record referencing all
                cited raw sources (multi-source, per the ratified schema below).
  - Absorb   -- admits an externally-created artifact into raw/, with provenance
                disclosing external origin. Admission, not endorsement -- it does NOT
                also extract; that is a separate, later Extract call.
  - Archive  -- captures dialogue near-verbatim (both sides) as an append-only raw/
                record. No extraction step.
  - Elevate  -- a PM's direct proposal intake. Files ONLY into memory/pending/, using
                the exact "proposed durable memory" frontmatter pattern already ratified
                by inheritance from PI v1 AGENTS.md (layer/status/source/derived_by/
                confidence/uncertainty/admissibility/verification/supersedes/review_after).
                Elevate is proposal, never approval; this function cannot and does not
                touch ledger/.

The `topic-glean` extraction schema (extraction_type, three-value status, multi-source
`source`) is ratified by `_governed/decisions/2026-07-24-ratify-generic-extraction-schema.md`
(accepted 2026-07-24, decided_by: Sean Johnson). `write_extraction()` produces exactly
that schema. Note: that decision ratifies the *vocabulary* only -- nothing in this
module transitions a record's `status` from `draft` to `reviewed`/`superseded`; the
decision explicitly leaves that mechanism unspecified as future work.

Remaining open, unratified item (tracked in pii_team_dashboard/open-questions.md --
read that file before adding a second one):
  1. Elevate's proposal-specific content (proposed change, affected fields/modules,
     authority requirement, requested human action) is deliberately kept in the
     markdown BODY rather than added as new frontmatter keys, to avoid inventing an
     unratified schema. If Elevate proposals need to be machine-queryable by those
     fields later, that's a decision-record-worthy schema question, not something to
     back into via additive frontmatter here.
"""
from __future__ import annotations

import datetime
import re
import threading
from pathlib import Path
from typing import Any

import yaml

from governed_reader import GOVERNED_ROOT as DEFAULT_GOVERNED_ROOT
from governed_reader import REPO_ROOT

DEFAULT_CAPTURED_BY = "pii-console (server/governed_writer.py)"

_WRITE_LOCK = threading.Lock()


def _slugify(text: str, max_len: int = 60) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text[:max_len].rstrip("-") or "untitled"


def _unique_path(directory: Path, stem: str, suffix: str = ".md") -> Path:
    """Return a path guaranteed not to already exist. Never returns an existing path,
    which is what makes every write in this module append-only by construction."""
    directory.mkdir(parents=True, exist_ok=True)
    candidate = directory / f"{stem}{suffix}"
    if not candidate.exists():
        return candidate
    n = 2
    while True:
        candidate = directory / f"{stem}-{n}{suffix}"
        if not candidate.exists():
            return candidate
        n += 1


def _rel(path: Path, repo_root: Path) -> str:
    return str(path.relative_to(repo_root)).replace("\\", "/")


def _render_record(frontmatter: dict[str, Any], title: str, body_text: str) -> str:
    fm_text = yaml.safe_dump(frontmatter, sort_keys=False, default_flow_style=False, allow_unicode=True)
    return f"---\n{fm_text}---\n\n# {title}\n\n{body_text.strip()}\n"


def write_raw(
    *,
    source_type: str,
    source_ref: str,
    title: str,
    body_text: str,
    captured_by: str = DEFAULT_CAPTURED_BY,
    captured_at: str | None = None,
    extra_frontmatter: dict[str, Any] | None = None,
    governed_root: Path | None = None,
) -> dict[str, Any]:
    governed_root = governed_root or DEFAULT_GOVERNED_ROOT
    repo_root = governed_root.parent
    captured_at = captured_at or datetime.date.today().isoformat()

    frontmatter: dict[str, Any] = {
        "layer": "raw",
        "captured_at": captured_at,
        "source_type": source_type,
        "source_ref": source_ref,
        "captured_by": captured_by,
        # Explicit rather than relying on read-time defaulting (Rule 1: OPTIONAL on raw,
        # but including them is the more legible choice and matches this repo's existing
        # raw records under _governed/raw/).
        "admissibility": "initiating",
        "verification": {"status": "unverified", "verified_by": None, "verified_on": None, "method": None},
    }
    if extra_frontmatter:
        frontmatter.update(extra_frontmatter)

    stem = f"{captured_at}-{_slugify(title)}"
    with _WRITE_LOCK:
        path = _unique_path(governed_root / "raw", stem)
        path.write_text(_render_record(frontmatter, title, body_text), encoding="utf-8")

    return {"path": _rel(path, repo_root), "frontmatter": frontmatter, "title": title}


def write_extraction(
    *,
    title: str,
    raw_refs: list[str],
    topics: list[str] | None = None,
    notes: str | None = None,
    captured_by: str = DEFAULT_CAPTURED_BY,
    captured_at: str | None = None,
    governed_root: Path | None = None,
) -> dict[str, Any]:
    """Writes the `topic-glean` extraction schema ratified by
    `_governed/decisions/2026-07-24-ratify-generic-extraction-schema.md`.
    `raw_refs` may cite more than one raw/ record (multi-source, per that decision)."""
    if not raw_refs:
        raise ValueError("write_extraction requires at least one raw_ref in raw_refs -- an extraction must cite its source(s)")
    governed_root = governed_root or DEFAULT_GOVERNED_ROOT
    repo_root = governed_root.parent
    captured_at = captured_at or datetime.date.today().isoformat()

    frontmatter: dict[str, Any] = {
        "layer": "extraction",
        "extraction_type": "topic-glean",
        "status": "draft",
        "source": list(raw_refs),
        "captured_by": captured_by,
        "captured_at": captured_at,
        "admissibility": "initiating",
        "verification": {"status": "unverified", "verified_by": None, "verified_on": None, "method": None},
    }

    refs_text = ", ".join(f"`{r}`" for r in raw_refs)
    body_parts = [f"Extracted from: {refs_text}", ""]
    if topics:
        body_parts.append("## Topics / concepts")
        body_parts.append("")
        for topic in topics:
            body_parts.append(f"- {topic}")
        body_parts.append("")
    if notes:
        body_parts.append("## Context")
        body_parts.append("")
        body_parts.append(notes)
        body_parts.append("")
    body_parts.append(
        "> Preservation record only (Authority Rule 9): citable as source evidence for "
        "later synthesis or decision records; does not itself decide anything."
    )

    stem = f"{captured_at}-extract-{_slugify(title)}"
    with _WRITE_LOCK:
        path = _unique_path(governed_root / "extractions", stem)
        path.write_text(_render_record(frontmatter, title, "\n".join(body_parts)), encoding="utf-8")

    return {"path": _rel(path, repo_root), "frontmatter": frontmatter, "title": title}


def extract(
    *,
    title: str,
    context: str | None = None,
    source_text: str | None = None,
    existing_raw_refs: list[str] | None = None,
    topics: list[str] | None = None,
    captured_by: str = DEFAULT_CAPTURED_BY,
    governed_root: Path | None = None,
) -> dict[str, Any]:
    """`existing_raw_refs` may name more than one already-captured raw/ record --
    multi-source extraction, per the ratified topic-glean schema. Combined with
    `source_text` (a fresh capture) if both are given; at least one is required."""
    existing_raw_refs = list(existing_raw_refs or [])
    if not existing_raw_refs and not source_text:
        raise ValueError("extract requires source_text (fresh pasted material) and/or existing_raw_refs (already-captured sources)")

    raw_result = None
    raw_refs = list(existing_raw_refs)
    if source_text:
        raw_result = write_raw(
            source_type="session",
            source_ref="pasted chat/artifact supplied directly to Extract",
            title=title,
            body_text=source_text,
            captured_by=captured_by,
            governed_root=governed_root,
        )
        raw_refs.append(raw_result["path"])

    extraction_result = write_extraction(
        title=title,
        raw_refs=raw_refs,
        topics=topics,
        notes=context,
        captured_by=captured_by,
        governed_root=governed_root,
    )
    return {"action": "extract", "raw": raw_result, "extraction": extraction_result}


def absorb(
    *,
    title: str,
    artifact_text: str,
    received_from: str,
    notes: str | None = None,
    captured_by: str = DEFAULT_CAPTURED_BY,
    governed_root: Path | None = None,
) -> dict[str, Any]:
    body = (
        f"**Received from:** {received_from}\n\n"
        "**Standing:** admitted via Absorb. Admission is not endorsement -- this artifact "
        "has not been Extracted, sorted, or triaged, and carries no ledger or synthesis "
        "standing until it is.\n\n---\n\n" + artifact_text.strip()
    )
    if notes:
        body += f"\n\n---\n\n**Intake note:** {notes}"

    raw_result = write_raw(
        source_type="external",
        source_ref=f"external artifact received from {received_from}",
        title=title,
        body_text=body,
        captured_by=captured_by,
        extra_frontmatter={"received_from": received_from, "endorsed": False},
        governed_root=governed_root,
    )
    return {"action": "absorb", "raw": raw_result}


def archive(
    *,
    title: str,
    dialogue_text: str,
    captured_by: str = DEFAULT_CAPTURED_BY,
    governed_root: Path | None = None,
) -> dict[str, Any]:
    raw_result = write_raw(
        source_type="session",
        source_ref="dialogue captured via Pii Console Archive (near-verbatim, both sides)",
        title=title,
        body_text=dialogue_text,
        captured_by=captured_by,
        governed_root=governed_root,
    )
    return {"action": "archive", "raw": raw_result}


_CONFIDENCE_VALUES = {"high", "medium", "low", "contested"}


def elevate(
    *,
    title: str,
    proposed_change: str,
    source: list[str],
    confidence: str,
    uncertainty: str,
    review_after: str,
    affected_fields: list[str] | None = None,
    affected_modules: list[str] | None = None,
    authority_requirement: str | None = None,
    requested_human_action: str | None = None,
    supersedes: str | None = None,
    derived_by: str = DEFAULT_CAPTURED_BY,
    governed_root: Path | None = None,
) -> dict[str, Any]:
    """File a proposal into memory/pending/. Proposal only -- never approval, and this
    function has no code path that can write to ledger/. See module docstring for the
    single-pen naming convention and why proposal-specific content lives in the body
    rather than as new frontmatter keys.

    `source`, `confidence`, `uncertainty`, and `review_after` are required with no
    defaults: PI v1's ratified pending-memory pattern requires all four, and no
    governed decision defines a default confidence, uncertainty text, or review
    window -- inventing one here would be exactly the kind of unratified schema
    creep flagged in the module docstring, just relocated to a different field.
    """
    if not source:
        raise ValueError(
            "elevate requires at least one `source` reference (a raw/extraction path, "
            "or an explicit note such as 'direct operator input via Pii Console, <date>' "
            "if there is no prior capture) -- proposals must not be unsourced"
        )
    if confidence not in _CONFIDENCE_VALUES:
        raise ValueError(f"confidence must be one of {sorted(_CONFIDENCE_VALUES)}, got {confidence!r}")
    if not uncertainty:
        raise ValueError(
            "elevate requires an explicit `uncertainty` statement -- what remains "
            "unconfirmed, ambiguous, or time-sensitive about this proposal"
        )
    if not review_after:
        raise ValueError(
            "elevate requires an explicit `review_after` date (YYYY-MM-DD) -- no default "
            "review window is defined by any governed decision"
        )

    governed_root = governed_root or DEFAULT_GOVERNED_ROOT
    repo_root = governed_root.parent
    today = datetime.date.today().isoformat()

    frontmatter: dict[str, Any] = {
        "layer": "memory",
        "status": "proposed",
        "source": list(source),
        "derived_by": derived_by,
        "confidence": confidence,
        "uncertainty": uncertainty,
        # Fixed, not caller-controllable: pending memory may only initiate, never
        # support (PI v1 2026-07-19 decision, layer-based defaults table). A proposal
        # cannot elevate its own admissibility by asking nicely.
        "admissibility": "initiating",
        "verification": {"status": "unverified", "verified_by": None, "verified_on": None, "method": None},
        "supersedes": supersedes,
        "review_after": review_after,
    }

    body_parts = [f"## Proposed change\n\n{proposed_change.strip()}"]
    if affected_fields:
        body_parts.append("## Affected fields\n\n" + "\n".join(f"- {f}" for f in affected_fields))
    if affected_modules:
        body_parts.append("## Affected modules\n\n" + "\n".join(f"- {m}" for m in affected_modules))
    if authority_requirement:
        body_parts.append(f"## Authority requirement\n\n{authority_requirement}")
    if requested_human_action:
        body_parts.append(f"## Requested human action\n\n{requested_human_action}")
    body_parts.append(
        "> Elevate is proposal intake, not approval "
        "(`_governed/decisions/2026-07-22-candidate-operational-data-layer-wikillm-pattern.md`). "
        "This record has no effect on `_governed/ledger/` or any other current-truth state "
        "until a human concurrence event -- performed outside this dashboard/API, per the "
        "resident-context concurrence rule -- explicitly promotes it."
    )

    stem = f"{today}-pii-console-elevate-{_slugify(title)}"
    with _WRITE_LOCK:
        path = _unique_path(governed_root / "memory" / "pending", stem)
        path.write_text(_render_record(frontmatter, title, "\n\n".join(body_parts)), encoding="utf-8")

    return {"action": "elevate", "pending": {"path": _rel(path, repo_root), "frontmatter": frontmatter, "title": title}}

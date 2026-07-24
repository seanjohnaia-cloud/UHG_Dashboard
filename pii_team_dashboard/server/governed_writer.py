"""Write-side for the three non-concurrence-gated console actions: Extract, Absorb, Archive.

Scope (Checkpoint 2): writes ONLY to _governed/raw/ and _governed/extractions/. Never
writes to _governed/ledger/, _governed/memory/, or _governed/decisions/ -- those require
either human concurrence (ledger, per the resident-context concurrence rule) or are
authority-bearing by hand (decisions). Elevate (which files memory/pending/ proposals)
is explicitly out of scope for this checkpoint.

Append-only by construction, not just convention: every write target path is produced by
_unique_path(), which only ever returns a path that does not yet exist. No function in
this module ever opens an existing file for writing. Existing raw/extraction records are
therefore structurally unreachable for edits.

Governed mapping (per decisions/2026-07-22-candidate-operational-data-layer-wikillm-pattern.md,
"RESOLVED 2026-07-22: the function strip"):
  - Extract  -- gleans topics/concepts *with context* from pasted chat or an already-
                captured artifact. Produces a raw/ record (only if the source wasn't
                already captured) plus an extractions/ record referencing it.
  - Absorb   -- admits an externally-created artifact into raw/, with provenance
                disclosing external origin. Admission, not endorsement -- it does NOT
                also extract; that is a separate, later Extract call.
  - Archive  -- captures dialogue near-verbatim (both sides) as an append-only raw/
                record. No extraction step.

Flag, not a decision: no governed decision record has ratified a frontmatter schema for
*generic* extraction records the way 2026-07-22-ratify-exchange-development-extraction.md
ratified the exchange-development sub-type. The `extraction_type: general` schema below
is this module's own reasonable inference (layer/status/source/captured_by/captured_at,
same admissibility/verification shape as every other non-raw layer), not a cited
standard. It should be treated as a proposal for review, not settled schema.
"""
from __future__ import annotations

import datetime
import re
from pathlib import Path
from typing import Any

import yaml

from governed_reader import GOVERNED_ROOT as DEFAULT_GOVERNED_ROOT
from governed_reader import REPO_ROOT

DEFAULT_CAPTURED_BY = "pii-console (server/governed_writer.py, Checkpoint 2)"


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
    path = _unique_path(governed_root / "raw", stem)
    path.write_text(_render_record(frontmatter, title, body_text), encoding="utf-8")

    return {"path": _rel(path, repo_root), "frontmatter": frontmatter, "title": title}


def write_extraction(
    *,
    title: str,
    raw_ref: str,
    topics: list[str] | None = None,
    notes: str | None = None,
    captured_by: str = DEFAULT_CAPTURED_BY,
    captured_at: str | None = None,
    governed_root: Path | None = None,
) -> dict[str, Any]:
    governed_root = governed_root or DEFAULT_GOVERNED_ROOT
    repo_root = governed_root.parent
    captured_at = captured_at or datetime.date.today().isoformat()

    frontmatter: dict[str, Any] = {
        "layer": "extraction",
        "extraction_type": "general",
        "status": "draft",
        "source": [raw_ref],
        "captured_by": captured_by,
        "captured_at": captured_at,
        "admissibility": "initiating",
        "verification": {"status": "unverified", "verified_by": None, "verified_on": None, "method": None},
    }

    body_parts = [f"Extracted from: `{raw_ref}`", ""]
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
        "> Preservation record only (Authority Rule 9-equivalent for generic extractions): "
        "citable as source evidence for later synthesis or decision records; does not itself "
        "decide anything."
    )

    stem = f"{captured_at}-extract-{_slugify(title)}"
    path = _unique_path(governed_root / "extractions", stem)
    path.write_text(_render_record(frontmatter, title, "\n".join(body_parts)), encoding="utf-8")

    return {"path": _rel(path, repo_root), "frontmatter": frontmatter, "title": title}


def extract(
    *,
    title: str,
    context: str | None = None,
    source_text: str | None = None,
    existing_raw_ref: str | None = None,
    topics: list[str] | None = None,
    captured_by: str = DEFAULT_CAPTURED_BY,
    governed_root: Path | None = None,
) -> dict[str, Any]:
    if not existing_raw_ref and not source_text:
        raise ValueError("extract requires either existing_raw_ref (already-captured source) or source_text (fresh pasted material)")

    raw_result = None
    if existing_raw_ref:
        raw_ref = existing_raw_ref
    else:
        raw_result = write_raw(
            source_type="session",
            source_ref="pasted chat/artifact supplied directly to Extract",
            title=title,
            body_text=source_text,
            captured_by=captured_by,
            governed_root=governed_root,
        )
        raw_ref = raw_result["path"]

    extraction_result = write_extraction(
        title=title,
        raw_ref=raw_ref,
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

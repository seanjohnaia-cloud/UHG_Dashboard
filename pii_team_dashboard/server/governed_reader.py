"""Read-only reader for this project's _governed/ layers.

Scope (Checkpoint 1 of the dashboard read-side wiring plan): ledger/, memory/pending/,
and decisions/. This module never writes to _governed/ -- it only parses existing files.

Governed by UHG_Dashboard/AGENTS.md and, specifically, the 2026-07-22 decisions:
  - decisions/2026-07-22-candidate-operational-data-layer-wikillm-pattern.md (ledger/)
  - decisions/2026-07-22-resident-context-concurrence-rule.md (concurrence gate)

admissibility/verification defaulting follows the layer x status table in PI v1's
decisions/2026-07-19-admissibility-and-verification-as-explicit-pi-fields.md. That table
has no row for `ledger/` -- it predates the ledger decision -- so ledger records with
missing frontmatter are reported as unresolved rather than defaulted to a guessed value.
"""
from __future__ import annotations

import datetime
import re
from pathlib import Path
from typing import Any

import yaml


def _json_safe(value: Any) -> Any:
    """Recursively convert YAML-parsed date/datetime values to ISO strings.

    PyYAML auto-parses unquoted `YYYY-MM-DD` frontmatter values (e.g. decision_date)
    into datetime.date objects, which json.dumps cannot serialize. Frontmatter is
    otherwise passed through unchanged -- this only normalizes date-like leaves.
    """
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: _json_safe(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_json_safe(v) for v in value]
    return value

REPO_ROOT = Path(__file__).resolve().parents[2]  # .../UHG_Dashboard
GOVERNED_ROOT = REPO_ROOT / "_governed"
LEDGER_DIR = GOVERNED_ROOT / "ledger"
PENDING_DIR = GOVERNED_ROOT / "memory" / "pending"
DECISIONS_DIR = GOVERNED_ROOT / "decisions"

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?(.*)\Z", re.DOTALL)

# (layer, status) -> (admissibility default, verification.status default)
# Source: PI v1 2026-07-19 decision, "Layer-based defaults" table.
LAYER_STATUS_DEFAULTS: dict[tuple[str, str | None], tuple[str, str | None]] = {
    ("raw", None): ("initiating", "unverified"),
    ("extractions", None): ("initiating", "unverified"),
    ("synthesis", None): ("initiating", "unverified"),
    ("memory", "pending"): ("initiating", "unverified"),
    ("memory", "accepted"): ("supporting", "verified"),
    ("memory", "superseded"): ("quarantined", None),
    ("decision", "candidate"): ("initiating", "unverified"),
    ("decision", "accepted"): ("supporting", "verified"),
    ("decision", "superseded"): ("quarantined", None),
}

SKIP_FILENAMES = {"README.md", "index.md"}


def _rel(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT)).replace("\\", "/")


def _read_record(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {
            "path": _rel(path),
            "frontmatter": {},
            "frontmatter_present": False,
            "body": text.strip(),
        }
    fm_text, body = match.group(1), match.group(2)
    try:
        frontmatter = yaml.safe_load(fm_text) or {}
        if not isinstance(frontmatter, dict):
            raise yaml.YAMLError(f"frontmatter did not parse to a mapping (got {type(frontmatter).__name__})")
        frontmatter = _json_safe(frontmatter)
    except yaml.YAMLError as exc:
        return {
            "path": _rel(path),
            "frontmatter": {},
            "frontmatter_present": True,
            "parse_error": str(exc),
            "body": body.strip(),
        }
    return {
        "path": _rel(path),
        "frontmatter": frontmatter,
        "frontmatter_present": True,
        "body": body.strip(),
    }


def _title(record: dict[str, Any]) -> str:
    for line in record.get("body", "").splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return Path(record["path"]).stem


def _excerpt(record: dict[str, Any], max_chars: int = 280) -> str:
    lines = [
        line.strip()
        for line in record.get("body", "").splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]
    text = " ".join(lines)
    return (text[: max_chars - 1] + "…") if len(text) > max_chars else text


def _apply_admissibility_verification(record: dict[str, Any]) -> dict[str, Any]:
    """Resolve admissibility/verification.status per the PI v1 defaulting table.

    Never fabricates a default outside the table: if (layer, status) has no row
    (this is currently true for every `ledger/` record), the fields are left
    unresolved and `defaults_unresolved: true` is set so callers can surface it
    honestly rather than display a guessed value.
    """
    fm = record.get("frontmatter") or {}
    layer = fm.get("layer")
    status = fm.get("status")
    default_row = LAYER_STATUS_DEFAULTS.get((layer, status)) or LAYER_STATUS_DEFAULTS.get((layer, None))

    admissibility = fm.get("admissibility")
    admissibility_defaulted = False
    if admissibility is None and default_row is not None:
        admissibility = default_row[0]
        admissibility_defaulted = True

    verification = fm.get("verification") or {}
    verification_status = verification.get("status") if isinstance(verification, dict) else None
    verification_status_defaulted = False
    if verification_status is None and default_row is not None:
        verification_status = default_row[1]
        verification_status_defaulted = True

    record["admissibility"] = admissibility
    record["admissibility_defaulted"] = admissibility_defaulted
    record["verification_status"] = verification_status
    record["verification_status_defaulted"] = verification_status_defaulted
    record["defaults_unresolved"] = default_row is None and (admissibility is None or verification_status is None)
    return record


def _list_records(dir_path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    if not dir_path.exists():
        return records
    for path in sorted(dir_path.rglob("*.md")):
        if path.name in SKIP_FILENAMES:
            continue
        record = _read_record(path)
        record["title"] = _title(record)
        record["excerpt"] = _excerpt(record)
        _apply_admissibility_verification(record)
        records.append(record)
    return records


def read_decisions() -> list[dict[str, Any]]:
    return _list_records(DECISIONS_DIR)


def read_ledger() -> list[dict[str, Any]]:
    return _list_records(LEDGER_DIR)


def read_pending() -> list[dict[str, Any]]:
    return _list_records(PENDING_DIR)


def _cross_reference_pending_against_ledger(pending: list[dict], ledger: list[dict]) -> None:
    """Mark each pending proposal with whether it targets a field that already
    has a ledger entry (i.e. proposes a change to existing state vs a new field).
    Mutates `pending` in place. With ledger empty this is currently a no-op for
    every record, which is itself the honest, correct answer today.
    """
    ledger_field_ids = {
        rec["frontmatter"].get("field_id")
        for rec in ledger
        if isinstance(rec.get("frontmatter"), dict) and rec["frontmatter"].get("field_id")
    }
    for rec in pending:
        fm = rec.get("frontmatter") or {}
        field_id = fm.get("field_id")
        rec["field_id"] = field_id
        rec["proposes_change_to_existing_field"] = bool(field_id) and field_id in ledger_field_ids
        rec["status_for_console"] = "awaiting_concurrence"


def read_state() -> dict[str, Any]:
    """Everything the console's read side needs in one call."""
    ledger = read_ledger()
    pending = read_pending()
    decisions = read_decisions()
    _cross_reference_pending_against_ledger(pending, ledger)

    warnings: list[str] = []
    if not ledger:
        warnings.append(
            "ledger/ has 0 field records. This is the true current state, not a load failure -- "
            "per ledger/README.md, first entries are expected to arrive via Extract -> pending -> concurrence."
        )
    if not pending:
        warnings.append("memory/pending/ has 0 proposals awaiting concurrence.")
    unresolved = [rec["path"] for rec in ledger if rec.get("defaults_unresolved")]
    if unresolved:
        warnings.append(
            "admissibility/verification could not be defaulted for ledger record(s) "
            f"{unresolved} -- the PI v1 defaulting table has no (layer, status) row for `ledger`, "
            "so these are reported as-authored rather than guessed."
        )

    return {
        "schema": "pii-team-dashboard.governed-state.v0",
        "ledger": ledger,
        "pending": pending,
        "decisions": decisions,
        "meta": {
            "counts": {"ledger": len(ledger), "pending": len(pending), "decisions": len(decisions)},
            "warnings": warnings,
            "source": "live read of _governed/ at request time (not cached, not authoritative synthesis)",
        },
    }


if __name__ == "__main__":
    import json
    import sys

    print(json.dumps(read_state(), indent=2), file=sys.stdout)

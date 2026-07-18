"""Dashboard configuration loading for Pii launcher and dashboard shells."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

APP_DIR = Path(__file__).resolve().parent
CONFIG_DIR = APP_DIR / "dashboard_configs"


def load_dashboard_config(dashboard_id: str) -> dict[str, Any]:
    """Load one dashboard configuration by dashboard_id."""
    path = CONFIG_DIR / f"{dashboard_id}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def list_dashboard_configs() -> list[dict[str, Any]]:
    """Return every known dashboard configuration sorted by file name."""
    return [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(CONFIG_DIR.glob("*.json"))
    ]


def display_name_for_dashboard(dashboard_id: str) -> str:
    """Return a human label for a dashboard, falling back to the id when missing."""
    try:
        config = load_dashboard_config(dashboard_id)
    except FileNotFoundError:
        return dashboard_id
    return str(config.get("display_name") or dashboard_id)

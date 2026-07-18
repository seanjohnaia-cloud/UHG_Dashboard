"""Selectable Pii dashboard module registry."""

from __future__ import annotations

from typing import Any

MODULE_REGISTRY: dict[str, dict[str, Any]] = {
    "portfolio_home": {
        "label": "Portfolio Home",
        "dashboard_types": ["portfolio"],
        "status": "development",
    },
    "project_index": {
        "label": "Project Index",
        "dashboard_types": ["portfolio"],
        "status": "development",
    },
    "cross_project_metrics": {
        "label": "Cross-Project Metrics",
        "dashboard_types": ["portfolio"],
        "status": "development",
    },
    "sla_kpi_reporting": {
        "label": "SLA / KPI Reporting",
        "dashboard_types": ["portfolio"],
        "status": "development",
    },
    "contract_governance": {
        "label": "Contract / SOW Governance",
        "dashboard_types": ["portfolio"],
        "status": "development",
    },
    "project_home": {
        "label": "Project Home",
        "dashboard_types": ["project"],
        "status": "approved",
    },
    "lcd_baseline": {
        "label": "LCD / Baseline",
        "dashboard_types": ["project"],
        "status": "development",
    },
    "project_scope": {
        "label": "Project Scope",
        "dashboard_types": ["project"],
        "status": "development",
    },
    "project_budget": {
        "label": "Project Budget",
        "dashboard_types": ["project"],
        "status": "development",
    },
    "compensation": {
        "label": "Compensation",
        "dashboard_types": ["project"],
        "status": "development",
    },
    "design_schedule": {
        "label": "Design Schedule",
        "dashboard_types": ["project"],
        "status": "development",
    },
    "consultants": {
        "label": "Consultants",
        "dashboard_types": ["project"],
        "status": "development",
    },
    "alliance_partners": {
        "label": "Alliance Partners",
        "dashboard_types": ["project"],
        "status": "development",
    },
    "contracts": {
        "label": "Contracts",
        "dashboard_types": ["project"],
        "status": "development",
    },
    "service_order_review": {
        "label": "Service Order Review",
        "dashboard_types": ["project"],
        "status": "development",
    },
    "project_metrics": {
        "label": "Metrics",
        "dashboard_types": ["project"],
        "status": "development",
    },
}


def modules_for_dashboard_type(dashboard_type: str) -> dict[str, dict[str, Any]]:
    """Return modules available to a Portfolio or Project Dashboard."""
    return {
        key: value
        for key, value in MODULE_REGISTRY.items()
        if dashboard_type in value["dashboard_types"]
    }


def module_label(module_id: str) -> str:
    """Return the display label for a module id."""
    module = MODULE_REGISTRY.get(module_id, {})
    return str(module.get("label") or module_id)

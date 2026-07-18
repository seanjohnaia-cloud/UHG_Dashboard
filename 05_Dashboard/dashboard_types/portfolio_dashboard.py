"""Portfolio Dashboard shell for UHG multi-project oversight."""

from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

DASHBOARD_DIR = Path(__file__).resolve().parents[1]
if str(DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(DASHBOARD_DIR))

from dashboard_config import display_name_for_dashboard, load_dashboard_config  # noqa: E402
from module_registry import module_label  # noqa: E402


def render_portfolio_dashboard(dashboard_id: str = "uhg_portfolio") -> None:
    st.set_page_config(page_title="UHG Portfolio Dashboard", layout="wide")
    config = load_dashboard_config(dashboard_id)

    st.title(config["display_name"])
    st.caption("Portfolio Dashboard · multi-project UHG/account oversight")

    st.subheader("Portfolio Modules")
    for module_id in config.get("active_modules", []):
        st.markdown(f"- **{module_label(module_id)}** — `{module_id}`")

    st.subheader("Child Project Dashboards")
    child_dashboards = config.get("child_dashboards", [])
    if not child_dashboards:
        st.info("No child Project Dashboards linked yet.")
    for child_id in child_dashboards:
        st.markdown(f"- **{display_name_for_dashboard(child_id)}** — `{child_id}`")

    st.subheader("Development Boundary")
    st.markdown(
        "Portfolio Dashboard modules are separated from Project Dashboard modules so cross-project intelligence "
        "does not contaminate individual project working records."
    )


if __name__ == "__main__":
    render_portfolio_dashboard()

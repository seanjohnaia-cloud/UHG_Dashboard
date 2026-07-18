"""Pii launcher for opening or creating Portfolio and Project Dashboards."""

from __future__ import annotations

import streamlit as st

from dashboard_config import list_dashboard_configs
from module_registry import modules_for_dashboard_type

DASHBOARD_TYPE_LABELS = {
    "Portfolio Dashboard": "portfolio",
    "Project Dashboard": "project",
}


def render_launcher() -> None:
    st.set_page_config(page_title="Pii Launcher", layout="wide")
    st.title("Launch Pii")
    st.caption("Open an existing Portfolio or Project Dashboard, or create a new dashboard container.")

    mode = st.radio("What do you want to do?", ["Open Existing Dashboard", "Create New Dashboard"])

    if mode == "Open Existing Dashboard":
        st.subheader("Open Existing Dashboard")
        dashboard_filter = st.radio("Dashboard Filter", ["All", "Portfolio Dashboard", "Project Dashboard"], horizontal=True)
        dashboards = list_dashboard_configs()
        if dashboard_filter != "All":
            desired_type = DASHBOARD_TYPE_LABELS[dashboard_filter]
            dashboards = [dashboard for dashboard in dashboards if dashboard["dashboard_type"] == desired_type]

        labels = [f"{dashboard['display_name']} ({dashboard['dashboard_type']})" for dashboard in dashboards]
        st.selectbox("Dashboard", labels)
        st.button("Open Dashboard")
        st.info("Routing is staged: this launcher defines the Portfolio/Project choice before deeper dashboard navigation is wired in.")
        return

    st.subheader("Create New Dashboard")
    dashboard_type_label = st.radio("Dashboard Type", ["Portfolio Dashboard", "Project Dashboard"])
    dashboard_type = DASHBOARD_TYPE_LABELS[dashboard_type_label]
    st.text_input("Dashboard Name")
    module_options = [module["label"] for module in modules_for_dashboard_type(dashboard_type).values()]
    st.multiselect("Select Modules", module_options, default=module_options[:3])
    if dashboard_type == "project":
        portfolio_options = [
            dashboard["display_name"]
            for dashboard in list_dashboard_configs()
            if dashboard["dashboard_type"] == "portfolio"
        ]
        st.selectbox("Parent Portfolio Dashboard", ["(None)", *portfolio_options])
    st.button(f"Create {dashboard_type_label}")


if __name__ == "__main__":
    render_launcher()

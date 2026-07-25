"""Grace Design Studios — UHG client-facing dashboard (entry point).

Client build of the 05_Dashboard surface: Portfolio home plus per-project
pages rendering LCD-W content read-only. Internal work surfaces (LCD manual
entry, Service Order preparation, metric logging) live in the separate Pii
Team Dashboard, not here.

Run: streamlit run client_app.py
"""

from __future__ import annotations

from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parent
GRACE_LOGO = APP_DIR / "assets" / "grace_stacked_logo.jpg"

st.set_page_config(
    page_title="Grace Design Studios — UHG program",
    page_icon=str(GRACE_LOGO),
    layout="wide",
    initial_sidebar_state="expanded",
)

st.logo(str(GRACE_LOGO), size="large")

page = st.navigation(
    {
        "": [
            st.Page(
                "app_pages/portfolio_home.py",
                title="Portfolio home",
                icon=":material/dashboard:",
                default=True,
            ),
        ],
        "Fairview Urgent Care": [
            st.Page("app_pages/overview.py", title="Overview", icon=":material/home:"),
            st.Page("app_pages/project_data.py", title="Project data", icon=":material/table_chart:"),
            st.Page("app_pages/partners.py", title="Alliance partners", icon=":material/handshake:"),
            st.Page("app_pages/scope.py", title="Scope", icon=":material/architecture:"),
            st.Page("app_pages/budget.py", title="Budget", icon=":material/payments:"),
            st.Page("app_pages/compensation.py", title="Compensation", icon=":material/receipt_long:"),
            st.Page("app_pages/schedule.py", title="Design schedule", icon=":material/calendar_month:"),
            st.Page("app_pages/consultants.py", title="Consultants", icon=":material/engineering:"),
            st.Page("app_pages/contracts.py", title="Contracts", icon=":material/contract:"),
        ],
    }
)

with st.sidebar:
    st.caption("Demonstration environment — Fairview specimen project (synthetic data).")

page.run()

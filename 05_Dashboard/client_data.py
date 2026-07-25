"""Data adapter for the client-facing dashboard.

Today this serves the Fairview specimen fixture. A real project (e.g. Muncie)
plugs in by returning the same payload shape from ``load_project`` — pages
never read fixture files directly, so swapping the source is a one-function
change. Real client data must not be wired in until its release is approved.
"""

from __future__ import annotations

from typing import Any

import streamlit as st

from project_home_dashboard import load_fixture


@st.cache_data(ttl=600)
def load_project() -> dict[str, Any]:
    return load_fixture()

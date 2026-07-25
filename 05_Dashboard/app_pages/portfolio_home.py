import pandas as pd
import streamlit as st

from client_data import load_project
from project_home_dashboard import (
    REQUIRED_METRIC_ROWS,
    SOW_KPI_ROWS,
    field_value,
    origin,
)

payload = load_project()
record = origin(payload)

st.title("UHG program portfolio")
st.caption(
    "Active Grace Design Studios projects under the UHG master agreement, "
    "with the program reporting required by the Scope of Work."
)

st.subheader("Active projects")
with st.container(border=True):
    name_col, info_col, action_col = st.columns([1.6, 2.2, 1.0], vertical_alignment="center")
    with name_col:
        st.markdown(f"**{field_value(record, 'general_project_information', 'project_name')}**")
        st.caption(field_value(record, "general_project_information", "project_location"))
    with info_col:
        phase_col, type_col = st.columns(2)
        phase_col.metric("Current phase", "Project initiation")
        type_col.metric("Project type", str(field_value(record, "general_project_information", "project_type")))
    with action_col:
        st.page_link("app_pages/overview.py", label="Open project", icon=":material/arrow_forward:")

st.subheader("Key performance indicators")
st.caption(
    "KPI categories and goals as defined in Exhibit A of the Scope of Work. "
    "Per the SOW, these are finalized before contract execution and reviewed "
    "at the six-month business reviews in Q2 and Q4."
)
st.dataframe(
    pd.DataFrame(SOW_KPI_ROWS, columns=["KPI category", "Goal"]).astype(str),
    width="stretch",
    hide_index=True,
)

st.subheader("Required program reporting")
st.caption(
    "Metrics reported across the program, drawn from SOW reporting, project "
    "tracking, design fee reporting, and business review requirements."
)
st.dataframe(
    pd.DataFrame(
        REQUIRED_METRIC_ROWS,
        columns=["Report area", "Metric", "Source / cadence"],
    ).astype(str),
    width="stretch",
    hide_index=True,
)

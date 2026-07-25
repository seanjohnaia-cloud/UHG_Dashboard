import pandas as pd
import streamlit as st

from client_data import load_project
from project_home_dashboard import (
    COMPENSATION_BASIC_FEE_ROWS,
    COMPENSATION_REFERENCE_ROWS,
    SCHEDULE_EF_REFERENCE_ROWS,
    field_value,
    origin,
    render_table,
    row,
)

payload = load_project()
record = origin(payload)

st.title("Compensation")
st.caption(
    "Project compensation data from the LCD worksheet: basic service fee "
    "basis, design consultant compensation, supplemental services, "
    "reimbursables, and additional services."
)

sf_col, basis_col, routing_col, readiness_col = st.columns(4)
sf_col.metric("Project S.F.", str(field_value(record, "project_square_footage", "existing_sf")))
basis_col.metric(
    "Compensation basis",
    str(field_value(record, "general_project_information", "compensation_basis_anticipated")),
)
routing_col.metric("Current routing", "Schedule F")
readiness_col.metric("Fee status", "Open")

st.subheader("Project compensation data")
render_table(
    [
        row(record, "Project name", "general_project_information", "project_name"),
        ("Project start date", "To be confirmed", "linked from initial information"),
        row(record, "Project location", "general_project_information", "project_location"),
        ("Project / S.O. number", "Requested", "required before the Service Order package is complete"),
        row(record, "Project S.F.", "project_square_footage", "existing_sf"),
    ],
    columns=("Field", "Value", "LCD-W reference"),
)

st.subheader("Fee for basic services (architectural and interior design)")
st.dataframe(
    pd.DataFrame(
        COMPENSATION_BASIC_FEE_ROWS,
        columns=["Basis for compensation", "Feasibility stage", "SD thru DD", "CD thru closeout"],
    ).astype(str),
    width="stretch",
    hide_index=True,
)

consultants_col, services_col = st.columns(2)
with consultants_col:
    st.subheader("Design consultants compensation")
    render_table(
        [
            ("Mechanical", "Basis or amount to be confirmed", "consultant fee input"),
            ("Electrical", "Basis or amount to be confirmed", "consultant fee input"),
            ("Structural", "Basis or amount to be confirmed", "consultant fee input"),
            ("Civil (if required)", "To be confirmed", "supplemental / conditional"),
        ],
        columns=("Consultant", "Current value", "Status"),
    )
with services_col:
    st.subheader("Other compensation inputs")
    render_table(
        [
            ("Basic service exception", "None identified", "reviewed if an exception exists"),
            ("Supplemental consulting services", "None identified", "selected if required"),
            ("Additional services", "None identified", "selected if required"),
            ("Reimbursable expenses", "To be confirmed", "travel, permit fees, field office"),
        ],
        columns=("Input", "Current value", "Status"),
    )

st.subheader("Schedule E / F reference")
st.dataframe(
    pd.DataFrame(SCHEDULE_EF_REFERENCE_ROWS, columns=["Schedule", "Use", "Routing note"]).astype(str),
    width="stretch",
    hide_index=True,
)
st.dataframe(
    pd.DataFrame(
        COMPENSATION_REFERENCE_ROWS,
        columns=["Compensation category", "Reference", "Rule / note"],
    ).astype(str),
    width="stretch",
    hide_index=True,
)

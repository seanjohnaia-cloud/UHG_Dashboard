import pandas as pd
import streamlit as st

from client_data import load_project
from project_home_dashboard import field_value, origin

payload = load_project()
record = origin(payload)

st.title("Budget")
st.caption(
    "The approved-for-construction amount from the project record, compared "
    "against the estimates Grace submits at each design phase."
)

afc_col, basis_col = st.columns(2)
afc_col.metric("Approved for construction (AFC)", str(field_value(record, "budget", "original_cow")))
basis_col.metric(
    "Compensation basis",
    str(field_value(record, "general_project_information", "compensation_basis_anticipated")),
)

st.subheader("Phase estimates vs AFC")
st.caption(
    "Each phase estimate is recorded when submitted and compared against the "
    "AFC amount. Variances are flagged for review before the next phase begins."
)
estimate_rows = [
    ("Feasibility", "Not yet submitted", "—", "Pending"),
    ("Schematic design", "Not yet submitted", "—", "Pending"),
    ("Design development", "Not yet submitted", "—", "Pending"),
    ("Construction documents", "Not yet submitted", "—", "Pending"),
]
st.dataframe(
    pd.DataFrame(
        estimate_rows,
        columns=["Phase", "Grace estimate", "Variance vs AFC", "Status"],
    ),
    width="stretch",
    hide_index=True,
)

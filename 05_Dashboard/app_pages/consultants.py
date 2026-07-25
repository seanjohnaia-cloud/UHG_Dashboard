import streamlit as st

from client_data import load_project
from project_home_dashboard import field_value, origin, render_table

payload = load_project()
record = origin(payload)

st.title("Consultants")
st.caption("Design consultants engaged under basic services, and project representation.")

render_table(
    [
        (
            "Mechanical / electrical / structural",
            field_value(record, "design_consultants_basic_services", "mechanical_electrical_structural"),
            "Basic services — engaged by the Architect",
        ),
        (
            "Architect's project representative",
            "To be assigned",
            "Required before the Service Order package is complete",
        ),
    ],
    columns=("Role", "Current value", "Status"),
)

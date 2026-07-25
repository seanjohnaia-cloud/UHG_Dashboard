import streamlit as st

from client_data import load_project
from project_home_dashboard import (
    field_value,
    origin,
    render_table,
    row,
    square_footage_rows,
    sustainability_rows,
)

payload = load_project()
record = origin(payload)

st.title("Scope")
st.write(field_value(record, "scope_description", "scope_narrative"))

render_table(
    [
        row(record, "Project type", "general_project_information", "project_type"),
        row(record, "Asset type", "general_project_information", "asset_type"),
    ],
    columns=("Field", "Value", "LCD-W reference"),
)

sf_col, sustainability_col = st.columns(2)
with sf_col:
    st.subheader("Square footage")
    render_table(square_footage_rows(record), columns=("Field", "Value", "LCD-W reference"))
with sustainability_col:
    st.subheader("Sustainability objectives")
    render_table(sustainability_rows(record), columns=("Field", "Value", "LCD-W reference"))

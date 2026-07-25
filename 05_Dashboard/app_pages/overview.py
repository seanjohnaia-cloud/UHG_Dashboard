import pandas as pd
import streamlit as st

from client_data import load_project
from project_home_dashboard import (
    field_value,
    general_information_rows,
    open_items,
    origin,
)

payload = load_project()
record = origin(payload)

name = field_value(record, "general_project_information", "project_name")
location = field_value(record, "general_project_information", "project_location")
project_type = field_value(record, "general_project_information", "project_type")
asset = field_value(record, "general_project_information", "asset_type")

st.title(str(name))
st.caption(f"{location} · {asset} · {project_type}")

items = open_items(payload)

phase_col, items_col, sf_col, completion_col = st.columns(4)
phase_col.metric("Current phase", "Project initiation")
items_col.metric("Open items", len(items))
sf_col.metric("Existing S.F.", str(field_value(record, "project_square_footage", "existing_sf")))
completion_col.metric(
    "Substantial completion",
    str(field_value(record, "initial_schedule", "substantial_completion")),
)

scope = field_value(record, "scope_description", "scope_narrative")
cow = field_value(record, "budget", "original_cow")
construction = field_value(record, "initial_schedule", "commencement_of_construction")
substantial = field_value(record, "initial_schedule", "substantial_completion")
occupancy = field_value(record, "initial_schedule", "estimated_occupancy_date")

asset_text = str(asset).lower()
asset_article = "an" if asset_text[:1] in "aeiou" else "a"

with st.container(border=True):
    st.markdown(":material/history_edu: **Current statement of understanding**")
    st.write(
        f"{name} is {asset_article} {asset_text} {str(project_type).lower()} at {location}. "
        f"{scope} The Owner-provided cost of work is {cow}. Construction is "
        f"anticipated to commence {construction}, reach substantial completion "
        f"{substantial}, with estimated occupancy {occupancy}."
    )
    st.caption(
        "Generated from the current project record. Open items below identify "
        "information still required before the Service Order package is complete."
    )

st.subheader("Open items")
if items:
    st.dataframe(
        pd.DataFrame(items).astype(str),
        width="stretch",
        hide_index=True,
    )
else:
    st.success("No open items on the current record.")

st.subheader("General information")
st.dataframe(
    pd.DataFrame(general_information_rows(record), columns=["Field", "Value", "LCD-W reference"]).astype(str),
    width="stretch",
    hide_index=True,
)

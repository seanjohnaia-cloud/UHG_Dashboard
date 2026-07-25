import pandas as pd
import streamlit as st

from client_data import load_project
from project_home_dashboard import (
    DESIGN_SCHEDULE_PHASES,
    SLA_REFERENCE_ROWS,
    field_value,
    origin,
    row,
)

payload = load_project()
record = origin(payload)

st.title("Design schedule")
st.warning("The design schedule must be created before the Service Order package is complete.")

phases_col, milestones_col = st.columns(2)
phases_col.metric("Phases", len(DESIGN_SCHEDULE_PHASES))
milestones_col.metric("Milestones", sum(len(items) for items in DESIGN_SCHEDULE_PHASES.values()))

st.subheader("Schedule anchors")
anchor_rows = [
    row(record, "Construction commencement", "initial_schedule", "commencement_of_construction"),
    row(record, "Substantial completion", "initial_schedule", "substantial_completion"),
    (
        "Estimated occupancy",
        field_value(record, "initial_schedule", "estimated_occupancy_date"),
        "—",
    ),
    ("Design milestone delivery dates", "To be established", "Design schedule"),
]
st.dataframe(
    pd.DataFrame(anchor_rows, columns=["Schedule item", "Value", "LCD-W reference"]).astype(str),
    width="stretch",
    hide_index=True,
)

st.subheader("Project flow")
st.caption("Milestones by phase; durations and delivery dates fill in as the schedule is established.")
for phase, milestones in DESIGN_SCHEDULE_PHASES.items():
    with st.expander(f"{phase} ({len(milestones)} milestones)"):
        flow_rows = [(milestone, "—", "—", "—") for milestone in milestones]
        st.dataframe(
            pd.DataFrame(
                flow_rows,
                columns=["Design milestone", "Duration (days)", "Actual delivery date", "Revision"],
            ),
            width="stretch",
            hide_index=True,
        )

st.subheader("Service level agreement reference")
st.caption("Agreed timeframe expectations by project type.")
st.dataframe(
    pd.DataFrame(
        SLA_REFERENCE_ROWS,
        columns=["Phase", "New location / relocation", "Remodel / expansion", "Refresh / infrastructure"],
    ).astype(str),
    width="stretch",
    hide_index=True,
)
st.info(
    "Per the SLA: incomplete data, untimely additions, or untimely approvals "
    "may extend the schedule."
)

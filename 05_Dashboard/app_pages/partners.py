import pandas as pd
import streamlit as st

from client_data import load_project
from project_home_dashboard import (
    OWNER_CONSULTANT_OPTIONS,
    field_value,
    included_alliance_partner_defaults,
    origin,
)

payload = load_project()
record = origin(payload)

st.title("Alliance partners")
st.caption(
    "Nationally contracted UHG companies and representatives coordinated on "
    "this project, from page 2 of the LCD worksheet."
)

rep_col, pm_col = st.columns(2)
with rep_col:
    with st.container(border=True):
        st.markdown(":material/badge: **UHG Design Experience regional representative**")
        st.write(str(field_value(record, "general_project_information", "uhg_design_experience_representative")))
with pm_col:
    with st.container(border=True):
        st.markdown(":material/badge: **UHG regional project management representative**")
        st.write(str(field_value(record, "general_project_information", "uhg_project_management_representative")))

st.subheader("Owner's consultants and contractors")
included = included_alliance_partner_defaults(record)
partner_rows = [
    {
        "Partner": partner,
        "On this project": "Included" if partner in included else "—",
    }
    for partner in OWNER_CONSULTANT_OPTIONS
]
st.dataframe(
    pd.DataFrame(partner_rows).astype(str),
    width="stretch",
    hide_index=True,
)

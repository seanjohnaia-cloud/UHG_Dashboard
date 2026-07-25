import pandas as pd
import streamlit as st

from client_data import load_project
from project_home_dashboard import manual_lcd_entry_rows, origin

payload = load_project()
record = origin(payload)

st.title("Project data")
st.caption(
    "The complete LCD worksheet record for this project, shown read-only. "
    "Status reflects how each value entered the record."
)

frame = pd.DataFrame(manual_lcd_entry_rows(record))
frame = frame[["Section", "LCD Field", "Source Default", "Source State", "LCD-W / Service Order Reference"]]
frame.columns = ["Section", "Field", "Value", "Status", "LCD-W reference"]
frame["Value"] = frame["Value"].replace("", "—")

for section in frame["Section"].unique():
    st.subheader(str(section))
    section_frame = frame.loc[frame["Section"] == section, ["Field", "Value", "Status", "LCD-W reference"]]
    st.dataframe(section_frame.astype(str), width="stretch", hide_index=True)

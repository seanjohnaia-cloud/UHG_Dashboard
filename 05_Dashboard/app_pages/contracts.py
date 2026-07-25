import streamlit as st

from client_data import load_project
from project_home_dashboard import (
    CONTRACT_DOCUMENT_ROWS,
    render_contract_document_preview,
    render_table,
    source_path,
)

payload = load_project()

st.title("Contracts")
st.caption(
    "The governing contract layer: Master Agreement, current Scope of Work, "
    "and the executed Service Order once received."
)

ma_col, sow_col, so_col = st.columns(3)
ma_col.metric("Master Agreement", "Available")
sow_col.metric("Scope of Work", "Available")
so_col.metric("Executed Service Order", "Pending")

st.subheader("Contract documents")
ROLE_CAPTIONS = {
    "Executed Service Order": "Filed here once received and executed.",
}
selected_document = st.session_state.get("contract_document_open")
for document_row in CONTRACT_DOCUMENT_ROWS:
    path = source_path(document_row["Path"]) if document_row["Path"] else None
    available = document_row["Status"] == "Available" and path is not None and path.exists()
    name_col, status_col, role_col, action_col = st.columns([1.15, 0.55, 2.1, 1.0], vertical_alignment="center")
    name_col.markdown(f"**{document_row['Document']}**")
    status_col.markdown(document_row["Status"])
    role_col.caption(ROLE_CAPTIONS.get(document_row["Document"], document_row["Role"]))
    if action_col.button(
        document_row["Action"],
        key=f"open_contract_{document_row['Document'].lower().replace(' ', '_')}",
        disabled=not available,
    ):
        selected_document = document_row["Document"]
        st.session_state["contract_document_open"] = selected_document

if selected_document:
    selected_row = next(
        (document_row for document_row in CONTRACT_DOCUMENT_ROWS if document_row["Document"] == selected_document),
        None,
    )
    if selected_row:
        render_contract_document_preview(selected_row)

st.subheader("Contract layer impacts")
st.caption("How changes to the governing documents flow through the project views.")
render_table(
    [
        ("Project scope", "Changes require SOW comparison and PM approval", "Scope"),
        ("Compensation", "Changes may alter Schedule E/F routing or fee basis", "Compensation"),
        ("Design schedule", "Changes may add or remove milestone obligations", "Design schedule"),
        ("Consultants", "Changes may add consultant requirements", "Consultants / Alliance partners"),
        ("Service Order", "The executed SO is the project-specific contract container", "Contracts"),
    ],
    columns=("Area", "Impact rule", "Affected page"),
)

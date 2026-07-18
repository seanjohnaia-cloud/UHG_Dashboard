"""Activation Gate Dashboard v0.

Streamlit proof-of-concept for the approved Activation Gate Conditions.

Design principle: build the override / Decision Record flow first. A blocked
Activation gate can only become an override when the required Decision Record
fields are complete. Overrides produce `startup_ready_with_recorded_risk`, not a
clean-green state.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Literal

import pandas as pd
import streamlit as st

GateStatus = Literal["unassessed", "confirmed", "blocked"]
StartupState = Literal[
    "startup_ready",
    "startup_ready_with_recorded_risk",
    "startup_blocked",
    "startup_unassessed",
]

REQUIRED_DECISION_FIELDS = (
    "accountable_human",
    "rationale",
    "accepted_risk",
    "mitigation_follow_up",
    "decision_date",
    "source_evidence",
)

APP_DIR = Path(__file__).resolve().parent
MUNCIE_TEST_RUN_PATH = APP_DIR / "test_runs" / "muncie_activation_gate_test_run.json"


@dataclass(frozen=True)
class ActivationGate:
    gate_id: str
    condition: str
    source_signal: str
    confirmation: str
    default_result: str
    override_routing: str


GATES: list[ActivationGate] = [
    ActivationGate(
        "A-GATE-001",
        "Acceptance status known",
        "PAC 9.2 Acceptance Block",
        "Confirm proposal/approval instrument shows approved, pending, revision required, or not approved",
        "Blocks if unknown",
        "Override requires Decision Record; no Startup should proceed with unknown acceptance unless explicitly authorized.",
    ),
    ActivationGate(
        "A-GATE-002",
        "Acceptance authority confirmed",
        "PAC 9.3 Authorization Confirmation Status",
        "Confirm signer/approver had authority under client and firm process",
        "Blocks if unconfirmed",
        "UHG failure mode: apparent movement without confirmed authority. Override becomes Framework B risk signal.",
    ),
    ActivationGate(
        "A-GATE-003",
        "NTP / equivalent authorization event confirmed",
        "Acceptance Block + client communication",
        "Written NTP, approved proposal, executed agreement, Service Order, PO, or other accepted authorization path",
        "Blocks if absent",
        "Exact acceptable instrument may vary by client/project; override must state accepted authorization basis.",
    ),
    ActivationGate(
        "A-GATE-004",
        "Project ownership assigned",
        "PAC project identity + internal routing",
        "PIC/PM/accountable owner assigned for Activation",
        "Blocks if unassigned",
        "This is not full staffing; it establishes accountable ownership before downstream team assembly.",
    ),
    ActivationGate(
        "A-GATE-005",
        "Project number / activation identifier created or provisional identifier approved",
        "PAC project name/client/location",
        "Internal project number, activation record, or approved provisional identifier exists",
        "Blocks if neither created nor provisionally approved",
        "Override must state why work may proceed without final identifier and how tracking/billing will be protected.",
    ),
    ActivationGate(
        "A-GATE-006",
        "Scope baseline sufficient for startup or explicitly qualified",
        "PAC 4.1 Project Description + 4.4 Scope Clarity Status",
        "Confirm scope clarity is sufficient, or unresolved gaps are named and accepted",
        "Blocks if insufficient/unassessed",
        "Override records accepted scope ambiguity and required follow-up.",
    ),
    ActivationGate(
        "A-GATE-007",
        "Fee basis approved and aligned with authorization instrument",
        "PAC 6.1 Professional Fee + 6.2 Fee Breakdown",
        "Confirm approved fee basis matches acceptance/NTP/Service Order/PO or other authorization",
        "Blocks if unapproved/misaligned",
        "Critical for fee-reduction or scope-revision situations; override must name authorized approver.",
    ),
    ActivationGate(
        "A-GATE-008",
        "Schedule baseline acknowledged and confidence classified",
        "PAC 7.1 Schedule + 7.2 Schedule Confidence",
        "Confirm schedule status: contractual, illustrative, preliminary, owner-dependent, or incomplete",
        "Blocks if unassessed",
        "Override records schedule uncertainty and downstream impact.",
    ),
    ActivationGate(
        "A-GATE-009",
        "Required contract path identified",
        "PAC 8.1 Form of Agreement",
        "Confirm AIA / owner form / MSA / Service Order / custom path / pending legal form",
        "Blocks if unidentified",
        "Prevents work beginning under wrong contractual assumption.",
    ),
    ActivationGate(
        "A-GATE-010",
        "Insurance / risk requirement reviewed for startup relevance",
        "PAC 8.2 Insurance Requirements",
        "Confirm requirements are stated, not applicable, or risk-reviewed if incomplete",
        "Blocks if relevant and unreviewed",
        "Especially important for public, institutional, clinical, or special-risk work.",
    ),
    ActivationGate(
        "A-GATE-011",
        "Unresolved consultant / additional-service triggers acknowledged and routed",
        "PAC 5.2 Additional Services + 5.3 Programming + 5.4 Record Drawings",
        "Identify any consultant/additional-service signals and route to Section B responsibility mapping before they are dropped",
        "Blocks if triggers are present and unrouted",
        "PAC signals need; Section B assigns parties/responsibilities. Override records accepted coordination risk.",
    ),
    ActivationGate(
        "A-GATE-012",
        "Billing path viable",
        "PAC 6.4 Billing Schedule",
        "Confirm billing schedule or approved provisional billing logic sufficient for setup",
        "Blocks if unassessed/insufficient",
        "Override must state how accounting/project setup can proceed without full billing clarity.",
    ),
    ActivationGate(
        "A-GATE-013",
        "All gate conditions evaluated",
        "Activation gate table",
        "Confirm no gate condition remains unassessed",
        "Blocks if any condition is unassessed",
        "Readiness flags are aggregate T-output, not a gate condition.",
    ),
    ActivationGate(
        "A-GATE-014",
        "Approval-path governance satisfied",
        "Firm constitutional/process layer",
        "Confirm required internal approval path was followed",
        "Blocks if unsatisfied",
        "Inherited governance/process knowledge; open dependency logged in Pending Constitutional Item - Firm Approval Path Governance.md.",
    ),
]


def blank_decision_record(gate_id: str) -> dict[str, str]:
    return {
        "gate_id": gate_id,
        "accountable_human": "",
        "rationale": "",
        "accepted_risk": "",
        "mitigation_follow_up": "",
        "decision_date": date.today().isoformat(),
        "source_evidence": "",
    }


def decision_record_complete(record: dict[str, str]) -> bool:
    return all(str(record.get(field, "")).strip() for field in REQUIRED_DECISION_FIELDS)


def evaluate_startup_state(statuses: dict[str, GateStatus], overrides: dict[str, dict[str, str]]) -> StartupState:
    """Return the approved startup state for current gate statuses/overrides."""
    if any(statuses.get(gate.gate_id, "unassessed") == "unassessed" for gate in GATES):
        return "startup_unassessed"

    blocked_gate_ids = [gate.gate_id for gate in GATES if statuses.get(gate.gate_id) == "blocked"]
    incomplete_blocks = [
        gate_id
        for gate_id in blocked_gate_ids
        if not decision_record_complete(overrides.get(gate_id, blank_decision_record(gate_id)))
    ]
    if incomplete_blocks:
        return "startup_blocked"
    if blocked_gate_ids:
        return "startup_ready_with_recorded_risk"
    return "startup_ready"


def state_label(state: StartupState) -> tuple[str, str]:
    labels = {
        "startup_ready": ("Startup Ready", "✅"),
        "startup_ready_with_recorded_risk": ("Startup Ready With Recorded Risk", "⚠️"),
        "startup_blocked": ("Startup Blocked", "🛑"),
        "startup_unassessed": ("Startup Unassessed / Incomplete", "◻️"),
    }
    return labels[state]


def gate_status_label(status: GateStatus, override_complete: bool = False) -> str:
    if status == "confirmed":
        return "✅ Confirmed"
    if status == "blocked" and override_complete:
        return "⚠️ Overridden / recorded risk"
    if status == "blocked":
        return "🛑 Blocked"
    return "◻️ Unassessed"


def gate_action(status: GateStatus, override_complete: bool = False) -> str:
    if status == "confirmed":
        return "No action needed for Startup gate."
    if status == "blocked" and override_complete:
        return "Proceed only as recorded-risk startup; Decision Record must remain linked."
    if status == "blocked":
        return "Resolve the condition, or record an accountable override Decision Record."
    return "Assess this gate before Startup can be evaluated."


def initialize_state() -> None:
    if "gate_statuses" not in st.session_state:
        st.session_state.gate_statuses = {gate.gate_id: "unassessed" for gate in GATES}
    if "gate_evidence" not in st.session_state:
        st.session_state.gate_evidence = {gate.gate_id: "" for gate in GATES}
    if "decision_records" not in st.session_state:
        st.session_state.decision_records = {}
    if "loaded_test_run" not in st.session_state:
        st.session_state.loaded_test_run = "Manual"
    if "project_info" not in st.session_state:
        st.session_state.project_info = {}


def load_test_run(path: Path) -> dict:
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def apply_test_run(test_run: dict) -> None:
    gate_data = test_run.get("gates", {})
    st.session_state.gate_statuses = {
        gate.gate_id: gate_data.get(gate.gate_id, {}).get("status", "unassessed") for gate in GATES
    }
    st.session_state.gate_evidence = {
        gate.gate_id: gate_data.get(gate.gate_id, {}).get("evidence", "") for gate in GATES
    }
    for gate in GATES:
        st.session_state[f"status_{gate.gate_id}"] = st.session_state.gate_statuses[gate.gate_id]
        st.session_state[f"evidence_{gate.gate_id}"] = st.session_state.gate_evidence[gate.gate_id]
    st.session_state.decision_records = test_run.get("decision_records", {})
    st.session_state.project_info = test_run.get("project_info", {})
    st.session_state.loaded_test_run = test_run.get("project", path_label(test_run))


def path_label(test_run: dict) -> str:
    return test_run.get("use_case", "Loaded test run")


def render_sidebar() -> None:
    st.sidebar.header("Test Runs")
    st.sidebar.caption("Load a preserved project specimen into the dashboard.")
    if st.sidebar.button("Load Muncie UC-001 test run"):
        apply_test_run(load_test_run(MUNCIE_TEST_RUN_PATH))
    st.sidebar.write(f"Loaded: {st.session_state.loaded_test_run}")


def render_project_context() -> None:
    info = st.session_state.project_info
    st.subheader("Project Snapshot")
    if not info:
        st.info("No project specimen loaded yet. Use the sidebar to load Muncie UC-001.")
        return

    left, right = st.columns(2)
    left.markdown(f"**Project name:** {info.get('project_name', 'unknown')}")
    left.markdown(f"**Project number:** {info.get('project_number', 'unknown')}")
    left.markdown(f"**Client:** {info.get('client', 'unknown')}")
    left.markdown(f"**Location:** {info.get('location', 'unknown')}")
    right.markdown(f"**Request type:** {info.get('request_type', 'unknown')}")
    right.markdown(f"**Workflow position:** {info.get('workflow_position', 'unknown')}")
    right.markdown(f"**Contract path:** {info.get('contract_path', 'unknown')}")
    right.markdown(f"**Authority posture:** {info.get('current_authority_posture', 'unknown')}")

    fee_a, fee_b = st.columns(2)
    fee_a.metric("Proposed Fee", info.get("proposed_fee", "unknown"))
    fee_b.metric("Contract Comparison", info.get("contract_comparison_fee", "unknown"))


def render_gate_frame() -> None:
    st.subheader("What the gates are for")
    st.write(
        "These gates do **not** decide whether a fee proposal can be studied. "
        "They decide whether the project is allowed and organized to move into Startup."
    )
    st.info(
        "Read this as: can Grace start the project now, or is startup blocked until authority, authorization, scope, fee, schedule, and routing conditions are confirmed?"
    )
    st.markdown(
        "**Status meanings:** `confirmed` = condition is satisfied; `blocked` = startup cannot proceed unless an accountable person records an override; `unassessed` = we do not know yet."
    )


def render_decision_record_form(gate: ActivationGate) -> None:
    records: dict[str, dict[str, str]] = st.session_state.decision_records
    record = records.get(gate.gate_id, blank_decision_record(gate.gate_id))

    with st.expander(f"Override Decision Record — {gate.gate_id}", expanded=False):
        st.warning(
            "This gate blocks by default. Proceeding requires a complete Decision Record; "
            "the resulting state is recorded risk, not clean green."
        )
        record["accountable_human"] = st.text_input(
            "Accountable human", value=record["accountable_human"], key=f"{gate.gate_id}_human"
        )
        record["rationale"] = st.text_area(
            "Rationale", value=record["rationale"], key=f"{gate.gate_id}_rationale"
        )
        record["accepted_risk"] = st.text_area(
            "Accepted risk", value=record["accepted_risk"], key=f"{gate.gate_id}_risk"
        )
        record["mitigation_follow_up"] = st.text_area(
            "Mitigation / follow-up", value=record["mitigation_follow_up"], key=f"{gate.gate_id}_mitigation"
        )
        decision_day = st.date_input(
            "Decision date", value=date.fromisoformat(record["decision_date"]), key=f"{gate.gate_id}_date"
        )
        record["decision_date"] = decision_day.isoformat()
        record["source_evidence"] = st.text_area(
            "Source / evidence", value=record["source_evidence"], key=f"{gate.gate_id}_evidence"
        )
        records[gate.gate_id] = record

        if decision_record_complete(record):
            st.success("Decision Record complete — override can be counted as recorded risk.")
        else:
            st.error("Decision Record incomplete — gate remains blocking.")


def render_dashboard() -> None:
    st.set_page_config(page_title="Activation Gate Dashboard v0", layout="wide")
    initialize_state()
    render_sidebar()

    st.title("Activation Gate Dashboard v0")
    st.caption("Approved requirement: Activation Gate Conditions. Implementation test: override flow first.")

    render_project_context()
    st.divider()
    render_gate_frame()

    statuses: dict[str, GateStatus] = st.session_state.gate_statuses
    overrides: dict[str, dict[str, str]] = st.session_state.decision_records
    startup_state = evaluate_startup_state(statuses, overrides)
    label, icon = state_label(startup_state)

    st.subheader("Startup Readiness Summary")
    metric_cols = st.columns(4)
    assessed_count = sum(1 for gate in GATES if statuses[gate.gate_id] != "unassessed")
    blocked_count = sum(1 for gate in GATES if statuses[gate.gate_id] == "blocked")
    override_count = sum(
        1
        for gate in GATES
        if statuses[gate.gate_id] == "blocked"
        and decision_record_complete(overrides.get(gate.gate_id, blank_decision_record(gate.gate_id)))
    )
    metric_cols[0].metric("Startup State", f"{icon} {label}")
    metric_cols[1].metric("Gates Assessed", f"{assessed_count}/14")
    metric_cols[2].metric("Blocked Gates", blocked_count)
    metric_cols[3].metric("Recorded Overrides", override_count)

    if startup_state == "startup_blocked":
        st.warning(
            "Startup is blocked. This does not mean the fee proposal work was invalid; it means the project is not yet authorized/organized for Startup."
        )
    elif startup_state == "startup_ready_with_recorded_risk":
        st.warning("Startup may proceed only with recorded risk: at least one blocking gate was overridden by Decision Record.")

    st.divider()

    st.subheader("Gate Review")
    st.caption("One row per gate: title → status → why → action. Click a gate to see details or record an override.")

    gate_rows = []
    for gate in GATES:
        override_complete = decision_record_complete(overrides.get(gate.gate_id, blank_decision_record(gate.gate_id)))
        status_label = gate_status_label(statuses[gate.gate_id], override_complete)
        title = f"{gate.gate_id} — {gate.condition} — {status_label}"
        with st.expander(title, expanded=statuses[gate.gate_id] == "blocked" and gate.gate_id == "A-GATE-002"):
            top_left, top_right = st.columns([2, 1])
            top_left.markdown(f"**What this gate checks:** {gate.confirmation}")
            top_left.caption(f"Source/signal: {gate.source_signal}")
            selected_status = top_right.selectbox(
                "Status",
                options=["unassessed", "confirmed", "blocked"],
                index=["unassessed", "confirmed", "blocked"].index(statuses[gate.gate_id]),
                key=f"status_{gate.gate_id}",
            )
            statuses[gate.gate_id] = selected_status
            st.session_state.gate_evidence[gate.gate_id] = st.text_area(
                "Why / evidence",
                value=st.session_state.gate_evidence[gate.gate_id],
                key=f"evidence_{gate.gate_id}",
                height=80,
            )
            st.markdown(f"**Action:** {gate_action(selected_status, override_complete)}")
            if selected_status == "blocked":
                render_decision_record_form(gate)

        gate_rows.append(
            {
                "Gate": gate.gate_id,
                "Title": gate.condition,
                "Status": gate_status_label(statuses[gate.gate_id], override_complete),
                "Action": gate_action(statuses[gate.gate_id], override_complete),
            }
        )

    st.divider()
    st.subheader("Gate Index")
    st.caption("Compact index only — the detailed review is above.")
    st.dataframe(pd.DataFrame(gate_rows), width="stretch", hide_index=True)

    st.subheader("Framework B Signal Lane")
    signal_rows = [
        {
            "Gate": gate.gate_id,
            "Condition": gate.condition,
            "Signal": "Override / accepted risk / deviation",
            "Decision Date": overrides.get(gate.gate_id, {}).get("decision_date", ""),
            "Accountable Human": overrides.get(gate.gate_id, {}).get("accountable_human", ""),
        }
        for gate in GATES
        if statuses[gate.gate_id] == "blocked"
        and decision_record_complete(overrides.get(gate.gate_id, blank_decision_record(gate.gate_id)))
    ]
    if signal_rows:
        st.dataframe(pd.DataFrame(signal_rows), width="stretch", hide_index=True)
    else:
        st.caption("No Framework B override signals yet.")


if __name__ == "__main__":
    render_dashboard()

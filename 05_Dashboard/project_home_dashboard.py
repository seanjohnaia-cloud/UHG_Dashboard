"""Project Home / Pii prototype.

LCD-style project front door for a persistent project intelligence cockpit. The
view reads a source-extracted Fairview fixture and keeps three ideas separate:
PAC / Origin, Pii context reconstruction, and UHG Service Order review.
"""

from __future__ import annotations

import json
import html
import base64
from pathlib import Path
from typing import Any

import pandas as pd
import streamlit as st

APP_DIR = Path(__file__).resolve().parent
FAIRVIEW_FIXTURE_PATH = APP_DIR / "test_runs" / "fairview_project_home_fixture.json"
GRACE_LOGO_PATH = APP_DIR / "assets" / "grace_stacked_logo.jpg"

NAV_ITEMS = [
    "Home",
    "LCD Manual Entry",
    "Project Scope",
    "Project Budget",
    "Compensation",
    "Design Schedule",
    "Consultants",
    "Alliance Partners",
    "Contracts",
    "Metrics",
    "Service Order Review",
]

DESIGN_SCHEDULE_PHASES = {
    "Project Initiation": [
        "Project Kick-off",
        "Scope Review/Clarification",
        "Budget Review/Clarification",
        "Supplemental and/or Additional Services",
        "Design Schedule",
        "Site Visit?",
        "Proposed Compensation",
        "Service Order Submittal Date",
        "Service Order Approval Date",
    ],
    "Site Planning Services": [
        "Project Kick-off",
        "Document Verification",
        "Proposed Compensation",
        "Service Order Submittal Date",
        "Service Order Approval Date",
        "Design Documentation",
        "Architectural/Preliminary Plan Submittal Date",
        "Architectural/Preliminary Plan Approval Date",
    ],
    "Feasibility Stage Services": [
        "Feasibility Kick-off",
        "Feasibility Scope Interview",
        "Preliminary Program",
        "Scenario Development",
        "Utilization Analysis",
        "Feasibility Phase Submittal Date",
        "Feasibility Phase Approval Date",
    ],
    "Schematic Design": [
        "Site Due Diligence Report",
        "Field Measurement",
        "Program Summary Document",
        "Preliminary Code Review",
        "Preliminary Floor Plan",
        "Preliminary Floor Plan Approval",
        "Schematic Design Documents",
        "Peer Design Review 1",
        "Design Exceptions",
        "Budget Review/Clarification",
        "SD Phase Submittal Date",
        "SD Phase Approval Date",
    ],
    "Design Development": [
        "DD Documents",
        "Specifications",
        "MEP Narrative",
        "Owner Progress Review 1",
        "Peer Design Review 2",
        "Owner Progress Review 2",
        "QA/QC Review 1",
        "Owner Progress Review 3",
        "Owner Consultant Coordination",
        "Design Exceptions (noted or Approved)",
        "Budget Review/Clarification",
        "DD Phase Submittal Date",
        "DD Phase Approval Date",
    ],
    "Construction Documents": [
        "Construction Documents",
        "Specifications",
        "Owner's Consultant's Work (Incorporation)",
        "Life Safety Plan",
        "50% CD Package Review Meeting (ground up Projects Only)",
        "90% CD Package Review Meeting (as determined by Owner)",
        "Final Cost of Work Adjustments",
        "Preparation of Bidding Information (w/DE)",
        "Clash Detection",
        "Final Code Review",
        "QA/QC Review 2",
        "Final Pick-ups",
        "CD Phase Submittal Date",
        "CD Phase Approval Date",
    ],
    "Bidding and Permitting Phase": [
        "Bid Time",
        "Permit Submittal",
        "Permit Review/Response",
        "Permit Received",
        "Bid Date",
        "Actual Bid Date",
        "Contract Negotiations",
    ],
    "Construction / Completion": [
        "Construction Start Date",
        "Actual Construction Start Date",
        "Substantial Completion",
        "Actual Substantial Completion Date",
        "Final Payment",
        "Warranty Period",
        "Warranty Period Conference",
        "Project Completion Date",
    ],
}

SLA_REFERENCE_ROWS = [
    ("Project Kick-off", "1", "1", "1"),
    ("Scope Review", "1–5", "1", "1"),
    ("Scenario Development", "5–10", "5–10", "5"),
    ("Utilization Analyses", "2–10", "2–5", "1–2"),
    ("Site Due Diligence", "5–10", "5", "5"),
    ("Detailed Programming", "5", "5", "5"),
    ("Preliminary Floor Plan / Schematic Design Documents", "5–10", "5–10", "5"),
    ("Design Development Phase", "15", "10–15", "5–10"),
    ("Construction Docs", "15–20", "15–20", "15"),
    ("Permitting / Bidding", "15–20", "15", "15"),
]

COMPENSATION_BASIC_FEE_ROWS = [
    ("Stipulated Sum", "Enter Amount", "Enter Amount", "Enter Amount"),
    ("Percentage Basis", "N/A", "Enter %", "Enter Percentage"),
    ("Other", "Enter N.T.E.", "Enter N.T.E.", "Enter Amount N.T.E."),
]

SCHEDULE_EF_REFERENCE_ROWS = [
    ("Schedule E", "New Site, Expansion, Large Renovation, and Relocation Fees", ">= 10,000 SF or percentage-basis routing"),
    ("Schedule F", "Small Remodels, Contraction, or Split Relocation Project Fees", "< 10,000 SF affected area; price per SF by project type/size"),
]

COMPENSATION_REFERENCE_ROWS = [
    ("(None)", "Schedule E", "If < 10,000 S.F."),
    ("Feasibility Stage", "Schedule F", "If < 10,000 S.F."),
    ("Architectural Site Plan", "Percentage Fee", "Compensation category"),
    ("Preliminary Site Plan", "Stipulated Fee", "Compensation category"),
    ("One-off", "Negotiated Fee", "Compensation category"),
]

CONTRACT_DOCUMENT_ROWS = [
    (
        "Master Agreement",
        "Available",
        "00_Source/Contract/Executed Agreement Package/original/master agreement.pdf",
        "Governing contract layer",
    ),
    (
        "Scope of Work Document",
        "Available",
        "00_Source/Contract/Exhibit A - Scope of Work/Exhibit A-Scope of Work.docx",
        "Current SOW basis; subject to periodic replacement/update",
    ),
    (
        "Service Order Template",
        "Available",
        "00_Source/Contract/Executed Agreement Package/original/Exhibit B-Service Order DRAFT AIA B221-2018.docx",
        "Template / Contracts output structure",
    ),
    (
        "Executed Service Order",
        "Not received",
        "Pending project-specific executed SO",
        "Must be attached when received; Contracts creates final SO",
    ),
]

SOW_UPDATE_ABSORPTION_STEPS = [
    ("1. Preserve", "Store the newly received SOW as a source artifact; never overwrite prior SOW."),
    ("2. Compare", "Diff new SOW against current SOW and Project Home assumptions."),
    ("3. Classify", "Tag impacts to scope, compensation, design schedule, consultants, SLA/KPI, and Service Order readiness."),
    ("4. Reconcile", "Produce a modification summary with source-backed before/after changes."),
    ("5. Approve", "PM reviews and approves absorption before Pii treats the updated SOW as current context."),
    ("6. Propagate", "Update Project Home, Compensation, Design Schedule, and Service Order Review gaps only after approval."),
]

SERVICE_ORDER_ARTICLES = {
    "Article 1 — Initial Information": [
        ("Service Order No.", "Provided by CBRE PM", "Missing / request"),
        ("Service Order Date", "Use date of Project Engagement Meeting", "TBD"),
        ("Owner", "United HealthCare Services, Inc.", "Template value"),
        ("Architect", "Grace Healthcare Studios entity", "Verify state/legal entity"),
        ("Project Name / Location", "From Initial Information", "Available / review"),
        ("Project Description", "From Initial Information; refine in Project Initiation", "Needs review"),
        ("Master Agreement Dated", "B121 dates", "Contract reference"),
        ("Attachments", "Project Scope Document; Project Design Schedule", "Required"),
        ("Sustainable Objective / Certification", "From Initial Information / select", "TBD"),
        ("Owner's Consultants", "Select list", "TBD"),
    ],
    "Article 2 — Services Under This Service Order": [
        ("Basic Services Consultants", "MEP & Structural plus selected consultants", "TBD"),
        ("Basic Services Exceptions", "Feasibility / SD-DD / CD-Closeout exceptions", "None or list"),
        ("Supplemental and Additional Services", "Responsibility by Architect / Owner / Not Provided", "TBD"),
        ("Supplemental Services", "3D scanning, field measurement, civil, landscape, MEP, OPR, commissioning, sustainability, historic, specialty, POE", "Select/review"),
        ("Other Supplemental Services", "List other services", "TBD"),
        ("CA Beyond Exhibit A Limits", "Additional Services note", "Needs decision"),
    ],
    "Article 3 — Date of Commencement and Substantial Completion": [
        ("Commencement of Construction Date", "From Initial Information", "Available / review"),
        ("Substantial Completion Date", "From Initial Information", "Available / review"),
    ],
    "Article 4 — Compensation": [
        ("Compensation Basis", "Per Exhibits E & F of B121", "Review"),
        ("Feasibility Phase", "Stipulated sum / percentage / other", "TBD"),
        ("SD thru DD", "Stipulated sum / percentage / other", "TBD"),
        ("DD thru Closeout", "Stipulated sum / percentage / other", "TBD"),
        ("Additional Services", "Attachment X — Additional Services and/or Reimbursables", "TBD"),
        ("Reimbursable Expenses", "Attachment X — Additional Services and/or Reimbursables", "TBD"),
        ("Section 4.4", "Needs editing — percentages do not equal 100%", "Open"),
    ],
    "Article 5 — Insurance": [
        ("Insurance", "Per B121 Master Agreement", "Confirm / COI gap"),
    ],
    "Article 6 — Party Representatives": [
        ("UHG Design Experience Regional Representative", "From Initial Information", "Available / review"),
        ("UHG Regional Project Management Representative", "From Initial Information", "Available / review"),
        ("Architect Project Management Representative", "From Initial Information", "Available / review"),
        ("Architect's Project Representative", "Select", "Missing"),
    ],
    "Article 7 — Attachments and Exhibits": [
        ("Attachment X", "Project Scope Document", "Required"),
        ("Attachment X", "Project Design Schedule", "Required"),
        ("Attachment X", "Additional Services and/or Reimbursable Expenses", "If applicable"),
        ("Other Documents", "TBD", "Open"),
    ],
}

SOW_KPI_ROWS = [
    (
        "Project Delivery Timeliness",
        "Deliver projects on or ahead of project schedule with % of projects delivered on time or early based on UHG MBO.",
    ),
    ("Client Satisfaction", "Achieve Net Promoter Score (NPS) satisfaction based on UHG MBO"),
    ("Design Quality & Innovation", "Maintain high design standards with limited RFIs or rework"),
    (
        "Regulatory Compliance",
        "Submit permits on time with minimal feedback (not more than one round of clarifications) on 98% or more of assigned projects.",
    ),
    (
        "Cost Alignment",
        "Stay within approved construction budgets, with less than 3% variance between DD and CD milestones per project",
    ),
    ("Change Order Frequency", "Minimize frequency of post-approval change orders <2% per project."),
]

REQUIRED_METRIC_ROWS = [
    ("Ongoing Performance Monitoring", "Pipeline, volume, and key initiatives", "SOW Reporting 1.0 / monthly reports"),
    ("Ongoing Performance Monitoring", "Performance against established KPI's", "SOW Reporting 1.0"),
    ("Ongoing Performance Monitoring", "Project tracking system compliance and data integrity", "SOW Reporting 1.0"),
    ("Ongoing Performance Monitoring", "Consistency of Project Authorization forms", "SOW Reporting 1.0"),
    ("Ongoing Performance Monitoring", "Comparative performance analysis and improvement recommendations", "SOW Reporting 1.0"),
    ("Project Tracking Reporting", "Total number of requests and projects handled", "SOW Reporting 2.0"),
    ("Project Tracking Reporting", "Percentage of requests that met expected response times", "SOW Reporting 2.0"),
    ("Project Tracking Reporting", "Project name", "SOW Reporting 2.0 / Project Tracking Report"),
    ("Project Tracking Reporting", "Brief description", "SOW Reporting 2.0"),
    ("Project Tracking Reporting", "Percentage of Existing Conditions / walls reused per project", "SOW Reporting 2.0 / Project Tracking Report"),
    ("Project Tracking Reporting", "Scheduled Project phases", "SOW Reporting 2.0 / Design Schedule"),
    ("Project Tracking Reporting", "Project order and installation status", "SOW Reporting 2.0"),
    ("Project Tracking Reporting", "Quote requested, received dates and approval status", "SOW Reporting 2.0"),
    ("Project Tracking Reporting", "Potential project risk and proposed mitigation strategies", "SOW Reporting 2.0 / Project Tracking Report"),
    ("Project Tracking Reporting", "Project team leader and contact point", "SOW Reporting 2.0 / Project Tracking Report"),
    ("Project Tracking Reporting", "Number of Staff and percentage of time spent on Owner's account", "SOW Reporting 2.0 / Project Tracking Report"),
    ("Project Tracking Reporting", "Deficiency report", "SOW Reporting 2.0 / Project Tracking Report"),
    ("Project Tracking Reporting", "Delivered according to agreed-upon schedule and budget at final funding milestone", "SOW Reporting 2.0 / Project Tracking Report"),
    ("Project Tracking Reporting", "Cost Savings and applied strategies for cost savings", "SOW Reporting 2.0 / Project Tracking Report"),
    ("Project Tracking Reporting", "Schedule reduction (savings)", "SOW Reporting 2.0 / Project Tracking Report"),
    ("Project Tracking Reporting", "Architectural and MEP coordination issues / misses", "SOW Reporting 2.0 / Project Tracking Report"),
    ("Project Tracking Reporting", "Number of Change Orders per project", "SOW Reporting 2.0 / Project Tracking Report"),
    ("Project Tracking Reporting", "Number of RFIs per project, broken down by type", "SOW Reporting 2.0 / Project Tracking Report"),
    ("Design Fee Reporting", "Architectural and consultant fees inclusive of reimbursables and additional services", "SOW Design Fee Reporting"),
    ("Design Fee Reporting", "Proposed / budgeted fees compared to actual costs", "SOW Design Fee Reporting"),
    ("Business Reviews", "Cost-saving initiatives and resulting savings", "SOW Business Reviews / QBR"),
    ("Business Reviews", "Quarterly project summary including project risks", "SOW Business Reviews / QBR"),
    ("Business Reviews", "Sustainability initiatives implemented on projects", "SOW Business Reviews / QBR"),
    ("Business Reviews", "Pilot initiatives implemented on projects", "SOW Business Reviews / QBR"),
    ("Business Reviews", "Lessons Learned discovered during last quarter", "SOW Business Reviews / QBR"),
    ("Business Reviews", "SLA and performance measures related to Agreement terms", "SOW Business Reviews / QBR"),
    ("Business Reviews", "Annual goals, plans, prior-year performance, Owner satisfaction surveys, and executive summary", "SOW Business Reviews / annual report"),
]

METRIC_GAUGE_ROWS = [
    ("Schedule Health", "Project Delivery Timeliness + SLA schedule fields", "Future gauge derived from required metrics"),
    ("Delivery Quality", "Design Quality & Innovation + deficiencies/RFIs/rework", "Future gauge derived from required metrics"),
    ("Budget / Fee Health", "Cost Alignment + design fee reporting + budget delivery", "Future gauge derived from required metrics"),
    ("Construction Responsiveness", "Change Order Frequency + RFIs/RFCs/addenda/review letters", "Future gauge derived from required metrics"),
]

METRIC_LOGGING_SECTIONS = {
    "Current Project Status": [
        ("Current Phase", "Select", "Project Tracking Report entry"),
        ("Issue(s)", "Deficiency Report", "Per-phase issue logging"),
        ("Completion %", "Consult with Project Leader", "Gauge input"),
        ("Completion Date", "From Design Schedule", "Schedule Health input"),
        ("At Risk", "Select", "Risk gauge input"),
    ],
    "Project Tracking per Phase": [
        ("Design Milestone Date", "From Design Schedule", "Contract/SOW schedule obligation"),
        ("Submittal Date", "Manual or source log", "Delivery performance input"),
        ("Submittal Attempts", "Manual Entry", "Review churn / quality input"),
        ("Approval Date", "Manual or source log", "Approval cycle input"),
        ("Approval Deficiencies", "Manual Entry from Deficiency Report", "Quality input"),
        ("No. of Staff", "Phase Close-out Data", "Resourcing input"),
        ("% Time spent on account", "Phase Close-out Data", "Efficiency input"),
    ],
    "Existing Conditions / Reuse": [
        ("Existing conditions reused", "Requested Data", "Scope / sustainability / renovation intelligence"),
        ("Project delivered on budget", "Manual Entry", "Budget gauge input"),
    ],
    "Bidding and Permitting Log": [
        ("Number of RFIs", "Manual Entry / future log", "Procurement responsiveness"),
        ("Coordination Issues", "Manual Entry / future log", "Risk and quality signal"),
        ("Number of Addenda", "Manual Entry / future log", "Document completeness signal"),
        ("Permitting Duration", "Manual Entry", "Schedule impact"),
        ("Review/Response Letters", "Manual Entry", "AHJ / stakeholder response tracking"),
    ],
    "Construction Phase Log": [
        ("Number of RFIs", "Manual Entry / future log", "Contract administration workload"),
        ("Number of RFCs", "Manual Entry / future log", "Change pressure"),
        ("Number of Change Orders", "Manual Entry / future log", "Budget/scope impact"),
    ],
    "Risk / Deficiency / Savings": [
        ("Potential Project Risk and proposed Mitigation Strategies", "Per Phase", "Risk gauge/detail source"),
        ("Deficiency Report", "Per Phase", "Quality gauge/detail source"),
        ("Schedule reduction (savings)", "Per Phase", "Schedule value signal"),
        ("Cost Savings and applied strategies", "Per Phase", "Cost value signal"),
    ],
    "Fee / Revision Tracking": [
        ("Original Design Fees", "Manual Entry from approved Service Order", "Baseline fee"),
        ("Approved Revisions", "Document Revisions", "Revision/change history"),
        ("Final Design Fees", "Manual Entry", "Final fee outcome"),
    ],
}

METRIC_CONTRACT_ALIGNMENT_ROWS = [
    ("Project status / phase tracking", "SOW lines 171–173", "Account team tracks and reports progress from proposal request through deficiency resolution and closeout."),
    ("SLA / KPI basis", "SOW lines 133–135", "SOW states SLAs and KPIs are intended to improve workplace functionality, comfort, and standards alignment."),
    ("Design schedule and milestone performance", "SOW lines 189–190, 269–279", "Architect submits schedule, updates Design Schedule monthly, and Design Milestone Dates are obligations."),
    ("RFI / submittal / construction response logging", "SOW lines 901–909, 931–959", "Repository, submittal/RFI review, written responses, and no unreasonable schedule delay."),
    ("Change request / change order logging", "SOW lines 963–979", "Change requests, change orders, compensation/schedule changes, and written approval must be tracked."),
    ("Deficiency report", "SOW lines 1011–1037", "Completed project data points and deficiency report fields are contract-backed."),
    ("Fees and approved revisions", "SOW lines 1063–1065", "Additional compensation requires written change-in-service terms and adjustment to compensation/schedule."),
]

TableRows = list[tuple[str, Any, str]]
OriginRecord = dict[str, dict[str, dict[str, Any]]]

MANUAL_LCD_DISABLED_COLUMNS = [
    "Section",
    "LCD Field",
    "Source Default",
    "Source State",
    "LCD-W / Service Order Reference",
]

MANUAL_LCD_FIELD_DEFINITIONS = [
    ("General Project Information", "Project Name", "general_project_information", "project_name"),
    ("General Project Information", "Project Start Date", None, None),
    ("General Project Information", "Project Location", "general_project_information", "project_location"),
    ("General Project Information", "Project Number", None, None),
    ("General Project Information", "Project Group", None, None),
    ("General Project Information", "Project Manager", None, None),
    ("General Project Information", "Project Type", "general_project_information", "project_type"),
    ("General Project Information", "Project Leader", None, None),
    ("General Project Information", "Special Type", "general_project_information", "asset_type"),
    (
        "General Project Information",
        "UHG DE Regional Rep.",
        "general_project_information",
        "uhg_design_experience_representative",
    ),
    (
        "General Project Information",
        "Compensation",
        "general_project_information",
        "compensation_basis_anticipated",
    ),
    (
        "General Project Information",
        "UHG Regional PM Rep.",
        "general_project_information",
        "uhg_project_management_representative",
    ),
    ("Project Scope", "Scope Narrative", "scope_description", "scope_narrative"),
    ("Project S.F.", "Existing S.F.", "project_square_footage", "existing_sf"),
    ("Project S.F.", "% of Existing", None, None),
    ("Project S.F.", "New S.F.", "project_square_footage", "new_sf"),
    ("Project S.F.", "Conditions Reused", "project_square_footage", "existing_conditions_reused"),
    ("Sustainability", "Certification Req'd.", None, None),
    ("Sustainability", "Sustainable Objective", "sustainability", "sustainable_objective"),
    ("Project Budget", "Original COW", "budget", "original_cow"),
    ("Project Budget", "DD COW", None, None),
    ("Project Budget", "CD COW", None, None),
    ("Project Budget", "Bid Amount", None, None),
    ("Project Budget", "Final COW", None, None),
    ("Design Schedule", "Project Start Date", None, None),
    ("Design Schedule", "Design Start Date", None, None),
    ("Design Schedule", "Design Completion Date", None, None),
    ("Design Schedule", "Construction Start Date", "initial_schedule", "commencement_of_construction"),
    ("Design Schedule", "Substantial Completion Date", "initial_schedule", "substantial_completion"),
    ("Design Schedule", "Estimated Occupancy", "initial_schedule", "estimated_occupancy_date"),
    (
        "Consultants",
        "Mechanical / Electrical / Structural",
        "design_consultants_basic_services",
        "mechanical_electrical_structural",
    ),
    ("Consultants", "Architect's Project Representative", None, None),
    ("Alliance Partners", "Owner-retained Consultants", "owner_consultants", "owner_retained_consultants"),
]

PROJECT_MANAGER_OPTIONS = ["Andrea Bowman, AIA", "Sean Johnson, AIA"]
PROJECT_LEADER_OPTIONS = ["Justin Aubert, AIA"]
PROJECT_GROUP_OPTIONS = ["Administrative", "Clinical"]
PROJECT_TYPE_OPTIONS = [
    "Consolidation",
    "Contraction",
    "Expansion",
    "New Site",
    "Ground Up",
    "Tenant Build-out",
    "Remodel/Renovation",
    "Relocation",
    "Split-Relocation",
]
SPECIAL_TYPE_OPTIONS = [
    "(None)",
    "Feasibility Stage",
    "Architectural Site Plan",
    "Preliminary Site Plan",
    "One-off",
    "Infrastructure/MDF",
    "Refresh",
]
COMPENSATION_OPTIONS = ["(Schedule E)", "(Schedule F)", "Percentage Fee", "Stipulated Fee", "Negotiated Fee"]
PHASE_OPTIONS = [
    "Project Initiation",
    "FS -Kick-off",
    "FS_Scope Interview",
    "FS-Preliminary Program",
    "FS-Scenario Development",
    "FS-Utilization Analysis",
    "Schematic Design",
    "Design Development",
    "Construction Documents",
    "Bidding/Permitting",
    "Construction Administration",
    "Project Close-out",
    "Post Occupancy",
    "Warranty Period",
]
OWNER_CONSULTANT_OPTIONS = [
    "Furniture",
    "Flooring",
    "Sound Masking",
    "Artwork/Branding",
    "Security (Owner internal and Business teams)",
    "Audio Visual",
    "Signage",
    "Medical Equipment",
    "IT/Technology/Low Voltage (Owner internal and Business teams)",
    "Storefront Systems",
    "Food Service",
]
YES_NO_NA_OPTIONS = ["N/A", "Yes", "No"]
AT_RISK_OPTIONS = ["High", "Moderate", "Low"]

CONTROLLED_LCD_OPTIONS = {
    "Project Group": PROJECT_GROUP_OPTIONS,
    "Project Manager": PROJECT_MANAGER_OPTIONS,
    "Project Type": PROJECT_TYPE_OPTIONS,
    "Project Leader": PROJECT_LEADER_OPTIONS,
    "Special Type": SPECIAL_TYPE_OPTIONS,
    "Compensation": COMPENSATION_OPTIONS,
    "Certification Req'd.": YES_NO_NA_OPTIONS,
    "Current Phase": PHASE_OPTIONS,
    "At Risk": AT_RISK_OPTIONS,
}
MULTI_SELECT_LCD_FIELDS = {"Owner-retained Consultants": OWNER_CONSULTANT_OPTIONS}


def load_fixture(path: Path = FAIRVIEW_FIXTURE_PATH) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def image_data_uri(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/jpeg;base64,{encoded}"


def origin(payload: dict[str, Any]) -> OriginRecord:
    return payload["origin_record"]


def field_value(record: OriginRecord, section: str, field: str, default: str = "—") -> Any:
    return record.get(section, {}).get(field, {}).get("value", default)


def field_ref(record: OriginRecord, section: str, field: str, default: str = "—") -> Any:
    return record.get(section, {}).get(field, {}).get("lcdw_reference") or default


def row(record: OriginRecord, label: str, section: str, field: str) -> tuple[str, Any, str]:
    return label, field_value(record, section, field), field_ref(record, section, field)


def manual_lcd_entry_rows(record: OriginRecord) -> list[dict[str, Any]]:
    """Build the editable LCD intake grid, pre-populated from the PDD origin record."""
    rows: list[dict[str, Any]] = []
    for section, label, source_section, source_field in MANUAL_LCD_FIELD_DEFINITIONS:
        if source_section and source_field:
            source_payload = record.get(source_section, {}).get(source_field, {})
            source_default = source_payload.get("value", "")
            source_state = source_payload.get("truth_state", "source gap")
            reference = source_payload.get("lcdw_reference") or "No LCD-W home / review schema"
        else:
            source_default = ""
            source_state = "manual required"
            reference = "Manual LCD entry"

        rows.append(
            {
                "Section": section,
                "LCD Field": label,
                "Manual Entry": source_default,
                "Source Default": source_default,
                "Source State": source_state,
                "LCD-W / Service Order Reference": reference,
                "Entry Notes": "",
            }
        )
    return rows


def manual_lcd_entry_frame(record: OriginRecord) -> pd.DataFrame:
    return pd.DataFrame(manual_lcd_entry_rows(record))


def manual_lcd_entry_by_field(record: OriginRecord) -> dict[str, dict[str, Any]]:
    return {row["LCD Field"]: row for row in manual_lcd_entry_rows(record)}


def manual_lcd_widget_key(field: str) -> str:
    return "lcd_manual_" + "".join(character.lower() if character.isalnum() else "_" for character in field)


def controlled_options(field: str, current_value: str = "") -> list[str]:
    options = ["", *CONTROLLED_LCD_OPTIONS.get(field, [])]
    if current_value and current_value not in options:
        options.append(current_value)
    return options


def source_label(value: Any) -> str:
    return str(value) if value not in (None, "") else "manual entry"


def render_table(rows: TableRows, columns: tuple[str, str, str] = ("Field", "Value", "State")) -> None:
    frame = pd.DataFrame(rows, columns=list(columns)).astype(str)
    st.dataframe(frame, width="stretch", hide_index=True)


def collect_fields(record: OriginRecord) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for section, fields in record.items():
        for field, payload in fields.items():
            rows.append(
                {
                    "Section": section.replace("_", " ").title(),
                    "Field": field.replace("_", " ").title(),
                    "Value": payload.get("value", "—"),
                    "Truth State": payload.get("truth_state", "unknown"),
                    "LCD-W / Service Order Reference": payload.get("lcdw_reference")
                    or "No LCD-W home",
                }
            )
    return rows


def open_items(payload: dict[str, Any]) -> list[dict[str, str]]:
    return [
        {
            "Field": item.get("field", "").replace("_", " ").title(),
            "Status": item.get("status", "unknown"),
            "Reason": item.get("reason", ""),
        }
        for item in payload.get("open_items", [])
    ]


def no_lcdw_home(payload: dict[str, Any]) -> list[dict[str, str]]:
    return [
        {
            "Field": item.get("field", "").replace("_", " ").title(),
            "Value": str(item.get("value", "")),
            "Truth State": item.get("truth_state", "unknown"),
        }
        for item in payload.get("not_currently_captured_in_lcdw", [])
    ]


def reconstructed_context(payload: dict[str, Any]) -> str:
    record = origin(payload)
    name = field_value(record, "general_project_information", "project_name")
    location = field_value(record, "general_project_information", "project_location")
    project_type = field_value(record, "general_project_information", "project_type")
    asset = field_value(record, "general_project_information", "asset_type")
    scope = field_value(record, "scope_description", "scope_narrative")
    cow = field_value(record, "budget", "original_cow")
    construction = field_value(record, "initial_schedule", "commencement_of_construction")
    substantial = field_value(record, "initial_schedule", "substantial_completion")
    occupancy = field_value(record, "initial_schedule", "estimated_occupancy_date")

    return (
        f"{name} is a fictional UHG {asset} {project_type} at {location}. "
        f"The preserved PDD describes {scope} The Owner-provided cost of work is {cow}. "
        f"Initial schedule context shows construction commencement on {construction}, "
        f"substantial completion on {substantial}, and estimated occupancy on {occupancy}. "
        "The record is strong enough for PAC / Origin absorption, but Service Order "
        "readiness still has genuine open items: existing conditions confirmation, "
        "certificate of insurance, and the Architect's project representative."
    )


def general_information_rows(record: OriginRecord) -> TableRows:
    return [
        row(record, "Project Name", "general_project_information", "project_name"),
        ("Project Start Date", "TBD / from Grace PAC start", "Project start rule"),
        row(record, "Project Location", "general_project_information", "project_location"),
        ("Project Number", "Must be requested", "LCD-W / Service Order downstream"),
        ("Project Group", "Select", "Controlled list / page 2 reference"),
        ("Project Manager", "Select", "Controlled list / page 2 reference"),
        row(record, "Project Type", "general_project_information", "project_type"),
        ("Project Leader", "Select", "Controlled list / page 2 reference"),
        row(record, "Special Type", "general_project_information", "asset_type"),
        row(
            record,
            "UHG DE Regional Rep.",
            "general_project_information",
            "uhg_design_experience_representative",
        ),
        row(record, "Compensation", "general_project_information", "compensation_basis_anticipated"),
        row(
            record,
            "UHG Regional PM Rep.",
            "general_project_information",
            "uhg_project_management_representative",
        ),
    ]


def square_footage_rows(record: OriginRecord) -> TableRows:
    return [
        row(record, "Existing S.F.", "project_square_footage", "existing_sf"),
        ("% of Existing", "TBD", "calculated / requested data"),
        row(record, "New S.F.", "project_square_footage", "new_sf"),
        (
            "Conditions Reused",
            field_value(record, "project_square_footage", "existing_conditions_reused"),
            "Deferred / site due diligence",
        ),
    ]


def sustainability_rows(record: OriginRecord) -> TableRows:
    return [
        ("Certification Req'd.", "Select / N/A", "Controlled value"),
        row(record, "Sustainable Objective", "sustainability", "sustainable_objective"),
    ]


def budget_rows(record: OriginRecord) -> TableRows:
    return [
        row(record, "Original COW", "budget", "original_cow"),
        ("DD COW", "TBD", "downstream update"),
        ("CD COW", "TBD", "downstream update"),
        ("Bid Amount", "TBD", "downstream update"),
        ("Final COW", "TBD", "downstream update"),
    ]


def schedule_summary_rows(record: OriginRecord) -> TableRows:
    return [
        ("Project Start Date", "TBD / PAC start", "Grace PAC"),
        ("Design Start Date", "Date of Purchase Order / TBD", "required for design schedule"),
        ("Design Completion Date", "Missing — create Design Schedule", "from Design Schedule"),
        row(record, "Construction Start Date", "initial_schedule", "commencement_of_construction"),
        row(record, "Substantial Completion Date", "initial_schedule", "substantial_completion"),
    ]


def basic_consultant_rows() -> TableRows:
    return [
        ("Mechanical", "Architect to engage", "Basic Services"),
        ("Electrical", "Architect to engage", "Basic Services"),
        ("Structural", "Architect to engage", "Basic Services"),
        ("Architect's Project Representative", "Missing", "Required for SO review"),
    ]


def render_header(payload: dict[str, Any], page: str) -> None:
    record = origin(payload)
    chips = [
        "PAC / Origin Ready",
        "Pre-Service-Order Mode",
        "Design Schedule Required",
        "Service Order Gaps Open",
    ]
    status_cells = "".join(
        f'<div class="pii-band-cell"><div class="pii-band-label">{label}</div><div class="pii-band-value">{value}</div></div>'
        for label, value, _state in current_project_status_rows(payload)
    )

    st.markdown(
        f"""
        <style>
            .stApp {{background: #d9d9d9;}}
            [data-testid="stHeader"] {{background: #8bd34b !important;}}
            .block-container {{padding: 16rem 14.25rem 1rem 1rem;}}
            [data-testid="stDeployButton"] {{display: none;}}
            [data-testid="collapsedControl"], [data-testid="stSidebarCollapseButton"] {{display: flex !important; visibility: visible !important; opacity: 1 !important; z-index: 100000 !important;}}
            [data-testid="stSidebar"] {{z-index: 99999 !important; width: 13rem !important; min-width: 13rem !important; background: #08b5dc !important;}}
            [data-testid="stSidebar"] > div {{width: 13rem !important; min-width: 13rem !important;}}
            [data-testid="stSidebar"] section, [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {{background: #08b5dc !important;}}
            [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {{gap: .65rem;}}
            [data-testid="stSidebar"] label {{font-size: 1.05rem !important; color: #111827 !important;}}
            [data-testid="stSidebar"] label:has(input:checked) {{background: #020617 !important; color: white !important; margin-left: -1rem; margin-right: -1rem; padding: .55rem 1rem;}}
            [data-testid="stSidebar"] label:has(input:checked) * {{color: white !important;}}
            .pii-green-cap {{position: fixed; top: 0; left: 0; right: 0; height: 15.25rem; background: #8bd34b; z-index: 99990;}}
            .pii-top-band {{position: fixed; top: 3.6rem; left: 13rem; right: 13rem; z-index: 99991; background: #8bd34b; border: 0; border-radius: 0; padding: .45rem .65rem .5rem .65rem; margin: 0;}}
            .pii-band-grid {{display: grid; grid-template-columns: 1fr; gap: .55rem; align-items: stretch;}}
            .pii-band-logo {{display: none;}}
            .pii-band-logo-main {{font-size: 1.45rem; font-weight: 800; line-height: 1.45rem; color: #102a43;}}
            .pii-band-logo-sub {{font-size: .68rem; color: #486581; margin-top: .15rem;}}
            .pii-sheet-title {{font-size: 1.25rem; font-weight: 800; line-height: 1.35rem; margin: 0; color: #102a43;}}
            .pii-caption {{font-size: .68rem; color: #486581; margin: 0 0 .12rem 0;}}
            .pii-band-row {{display: grid; gap: .25rem; margin-top: .18rem;}}
            .pii-band-project {{grid-template-columns: 1.35fr 2.2fr .9fr .9fr .65fr .65fr;}}
            .pii-band-status {{grid-template-columns: .9fr 1.45fr .65fr .9fr .6fr .65fr;}}
            .pii-band-cell {{background: rgba(255,255,255,.48); border: 1px solid rgba(2, 6, 23, .16); border-radius: .3rem; padding: .12rem .32rem; min-height: 1.48rem;}}
            .pii-band-label {{font-size: .53rem; line-height: .62rem; color: rgba(2, 6, 23, .7); text-transform: uppercase; letter-spacing: .035em;}}
            .pii-band-value {{font-size: .73rem; line-height: .85rem; font-weight: 650; color: #102a43;}}
            .pii-chipline {{font-size: .64rem; color: rgba(2, 6, 23, .78); margin-top: .16rem;}}
            .grace-logo-box {{height: 15.25rem; display: flex; align-items: center; justify-content: center; border-bottom: 1px solid rgba(2, 6, 23, .35); margin: 0 0 1.4rem 0; padding: 1rem 0;}}
            .grace-logo-img {{display: block; width: 8.5rem; max-width: 90%; height: auto; object-fit: contain; mix-blend-mode: multiply;}}
            .pii-sidebar-loaded {{border-bottom: 1px solid rgba(2, 6, 23, .35); padding-bottom: 1rem; margin-bottom: 1.1rem; color: #111827;}}
            .pii-sidebar-loaded-title {{font-size: .98rem; line-height: 1.55rem;}}
            .pii-sidebar-loaded-caption {{font-size: .82rem; line-height: 1.15rem; color: rgba(2, 6, 23, .65); margin-top: .8rem;}}
            .pii-right-rail {{position: fixed; top: 15.25rem; right: 0; width: 13rem; height: calc(100vh - 15.25rem); overflow-y: auto; z-index: 99998; background: #08b5dc; border-left: 1px solid rgba(0, 0, 0, .18); border-top: 1px solid rgba(2, 6, 23, .35); padding: 2.4rem 1rem 1rem 1rem; font-family: "Source Sans Pro", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color: #020617;}}
            .pii-right-title {{font-size: 1.55rem; line-height: 1.9rem; font-weight: 500; color: #020617; margin: 0 0 2rem 0;}}
            .pii-right-caption {{font-size: .95rem; line-height: 1.25rem; color: rgba(2, 6, 23, .72); margin-bottom: 1rem;}}
            .pii-pending-item {{border-top: 1px solid rgba(2, 6, 23, .2); padding: .65rem 0 .65rem 1.65rem; position: relative;}}
            .pii-pending-item::before {{content: ""; position: absolute; left: .15rem; top: .86rem; width: .9rem; height: .9rem; border-radius: 50%; background: #f4f7fb; border: 1px solid rgba(2, 6, 23, .28);}}
            .pii-pending-item[open]::before {{background: #ef4444; box-shadow: inset 0 0 0 .28rem #f4f7fb;}}
            .pii-pending-item summary {{cursor: pointer; font-size: .98rem; font-weight: 600; color: #020617; line-height: 1.25rem; list-style: none;}}
            .pii-pending-item summary::-webkit-details-marker {{display: none;}}
            .pii-pending-detail {{font-size: .86rem; line-height: 1.18rem; color: rgba(2, 6, 23, .72); margin: .42rem 0 0 .15rem;}}
            .pii-side-metrics {{position: relative; margin-top: 2rem; display: grid; grid-template-columns: 1fr 1fr; gap: .8rem; align-items: end;}}
            .pii-side-metric-label {{font-size: 1.15rem; color: #020617; margin-bottom: .45rem;}}
            .pii-gauge {{width: 5.35rem; height: 5.35rem; border-radius: 50%; background: #1d6982; border: .42rem solid #102a43;}}
            .pii-sidebar-metric {{position: fixed; left: 1.1rem; bottom: 1rem; z-index: 100000;}}
            .pii-terminal-screen {{background: #000; border: .18rem solid #14532d; border-radius: 3.2rem; min-height: 68vh; padding: 2.3rem 2.65rem; box-shadow: inset 0 0 34px rgba(56, 189, 248, .1); color: #38bdf8; font-family: "Cascadia Code", "Consolas", "Courier New", monospace;}}
            .pii-terminal-title {{font-size: 1.15rem; letter-spacing: .08em; text-transform: uppercase; color: #7dd3fc; margin-bottom: 1.15rem;}}
            .pii-terminal-prompt {{font-size: 1.18rem; line-height: 1.62rem; color: #38bdf8; margin-bottom: 1.35rem;}}
            .pii-terminal-list {{margin: 0; padding-left: 1.1rem;}}
            .pii-terminal-list li {{font-size: 1rem; line-height: 1.55rem; color: #60a5fa; margin: .45rem 0;}}
        </style>
        <div class="pii-green-cap"></div>
        <div class="pii-top-band">
            <div class="pii-band-grid">
                <div class="pii-band-logo">
                    <div class="pii-band-logo-main">Grace</div>
                    <div class="pii-band-logo-sub">Logo placeholder</div>
                </div>
                <div>
                    <div class="pii-sheet-title">Pii / {page}</div>
                    <div class="pii-caption">Project Information</div>
                    <div class="pii-band-row pii-band-project">
                        <div class="pii-band-cell"><div class="pii-band-label">Project</div><div class="pii-band-value">{field_value(record, 'general_project_information', 'project_name')}</div></div>
                        <div class="pii-band-cell"><div class="pii-band-label">Location</div><div class="pii-band-value">{field_value(record, 'general_project_information', 'project_location')}</div></div>
                        <div class="pii-band-cell"><div class="pii-band-label">Type</div><div class="pii-band-value">{field_value(record, 'general_project_information', 'project_type')}</div></div>
                        <div class="pii-band-cell"><div class="pii-band-label">Asset</div><div class="pii-band-value">{field_value(record, 'general_project_information', 'asset_type')}</div></div>
                        <div class="pii-band-cell"><div class="pii-band-label">Existing SF</div><div class="pii-band-value">{field_value(record, 'project_square_footage', 'existing_sf')}</div></div>
                        <div class="pii-band-cell"><div class="pii-band-label">New SF</div><div class="pii-band-value">{field_value(record, 'project_square_footage', 'new_sf')}</div></div>
                    </div>
                    <div class="pii-caption" style="margin-top:.22rem;">Current Project Status</div>
                    <div class="pii-band-row pii-band-status">{status_cells}</div>
                    <div class="pii-chipline">{" · ".join(chips)}</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_ask_pii() -> None:
    prompt_items = "".join(
        f"<li>{html.escape(prompt)}</li>"
        for prompt in [
            "Reconstruct the current project context.",
            "What can Grace use now from PAC / Origin?",
            "What is missing for Service Order review?",
            "Show the source trail for the design schedule.",
        ]
    )
    st.markdown(
        f"""
        <div class="pii-terminal-screen">
            <div class="pii-terminal-title">Ask Pii / Project Dialogue</div>
            <div class="pii-terminal-prompt">Ask what is missing, what changed, what is contract-backed, or what must happen next.</div>
            <ul class="pii-terminal-list">{prompt_items}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


def pending_items() -> list[tuple[str, str]]:
    return [
        ("Next Meeting", "TBD — confirm project kickoff / phase check-in"),
        ("Design Schedule", "Due in Project Initiation; required before Service Order package is complete"),
        ("Certificate of Insurance", "Missing; required for Service Order readiness"),
        ("Architect's Project Representative", "Missing; required for Service Order Article 6"),
        ("Existing Conditions Reused", "Deferred; confirm during site due diligence"),
    ]


def render_pending_panel() -> None:
    st.subheader("Pending")
    st.caption("Current phase reminders, due dates, and open items.")
    for title, detail in pending_items():
        st.markdown(f"**{title}**  \n{detail}")


def render_pending_rail() -> None:
    items = "".join(
        "<details class=\"pii-pending-item\">"
        f"<summary>{html.escape(title)}</summary>"
        f"<div class=\"pii-pending-detail\">{html.escape(detail)}</div>"
        "</details>"
        for title, detail in pending_items()
    )
    st.markdown(
        f"""
        <aside class="pii-right-rail">
            <div class="pii-right-title">Pending Items:</div>
            <div class="pii-right-caption">Current phase reminders, due dates, and open items.</div>
            {items}
            <div class="pii-side-metrics">
                <div><div class="pii-side-metric-label">Metric 2</div><div class="pii-gauge"></div></div>
                <div><div class="pii-side-metric-label">Metric 3</div><div class="pii-gauge"></div></div>
            </div>
        </aside>
        """,
        unsafe_allow_html=True,
    )


def render_intelligence_snapshot(payload: dict[str, Any]) -> None:
    cols = st.columns(5)
    cols[0].metric("Origin Fields", len(collect_fields(origin(payload))))
    cols[1].metric("Open Items", len(open_items(payload)))
    cols[2].metric("No LCD-W Home", len(no_lcdw_home(payload)))
    cols[3].metric("Source Artifacts", 1)
    cols[4].metric("SO Readiness", "Open")


def current_project_status_rows(payload: dict[str, Any]) -> TableRows:
    return [
        ("Current Phase", "Project Initiation", "selected / phase tracking"),
        ("Issue(s)", "Design Schedule / SO readiness open", "quick-reference blocker"),
        ("Completion %", "TBD", "consult with Project Leader"),
        ("Completion Date", "From Design Schedule", "key milestone date source"),
        ("At Risk", "TBD", "select / PM review"),
        ("Actionable Items", len(open_items(payload)), "current open item count"),
    ]


def render_current_status_panel(payload: dict[str, Any]) -> None:
    cells = "".join(
        f'<div class="pii-strip-cell"><div class="pii-strip-label">{label}</div><div class="pii-strip-value">{value}</div></div>'
        for label, value, _state in current_project_status_rows(payload)
    )
    st.markdown(
        f"""
        <div class="pii-caption" style="font-weight:700;color:#344054;margin-top:.15rem;">Current Project Status</div>
        <div class="pii-strip pii-strip-6">{cells}</div>
        <div class="pii-chipline">Actionable now: create the Design Schedule; confirm COI; assign Architect's Project Representative.</div>
        """,
        unsafe_allow_html=True,
    )


def render_home(payload: dict[str, Any]) -> None:
    render_ask_pii()


def render_lcd_manual_entry(payload: dict[str, Any]) -> None:
    record = origin(payload)
    entries = manual_lcd_entry_by_field(record)

    st.markdown(
        """
        <style>
            .lcd-sheet-note {font-size: .86rem; color: #475467; margin: -.2rem 0 1rem 0;}
            .lcd-section-title {background: #d9ead3; border: 1px solid #2f3a27; color: #111827; font-weight: 800; padding: .28rem .45rem; margin: .6rem 0 .2rem 0;}
            .lcd-field-label {background: #eeeeee; border: 1px solid #7a7a7a; border-right: 0; min-height: 2.15rem; padding: .38rem .42rem; font-weight: 700; font-size: .82rem; color: #111827;}
            .lcd-phase-box {background: #f8fafc; border: 1px solid #7a7a7a; padding: .38rem .55rem; min-height: 2.1rem; font-size: .84rem;}
            .lcd-source-chip {font-size: .68rem; color: #667085; margin: -.35rem 0 .35rem 0; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;}
            .lcd-save-strip {background: #f2f4f7; border: 1px solid #98a2b3; padding: .55rem .7rem; margin-top: .8rem; font-size: .86rem;}
            div[data-testid="stTextInput"] input, div[data-testid="stTextArea"] textarea {border-radius: 0 !important; border: 1px solid #7a7a7a !important; background: #fff !important; color: #101828 !important; font-size: .86rem !important;}
            div[data-testid="stTextInput"], div[data-testid="stTextArea"], div[data-testid="stSelectbox"], div[data-testid="stMultiSelect"] {margin-bottom: .1rem;}
            div[data-testid="stSelectbox"] div[data-baseweb="select"] > div, div[data-testid="stMultiSelect"] div[data-baseweb="select"] > div {border-radius: 0 !important; border: 1px solid #7a7a7a !important; background: #fff !important; min-height: 2.35rem; font-size: .86rem !important;}
        </style>
        """,
        unsafe_allow_html=True,
    )

    def cell(field: str, *, area: bool = False, key_suffix: str = "") -> None:
        entry = entries[field]
        key = manual_lcd_widget_key(field if not key_suffix else f"{field}_{key_suffix}")
        current = str(entry["Manual Entry"] if entry["Manual Entry"] is not None else "")
        help_text = f"Source default: {entry['Source Default'] or 'manual required'} | {entry['Source State']} | {entry['LCD-W / Service Order Reference']}"
        if field in MULTI_SELECT_LCD_FIELDS:
            defaults = [] if current.lower().startswith("none identified") else [current] if current else []
            options = [*MULTI_SELECT_LCD_FIELDS[field], *[value for value in defaults if value not in MULTI_SELECT_LCD_FIELDS[field]]]
            st.multiselect(field, options, default=defaults, key=key, label_visibility="collapsed", help=help_text)
        elif field in CONTROLLED_LCD_OPTIONS:
            options = controlled_options(field, current)
            if key not in st.session_state:
                st.session_state[key] = current if current in options else ""
            st.selectbox(field, options, key=key, label_visibility="collapsed", help=help_text)
        elif area:
            if key not in st.session_state:
                st.session_state[key] = current
            st.text_area(field, key=key, height=130, label_visibility="collapsed", help=help_text)
        else:
            if key not in st.session_state:
                st.session_state[key] = current
            st.text_input(field, key=key, label_visibility="collapsed", help=help_text)

    def pair(label: str, field: str, *, key_suffix: str = "") -> None:
        st.markdown(f'<div class="lcd-field-label">{html.escape(label)}</div>', unsafe_allow_html=True)
        cell(field, key_suffix=key_suffix)
        source = entries[field]
        st.markdown(
            f'<div class="lcd-source-chip">{html.escape(source["Source State"])} · {html.escape(source_label(source["Source Default"]))}</div>',
            unsafe_allow_html=True,
        )

    st.subheader("Life Cycle Data Worksheet")
    st.markdown(
        '<div class="lcd-sheet-note">Excel-style LCD page entry surface. Click white cells to enter or revise project data; PDD defaults are pre-filled where available.</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="lcd-section-title">General Project Information</div>', unsafe_allow_html=True)
    cols = st.columns([1.1, 2.4, .95, 1.55], gap="small")
    with cols[0]:
        pair("Project Name:", "Project Name")
    with cols[1]:
        pair("Project Location:", "Project Location")
    with cols[2]:
        pair("Project Start Date:", "Project Start Date")
    with cols[3]:
        pair("Project Number:", "Project Number")

    cols = st.columns(4, gap="small")
    for column, (label, field) in zip(
        cols,
        [
            ("Project Group:", "Project Group"),
            ("Project Manager:", "Project Manager"),
            ("Project Type:", "Project Type"),
            ("Project Leader:", "Project Leader"),
        ],
    ):
        with column:
            pair(label, field)

    cols = st.columns(4, gap="small")
    for column, (label, field) in zip(
        cols,
        [
            ("Special Type:", "Special Type"),
            ("Compensation:", "Compensation"),
            ("UHG DE Regional Rep.:", "UHG DE Regional Rep."),
            ("UHG Regional PM Rep.:", "UHG Regional PM Rep."),
        ],
    ):
        with column:
            pair(label, field)

    st.markdown('<div class="lcd-section-title">Current Project Status</div>', unsafe_allow_html=True)
    cols = st.columns(5, gap="small")
    for column, (label, value, _state) in zip(cols, current_project_status_rows(payload)[:5]):
        with column:
            st.markdown(f'<div class="lcd-field-label">{html.escape(label)}:</div>', unsafe_allow_html=True)
            status_key = manual_lcd_widget_key(f"status_{label}")
            status_value = str(value)
            if label in CONTROLLED_LCD_OPTIONS:
                status_options = controlled_options(label, status_value)
                st.selectbox(label, status_options, index=status_options.index(status_value), label_visibility="collapsed", key=status_key)
            else:
                st.text_input(label, value=status_value, label_visibility="collapsed", key=status_key)

    left, right = st.columns([3, 1.1], gap="large")
    with left:
        st.markdown('<div class="lcd-section-title">Scope Description</div>', unsafe_allow_html=True)
        cell("Scope Narrative", area=True)

        sf_cols = st.columns(4, gap="small")
        with sf_cols[0]:
            pair("Existing (S.F.):", "Existing S.F.")
        with sf_cols[1]:
            pair("% of Existing", "% of Existing")
        with sf_cols[2]:
            pair("New (S.F.):", "New S.F.")
        with sf_cols[3]:
            pair("Conditions Reused:", "Conditions Reused")

        st.markdown('<div class="lcd-section-title">Project Sustainability Objectives</div>', unsafe_allow_html=True)
        sustain_cols = st.columns(2, gap="small")
        with sustain_cols[0]:
            pair("Certification Req'd.:", "Certification Req'd.")
        with sustain_cols[1]:
            pair("Sustainable Objective:", "Sustainable Objective")

        st.markdown('<div class="lcd-section-title">Budget (Cost of the Work)</div>', unsafe_allow_html=True)
        budget_cols = st.columns(5, gap="small")
        for column, (label, field) in zip(
            budget_cols,
            [
                ("Original COW:", "Original COW"),
                ("DD COW:", "DD COW"),
                ("CD COW:", "CD COW"),
                ("Bid Amount:", "Bid Amount"),
                ("Final COW:", "Final COW"),
            ],
        ):
            with column:
                pair(label, field)

        st.markdown('<div class="lcd-section-title">Project Schedule Information (Initial)</div>', unsafe_allow_html=True)
        schedule_cols = st.columns(5, gap="small")
        for column, (label, field) in zip(
            schedule_cols,
            [
                ("Project Start Date:", "Project Start Date"),
                ("Design Start Date:", "Design Start Date"),
                ("Design Completion Date:", "Design Completion Date"),
                ("Construction Start Date:", "Construction Start Date"),
                ("Substantial Completion Date:", "Substantial Completion Date"),
            ],
        ):
            with column:
                pair(label, field, key_suffix="schedule")

    with right:
        st.markdown('<div class="lcd-section-title">Phases</div>', unsafe_allow_html=True)
        for phase in [
            "Project Initiation",
            "FS - Kick-off",
            "Schematic Design",
            "Design Development",
            "Construction Documents",
            "Bidding/Permitting",
            "Construction Administration",
            "Project Close-out",
            "Post Occupancy",
            "Warranty Period",
        ]:
            st.markdown(f'<div class="lcd-phase-box">{html.escape(phase)}</div>', unsafe_allow_html=True)

        st.markdown('<div class="lcd-section-title">Owner\'s Consultants and Contractors</div>', unsafe_allow_html=True)
        pair("Owner-retained:", "Owner-retained Consultants")

    st.markdown(
        '<div class="lcd-save-strip">Draft entry mode: values are held in this dashboard session. Next build step is Save LCD Draft / Apply Dialogue Update into the same record path.</div>',
        unsafe_allow_html=True,
    )


def render_project_scope(payload: dict[str, Any]) -> None:
    record = origin(payload)
    st.subheader("Project Scope")
    st.write(field_value(record, "scope_description", "scope_narrative"))
    render_table(
        [
            row(record, "Project Type", "general_project_information", "project_type"),
            row(record, "Asset Type", "general_project_information", "asset_type"),
        ],
        columns=("Field", "Value", "Reference"),
    )

    sf_col, sustainability_col = st.columns(2)
    with sf_col:
        st.subheader("Project S.F.")
        render_table(square_footage_rows(record))
    with sustainability_col:
        st.subheader("Project Sustainability Objectives")
        render_table(sustainability_rows(record))


def render_project_budget(payload: dict[str, Any]) -> None:
    record = origin(payload)
    st.subheader("Project Budget")
    cols = st.columns(2)
    cols[0].metric("Original Cost of Work", field_value(record, "budget", "original_cow"))
    cols[1].metric(
        "Compensation Basis",
        field_value(record, "general_project_information", "compensation_basis_anticipated"),
    )
    st.info(
        "Fee Proposal is a generated view: it should read Origin + classification + "
        "Exhibit E/F routing, not collect data again."
    )


def render_compensation(payload: dict[str, Any]) -> None:
    record = origin(payload)
    st.subheader("Compensation")
    st.caption(
        "Compensation is its own LCD workbook page: project compensation data, basic service fee basis, "
        "design consultant compensation, supplemental services, reimbursables, and additional services."
    )

    cols = st.columns(4)
    cols[0].metric("Project S.F.", field_value(record, "project_square_footage", "existing_sf"))
    cols[1].metric("Compensation Basis", field_value(record, "general_project_information", "compensation_basis_anticipated"))
    cols[2].metric("Current Routing", "Schedule F")
    cols[3].metric("Fee Readiness", "Open")

    st.subheader("Project Compensation Data")
    render_table(
        [
            row(record, "Project Name", "general_project_information", "project_name"),
            ("Project Start Date", "TBD / from LCD first page", "linked from Initial Information"),
            row(record, "Project Location", "general_project_information", "project_location"),
            ("Project/S.O. Number", "Must be requested", "required before complete SO package"),
            row(record, "Project S.F.", "project_square_footage", "existing_sf"),
        ]
    )

    st.subheader("Fee for Basic Services (Architectural and Interior Design)")
    st.dataframe(
        pd.DataFrame(
            COMPENSATION_BASIC_FEE_ROWS,
            columns=["Basis for Compensation", "Feasibility Stage", "SD Thru DD", "CD Thru Closeout"],
        ),
        width="stretch",
        hide_index=True,
    )

    consultants_col, services_col = st.columns(2)
    with consultants_col:
        st.subheader("Design Consultants Compensation")
        render_table(
            [
                ("Mechanical", "Basis or amount TBD", "Architect/consultant fee input"),
                ("Electrical", "Basis or amount TBD", "Architect/consultant fee input"),
                ("Structural", "Basis or amount TBD", "Architect/consultant fee input"),
                ("Civil (if Required)", "TBD", "supplemental / conditional"),
            ],
            columns=("Consultant", "Current Value", "State"),
        )
    with services_col:
        st.subheader("Other Compensation Inputs")
        render_table(
            [
                ("Basic Service Exception", "None identified", "review if exception exists"),
                ("Supplemental Consulting Services", "None identified", "select if required"),
                ("Additional Services", "None identified", "select if required"),
                ("Reimbursable Expenses", "TBD", "travel, permit fees, field office"),
            ],
            columns=("Input", "Current Value", "State"),
        )

    st.subheader("Schedule E/F Quick Reference")
    st.dataframe(
        pd.DataFrame(SCHEDULE_EF_REFERENCE_ROWS, columns=["Schedule", "Use", "Routing Note"]),
        width="stretch",
        hide_index=True,
    )
    st.dataframe(
        pd.DataFrame(COMPENSATION_REFERENCE_ROWS, columns=["Compensation Category", "Reference", "Rule / Note"]),
        width="stretch",
        hide_index=True,
    )
    st.info(
        "For Fairview, the fixture is a 1,800 SF remodel/renovation, so the prototype routes fee review toward Schedule F. "
        "Contracts still creates the actual Service Order; Pii exposes the review package and gaps."
    )


def render_design_schedule(payload: dict[str, Any]) -> None:
    record = origin(payload)
    st.subheader("Design Schedule")
    st.warning("Design Schedule must be created before the Service Order review package is complete.")

    st.caption(
        "Pages 1–2 of the Design Schedule source are the complete project flow. "
        "Phases are shown collapsed so the user can quickly scan what is required."
    )
    cols = st.columns(3)
    cols[0].metric("Flow Pages", "1–2")
    cols[1].metric("Phases", len(DESIGN_SCHEDULE_PHASES))
    cols[2].metric("Milestones", sum(len(items) for items in DESIGN_SCHEDULE_PHASES.values()))

    st.subheader("Initial Schedule Anchors")
    rows = [
        (*row(record, "Construction Commencement", "initial_schedule", "commencement_of_construction"), "extracted"),
        (*row(record, "Substantial Completion", "initial_schedule", "substantial_completion"), "extracted"),
        (
            "Estimated Occupancy",
            field_value(record, "initial_schedule", "estimated_occupancy_date"),
            "No LCD-W home",
            "extracted / schema gap",
        ),
        ("Design Milestone Delivery Dates", "TBD", "Design Schedule tab", "required for SO package"),
    ]
    st.dataframe(
        pd.DataFrame(rows, columns=["Schedule Item", "Value", "Reference", "State"]).astype(str),
        width="stretch",
        hide_index=True,
    )

    st.subheader("Project Flow")
    for phase, milestones in DESIGN_SCHEDULE_PHASES.items():
        with st.expander(f"{phase} ({len(milestones)} milestones)"):
            flow_rows = [(milestone, "TBD", "TBD", "TBD") for milestone in milestones]
            st.dataframe(
                pd.DataFrame(
                    flow_rows,
                    columns=["Design Milestone", "Duration (Days)", "Actual Delivery Date", "Revision"],
                ),
                width="stretch",
                hide_index=True,
            )

    st.subheader("SLA Reference")
    st.caption(
        "Page 3 reference only: agreed timeframe expectations by project type. "
        "Useful for future schedule checks, but not project-specific data by itself."
    )
    st.dataframe(
        pd.DataFrame(
            SLA_REFERENCE_ROWS,
            columns=["Phase", "New Location / Relocation", "Remodel / Expansion", "Refresh / Infrastructure"],
        ),
        width="stretch",
        hide_index=True,
    )
    st.info(
        "SLA note: incomplete data, untimely additions, or untimely approvals may extend the schedule; "
        "incomplete drawings or missed design intent do not warrant additional Architect time."
    )


def render_consultants(payload: dict[str, Any]) -> None:
    record = origin(payload)
    st.subheader("Consultants")
    render_table(
        [
            (
                "Mechanical / Electrical / Structural",
                field_value(record, "design_consultants_basic_services", "mechanical_electrical_structural"),
                "Basic Services / Architect to engage",
            ),
            (
                "Architect's Project Representative",
                "Missing",
                "Required before Service Order review is complete",
            ),
        ],
        columns=("Role", "Current Value", "State"),
    )


def render_alliance_partners(payload: dict[str, Any]) -> None:
    record = origin(payload)
    rows = [
        (
            "UHG Design Experience Regional Representative",
            field_value(record, "general_project_information", "uhg_design_experience_representative"),
        ),
        (
            "UHG Regional Project Management Representative",
            field_value(record, "general_project_information", "uhg_project_management_representative"),
        ),
        ("Owner-retained Consultants", field_value(record, "owner_consultants", "owner_retained_consultants")),
    ]
    st.subheader("Alliance Partners")
    st.dataframe(pd.DataFrame(rows, columns=["Partner / Representative", "Current Value"]), width="stretch", hide_index=True)


def render_contracts(payload: dict[str, Any]) -> None:
    st.subheader("Contracts")
    st.caption(
        "Contracts is the governing-source layer: Master Agreement, current Scope of Work, "
        "SOW modifications, and the executed Service Order once received."
    )

    cols = st.columns(4)
    cols[0].metric("Master Agreement", "Available")
    cols[1].metric("Scope of Work", "Current + updateable")
    cols[2].metric("Executed SO", "Pending")
    cols[3].metric("SOW Updates", "Absorption required")

    st.subheader("Contract Documents")
    st.dataframe(
        pd.DataFrame(CONTRACT_DOCUMENT_ROWS, columns=["Document", "Status", "Path / Placeholder", "Role"]),
        width="stretch",
        hide_index=True,
    )

    st.subheader("Scope of Work Update Absorption")
    st.warning(
        "Updated SOW material should arrive as a complete new source document whenever possible. "
        "Pii must not silently overwrite current context; it must preserve, compare, classify, reconcile, approve, then propagate."
    )
    st.dataframe(
        pd.DataFrame(SOW_UPDATE_ABSORPTION_STEPS, columns=["Step", "Requirement"]),
        width="stretch",
        hide_index=True,
    )

    st.subheader("Current Contract Layer Impacts")
    render_table(
        [
            ("Project Scope", "Changes require SOW comparison and PM approval", "affects Project Home / Scope"),
            ("Compensation", "Changes may alter Schedule E/F routing or fee basis", "affects Compensation / SO Article 4"),
            ("Design Schedule", "Changes may add/remove milestone obligations", "affects Design Schedule / SO Article 3"),
            ("Consultants", "Changes may add owner, supplemental, or basic-service consultant requirements", "affects Consultants / Alliance Partners"),
            ("Service Order", "Executed SO is final project-specific contract container", "Contracts page stores received executed SO"),
        ],
        columns=("Area", "Impact Rule", "Downstream Surface"),
    )


def render_metrics(payload: dict[str, Any]) -> None:
    st.subheader("Metrics")
    st.caption(
        "Source-backed Metrics page for SOW KPIs, required reporting metrics, and Project Tracking Report logging. "
        "Gauge visuals will come later as rollups derived from this required metric set."
    )

    cols = st.columns(4)
    cols[0].metric("SOW KPI Categories", len(SOW_KPI_ROWS))
    cols[1].metric("Required Metrics", len(REQUIRED_METRIC_ROWS))
    cols[2].metric("Tracking Fields", sum(len(rows) for rows in METRIC_LOGGING_SECTIONS.values()))
    cols[3].metric("Gauge Families Later", len(METRIC_GAUGE_ROWS))

    st.subheader('Key Performance Indicators (“KPIs”)')
    st.caption(
        "Displayed in the same two-column structure used by Exhibit A Scope of Work: KPI Category and Goal. "
        "The SOW notes these are to be finalized before contract execution and reviewed at the 6-month QBRs in Q2 and Q4."
    )
    st.dataframe(
        pd.DataFrame(SOW_KPI_ROWS, columns=["KPI Category", "Goal"]).astype(str),
        width="stretch",
        hide_index=True,
    )

    st.subheader("Required Metrics List")
    st.caption(
        "All required metrics currently identified from SOW Reporting 1.0, Project Tracking Reporting, Design Fee Reporting, "
        "Business Reviews, and the Project Tracking Report template."
    )
    st.dataframe(
        pd.DataFrame(REQUIRED_METRIC_ROWS, columns=["Required Report Area", "Required Metric", "Source / Cadence"]).astype(str),
        width="stretch",
        hide_index=True,
    )

    st.subheader("Contract / Scope of Work Alignment")
    st.success("Reviewed against Exhibit A Scope of Work: these metrics are aligned with project reporting, schedule, quality, change, deficiency, and fee/revision obligations.")
    render_table(METRIC_CONTRACT_ALIGNMENT_ROWS, columns=("Metric Area", "Evidence", "Why it belongs"))

    st.subheader("Future Gauge Summary Inputs")
    st.info(
        "These are placeholders for the future dashboard/home-page gauges. No scoring formulas or thresholds are applied yet."
    )
    render_table(METRIC_GAUGE_ROWS, columns=("Future Gauge", "Required Inputs", "Current Status"))

    st.subheader("Metric Logging Entry Point")
    st.caption("Use these sections as the detailed logging surface; later the logs can roll up to project-home gauges.")
    for section, rows in METRIC_LOGGING_SECTIONS.items():
        with st.expander(f"{section} ({len(rows)} fields)"):
            render_table(rows, columns=("Metric / Log Field", "Entry Source", "Dashboard Use"))


def render_service_order_review(payload: dict[str, Any]) -> None:
    st.subheader("Service Order Review")
    st.caption(
        "Contracts creates the actual Service Order. Pii prepares the article-based information package "
        "needed to communicate with Contracts without duplicating the B221 form."
    )

    total_items = sum(len(items) for items in SERVICE_ORDER_ARTICLES.values())
    cols = st.columns(4)
    cols[0].metric("Articles", len(SERVICE_ORDER_ARTICLES))
    cols[1].metric("Preparation Items", total_items)
    cols[2].metric("Executed SO", "Pending")
    cols[3].metric("Readiness", "Open")

    st.warning(
        "This is a preparation/checklist view based on the Service Order template. "
        "It does not create the legal form; it collects and reviews the information Contracts needs."
    )

    for article, rows in SERVICE_ORDER_ARTICLES.items():
        with st.expander(f"{article} ({len(rows)} items)"):
            render_table(rows, columns=("Required Information", "Source / Current Value", "Review State"))

    st.subheader("Contracts Communication Package")
    render_table(
        [
            ("Project Scope Document", "Attachment X", "Required before SO package is complete"),
            ("Project Design Schedule", "Attachment X", "Required before SO package is complete"),
            ("Additional Services / Reimbursables", "Attachment X", "If applicable"),
            ("Executed Service Order", "Returned by Contracts", "Attach when received; tracked on Contracts page"),
        ],
        columns=("Package Item", "SO Location", "State"),
    )


def render_sidebar(payload: dict[str, Any]) -> str:
    logo_uri = image_data_uri(GRACE_LOGO_PATH)
    with st.sidebar:
        st.markdown(
            f"""
            <div class="grace-logo-box">
                <img class="grace-logo-img" src="{logo_uri}" alt="Grace Design Studios logo" />
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f"""
            <div class="pii-sidebar-loaded">
                <div class="pii-sidebar-loaded-title">Loaded: {html.escape(payload['project'])}</div>
                <div class="pii-sidebar-loaded-caption">Fixture: Fairview fictional PDD</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        choice = st.radio("LCD / Pii Navigation", NAV_ITEMS, label_visibility="visible")
        st.markdown(
            """
            <div class="pii-sidebar-metric">
                <div class="pii-side-metric-label">Metric 1</div>
                <div class="pii-gauge"></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return choice


def render_dashboard() -> None:
    st.set_page_config(page_title="Pii Dashboard", layout="wide", initial_sidebar_state="expanded")
    payload = load_fixture()
    choice = render_sidebar(payload)
    render_header(payload, choice)
    render_pending_rail()

    if choice == "Home":
        render_home(payload)
    elif choice == "LCD Manual Entry":
        render_lcd_manual_entry(payload)
    elif choice == "Project Scope":
        render_project_scope(payload)
    elif choice == "Project Budget":
        render_project_budget(payload)
    elif choice == "Compensation":
        render_compensation(payload)
    elif choice == "Design Schedule":
        render_design_schedule(payload)
    elif choice == "Consultants":
        render_consultants(payload)
    elif choice == "Alliance Partners":
        render_alliance_partners(payload)
    elif choice == "Contracts":
        render_contracts(payload)
    elif choice == "Metrics":
        render_metrics(payload)
    elif choice == "Service Order Review":
        render_service_order_review(payload)


if __name__ == "__main__":
    render_dashboard()

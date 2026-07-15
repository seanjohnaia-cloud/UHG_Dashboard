---
record_type: workflow_start_date_rule
status: active_user_confirmed_rule
scope: normal_project_workflow
source_artifacts:
  - 00_Source/Workflow/Project Workflow/original/!_Project Workflow.xlsx
  - user clarification
---

# Workflow Start Date Rule — Normal Projects

## User-Confirmed Rule

For a **normal project**, referring to the workflow:

```text
The day Grace receives the scope document is the recorded project start date.
```

## Meaning

The start date is not necessarily:

- the day someone first discusses the project informally;
- the day a Service Order is executed;
- the day a fee proposal is finalized;
- the day design work begins;
- the day a purchase order is issued.

For normal workflow tracking, the recorded start date begins when the **scope document is received**.

## Evidence / Relationship to Workflow

The Project Workflow workbook is preserved at:

```text
00_Source/Workflow/Project Workflow/original/!_Project Workflow.xlsx
```

An extracted access layer exists at:

```text
00_Source/Workflow/Project Workflow/extracted/
```

The `WORKFLOW` sheet includes a `Scope (Initial)` workflow item, and the user clarified that receipt of the scope document is the start-date trigger for normal projects.

## Impact on KPI / Response-Time Metrics

Pii must distinguish at least three date concepts:

| Date Concept | Definition | Applies To |
|---|---|---|
| `request_received_at` | Date the request/email/inquiry is received. | All request intake, including deficient/informal requests. |
| `scope_document_received_at` | Date the scope document is received. | Normal project workflow start-date trigger. |
| `recorded_project_start_date` | The official project start date used by workflow/reporting. | Usually equals `scope_document_received_at` for normal projects. |

## UC-001 Difference

UC-001 is not a clean normal project example. It began as an incomplete project request / small-project fee exercise before a formal Service Order was required.

Therefore UC-001 should track:

```text
request_received_at = 2026-07-02
work_started_at = 2026-07-06
client_response_issued_at = 2026-07-09
scope_document_received_at = unknown / not separately established yet
recorded_project_start_date = not established for normal workflow yet
```

## Design Consequence

Future Pii response-time and KPI tracking must not collapse all dates into one field.

A normal project can have:

```text
request_received_at < scope_document_received_at = recorded_project_start_date < notice_to_proceed_or_authorization
```

or, if the request package includes the scope document immediately:

```text
request_received_at = scope_document_received_at = recorded_project_start_date
```

The system must preserve which case applies.

PAC information should begin before Notice to Proceed through common data fields, then be confirmed for sufficiency once NTP/equivalent authorization is received.

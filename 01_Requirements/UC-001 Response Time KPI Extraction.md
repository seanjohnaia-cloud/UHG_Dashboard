---
record_type: contract_kpi_extraction
status: draft_extracted_from_contract
use_case: UC-001
experiment_focus: Muncie Family Physicians
source_ids:
  - SRC-CONTRACT-EXHIBIT-A
  - SRC-CONTRACT-EXECUTED-PACKAGE
---

# Contract KPI Extraction — Request / Response Time

## Finding

Yes. The contract/reporting materials appear to make request response time a reportable performance metric.

The clearest language found is in **Project Tracking Reporting**, which requires reporting:

```text
The percentage of requests that met the expected response times.
```

This is present in:

1. Exhibit A extracted text, lines 1413-1417.
2. `!_Required Reports and Tracking.docx` extraction, paragraphs 19-21.

## Evidence 1 — Exhibit A Scope of Work

Source:

```text
00_Source/Contract/Exhibit A - Scope of Work/extracted-text.md
```

Relevant excerpt:

```text
PROJECT TRACKING REPORTING: Architect shall provide Project tracking reporting, which shall include a summary of all projects by project phase. The report shall provide both a “dashboard” type summary supported by detailed project level information. The report shall include the following:

The total number of requests and projects handled.

The percentage of requests that met the expected response times.
```

Approximate extraction lines:

```text
1413-1417
```

## Evidence 2 — Required Reports and Tracking

Source:

```text
00_Source/Contract/Executed Agreement Package/extracted/required-reports-and-tracking-extracted.md
```

Relevant excerpt:

```text
PROJECT TRACKING REPORTING: Architect shall provide Project tracking reporting, which shall include a summary of all projects by project phase. The report shall provide both a “dashboard” type summary supported by detailed project level information. The report shall include the following:

The total number of requests and projects handled. (Dashboard)
The percentage of requests that met the expected response times. (Dashboard)
```

Approximate extraction paragraphs:

```text
19-21
```

## Relation to KPI Section

The explicit KPI table in Exhibit A identifies categories such as:

- Project Delivery Timeliness;
- Client Satisfaction;
- Design Quality & Innovation;
- Regulatory Compliance;
- Cost Alignment;
- Change Order Frequency.

The request-response metric is not listed in the KPI table as a named row, but it is included in required project tracking/dashboard reporting and therefore should be treated as a **contract-reportable operational performance metric**, likely feeding timeliness / process performance / QBR reporting.

## Pii Interpretation

For Pii, this means UC-001's response timeline is not just an internal improvement note. It is contract-relevant reporting data.

The metric should be tracked from:

```text
proposal request received
→ response issued
```

with sub-metrics for:

```text
time to first ACT
time to clarification
time to internal assessment
team fee accumulation time
calendar days
available workdays
holiday/weekend adjustments
```

## UC-001 Application

For the Muncie exchange:

| Metric | Value |
|---|---:|
| Request received | 2026-07-02 |
| Response issued | 2026-07-09 |
| Calendar days elapsed | 7 |
| Work began | 2026-07-06 |
| Calendar days from work start to response | 3 |
| Team budget/fee accumulation | 3 days |

## Open Issue

The contract language references **expected response times**, but the specific expected response-time threshold has not yet been located in the preserved sources.

A separate workflow rule now clarifies that for a normal project, the day Grace receives the scope document is the recorded project start date:

```text
01_Requirements/Workflow Start Date Rule.md
```

Pii should therefore record separate fields:

```text
actual_response_time
expected_response_time_source
request_received_at
scope_document_received_at
recorded_project_start_date
```

Until the expected threshold is found, compliance cannot be computed; only elapsed time can be computed. For normal projects, compliance may need to be evaluated from the recorded start date / scope-document receipt date, while informal or deficient requests like UC-001 may also need request-intake elapsed time.

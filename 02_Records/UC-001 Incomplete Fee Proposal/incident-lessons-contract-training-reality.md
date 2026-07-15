---
record_type: incident_lessons
status: draft_pattern_extraction
use_case: UC-001
experiment_focus: Muncie Family Physicians
---

# UC-001 Incident Lessons — Contract, Training, Reality

## Core Observation

This incident is small, but it exposed the practical stack Pii must reconcile:

```text
Contract
+ UHG training / intended workflow
+ Reality of the actual exchange
= useful project intelligence
```

## 1. Contract Layer

The contract gives the governing terms:

- Service Order structure;
- fee schedules;
- deliverable names;
- SLA / timeframe language;
- consultant and owner responsibility language;
- required exhibits and formal documentation expectations.

## 2. UHG Training / Intended Workflow Layer

The training/workflow layer gives the expected practice:

- how Service Orders are supposed to be prepared;
- how project types map to deliverables;
- how fees are pulled from schedules;
- how schedule/SLA frameworks should be applied;
- how the LCD/SO Matrix workbooks help organize project data.

## 3. Reality Layer

The actual exchange changed the path:

- two projects arrived at once;
- Muncie had to be isolated for the experiment;
- the PM did not need a formal Service Order today;
- the PM wanted Grace's proposal only, no MEP fee now;
- MEP was still acknowledged as likely required later;
- the artifact sent gave fee/schedule data, but not a complete scope/statement of understanding;
- the response took 7 calendar days from request to client response, with a holiday/weekend and 3-day team fee accumulation inside that span.

## Major Pii Lesson

Pii should not merely reproduce the contract or automate the workbook. It must preserve and govern the translation between:

1. what the contract says;
2. what training says should happen;
3. what the client/PM actually needs right now;
4. what the team actually produces;
5. what the response should become if it were done to a gold standard.

## Gold Standard Output Pattern

For small-project fee exercises, the output should be more than a data table.

The target is:

```text
Request Summary
+ Scope Understanding
+ Grace Response / Fee Basis
+ Assumptions and Exclusions
+ Schedule / SLA Understanding
+ Carry-Forward Path
= Complete Statement of Understanding
```

## Time-to-Response Lesson

The response-time metric should be decomposed:

| Metric | Why It Matters |
|---|---|
| Calendar response time | Client-perceived delay. |
| Available-workday response time | Operational reality after holidays/weekends. |
| Time to first ACT | Whether the request was converted into action quickly. |
| Time to clarification | Whether blockers were identified quickly. |
| Internal fee accumulation time | Whether the team response cycle is too slow. |

For UC-001, the user executed the first ACT on the first working day after the holiday/weekend. The improvement opportunity is likely not only first-action speed, but internal fee accumulation and repeatable output assembly.

## Candidate Future Pii Feature

Add a standard response-time ledger to every project request:

```text
request_received_at
first_reviewed_at
first_ACT_started_at
clarification_sent_at
PM_response_received_at
internal_assessment_sent_at
team_fee_request_sent_at
team_fee_received_at
client_response_issued_at
non_working_days
elapsed_calendar_days
elapsed_available_workdays
time_to_first_ACT
internal_accumulation_time
```

## Governing Caution

Do not treat the first incident as enough evidence to finalize all standards. Treat it as the first reality specimen. Future incidents should be compared against this one to see which patterns persist.

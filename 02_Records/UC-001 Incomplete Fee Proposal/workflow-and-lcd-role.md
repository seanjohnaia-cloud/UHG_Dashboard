---
record_type: workflow_architecture_note
status: active
scope: Pii operational workflow
---

# Workflow and LCW/LCD Workbook Roles in Pii

## Concept Boundary Clarification

The user clarified that the LCW/LCD workbook currently being examined is **customized to UHG only** and was the user's attempt at automation for UHG-specific project management/data handling.

PAC is separate: it is a broader Grace-wide framework concept that includes all processes required to start a project at Grace.

Do not treat the UHG LCW/LCD workbook as the PAC model.

## User Addendum Preserved

The user clarified two foundational workflow distinctions:

1. **Service Order preparation is the first ACT in the workflow.**
2. The **LCW/LCD Workbook** is the user's human attempt at creating a document that has everything needed to manage the project **as data**, not merely as context. The file currently present in the inbox is named `!_LCD Workbook.xlsx`; if `LCW` is the intended name, treat that as an alias/correction to resolve later.

## Workflow Artifact

The project workflow source is preserved as:

```text
00_Source/Workflow/Project Workflow/original/!_Project Workflow.xlsx
```

Observed workbook sheets, without extracting/canonizing cell contents:

- `WORKFLOW`
- `PROJECT NUMBER`
- `INITIATION PHASE`
- `FEASIBILITY STAGE`
- `SITE PLANNING`
- `SD`
- `DD`
- `CD`
- `B&P`
- `CA`
- `CLOSEOUT`

## Service Order Preparation as First ACT

For Pii, the first operational act is not generic intake and not abstract project setup. The first ACT is:

```text
Service Order Preparation
```

This means the initial operational workflow should orient around preparing the Service Order / fee proposal package from incomplete source material, rather than trying to model the entire project lifecycle upfront.

## LCD Workbook Role

The LCD Workbook is preserved as:

```text
00_Source/Workflow/LCD Workbook/original/!_LCD Workbook.xlsx
```

Observed workbook sheets, without extracting/canonizing cell contents:

- `Life Cycle Data Worksheet`
- `Design Schedule`
- `Compensation`
- `Service Order`
- `Project Tracking Report`

The LCD Workbook is classified as:

```text
human_attempt_project_management_as_data
```

It is not just context. It is a prototype/attempt to hold the project-management substrate as data fields, records, schedules, compensation, service order information, and tracking.

## Architectural Consequence

The emerging Pii stack for UC-001 is now clearer:

```text
Contract Source
+ UHG Request / Project Material
+ SO Matrix Contract Scrub
→ Service Order Preparation as First ACT
→ LCD-style Project Data Record
→ Proposal / Readiness / Tracking Outputs
```

## Boundary

Do not convert the whole LCW/LCD Workbook into Pii architecture or PAC. For UC-001, use it as UHG-specific evidence of one client-customized project-management-as-data attempt, but only instantiate fields/entities required by the Muncie Service Order Preparation act.

PAC must be treated as a broader Grace-wide project-start framework and should be developed separately through review before implementation.

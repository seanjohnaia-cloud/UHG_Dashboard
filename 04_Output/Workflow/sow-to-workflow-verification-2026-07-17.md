# SOW → Project Workflow Verification

**Date:** 2026-07-17  
**Status:** First-pass source-backed verification; not canon until reviewed.  

## Sources checked

### Contractual source of record

- `00_Source/Contract/Exhibit A - Scope of Work/Exhibit A-Scope of Work.docx`
- Access layer: `00_Source/Contract/Exhibit A - Scope of Work/extracted-text.md`
- Source ID: `SRC-CONTRACT-EXHIBIT-A`
- SHA-256: `b40eb296b6c67ecf0bed6ad004e9ebbaf41097296d4112fe784377d1e2315b7e`

### Workflow source

- `00_Source/Workflow/Project Workflow/original/!_Project Workflow.xlsx`
- Sheets inspected: `WORKFLOW`, `PROJECT NUMBER`, `INITIATION PHASE`, `FEASIBILITY STAGE`, `SITE PLANNING`, `SD`, `DD`, `CD`, `B&P`, `CA`, `CLOSEOUT`
- Both worksheet cell text and embedded drawing/shape text were extracted.

---

## Executive finding

The current Excel workflow is directionally aligned with the contractual Scope of Work, but it is **not yet sufficient as a self-updating or contract-verifiable workflow spine**.

It captures the major lifecycle phases and several key contractual decision points, especially:

- request receipt;
- LCD workbook creation / entry of known data;
- project number request;
- kickoff and/or site visit;
- project initiation;
- Service Order preparation and approval;
- feasibility;
- site planning;
- schematic design;
- design development;
- construction documents;
- bidding and permitting;
- construction administration;
- closeout;
- PM performance metric review.

However, several contractual requirements in the SOW are either missing, underdeveloped, or only implied in the workflow. The workflow should therefore be treated as a **contract-derived guide/spine**, not as a verified complete representation of Exhibit A.

If Exhibit A is revised, the workflow should be re-generated or re-verified against the revised source. Otherwise the workflow will become stale and operationally misleading.

---

## Verification matrix

| Area | SOW evidence | Workflow evidence | Verification status | Notes |
|---|---:|---:|---|---|
| Request/project tracking from proposal request through closeout | lines 171-173 | WORKFLOW: `REQUEST RECEIPT`; `NEED TO TRACK EACH REQUEST`; `END` | **Aligned** | Workflow correctly begins at request receipt. |
| Service Order required per project | lines 255-259; 1133-1141; 1211 | WORKFLOW: `SUBMIT SERVICE ORDER FOR APPROVAL`; INITIATION: `COMPLETE SERVICE ORDER TEMPLATE (AIA B221-2018)` | **Aligned** | Workflow should also retain source fields: scope, compensation, schedule. |
| Service Order scope/compensation/schedule | lines 255-259 | INITIATION: design schedule, compensation form, reimbursables, fees | **Aligned** | Needs explicit source mapping from LCD/baseline fields to SO Article fields. |
| Authorization to proceed / PO | lines 261-263 | Not explicit | **Gap** | Workflow should include PO / authorization state separate from SO preparation. |
| Service Order/PO changes | lines 265-267; 1063-1065 | Not explicit | **Gap** | Add change-in-service/change-to-SO control node. |
| Project Schedule / Design Schedule | lines 249-251; 269-275; 467-469; 1329-1356 | WORKFLOW notes LCD populates Project Design Schedule; INITIATION requires Design Schedule | **Aligned but needs strengthening** | Workflow should track schedule updates and monthly design-phase updates. |
| Design milestone dates | lines 275-279 | INITIATION: design milestone delivery dates; revisions tracked | **Aligned** | Good match. |
| Fast-tracking / out-of-sequence work | lines 281-283; 337 | Not explicit | **Gap** | Add node for fast-track/out-of-sequence approval and fee impact. |
| Owner consultants / Alliance Partners | lines 225-247; 677-679; 1305-1323 | Workflow mentions Alliance Partners in DD/CD; LCD initial info includes Owner's Consultants | **Partial** | Needs owner-consultant artifact/evidence tracking across phases. |
| Feasibility stage | lines 341-377 | FEASIBILITY sheet: kickoff, internal interview, preliminary program, scenario development, utilization analysis, approval | **Aligned** | Strong match. |
| Site due diligence / field measurements | lines 383-439 | SD sheet: initial site visit, existing documents, field measurements as Additional Services, Site Due Diligence Report | **Aligned** | Strong match; should include BOMA variance and checklist requirement if used operationally. |
| Detailed programming / Programming Lite | lines 441-483 | SD sheet: detailed programming; programming lite note in cell text | **Aligned** | Good match. |
| Preliminary floor plan / Schematic Design | lines 487-525; SLA table lines 1347 | SD sheet: preliminary floor plans, approval, schematic design documents, peer review, code review | **Aligned** | Add page-turn meeting with Design Experience and approval dependency. |
| No DD before preliminary floor plan approval | lines 521-525 | SD sheet: preliminary floor plan approval | **Partial** | Workflow implies approval but should explicitly block DD start without approval. |
| Design Development package | lines 527-701 | DD sheet: DD package with consultants, Alliance Partner coordination, reviews, MEP narrative, exceptions | **Aligned** | Good match. |
| DD exceptions block CDs | lines 697-701; 705; 1358 | DD sheet note: cannot proceed to CD with outstanding exceptions | **Aligned** | Strong control-advancement match. |
| Construction Documents | lines 703-825 | CD sheet: develop CD package, consultants, clash detection, 50% and 90% review | **Partial** | Workflow has key nodes but lacks detailed CD deliverable requirements from SOW. |
| Clash detection | line 203 | CD sheet: perform clash detection | **Aligned** | Good match. |
| Ground-up-only 50% CD review | lines 725-727 | CD sheet: 50% progress review, ground-up only | **Aligned** | Good match. |
| 90% CD review as required | lines 729-733 | CD sheet: 90% review as required | **Aligned** | Good match. |
| Bidding and Permitting | lines 827-889 | B&P sheet only contains START/EXIT | **Major gap** | Needs generated workflow nodes from SOW. |
| Permit status/submittal log | lines 835-859 | Not present | **Major gap** | Add permit requirements, expeditor decision, weekly submittal log, active status management. |
| Bidding Q&A/addenda/pre-bid/VE | lines 877-889 | Not present | **Major gap** | Add bidding nodes. |
| Construction Administration | lines 891-1059 | CA sheet only contains START/EXIT | **Major gap** | Add OAC calls, RFIs, submittals, changes, site visits, punch list, warranty. |
| Closeout / record documents | lines 995-1059; 1321-1323 | CLOSEOUT sheet only contains START/EXIT | **Major gap** | Add substantial/final completion, deficiency resolution, record Revit/CAD, emergency evacuation plan, warranty walk. |
| Supplemental/Additional Services | lines 217; 437-439; 1061-1065; 1267 | INITIATION and SD note field measurements; additional/supplemental service determination | **Partial** | Needs universal additional-service classification across all phases. |
| Change management / written approval before proceeding | lines 963-979; 1063-1065 | Not explicit | **Major gap** | Add `Protect Integrity` control: price every change, written approval before proceeding. |
| Reporting/KPIs/SLAs | lines 1301-1485 | WORKFLOW repeats PM review/document required performance metrics | **Partial** | Workflow should map actual KPI/reporting fields, not just generic metric review. |
| Project Tracking Report | lines 1413-1449 | WORKFLOW says Project Tracking Report; metrics notes include totals, response times, deficiencies, staff time | **Aligned but incomplete** | Needs field-level report schema. |

---

## Current workflow coverage by phase

### Covered well enough for a first spine

- Request receipt / intake
- LCD workbook / known-data entry
- Project number request
- Initiation / Service Order preparation
- Feasibility
- Site Planning
- Schematic Design
- Design Development
- Construction Documents, at a high level

### Underdeveloped / stale if used as an execution guide

- Bidding & Permitting
- Construction Administration
- Closeout
- Change-in-service/change-order governance
- PO / authorization-to-proceed state
- Permit status tracking
- Cloud repository / artifact governance
- KPI/reporting fields beyond generic performance metrics

---

## SOW-derived workflow spine draft

This draft should replace the idea of a fixed workflow checklist. Each node should be project-classified as:

`Expected`, `Required`, `Not Required`, `Additional Service`, `Deferred`, `Added`, `Blocked`, `Complete`, `Superseded`, or `Unknown`.

### 0. Request / Intake

Source basis:

- SOW lines 171-173: track progress from proposal request through delivery/closeout.
- Workflow sheet: request receipt is project start/date of receipt.

Nodes:

1. Record request receipt date.
2. Identify project group and project type.
3. Identify PM and project leader.
4. Preserve original request artifact.
5. Enter all known data into baseline/LCD access view.
6. Identify missing initial information.
7. Determine whether project proceeds, is rejected, or remains pending.

### 1. Baseline / LCD / Service Order Preparation

Source basis:

- SOW lines 255-259: Service Order indicates project-specific scope, compensation, and schedule.
- SOW lines 269-275: Project Schedule and Design Milestone Dates.
- Workflow INITIATION sheet: determine required phases, additional/supplemental services, reimbursables, fees, complete AIA B221 template.

Nodes:

1. Review initial information.
2. Determine required contractual phases.
3. Determine additional/supplemental services.
4. Determine reimbursable expenses.
5. Determine design milestone dates.
6. Prepare project design schedule.
7. Prepare compensation data / fee basis.
8. Complete Service Order template fields.
9. Confirm actual Service Order completion responsibility.
10. Submit Service Order for approval.
11. Record Service Order approval/completion.
12. Record PO / authorization to proceed.

### 2. Feasibility

Source basis:

- SOW lines 341-377.
- Workflow FEASIBILITY sheet.

Nodes:

1. Feasibility kickoff.
2. Internal interview / high-level programming discussion.
3. Preliminary program development.
4. Scenario development.
5. Utilization analysis, if required.
6. Owner/designated representative approval.
7. Evidence package: scope, budget, schedule, assumptions, background info.

### 3. Site Planning

Source basis:

- SOW lines 1209-1269.
- Workflow SITE PLANNING sheet.

Nodes:

1. Receive initial site information: CAD/Revit/PDF.
2. Verify document suitability.
3. Planning and zoning research.
4. Architectural Site Plan design/documentation.
5. Architectural Site Plan review meeting.
6. Architectural Site Plan approval.
7. Preliminary Site Plan kickoff.
8. Preliminary Site Plan design/documentation.
9. Preliminary Site Plan review meeting.
10. Preliminary Site Plan approval.
11. Classify revisions/options as Basic or Additional Service.

### 4. Schematic Design / Preliminary Floor Plan

Source basis:

- SOW lines 379-525.
- Workflow SD sheet.

Nodes:

1. Determine whether first site visit is required.
2. Determine whether existing accurate CDs exist.
3. Determine whether field measurement/site due diligence is Additional Service.
4. Determine whether CAD/Revit file complies with Owner standards.
5. Develop/update compliant CAD/Revit existing conditions if approved.
6. Develop Site Due Diligence Report using current checklist.
7. Determine Detailed Programming vs Programming Lite.
8. Schedule/conduct interviews.
9. Develop program summary.
10. Develop preliminary floor plan(s).
11. Conduct preliminary floor plan review.
12. Receive preliminary floor plan approval.
13. Develop Schematic Design Documents.
14. Conduct peer design review / preliminary code review.
15. Host schematic design page-turn meeting with Owner/Design Experience.
16. Receive written approval before DD proceeds.

### 5. Design Development

Source basis:

- SOW lines 527-701.
- Workflow DD sheet.

Nodes:

1. Confirm SD approval and authorized adjustments.
2. Create DD package with consultants.
3. Coordinate package with Alliance Partners.
4. Schedule progress review for architectural/furniture/medical equipment/millwork elevations.
5. Conduct QA/QC Review 1.
6. Document exceptions to design standards.
7. Conduct Peer Design Review 2.
8. Review power/data requirements, revisions, additions, and design-standard exceptions.
9. Continue consultant/Alliance Partner coordination.
10. Develop MEP Narrative with consultants.
11. Final review: power/data, finishes, revisions, exceptions.
12. Upload DD package to repository.
13. Block CD start if exceptions remain unapproved.
14. Receive written DD approval before CD proceeds.

### 6. Construction Documents

Source basis:

- SOW lines 703-825.
- Workflow CD sheet.

Nodes:

1. Confirm DD approval and approved exceptions.
2. Develop CD package with consultants.
3. Coordinate final package with Alliance Partners.
4. Perform clash detection.
5. Prepare 50% CD review set for ground-up projects only.
6. Conduct 50% review, if applicable.
7. Prepare/conduct 90% review as required.
8. Prepare drawings/specifications adequate for bid and permit.
9. Identify delegated design requirements.
10. Submit CDs and request approval.
11. Record adjustments to Cost of Work.

### 7. Bidding & Permitting

Source basis:

- SOW lines 827-889.
- Current workflow has only a placeholder sheet.

Nodes to generate:

1. Confirm Owner written request/authorization for preconstruction/bidding assistance.
2. Assist reviewing contractor proposal, if requested.
3. Incorporate agreed assumptions/clarifications into documents upon authorization.
4. Prepare permit submittal documents.
5. Determine AHJ requirements and review timeline.
6. Determine whether Permit Expeditor is required.
7. Submit original permit package.
8. Maintain weekly submittal log.
9. Respond to permit comments.
10. Coordinate bid package preparation.
11. Answer bidder questions / issue addenda.
12. Attend pre-bid meeting as needed.
13. Review GC bid package / questions if requested.
14. Coordinate value engineering items.
15. Record rebidding if requested.

### 8. Construction Administration

Source basis:

- SOW lines 891-979.
- Current workflow has only a placeholder sheet.

Nodes to generate:

1. Participate in OAC calls.
2. Provide interpretations of Contract Documents.
3. Review shop drawings, submittals, and finish samples.
4. Respond to RFIs.
5. Issue modifications/minor revisions as required.
6. Review applications for payment, if requested.
7. Review/approve change orders if requested.
8. Visit site at required/appropriate intervals.
9. Report deviations from documents, schedule, or observed quality.
10. Review submittal schedule.
11. Maintain submittal records.
12. Review change requests within 5 business days.
13. Require written approval before scope/schedule/budget changes proceed.

### 9. Closeout / Occupancy / Warranty

Source basis:

- SOW lines 995-1059.
- Current workflow has only a placeholder sheet.

Nodes to generate:

1. Inspect for Substantial Completion.
2. Issue Certificate(s) of Substantial Completion, if applicable.
3. Forward warranties and related documents.
4. Conduct final inspection / final certificate, if requested.
5. Provide completed-project data points.
6. Produce deficiency/punch list.
7. Track each deficiency through resolution.
8. Obtain sign-off by Architect and Owner.
9. Upload As-Constructed Revit/CAD files within required timeframe.
10. Submit As-Constructed Record Documents / Master BIM.
11. Prepare Emergency Evacuation Plan.
12. Submit unflattened building-guide PDF plans.
13. Conduct facility operation/start-up support, if requested.
14. Conduct 11-month warranty / post-C of O walk-through.
15. Notify Owner of warranty claims before expiration.

### 10. Reporting / Metrics / KPI layer

Source basis:

- SOW lines 1301-1485.
- Workflow repeatedly requires PM to review/document all required performance metrics.

Nodes:

1. Track SLA delivery timeframes by project type.
2. Track project delivery timeliness.
3. Track client satisfaction/NPS if applicable.
4. Track design quality / RFIs / rework.
5. Track regulatory compliance / permit feedback.
6. Track cost alignment between DD and CD.
7. Track change order frequency.
8. Maintain monthly reports.
9. Maintain project tracking dashboard/detail report.
10. Maintain design fee reporting, where appropriate outside Pii/BST11 boundary.
11. Support QBR reporting.

---

## Recommended dashboard implication

The workflow should become a source-derived, versioned **Workflow Spine** object, not a static Excel diagram.

Required data fields:

```text
workflow_node_id
source_scope_version/source_sha256
source_line_refs
phase
node_title
node_type: intake | service_order | phase_task | gate | artifact | metric | approval | change_control
contractual_status: required | if_applicable | supplemental | additional_service | owner_provided | not_applicable | unknown
project_relevance: expected | required | not_required | deferred | added | blocked | complete | superseded | unknown
reason
owner/person
role
required_artifact_or_evidence
approval_required
stop_point
last_verified_against_sow
```

This gives Pii the behavior you described:

- if the SOW changes, rerun extraction and compare the workflow spine;
- changed source sections flag affected workflow nodes;
- phase pages update their expected tasks/artifacts/gates;
- users can mark items not required or added with reasons;
- narrative explains deviations from the contractual spine.

---

## Bottom line

Yes, Pii can verify the workflow against the Scope of Work and can generate a workflow from the contractual SOW.

The first-pass result is:

1. **Current workflow is valid as a historical/client-process spine.**
2. **It is not complete enough to rely on without SOW verification.**
3. **A source-derived workflow generator/comparator should become part of Pii.**
4. **When Exhibit A is revised, the workflow must be re-verified and affected nodes should be flagged.**

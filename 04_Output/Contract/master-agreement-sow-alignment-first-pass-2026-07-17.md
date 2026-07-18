# Master Agreement ↔ Exhibit A Scope of Work Alignment — First-Pass Process-Improvement Review

**Date:** 2026-07-17  
**Status:** First-pass source-backed working analysis; not legal advice; not canon until reviewed by Grace/legal/contract stakeholders.  
**Purpose:** Identify alignment issues between the AIA B121 Master Service Agreement, Exhibit A Scope of Work, Service Order logic, and the user's pre-Pii contract comments so Pii can later keep the workflow/SOW/Service Order spine synchronized when contractual language changes.

---

## Sources reviewed

### Master Agreement / MSA bundle

- `00_Source/Contract/Executed Agreement Package/original/master agreement.pdf`
  - SHA-256 in manifest: `98f92d27d752924c186c8bf5ab9b54e9d055cc9fea088673db93c3ffc67d0c54`
  - Image/scanned PDF; normal text extraction produced no text.
  - Key clauses were visually read from rendered page images.
- `00_Source/Contract/Executed Agreement Package/original/!_MSA B121 for Architectural Services AIA B121-2018 - signed.pdf`
  - SHA-256 in manifest: `1e0e503967693825cdf1b4e58d492d1259d98d189620f1760aa0803321d588d4`
  - PyMuPDF text extraction yielded text for exhibits/bundle pages but not the first image-only MSA body pages.

### Scope of Work

- `00_Source/Contract/Exhibit A - Scope of Work/Exhibit A-Scope of Work.docx`
- Access layer: `00_Source/Contract/Exhibit A - Scope of Work/extracted-text.md`
- Source ID: `SRC-CONTRACT-EXHIBIT-A`
- SHA-256: `b40eb296b6c67ecf0bed6ad004e9ebbaf41097296d4112fe784377d1e2315b7e`

### User-created comment / improvement documents

- `00_Source/Contract/Executed Agreement Package/original/!_Remarks on AIA B121 Master Service Agreement.docx`
  - SHA-256 in manifest: `f563b3207ba138e10658d0fc2b12bd478fc41d01fb8b9149281f88ffeb9a1cac`
- `00_Source/Contract/Executed Agreement Package/original/!_Required Reports and Tracking.docx`
  - SHA-256 in manifest: `02dab79a9ab9010d844a4026cc5b173305aeada6df54a67073c58309c2b2f5e5`

---

## Executive summary

The Master Agreement and Exhibit A SOW are broadly aligned around a project-by-project Service Order model, but the user's comments correctly identify several areas where the SOW and project workflow would benefit from added clarity.

The most important alignment issue is not only whether the documents legally conflict. It is that several operational terms are distributed across the MSA, SOW, exhibits, Service Order template, and reporting requirements. Without a Pii-managed contract spine, project teams can miss which document controls which action.

Primary improvement themes:

1. **Clarify Service Order preconditions.** The MSA representation says the Architect visits the project site and reviews local conditions before each Service Order, while the SOW places Site Due Diligence and Field Measurement logic inside SD / Supplemental or Additional Services. This should be reconciled operationally.
2. **Separate Project Schedule from Design Schedule.** The SOW uses both concepts; the MSA payment condition refers to a Project Schedule and says it is defined in Exhibit C, while user remarks state Project Schedule is not defined there. Pii should treat this as a controlled terminology issue.
3. **Clarify consultant/basic-service fee treatment.** The MSA says Basic Services include usual/customary structural, mechanical, and electrical services regardless of whether expressly identified, while fee exhibits/commentary describe engineering and specialty consultants as separate lump-sum proposals per project. The SOW should make this relationship unambiguous.
4. **Make Additional Services/Reimbursables explicit in the Service Order readiness workflow.** The MSA repeatedly conditions compensation/reimbursement on written identification/approval in the Service Order. Pii should turn this into a blocking readiness check.
5. **Turn reporting requirements into a structured dashboard/reporting schema.** The Required Reports and Tracking document and SOW KPI/reporting sections align, but the requirements are scattered. Pii should consolidate them into dashboard fields and recurring reports.
6. **Clarify entity/licensure/territory and stamping/digital-stamp workflow.** These are operationally critical and should become contract setup / Service Order readiness prompts.
7. **Handle innovation/AI scope carefully.** MSA Exhibit H lists Innovation Scope of Work, while the package includes Exhibit H as intentionally omitted; Exhibit M covers responsible AI use. The SOW already mentions AI-assisted design tools as possible enhanced visualization/change-management services. Pii should flag innovation/AI-enabled services as requiring explicit scope/fee/approval mapping.

---

## Alignment findings and improvement opportunities

### 1. Agreement date / execution date / Service Order date

**User comment source:** `!_Remarks...docx`, lines 13-14.  
**MSA page evidence:** rendered MSA page 1 shows the agreement is dated October 2025 in the opening block; rendered MSA page 2 shows §1.1: the `Date of this Agreement` is `January 1, 2026`.  
**Operational concern:** The signed/executed date and the defined Agreement Date differ. The user notes the Agreement Date is required for each Service Order.

**Risk:** Service Orders may reference the wrong operative agreement date if users rely on signature date rather than defined Agreement Date.

**Suggested Pii control:**

- Store both dates separately:
  - `msa_execution_or_signature_date`
  - `defined_date_of_agreement`
- Service Order generation should pull `defined_date_of_agreement` unless counsel/contract admin overrides.
- Dashboard should show a warning if the signature date and defined Agreement Date differ.

**Suggested SOW/process clarification:** Add a contract setup note: “For Service Order references, use the defined Date of Agreement stated in B121 §1.1 unless otherwise directed.”

---

### 2. Service Order precedence over MSA terms

**User comment source:** `!_Remarks...docx`, line 14.  
**MSA page evidence:** rendered MSA page 2, §1.4: in the event of conflict between the Agreement and Service Order information for a Project, the Service Order terms take precedence for services under that Project.

**Operational concern:** Project-specific Service Orders can override general MSA/SOW expectations, but workflow/LCD logic can easily treat SOW defaults as mandatory.

**Suggested Pii control:**

- Every workflow node should carry:
  - `source_default = MSA/SOW`
  - `service_order_override = yes/no`
  - `active_project_rule`
- If a Service Order differs from the SOW-derived workflow spine, the phase page should show: `Modified by Service Order`.

**Suggested SOW/process clarification:** Explicitly state that SOW-derived workflow is a default unless modified by the project Service Order.

---

### 3. Authorized representatives per Service Order

**User comment source:** `!_Remarks...docx`, lines 15-17.  
**MSA page evidence:** rendered MSA page 2 shows:

- §1.6 Owner representative for the Agreement: Senior Director of Owner’s Design Experience or other representatives as identified by Owner.
- §1.6.1 each Service Order identifies an Owner representative for that Service Order.
- §1.7 Architect representative for the Agreement: Kriste Rigby.
- rendered MSA page 3, §1.7.1: each Service Order identifies Architect representative for that Service Order.

**Operational concern:** The Agreement representative is not necessarily the project representative. The user asks whether Service Order representative should be Group PM and Project Architect/Interior Designer/Project Leader.

**Suggested Pii control:**

- Separate fields:
  - `msa_owner_representative`
  - `msa_architect_representative`
  - `service_order_owner_representative`
  - `service_order_architect_representative`
  - `project_manager`
  - `project_leader`
  - `project_architect`
  - `interior_designer`
- Service Order readiness should block if project-specific representatives are missing.

**Suggested SOW/process clarification:** Add a Service Order preparation matrix defining which roles must be identified and which role has authority for each action.

---

### 4. Entity, licensure, territory, and stamping

**User comment source:** `!_Remarks...docx`, lines 4-12.  
**MSA page evidence:** rendered MSA page 1 identifies the Architect as `Grace Healthcare Studios LLC`; rendered page 3, §3.4 representations require licenses/authorizations necessary to act as architect for the Project jurisdiction.

**Operational concern:** The user asks which Grace entity applies, whether different MSAs are needed for different corporations/states, what the territory is, whether digital stamping is allowed per state, and whether correspondence must come from the appropriate corporation.

**Risk:** Incorrect entity/licensure/stamping practice could undermine Service Order execution, project authorization, or permit submission.

**Suggested Pii control:**

- Add `jurisdiction/entity readiness` checks to Service Order initiation:
  - project state/jurisdiction;
  - contracting Grace entity;
  - licensed architect / seal state;
  - digital stamp allowed;
  - correspondence entity requirement;
  - Revit template/version requirement;
  - consultants template/version requirement.

**Suggested SOW/process clarification:** Add a contract administration appendix or Service Order intake prompt: “Confirm Grace contracting entity and jurisdiction-specific licensure/stamping requirements before Service Order execution and before permit deliverables.”

---

### 5. Basic Services vs consultant fee treatment

**User comment source:** `!_Remarks...docx`, lines 18-26.  
**MSA page evidence:** rendered MSA page 3, §2.3 says Basic Services include usual and customary structural, mechanical, and electrical engineering services regardless of whether expressly identified in the SOW or Service Order.  
**SOW evidence:**

- `extracted-text.md` lines 199-207: Architect responsible for coordination of all services and consultants required to fulfill design responsibilities.
- lines 205-207: Architect shall retain consultants required for achieving project requirements; Architect's Consultants clause delegates responsibility for coordination of architectural and engineering design services except services otherwise expressly provided.
- lines 677-679: furniture/medical equipment installation plans are by Owner Alliance Partners, but Architect shows proposed placement and confirms with Owner.
- user remarks cite Exhibits E/F fee language treating structural/MEP/civil/specialty consultants as separate lump sum proposals per project.

**Operational concern:** The SOW should distinguish:

- Basic Services responsibility / coordination obligation;
- engineering/consultant scope required for the project;
- whether consultant fees are included in base fee, separate lump sum, supplemental/additional, or owner-provided.

**Risk:** Teams may either absorb consultant coordination/fees silently or omit required consultant fee proposals from Service Order preparation.

**Suggested Pii control:**

- Service Order readiness should require a consultant responsibility matrix:
  - discipline;
  - required for project?;
  - Basic/Supplemental/Additional/Owner-provided;
  - fee basis;
  - included/excluded from Grace proposal;
  - owner approval status;
  - source evidence.

**Suggested SOW/process clarification:** Add clear language: “Basic Services may include responsibility for coordination of customary engineering services, but project-specific consultant fee proposals and responsibility allocation shall be identified in the Service Order and Exhibits E/F fee basis.” Legal/contract review needed.

---

### 6. Site visit before Service Order vs SOW Site Due Diligence sequence

**User comment source:** `!_Remarks...docx`, lines 27-28.  
**MSA page evidence:** rendered MSA page 4, §3.4 item 4: prior to execution of each Service Order, Architect will visit the Project site and review local conditions, recommend tests/documents/relevant information needed, etc.  
**SOW evidence:**

- lines 383-439: Site Due Diligence and Field Measurement are part of Schematic Design Phase Services and may be Supplemental/Additional Services under Service Order §2.1.2.
- lines 437-439: Field Measurement and Site Due Diligence Report services will be outlined in Service Order Section 2.1.2 Supplemental and Additional Services, approved by Owner/Designated Representative, and should include travel/reimbursable estimate.
- lines 443-445: Detailed Programming/Programming Lite consultation aligns intended scope, schedule and budget for Service Order preparation.

**Operational concern:** The MSA representation sounds like site review happens before Service Order execution, but the SOW places detailed site due diligence inside/after Service Order scope definition.

**Risk:** Teams may be asked to execute a Service Order before seeing the site, while the MSA representation implies a pre-execution site review obligation.

**Suggested Pii control:**

- Add a Service Order readiness decision:
  - `pre-SO site visit completed?`
  - `site visit waived/deferred by Owner?`
  - `SO based solely on Owner-provided information?`
  - `site due diligence included as Supplemental/Additional Service?`
  - `travel/reimbursables included?`
  - `known risk narrative / assumption recorded?`

**Suggested SOW/process clarification:** Add language distinguishing:

1. pre-Service Order preliminary site familiarity/review, if required;
2. Owner-provided-information basis when no pre-SO visit occurs;
3. formal Site Due Diligence / Field Measurement scope as a Service Order item;
4. consequence if existing information is inaccurate.

This is a high-priority clarity improvement.

---

### 7. Additional Services and written authorization before proceeding

**User comment source:** `!_Remarks...docx`, line 29.  
**MSA page evidence:**

- rendered MSA page 4, §4.1-4.2: Architect may provide Additional Services after execution of a Service Order; upon recognizing need, Architect must notify Owner and shall not proceed without Owner written authorization for listed Additional Services.
- rendered MSA page 7, §9.3: Additional Services must be identified in the Service Order with compensation; Owner only required to compensate if agreed in the Service Order.
- SOW lines 1061-1065: Service Order Article 2.1.2 services are not Basic Services but may be required; terms of Change in Services and compensation/schedule adjustment must be memorialized in writing before performance.

**Operational concern:** Additional Services are both a scope classification and a compensation precondition.

**Risk:** Grace may do additional work without compensation if Additional Services are not identified/approved in the Service Order or written change.

**Suggested Pii control:**

- Every task/artifact should classify `basic | supplemental | additional | owner-provided | excluded | unknown`.
- Add a `do-not-proceed` control for work marked Additional Service without written approval/compensation basis.
- Narrative capture should specifically ask: “Is this a change in service or additional service?”

**Suggested SOW/process clarification:** Add a project workflow table of common items likely to become Additional Services: field measurements, site due diligence, non-standard visualization, scan-to-BIM, additional site plan options, major site plan revisions, permit expeditor/pre-submittal meetings if applicable, out-of-sequence/fast-track work.

---

### 8. Reimbursable Expenses must be expressly identified

**User comment source:** `!_Remarks...docx`, lines 30-34.  
**MSA page evidence:** rendered MSA page 8, §9.4.1-9.4.2: reimbursable expenses reimbursed only to extent expressly identified in a Service Order; include travel/subsistence per Exhibit N, permitting/AHJ fees, and site office expenses agreed in writing.  
**SOW evidence:** lines 437-439 require Site Due Diligence/Field Measurement Service Order to include travel time and reimbursable expense estimate.

**Operational concern:** Reimbursables are easy to omit during fast Service Order preparation.

**Suggested Pii control:** Service Order readiness should include a reimbursable-expense checklist:

- travel required?;
- permit/AHJ fees?;
- site office expenses?;
- reimbursable estimate included?;
- pre-approval evidence?;
- Exhibit N compliance check.

---

### 9. Project Schedule vs Design Schedule terminology and payment condition

**User comment source:** `!_Remarks...docx`, lines 35-37.  
**MSA page evidence:** rendered MSA page 9, §9.5.2 item 3: before requesting payment, Architect must have submitted to Owner and Owner accepted in writing the Project Schedule “as defined in Exhibit C” setting dates for schematic design, design development, construction documents, bidding/negotiation, and dates by which Owner actions/decisions/information are required.  
**SOW evidence:**

- lines 249-251: Architect submits schedule for performance of Architect's services, initially including anticipated construction/Substantial Completion dates and Owner review/consultant/AHJ allowances.
- lines 269-275: Project Schedule is prepared by Owner with active Architect participation; Architect updates Design Schedule monthly; Design Milestone Dates are components of Design Schedule.
- lines 467-469: develop Project Design Schedule, including phasing strategy.
- lines 1329-1356: SLA framework guides project schedule; Owner PM manages project schedule/internal approvals; Architect responsible for design delivery components.

**Operational concern:** Terms are overloaded:

- `Project Schedule` appears to be Owner-managed / whole-project schedule;
- `Design Schedule` appears to be Architect services/milestone schedule;
- §9.5.2 ties enforceability/payment to Owner acceptance of `Project Schedule` but user remarks say Project Schedule is not defined in Exhibit C.

**Risk:** Payment, phase readiness, and Service Order completeness can be delayed or disputed if the required schedule artifact is unclear.

**Suggested Pii control:**

- Maintain separate artifacts:
  - `owner_project_schedule`
  - `architect_design_schedule`
  - `design_milestone_dates`
  - `owner_decision_due_dates`
  - `approval_intervals`
- Service Order completion should not go green until required schedule artifact(s) are accepted or formally marked not required/deferred.

**Suggested SOW/process clarification:** Add definitions and responsibility split:

- Owner PM owns Project Schedule.
- Architect actively participates, reviews, comments, and reports status.
- Architect prepares/updates Design Schedule for Architect services.
- Service Order must identify Design Milestone Dates and Owner action/decision/information dates.
- Clarify what schedule must be accepted before invoicing.

This is a high-priority terminology improvement.

---

### 10. BIM / model reliance protocols

**User comment source:** `!_Remarks...docx`, line 38.  
**MSA page evidence:** rendered MSA page 10, §10.9: use/reliance on all or portion of a BIM without written protocols governing use and reliance is at using/relying party’s sole risk and without liability to other parties/contributors.  
**SOW evidence:**

- lines 329-331: deliverables produced in Revit; Revit version no older than two years from current issue; Owner standards for layers, families, line thickness, LOD 300 minimum, naming conventions; refer to Drawing Management.
- lines 1041-1043: As-Constructed Revit/CAD files and Master BIM submitted post-construction.
- lines 1305-1323: cloud repository/access and uploaded maintained files include CAD/RVT, polylining, as-builts/record drawings.

**Operational concern:** SOW requires model production and file delivery, but BIM reliance protocols are not surfaced in the workflow.

**Suggested Pii control:**

- Add BIM/drawing-management artifact controls:
  - Revit version;
  - Owner template compliance;
  - LOD expectation;
  - model reliance protocol present?;
  - Drawing Management Exhibit I compliance;
  - Record model delivery status.

**Suggested SOW/process clarification:** If models are used by Owner/Alliance Partners/contractors beyond viewing/reference, require written BIM-use/reliance protocols or a clear limitation statement.

---

### 11. Innovation / AI / enhanced visualization scope ambiguity

**User comment source:** `!_Remarks...docx`, line 39.  
**MSA page evidence:** rendered MSA page 12, §12.2 lists Exhibit H as `Innovation Scope of Work`; the executed package manifest identifies `Exhibit H-Intentionally Omitted.docx`.  
**SOW evidence:**

- lines 307-327: enhanced visualization / VR / scan-to-BIM / photorealistic rendering / live simulation / AI-assisted design tools / change management collateral may be determined collaboratively and provided as Additional Services.
- lines 1271-1273: Rx Projects and Innovation/Strategic Design Architectural Partner requirements refer to Exhibits G/H if awarded.
- Exhibit M exists for Responsible Use of Artificial Intelligence.

**Operational concern:** MSA exhibit list references an Innovation Scope of Work, but the package includes Exhibit H intentionally omitted. SOW includes possible AI-assisted/enhanced services, but they are not fully scoped/fee-defined.

**Risk:** Innovation/AI work could be requested without clear scope, fee basis, data controls, responsible-use constraints, or deliverable expectations.

**Suggested Pii control:**

- Flag any AI/innovation/enhanced visualization request as:
  - Additional Service unless included in Service Order;
  - subject to Exhibit M responsible AI controls;
  - requiring deliverable definition, data/privacy review, fee basis, and approval.

**Suggested SOW/process clarification:** Add a concise innovation/enhanced-visualization decision table: service type, basic/additional status, approval required, data/privacy constraints, fee basis, deliverables.

---

### 12. Reporting / metrics / project tracking consolidation

**User comment source:** `!_Required Reports and Tracking.docx`.  
**SOW evidence:**

- lines 97-105: internal QC reviews, trends/performance metrics, reporting/program oversight.
- lines 1301-1485: Work Product/Deliverables, Cloud Repository, SLA framework, KPIs, reporting, project tracking, design fee reporting, business reviews.
- Required Reports document lines 30-49 list project tracking report fields.
- Required Reports document lines 86-87 repeat monthly Design Schedule update/status obligation.

**Operational concern:** Reporting requirements are important but scattered. Pii should convert them into a structured dashboard/reporting schema.

**Suggested Pii control:**

- Build a `required_reports_and_tracking` schema with cadence:
  - monthly;
  - quarterly/QBR;
  - semiannual KPI progress;
  - annual;
  - per-project closeout.
- Map dashboard fields to source lines, e.g.:
  - request count;
  - response-time compliance;
  - project phase;
  - project order/installation status;
  - risks/mitigation;
  - deficiency report;
  - schedule/budget final funding milestone status;
  - change orders by type;
  - RFIs by type;
  - design fee reporting.

**Suggested SOW/process clarification:** Attach or incorporate a reporting matrix into the SOW/Service Order process so reporting obligations are not only narrative paragraphs.

---

## Suggested SOW clarity additions

These are not redlined legal clauses; they are process-improvement targets for contract/legal review.

### A. Service Order Readiness / Required Inputs section

Add a checklist-style section that states a Service Order is complete when project-specific required information is supplied, deemed not required, or accepted as an explicit assumption/risk. Include:

- project name/location/number;
- project type and special type;
- contracting entity and jurisdiction;
- owner and architect project representatives;
- scope narrative;
- required phases;
- design milestone dates;
- Owner decision/information due dates;
- compensation/fee basis;
- consultant matrix;
- Additional/Supplemental Services;
- reimbursables;
- site visit/due diligence status;
- project schedule/design schedule artifacts;
- BIM/drawing-management requirements.

### B. Schedule Definitions section

Clarify:

- `Project Schedule`
- `Design Schedule`
- `Design Milestone Dates`
- `Owner review/approval intervals`
- `Owner action/decision/information due dates`
- which schedule must be accepted before invoicing.

### C. Site Visit / Due Diligence Basis section

Clarify whether Service Order is based on:

1. pre-SO site visit;
2. Owner-provided information only;
3. formal Site Due Diligence / Field Measurement included in Service Order;
4. deferred site verification with explicit assumptions and stop points.

### D. Consultant Responsibility / Fee Matrix

Clarify for each discipline:

- Basic responsibility;
- separate consultant fee;
- Owner-provided consultant;
- Alliance Partner;
- Additional/Supplemental Service;
- not required.

### E. Change / Additional Service Control

Make explicit:

- written approval before proceeding;
- Service Order or written change must identify service, compensation, schedule impact;
- Pii/PM should price every change and never silently absorb.

### F. Reporting Matrix

Convert required reporting into a source-backed table with cadence, owner, data source, output format, and dashboard field.

### G. Innovation / AI / Enhanced Visualization Matrix

Tie Exhibit H omission, Exhibit M, and enhanced visualization/AI references together:

- basic vs additional;
- data restrictions;
- owner approval;
- fee basis;
- allowed tools/process;
- deliverables.

---

## Pii implementation implication

This alignment exercise should become a repeatable Pii verification routine:

1. Preserve new/revised contract source.
2. Extract text and source hash.
3. Compare MSA/SOW/Service Order template/exhibits/commentary.
4. Generate or update:
   - contract spine;
   - workflow spine;
   - Service Order readiness checklist;
   - required report schema;
   - phase/task roadmap;
   - known inconsistencies / required clarifications.
5. Flag downstream dashboard/workflow nodes affected by any SOW/MSA revision.

Recommended Pii objects:

```text
contract_clause
sow_requirement
service_order_field
workflow_node
phase_task
reporting_requirement
clarification_issue
project_specific_override
```

Each should carry:

```text
source_file
source_hash
source_page_or_line
status
owner
required_action
last_verified_against_contract
```

---

## First-pass issue register

| ID | Issue | Priority | Source anchors | Recommended action |
|---|---|---:|---|---|
| ALIGN-001 | Defined Agreement Date differs from signature/execution date | Medium | Remarks line 13; MSA page 1-2 §1.1 | Store both dates; Service Orders use defined Agreement Date unless directed otherwise. |
| ALIGN-002 | Service Order overrides Agreement for project-specific conflicts | High | Remarks line 14; MSA page 2 §1.4 | Add Service Order override tracking to Pii workflow nodes. |
| ALIGN-003 | Project-specific Owner/Architect representatives need definition | High | Remarks lines 15-17; MSA page 2-3 §§1.6-1.7.1 | Add representative matrix/check before SO completion. |
| ALIGN-004 | Entity/licensure/territory/digital stamping unresolved | High | Remarks lines 4-12; MSA page 3 §3.4 | Add jurisdiction/entity readiness checks. |
| ALIGN-005 | Basic Services vs separate consultant fees ambiguous operationally | High | Remarks lines 18-26; MSA page 3 §2.3; SOW lines 199-207 | Create consultant responsibility/fee matrix. |
| ALIGN-006 | Pre-SO site visit requirement conflicts with SOW due-diligence sequence | High | Remarks lines 27-28; MSA page 4 §3.4.4; SOW lines 383-439 | Clarify pre-SO basis and formal site due diligence scope. |
| ALIGN-007 | Additional Services compensation depends on SO/written approval | High | Remarks line 29; MSA page 4 §§4.1-4.2; MSA page 7 §9.3; SOW lines 1061-1065 | Add stop-work/add-service approval gate. |
| ALIGN-008 | Reimbursables only if expressly identified in SO | Medium/High | Remarks lines 30-34; MSA page 8 §9.4; SOW lines 437-439 | Add reimbursable checklist to SO readiness. |
| ALIGN-009 | Project Schedule / Design Schedule terminology conflict | High | Remarks lines 35-37; MSA page 9 §9.5.2; SOW lines 249-275, 467-469, 1329-1356 | Define terms and responsibility split; add schedule acceptance checks. |
| ALIGN-010 | BIM reliance protocols not surfaced in workflow | Medium | Remarks line 38; MSA page 10 §10.9; SOW lines 329-331, 1041-1043 | Add BIM protocol/drawing-management checks. |
| ALIGN-011 | Innovation Scope of Work omitted but SOW references innovation/AI-like services | Medium/High | Remarks line 39; MSA page 12 §12.2; SOW lines 307-327, 1271-1273 | Add innovation/AI additional-service matrix. |
| ALIGN-012 | Reporting requirements need structured schema | High | Required Reports doc; SOW lines 1301-1485 | Build reporting/dashboard schema with cadence and source references. |

---

## Bottom line

Your instinct is right: the SOW can be improved to add clarity, and Pii is the right place to make that improvement operational.

The useful experiment is not just to produce a cleaner SOW; it is to make Pii capable of detecting when the SOW, MSA, Service Order, workflow spine, phase tasks, and reporting schema drift apart.

The contract-derived system should answer:

```text
What does the Agreement require?
What does Exhibit A say we do?
What does the Service Order require for this project?
What changed?
What is ambiguous?
What must be clarified before work proceeds?
What must be priced before work is performed?
What evidence proves the current state?
```

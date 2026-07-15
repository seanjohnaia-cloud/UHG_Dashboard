---
record_type: transition_history
status: active
use_case: UC-001
---

# UC-001 Transition History

| ID | Record | From | To | Actor | Reason | Evidence |
|---|---|---|---|---|---|---|
| T-001 | G-001 floor plans | missing | provided_preserved_for_review | user / Hermes | User attached Muncie and Russiaville PDFs after initial email intake. | `SRC-UC001-PDF-MUNCIE-001`; `SRC-UC001-PDF-RUSSIAVILLE-001` |
| T-002 | Muncie PDF | attached | preserved_extracted_rendered | Hermes | Preserve source before interpretation and provide review access layers. | SHA-256 `596d6262e956840505bfb4bbb352ef98ff7cc5fafee8e5a462757cad2a6572b2` |
| T-003 | Russiaville PDF | attached | preserved_extracted_rendered | Hermes | Preserve source before interpretation and provide review access layers. | SHA-256 `d376dcb4880c076ccf07dac6e26bb9b0b63d3b53381892cf76ed103efc864ab2` |
| T-004 | UC-001 experiment scope | two_project_request | muncie_only_active_experiment | user / Hermes | User directed that Russiaville should be ignored for the experiment and Muncie Family Physicians should be the focus. | `experiment-scope.md` |
| T-005 | PM clarification: MEP/SO | pending_pm_answer | grace_only_no_mep_no_so_today | UHG PM via user | PM clarified Grace proposal only, no MEP at this time, no Service Order today; purpose is to hammer out small project fees. | Response preserved at `03_Communications/UC-001 Muncie/incoming-pm-response-001-grace-only-no-so.md`. |
| T-006 | UHG internal review response | fee_proposal_submitted | post_proposal_scope_negotiation | UHG PM via user | UHG requested call to discuss proposed scopes/fees and introduced possible reduced AOR scope: site due diligence then direct to 90% CD for review/final comments. | Response preserved at `03_Communications/UC-001 Muncie/incoming-uhg-review-request-002-reduced-aor-call.md`. |
| T-007 | Response authority constraint | can_respond_quickly | internal_authority_review_required_before_substantive_client_response | user / Hermes | User can coordinate but is on UHG Admin Team, not Clinical Projects team/PIC, and cannot approve fee reduction or scope commitments. | Governance recorded at `02_Records/UC-001 Incomplete Fee Proposal/authority-and-response-governance.md`. |

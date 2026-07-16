---
status: active_source_inventory
layer: source_preservation
project: Pii UHG Dashboard
---

# Source Inventory

## Governance Rule

This vault is the operational Pii build space. External DIF/UHG source material is treated as read-only evidence unless explicitly copied into this vault as preserved source.

No edits are made to:

```text
C:\Obsidian\My Projects\DIF_OS_Vault\V_UHG_Data_Core
```

## Preserved Sources

### SRC-CONTRACT-EXECUTED-PACKAGE

- Title: Executed Contract Package
- Source type: promoted contract folder / mixed PDF, DOCX, TXT
- Inbox source path:
  - `00_Source/Inbox/Contract`
- Preserved active source package:
  - `00_Source/Contract/Executed Agreement Package/original`
- Manifest:
  - `00_Source/Contract/Executed Agreement Package/manifest.md`
- Provenance:
  - `00_Source/Contract/Executed Agreement Package/provenance.md`
- Status: promoted to active source package; not extracted/canonized by promotion event
- Contamination note: original files are preserved in `original/`; derived access layers should be separate.

### SRC-PAC-WORKING-DRAFT-V1-1

- Title: PAC Working Draft v1.1
- Source type: user-provided working draft / framework source
- Original attachment path: `.hermes/desktop-attachments/PAC_Canonical_Data_Model_v1.1.md`
- Preserved path: `00_Source/PAC/Working Drafts/PAC_Canonical_Data_Model_v1.1.md`
- Status: preserved working draft; canonical wording intentionally ignored per user instruction
- Use: discussion source for PAC / Grace project-start framework review; not implemented as developmental structure without approval

### SRC-UC001-CLIENT-SENT-OUTPUTS

- Title: UC-001 Client-Sent Output Artifacts
- Source type: client-sent / intended output evidence
- Inbox source paths:
  - `00_Source/Inbox/SO Development Matrix_Muncie.pdf`
  - `00_Source/Inbox/SO Development Matrix_Russiaville.pdf`
- Preserved active source package:
  - `00_Source/Project Requests/UC-001 Incomplete Fee Proposal/Client-Sent Artifacts/`
- Manifest:
  - `00_Source/Project Requests/UC-001 Incomplete Fee Proposal/Client-Sent Artifacts/manifest.md`
- Status: preserved and extracted for review
- Scope note: Muncie is active experiment output; Russiaville is preserved out-of-scope.
- User design note: artifact has requested data, but gold standard output should add a scope section so request + response form a complete statement of understanding.

### SRC-WORKFLOW-PROJECT-WORKFLOW

- Title: Project Workflow Workbook
- Source type: workflow reference / XLSX
- Inbox source path:
  - `00_Source/Inbox/!_Project Workflow.xlsx`
- Preserved active source package:
  - `00_Source/Workflow/Project Workflow/original/!_Project Workflow.xlsx`
- Manifest:
  - `00_Source/Workflow/Project Workflow/manifest.md`
- Status: active workflow reference; structure inspected only; not canonized
- Note: user clarified Service Order preparation is the first ACT in the workflow.

### SRC-WORKFLOW-LCD-WORKBOOK

- Title: LCD Workbook / possible LCW alias
- Source type: human attempt at project management as data / XLSX
- Inbox source path:
  - `00_Source/Inbox/!_LCD Workbook.xlsx`
- Preserved active source package:
  - `00_Source/Workflow/LCD Workbook/original/!_LCD Workbook.xlsx`
- Manifest:
  - `00_Source/Workflow/LCD Workbook/manifest.md`
- Status: active workflow/data-model reference; structure inspected only; not canonized
- Note: user clarified this workbook tries to capture everything needed to manage the project as data, not context.

### SRC-CONTRACT-EXHIBIT-A

- Title: Exhibit A — Scope of Work
- Source type: contract exhibit / DOCX
- Original read-only DIF path:
  - `C:\Obsidian\My Projects\DIF_OS_Vault\V_UHG_Data_Core\03_Draft_Artifacts\Contract\Exhibit A-Scope of Work.docx`
- Hermes attachment path:
  - `C:\Obsidian\My Projects\Pi Vault\UHG_Dashboard\.hermes\desktop-attachments\Exhibit A-Scope of Work.docx`
- Preserved local source copy:
  - `00_Source/Contract/Exhibit A - Scope of Work/Exhibit A-Scope of Work.docx`
- Access/extraction layer:
  - `00_Source/Contract/Exhibit A - Scope of Work/extracted-text.md`
- SHA-256:
  - `b40eb296b6c67ecf0bed6ad004e9ebbaf41097296d4112fe784377d1e2315b7e`
- Status: preserved and text-extracted for review
- Contamination note: source was copied into this vault; DIF source was not modified.

## Candidate External Sources — Read-Only Inventory Only

Located under:

```text
C:\Obsidian\My Projects\DIF_OS_Vault\V_UHG_Data_Core
```

This project may later preserve selected copies of contract exhibits, draft artifacts, or intake chats as source records. Do not extract/canonize from these until explicitly selected for the active use case.

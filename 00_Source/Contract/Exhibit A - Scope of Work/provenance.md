---
source_id: SRC-CONTRACT-EXHIBIT-A
title: Exhibit A — Scope of Work
status: preserved_and_extracted
layer: source_preservation
---

# Provenance — Exhibit A Scope of Work

## Source Identity

- Source record ID: `SRC-CONTRACT-EXHIBIT-A`
- Source title: `Exhibit A — Scope of Work`
- File type: DOCX
- SHA-256: `b40eb296b6c67ecf0bed6ad004e9ebbaf41097296d4112fe784377d1e2315b7e`

## Source Locations

Original read-only DIF source:

```text
C:\Obsidian\My Projects\DIF_OS_Vault\V_UHG_Data_Core\03_Draft_Artifacts\Contract\Exhibit A-Scope of Work.docx
```

Hermes attachment source:

```text
C:\Obsidian\My Projects\Pi Vault\UHG_Dashboard\.hermes\desktop-attachments\Exhibit A-Scope of Work.docx
```

Preserved Pii vault source copy:

```text
00_Source/Contract/Exhibit A - Scope of Work/Exhibit A-Scope of Work.docx
```

Text extraction/access layer:

```text
00_Source/Contract/Exhibit A - Scope of Work/extracted-text.md
```

## Preservation Result

The preserved Pii vault copy, Hermes attachment, and read-only DIF source produced the same SHA-256 hash:

```text
b40eb296b6c67ecf0bed6ad004e9ebbaf41097296d4112fe784377d1e2315b7e
```

## Extraction Method

Text was extracted using Python standard-library DOCX parsing:

- `zipfile` to read `word/document.xml`
- `xml.etree.ElementTree` to extract paragraph/table text

No changes were made to the DIF source vault.

## Use Boundary

This source may support requirements extraction for Pii and UC-001, but extracted operational requirements are not yet canonical until they are recorded with evidence references and validated under Layer 1 governance.

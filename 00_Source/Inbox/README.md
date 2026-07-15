---
record_type: source_deposit_readme
status: active
layer: source_preservation
---

# Source Inbox

Use this directory to deposit artifacts created outside Pii or received from outside systems before they are extracted, interpreted, or turned into records.

## Directory

```text
00_Source/Inbox
```

## Rule

Artifacts placed here are **source candidates**, not operational facts.

Do not edit deposited source files in place. If a source needs annotation, extraction, conversion, or normalization, create an access layer or derived record elsewhere while preserving the original file.

## Recommended Pattern

For each source drop, create a subfolder:

```text
00_Source/Inbox/YYYY-MM-DD_short-source-name/
```

Inside the subfolder:

```text
original/        # untouched deposited files
extracted/       # text/OCR/rendered/access layers
provenance.md    # where it came from, when, why, hash if possible
notes.md         # non-canonical handling notes if needed
```

## Current Experiment Boundary

For the current UC-001 experiment, prioritize sources related to:

```text
Muncie Family Physicians / IN125
```

Russiaville artifacts may be preserved, but they should be marked `preserved_out_of_scope_for_now` unless intentionally reactivated.

## Contamination Boundary

If an artifact originates from DIF, SharePoint, email, CAD/BIM, PDF, or another external system, copy it here first. Do not work directly against the external source as if it were Pii's canonical record.

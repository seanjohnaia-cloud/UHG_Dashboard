---
record_type: pac_lcdw_relationship_model
status: draft_for_review
scope: Pii developmental structure
---

# PAC / LCD-W / UHG-Specific LCD Relationship Model

## User Clarification

The current UHG work should be understood as:

```text
Grace is doing project-start / proposal / activation work specifically for UHG,
using the UHG-specific LCD/LCW because UHG has an established framework that is contractually binding.
```

However, Grace still needs the broader PAC information to actually start a project once there is a notice to proceed — and really before that, Grace should begin with common data fields.

On most projects, a generic `LCD-W` will likely suffice.

This UHG situation is atypical because the client has an established framework that is contractually binding.

## Corrected Relationship

```text
PAC = Grace-wide framework for processes/info required to start a project
LCD-W = typical/common Grace project data worksheet that usually satisfies project data needs
UHG LCD/LCW = client-specific, contractually binding UHG framework / workbook variant
```

## Layering

| Layer | Role | Typical / Atypical |
|---|---|---|
| Common Data Fields | Earliest shared project-start data surface | Universal / Grace-wide |
| PAC | Governs what Grace needs to start a project responsibly | Universal / Grace-wide |
| Generic LCD-W | Standard internal project data worksheet for most projects | Typical |
| UHG LCD/LCW | UHG-specific data/workflow framework tied to contract/training | Atypical / client-specific |
| Notice to Proceed | Trigger that allows the project to truly start, assuming PAC info/authority are sufficient | Project-specific |

## Timing Concept

The PAC information does not wait until after Notice to Proceed.

Better timing:

```text
early request / opportunity / proposal stage
→ begin common data fields
→ identify missing PAC information
→ clarify scope/fee/authority/schedule
→ receive NTP or equivalent authorization
→ confirm PAC sufficiency
→ start project
```

## UHG-Specific Consequence

For UHG projects, Grace cannot simply use the generic LCD-W if the contractually binding UHG framework requires a specific structure, fields, Service Order logic, Schedule E/F logic, reporting, or workflow expectations.

Therefore, UHG projects may require:

```text
PAC common fields
+ generic Grace LCD-W concepts
+ UHG-specific LCD/LCW contract fields
+ UHG training/workflow rules
+ reality-specific project clarification
```

## Governance Note

This is a relationship model, not yet an implemented structure. Because PAC changes developmental structure, it remains draft-for-review until approved.

## Working Design Implication

Pii should eventually support a common PAC core with project/client overlays:

```text
PAC Core
  ├─ Generic LCD-W overlay
  └─ UHG contract/LCD/LCW overlay
```

But the overlay architecture should be reviewed before implementation.

# Pii Team Dashboard — Seed Layer

Status: implementation seed / non-authoritative prototype input

This folder is for the Grace/team-side **Pii Team Dashboard / Pii Console** lens. It is intentionally separate from `05_Dashboard/`, which remains the client-facing Streamlit dashboard modeled around the UHG contractual/LCD structure.

## Standing

These files are seed data for design/prototype work. They do not create accepted project authority. Claims should remain traceable to governed synthesis, requirements notes, source artifacts, or later human-approved decisions.

## Source orientation

The dashboard seed is based on this relationship:

```text
PAC = Grace-wide project-start origin/intake framework
Generic LCD-W = typical/common Grace project data worksheet for most projects
UHG LCD/LCW = client-specific, contractually binding UHG workbook/framework
Pii Team Dashboard = Grace command center for project management, using PAC/LCD-W/UHG overlays as source/lens inputs
```

Primary references:

- `_governed/synthesis/concepts/pii-console-team-side-architecture.md`
- `01_Requirements/PAC - LCD-W - UHG Relationship Model.md`
- `01_Requirements/Concept Boundary - LCW-LCD vs PAC.md`
- `00_Source/PAC/Working Drafts/PAC_Canonical_Data_Model_v1.1.md`
- `sketches/001-amber-console/README.md`
- `sketches/002-sonar-bunker/README.md`
- `sketches/003-patchbay-modular/README.md`

Pi v1 WikiLLM / PI model references loaded for alignment:

- `C:\Obsidian\My Projects\PI v1\_governed\synthesis\concepts\project-intelligence-current-state.md`
- `C:\Obsidian\My Projects\PI v1\_governed\synthesis\concepts\pii-operating-workflow.md`
- `C:\Obsidian\My Projects\PI v1\_governed\synthesis\concepts\pac-project-start.md`
- `C:\Obsidian\My Projects\PI v1\_governed\synthesis\concepts\lcw-lcd-uhg-relationship.md`
- `C:\Obsidian\My Projects\PI v1\_governed\synthesis\concepts\grace-startup-a-f-requirements.md`
- `C:\Obsidian\My Projects\PI v1\_governed\synthesis\concepts\dashboard-state-model.md`
- `C:\Obsidian\My Projects\PI v1\_governed\synthesis\concepts\field-truth-states.md`
- `C:\Obsidian\My Projects\PI v1\_governed\synthesis\concepts\process-revision-integration-protocols.md`

## Boundary rules

- Do not collapse this into the Streamlit client dashboard.
- Do not treat the UHG LCW/LCD workbook as the universal PAC model.
- Do not overwrite PAC origin truth with later validation or operational truth.
- Keep Institutional Learning out of this dashboard; that remains DIF-side.
- Treat modules as lenses onto shared project data, not separate data copies.
- Treat dashboard status as a view of governed/project state, not authority.
- Preserve field truth states before readiness, output, or routing decisions.
- Keep Centerline as a deferred/adjacent integration dependency unless the scope is reopened; use "Centerline-style handoff" as a context pattern, not a live integration assumption.
- Use Archive, not Quarantine, as the fourth console function; unresolved/conflict states remain visible through field truth, admissibility, verification, risk/gap routing, and archive/source preservation.

## Initial seed files

- `data/project-context.seed.json` — Centerline-style launch handoff and project context assumptions.
- `data/module-catalog.seed.json` — stable team-side module nodes.
- `data/views.seed.json` — clustering/lens definitions over the same node set.
- `data/dependency-edges.seed.json` — initial data-dependency edges for propagation/integrity.

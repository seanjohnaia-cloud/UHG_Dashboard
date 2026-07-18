# Pii Portfolio + Project Dashboard Architecture Implementation Plan

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task.

**Goal:** Add a Pii launch architecture where users can open/create either a Portfolio Dashboard or a Project Dashboard, select modules, and keep module development branches separate from approved dashboard modules.

**Architecture:** Introduce a thin launcher/router layer above the current Project Dashboard. Keep `project_home_dashboard.py` working while extracting durable concepts into configuration files and panel modules over time. Portfolio Dashboard and Project Dashboard become dashboard types; LCD, Metrics, etc. become selectable modules that can be approved or under development.

**Tech Stack:** Python, Streamlit, YAML/JSON config, existing `05_Dashboard/project_home_dashboard.py`, `streamlit.testing.v1.AppTest`, `unittest`.

---

## Current Context

The current repo is already the Pii UHG Dashboard working home:

```text
C:\Obsidian\My Projects\Pi Vault\UHG_Dashboard
```

Current app surface:

```text
05_Dashboard/project_home_dashboard.py
```

Current state:

- LCD Manual Entry and Metrics are Streamlit pages/functions inside `project_home_dashboard.py`.
- There are no separate `LCD Panel` or `Metrics Panel` branch folders yet.
- Source workbook and PDFs are preserved under `00_Source/Workflow/LCD Workbook/` and should not be moved into dashboard code.
- The desired product hierarchy is:

```text
Pii
├── Portfolio Dashboard
│   ├── portfolio modules
│   └── child Project Dashboards
└── Project Dashboard
    └── selectable project modules
```

Important product rule:

- The dashboard can be one running experience.
- The approved code/config and development branches should remain separated.
- Portfolio Dashboard is the correct term, not “master dashboard.”

---

## Proposed Target Structure

Implement gradually toward:

```text
05_Dashboard/
  pii_launcher.py
  project_home_dashboard.py                 # existing project dashboard shell, kept running

  dashboard_types/
    __init__.py
    portfolio_dashboard.py                  # Portfolio Dashboard shell
    project_dashboard.py                    # Project Dashboard shell / adapter around current app

  modules/
    approved/
      __init__.py
      portfolio_home.py
      project_index.py
      cross_project_metrics.py
      contract_governance.py
      project_home.py
      lcd_baseline.py
      project_metrics.py

    development/
      lcd_baseline/
        README.md
        lcd_baseline.py
      project_metrics/
        README.md
        project_metrics.py

  dashboard_configs/
    uhg_portfolio.json
    fairview_urgent_care.json

  test_project_home_dashboard.py
  test_pii_launcher.py
```

Near-term implementation should avoid a large rewrite. First add config and launcher. Then extract modules one at a time.

---

## Dashboard Type Model

Create two dashboard types:

### Portfolio Dashboard

Purpose:

- Multi-project oversight.
- UHG account/portfolio intelligence.
- Child Project Dashboard index.
- Cross-project metrics and SLA/KPI views.
- Contract/SOW governance across projects.

Example modules:

```text
Portfolio Home
Project Index
Cross-Project Metrics
SLA / KPI Reporting
Contract / SOW Governance
Risk / Deficiency Trends
Executive Report Generator
```

### Project Dashboard

Purpose:

- Single project working container.
- Project Home.
- LCD/Baseline entry.
- Scope/Budget/Compensation.
- Design Schedule.
- Service Order Review.
- Project Metrics.

Example modules:

```text
Project Home
LCD / Baseline
Project Scope
Project Budget
Compensation
Design Schedule
Consultants
Alliance Partners
Contracts
Service Order Review
Metrics
Activation Gates
Deficiency Report
Change Order Log
Closeout
```

---

## Config Shapes

### `05_Dashboard/dashboard_configs/uhg_portfolio.json`

```json
{
  "dashboard_id": "uhg_portfolio",
  "dashboard_type": "portfolio",
  "display_name": "UHG Portfolio Dashboard",
  "status": "development",
  "active_modules": [
    "portfolio_home",
    "project_index",
    "cross_project_metrics",
    "sla_kpi_reporting",
    "contract_governance"
  ],
  "child_dashboards": [
    "fairview_urgent_care"
  ]
}
```

### `05_Dashboard/dashboard_configs/fairview_urgent_care.json`

```json
{
  "dashboard_id": "fairview_urgent_care",
  "dashboard_type": "project",
  "display_name": "Fairview Urgent Care",
  "parent_dashboard": "uhg_portfolio",
  "status": "development",
  "active_modules": [
    "project_home",
    "lcd_baseline",
    "project_scope",
    "project_budget",
    "compensation",
    "design_schedule",
    "consultants",
    "alliance_partners",
    "contracts",
    "service_order_review",
    "project_metrics"
  ]
}
```

---

## Module Registry Shape

Add a Python registry first. Later it can become JSON/YAML.

Proposed file:

```text
05_Dashboard/module_registry.py
```

Initial code shape:

```python
from __future__ import annotations

MODULE_REGISTRY = {
    "portfolio_home": {
        "label": "Portfolio Home",
        "dashboard_types": ["portfolio"],
        "status": "development",
    },
    "project_index": {
        "label": "Project Index",
        "dashboard_types": ["portfolio"],
        "status": "development",
    },
    "cross_project_metrics": {
        "label": "Cross-Project Metrics",
        "dashboard_types": ["portfolio"],
        "status": "development",
    },
    "contract_governance": {
        "label": "Contract / SOW Governance",
        "dashboard_types": ["portfolio"],
        "status": "development",
    },
    "project_home": {
        "label": "Project Home",
        "dashboard_types": ["project"],
        "status": "approved",
    },
    "lcd_baseline": {
        "label": "LCD / Baseline",
        "dashboard_types": ["project"],
        "status": "development",
    },
    "project_metrics": {
        "label": "Metrics",
        "dashboard_types": ["project", "portfolio"],
        "status": "development",
    },
}


def modules_for_dashboard_type(dashboard_type: str) -> dict[str, dict[str, object]]:
    return {
        key: value
        for key, value in MODULE_REGISTRY.items()
        if dashboard_type in value["dashboard_types"]
    }
```

---

# Task Plan

## Task 1: Add Tests for Dashboard Config Loading

**Objective:** Define dashboard config behavior before implementation.

**Files:**

- Create: `05_Dashboard/test_pii_launcher.py`
- Create later: `05_Dashboard/dashboard_config.py`
- Create later: `05_Dashboard/dashboard_configs/uhg_portfolio.json`
- Create later: `05_Dashboard/dashboard_configs/fairview_urgent_care.json`

**Step 1: Write failing tests**

Create `05_Dashboard/test_pii_launcher.py` with tests that expect:

- Config loader can list dashboards.
- UHG Portfolio config loads as `dashboard_type == "portfolio"`.
- Fairview config loads as `dashboard_type == "project"`.
- Fairview links to parent `uhg_portfolio`.

**Step 2: Run failing test**

```bash
python -m unittest 05_Dashboard/test_pii_launcher.py -v
```

Expected failure:

```text
ModuleNotFoundError: No module named 'dashboard_config'
```

**Step 3: Implement minimal config loader**

Create `05_Dashboard/dashboard_config.py` with:

```python
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

APP_DIR = Path(__file__).resolve().parent
CONFIG_DIR = APP_DIR / "dashboard_configs"


def load_dashboard_config(dashboard_id: str) -> dict[str, Any]:
    path = CONFIG_DIR / f"{dashboard_id}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def list_dashboard_configs() -> list[dict[str, Any]]:
    return [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(CONFIG_DIR.glob("*.json"))
    ]
```

**Step 4: Add config files**

Create:

- `05_Dashboard/dashboard_configs/uhg_portfolio.json`
- `05_Dashboard/dashboard_configs/fairview_urgent_care.json`

Use the config shapes above.

**Step 5: Verify**

```bash
python -m unittest 05_Dashboard/test_pii_launcher.py -v
```

Expected:

```text
OK
```

---

## Task 2: Add Module Registry Tests and Implementation

**Objective:** Add the selectable module catalog for Portfolio vs Project dashboards.

**Files:**

- Modify: `05_Dashboard/test_pii_launcher.py`
- Create: `05_Dashboard/module_registry.py`

**Step 1: Write failing tests**

Add tests that assert:

- Portfolio modules include `portfolio_home`, `project_index`, and `cross_project_metrics`.
- Project modules include `project_home`, `lcd_baseline`, and `project_metrics`.
- `lcd_baseline` is not a Portfolio-only module.

**Step 2: Run failing tests**

```bash
python -m unittest 05_Dashboard/test_pii_launcher.py -v
```

Expected failure:

```text
ModuleNotFoundError: No module named 'module_registry'
```

**Step 3: Implement `module_registry.py`**

Use the module registry shape above.

**Step 4: Verify**

```bash
python -m unittest 05_Dashboard/test_pii_launcher.py -v
```

Expected:

```text
OK
```

---

## Task 3: Add Pii Launcher Shell

**Objective:** Add a launcher that lets the user open/create Portfolio or Project dashboards without replacing the current app yet.

**Files:**

- Create: `05_Dashboard/pii_launcher.py`
- Modify: `05_Dashboard/test_pii_launcher.py`

**Step 1: Write failing AppTest smoke test**

Test expected launcher UI text:

- `Launch Pii`
- `Open Existing Dashboard`
- `Create New Dashboard`
- `Portfolio Dashboard`
- `Project Dashboard`

**Step 2: Run failing test**

```bash
python -m unittest 05_Dashboard/test_pii_launcher.py -v
```

Expected failure because `pii_launcher.py` does not exist.

**Step 3: Implement minimal `pii_launcher.py`**

Use Streamlit radio/buttons for now:

```python
from __future__ import annotations

import streamlit as st

from dashboard_config import list_dashboard_configs
from module_registry import modules_for_dashboard_type


def render_launcher() -> None:
    st.set_page_config(page_title="Pii Launcher", layout="wide")
    st.title("Launch Pii")

    mode = st.radio("What do you want to do?", ["Open Existing Dashboard", "Create New Dashboard"])

    if mode == "Open Existing Dashboard":
        st.subheader("Open Existing Dashboard")
        dashboards = list_dashboard_configs()
        labels = [f"{item['display_name']} ({item['dashboard_type']})" for item in dashboards]
        st.selectbox("Dashboard", labels)

    else:
        st.subheader("Create New Dashboard")
        dashboard_type = st.radio("Dashboard Type", ["Portfolio Dashboard", "Project Dashboard"])
        normalized_type = "portfolio" if dashboard_type == "Portfolio Dashboard" else "project"
        st.text_input("Dashboard Name")
        st.multiselect(
            "Select Modules",
            [module["label"] for module in modules_for_dashboard_type(normalized_type).values()],
        )
        st.button(f"Create {dashboard_type}")


if __name__ == "__main__":
    render_launcher()
```

**Step 4: Verify**

```bash
python -m unittest 05_Dashboard/test_pii_launcher.py -v
```

Expected:

```text
OK
```

Manual run:

```bash
python -m streamlit run 05_Dashboard/pii_launcher.py --server.port 8502
```

---

## Task 4: Add Portfolio Dashboard Shell

**Objective:** Create a first Portfolio Dashboard view that can show child project dashboards and portfolio modules.

**Files:**

- Create: `05_Dashboard/dashboard_types/__init__.py`
- Create: `05_Dashboard/dashboard_types/portfolio_dashboard.py`
- Modify: `05_Dashboard/test_pii_launcher.py`

**Step 1: Write tests**

Assert Portfolio Dashboard AppTest renders:

- `UHG Portfolio Dashboard`
- `Portfolio Home`
- `Project Index`
- `Fairview Urgent Care`

**Step 2: Implement minimal shell**

`portfolio_dashboard.py` should:

- Load `uhg_portfolio` config.
- Display its name.
- Display active module labels.
- Display child dashboard IDs resolved to display names.

**Step 3: Verify**

```bash
python -m unittest 05_Dashboard/test_pii_launcher.py -v
```

---

## Task 5: Keep Current Project Dashboard as Project Shell

**Objective:** Treat the current `project_home_dashboard.py` as the first Project Dashboard implementation without moving code yet.

**Files:**

- Modify: `05_Dashboard/project_home_dashboard.py`
- Modify: `05_Dashboard/test_project_home_dashboard.py`

**Step 1: Add module/dashboard labels**

Add a visible caption or config-driven loaded label:

```text
Dashboard Type: Project Dashboard
Parent Portfolio: UHG Portfolio Dashboard
```

**Step 2: Add tests**

Verify the current app still renders Project Dashboard and LCD/Metrics pages.

**Step 3: Verify**

```bash
python -m unittest 05_Dashboard/test_project_home_dashboard.py -v
```

---

## Task 6: Create Development Branch Folders for LCD and Metrics

**Objective:** Add branch folders without moving source artifacts or breaking current app.

**Files:**

- Create: `05_Dashboard/modules/development/lcd_baseline/README.md`
- Create: `05_Dashboard/modules/development/project_metrics/README.md`
- Create: `05_Dashboard/modules/approved/README.md`

**README content should state:**

For LCD:

```markdown
# LCD Baseline Module — Development Branch

Status: development / prototype

Purpose: In-dashboard Excel-style LCD entry surface with controlled workbook pick lists, PDD defaults, and future Save LCD Draft behavior.

Promotion requirement:
- AppTest smoke checks pass.
- User approves worksheet resemblance and interaction model.
- Save/persistence path is defined before canonical baseline use.
```

For Metrics:

```markdown
# Project Metrics Module — Development Branch

Status: development / prototype

Purpose: Project-level metrics and UHG SOW/KPI-aligned reporting surface.

Promotion requirement:
- SOW/KPI source mapping reviewed.
- Metrics remain distinct from Portfolio cross-project metrics.
- AppTest smoke checks pass.
```

**Verification:**

```bash
python - <<'PY'
from pathlib import Path
for path in [
    '05_Dashboard/modules/development/lcd_baseline/README.md',
    '05_Dashboard/modules/development/project_metrics/README.md',
    '05_Dashboard/modules/approved/README.md',
]:
    assert Path(path).exists(), path
print('branch folders verified')
PY
```

---

## Task 7: Extract LCD Module Only After Approval

**Objective:** Avoid contaminating the current working dashboard while preparing modular extraction.

**Do not do this until user approves current LCD behavior.**

When approved:

- Move LCD constants/helpers/render function from `project_home_dashboard.py` into:

```text
05_Dashboard/modules/development/lcd_baseline/lcd_baseline.py
```

- Import it from `project_home_dashboard.py`.

Expected import:

```python
from modules.development.lcd_baseline.lcd_baseline import render_lcd_manual_entry
```

**Risk:** Streamlit imports from nested folders may require `__init__.py` files.

Add:

```text
05_Dashboard/modules/__init__.py
05_Dashboard/modules/development/__init__.py
05_Dashboard/modules/development/lcd_baseline/__init__.py
```

**Verification:**

```bash
python -m unittest 05_Dashboard/test_project_home_dashboard.py -v
```

Run the Streamlit app and visually confirm LCD page still renders.

---

## Task 8: Extract Metrics Module Separately

**Objective:** Keep Metrics as its own project module and avoid mixing it with Portfolio cross-project metrics.

When ready:

- Move project-level metrics constants/helpers/render function to:

```text
05_Dashboard/modules/development/project_metrics/project_metrics.py
```

- Keep future Portfolio metrics separate:

```text
05_Dashboard/modules/approved/cross_project_metrics.py
```

**Verification:**

```bash
python -m unittest 05_Dashboard/test_project_home_dashboard.py -v
```

---

## Task 9: Add Promotion Metadata

**Objective:** Establish approved vs development status without implementing full governance tooling yet.

**Files:**

- Create: `05_Dashboard/modules/development/lcd_baseline/module_status.json`
- Create: `05_Dashboard/modules/development/project_metrics/module_status.json`

Example:

```json
{
  "module_id": "lcd_baseline",
  "status": "development",
  "dashboard_types": ["project"],
  "promotion_state": "not_approved",
  "requires_user_approval": true,
  "notes": "Prototype currently supports Excel-style manual entry and controlled pick lists; persistence not yet implemented."
}
```

**Verification:**

Read and assert JSON parses.

---

## Task 10: Decide Launcher Integration Strategy

**Objective:** Choose whether the user opens `pii_launcher.py` first or current `project_home_dashboard.py` first.

Options:

### Option A — Keep Current App as Default

Use current URL for project work:

```bash
python -m streamlit run 05_Dashboard/project_home_dashboard.py --server.port 8501
```

Use launcher separately:

```bash
python -m streamlit run 05_Dashboard/pii_launcher.py --server.port 8502
```

Best for low-risk iteration.

### Option B — Make Launcher the Default

Change docs/scripts so Pii starts at:

```bash
python -m streamlit run 05_Dashboard/pii_launcher.py --server.port 8501
```

Best once launcher can route to project dashboards.

Recommended now: **Option A** until Project Dashboard routing is stable.

---

## Validation Commands

Run after each implementation slice:

```bash
python -m unittest 05_Dashboard/test_project_home_dashboard.py -v
python -m unittest 05_Dashboard/test_pii_launcher.py -v
python -m py_compile 05_Dashboard/project_home_dashboard.py 05_Dashboard/pii_launcher.py
```

For focused ad-hoc runtime checks, use Streamlit AppTest in a temp script with `hermes-verify-` prefix under OS temp dir, then clean it up.

Manual browser checks:

```bash
python -m streamlit run 05_Dashboard/project_home_dashboard.py --server.port 8501
python -m streamlit run 05_Dashboard/pii_launcher.py --server.port 8502
```

---

## Risks and Tradeoffs

### Risk: Too much refactor too soon

Mitigation:

- Add launcher/config first.
- Do not extract LCD/Metrics until the user approves the prototype behavior.

### Risk: Portfolio metrics and project metrics collapse into one thing

Mitigation:

- Use separate module IDs:
  - `project_metrics`
  - `cross_project_metrics`

### Risk: Source folders get moved into dashboard code

Mitigation:

- Keep `00_Source` preserved.
- Dashboard modules read/source-map from `00_Source`; they do not own source artifacts.

### Risk: “Development branch” becomes invisible to user

Mitigation:

- Add visible status labels in module pages:

```text
Module Status: Development Prototype
Promotion: Not Approved
```

### Risk: Launcher implies full persistence before it exists

Mitigation:

- Label create/open flows as prototype until config writing is implemented.
- Initially create static configs by code, not user-created files.

---

## Open Questions

1. Should UHG Portfolio Dashboard be the default landing page once launcher exists?
2. Should standalone Project Dashboards be allowed without a Portfolio parent?
3. Should development modules be visible in the UI, or only selected through developer config?
4. What approval act promotes a module from development to approved?
5. Should module selection be per Portfolio Dashboard, per Project Dashboard, or both?

---

## Recommended Implementation Order

1. Add dashboard configs and loader.
2. Add module registry.
3. Add Pii launcher prototype.
4. Add Portfolio Dashboard shell.
5. Add branch folders and module status metadata.
6. Keep current Project Dashboard running.
7. Extract LCD module only after user approves current behavior.
8. Extract Metrics separately.
9. Add persistence / Save LCD Draft later.

This gives the hierarchy now without destabilizing the working dashboard prototype.

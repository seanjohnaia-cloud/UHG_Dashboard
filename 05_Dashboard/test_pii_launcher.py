"""Regression tests for Pii launcher, Portfolio Dashboard, and module branches."""

from __future__ import annotations

import importlib
import json
import pathlib
import sys
import unittest

from streamlit.testing.v1 import AppTest

DASHBOARD_DIR = pathlib.Path(__file__).resolve().parent
if str(DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(DASHBOARD_DIR))


class PiiLauncherArchitectureTests(unittest.TestCase):
    def test_dashboard_configs_define_portfolio_and_project_relationship(self) -> None:
        dashboard_config = importlib.import_module("dashboard_config")

        portfolio = dashboard_config.load_dashboard_config("uhg_portfolio")
        project = dashboard_config.load_dashboard_config("fairview_urgent_care")
        dashboards = dashboard_config.list_dashboard_configs()

        self.assertEqual(portfolio["dashboard_type"], "portfolio")
        self.assertEqual(portfolio["display_name"], "UHG Portfolio Dashboard")
        self.assertIn("fairview_urgent_care", portfolio["child_dashboards"])
        self.assertEqual(project["dashboard_type"], "project")
        self.assertEqual(project["parent_dashboard"], "uhg_portfolio")
        self.assertIn("lcd_baseline", project["active_modules"])
        self.assertIn("project_metrics", project["active_modules"])
        self.assertGreaterEqual(len(dashboards), 2)

    def test_module_registry_splits_portfolio_and_project_modules(self) -> None:
        module_registry = importlib.import_module("module_registry")

        portfolio_modules = module_registry.modules_for_dashboard_type("portfolio")
        project_modules = module_registry.modules_for_dashboard_type("project")

        self.assertIn("portfolio_home", portfolio_modules)
        self.assertIn("project_index", portfolio_modules)
        self.assertIn("cross_project_metrics", portfolio_modules)
        self.assertIn("contract_governance", portfolio_modules)
        self.assertNotIn("lcd_baseline", portfolio_modules)
        self.assertIn("project_home", project_modules)
        self.assertIn("lcd_baseline", project_modules)
        self.assertIn("project_metrics", project_modules)
        self.assertNotIn("project_index", project_modules)

    def test_launcher_renders_open_create_and_dashboard_type_options(self) -> None:
        app = AppTest.from_file(str(DASHBOARD_DIR / "pii_launcher.py")).run(timeout=10)

        self.assertEqual(list(app.exception), [])
        self.assertIn("Launch Pii", [title.value for title in app.title])
        radio_labels = [radio.label for radio in app.radio]
        self.assertIn("What do you want to do?", radio_labels)
        self.assertIn("Open Existing Dashboard", app.radio[0].options)
        self.assertIn("Create New Dashboard", app.radio[0].options)

        app.radio[0].set_value("Create New Dashboard").run(timeout=10)
        self.assertEqual(list(app.exception), [])
        dashboard_type_radio = next(radio for radio in app.radio if radio.label == "Dashboard Type")
        self.assertIn("Portfolio Dashboard", dashboard_type_radio.options)
        self.assertIn("Project Dashboard", dashboard_type_radio.options)

    def test_portfolio_dashboard_shell_lists_child_project_and_modules(self) -> None:
        app = AppTest.from_file(str(DASHBOARD_DIR / "dashboard_types" / "portfolio_dashboard.py")).run(timeout=10)

        self.assertEqual(list(app.exception), [])
        self.assertIn("UHG Portfolio Dashboard", [title.value for title in app.title])
        page_text = "\n".join(str(markdown.value) for markdown in app.markdown)
        self.assertIn("Portfolio Home", page_text)
        self.assertIn("Project Index", page_text)
        self.assertIn("Cross-Project Metrics", page_text)
        self.assertIn("Fairview Urgent Care", page_text)

    def test_development_branch_folders_exist_with_status_metadata(self) -> None:
        expected = {
            "lcd_baseline": DASHBOARD_DIR / "modules" / "development" / "lcd_baseline" / "module_status.json",
            "project_metrics": DASHBOARD_DIR / "modules" / "development" / "project_metrics" / "module_status.json",
            "contracts": DASHBOARD_DIR / "modules" / "development" / "contracts" / "module_status.json",
        }

        for module_id, path in expected.items():
            self.assertTrue(path.exists(), f"missing {path}")
            status = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(status["module_id"], module_id)
            self.assertEqual(status["status"], "development")
            self.assertEqual(status["promotion_state"], "not_approved")


if __name__ == "__main__":
    unittest.main()

"""Regression tests for the Project Home / Pii prototype."""

from __future__ import annotations

import importlib.util
import pathlib
import unittest

from streamlit.testing.v1 import AppTest

MODULE_PATH = pathlib.Path(__file__).with_name("project_home_dashboard.py")
spec = importlib.util.spec_from_file_location("project_home_dashboard", MODULE_PATH)
project_home_dashboard = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(project_home_dashboard)


class ManualLcdEntryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.payload = project_home_dashboard.load_fixture()
        self.record = project_home_dashboard.origin(self.payload)

    def test_manual_lcd_entry_rows_are_prepopulated_from_pdd_origin(self) -> None:
        rows = project_home_dashboard.manual_lcd_entry_rows(self.record)

        by_field = {row["LCD Field"]: row for row in rows}
        self.assertEqual(by_field["Project Name"]["Manual Entry"], "Fairview Urgent Care")
        self.assertEqual(
            by_field["Project Location"]["Manual Entry"],
            "4210 Preston Commons Blvd, Fairview, TX 75069",
        )
        self.assertEqual(by_field["Existing S.F."]["Manual Entry"], 1800)
        self.assertEqual(by_field["Original COW"]["Manual Entry"], "$850,000")
        self.assertEqual(
            by_field["Scope Narrative"]["LCD-W / Service Order Reference"],
            "Life Cycle Data Worksheet!A16; Service Order!A17",
        )

    def test_manual_lcd_entry_table_keeps_manual_entry_and_notes_editable(self) -> None:
        disabled_columns = project_home_dashboard.MANUAL_LCD_DISABLED_COLUMNS

        self.assertNotIn("Manual Entry", disabled_columns)
        self.assertNotIn("Entry Notes", disabled_columns)
        self.assertIn("Source Default", disabled_columns)
        self.assertIn("Source State", disabled_columns)
        self.assertIn("LCD-W / Service Order Reference", disabled_columns)

    def test_controlled_lcd_options_match_workbook_pick_lists(self) -> None:
        self.assertEqual(["Administrative", "Clinical"], project_home_dashboard.PROJECT_GROUP_OPTIONS)
        self.assertIn("Andrea Bowman, AIA", project_home_dashboard.PROJECT_MANAGER_OPTIONS)
        self.assertIn("Justin Aubert, AIA", project_home_dashboard.PROJECT_LEADER_OPTIONS)
        self.assertIn("Project Initiation", project_home_dashboard.PHASE_OPTIONS)
        self.assertIn("Furniture", project_home_dashboard.OWNER_CONSULTANT_OPTIONS)
        self.assertIn("Owner-retained Consultants", project_home_dashboard.MULTI_SELECT_LCD_FIELDS)

    def test_manual_lcd_entry_page_renders_in_streamlit(self) -> None:
        app = AppTest.from_file(str(MODULE_PATH)).run(timeout=10)
        app.radio[0].set_value("LCD Manual Entry").run(timeout=10)

        self.assertEqual(list(app.exception), [])
        self.assertIn("Life Cycle Data Worksheet", [subheader.value for subheader in app.subheader])
        self.assertGreaterEqual(len(app.text_input), 20)
        self.assertGreaterEqual(len(app.selectbox), 8)
        self.assertEqual(len(app.multiselect), 1)
        self.assertGreaterEqual(len(app.text_area), 1)

        selectboxes = {selectbox.label: selectbox for selectbox in app.selectbox}
        self.assertIn("Project Manager", selectboxes)
        self.assertIn("Andrea Bowman, AIA", selectboxes["Project Manager"].options)
        self.assertIn("Current Phase", selectboxes)
        self.assertIn("Project Initiation", selectboxes["Current Phase"].options)
        self.assertIn("Furniture", app.multiselect[0].options)

    def test_metrics_source_tables_match_sow_structure(self) -> None:
        self.assertEqual(
            ["KPI Category", "Goal"],
            list(project_home_dashboard.pd.DataFrame(project_home_dashboard.SOW_KPI_ROWS, columns=["KPI Category", "Goal"]).columns),
        )
        self.assertEqual(len(project_home_dashboard.SOW_KPI_ROWS), 6)
        self.assertIn(
            ("Change Order Frequency", "Minimize frequency of post-approval change orders <2% per project."),
            project_home_dashboard.SOW_KPI_ROWS,
        )
        required_metric_names = {row[1] for row in project_home_dashboard.REQUIRED_METRIC_ROWS}
        self.assertIn("Percentage of requests that met expected response times", required_metric_names)
        self.assertIn("Number of RFIs per project, broken down by type", required_metric_names)
        self.assertIn("Proposed / budgeted fees compared to actual costs", required_metric_names)

    def test_metrics_page_renders_in_streamlit(self) -> None:
        app = AppTest.from_file(str(MODULE_PATH)).run(timeout=10)
        app.radio[0].set_value("Metrics").run(timeout=10)

        self.assertEqual(list(app.exception), [])
        self.assertIn('Key Performance Indicators (“KPIs”)', [subheader.value for subheader in app.subheader])
        self.assertIn("Required Metrics List", [subheader.value for subheader in app.subheader])
        self.assertIn("Future Gauge Summary Inputs", [subheader.value for subheader in app.subheader])


if __name__ == "__main__":
    unittest.main()

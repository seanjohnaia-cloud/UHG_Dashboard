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

    def test_alliance_partners_page_uses_owner_consultant_checklist(self) -> None:
        self.assertEqual(len(project_home_dashboard.OWNER_CONSULTANT_OPTIONS), 11)
        self.assertIn("Furniture", project_home_dashboard.OWNER_CONSULTANT_OPTIONS)
        self.assertIn("Storefront Systems", project_home_dashboard.OWNER_CONSULTANT_OPTIONS)
        self.assertIn("Food Service", project_home_dashboard.OWNER_CONSULTANT_OPTIONS)
        self.assertEqual(project_home_dashboard.included_alliance_partner_defaults(self.record), set())

        app = AppTest.from_file(str(MODULE_PATH)).run(timeout=10)
        app.radio[0].set_value("Alliance Partners").run(timeout=10)

        self.assertEqual(list(app.exception), [])
        self.assertIn("Alliance Partners", [subheader.value for subheader in app.subheader])
        self.assertEqual(len(app.checkbox), len(project_home_dashboard.OWNER_CONSULTANT_OPTIONS))
        self.assertGreaterEqual(len(app.text_input), 2)

        checkbox_keys = [checkbox.key for checkbox in app.checkbox]
        self.assertEqual(len(checkbox_keys), len(set(checkbox_keys)))

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

    def test_contract_documents_exclude_service_order_template_row(self) -> None:
        documents = {row["Document"]: row for row in project_home_dashboard.CONTRACT_DOCUMENT_ROWS}

        self.assertIn("Master Agreement", documents)
        self.assertIn("Scope of Work", documents)
        self.assertIn("Executed Service Order", documents)
        self.assertNotIn("Service Order Template", documents)
        self.assertTrue(documents["Master Agreement"]["Path"].endswith("master agreement.pdf"))
        self.assertEqual(documents["Executed Service Order"]["Status"], "Pending")
        self.assertEqual(documents["Executed Service Order"]["Path"], "")
        self.assertEqual(documents["Master Agreement"]["Display Mode"], "image_pages")
        self.assertEqual(documents["Scope of Work"]["Display Mode"], "extracted_markdown")

    def test_contracts_page_renders_clickable_contract_document_actions(self) -> None:
        app = AppTest.from_file(str(MODULE_PATH)).run(timeout=10)
        app.radio[0].set_value("Contracts").run(timeout=10)

        self.assertEqual(list(app.exception), [])
        self.assertIn("Contract Documents", [subheader.value for subheader in app.subheader])
        button_labels = [button.label for button in app.button]
        self.assertIn("Open Master Agreement", button_labels)
        self.assertIn("Open Scope of Work", button_labels)
        self.assertIn("Attach Executed Service Order", button_labels)
        self.assertNotIn("Open Service Order Template", button_labels)

    def test_service_order_template_rows_autopopulate_as_lcd_like_editable_fields(self) -> None:
        rows = project_home_dashboard.service_order_template_entry_rows()
        first = rows[0]

        self.assertGreaterEqual(len(rows), 20)
        self.assertIn("Article", first)
        self.assertEqual(first["Article"], "Article 1 — Initial Information")
        self.assertEqual(first["SO Template Field"], "Service Order No.")
        self.assertIn("Editable Entry", first)
        self.assertIn("Entry Notes", first)
        self.assertEqual(first["Editable Entry"], "Provided by CBRE PM")

        by_field = {row["SO Template Field"]: row for row in rows}
        self.assertEqual(by_field["Project Name / Location"]["Editable Entry"], "From Initial Information")
        self.assertEqual(by_field["Other Documents"]["Editable Entry"], "TBD")
        duplicate_attachment_keys = [
            project_home_dashboard.service_order_template_widget_key(row["Article"], row["SO Template Field"], index)
            for index, row in enumerate(rows)
            if row["SO Template Field"] == "Attachment X"
        ]
        self.assertEqual(len(duplicate_attachment_keys), len(set(duplicate_attachment_keys)))

    def test_service_order_template_page_renders_template_editor(self) -> None:
        app = AppTest.from_file(str(MODULE_PATH)).run(timeout=10)
        app.radio[0].set_value("Service Order Template").run(timeout=10)

        self.assertEqual(list(app.exception), [])
        self.assertIn("Service Order Template Worksheet", [subheader.value for subheader in app.subheader])
        self.assertIn("Uploaded Template PDF Reference", [subheader.value for subheader in app.subheader])
        self.assertIn("Contracts Communication Package", [subheader.value for subheader in app.subheader])
        self.assertGreaterEqual(len(app.text_input), 20)


if __name__ == "__main__":
    unittest.main()

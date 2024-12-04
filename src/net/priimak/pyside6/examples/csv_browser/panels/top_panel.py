from PySide6.QtCore import QMargins
from PySide6.QtWidgets import QComboBox, QHBoxLayout

from net.priimak.pyside6.examples.csv_browser.app_context import AppContext
from net.priimak.pyside6.examples.csv_browser.filter_line_edit import FilterLineEdit
from net.priimak.pyside6.tools.panel_widget import Panel


class TopPanel(Panel[QHBoxLayout]):
    def __init__(self, ctx: AppContext):
        super().__init__(QHBoxLayout())
        self.layout.setContentsMargins(QMargins(1, 1, 1, 5))

        self.search_target_combo_box = QComboBox(self)
        self.search_target_combo_box.addItems(["Substring Search", "SQL Query"])

        self.filter_line_edit = FilterLineEdit()
        self.saved_filter_line_edit_text = ""

        def handle_filter_type_change():
            if self.search_target_combo_box.currentText() == "SQL Query":
                ctx.enable_sql_filter()
            else:
                ctx.enable_substring_filter()
            prev_filter_line_edit_text = self.filter_line_edit.text()
            self.filter_line_edit.setText(self.saved_filter_line_edit_text)
            self.saved_filter_line_edit_text = prev_filter_line_edit_text

        self.search_target_combo_box.currentIndexChanged.connect(handle_filter_type_change)
        self.layout.addWidget(self.search_target_combo_box)

        self.filter_line_edit.textChanged.connect(lambda: ctx.apply_filter(self.filter_line_edit.text()))
        self.layout.addWidget(self.filter_line_edit)

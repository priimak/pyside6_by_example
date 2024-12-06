from PySide6.QtCore import QMargins
from PySide6.QtWidgets import QWidget, QVBoxLayout


class RootPanel(QWidget):
    def __init__(self, top_panel: QWidget, main_panel: QWidget, bottom_panel: QWidget):
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.setContentsMargins(QMargins(5, 5, 5, 1))
        layout.setSpacing(0)

        layout.addWidget(top_panel)
        layout.addWidget(main_panel, stretch = 1)
        layout.addWidget(bottom_panel)

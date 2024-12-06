from PySide6.QtGui import QPalette, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class MainPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, "orange")
        self.setPalette(palette)

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(
            QLabel("Main Panel"),
            alignment = Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
        )

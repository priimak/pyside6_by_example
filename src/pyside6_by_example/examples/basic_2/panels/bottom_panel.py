from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QLabel, QWidget, QHBoxLayout


class BottomPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, "pink")
        self.setPalette(palette)

        layout = QHBoxLayout()
        layout.addWidget(QLabel("Bottom Panel"))
        self.setLayout(layout)

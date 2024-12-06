from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel


class TopPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, "lightblue")
        self.setPalette(palette)

        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.addWidget(QLabel("Top Panel"))

from PySide6.QtWidgets import QMenu, QMessageBox, QWidget


class HelpMenu(QMenu):
    def __init__(self, parent, dialog_parent: QWidget):
        super().__init__("&Help", parent)
        self.addAction("&About", lambda: QMessageBox.about(dialog_parent, "About", "Basic example"))

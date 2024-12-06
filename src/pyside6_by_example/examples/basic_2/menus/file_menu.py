from typing import Callable, Any

from PySide6.QtWidgets import QMenu


class FileMenu(QMenu):
    def __init__(self, parent, on_quit: Callable[[], Any]):
        super().__init__("&File", parent)

        self.addAction("&Open", lambda: None)
        self.addAction("&Save", lambda: None)
        self.addAction("Save &As", lambda: None)
        self.addSeparator()
        self.addAction("&Quit", on_quit)

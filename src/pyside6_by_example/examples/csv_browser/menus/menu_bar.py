from PySide6.QtWidgets import QMenuBar, QWidget

from pyside6_by_example.examples.csv_browser.app_context import AppContext
from pyside6_by_example.examples.csv_browser.menus.file_menu import FileMenu
from pyside6_by_example.examples.csv_browser.menus.help_menu import HelpMenu


class MainMenuBar(QMenuBar):
    def __init__(self, ctx: AppContext, dialogs_parent: QWidget):
        super().__init__(None)

        self.file_menu = FileMenu(self, ctx, dialogs_parent)
        self.addMenu(self.file_menu)
        self.addMenu(HelpMenu(self, dialogs_parent))

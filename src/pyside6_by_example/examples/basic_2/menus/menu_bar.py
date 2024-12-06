from PySide6.QtWidgets import QMenuBar, QMainWindow

from pyside6_by_example.examples.basic_2.menus.file_menu import FileMenu
from pyside6_by_example.examples.basic_2.menus.help_menu import HelpMenu


class MainMenuBar(QMenuBar):
    def __init__(self, main_window: QMainWindow):
        super().__init__()
        self.addMenu(FileMenu(self, main_window.close))
        self.addMenu(HelpMenu(self, main_window))

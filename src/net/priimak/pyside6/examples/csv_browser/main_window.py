from pathlib import Path
from typing import override

from PySide6.QtGui import QIcon, QCloseEvent
from PySide6.QtWidgets import QMessageBox

from net.priimak.pyside6.examples.csv_browser import AppContext, MainMenuBar, TopPanel, MainPanel, BottomPanel
from net.priimak.pyside6.tools import AppPersistence
from net.priimak.pyside6.tools.templates import MainWindowBaseA


class MainWindow(MainWindowBaseA):
    def __init__(self, screen_dim: tuple[int, int], app_persistence: AppPersistence):
        super().__init__(title = "CSV Browser", screen_dim = screen_dim, app_persistence = app_persistence)
        cvsx_icon_file_path = Path(__file__).parent / "csv_browser.png"
        self.setWindowIcon(QIcon(f"{cvsx_icon_file_path}"))

        self.ctx = AppContext(app_persistence)

        # setup menu bar and panels
        main_menu_bar = MainMenuBar(self.ctx, dialogs_parent = self)
        self.setMenuBar(main_menu_bar)
        self.add_panels(
            top_panel = TopPanel(self.ctx),
            main_panel = MainPanel(self.ctx, main_menu_bar.file_menu.recently_opened_menu, dialogs_parent = self),
            bottom_panel = BottomPanel(self.ctx)
        )

        # connect dispatching methods in AppContext to relevant functions
        self.ctx.upd_last_opened_files_menu = self.update_last_opened_files_menu
        self.ctx.exit_application = self.close

        # re-open last opened file if so set in app config.
        if self.app_config.get_value("open_last_opened_file_on_load", bool | None) is True:
            last_opened_files = self.app_state.get_value("last_opened_files", [])
            if last_opened_files != []:
                self.ctx.load_csv_file(last_opened_files[0])

    @override
    def closeEvent(self, event: QCloseEvent):
        open_last_opened_file_on_load = self.app_config.get_value("open_last_opened_file_on_load", bool | None)
        if open_last_opened_file_on_load is None:
            # prompt user if he always wants to open last opened file
            result = QMessageBox.question(
                self, "Re-open file on start?",
                "Do you want to always automatically reopen last opened file when this application starts?"
            )
            self.app_config.set_value("open_last_opened_file_on_load", result == QMessageBox.StandardButton.Yes)

        super().closeEvent(event)

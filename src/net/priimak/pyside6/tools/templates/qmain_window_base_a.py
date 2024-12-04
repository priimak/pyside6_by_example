from pathlib import Path
from typing import Callable

from PySide6.QtCore import QMargins
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMenu

from net.priimak.pyside6.tools.app_persist import AppPersistence


class MainWindowBaseA(QMainWindow):
    def __init__(self, *, title: str, screen_dim: tuple[int, int], app_persistence: AppPersistence):
        super().__init__()
        self.app_state = app_persistence.state
        self.app_config = app_persistence.config
        self.setWindowTitle(title)
        self.set_geometry(screen_dim[0], screen_dim[1])
        self.recently_opened_menu: QMenu | None = None

    def closeEvent(self, event: QCloseEvent):
        self.app_state.save_geometry("main", self.saveGeometry())
        event.accept()

    def set_geometry(self, screen_width: int, screen_height: int):
        # Try loading geometry from saved app state
        loaded_geometry = self.app_state.get_geometry("main")
        if loaded_geometry is None:
            # Init main window size to be 60% of the screen size
            win_size_fraction = 0.6
            self.setGeometry(
                int(screen_width * (1 - win_size_fraction) / 2),
                int(screen_height * (1 - win_size_fraction) / 2),
                int(screen_width * win_size_fraction),
                int(screen_height * win_size_fraction)
            )
        else:
            self.restoreGeometry(loaded_geometry)

    def add_panels(self, *, top_panel: QWidget, main_panel: QWidget, bottom_panel: QWidget) -> None:
        root_panel = QWidget()
        layout = QVBoxLayout()
        root_panel.setLayout(layout)
        layout.setContentsMargins(QMargins(5, 5, 5, 1))
        layout.setSpacing(0)

        layout.addWidget(top_panel)
        layout.addWidget(main_panel, stretch = 1)
        layout.addWidget(bottom_panel)

        self.setCentralWidget(root_panel)

    def update_last_opened_files_menu(
            self,
            file_name: str,
            file_opener_factory: Callable[[str], Callable[[], None]]
    ) -> None:
        last_opened_files = self.app_state.get_value("last_opened_files", [])
        fname = f"{Path(file_name).absolute()}"

        # remove previously seen file as it will be placed at the top of this list
        last_opened_files = [f for f in last_opened_files if f != fname]

        # place it at the top
        last_opened_files.insert(0, fname)

        max_num_of_recorded_last_opened_files = self.app_config.get_value("max_last_opened_files", int)
        if len(last_opened_files) > max_num_of_recorded_last_opened_files:
            last_opened_files = last_opened_files[0:max_num_of_recorded_last_opened_files]
        self.app_state.save_value("last_opened_files", last_opened_files)

        self.update_prev_opened_submenu(file_opener_factory)  # update sub-menu "Prev Opened"

    def update_prev_opened_submenu(self, file_opener_factory: Callable[[str], Callable[[], None]]) -> None:
        if self.recently_opened_menu is not None:
            self.recently_opened_menu.clear()
            for file in self.app_state.get_value("last_opened_files", []):
                self.recently_opened_menu.addAction(file, file_opener_factory(file))

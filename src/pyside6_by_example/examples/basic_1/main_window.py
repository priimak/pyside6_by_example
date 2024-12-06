from typing import override

from PySide6.QtCore import QMargins, QByteArray
from PySide6.QtGui import QPalette, Qt, QCloseEvent
from PySide6.QtWidgets import QMainWindow, QMessageBox, QMenuBar, QMenu, QVBoxLayout, QWidget, QHBoxLayout, QLabel

from pyside6_by_example.tools.app_persist import AppPersistence


class MainWindow(QMainWindow):
    def __init__(self, screen_dim: tuple[int, int], app_persistence: AppPersistence):
        super().__init__()
        self.app_state = app_persistence.state
        self.setWindowTitle("Main Window")
        self.set_geometry(screen_dim[0], screen_dim[1])
        self.define_menus()
        self.define_panels()

    @override
    def closeEvent(self, event: QCloseEvent):
        self.app_state.save_geometry("main", self.saveGeometry())
        event.accept()

    def set_geometry(self, screen_width: int, screen_height: int):
        # Try loading geometry from saved app state
        loaded_geometry: QByteArray | None = self.app_state.get_geometry("main")
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

    def get_file_menu(self, menu_bar: QMenuBar) -> QMenu:
        file_menu = QMenu("&File", menu_bar)
        file_menu.addAction("&Open", lambda: None)
        file_menu.addAction("&Save", lambda: None)
        file_menu.addAction("Save &As", lambda: None)
        file_menu.addSeparator()
        file_menu.addAction("&Quit", self.close)
        return file_menu

    def get_help_menu(self, menu_bar: QMenuBar) -> QMenu:
        help_menu = QMenu("&Help", menu_bar)
        help_menu.addAction("&About", lambda: QMessageBox.about(self, "About", "Basic example"))
        return help_menu

    def define_menus(self) -> None:
        menu_bar = QMenuBar()
        menu_bar.addMenu(self.get_file_menu(menu_bar))
        menu_bar.addMenu(self.get_help_menu(menu_bar))
        self.setMenuBar(menu_bar)

    def get_top_panel(self) -> QWidget:
        top_panel = QWidget()
        top_panel.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, "lightblue")
        top_panel.setPalette(palette)

        layout = QHBoxLayout()
        top_panel.setLayout(layout)
        layout.addWidget(QLabel("Top Panel"))

        return top_panel

    def get_main_panel(self) -> QWidget:
        panel = QWidget()
        panel.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, "orange")
        panel.setPalette(palette)

        layout = QVBoxLayout()
        panel.setLayout(layout)
        layout.addWidget(
            QLabel("Main Panel"),
            alignment = Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
        )

        return panel

    def get_bottom_panel(self) -> QWidget:
        panel = QWidget()
        panel.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, "pink")
        panel.setPalette(palette)

        layout = QHBoxLayout()
        layout.addWidget(QLabel("Bottom Panel"))
        panel.setLayout(layout)

        return panel

    def define_panels(self) -> None:
        root_panel = QWidget()
        layout = QVBoxLayout()
        root_panel.setLayout(layout)
        layout.setContentsMargins(QMargins(5, 5, 5, 1))
        layout.setSpacing(0)

        layout.addWidget(self.get_top_panel())
        layout.addWidget(self.get_main_panel(), stretch = 1)
        layout.addWidget(self.get_bottom_panel())

        self.setCentralWidget(root_panel)

import sys

from PySide6.QtWidgets import QApplication

from net.priimak.pyside6.examples.basic_1.main_window import MainWindow
from net.priimak.pyside6.tools.app_persist import AppPersistence


def main():
    app = QApplication(sys.argv)

    # Will init main window size to be some fraction of the screen size
    # unless defined elsewhere
    screen_width, screen_height = app.primaryScreen().size().toTuple()

    win = MainWindow(
        screen_dim = (screen_width, screen_height),
        app_persistence = AppPersistence("basic_1", {})
    )
    win.show()

    app.exec()


if __name__ == '__main__':
    main()

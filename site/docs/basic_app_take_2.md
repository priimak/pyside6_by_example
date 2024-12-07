# Basic app. Take 2

## Introduction

This app is going to be exactly like `pyside6_example_1` from the previous page except that code will be broken into
a set of files in the following directory structure.

```text
menus/
  file_menu.py
  help_menu.py
  menu_bar.py
panels/
  bottom_panel.py
  main_panel.py
  root_panel.py
  top_panel.py
main.py
main_window.py
```
i.e. every class declaration is placed into its own .py file.

## Overview
## MainClass
```python
from typing import override

from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMainWindow

from pyside6_by_example.examples.basic_2.menus import MainMenuBar
from pyside6_by_example.examples.basic_2.panels import BottomPanel, MainPanel, RootPanel, TopPanel
from pyside6_by_example.tools import AppPersistence
from pyside6_by_example.tools.geometry_helpers import set_geometry


class MainWindow(QMainWindow):
    def __init__(self, screen_dim: tuple[int, int], app_persistence: AppPersistence):
        super().__init__()
        self.app_state = app_persistence.state
        self.setWindowTitle("Main Window")
        self.setObjectName("main")
        set_geometry(self, self.app_state, screen_dim)

        self.setMenuBar(MainMenuBar(self))

        self.setCentralWidget(RootPanel(
            TopPanel(), MainPanel(), BottomPanel()
        ))

    @override
    def closeEvent(self, event: QCloseEvent):
        self.app_state.save_geometry(self.objectName(), self.saveGeometry())
        event.accept()
```
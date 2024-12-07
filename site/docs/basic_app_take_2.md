# Basic app re-structured

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
i.e. every class declaration is placed into its own .py file. Overall there will be a lot more code, however, this 
structure will be much easier to understand and handle if your app will grow to express complex behaviour. 

Complete code for it available [here](https://github.com/priimak/pyside6_by_example/tree/master/src/pyside6_by_example/examples/basic_2).
Once installed using `pipx` you can run this app by typing 
```text
$ pyside6_example_2
```
in the terminal (PowerShell window on Windows).

## MainWindow
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

Key differences here are:

1. Function [set_geometry(...)](https://github.com/priimak/pyside6_by_example/blob/master/src/pyside6_by_example/tools/geometry_helpers.py) being generic moved to it its own file, and it uses object name (set by calling [self.setObjectName(...)](https://doc.qt.io/qtforpython-6/PySide6/QtCore/QObject.html#PySide6.QtCore.QObject.setObjectName) to record geometry under it.
2. Classes [`MainMenuBar`](https://github.com/priimak/pyside6_by_example/blob/master/src/pyside6_by_example/examples/basic_2/menus/menu_bar.py), [`RootPanel`](https://github.com/priimak/pyside6_by_example/blob/master/src/pyside6_by_example/examples/basic_2/panels/root_panel.py), [`TopPanel`](https://github.com/priimak/pyside6_by_example/blob/master/src/pyside6_by_example/examples/basic_2/panels/top_panel.py), [`MainPanel`](https://github.com/priimak/pyside6_by_example/blob/master/src/pyside6_by_example/examples/basic_2/panels/main_panel.py) and [`BottomPanel`](https://github.com/priimak/pyside6_by_example/blob/master/src/pyside6_by_example/examples/basic_2/panels/bottom_panel.py) are now placed into their own files as is [`main()`](https://github.com/priimak/pyside6_by_example/blob/master/src/pyside6_by_example/examples/basic_2/main.py) function.
from typing import Callable

from pyside6_by_example.tools.app_persist import AppPersistence


class AppContext:
    def __init__(self, app_persistence: AppPersistence):
        self.app_persistence = app_persistence
        self.upd_last_opened_files_menu: Callable[[str, Callable[[str], Callable[[], None]]], None] = lambda a, b: None
        self.set_opened_file_label_text: Callable[[str], None] = lambda _: None
        self.set_csv_dimensions_label_text: Callable[[str], None] = lambda _: None
        self.load_csv_file: Callable[[str], None] = lambda _: None
        self.save_csv_file: Callable[[str | None], None | Exception] = lambda _: None
        self.enable_substring_filter: Callable[[], None] = lambda: None
        self.enable_sql_filter: Callable[[], None] = lambda: None
        self.apply_filter: Callable[[str], None] = lambda _: None
        self.exit_application: Callable[[], None] = lambda: None

from pathlib import Path
from typing import Any

from net.priimak.pyside6.tools.app_config import AppConfig
from net.priimak.pyside6.tools.app_state import AppState
from net.priimak.pyside6.tools.io import ensure_dir


class AppPersistence:
    def __init__(self, app_name: str, init_config_data: dict[str, Any]):
        config_root_dir = ensure_dir(Path.home() / f".{app_name}")
        self.state = AppState(config_root_dir)
        self.config = AppConfig(config_root_dir, init_config_data)

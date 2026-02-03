import logging
from pathlib import Path

from . import config

def log_manager():
    current_dir = Path(__file__).resolve()
    project_root = current_dir.parent.parent
    log_dir = project_root / "logs"
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / "app.log"
    log_level = getattr(logging, config.settings.log_level.upper(), logging.INFO)
    logging.basicConfig(
        filename=log_file,
        filemode="a",
        level=log_level,
        format=" %(levelname)s | %(message)s"
    )

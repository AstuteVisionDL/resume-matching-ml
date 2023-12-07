import os
from pathlib import Path

PROJECT_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"

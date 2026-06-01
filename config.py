from pathlib import Path

# Set your local root directory here
ROOT_DIR = Path("/your/local/path/to/project")

# All other paths are relative to ROOT_DIR
DATA_DIR = ROOT_DIR / "data"
OUT_DIR  = ROOT_DIR / "data" / "output"
OBIA_DIR = ROOT_DIR / "data" / "output" / "OBIA_lake_outlines"

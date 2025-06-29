from rescreener.utils.path_utils import *
from pathlib import Path

def test_get_root():
    path: Path = get_root_dir()
    assert path.exists()
    assert path.is_dir()
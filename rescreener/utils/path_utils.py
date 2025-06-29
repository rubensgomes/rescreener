"""A module for file path utilities."""
from pathlib import Path


__all__ = ["get_root_dir"]

def get_root_dir() -> Path:
    """
    Attempts to find the project root directory by searching for a common marker
    (e.g., .git folder or pyproject.toml) upwards from the current script's location.

    Raises:
        FileNotFoundError: If the project root cannot be found.

    Returns:
        Path: The path to the project root directory.
    """
    current_path: Path = Path(__file__).resolve()
    for parent in current_path.parents:
        if (parent / ".git").exists() or (parent / "pyproject.toml").exists():
            return parent
    raise FileNotFoundError("Project root not found.")

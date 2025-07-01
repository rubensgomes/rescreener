"""A module for file path utilities."""

from pathlib import Path

__all__ = ["get_root_dir",
           "validate_extension",
           "validate_content_type",
           "validate_file_size"]


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


def validate_content_type(content_type: str, allowed_content_types: list[str]):
    """
    Validates the given content type to ensure it is one of the allowed content types.

    Args:
        content_type  (str): the content type to be validated.
        allowed_content_types (list[str]): a list of allowed content types
          (e.g., ['application/pdf', 'text/plain']).

    Returns:
        bool: True if the content type is valid, False otherwise.
    """
    return content_type.lower() in (
        allowed_content_type.lower()
        for allowed_content_type in allowed_content_types
    )


def validate_extension(filename: str, allowed_exts: list[str]):
    """
    Validates the given filename extension to ensure it is one of the allowed extensions.

    Args:
        filename  (str): the filename to be validated.
        allowed_exts (list[str]): a list of allowed file extensions (e.g., ['.pdf', '.txt']).

    Returns:
        bool: True if the filename extension is valid, False otherwise.
    """
    return filename.lower().endswith(tuple(allowed_exts))


def validate_file_size(file_path: Path, size_mbytes: int) -> bool:
    """
    Validates the given file size to ensure it is within the specified size limit.

    Args:
        file_path (Path): the file path to be validated.
        size_mbytes (int): the maximum allowed file size in mega bytes.

    Returns:
        bool: True if the file size is valid, False otherwise.
    """
    return file_path.stat().st_size <= size_mbytes * 1024 * 1024

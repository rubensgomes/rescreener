"""A module with supporting pyproject.toml.functions."""

import tomllib
from pathlib import Path

__all__ = ['get_description',
           'get_prg_name',
           'get_pyproject_toml',
           'get_version',
           'DESCRIPTION',
           'PRG',
           'VERSION']


# ------------------------------------------------------------------------------
# --------------->>> get_pyproject_toml <<<-------------------------------------
# ------------------------------------------------------------------------------
def get_pyproject_toml() -> dict:
    """Get pyproject.toml information dictionary.

    Returns:
        the pyproject.toml file dictionary.

    Raises:
        ValueError: if the pyproject.toml not found.
    """
    pyproject_toml_file = Path(__file__).parent.parent.parent / 'pyproject.toml'

    if not pyproject_toml_file.exists() or not pyproject_toml_file.is_file():
        raise ValueError('pyproject.toml file does not exist')

    with open(pyproject_toml_file, 'rb') as f:
        return tomllib.load(f)


# ------------------------------------------------------------------------------
# --------------->>> get_description <<<-------------------------------------
# ------------------------------------------------------------------------------
def get_description(toml_data: dict) -> str:
    """Get program description.

    Args:
        toml_data: the pyproject.toml file dictionary.

    Returns:
        the description from the pyproject.toml file.

    Raises:
        TypeError: if description is not found in pyproject.toml file.
    """
    return toml_data['project']['description']


# ------------------------------------------------------------------------------
# --------------->>> get_prg_name <<<-------------------------------------------
# ------------------------------------------------------------------------------
def get_prg_name(toml_data: dict) -> str:
    """Get program name.

    Args:
        toml_data: the pyproject.toml file dictionary.

    Returns:
        the program name from the pyproject.toml file.

    Raises:
        TypeError: if name is not found in pyproject.toml file.
    """
    return toml_data['project']['name']


# ------------------------------------------------------------------------------
# --------------->>> get_version <<<-------------------------------------------
# ------------------------------------------------------------------------------
def get_version(toml_data: dict) -> str:
    """Get version information.

    Args:
        toml_data: the pyproject.toml file dictionary.

    Returns:
        the version from the pyproject.toml file.

    Raises:
        TypeError: if version is not found in pyproject.toml file.
    """
    return toml_data['project']['version']


_toml_data = get_pyproject_toml()

DESCRIPTION = get_description(_toml_data)
PRG = get_prg_name(_toml_data)
VERSION = get_version(_toml_data)

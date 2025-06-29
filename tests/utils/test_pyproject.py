from rescreener.utils.pyproject import *

def test_succeed_get_pyproject_toml():
    toml = get_pyproject_toml()
    assert isinstance(toml, dict)


def test_succeed_get_description():
    toml = get_pyproject_toml()
    description = get_description(toml)
    assert isinstance(description, str)


def test_succeed_get_prg_name():
    toml = get_pyproject_toml()
    prg = get_prg_name(toml)
    assert isinstance(prg, str)


def test_succeed_get_prg_name():
    toml = get_pyproject_toml()
    version = get_version(toml)
    assert isinstance(version, str)
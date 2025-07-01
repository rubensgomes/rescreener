import pytest
from rescreener.main import main


def test_main_debug(capsys):
    argv = ['--debug']
    main(argv)
    out, err = capsys.readouterr()
    assert out is not None
    # empty string is falsy
    assert not err


def test_main_help(capsys):
    argv = ['--help']
    with pytest.raises(SystemExit) as excinfo:
        main(argv)
    out, err = capsys.readouterr()
    assert out is not None
    # empty string is falsy
    assert not err
    assert excinfo.value.code == 0


def test_main_version(capsys):
    argv = ['--version']
    with pytest.raises(SystemExit) as excinfo:
        main(argv)
    out, err = capsys.readouterr()
    assert out is not None
    # empty string is falsy
    assert not err
    assert excinfo.value.code == 0

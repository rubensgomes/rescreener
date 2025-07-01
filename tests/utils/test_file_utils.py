from pathlib import Path

import pytest

from rescreener.utils.file_utils import *
from tests.utils.create_files_fixture import *


def test_get_root():
    path: Path = get_root_dir()
    assert path.exists()
    assert path.is_dir()


def test_validate_content_type():
    assert validate_content_type("text/plain", ["text/plain", "application/pdf"])
    assert validate_content_type("application/pdf", ["text/plain", "application/pdf"])
    assert not validate_content_type("application/pdf", ["text/plain"])


def test_validate_extension():
    assert validate_extension("test.pdf", [".pdf", ".txt"])
    assert validate_extension("test.PDF", [".pdf"])
    assert not validate_extension("test.docx", [".pdf", ".txt"])


@pytest.mark.parametrize("txt_file_path",
                         [{"file_path": Path("/tmp/example.txt"), "content": "hello"}],
                         indirect=True)
def test_validate_file_size(txt_file_path: Path):
    assert validate_file_size(txt_file_path, 1)
    assert not validate_file_size(txt_file_path, 0)

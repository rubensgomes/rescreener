import os
from typing import Any, Generator

import pytest

from pathlib import Path

from rescreener.utils.pdf_utils import pdf_to_text
from tests.utils.create_files_fixture import *

TXT_FILE_PATH: Path = Path("/tmp/example.txt")
CONTEXT: str = "hello"

@pytest.fixture
def remove_txt_file() -> Generator[Path, Any, Path]:
    yield TXT_FILE_PATH
    os.remove(TXT_FILE_PATH)
    return TXT_FILE_PATH

@pytest.mark.parametrize("pdf_file_path",
                         [{"file_path": Path("/tmp/example.pdf"), "content": CONTEXT}],
                         indirect=True)
def test_pdf_to_text(pdf_file_path: Path, remove_txt_file: Path):
    pdf_to_text(pdf_file_path, TXT_FILE_PATH)
    # reading a text file
    with open(TXT_FILE_PATH, 'r', encoding='utf-8') as file:
        txt_file_content: str = file.read()
    assert CONTEXT in txt_file_content

import os

import pytest

from rescreener.utils.pdf_utils import pdf_to_text
from tests.utils.create_pdf_fixture import create_pdf_fixture, PDF_FILE_PATH, PDF_TXT

TXT_FILE_PATH = "/tmp/example.txt"


@pytest.fixture
def remote_txt_file():
    yield
    os.remove(TXT_FILE_PATH)


def test_pdf_to_text(create_pdf_fixture, remote_txt_file):
    pdf_to_text(PDF_FILE_PATH, TXT_FILE_PATH)
    # reading a text file
    with open(TXT_FILE_PATH, 'r', encoding='utf-8') as file:
        content: str = file.read()
    assert PDF_TXT in content

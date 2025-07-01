import os
from pathlib import Path
from typing import Any, Generator

import pytest
from fpdf import FPDF

__all__ = ["pdf_file_path",
           "txt_file_path"]


def _create_pdf_file(pdf_file_path: Path, some_text: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, some_text)
    pdf.output(pdf_file_path)
    return None


@pytest.fixture
def pdf_file_path(request) -> Generator[Path, Any, Path]:
    pdf_file_path: Path = request.param["file_path"]
    some_text: str = request.param["content"]
    _create_pdf_file(pdf_file_path, some_text)
    yield pdf_file_path
    os.remove(pdf_file_path)
    return pdf_file_path


@pytest.fixture
def txt_file_path(request) -> Generator[Path, Any, Path]:
    txt_file_path: Path = request.param["file_path"]
    some_text: str = request.param["content"]
    with open(txt_file_path, 'wt') as file:
        file.write(some_text)
    yield txt_file_path
    os.remove(txt_file_path)
    return txt_file_path

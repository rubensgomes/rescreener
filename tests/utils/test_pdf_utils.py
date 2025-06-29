import pytest
import os

from pathlib import Path
from fpdf import FPDF
from rescreener.utils.pdf_utils import pdf_to_text

PDF_FILE="example.pdf"
PDF_TXT="Hello World!"
TXT_FILE="example.txt"

@pytest.fixture
def _fixture():
    _create_pdf_file()
    yield
    os.remove(PDF_FILE)
    os.remove(TXT_FILE)

def _create_pdf_file():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, PDF_TXT)
    pdf.output(PDF_FILE)

def test_pdf_to_text(_fixture):
    pdf_to_text(PDF_FILE, TXT_FILE)
    with open(TXT_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    assert PDF_TXT in content

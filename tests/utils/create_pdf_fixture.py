import os

import pytest
from fpdf import FPDF

PDF_FILE_PATH= "/tmp/example.pdf"
PDF_TXT="Hello World!"

__all__ = [
    'PDF_FILE_PATH',
    'PDF_TXT',
    'create_pdf_fixture']

def _create_pdf_file():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, PDF_TXT)
    pdf.output(PDF_FILE_PATH)

@pytest.fixture
def create_pdf_fixture():
    _create_pdf_file()
    yield
    os.remove(PDF_FILE_PATH)


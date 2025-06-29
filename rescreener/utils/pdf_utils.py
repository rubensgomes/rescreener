"""A module of PDF utilities"""

import PyPDF2

__all__ = ['pdf_to_text']

def pdf_to_text(pdf_path: str, txt_path: str) -> None:
    """Converts a given input pdf_path file to an output txt_path text file.

    Args:
        pdf_path (str): a fully-qualified path to input PDF file.
        txt_path (str): a fully-qualified path to output text file.

    Returns:
        None
    """
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        with open(txt_path, 'w', encoding='utf-8') as text_file:
            for page_num, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    text_file.write(f"--- Page {page_num + 1} ---\n")
                    text_file.write(text)
                    text_file.write("\n\n")
                else:
                    text_file.write(f"--- Page {page_num + 1} (No text found) ---\n\n")

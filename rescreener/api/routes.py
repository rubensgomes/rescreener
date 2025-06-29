"""A module containing end point controller functions."""
from typing import Dict

from fastapi import APIRouter, UploadFile, File

router = APIRouter()


@router.post("/pdf-file/")
async def upload_pdf_file(file: UploadFile = File(...)) -> Dict[str, bytes]:
    """Handles the upload of a PDF file from a web page.

    Args:
        file  (UploadFile): a file uploaded from a web page.

    Returns:
        dict: a dictionary containing the filename and the bytes content of the uploaded file.
    """
    content = await file.read()
    data: Dict[str, bytes] = {"filename": file.filename, "content": content}
    return data

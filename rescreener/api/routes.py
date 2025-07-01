"""A module containing end point controller functions."""

import os
import shutil
import uuid
from pathlib import Path
from typing import Dict, Annotated

from fastapi import APIRouter, UploadFile, Request, File, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from rescreener.utils.file_utils import get_root_dir, validate_content_type, validate_extension

router = APIRouter()
templates_dir: Path = get_root_dir() / "templates"
templates = Jinja2Templates(directory=templates_dir)

# Max file size (in bytes) — e.g., 10 MB
MAX_FILE_SIZE = 10 * 1024 * 1024

# folder to save temporary resume + job_descript files.
UPLOAD_DIR = "/tmp/rescreener_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# Helper to save with unique filename
def _save_upload_file(upload_file: UploadFile, destination: str) -> str:
    filename = f"{uuid.uuid4().hex}_{upload_file.filename}"
    file_path = os.path.join(destination, filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return filename

@router.get("/", tags=["index"], response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    """Returns the HTML index page to the user.

    Returns:
        str: a Bootstrap index HTML page.
    """
    response: HTMLResponse = templates.TemplateResponse(request, "index.html")
    return response


@router.post("/upload-files")
async def upload_files(
        pdf_file: Annotated[UploadFile, File(..., description="PDF file")],
        txt_file: Annotated[UploadFile, File(..., description="Text file")]
) -> Dict[str, str]:
    """Handles the upload of a PDF resume file a text job description file from a web page.

    Args:
        pdf_file  (UploadFile): a PDF resume file uploaded from a web page.
        txt_file  (UploadFile): a text job description file uploaded from a web page.

    Returns:
        dict: a dictionary containing filename, content-type
    """
    # Validate pdf_file: content type, extension and size
    if not validate_content_type(pdf_file.content_type, ["application/pdf"]):
        raise HTTPException(status_code=400, detail=f"resume file must be a PDF. Received: "
                                                    f"{pdf_file.content_type}")
    if not validate_extension(pdf_file.filename, [".pdf"]):
        raise HTTPException(status_code=400, detail=f"resume file must end in .pdf. Received: "
                                                    f"{pdf_file.filename}")

    pdf_file.file.seek(0, os.SEEK_END)
    pdf_file_size: int = pdf_file.file.tell()
    pdf_file.file.seek(0)

    if pdf_file_size > MAX_FILE_SIZE:
        raise HTTPException(400, detail="Resume PDF file exceeds 10 MB limit")

    # Validate txt_file: content type, extension and size
    if not validate_content_type(txt_file.content_type, ["text/plain"]):
        raise HTTPException(status_code=400,
                            detail=f"job description file must be a text file. Received: "
                                   f"{txt_file.content_type}")
    if not validate_extension(txt_file.filename, [".txt"]):
        raise HTTPException(status_code=400,
                            detail=f"job description file must end in .txt. Received: "
                                   f"{txt_file.filename}")

    txt_file.file.seek(0, os.SEEK_END)
    txt_file_size: int = txt_file.file.tell()
    txt_file.file.seek(0)

    if txt_file_size > MAX_FILE_SIZE:
        raise HTTPException(400, detail="Job description TXT file exceeds 10 MB limit")

    # Save files
    saved_pdf_file = _save_upload_file(pdf_file, UPLOAD_DIR)
    saved_txt_file = _save_upload_file(txt_file, UPLOAD_DIR)

    return {
        "message": "Files uploaded successfully",
        "resume": saved_pdf_file,
        "job description": saved_txt_file
    }

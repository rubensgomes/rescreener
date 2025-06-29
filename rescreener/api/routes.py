"""A module containing end point controller functions."""
from pathlib import Path
from typing import Dict

from fastapi import APIRouter, UploadFile, Request, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from rescreener.utils.path_utils import get_root_dir

router = APIRouter()
templates_dir: Path = get_root_dir() / "templates"
templates = Jinja2Templates(directory=templates_dir)

@router.get("/", tags=["index"], response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    """Returns the HTML index page to the user.

    Returns:
        str: a Bootstrap index HTML page.
    """
    response: HTMLResponse = templates.TemplateResponse("index.html", {"request": request})
    return response


@router.post("/pdf-file")
async def upload_pdf_file(file: UploadFile = File(...)) -> Dict[str, str]:
    """Handles the upload of a PDF file from a web page.

    Args:
        file  (UploadFile): a file uploaded from a web page.

    Returns:
        dict: a dictionary containing filename, content-type
    """
    data: Dict[str, str] = {"filename": file.filename, "content_type": file.content_type}
    return data

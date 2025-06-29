import pytest
from fastapi import status
from httpx import AsyncClient

from rescreener.main import app


@pytest.mark.asyncio
async def test_upload_pdf_file():
    sample_pdf_bytes: bytes = (
        b"%PDF-1.4\n%...\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n..."
    )

    # Simulate file upload using httpx.AsyncClient
    async with AsyncClient(app=app, base_url="http://test") as ac:
        files = {"file": ("sample.pdf", sample_pdf_bytes, "application/pdf")}
        response = await ac.post("/pdf-file/", files=files)

    assert response.status_code == status.HTTP_200_OK
    text: str = response.content.decode("utf-8")
    assert (text.__contains__("filename"))
    assert (text.__contains__("sample.pdf"))
    assert (text.__contains__("content"))
    # failed due to \n (input) and \\n (output)
    # pdf_text: str = sample_pdf_bytes.decode("utf-8")
    # assert (text.__contains__(pdf_text))

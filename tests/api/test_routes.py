from pathlib import Path

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from rescreener.api import routes
from tests.utils.create_files_fixture import *

app = FastAPI()
app.include_router(routes.router)


# auto closeable TestClient instance
@pytest.fixture
def client() -> TestClient:
    with TestClient(app) as client:
        yield client


# /
def test_index(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.parametrize("pdf_file_path",
                         [{"file_path": Path("/tmp/example.pdf"), "content": "hello"}],
                         indirect=True)
@pytest.mark.parametrize("txt_file_path",
                         [{"file_path": Path("/tmp/example.txt"), "content": "hello"}],
                         indirect=True)
def test_upload_files(pdf_file_path: Path, txt_file_path: Path, client: TestClient):
    # create pdf_file + txt_file objects
    with pdf_file_path.open('rb') as pdf_file, txt_file_path.open('rb') as txt_file:
        response = client.post(
            "/upload-files",
            files={
                "pdf_file": (pdf_file_path.name, pdf_file, "application/pdf"),
                "txt_file": (txt_file_path.name, txt_file, "text/plain"),
            }
        )

    assert response.status_code == 200

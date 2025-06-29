import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from rescreener.api import routes
from tests.utils.create_pdf_fixture import create_pdf_fixture, PDF_FILE_PATH

app = FastAPI()
app.include_router(routes.router)

# auto closeable TestClient instance
@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

# /
def test_index(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200

# /pdf-file
def test_upload_pdf_file(create_pdf_fixture, client: TestClient):
    with open(PDF_FILE_PATH, 'rb') as pdf_file:
        files = {"file": (PDF_FILE_PATH, pdf_file, "application/pdf")}
        response = client.post("/pdf-file", files=files)
    assert response.status_code == 200
    json: str = response.json()
    assert json.__contains__("filename")
    assert json.__contains__("content_type")

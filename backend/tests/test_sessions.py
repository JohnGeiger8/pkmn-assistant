from datetime import datetime, timedelta, timezone

import io

import pytest

from app import create_app
from app import sessions
from app import storage


@pytest.fixture(autouse=True)
def clear_sessions():
    sessions._SESSIONS.clear()


@pytest.fixture()
def client():
    app = create_app()
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client


def test_create_session(client):
    response = client.post("/api/sessions")
    assert response.status_code == 201
    payload = response.get_json()
    assert "session" in payload
    session = payload["session"]
    assert "id" in session
    assert "createdAt" in session
    assert "expiresAt" in session


def test_get_session_success(client):
    create_response = client.post("/api/sessions")
    session_id = create_response.get_json()["session"]["id"]

    response = client.get(f"/api/sessions/{session_id}")
    assert response.status_code == 200
    payload = response.get_json()
    assert payload["session"]["id"] == session_id


def test_get_session_not_found(client):
    response = client.get("/api/sessions/does-not-exist")
    assert response.status_code == 404
    payload = response.get_json()
    assert payload["code"] == "session_not_found"


def test_get_session_expired(client):
    session = sessions.create_session()
    session.expires_at = datetime.now(timezone.utc) - timedelta(seconds=1)
    sessions._SESSIONS[session.id] = session

    response = client.get(f"/api/sessions/{session.id}")
    assert response.status_code == 404
    payload = response.get_json()
    assert payload["code"] == "session_not_found"


def test_upload_save_success(client, monkeypatch):
    create_response = client.post("/api/sessions")
    session_id = create_response.get_json()["session"]["id"]

    uploaded = {}

    def fake_upload(file_obj, key, content_type):
        uploaded["key"] = key
        uploaded["content_type"] = content_type
        file_obj.read()
        return key, 7

    monkeypatch.setattr(storage, "upload_save_file", fake_upload)

    data = {"file": (io.BytesIO(b"pokemon"), "save.sav")}
    response = client.post(
        f"/api/sessions/{session_id}/save",
        data=data,
        content_type="multipart/form-data",
    )

    assert response.status_code == 201
    payload = response.get_json()
    assert payload["save"]["fileName"] == "save.sav"
    assert payload["save"]["storageKey"] == f"sessions/{session_id}/save/save.sav"
    assert payload["save"]["size"] == 7
    assert uploaded["key"] == f"sessions/{session_id}/save/save.sav"


def test_upload_save_missing_file(client):
    create_response = client.post("/api/sessions")
    session_id = create_response.get_json()["session"]["id"]

    response = client.post(f"/api/sessions/{session_id}/save")

    assert response.status_code == 400
    payload = response.get_json()
    assert payload["code"] == "file_missing"


def test_upload_save_invalid_extension(client):
    create_response = client.post("/api/sessions")
    session_id = create_response.get_json()["session"]["id"]

    data = {"file": (io.BytesIO(b"pokemon"), "save.txt")}
    response = client.post(
        f"/api/sessions/{session_id}/save",
        data=data,
        content_type="multipart/form-data",
    )

    assert response.status_code == 400
    payload = response.get_json()
    assert payload["code"] == "invalid_file_type"


def test_upload_save_empty_file(client):
    create_response = client.post("/api/sessions")
    session_id = create_response.get_json()["session"]["id"]

    data = {"file": (io.BytesIO(b""), "save.sav")}
    response = client.post(
        f"/api/sessions/{session_id}/save",
        data=data,
        content_type="multipart/form-data",
    )

    assert response.status_code == 400
    payload = response.get_json()
    assert payload["code"] == "invalid_file"


def test_upload_save_session_not_found(client):
    data = {"file": (io.BytesIO(b"pokemon"), "save.sav")}
    response = client.post(
        "/api/sessions/does-not-exist/save",
        data=data,
        content_type="multipart/form-data",
    )

    assert response.status_code == 404
    payload = response.get_json()
    assert payload["code"] == "session_not_found"
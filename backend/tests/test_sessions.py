from datetime import datetime, timedelta, timezone

import pytest

from app import create_app
from app import sessions


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
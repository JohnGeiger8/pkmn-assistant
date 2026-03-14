from pathlib import Path

from botocore.exceptions import BotoCoreError, ClientError
from flask import Blueprint, jsonify, request

from app.sessions import create_session, get_session, serialize_session
from app import storage

api_bp = Blueprint("api", __name__)


@api_bp.get("/health")
def health_check():
    return jsonify({"status": "ok"})


@api_bp.post("/sessions")
def create_session_route():
    session = create_session()
    return jsonify({"session": serialize_session(session)}), 201


@api_bp.get("/sessions/<session_id>")
def get_session_route(session_id: str):
    session = get_session(session_id)
    if not session:
        return (
            jsonify(
                {
                    "code": "session_not_found",
                    "message": "Session not found or expired.",
                }
            ),
            404,
        )
    return jsonify({"session": serialize_session(session)})


@api_bp.post("/sessions/<session_id>/save")
def upload_save_route(session_id: str):
    session = get_session(session_id)
    if not session:
        return (
            jsonify(
                {
                    "code": "session_not_found",
                    "message": "Session not found or expired.",
                }
            ),
            404,
        )

    if "file" not in request.files:
        return (
            jsonify(
                {
                    "code": "file_missing",
                    "message": "No save file uploaded. Please attach a .sav or .dsv file.",
                }
            ),
            400,
        )

    upload = request.files["file"]
    if not upload.filename:
        return (
            jsonify(
                {
                    "code": "file_missing",
                    "message": "No save file uploaded. Please attach a .sav or .dsv file.",
                }
            ),
            400,
        )

    extension = Path(upload.filename).suffix.lower()
    if extension not in {".sav", ".dsv"}:
        return (
            jsonify(
                {
                    "code": "invalid_file_type",
                    "message": "Only .sav and .dsv files are supported.",
                }
            ),
            400,
        )

    upload.stream.seek(0, 2)
    size = upload.stream.tell()
    upload.stream.seek(0)
    if size <= 0:
        return (
            jsonify(
                {
                    "code": "invalid_file",
                    "message": "Save file is empty or corrupt.",
                }
            ),
            400,
        )

    storage_key = f"sessions/{session_id}/save/{upload.filename}"
    try:
        storage.upload_save_file(
            file_obj=upload.stream,
            key=storage_key,
            content_type=upload.mimetype or "application/octet-stream",
        )
    except (BotoCoreError, ClientError):
        return (
            jsonify(
                {
                    "code": "storage_error",
                    "message": "Unable to store the save file right now.",
                }
            ),
            500,
        )

    return (
        jsonify(
            {
                "save": {
                    "fileName": upload.filename,
                    "storageKey": storage_key,
                    "size": size,
                }
            }
        ),
        201,
    )
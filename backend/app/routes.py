from flask import Blueprint, jsonify

from app.sessions import create_session, get_session, serialize_session

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
import os
import uuid
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Dict, Optional


SESSION_TTL_SECONDS = int(os.getenv("SESSION_TTL_SECONDS", "3600"))


@dataclass
class Session:
    id: str
    created_at: datetime
    expires_at: datetime


_SESSIONS: Dict[str, Session] = {}


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _is_expired(session: Session, now: Optional[datetime] = None) -> bool:
    current_time = now or _now()
    return current_time >= session.expires_at


def create_session() -> Session:
    session_id = str(uuid.uuid4())
    created_at = _now()
    expires_at = created_at + timedelta(seconds=SESSION_TTL_SECONDS)
    session = Session(id=session_id, created_at=created_at, expires_at=expires_at)
    _SESSIONS[session_id] = session
    return session


def get_session(session_id: str) -> Optional[Session]:
    session = _SESSIONS.get(session_id)
    if not session:
        return None
    if _is_expired(session):
        _SESSIONS.pop(session_id, None)
        return None
    return session


def purge_expired() -> int:
    now = _now()
    expired_ids = [session_id for session_id, session in _SESSIONS.items() if _is_expired(session, now)]
    for session_id in expired_ids:
        _SESSIONS.pop(session_id, None)
    return len(expired_ids)


def serialize_session(session: Session) -> dict:
    return {
        "id": session.id,
        "createdAt": session.created_at.isoformat(),
        "expiresAt": session.expires_at.isoformat(),
    }
# System Patterns

## Architecture Overview
- Monorepo with `frontend` (Angular) and `backend` (Flask) applications.
- Web client communicates with backend APIs for sessions, uploads, and recommendations.
- ML identification will run server-side; milestone 1 uses manual entry to validate end-to-end flow.

## Key Workflows
- Session management:
  - `POST /api/sessions` creates a session.
  - `GET /api/sessions/{id}` fetches session state.
- Image uploads:
  - `POST /api/sessions/{id}/images` accepts multiple images per session.
  - Images stored in S3-compatible storage with TTL cleanup.
- Recommendation flow:
  - Manual Pokémon entry (Milestone 1) or ML identification (future).
  - `POST /api/sessions/{id}/recommendation` returns up to 6 Pokémon and explanation.

## Backend Scaffold (Milestone 1 - Section A)
- Flask app factory in `backend/app/__init__.py`.
- API blueprint in `backend/app/routes.py` (health check).
- Entry point at `backend/wsgi.py` for local runs.

## Data Handling Patterns
- Treat all images in a session as a single combined Pokémon pool.
- Exclude eggs from identification and downstream processing.
- Normalize orientation/scale for image preprocessing.

## Testing and Traceability
- Requirements map to tests via `docs/traceability.md`.
- Acceptance dataset `acceptance_v1` gates Top-3 accuracy (≥95%).
- CI artifacts saved in `artifacts/` per doc guidance.
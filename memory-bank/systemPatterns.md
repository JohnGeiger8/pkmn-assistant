# System Patterns

## Architecture Overview
- Monorepo with `frontend` (Angular) and `backend` (Flask) applications.
- Web client communicates with backend APIs for sessions, uploads, and recommendations.
- ML identification will run server-side; milestone 1 uses manual entry to validate end-to-end flow.

## Key Workflows
- Session management:
  - `POST /api/sessions` creates a session.
  - `GET /api/sessions/{id}` fetches session state.
- Save uploads:
  - `POST /api/sessions/{id}/save` accepts one save file per session.
  - Save files stored in S3-compatible storage with TTL cleanup.
- Recommendation flow:
  - Save parsing populates the Pokémon pool; users can exclude entries before recommendation.
  - `POST /api/sessions/{id}/recommendation` returns up to 6 Pokémon and explanation.

## Backend Scaffold (Milestone 1 - Section A)
- Flask app factory in `backend/app/__init__.py`.
- API blueprint in `backend/app/routes.py` (health check).
- Entry point at `backend/wsgi.py` for local runs.

## Data Handling Patterns
- Treat party + PC entries from a save file as a combined Pokémon pool.
- Parse eggs as their hatch species when available in the save data.
- Normalize species (shiny treated as normal, Unown forms collapsed).

## Testing and Traceability
- Requirements map to tests via `docs/traceability.md`.
- Save parsing uses known-good save fixtures for validation.
- CI artifacts saved in `artifacts/` per doc guidance.
# Tech Context

## Stack
- Frontend: Angular (web)
- Backend: Flask (API)
- ML (future): PyTorch
- Storage: S3-compatible object storage
- CI/CD: GitHub Actions

## Backend Runtime
- Python 3.14
- `venv` + `pip` + `requirements.txt`
- Entry point: `backend/wsgi.py` (Flask app factory)

## Local Development
- Monorepo structure:
  - `frontend/`
  - `backend/`
  - `docs/`
  - `artifacts/` (gitignored)
  - `docker-compose.yml` (optional)
- Backend health check: `GET /api/health`
- Docker compose: `docker compose up --build` runs frontend (4200) + backend (5000)
- Angular dev server proxy: `frontend/pkmn-assistant/proxy.conf.json` proxies `/api` -> `http://localhost:5000`
- Angular environments: `environment.ts` uses `/api`, `environment.prod.ts` uses full API host
- Docker proxy config: `frontend/pkmn-assistant/proxy.conf.docker.json` proxies `/api` -> `http://backend:5000`

## Interface Contracts
- Sessions: `POST /api/sessions`, `GET /api/sessions/{id}`
- Uploads: `POST /api/sessions/{id}/images` (multipart)
- Recommendation: `POST /api/sessions/{id}/recommendation`

## Data Requirements
- Acceptance dataset `acceptance_v1` for Top-3 accuracy gating.
- Supported image formats: PNG, JPG, JPEG, HEIC (if browser-supported).
- Processing constraints: ≤5 seconds end-to-end under nominal load.
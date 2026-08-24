# Pokémon Assistant

Pokémon Assistant is a browser-based Generation 3 team-building application. It accepts a supported save file, extracts the player's party and PC inventory, lets the player exclude entries, and produces an in-game team recommendation with an explanation.

The application prioritizes low-friction use and accurate save parsing over competitive optimization. Screenshot recognition and other ML capabilities are future work, not a dependency for the first milestone.

## Architecture

- **Frontend:** Angular application in `frontend/pkmn-assistant/`
- **Backend:** Flask API in `backend/`
- **Storage:** S3-compatible object storage; MinIO is included for local development
- **Session model:** short-lived in-memory sessions with uploaded files stored under session-scoped object keys
- **Durable requirements and traceability:** `docs/`
- **Architecture, decisions, and current progress:** `memory-bank/`

The current API supports health, session management, and save upload foundations. Save parsing, inventory review, and recommendation are the next Milestone 1 slices.

## Run the complete local stack

Prerequisites: Docker with Compose.

```bash
docker compose up --build
```

Then open:

- Frontend: `http://localhost:4200`
- Backend health: `http://localhost:5000/api/health`
- MinIO console: `http://localhost:9001`

## Backend development

Python 3.14 is the documented project target.

```bash
cd backend
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python wsgi.py
```

Run backend tests from the repository root:

```bash
python -m pytest backend/tests
```

Local S3 settings are documented in `.env.example`; never commit real credentials.

## Frontend development

```bash
cd frontend/pkmn-assistant
npm ci
npm start
```

The local Angular proxy sends `/api` to the Flask backend. The Docker stack uses `proxy.conf.docker.json` and the `backend` service name.

Verify the frontend with:

```bash
npm run build
npm test -- --watch=false --browsers=ChromeHeadless
```

## Documentation map

- `docs/requirements.md` — product and system requirements
- `docs/milestone-1.md` — first milestone plan
- `docs/traceability.md` — requirements-to-test mapping
- `docs/CONTRIBUTING.md` — contribution workflow
- `memory-bank/architecture.md` — current architecture and data flow
- `memory-bank/decisions.md` — durable technical decisions
- `memory-bank/progress.md` — implemented and remaining work
- `AGENTS.md` — operating instructions for coding agents

## Scope boundaries

Milestone 1 supports English-language Generation 3 saves (`.sav` and `.dsv`). It does not include authentication, competitive IV/EV assumptions, ROM hacks, or a required ML pipeline. Eggs are normalized to their hatch species when available, shiny variants are treated as their normal species, and Unown forms are collapsed.

# pkmn-assistant
Browser-based Pokémon team-building tools, beginning with a generation 3 screenshot/image processing tool which takes images of player's PC boxes and outputs team recommendations.

## Backend (Flask) Setup

### Prerequisites
- Python 3.14

### Install & Run
```bash
cd backend
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Start the API:
```bash
python wsgi.py
```

Health check:
```bash
curl http://localhost:5000/api/health
```

## Docker Compose (Frontend + Backend)

Start both services:
```bash
docker compose up --build
```

Then visit:
- Frontend: http://localhost:4200
- Backend health: http://localhost:5000/api/health

## Angular Dev Server Proxy

During local development, the Angular dev server proxies API calls to the Flask backend.
This lets you call `/api/...` from the frontend without CORS issues.

Proxy config: `frontend/pkmn-assistant/proxy.conf.json`

When running via Docker Compose, the frontend container uses:
`frontend/pkmn-assistant/proxy.conf.docker.json` (targets `http://backend:5000`).

## Angular Environments

API base URL is configured via Angular environment files:
- `environment.ts`: `apiBaseUrl: '/api'` (proxied locally)
- `environment.prod.ts`: `apiBaseUrl: 'https://my-api-host.com/api'`

Production builds replace `environment.ts` with `environment.prod.ts` via `angular.json`.

## Example Backend Call

`AppComponent` makes a simple GET request to `/api/health` and displays the status.

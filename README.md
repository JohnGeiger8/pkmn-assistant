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

## A recommended development workflow from ChatGPT

Here’s a workflow that stays low-effort but noticeably improves quality.

Where memory-bank updates fit in the workflow
1. Start of a task (30 seconds)
- Do not rewrite files. Just make sure Cline is anchored:
  - Point it at your “Read First” list (you already did).
  - State the one outcome you want + “done when” checks.
  - No memory-bank edits needed here unless you’re changing direction.

2. During implementation
- Don’t update memory files mid-task unless:
  - You discover a new constraint
  - You change an interface contract
  - You decide on a new dependency or storage approach
Those are decision points, not progress notes.

3. End of a task (the best time)

Your current approach is good: once you’re satisfied, tell Cline:

“Update memory bank.”

That’s appropriate. But: be specific about what should change so it doesn’t bloat or overwrite your intent.

Use a closing prompt like:

“Update progress.md with what was completed and what’s next.”

“If any architectural assumptions changed, update architecture.md.”

“If we made a new choice, add a short entry to decisions.md.”

This keeps updates precise and prevents random churn.

### Which files should be updated how often?
#### Update frequently (most tasks)
- progress.md: yes — after most tasks
What changed? What’s next? Any blockers?

- activeContext.md: only when priorities shift
What are we working on right now?

#### Update occasionally (only when needed)
- decisions.md: only when you make a “we chose X” decision
Examples: picking MinIO vs local disk, label format, API error schema, session TTL policy

- architecture.md: only when structure/interfaces change
Examples: new endpoint patterns, new module boundaries, storage conventions

- aiContract.md: rarely
Only when you notice a recurring failure mode (“Cline keeps refactoring too much” → add a rule)

#### A simple rule of thumb

If the change would matter two weeks from now or to a new contributor, it belongs in memory bank.

If it’s just “implemented endpoint X,” that’s progress.md only.

At the end of a slice, tell Cline:

- Update progress.md (always)

- Update activeContext.md (only if the next focus changed)

- Update decisions.md (only if a new decision was made)

- Update architecture.md (only if contracts/structure changed)

That’s it. Keeps the repo clean and the agent consistent.
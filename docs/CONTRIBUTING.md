# Contributing

Thanks for your interest in contributing!

This project is an open-source Pokémon AI Team Assistant focused on clean architecture, correctness, and extensibility.

---

## Development Setup

### Prerequisites
- Node.js (for Angular)
- Python 3.10+
- Docker (recommended for local services)
- Git

### Running Locally
1. Clone the repository
2. Follow instructions in `README.md`
3. Start frontend and backend
4. Verify the app loads and can create a session

---

## Project Structure

- `frontend/` — Angular web app
- `backend/` — Flask REST API
- `docs/` — Requirements, architecture, and milestones
- `memory-bank/` — Persistent AI and architectural context

---

## Workflow

- Create a feature branch from `main`
- Keep changes small and focused
- Prefer vertical slices over refactors
- Add or update tests when behavior changes

---

## Testing

Before submitting a PR, ensure:
- Backend tests pass (`pytest`)
- Frontend tests pass (`npm test` or `ng test`)
- No failing lint checks

---

## Pull Requests

Each PR should:
- Reference a GitHub Issue
- Clearly describe what changed
- Leave the codebase in a green state

---

## AI-Assisted Development

This project uses AI-assisted coding tools.
Contributors should:
- Follow the rules in `memory-bank/aiContract.md`
- Avoid large, unrelated refactors
- Favor clarity over cleverness

---

## Questions?

Open a GitHub Issue or discussion — happy to help!

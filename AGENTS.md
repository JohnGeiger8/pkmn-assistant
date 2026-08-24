# Agent operating guide

## Read first

1. `README.md`
2. `.clinerules`
3. Every file under `memory-bank/`
4. Relevant requirements and traceability documents under `docs/`
5. The source and tests involved in the requested change

Project truth lives in the README, `docs/`, `memory-bank/`, source, and tests. Keep this file limited to operating rules.

## Working rules

- Propose a short plan with files and verification commands before editing.
- Make the smallest testable change and avoid unrelated refactors.
- Keep Flask routes thin and move business logic into appropriate modules.
- Keep Angular API calls in services and UI state explicit.
- Add or update tests for behavior changes; every new endpoint needs an integration test.
- Do not add frameworks, authentication, or dependencies without explicit approval and a durable decision record.
- Preserve existing uncommitted work.

## Commands

Backend, from the repository root:

```bash
python -m pytest backend/tests
```

Frontend:

```bash
cd frontend/pkmn-assistant
npm run build
npm test -- --watch=false --browsers=ChromeHeadless
```

Complete stack:

```bash
docker compose up --build
```

## Completion checks

- Relevant backend and frontend checks pass, or limitations are reported.
- Requirements and `docs/traceability.md` stay aligned with behavior.
- Update `memory-bank/progress.md` for meaningful implementation work.
- Update `activeContext.md`, `decisions.md`, or `architecture.md` only when priorities, decisions, or interfaces changed.
- No secrets, uploaded saves, local artifacts, virtual environments, or generated output are committed.
- Close with a concise change summary and the exact commands and results.

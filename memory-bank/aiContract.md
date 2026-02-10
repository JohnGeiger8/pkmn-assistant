# AI Contract

## Prime Directive
Make small, testable changes that keep the repo green.

## Required Workflow
- Always propose a Plan (files touched + commands to run) before editing.
- Prefer the smallest diff that satisfies the requirement.
- Do not refactor unrelated code.

## Coding Standards
### Backend (Flask)
- Use type hints where practical.
- No business logic in route handlers; keep routes thin.
- Add/adjust tests for behavior changes.

### Frontend (Angular)
- Prefer services for API calls, avoid logic in components.
- Keep UI state minimal and explicit.
- Add/adjust tests for non-trivial UI logic.

## Testing Rules
- Every new endpoint: add at least 1 integration test.
- Any parsing logic change: update fixtures or golden outputs.
- Always run:
  - backend: `pytest`
  - frontend: `npm test` (or `ng test`)

## Forbidden
- Introducing new frameworks without a decision record.
- Large rewrites “for cleanliness.”
- Adding auth/accounts unless explicitly required.

## Definition of Done (per task)
- Code compiles
- Tests pass
- Docs updated if behavior or interfaces changed

## Task Closeout (Required)
- Summarize changes in 5 bullets
- List commands run + results
- Update memory-bank:
  - progress.md (always)
  - activeContext.md (if priorities changed)
  - decisions.md (if a new decision was made)
  - architecture.md (if interfaces/structure changed)

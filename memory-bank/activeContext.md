# Active Context

## Read First
- memory-bank/aiContract.md
- memory-bank/architecture.md
- memory-bank/decisions.md

## Current Focus
- Maintain session management + save upload backend path with S3-compatible storage.
- Continue Milestone 1 backend/FE flow (save parsing, inventory review, recommendation).
- Keep future ML expansion in scope, but not blocking.

## Recent Decisions
- Shift MVP data source to save file import and parsing instead of screenshot parsing.
- Keep inventory exclusion toggles so users can remove Pokémon from eligibility.
- Parse eggs as their hatch species when the save format provides it.
- Update API contracts to use save upload endpoint `POST /api/sessions/{id}/save` (deprecate image uploads).
- Maintain strict requirements mapping to tests via `docs/traceability.md`.
- Use env-driven S3 config loaded via `.env` in Flask app startup.
- Use MinIO in docker-compose for local S3-compatible development.
- Keep upload size calculation in route (before transfer), not in storage helper.

## Next Steps
- Continue Milestone 1 implementation after upload foundation: save parsing, inventory review, recommendation endpoint.
- Add/verify frontend save upload UI integration to call `POST /api/sessions/{id}/save`.
- Add broader test pass + regression checks around storage error handling.
- Build acceptance dataset workflow and CI reporting for ML gating once ML pipeline exists.

## Notes
- Eggs are parsed as their hatch species when available.
- Unown forms collapsed; shiny treated as normal species.
- No competitive assumptions (IVs/EVs, held items).
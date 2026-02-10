# Active Context

## Read First
- memory-bank/aiContract.md
- memory-bank/architecture.md
- memory-bank/decisions.md

## Current Focus
- Update memory bank and architecture to align with save-file parsing MVP.
- Maintain session management, save upload, parsing, inventory review, and recommendation flow.
- Keep future ML expansion in scope, but not blocking.

## Recent Decisions
- Shift MVP data source to save file import and parsing instead of screenshot parsing.
- Keep inventory exclusion toggles so users can remove Pokémon from eligibility.
- Parse eggs as their hatch species when the save format provides it.
- Update API contracts to use save upload endpoint `POST /api/sessions/{id}/save` (deprecate image uploads).
- Maintain strict requirements mapping to tests via `docs/traceability.md`.

## Next Steps
- Continue implementation of Milestone 1 scope (session management, save upload UI/API, save parsing, inventory review, recommendation endpoint).
- Update frontend/backend contracts and docs to remove image upload references.
- Build acceptance dataset workflow and CI reporting for ML gating once ML pipeline exists.
- Add `.env.example` once backend configuration expands.

## Notes
- Eggs are parsed as their hatch species when available.
- Unown forms collapsed; shiny treated as normal species.
- No competitive assumptions (IVs/EVs, held items).
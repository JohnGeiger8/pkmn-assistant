# Active Context

## Current Focus
- Initialize memory bank documentation from existing project docs.
- Capture requirements, milestones, and dataset/traceability details for MVP.
- Stand up backend Flask scaffold and document local setup.
- Wire docker-compose to run frontend + backend together.
- Add Angular dev server proxy for `/api`.
- Finalize environment-based API base URLs and verify frontend can call backend.
- Fix docker compose proxy to target backend service name.

## Recent Decisions
- Use Milestone 1 walking skeleton with manual Pokémon entry to validate app flow before ML integration.
- Maintain strict requirements mapping to tests via `docs/traceability.md`.
- Standardize backend setup on Python 3.14 with `venv` + `pip` + `requirements.txt`.
- Add docker-compose services for frontend (Angular) and backend (Flask).
- Configure Angular dev server proxy to target the Flask backend on port 5000.
- Use Angular environment files for API base URL (dev `/api`, prod full host URL).
- Add docker-specific proxy config pointing to `http://backend:5000`.

## Next Steps
- Continue implementation of Milestone 1 scope (session management, upload UI/API, manual picker, recommendation endpoint).
- Build acceptance dataset workflow and CI reporting for Top-3 accuracy gating once ML pipeline exists.
- Add `.env.example` once backend configuration expands.

## Notes
- Eggs are excluded from identification and evaluation.
- Unown forms collapsed; shiny treated as normal species.
- No competitive assumptions (IVs/EVs, held items).
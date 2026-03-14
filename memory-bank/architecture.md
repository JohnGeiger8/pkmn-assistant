# Architecture

## Overview
- Angular frontend calls Flask REST API.
- Stateless backend except for session records.
- S3-compatible object storage holds uploaded save files (TTL-limited).

## Components
### Frontend (Angular)
- Pages:
  - Upload Save
  - Pokemon Inventory Review
  - Recommendation Results
- Services:
  - SessionService
  - SaveUploadService
  - PokemonInventoryService
  - RecommendationService

### Backend (Flask)
- Modules:
  - `app/routes.py` (session + save upload endpoints)
  - `app/sessions.py` (in-memory session store with TTL)
  - `app/storage.py` (S3-compatible upload helper)
  - `app/config.py` (env-driven runtime config)

## Data Flow (Milestone 1)
1. FE creates session
2. FE uploads save -> BE -> S3
3. BE parses save -> inventory JSON
4. FE shows inventory; user excludes entries
5. FE requests recommendation -> team + explanation

### Upload Path (Implemented)
1. `POST /api/sessions/{sessionId}/save` receives multipart `file`.
2. BE validates session existence, extension (`.sav`/`.dsv`), and non-empty payload.
3. BE computes size before transfer, then uploads to S3-compatible storage.
4. Object key format: `sessions/{sessionId}/save/{original_filename}`.
5. Response returns `fileName`, `storageKey`, and `size`.

## API Conventions
- Base path: `/api`
- Session scoped endpoints: `/api/sessions/{sessionId}/...`
- Errors: consistent JSON `{ code, message, details? }`

## Storage & TTL
- Save files stored under: `sessions/{sessionId}/save/{original_filename}`
- TTL cleanup job removes expired session artifacts

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
  - routes/
  - services/
  - parsing/
  - models/
  - storage/

## Data Flow (Milestone 1)
1. FE creates session
2. FE uploads save -> BE -> S3
3. BE parses save -> inventory JSON
4. FE shows inventory; user excludes entries
5. FE requests recommendation -> team + explanation

## API Conventions
- Base path: `/api`
- Session scoped endpoints: `/api/sessions/{sessionId}/...`
- Errors: consistent JSON `{ code, message, details? }`

## Storage & TTL
- Save files stored under: `sessions/{sessionId}/save/{saveId}`
- TTL cleanup job removes expired session artifacts

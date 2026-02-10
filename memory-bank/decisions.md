# Decisions (ADRs-lite)

## D-001: Save-import first MVP
**Decision:** MVP uses save file import for Gen 3.
**Why:** Reduces ML risk; provides accurate inventory.
**Implications:** Parsing + fixtures are critical; screenshot CV is future milestone.

## D-002: Angular + Flask
**Decision:** Angular FE + Flask API.
**Why:** Familiar stack; clear separation.
**Implications:** CORS, consistent API client patterns.

## D-003: S3-compatible storage for uploads
**Decision:** Uploads stored in S3-compatible object storage with TTL cleanup.
**Why:** Production-like; simple scaling.
**Implications:** Need local dev (MinIO) and TTL deletion strategy.

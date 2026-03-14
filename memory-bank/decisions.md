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

## D-004: Local object storage via MinIO in docker-compose
**Decision:** Use MinIO services in docker-compose for local S3-compatible upload testing.
**Why:** Enables realistic upload behavior without AWS dependencies.
**Implications:** Requires stable MinIO image tags, bucket bootstrap, and env vars (`S3_*`) aligned between backend and compose.

## D-005: Upload metadata handling for stream safety
**Decision:** Compute uploaded file size in route before transfer; storage helper performs upload only.
**Why:** Transfer layer may close request stream, making post-upload stream reads unsafe.
**Implications:** Keep request-derived metadata (like size) in route/service layer before storage call.

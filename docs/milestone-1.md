# Milestone 1 — Walking Skeleton (No ML)

**Goal:**  
Deliver a complete end-to-end app flow using **manual Pokémon entry** instead of ML, proving:
- session management
- multi-image upload
- team recommendation
- explanation output

This milestone intentionally avoids ML to reduce risk and unblock progress.

---

## Tech Stack
- **Frontend:** Angular (web; mobile + desktop browsers)
- **Backend:** Flask (API)
- **ML (future):** PyTorch
- **Storage:** S3-compatible object storage (images)
- **CI/CD:** GitHub Actions

---

## A) Repository & Dev Environment

### A1. Monorepo Structure
- frontend # Angular app
- backend # Flask API
- docs # SRS, traceability, dataset definitions
- artifacts # CI outputs (gitignored)
- docker-compose.yml # Optional local dev
- README.md

**Done when:**
- Frontend and backend can be run locally
- Clear README instructions exist

---

### A2. Local Dev Setup (Optional but Recommended)
- `docker-compose.yml` with:
  - `frontend` service
  - `backend` service
- Shared environment config for API base URL

**Done when:**
- One command starts both FE and BE
- FE can call BE endpoints successfully

---

## B) Backend — Session & Upload API

### B1. Session Management
**Endpoints**
- `POST /api/sessions` → `{ session_id }`
- `GET /api/sessions/{id}` → session state

**Notes**
- Sessions may be stored in memory initially
- Structure should allow future migration (Redis/Postgres)

**Done when:**
- Sessions persist across multiple requests

---

### B2. Image Upload
**Endpoint**
- `POST /api/sessions/{id}/images` (multipart)

**Behavior**
- Accept multiple images per session
- Store images in S3-compatible storage
- Return `{ image_id, status }`

**Done when:**
- User can upload 2+ images into the same session
- Session lists uploaded images

---

### B3. TTL Cleanup (Simple)
- Images tagged with upload timestamp
- Cleanup job (scheduled or opportunistic)
- Configurable TTL (e.g., 24 hours)

**Done when:**
- Images older than TTL are deleted
- No permanent image storage

---

## C) Frontend — Upload & Review Flow (No ML)

### C1. Session Initialization
- Create session on app load
- Persist session ID client-side

**Done when:**
- Refreshing the page retains the same session

---

### C2. Multi-Image Upload UI
- File picker (multiple files)
- Upload progress indicator
- Uploaded image list

**Done when:**
- User can upload multiple PC screenshots/photos

---

### C3. Review Screen v0 (Manual Inventory)
- Display list/table of Pokémon entries
- Button: “Add Pokémon”

**Done when:**
- User can create an inventory manually

---

### C4. Manual Pokémon Picker
- Dropdown/autocomplete of Gen 3 Pokémon
- Add/remove entries
- Duplicates allowed
- Entries default to “confirmed”

**Done when:**
- User can quickly enter ≥6 Pokémon without friction

---

## D) Recommendation Engine v0 (Rules-Only)

### D1. Recommendation API
**Endpoint**
- `POST /api/sessions/{id}/recommendation`

**Input**
- Confirmed Pokémon species list

**Output**
- Up to 6 Pokémon (or fewer if pool <6)
- Simple explanation text

**Logic (MVP)**
- Type coverage
- Offensive/defensive balance (Gen 3 mechanics)

**Done when:**
- Deterministic team is always returned

---

### D2. Results UI
- Display recommended team
- Display explanation

**Done when:**
- Full happy path completes end-to-end

---

## E) CI/CD (GitHub Actions)

### E1. Backend CI
- Lint (ruff/flake8)
- Unit tests (pytest)

**Done when:**
- CI blocks PRs on failure

---

### E2. Frontend CI
- Lint
- Unit tests

**Done when:**
- CI blocks PRs on failure

---

### E3. End-to-End Test
- Playwright:
  1. Create session
  2. Upload 2 images
  3. Manually add Pokémon
  4. Generate recommendation

**Done when:**
- E2E test runs in CI
- Screenshots/videos captured on failure

---

## Deliverables
- Working Angular + Flask app
- Multi-image session flow
- Manual Pokémon inventory
- Team recommendation + explanation
- CI with at least one E2E test

---

## Exit Criteria
Milestone 1 is complete when:
- The full app loop works without ML
- User never types Pokémon names outside a picker
- Architecture supports later ML insertion without refactor

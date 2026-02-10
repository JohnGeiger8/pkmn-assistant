# Milestone 1 — Save Import + Basic Team Builder (No ML)

## Purpose

Establish a complete, end-to-end functional application loop using **Pokémon save file import** as the data source and a **rules-based team recommendation engine**.

This milestone intentionally excludes machine learning in order to:

- Deliver a working, usable product quickly
- Validate architecture and data flow
- Reduce early technical risk
- Create a stable foundation for future ML integration

**Important:**  
This milestone does **not** deprioritize ML. It enables later ML milestones by creating the infrastructure and user flow they will plug into.

---

## High-Level Goal

A user can:

1. Upload a Generation 3 Pokémon save file
2. View all Pokémon in their PC and party
3. Generate a recommended in-game team
4. Receive a simple explanation of the recommendation

No screenshot parsing or ML classification is required in this phase.

---

## Supported Scope

### Games
- Pokémon Ruby
- Pokémon Sapphire
- Pokémon Emerald
- Pokémon FireRed
- Pokémon LeafGreen

### Save Formats (Initial Target)
- `.sav`
- `.dsv`

Additional formats may be added later.

---

## Technology Stack

- **Frontend:** Angular
- **Backend:** Flask (REST API)
- **ML (Future):** PyTorch
- **Storage:** S3-compatible object storage
- **CI/CD:** GitHub Actions

---

## System Capabilities

### 0. Repository & Dev Environment

#### 0.1 Monorepo Structure
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

### 0.2 Local Dev Setup (Optional but Recommended)
- `docker-compose.yml` with:
  - `frontend` service
  - `backend` service
- Shared environment config for API base URL

**Done when:**
- One command starts both FE and BE
- FE can call BE endpoints successfully

### 1. Session Management
A session represents one active team-building workspace.

**Capabilities**
- Create anonymous session
- Associate uploaded save files with session
- TTL-based expiration and cleanup

---

### 2. Save File Upload

**Endpoint**
- POST /api/sessions/{id}/save

**Behavior**
- Accept a supported save file
- Store file in S3-compatible storage
- Associate file with session
- Return status and metadata

---

### 3. Save Parsing

**Responsibilities**
- Extract all Pokémon in party and PC
- Capture:
  - Species
  - Level
  - Types
  - Held item (optional MVP)
  - Moves (optional MVP)
- Ignore IV/EV/stat math in MVP unless easily available

**Output**
Structured JSON representation of user’s available Pokémon.

---

### 4. Pokémon Inventory Display (Frontend)

**Features**
- List all available Pokémon
- Allow filtering/search by species
- Allow manual removal from pool
- Mark entries as “eligible” or “excluded”

---

### 5. Team Recommendation Engine (Rules-Based)

**Endpoint**
- POST /api/sessions/{id}/recommendation

**Inputs**
- Confirmed Pokémon list

**Outputs**
- Up to 6 Pokémon
- Explanation text

**Logic (MVP)**
- Type coverage balance
- Offensive vs defensive spread
- Avoid duplicate primary types when possible
- No IV/EV or competitive assumptions

---

### 6. Recommendation Explanation

Explanation SHALL include:
- Type coverage summary
- Balance rationale
- High-level reasoning only (no deep stat math)

---

## Non-Goals (Milestone 1)

- Screenshot image parsing
- Sprite classification ML
- Damage calculators
- Trainer battle simulations
- Competitive/meta optimization
- ROM hack support
- User accounts or authentication

---

## Data Requirements

### Static Data Needed
- Gen 3 Pokémon species list
- Type mappings
- Basic learnset data (optional)
- Held item list (optional)

---

## CI/CD Requirements

### Backend
- Linting
- Unit tests
- Save parsing tests

### Frontend
- Linting
- Unit tests

### End-to-End Test
Automated test covering:
1. Session creation
2. Save upload
3. Pokémon list retrieval
4. Team generation
5. Explanation rendering

Artifacts captured on failure.

---

## Deliverables

- Angular web application
- Flask REST API
- Save parsing pipeline
- Pokémon inventory UI
- Rules-based team recommendation engine
- CI pipeline with one E2E test
- Documentation updates

---

## Exit Criteria

Milestone 1 is complete when:

- A user can upload a supported save file and view all Pokémon
- A team recommendation is generated successfully
- The full flow works without ML
- No manual data entry is required
- CI pipelines pass consistently

---

## Future Milestone Alignment

This milestone enables:

- **Milestone 2:** Screenshot PC parsing (Computer Vision ML)
- **Milestone 3:** ML-driven team recommendation and ranking
- **Milestone 4:** Advanced battle modeling and predictive analytics

The system architecture SHALL be designed so these features can be added without refactoring the core application flow.

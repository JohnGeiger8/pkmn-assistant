# Traceability Matrix — Generation 3 Pokémon AI Team Assistant (MVP)

## Purpose
This matrix maps Software Requirements Specification (SRS) requirements to:
- Owning subsystem
- Verification method
- CI test identifiers
- Evidence artifacts

It ensures all SHALL/MUST requirements are:
- Implemented
- Tested
- Measurable
- Auditable

---

## Subsystem Legend

| Code | Subsystem |
|------|---------|
| FE | Angular Frontend |
| BE | Flask Backend |
| SES | Session Management |
| SAVE | Save File Ingestion |
| PARSE | Save Parsing Engine |
| INV | Pokémon Inventory UI |
| REC | Team Recommendation Engine |
| EXP | Explanation Generator |
| OBS | Observability / Logging / Privacy |
| QA | Test Harness / CI |

---

## Test Type Legend

| Code | Meaning |
|------|--------|
| UNIT | Unit Test |
| INT | Integration Test |
| E2E | End-to-End Test |
| VAL | Validation Dataset Test |
| SEC | Security / Privacy Test |
| LOAD | Performance / Load Test |
| GOLD | Golden Output Comparison |

---

## 5.1 Session Management

| Requirement | Owner | Verification | Test ID | Pass Criteria | Evidence |
|------------|------|-------------|--------|--------------|---------|
| REQ-SES-001 | SES/BE | INT | T-SES-001-INT-01 | Session created with valid ID | API response JSON |
| REQ-SES-002 | SES/BE | INT | T-SES-002-INT-01 | Uploaded artifacts linked to session | Session state snapshot |
| REQ-SES-003 | SES/OBS | SEC/INT | T-SES-003-SEC-01 | Expired sessions removed | TTL audit log |

---

## 5.2 Save File Input

| Requirement | Owner | Verification | Test ID | Pass Criteria | Evidence |
|------------|------|-------------|--------|--------------|---------|
| REQ-SAVE-001 | SAVE/BE | E2E | T-SAVE-001-E2E-01 | Save file accepted and stored | Upload logs |
| REQ-SAVE-002 | SAVE/BE | UNIT | T-SAVE-002-UNIT-01 | `.sav` and `.dsv` accepted | Unit report |
| REQ-SAVE-003 | SAVE/BE | UNIT | T-SAVE-003-UNIT-01 | Corrupt saves rejected gracefully | Error response snapshot |

---

## 5.3 Save Parsing & Pokémon Extraction

| Requirement | Owner | Verification | Test ID | Pass Criteria | Evidence |
|------------|------|-------------|--------|--------------|---------|
| REQ-PARSE-001 | PARSE | VAL | T-PARSE-001-VAL-01 | All party + PC Pokémon extracted | Fixture comparison JSON |
| REQ-PARSE-002 | PARSE | UNIT | T-PARSE-002-UNIT-01 | Species/Level/Types present | Unit output JSON |
| REQ-PARSE-003 | PARSE | UNIT | T-PARSE-003-UNIT-01 | Optional data parsed when available | Fixture diff |
| REQ-PARSE-004 | PARSE | UNIT | T-PARSE-004-UNIT-01 | Eggs excluded if enabled | Extraction log |

---

## 5.4 Pokémon Inventory Review

| Requirement | Owner | Verification | Test ID | Pass Criteria | Evidence |
|------------|------|-------------|--------|--------------|---------|
| REQ-INV-001 | FE | E2E | T-INV-001-E2E-01 | Pokémon list displayed | UI screenshot |
| REQ-INV-002 | FE/BE | E2E | T-INV-002-E2E-01 | Exclusion toggle works | UI + API trace |
| REQ-INV-003 | BE | INT | T-INV-003-INT-01 | Duplicate Pokémon preserved | Inventory JSON |

---

## 5.5 Team Recommendation Engine

| Requirement | Owner | Verification | Test ID | Pass Criteria | Evidence |
|------------|------|-------------|--------|--------------|---------|
| REQ-TEAM-001 | REC | E2E | T-TEAM-001-E2E-01 | Exactly one team returned | Response JSON |
| REQ-TEAM-002 | REC | UNIT | T-TEAM-002-UNIT-01 | Team size = min(6, pool size) | Unit report |
| REQ-TEAM-003 | REC | INT | T-TEAM-003-INT-01 | Only eligible Pokémon selected | Fixture diff |
| REQ-TEAM-004 | REC | GOLD | T-TEAM-004-GOLD-01 | Known fixture yields expected team | Golden output |
| REQ-TEAM-005 | REC | SEC | T-TEAM-005-SEC-01 | No IV/EV/meta logic present | Static scan log |

---

## 5.6 Recommendation Explanation

| Requirement | Owner | Verification | Test ID | Pass Criteria | Evidence |
|------------|------|-------------|--------|--------------|---------|
| REQ-EXP-001 | EXP | E2E | T-EXP-001-E2E-01 | Explanation returned | Response JSON |
| REQ-EXP-002 | EXP | GOLD | T-EXP-002-GOLD-01 | Explanation mentions coverage & balance | Golden text diff |

---

## 6. Non-Functional Requirements

| Requirement | Owner | Verification | Test ID | Pass Criteria | Evidence |
|------------|------|-------------|--------|--------------|---------|
| REQ-PERF-001 | BE/REC | LOAD | T-PERF-001-LOAD-01 | p95 ≤ 5s | Load report JSON |
| REQ-REL-001 | BE | E2E | T-REL-001-E2E-01 | Invalid save handled gracefully | Error UI screenshot |
| REQ-PRIV-001 | OBS | SEC | T-PRIV-001-SEC-01 | Save deleted after TTL | Storage audit |
| REQ-PRIV-002 | BE | E2E | T-PRIV-002-E2E-01 | No login required | CI E2E log |

---

## 7. Machine Learning (Future Scope — Not MVP Gating)

| Requirement | Owner | Verification | Test ID | Evidence |
|------------|------|-------------|--------|---------|
| REQ-ML-001 | ML | VAL | T-ML-001-VAL-01 | Acceptance dataset metrics |
| REQ-ML-002 | ML | VAL | T-ML-002-VAL-01 | Ranking accuracy report |
| REQ-ML-003 | ML/BE | INT | T-ML-003-INT-01 | Deployment logs |
| REQ-ML-004 | QA | VAL | T-ML-004-VAL-01 | CI benchmark artifact |

---

## Evidence Artifact Locations (Suggested)
/artifacts/
benchmarks/
golden/
load/
logs/
screenshots/

---

## Notes

- ML requirements are **non-blocking for MVP completion**
- All Test IDs are CI-friendly and map 1:1 to automation jobs
- Golden outputs SHOULD be versioned
- Acceptance datasets SHALL be immutable per version

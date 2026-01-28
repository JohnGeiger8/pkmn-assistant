# Traceability Matrix (MVP) — Gen 3 PC Team Assistant

## Legend
- **Owner:** FE, BE, IMG, DET, ID, REC, EXP, OBS, QA
- **Test Types:** UNIT, INT, E2E, VAL, GOLD, LOAD, SEC
- **Evidence:** CI artifacts (JUnit/XML, JSON metrics, screenshots, videos)

---

## 5.1 Image Input & Session Management

| Requirement | Owner | Verification | Test ID(s) | Pass/Fail | Evidence |
|---|---|---|---|---|---|
| REQ-IMG-001 | FE/BE | E2E | T-IMG-REQ-IMG-001-E2E-01 | Upload ≥2 images; both in session | Playwright video/log + API traces |
| REQ-IMG-002 | BE | INT | T-IMG-REQ-IMG-002-INT-01 | Unified pool contains all images’ mons | Backend report + pool JSON snapshot |
| REQ-IMG-003 | FE/BE | E2E/UNIT | T-IMG-REQ-IMG-003-E2E-01, T-IMG-REQ-IMG-003-UNIT-01 | Accept PNG/JPG/JPEG; HEIC if provided; reject others | CI logs + UI screenshots |
| REQ-IMG-004 | IMG/DET/ID | VAL | T-IMG-REQ-IMG-004-VAL-01 | Meets accuracy on screenshot+photo subsets | benchmarks/accuracy_by_subset.json |
| REQ-IMG-005 | IMG | UNIT/GOLD | T-IMG-REQ-IMG-005-UNIT-01, T-IMG-REQ-IMG-005-GOLD-01 | Orientation normalized; crops match canonical | Golden diffs + crop outputs |

---

## 5.2 PC Layout Detection & Slot Extraction

| Requirement | Owner | Verification | Test ID(s) | Pass/Fail | Evidence |
|---|---|---|---|---|---|
| REQ-PC-001 | DET | VAL | T-PC-REQ-PC-001-VAL-01 | ≥99% grid detection or defined fallback | benchmarks/grid_detection.json |
| REQ-PC-002 | DET | VAL | T-PC-REQ-PC-002-VAL-01 | ≥98% occupancy accuracy | benchmarks/occupancy.json |
| REQ-PC-003 | DET | GOLD/VAL | T-PC-REQ-PC-003-GOLD-01, T-PC-REQ-PC-003-VAL-01 | Crop IoU ≥0.9 avg | IoU JSON + overlay images |
| REQ-PC-004 | DET/ID | VAL | T-PC-REQ-PC-004-VAL-01 | Still meets Top-3 target with artifacts | delta report + samples |

---

## 5.3 Pokémon Identification

| Requirement | Owner | Verification | Test ID(s) | Pass/Fail | Evidence |
|---|---|---|---|---|---|
| REQ-ID-001 | ID | VAL | T-ID-REQ-ID-001-VAL-01 | Report Top-1/Top-3; Top-3 meets target | benchmarks/id_accuracy.json |
| REQ-ID-002 | ID/BE | UNIT | T-ID-REQ-ID-002-UNIT-01 | Always returns Top-3 + confidence format | Unit report + sample JSON |
| REQ-ID-003 | ID/QA | VAL (Acceptance) | T-ID-REQ-ID-003-VAL-ACCEPT-01 | **Per-slot** Top-3 ≥95% on acceptance_v1 | acceptance_v1_metrics.json + run metadata |
| REQ-ID-004 | DET/ID/BE | VAL | T-ID-REQ-ID-004-VAL-01 | Eggs excluded from pool/UI | egg_filter.json + UI snapshot |
| REQ-ID-005 | ID | VAL | T-ID-REQ-ID-005-VAL-01 | Shiny treated as normal | subset metrics report |
| REQ-ID-006 | ID | UNIT | T-ID-REQ-ID-006-UNIT-01 | All Unown forms -> Unown | Unit report |
| REQ-ID-007 | BE | INT | T-ID-REQ-ID-007-INT-01 | Duplicates preserved as instances | pool snapshot JSON |

---

## 5.4 User Confirmation & Correction

| Requirement | Owner | Verification | Test ID(s) | Pass/Fail | Evidence |
|---|---|---|---|---|---|
| REQ-UC-001 | FE/BE | E2E | T-UC-REQ-UC-001-E2E-01 | Review screen shown pre-recommendation | Playwright evidence |
| REQ-UC-002 | FE/BE | E2E | T-UC-REQ-UC-002-E2E-01 | Correction works; skip path works | API trace + screenshots |
| REQ-UC-003 | BE/FE | INT/E2E | T-UC-REQ-UC-003-INT-01, T-UC-REQ-UC-003-E2E-01 | Recommendation blocked until confirmed | response assertions + UI state |
| REQ-UC-004 | OBS/BE | INT/SEC | T-UC-REQ-UC-004-INT-01 | If enabled, logs w/o raw image retention | event logs + privacy audit |

---

## 5.5 Team Recommendation Engine

| Requirement | Owner | Verification | Test ID(s) | Pass/Fail | Evidence |
|---|---|---|---|---|---|
| REQ-TEAM-001 | REC/BE | E2E | T-TEAM-REQ-TEAM-001-E2E-01 | One team returned | response snapshot |
| REQ-TEAM-002 | REC | UNIT | T-TEAM-REQ-TEAM-002-UNIT-01 | Size == min(6, pool size) | unit report |
| REQ-TEAM-003 | BE/REC | INT | T-TEAM-REQ-TEAM-003-INT-01 | Unconfirmed excluded | fixture + output JSON |
| REQ-TEAM-004 | REC | UNIT/GOLD | T-TEAM-REQ-TEAM-004-UNIT-01, T-TEAM-REQ-TEAM-004-GOLD-01 | Fixtures yield expected ordering | golden diffs |
| REQ-TEAM-005 | REC/BE | SEC | T-TEAM-REQ-TEAM-005-SEC-01 | No IV/EV/meta endpoints/features | API contract + static checks |

---

## 5.6 Recommendation Explanation

| Requirement | Owner | Verification | Test ID(s) | Pass/Fail | Evidence |
|---|---|---|---|---|---|
| REQ-EXP-001 | EXP/BE | E2E | T-EXP-REQ-EXP-001-E2E-01 | Explanation included | response snapshot |
| REQ-EXP-002 | EXP | GOLD | T-EXP-REQ-EXP-002-GOLD-01 | Mentions coverage + balance | golden text diffs |

---

## 6. Non-Functional Requirements

| Requirement | Owner | Verification | Test ID(s) | Pass/Fail | Evidence |
|---|---|---|---|---|---|
| REQ-PERF-001 | BE/DET/ID | LOAD | T-PERF-REQ-PERF-001-LOAD-01 | p95 ≤5s nominal load | load report + latency JSON |
| REQ-PERF-002 | DET/ID | VAL | T-PERF-REQ-PERF-002-VAL-01 | Top-3 drop ≤5% abs on degraded set | robustness delta report |
| REQ-REL-001 | BE | INT/E2E | T-REL-REQ-REL-001-INT-01, T-REL-REQ-REL-001-E2E-01 | One image fails; session still works | session audit JSON |
| REQ-REL-002 | FE/BE | E2E | T-REL-REQ-REL-002-E2E-01 | Low confidence prompts user | UI screenshots + logs |
| REQ-PRIV-001 | BE/OBS | SEC | T-PRIV-REQ-PRIV-001-SEC-01 | TTL deletion verified | storage audit logs |
| REQ-PRIV-002 | FE/BE | E2E | T-PRIV-REQ-PRIV-002-E2E-01 | No auth required | E2E logs |

# Software Requirements Specification (SRS)

**Project:** Generation 3 Pokémon AI Team Assistant (MVP)  
**Document Type:** NASA-Style Level-3 Software Requirements  
**Revision:** 2.0  
**Status:** Approved for Implementation  

---

## 1. Purpose

The purpose of this system is to assist players of Generation 3 Pokémon games in building a balanced in-game team by ingesting authoritative player data and generating an intelligent team recommendation using game-specific logic.

The MVP SHALL use **save file import** as the primary data source in order to:
- maximize correctness and completeness of Pokémon data
- eliminate manual data entry
- reduce early technical risk

The system architecture SHALL explicitly support future **machine-learning–based perception and recommendation capabilities**, including screenshot-based computer vision and ML-driven team optimization.

---

## 2. Mission Objectives

### 2.1 Primary Objective

The system SHALL allow a user to:
1. Upload a supported Generation 3 Pokémon save file  
2. Automatically extract all owned Pokémon from the save  
3. Generate a balanced six-Pokémon team using only extracted Pokémon  
4. Receive a simple explanation of the recommendation  

---

### 2.2 Success Criteria

The MVP SHALL be considered successful if:
- Users can complete the full flow without manually entering Pokémon data  
- Pokémon extraction from save files is accurate and complete  
- A valid team recommendation is produced within performance constraints  
- The system architecture supports future ML-driven extensions without refactor  

---

## 3. Supported Games & Scope

### 3.1 Supported Titles

The system SHALL support the following Generation 3 games:
- Pokémon Ruby  
- Pokémon Sapphire  
- Pokémon Emerald  
- Pokémon FireRed  
- Pokémon LeafGreen  

---

### 3.2 Assumptions

- Games are unmodified retail versions  
- English-language save formats  
- Standard save structures  
- No ROM hacks in MVP  

---

## 4. System Overview

### 4.1 High-Level Architecture

The system SHALL consist of:
- A web-based client supporting desktop and mobile browsers  
- A server-side backend providing:
  - Save file ingestion and parsing  
  - Pokémon inventory extraction  
  - Team recommendation logic  
  - (Future) ML-based perception and recommendation services  

---

### 4.2 Operational Flow (MVP)

1. User uploads a save file  
2. System parses the save file  
3. System extracts all owned Pokémon  
4. User reviews and optionally excludes Pokémon  
5. System generates a single recommended team  
6. System explains the recommendation  

---

## 5. Functional Requirements

### 5.1 Session Management

**REQ-SES-001**  
The system SHALL create an anonymous session representing a single team-building workspace.

**REQ-SES-002**  
All uploaded artifacts and derived data SHALL be associated with a session.

**REQ-SES-003**  
Sessions SHALL expire automatically after a configurable TTL.

---

### 5.2 Save File Input

**REQ-SAVE-001**  
The system SHALL accept Generation 3 Pokémon save files.

**REQ-SAVE-002**  
Supported save formats SHALL include:
- `.sav`
- `.dsv`

**REQ-SAVE-003**  
The system SHALL validate save file integrity prior to parsing.

---

### 5.3 Save Parsing & Pokémon Extraction

**REQ-PARSE-001**  
The system SHALL extract all Pokémon present in:
- Player party
- PC storage

**REQ-PARSE-002**  
For each Pokémon, the system SHALL extract at minimum:
- Species
- Level
- Primary and secondary types

**REQ-PARSE-003**  
The system MAY extract additional data (e.g., moves, held items) if readily available.

**REQ-PARSE-004**  
Egg Pokémon MAY be excluded from extraction.

---

### 5.4 Pokémon Inventory Review

**REQ-INV-001**  
The system SHALL present all extracted Pokémon to the user.

**REQ-INV-002**  
The user SHALL be able to exclude Pokémon from eligibility.

**REQ-INV-003**  
Duplicate Pokémon SHALL be allowed and treated as separate instances.

---

### 5.5 Team Recommendation Engine

**REQ-TEAM-001**  
The system SHALL generate one recommended team per session.

**REQ-TEAM-002**  
The team SHALL contain:
- Up to 6 Pokémon  
- Fewer than 6 if the user owns fewer than 6 Pokémon  

**REQ-TEAM-003**  
Only Pokémon marked as eligible SHALL be considered.

**REQ-TEAM-004**  
Team selection SHALL consider Generation 3 mechanics, including:
- Type coverage  
- Physical vs special attack split (type-based)  
- Defensive balance  

**REQ-TEAM-005**  
The system SHALL NOT assume:
- Competitive movesets  
- IV or EV optimization  
- Breeding or trading  

---

### 5.6 Recommendation Explanation

**REQ-EXP-001**  
The system SHALL provide a simple explanation of the selected team.

**REQ-EXP-002**  
The explanation SHALL include:
- Type coverage summary  
- Balance rationale  

---

## 6. Non-Functional Requirements

### 6.1 Performance

**REQ-PERF-001**  
End-to-end processing time SHALL NOT exceed 5 seconds under nominal load.

---

### 6.2 Reliability

**REQ-REL-001**  
Malformed or unsupported save files SHALL result in graceful failure with user feedback.

---

### 6.3 Privacy & Data Handling

**REQ-PRIV-001**  
Uploaded save files SHALL NOT be permanently stored beyond session scope.

**REQ-PRIV-002**  
No user authentication or personally identifiable information SHALL be required.

---

## 7. Machine Learning System Requirements (Future Scope)

**REQ-ML-001**  
The system architecture SHALL support ML-driven perception components, including screenshot-based Pokémon identification.

**REQ-ML-002**  
The system architecture SHALL support ML-driven recommendation components beyond rule-based logic.

**REQ-ML-003**  
ML components SHALL run server-side.

**REQ-ML-004**  
ML components SHALL be evaluated using explicit acceptance datasets and CI gating.

---

## 8. Constraints & Explicit Non-Goals (MVP)

The system SHALL NOT:
- Perform damage calculations  
- Simulate trainer battles  
- Optimize competitive strategies  
- Support non-Gen-3 games  
- Require user accounts  

---

## 9. Failure Modes & Edge Cases

The system SHALL handle:
- Partial save corruption  
- Duplicate Pokémon  
- Saves with fewer than six Pokémon  

---

## 10. Verification & Validation

Each requirement SHALL be verifiable via:
- Save parsing unit tests  
- Known-good save fixtures  
- End-to-end flow tests  

---

## 11. MVP Exit Criteria

The MVP SHALL be considered complete when:
- Users can upload a supported save file and view all Pokémon  
- A valid team recommendation is generated  
- No manual Pokémon data entry is required  
- The system architecture clearly supports future ML expansion  

# Software Requirements Specification (SRS)

**Project:** Generation 3 Pokémon PC Screenshot Team Assistant (MVP)  
**Document Type:** NASA-Style Level-3 Software Requirements  
**Revision:** 1.0  
**Status:** Approved for Implementation  

---

## 1. Purpose

The purpose of this system is to assist players of Generation 3 Pokémon games in building a balanced in-game team by automatically identifying Pokémon available in the player’s PC storage using uploaded images and generating a recommended team using in-game logic.

The system prioritizes low-friction user experience, minimal manual input, and high identification reliability over competitive optimization.

---

## 2. Mission Objectives

### 2.1 Primary Objective

The system SHALL allow a user to:
1. Upload one or more images of Pokémon PC boxes  
2. Automatically identify all Pokémon present  
3. Generate a balanced six-Pokémon team using only identified Pokémon  

### 2.2 Success Criteria

The MVP SHALL be considered successful if:
- Pokémon identification achieves ≥95% Top-3 accuracy on Gen 3 PC sprites  
- Users can complete the flow without manually entering Pokémon names  
- A valid team recommendation is produced within performance constraints  

---

## 3. Supported Games & Scope

### 3.1 Supported Titles

The system SHALL support the following Generation 3 games:
- Pokémon Ruby  
- Pokémon Sapphire  
- Pokémon Emerald  
- Pokémon FireRed  
- Pokémon LeafGreen  

### 3.2 Assumptions

- Games are unmodified retail versions  
- English-language UI  
- Standard PC box layouts  
- No ROM hacks or custom sprite replacements  

---

## 4. System Overview

### 4.1 High-Level Architecture

The system SHALL consist of:
- A web-based client supporting desktop and mobile browsers  
- A server-side backend providing:
  - Image processing  
  - Pokémon identification (ML-based)  
  - Team recommendation logic  

### 4.2 Operational Flow

1. User uploads one or more PC images  
2. System detects and extracts Pokémon slots  
3. System identifies Pokémon species per slot  
4. User optionally corrects identifications  
5. System generates a single recommended team  
6. System explains the recommendation at a high level  

---

## 5. Functional Requirements

### 5.1 Image Input & Session Management

**REQ-IMG-001**  
The system SHALL accept multiple image uploads within a single user session.

**REQ-IMG-002**  
The system SHALL treat all uploaded images in a session as a single combined Pokémon pool.

**REQ-IMG-003**  
Supported image types SHALL include:
- PNG  
- JPG  
- JPEG  
- HEIC (if browser-supported)  

**REQ-IMG-004**  
The system SHALL support:
- Direct game screenshots  
- Phone photos of screens  

**REQ-IMG-005**  
The system SHALL normalize orientation and scale prior to analysis.

---

### 5.2 PC Layout Detection & Slot Extraction

**REQ-PC-001**  
The system SHALL detect Pokémon PC grid layouts automatically.

**REQ-PC-002**  
The system SHALL identify:
- Occupied slots  
- Empty slots  

**REQ-PC-003**  
The system SHALL extract individual Pokémon icon sprites from occupied slots.

**REQ-PC-004**  
The system SHALL tolerate UI artifacts including:
- Cursor overlays  
- Selection highlights  
- Minor motion blur  

---

### 5.3 Pokémon Identification

**REQ-ID-001**  
The system SHALL identify Pokémon species from Generation 3 PC icon sprites.

**REQ-ID-002**  
The system SHALL output the Top-3 most likely Pokémon species per slot with confidence scores.

**REQ-ID-003**  
The system SHALL achieve ≥95% Top-3 identification accuracy on validation data representative of real PC screenshots.

**REQ-ID-004**  
Eggs SHALL be ignored and SHALL NOT be identified or included in downstream processing.

**REQ-ID-005**  
Shiny Pokémon SHALL be treated as their normal species equivalents.

**REQ-ID-006**  
All Unown forms SHALL be identified as a single “Unown” species.

**REQ-ID-007**  
Duplicate Pokémon SHALL be allowed and treated as separate instances.

---

### 5.4 User Confirmation & Correction

**REQ-UC-001**  
The system SHALL present identified Pokémon to the user for confirmation prior to team generation.

**REQ-UC-002**  
User correction of misidentified Pokémon SHALL be optional.

**REQ-UC-003**  
The system SHALL NOT proceed to team recommendation until all identified Pokémon are either:
- Accepted  
- Corrected by the user  

**REQ-UC-004**  
User corrections MAY be logged for future model improvement.

---

### 5.5 Team Recommendation Engine

**REQ-TEAM-001**  
The system SHALL generate one recommended team per session.

**REQ-TEAM-002**  
The team SHALL contain:
- Up to 6 Pokémon  
- Fewer than 6 if the user owns fewer than 6 Pokémon  

**REQ-TEAM-003**  
Only Pokémon confirmed in the current session SHALL be eligible.

**REQ-TEAM-004**  
Team selection SHALL consider Generation 3 mechanics, including:
- Type coverage  
- Physical vs special attack split (type-based)  
- Defensive balance  
- Status utility potential  

**REQ-TEAM-005**  
The system SHALL NOT assume access to:
- Competitive movesets  
- IVs or EVs  
- Breeding or trading  

---

### 5.6 Recommendation Explanation

**REQ-EXP-001**  
The system SHALL provide a simple explanation of the selected team.

**REQ-EXP-002**  
The explanation SHALL include:
- Type coverage summary  
- Offensive/defensive balance rationale  

---

## 6. Non-Functional Requirements

### 6.1 Performance

**REQ-PERF-001**  
End-to-end processing time SHALL NOT exceed 5 seconds under nominal load.

**REQ-PERF-002**  
Identification SHALL be resilient to moderate image quality degradation.

---

### 6.2 Reliability

**REQ-REL-001**  
Partial failures (e.g., one image failing to parse) SHALL NOT invalidate the entire session.

**REQ-REL-002**  
The system SHALL fail gracefully and prompt user action when confidence thresholds are not met.

---

### 6.3 Privacy & Data Handling

**REQ-PRIV-001**  
Uploaded images SHALL NOT be permanently stored beyond session scope.

**REQ-PRIV-002**  
No personally identifiable information SHALL be required.

---

## 7. Machine Learning System Requirements

**REQ-ML-001**  
The identification system SHALL use an embedding-based or retrieval-based approach rather than a fixed closed-set classifier.

**REQ-ML-002**  
The system SHALL maintain a Generation 3 sprite reference gallery.

**REQ-ML-003**  
Synthetic training data SHALL be used to approximate real PC screenshot conditions.

**REQ-ML-004**  
The ML model SHALL run exclusively server-side.

---

## 8. Constraints & Explicit Non-Goals

The system SHALL NOT:
- Parse save files  
- Infer player progression  
- Optimize competitive strategies  
- Recommend held items or EV spreads  
- Support non-Gen-3 games in MVP  

---

## 9. Failure Modes & Edge Cases

The system SHALL handle:
- Partial PC pages  
- Repeated Pokémon across multiple images  
- Blurry or compressed phone photos  
- Mixed game screenshots within one session (treated uniformly)  

---

## 10. Verification & Validation

Each requirement SHALL be verifiable via:
- Synthetic PC box image tests  
- Real screenshot test sets  
- Manual validation against known Pokémon inventories  

---

## 11. MVP Exit Criteria

The MVP SHALL be considered complete when:
- ≥95% Top-3 identification accuracy is achieved  
- Users can upload multiple PC pages per session  
- A valid team is generated without manual Pokémon entry  
- Users can correct errors without blocking the flow  

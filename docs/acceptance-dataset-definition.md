# Acceptance Dataset Definition (Starter) — Gen 3 PC Identification (MVP)

**Dataset Name:** `acceptance_v1`  
**Purpose:** Gatekeeper dataset for MVP requirement **REQ-ID-003** (≥95% Top-3 accuracy, per-slot).  
**Scope:** Generation 3 Pokémon PC boxes only (R/S/E/FR/LG), English UI, unmodified games.

---

## 1) Evaluation Unit and Metric (Per-slot)

### 1.1 Evaluated Units
- **Occupied PC slots** only.
- **Empty slots** excluded.
- **Egg slots** excluded entirely (ignored per REQ-ID-004).

### 1.2 Ground Truth Label
- Ground truth for each evaluated slot is a **species label**.
- **Shiny** is ignored (label is the normal species).
- **Unown** forms are collapsed to the single label `Unown`.

### 1.3 Metric Definition: Top-3 Accuracy (Per-slot)
For each evaluated occupied slot `i`:
- Model returns `Top3(i)` = three candidate species
- Ground truth is `GT(i)`

A slot is correct if: `GT(i) ∈ Top3(i)`

**Top-3 Accuracy** = `(# correct slots) / (# evaluated slots)`

**Acceptance Criterion:** Top-3 Accuracy ≥ **0.95** on `acceptance_v1`.

---

## 2) Dataset Composition Targets (Acceptance v1)

### 2.1 Size Targets
- **Images:** ≥ **200**
- **Labeled occupied slots:** **4,000–8,000** total

### 2.2 Capture Type Mix
- **Screenshots:** ~**60%**
- **Phone photos:** ~**40%**  
  Phone photos must include a variety of:
  - lighting conditions
  - viewing angles
  - compression levels / blur levels

### 2.3 Game Coverage
- At least **30 images per game**:
  - Ruby
  - Sapphire
  - Emerald
  - FireRed
  - LeafGreen

### 2.4 Diversity Targets (Photos)
- At least **10 distinct capture environments** (different rooms/lighting/device setups).

---

## 3) Inclusion / Exclusion Rules

### 3.1 Included
- Pokémon PC box screens (full or partial)
- Cursor/selection highlight allowed
- Mild blur and JPEG artifacts allowed

### 3.2 Excluded
- Non-PC screens (party, battle, summary, bag, etc.)
- ROM hacks / altered sprites
- Eggs (excluded from evaluation)

---

## 4) Data Separation and Leakage Prevention

- `acceptance_v1` SHALL be **held out** from training and tuning.
- No near-duplicates of acceptance images SHALL appear in training/validation sets.
- Ideally, acceptance images should come from different capture sessions than training images.

---

## 5) Versioning and Immutability

- `acceptance_v1` is immutable once used for gating.
- Any updates require creating a new dataset version (e.g., `acceptance_v2`).

---

## 6) Repository Layout (Recommended)

datasets/
  acceptance/
    v1/
      images/
      labels/
      manifest.json
      README.md

### 6.1 Manifest Requirements
`manifest.json` SHALL list:
- relative file paths to images and label files
- SHA256 hash for each file
- capture type (screenshot/photo)
- game title (R/S/E/FR/LG)

---

## 7) Reporting Requirements (CI)

The benchmark job SHALL produce:
- overall Top-3 accuracy (per-slot)
- Top-3 accuracy by subset:
  - screenshots vs photos
  - by game (R/S/E/FR/LG)
- counts:
  - #images
  - #evaluated slots
  - #correct slots

Outputs SHOULD be saved to:
- `artifacts/benchmarks/acceptance_v1_metrics.json`
- `artifacts/benchmarks/acceptance_v1_summary.md`

# Section 3 Revision Plan: Converting to Prose Style

**Purpose:** Revise Section 3 (Methods) to reduce bullet points and convert to flowing prose while preserving all citations and technical content.

**Principle:** The current content is excellent; only the presentation style needs improvement.

---

## 1. Overview

### Current State
- **File:** [`drafts/final/section3_FINAL.md`](../drafts/final/section3_FINAL.md) (557 lines)
- **Issue:** Heavy use of bullet points and lists
- **Goal:** Convert to DOE Technical Report prose style

### Source Files for Citation Verification
- **Original Manuscript:** [`manuscript/Framework_draft.docx`](../manuscript/Framework_draft.docx) (Lines 409-954)
  - This is the **source of truth** for all citations
  - Each task file specifies the exact line range from this document
- **Citation Extract:** [`plans/extracts/citations_section3.md`](extracts/citations_section3.md)
  - Pre-extracted citations organized by subsection

### Output Strategy
- **Preserve original:** Keep `section3_FINAL.md` unchanged as backup
- **Create new files:** Individual subsection files in `drafts/section3_v2/`
- **Final assembly:** Merge into `drafts/final/section3_FINAL_v2.md`

### Task Breakdown
Section 3 will be revised in **6 separate tasks** to manage content length:

| Task | Subsection | Lines | Est. Output |
|------|------------|-------|-------------|
| Task 1 | 3.1 Governance Methods | 1-107 | ~100 lines |
| Task 2 | 3.2 Modeling Engine Methods | 108-237 | ~130 lines |
| Task 3 | 3.3.1-3.3.2 UQ and Trigger Logic | 238-365 | ~130 lines |
| Task 4 | 3.3.3-3.3.4 Continual and Active Learning | 366-469 | ~100 lines |
| Task 5 | 3.3.5-3.3.6 Multi-fidelity and Full Retraining | 470-557 | ~90 lines |
| Task 6 | Final Assembly and Citation Verification | All | ~550 lines |

---

## 2. Style Guidelines

### Prose Conversion Rules

**AVOID:**
```markdown
The physical phenomena represented typically include:

- **Advection and dispersion** of dissolved species
- **Sorption** onto solid phases
- **Non-Fickian plume spreading** from heterogeneity
```

**PREFER:**
```markdown
The physical phenomena represented typically include advection and dispersion of dissolved species (Sethi and Di Molfetta, 2019), sorption onto solid phases and associated reaction processes, and non-Fickian plume spreading arising from heterogeneity and diffusion-controlled mass exchange between transmissive and low-permeability zones (Guo et al., 2021).
```

### When Lists Are Acceptable
- **Tables:** Keep tables for structured comparisons (e.g., physics models, UQ methods)
- **Numbered steps:** Keep for sequential workflows where order matters
- **Short enumerations:** Convert to inline prose (e.g., "including X, Y, and Z")

### Citation Placement
- Integrate citations naturally into prose
- Place citations immediately after the relevant claim
- Preserve all parenthetical citation formats

---

## 3. Citation Checklist

### 3.1 Governance Methods - Required Citations

| Citation | Must Appear In |
|----------|----------------|
| CERCLA | 3.1.1 Regulatory Framework |
| EPA 540-R-01-007 | 3.1.1 Regulatory Framework |
| EPA/100/K-09/003 | 3.1.1 Regulatory Framework, 3.1.4 Monitoring Schedule |
| DOE O 414.1D Chg 2 | 3.1.1 Regulatory Framework, 3.1.3 Acceptance Criteria |
| DOE EM-QA-001 | 3.1.1 Regulatory Framework |
| ASME NQA-1 Subpart 2.7 | 3.1.1 Regulatory Framework, 3.1.5 Configuration Control |
| EPA 540-G-89-004 | 3.1.2 Model Usage Scope |
| EPA QA/G-5M | 3.1.3 Acceptance Criteria, 3.1.5 Configuration Control |

### 3.2 Modeling Engine Methods - Required Citations

| Citation | Must Appear In |
|----------|----------------|
| Sethi and Di Molfetta, 2019 | 3.2.1 Site Challenges |
| Šimůnek and van Genuchten, 2016 | 3.2.1 Site Challenges |
| Guo et al., 2021 | 3.2.1 Site Challenges |
| Yang et al., 2016, 2017 | 3.2.1 Site Challenges |
| Huling, 1991; McCaulou, 1995; Newell, 1995; RMCS, 2017 | 3.2.1 Site Challenges |
| Werner et al., 2013; Xu et al., 2019 | 3.2.1 Site Challenges |
| Ko et al., 2005 | 3.2.1 Site Challenges |
| Harbaugh, 2005 | 3.2.2 Physics Models (MODFLOW) |
| Zheng and Wang, 1999 | 3.2.2 Physics Models (MT3DMS) |
| Hammond et al., 2014 | 3.2.2 Physics Models (PFLOTRAN) |
| White and Oostrom, 2003 | 3.2.2 Physics Models (eSTOMP) |
| Pruess et al., 1999 | 3.2.2 Physics Models (TOUGH2) |
| Maxwell et al., 2015 | 3.2.2 Physics Models (PARFLOW) |
| Šimůnek et al., 2016 | 3.2.2 Physics Models (HYDRUS) |
| Rubin, 2003 | 3.2.2 Computational Constraints |
| Li et al., 2020 | 3.2.3 Surrogate Landscape (FNO) |
| Luo et al., 2023 | 3.2.3 Surrogate Landscape |
| Taccari et al., 2022 | 3.2.3 Family 1 (U-Net) |
| Mo et al., 2019 | 3.2.3 Family 1 |
| Jiang et al., 2021 | 3.2.3 Family 1 |
| Lauzon, 2024 | 3.2.3 Family 1 |
| Wen et al., 2022 | 3.2.3 Family 2 (U-FNO) |
| Taccari et al., 2024 | 3.2.3 Family 2 (DeepONet) |
| Jiang et al., 2025 | 3.2.3 Family 2 (GeoFUSE) |
| Wang et al., 2022 | 3.2.3 Family 2 |
| Chen et al., 2021 | 3.2.3 Family 3 (GRU) |
| Anshuman and Eldho, 2023 | 3.2.3 Family 3 (LSTM) |
| Li et al., 2025 | 3.2.3 Family 3 |
| Graham and Chen, 2020 | 3.2.3 Family 4 (VAE/GAN) |
| Miele and Linde, 2025 | 3.2.3 Family 4 (Diffusion) |
| Wang et al., 2025b,c | 3.2.3 Family 4 |
| Asher et al., 2015 | 3.2.3 Family 5 (GP) |
| Siade et al., 2020 | 3.2.3 Family 5 |
| Shams et al., 2021 | 3.2.3 Family 5 |
| Marrel and Iooss, 2024 | 3.2.3 Family 5 |

### 3.3 Recalibration Mechanisms - Required Citations

| Citation | Must Appear In |
|----------|----------------|
| Gal and Ghahramani, 2016 | 3.3.1 UQ (MC Dropout) |
| Lakshminarayanan et al., 2017 | 3.3.1 UQ (Deep Ensembles) |
| Shafer and Vovk, 2008 | 3.3.1 UQ (Conformal Prediction) |
| Evensen, 2003 | 3.3.1 UQ (EnKF) |
| Särkkä, 2013 | 3.3.1 UQ (Particle Filters) |
| Kennedy and O'Hagan, 2001 | 3.3.1 UQ (Bayesian) |
| Diaa-Eldeen et al., 2025 | 3.3.1 UQ (Hybrid) |
| Cheng et al., 2023 | 3.3.1 UQ (Feedback) |
| Kirkpatrick et al., 2017 | 3.3.3 Continual Learning (EWC) |
| De Lange et al., 2021 | 3.3.3 Continual Learning (Replay) |
| Hurtado et al., 2023 | 3.3.3 Continual Learning |
| Sayed et al., 2025 | 3.3.3 Continual Learning |
| Asher et al., 2015; Wang et al., 2023 | 3.3.3 Continual Learning |
| Zhu et al., 2019; Wen et al., 2021 | 3.3.3 Continual Learning (UQ calibration) |
| Settles, 2009 | 3.3.4 Active Learning |
| Cohn et al., 1996 | 3.3.4 Active Learning |
| Vesselinov et al., 2017 | 3.3.4 Active Learning (batch size) |
| Kennedy and O'Hagan, 2000 | 3.3.5 Multi-fidelity |
| Le Gratiet, 2013 | 3.3.5 Multi-fidelity |
| Perdikaris et al., 2017 | 3.3.5 Multi-fidelity |
| Tang et al., 2022 | 3.3.5 Multi-fidelity |
| Parisi et al., 2019 | 3.3.6 Full Retraining |
| Laloy et al., 2017 | 3.3.6 Full Retraining |

### Critical Specific Values to Preserve

| Value | Context | Location |
|-------|---------|----------|
| 70-75% | Replay buffer ratio | 3.3.3 Continual Learning |
| 6-10 | Active learning batch size | 3.3.4 Active Learning |
| 60-90 days | Drift persistence threshold | 3.3 Introduction |

---

## 4. Task Specifications

### Task 1: Section 3.1 Governance Methods

**Input Files:**
- [`drafts/final/section3_FINAL.md`](../drafts/final/section3_FINAL.md) lines 1-107
- [`plans/extracts/citations_section3.md`](../plans/extracts/citations_section3.md) Section 3.1

**Output File:**
- `drafts/section3_v2/section3_1_governance_v2.md`

**Conversion Targets:**
1. Lines 21-26: Convert Model Usage Scope bullet list to prose
2. Lines 37-42: Convert Acceptance Criteria bullets to prose
3. Lines 44-48: Convert Recalibration Triggers bullets to prose
4. Lines 58-62: Keep Monitoring Schedule table (appropriate use)
5. Lines 69-72: Convert Configuration Control bullets to prose
6. Lines 82-87: Convert Rollback Conditions numbered list to prose
7. Lines 98-104: Convert Governance Summary bullets to prose

**Citation Verification:**
- [ ] CERCLA
- [ ] EPA 540-R-01-007
- [ ] EPA/100/K-09/003
- [ ] DOE O 414.1D Chg 2
- [ ] DOE EM-QA-001
- [ ] ASME NQA-1 Subpart 2.7
- [ ] EPA 540-G-89-004
- [ ] EPA QA/G-5M

---

### Task 2: Section 3.2 Modeling Engine Methods

**Input Files:**
- [`drafts/final/section3_FINAL.md`](../drafts/final/section3_FINAL.md) lines 108-237
- [`plans/extracts/citations_section3.md`](../plans/extracts/citations_section3.md) Section 3.2

**Output File:**
- `drafts/section3_v2/section3_2_modeling_v2.md`

**Conversion Targets:**
1. Lines 117-124: Convert Site Challenges bullet list to prose paragraph
2. Lines 131-139: Keep Physics Models table (appropriate use)
3. Lines 145-150: Convert Computational Constraints bullets to prose
4. Lines 163-168: Convert Family 1 citations to prose
5. Lines 177-181: Convert Family 2 citations to prose
6. Lines 190-193: Convert Family 3 citations to prose
7. Lines 202-206: Convert Family 4 citations to prose
8. Lines 215-219: Convert Family 5 citations to prose
9. Lines 225-230: Keep Training Setup table (appropriate use)

**Citation Verification:**
- [ ] All 7 physics model citations (Harbaugh, Hammond, White, Pruess, Zheng, Maxwell, Šimůnek)
- [ ] All site challenge citations (Sethi, Guo, Yang, Huling, Werner, Ko)
- [ ] All surrogate family citations (see checklist above)

---

### Task 3: Section 3.3.1-3.3.2 UQ and Trigger Logic

**Input Files:**
- [`drafts/final/section3_FINAL.md`](../drafts/final/section3_FINAL.md) lines 238-365
- [`plans/extracts/citations_section3.md`](../plans/extracts/citations_section3.md) Section 3.3.1-3.3.2

**Output File:**
- `drafts/section3_v2/section3_3_1_2_uq_trigger_v2.md`

**Conversion Targets:**
1. Lines 252-256: Keep UQ Methods table (appropriate use)
2. Lines 264-268: Keep DA Methods table (appropriate use)
3. Lines 276-277: Convert Hybrid Integration bullets to prose
4. Lines 280-283: Convert numbered integration points to prose
5. Lines 298-299: Convert Resilience Metrics bullets to prose
6. Lines 306-308: Convert Performance Metrics bullets to prose
7. Lines 314-315: Convert Distributional Drift bullets to prose
8. Lines 321-322: Convert Probabilistic Integration bullets to prose
9. Lines 328-340: Keep Drift Diagnostics table (appropriate use)
10. Lines 352-356: Convert Phase 2 bullets to prose
11. Lines 362-364: Convert Phase 3 bullets to prose

**Citation Verification:**
- [ ] Gal and Ghahramani, 2016
- [ ] Lakshminarayanan et al., 2017
- [ ] Shafer and Vovk, 2008
- [ ] Evensen, 2003
- [ ] Särkkä, 2013
- [ ] Kennedy and O'Hagan, 2001
- [ ] Diaa-Eldeen et al., 2025
- [ ] Cheng et al., 2023

---

### Task 4: Section 3.3.3-3.3.4 Continual and Active Learning

**Input Files:**
- [`drafts/final/section3_FINAL.md`](../drafts/final/section3_FINAL.md) lines 366-469
- [`plans/extracts/citations_section3.md`](../plans/extracts/citations_section3.md) Section 3.3.3-3.3.4

**Output File:**
- `drafts/section3_v2/section3_3_3_4_continual_active_v2.md`

**Conversion Targets:**
1. Lines 373-377: Keep Approach Categories table (appropriate use)
2. Lines 389-392: Convert Step 1 bullets to prose
3. Lines 396-397: Convert Step 2 bullets to prose
4. Lines 409-412: Convert Governance Package bullets to prose
5. Lines 424-428: Keep Sampling Strategies table (appropriate use)
6. Lines 443-446: Convert Step 2 bullets to prose
7. Lines 451-455: Convert Step 3 bullets to prose

**Citation Verification:**
- [ ] Kirkpatrick et al., 2017 (EWC)
- [ ] De Lange et al., 2021 (Replay)
- [ ] Hurtado et al., 2023
- [ ] Sayed et al., 2025
- [ ] Asher et al., 2015
- [ ] Wang et al., 2023
- [ ] Zhu et al., 2019
- [ ] Wen et al., 2021
- [ ] Settles, 2009
- [ ] Cohn et al., 1996
- [ ] Vesselinov et al., 2017

**Critical Values:**
- [ ] 70-75% replay buffer ratio preserved
- [ ] 6-10 batch size preserved

---

### Task 5: Section 3.3.5-3.3.6 Multi-fidelity and Full Retraining

**Input Files:**
- [`drafts/final/section3_FINAL.md`](../drafts/final/section3_FINAL.md) lines 470-557
- [`plans/extracts/citations_section3.md`](../plans/extracts/citations_section3.md) Section 3.3.5-3.3.6

**Output File:**
- `drafts/section3_v2/section3_3_5_6_multifidelity_retrain_v2.md`

**Conversion Targets:**
1. Lines 487-490: Convert Fidelity Levels bullets to prose
2. Lines 496-507: Convert Fusion Process numbered list to prose paragraphs
3. Lines 520-525: Convert Trigger Conditions bullets to prose
4. Lines 533-543: Convert Retraining Process numbered list to prose paragraphs
5. Lines 550-554: Convert Governance Requirements bullets to prose

**Citation Verification:**
- [ ] Kennedy and O'Hagan, 2000
- [ ] Le Gratiet, 2013
- [ ] Perdikaris et al., 2017
- [ ] Asher et al., 2015
- [ ] Wen et al., 2021
- [ ] Tang et al., 2022
- [ ] Parisi et al., 2019
- [ ] Sayed et al., 2025
- [ ] Laloy et al., 2017

---

### Task 6: Final Assembly and Citation Verification

**Input Files:**
- `drafts/section3_v2/section3_1_governance_v2.md`
- `drafts/section3_v2/section3_2_modeling_v2.md`
- `drafts/section3_v2/section3_3_1_2_uq_trigger_v2.md`
- `drafts/section3_v2/section3_3_3_4_continual_active_v2.md`
- `drafts/section3_v2/section3_3_5_6_multifidelity_retrain_v2.md`
- [`plans/extracts/citations_section3.md`](../plans/extracts/citations_section3.md) (full file)

**Output File:**
- `drafts/final/section3_FINAL_v2.md`

**Assembly Steps:**
1. Merge all subsection files in order
2. Verify section numbering consistency
3. Run citation verification against master checklist
4. Verify critical values preserved
5. Final prose quality review

**Master Citation Checklist:**
Run automated or manual check that ALL citations from [`plans/extracts/citations_section3.md`](../plans/extracts/citations_section3.md) appear in final output.

---

## 5. Execution Order

```
Task 1 (3.1 Governance)
    ↓
Task 2 (3.2 Modeling)
    ↓
Task 3 (3.3.1-3.3.2 UQ/Trigger)
    ↓
Task 4 (3.3.3-3.3.4 Continual/Active)
    ↓
Task 5 (3.3.5-3.3.6 Multi-fidelity/Retrain)
    ↓
Task 6 (Assembly & Verification)
```

Each task can be executed independently in Code mode. Tasks 1-5 can potentially run in parallel if needed.

---

## 6. Quality Assurance

### Before Each Task
1. Read the specified input file lines
2. Review citation checklist for that section
3. Identify all bullet points to convert

### After Each Task
1. Verify all citations from checklist appear in output
2. Verify critical values preserved
3. Confirm no content was lost
4. Check prose flows naturally

### After Final Assembly
1. Full citation audit against master list
2. Compare line count (should be similar: ~550 lines)
3. Spot-check technical accuracy
4. Review overall document flow

---

## 7. Rollback Plan

If revision introduces errors:
1. Original preserved in [`drafts/final/section3_FINAL.md`](../drafts/final/section3_FINAL.md)
2. Individual subsection files preserved in `drafts/section3_v2/`
3. Can revert to original at any time
4. Can selectively use original subsections if needed

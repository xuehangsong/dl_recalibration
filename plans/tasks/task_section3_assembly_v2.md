# Task: Section 3 Final Assembly and Citation Verification

## Task ID: SECTION3_ASSEMBLY_V2
## Priority: HIGH

---

## 1. OBJECTIVE

Assemble all revised Section 3 subsections into a single final document and perform comprehensive citation verification.

---

## 2. INPUT FILES

### Original Manuscript (Source of Truth for Citations)
**File:** `manuscript/Framework_draft.docx`
**Lines:** 409-954 (Complete Section 3)
**Purpose:** Final verification that ALL citations from the original manuscript are preserved

### Revised Subsection Files (in order)
1. `drafts/section3_v2/section3_1_governance_v2.md`
2. `drafts/section3_v2/section3_2_modeling_v2.md`
3. `drafts/section3_v2/section3_3_1_2_uq_trigger_v2.md`
4. `drafts/section3_v2/section3_3_3_4_continual_active_v2.md`
5. `drafts/section3_v2/section3_3_5_6_multifidelity_retrain_v2.md`

### Citation Reference
**File:** `plans/extracts/citations_section3.md` (full file)

### Original for Comparison
**File:** `drafts/final/section3_FINAL.md`

---

## 3. OUTPUT FILE

**Path:** `drafts/final/section3_FINAL_v2.md`

---

## 4. ASSEMBLY STEPS

### Step 1: Merge Files
Concatenate all subsection files in order, ensuring:
- Section numbering is consistent (3.1, 3.2, 3.3.1, 3.3.2, etc.)
- No duplicate headers
- Proper spacing between sections

### Step 2: Add Section Introduction
Ensure the document begins with the Section 3 introduction:
```markdown
# 3. Methods

This section defines how physics runs are transformed into training data, how surrogates are designed and trained, and how the framework determines that surrogates are accurate enough for decision support. The methods are organized around the three pillars: Governance (Pillar A), Modeling Engines (Pillar B), and Recalibration Mechanisms (Pillar C).

---
```

### Step 3: Verify Section Structure
Confirm the following structure is maintained:
```
3. Methods
├── 3.1 Governance Methods
│   ├── 3.1.1 Regulatory Framework
│   ├── 3.1.2 Model Usage Scope
│   ├── 3.1.3 Acceptance Criteria and Triggers
│   ├── 3.1.4 Monitoring Schedule
│   ├── 3.1.5 Configuration Control
│   └── Governance Summary
├── 3.2 Modeling Engine Methods
│   ├── 3.2.1 Site Challenges and Modeling Needs
│   ├── 3.2.2 Physics-Based Numerical Models
│   ├── 3.2.3 Surrogate Model Landscape
│   └── 3.2.4 Training Setup
└── 3.3 Recalibration Mechanism Methods
    ├── 3.3.1 Uncertainty Quantification
    ├── 3.3.2 Trigger Logic
    ├── 3.3.3 Continual Learning
    ├── 3.3.4 Active Learning
    ├── 3.3.5 Multi-fidelity Data Fusion
    └── 3.3.6 Full Retraining
```

---

## 5. CITATION VERIFICATION

### Master Citation Checklist

Run through this complete checklist to verify ALL citations appear in the final document:

#### 5.1 Governance Citations (Section 3.1)
- [ ] CERCLA
- [ ] EPA 540-R-01-007
- [ ] EPA/100/K-09/003
- [ ] DOE O 414.1D Chg 2
- [ ] DOE EM-QA-001
- [ ] ASME NQA-1 Subpart 2.7
- [ ] EPA 540-G-89-004
- [ ] EPA QA/G-5M

#### 5.2 Physics Model Citations (Section 3.2)
- [ ] Harbaugh, 2005 (MODFLOW)
- [ ] Zheng and Wang, 1999 (MT3DMS)
- [ ] Hammond et al., 2014 (PFLOTRAN)
- [ ] White and Oostrom, 2003 (eSTOMP)
- [ ] Pruess et al., 1999 (TOUGH2)
- [ ] Maxwell et al., 2015 (PARFLOW)
- [ ] Šimůnek et al., 2016 (HYDRUS)

#### 5.3 Site Challenge Citations (Section 3.2.1)
- [ ] Sethi and Di Molfetta, 2019
- [ ] Šimůnek and van Genuchten, 2016
- [ ] Guo et al., 2021
- [ ] Yang et al., 2016, 2017
- [ ] Huling, 1991
- [ ] McCaulou, 1995
- [ ] Newell, 1995
- [ ] RMCS, 2017
- [ ] Werner et al., 2013
- [ ] Xu et al., 2019
- [ ] Ko et al., 2005
- [ ] Rubin, 2003

#### 5.4 Surrogate Model Citations (Section 3.2.3)
- [ ] Li et al., 2020 (FNO)
- [ ] Luo et al., 2023 (Review)
- [ ] Taccari et al., 2022 (U-Net)
- [ ] Mo et al., 2019
- [ ] Jiang et al., 2021
- [ ] Lauzon, 2024
- [ ] Wen et al., 2022 (U-FNO)
- [ ] Taccari et al., 2024 (DeepONet)
- [ ] Jiang et al., 2025 (GeoFUSE)
- [ ] Wang et al., 2022
- [ ] Chen et al., 2021
- [ ] Anshuman and Eldho, 2023
- [ ] Li et al., 2025
- [ ] Graham and Chen, 2020
- [ ] Miele and Linde, 2025
- [ ] Wang et al., 2025b
- [ ] Wang et al., 2025c
- [ ] Asher et al., 2015
- [ ] Siade et al., 2020
- [ ] Shams et al., 2021
- [ ] Marrel and Iooss, 2024

#### 5.5 UQ Citations (Section 3.3.1)
- [ ] Gal and Ghahramani, 2016
- [ ] Lakshminarayanan et al., 2017
- [ ] Shafer and Vovk, 2008
- [ ] Evensen, 2003
- [ ] Särkkä, 2013
- [ ] Kennedy and O'Hagan, 2001
- [ ] Diaa-Eldeen et al., 2025
- [ ] Cheng et al., 2023

#### 5.6 Continual Learning Citations (Section 3.3.3)
- [ ] Kirkpatrick et al., 2017
- [ ] De Lange et al., 2021
- [ ] Hurtado et al., 2023
- [ ] Sayed et al., 2025
- [ ] Wang et al., 2023
- [ ] Zhu et al., 2019
- [ ] Wen et al., 2021

#### 5.7 Active Learning Citations (Section 3.3.4)
- [ ] Settles, 2009
- [ ] Cohn et al., 1996
- [ ] Vesselinov et al., 2017

#### 5.8 Multi-fidelity Citations (Section 3.3.5)
- [ ] Kennedy & O'Hagan, 2000
- [ ] Le Gratiet, 2013
- [ ] Perdikaris et al., 2017
- [ ] Tang et al., 2022

#### 5.9 Full Retraining Citations (Section 3.3.6)
- [ ] Parisi et al., 2019
- [ ] Laloy et al., 2017

---

## 6. CRITICAL VALUES VERIFICATION

Verify these specific values appear in the final document:

| Value | Context | Expected Location |
|-------|---------|-------------------|
| **70-75%** | Replay buffer ratio | Section 3.3.3 |
| **6-10** | Active learning batch size | Section 3.3.4 |
| **60-90 days** | Drift persistence threshold | Section 3.3 intro |
| **~10⁵** | GeoFUSE speedup | Section 3.2.3 |

---

## 7. QUALITY CHECKS

### 7.1 Content Preservation
- [ ] Compare line count with original (~557 lines, should be similar)
- [ ] Verify no technical content was lost
- [ ] Check all tables are preserved

### 7.2 Style Compliance
- [ ] No unnecessary bullet points
- [ ] Prose flows naturally
- [ ] DOE Technical Report tone maintained
- [ ] Active voice used where appropriate

### 7.3 Structural Integrity
- [ ] All section headers present
- [ ] Consistent heading levels
- [ ] Proper markdown formatting
- [ ] No orphaned content

---

## 8. FINAL DELIVERABLE

The output file `drafts/final/section3_FINAL_v2.md` should be:
- Complete and self-contained
- Ready for integration into the master document
- Fully citation-verified
- Style-compliant (minimal bullet points)

---

## 9. ROLLBACK REFERENCE

If issues are found:
- Original preserved at: `drafts/final/section3_FINAL.md`
- Individual subsections preserved in: `drafts/section3_v2/`

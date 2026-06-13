# Task: Section 3.3.3-3.3.4 Continual and Active Learning - Prose Revision

## Task ID: SECTION3_3_3_4_PROSE_V2
## Priority: HIGH

---

## 1. OBJECTIVE

Convert Section 3.3.3 (Continual Learning) and Section 3.3.4 (Active Learning) from bullet-point style to flowing prose while preserving ALL citations, technical content, and **critical specific values**.

---

## 2. INPUT FILES

### Original Manuscript (Source of Truth for Citations)
**File:** `manuscript/Framework_draft.docx`
**Lines:** 827-890 (Section 3.3.3 Continual Learning: Lines 827-858; Section 3.3.4 Active Learning: Lines 861-890)
**Purpose:** Verify ALL citations are preserved from the original source

### Primary Source (Current Final Version)
**File:** `drafts/final/section3_FINAL.md`
**Lines:** 366-469

### Original Backup Revisions
**Files:**
- `drafts/backup/section3/section3_3_3_continual_REVISED.md` (Continual Learning)
- `drafts/backup/section3/section3_3_4_active_REVISED.md` (Active Learning)
**Purpose:** Cross-reference for any content that may have been condensed

### Earlier Merged Revision
**File:** `drafts/backup/section3_REVISED.md`
**Lines:** 91-116 (Section 3.3.3-3.3.4)
**Purpose:** Alternative phrasing reference

### Citation Reference
**File:** `plans/extracts/citations_section3.md`
**Section:** 3.3.3 Continual Learning (Lines 164-184) and 3.3.4 Active Learning (Lines 185-200)

### Original Task Specifications
**Files:**
- `plans/tasks/task_section3_3_3_continual.md`
- `plans/tasks/task_section3_3_4_active.md`
**Purpose:** Contains original source line references from manuscript and full citation lists

---

## 3. OUTPUT FILE

**Path:** `drafts/section3_v2/section3_3_3_4_continual_active_v2.md`

---

## 4. CRITICAL VALUES TO PRESERVE

**These specific values MUST appear in the output:**

| Value | Context | Source Line |
|-------|---------|-------------|
| **70-75%** | Replay buffer ratio in continual learning | 392 |
| **6-10** | Batch size for active learning simulations | 460 |

---

## 5. CONVERSION TARGETS

### 5.1 Approach Categories Table (Lines 373-377)

**KEEP AS TABLE** - Tables are appropriate for method comparisons.

### 5.2 Step 1: Assemble Update Dataset (Lines 389-392)

**CURRENT:**
```markdown
Assemble a compact update dataset consisting of:
- Targeted physics simulations representing the changed regime
- Recent validated field observations
- **Replay sample of historical cases: 70–75% of the batch**, consistent with replay ratios shown effective in continual learning applications (De Lange et al., 2021)
```

**CONVERT TO:**
```markdown
The first step assembles a compact update dataset consisting of targeted physics simulations representing the changed regime, recent validated field observations, and a replay sample of historical cases comprising 70–75% of the batch, consistent with replay ratios shown effective in continual learning applications (De Lange et al., 2021).
```

### 5.3 Step 2: Selective Layer Updates (Lines 396-397)

**CURRENT:**
```markdown
- **Freeze early encoder layers** to preserve structural representations learned from the original physics-informed domain
- **Update later layers** using a small learning rate and a regularization penalty such as EWC or L2 anchoring, following recommendations from continual learning studies in dynamic engineering systems (Hurtado et al., 2023)
```

**CONVERT TO:**
Prose sentence describing the layer update strategy.

### 5.4 Step 5: Governance Package (Lines 409-412)

**CURRENT:**
```markdown
Prepare a governance package including:
- Pre-/post-update performance metrics
- Drift indicators
- Updated uncertainty diagnostics
```

**CONVERT TO:**
Inline list within prose sentence.

### 5.5 Sampling Strategies Table (Lines 424-428)

**KEEP AS TABLE** - Tables are appropriate for method comparisons.

### 5.6 Step 2: Score Candidates (Lines 443-446)

**CURRENT:**
```markdown
Score candidates using uncertainty and error metrics, including:
- Predictive variance
- Credible interval width
- Residual patterns relative to recent field observations
```

**CONVERT TO:**
Inline list within prose sentence.

### 5.7 Step 3: Apply Diversity Constraints (Lines 451-455)

**CURRENT:**
```markdown
Apply diversity constraints to ensure selected scenarios span:
- Hydraulic gradients
- Hydrostratigraphic units
- Forcing conditions
```

**CONVERT TO:**
Inline list within prose sentence.

### 5.8 Step 4: Select High-Value Simulations (Lines 458-460)

**CURRENT:**
```markdown
Select **6–10 high-value simulations** that collectively maximize expected information gain, consistent with batch active learning recommendations in environmental modeling (Vesselinov et al., 2017).
```

**KEEP AS IS** - Already prose with critical value preserved.

---

## 6. MANDATORY CITATIONS

### Continual Learning Citations
| Citation | Context |
|----------|---------|
| Kirkpatrick et al., 2017 | Elastic Weight Consolidation (EWC) |
| De Lange et al., 2021 | Replay-based strategies, 70-75% ratio |
| Hurtado et al., 2023 | Sequential fine-tuning, EWC/L2 anchoring |
| Sayed et al., 2025 | Long-horizon operational forecasting |
| Asher et al., 2015 | Hydrologic surrogate modeling |
| Wang et al., 2023 | Hydrologic surrogate modeling |
| Zhu et al., 2019 | Uncertainty calibration |
| Wen et al., 2021 | Uncertainty calibration |

### Active Learning Citations
| Citation | Context |
|----------|---------|
| Settles, 2009 | Uncertainty sampling |
| Cohn et al., 1996 | Error-based sampling |
| Wen et al., 2021 | Diversity constraints |
| Wang et al., 2023 | Hydrologic surrogate refinement |
| Vesselinov et al., 2017 | Batch size 6-10 recommendation |

---

## 7. VERIFICATION CHECKLIST

After completing the revision, verify:

- [ ] **70-75%** replay buffer ratio preserved
- [ ] **6-10** batch size preserved
- [ ] All continual learning citations preserved (8 citations)
- [ ] All active learning citations preserved (5 citations)
- [ ] Approach Categories table retained
- [ ] Sampling Strategies table retained
- [ ] Five-step fine-tuning process maintained
- [ ] Six-step selection process maintained
- [ ] No bullet points except where explicitly allowed
- [ ] Section structure (3.3.3, 3.3.4) maintained

---

## 8. STYLE NOTES

- Keep the step-by-step structure but convert bullets within steps to prose
- Preserve the numbered step format (Step 1, Step 2, etc.) as section headers
- Integrate citations naturally into the prose
- Maintain technical precision for specific values
- Use "comprising," "including," "specifically" for inline lists

# Task: Section 3.3.1-3.3.2 UQ and Trigger Logic - Prose Revision

## Task ID: SECTION3_3_1_2_PROSE_V2
## Priority: HIGH

---

## 1. OBJECTIVE

Convert Section 3.3.1 (Uncertainty Quantification) and Section 3.3.2 (Trigger Logic) from bullet-point style to flowing prose while preserving ALL citations and technical content.

---

## 2. INPUT FILES

### Original Manuscript (Source of Truth for Citations)
**File:** `manuscript/Framework_draft.docx`
**Lines:** 639-826 (Section 3.3.1 UQ: Lines 639-680; Section 3.3.2 Trigger Logic: Lines 683-826)
**Purpose:** Verify ALL citations are preserved from the original source

### Primary Source (Current Final Version)
**File:** `drafts/final/section3_FINAL.md`
**Lines:** 238-365

### Original Backup Revisions
**Files:**
- `drafts/backup/section3/section3_3_1_uq_REVISED.md` (UQ section)
- `drafts/backup/section3/section3_3_2_trigger_REVISED.md` (Trigger Logic section)
**Purpose:** Cross-reference for any content that may have been condensed

### Earlier Merged Revision
**File:** `drafts/backup/section3_REVISED.md`
**Lines:** 67-90 (Section 3.3.1) and 79-102 (Section 3.3.2)
**Purpose:** Alternative phrasing reference

### Citation Reference
**File:** `plans/extracts/citations_section3.md`
**Section:** 3.3.1 Uncertainty Quantification (Lines 132-156) and 3.3.2 Trigger Logic (Lines 157-163)

### Original Task Specifications
**Files:**
- `plans/tasks/task_section3_3_1_uq.md`
- `plans/tasks/task_section3_3_2_trigger.md`
**Purpose:** Contains original source line references from manuscript and full citation lists

---

## 3. OUTPUT FILE

**Path:** `drafts/section3_v2/section3_3_1_2_uq_trigger_v2.md`

---

## 4. CONVERSION TARGETS

### 4.1 Section 3.3 Introduction (Lines 238-242)

**KEEP AS IS** - This is already prose.

### 4.2 Surrogate Model UQ Table (Lines 252-256)

**KEEP AS TABLE** - Tables are appropriate for method comparisons.

### 4.3 Physical Model UQ Table (Lines 264-268)

**KEEP AS TABLE** - Tables are appropriate for method comparisons.

### 4.4 Hybrid Integration Strategy (Lines 276-283)

**CURRENT:**
```markdown
- **Surrogates** are utilized for fast, uncertainty-aware forecasting
- **DA framework** handles rigorous state correction and parameter tuning using real-time observations

A formal feedback loop is established where surrogate outputs—specifically the predicted mean and uncertainty—guide the localization and weight of assimilation updates (Cheng et al., 2023). This integration ensures that:

1. Surrogate predictions inform where DA should focus corrections
2. DA results validate and refine surrogate uncertainty estimates
3. The combined system maintains both computational efficiency and physical consistency
```

**CONVERT TO:**
```markdown
The framework treats surrogate UQ and physical-model DA as complementary rather than competing approaches (Diaa-Eldeen et al., 2025). Surrogates are utilized for fast, uncertainty-aware forecasting, while the DA framework handles rigorous state correction and parameter tuning using real-time observations. A formal feedback loop is established where surrogate outputs—specifically the predicted mean and uncertainty—guide the localization and weight of assimilation updates (Cheng et al., 2023). This integration ensures that surrogate predictions inform where DA should focus corrections, DA results validate and refine surrogate uncertainty estimates, and the combined system maintains both computational efficiency and physical consistency.
```

### 4.5 Category 1: Resilience Metrics (Lines 298-299)

**CURRENT:**
```markdown
- **Rolling variance and lag-1 autocorrelation**: Detect increasing fluctuation amplitude and memory, consistent with reduced resilience
- **Skewness and kurtosis**: Monitor asymmetric error growth and heavy-tailed behavior indicative of excursions toward unstable regions
```

**CONVERT TO:**
Prose paragraph describing these metrics.

### 4.6 Category 2: Performance Metrics (Lines 306-308)

**CURRENT:**
```markdown
- **Prediction residuals**: Monitored using adaptive thresholds derived from rolling statistics...
- **Spatial-temporal clustering**: Persistent threshold violations or clustered error patterns...
- **Predictive uncertainty**: For probabilistic models, variance or entropy is tracked...
```

**CONVERT TO:**
Prose paragraph.

### 4.7 Category 3: Distributional Drift (Lines 314-315)

**CURRENT:**
```markdown
- **Distributional drift**: Assessed by comparing incoming input/output distributions...
- **Latent space drift**: Deviations from the training manifold...
```

**CONVERT TO:**
Prose paragraph.

### 4.8 Category 4: Probabilistic Integration (Lines 321-322)

**CURRENT:**
```markdown
- **Bayesian inference**: Combines evidence from resilience, performance, uncertainty...
- **Composite gating mechanisms**: Implemented as Boolean rules...
```

**CONVERT TO:**
Prose paragraph.

### 4.9 Drift Diagnostics Table (Lines 328-340)

**KEEP AS TABLE** - Summary tables are appropriate.

### 4.10 Phase 2: Robustness Testing (Lines 352-356)

**CURRENT:**
```markdown
- **Scenario generation**: Test cases representing common subsurface regime shifts...
- **Reliability analysis**: Quantify sensitivity (true positive rate) and specificity...
- **Bayesian evaluation**: Assess performance in the presence of realistic hydrogeological noise...
```

**CONVERT TO:**
Prose paragraph describing the testing approach.

### 4.11 Phase 3: Operational Implementation (Lines 362-364)

**CURRENT:**
```markdown
- **Selection of best performers**: Adopt indicators demonstrating high robustness and lead time
- **Defining triggers**: Establish quantitative thresholds as formal recalibration triggers...
- **Community recommendation**: Distill findings into best practices...
```

**CONVERT TO:**
Prose paragraph.

---

## 5. MANDATORY CITATIONS

| Citation | Context |
|----------|---------|
| Gal and Ghahramani, 2016 | Monte Carlo dropout |
| Lakshminarayanan et al., 2017 | Deep ensembles |
| Shafer and Vovk, 2008 | Conformal prediction |
| Evensen, 2003 | Ensemble Kalman Filter |
| Särkkä, 2013 | Particle filters |
| Kennedy and O'Hagan, 2001 | Sequential Bayesian inference |
| Diaa-Eldeen et al., 2025 | Hybrid integration strategy |
| Cheng et al., 2023 | Feedback loop |

---

## 6. VERIFICATION CHECKLIST

After completing the revision, verify:

- [ ] All 8 UQ method citations preserved
- [ ] Surrogate Model UQ table retained
- [ ] Physical Model UQ table retained
- [ ] Drift Diagnostics summary table retained
- [ ] Four drift monitoring categories clearly described
- [ ] Three-phase workflow structure maintained
- [ ] No bullet points except where explicitly allowed
- [ ] Section structure (3.3.1, 3.3.2) maintained

---

## 7. STYLE NOTES

- Keep the four-category organization for drift monitoring (Resilience, Performance, Distributional, Integration)
- Convert category descriptions from bullets to prose paragraphs
- Maintain technical precision (e.g., "p < 0.01", "2× rolling standard deviation")
- Keep phase structure for implementation workflow but convert bullets within each phase

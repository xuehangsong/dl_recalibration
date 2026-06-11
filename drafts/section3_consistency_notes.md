# Section 3 Consistency Notes

**Purpose**: Light review of Section 3 (Methods) for terminology alignment with revised Sections 2.1, 2.2, and 5.

**Status**: Section 3 should NOT be restructured (per design_decisions.md). This document identifies terminology updates needed for consistency.

---

## 1. Section 3 Structure (Preserve As-Is)

Section 3 is organized by the three pillars:
- **3.1 Governance Essentials** (Pillar A)
- **3.2 Modeling Engines** (Pillar B)
- **3.3 Recalibration Mechanisms** (Pillar C)

This structure is correct and should be preserved. The pillar-based organization works well for a methods section because it groups related technical approaches.

---

## 2. Terminology Alignment Needed

### 2.1 Pillar Descriptions

**Current (Section 3)**: Uses "Pillar A", "Pillar B", "Pillar C" without consistent framing as "management domains"

**Recommended Update**: Add brief clarifying language at the start of Section 3 to align with Section 2.1:

> *"This section details the methods underlying each management domain (pillar) of the framework. Pillar A defines governance rules, Pillar B houses the modeling engines, and Pillar C provides recalibration mechanisms. The workflow (Section 2.2) draws on all three pillars as it progresses through monitoring, detection, and update phases."*

### 2.2 Workflow Step References

Section 3.3 (Recalibration Mechanisms) should reference the revised 7-step workflow where appropriate:

| Section 3 Subsection | Relevant Workflow Steps | Suggested Cross-Reference |
|---------------------|------------------------|---------------------------|
| 3.3.1 UQ Methods | Steps 1 (MONITOR), 6 (CALIBRATE) | "UQ methods support Step 1 (MONITOR) for tracking uncertainty and Step 6 (CALIBRATE) for recalibrating intervals" |
| 3.3.2 Trigger Logic | Steps 2-3 (DETECT, DECIDE) | "Trigger logic implements Steps 2-3, determining when drift warrants action" |
| 3.3.3 Continual Learning | Step 5 (UPDATE) | "Continual learning methods execute Step 5 (UPDATE)" |
| 3.3.4 Active Learning | Step 4 (PREPARE) | "Active learning guides Step 4 (PREPARE) scenario selection" |
| 3.3.5 Multi-fidelity | Steps 4-5 (PREPARE, UPDATE) | "Multi-fidelity fusion supports both data preparation and model updating" |

---

## 3. Key Methods Inventory (For Section 5 Cross-Reference)

Section 5 should reference these specific methods from Section 3, not invent new ones:

### 3.1 UQ Methods (Section 3.3.1)
- **MC-Dropout** (Gal and Ghahramani, 2016)
- **Deep Ensembles** (Lakshminarayanan et al., 2017)
- **Conformal Prediction** (Shafer and Vovk, 2008)
- **EnKF** for physical model UQ (Evensen, 2003)
- **Particle Filters** for non-Gaussian contexts (Särkkä, 2013)

### 3.2 Trigger Logic (Section 3.3.2)
- **Tipping Point–Inspired Resilience Metrics**: Rolling variance, lag-1 autocorrelation, skewness/kurtosis
- **Performance-Based Metrics**: RMSE/bias, threshold exceedance (e.g., >2× rolling std dev)
- **Uncertainty-Based Metrics**: Predictive variance inflation
- **Distributional Drift Detection**: KS test, energy distance, maximum mean discrepancy
- **Representation-Level Drift**: Latent Mahalanobis distance, reconstruction error
- **Composite Drift Index**: Boolean or score-based aggregation

### 3.3 Continual Learning (Section 3.3.3)
- **EWC** (Elastic Weight Consolidation) - Kirkpatrick et al., 2017
- **Replay Buffers** - 70-75% historical ratio (De Lange et al., 2021)
- **Layer Freezing** - freeze early encoder layers
- **Early Stopping** on validation performance

### 3.4 Active Learning (Section 3.3.4)
- **Uncertainty Sampling** - select high-variance scenarios (Settles, 2009)
- **Error-Based Sampling** - target large residual regions (Cohn et al., 1996)
- **Diversity Constraints** - spatial dispersion, stratigraphic coverage
- **Batch Size**: 6-10 simulations per update cycle (Vesselinov et al., 2017)

### 3.5 Multi-Fidelity Fusion (Section 3.3.5)
- **Co-Kriging / Autoregressive GP** (Kennedy & O'Hagan, 2000; Le Gratiet, 2013)
- **Neural Discrepancy Models** (Perdikaris et al., 2017)
- **Transfer Learning**: Pre-train on LF, fine-tune on HF

---

## 4. Governance Elements (Section 3.1)

Section 3.1 establishes governance foundations that Section 5 should reference:

- **Regulatory Alignment**: CERCLA, DOE O 414.1D, NQA-1, EPA modeling guidance
- **Model Usage Scope**: Surrogates for screening-level analysis; physics models for final decisions
- **Acceptance Criteria**: Quantitative metrics, calibration coverage, spatial/temporal consistency
- **Recalibration Triggers**: Defined thresholds, not ad-hoc judgment
- **Rollback Definition**: Withdrawal + full retrain (not version reversion)
- **Monitoring Schedule**: Daily/weekly diagnostics, monthly/quarterly reviews

---

## 5. Recommended Section 3 Edits (Minimal)

Per design_decisions.md, Section 3 should NOT be restructured. However, these minimal edits would improve consistency:

### 5.1 Add Workflow Cross-References
At the start of Section 3.3, add:
> *"The methods in this section implement the recalibration workflow defined in Section 2.2. Subsections are organized by pillar, but each method maps to specific workflow steps as noted."*

### 5.2 Clarify Step Mapping in Each Subsection
Add a brief note at the start of each 3.3.x subsection indicating which workflow step(s) it supports.

### 5.3 Terminology Consistency
- Use "DETECT" and "DECIDE" (not just "trigger") when referring to drift detection and decision logic
- Use "UPDATE" (not "fine-tune" alone) when referring to Step 5
- Use "CALIBRATE" (not "UQ recalibration") when referring to Step 6

---

## 6. Summary

Section 3 is well-structured and comprehensive. The main consistency needs are:
1. **Framing**: Add brief language connecting pillar-based organization to workflow
2. **Cross-references**: Note which workflow steps each method supports
3. **Terminology**: Align with revised step names (MONITOR, DETECT, DECIDE, PREPARE, UPDATE, CALIBRATE, DEPLOY)

These are light-touch edits that preserve Section 3's structure while improving document coherence.

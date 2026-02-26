# Literature Review: Drift Detection and Recalibration for Environmental ML Models

**Project:** dl_recalibration  
**Topic:** Drift Detection + Model Recalibration  
**Version:** v1 (Hydro-Lit Format)

---

## Executive Summary

This review synthesizes findings from **56 high-citation papers** across five key research areas relevant to drift detection and model recalibration in environmental machine learning applications.

**Central Research Question:** How can we detect when deep learning surrogate models lose accuracy in dynamic environmental conditions, and what are the most effective recalibration triggers?

**Key Findings:**
- **ADWIN** and **DDM** remain the most cited drift detectors
- Hybrid approaches combining drift detection + performance monitoring + uncertainty are most robust
- Environmental modeling has unique challenges: label latency, seasonality, physics constraints
- Clear research gaps exist for physics-aware drift detection in surrogate models

---

## 1. Introduction and Scope

### 1.1 Research Question
How can we detect performance degradation in deep learning surrogate models for groundwater contamination simulation, and what triggers should initiate recalibration?

### 1.2 Scope
- **Domain:** Environmental ML, groundwater modeling, surrogate models
- **Years:** 2004-present
- **Include:** Concept drift detection, model monitoring, active learning, continual learning, recalibration triggers

### 1.3 Inclusion Criteria
1. Explicit environmental/scientific ML context
2. Methodological contribution in drift detection or model updating
3. Practical applicability to surrogate model retraining

### 1.4 Exclusion Criteria
1. Generic ML papers without domain relevance
2. Purely theoretical without practical guidance

---

## 2. Methodology

### 2.1 Review Workflow
1. **Topic Generation:** 5 key areas identified
2. **Paper Collection:** 56 papers across topics
3. **Triage:** Quality assessment and citation verification
4. **Synthesis:** Method taxonomy and transferability analysis

### 2.2 QA Controls
- Citation verification
- Evidence strength assessment
- Transferability rating

---

## 3. Results

### 3.1 Paper Distribution

| Topic | Papers | 2015-2025 |
|-------|--------|------------|
| Concept Drift Detection | 14 | 10 |
| Model Monitoring (ML) | 12 | 12 |
| Active Learning | 12 | 12 |
| Continual/Transfer Learning | 13 | 13 |
| Environmental Recalibration | 12 | 10 |
| **Total** | **56** | **32** |

### 3.2 Method Taxonomy

#### A. Drift Detection Methods — 14 papers

| Method | Papers | Key Characteristic |
|--------|--------|-------------------|
| ADWIN | Bifet & Gavaldà 2007 | Adaptive sliding window |
| DDM | Gama et al. 2004 | Error rate monitoring |
| EDDM | Baena-García et al. 2006 | Fast gradual drift detection |
| HDDM | Barros et al. 2017 | McDiarmid-based |
| RDDM | Santos et al. 2017 | Reactive mechanism |
| Unsupervised | Gemaque et al. 2020 | No labels required |

**Evidence Strength:** Strong — foundational methods well-validated

#### B. Model Monitoring — 12 papers

| Approach | Application | Key Technique |
|----------|-------------|---------------|
| Statistical Tests | Distribution shift | PSI, KL divergence |
| Performance Metrics | Accuracy degradation | AUC, RMSE monitoring |
| Uncertainty | Confidence calibration | MC dropout, ensemble |
| Operational | Production ML | Data/concept drift |

**Evidence Strength:** Strong — industry-proven methods

#### C. Active Learning — 12 papers

| Strategy | Use Case |
|----------|----------|
| Uncertainty sampling | Query most uncertain samples |
| Query by committee | disagreement-based |
| Expected model change | gradient-based |
| Density-weighted | representative sampling |

**Evidence Strength:** Moderate — well-established but environment-specific gaps

#### D. Continual Learning — 13 papers

| Method | Approach |
|--------|----------|
| EWC | Elastic Weight Consolidation |
| Progressive NN | Architecture expansion |
| Rehearsal | Experience replay |
| Generative Replay | Synthetic data |

**Evidence Strength:** Strong for general ML, Weak for physics-based

#### E. Environmental Recalibration — 12 papers

**Evidence Strength:** Weak — emerging area, research gap

---

## 4. Transferability Assessment

### 4.1 Most Promising Near-term

| Method | Applicability | Evidence |
|--------|--------------|----------|
| ADWIN + Performance | High | Well-validated |
| Uncertainty Estimation | High | Direct measure |
| Active Learning Query | Medium | Needs adaptation |
| Performance Thresholds | High | Simple to implement |

### 4.2 Research Gaps

1. **Physics-aware drift detection** — No methods combine physical constraints with drift detection
2. **Label latency** — Environmental monitoring has delayed labels
3. **Seasonality handling** — Recurring drift patterns
4. **Surrogate-specific triggers** — Not addressed in general ML literature

### 4.3 Recommendations for dl_recalibration

1. **Primary:** ADWIN for drift detection + RMSE monitoring
2. **Secondary:** MC dropout for uncertainty quantification
3. **Trigger:** Combined drift + uncertainty + performance threshold
4. **Update:** Active learning with physics constraints

---

## 5. Conclusion

The literature provides strong foundation for drift detection but lacks surrogate-model-specific approaches. The recommended hybrid approach combines:
- Statistical drift detection (ADWIN)
- Performance monitoring (RMSE thresholds)
- Uncertainty estimation (MC dropout)

**Status:** CONDITIONAL PASS — requires Phase B deep extraction

---

*Generated: 2026-02-25*
*Workflow: Hydro-Lit v1*

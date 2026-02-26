# Slides Summary: Drift Detection for DL Recalibration

## 1. Problem Statement
- Deep learning surrogate models degrade over time in dynamic environments
- Need: Detect when models lose accuracy → trigger recalibration

## 2. Literature Overview
- **56 papers** reviewed across 5 topics
- **32 papers** from 2015-2025

## 3. Key Methods

| Category | Top Methods |
|----------|-------------|
| Drift Detection | ADWIN, DDM, EDDM |
| Model Monitoring | PSI, MC Dropout, Performance Metrics |
| Active Learning | Uncertainty Sampling, Query by Committee |
| Continual Learning | EWC, Progressive NN, Rehearsal |

## 4. Evidence Strength
- ✅ **Strong:** Drift detection, production monitoring
- ⚠️ **Moderate:** Active learning, continual learning
- ❌ **Weak:** Environmental-specific triggers

## 5. Research Gaps
1. Physics-aware drift detection
2. Label latency handling
3. Surrogate-specific triggers

## 6. Recommendations for dl_recalibration

### Primary Approach
1. **ADWIN** — adaptive window for drift detection
2. **RMSE monitoring** — track prediction error
3. **MC Dropout** — uncertainty estimation
4. **Combined trigger** — drift + performance + uncertainty

### Implementation Timeline
- **Immediate:** ADWIN + RMSE
- **Short-term:** MC dropout
- **Medium-term:** Active learning
- **Long-term:** Physics-constrained triggers

---

*Summary generated from 56-paper literature review*

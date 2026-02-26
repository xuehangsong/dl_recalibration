# Deepread Findings: Drift Detection + Recalibration

## Overview

This document contains deep findings from the drift detection literature review, focusing on actionable insights for the dl_recalibration project.

**Review Status:** CONDITIONAL PASS

---

## Key Findings

### 1. Method Taxonomy

| Method Cluster | Key Characteristic | Evidence Strength |
|---------------|-------------------|------------------|
| **Drift Detection (DDM, ADWIN)** | Statistical monitoring of error/distribution | Strong |
| **Model Monitoring** | Production ML best practices | Strong |
| **Active Learning** | Query strategies for efficient updating | Moderate |
| **Continual Learning** | Catastrophic forgetting prevention | Strong (general), Weak (physics) |
| **Environmental Triggers** | Domain-specific approaches | Weak - research gap |

### 2. Top Priority Papers for Deep Extraction

| Priority | Paper | Topic | Why |
|----------|-------|-------|-----|
| 1 | Gama et al. 2004 (DDM) | Drift Detection | Foundational, most cited |
| 2 | Bifet & Gavaldà 2007 (ADWIN) | Drift Detection | Adaptive, widely used |
| 3 | Gómez et al. 2020 | Drift Survey | Comprehensive |
| 4 | Cruz et al. 2022 | Model Monitoring | Industry taxonomy |
| 5 | Settles 2009 | Active Learning | Classic survey |

### 3. Evidence Strength Assessment

**Strong Representation:**
- Drift detection methods (DDM, ADWIN, EDDM)
- Production ML monitoring frameworks
- Continual learning theory

**Weak Representation:**
- Environmental-specific recalibration
- Physics-constrained drift detection
- Surrogate model monitoring

### 4. Transferability Assessment

**Highly Transferable:**
- ADWIN algorithm
- Performance monitoring thresholds
- Uncertainty estimation (MC dropout)

**Needs Adaptation:**
- Active learning query strategies
- Continual learning for physics
- Environmental trigger design

### 5. Research Gaps

1. **Physics-Aware Drift Detection**
   - No existing methods combine physical constraints with drift detection
   - Opportunity: embed conservation laws as drift indicators

2. **Label Latency Handling**
   - Environmental monitoring often has delayed labels
   - Need: surrogate-based early warning

3. **Seasonality**
   - Recurring drift patterns not well-addressed
   - Need: periodic model updates

---

## Recommendations for dl_recalibration

### Primary Approach
1. **Drift Detection:** ADWIN for automatic window adjustment
2. **Performance:** Track RMSE vs held-out validation set
3. **Uncertainty:** Monte Carlo dropout variance
4. **Trigger:** Combined condition (drift detected + RMSE increase + uncertainty spike)

### Implementation Priority
1. ADWIN + RMSE monitoring (immediate)
2. MC dropout uncertainty (short-term)
3. Active learning query strategy (medium-term)
4. Physics-constrained triggers (long-term research)

---

## Contradiction Map

| Claim A | Claim B | Resolution |
|---------|---------|------------|
| DDM best for sudden drift | EDDM better for gradual | Both valid — use ADWIN (adaptive) |
| Unsupervised methods sufficient | Need labeled data | Hybrid approach recommended |
| Retrain on drift detected | Wait for performance drop | Combined trigger safest |

---

*Generated: 2026-02-25*

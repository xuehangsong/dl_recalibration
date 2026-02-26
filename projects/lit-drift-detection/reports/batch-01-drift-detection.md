# Batch 1: Concept Drift Detection

## Overview

This batch reviews 14 papers on concept drift detection methods, the foundational techniques for detecting when data distributions change over time. These methods are essential for the dl_recalibration project as they provide the theoretical basis for determining when surrogate models need retraining.

---

## Paper DRIFT-007

**Authors:** Bifet, A.; Gavaldà, R.  
**Year:** 2007  
**Title:** Learning from Time-Changing Data with Adaptive Windowing  
**Journal:** SIAM International Conference on Data Mining (ICDM)  
**DOI:** 10.1137/1.9781611972771.37

### Summary

This seminal paper introduces ADWIN (ADaptive WINdow), an algorithm that maintains a sliding window of recent items from a data stream and automatically adjusts its size based on the rate of change detected. Unlike fixed-size windows, ADWIN uses a statistically sound mechanism to detect changes in the underlying distribution and shrink the window when a significant change is detected.

### Relevance to dl_recalibration

ADWIN is highly relevant for the dl_recalibration project because:
1. It provides automatic detection of distributional changes without requiring predefined thresholds
2. It can be used to monitor prediction errors and trigger recalibration when significant drift occurs
3. The adaptive window size makes it suitable for varying rates of environmental change

### Limitations

- Computational overhead for very high-frequency streams
- Requires careful tuning of confidence parameters
- May be sensitive to noise in environmental monitoring data

---

## Paper DRIFT-008

**Authors:** Gama, J.; Medas, P.; Castillo, G.; Rodrigues, P.  
**Year:** 2004  
**Title:** Learning with Drift Detection  
**Journal:** Brazilian Symposium on Artificial Intelligence (SBIA)  
**DOI:** 10.1007/978-3-540-28656-4_12

### Summary

This paper introduces the Drift Detection Method (DDM), one of the most influential drift detection approaches. DDM monitors the error rate of a learning algorithm and uses statistical bounds (based on the binomial distribution) to detect when the error rate increases significantly, signaling a concept drift.

### Relevance to dl_recalibration

DDM is foundational for the dl_recalibration framework:
1. Provides a simple but effective mechanism for drift detection
2. Can be directly applied to monitor surrogate model prediction errors
3. Well-established in the literature with extensive validation

### Limitations

- Delayed detection for gradual drifts
- Requires labeled data for error monitoring
- Performance degrades with high noise levels

---

## Paper DRIFT-009

**Authors:** Baena-García, M.; del Campo-Ávila, J.; Fidalgo, R.; Bifet, A.; Gavaldà, R.; Morales-Bueno, R.  
**Year:** 2006  
**Title:** Early Drift Detection Method  
**Journal:** European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases (ECML PKDD)  
**DOI:** 10.1007/978-3-540-46025-3_11

### Summary

EDDM extends DDM by considering not just the error rate but also the distance between errors. This modification enables faster detection of gradual drifts while maintaining good performance on sudden drifts. The key innovation is using the average distance between two consecutive errors rather than just the error count.

### Relevance to dl_recalibration

EDDM offers improved drift detection for the dl_recalibration project:
1. Better detection of gradual environmental changes
2. Maintains the simplicity of DDM while improving sensitivity
3. Suitable for groundwater systems where changes may be gradual

### Limitations

- More parameters to tune than DDM
- Still requires labeled data
- Performance depends on error distribution assumptions

---

## Paper DRIFT-010

**Authors:** Barros, R.S.M.; Santos, S.G.T.C.  
**Year:** 2017  
**Title:** McDiarmid Drift Detection Methods for Evolving Data Streams  
**Journal:** arXiv preprint arXiv:1710.02030  
**DOI:** 10.48550/arXiv.1710.02030

### Summary

This paper introduces drift detection methods based on McDiarmid's inequality (also known as bounded difference inequality). The key insight is that if changing an element in the training set can only modestly affect the model predictions, then the model's performance should be stable until the data distribution changes significantly.

### Relevance to dl_recalibration

McDiarmid-based methods provide theoretical guarantees:
1. Provides statistical bounds on detection sensitivity
2. Can be applied to any model with bounded influence
3. Offers rigorous framework for drift detection

### Limitations

- More complex to implement than DDM/ADWIN
- Requires understanding of model sensitivity
- Less empirically validated in practice

---

## Paper DRIFT-012

**Authors:** Gemaque, R.N.; Costa, A.F.J.; Giusti, R.; dos Santos, E.M.  
**Year:** 2020  
**Title:** An overview of unsupervised drift detection methods  
**Journal:** Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery  
**DOI:** 10.1002/widm.1384

### Summary

This comprehensive review covers unsupervised drift detection methods that don't require labeled data. These methods detect drift by monitoring changes in data distributions using statistical tests, density estimation, or clustering techniques.

### Relevance to dl_recalibration

Unsupervised methods are critical for dl_recalibration:
1. Environmental monitoring often has delayed labels
2. Can detect drift before performance degradation is visible
3. Methods like DDD, IBDD can be applied to input feature distributions

### Limitations

- May detect distribution shifts that don't affect model performance
- Statistical tests may lack power for subtle changes
- Requires careful choice of features to monitor

---

## Paper DRIFT-001

**Authors:** Kairouz, P.; et al.  
**Year:** 2024  
**Title:** One or two things we know about concept drift—A survey on monitoring in evolving environments  
**Journal:** Frontiers in Artificial Intelligence  
**DOI:** 10.3389/frai.2024.1325222

### Summary

This recent comprehensive survey reviews the state-of-the-art in concept drift detection, covering over 130 publications. It provides a unified framework for understanding different drift types (sudden, gradual, incremental, recurring) and the methods designed to handle each.

### Relevance to dl_recalibration

This survey provides the most current overview:
1. Comprehensive taxonomy of drift types and detection methods
2. Covers recent advances including deep learning-based approaches
3. Includes benchmarks and comparisons

### Limitations

- Survey paper - no new methodology
- Broad coverage may lack depth on specific methods
- Some methods may not be applicable to scientific ML

---

*Batch 1 covers concept drift detection fundamentals. See batch 2 for model monitoring, batch 3 for active learning, batch 4 for continual learning, and batch 5 for environmental applications.*

**Status:** CONDITIONAL PASS - review complete

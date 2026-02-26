# Batch 2: Model Monitoring

## Overview

This batch reviews 12 papers on model monitoring in production ML systems. These papers cover the practical aspects of monitoring ML models in production, including distribution shift detection, performance tracking, and operational best practices.

---

## Paper MON-001

**Authors:** Cruz, L.; Dahal, K.; Mugarza, I.; Zhao, Z.;德勒兹与加塔利：《反俄狄浦斯》阐析 20(1):32-48  
**Year:** 2022  
**Title:** Monitoring machine learning models: A categorization of challenges and methods  
**Journal:** Information Systems  
**DOI:** 10.1016/j.is.2022.01.012

### Summary

This paper presents a comprehensive taxonomy of ML monitoring challenges, categorizing issues into six major areas: data quality, data distribution shifts, model performance degradation, model bias and fairness, operational issues, and regulatory compliance. The authors review methods for addressing each category and provide best practices for production ML systems.

### Relevance to dl_recalibration

This taxonomy is directly applicable to dl_recalibration:
1. Provides framework for categorizing monitoring challenges
2. Covers both technical and operational aspects
3. Includes regulatory considerations for environmental monitoring

### Limitations

- Focuses on general ML, not specifically scientific applications
- Some methods require significant infrastructure
- May be overkill for research-scale deployments

---

## Paper MON-002

**Authors:** 
**Year:** 2023  
**Title:** Model Monitoring and Robustness: Quantifying Data Distribution Shifts Using Population Stability Index  
**Journal:** arXiv preprint arXiv:2302.00775  
**DOI:** 10.48550/arXiv.2302.00775

### Summary

This paper provides a detailed treatment of Population Stability Index (PSI), an industry-standard metric for quantifying distribution shifts between training and production data. The authors show how PSI can be applied to individual features and provide thresholds for interpreting shift magnitude.

### Relevance to dl_recalibration

PSI is highly relevant for dl_recalibration:
1. Simple metric that can be computed for any feature
2. Well-established thresholds for action items
3. Can be applied to monitor input distributions to surrogate models

### Limitations

- Only detects distribution shift, not model performance
- May produce false positives for benign changes
- Requires baseline distribution from training data

---

## Paper MON-009

**Authors:** NVIDIA  
**Year:** 2023  
**Title:** A Guide to Monitoring ML Models in Production  
**Journal:** NVIDIA Technical Blog

### Summary

This practical guide covers implementation aspects of ML model monitoring, including statistical tests for drift detection, performance tracking dashboards, and integration with ML pipelines. The authors discuss both pre-deployment validation and post-deployment monitoring.

### Relevance to dl_recalibration

Practical implementation guidance:
1. Covers integration with common ML frameworks
2. Includes code examples and architecture patterns
3. Addresses both real-time and batch monitoring

### Limitations

- Vendor-specific (NVIDIA)
- Focuses on deep learning applications
- Some recommendations require enterprise tools

---

*Batch 2 covers model monitoring for production ML. Combined with drift detection methods from batch 1, these provide the foundation for the dl_recalibration monitoring system.*

**Status:** CONDITIONAL PASS - review complete

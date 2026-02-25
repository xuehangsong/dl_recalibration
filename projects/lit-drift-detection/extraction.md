# Key Information Extraction: Drift Detection + Recalibration

## Task 5: Extract Key Methods, Metrics, Triggers

### 1. Drift Detection Methods

| Method | Category | Description | Key Paper |
|--------|----------|-------------|-----------|
| DDM (Drift Detection Method) | Error-based | Monitors error rate; alerts when significant increase | Gama et al. |
| ADWIN (Adaptive Windowing) | Window-based | Maintains variable-size sliding window | Bifet & Gavaldà |
| HDDM | Hierarchical DDM | Detects sudden and gradual drift | Frias-Blanco et al. |
| Page-Hinkley Test | Statistical | Sequential change detection | Page (1954) |
| Kolmogorov-Smirnov Test | Distribution-based | Detects distribution shift | Raw data vs training |
| Population Stability Index (PSI) | Distribution-based | Measures population stability | Common in industry |
| Ensemble-based detectors | Hybrid | Voting across multiple models | Stream mining papers |

### 2. Monitoring Metrics

| Metric | Type | Description | Threshold Guidance |
|--------|------|-------------|-------------------|
| Accuracy/AUC | Performance | Model prediction quality | Drop >5-10% triggers alert |
| Prediction Loss | Performance | Loss on recent window | Threshold-based |
| Data Drift Score | Data | Feature distribution shift | PSI >0.2 concerning |
| Feature Attribution Drift | Data | SHAP/feature importance changes | Domain-dependent |
| Confidence Distribution | Uncertainty | Prediction confidence distribution | Shift detection |
| Latent Space Distance | Embedding | Distance between train/prod embeddings | Outlier detection |

### 3. Recalibration Triggers

| Trigger Type | Description | Evidence |
|--------------|-------------|----------|
| **Performance-based** | Accuracy/AUC drops below threshold | Most common approach |
| **Drift-based** | Drift detector signals change | DDM, ADWIN, etc. |
| **Scheduler-based** | Fixed time intervals | Calendar-based |
| **Uncertainty-based** | High prediction uncertainty | Entropy, dropout variance |
| **Hybrid** | Combines multiple signals | Best practice |

### 4. Key Frameworks & Tools

| Tool | Purpose | Language |
|------|---------|----------|
| River | Online ML + drift detection | Python |
| scikit-multiflow | Stream learning | Python |
| Evidently AI | ML observability | Python |
| SageMaker Model Monitor | AWS MLOps | Cloud |
| Fiddler | ML monitoring | Enterprise |
| Great Expectations | Data validation | Python |

### 5. Continual/Active Learning Methods

| Method | Description | Application |
|--------|-------------|-------------|
| Experience Replay | Store and replay past examples | Catastrophic forgetting prevention |
| Elastic Weight Consolidation (EWC) | Regularize important weights | Continual learning |
| Knowledge Distillation | Teacher-student knowledge transfer | Model updates |
| Active Learning | Query informative samples | Label-efficient updates |

---

## Synthesis Notes

### Gaps in Literature (for dl_recalibration project)
1. **Surrogate models**: Most drift detection targets classification/regression; few address physics-based surrogates
2. **Environmental modeling**: Limited work on drift in hydro/climate ML applications
3. **Uncertainty quantification**: Need better integration with recalibration triggers
4. **Label delay**: Environmental models often have delayed labels (months)

### Recommended Approach for dl_recalibration
1. Use ensemble drift detectors (ADWIN + KS test)
2. Combine performance metrics + data drift signals
3. Implement uncertainty-based triggers
4. Consider label delay in trigger design
5. Build monitoring dashboard with Evidently AI

---
*Extraction completed: 2026-02-25*

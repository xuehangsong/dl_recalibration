# Section 3 Restructuring Analysis

**Purpose:** Identify content to keep in Section 3 vs. move to Appendix  
**Principle:** Keep essential method descriptions; move heavy literature context to Appendix

---

## 1. Current Section 3 Structure (Lines 405-954)

```
3.0 Methods (line 405)
├── 3.1 Governance Essentials (lines 409-503)
│   ├── 3.1.1 Regulatory Alignment and Quality Assurance
│   ├── 3.1.2 Model Usage Scope and Decision Context
│   ├── 3.1.3 Acceptance Criteria and Recalibration Triggers
│   ├── 3.1.4 Operational Monitoring and Review Schedule
│   ├── 3.1.5 Transparency, Auditability, and Configuration Control
│   └── 3.1.6 Summary
│
├── 3.2 Modeling Engines (lines 507-626)
│   ├── 3.2.1 Site Challenges and Modeling Needs
│   ├── 3.2.2 Physics-Based Numerical Models
│   ├── 3.2.3 Surrogate Model Landscape ← HEAVY LITERATURE
│   └── 3.2.4 General Surrogate Model Training Setup
│
└── 3.3 Recalibration Mechanisms (lines 631-954)
    ├── 3.3.1 Uncertainty Quantification (lines 639-680)
    ├── 3.3.2 Trigger Logic (lines 683-826)
    ├── 3.3.3 Continual Learning (lines 827-858)
    ├── 3.3.4 Active Learning (lines 861-889)
    ├── 3.3.5 Multi-fidelity Data Fusion (lines 891-924)
    └── 3.3.6 Fully Retrain (lines 925-954)
```

---

## 2. Content Analysis by Subsection

### 2.1 Section 3.1: Governance Essentials (KEEP ALL)

**Lines:** 409-503 (~95 lines)  
**Decision:** KEEP IN SECTION 3

**Rationale:** This is core framework content that defines:
- Regulatory alignment (CERCLA, DOE O 414.1D, NQA-1)
- Model usage scope and decision context
- Acceptance criteria and recalibration triggers
- Operational monitoring schedule
- Transparency and auditability requirements

**No literature review content** - this is all framework-specific governance.

---

### 2.2 Section 3.2: Modeling Engines (PARTIAL MOVE)

#### 3.2.1 Site Challenges and Modeling Needs (KEEP)
**Lines:** 509-519 (~10 lines)  
**Decision:** KEEP - Essential context for why surrogates are needed

#### 3.2.2 Physics-Based Numerical Models (KEEP)
**Lines:** 521-531 (~10 lines)  
**Decision:** KEEP - Brief overview of MODFLOW, PFLOTRAN, etc.

#### 3.2.3 Surrogate Model Landscape (MOVE MOST TO APPENDIX)
**Lines:** 533-612 (~80 lines)  
**Decision:** MOVE ~60 lines to Appendix, KEEP ~20 lines summary

**Content to MOVE to Appendix A:**

| Lines | Content | Reason to Move |
|-------|---------|----------------|
| 535-545 | Web of Science search methodology, Figure 1 description | Literature review methodology |
| 541-545 | Method family breakdown methodology | Literature review methodology |
| 555-561 | Convolutional encoder-decoder detailed literature (Taccari, Mo, Jiang, Lauzon citations) | Detailed literature context |
| 563-569 | Operator-learning detailed literature (Li, Wen, Taccari, Jiang, Wang citations) | Detailed literature context |
| 571-578 | Sequence models detailed literature (Chen, Xie, Anshuman, Li, Zhang citations) | Detailed literature context |
| 581-589 | Generative models detailed literature (Graham, Miele, Wang citations) | Detailed literature context |
| 591-597 | Regression surrogates detailed literature (Asher, Siade, Shams, Marrel citations) | Detailed literature context |
| 599-611 | Structured domain surrogates (POD, DMD, Koopman, graph neural) | Adjacent methods context |
| 605-611 | Figure 4 heatmap detailed description | Literature analysis |

**Content to KEEP in Section 3.2.3:**

| Lines | Content | Reason to Keep |
|-------|---------|----------------|
| 533-534 | Section intro | Context |
| 555-557 | CNN/U-Net brief description (1-2 sentences) | Method overview |
| 563-565 | FNO/U-FNO brief description (1-2 sentences) | Method overview |
| 571-573 | Sequence models brief description (1-2 sentences) | Method overview |
| 581-583 | Generative models brief description (1-2 sentences) | Method overview |
| 591-593 | Regression surrogates brief description (1-2 sentences) | Method overview |

**Estimated:** Move ~60 lines, Keep ~20 lines

#### 3.2.4 General Surrogate Model Training Setup (KEEP)
**Lines:** 615-626 (~12 lines)  
**Decision:** KEEP - Practical training guidance

---

### 2.3 Section 3.3: Recalibration Mechanisms (KEEP MOST)

#### 3.3.1 Uncertainty Quantification (KEEP)
**Lines:** 639-680 (~40 lines)  
**Decision:** KEEP ALL

**Content:**
- MC-Dropout, deep ensembles, conformal prediction
- EnKF, particle filters for DA
- Sequential Bayesian inference
- Hybrid integration strategy

**Rationale:** Core methods for the framework, not heavy literature review.

#### 3.3.2 Trigger Logic (KEEP)
**Lines:** 683-826 (~140 lines)  
**Decision:** KEEP ALL

**Content:**
- Tipping point-inspired resilience metrics
- Performance and uncertainty-based metrics
- Distributional and representation-level drift detection
- Probabilistic integration and decision logic
- Table 1: Exemplary Regime Drift Diagnostics
- Three-phase workflow for drift monitoring

**Rationale:** Core framework methodology, not literature review.

#### 3.3.3 Continual Learning (KEEP)
**Lines:** 827-858 (~30 lines)  
**Decision:** KEEP ALL

**Content:**
- EWC, replay buffers (70-75%)
- Layer freezing strategy
- Fine-tuning workflow steps

**Rationale:** Core methods with specific parameters for the framework.

#### 3.3.4 Active Learning (KEEP)
**Lines:** 861-889 (~30 lines)  
**Decision:** KEEP ALL

**Content:**
- Uncertainty sampling, error-based sampling
- Diversity constraints
- Batch size 6-10 recommendations
- Structured workflow steps

**Rationale:** Core methods with specific parameters for the framework.

#### 3.3.5 Multi-fidelity Data Fusion (KEEP)
**Lines:** 891-924 (~35 lines)  
**Decision:** KEEP ALL

**Content:**
- Co-Kriging, neural discrepancy models
- Pre-training on low-fidelity, fine-tuning on high-fidelity
- Structured workflow steps

**Rationale:** Core methods for the framework.

#### 3.3.6 Fully Retrain (KEEP)
**Lines:** 925-954 (~30 lines)  
**Decision:** KEEP ALL

**Content:**
- When full retraining is needed
- Structured retraining workflow

**Rationale:** Core framework methodology.

---

## 3. Summary: Content Movement Plan

### 3.1 Content to MOVE to Appendix A

| Source | Content | Est. Lines | New Location |
|--------|---------|------------|--------------|
| 3.2.3 | Web of Science methodology | ~10 | Appendix A.1 |
| 3.2.3 | CNN/U-Net detailed literature | ~10 | Appendix A.2.1 |
| 3.2.3 | FNO/U-FNO detailed literature | ~10 | Appendix A.2.2 |
| 3.2.3 | Sequence models detailed literature | ~10 | Appendix A.2.3 |
| 3.2.3 | Generative models detailed literature | ~10 | Appendix A.2.4 |
| 3.2.3 | Regression surrogates detailed literature | ~10 | Appendix A.2.5 |
| 3.2.3 | Structured domain surrogates | ~15 | Appendix A.2.6 |
| 3.2.3 | Figure 4 heatmap analysis | ~10 | Appendix A.3 |

**Total to move:** ~85 lines

### 3.2 Content to KEEP in Section 3

| Subsection | Content | Est. Lines |
|------------|---------|------------|
| 3.1 | Governance Essentials (all) | ~95 |
| 3.2.1 | Site Challenges | ~10 |
| 3.2.2 | Physics-Based Models | ~10 |
| 3.2.3 | Surrogate Landscape (summary only) | ~20 |
| 3.2.4 | Training Setup | ~12 |
| 3.3.1 | UQ Methods | ~40 |
| 3.3.2 | Trigger Logic | ~140 |
| 3.3.3 | Continual Learning | ~30 |
| 3.3.4 | Active Learning | ~30 |
| 3.3.5 | Multi-fidelity Fusion | ~35 |
| 3.3.6 | Fully Retrain | ~30 |

**Total to keep:** ~450 lines (down from ~550)

---

## 4. Proposed Appendix A Structure

```
Appendix A: Surrogate Model Literature Context

A.1 Literature Review Methodology
    - Web of Science search strategy
    - Screening criteria
    - Method family classification

A.2 Surrogate Model Families: Detailed Review
    A.2.1 Convolutional Encoder-Decoder Models
          - U-Net, ResNet architectures
          - Key papers: Taccari 2022, Mo 2019, Jiang 2021, Lauzon 2024
          
    A.2.2 Operator-Learning Models
          - FNO, U-FNO, DeepONet
          - Key papers: Li 2020, Wen 2022, Taccari 2024, Jiang 2025
          
    A.2.3 Sequence Models
          - LSTM, GRU, Transformers
          - Key papers: Chen 2021, Xie 2024, Anshuman 2023
          
    A.2.4 Generative Models
          - VAEs, GANs, Diffusion models
          - Key papers: Graham 2020, Miele 2025, Wang 2025
          
    A.2.5 Regression and Classical Surrogates
          - Gaussian processes, Kriging, shallow ANNs
          - Key papers: Asher 2015, Siade 2020, Shams 2021
          
    A.2.6 Structured Domain Surrogates
          - POD, DMD, Koopman operators, Graph neural networks
          - Key papers: Schmid 2010, Mezić 2013, Pfaff 2020

A.3 Literature Analysis Figures
    - Figure A1: Publication trends (current Figure 1)
    - Figure A2: Method evolution (current Figure 2)
    - Figure A3: Application heatmap (current Figure 4)
```

---

## 5. Streamlined Section 3.2.3 Skeleton

```markdown
### 3.2.3 Surrogate Model Landscape

The framework supports multiple surrogate model families, each suited to different 
prediction tasks. For detailed literature context and architecture comparisons, 
see Appendix A.

**Convolutional Encoder-Decoder Models** (e.g., U-Net, ResNet) are well-suited for 
high-resolution spatial field prediction where local patterns and interfaces are 
important. These models treat spatial fields as images and learn direct mappings 
from inputs to outputs.

**Operator-Learning Models** (e.g., FNO, U-FNO, DeepONet) learn the solution operator 
of the PDE, enabling resolution-invariant surrogates that generalize across boundary 
conditions and parameter configurations.

**Sequence Models** (e.g., LSTM, GRU, Transformers) focus on low-dimensional time 
series outputs such as breakthrough curves or well responses, capturing long-range 
temporal dependencies.

**Generative Models** (e.g., VAEs, diffusion models) sample ensembles of plausible 
states consistent with physics and observations, supporting uncertainty quantification 
and probabilistic inversion.

**Regression Surrogates** (e.g., Gaussian processes, shallow ANNs) remain effective 
for low-dimensional scalar metrics where interpretability and small-data robustness 
are priorities.

The choice of surrogate family depends on the prediction task, data availability, 
and decision-support requirements. Section 5 (Implementation Roadmap) describes 
how these surrogates integrate with the recalibration workflow.
```

---

## 6. Decision: Other Sections for Appendix?

Based on your question about whether continual learning or UQ content should also move to appendix:

### UQ Methods (Section 3.3.1): KEEP
- Content is concise (~40 lines)
- Describes specific methods (MC-Dropout, ensembles, conformal prediction)
- No heavy literature review
- Essential for understanding the framework

### Continual Learning (Section 3.3.3): KEEP
- Content is concise (~30 lines)
- Provides specific parameters (70-75% replay, EWC)
- No heavy literature review
- Essential for understanding the update workflow

### Trigger Logic (Section 3.3.2): KEEP
- Content is substantial (~140 lines) but all framework-specific
- Table 1 is essential reference
- Three-phase workflow is core methodology
- No heavy literature review

**Recommendation:** Only Section 3.2.3 (Surrogate Model Landscape) has significant literature review content that should move to appendix. The other sections are already appropriately focused on framework methodology.

---

## 7. Next Steps

1. Create structural skeleton for streamlined Section 3
2. Create structural skeleton for new Section 5 (Prototype & Case Study)
3. Create structural skeleton for new Section 6 (Future Work & Summary)
4. Create structural skeleton for expanded Appendix A
5. Get user review of all skeletons
6. Implement in Code mode

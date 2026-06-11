# Master Document Layout

**Title:** Keeping Deep-Learning Surrogates Accurate for Long-Term Groundwater Remediation: Concept & Prototype Plan  
**Version:** Restructured Draft  
**Date:** 2025-03-19

---

## Document Overview

This master layout integrates all existing work into the new document structure. Each section shows:
- **Source:** Where content comes from
- **Status:** Ready / Needs Work / New Content Needed
- **Content:** What goes in each section

---

# FRONT MATTER

## Title Page
**Source:** Framework_draft.docx (lines 1-160)  
**Status:** Keep as-is

## Abstract
**Source:** Framework_draft.docx (lines 163-165)  
**Status:** Needs update after restructuring

## Summary
**Source:** Framework_draft.docx (lines 167-176)  
**Status:** Keep as-is (good overview of three pillars and framework)

## Acknowledgments
**Source:** Framework_draft.docx (lines 179-181)  
**Status:** Keep as-is

## Acronyms and Abbreviations
**Source:** Framework_draft.docx (lines 183-186)  
**Status:** Keep as-is

## Table of Contents
**Status:** Auto-generate after restructuring

---

# SECTION 1: INTRODUCTION

**Source:** Framework_draft.docx (lines 339-356)  
**Status:** ✅ Keep as-is  
**Length:** ~18 lines

### Content Summary:
- Problem statement: DL surrogates drift from reality
- Key challenges: Concept/distribution drift, data/compute scarcity, physical realism
- Motivation for adaptive strategies
- Document overview

### Key Points Preserved:
- "Physics-based simulators provide high-fidelity forecasts but are too slow"
- "Deep learning surrogates can predict rapidly but lose accuracy over time"
- "Continual learning, multi-fidelity methods, and rigorous UQ"

---

# SECTION 2: FRAMEWORK OVERVIEW

**Status:** ✅ COMPLETE (Revised drafts ready)

## 2.1 Three-Pillar Architecture

**Source:** [`drafts/section2_1_pillars_REVISED.md`](drafts/section2_1_pillars_REVISED.md)  
**Status:** ✅ Ready to use  
**Length:** 109 lines

### Content:
```
2.1 Three-Pillar Architecture

## Pillar A: Conceptual Design & Governance
- Rules Repository
- Regulatory requirements, validation protocols, documentation standards
- Workflow Integration: Steps 3 (DECIDE) and 7 (DEPLOY)

## Pillar B: Modeling Engines
- Models Repository
- Physics-based simulators + DL surrogates
- Workflow Integration: Steps 5 (UPDATE) and 6 (CALIBRATE)

## Pillar C: Recalibration Mechanisms
- Adaptive Methods Toolkit
- UQ, trigger logic, continual learning, active learning
- Workflow Integration: All steps, especially 1-3 and 4-6

## Complementary Roles of the Three Pillars
- Pillars define WHAT; Workflow defines HOW

## Cross-Reference: Pillars and Workflow
- Table showing which pillars are active in each workflow step
```

## 2.2 Recalibration Workflow

**Source:** [`drafts/section2_2_workflow_REVISED.md`](drafts/section2_2_workflow_REVISED.md)  
**Status:** ✅ Ready to use  
**Length:** 366 lines

### Content:
```
2.2 Recalibration Workflow

## Phase 1: Continuous Monitoring
- Step 1: MONITOR - Track predictions vs. observations
- Step 2: DETECT - Identify drift signals
- Step 3: DECIDE - Governance decision on update

## Phase 2: Triggered Response
- Step 4: PREPARE - Assemble update dataset
- Step 5: UPDATE - Fine-tune surrogate
- Step 6: CALIBRATE - Recalibrate uncertainty
- Step 7: DEPLOY - Release with audit trail

## Cross-Reference: Workflow Steps and Pillars
- Table showing pillar involvement per step

## Workflow Visualization
- Mermaid diagram of two-phase workflow

## Update Pathways
- Pathway A: Observation-Driven Update
- Pathway B: Simulation-Driven Update

## Operational Considerations
- Monitoring frequency
- Update frequency
- Cycle continuation
```

---

# SECTION 3: METHODS

**Status:** Needs streamlining (move literature to Appendix A)

## 3.0 Methods Introduction

**Source:** New content  
**Status:** New paragraph needed

```markdown
This section details the methods organized by the three pillars defined in 
Section 2.1. Each subsection describes the specific techniques and approaches 
that enable the recalibration framework. For extended literature context on 
surrogate model architectures, see Appendix A.
```

## 3.1 Governance Methods (Pillar A)

**Source:** Framework_draft.docx (lines 409-503)  
**Status:** ✅ Keep all content  
**Length:** ~95 lines

### Content:
```
3.1 Governance Essentials

3.1.1 Regulatory Alignment and Quality Assurance Foundations
      - CERCLA, DOE O 414.1D, NQA-1, EM-QA-001
      - Surrogate models as controlled analytical software

3.1.2 Model Usage Scope and Decision Context
      - Screening-level analyses vs. regulatory decisions
      - Physics-based models remain authoritative

3.1.3 Acceptance Criteria and Recalibration Triggers
      - Quantitative performance metrics
      - Uncertainty calibration requirements
      - Trigger thresholds (objective, documented)

3.1.4 Operational Monitoring and Review Schedule
      - Automated diagnostics (regular basis)
      - Summary evaluations (monthly/quarterly)
      - Formal decision points (quarterly)

3.1.5 Transparency, Auditability, and Configuration Control
      - Version tracking
      - Governance records
      - Data provenance
      - Rollback procedures (withdrawal + full retrain)

3.1.6 Summary

**Workflow Integration:** Steps 3 (DECIDE) and 7 (DEPLOY)
```

## 3.2 Modeling Engine Methods (Pillar B)

**Source:** Framework_draft.docx (lines 507-626) + streamlining  
**Status:** Needs work (streamline 3.2.3)

### 3.2.1 Site Challenges and Modeling Needs
**Source:** Framework_draft.docx (lines 509-519)  
**Status:** ✅ Keep as-is  
**Length:** ~10 lines

```
- Heterogeneity in hydraulic and transport properties
- Diffusion-controlled mass exchange
- Back diffusion from low-permeability zones
- Density and buoyancy effects
- Engineered operations representation
```

### 3.2.2 Physics-Based Numerical Models
**Source:** Framework_draft.docx (lines 521-531)  
**Status:** ✅ Keep as-is  
**Length:** ~10 lines

```
- MODFLOW for regional groundwater flow
- MT3DMS for solute transport
- PFLOTRAN, eSTOMP, TOUGH2 for reactive transport
- PARFLOW for integrated surface/subsurface
- HYDRUS for vadose zone
- Computational constraints motivating surrogates
```

### 3.2.3 Surrogate Model Landscape
**Source:** Framework_draft.docx (lines 533-612) → STREAMLINED  
**Status:** Needs work (move ~60 lines to Appendix A)  
**New Length:** ~20 lines

```markdown
### 3.2.3 Surrogate Model Landscape

The framework supports multiple surrogate model families, each suited to 
different prediction tasks. For detailed literature context and architecture 
comparisons, see Appendix A.

**Convolutional Encoder-Decoder Models** (e.g., U-Net, ResNet) are well-suited 
for high-resolution spatial field prediction where local patterns and interfaces 
are important. These models treat spatial fields as images and learn direct 
mappings from inputs to outputs.

**Operator-Learning Models** (e.g., FNO, U-FNO, DeepONet) learn the solution 
operator of the PDE, enabling resolution-invariant surrogates that generalize 
across boundary conditions and parameter configurations.

**Sequence Models** (e.g., LSTM, GRU, Transformers) focus on low-dimensional 
time series outputs such as breakthrough curves or well responses, capturing 
long-range temporal dependencies.

**Generative Models** (e.g., VAEs, diffusion models) sample ensembles of 
plausible states consistent with physics and observations, supporting 
uncertainty quantification and probabilistic inversion.

**Regression Surrogates** (e.g., Gaussian processes, shallow ANNs) remain 
effective for low-dimensional scalar metrics where interpretability and 
small-data robustness are priorities.

The choice of surrogate family depends on the prediction task, data availability, 
and decision-support requirements. Section 4 (Implementation Roadmap) describes 
how these surrogates integrate with the recalibration workflow.
```

### 3.2.4 General Surrogate Model Training Setup
**Source:** Framework_draft.docx (lines 615-626)  
**Status:** ✅ Keep as-is  
**Length:** ~12 lines

```
- Data splits: Hold out realizations across time and parameter ranges
- Normalization: Standardize each channel, record scaling in metadata
- Early stopping: Track validation metric on decision outputs
- Runtime reporting: Record forward runtime and surrogate inference time
```

**Workflow Integration:** Steps 5 (UPDATE) and 6 (CALIBRATE)

## 3.3 Recalibration Mechanism Methods (Pillar C)

**Source:** Framework_draft.docx (lines 631-954)  
**Status:** ✅ Keep all content  
**Length:** ~320 lines

### 3.3.1 Uncertainty Quantification of Surrogate Models
**Source:** Framework_draft.docx (lines 639-680)  
**Status:** ✅ Keep as-is  
**Length:** ~40 lines

```
- MC-Dropout, deep ensembles for epistemic uncertainty
- Conformal prediction for statistically valid bounds
- EnKF for Gaussian contexts
- Particle filters for non-Gaussian/nonlinear
- Sequential Bayesian inference
- Hybrid integration strategy
```

### 3.3.2 Trigger Logic
**Source:** Framework_draft.docx (lines 683-826)  
**Status:** ✅ Keep as-is  
**Length:** ~140 lines

```
- Tipping Point-Inspired Resilience Metrics
  - Rolling variance, lag-1 autocorrelation
  - Skewness, kurtosis

- Performance and Uncertainty-Based Metrics
  - Prediction residuals with adaptive thresholds
  - Predictive uncertainty tracking

- Distributional and Representation-Level Drift Detection
  - Kolmogorov-Smirnov test
  - Latent space drift indicators

- Probabilistic Integration and Decision Logic
  - Bayesian inference combining multiple signals
  - Composite gating mechanisms

- Table 1: Exemplary Regime Drift Diagnostics

- Three-Phase Workflow for Drift Monitoring
  - Phase 1: Candidate Identification
  - Phase 2: Simulation-Based Robustness Testing
  - Phase 3: Operational Implementation
```

### 3.3.3 Continual Learning
**Source:** Framework_draft.docx (lines 827-858)  
**Status:** ✅ Keep as-is  
**Length:** ~30 lines

```
- EWC (Elastic Weight Consolidation)
- Replay buffers (70-75% historical samples)
- Layer freezing (early encoder layers)
- Small learning rate + regularization
- Early stopping on validation
- Uncertainty recalibration
- Governance package preparation
```

### 3.3.4 Active Learning
**Source:** Framework_draft.docx (lines 861-889)  
**Status:** ✅ Keep as-is  
**Length:** ~30 lines

```
- Uncertainty sampling (high predictive variance)
- Error-based sampling (large residuals)
- Diversity constraints (spatial, stratigraphic, forcing)
- Batch size 6-10 simulations
- Document simulation rationale
```

### 3.3.5 Multi-fidelity Data Fusion
**Source:** Framework_draft.docx (lines 891-924)  
**Status:** ✅ Keep as-is  
**Length:** ~35 lines

```
- Autoregressive GP / co-Kriging
- Neural discrepancy models
- Pre-train on low-fidelity, fine-tune on high-fidelity
- Fidelity-conditioned uncertainty
- Validation against withheld HF runs
```

### 3.3.6 Fully Retrain
**Source:** Framework_draft.docx (lines 925-954)  
**Status:** ✅ Keep as-is  
**Length:** ~30 lines

```
- When needed: regime shifts, major forcing changes, repeated failures
- Verify retraining triggers
- Redesign training domain
- Generate new HF ensemble
- Integrate recent field observations
- Train from scratch with full UQ
- Archive prior surrogate
```

**Workflow Integration:** All steps, especially Steps 1-3 (monitoring) and Steps 4-6 (update)

---

# SECTION 4: IMPLEMENTATION ROADMAP

**Source:** [`drafts/section5_REVISED_v3.md`](drafts/section5_REVISED_v3.md)  
**Status:** ✅ COMPLETE (Ready to use, just renumber from 5.x to 4.x)  
**Length:** 277 lines

### Content:
```
4.0 Implementation Roadmap (was 5.0)

4.1 Design Philosophy (was 5.1)
    4.1.1 Guiding Principles
    4.1.2 Relationship to Section 3 Methods

4.2 Phase 1 Capabilities: Continuous Monitoring (was 5.2)
    4.2.1 Performance Monitoring (Step 1: MONITOR)
    4.2.2 Drift Detection (Step 2: DETECT)
    4.2.3 Governance Decision (Step 3: DECIDE)

4.3 Phase 2 Capabilities: Triggered Response (was 5.3)
    4.3.1 Data Preparation (Step 4: PREPARE)
    4.3.2 Model Update (Step 5: UPDATE)
    4.3.3 Uncertainty Recalibration (Step 6: CALIBRATE)
    4.3.4 Deployment and Governance (Step 7: DEPLOY)

4.4 Infrastructure Requirements (was 5.4)
    4.4.1 Data Management
    4.4.2 Computational Resources
    4.4.3 Interoperability

4.5 Development Phases (was 5.5)
    - Phase 1: Prototype Demonstration
    - Phase 2: Integrated Framework
    - Phase 3: Operational System

4.6 Open Design Questions (was 5.6)

4.7 Summary (was 5.7)
```

---

# SECTION 5: PROTOTYPE & CASE STUDY

**Source:** Framework_draft.docx Sections 4 + 6 (merged) + new content  
**Status:** Needs work (merge and add new content)

## 5.0 Introduction

**Source:** New content  
**Status:** New paragraph needed

```markdown
This section presents the validation framework, prototype implementations, and 
case study design that demonstrate the recalibration framework in practice. 
The prototypes serve as proof-of-concept implementations that validate the 
seven-step workflow described in Section 2.2.
```

## 5.1 Validation Framework

**Source:** Framework_draft.docx (lines 955-968)  
**Status:** Needs expansion  
**Current Length:** ~15 lines → Expand to ~40 lines

### 5.1.1 Performance Metrics
```
- Accuracy: RMSE, MAE, bias
- Contaminant mass reduction
- Plume extent prediction accuracy
- Drawdown head error
```

### 5.1.2 Uncertainty Metrics
```
- Predictive interval coverage
- Calibration of uncertainty estimates
- Confidence in capture zones
```

### 5.1.3 Drift Detection Metrics
```
- Residual thresholds
- Distributional drift indicators
- Composite drift index
```

### 5.1.4 Governance Compliance Metrics
```
- Acceptance criteria alignment
- Audit trail completeness
- Regulatory documentation
```

### 5.1.5 Acceptance Thresholds
```
- Example: ≥90% contaminant mass removed within 10 years
- Example: 95% prediction interval coverage ≥90%
- Example: Monitoring network cost reduction ≥30%
```

## 5.2 Prototype Implementations

**Source:** Framework_draft.docx (lines 1245-1384)  
**Status:** ✅ Keep content, add workflow integration  
**Length:** ~140 lines

### 5.2.1 U-FNO Surrogate for 2D Cross-Section Transport

**Source:** Framework_draft.docx (lines 1277-1318)

```
**PFLOTRAN Baseline Model**
- 84m × 4m domain, 28 × 40 grid
- Variably saturated Richards equation
- Time-varying boundary conditions (tidal influence)
- Heterogeneous permeability/porosity fields (Gaussian)
- Adapted from GeoFUSE (Jiang et al., 2025)

**U-FNO Architecture and Training**
- Fourier layers + U-Net path
- ~126 million parameters
- Learning rate 0.001 with stepwise decay
- 200 epochs, batch size 4
- Separate networks for pressure and concentration

**Workflow Integration** [NEW]
- Supports Steps 1-3: Fast inference for continuous monitoring
- Enables rapid scenario testing for decision support
- UQ via ensemble or MC-Dropout
```

### 5.2.2 U-Net Surrogate for 2D Pump-and-Treat Plume Prediction

**Source:** Framework_draft.docx (lines 1321-1384)

```
**Training Data Generation**
- 128 × 100 mesh, 1m × 1m cells
- 1-5 extraction wells in central well field
- 10,000 physics simulation runs
- Plume snapshots at 0, 1, 2, 3, 4 days
- Based on Song et al. (2025)

**Architectural Modifications**
- Thiem equation drawdown map as physics-inspired input
- Strided convolutions (not max pooling)
- Leaky Tanh bounded activation
- Skip connections for sharp fronts

**Training Workflow**
- 70/15/15 train/validate/test split
- MSE loss, Adam optimizer
- Early stopping
- Autoregressive rollout for multi-step prediction

**Workflow Integration** [NEW]
- Supports P&T scenario screening
- Enables rapid evaluation of well configurations
- Integration with recalibration loop for long-term operation
```

## 5.3 Case Study Design

**Source:** New content (synthesize from existing material)  
**Status:** New content needed  
**Length:** ~40 lines

### 5.3.1 Hydrological Modeling Scenario
```
- Synthetic site based on EM site characteristics
- Contaminant: [specify based on prototype]
- Initial conditions: contaminated plume
- Remediation system: pump-and-treat configuration
```

### 5.3.2 Data Sources and Simulation Setup
```
- Physics model: PFLOTRAN configuration
- Training data: ensemble of heterogeneous realizations
- Monitoring data: simulated observations at well locations
- Drift injection: regime change scenario
```

### 5.3.3 Recalibration Demonstration
```
- Baseline surrogate performance
- Drift injection (e.g., pumping regime change)
- Trigger activation (Step 2-3)
- Targeted physics runs (Step 4)
- Fine-tuning execution (Step 5)
- UQ recalibration (Step 6)
- Performance comparison (before/after)
```

## 5.4 Evaluation Plan

**Source:** New content  
**Status:** New content needed  
**Length:** ~30 lines

### 5.4.1 Baseline Comparison
```
- Physics-only vs. surrogate-only vs. hybrid
- Computational cost comparison
- Accuracy comparison across scenarios
```

### 5.4.2 Recalibration Effectiveness
```
- Error reduction after update
- Uncertainty calibration improvement
- Time to detect drift
- Number of physics runs required
```

### 5.4.3 Computational Efficiency
```
- Speedup factors (target: 10³-10⁴×)
- Cost of targeted physics runs
- Total computational budget
- Comparison to full retraining
```

## 5.5 Development Timeline

**Source:** Framework_draft.docx (lines 1263-1266) + section5_REVISED_v3.md  
**Status:** Merge from both sources  
**Length:** ~20 lines

```
- Phase 1: Prototype Demonstration
  - Single surrogate architecture
  - Basic drift detection
  - Manual recalibration trigger

- Phase 2: Integrated Framework
  - Multiple surrogate options
  - Automated trigger logic
  - Governance integration

- Phase 3: Operational System
  - Full workflow automation
  - Multi-site deployment
  - Regulatory documentation
```

---

# SECTION 6: FUTURE WORK & SUMMARY

**Source:** Framework_draft.docx (lines 1387-1394) + new content  
**Status:** Needs expansion

## 6.0 Introduction

**Source:** New content  
**Status:** New paragraph needed

```markdown
This section outlines the research roadmap, expected impact, and key conclusions 
of the recalibration framework. The framework represents a significant step 
toward maintaining deep-learning surrogate accuracy over multi-year operational 
periods while preserving regulatory confidence.
```

## 6.1 Research Roadmap

**Source:** Framework_draft.docx (lines 1387-1394)  
**Status:** Expand from ~8 lines to ~30 lines

### 6.1.1 Short-Term Goals
```
- Complete prototype demonstration
- Validate recalibration loop on synthetic case
- Document framework design package
- Establish baseline performance metrics
```

### 6.1.2 Medium-Term Goals
```
- Extend to additional constituents (CTET, TCE)
- Apply to real EM site data
- Integrate with operational workflows
- Develop user-facing dashboard
```

### 6.1.3 Long-Term Vision
```
- Multi-site deployment
- Digital twin integration
- Autonomous recalibration systems
- Alignment with DOE digital-twin initiatives
```

## 6.2 Expected Impact

**Source:** Framework_draft.docx (lines 1389-1393) + new content  
**Status:** Expand  
**Length:** ~40 lines

### 6.2.1 Scientific Contributions
```
- Novel integration of UQ, active learning, continual learning
- Framework for adaptive surrogate maintenance
- Methodology for drift detection in environmental models
- Governance framework for ML in regulatory contexts
```

### 6.2.2 Operational Benefits
```
- Faster scenario iteration (10³-10⁴× speedup)
- Reduced unnecessary simulator runs
- Explainable updates for regulator confidence
- Maintained accuracy over multi-year timelines
- Reduced computational costs (target: xx-xx%)
```

### 6.2.3 Broader Applications
```
- Other DOE EM sites
- Climate resilience applications
- General scientific surrogate maintenance
- Open-source code, containers, demo datasets
```

## 6.3 Limitations and Open Questions

**Source:** New content + cross-reference to Section 4.6  
**Status:** New content needed  
**Length:** ~30 lines

### 6.3.1 Current Framework Limitations
```
- Dependence on physics model quality
- Computational requirements for ensemble methods
- Generalization across site types
- Limited validation on real field data
```

### 6.3.2 Areas Requiring Further Research
```
- Optimal trigger threshold calibration
- Multi-fidelity fusion strategies
- Transfer learning across sites
- Scalability to 3D problems
```

### 6.3.3 Governance Considerations
```
- Regulatory acceptance pathway
- Long-term maintenance requirements
- Documentation standards evolution
- Stakeholder engagement strategy
```

## 6.4 Conclusion

**Source:** New content  
**Status:** New content needed  
**Length:** ~30 lines

### 6.4.1 Summary of Framework Contributions
```
This document presents a comprehensive framework for maintaining deep-learning 
surrogate accuracy in long-term groundwater remediation applications. The 
framework is organized around three pillars:

- **Pillar A (Governance):** Ensures regulatory alignment and operational stability
- **Pillar B (Modeling Engines):** Provides physics-based truth and fast surrogates
- **Pillar C (Recalibration Mechanisms):** Enables adaptive maintenance

The seven-step, two-phase workflow operationalizes these pillars through 
continuous monitoring (Steps 1-3) and triggered response (Steps 4-7).
```

### 6.4.2 Key Takeaways
```
- Surrogates require systematic maintenance to remain accurate
- Physics-based models remain the authoritative reference
- Governance ensures regulatory confidence
- Adaptive strategies outperform static approaches
- The framework balances accuracy, efficiency, and trust
```

### 6.4.3 Path Forward
```
The prototype demonstration will validate the framework on synthetic cases, 
followed by application to real EM site data. Open-source release of code, 
containers, and demo datasets will enable broader adoption and community 
contribution to framework development.
```

---

# SECTION 7: REFERENCES

**Source:** Framework_draft.docx (lines 1397-1572)  
**Status:** ✅ Keep as-is  
**Length:** ~175 lines

---

# APPENDIX A: SURROGATE MODEL LITERATURE CONTEXT

**Source:** Moved from Section 3.2.3 + existing Appendix  
**Status:** Needs assembly

## A.1 Literature Review Methodology

**Source:** Framework_draft.docx (lines 535-545)  
**Status:** Move here

```
- Web of Science Core Collection search
- Topic search: groundwater/subsurface + surrogate-modeling terms
- Period: 2005-2026
- Screening criteria
- Method family classification (5 families)
```

## A.2 Surrogate Model Families: Detailed Review

**Source:** Framework_draft.docx (lines 555-611)  
**Status:** Move here

### A.2.1 Convolutional Encoder-Decoder Models
```
- Architecture overview
- Key papers: Taccari 2022, Mo 2019, Jiang 2021, Lauzon 2024
- Strengths and limitations
```

### A.2.2 Operator-Learning Models
```
- Architecture overview
- Key papers: Li 2020, Wen 2022, Taccari 2024, Jiang 2025, Wang 2022
- Strengths and limitations
```

### A.2.3 Sequence Models
```
- Architecture overview
- Key papers: Chen 2021, Xie 2024, Anshuman 2023, Li 2025
- Strengths and limitations
```

### A.2.4 Generative Models
```
- Architecture overview
- Key papers: Graham 2020, Miele 2025, Wang 2025
- Strengths and limitations
```

### A.2.5 Regression and Classical Surrogates
```
- Architecture overview
- Key papers: Asher 2015, Siade 2020, Shams 2021, Marrel 2024
- Strengths and limitations
```

### A.2.6 Structured Domain Surrogates
```
- Architecture overview
- Key papers: Schmid 2010, Mezić 2013, Pfaff 2020
- Strengths and limitations
```

## A.3 Literature Analysis Figures

**Source:** Framework_draft.docx (lines 311-317, 538-545, 605-611)  
**Status:** Move here

```
- Figure A1: Publication trends (current Figure 1)
- Figure A2: Method evolution (current Figure 2)
- Figure A3: Conceptual mind-map (current Figure 3)
- Figure A4: Application heatmap (current Figure 4)
```

## A.4 Paper Review Tables

**Source:** Framework_draft.docx (lines 1603-2250)  
**Status:** ✅ Keep as-is

```
- Table A1: Machine Learning Based Surrogates Paper Review
- Table A2: Curated set of representative publications
```

---

# APPENDIX B: SOFTWARE ARCHITECTURE DETAILS

**Source:** Framework_draft.docx (lines 969-1244) + manuscript/Section5_Software_Architecture_REVISED.md  
**Status:** Optional - move detailed software specs here

```
- Software Requirements
- System Architecture
- Independent Software Packages
- Operational System Architecture
- User Interface Concepts
- Software Development Guidelines
- Hosting Options
```

---

# APPENDIX C: USER INTERFACE CONCEPTS

**Source:** Framework_draft.docx (lines 2255-2276)  
**Status:** ✅ Keep as-is

```
- Figure: Modeling control panel
- Figure: Dashboard for metrics
- Figure: Dashboard for sensor histories
- Figure: Dashboard for model comparisons
```

---

## IMPLEMENTATION CHECKLIST

### Ready to Use (No Changes Needed)
- [ ] Section 1: Introduction
- [ ] Section 2.1: Three-Pillar Architecture (from drafts/section2_1_pillars_REVISED.md)
- [ ] Section 2.2: Recalibration Workflow (from drafts/section2_2_workflow_REVISED.md)
- [ ] Section 3.1: Governance Methods
- [ ] Section 3.2.1: Site Challenges
- [ ] Section 3.2.2: Physics-Based Models
- [ ] Section 3.2.4: Training Setup
- [ ] Section 3.3: All Recalibration Mechanism Methods
- [ ] Section 4: Implementation Roadmap (from drafts/section5_REVISED_v3.md, renumber)
- [ ] Section 7: References
- [ ] Appendix A.4: Paper Review Tables

### Needs Streamlining
- [ ] Section 3.2.3: Surrogate Model Landscape (move literature to Appendix A)

### Needs Merging
- [ ] Section 5: Prototype & Case Study (merge Sections 4+6)

### Needs New Content
- [ ] Section 5.3: Case Study Design
- [ ] Section 5.4: Evaluation Plan
- [ ] Section 6.3: Limitations and Open Questions
- [ ] Section 6.4: Conclusion

### Needs Assembly
- [ ] Appendix A.1-A.3: Literature context (from Section 3.2.3)

---

## FILE MAPPING

| New Section | Source File(s) | Status |
|-------------|----------------|--------|
| Section 1 | Framework_draft.docx | Keep |
| Section 2.1 | drafts/section2_1_pillars_REVISED.md | ✅ Ready |
| Section 2.2 | drafts/section2_2_workflow_REVISED.md | ✅ Ready |
| Section 3.1 | Framework_draft.docx (lines 409-503) | Keep |
| Section 3.2.1-2 | Framework_draft.docx (lines 509-531) | Keep |
| Section 3.2.3 | Framework_draft.docx → Streamline | Work needed |
| Section 3.2.4 | Framework_draft.docx (lines 615-626) | Keep |
| Section 3.3 | Framework_draft.docx (lines 631-954) | Keep |
| Section 4 | drafts/section5_REVISED_v3.md | ✅ Ready (renumber) |
| Section 5.1 | Framework_draft.docx (lines 955-968) | Expand |
| Section 5.2 | Framework_draft.docx (lines 1277-1384) | Keep + add |
| Section 5.3 | New content | Create |
| Section 5.4 | New content | Create |
| Section 5.5 | Framework_draft.docx + v3 | Merge |
| Section 6.1 | Framework_draft.docx (lines 1387-1394) | Expand |
| Section 6.2 | New content | Create |
| Section 6.3 | New content | Create |
| Section 6.4 | New content | Create |
| Section 7 | Framework_draft.docx (lines 1397-1572) | Keep |
| Appendix A | Framework_draft.docx (moved from 3.2.3) | Assemble |
| Appendix B | Framework_draft.docx (lines 969-1244) | Optional |
| Appendix C | Framework_draft.docx (lines 2255-2276) | Keep |

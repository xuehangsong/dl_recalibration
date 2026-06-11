# Document Structural Skeletons

**Purpose:** Provide structural outlines for all sections needing work  
**Status:** DRAFT - For User Review  
**Date:** 2025-03-19

---

## Document Overview (New Structure)

| Section | Title | Status | Source |
|---------|-------|--------|--------|
| 1 | Introduction | Keep as-is | Current Section 1 |
| 2 | Framework Overview | ✅ DONE | Revised drafts |
| 3 | Methods | **SKELETON BELOW** | Current Section 3 (streamlined) |
| 4 | Implementation Roadmap | ✅ DONE | section5_REVISED_v3.md |
| 5 | Prototype & Case Study | **SKELETON BELOW** | Current Sections 4+6 merged |
| 6 | Future Work & Summary | **SKELETON BELOW** | Current Section 7 + new |
| - | References | Keep as-is | Current Section 8 |
| A | Appendix: Literature Context | **SKELETON BELOW** | Moved from Section 3 |

---

# SECTION 3: METHODS (Streamlined)

## Skeleton Structure

```
3.0 Methods

    [Introduction paragraph: This section details the methods organized by the 
    three pillars. For extended literature context on surrogate model 
    architectures, see Appendix A.]

3.1 Governance Methods (Pillar A)
    
    [KEEP ALL EXISTING CONTENT from current 3.1]
    
    3.1.1 Regulatory Alignment and Quality Assurance Foundations
          - CERCLA, DOE O 414.1D, NQA-1 alignment
          - Surrogate models as controlled analytical software
    
    3.1.2 Model Usage Scope and Decision Context
          - Screening-level analyses vs. regulatory decisions
          - Physics-based models remain authoritative
    
    3.1.3 Acceptance Criteria and Recalibration Triggers
          - Quantitative performance metrics
          - Uncertainty calibration requirements
          - Trigger thresholds
    
    3.1.4 Operational Monitoring and Review Schedule
          - Automated diagnostics frequency
          - Quarterly decision points
    
    3.1.5 Transparency, Auditability, and Configuration Control
          - Version tracking
          - Governance records
          - Rollback procedures
    
    3.1.6 Summary
    
    **Workflow Integration:** Steps 3 (DECIDE) and 7 (DEPLOY)

3.2 Modeling Engine Methods (Pillar B)
    
    3.2.1 Site Challenges and Modeling Needs
          [KEEP existing content]
          - Heterogeneity, back-diffusion, density effects
          - Engineered operations representation
    
    3.2.2 Physics-Based Numerical Models
          [KEEP existing content]
          - MODFLOW, PFLOTRAN, TOUGH2, etc.
          - Computational constraints motivating surrogates
    
    3.2.3 Surrogate Model Landscape
          [STREAMLINED - detailed literature moved to Appendix A]
          
          [New intro paragraph:]
          The framework supports multiple surrogate model families, each suited 
          to different prediction tasks. For detailed literature context and 
          architecture comparisons, see Appendix A.
          
          **Convolutional Encoder-Decoder Models** (e.g., U-Net, ResNet)
          - High-resolution spatial field prediction
          - Local patterns and interfaces
          - 1-2 sentences only
          
          **Operator-Learning Models** (e.g., FNO, U-FNO, DeepONet)
          - Resolution-invariant surrogates
          - Generalize across boundary conditions
          - 1-2 sentences only
          
          **Sequence Models** (e.g., LSTM, GRU, Transformers)
          - Low-dimensional time series outputs
          - Breakthrough curves, well responses
          - 1-2 sentences only
          
          **Generative Models** (e.g., VAEs, diffusion models)
          - Ensemble sampling
          - Probabilistic inversion
          - 1-2 sentences only
          
          **Regression Surrogates** (e.g., Gaussian processes, shallow ANNs)
          - Low-dimensional scalar metrics
          - Interpretability and small-data robustness
          - 1-2 sentences only
          
          [Closing paragraph:]
          The choice of surrogate family depends on the prediction task, data 
          availability, and decision-support requirements. Section 4 
          (Implementation Roadmap) describes how these surrogates integrate 
          with the recalibration workflow.
    
    3.2.4 General Surrogate Model Training Setup
          [KEEP existing content]
          - Data splits, augmentation, convergence
          - Normalization, early stopping
          - Runtime reporting
    
    **Workflow Integration:** Steps 5 (UPDATE) and 6 (CALIBRATE)

3.3 Recalibration Mechanism Methods (Pillar C)
    
    [KEEP ALL EXISTING CONTENT from current 3.3]
    
    3.3.1 Uncertainty Quantification of Surrogate Models
          - MC-Dropout, deep ensembles, conformal prediction
          - EnKF, particle filters for DA
          - Sequential Bayesian inference
          - Hybrid integration strategy
    
    3.3.2 Trigger Logic
          - Tipping point-inspired resilience metrics
          - Performance and uncertainty-based metrics
          - Distributional and representation-level drift detection
          - Probabilistic integration and decision logic
          - Table 1: Exemplary Regime Drift Diagnostics
          - Three-phase workflow for drift monitoring
    
    3.3.3 Continual Learning
          - EWC, replay buffers (70-75%)
          - Layer freezing strategy
          - Fine-tuning workflow steps
    
    3.3.4 Active Learning
          - Uncertainty sampling, error-based sampling
          - Diversity constraints
          - Batch size 6-10 recommendations
    
    3.3.5 Multi-fidelity Data Fusion
          - Co-Kriging, neural discrepancy models
          - Pre-training on low-fidelity
          - Structured workflow steps
    
    3.3.6 Fully Retrain
          - When full retraining is needed
          - Structured retraining workflow
    
    **Workflow Integration:** All steps, especially Steps 1-3 (monitoring) 
    and Steps 4-6 (update)
```

---

# SECTION 5: PROTOTYPE & CASE STUDY (Merged)

## Skeleton Structure

```
5.0 Prototype & Case Study

    [Introduction paragraph: This section presents the validation framework, 
    prototype implementations, and case study design that demonstrate the 
    recalibration framework in practice.]

5.1 Validation Framework
    
    [Source: Current Section 4 - Validation & Metrics]
    
    5.1.1 Performance Metrics
          - Accuracy metrics (RMSE, MAE, bias)
          - Contaminant mass reduction
          - Plume extent prediction accuracy
          - Drawdown head error
    
    5.1.2 Uncertainty Metrics
          - Predictive interval coverage
          - Calibration of uncertainty estimates
          - Confidence in capture zones
    
    5.1.3 Drift Detection Metrics
          - Residual thresholds
          - Distributional drift indicators
          - Composite drift index
    
    5.1.4 Governance Compliance Metrics
          - Acceptance criteria alignment
          - Audit trail completeness
          - Regulatory documentation
    
    5.1.5 Acceptance Thresholds
          - Example: ≥90% contaminant mass removed within 10 years
          - Example: 95% prediction interval coverage ≥90%
          - Example: Monitoring network cost reduction ≥30%

5.2 Prototype Implementations
    
    [Source: Current Section 6.1 and 6.2]
    
    5.2.1 U-FNO Surrogate for 2D Cross-Section Transport
          
          **PFLOTRAN Baseline Model**
          - 84m × 4m domain, 28 × 40 grid
          - Variably saturated Richards equation
          - Time-varying boundary conditions
          - Heterogeneous permeability/porosity fields
          
          **U-FNO Architecture and Training**
          - Fourier layers + U-Net path
          - ~126 million parameters
          - Learning rate 0.001 with decay
          - 200 epochs, batch size 4
          - Separate networks for pressure and concentration
          
          **Workflow Integration**
          - How U-FNO supports Steps 1-3 (monitoring)
          - How U-FNO enables rapid scenario testing
    
    5.2.2 U-Net Surrogate for 2D Pump-and-Treat Plume Prediction
          
          **Training Data Generation**
          - 128 × 100 mesh, 1m × 1m cells
          - 1-5 extraction wells
          - 10,000 physics simulation runs
          - Plume snapshots at 0, 1, 2, 3, 4 days
          
          **Architectural Modifications**
          - Thiem equation drawdown map as input
          - Strided convolutions (not max pooling)
          - Leaky Tanh bounded activation
          - Skip connections for sharp fronts
          
          **Training Workflow**
          - 70/15/15 train/validate/test split
          - MSE loss, Adam optimizer
          - Early stopping
          - Autoregressive rollout for multi-step prediction
          
          **Workflow Integration**
          - How U-Net supports P&T scenario screening
          - Integration with recalibration loop

5.3 Case Study Design
    
    [New content - synthesize from existing material]
    
    5.3.1 Hydrological Modeling Scenario
          - Site characteristics (synthetic or based on EM site)
          - Contaminant type and initial conditions
          - Remediation system configuration
    
    5.3.2 Data Sources and Simulation Setup
          - Physics model configuration
          - Training data generation strategy
          - Monitoring data simulation
    
    5.3.3 Recalibration Demonstration
          - Drift injection scenario
          - Trigger activation
          - Targeted physics runs
          - Fine-tuning execution
          - Performance comparison (before/after)

5.4 Evaluation Plan
    
    [New content]
    
    5.4.1 Baseline Comparison
          - Physics-only vs. surrogate-only vs. hybrid
          - Computational cost comparison
          - Accuracy comparison
    
    5.4.2 Recalibration Effectiveness
          - Error reduction after update
          - Uncertainty calibration improvement
          - Time to detect drift
    
    5.4.3 Computational Efficiency
          - Speedup factors (10³-10⁴×)
          - Cost of targeted physics runs
          - Total computational budget

5.5 Development Timeline
    
    [Source: Current Section 6 schedule content]
    
    - Phase 1: Prototype demonstration
    - Phase 2: Integrated framework
    - Phase 3: Operational system
```

---

# SECTION 6: FUTURE WORK & SUMMARY

## Skeleton Structure

```
6.0 Future Work & Summary

    [Introduction paragraph: This section outlines the research roadmap, 
    expected impact, and key conclusions of the recalibration framework.]

6.1 Research Roadmap
    
    [Source: Current Section 7 - Roadmap and Impact]
    
    6.1.1 Short-Term Goals
          - Complete prototype demonstration
          - Validate recalibration loop
          - Document framework design package
    
    6.1.2 Medium-Term Goals
          - Extend to additional constituents (CTET, TCE)
          - Apply to real EM site data
          - Integrate with operational workflows
    
    6.1.3 Long-Term Vision
          - Multi-site deployment
          - Digital twin integration
          - Autonomous recalibration systems

6.2 Expected Impact
    
    6.2.1 Scientific Contributions
          - Novel integration of UQ, active learning, continual learning
          - Framework for adaptive surrogate maintenance
          - Methodology for drift detection in environmental models
    
    6.2.2 Operational Benefits
          - Faster scenario iteration (10³-10⁴× speedup)
          - Reduced unnecessary simulator runs
          - Explainable updates for regulator confidence
          - Maintained accuracy over multi-year timelines
    
    6.2.3 Broader Applications
          - Other DOE EM sites
          - Climate resilience applications
          - General scientific surrogate maintenance

6.3 Limitations and Open Questions
    
    [Cross-reference to Section 4.6 Open Design Questions]
    
    6.3.1 Current Framework Limitations
          - Dependence on physics model quality
          - Computational requirements for ensemble methods
          - Generalization across site types
    
    6.3.2 Areas Requiring Further Research
          - Optimal trigger threshold calibration
          - Multi-fidelity fusion strategies
          - Transfer learning across sites
    
    6.3.3 Governance Considerations
          - Regulatory acceptance pathway
          - Long-term maintenance requirements
          - Documentation standards evolution

6.4 Conclusion
    
    [New content - synthesis]
    
    6.4.1 Summary of Framework Contributions
          - Three-pillar architecture (Governance, Modeling Engines, 
            Recalibration Mechanisms)
          - Seven-step, two-phase workflow
          - Integration of UQ, active learning, continual learning
    
    6.4.2 Key Takeaways
          - Surrogates require systematic maintenance
          - Physics models remain authoritative
          - Governance ensures regulatory confidence
          - Adaptive strategies outperform static approaches
    
    6.4.3 Path Forward
          - Prototype validation
          - Stakeholder engagement
          - Operational deployment roadmap
```

---

# APPENDIX A: SURROGATE MODEL LITERATURE CONTEXT

## Skeleton Structure

```
Appendix A: Surrogate Model Literature Context

    [Introduction: This appendix provides detailed literature context for 
    surrogate model architectures discussed in Section 3.2.3. The content 
    supports method selection decisions but is not required for understanding 
    the core framework.]

A.1 Literature Review Methodology
    
    [Source: Current Section 3.2.3, lines 535-545]
    
    A.1.1 Search Strategy
          - Web of Science Core Collection
          - Topic search combining groundwater/subsurface keywords with 
            surrogate-modeling terms
          - Period: 2005-2026
    
    A.1.2 Screening Criteria
          - Relevance to subsurface flow/transport
          - DOE-relevant decision workflows
          - Coverage across method families
    
    A.1.3 Classification Approach
          - Five primary method families
          - Single primary label per paper
          - Application and domain categorization

A.2 Surrogate Model Families: Detailed Review
    
    A.2.1 Convolutional Encoder-Decoder Models
          
          [Source: Current Section 3.2.3, CNN/U-Net detailed content]
          
          **Architecture Overview**
          - Treat spatial fields as images
          - Learn direct input-output mappings
          - Preserve interfaces and sharp fronts
          
          **Key Papers**
          - Taccari et al. (2022): Attention U-Net for steady-state heads
          - Mo et al. (2019): Image-to-image regression for multiphase flow
          - Jiang et al. (2021): AR-ResUNet for dynamic transport
          - Lauzon (2024): U-Net in stochastic inverse framework
          
          **Strengths and Limitations**
          - Strong for high-resolution spatial fields
          - Requires autoregressive strategy for time-dependent problems
    
    A.2.2 Operator-Learning Models
          
          [Source: Current Section 3.2.3, FNO/U-FNO detailed content]
          
          **Architecture Overview**
          - Learn solution operator in Fourier space
          - Resolution-invariant
          - U-FNO adds U-Net path for local features
          
          **Key Papers**
          - Li et al. (2020): Original FNO
          - Wen et al. (2022): U-FNO for CO₂-water systems
          - Taccari et al. (2024): DeepONet for confined aquifer flow
          - Jiang et al. (2025): GeoFUSE framework
          - Wang et al. (2022): Physics-informed U-FNO
          
          **Strengths and Limitations**
          - Site-agnostic, reusable
          - Higher computational cost for training
    
    A.2.3 Sequence Models
          
          [Source: Current Section 3.2.3, sequence models detailed content]
          
          **Architecture Overview**
          - Focus on low-dimensional time series
          - Capture long-range temporal dependencies
          
          **Key Papers**
          - Chen et al. (2021): GRU for groundwater levels
          - Xie and Zhang (2024): STA-GRU with attention
          - Anshuman and Eldho (2023): Encoder-decoder LSTM
          - Li et al. (2025): DSCNN-GRU hybrid
          
          **Strengths and Limitations**
          - Efficient for time series at limited locations
          - Not suited for full spatial field prediction
    
    A.2.4 Generative Models
          
          [Source: Current Section 3.2.3, generative models detailed content]
          
          **Architecture Overview**
          - Sample ensembles of plausible states
          - Support probabilistic inversion
          
          **Key Papers**
          - Graham and Chen (2020): VAEs/GANs for CO₂ storage
          - Miele and Linde (2025): Diffusion models for subsurface
          - Wang et al. (2025c): Pretrained diffusion for porous media
          - Wang et al. (2025b): Conditional diffusion for CO₂ plumes
          
          **Strengths and Limitations**
          - Excellent for UQ and ensemble generation
          - Higher computational cost
    
    A.2.5 Regression and Classical Surrogates
          
          [Source: Current Section 3.2.3, regression detailed content]
          
          **Architecture Overview**
          - Gaussian processes, Kriging, shallow ANNs
          - Low-dimensional input-output mappings
          
          **Key Papers**
          - Asher et al. (2015): Review of groundwater surrogates
          - Siade et al. (2020): GP for groundwater allocation
          - Shams et al. (2021): GP for DNAPL remediation
          - Marrel and Iooss (2024): GP construction advances
          
          **Strengths and Limitations**
          - Interpretable, uncertainty estimates
          - Limited to low-dimensional problems
    
    A.2.6 Structured Domain Surrogates
          
          [Source: Current Section 3.2.3, structured domain content]
          
          **Architecture Overview**
          - POD, DMD, Koopman operators
          - Graph/mesh neural networks
          
          **Key Papers**
          - Schmid (2010): Dynamic Mode Decomposition
          - Mezić (2013): Koopman operator analysis
          - Pfaff et al. (2020): Learning mesh-based simulation
          - Sanchez-Gonzalez et al. (2020): Graph networks for physics
          
          **Strengths and Limitations**
          - Learn evolution operators
          - Less prevalent in groundwater applications

A.3 Literature Analysis Figures
    
    A.3.1 Publication Trends
          - Figure A1: Article publication growth (2005-2025)
          - [Current Figure 1]
    
    A.3.2 Method Evolution
          - Figure A2: Method family breakdown by year
          - [Current Figure 2]
    
    A.3.3 Application Heatmap
          - Figure A3: Papers by method family vs. application
          - Figure A4: Papers by method family vs. project domain
          - [Current Figure 4]

A.4 Paper Review Tables
    
    [KEEP existing Appendix content]
    
    - Table A1: Machine Learning Based Surrogates Paper Review
    - Table A2: Curated set of representative publications
```

---

## Summary: What Changes vs. What Stays

### Content That STAYS AS-IS
- Section 1 (Introduction)
- Section 2 (Framework Overview) - already revised
- Section 3.1 (Governance) - all content
- Section 3.2.1, 3.2.2, 3.2.4 - all content
- Section 3.3 (Recalibration Mechanisms) - all content
- Section 4 (Implementation Roadmap) - already revised as v3
- References
- Existing Appendix tables (A1, A2)

### Content That MOVES
- Section 3.2.3 detailed literature → Appendix A.2
- Section 3.2.3 figures → Appendix A.3

### Content That MERGES
- Current Section 4 (Validation) + Current Section 6 (Prototype) → New Section 5

### Content That EXPANDS
- Current Section 7 (Roadmap) → New Section 6 (with new conclusion)

### New Content Needed
- Section 5.3 (Case Study Design) - new synthesis
- Section 5.4 (Evaluation Plan) - new content
- Section 6.3 (Limitations) - new content
- Section 6.4 (Conclusion) - new synthesis

---

## Implementation Order (Recommended)

1. **Section 3 Streamlining** - Extract literature to Appendix A
2. **Appendix A Creation** - Organize moved content
3. **Section 5 Merge** - Combine Sections 4+6, add new content
4. **Section 6 Creation** - Expand Section 7, add conclusion
5. **Final Assembly** - Renumber, update cross-references

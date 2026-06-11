# 5.0 Implementation Roadmap

This section describes how the three-pillar framework (Section 2.1) and seven-step workflow (Section 2.2) translate into an operational system. Rather than prescribing specific software architecture, this section outlines the **capabilities required**, the **methods that support them** (drawing from Section 3), and a **phased development approach** appropriate for DOE environmental management applications.

The implementation must satisfy two demands: (1) support the scientific workflow of monitoring, detecting drift, and executing recalibration; and (2) meet DOE governance requirements for traceability, reproducibility, and quality assurance.

---

## 5.1 Framework Design Principles

### 5.1.1 Guiding Principles

The implementation follows three guiding principles derived from the framework:

1. **Workflow-Centric Organization**: Operational capabilities map directly to the two workflow phases (Continuous Monitoring and Triggered Response), ensuring that implementation supports the recalibration cycle defined in Section 2.2.

2. **Pillar Awareness**: Each capability draws on one or more management domains—Pillar A (Governance), Pillar B (Modeling Engines), or Pillar C (Recalibration Mechanisms)—as defined in Section 2.1.

3. **Governance Integration**: Pillar A requirements (audit trails, acceptance criteria, human decision points) are embedded throughout the workflow, not isolated as a separate concern.

### 5.1.2 Relationship to Section 3 Methods

The methods detailed in Section 3 provide the technical foundation for implementation:

| Workflow Phase | Capability Needed | Section 3 Methods |
|----------------|-------------------|-------------------|
| Phase 1: Monitoring | Uncertainty quantification | MC-Dropout, deep ensembles, conformal prediction (3.3.1) |
| Phase 1: Detection | Drift identification | KS test, composite drift index, resilience metrics (3.3.2) |
| Phase 1: Decision | Governance thresholds | Acceptance criteria, trigger policies (3.1.3) |
| Phase 2: Preparation | Scenario selection | Uncertainty sampling, error-based sampling (3.3.4) |
| Phase 2: Update | Model fine-tuning | EWC, replay buffers, layer freezing (3.3.3) |
| Phase 2: Calibration | UQ adjustment | Coverage evaluation, interval calibration (3.3.1) |
| Phase 2: Deployment | Version control | Configuration management, audit trails (3.1.5) |

---

## 5.2 Phase 1 Capabilities: Continuous Monitoring (Steps 1-3)

Phase 1 runs continuously during site operations, implementing Steps 1-3 of the workflow (MONITOR → DETECT → DECIDE). These capabilities serve primarily **Pillar C** for technical diagnostics and **Pillar A** for governance oversight.

### 5.2.1 Performance Monitoring (Step 1: MONITOR)

**Purpose**: Continuously compare surrogate predictions against monitoring data to track accuracy and uncertainty.

**Required Capabilities**:
- Compute prediction-observation residuals at monitoring wells and compliance points
- Track spatial and temporal patterns in residuals
- Maintain rolling statistics (e.g., 30-day, 90-day windows) for baseline comparison
- Ingest and validate new observations from field sensors and laboratory results

**Section 3 Methods Applied**:
- **UQ computation** using MC-Dropout or deep ensembles (Section 3.3.1) to generate predictive uncertainty estimates
- **Calibration tracking** to verify that stated uncertainty intervals match empirical coverage (e.g., 95% intervals should contain true values ~95% of the time)

**Governance Integration** (Pillar A):
- All metrics stored with full provenance for audit trails
- Summary reports generated for periodic governance review per Section 3.1.4 monitoring schedule

### 5.2.2 Drift Detection (Step 2: DETECT)

**Purpose**: Identify when surrogate performance has degraded sufficiently to warrant recalibration.

**Required Capabilities**:
- Evaluate multiple drift indicators against predefined thresholds
- Integrate signals into composite assessment
- Distinguish transient anomalies from persistent degradation

**Section 3 Methods Applied** (from Section 3.3.2 Trigger Logic):

| Metric Category | Specific Methods | Threshold Examples |
|-----------------|------------------|-------------------|
| Performance-based | RMSE, bias, threshold exceedance | Residuals >2× rolling standard deviation |
| Uncertainty-based | Predictive variance inflation | Variance >150% of baseline |
| Distributional | Kolmogorov-Smirnov test | p-value <0.01 indicates significant drift |
| Resilience | Rolling variance, lag-1 autocorrelation | Sustained increase over 60-90 days |
| Composite | Drift index aggregation | Boolean or score-based gating |

**Persistence Filtering**: Per Section 3.3.2, drift signals must persist for a minimum duration (e.g., 60-90 days) before triggering action, reducing false positives from transient anomalies.

### 5.2.3 Governance Decision (Step 3: DECIDE)

**Purpose**: Present evidence for human review and obtain authorization before proceeding to Phase 2.

**Required Capabilities**:
- Synthesize diagnostic results into actionable summary
- Present historical context (previous recalibration events, outcomes)
- Document decision rationale for regulatory transparency

**Governance Integration** (Pillar A):
- **Human decision point**: The DECIDE step requires explicit human authorization before triggering Phase 2. This aligns with DOE quality assurance requirements (Section 3.1) that surrogate updates be justified, proportional, and documented.
- **Decision options**: Approve update, defer pending additional evidence, or reject with justification

**Trigger State Logic**:
The framework maintains operational state to guide decisions:
- **OK**: Surrogate meets acceptance criteria; continue normal monitoring
- **WARNING**: Drift detected; intensify monitoring; accumulate evidence
- **UPDATE**: Governance approved; proceed to Phase 2
- **ESCALATE**: Update failed validation; surrogate withdrawn; revert to physics-only mode

---

## 5.3 Phase 2 Capabilities: Triggered Response (Steps 4-7)

Phase 2 activates only when DECIDE authorizes an update, implementing Steps 4-7 of the workflow (PREPARE → UPDATE → CALIBRATE → DEPLOY). These capabilities serve primarily **Pillar C** and **Pillar B**.

### 5.3.1 Data Preparation (Step 4: PREPARE)

**Purpose**: Assemble training data for surrogate update, potentially including new physics simulations.

**Two Pathways** (per Section 2.2):
1. **Observation-driven**: When new field data alone is sufficient, proceed directly to UPDATE
2. **Simulation-driven**: When new physics runs are needed, use active learning to select scenarios

**Section 3 Methods Applied** (from Section 3.3.4 Active Learning):
- **Uncertainty sampling**: Prioritize scenarios where surrogate has high predictive variance (Settles, 2009)
- **Error-based sampling**: Target regions with large or persistent residuals (Cohn et al., 1996)
- **Diversity constraints**: Ensure selected scenarios span hydraulic gradients, hydrostratigraphic units, and forcing conditions
- **Batch size**: Select 6-10 high-value simulations per update cycle (Vesselinov et al., 2017)

**Physics Model Interface** (Pillar B):
- Execute targeted simulations using site physics models (PFLOTRAN, MODFLOW, STOMP, etc.)
- Archive outputs with full provenance for reproducibility

### 5.3.2 Model Update (Step 5: UPDATE)

**Purpose**: Fine-tune surrogate weights using new data while preserving previously learned knowledge.

**Section 3 Methods Applied** (from Section 3.3.3 Continual Learning):

| Method | Purpose | Implementation Guidance |
|--------|---------|------------------------|
| **Replay buffers** | Prevent catastrophic forgetting | Include 70-75% historical samples in training batch (De Lange et al., 2021) |
| **EWC regularization** | Protect important weights | Penalize deviations from weights influential in previous training (Kirkpatrick et al., 2017) |
| **Layer freezing** | Preserve structural representations | Freeze early encoder layers; update later layers with small learning rate |
| **Early stopping** | Prevent overfitting | Stop when validation performance plateaus |

**Multi-Fidelity Integration** (from Section 3.3.5):
When available, combine low-fidelity simulations (broad coverage) with high-fidelity runs (local accuracy) using co-Kriging or neural discrepancy models (Kennedy & O'Hagan, 2000; Perdikaris et al., 2017).

### 5.3.3 Uncertainty Recalibration (Step 6: CALIBRATE)

**Purpose**: Ensure updated surrogate's uncertainty estimates remain well-calibrated.

**Section 3 Methods Applied** (from Section 3.3.1 UQ):
- **Coverage evaluation**: Test whether uncertainty intervals achieve target coverage on held-out data
- **Calibration adjustment**: If intervals are too narrow (under-coverage) or too wide (over-coverage), adjust scaling factors
- **Method-specific procedures**:
  - MC-Dropout: Adjust dropout rate or number of forward passes
  - Deep Ensembles: Retrain ensemble members on updated data
  - Conformal Prediction: Recompute nonconformity scores on calibration set

**Validation Requirement**: Calibrated uncertainty must meet acceptance criteria (Section 3.1.3) before proceeding to deployment.

### 5.3.4 Deployment and Governance (Step 7: DEPLOY)

**Purpose**: Validate updated surrogate against acceptance criteria and deploy with full documentation.

**Required Capabilities**:
- Verify acceptance criteria from Section 3.1.3 (accuracy metrics, uncertainty coverage, spatial/temporal consistency)
- Maintain version control for surrogate models
- Generate governance documentation package
- Handle failed validations through rollback procedures

**Governance Integration** (Pillar A, from Section 3.1.5):
- **Configuration control**: Track all surrogate versions with training data, assumptions, and validation results
- **Audit trail**: Document trigger rationale, data sources, evaluation results, and verification outcomes
- **Rollback definition**: Per Section 3.1.5, rollback means withdrawal of surrogate from operational use and escalation to full retraining—not reversion to a previous version (since the prior version has already been flagged as degraded)

---

## 5.4 Infrastructure Considerations

### 5.4.1 Data Management

The framework requires data management capabilities that support all three pillars:
- **Observations**: Field measurements, laboratory results, sensor data
- **Simulations**: Physics model inputs and outputs with full provenance
- **Models**: Surrogate weights, training configurations, validation results
- **Governance**: Decision logs, audit trails, acceptance criteria records

### 5.4.2 Computational Resources

- **Surrogate inference**: Typically runs on standard computing resources (CPU or single GPU)
- **Physics simulations**: May require HPC resources depending on model complexity
- **Training/fine-tuning**: GPU resources beneficial but not always required for incremental updates

### 5.4.3 Interoperability

The framework should interface with:
- Existing site physics models (PFLOTRAN, MODFLOW, STOMP, TOUGH2, etc.)
- Site monitoring databases and sensor networks
- DOE quality assurance and configuration management systems

---

## 5.5 Development Phases

Implementation proceeds through three phases, progressively building capability and confidence:

### Phase 1: Prototype Demonstration

**Objective**: Demonstrate one complete recalibration cycle on a synthetic or simplified test case.

**Scope**:
- Single surrogate architecture (e.g., U-Net or U-FNO from Section 6)
- Basic UQ using MC-Dropout or deep ensembles
- Simple drift detection (threshold-based)
- Manual governance decisions
- Documented recalibration event

**Success Criteria**: Complete MONITOR → DETECT → DECIDE → PREPARE → UPDATE → CALIBRATE → DEPLOY cycle with documented performance improvement.

### Phase 2: Integrated Framework

**Objective**: Integrate all framework components with realistic site data.

**Scope**:
- Multiple surrogate options
- Full trigger logic from Section 3.3.2 (composite drift index)
- Continual learning with replay buffers and EWC
- Active learning for scenario selection
- Governance dashboard for decision support
- Automated monitoring with human-in-the-loop decisions

**Success Criteria**: Framework operates on representative site data with governance-compliant documentation.

### Phase 3: Operational System

**Objective**: Deploy framework for operational use at DOE EM sites.

**Scope**:
- Production-quality implementation
- Integration with site monitoring systems
- Full regulatory documentation
- Training materials for site operators
- Maintenance and support procedures

**Success Criteria**: Framework accepted for operational use under DOE quality assurance requirements.

---

## 5.6 Open Design Questions

Several design decisions remain for site-specific implementation:

1. **Surrogate architecture selection**: Which architecture(s) best fit site-specific prediction needs? (See Section 3.2 for options)

2. **UQ method selection**: MC-Dropout vs. deep ensembles vs. conformal prediction—tradeoffs between computational cost and calibration quality

3. **Trigger threshold calibration**: Site-specific thresholds for drift detection metrics require tuning based on historical variability

4. **Update frequency**: Balance between responsiveness (frequent updates) and stability (conservative updates)

5. **Multi-fidelity integration**: When and how to incorporate low-fidelity simulations alongside high-fidelity runs

6. **Governance workflow**: Site-specific approval processes and documentation requirements

These questions will be addressed during Phase 1 prototyping and refined through operational experience.

---

## 5.7 Summary

This implementation roadmap translates the three-pillar framework and seven-step workflow into operational capabilities. Key points:

1. **Workflow-centric design**: Capabilities organized around the two workflow phases (Continuous Monitoring and Triggered Response)

2. **Method grounding**: All technical capabilities draw from methods detailed in Section 3 (UQ, trigger logic, continual learning, active learning, multi-fidelity)

3. **Governance integration**: Pillar A requirements embedded throughout, with explicit human decision points

4. **Phased development**: Progressive build-up from prototype demonstration to operational system

5. **Flexibility**: Framework accommodates site-specific choices while maintaining consistent workflow and governance structure

The framework enables adaptive surrogate management that maintains prediction accuracy over multi-year remediation timelines while meeting DOE quality assurance and regulatory requirements.

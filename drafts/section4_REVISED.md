# 4. Implementation Roadmap

This section describes how the three-pillar framework (Section 2.1) and seven-step workflow (Section 2.2) translate into an operational system. Rather than prescribing specific software architecture, this section outlines the capabilities required, the methods that support them (drawing from Section 3), and a phased development approach appropriate for DOE environmental management applications.

The implementation must satisfy two demands: first, support the scientific workflow of monitoring, detecting drift, and executing recalibration; and second, meet DOE governance requirements for traceability, reproducibility, and quality assurance.

## 4.1 Framework Design Principles

### 4.1.1 Guiding Principles

The implementation follows three guiding principles derived from the framework. The first principle is workflow-centric organization, where operational capabilities map directly to the two workflow phases (Continuous Monitoring and Triggered Response), ensuring that implementation supports the recalibration cycle defined in Section 2.2. The second principle is pillar awareness, where each capability draws on one or more management domains—Pillar A (Governance), Pillar B (Modeling Engines), or Pillar C (Recalibration Mechanisms)—as defined in Section 2.1. The third principle is governance integration, where Pillar A requirements including audit trails, acceptance criteria, and human decision points are embedded throughout the workflow rather than isolated as a separate concern.

### 4.1.2 Relationship to Section 3 Methods

The methods detailed in Section 3 provide the technical foundation for implementation. Table 4.1 summarizes the mapping between workflow phases, required capabilities, and the Section 3 methods that support them.

**Table 4.1: Workflow Capabilities and Supporting Methods**

| Workflow Phase | Capability Needed | Section 3 Methods |
|----------------|-------------------|-------------------|
| Phase 1: Monitoring | Uncertainty quantification | MC-Dropout, deep ensembles, conformal prediction (3.3.1) |
| Phase 1: Detection | Drift identification | KS test, composite drift index, resilience metrics (3.3.2) |
| Phase 1: Decision | Governance thresholds | Acceptance criteria, trigger policies (3.1.3) |
| Phase 2: Preparation | Scenario selection | Uncertainty sampling, error-based sampling (3.3.4) |
| Phase 2: Update | Model fine-tuning | EWC, replay buffers, layer freezing (3.3.3) |
| Phase 2: Calibration | UQ adjustment | Coverage evaluation, interval calibration (3.3.1) |
| Phase 2: Deployment | Version control | Configuration management, audit trails (3.1.5) |

## 4.2 Phase 1 Capabilities: Continuous Monitoring (Steps 1-3)

Phase 1 runs continuously during site operations, implementing Steps 1-3 of the workflow (MONITOR → DETECT → DECIDE). These capabilities serve primarily Pillar C for technical diagnostics and Pillar A for governance oversight.

### 4.2.1 Performance Monitoring (Step 1: MONITOR)

The purpose of performance monitoring is to continuously compare surrogate predictions against monitoring data to track accuracy and uncertainty. Required capabilities include computing prediction-observation residuals at monitoring wells and compliance points, tracking spatial and temporal patterns in residuals, maintaining rolling statistics (such as 30-day and 90-day windows) for baseline comparison, and ingesting and validating new observations from field sensors and laboratory results.

Section 3 methods applied include UQ computation using MC-Dropout or deep ensembles (Section 3.3.1) to generate predictive uncertainty estimates, and calibration tracking to verify that stated uncertainty intervals match empirical coverage (for example, 95% intervals should contain true values approximately 95% of the time).

Governance integration under Pillar A requires that all metrics be stored with full provenance for audit trails, and that summary reports be generated for periodic governance review per Section 3.1.4 monitoring schedule.

### 4.2.2 Drift Detection (Step 2: DETECT)

The purpose of drift detection is to identify when surrogate performance has degraded sufficiently to warrant recalibration. Required capabilities include evaluating multiple drift indicators against predefined thresholds, integrating signals into composite assessment, and distinguishing transient anomalies from persistent degradation.

Section 3 methods applied from Section 3.3.2 Trigger Logic include performance-based metrics (RMSE, bias, threshold exceedance with residuals exceeding 2× rolling standard deviation), uncertainty-based metrics (predictive variance inflation exceeding 150% of baseline), distributional metrics (Kolmogorov-Smirnov test with p-value below 0.01 indicating significant drift), resilience metrics (rolling variance and lag-1 autocorrelation showing sustained increase over 60-90 days), and composite metrics (drift index aggregation using Boolean or score-based gating).

Persistence filtering per Section 3.3.2 requires that drift signals persist for a minimum duration (typically 60-90 days) before triggering action, reducing false positives from transient anomalies.

### 4.2.3 Governance Decision (Step 3: DECIDE)

The purpose of the governance decision step is to present evidence for human review and obtain authorization before proceeding to Phase 2. Required capabilities include synthesizing diagnostic results into actionable summary, presenting historical context (previous recalibration events and outcomes), and documenting decision rationale for regulatory transparency.

Governance integration under Pillar A establishes that the DECIDE step requires explicit human authorization before triggering Phase 2. This aligns with DOE quality assurance requirements (Section 3.1) that surrogate updates be justified, proportional, and documented. Decision options include approving the update, deferring pending additional evidence, or rejecting with justification.

The framework maintains operational state through trigger state logic to guide decisions. The OK state indicates the surrogate meets acceptance criteria and normal monitoring continues. The WARNING state indicates drift has been detected, monitoring should intensify, and evidence should accumulate. The UPDATE state indicates governance has approved proceeding to Phase 2. The ESCALATE state indicates the update failed validation, the surrogate is withdrawn, and operations revert to physics-only mode.

## 4.3 Phase 2 Capabilities: Triggered Response (Steps 4-7)

Phase 2 activates only when DECIDE authorizes an update, implementing Steps 4-7 of the workflow (PREPARE → UPDATE → CALIBRATE → DEPLOY). These capabilities serve primarily Pillar C and Pillar B.

### 4.3.1 Data Preparation (Step 4: PREPARE)

The purpose of data preparation is to assemble training data for surrogate update, potentially including new physics simulations. Two pathways exist per Section 2.2: the observation-driven pathway proceeds directly to UPDATE when new field data alone is sufficient, while the simulation-driven pathway uses active learning to select scenarios when new physics runs are needed.

Section 3 methods applied from Section 3.3.4 Active Learning include uncertainty sampling to prioritize scenarios where the surrogate has high predictive variance, error-based sampling to target regions with large or persistent residuals, diversity constraints to ensure selected scenarios span hydraulic gradients, hydrostratigraphic units, and forcing conditions, and batch sizing to select 6-10 high-value simulations per update cycle.

The physics model interface under Pillar B executes targeted simulations using site physics models (PFLOTRAN, MODFLOW, STOMP, or similar) and archives outputs with full provenance for reproducibility.

### 4.3.2 Model Update (Step 5: UPDATE)

The purpose of model update is to fine-tune surrogate weights using new data while preserving previously learned knowledge. Section 3 methods applied from Section 3.3.3 Continual Learning include replay buffers to prevent catastrophic forgetting by including 70-75% historical samples in training batches, EWC regularization to protect important weights by penalizing deviations from weights influential in previous training, layer freezing to preserve structural representations by freezing early encoder layers while updating later layers with small learning rate, and early stopping to prevent overfitting by stopping when validation performance plateaus.

Multi-fidelity integration from Section 3.3.5 combines low-fidelity simulations (broad coverage) with high-fidelity runs (local accuracy) using co-Kriging or neural discrepancy models when available.

### 4.3.3 Uncertainty Recalibration (Step 6: CALIBRATE)

The purpose of uncertainty recalibration is to ensure the updated surrogate's uncertainty estimates remain well-calibrated. Section 3 methods applied from Section 3.3.1 UQ include coverage evaluation to test whether uncertainty intervals achieve target coverage on held-out data, and calibration adjustment to modify scaling factors if intervals are too narrow (under-coverage) or too wide (over-coverage).

Method-specific procedures include adjusting dropout rate or number of forward passes for MC-Dropout, retraining ensemble members on updated data for deep ensembles, and recomputing nonconformity scores on calibration set for conformal prediction. The validation requirement specifies that calibrated uncertainty must meet acceptance criteria (Section 3.1.3) before proceeding to deployment.

### 4.3.4 Deployment and Governance (Step 7: DEPLOY)

The purpose of deployment is to validate the updated surrogate against acceptance criteria and deploy with full documentation. Required capabilities include verifying acceptance criteria from Section 3.1.3 (accuracy metrics, uncertainty coverage, spatial/temporal consistency), maintaining version control for surrogate models, generating governance documentation package, and handling failed validations through rollback procedures.

Governance integration under Pillar A from Section 3.1.5 includes configuration control to track all surrogate versions with training data, assumptions, and validation results, and audit trail documentation of trigger rationale, data sources, evaluation results, and verification outcomes. Rollback definition per Section 3.1.5 specifies that rollback means withdrawal of surrogate from operational use and escalation to full retraining—not reversion to a previous version, since the prior version has already been flagged as degraded.

## 4.4 Infrastructure Considerations

### 4.4.1 Data Management

The framework requires data management capabilities that support all three pillars. These include observations (field measurements, laboratory results, sensor data), simulations (physics model inputs and outputs with full provenance), models (surrogate weights, training configurations, validation results), and governance (decision logs, audit trails, acceptance criteria records).

### 4.4.2 Computational Resources

Surrogate inference typically runs on standard computing resources (CPU or single GPU). Physics simulations may require HPC resources depending on model complexity. Training and fine-tuning benefit from GPU resources but do not always require them for incremental updates.

### 4.4.3 Interoperability

The framework should interface with existing site physics models (PFLOTRAN, MODFLOW, STOMP, TOUGH2, and similar), site monitoring databases and sensor networks, and DOE quality assurance and configuration management systems.

## 4.5 Development Phases

Implementation proceeds through three phases, progressively building capability and confidence.

### 4.5.1 Phase 1: Prototype Demonstration

The objective of Phase 1 is to demonstrate one complete recalibration cycle on a synthetic or simplified test case. The scope includes a single surrogate architecture (such as U-Net or U-FNO from Section 5), basic UQ using MC-Dropout or deep ensembles, simple drift detection (threshold-based), manual governance decisions, and documented recalibration event. Success criteria require completing the full MONITOR → DETECT → DECIDE → PREPARE → UPDATE → CALIBRATE → DEPLOY cycle with documented performance improvement.

### 4.5.2 Phase 2: Integrated Framework

The objective of Phase 2 is to integrate all framework components with realistic site data. The scope includes multiple surrogate options, full trigger logic from Section 3.3.2 (composite drift index), continual learning with replay buffers and EWC, active learning for scenario selection, governance dashboard for decision support, and automated monitoring with human-in-the-loop decisions. Success criteria require the framework to operate on representative site data with governance-compliant documentation.

### 4.5.3 Phase 3: Operational System

The objective of Phase 3 is to deploy the framework for operational use at DOE EM sites. The scope includes production-quality implementation, integration with site monitoring systems, full regulatory documentation, training materials for site operators, and maintenance and support procedures. Success criteria require the framework to be accepted for operational use under DOE quality assurance requirements.

## 4.6 Open Design Questions

Several design decisions remain for site-specific implementation. Surrogate architecture selection must determine which architecture(s) best fit site-specific prediction needs (see Section 3.2 for options). UQ method selection involves tradeoffs between MC-Dropout, deep ensembles, and conformal prediction regarding computational cost and calibration quality. Trigger threshold calibration requires site-specific thresholds for drift detection metrics based on historical variability. Update frequency must balance responsiveness (frequent updates) against stability (conservative updates). Multi-fidelity integration decisions determine when and how to incorporate low-fidelity simulations alongside high-fidelity runs. Governance workflow must address site-specific approval processes and documentation requirements. These questions will be addressed during Phase 1 prototyping and refined through operational experience.

## 4.7 Summary

This implementation roadmap translates the three-pillar framework and seven-step workflow into operational capabilities. The design follows workflow-centric organization, with capabilities organized around the two workflow phases (Continuous Monitoring and Triggered Response). All technical capabilities draw from methods detailed in Section 3, including UQ, trigger logic, continual learning, active learning, and multi-fidelity approaches. Pillar A governance requirements are embedded throughout, with explicit human decision points at the DECIDE step. The phased development approach provides progressive build-up from prototype demonstration to operational system. The framework accommodates site-specific choices while maintaining consistent workflow and governance structure.

The framework enables adaptive surrogate management that maintains prediction accuracy over multi-year remediation timelines while meeting DOE quality assurance and regulatory requirements.

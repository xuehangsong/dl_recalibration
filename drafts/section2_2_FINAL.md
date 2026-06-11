# 2.2 Recalibration Workflow

The recalibration workflow defines how the three pillars interact during operations to maintain surrogate accuracy over time. While the pillars described in Section 2.1 organize what the framework manages, the workflow specifies the operational sequence that traverses these pillars, drawing resources, methods, and constraints from each as needed.

The workflow is structured as a seven-step cycle organized into two phases. Phase 1, Continuous Monitoring, encompasses Steps 1 through 3 and runs continuously during operations, tracking surrogate performance and determining when intervention may be needed. Phase 2, Triggered Response, encompasses Steps 4 through 7 and is activated only when Phase 1 indicates that an update is warranted and governance approves the intervention.

This two-phase structure reflects a key principle from the governance framework described in Section 3.1.3: the presence of a recalibration trigger does not automatically mandate recalibration. Instead, the framework requires formal justification that an update is necessary, proportional, and expected to improve performance. The explicit DECIDE step (Step 3) implements this governance requirement.

## 2.2.1 Phase 1: Continuous Monitoring

Phase 1 runs continuously during site operations, providing ongoing assessment of surrogate performance without modifying the operational model. These steps implement the monitor-detect-decide logic that determines whether intervention is needed.

### Step 1: MONITOR

The purpose of the MONITOR step is to track surrogate predictions against available observations and compute diagnostic metrics. This step compares surrogate predictions to field monitoring data as observations become available, calculates prediction-observation residuals at priority monitoring locations, and computes uncertainty metrics using embedded uncertainty quantification methods such as Monte Carlo dropout and deep ensembles. The step also tracks prediction interval coverage and calibration statistics, logging all comparisons for trend analysis and audit purposes.

The MONITOR step draws from Pillar A for data policies specifying which observations to assimilate, quality assurance and quality control standards for data validation, and specifications for what metrics to track. It draws from Pillar C for uncertainty quantification methods used to compute predictive uncertainty and confidence intervals. The outputs of this step are time series of residuals, uncertainty metrics, and coverage statistics that feed into Step 2.

### Step 2: DETECT

The purpose of the DETECT step is to identify when surrogate performance has degraded beyond acceptable thresholds using automated diagnostics. This step applies drift detection algorithms to residual and uncertainty time series and compares current metrics against predefined trigger thresholds from Pillar A. The step evaluates multiple detection criteria including predictive uncertainty exceeding confidence bounds, systematic bias in prediction-observation residuals, uncertainty inflation relative to historical baselines, distributional drift in inputs or outputs using tests such as the Kolmogorov-Smirnov test, and extrapolation beyond the original training domain. Based on detection results, the step updates the trigger state machine.

The framework uses a state machine to manage the transition from routine monitoring to triggered response, as illustrated in Figure 2.2.

```
    ┌─────────────────────────────────────────────────────────┐
    │                  TRIGGER STATE MACHINE                   │
    │                                                          │
    │   ┌──────┐    threshold    ┌─────────┐    sustained    │
    │   │  OK  │───exceeded────▶│ WARNING │───degradation──▶ │
    │   └──────┘                 └─────────┘                  │
    │       ▲                         │                       │
    │       │                         │                       │
    │       │    metrics              │ 60-90 days            │
    │       │    recover              │ persistence           │
    │       │                         ▼                       │
    │       │                    ┌─────────┐                  │
    │       └────────────────────│ UPDATE  │                  │
    │         validation         └────┬────┘                  │
    │         passes                  │                       │
    │                                 │ validation            │
    │                                 │ fails                 │
    │                                 ▼                       │
    │                           ┌──────────┐                  │
    │                           │ ESCALATE │                  │
    │                           └──────────┘                  │
    │                           (full retrain)                │
    └─────────────────────────────────────────────────────────┘
```

**Figure 2.2.** Trigger state machine showing transitions between monitoring states. The OK state indicates acceptable performance; WARNING indicates threshold exceedance that may be transient; UPDATE indicates sustained degradation requiring governance review; ESCALATE indicates that incremental updates have failed and full retraining is required.

The DETECT step draws from Pillar A for trigger thresholds, persistence requirements (typically 60-90 days), and criteria for state transitions. It draws from Pillar C for drift detection algorithms, statistical tests, and resilience metrics. The outputs of this step are the current trigger state and an evidence package documenting the detection rationale.

### Step 3: DECIDE

The purpose of the DECIDE step is to conduct human or governance review of detection evidence and formally determine whether an update is warranted. This step is critical because it implements the governance requirement that triggers do not automatically mandate recalibration. A human reviewer or governance committee, depending on site procedures, must evaluate the evidence and make a formal determination.

The DECIDE step reviews the evidence package from Step 2, including residual trends and uncertainty metrics, drift detection results and statistical significance, documented operational changes such as new wells or pumping schedule changes, and comparison to historical performance patterns. The reviewer assesses whether the observed degradation is meaningful (large enough to affect decision quality), persistent (not a transient anomaly), and addressable (likely to be corrected by an incremental update).

Based on this assessment, the step determines the appropriate response. If evidence is insufficient, the system returns to the OK state with no action. If the situation is ambiguous, the system remains in the WARNING state and continues monitoring. If an update is warranted, the system proceeds to Phase 2. If an incremental update is unlikely to succeed, the system escalates directly to full retraining.

When an update is approved, the DECIDE step also selects the update pathway. Pathway A, the observation-driven approach, is selected when recent field observations provide sufficient new information for fine-tuning. Pathway B, the simulation-driven approach, is selected when active learning should identify new physics simulations to generate targeted training data.

The DECIDE step draws exclusively from Pillar A for governance policies, formal justification requirements, approval workflows, and documentation standards. The outputs of this step are a formal decision record documenting the determination, rationale, and selected pathway if an update is approved.

## 2.2.2 Phase 2: Triggered Response

Phase 2 is activated only when Step 3 (DECIDE) approves an update. These steps implement the prepare-update-calibrate-deploy sequence that modifies the operational surrogate.

### Step 4: PREPARE

The purpose of the PREPARE step is to assemble the dataset that will be used to update the surrogate. The specific activities depend on the pathway selected in Step 3.

For Pathway A (observation-driven updates), the step compiles recent field observations that were not in the original training set, applies quality assurance and quality control procedures per Pillar A data policies, formats data for compatibility with the surrogate training pipeline, and assembles a replay buffer of historical training samples—typically 70-75% of the update batch—to prevent catastrophic forgetting.

For Pathway B (simulation-driven updates), the step generates a candidate pool of operationally relevant simulation scenarios and applies active learning algorithms to score candidates based on predictive uncertainty in the candidate region, residual patterns relative to recent observations, and diversity constraints covering spatial, temporal, and parameter dimensions. The step then selects 6-10 high-value scenarios that maximize expected information gain, executes targeted physics simulations for selected scenarios, and combines new simulation outputs with the replay buffer.

The PREPARE step draws from Pillar A for data policies and quality assurance standards, from Pillar B for the physics simulator when executing new runs under Pathway B, and from Pillar C for active learning strategies used in scenario selection. The output of this step is a prepared update dataset with provenance documentation.

### Step 5: UPDATE

The purpose of the UPDATE step is to fine-tune the deep-learning surrogate using continual learning methods to incorporate new information while preserving previously learned knowledge. This step configures the continual learning approach based on the update context, selecting from methods such as Elastic Weight Consolidation to penalize changes to weights important for previous tasks, experience replay to include historical samples in each training batch, and layer freezing to preserve learned representations in early encoder layers.

The step sets conservative hyperparameters including a small learning rate to prevent catastrophic forgetting, L2 regularization anchored to pre-update weights, and early stopping based on validation performance. The step then executes fine-tuning on the prepared dataset while monitoring training for convergence and stability.

A key principle of this step is that it performs an incremental update, not full retraining. The goal is to adapt the surrogate to new conditions while preserving its validity in previously learned domains. Full retraining is reserved for cases where incremental updates repeatedly fail, triggering the ESCALATE state.

The UPDATE step draws from Pillar B for the surrogate model to be updated and training infrastructure, and from Pillar C for continual learning methods including Elastic Weight Consolidation, replay, and layer freezing. The output of this step is an updated surrogate model in candidate status, not yet operational.

### Step 6: CALIBRATE

The purpose of the CALIBRATE step is to perform post-hoc calibration of the updated model's uncertainty estimates to ensure stated confidence intervals accurately reflect true prediction reliability. This step is separate from UPDATE because while some uncertainty quantification methods such as deep ensembles are integral to training, probability calibration techniques like temperature scaling and isotonic regression are post-training activities that adjust the model's uncertainty outputs without modifying its point predictions.

The CALIBRATE step evaluates the updated model's uncertainty calibration on held-out validation data and generates reliability diagrams comparing stated confidence levels to empirical coverage. The step applies calibration methods as needed, including temperature scaling to learn a single parameter that rescales outputs, isotonic regression to learn a monotonic mapping from predicted to calibrated probabilities, and Platt scaling to fit a logistic regression on model outputs. The step verifies that calibrated prediction intervals meet acceptance criteria, typically requiring prediction interval coverage probability near 90%, and documents calibration parameters for reproducibility.

The CALIBRATE step draws from Pillar A for acceptance criteria for uncertainty calibration such as coverage targets, and from Pillar C for probability calibration methods and reliability diagram analysis. The output of this step is a calibrated surrogate model with documented uncertainty characteristics.

### Step 7: DEPLOY

The purpose of the DEPLOY step is to validate the updated model against acceptance criteria and, if successful, promote it to operational status with full governance documentation.

The validation phase evaluates the calibrated model on held-out test data not used in training or calibration. Performance is compared against predefined acceptance criteria from Pillar A, including error statistics at priority monitoring locations, uncertainty calibration metrics, spatial and temporal consistency, and performance relative to the pre-update baseline. All validation results are documented.

If validation fails, the updated model is not deployed. The step assesses whether failure indicates a need for a larger update batch, in which case the workflow returns to Step 4 with expanded scope, or whether failure indicates a fundamental domain shift requiring transition to the ESCALATE state for full retraining. Failure rationale and next steps are documented.

If validation passes, the validated model is promoted to operational status. The previous operational model is archived but not deleted. Model version records in Pillar B are updated. The step generates comprehensive governance documentation including trigger rationale from Step 2, decision justification from Step 3, data sources and provenance from Step 4, training configuration from Step 5, calibration parameters from Step 6, and validation results from Step 7. The trigger state machine returns to the OK state.

The DEPLOY step draws from Pillar A for acceptance criteria, audit requirements, and rollback procedures, and from Pillar B for model versioning and artifact management. The outputs of this step are a deployed operational model if validation passes, or an escalation decision if validation fails, along with a complete audit trail.

## 2.2.3 Cross-Reference: Workflow Steps and Pillars

Table 2.1 summarizes how each workflow step draws from the three pillars.

**Table 2.1.** Workflow step dependencies on the three pillars.

| Step | Phase | Pillar A (Rules) | Pillar B (Models) | Pillar C (Methods) |
|------|-------|------------------|--------------------|--------------------|
| 1. MONITOR | Continuous | Data policies, metrics to track | — | UQ metrics computation |
| 2. DETECT | Continuous | Trigger thresholds, state transitions | — | Drift detection algorithms |
| 3. DECIDE | Continuous | Governance approval, justification | — | — |
| 4. PREPARE | Triggered | Data policies, QA/QC | Physics simulator (Pathway B) | Active learning selection |
| 5. UPDATE | Triggered | — | Surrogate fine-tuning | Continual learning methods |
| 6. CALIBRATE | Triggered | Acceptance criteria (coverage) | — | Probability calibration |
| 7. DEPLOY | Triggered | Audit trail, rollback procedures | Model versioning | — |

## 2.2.4 Workflow Visualization

Figure 2.3 shows the complete workflow with phase separation and pillar interactions.

```
            ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
            │   PILLAR A   │   │   PILLAR B   │   │   PILLAR C   │
            │    Rules     │   │    Models    │   │   Methods    │
            └──────┬───────┘   └──────┬───────┘   └──────┬───────┘
                   │                  │                  │
    ═══════════════╪══════════════════╪══════════════════╪═══════════
    PHASE 1:       │                  │                  │
    CONTINUOUS     │                  │                  │
    MONITORING     │                  │                  │
                   │                  │                  │
    1. MONITOR ────┤ data policies    │                  ├── UQ metrics
                   │                  │                  │
    2. DETECT ─────┤ thresholds       │                  ├── drift tests
                   │                  │                  │
    3. DECIDE ─────┤ governance       │                  │
                   │ approval         │                  │
    ───────────────┼──────────────────┼──────────────────┼───────────
    PHASE 2:       │                  │                  │
    TRIGGERED      │                  │                  │
    RESPONSE       │                  │                  │
                   │                  │                  │
    4. PREPARE ────┤ QA/QC            ├── physics        ├── active learning
                   │                  │   simulator      │
    5. UPDATE ─────┤                  ├── surrogate      ├── continual learning
                   │                  │                  │
    6. CALIBRATE ──┤ acceptance       │                  ├── calibration
                   │ criteria         │                  │
    7. DEPLOY ─────┤ audit trail      ├── versioning     │
                   │ rollback         │                  │
    ═══════════════╧══════════════════╧══════════════════╧═══════════
                          │
                          ▼
                   Return to Step 1
                   (continuous cycle)
```

**Figure 2.3.** Complete workflow visualization showing the two-phase structure and pillar interactions. Phase 1 (Continuous Monitoring) runs continuously; Phase 2 (Triggered Response) activates only when governance approves an update.

## 2.2.5 Update Pathways

The framework supports two update pathways, selected during Step 3 (DECIDE) based on the nature of the detected degradation.

### Pathway A: Observation-Driven Update

Pathway A is appropriate when recent field observations provide sufficient new information to correct the surrogate without additional physics simulations. This pathway offers faster turnaround because no physics simulation wait time is required, and lower computational cost. It is appropriate when degradation is due to gradual drift within the existing parameter space and relies on the assumption that field observations adequately represent the conditions causing degradation. The workflow proceeds from Steps 1-3 through Step 4 (compile observations) to Steps 5-7.

### Pathway B: Simulation-Driven Update

Pathway B is appropriate when the surrogate has encountered conditions outside its training domain and targeted physics simulations are needed to generate appropriate training data. This pathway requires longer turnaround due to physics simulation execution and incurs higher computational cost. It is appropriate when degradation is due to operational changes such as new wells or changed boundary conditions, or regime shifts. Active learning ensures simulations target the most informative conditions. The workflow proceeds from Steps 1-3 through Step 4 (active learning plus physics runs) to Steps 5-7.

The choice between pathways is a governance decision made in Step 3 based on the evidence and operational context.

## 2.2.6 Operational Considerations

### Monitoring Frequency

The continuous monitoring phase (Steps 1-3) operates on a schedule aligned with data availability and site-specific needs. Automated diagnostics run whenever new observations are available, which may be daily or weekly depending on the monitoring network. Summary evaluations are compiled periodically, typically monthly or quarterly, for management review. Formal decision points are evaluated on a predictable schedule, typically quarterly, for governance review.

### Update Frequency

The triggered response phase (Steps 4-7) is activated only when needed. Typical frequency involves quarterly evaluation of whether updates are warranted. A minimum persistence period of 60-90 days of sustained degradation is required before the UPDATE state is reached. The framework takes a conservative approach in which updates are not performed more frequently than necessary to maintain stability.

### Cycle Continuation

After Step 7 completes, whether through successful deployment or escalation, the workflow returns to Step 1 and continues the monitoring cycle. The framework operates continuously throughout the site's operational lifetime, adapting the surrogate as conditions evolve while maintaining governance oversight and audit trails.

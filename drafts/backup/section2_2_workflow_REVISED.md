# 2.2 Recalibration Workflow

The recalibration workflow defines **HOW** the three pillars interact during operations to maintain surrogate accuracy over time. While the pillars (Section 2.1) organize WHAT the framework manages, the workflow specifies the operational sequence that traverses these pillars, drawing resources, methods, and constraints from each as needed.

The workflow is structured as a **seven-step cycle organized into two phases**:

- **Phase 1: Continuous Monitoring** (Steps 1-3) — Always running during operations, tracking surrogate performance and determining when intervention may be needed.

- **Phase 2: Triggered Response** (Steps 4-7) — Activated only when Phase 1 indicates that an update is warranted and governance approves the intervention.

This two-phase structure reflects a key principle from the governance framework (Section 3.1.3): **the presence of a recalibration trigger does not automatically mandate recalibration**. Instead, the framework requires formal justification that an update is necessary, proportional, and expected to improve performance. The explicit DECIDE step (Step 3) implements this governance requirement.

---

## Phase 1: Continuous Monitoring

Phase 1 runs continuously during site operations, providing ongoing assessment of surrogate performance without modifying the operational model. These steps implement the "monitor → detect → decide" logic that determines whether intervention is needed.

### Step 1: MONITOR

**Purpose**: Track surrogate predictions against available observations and compute diagnostic metrics.

**Activities**:
- Compare surrogate predictions to field monitoring data as observations become available
- Calculate prediction-observation residuals at priority monitoring locations
- Compute uncertainty metrics using embedded UQ methods (e.g., Monte Carlo dropout, deep ensembles)
- Track prediction interval coverage and calibration statistics
- Log all comparisons for trend analysis and audit purposes

**Draws from**:
- **Pillar A (Rules)**: Data policies specifying which observations to assimilate, QA/QC standards for data validation, and specifications for what metrics to track
- **Pillar C (Methods)**: Uncertainty quantification methods for computing predictive uncertainty and confidence intervals

**Outputs**: Time series of residuals, uncertainty metrics, and coverage statistics that feed into Step 2.

---

### Step 2: DETECT

**Purpose**: Identify when surrogate performance has degraded beyond acceptable thresholds using automated diagnostics.

**Activities**:
- Apply drift detection algorithms to residual and uncertainty time series
- Compare current metrics against predefined trigger thresholds from Pillar A
- Evaluate multiple detection criteria:
  - Predictive uncertainty exceeding confidence bounds
  - Systematic bias in prediction-observation residuals
  - Uncertainty inflation relative to historical baselines
  - Distributional drift in inputs or outputs (e.g., Kolmogorov-Smirnov tests)
  - Extrapolation beyond the original training domain
- Update the trigger state machine based on detection results

**Trigger State Machine**:

The framework uses a state machine to manage the transition from routine monitoring to triggered response:

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

- **OK**: Surrogate performance is within acceptable bounds; continue routine monitoring
- **WARNING**: Metrics have exceeded thresholds but may be transient; continue monitoring with elevated attention
- **UPDATE**: Sustained degradation confirmed; proceed to DECIDE step for governance review
- **ESCALATE**: Incremental update failed validation; escalate to full retraining under governance control

**Draws from**:
- **Pillar A (Rules)**: Trigger thresholds, persistence requirements (e.g., 60-90 days), and criteria for state transitions
- **Pillar C (Methods)**: Drift detection algorithms, statistical tests, and resilience metrics

**Outputs**: Current trigger state and evidence package documenting the detection rationale.

---

### Step 3: DECIDE

**Purpose**: Conduct human/governance review of detection evidence and formally determine whether an update is warranted.

**This step is critical**: It implements the governance requirement that triggers do not automatically mandate recalibration. A human reviewer (or governance committee, depending on site procedures) must evaluate the evidence and make a formal determination.

**Activities**:
- Review the evidence package from Step 2, including:
  - Residual trends and uncertainty metrics
  - Drift detection results and statistical significance
  - Documented operational changes (e.g., new wells, pumping schedule changes)
  - Comparison to historical performance patterns
- Assess whether the observed degradation is:
  - **Meaningful**: Large enough to affect decision quality
  - **Persistent**: Not a transient anomaly
  - **Addressable**: Likely to be corrected by an incremental update
- Determine the appropriate response:
  - **No action**: Return to OK state if evidence is insufficient
  - **Continue monitoring**: Remain in WARNING state if situation is ambiguous
  - **Approve update**: Proceed to Phase 2 if update is warranted
  - **Escalate**: Proceed directly to full retraining if incremental update is unlikely to succeed
- If update is approved, select the **update pathway**:
  - **Pathway A (Observation-driven)**: Recent field observations provide sufficient new information for fine-tuning
  - **Pathway B (Simulation-driven)**: Active learning should select new physics simulations to generate targeted training data

**Draws from**:
- **Pillar A (Rules)**: Governance policies, formal justification requirements, approval workflows, and documentation standards

**Outputs**: Formal decision record documenting the determination, rationale, and selected pathway (if update approved).

---

## Phase 2: Triggered Response

Phase 2 is activated only when Step 3 (DECIDE) approves an update. These steps implement the "prepare → update → calibrate → deploy" sequence that modifies the operational surrogate.

### Step 4: PREPARE

**Purpose**: Assemble the dataset that will be used to update the surrogate.

**Activities**:

*For Pathway A (Observation-driven):*
- Compile recent field observations that were not in the original training set
- Apply QA/QC procedures per Pillar A data policies
- Format data for compatibility with the surrogate training pipeline
- Assemble a replay buffer of historical training samples (typically 70-75% of the update batch) to prevent catastrophic forgetting

*For Pathway B (Simulation-driven):*
- Generate a candidate pool of operationally relevant simulation scenarios
- Apply active learning algorithms to score candidates based on:
  - Predictive uncertainty in the candidate region
  - Residual patterns relative to recent observations
  - Diversity constraints (spatial, temporal, parameter coverage)
- Select 6-10 high-value scenarios that maximize expected information gain
- Execute targeted physics simulations for selected scenarios
- Combine new simulation outputs with replay buffer

**Draws from**:
- **Pillar A (Rules)**: Data policies and QA/QC standards
- **Pillar B (Models)**: Physics simulator for executing new runs (Pathway B)
- **Pillar C (Methods)**: Active learning strategies for scenario selection

**Outputs**: Prepared update dataset with provenance documentation.

---

### Step 5: UPDATE

**Purpose**: Fine-tune the DL surrogate using continual learning methods to incorporate new information while preserving previously learned knowledge.

**Activities**:
- Configure the continual learning approach based on the update context:
  - **Elastic Weight Consolidation (EWC)**: Penalize changes to weights important for previous tasks
  - **Experience replay**: Include historical samples in each training batch
  - **Layer freezing**: Freeze early encoder layers to preserve learned representations
- Set conservative hyperparameters:
  - Small learning rate to prevent catastrophic forgetting
  - L2 regularization anchored to pre-update weights
  - Early stopping based on validation performance
- Execute fine-tuning on the prepared dataset
- Monitor training for convergence and stability

**Key principle**: This is an **incremental update, NOT full retraining**. The goal is to adapt the surrogate to new conditions while preserving its validity in previously learned domains. Full retraining is reserved for cases where incremental updates repeatedly fail (ESCALATE state).

**Draws from**:
- **Pillar B (Models)**: Surrogate model to be updated, training infrastructure
- **Pillar C (Methods)**: Continual learning methods (EWC, replay, layer freezing)

**Outputs**: Updated surrogate model (candidate version, not yet operational).

---

### Step 6: CALIBRATE

**Purpose**: Perform post-hoc calibration of the updated model's uncertainty estimates to ensure stated confidence intervals accurately reflect true prediction reliability.

**This step is separate from UPDATE**: While some UQ methods (e.g., deep ensembles) are integral to training, probability calibration techniques like temperature scaling and isotonic regression are post-training activities that adjust the model's uncertainty outputs without modifying its point predictions.

**Activities**:
- Evaluate the updated model's uncertainty calibration on held-out validation data
- Generate reliability diagrams comparing stated confidence levels to empirical coverage
- Apply calibration methods as needed:
  - **Temperature scaling**: Learn a single parameter to rescale logits/outputs
  - **Isotonic regression**: Learn a monotonic mapping from predicted to calibrated probabilities
  - **Platt scaling**: Fit a logistic regression on model outputs
- Verify that calibrated prediction intervals meet acceptance criteria (e.g., PICP ≈ 90%)
- Document calibration parameters for reproducibility

**Draws from**:
- **Pillar A (Rules)**: Acceptance criteria for uncertainty calibration (e.g., coverage targets)
- **Pillar C (Methods)**: Probability calibration methods and reliability diagram analysis

**Outputs**: Calibrated surrogate model with documented uncertainty characteristics.

---

### Step 7: DEPLOY

**Purpose**: Validate the updated model against acceptance criteria and, if successful, promote it to operational status with full governance documentation.

**Activities**:

*Validation:*
- Evaluate the calibrated model on held-out test data not used in training or calibration
- Compare performance against predefined acceptance criteria from Pillar A:
  - Error statistics at priority monitoring locations
  - Uncertainty calibration metrics
  - Spatial and temporal consistency
  - Performance relative to the pre-update baseline
- Document validation results

*If validation FAILS:*
- Do NOT deploy the updated model
- Assess whether failure indicates:
  - Need for larger update batch → return to Step 4 with expanded scope
  - Fundamental domain shift → transition to ESCALATE state for full retraining
- Document failure rationale and next steps

*If validation PASSES:*
- Promote the validated model to operational status
- Archive the previous operational model (do not delete)
- Update model version records in Pillar B
- Generate comprehensive governance documentation:
  - Trigger rationale (from Step 2)
  - Decision justification (from Step 3)
  - Data sources and provenance (from Step 4)
  - Training configuration (from Step 5)
  - Calibration parameters (from Step 6)
  - Validation results (from Step 7)
- Return trigger state machine to OK state

**Draws from**:
- **Pillar A (Rules)**: Acceptance criteria, audit requirements, rollback procedures
- **Pillar B (Models)**: Model versioning and artifact management

**Outputs**: Deployed operational model (if validation passes) or escalation decision (if validation fails), with complete audit trail.

---

## Cross-Reference: Workflow Steps and Pillars

The following table summarizes how each workflow step draws from the three pillars:

| Step | Phase | Pillar A (Rules) | Pillar B (Models) | Pillar C (Methods) |
|------|-------|------------------|--------------------|--------------------|
| 1. MONITOR | Continuous | Data policies, metrics to track | — | UQ metrics computation |
| 2. DETECT | Continuous | Trigger thresholds, state transitions | — | Drift detection algorithms |
| 3. DECIDE | Continuous | Governance approval, justification | — | — |
| 4. PREPARE | Triggered | Data policies, QA/QC | Physics simulator (Pathway B) | Active learning selection |
| 5. UPDATE | Triggered | — | Surrogate fine-tuning | Continual learning methods |
| 6. CALIBRATE | Triggered | Acceptance criteria (coverage) | — | Probability calibration |
| 7. DEPLOY | Triggered | Audit trail, rollback procedures | Model versioning | — |

---

## Workflow Visualization

The following diagram shows the complete workflow with phase separation and pillar interactions:

```
            ┌──────────┐   ┌──────────┐   ┌──────────┐
            │ PILLAR A │   │ PILLAR B │   │ PILLAR C │
            │  Rules   │   │  Models  │   │ Methods  │
            └────┬─────┘   └────┬─────┘   └────┬─────┘
                 │              │              │
    ═════════════╪══════════════╪══════════════╪════════
    PHASE 1:     │              │              │
    CONTINUOUS   │              │              │
    MONITORING   │              │              │
                 │              │              │
    1. MONITOR ──┤ data policies│              ├── UQ metrics
                 │              │              │
    2. DETECT ───┤ thresholds   │              ├── drift tests
                 │              │              │
    3. DECIDE ───┤ governance   │              │
                 │ approval     │              │
    ─────────────┼──────────────┼──────────────┼────────
    PHASE 2:     │              │              │
    TRIGGERED    │              │              │
    RESPONSE     │              │              │
                 │              │              │
    4. PREPARE ──┤ QA/QC        ├── physics    ├── active learning
                 │              │   simulator  │
    5. UPDATE ───┤              ├── surrogate  ├── continual learning
                 │              │              │
    6. CALIBRATE ┤ acceptance   │              ├── calibration
                 │ criteria     │              │
    7. DEPLOY ───┤ audit trail  ├── versioning │
                 │ rollback     │              │
    ═════════════╧══════════════╧══════════════╧════════
                        │
                        ▼
                 Return to Step 1
                 (continuous cycle)
```

---

## Update Pathways

The framework supports two update pathways, selected during Step 3 (DECIDE) based on the nature of the detected degradation:

### Pathway A: Observation-Driven Update

**When to use**: Recent field observations provide sufficient new information to correct the surrogate without additional physics simulations.

**Characteristics**:
- Faster turnaround (no physics simulation wait time)
- Lower computational cost
- Appropriate when degradation is due to gradual drift within the existing parameter space
- Relies on the assumption that field observations adequately represent the conditions causing degradation

**Workflow**: Steps 1-3 → Step 4 (compile observations) → Steps 5-7

### Pathway B: Simulation-Driven Update

**When to use**: The surrogate has encountered conditions outside its training domain, and targeted physics simulations are needed to generate appropriate training data.

**Characteristics**:
- Longer turnaround (requires physics simulation execution)
- Higher computational cost
- Appropriate when degradation is due to operational changes (new wells, changed boundary conditions) or regime shifts
- Active learning ensures simulations target the most informative conditions

**Workflow**: Steps 1-3 → Step 4 (active learning + physics runs) → Steps 5-7

The choice between pathways is a governance decision (Step 3) based on the evidence and operational context.

---

## Operational Considerations

### Monitoring Frequency

The continuous monitoring phase (Steps 1-3) operates on a schedule aligned with data availability and site-specific needs:
- **Automated diagnostics**: Run whenever new observations are available (e.g., daily, weekly)
- **Summary evaluations**: Compiled periodically (e.g., monthly, quarterly) for management review
- **Formal decision points**: Evaluated on a predictable schedule (e.g., quarterly) for governance review

### Update Frequency

The triggered response phase (Steps 4-7) is activated only when needed:
- **Typical frequency**: Quarterly evaluation of whether updates are warranted
- **Minimum persistence**: 60-90 days of sustained degradation before UPDATE state is reached
- **Conservative approach**: Updates are not performed more frequently than necessary to maintain stability

### Cycle Continuation

After Step 7 completes (whether through successful deployment or escalation), the workflow returns to Step 1 and continues the monitoring cycle. The framework operates continuously throughout the site's operational lifetime, adapting the surrogate as conditions evolve while maintaining governance oversight and audit trails.

# 5.0 Software Architecture and Implementation Roadmap

This section describes how the three-pillar recalibration framework (Section 2.1) and seven-step workflow (Section 2.2) translate into a computational system. The software architecture is organized around the two workflow phases—Continuous Monitoring (Phase 1) and Triggered Response (Phase 2)—ensuring that implementation directly supports operational needs.

The implementation must satisfy two demands: (1) support the scientific workflow of running physics simulations, training surrogates, quantifying uncertainty, and executing recalibration; and (2) meet DOE governance requirements for traceability, reproducibility, and quality assurance. The design outlined here balances both.

---

## 5.1 Software Architecture Overview

### 5.1.1 Design Principles

The software architecture follows three guiding principles derived from the framework:

1. **Workflow-Centric Organization**: Software modules map directly to workflow phases and steps, not to abstract layers or independent pillars.

2. **Pillar Awareness**: Each module explicitly identifies which management domain(s) it serves (Pillar A: Governance, Pillar B: Modeling Engines, Pillar C: Recalibration Mechanisms).

3. **Governance Integration**: Pillar A requirements (audit trails, acceptance criteria, human decision points) are embedded throughout, not isolated in a separate layer.

### 5.1.2 Module-to-Workflow Mapping

The following diagram shows how software modules support the seven-step, two-phase workflow:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SOFTWARE ARCHITECTURE OVERVIEW                           │
│                  (Organized by Workflow Phases)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ╔═══════════════════════════════════════════════════════════════════════╗  │
│  ║  PHASE 1: CONTINUOUS MONITORING (Steps 1-3)                           ║  │
│  ║  Module: Monitoring & Detection System                                ║  │
│  ╠═══════════════════════════════════════════════════════════════════════╣  │
│  ║                                                                       ║  │
│  ║  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐               ║  │
│  ║  │   MONITOR   │───▶│   DETECT    │───▶│   DECIDE    │               ║  │
│  ║  │   (Step 1)  │    │   (Step 2)  │    │   (Step 3)  │               ║  │
│  ║  └─────────────┘    └─────────────┘    └─────────────┘               ║  │
│  ║        │                  │                  │                        ║  │
│  ║        ▼                  ▼                  ▼                        ║  │
│  ║  ┌───────────────────────────────────────────────────────────────┐   ║  │
│  ║  │ • Performance Tracker (Pillar C)                              │   ║  │
│  ║  │ • UQ Computation Engine (Pillar C)                            │   ║  │
│  ║  │ • Drift Detection Module (Pillar C)                           │   ║  │
│  ║  │ • Trigger State Machine (Pillar A + C)                        │   ║  │
│  ║  │ • Decision Support Dashboard (Pillar A)                       │   ║  │
│  ║  └───────────────────────────────────────────────────────────────┘   ║  │
│  ╚═══════════════════════════════════════════════════════════════════════╝  │
│                              │                                              │
│                              │ Trigger (if DECIDE approves)                 │
│                              ▼                                              │
│  ╔═══════════════════════════════════════════════════════════════════════╗  │
│  ║  PHASE 2: TRIGGERED RESPONSE (Steps 4-7)                              ║  │
│  ║  Module: Model Update Pipeline + Deployment System                    ║  │
│  ╠═══════════════════════════════════════════════════════════════════════╣  │
│  ║                                                                       ║  │
│  ║  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐               ║  │
│  ║  │   PREPARE   │───▶│   UPDATE    │───▶│  CALIBRATE  │               ║  │
│  ║  │   (Step 4)  │    │   (Step 5)  │    │   (Step 6)  │               ║  │
│  ║  └─────────────┘    └─────────────┘    └─────────────┘               ║  │
│  ║        │                  │                  │                        ║  │
│  ║        ▼                  ▼                  ▼                        ║  │
│  ║  ┌───────────────────────────────────────────────────────────────┐   ║  │
│  ║  │ • Active Learning Sampler (Pillar C)                          │   ║  │
│  ║  │ • Physics Model Interface (Pillar B)                          │   ║  │
│  ║  │ • Continual Learning Trainer (Pillar C)                       │   ║  │
│  ║  │ • UQ Calibration Module (Pillar C)                            │   ║  │
│  ║  └───────────────────────────────────────────────────────────────┘   ║  │
│  ║                              │                                        ║  │
│  ║                              ▼                                        ║  │
│  ║  ┌─────────────┐                                                     ║  │
│  ║  │   DEPLOY    │                                                     ║  │
│  ║  │   (Step 7)  │                                                     ║  │
│  ║  └─────────────┘                                                     ║  │
│  ║        │                                                             ║  │
│  ║        ▼                                                             ║  │
│  ║  ┌───────────────────────────────────────────────────────────────┐   ║  │
│  ║  │ • Validation Engine (Pillar A + C)                            │   ║  │
│  ║  │ • Model Registry (Pillar A + B)                               │   ║  │
│  ║  │ • Audit Logger (Pillar A)                                     │   ║  │
│  ║  │ • Rollback Manager (Pillar A)                                 │   ║  │
│  ║  └───────────────────────────────────────────────────────────────┘   ║  │
│  ╚═══════════════════════════════════════════════════════════════════════╝  │
│                                                                             │
│  ╔═══════════════════════════════════════════════════════════════════════╗  │
│  ║  CROSS-CUTTING: Infrastructure Layer                                  ║  │
│  ╠═══════════════════════════════════════════════════════════════════════╣  │
│  ║  • Data Management & Provenance (All Pillars)                        ║  │
│  ║  • HPC Integration (Pillar B)                                        ║  │
│  ║  • Surrogate Model Engine (Pillar B)                                 ║  │
│  ║  • Configuration Management (Pillar A)                               ║  │
│  ╚═══════════════════════════════════════════════════════════════════════╝  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.1.3 Module-Pillar-Step Reference Table

| Software Module | Workflow Steps | Primary Pillar(s) | Function |
|-----------------|----------------|-------------------|----------|
| Performance Tracker | Step 1 (MONITOR) | C | Compare predictions vs. observations |
| UQ Computation Engine | Steps 1, 6 | C | Calculate uncertainty metrics |
| Drift Detection Module | Step 2 (DETECT) | C | Evaluate trigger conditions |
| Trigger State Machine | Steps 2-3 | A, C | Manage OK→WARNING→UPDATE states |
| Decision Support Dashboard | Step 3 (DECIDE) | A | Present evidence for governance review |
| Active Learning Sampler | Step 4 (PREPARE) | C | Select informative simulation scenarios |
| Physics Model Interface | Step 4 (PREPARE) | B | Execute targeted physics runs |
| Continual Learning Trainer | Step 5 (UPDATE) | C | Fine-tune surrogate weights |
| UQ Calibration Module | Step 6 (CALIBRATE) | C | Recalibrate uncertainty estimates |
| Validation Engine | Step 7 (DEPLOY) | A, C | Verify acceptance criteria |
| Model Registry | Step 7 (DEPLOY) | A, B | Version control for surrogates |
| Audit Logger | All Steps | A | Record decisions and provenance |
| Rollback Manager | Step 7 (DEPLOY) | A | Handle failed validations |
| Data Management Layer | All Steps | All | Store observations, outputs, models |
| Surrogate Model Engine | Steps 1, 5 | B | Inference and training |
| HPC Integration | Step 4 | B | Job scheduling for physics runs |

---

## 5.2 Monitoring & Detection System (Supports Steps 1-3)

This module implements Phase 1 of the workflow—the continuous monitoring loop that runs throughout operations. It serves primarily **Pillar C (Recalibration Mechanisms)** for technical diagnostics and **Pillar A (Governance)** for decision support.

### 5.2.1 Performance Tracking (Step 1: MONITOR)

**Pillar(s) Served**: Pillar C (primary), Pillar A (audit)

The Performance Tracker continuously compares surrogate predictions against available monitoring data:

- **Residual Computation**: Calculate prediction-observation residuals at monitoring wells and compliance points. Track spatial and temporal patterns in residuals.

- **Accuracy Metrics**: Compute RMSE, MAE, bias, and correlation coefficients. Maintain rolling statistics over configurable time windows (e.g., 30-day, 90-day).

- **Baseline Comparison**: Compare current performance against the stable baseline established at deployment. Flag sustained deviations from baseline accuracy.

- **Data Ingestion**: Automatically ingest new observations from field sensors, laboratory results, and manual measurements. Validate data quality before use.

**Implementation Notes**:
- Runs on a configurable schedule (e.g., daily, weekly)
- Stores all metrics in the Data Management Layer for audit trails
- Generates summary reports for governance review

### 5.2.2 Uncertainty Quantification Computation (Step 1: MONITOR)

**Pillar(s) Served**: Pillar C

The UQ Computation Engine tracks surrogate uncertainty using methods described in Section 3.3.1:

- **Predictive Uncertainty**: Compute uncertainty estimates using MC-Dropout, deep ensembles, or conformal prediction. Track predictive variance at key locations.

- **Calibration Metrics**: Evaluate whether stated uncertainty intervals match empirical coverage. A well-calibrated 95% interval should contain the true value ~95% of the time.

- **Uncertainty Inflation Detection**: Flag when predictive variance increases significantly relative to historical baselines, indicating potential extrapolation beyond the training domain.

### 5.2.3 Drift Detection (Step 2: DETECT)

**Pillar(s) Served**: Pillar C (primary), Pillar A (trigger policy)

The Drift Detection Module implements the trigger logic from Section 3.3.2:

- **Threshold Evaluation**: Compare metrics against predefined thresholds established in Pillar A governance. Thresholds include:
  - Residual exceedance (e.g., >2× rolling standard deviation)
  - Uncertainty inflation (e.g., variance >150% of baseline)
  - Distributional drift (e.g., KS test p-value <0.01)

- **Composite Drift Index**: Integrate multiple signals into a unified drift risk score. Require concurrent exceedance across multiple metric families to reduce false positives.

- **Persistence Filtering**: Require drift signals to persist for a minimum duration (e.g., 60-90 days) before triggering action, distinguishing transient anomalies from genuine degradation.

### 5.2.4 Trigger State Machine (Steps 2-3)

**Pillar(s) Served**: Pillar A, Pillar C

The state machine manages transitions between operational states:

```
┌─────────────────────────────────────────────────────────────────┐
│                    TRIGGER STATE MACHINE                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│    ┌──────┐                                                     │
│    │  OK  │◀──────────────────────────────────────┐             │
│    └──┬───┘                                       │             │
│       │ Drift detected                            │             │
│       ▼                                           │             │
│    ┌─────────┐                                    │             │
│    │ WARNING │                                    │             │
│    └────┬────┘                                    │             │
│         │ Drift persists + DECIDE approves        │             │
│         ▼                                         │             │
│    ┌─────────┐      Update succeeds      ┌───────┴───────┐     │
│    │ UPDATE  │──────────────────────────▶│ Return to OK  │     │
│    └────┬────┘                           └───────────────┘     │
│         │ Update fails validation                               │
│         ▼                                                       │
│    ┌──────────┐                                                 │
│    │ ESCALATE │──▶ Rollback + Full Retrain Required            │
│    └──────────┘                                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

- **OK**: Normal operations; surrogate meets acceptance criteria
- **WARNING**: Drift detected; monitoring intensified; evidence accumulating
- **UPDATE**: Governance approved; Phase 2 triggered
- **ESCALATE**: Update failed; surrogate withdrawn; physics-only mode

### 5.2.5 Decision Support Dashboard (Step 3: DECIDE)

**Pillar(s) Served**: Pillar A (primary)

The Decision Support Dashboard presents evidence for human governance review:

- **Diagnostic Summary**: Current state, drift indicators, confidence levels, and recommended action

- **Historical Context**: Performance trends, previous recalibration events, and their outcomes

- **Evidence Package**: All data supporting the recalibration recommendation, formatted for regulatory documentation

- **Decision Interface**: Approve/defer/reject options with required justification fields

**Human Decision Point**: The DECIDE step requires explicit human authorization before proceeding to Phase 2. The dashboard provides information; humans make the call.

---

## 5.3 Model Update Pipeline (Supports Steps 4-6)

This module implements the core of Phase 2—the triggered response that updates the surrogate when governance approves. It serves primarily **Pillar C (Recalibration Mechanisms)** and **Pillar B (Modeling Engines)**.

### 5.3.1 Active Learning Sampler (Step 4: PREPARE)

**Pillar(s) Served**: Pillar C

When new physics simulations are needed (simulation-driven pathway), the Active Learning Sampler selects informative scenarios:

- **Candidate Generation**: Create a pool of operationally relevant simulation scenarios representing current conditions and near-term management options

- **Uncertainty-Based Scoring**: Prioritize scenarios where the surrogate has high predictive uncertainty or where recent residuals are large

- **Diversity Constraints**: Ensure selected scenarios span hydraulic gradients, hydrostratigraphic units, and forcing conditions rather than clustering redundantly

- **Batch Selection**: Select 6-10 high-value simulations that collectively maximize expected information gain

- **Documentation**: Record selection rationale, expected uncertainty reduction, and operational relevance

### 5.3.2 Physics Model Interface (Step 4: PREPARE)

**Pillar(s) Served**: Pillar B

The Physics Model Interface manages communication with high-fidelity simulators (PFLOTRAN, MODFLOW, STOMP, etc.):

- **Input Generation**: Create simulator input files from scenario specifications

- **Job Submission**: Submit runs to HPC resources with appropriate scheduling and resource requests

- **Output Parsing**: Extract relevant fields (heads, concentrations, fluxes) from simulator outputs

- **Result Archiving**: Store simulation outputs with full provenance in the Data Management Layer

**Implementation Notes**:
- Supports multiple simulators through a common interface
- Handles file-based coupling (input files → run → output files)
- Manages parallel execution for batch scenarios

### 5.3.3 Continual Learning Trainer (Step 5: UPDATE)

**Pillar(s) Served**: Pillar C (primary), Pillar B (surrogate)

The Continual Learning Trainer updates surrogate weights using methods from Section 3.3.3:

- **Training Data Assembly**: Combine new physics outputs, recent field observations, and replay samples from historical cases (typically 70-75% replay ratio)

- **Selective Fine-Tuning**: Freeze early encoder layers to preserve structural representations; update later layers with small learning rate and regularization (EWC or L2 anchoring)

- **Early Stopping**: Monitor validation performance; stop when improvements plateau

- **Checkpoint Management**: Save model states at each epoch; retain best-performing checkpoint

**Two Update Pathways**:
1. **Observation-Driven**: When new field data alone is sufficient, skip active learning and physics runs; proceed directly to fine-tuning with observational data
2. **Simulation-Driven**: When new physics runs are needed, execute Steps 4a-4b before fine-tuning

### 5.3.4 UQ Calibration Module (Step 6: CALIBRATE)

**Pillar(s) Served**: Pillar C

After updating surrogate weights, uncertainty estimates must be recalibrated:

- **Coverage Evaluation**: Test whether updated model's uncertainty intervals achieve target coverage on held-out data

- **Calibration Adjustment**: If intervals are too narrow (under-coverage) or too wide (over-coverage), adjust uncertainty scaling factors

- **Method-Specific Procedures**:
  - MC-Dropout: Adjust dropout rate or number of forward passes
  - Deep Ensembles: Retrain ensemble members on updated data
  - Conformal Prediction: Recompute nonconformity scores on calibration set

- **Validation**: Confirm calibrated uncertainty meets acceptance criteria before proceeding to deployment

---

## 5.4 Deployment & Governance System (Supports Step 7)

This module implements the final step of Phase 2—validating and deploying the updated surrogate. It serves primarily **Pillar A (Governance)** with support from **Pillar C** for validation metrics.

### 5.4.1 Validation Engine (Step 7: DEPLOY)

**Pillar(s) Served**: Pillar A (criteria), Pillar C (metrics)

The Validation Engine verifies that the updated surrogate meets pre-registered acceptance criteria:

- **Accuracy Validation**: Compare updated model performance against acceptance thresholds (e.g., RMSE < X at priority wells)

- **UQ Validation**: Confirm uncertainty calibration meets coverage requirements (e.g., 95% intervals achieve ≥90% empirical coverage)

- **Stability Checks**: Verify that performance on historical test cases has not degraded (catastrophic forgetting detection)

- **Comparison Report**: Generate side-by-side comparison of pre-update vs. post-update performance

**Decision Point**: If validation fails, the update is rejected and the system transitions to ESCALATE state.

### 5.4.2 Model Registry (Step 7: DEPLOY)

**Pillar(s) Served**: Pillar A (versioning), Pillar B (storage)

The Model Registry provides version control for surrogate models:

- **Version Tracking**: Assign unique version identifiers to each trained model

- **Metadata Storage**: Record training data provenance, hyperparameters, validation results, and deployment dates

- **Model Retrieval**: Enable retrieval of any previous model version for comparison or rollback analysis

- **Promotion Workflow**: Manage transitions from "candidate" to "validated" to "operational" status

### 5.4.3 Audit Logger (All Steps)

**Pillar(s) Served**: Pillar A

The Audit Logger maintains comprehensive records for regulatory compliance:

- **Decision Logging**: Record all governance decisions (DECIDE approvals, validation outcomes, deployment authorizations)

- **Data Provenance**: Track which observations, simulations, and training data contributed to each model version

- **Change History**: Document what triggered each update, what data was used, and how performance changed

- **Retention Policy**: Retain logs for project lifetime per DOE quality assurance requirements

### 5.4.4 Rollback Manager (Step 7: DEPLOY)

**Pillar(s) Served**: Pillar A

The Rollback Manager handles failed validations:

- **Rollback Trigger**: Activated when updated surrogate fails acceptance criteria

- **Surrogate Withdrawal**: Remove failed surrogate from operational use; do NOT revert to previous version (per Section 3.1.5 governance)

- **Physics-Only Mode**: Transition to high-fidelity physics model for all decision support until new surrogate is available

- **Escalation Notification**: Alert governance team that full retraining is required

- **Documentation**: Record rollback rationale, failed validation results, and escalation plan

---

## 5.5 Infrastructure & Development Phases

This section describes cross-cutting infrastructure and the phased development approach.

### 5.5.1 Data Management and Provenance

**Pillar(s) Served**: All Pillars

The Data Management Layer underlies all components:

- **Observation Storage**: Field measurements, laboratory results, sensor data with quality flags and timestamps

- **Simulation Archive**: Physics model inputs, outputs, and metadata for all runs

- **Model Repository**: Trained surrogate weights, configurations, and validation results

- **Audit Trail**: Complete record of all system actions, decisions, and data flows

**Provenance Requirements**:
- Every prediction traceable to its model version and input data
- Every recalibration decision reconstructable from archived evidence
- Every model version retrievable with full training history

### 5.5.2 HPC Integration

**Pillar(s) Served**: Pillar B

Physics simulations and surrogate training require high-performance computing:

- **Job Scheduling**: Interface with HPC batch schedulers (SLURM, PBS) for physics runs

- **GPU Access**: Manage GPU resources for surrogate training and inference

- **Data Transfer**: Move large datasets between HPC storage and operational systems

- **Resource Monitoring**: Track computational costs and optimize resource utilization

### 5.5.3 API Design

**Pillar(s) Served**: All Pillars

Standardized interfaces enable modularity and extensibility:

- **Simulator Interface**: Common API for different physics simulators (PFLOTRAN, MODFLOW, STOMP)

- **Surrogate Interface**: Standard interface for different surrogate architectures (U-FNO, U-Net, etc.)

- **Metric Interface**: Pluggable metrics for drift detection and validation

- **Data Interface**: Consistent data formats for observations, simulations, and model artifacts

### 5.5.4 Development Phases

Implementation proceeds in three phases:

#### Phase 1: Prototype Demonstration (Current)

**Goal**: Demonstrate that the recalibration concept works

**Deliverables**:
- Single surrogate architecture (U-FNO for 2D cross-section, U-Net for pump-and-treat)
- Manual recalibration workflow documented in Jupyter notebooks
- Before/after demonstration showing performance improvement after update

**Characteristics**:
- No persistent software system
- Researcher executes each step manually
- Focus on proving the concept

#### Phase 2: Integrated Framework

**Goal**: Create reusable software components

**Deliverables**:
- Modular Python packages for each core component
- Automated drift detection running on schedule
- Scripted recalibration workflow with minimal manual intervention
- Configuration management for model versions and parameters

**Characteristics**:
- Requires technically skilled operator (Python, command-line)
- Routine operations largely automated
- Operator role shifts to reviewing outputs and making decisions

#### Phase 3: Operational System

**Goal**: Deployable system for EM site operations

**Deliverables**:
- Persistent monitoring service running continuously
- Web-based user interface for analysts and managers
- Multi-surrogate support with coordinated monitoring
- Integration with site data systems

**Characteristics**:
- Operable by staff who are not ML specialists
- Full governance workflow with decision support
- Production-ready reliability and documentation

### 5.5.5 Quality Assurance Alignment

DOE quality assurance requirements (DOE O 414.1D, NQA-1) apply to software used in decision support:

- **Configuration Control**: Every deployed component has defined version; changes documented and reviewed

- **Verification and Validation**: Each component tested against acceptance criteria before deployment

- **Traceability**: Audit logs record data used, computations performed, and results produced

- **Corrective Action**: Procedures define how problems are diagnosed, fixes implemented, and effectiveness verified

The architecture makes compliance straightforward by embedding governance requirements throughout rather than treating them as an afterthought.

---

## 5.6 Summary

The software architecture translates the three-pillar framework and seven-step workflow into implementable components:

| Workflow Phase | Software System | Key Modules | Primary Pillars |
|----------------|-----------------|-------------|-----------------|
| Phase 1 (Steps 1-3) | Monitoring & Detection | Performance Tracker, Drift Detection, Decision Dashboard | A, C |
| Phase 2 (Steps 4-6) | Model Update Pipeline | Active Learning, Physics Interface, Continual Learning | B, C |
| Phase 2 (Step 7) | Deployment & Governance | Validation Engine, Model Registry, Audit Logger | A, B |
| Cross-Cutting | Infrastructure | Data Management, HPC Integration, APIs | All |

The phased development approach delivers value incrementally: prototype demonstration (Phase 1), integrated framework (Phase 2), and operational system (Phase 3). Throughout, the architecture maintains alignment with DOE governance requirements and the core principle that **pillars define WHAT resources exist; the workflow defines HOW they are used**.

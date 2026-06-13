# Section 4 Revision Plan (REVISED)

**Date:** 2026-03-23
**Status:** DRAFT v2 - Awaiting User Approval

---

## 1. Design Constraints

### 1.1 Established Framework Structure (DO NOT CHANGE)

The document has an established organizational structure that must be preserved:

- **3 Pillars** (management domains): Governance (A), Modeling Engines (B), Recalibration Mechanisms (C)
- **7 Steps** (workflow): MONITOR → DETECT → DECIDE → PREPARE → UPDATE → CALIBRATE → DEPLOY
- **2 Phases**: Continuous Monitoring (Steps 1-3) + Triggered Response (Steps 4-7)

**CRITICAL**: We must NOT introduce new organizational schemes (like "5 computational components") that would confuse readers. Section 4 must use the same pillars + workflow structure.

### 1.2 Section 4's Role in the Document

Looking at the document flow:
- **Section 2**: Defines the framework (pillars + workflow) - WHAT the framework is
- **Section 3**: Details the methods organized by pillar - HOW each pillar works technically
- **Section 4**: Implementation roadmap - HOW to build and deploy the system over time
- **Section 5**: Prototype & Case Study - DEMONSTRATION of the framework
- **Section 6**: Future Work - WHERE we go next

Section 4 should focus on **development needs and phased implementation**, not re-explaining methods or inventing new organizational structures.

### 1.3 Problems with Current Section 4

1. **Over-repetition of Section 3**: Table 4.1 and subsections re-explain methods already detailed in Section 3
2. **Missing development phases detail**: The original had excellent Phase 1/2/3 structure with objectives, scope, and success criteria
3. **Missing operational modes**: Offline (development) vs Online (operations) distinction is valuable
4. **Missing human decision points emphasis**: Where human judgment is required
5. **Missing technical considerations**: Computational requirements, interoperability, QA alignment

### 1.4 What to Preserve

- Workflow-centric organization (aligns with Section 2.2)
- Pillar awareness (aligns with Section 2.1)
- Governance integration emphasis
- Trigger state logic (OK → WARNING → UPDATE → ESCALATE)

---

## 2. Proposed New Structure for Section 4

```
4. Implementation Roadmap

[Leading paragraphs - no separate 4.0]
    - Purpose: translate framework into operational system
    - Balance scientific workflow with DOE governance requirements
    - Reference to pillars (Section 2.1) and workflow (Section 2.2)

4.1 System Requirements
    4.1.1 Operational Modes
          - Offline mode (initial development, HPC-intensive)
          - Online mode (operational deployment, faster turnaround)
          - Transitions between modes
    4.1.2 Pillar-Based Capabilities
          - What Pillar A requires (governance infrastructure)
          - What Pillar B requires (physics + surrogate infrastructure)
          - What Pillar C requires (monitoring + adaptation infrastructure)
    4.1.3 Workflow Support
          - Phase 1 capabilities (Steps 1-3)
          - Phase 2 capabilities (Steps 4-7)
          - Brief references to Section 3 methods (NOT re-explanations)

4.2 Human Decision Points
    4.2.1 Recalibration Approval (Step 3: DECIDE)
    4.2.2 Acceptance Criteria Definition (Pillar A)
    4.2.3 Rollback Decisions (Step 7: DEPLOY failure)
    4.2.4 Full Retraining Triggers (ESCALATE state)

4.3 Development Phases
    4.3.1 Phase 1: Prototype Demonstration
          - Objective, Scope, Deliverables, Success Criteria
    4.3.2 Phase 2: Integrated Framework
          - Objective, Scope, Deliverables, Success Criteria
    4.3.3 Phase 3: Operational System
          - Objective, Scope, Deliverables, Success Criteria

4.4 Technical Considerations
    4.4.1 Computational Requirements
    4.4.2 Interoperability
    4.4.3 Quality Assurance Alignment

4.5 Summary
```

---

## 3. Key Changes from Current Section 4

### 3.1 Remove (Too Repetitive)

| Current Content | Action | Reason |
|-----------------|--------|--------|
| Table 4.1 detailed method mapping | Remove or drastically simplify | Re-explains Section 3 |
| 4.2.1 detailed UQ method descriptions | Remove | Already in Section 3.3.1 |
| 4.2.2 detailed drift detection descriptions | Remove | Already in Section 3.3.2 |
| 4.3.1 detailed active learning descriptions | Remove | Already in Section 3.3.4 |
| 4.3.2 detailed continual learning descriptions | Remove | Already in Section 3.3.3 |
| 4.3.3 detailed UQ recalibration descriptions | Remove | Already in Section 3.3.1 |

### 3.2 Add (From Original Section 5)

| New Content | Source | Reason |
|-------------|--------|--------|
| Operational Modes (Offline/Online) | Original 5.2 | Critical operational concept |
| Human Decision Points section | Original 5.3 | Governance emphasis |
| Detailed Development Phases | Original 5.4 | **Critical roadmap content** |
| Technical Considerations | Original 5.5 | Practical implementation |

### 3.3 Do NOT Add

| Content | Reason |
|---------|--------|
| "5 computational components" | Would conflict with 3 pillars structure |
| Open Design Questions | Move to Section 6 (Future Work) or remove |
| Detailed software specifications | This is framework design, not software spec |

---

## 4. Detailed Content Outline

### Leading Paragraphs (no section number)

```markdown
This section describes how the three-pillar framework (Section 2.1) and
seven-step workflow (Section 2.2) translate into an operational system.
Rather than prescribing specific software tools, we focus on what
capabilities are needed and how they should be developed over time.

The implementation must satisfy two demands: (1) support the scientific
workflow of monitoring, detecting drift, and executing recalibration;
and (2) meet DOE governance requirements for traceability, reproducibility,
and quality assurance.
```

### 4.1 System Requirements

#### 4.1.1 Operational Modes

**Offline Mode** (Initial Development):
- Generate training ensembles with physics model (Pillar B)
- Train surrogate, calibrate UQ, validate (Pillar B + C)
- Computationally intensive (HPC, GPU)
- Not time-critical

**Online Mode** (Operations):
- Surrogate generates predictions on demand (Pillar B)
- Monitoring tracks performance (Pillar C)
- Recalibration triggered when needed (Pillar C + A)
- Faster turnaround required

**Transitions**: Architecture must support smooth transitions between modes.

#### 4.1.2 Pillar-Based Capabilities

What each pillar requires for implementation:

**Pillar A (Governance) requires:**
- Configuration management for model versions
- Audit logging for all decisions
- Documentation generation for regulatory compliance
- Human review interfaces for DECIDE step

**Pillar B (Modeling Engines) requires:**
- Physics model interface (PFLOTRAN, MODFLOW, STOMP, etc.)
- Surrogate training and inference infrastructure
- Model versioning and artifact storage
- Data management for simulations and observations

**Pillar C (Recalibration Mechanisms) requires:**
- UQ computation infrastructure
- Drift detection and monitoring
- Active learning for scenario selection
- Continual learning for model updates

#### 4.1.3 Workflow Support

**Phase 1 (Continuous Monitoring - Steps 1-3):**
- Automated comparison of predictions vs observations
- Drift detection against thresholds from Pillar A
- Evidence packaging for governance review
- Methods: See Section 3.3.1 (UQ) and Section 3.3.2 (Trigger Logic)

**Phase 2 (Triggered Response - Steps 4-7):**
- Data preparation with active learning
- Surrogate fine-tuning with continual learning
- UQ recalibration
- Validation and deployment with audit trail
- Methods: See Section 3.3.3-3.3.6

**Trigger State Logic**: OK → WARNING → UPDATE → ESCALATE (per Section 2.2)

### 4.2 Human Decision Points

Four explicit decision points where human judgment is required:

#### 4.2.1 Recalibration Approval (Step 3: DECIDE)
Even when automated diagnostics indicate drift, the decision to update a surrogate involves human review. The monitoring system provides evidence; humans make the call. This is both a governance requirement and a practical safeguard against false alarms.

#### 4.2.2 Acceptance Criteria Definition (Pillar A)
Humans define what "good enough" means for a given application—the error thresholds, uncertainty coverage requirements, and performance metrics that determine whether a surrogate is fit for purpose. The system evaluates against these criteria, but setting them requires understanding of site-specific risks and regulatory context.

#### 4.2.3 Rollback Decisions (Step 7: DEPLOY failure)
When an updated surrogate fails validation, rollback means withdrawing the surrogate from operational use and reverting to physics-only analysis (per Section 3.1.5). This is a significant operational change that requires human authorization and documentation.

#### 4.2.4 Full Retraining Triggers (ESCALATE state)
When incremental updates repeatedly fail or when site conditions change fundamentally, the decision to abandon the current surrogate and retrain from scratch involves judgment about whether the surrogate's foundational assumptions remain valid. This decision has major resource implications and should not be automated.

### 4.3 Development Phases

Implementation proceeds through three phases, progressively building capability and confidence:

#### 4.3.1 Phase 1: Prototype Demonstration

**Objective**: Demonstrate one complete recalibration cycle on a synthetic test case.

**Scope**:
- Single surrogate architecture (U-FNO or U-Net)
- Basic UQ using MC-Dropout or deep ensembles
- Simple drift detection (threshold-based)
- Manual governance decisions
- Documented in Jupyter notebooks or Python scripts

**Deliverables**:
- Working code demonstrating before/after performance
- Documentation of each workflow step
- Small demonstration showing surrogate update in response to simulated drift

**Success Criteria**: Complete MONITOR → DETECT → DECIDE → PREPARE → UPDATE → CALIBRATE → DEPLOY cycle with documented performance improvement.

**Note**: At this phase, there is no persistent software system—just reproducible code that proves the concept.

#### 4.3.2 Phase 2: Integrated Framework

**Objective**: Create reusable software components with realistic site data.

**Scope**:
- Modular Python packages with documented interfaces and test coverage
- Automated drift detection running on schedule
- Scripted recalibration workflow with minimal manual effort
- Configuration management for model versions and data provenance
- Multiple surrogate architecture options

**Deliverables**:
- Installable packages that can be used independently or together
- Automated diagnostic reports
- Governance dashboard prototype for decision support

**Success Criteria**: Framework operates on representative site data with governance-compliant documentation.

**Note**: System still requires technically skilled operator comfortable with Python and command-line tools, but routine operations are largely automated.

#### 4.3.3 Phase 3: Operational System

**Objective**: Deploy framework for operational use at DOE EM sites.

**Scope**:
- Persistent monitoring service running continuously
- User interface (likely web-based) for non-ML specialists
- Multi-surrogate support for different prediction tasks
- Integration with site monitoring databases and sensor networks
- Full regulatory documentation meeting DOE QA requirements

**Deliverables**:
- Production-quality implementation
- Training materials for site operators
- Maintenance and support procedures

**Success Criteria**: Framework accepted for operational use under DOE quality assurance requirements.

**Note**: This phase requires significant software engineering effort and should be informed by experience from earlier phases.

### 4.4 Technical Considerations

#### 4.4.1 Computational Requirements

| Task | Resources | Typical Time |
|------|-----------|--------------|
| Physics simulations | HPC with batch scheduling | Minutes to hours per run |
| Training ensemble generation | HPC (hundreds to thousands of runs) | Days to weeks |
| Initial surrogate training | GPU | Hours |
| Fine-tuning for recalibration | GPU (beneficial but not required) | Minutes to hour |
| Inference and monitoring | Standard compute | Milliseconds per prediction |

The architecture should not assume all components run on the same hardware. Physics simulations may run on one HPC system, training on another, and monitoring on a third.

#### 4.4.2 Interoperability

**Simulator Coupling**: Physics simulators were not designed with ML workflows in mind. The framework must work with simulators through file-based interfaces: generate input files, run the simulator, parse output files. This is practical given the diversity of simulators across EM sites.

**Data Formats**: Read native formats where possible (PFLOTRAN HDF5, MODFLOW binary). For internal data (trained models, diagnostic logs, configuration files), use standard formats.

**Reproducibility**: Every result must be regenerable from archived inputs. This means versioning code, training data, model weights, configuration files, and random seeds.

#### 4.4.3 Quality Assurance Alignment

DOE quality assurance requirements (DOE O 414.1D, NQA-1) apply to software used in decision support:

| Requirement | Implementation |
|-------------|----------------|
| Configuration control | Every deployed component has defined version; changes documented and reviewed |
| Verification and validation | Each component tested against acceptance criteria before deployment |
| Traceability | Audit logs record data used, computations performed, results produced |
| Corrective action | Procedures define how problems are diagnosed and fixes verified |

These requirements constrain how software is developed and operated. The architecture should make compliance straightforward rather than burdensome.

### 4.5 Summary

This implementation roadmap translates the three-pillar framework and seven-step workflow into operational capabilities:

1. **Pillar-aligned requirements**: Capabilities organized around what each pillar needs
2. **Operational modes**: Offline development and online operations with smooth transitions
3. **Human decision points**: Four explicit points where human judgment is required
4. **Phased development**: Progressive build-up from prototype to operational system
5. **Technical grounding**: Computational requirements, interoperability, and QA alignment

The framework enables adaptive surrogate management that maintains prediction accuracy over multi-year remediation timelines while meeting DOE quality assurance and regulatory requirements.

---

## 5. Comparison: Current vs Proposed

| Aspect | Current Section 4 | Proposed Section 4 |
|--------|-------------------|-------------------|
| Organizational scheme | Introduces workflow capabilities | Uses established pillars + workflow |
| Section 3 repetition | High (Table 4.1, detailed descriptions) | Minimal (brief references only) |
| Operational modes | Missing | Offline/Online defined |
| Human decision points | Embedded in workflow | Dedicated section |
| Development phases | Brief (4.5) | Detailed with objectives, scope, criteria |
| Technical considerations | Brief (4.4) | Expanded with tables |
| Open questions | Missing | Removed (belongs in Section 6) |
| Consistency with Section 2 | Partial | Full alignment |

---

## 6. Implementation Approach

### Step 1: Write Leading Paragraphs
- Brief introduction connecting to Sections 2.1 and 2.2
- No separate section number

### Step 2: Write 4.1 System Requirements
- Operational modes (Offline/Online)
- Pillar-based capabilities (what each pillar needs)
- Workflow support (brief, reference Section 3)

### Step 3: Write 4.2 Human Decision Points
- Four decision points from original Section 5.3
- Connect to workflow steps and pillars

### Step 4: Write 4.3 Development Phases
- Detailed Phase 1/2/3 from original Section 5.4
- Include objectives, scope, deliverables, success criteria

### Step 5: Write 4.4 Technical Considerations
- Computational requirements table
- Interoperability discussion
- QA alignment table

### Step 6: Write 4.5 Summary
- Key points recap

---

## 7. Approval Request

Please review this revised plan and confirm:

1. Is the proposed structure acceptable (no "5 components", uses pillars + workflow)?
2. Is the level of detail appropriate for development phases?
3. Should human decision points be a separate section or integrated elsewhere?
4. Any other content to add or remove?

Once approved, I can switch to Code mode to implement the revised Section 4.

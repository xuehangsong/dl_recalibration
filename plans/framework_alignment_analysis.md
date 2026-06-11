# Framework Alignment Analysis: Three Pillars, Seven Steps, and Software Components

**Date**: 2026-03-18  
**Purpose**: Resolve structural confusion between the three organizational schemes in the recalibration framework document

---

## 1. Current State: Three Overlapping Organizational Schemes

### Scheme 1: Three Pillars (Conceptual Architecture)

**Pillar A: Conceptual Design & Governance**
- Objectives, success metrics, regulatory requirements
- Trigger criteria for model updates
- Data policies and interpretability standards
- Ensures alignment with DOE mission goals and compliance

**Pillar B: Modeling Engines**
- High-fidelity physics-based simulator (PFLOTRAN, MODFLOW, etc.)
- DL surrogate architectures (U-Net, U-FNO, LSTM, etc.)
- Training data generation and model validation

**Pillar C: Recalibration Mechanisms**
- Uncertainty quantification (UQ)
- Active learning workflows
- Continual learning methods
- Drift detection and monitoring

### Scheme 2: Seven-Step Operational Workflow

1. **Monitor** - Track surrogate predictions vs. observations, calculate residuals and uncertainty
2. **Detect** - Identify when surrogate begins to fail using automated diagnostics
3. **Select** (optional) - Active learning identifies most informative new simulation scenarios
4. **Simulate** (optional) - Execute targeted physics runs
5. **Fine-tune** - Update DL surrogate using continual learning methods
6. **Recalibrate UQ** - Update uncertainty estimates for the revised model
7. **Redeploy** - Deploy improved surrogate with audit trails

### Scheme 3: Five Software Components (Section 5 Draft)

1. **Physics Model Interface** - Manages communication with high-fidelity simulators
2. **Surrogate Model Engine** - Handles surrogate training, storage, and inference
3. **Monitoring and Diagnostics Module** - Tracks predictions, calculates uncertainty, detects drift
4. **Recalibration Orchestrator** - Coordinates Steps 3-7 of the workflow
5. **Data Management Layer** - Stores observations, simulations, models, audit logs

---

## 2. The Confusion: Misalignment Analysis

### Problem 1: Unclear Relationship Between Pillars and Components

The five software components don't map cleanly to the three pillars:

| Software Component | Maps to Pillar? | Issue |
|-------------------|-----------------|-------|
| Physics Model Interface | Pillar B (partially) | Only covers physics side, not surrogate |
| Surrogate Model Engine | Pillar B (partially) | Only covers surrogate side, not physics |
| Monitoring & Diagnostics | Pillar C (partially) | Only covers monitoring, not active/continual learning |
| Recalibration Orchestrator | Pillar C (partially) + Pillar A (partially) | Spans multiple pillars, unclear boundaries |
| Data Management Layer | All pillars? | Cross-cutting concern, not a pillar |

**Result**: The 5 components create a parallel structure that doesn't reinforce the 3-pillar conceptual model.

### Problem 2: Seven Steps Don't Map Clearly to Five Components

| Step | Which Component(s)? | Issue |
|------|-------------------|-------|
| 1. Monitor | Monitoring & Diagnostics | Clear |
| 2. Detect | Monitoring & Diagnostics | Clear |
| 3. Select | Recalibration Orchestrator? | Unclear - is this a separate module? |
| 4. Simulate | Physics Model Interface | Clear |
| 5. Fine-tune | Surrogate Model Engine | Clear |
| 6. Recalibrate UQ | Monitoring & Diagnostics? Surrogate Engine? | Unclear ownership |
| 7. Redeploy | Recalibration Orchestrator? Surrogate Engine? | Unclear ownership |

**Result**: Steps 3, 6, and 7 have ambiguous ownership across components.

### Problem 3: Pillar A (Governance) Has No Clear Software Representation

Pillar A defines:
- Acceptance criteria
- Trigger thresholds
- Rollback policies
- Audit requirements

But in the 5-component model:
- No "Governance Module" exists
- Governance is scattered across Orchestrator, Monitoring, and Data Management
- No clear place to configure policies or review decisions

**Result**: The most important pillar for DOE compliance has the weakest software representation.

---

## 3. Root Cause Analysis

The confusion stems from **mixing abstraction levels**:

- **Pillars** = Conceptual/functional domains (WHAT the framework does)
- **Steps** = Temporal workflow (WHEN things happen)
- **Components** = Software modules (HOW it's implemented)

These are three different views of the same system, but the document treats them as parallel structures rather than complementary perspectives.

---

## 4. Proposed Resolution: Unified Framework Architecture

### Option A: Pillars as Primary Organizing Principle (RECOMMENDED)

**Structure the entire document around the three pillars**, with steps and components as subordinate concepts:

```
Section 2: Framework Overview
  2.1 Three-Pillar Architecture (conceptual)
  2.2 Seven-Step Operational Workflow (how pillars interact)

Section 3: Methods (detailed pillar descriptions)
  3.1 Pillar A: Governance Essentials
  3.2 Pillar B: Modeling Engines
  3.3 Pillar C: Recalibration Mechanisms

Section 5: Implementation Roadmap
  5.1 Software Architecture Overview
      - Map pillars → software modules
      - Show how 7 steps flow through modules
  5.2 Pillar A Implementation (Governance Layer)
  5.3 Pillar B Implementation (Modeling Layer)
  5.4 Pillar C Implementation (Recalibration Layer)
  5.5 Cross-Cutting Concerns (Data Management, HPC Integration)
  5.6 Development Phases
```

**Advantages**:
- Maintains conceptual clarity from Section 2 through Section 5
- Each pillar has clear software representation
- Steps are shown as workflow that traverses pillars
- Easier for readers to understand the "why" before the "how"

**Disadvantages**:
- Requires restructuring Section 5 significantly
- Some software concerns (data management, HPC) don't fit neatly into pillars

### Option B: Steps as Primary Organizing Principle

Structure around the operational workflow:

```
Section 5: Implementation Roadmap
  5.1 Step 1-2 Implementation: Monitoring & Detection
  5.2 Step 3-4 Implementation: Active Learning & Simulation
  5.3 Step 5-6 Implementation: Fine-tuning & UQ Recalibration
  5.4 Step 7 Implementation: Redeployment & Governance
  5.5 Supporting Infrastructure
```

**Advantages**:
- Follows the temporal flow of operations
- Clear "what happens when"

**Disadvantages**:
- Loses the conceptual clarity of pillars
- Harder to see the big picture
- Governance becomes an afterthought (Step 7) rather than foundational

### Option C: Hybrid - Pillars for Concepts, Layers for Software

Keep pillars conceptual, but introduce **software layers** that map more naturally to implementation:

```
Section 2: Framework Overview
  2.1 Three Pillars (conceptual)
  2.2 Seven Steps (workflow)

Section 5: Implementation Roadmap
  5.1 Software Architecture Overview
  5.2 Four Software Layers:
      - Governance & Policy Layer (Pillar A)
      - Modeling & Simulation Layer (Pillar B)
      - Adaptation & Learning Layer (Pillar C)
      - Data & Infrastructure Layer (cross-cutting)
  5.3 Workflow Execution Across Layers
  5.4 Development Phases
```

**Advantages**:
- Cleaner mapping: 3 pillars → 3 functional layers + 1 infrastructure layer
- Governance gets first-class treatment
- Steps shown as cross-layer workflow

**Disadvantages**:
- Introduces yet another term ("layers") that needs explanation

---

## 5. Detailed Mapping: Option A (Recommended)

### Pillar A → Governance Layer (Software)

**Responsibilities**:
- Store and enforce acceptance criteria
- Evaluate trigger conditions
- Log all recalibration decisions
- Manage rollback procedures
- Generate audit reports

**Software Modules**:
- Policy Configuration Service
- Decision Review Dashboard
- Audit Trail Database
- Compliance Reporting Engine

**Workflow Steps Supported**: Steps 2 (Detect - applies triggers), 7 (Redeploy - enforces governance)

---

### Pillar B → Modeling Layer (Software)

**Responsibilities**:
- Execute physics simulations
- Train and store surrogate models
- Perform inference
- Version control for models

**Software Modules**:
- Physics Model Interface (PFLOTRAN, MODFLOW connectors)
- Surrogate Model Registry (stores trained models)
- Inference Engine (fast prediction service)
- Training Pipeline (offline surrogate development)

**Workflow Steps Supported**: Steps 4 (Simulate), 5 (Fine-tune - partially)

---

### Pillar C → Adaptation Layer (Software)

**Responsibilities**:
- Monitor surrogate performance
- Quantify uncertainty
- Detect drift
- Select new training scenarios (active learning)
- Update models (continual learning)
- Recalibrate uncertainty estimates

**Software Modules**:
- Performance Monitoring Service
- Uncertainty Quantification Engine
- Drift Detection Module
- Active Learning Sampler
- Continual Learning Trainer
- UQ Recalibration Service

**Workflow Steps Supported**: Steps 1 (Monitor), 2 (Detect), 3 (Select), 5 (Fine-tune - partially), 6 (Recalibrate UQ)

---

### Cross-Cutting: Data & Infrastructure Layer

**Responsibilities**:
- Store all data (observations, simulations, models)
- Manage HPC job submission
- Provide APIs for inter-module communication
- Handle authentication and access control

**Software Modules**:
- Operational Database (time-series observations)
- Model Repository (trained surrogates, physics model configs)
- HPC Job Scheduler Interface
- API Gateway
- Authentication Service

**Workflow Steps Supported**: All steps (provides data and compute infrastructure)

---

## 6. Revised Section Structure Proposal

### Section 2: Framework Overview

**2.1 Three-Pillar Architecture**
- Pillar A: Governance (the "why" and "when")
- Pillar B: Modeling Engines (the "what")
- Pillar C: Recalibration Mechanisms (the "how")
- [Add diagram showing pillars and their relationships]

**2.2 Seven-Step Operational Workflow**
- Describe the workflow as a cycle that traverses the three pillars
- [Add flowchart showing steps flowing through pillars]
- Clarify: Steps 3-4 are optional (triggered by Step 2 detection)

### Section 5: Implementation Roadmap

**5.0 Introduction**
- Explain that implementation translates the three pillars into software
- Preview the four-layer software architecture

**5.1 Software Architecture Overview**
- Four-layer architecture diagram
- Mapping table: Pillars → Software Layers → Modules
- Workflow execution diagram: 7 Steps → Software Modules

**5.2 Governance Layer (Pillar A Implementation)**
- Policy configuration and enforcement
- Decision review and approval workflows
- Audit trail and compliance reporting
- Human decision points

**5.3 Modeling Layer (Pillar B Implementation)**
- Physics model interface and job management
- Surrogate model registry and versioning
- Training pipeline (offline)
- Inference engine (online)

**5.4 Adaptation Layer (Pillar C Implementation)**
- Monitoring and diagnostics
- Uncertainty quantification
- Drift detection and trigger evaluation
- Active learning and scenario selection
- Continual learning and fine-tuning
- UQ recalibration

**5.5 Data & Infrastructure Layer**
- Data management and provenance
- HPC integration
- API design and inter-module communication
- Operational modes (offline vs. online)

**5.6 Development Phases**
- Phase 1: Prototype Demonstration
- Phase 2: Integrated Framework
- Phase 3: Operational System

**5.7 Technical Considerations**
- Computational requirements
- Interoperability
- Quality assurance alignment

**5.8 Open Design Questions**

---

## 7. Key Decisions Needed

### Decision 1: Terminology
- Should we call them "layers", "modules", "subsystems", or something else?
- **Recommendation**: Use "software layers" to distinguish from conceptual "pillars"

### Decision 2: Governance Representation
- Should Governance be a separate software layer or integrated into other layers?
- **Recommendation**: Make it a first-class layer to emphasize DOE compliance requirements

### Decision 3: Section 2 Revision
- Does Section 2 need revision to clarify pillar-step relationships?
- **Recommendation**: Yes - add explicit mapping diagrams in Section 2.2

### Decision 4: Methods Section (Section 3)
- Should Section 3 be reorganized to match the pillar structure?
- **Current**: 3.1 Governance, 3.2 Modeling Engines, 3.3 Recalibration (already aligned!)
- **Recommendation**: Keep Section 3 as-is, it's already well-structured

---

## 8. Proposed Alignment Table

| Conceptual Pillar | Software Layer | Key Modules | Workflow Steps |
|------------------|----------------|-------------|----------------|
| **Pillar A: Governance** | Governance Layer | Policy Config, Decision Review, Audit Trail | Steps 2 (trigger eval), 7 (approval) |
| **Pillar B: Modeling Engines** | Modeling Layer | Physics Interface, Surrogate Registry, Inference Engine | Steps 4 (simulate), 5 (train) |
| **Pillar C: Recalibration** | Adaptation Layer | Monitoring, UQ, Drift Detection, Active Learning, Continual Learning | Steps 1, 2, 3, 5, 6 |
| **(Cross-cutting)** | Data & Infrastructure | Database, Model Repo, HPC Interface, APIs | All steps |

---

## 9. Visual Diagrams Needed

1. **Pillar Relationship Diagram** (Section 2.1)
   - Show three pillars and their interactions
   - Indicate feedback loops

2. **Workflow-Pillar Mapping** (Section 2.2)
   - Flowchart of 7 steps
   - Color-code by pillar
   - Show optional paths (Steps 3-4)

3. **Software Architecture Diagram** (Section 5.1)
   - Four-layer architecture
   - Show modules within each layer
   - Indicate data flows and APIs

4. **Workflow Execution Diagram** (Section 5.1)
   - Sequence diagram showing how 7 steps execute across software modules
   - Include human decision points

---

## 10. Next Steps

1. **Get user approval** on Option A (Pillar-based organization)
2. **Create visual diagrams** for Section 2 and Section 5
3. **Revise Section 2.2** to add explicit pillar-step mapping
4. **Completely rewrite Section 5** following the new structure
5. **Update Section 3** subsection titles if needed for consistency
6. **Add cross-references** throughout the document to reinforce alignment

---

## 11. Questions for User

1. Do you agree with **Option A** (Pillar-based organization) as the primary structure?
2. Should we introduce "software layers" as distinct from "pillars", or use different terminology?
3. Does the four-layer architecture (Governance, Modeling, Adaptation, Data/Infrastructure) make sense?
4. Should Section 2 be revised to add the mapping diagrams, or keep it as-is?
5. Are there any other organizational concerns I haven't addressed?

---

**End of Analysis**



# Framework Design Decisions — Authoritative Reference
# =====================================================
# STATUS: FINAL
# RULE: Read this file FIRST before modifying any document.
# RULE: Do NOT change decisions below without explicit user approval.
# RULE: Do NOT invent new organizational schemes beyond what is here.
# RULE: Do NOT modify `plans/framework_alignment_analysis.md` (historical)
# RULE: Do NOT modify `plans/framework_alignment_analysis_v2.md` (historical)
# RULE: Do NOT overwrite `manuscript/Framework_draft.docx` (original)
# Last updated: 2025-03-18
# Version: FINAL (supersedes all previous analysis versions)

═══════════════════════════════════════════════════════════════════
                    TABLE OF CONTENTS
═══════════════════════════════════════════════════════════════════

0.  Background & Problem Statement
1.  Core Principle (THE KEY INSIGHT)
2.  The Three Pillars (Management Domains)
3.  The Recalibration Workflow (7 Steps, 2 Phases)
4.  Cross-Reference Diagrams
5.  Document Structure Decisions (Section by Section)
6.  Existing Figures — Preserve or Update
7.  Terminology Decisions
8.  Things to PRESERVE (Do NOT Change)
9.  Things to AVOID
10. File Management Rules
11. Previous Analyses (Historical Context)

═══════════════════════════════════════════════════════════════════


---

## 0. Background & Problem Statement

This framework addresses: **How do you maintain a DL surrogate's 
predictive accuracy when the environmental system it models is 
non-stationary?**

The framework's core contribution is NOT building surrogates 
(well-established) or running physics models (standard practice). 
The contribution is **the systematic approach to keeping surrogates 
accurate over operational timescales** for DOE environmental 
management sites.

The original document states:
> "The framework is organized around three core pillars that interact 
> in a feedback loop. A Conceptual Governance pillar sets objectives, 
> success metrics and regulatory constraints... A Modeling Engines 
> pillar includes the physics-based simulator... A Recalibration 
> Mechanisms pillar continuously monitors surrogate performance... 
> By integrating these pillars in a dynamic feedback loop, the project 
> balances physical consistency, computational efficiency, and 
> adaptability."

The framework serves three audiences:
- **DOE reviewers**: governance, compliance, accountability
- **Environmental scientists**: physical realism, model validity, UQ
- **ML researchers**: technical novelty, continual learning, drift

---

## 1. Core Principle (THE KEY INSIGHT)

The framework has TWO distinct concepts that were previously tangled:

> **"The three pillars define WHAT the framework manages;  
> the recalibration workflow defines HOW these elements interact  
> during operations. Each workflow step draws resources, methods,  
> or constraints from one or more pillars."**

| Concept      | What It Is                    | Analogy                    |
|-------------|-------------------------------|----------------------------|
| **Pillars** | Management Domains (static)   | Departments in an org      |
|             | What you organize & maintain  | Places that hold things    |
| **Workflow**| Operational Sequence (dynamic)| Business process           |
|             | What actually happens         | Crosses all departments    |

These are COMPLEMENTARY, not redundant:
- The workflow TRAVERSES all three pillars
- No single pillar "owns" the workflow
- Each workflow step reaches into one or more pillars for what it needs

### Why This Matters
Previously, the document had three overlapping organizational schemes 
(3 pillars, 7 steps, 5 software components) that didn't align cleanly. 
The confusion arose because:
- Pillar C (Recalibration Mechanisms) was doing double duty — it was 
  described as both a management domain AND essentially the workflow itself
- Readers couldn't tell: How do 5 components map to 3 pillars? How do 
  7 steps flow through 5 components?

The resolution: Pillars are WHERE things are managed. Workflow is 
WHAT actually happens. Pillar C PROVIDES methods that the workflow 
USES — it does not contain or own the workflow.

---

## 2. The Three Pillars (Management Domains)

Pillars are NOT workflow stages. They are NOT software layers. They are 
**domains that organize and maintain specific concerns** — like 
departments in an organization.

All three pillars are **co-essential**. They play COMPLEMENTARY roles:
- Pillar A is the **design authority** (defines rules)
- Pillar B provides the **computational foundation** (manages tools)
- Pillar C supplies the **adaptive intelligence** (manages methods)

Do NOT demote any pillar to "infrastructure" or "guardrails."


### Pillar A: Conceptual Design & Governance (Rules Repository)

The design authority. Manages the rules under which everything operates.

Contents:
- **Trigger policies**: when to recalibrate — thresholds on residuals, 
  uncertainty, drift metrics
- **Acceptance criteria**: what "good enough" means — RMSE targets, 
  PICP ≈ 90%, calibration scores
- **Rollback procedures**: what happens if an update fails validation
- **Audit requirements**: documentation, justification, decision logs
- **Data policies**: which measurements to assimilate, QA/QC standards
- **Interpretability standards**: explainability for governance 
  (per Goebel 2019 as referenced in document)
- **Success metrics**: DOE mission alignment and compliance needs

**Key insight**: Governance doesn't just constrain — it DEFINES what 
the other pillars do. It determines trigger thresholds, selects which 
learning strategies to use, and decides whether results are acceptable. 
It is the design authority, not just guardrails.

From the document:
> "This pillar defines the project's objectives, success metrics, and 
> regulatory requirements. It establishes trigger criteria for when to 
> update models... It also includes data policies and interpretability 
> standards. This layer ensures the framework aligns with DOE mission 
> goals and compliance needs."

> "The presence of a recalibration trigger does not automatically 
> mandate recalibration. Instead, governance requires formal 
> justification that an update is necessary, proportional, and 
> expected to improve performance."


### Pillar B: Modeling Engines (Models Repository)

The computational tools. Manages the models that generate predictions 
and ground truth.

Contents:
- **Physics simulator** as "truth" generator (PFLOTRAN, MODFLOW, etc.)
  - High fidelity but slow/expensive
  - Used to generate targeted training data when correction needed
- **DL surrogate** for fast inference (U-Net, U-FNO, LSTM, 
  DeepONet, diffusion networks, etc.)
  - Fast but interpolates within training domain
  - Subject to distribution drift and catastrophic forgetting
- **Clear I/O contracts** between physics model and surrogate
- **Versioned artifacts** — model version control and management
- **Training data archives**

From the document:
> "A Modeling Engines pillar includes the physics-based simulator 
> (the 'truth' model) and the DL surrogate (e.g. U-Net, LSTM or 
> diffusion networks) for fast inference."


### Pillar C: Recalibration Mechanisms (Adaptive Methods Toolkit)

The methods library. Manages the techniques used for monitoring, 
detection, and correction.

Contents:
- **Uncertainty quantification (UQ) methods**: MC-dropout, deep 
  ensembles, Bayesian neural networks, conformal prediction
- **Drift detection algorithms**: residual monitoring, uncertainty 
  inflation tracking, statistical tests
- **Active learning strategies**: scenario selection for most 
  informative new physics simulations
- **Continual learning methods**: Elastic Weight Consolidation (EWC), 
  experience replay, layer freezing — avoids full retraining, 
  preserves previous knowledge
- **Multi-fidelity data fusion**: combining observations, physics 
  outputs, and surrogate predictions
- **Probability calibration**: temperature scaling, isotonic 
  regression, reliability diagrams

**Key insight**: Pillar C PROVIDES methods that the workflow USES. 
Pillar C does not "contain" or "own" the workflow.

From the document:
> "This pillar performs ongoing model maintenance. It embeds 
> uncertainty quantification (UQ) and active learning workflows 
> that watch for surrogate failure."


---

## 3. The Recalibration Workflow (7 Steps, 2 Phases)

The workflow is a **cycle** that traverses all three pillars. 

It replaces the previous 7-step formulation which had these problems:
1. Missing explicit DECIDE step (governance says triggers don't 
   automatically mandate recalibration)
2. "Optional" Steps 3-4 conflated two different update pathways
3. UQ recalibration was awkwardly separated from the fine-tuning context
4. Redeploy conflated technical deployment with governance actions

The original document described:
> Monitor → Detect → Select → Simulate → Fine-tune → Calibrate → Redeploy

The revised workflow preserves the same concepts but reorganizes them 
for clarity.


### Phase 1: Continuous Monitoring (always running)

**Step 1: MONITOR**
- Track surrogate predictions against field observations
- Compute residuals, uncertainty metrics, prediction intervals
- Draws from: **Pillar C** (UQ methods) + **Pillar A** (what to 
  track, data policies)

**Step 2: DETECT**
- Identify performance degradation via automated diagnostics
- Apply drift tests, check residual thresholds, detect uncertainty 
  inflation
- Trigger state machine: OK → WARNING → UPDATE 
  (per Fig-3 in document)
- Draws from: **Pillar C** (drift detection algorithms) + 
  **Pillar A** (trigger thresholds, governance criteria)

**Step 3: DECIDE** ← THIS STEP IS NEW (was missing in original)
- Human/governance review of evidence
- Formal determination: is update warranted, proportional, and 
  expected to improve performance?
- Choose update pathway:
  - **Pathway A**: Observation-driven (new field data sufficient)
  - **Pathway B**: Simulation-driven (active learning selects new 
    physics runs)
- Draws from: **Pillar A** (governance policies, formal justification 
  requirements)
- Justification from document: Section 3.1.3 states "the presence 
  of a recalibration trigger does not automatically mandate 
  recalibration"


### Phase 2: Triggered Response (activated when DECIDE approves update)

**Step 4: PREPARE**
- Assemble update dataset from recent field observations
- If needed (Pathway B): use active learning to select most 
  informative scenarios, then run targeted physics simulations
- Draws from: **Pillar C** (active learning strategies) + 
  **Pillar B** (physics simulator for new runs)

**Step 5: UPDATE**
- Fine-tune DL surrogate using continual learning methods
- Apply EWC, experience replay, or layer freezing to prevent 
  catastrophic forgetting
- Incremental update — NOT full retraining
- Draws from: **Pillar C** (continual learning methods) + 
  **Pillar B** (surrogate model to be updated)

**Step 6: CALIBRATE**
- Post-hoc UQ calibration of the updated model
- Temperature scaling, isotonic regression
- Verify with reliability diagrams before proceeding
- Check against acceptance criteria (e.g., PICP ≈ 90%)
- NOTE: This IS a separate step from UPDATE. Temperature scaling 
  and isotonic regression are post-training activities. 
  Do NOT merge into Step 5.
- Draws from: **Pillar C** (probability calibration methods) + 
  **Pillar A** (acceptance criteria)

**Step 7: DEPLOY**
- Validate updated model meets all acceptance criteria on held-out data
- If validation fails: trigger rollback or escalation (bigger batch 
  or partial refresh per trigger state machine)
- If validation passes: promote to operational status
- Full governance documentation: audit trail, decision justification, 
  model version records
- Draws from: **Pillar A** (audit requirements, rollback procedures) + 
  **Pillar B** (model versioning)


## 4. Cross-Reference Diagrams

### Diagram A: Primary (Use in Section 2.1)
The simplest, clearest version. Shows the key insight instantly.


            ┌──────────┐   ┌──────────┐   ┌──────────┐
            │ PILLAR A │   │ PILLAR B │   │ PILLAR C │
            │  Rules   │   │  Models  │   │ Methods  │
            └────┬─────┘   └────┬─────┘   └────┬─────┘
                 │              │              │
    ═════════════╪══════════════╪══════════════╪════════
    WORKFLOW     │              │              │
                 │              │              │
    MONITOR ─────┤              │              ├── UQ metrics
    DETECT ──────┤ thresholds   │              ├── drift tests
    DECIDE ──────┤ governance   │              │
    PREPARE ─────┤              ├── physics    ├── active learning
    UPDATE ──────┤              ├── surrogate  ├── continual learning
    CALIBRATE ───┤ acceptance   │              ├── calibration
    DEPLOY ──────┤ audit trail  ├── versioning │
    ═════════════╧══════════════╧══════════════╧════════



### Diagram B: Phase-Separated (Use in Section 2.2)
Shows the two-phase structure with the decision gate between them.
### Detailed Diagram (use in Section 2.2 — shows two phases)

            ┌──────────┐   ┌──────────┐   ┌──────────┐
            │ PILLAR A │   │ PILLAR B │   │ PILLAR C │
            │  Rules   │   │  Models  │   │ Methods  │
            └────┬─────┘   └────┬─────┘   └────┬─────┘
                 │              │              │
    ═════════════╪══════════════╪══════════════╪════════
    CONTINUOUS   │              │              │
    MONITORING   │              │              │
                 │              │              │
    MONITOR ─────┤              │              ├── UQ metrics
    DETECT ──────┤ thresholds   │              ├── drift tests
    DECIDE ──────┤ governance   │              │
                 │              │              │
    ─────────────┼──────────────┼──────────────┼────────
    TRIGGERED    │              │              │
    RESPONSE     │              │              │
                 │              │              │
    PREPARE ─────┤              ├── physics    ├── active learning
    UPDATE ──────┤              ├── surrogate  ├── continual learning
    CALIBRATE ───┤ acceptance   │              ├── calibration
    DEPLOY ──────┤ audit trail  ├── versioning │
                 │              │              │
    ═════════════╧══════════════╧══════════════╧════════
    
---



### Companion Table (Use alongside either diagram)

| Step | Phase | Pillar A (Rules) | Pillar B (Models) | Pillar C (Methods) |
|------|-------|------------------|--------------------|--------------------|
| 1. MONITOR | Continuous | What to track, data policies | — | UQ metrics computation |
| 2. DETECT | Continuous | Trigger thresholds | — | Drift detection algorithms |
| 3. DECIDE | Continuous | Governance approval, justification | — | — |
| 4. PREPARE | Triggered | — | Physics simulator runs | Active learning selection |
| 5. UPDATE | Triggered | — | Surrogate fine-tuning | Continual learning methods |
| 6. CALIBRATE | Triggered | Acceptance criteria | — | Probability calibration |
| 7. DEPLOY | Triggered | Audit trail, rollback | Model versioning | — |


---

## 5. Document Structure Decisions (Section by Section)

### Section 1 (Introduction / Motivation)
- NO structural changes needed
- Ensure it references the three-pillar + workflow structure
- Preserve existing content and citations

### Section 2 (Framework Overview) — MAJOR REVISION

**Section 2.1: Three-Pillar Architecture**
- Reframe pillars as "management domains" — places that organize 
  and maintain specific concerns
- Pillar A manages rules & governance
- Pillar B manages modeling engines
- Pillar C manages adaptive methods
- Add paragraph explaining COMPLEMENTARY roles:
  > "Pillar A serves as the design authority, defining when and 
  > whether recalibration occurs. Pillar B provides the computational 
  > tools — physics models for ground truth and surrogates for 
  > operational predictions. Pillar C supplies the adaptive methods 
  > that monitor, detect, and correct. All three are co-essential."
- Include core principle sentence
- Emphasize: no pillar "owns" the workflow
- Include Diagram A (primary cross-reference diagram)

**Section 2.2: Recalibration Workflow**
- Replace old 7 steps with new 7 steps in 2 phases
- Phase 1: Continuous Monitoring (Steps 1-3: MONITOR, DETECT, DECIDE)
- Phase 2: Triggered Response (Steps 4-7: PREPARE, UPDATE, CALIBRATE, 
  DEPLOY)
- Step 3 (DECIDE) is NEW — emphasize human governance review
- For EACH step, explicitly note which pillar(s) it draws from
- Include Diagram B (phase-separated cross-reference diagram)
- Include companion table
- Explain two update pathways (observation-driven vs simulation-driven)
- Include or reference trigger state machine 
  (OK → WARNING → UPDATE → OK/ESCALATE)

### Section 3 (Methods) — DO NOT RESTRUCTURE
- Already organized by pillar — works well:
  - 3.1 Governance (Pillar A) ✓
  - 3.2 Modeling Engines (Pillar B) ✓
  - 3.3 Recalibration Mechanisms (Pillar C) ✓
- Only light terminology updates if needed to match "management 
  domain" framing
- Check that workflow references match new 7-step, 2-phase structure
- Preserve all technical content and citations

### Section 4 (Proof of Concept / Case Study)
- NO structural changes needed
- Ensure it references workflow steps by name/number
- Check consistency with revised terminology

### Section 5 (Implementation / Software Architecture) — MAJOR REVISION
- Reorganize by WORKFLOW PHASES (not by pillar, not by old 5 components)
- Do NOT introduce "four layers" or any new organizational scheme
- Structure:
  - **5.1 Software Architecture Overview**
    - Diagram: workflow steps mapped to software modules
    - Each module notes which pillar(s) it serves
  - **5.2 Monitoring & Detection** (supports Steps 1-3)
    - Performance tracking, UQ computation, drift detection
    - Decision support interface for governance review
  - **5.3 Model Update Pipeline** (supports Steps 4-6)
    - Active learning sampler, physics model interface
    - Continual learning trainer, UQ calibration
  - **5.4 Deployment & Governance** (supports Step 7)
    - Validation against acceptance criteria
    - Promotion to operations, audit logging, rollback
  - **5.5 Infrastructure & Development Phases**
    - Data management and provenance
    - HPC integration
    - API design
    - Phase 1: Prototype → Phase 2: Integrated → Phase 3: Operational
- For each subsection, note which pillar(s) the software serves
- Preserve useful technical content from old Section 5

### Sections 6-7 (Discussion, Future Work, Conclusion)
- Light updates for consistency with new terminology
- NO structural changes needed
- Preserve existing content

---

## 6. Existing Figures — Preserve or Update

From the current document:

| Figure | Action | Notes |
|--------|--------|-------|
| Fig-1 / 3-1: Three-Pillar Architecture | **UPDATE** | Redraw to show management domain framing + workflow traversal |
| Fig-2: End-to-End Recalibration Loop | **REPLACE** | Replace with new 7-step, 2-phase workflow + cross-reference diagram |
| Fig-3: Trigger State Machine | **KEEP AS-IS** | Good concept, already works |
| Fig-4: Dashboard Storyboard | **KEEP AS-IS** | No changes needed |

New diagrams needed:
- **Diagram A**: Cross-reference diagram (pillars × workflow steps) — for Section 2.1
- **Diagram B**: Phase-separated cross-reference — for Section 2.2
- **Table**: Companion table (steps × pillars with details) — for Section 2.2

---

## 7. Terminology Decisions

| Use This | NOT This | Reason |
|----------|----------|--------|
| Management domains | Layers, subsystems | Pillars manage concerns, they're not software |
| Recalibration | Retraining | Framework does incremental updates |
| Co-essential | Co-equal | Different roles, all necessary |
| Complementary roles | Equal pillars | Acknowledges they do different things |
| Design authority (Pillar A) | Guardrails | Governance defines, not just constrains |
| Workflow steps | Pipeline stages | Steps cross pillars |
| Triggered response | Automatic response | Human DECIDE step exists |
| Adaptive methods toolkit (Pillar C) | — | Consider renaming from "Recalibration Mechanisms" |

NOTE on Pillar C naming: The current document calls it "Recalibration 
Mechanisms." The term "Adaptive Methods Toolkit" may be clearer. 
If changing, do so consistently throughout. Discuss with user first 
before renaming.

---

## 8. Things to PRESERVE (Do NOT Change)

- Three-pillar language and three-pillar structure
- All technical content in Section 3 (methods)
- The term "recalibration" (not "retraining")
- Physics model as authoritative truth source
- Governance as first-class concern and design authority
- Trigger state machine concept (OK → WARNING → UPDATE → ESCALATE)
- Case study / proof-of-concept content (Section 4)
- Existing citations and references throughout
- Dashboard storyboard concept (Fig-4)
- Feedback loop narrative ("pillars interact in a feedback loop")
- DOE mission alignment language
- All original files (create new versions, don't overwrite)

## 9. Things to AVOID

- Do NOT invent new organizational schemes (no "four layers," 
  no "functional layers," no "software layers")
- Do NOT demote governance to "infrastructure" or "guardrails"
- Do NOT present Pillar C as "the actual framework" — all pillars 
  are co-essential
- Do NOT merge CALIBRATE (Step 6) into UPDATE (Step 5) — temperature 
  scaling and reliability diagrams are post-training activities
- Do NOT restructure Section 3 — it's already well-organized
- Do NOT overwrite original files — always create new versions
- Do NOT use the word "layer" to describe pillars
- Do NOT call the adaptive loop "the true backbone" — it's the 
  workflow, complementary to the pillars
- Do NOT make the 7 steps into 8 steps — keep it at 7

---

## 10. File Management Rules

### Read-Only Files (NEVER modify)
- `Framework_draft.docx` — the original document
- `plans/framework_alignment_analysis.md` — v1 analysis (historical)
- `plans/framework_alignment_analysis_v2.md` — v2 analysis (historical)

### Authoritative Reference (modify only with user approval)
- `plans/design_decisions.md` — THIS FILE

### Working Drafts (create new, iterative versions)
- `drafts/section2_1_pillars_REVISED.md`
- `drafts/section2_2_workflow_REVISED.md`
- `drafts/section5_REVISED_v2.md`
- `drafts/section3_consistency_notes.md`
- `drafts/consistency_check.md`

### Final Output
- `Framework_REVISED_COMPLETE.md` — full assembled markdown
- `Framework_REVISED_COMPLETE.docx` — converted Word document

---

## 11. Previous Analyses (Historical Context)

Two previous analysis documents exist. They informed these decisions 
but are SUPERSEDED by this file:

### framework_alignment_analysis.md (v1)
- Identified the three overlapping organizational schemes
- Proposed Option A (Pillar-based organization)
- Recommended four-layer software architecture
- **Status**: Superseded. The "four layers" recommendation is rejected.

### framework_alignment_analysis_v2.md (v2)
- Challenged v1, proposed the "adaptive loop" as true backbone
- Claimed Pillar C IS the framework, A and B are infrastructure
- Proposed Option D (Adaptive Loop as Primary)
- Proposed expanding to 8 steps
- **Status**: Superseded. Key insights retained (adaptive loop as 
  narrative, missing DECIDE step, step critique) but structural 
  recommendations rejected (pillars remain primary, kept at 7 steps, 
  no pillar demotion).

### What Was Retained from Each

| From v1 | From v2 | New in Final |
|---------|---------|--------------|
| Three-pillar structure | Missing DECIDE step critique | "Management domains" framing |
| Mapping tables | Two-phase workflow concept | Pillars as repositories |
| Section 3 stays as-is | Audience-specific analysis | Cross-reference diagrams |
| — | UQ separate step is valid | Workflow traverses pillars |
| — | Two update pathways | Companion table |

---

═══════════════════════════════════════════════════════════════════
END OF DESIGN DECISIONS
═══════════════════════════════════════════════════════════════════
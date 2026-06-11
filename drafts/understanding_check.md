# Understanding Check — TASK 1 Confirmation

**Date**: 2026-03-19  
**Purpose**: Confirm understanding of the framework revision requirements before proceeding with revisions

---

## 1. The Three Pillars (Management Domains, NOT Workflow Stages)

I understand that the three pillars are **management domains** — organizational containers that hold and maintain specific concerns. They are NOT workflow stages, NOT software layers, and NOT sequential phases.

### Pillar A: Conceptual Design & Governance (Rules Repository)
- The **design authority** — defines rules under which everything operates
- Contains: trigger policies, acceptance criteria, rollback procedures, audit requirements, data policies, interpretability standards, success metrics
- Key insight: Governance doesn't just constrain — it **DEFINES** what the other pillars do

### Pillar B: Modeling Engines (Models Repository)
- The **computational foundation** — manages the models that generate predictions and ground truth
- Contains: physics simulator (PFLOTRAN, MODFLOW, etc.) as "truth" generator, DL surrogate (U-Net, U-FNO, LSTM, etc.) for fast inference, versioned artifacts, training data archives
- Key insight: Physics model is authoritative truth source; surrogate is subject to drift

### Pillar C: Recalibration Mechanisms (Adaptive Methods Toolkit)
- The **adaptive intelligence** — manages techniques for monitoring, detection, and correction
- Contains: UQ methods (MC-dropout, deep ensembles, conformal prediction), drift detection algorithms, active learning strategies, continual learning methods (EWC, experience replay), multi-fidelity data fusion, probability calibration
- Key insight: Pillar C **PROVIDES** methods that the workflow **USES** — it does not "contain" or "own" the workflow

### Critical Understanding
All three pillars are **co-essential** and play **complementary roles**:
- No pillar should be demoted to "infrastructure" or "guardrails"
- No pillar "owns" the workflow
- The workflow **traverses** all three pillars

---

## 2. The Revised 7-Step, 2-Phase Workflow

I understand the workflow has been revised from the original 7 steps to a clearer 7-step, 2-phase structure.

### Phase 1: Continuous Monitoring (always running)

| Step | Name | Description | Draws From |
|------|------|-------------|------------|
| 1 | MONITOR | Track surrogate predictions against field observations; compute residuals, uncertainty metrics | Pillar C (UQ methods) + Pillar A (data policies) |
| 2 | DETECT | Identify performance degradation via automated diagnostics; apply drift tests; trigger state machine (OK → WARNING → UPDATE) | Pillar C (drift detection) + Pillar A (trigger thresholds) |
| 3 | DECIDE | **NEW STEP** — Human/governance review of evidence; formal determination if update is warranted; choose update pathway (observation-driven vs simulation-driven) | Pillar A (governance policies) |

### Phase 2: Triggered Response (activated when DECIDE approves update)

| Step | Name | Description | Draws From |
|------|------|-------------|------------|
| 4 | PREPARE | Assemble update dataset from recent observations; if needed, use active learning to select scenarios and run targeted physics simulations | Pillar C (active learning) + Pillar B (physics simulator) |
| 5 | UPDATE | Fine-tune DL surrogate using continual learning methods (EWC, replay, layer freezing); incremental update, NOT full retraining | Pillar C (continual learning) + Pillar B (surrogate) |
| 6 | CALIBRATE | Post-hoc UQ calibration (temperature scaling, isotonic regression); verify with reliability diagrams; check acceptance criteria (PICP ≈ 90%) | Pillar C (probability calibration) + Pillar A (acceptance criteria) |
| 7 | DEPLOY | Validate against acceptance criteria on held-out data; if fails → rollback/escalation; if passes → promote to operations; full governance documentation | Pillar A (audit, rollback) + Pillar B (versioning) |

### Key Changes from Original
- **Step 3 (DECIDE) is NEW** — addresses the document's statement that "triggers don't automatically mandate recalibration"
- **Steps 3-4 are no longer "optional"** — instead, there are two update pathways (observation-driven vs simulation-driven)
- **CALIBRATE (Step 6) remains separate from UPDATE (Step 5)** — temperature scaling and reliability diagrams are post-training activities
- **Two phases** clearly distinguish continuous monitoring from triggered response

---

## 3. The Core Principle (Pillars = WHAT, Workflow = HOW)

I understand the key insight that resolves the previous confusion:

> **"The three pillars define WHAT the framework manages;  
> the recalibration workflow defines HOW these elements interact  
> during operations. Each workflow step draws resources, methods,  
> or constraints from one or more pillars."**

| Concept | What It Is | Analogy |
|---------|-----------|---------|
| **Pillars** | Management Domains (static) — what you organize & maintain | Departments in an organization |
| **Workflow** | Operational Sequence (dynamic) — what actually happens | Business process that crosses all departments |

These are **COMPLEMENTARY**, not redundant:
- The workflow **TRAVERSES** all three pillars
- No single pillar "owns" the workflow
- Each workflow step reaches into one or more pillars for what it needs

---

## 4. How the Workflow Traverses the Pillars (Cross-Reference Diagrams)

I understand the cross-reference diagrams that will be used:

### Diagram A (Primary — for Section 2.1)
Shows pillars as columns with workflow steps as rows, indicating which pillar(s) each step draws from.

### Diagram B (Phase-Separated — for Section 2.2)
Same structure but with a visual separator between Phase 1 (Continuous Monitoring) and Phase 2 (Triggered Response).

### Companion Table
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

## 5. What Needs to Change in Sections 2 and 5

### Section 2 (Framework Overview) — MAJOR REVISION

**Section 2.1: Three-Pillar Architecture**
- Reframe pillars as "management domains"
- Add paragraph explaining complementary roles
- Include core principle sentence
- Emphasize: no pillar "owns" the workflow
- Include Diagram A

**Section 2.2: Recalibration Workflow**
- Replace old 7 steps with new 7 steps in 2 phases
- Step 3 (DECIDE) is NEW — emphasize human governance review
- For EACH step, explicitly note which pillar(s) it draws from
- Include Diagram B and companion table
- Explain two update pathways
- Include trigger state machine reference

### Section 5 (Implementation) — MAJOR REVISION

Reorganize by **WORKFLOW PHASES** (not by pillar, not by old 5 components):

- **5.1 Software Architecture Overview** — diagram mapping workflow steps to software modules; each module notes which pillar(s) it serves; NO "four layers" or new schemes
- **5.2 Monitoring & Detection** (supports Steps 1-3) — performance tracking, UQ computation, drift detection, decision support interface
- **5.3 Model Update Pipeline** (supports Steps 4-6) — active learning sampler, physics model interface, continual learning trainer, UQ calibration
- **5.4 Deployment & Governance** (supports Step 7) — validation, promotion, audit logging, rollback
- **5.5 Infrastructure & Development Phases** — data management, HPC integration, API design, Phase 1→2→3 roadmap

---

## 6. What Should NOT Change

### Section 3 (Methods) — DO NOT RESTRUCTURE
- Already organized by pillar (3.1 Governance, 3.2 Modeling Engines, 3.3 Recalibration Mechanisms) — this works well
- Only light terminology updates if needed to match "management domain" framing
- Check that workflow references match new 7-step, 2-phase structure
- Preserve all technical content and citations

### Original Files — NEVER MODIFY
- `manuscript/Framework_draft.docx` — the original document (read-only)
- `plans/framework_alignment_analysis.md` — v1 analysis (historical, read-only)
- `plans/framework_alignment_analysis_v2.md` — v2 analysis (historical, read-only)

### Content to Preserve
- Three-pillar language and structure
- All technical content in Section 3
- The term "recalibration" (not "retraining")
- Physics model as authoritative truth source
- Governance as first-class concern and design authority
- Trigger state machine concept (OK → WARNING → UPDATE → ESCALATE)
- Case study / proof-of-concept content (Section 4)
- Existing citations and references
- Dashboard storyboard concept
- Feedback loop narrative
- DOE mission alignment language

---

## 7. What Was Retained vs Rejected from v1 and v2 Analyses

### From v1 Analysis (framework_alignment_analysis.md)

| Retained | Rejected |
|----------|----------|
| Three-pillar structure as organizing principle | "Four layers" software architecture recommendation |
| Mapping tables showing pillar-step relationships | — |
| Section 3 stays as-is (already well-organized) | — |

### From v2 Analysis (framework_alignment_analysis_v2.md)

| Retained | Rejected |
|----------|----------|
| Missing DECIDE step critique → added as Step 3 | "Adaptive loop as true backbone" framing |
| Two-phase workflow concept (Continuous + Triggered) | Pillar C as "the actual framework" (all pillars are co-essential) |
| Audience-specific analysis (DOE, scientists, ML researchers) | Demoting Pillars A and B to "infrastructure" |
| UQ separate step is valid (kept as Step 6) | Expanding to 8 steps (kept at 7) |
| Two update pathways (observation-driven vs simulation-driven) | — |

### New in Final Design Decisions

- "Management domains" framing for pillars
- Pillars as repositories (Rules, Models, Methods)
- Cross-reference diagrams (Diagram A and B)
- Workflow traverses pillars (not owned by any pillar)
- Companion table (steps × pillars with details)
- Terminology decisions (e.g., "co-essential" not "co-equal")

---

## 8. Terminology Decisions

| Use This | NOT This | Reason |
|----------|----------|--------|
| Management domains | Layers, subsystems | Pillars manage concerns, they're not software |
| Recalibration | Retraining | Framework does incremental updates |
| Co-essential | Co-equal | Different roles, all necessary |
| Complementary roles | Equal pillars | Acknowledges they do different things |
| Design authority (Pillar A) | Guardrails | Governance defines, not just constrains |
| Workflow steps | Pipeline stages | Steps cross pillars |
| Triggered response | Automatic response | Human DECIDE step exists |

---

## 9. Things to AVOID

- Do NOT invent new organizational schemes (no "four layers," no "functional layers")
- Do NOT demote governance to "infrastructure" or "guardrails"
- Do NOT present Pillar C as "the actual framework"
- Do NOT merge CALIBRATE (Step 6) into UPDATE (Step 5)
- Do NOT restructure Section 3
- Do NOT overwrite original files
- Do NOT use the word "layer" to describe pillars
- Do NOT call the adaptive loop "the true backbone"
- Do NOT make the 7 steps into 8 steps

---

## 10. Confirmation

I confirm that I understand:

✅ The three pillars are management domains, not workflow stages  
✅ The revised 7-step, 2-phase workflow with the new DECIDE step  
✅ The core principle: pillars = WHAT, workflow = HOW  
✅ How the workflow traverses the pillars (cross-reference diagrams)  
✅ What needs to change in Sections 2 and 5  
✅ What should NOT change (Section 3, original files)  
✅ What was retained vs rejected from v1 and v2 analyses  

I am ready to proceed with TASK 2 (Revise Section 2.1) upon your approval.

---

**End of Understanding Check**

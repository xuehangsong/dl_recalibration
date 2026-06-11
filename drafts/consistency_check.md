# Document Consistency Check

**Purpose**: Verify alignment across all revised sections and identify any remaining inconsistencies.

**Scope**: Sections 2.1, 2.2, 3, and 5 (revised drafts and original)

---

## 1. Executive Summary

### Overall Assessment: **MOSTLY CONSISTENT** with specific revisions needed

The revised sections (2.1, 2.2, 5) are internally consistent with each other and with design_decisions.md. However, **Section 5 needs revision** to better align with Section 3's actual methods and to adopt a "framework design" tone rather than strict software specification.

### Key Issues Identified:
1. **Section 5 invents implementation details** not grounded in Section 3 methods
2. **Section 5 reads too much like software specification** rather than framework design
3. **Minor terminology inconsistencies** between sections

---

## 2. Core Principle Consistency

### The Key Insight: "Pillars define WHAT; Workflow defines HOW"

| Section | Adherence | Notes |
|---------|-----------|-------|
| 2.1 (Pillars) | ✅ GOOD | Clearly frames pillars as "management domains" (repositories of rules, models, methods) |
| 2.2 (Workflow) | ✅ GOOD | Clearly shows workflow as operational sequence that draws from all pillars |
| 3 (Methods) | ✅ GOOD | Organized by pillar, which is appropriate for a methods section |
| 5 (Implementation) | ⚠️ NEEDS WORK | Organized by workflow phases (correct), but invents details not in Section 3 |

---

## 3. Pillar Terminology Consistency

### Pillar Names and Descriptions

| Pillar | Section 2.1 | Section 3 | Section 5 | Consistent? |
|--------|-------------|-----------|-----------|-------------|
| A | "Conceptual Design & Governance (Rules Repository)" | "Governance Essentials" | "Governance" | ⚠️ Minor variation |
| B | "Modeling Engines (Models Repository)" | "Modeling Engines" | "Modeling Engines" | ✅ |
| C | "Recalibration Mechanisms (Adaptive Methods Toolkit)" | "Recalibration Mechanisms" | "Recalibration Mechanisms" | ✅ |

**Recommendation**: Use consistent short names throughout:
- Pillar A: Governance
- Pillar B: Modeling Engines  
- Pillar C: Recalibration Mechanisms

---

## 4. Workflow Step Consistency

### 7-Step, 2-Phase Workflow

| Step | Section 2.2 Name | Section 5 Name | Section 3 Coverage | Consistent? |
|------|------------------|----------------|-------------------|-------------|
| 1 | MONITOR | MONITOR | 3.3.1 (UQ), 3.3.2 (metrics) | ✅ |
| 2 | DETECT | DETECT | 3.3.2 (Trigger Logic) | ✅ |
| 3 | DECIDE | DECIDE | 3.1 (Governance) | ✅ |
| 4 | PREPARE | PREPARE | 3.3.4 (Active Learning) | ✅ |
| 5 | UPDATE | UPDATE | 3.3.3 (Continual Learning) | ✅ |
| 6 | CALIBRATE | CALIBRATE | 3.3.1 (UQ recalibration) | ✅ |
| 7 | DEPLOY | DEPLOY | 3.1 (Governance) | ✅ |

**Assessment**: Step names are consistent across sections. ✅

---

## 5. Section 5 Specific Issues

### Issue 1: Invents Details Not in Section 3

Section 5 currently includes implementation details that are not grounded in Section 3's methods:

| Section 5 Content | Section 3 Basis | Issue |
|-------------------|-----------------|-------|
| "Performance Tracker" module | 3.3.2 mentions RMSE/bias | OK, but overly specific |
| "Trigger State Machine" with OK→WARNING→UPDATE→ESCALATE | 3.3.2 mentions composite gating | OK conceptually, but too prescriptive |
| "Rollback Manager" | 3.1.5 defines rollback | OK |
| "HPC Integration" details | Not in Section 3 | ⚠️ Too implementation-specific |
| "Docker containers" | Not in Section 3 | ⚠️ Too implementation-specific |
| Specific module names | Not in Section 3 | ⚠️ Reads like software spec |

### Issue 2: Tone is Too Prescriptive

**Current tone** (Section 5): Reads like a software requirements document
- "The Performance Tracker continuously compares..."
- "The Active Learning Sampler selects informative scenarios..."
- Detailed module-to-step mapping tables

**Needed tone**: Framework design document
- "The framework requires capabilities for performance tracking..."
- "Active learning approaches (Section 3.3.4) guide scenario selection..."
- Conceptual descriptions with references to Section 3 methods

### Issue 3: Missing Section 3 Method References

Section 5 should explicitly reference these Section 3 methods:

| Workflow Step | Section 3 Methods to Reference |
|---------------|-------------------------------|
| MONITOR | MC-Dropout, deep ensembles, conformal prediction (3.3.1) |
| DETECT | KS test, composite drift index, tipping-point metrics (3.3.2) |
| DECIDE | Governance thresholds, acceptance criteria (3.1.3) |
| PREPARE | Uncertainty sampling, error-based sampling, 6-10 batch size (3.3.4) |
| UPDATE | EWC, replay buffers (70-75%), layer freezing (3.3.3) |
| CALIBRATE | Coverage evaluation, interval adjustment (3.3.1) |
| DEPLOY | Configuration control, audit trails, rollback (3.1.5) |

---

## 6. Recommended Section 5 Revisions

### 6.1 Reframe as Framework Design

**Before** (current):
> "The Performance Tracker continuously compares surrogate predictions against available monitoring data"

**After** (recommended):
> "The framework requires continuous comparison of surrogate predictions against monitoring data. Section 3.3.1 describes UQ methods (MC-Dropout, deep ensembles) that provide the uncertainty metrics needed for this comparison."

### 6.2 Add Explicit Section 3 Cross-References

Each workflow step in Section 5 should cite the relevant Section 3 subsection:

```
Step 2 (DETECT): Drift detection implements the trigger logic defined in Section 3.3.2, 
including distributional tests (KS test), performance thresholds (>2× rolling std dev), 
and composite drift indices that integrate multiple signals.
```

### 6.3 Remove Overly Specific Implementation Details

Remove or move to appendix:
- Specific module names (these are design choices, not framework requirements)
- Docker/containerization details
- Specific database schemas
- GUI mockups

Keep:
- Conceptual architecture (workflow-centric organization)
- Capability requirements (what the system must do)
- Governance integration points
- Development phases (Prototype → Integrated → Operational)

### 6.4 Align with User Feedback

User feedback: *"don't invent things we are not doing, don't think we are developing a very strict real software, but more like a framework design"*

This means Section 5 should:
- Describe **what capabilities are needed**, not how to implement them
- Reference **Section 3 methods** as the technical foundation
- Present **conceptual architecture**, not software specification
- Include **development phases** showing progression from prototype to operational

---

## 7. Cross-Section Reference Consistency

### Diagram Consistency

| Diagram | Location | Content | Consistent? |
|---------|----------|---------|-------------|
| Diagram A (Pillars + Workflow) | Section 2.1 | Shows pillars as domains, workflow traversing | ✅ |
| Diagram B (Two Phases) | Section 2.2 | Shows 7 steps in 2 phases | ✅ |
| Software Architecture Diagram | Section 5 | Shows modules mapped to workflow | ⚠️ Needs simplification |

**Recommendation**: Section 5 diagram should be simplified to show conceptual architecture, not detailed module structure.

### Table Consistency

| Table | Location | Content | Consistent? |
|-------|----------|---------|-------------|
| Pillar Summary | Section 2.1 | Pillar descriptions | ✅ |
| Step-Pillar Mapping | Section 2.2 | Which pillars each step uses | ✅ |
| Module-Step Mapping | Section 5 | Software modules per step | ⚠️ Too detailed |

---

## 8. Terminology Glossary Check

### Terms That Must Be Used Consistently

| Term | Definition | Usage Check |
|------|------------|-------------|
| Pillar | Management domain (not workflow stage, not software layer) | ✅ Consistent |
| Workflow | 7-step operational sequence | ✅ Consistent |
| Phase 1 | Continuous Monitoring (Steps 1-3) | ✅ Consistent |
| Phase 2 | Triggered Response (Steps 4-7) | ✅ Consistent |
| DECIDE | New step for governance approval | ✅ Consistent |
| Rollback | Withdrawal + full retrain (not version reversion) | ✅ Consistent |
| Surrogate | DL model trained on physics outputs | ✅ Consistent |
| Recalibration | Updating surrogate (not physics model calibration) | ✅ Consistent |

---

## 9. Action Items

### High Priority (Must Fix)

1. **Revise Section 5** to:
   - Adopt framework design tone (not software specification)
   - Add explicit Section 3 method references
   - Remove overly specific implementation details
   - Simplify architecture diagram

### Medium Priority (Should Fix)

2. **Add Section 3 cross-references** noting which workflow steps each method supports

3. **Standardize pillar short names** across all sections

### Low Priority (Nice to Have)

4. **Add brief connecting language** at start of Section 3 linking to workflow

5. **Update Section 3 terminology** to use step names (DETECT, DECIDE, etc.)

---

## 10. Conclusion

The revised sections are structurally sound and follow the core principle from design_decisions.md. The main issue is that **Section 5 needs to be reframed as framework design** rather than software specification, with explicit references to Section 3 methods.

Once Section 5 is revised per the recommendations above, the document will be internally consistent and ready for assembly.

---

## Appendix: Section 5 Revision Checklist

- [ ] Reframe introduction as "framework design" not "software architecture"
- [ ] Add Section 3 method references to each workflow step description
- [ ] Remove specific module names (or move to appendix as "example implementation")
- [ ] Simplify architecture diagram to conceptual level
- [ ] Remove Docker/containerization details (or move to appendix)
- [ ] Keep development phases (Prototype → Integrated → Operational)
- [ ] Keep governance integration points
- [ ] Keep human decision point emphasis
- [ ] Ensure all methods mentioned are from Section 3 (not invented)

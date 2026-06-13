# Section 5 Revision Plan

**Document:** Keeping Deep-Learning Surrogates Accurate for Long-Term Groundwater Remediation: Concept & Prototype Plan  
**Section:** 5. Prototype Demonstration  
**Status:** Planning  
**Date:** 2025-03-23

---

## 1. Section Purpose

Section 5 answers the question: ***"How will we demonstrate and validate this framework?"***

This is a **planning document**, not a results report. Section 5 describes:
- What prototypes will be built
- What case study will be conducted
- How success will be measured
- What outcomes are expected

It does NOT contain:
- Actual experimental results
- Validation metrics definitions (already in Section 3.1.3)
- Development timeline details (already in Section 4.3)

---

## 2. Recommended Structure

```
5. Prototype Demonstration

5.1 Demonstration Objectives
    - Purpose of the prototype demonstration
    - Relationship to Phase 1 development (cross-ref Section 4.3.1)
    - Success criteria overview (cross-ref Section 3.1.3)

5.2 Prototype Implementations
    5.2.1 U-FNO Surrogate for 2D Cross-Section Transport
          - PFLOTRAN baseline model description
          - U-FNO architecture overview
          - Workflow integration plan
    
    5.2.2 U-Net Surrogate for 2D Pump-and-Treat Plume Prediction
          - Training data generation approach
          - Architecture modifications
          - Workflow integration plan

5.3 Case Study Design
    5.3.1 Scenario Description
          - Synthetic site characteristics
          - Initial surrogate training setup
    
    5.3.2 Drift Injection Plan
          - How drift will be introduced
          - Expected detection approach
    
    5.3.3 Recalibration Demonstration Plan
          - How each workflow step will be demonstrated
          - Governance decision demonstration
    
    5.3.4 Evaluation Approach
          - Before vs. after comparison plan
          - Computational efficiency measurement

5.4 Expected Outcomes
    - Quantitative targets
    - Deliverables
    - Lessons for subsequent phases

5.5 Summary
```

---

## 3. Source Files

### Primary Sources

| Source File | Content to Extract | Use In |
|-------------|-------------------|--------|
| `drafts/backup/section5_case_study_REVISED.md` | U-FNO prototype details (lines 37-45) | 5.2.1 |
| `drafts/backup/section5_case_study_REVISED.md` | U-Net prototype details (lines 47-57) | 5.2.2 |
| `drafts/backup/section5_case_study_REVISED.md` | Case study scenario (lines 59-83) | 5.3 |
| `drafts/backup/section5_case_study_REVISED.md` | Evaluation plan (lines 85-99) | 5.3.4 |
| `manuscript/Framework_draft.docx` | Original prototype details (lines 1277-1384) | 5.2 |

### Cross-Reference Sources

| Source File | Content | Cross-Reference In |
|-------------|---------|-------------------|
| `drafts/final/section3_FINAL.md` | Acceptance criteria (Section 3.1.3) | 5.1 |
| `drafts/final/section4_FINAL.md` | Phase 1 scope (Section 4.3.1) | 5.1 |
| `drafts/final/section2_2_FINAL.md` | 7-step workflow | 5.3.3 |

### Literature Support

| Source File | Content | Use In |
|-------------|---------|--------|
| `projects/lit-surrogate-models/papers.md` | U-FNO citations (Wen et al., 2022; Jiang et al., 2025) | 5.2.1 |
| `projects/lit-surrogate-models/papers.md` | U-Net citations (Song et al., 2025) | 5.2.2 |

---

## 4. Revision Prompt

### System Context
```
You are revising Section 5 of a technical document titled "Keeping Deep-Learning 
Surrogates Accurate for Long-Term Groundwater Remediation: Concept & Prototype Plan."

This is a PLANNING document, not a results report. Section 5 describes what will 
be built and tested, not what has been achieved.
```

### Task Instructions
```
Create Section 5 (Prototype Demonstration) following this structure:

5.1 Demonstration Objectives (~10 lines)
- State the purpose: demonstrate one complete recalibration cycle
- Reference Section 4.3.1 for Phase 1 scope
- Reference Section 3.1.3 for acceptance criteria (do NOT re-define metrics)

5.2 Prototype Implementations (~40 lines)
- 5.2.1 U-FNO for 2D cross-section transport
  - PFLOTRAN baseline: 84m × 4m domain, 28 × 40 grid, Richards equation
  - U-FNO: ~126M parameters, Fourier layers + U-Net skip connections
  - Cite: Jiang et al. (2025) GeoFUSE framework
- 5.2.2 U-Net for pump-and-treat plume prediction
  - Training: 128 × 100 mesh, 10,000 physics runs, 1-5 wells
  - Architecture: Thiem equation input, strided convolutions, leaky tanh
  - Cite: Song et al. (2025)

5.3 Case Study Design (~35 lines)
- 5.3.1 Scenario: synthetic DOE EM site, pump-and-treat remediation
- 5.3.2 Drift injection: pumping regime change mid-simulation
- 5.3.3 Recalibration demonstration: walk through all 7 workflow steps
  - Explicitly mention governance decision at DECIDE step
- 5.3.4 Evaluation: before/after comparison, computational efficiency

5.4 Expected Outcomes (~15 lines)
- Quantitative targets: 10³-10⁴× speedup, <10 targeted physics runs
- Deliverables: documented recalibration cycle, governance records
- Lessons for Phase 2 development

5.5 Summary (~5 lines)

TOTAL: ~105 lines
```

### Style Guidelines
```
- Use prose paragraphs, not bullet lists (except for brief enumerations)
- Avoid bold formatting for inline terms
- Use cross-references: "as defined in Section X.X" or "described in Section X.X"
- This is planning language: "will be," "is designed to," "the demonstration will"
- Do NOT re-define metrics or timelines that exist in other sections
```

### Content to Remove from Current Draft
```
- Section 5.1 (Validation Framework) - redundant with Section 3.1.3
- Section 5.5 (Development Timeline) - redundant with Section 4.3
- Detailed metric definitions - reference Section 3.1.3 instead
```

### Content to Keep from Current Draft
```
- U-FNO prototype details (lines 37-45)
- U-Net prototype details (lines 47-57)
- Case study scenario description (lines 63-73)
- Recalibration demonstration walkthrough (lines 75-83)
- Evaluation approach (lines 89-99)
```

---

## 5. Checklist for Revision

### Structure
- [ ] Section follows recommended outline (5.1-5.5)
- [ ] No redundancy with Section 3.1.3 (metrics)
- [ ] No redundancy with Section 4.3 (timeline)
- [ ] Cross-references to Sections 2.2, 3.1.3, 4.3.1 included

### Content
- [ ] U-FNO prototype described with PFLOTRAN baseline
- [ ] U-Net prototype described with training approach
- [ ] Case study scenario clearly defined
- [ ] Drift injection method explained
- [ ] All 7 workflow steps mentioned in demonstration plan
- [ ] Governance decision (DECIDE step) explicitly addressed
- [ ] Expected outcomes stated with quantitative targets

### Style
- [ ] Planning language used throughout ("will be," "is designed to")
- [ ] Prose paragraphs (not excessive bullet lists)
- [ ] Minimal bold formatting
- [ ] Citations included (Jiang et al., Song et al.)

### Length
- [ ] Total ~100-110 lines (reduced from 122)
- [ ] Each subsection within target length

---

## 6. Output File

**Target:** `drafts/final/section5_FINAL.md`

---

## 7. Dependencies

Before creating Section 5, ensure these files are finalized:
- [x] `drafts/final/section2_2_FINAL.md` (workflow reference)
- [x] `drafts/final/section3_FINAL.md` (acceptance criteria reference)
- [x] `drafts/final/section4_FINAL.md` (Phase 1 scope reference)

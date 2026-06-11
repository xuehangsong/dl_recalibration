# Task: Section 3.3.6 Full Retraining Revision

## Task ID: SECTION3_3_6_RETRAIN
## Status: PENDING
## Priority: HIGH

---

## 1. OBJECTIVE

Revise Section 3.3.6 (Full Retraining) from the original document into DOE Technical Report style while **preserving ALL citations**.

---

## 2. SOURCE MATERIAL

### Source File
`manuscript/Framework_draft.docx`

### Source Line Range
**Lines 925-954** (Section 3.3.6 Full Retraining)

---

## 3. MANDATORY CITATIONS TO PRESERVE

### Core Method Citations (MUST INCLUDE ALL)
| Topic | Citation | Context |
|-------|----------|---------|
| Concept drift | (Parisi et al., 2019; Sayed et al., 2025) | When foundational assumptions no longer hold |
| Groundwater recalibration | (Laloy et al., 2017) | After numerical model recalibration |
| Multi-fidelity deviation | (Wen et al., 2021) | When HF deviates substantially from prior domains |

### Citation Verification Checklist
After revision, verify these citations appear:
- [ ] Parisi et al. (2019) - continual learning review
- [ ] Sayed et al. (2025) - energy management systems
- [ ] Laloy et al. (2017) - groundwater inversion
- [ ] Wen et al. (2021) - multi-fidelity

---

## 4. KEY CONCEPTS TO PRESERVE

### When Full Retraining is Required
1. Regime shifts or major forcing changes
2. Redefinition of underlying physics model
3. Recalibration of numerical model
4. New hydrogeologic interpretations
5. Major reconfiguration of pumping/boundary conditions
6. Repeated fine-tuning failures

### Full Retraining Process Steps
1. Verify retraining triggers (major changes, physics model updates, repeated failures)
2. Redesign training domain (updated ranges of hydrofacies, scenarios, forcings)
3. Generate new ensemble of high-fidelity simulations (+ LF for coverage)
4. Integrate recent field observations
5. Train new surrogate from scratch (including UQ calibration, validation)
6. Designate as operational baseline; archive prior surrogate and artifacts

### Key Insight
"Retraining provides a clean, traceable reset that aligns with DOE's emphasis on lifecycle documentation and reproducibility"

### Governance Connection
- Full retraining is invoked when incremental updates fail acceptance criteria
- Prior surrogate is archived, not reverted to
- New baseline requires full verification/validation cycle

---

## 5. STYLE REQUIREMENTS

### Document Style
- DOE Technical Report format
- Clear trigger conditions
- Process steps with governance emphasis
- Technical precision

### Section Structure
```
### 3.3.6 Full Retraining

#### Trigger Conditions
[When full retraining is required]

#### Retraining Process
[Step-by-step workflow]

#### Governance Requirements
[Documentation, archival, traceability]
```

### Target Length
- Original: ~30 lines
- Target: ~25-35 lines (preserve technical depth)

---

## 6. OUTPUT REQUIREMENTS

### Output File
`drafts/section3/section3_3_6_retrain_REVISED.md`

### Quality Checklist
Before finalizing, verify:
- [ ] Parisi et al. (2019) citation preserved
- [ ] Wen et al. (2021) citation preserved
- [ ] Trigger conditions listed
- [ ] Process steps included
- [ ] Governance/archival requirements mentioned
- [ ] DOE Technical Report style applied

---

## 7. CONTEXT LOADING INSTRUCTIONS

When executing this task:
1. Load this task file first
2. Load `plans/extracts/citations_section3.md` (Section 3.3.6 portion only)
3. Load source lines 925-954 from `manuscript/Framework_draft.docx`
4. Do NOT load other sections to preserve context window

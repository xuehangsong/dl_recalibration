# Task: Section 3.3.3 Continual Learning Revision

## Task ID: SECTION3_3_3_CONTINUAL
## Status: PENDING
## Priority: HIGH

---

## 1. OBJECTIVE

Revise Section 3.3.3 (Continual Learning) from the original document into DOE Technical Report style while **preserving ALL citations and specific values**.

---

## 2. SOURCE MATERIAL

### Source File
`manuscript/Framework_draft.docx`

### Source Line Range
**Lines 827-858** (Section 3.3.3 Continual Learning)

---

## 3. MANDATORY CITATIONS TO PRESERVE

### Core Method Citations (MUST INCLUDE ALL)
| Method | Citation | Context |
|--------|----------|---------|
| Elastic Weight Consolidation (EWC) | (Kirkpatrick et al., 2017) | Regularization-based continual learning |
| Replay-based strategies | (De Lange et al., 2021) | Stability via historical samples |
| Sequential fine-tuning | (Hurtado et al., 2023) | Outperforms static surrogates |
| Long-horizon forecasting | (Sayed et al., 2025) | Operational forecasting applications |
| Hydrologic surrogate modeling | (Asher et al., 2015; Wang et al., 2023) | Domain-specific applications |
| Uncertainty calibration | (Zhu et al., 2019; Wen et al., 2021) | UQ practices in hydrology |

### Citation Verification Checklist
After revision, verify these citations appear:
- [ ] Kirkpatrick et al. (2017) - EWC
- [ ] De Lange et al. (2021) - replay strategies
- [ ] Hurtado et al. (2023) - sequential fine-tuning
- [ ] Asher et al. (2015) - surrogate review
- [ ] Wen et al. (2021) - uncertainty calibration

---

## 4. CRITICAL VALUES TO PRESERVE

### Specific Numbers (MUST INCLUDE)
| Value | Context | Source Line |
|-------|---------|-------------|
| **70-75%** | Replay buffer ratio (historical samples in batch) | Line 833 |

### Technical Parameters
- Freeze early encoder layers
- Small learning rate for later layers
- EWC or L2 anchoring regularization
- Early stopping when improvements plateau

---

## 5. KEY CONCEPTS TO PRESERVE

### Two Continual Learning Categories
1. **Regularization-based** - constrain parameter updates (EWC)
2. **Replay-based** - include historical samples during updating

### Fine-tuning Process Steps
1. Assemble compact update dataset:
   - Targeted physics simulations (new regime)
   - Recent validated field observations
   - Replay sample of historical cases (70-75% of batch)
2. Freeze early encoder layers
3. Update later layers with small learning rate + regularization
4. Monitor validation performance, early stopping
5. Recalibrate predictive uncertainty
6. Prepare governance package with pre/post metrics

### Key Insight
"Frequent retraining is unnecessary—and often destabilizing—when well-designed continual learning mechanisms are in place"

---

## 6. STYLE REQUIREMENTS

### Document Style
- DOE Technical Report format
- Clear method-citation pairing
- Include specific values (70-75%)
- Technical precision

### Section Structure
```
### 3.3.3 Continual Learning

#### Approach Categories
[Regularization vs replay-based with citations]

#### Fine-tuning Process
[Step-by-step with specific values]

#### Governance Integration
[Documentation requirements]
```

### Target Length
- Original: ~30 lines
- Target: ~25-35 lines (preserve technical depth)

---

## 7. OUTPUT REQUIREMENTS

### Output File
`drafts/section3/section3_3_3_continual_REVISED.md`

### Quality Checklist
Before finalizing, verify:
- [ ] Kirkpatrick et al. (2017) EWC citation preserved
- [ ] De Lange et al. (2021) replay citation preserved
- [ ] **70-75% replay ratio** explicitly stated
- [ ] Two categories (regularization, replay) distinguished
- [ ] Fine-tuning steps included
- [ ] DOE Technical Report style applied

---

## 8. CONTEXT LOADING INSTRUCTIONS

When executing this task:
1. Load this task file first
2. Load `plans/extracts/citations_section3.md` (Section 3.3.3 portion only)
3. Load source lines 827-858 from `manuscript/Framework_draft.docx`
4. Do NOT load other sections to preserve context window

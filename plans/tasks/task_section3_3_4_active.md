# Task: Section 3.3.4 Active Learning Revision

## Task ID: SECTION3_3_4_ACTIVE
## Status: PENDING
## Priority: HIGH

---

## 1. OBJECTIVE

Revise Section 3.3.4 (Active Learning) from the original document into DOE Technical Report style while **preserving ALL citations and specific values**.

---

## 2. SOURCE MATERIAL

### Source File
`manuscript/Framework_draft.docx`

### Source Line Range
**Lines 861-890** (Section 3.3.4 Active Learning)

---

## 3. MANDATORY CITATIONS TO PRESERVE

### Core Method Citations (MUST INCLUDE ALL)
| Method | Citation | Context |
|--------|----------|---------|
| Uncertainty sampling | (Settles, 2009) | Select high predictive variance locations |
| Error-based sampling | (Cohn et al., 1996) | Target large/persistent residuals |
| Groundwater applications | (Wang et al., 2023) | Inversion, transport, CO₂ storage |
| Diversity constraints | (Wen et al., 2021) | Prevent sampling redundancy |
| Batch active learning | (Vesselinov et al., 2017) | Batch size recommendations |

### Citation Verification Checklist
After revision, verify these citations appear:
- [ ] Settles (2009) - uncertainty sampling
- [ ] Cohn et al. (1996) - error-based sampling
- [ ] Wang et al. (2023) - hydrologic applications
- [ ] Wen et al. (2021) - diversity constraints
- [ ] Vesselinov et al. (2017) - batch size

---

## 4. CRITICAL VALUES TO PRESERVE

### Specific Numbers (MUST INCLUDE)
| Value | Context | Source Line |
|-------|---------|-------------|
| **6-10** | Number of high-value simulations per batch | Line 873 |

---

## 5. KEY CONCEPTS TO PRESERVE

### Active Learning Strategies
1. **Uncertainty sampling** - select locations with high predictive variance
2. **Error-based sampling** - target regions with large/persistent residuals
3. **Diversity constraints** - spatial dispersion, stratigraphic coverage, forcing variability

### Active Learning Process Steps
1. Generate candidate pool of operationally relevant scenarios
2. Score candidates using uncertainty and error metrics
3. Apply diversity constraints (hydraulic gradients, hydrostratigraphic units, forcing conditions)
4. Select **6-10 high-value simulations** maximizing expected information gain
5. Document simulation rationale
6. Execute and incorporate into fine-tuning batch

### Key Insight
"Active learning is invoked only when a quarterly update is justified by monitoring diagnostics"

---

## 6. STYLE REQUIREMENTS

### Document Style
- DOE Technical Report format
- Clear method-citation pairing
- Include specific values (6-10 simulations)
- Technical precision

### Section Structure
```
### 3.3.4 Active Learning

#### Sampling Strategies
[Uncertainty, error-based, diversity with citations]

#### Selection Process
[Step-by-step with specific values]

#### Integration with Continual Learning
[Connection to fine-tuning]
```

### Target Length
- Original: ~30 lines
- Target: ~25-35 lines (preserve technical depth)

---

## 7. OUTPUT REQUIREMENTS

### Output File
`drafts/section3/section3_3_4_active_REVISED.md`

### Quality Checklist
Before finalizing, verify:
- [ ] Settles (2009) uncertainty sampling citation preserved
- [ ] Cohn et al. (1996) error-based citation preserved
- [ ] **6-10 simulations** batch size explicitly stated
- [ ] Diversity constraints mentioned
- [ ] Process steps included
- [ ] DOE Technical Report style applied

---

## 8. CONTEXT LOADING INSTRUCTIONS

When executing this task:
1. Load this task file first
2. Load `plans/extracts/citations_section3.md` (Section 3.3.4 portion only)
3. Load source lines 861-890 from `manuscript/Framework_draft.docx`
4. Do NOT load other sections to preserve context window

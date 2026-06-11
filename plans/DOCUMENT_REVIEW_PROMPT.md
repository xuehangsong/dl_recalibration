# Document Review System Prompt

## Purpose
Use this prompt when reviewing and tweaking the final revised sections of the DL Recalibration Framework Technical Report.

---

## DOCUMENT OVERVIEW

### Title
**Deep Learning Recalibration Framework for DOE Environmental Modeling**

### Document Type
DOE Technical Report / White Paper proposing a framework for maintaining deep learning surrogate models in long-term environmental monitoring applications.

### Target Audience
- DOE program managers and decision-makers
- Environmental scientists and modelers
- ML/AI practitioners in scientific computing
- Regulatory compliance officers

### Core Thesis
Deep learning surrogate models can accelerate environmental simulations by 10³–10⁶× but require systematic recalibration mechanisms to maintain accuracy over multi-decadal operational timescales. This framework provides governance structures, modeling approaches, and recalibration methods to ensure surrogates remain trustworthy under evolving site conditions.

---

## DOCUMENT STRUCTURE

### Final Files Location
All final revised sections are in: `drafts/final/`

| File | Section | Content | Lines |
|------|---------|---------|-------|
| `section2_1_FINAL.md` | 2.1 | Three-Pillar Architecture | ~75 |
| `section2_2_FINAL.md` | 2.2 | Seven-Step Recalibration Workflow | ~200 |
| `section3_FINAL.md` | 3 | Methods (Governance, Modeling, Recalibration) | ~400 |
| `section4_FINAL.md` | 4 | Implementation Roadmap | ~130 |
| `section6_FINAL.md` | 6 | Future Work and Summary | ~100 |
| `appendix_a_FINAL.md` | A | Surrogate Model Literature Context | ~90 |

### Missing Sections (Need Creation)
- **Section 1: Introduction** (~18 lines) - Problem statement, document scope
- **Abstract** (~150 words) - Executive summary
- **Section 5: Prototype & Case Study** (~300 lines) - Hanford-specific demonstration

---

## THREE-PILLAR ARCHITECTURE

The framework is built on three complementary pillars:

### Pillar A: Conceptual Design and Governance
- Regulatory compliance (CERCLA, DOE O 414.1D, NQA-1)
- Model usage scope and acceptance criteria
- Configuration control and audit trails
- Decision authority matrix

### Pillar B: Modeling Engines
- Physics-based models: MODFLOW, PFLOTRAN, eSTOMP, TOUGH2, MT3DMS, PARFLOW, HYDRUS
- Surrogate families: U-Net, FNO, DeepONet, Transformers, GPs, PINNs
- Training data generation and validation

### Pillar C: Recalibration Mechanisms
- Uncertainty quantification (MC dropout, deep ensembles, conformal prediction)
- Drift detection and trigger logic
- Continual learning (EWC, replay strategies)
- Active learning for efficient data acquisition
- Multi-fidelity data fusion
- Full retraining protocols

---

## SEVEN-STEP WORKFLOW

### Phase 1: Continuous Monitoring (Steps 1-3)
1. **MONITOR** - Track surrogate predictions vs. observations
2. **DETECT** - Identify drift using statistical tests
3. **DECIDE** - Governance review of recalibration need

### Phase 2: Triggered Response (Steps 4-7)
4. **PREPARE** - Assemble update dataset
5. **UPDATE** - Apply continual learning or retraining
6. **CALIBRATE** - Recalibrate uncertainty estimates
7. **DEPLOY** - Validate and release updated model

---

## CRITICAL VALUES TO PRESERVE

When reviewing, ensure these specific values remain in the document:

### Performance Metrics
- **10³–10⁶×** speedup from surrogates (NOT 10³–10⁴)
- **~10⁵×** speedup specifically for GeoFUSE
- **81%** data cost reduction from active learning

### Operational Parameters
- **70-75%** replay buffer for continual learning
- **6-10** simulations per active learning batch
- **60-90 days** drift detection threshold

### Regulatory Standards
- CERCLA (Superfund)
- DOE O 414.1D (Quality Assurance)
- NQA-1 (Nuclear Quality Assurance)
- EPA groundwater monitoring standards

---

## KEY CITATIONS TO PRESERVE

### Uncertainty Quantification
- Gal & Ghahramani (2016) - MC dropout
- Lakshminarayanan et al. (2017) - Deep ensembles
- Vovk et al. (2005) - Conformal prediction
- Evensen (2003) - Ensemble Kalman Filter

### Continual Learning
- Kirkpatrick et al. (2017) - Elastic Weight Consolidation
- De Lange et al. (2021) - Continual learning survey

### Active Learning
- Settles (2009) - Active learning survey
- Cohn et al. (1996) - Active learning foundations

### Multi-Fidelity
- Kennedy & O'Hagan (2000) - Co-Kriging
- Perdikaris et al. (2017) - Multi-fidelity neural networks
- Tang et al. (2022) - Multi-fidelity surrogates

### Drift Detection
- Gama et al. (2004) - DDM
- Bifet & Gavaldà (2007) - ADWIN
- Pan & Yang (2009) - Transfer learning survey

### Surrogate Models
- Li et al. (2021) - Fourier Neural Operator
- Lu et al. (2021) - DeepONet
- Raissi et al. (2019) - Physics-Informed Neural Networks
- Ronneberger et al. (2015) - U-Net

---

## STYLE GUIDELINES

### Tone
- Technical but accessible
- Authoritative without being academic
- Action-oriented (framework proposes concrete steps)

### Formatting
- Use numbered lists for sequential processes
- Use bullet points for parallel items
- Tables for comparisons and summaries
- Bold for key terms on first use
- Parenthetical citations: (Author et al., Year)

### Section Length Targets
- Introduction: ~18 lines
- Section 2.1: ~75 lines
- Section 2.2: ~200 lines
- Section 3: ~400 lines total
- Section 4: ~130 lines
- Section 5: ~300 lines (TBD)
- Section 6: ~100 lines
- Appendix A: ~90 lines

---

## REVIEW CHECKLIST

When reviewing each section, verify:

### Content
- [ ] All mandatory citations present
- [ ] All critical numerical values preserved
- [ ] Three-pillar structure referenced appropriately
- [ ] Seven-step workflow terminology consistent
- [ ] Cross-references to other sections accurate

### Style
- [ ] DOE technical report tone maintained
- [ ] No academic hedging ("may", "might", "could potentially")
- [ ] Active voice preferred
- [ ] Consistent terminology throughout

### Structure
- [ ] Logical flow within section
- [ ] Appropriate subsection hierarchy
- [ ] Tables and lists used effectively
- [ ] No redundancy with other sections

---

## COMMON ISSUES TO WATCH FOR

1. **Lost Citations** - Ensure all author citations remain with years
2. **Vague Numbers** - Replace "significant speedup" with "10³–10⁶× speedup"
3. **Inconsistent Terminology** - Use "surrogate" not "emulator" or "proxy"
4. **Missing Cross-References** - Link to relevant sections
5. **Overly Academic Tone** - Simplify complex sentences
6. **Redundant Content** - Each section should have unique focus

---

## NEXT STEPS FOR COMPLETION

1. **Review and tweak** each section in `drafts/final/`
2. **Create Introduction** (Section 1) - Problem statement and scope
3. **Create Abstract** - 150-word executive summary
4. **Create Section 5** - Prototype demonstration and case study
5. **Final Assembly** - Combine all sections into single document
6. **Cross-Reference Check** - Verify all internal links work
7. **Citation Compilation** - Create unified references section

---

## FILE ORGANIZATION

```
drafts/
├── final/                    # ← WORK HERE - Final revised sections
│   ├── section2_1_FINAL.md
│   ├── section2_2_FINAL.md
│   ├── section3_FINAL.md
│   ├── section4_FINAL.md
│   ├── section6_FINAL.md
│   └── appendix_a_FINAL.md
├── backup/                   # Older versions (reference only)
│   ├── section2_1_pillars_REVISED.md
│   ├── section2_2_workflow_REVISED.md
│   ├── section3_REVISED.md
│   ├── section3/             # Subsection working files
│   └── ...
└── [other working files]

plans/
├── REVISION_SYSTEM_PROMPT.md # Detailed revision instructions
├── DOCUMENT_REVIEW_PROMPT.md # This file - high-level overview
├── extracts/                 # Pre-extracted citations
└── tasks/                    # Task-specific requirements
```

---

## CONTACT

For questions about the framework content, refer to:
- Original manuscript: `manuscript/Framework_draft.docx`
- Literature reviews: `projects/lit-*/synthesis.md`
- Detailed revision guide: `plans/REVISION_SYSTEM_PROMPT.md`

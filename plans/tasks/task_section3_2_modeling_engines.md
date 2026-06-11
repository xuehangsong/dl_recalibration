# Task: Section 3.2 Modeling Engines Revision

## Task ID: SECTION3_2_MODELING_ENGINES
## Status: PENDING
## Priority: HIGH

---

## 1. OBJECTIVE

Revise Section 3.2 (Modeling Engines) from the original document into DOE Technical Report style while **preserving ALL citations and model names**.

---

## 2. SOURCE MATERIAL

### Source File
`manuscript/Framework_draft.docx`

### Source Line Range
**Lines 507-627** (Section 3.2 Modeling Engines)

### Subsections to Process
- 3.2.1 Site Challenges and Modeling Needs (Lines 509-520)
- 3.2.2 Physics-Based Numerical Models (Lines 521-531)
- 3.2.3 Surrogate Model Landscape (Lines 533-612)
- 3.2.4 General Surrogate Model Training Setup (Lines 615-627)

---

## 3. MANDATORY CITATIONS TO PRESERVE

### Physics Model Citations (MUST INCLUDE ALL)
| Model | Citation |
|-------|----------|
| MODFLOW | (Harbaugh, 2005) |
| PFLOTRAN | (Hammond et al., 2014) |
| eSTOMP | (White and Oostrom, 2003) |
| TOUGH2 | (Pruess et al., 1999) |
| MT3DMS | (Zheng and Wang, 1999) |
| PARFLOW | (Maxwell et al., 2015) |
| HYDRUS | (Šimůnek et al., 2016) |

### Site Challenges Citations
| Topic | Citation |
|-------|----------|
| Advection/dispersion | (Sethi and Di Molfetta, 2019; Šimůnek and van Genuchten, 2016) |
| Non-Fickian dispersion | (Guo et al., 2021) |
| Back diffusion | (Yang et al., 2016, 2017) |
| DNAPL/LNAPL | (Huling, 1991; McCaulou, 1995; Newell, 1995; RMCS, 2017) |
| Seawater intrusion | (Werner et al., 2013; Xu et al., 2019) |
| Pump-and-treat | (Ko et al., 2005) |

### Surrogate Model Citations
| Model Family | Key Citations |
|--------------|---------------|
| U-Net/CNN | Taccari et al. (2022), Mo et al. (2019), Jiang et al. (2021), Lauzon (2024) |
| FNO/U-FNO | Li et al. (2020), Wen et al. (2022), Jiang et al. (2025) |
| DeepONet | Taccari et al. (2024) |
| LSTM/GRU | Chen et al. (2021), Anshuman and Eldho (2023), Li et al. (2025) |
| Generative | Graham and Chen (2020), Miele and Linde (2025), Wang et al. (2025b,c) |
| GP/Kriging | Asher et al. (2015), Siade et al. (2020), Shams et al. (2021) |

### Citation Verification Checklist
After revision, verify these citations appear:
- [ ] All 7 physics model names with citations
- [ ] At least 3 U-Net/CNN citations
- [ ] FNO and U-FNO citations (Li et al., Wen et al.)
- [ ] GeoFUSE/Jiang et al. (2025) mentioned
- [ ] GP/Kriging citations for regression surrogates
- [ ] Review paper (Luo et al., 2023) referenced

---

## 4. KEY CONCEPTS TO PRESERVE

### Physics Model Capabilities
1. Advection, dispersion, sorption, reaction processes
2. Non-Fickian plume spreading from heterogeneity
3. Back diffusion from low-permeability zones
4. Density-driven flow (DNAPL, LNAPL, seawater)
5. Pump-and-treat system representation

### Surrogate Model Families (5 categories)
1. **Convolutional encoder-decoder** (U-Net, ResNet) - spatial fields
2. **Operator-learning** (FNO, U-FNO, DeepONet) - PDE solution operators
3. **Sequence models** (LSTM, GRU, Transformer) - time series
4. **Generative models** (VAE, GAN, diffusion) - ensemble sampling
5. **Regression surrogates** (GP, Kriging, shallow ANN) - scalar metrics

### Specific Technical Details
- Forward runs: hours to days on standard computing
- Speedup: orders of magnitude (10³-10⁴×)
- Training data: Monte Carlo ensembles
- GeoFUSE: ~10⁵ speedup per inference

---

## 5. STYLE REQUIREMENTS

### Document Style
- DOE Technical Report format
- Technical precision with citations
- Organize by surrogate family
- Include computational context

### Section Structure
```
## 3.2 Modeling Engine Methods

### 3.2.1 Site Challenges and Modeling Needs
[Physics processes with citations]

### 3.2.2 Physics-Based Numerical Models
[Model names with citations, computational costs]

### 3.2.3 Surrogate Model Landscape
[5 families with key citations each]

### 3.2.4 Training Setup
[Data splits, normalization, early stopping]
```

### Target Length
- Original: ~120 lines
- Target: ~80-100 lines (streamlined but complete)

---

## 6. OUTPUT REQUIREMENTS

### Output File
`drafts/section3/section3_2_modeling_engines_REVISED.md`

### Quality Checklist
Before finalizing, verify:
- [ ] All 7 physics models named with citations
- [ ] 5 surrogate families clearly distinguished
- [ ] Key citations for each family preserved
- [ ] Computational speedup mentioned
- [ ] GeoFUSE example included
- [ ] DOE Technical Report style applied

---

## 7. CONTEXT LOADING INSTRUCTIONS

When executing this task:
1. Load this task file first
2. Load `plans/extracts/citations_section3.md` (Section 3.2 portion only)
3. Load source lines 507-627 from `manuscript/Framework_draft.docx`
4. Do NOT load other sections to preserve context window

---

## 8. NOTE ON APPENDIX A

Detailed surrogate model literature review content (Tables A1, A2) should be moved to Appendix A, not included in Section 3.2. Section 3.2 provides the conceptual overview; Appendix A provides the detailed paper-by-paper analysis.

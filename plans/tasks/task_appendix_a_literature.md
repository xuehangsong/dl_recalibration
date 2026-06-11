# Task: Appendix A - Surrogate Model Literature Revision

## Priority: HIGH
## Status: PENDING
## Dependencies: Section 3 complete

---

## 1. OBJECTIVE

Revise Appendix A (Surrogate Model Literature Context) to add specific author citations from the literature review projects. The current draft has generic descriptions without proper scholarly attribution.

---

## 2. SOURCE MATERIAL

### Current Draft
- File: `drafts/appendix_a_REVISED.md`
- Lines: 1-92

### Citation Source
- File: `plans/extracts/citations_section6_appendixA.md`
- Section: "APPENDIX A: SURROGATE MODEL LITERATURE"

### Additional Source
- File: `projects/lit-surrogate-models/synthesis.md`
- Contains detailed citations for all surrogate families

---

## 3. MANDATORY CITATIONS BY FAMILY

### A.2.1 Convolutional Encoder-Decoder Models (at least 4)
- **Taccari et al. (2022)** - Attention U-Net for groundwater
- **Taccari et al. (2024)** - U-Net with geostatistical spectral algorithms
- **Yu et al. (2020)** - Deep learning emulators for contaminant transport
- **Tang et al. (2020)** - 3D convLSTM for dynamic subsurface flow
- Li et al. (2025) - Hybrid DSCNN-GRU (optional)
- Bhatt et al. (2024) - Dual-path CNN-MLP (optional)

### A.2.2 Operator-Learning Models (at least 5)
- **Li et al. (2021)** - FNO foundational paper (ICLR)
- **Wen et al. (2022)** - U-FNO for multiphase flow
- **Lu et al. (2021)** - DeepONet (Nature Machine Intelligence)
- **Kurihana et al. (2022)** - Physics-informed U-FNO
- **Tang et al. (2024)** - Multi-fidelity FNO (81% less data)
- Chen et al. (2024) - GeoFUSE (optional)
- Li et al. (2023) - GINO (optional)

### A.2.3 Sequence Models (at least 2)
- **Li et al. (2023)** - Scalable Transformer (FactFormer)
- **Huan et al. (2022)** - Transformer for contamination source ID
- Lin et al. (2025) - U-Net with Vision Transformer (optional)
- Wen et al. (2025) - GAOT (optional)

### A.2.4 Generative Models (at least 1)
- Mention VAE, GAN, diffusion models with general context
- Shin et al. (2017) - Generative replay (from continual learning)

### A.2.5 Regression and Classical Surrogates (at least 3)
- **Razavi et al. (2012)** - Review of surrogate modeling
- **Asher et al. (2015)** - Review of surrogates for groundwater
- **Pool et al. (2025)** - ML surrogates for hydrologic modeling
- Deman et al. (2016) - PCE for groundwater UQ (optional)

### A.2.6 Physics-Informed Neural Networks (at least 2)
- **Raissi et al. (2019)** - PINN foundational paper
- **He et al. (2020)** - PINNs for groundwater flow
- Zhang et al. (2022) - PINNs for transient problems (optional)

---

## 4. CRITICAL VALUES TO INCLUDE

| Value | Context | Source |
|-------|---------|--------|
| <5% prediction error | U-Net for groundwater | Taccari et al. (2022) |
| ~2% mean relative error | Physics-informed DeepONet | Meng et al. (2024) |
| 81% less data cost | Multi-fidelity FNO | Tang et al. (2024) |
| 10³-10⁶ speedup | General DL surrogates | Literature synthesis |
| ~10⁵ speedup | GeoFUSE framework | Chen et al. (2024) |

---

## 5. STRUCTURE REQUIREMENTS

### A.1 Literature Review Methodology
- Keep brief (current is fine)
- Mention 2018-2024 publication range
- Note six architectural families

### A.2 Surrogate Model Families: Detailed Review

#### A.2.1 Convolutional Encoder-Decoder Models
- U-Net architecture explanation
- Attention mechanisms (Taccari et al., 2022)
- Applications to groundwater (Yu et al., 2020; Tang et al., 2020)
- Transient flow (Taccari et al., 2024)

#### A.2.2 Operator-Learning Models
- FNO explanation (Li et al., 2021)
- U-FNO for porous media (Wen et al., 2022)
- DeepONet architecture (Lu et al., 2021)
- Multi-fidelity approaches (Tang et al., 2024)

#### A.2.3 Sequence Models
- LSTM/GRU for time series
- Transformers for PDEs (Li et al., 2023)
- Groundwater applications (Huan et al., 2022)

#### A.2.4 Generative Models
- VAE and GAN overview
- Applications to uncertainty quantification

#### A.2.5 Regression and Classical Surrogates
- Gaussian Process foundations
- Comparison with deep learning (Pool et al., 2025)
- Review papers (Razavi et al., 2012; Asher et al., 2015)

#### A.2.6 Structured Domain Surrogates
- PINNs (Raissi et al., 2019)
- Groundwater applications (He et al., 2020)

### A.3 Literature Analysis Summary
- Trends in hybrid architectures
- UQ importance
- Transfer learning directions

### A.4 Implications for Framework Design
- Architecture selection guidance
- UQ recommendations
- Continual learning compatibility

---

## 6. STYLE REQUIREMENTS

### Document Style
- DOE Technical Report prose
- Academic tone with proper citations
- Tables allowed for comparisons

### Citation Format
- Author et al. (Year) for in-text citations
- Integrate citations naturally into sentences

### Target Length
- 100-120 lines (current is 92 - needs expansion for citations)

---

## 7. OUTPUT

### Output File
`drafts/appendix_a_FINAL.md`

### Quality Checklist
- [ ] At least 15 author citations included
- [ ] U-Net citations (Taccari 2022, 2024; Yu 2020; Tang 2020)
- [ ] FNO citations (Li 2021, Wen 2022)
- [ ] DeepONet citations (Lu 2021)
- [ ] PINN citations (Raissi 2019, He 2020)
- [ ] Classical surrogate citations (Razavi, Asher, Pool)
- [ ] Multi-fidelity citations (Tang 2024)
- [ ] Speedup values included (10³-10⁶, ~10⁵)
- [ ] Error values included (<5%, ~2%)
- [ ] DOE report prose style maintained
- [ ] Six architectural families covered

---

## 8. CONTEXT LOADING INSTRUCTIONS

1. Load this task file first
2. Load `plans/extracts/citations_section6_appendixA.md` (Appendix A portion)
3. Load `drafts/appendix_a_REVISED.md` (current draft)
4. Optionally load `projects/lit-surrogate-models/synthesis.md` for additional context
5. Revise while checking citation checklist
6. Verify all mandatory citations appear in output

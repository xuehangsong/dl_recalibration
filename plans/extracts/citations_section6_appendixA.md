# Citation Extracts for Section 6 and Appendix A

## Purpose
Pre-extracted citations from literature review projects to ensure they are preserved during revision.

---

## SECTION 6: FUTURE WORK AND SUMMARY

### 6.1 Research Roadmap Citations

#### Digital Twin and HPC Integration
- HP2C-DT framework (Iraola et al., 2025) - High-Precision High-Performance Computer-enabled Digital Twin
- Digital Twin Factory framework (EGU, 2025) - DTaaS architectures
- Digital twin narratives for environmental contexts (Springer, 2023)

#### Continual Learning for Long-term Maintenance
- De Lange et al. (2021) - "A Continual Learning Survey: Defying Forgetting in Classification Tasks" (TPAMI)
- Parisi et al. (2019) - "Continual Learning: A Review" (Neural Networks)
- Wang et al. (2024) - "Continual Learning of Large Language Models: A Comprehensive Survey"

#### Active Learning for Efficient Updates
- Settles (2009) - Active Learning Literature Survey (~5000 citations)
- Yuan et al. (2024) - "A Survey on Deep Active Learning: Recent Advances and New Frontiers"
- Kottke et al. (2023) - Active learning for data streams

### 6.2 Expected Impact Citations

#### Speedup Values (CRITICAL - must preserve)
- **~10⁵ speedup** - GeoFUSE framework (Chen et al., 2024)
- **10³ to 10⁶ speedup** - General deep learning surrogates (synthesis document)
- **81% less data generation cost** - Multi-fidelity FNO (Tang et al., 2024)

#### Scientific Contributions
- Knowledge-guided machine learning (Karpatne et al., 2023) - Nature Reviews
- Xu et al. (2021) - "Machine learning for hydrologic sciences: An introductory overview"
- Schmidt et al. (2020) - "Challenges in Applying ML Models for Hydrological Inference"

### 6.3 Limitations and Open Questions

#### Drift Detection
- Gama et al. (2004) - DDM (Drift Detection Method) ~3000 citations
- Bifet & Gavaldà (2007) - ADWIN ~2500 citations
- Gómez et al. (2020) - "Learning under Concept Drift: A Review"

#### Transfer Learning
- Pan & Yang (2009) - IEEE TKDE Transfer Learning Survey ~10,000 citations
- Wang & Deng (2020) - "A Survey of Unsupervised Deep Domain Adaptation"

---

## APPENDIX A: SURROGATE MODEL LITERATURE

### A.1 Convolutional Encoder-Decoder Models

#### U-Net and Variants
- **Taccari et al. (2022)** - Attention U-Net for groundwater, Advances in Water Resources
- **Taccari et al. (2024)** - U-Net with geostatistical spectral algorithms for transient flow
- **Yu et al. (2020)** - Deep learning emulators for groundwater contaminant transport
- **Tang et al. (2020)** - 3D convLSTM for dynamic subsurface flow
- **Li et al. (2025)** - Hybrid DSCNN-GRU for transient groundwater flow
- **Bhatt et al. (2024)** - Dual-path CNN-MLP for regional groundwater (Qatar aquifer)

### A.2 Operator-Learning Models

#### Fourier Neural Operators
- **Li et al. (2021)** - FNO foundational paper, ICLR
- **Wen et al. (2022)** - U-FNO for multiphase flow, Advances in Water Resources
- **Kurihana et al. (2022)** - Physics-informed U-FNO for groundwater contamination
- **Tang et al. (2024)** - Multi-fidelity FNO, 81% less data cost
- **Chen et al. (2024)** - GeoFUSE (U-FNO + PCA + ES-MDA) for seawater intrusion
- **Li et al. (2023)** - GINO (Geometry-Informed Neural Operator)

#### DeepONet
- **Lu et al. (2021)** - DeepONet foundational paper, Nature Machine Intelligence
- **Meng et al. (2024)** - Physics-informed DeepONet for advection-dominated PDEs (~2% error)
- **Wang et al. (2021)** - Improved DeepONet architectures

### A.3 Sequence Models

#### LSTM and Transformers
- **Li et al. (2023)** - Scalable Transformer (FactFormer) for PDE surrogates
- **Lin et al. (2025)** - U-Net with Vision Transformer for reservoir modeling
- **Huan et al. (2022)** - Transformer for groundwater contamination source identification
- **Wen et al. (2025)** - GAOT (Geometry-Aware Operator Transformer)

### A.4 Generative Models

#### VAE and GAN
- Variational Autoencoders for hydraulic conductivity field generation
- Conditional GANs for uncertainty quantification
- Diffusion models (emerging for scientific applications)

### A.5 Classical Surrogates

#### Gaussian Processes
- **Pool et al. (2025)** - ML surrogates for hydrologic modeling (GP comparison)
- **Razavi et al. (2012)** - Review of surrogate modeling in water resources
- **Asher et al. (2015)** - Review of surrogate models for groundwater

#### Polynomial Chaos Expansion
- **Deman et al. (2016)** - PCE for groundwater uncertainty quantification

### A.6 Physics-Informed Neural Networks

- **Raissi et al. (2019)** - PINN foundational paper, Journal of Computational Physics
- **He et al. (2020)** - PINNs for groundwater flow, Advances in Water Resources
- **Zhang et al. (2022)** - PINNs for transient groundwater problems

### A.7 Multi-Fidelity and Hybrid Approaches

- **Jiang & Durlofsky (2022)** - Multi-fidelity transfer learning for subsurface flow
- **Kennedy & O'Hagan (2000)** - Co-Kriging foundational work
- **Perdikaris et al. (2017)** - Multi-fidelity neural networks

---

## CRITICAL VALUES TO PRESERVE

| Value | Context | Source |
|-------|---------|--------|
| ~10⁵ speedup | GeoFUSE framework | Chen et al. (2024) |
| 10³-10⁶ speedup | General DL surrogates | Literature synthesis |
| 81% less data cost | Multi-fidelity FNO | Tang et al. (2024) |
| ~2% mean relative error | Physics-informed DeepONet | Meng et al. (2024) |
| <5% prediction error | U-Net for groundwater | Taccari et al. (2022) |
| ~5000 citations | Settles AL survey | Settles (2009) |
| ~10,000 citations | Pan & Yang TL survey | Pan & Yang (2009) |
| ~3000 citations | DDM paper | Gama et al. (2004) |

---

## CITATION VERIFICATION CHECKLIST

### Section 6 Must Include:
- [ ] At least 3 continual learning citations (De Lange, Parisi, Wang)
- [ ] At least 2 active learning citations (Settles, Yuan/Kottke)
- [ ] At least 2 drift detection citations (Gama/DDM, Bifet/ADWIN)
- [ ] Speedup value (~10⁵ or 10³-10⁶)
- [ ] Knowledge-guided ML reference (Karpatne et al.)

### Appendix A Must Include:
- [ ] U-Net citations (Taccari 2022, 2024)
- [ ] FNO citations (Li 2021, Wen 2022)
- [ ] DeepONet citations (Lu 2021)
- [ ] PINN citations (Raissi 2019)
- [ ] Multi-fidelity citations (Tang 2024, Kennedy & O'Hagan 2000)
- [ ] At least 15 total author citations

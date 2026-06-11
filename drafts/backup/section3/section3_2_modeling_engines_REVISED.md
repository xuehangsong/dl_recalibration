# 3.2 Modeling Engine Methods

This section describes the physics-based numerical models and deep-learning surrogates that form Pillar B of the recalibration framework. Physics models provide high-fidelity reference simulations; surrogates provide fast inference for screening and scenario analysis.

## 3.2.1 Site Challenges and Modeling Needs

Numerical groundwater and reactive transport models provide the high-fidelity representation of site-specific subsurface processes that underpin Pillar B. At EM sites, these models describe how contaminants move and transform in complex hydrogeologic settings, and how engineered controls (e.g., pump-and-treat systems) influence plume evolution.

The physical phenomena represented typically include:

- **Advection and dispersion** of dissolved species (Sethi and Di Molfetta, 2019; Šimůnek and van Genuchten, 2016)
- **Sorption** onto solid phases and associated reaction processes
- **Non-Fickian plume spreading** from heterogeneity and diffusion-controlled mass exchange between transmissive and low-permeability zones (Guo et al., 2021)
- **Back diffusion** from fine-grained units, recognized as a major control on plume persistence after source removal (Yang et al., 2016, 2017)
- **Density-driven flow** in systems impacted by DNAPL, LNAPL (Huling, 1991; McCaulou, 1995; Newell, 1995; RMCS, 2017), or seawater intrusion (Werner et al., 2013; Xu et al., 2019)
- **Engineered operations** including pump-and-treat wells, injection/extraction networks, and time-varying boundary conditions (Ko et al., 2005)

These mechanisms explain why plumes can remain above regulatory thresholds long after active remediation has ceased, and must be explicitly represented in numerical models.

## 3.2.2 Physics-Based Numerical Models

Several well-established simulators serve as workhorses for groundwater flow and transport modeling:

| Model | Application | Citation |
|-------|-------------|----------|
| **MODFLOW** | Regional groundwater flow, multi-layer systems | (Harbaugh, 2005) |
| **MT3DMS** | Conservative and reactive solute transport | (Zheng and Wang, 1999) |
| **PFLOTRAN** | Reactive transport, multiphase flow, variable density | (Hammond et al., 2014) |
| **eSTOMP** | Variably saturated flow with geochemical reactions | (White and Oostrom, 2003) |
| **TOUGH2** | Non-isothermal processes, variable fluid density | (Pruess et al., 1999) |
| **PARFLOW** | Integrated surface-subsurface flow at high resolution | (Maxwell et al., 2015) |
| **HYDRUS** | Vadose zone and near-surface transport | (Šimůnek et al., 2016) |

Within Pillar B, these codes collectively form the high-fidelity modeling layer that defines the governing equations, numerical schemes, and parameterizations treated as authoritative reference.

### Computational Constraints

Despite their fidelity, these simulators impose significant computational constraints:

- Individual forward runs can take **hours to days** on standard computing resources (Hammond et al., 2014; Maxwell et al., 2015)
- Planning tasks often require **hundreds to thousands** of model evaluations for Monte Carlo realizations, scenario sweeps, or sensitivity analyses (Rubin, 2003)
- Interactive exploration of design space becomes impractical using only high-fidelity models

These limitations motivate the data-driven surrogate modeling engines that sit on top of the numerical model.

## 3.2.3 Surrogate Model Landscape

Recent work in hydrogeology and subsurface reactive transport has demonstrated that deep-learning surrogates can emulate high-fidelity simulators with **orders-of-magnitude speedup** while retaining accuracy (Li et al., 2020). We organize existing surrogate approaches into five families based on input-output structure and typical EM use-cases (Luo et al., 2023):

### Family 1: Convolutional Encoder-Decoder Models

**Architecture:** U-Net, ResNet variants  
**Use case:** High-resolution spatial fields (heads, salinity, plume extent)

These networks treat spatial fields as images and learn direct mappings from input fields (hydraulic conductivity, boundary conditions, pumping patterns) to output fields. Convolutions preserve interfaces, sharp fronts, and channelized structures.

Key citations:
- Attention U-Net for steady-state hydraulic head fields (Taccari et al., 2022)
- Image-to-image regression for multiphase flow (Mo et al., 2019)
- AR-ResUNet for dynamic multiphase flow and solute transport (Jiang et al., 2021)
- U-Net surrogate for transient groundwater flow inverse problems (Lauzon, 2024)

### Family 2: Operator-Learning Models

**Architecture:** FNO, U-FNO, DeepONet  
**Use case:** Learning PDE solution operators across many boundary/parameter configurations

Operator-learning models generalize beyond pointwise mappings to learn the entire solution operator of the PDE. The Fourier Neural Operator (FNO) learns this operator in Fourier space, enabling resolution-invariant surrogates (Li et al., 2020).

Key citations:
- U-FNO for CO₂-water multiphase systems (Wen et al., 2022)
- DeepONet for confined aquifer flow (Taccari et al., 2024)
- **GeoFUSE framework** for seawater intrusion: U-FNO achieves ~10⁵ speedup per inference relative to PFLOTRAN (Jiang et al., 2025)
- Physics-informed U-FNO for climate stress testing at Savannah River Site (Wang et al., 2022)

### Family 3: Sequence Models

**Architecture:** LSTM, GRU, Transformer variants  
**Use case:** Low-dimensional time series (breakthrough curves, well responses)

Sequence models focus on time series outputs monitored at high frequency. LSTM and GRU networks capture long-range temporal dependencies.

Key citations:
- GRU-based surrogates for groundwater levels and water quality (Chen et al., 2021)
- Encoder-decoder LSTM for contaminant source identification (Anshuman and Eldho, 2023)
- DSCNN-GRU surrogate for transient groundwater head fields (Li et al., 2025)

### Family 4: Generative Models

**Architecture:** VAE, GAN, diffusion models  
**Use case:** Sampling full state ensembles, probabilistic inversion

Generative surrogates sample entire ensembles of plausible states and parameter fields consistent with physics and observations.

Key citations:
- VAE/GAN for facies realizations and Bayesian inversion (Graham and Chen, 2020)
- Diffusion models for multivariate subsurface property fields (Miele and Linde, 2025)
- Pretrained diffusion model for porous-media flow (Wang et al., 2025c)
- Conditional diffusion for CO₂ storage plume forecasting (Wang et al., 2025b)

### Family 5: Regression Surrogates

**Architecture:** Gaussian processes, Kriging, shallow ANNs  
**Use case:** Low-dimensional mappings (design variables → scalar metrics)

For decision-support tasks where quantities of interest are scalar metrics (total cost, cleanup time, risk index), simpler regression surrogates remain powerful tools, especially when data are limited and interpretability matters.

Key citations:
- Review of surrogate models in groundwater (Asher et al., 2015)
- Reduced-dimensional GP regression for groundwater allocation (Siade et al., 2020)
- GP surrogate for surfactant-enhanced aquifer remediation (Shams et al., 2021)
- Advances in GP surrogate construction and validation (Marrel and Iooss, 2024)

## 3.2.4 Training Setup

Standard practices for surrogate model training include:

| Element | Approach |
|---------|----------|
| **Data splits** | Hold out realizations across time and parameter ranges; separate training and test ensembles (Jiang et al., 2025) |
| **Normalization** | Standardize each channel; record scaling in metadata for consistent inference |
| **Early stopping** | Track validation metric on decision outputs, not only global averages; save best checkpoint |
| **Runtime reporting** | Record forward runtime and surrogate inference time to report speedups alongside accuracy |

The numerical models described in this section provide training data, physical grounding, and validation targets for surrogates, while surrogates aim to reproduce key numerical results at a fraction of the computational cost.

---

**Note:** Detailed paper-by-paper analysis of surrogate modeling literature is provided in Appendix A (Tables A1, A2).

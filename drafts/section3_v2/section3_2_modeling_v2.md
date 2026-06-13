# 3.2 Modeling Engine Methods

This section describes the physics-based numerical models and deep-learning surrogates that form Pillar B of the recalibration framework. Physics models provide high-fidelity reference simulations; surrogates provide fast inference for screening and scenario analysis.

## 3.2.1 Site Challenges and Modeling Needs

Numerical groundwater and reactive transport models provide the high-fidelity representation of site-specific subsurface processes that underpin Pillar B. At EM sites, these models describe how contaminants move and transform in complex hydrogeologic settings, and how engineered controls (e.g., pump-and-treat systems) influence plume evolution.

The physical phenomena represented typically include advection and dispersion of dissolved species (Sethi and Di Molfetta, 2019; Šimůnek and van Genuchten, 2016), sorption onto solid phases and associated reaction processes, and non-Fickian plume spreading arising from heterogeneity and diffusion-controlled mass exchange between transmissive and low-permeability zones (Guo et al., 2021). Back diffusion from fine-grained units is recognized as a major control on plume persistence after source removal (Yang et al., 2016, 2017). Density-driven flow occurs in systems impacted by DNAPL or LNAPL (Huling, 1991; McCaulou, 1995; Newell, 1995; RMCS, 2017) or by seawater intrusion (Werner et al., 2013; Xu et al., 2019). Engineered operations, including pump-and-treat wells, injection/extraction networks, and time-varying boundary conditions, must also be represented (Ko et al., 2005).

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

Despite their fidelity, these simulators impose significant computational constraints. Individual forward runs can take hours to days on standard computing resources (Hammond et al., 2014; Maxwell et al., 2015), and planning tasks often require hundreds to thousands of model evaluations for Monte Carlo realizations, scenario sweeps, or sensitivity analyses (Rubin, 2003). As a result, interactive exploration of design space becomes impractical using only high-fidelity models.

These limitations motivate the data-driven surrogate modeling engines that sit on top of the numerical model.

## 3.2.3 Surrogate Model Landscape

Recent work in hydrogeology and subsurface reactive transport has demonstrated that deep-learning surrogates can emulate high-fidelity simulators with **orders-of-magnitude speedup** while retaining accuracy (Li et al., 2020). We organize existing surrogate approaches into five families based on input-output structure and typical EM use-cases (Luo et al., 2023):

### Family 1: Convolutional Encoder-Decoder Models

Convolutional encoder-decoder architectures such as U-Net and ResNet variants are well-suited for predicting high-resolution spatial fields including hydraulic heads, salinity distributions, and plume extents. These networks treat spatial fields as images and learn direct mappings from input fields (hydraulic conductivity, boundary conditions, pumping patterns) to output fields, with convolutions preserving interfaces, sharp fronts, and channelized structures. Representative applications include attention U-Net architectures for steady-state hydraulic head fields (Taccari et al., 2022), image-to-image regression for multiphase flow (Mo et al., 2019), autoregressive residual U-Net (AR-ResUNet) for dynamic multiphase flow and solute transport (Jiang et al., 2021), and U-Net surrogates for transient groundwater flow inverse problems (Lauzon, 2024).

### Family 2: Operator-Learning Models

Operator-learning architectures including FNO, U-FNO, and DeepONet are designed for learning PDE solution operators across many boundary and parameter configurations. These models generalize beyond pointwise mappings to learn the entire solution operator of the PDE, with the Fourier Neural Operator (FNO) learning this operator in Fourier space to enable resolution-invariant surrogates (Li et al., 2020). Notable applications include U-FNO for CO₂-water multiphase systems (Wen et al., 2022), DeepONet for confined aquifer flow (Taccari et al., 2024), the GeoFUSE framework for seawater intrusion where U-FNO achieves approximately 10⁵ speedup per inference relative to PFLOTRAN (Jiang et al., 2025), and physics-informed U-FNO for climate stress testing at Savannah River Site (Wang et al., 2022).

### Family 3: Sequence Models

Sequence architectures including LSTM, GRU, and Transformer variants focus on low-dimensional time series outputs such as breakthrough curves and well responses monitored at high frequency. LSTM and GRU networks capture long-range temporal dependencies essential for forecasting contaminant evolution. Applications include GRU-based surrogates for groundwater levels and water quality (Chen et al., 2021), encoder-decoder LSTM for contaminant source identification (Anshuman and Eldho, 2023), and DSCNN-GRU surrogates for transient groundwater head fields (Li et al., 2025).

### Family 4: Generative Models

Generative architectures including VAE, GAN, and diffusion models are designed for sampling full state ensembles and probabilistic inversion. These surrogates sample entire ensembles of plausible states and parameter fields consistent with physics and observations. Applications include VAE/GAN for facies realizations and Bayesian inversion (Graham and Chen, 2020), diffusion models for multivariate subsurface property fields (Miele and Linde, 2025), pretrained diffusion models for porous-media flow (Wang et al., 2025c), and conditional diffusion for CO₂ storage plume forecasting (Wang et al., 2025b).

### Family 5: Regression Surrogates

Classical regression approaches including Gaussian processes, Kriging, and shallow ANNs remain powerful tools for low-dimensional mappings from design variables to scalar metrics such as total cost, cleanup time, or risk index. These methods are especially valuable when data are limited and interpretability matters. The literature includes comprehensive reviews of surrogate models in groundwater applications (Asher et al., 2015), reduced-dimensional GP regression for groundwater allocation (Siade et al., 2020), GP surrogates for surfactant-enhanced aquifer remediation (Shams et al., 2021), and advances in GP surrogate construction and validation (Marrel and Iooss, 2024).

## 3.2.4 Training Setup

Standard practices for surrogate model training include:

| Element | Approach |
|---------|----------|
| **Data splits** | Hold out realizations across time and parameter ranges; separate training and test ensembles (Jiang et al., 2025) |
| **Normalization** | Standardize each channel; record scaling in metadata for consistent inference |
| **Early stopping** | Track validation metric on decision outputs, not only global averages; save best checkpoint |
| **Runtime reporting** | Record forward runtime and surrogate inference time to report speedups alongside accuracy |

The numerical models described in this section provide training data, physical grounding, and validation targets for surrogates, while surrogates aim to reproduce key numerical results at a fraction of the computational cost.

**Note:** Detailed paper-by-paper analysis of surrogate modeling literature is provided in Appendix A.

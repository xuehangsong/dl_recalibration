# Appendix A: Surrogate Model Literature Context

This appendix provides detailed literature context for the surrogate model landscape discussed in Section 3.2.3. The material presented here supports the framework's modeling engine component (Pillar B) by documenting the current state of deep learning surrogate models for subsurface flow and transport applications.

## A.1 Literature Review Methodology

The surrogate model literature review was conducted using Web of Science with search terms targeting deep learning applications in groundwater modeling, subsurface flow prediction, and contaminant transport simulation. The search covered publications from 2018 to 2024, reflecting the rapid development of deep learning methods for scientific computing during this period. Papers were selected based on relevance to groundwater remediation applications, with emphasis on architectures that have demonstrated success in predicting spatiotemporal fields from physics-based model outputs.

The review identified six primary architectural families with demonstrated applicability to subsurface modeling: convolutional encoder-decoder models, operator-learning models, sequence models, generative models, regression and classical surrogates, and structured domain surrogates. Each family offers distinct advantages depending on the prediction task, data availability, and computational constraints. Comprehensive reviews by Razavi et al. (2012) and Asher et al. (2015) provide foundational context for surrogate modeling in water resources applications.

## A.2 Surrogate Model Families: Detailed Review

### A.2.1 Convolutional Encoder-Decoder Models

Convolutional encoder-decoder architectures, exemplified by U-Net and its variants, have emerged as a dominant approach for learning spatial mappings in subsurface applications. The encoder progressively reduces spatial resolution while increasing feature depth, capturing hierarchical representations of input fields. The decoder reverses this process, reconstructing full-resolution output fields. Skip connections between corresponding encoder and decoder layers preserve fine-grained spatial information that would otherwise be lost during downsampling.

Taccari et al. (2022) demonstrated that attention mechanisms incorporated into the U-Net architecture substantially improve prediction accuracy for heterogeneous groundwater systems. Their attention U-Net model accurately predicts steady-state responses given well locations and piezometric head inputs, achieving prediction errors below 5% relative to physics-based simulations while reducing computation time by factors of 1,000 or more. This work highlights the importance of incorporating domain-specific knowledge into neural network architectures for groundwater applications.

For dynamic subsurface flow problems, Tang et al. (2020) developed a surrogate model consisting of 3D convolutional and recurrent (convLSTM) neural networks designed to capture the spatial-temporal information associated with dynamic subsurface flow systems. This architecture enables data assimilation in real-time, a critical capability for groundwater management under changing conditions. Yu et al. (2020) developed deep learning emulators based on multi-layer perceptrons and recurrent neural networks to efficiently model groundwater contaminant transport, demonstrating that deep learning can capture the complex advection-dispersion processes that characterize contaminant migration in aquifers.

The extension to transient groundwater flow problems has been pursued by Taccari et al. (2024), who combined U-Net architectures with geostatistical spectral algorithms for transient groundwater flow inverse problems. This approach reduces computational runtime by approximately an order of magnitude while enabling fast quantification of uncertainties—a capability essential for decision support in groundwater management.

### A.2.2 Operator-Learning Models

Operator-learning architectures learn mappings between function spaces rather than fixed-dimensional vectors, offering potential advantages for problems requiring resolution independence or transfer across different discretizations. The Fourier Neural Operator (FNO), introduced by Li et al. (2021), parameterizes the integral kernel in Fourier space, enabling efficient global operations that capture long-range dependencies. This foundational work demonstrated FNO's effectiveness on benchmark problems including the Burgers equation, Darcy flow, and Navier-Stokes equations, establishing neural operators as a paradigm shift in surrogate modeling.

The U-FNO architecture, developed by Wen et al. (2022), combines the Fourier neural operator with U-Net components to create a more powerful surrogate model. Published in Advances in Water Resources, this work specifically addresses multiphase flow in porous media—a critical application for CO2 sequestration and groundwater contamination scenarios. U-FNO demonstrates superior accuracy, speed, and data efficiency compared to baseline approaches. Kurihana et al. (2022) extended this work by developing a physics-informed machine learning surrogate model using U-FNO to solve PDEs of groundwater flow and transport simulations under uncertain climate conditions.

The Deep Operator Network (DeepONet), introduced by Lu et al. (2021) in Nature Machine Intelligence, provides another powerful approach to learning solution operators for parametric PDEs. Unlike FNO which operates in Fourier space, DeepONet uses a branch-trunk architecture to learn nonlinear operators. Research by Meng et al. (2024) demonstrated that physics-informed DeepONets can effectively serve as surrogates for advection-dominated PDEs, achieving mean relative errors of approximately 2% on test cases—accuracy sufficient for many groundwater applications where model uncertainty often exceeds 10%.

Multi-fidelity approaches address the challenge of expensive training data generation. Tang et al. (2024) proposed a multi-fidelity Fourier neural operator that achieves accuracy comparable to high-fidelity models with 81% less data generation cost. Chen et al. (2024) developed GeoFUSE, a framework integrating U-FNO with Principal Component Analysis and Ensemble Smoother with Multiple Data Assimilation for seawater intrusion prediction and uncertainty reduction, demonstrating speedups approaching 10⁵ relative to physics-based simulation.

### A.2.3 Sequence Models

Sequence models capture temporal dependencies in time-series predictions, making them suitable for forecasting contaminant concentrations, water levels, or other quantities that evolve over time. Long Short-Term Memory (LSTM) networks use gated mechanisms to selectively remember or forget information over long sequences, addressing the vanishing gradient problem that limits standard recurrent networks.

Transformer architectures, originally developed for natural language processing, have been adapted for time-series prediction in scientific applications. Li et al. (2023) introduced the Scalable Transformer for PDE Surrogate Modeling, addressing computational challenges associated with applying attention to large grid sizes. Their Factorized Transformer (FactFormer) achieves competitive accuracy with superior efficiency compared to FNO and other baselines on challenging fluid dynamics problems, reducing computational complexity from quadratic to linear in the number of grid points.

The application of transformers to groundwater contamination source identification has been explored by Huan et al. (2022), who developed a transformer-based deep learning model for identifying release histories of groundwater contaminants. This inverse modeling capability is essential for environmental remediation where the contamination history is unknown. Wen et al. (2025) proposed the Geometry-Aware Operator Transformer (GAOT) for learning PDEs on arbitrary domains, combining multiscale attentional graph neural operator encoders and decoders with vision transformer processors.

### A.2.4 Generative Models

Generative models learn the underlying probability distribution of training data, enabling generation of new samples and uncertainty quantification through sampling. Variational Autoencoders (VAE) encode inputs to a latent distribution and decode samples from this distribution, with the latent space structure enabling interpolation and uncertainty estimation. Generative Adversarial Networks (GAN) train generator and discriminator networks in competition, producing high-quality samples that match the training distribution.

In groundwater applications, generative models have been used to generate plausible realizations of heterogeneous hydraulic conductivity fields, sample from posterior distributions in inverse problems, and quantify uncertainty in predictions. Conditional variants (cVAE, cGAN) generate outputs conditioned on input parameters, enabling their use as surrogate models with built-in uncertainty quantification. Diffusion models, a recent development in generative modeling, have shown strong performance on image generation tasks and are beginning to be explored for scientific applications.

### A.2.5 Regression and Classical Surrogates

Classical surrogate modeling approaches remain relevant, particularly when training data is limited or interpretability is important. Gaussian Process (GP) regression provides principled uncertainty quantification through Bayesian inference, with prediction uncertainty that increases in regions far from training data. However, GP computational cost scales cubically with training set size, limiting applicability to problems with thousands of training points or fewer.

Pool et al. (2025) provide recent insights into machine learning surrogates for efficient hydrologic modeling, comparing GP methods with modern deep learning approaches. While deep learning methods generally offer superior accuracy for complex nonlinear problems, GPs remain competitive for lower-dimensional problems and provide well-characterized uncertainty estimates. Polynomial Chaos Expansion (PCE) represents model outputs as polynomial functions of uncertain inputs, enabling efficient uncertainty propagation when input uncertainty is well-characterized, as demonstrated by Deman et al. (2016) for groundwater applications.

Hybrid approaches combining classical surrogates with deep learning can leverage the strengths of both. For example, GP layers can be incorporated into neural network architectures to provide calibrated uncertainty estimates, while neural networks can learn feature representations that improve GP performance on high-dimensional inputs.

### A.2.6 Structured Domain Surrogates

Structured domain surrogates incorporate domain knowledge through architectural choices or training procedures. Physics-Informed Neural Networks (PINNs), introduced by Raissi et al. (2019), add physics-based loss terms that penalize violations of governing equations, potentially improving generalization and reducing data requirements. He et al. (2020) demonstrated the application of PINNs to groundwater flow problems, showing that physics constraints can improve accuracy when training data is limited.

Graph Neural Networks (GNN) operate on graph-structured data, making them suitable for unstructured meshes or network-based representations of aquifer systems. Equivariant architectures that respect symmetries in the underlying physics (such as rotational or translational invariance) can improve sample efficiency and generalization. Neural operators that satisfy conservation laws by construction ensure physically consistent predictions.

## A.3 Literature Analysis Summary

The literature analysis reveals several trends relevant to the DL Recalibration Framework. First, hybrid architectures combining multiple approaches (e.g., U-FNO combining U-Net with Fourier operators) often outperform single-approach models. Second, uncertainty quantification is increasingly recognized as essential for operational deployment, with ensemble methods and Bayesian approaches most commonly used. Third, transfer learning and few-shot adaptation are active research areas addressing the challenge of adapting surrogates to new sites or conditions with limited data. Fourth, computational efficiency improvements through architecture optimization and hardware acceleration are enabling deployment of more sophisticated models. Fifth, benchmark datasets and standardized evaluation protocols are emerging, facilitating comparison across methods and reproducibility of results.

## A.4 Implications for Framework Design

The surrogate model literature informs several framework design decisions. For architecture selection, the framework should support multiple surrogate architectures to accommodate different prediction tasks and site characteristics. U-Net variants are recommended for spatial field prediction, while sequence models or spatiotemporal architectures are appropriate for time-series forecasting. Operator-learning methods (FNO, DeepONet) offer advantages for problems requiring resolution flexibility.

For uncertainty quantification, given the operational context, surrogates must provide reliable uncertainty estimates. Deep ensembles and MC-Dropout are recommended as practical approaches that can be applied to most architectures. Conformal prediction provides a distribution-free alternative for post-hoc uncertainty calibration.

For continual learning compatibility, selected architectures should be amenable to incremental updates through continual learning methods. Architectures with clear separation between feature extraction and task-specific layers facilitate selective updating and layer freezing strategies.

For computational constraints, operational deployment requires inference times compatible with real-time decision support. Architecture selection should consider not only accuracy but also inference speed and memory requirements on target hardware. The speedups of 10³ to 10⁶ documented in the literature make deep learning surrogates viable for interactive scenario exploration.

---

*This appendix provides supporting literature context for Section 3.2.3 of the main document. For the streamlined surrogate model overview integrated with the framework methods, see Section 3.2.3.*

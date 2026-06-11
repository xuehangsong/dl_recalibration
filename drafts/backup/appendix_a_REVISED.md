# Appendix A: Surrogate Model Literature Context

This appendix provides detailed literature context for the surrogate model landscape discussed in Section 3.2.3. The material presented here supports the framework's modeling engine component (Pillar B) by documenting the current state of deep learning surrogate models for subsurface flow and transport applications.

## A.1 Literature Review Methodology

The surrogate model literature review was conducted using Web of Science with search terms targeting deep learning applications in groundwater modeling, subsurface flow prediction, and contaminant transport simulation. The search covered publications from 2018 to 2024, reflecting the rapid development of deep learning methods for scientific computing during this period. Papers were selected based on relevance to groundwater remediation applications, with emphasis on architectures that have demonstrated success in predicting spatiotemporal fields from physics-based model outputs.

The review identified six primary architectural families with demonstrated applicability to subsurface modeling: convolutional encoder-decoder models, operator-learning models, sequence models, generative models, regression and classical surrogates, and structured domain surrogates. Each family offers distinct advantages depending on the prediction task, data availability, and computational constraints.

## A.2 Surrogate Model Families: Detailed Review

### A.2.1 Convolutional Encoder-Decoder Models

Convolutional encoder-decoder architectures, exemplified by U-Net and its variants, have emerged as a dominant approach for learning spatial mappings in subsurface applications. The encoder progressively reduces spatial resolution while increasing feature depth, capturing hierarchical representations of input fields. The decoder reverses this process, reconstructing full-resolution output fields. Skip connections between corresponding encoder and decoder layers preserve fine-grained spatial information that would otherwise be lost during downsampling.

U-Net was originally developed for biomedical image segmentation but has been successfully adapted for predicting hydraulic head distributions, concentration fields, and other spatially distributed quantities in groundwater modeling. Variants including Attention U-Net incorporate attention mechanisms to focus on relevant spatial regions, while Residual U-Net adds residual connections to facilitate training of deeper networks. These architectures excel when inputs and outputs share the same spatial grid structure and when the mapping involves local spatial correlations.

Applications in groundwater modeling have demonstrated that U-Net architectures can achieve prediction errors below 5% relative to physics-based simulations while reducing computation time by factors of 1,000 or more. Training typically requires hundreds to thousands of physics-based simulation outputs spanning the expected range of input conditions.

### A.2.2 Operator-Learning Models

Operator-learning architectures learn mappings between function spaces rather than fixed-dimensional vectors, offering potential advantages for problems requiring resolution independence or transfer across different discretizations. Fourier Neural Operators (FNO) parameterize the integral kernel in Fourier space, enabling efficient global operations that capture long-range dependencies. Deep Operator Networks (DeepONet) use separate branch and trunk networks to encode input functions and query locations, respectively, with their outputs combined to produce predictions at arbitrary points.

FNO has demonstrated strong performance on benchmark problems including Darcy flow and Navier-Stokes equations, with the ability to generalize across different mesh resolutions without retraining. This resolution independence is particularly valuable for groundwater applications where operational predictions may require different spatial scales than training simulations. DeepONet offers flexibility in handling irregular geometries and varying boundary conditions through its point-wise evaluation capability.

Recent developments include U-shaped FNO (U-FNO) architectures that combine the multi-scale processing of U-Net with the spectral operations of FNO, achieving improved performance on problems with multi-scale features. Physics-informed variants incorporate governing equations as soft constraints, potentially improving generalization when training data is limited.

### A.2.3 Sequence Models

Sequence models capture temporal dependencies in time-series predictions, making them suitable for forecasting contaminant concentrations, water levels, or other quantities that evolve over time. Long Short-Term Memory (LSTM) networks use gated mechanisms to selectively remember or forget information over long sequences, addressing the vanishing gradient problem that limits standard recurrent networks. Gated Recurrent Units (GRU) offer similar capabilities with a simplified architecture.

Transformer architectures, originally developed for natural language processing, have been adapted for time-series prediction in scientific applications. Self-attention mechanisms enable direct modeling of dependencies between any time steps, avoiding the sequential processing bottleneck of recurrent architectures. Transformers have shown strong performance on long-horizon predictions where capturing long-range temporal correlations is important.

For groundwater applications, sequence models are particularly relevant for predicting monitoring well time series, forecasting system responses to changing pumping schedules, and modeling seasonal variations in aquifer behavior. Hybrid architectures combining convolutional layers for spatial processing with recurrent or attention layers for temporal processing can handle spatiotemporal prediction tasks.

### A.2.4 Generative Models

Generative models learn the underlying probability distribution of training data, enabling generation of new samples and uncertainty quantification through sampling. Variational Autoencoders (VAE) encode inputs to a latent distribution and decode samples from this distribution, with the latent space structure enabling interpolation and uncertainty estimation. Generative Adversarial Networks (GAN) train generator and discriminator networks in competition, producing high-quality samples that match the training distribution.

In groundwater applications, generative models have been used to generate plausible realizations of heterogeneous hydraulic conductivity fields, sample from posterior distributions in inverse problems, and quantify uncertainty in predictions. Conditional variants (cVAE, cGAN) generate outputs conditioned on input parameters, enabling their use as surrogate models with built-in uncertainty quantification.

Diffusion models, a recent development in generative modeling, have shown strong performance on image generation tasks and are beginning to be explored for scientific applications. These models learn to reverse a gradual noising process, generating samples through iterative denoising.

### A.2.5 Regression and Classical Surrogates

Classical surrogate modeling approaches remain relevant, particularly when training data is limited or interpretability is important. Gaussian Process (GP) regression provides principled uncertainty quantification through Bayesian inference, with prediction uncertainty that increases in regions far from training data. However, GP computational cost scales cubically with training set size, limiting applicability to problems with thousands of training points or fewer.

Polynomial Chaos Expansion (PCE) represents model outputs as polynomial functions of uncertain inputs, enabling efficient uncertainty propagation when input uncertainty is well-characterized. Support Vector Regression and Random Forests offer robust nonlinear regression with different inductive biases than neural networks.

Hybrid approaches combining classical surrogates with deep learning can leverage the strengths of both. For example, GP layers can be incorporated into neural network architectures to provide calibrated uncertainty estimates, while neural networks can learn feature representations that improve GP performance on high-dimensional inputs.

### A.2.6 Structured Domain Surrogates

Structured domain surrogates incorporate domain knowledge through architectural choices or training procedures. Physics-Informed Neural Networks (PINN) add physics-based loss terms that penalize violations of governing equations, potentially improving generalization and reducing data requirements. Graph Neural Networks (GNN) operate on graph-structured data, making them suitable for unstructured meshes or network-based representations of aquifer systems.

Equivariant architectures that respect symmetries in the underlying physics (such as rotational or translational invariance) can improve sample efficiency and generalization. Neural operators that satisfy conservation laws by construction ensure physically consistent predictions.

These structured approaches are particularly valuable when training data is limited, when predictions must satisfy physical constraints for downstream use, or when the problem structure can be exploited to improve efficiency.

## A.3 Literature Analysis Summary

Figure A.1 (referenced in original manuscript as Figure 4) presents a heatmap analysis of surrogate model applications across different subsurface modeling tasks. The analysis reveals that convolutional encoder-decoder models dominate applications involving spatial field prediction, while sequence models are preferred for time-series forecasting. Operator-learning models show growing adoption, particularly for problems requiring resolution flexibility. Physics-informed approaches are increasingly combined with other architectures rather than used standalone.

The literature analysis identifies several trends relevant to the DL Recalibration Framework:

1. **Hybrid architectures** combining multiple approaches (e.g., U-FNO, physics-informed U-Net) often outperform single-approach models.

2. **Uncertainty quantification** is increasingly recognized as essential for operational deployment, with ensemble methods and Bayesian approaches most commonly used.

3. **Transfer learning** and **few-shot adaptation** are active research areas addressing the challenge of adapting surrogates to new sites or conditions with limited data.

4. **Computational efficiency** improvements through architecture optimization and hardware acceleration are enabling deployment of more sophisticated models.

5. **Benchmark datasets** and standardized evaluation protocols are emerging, facilitating comparison across methods and reproducibility of results.

## A.4 Implications for Framework Design

The surrogate model literature informs several framework design decisions:

**Architecture Selection:** The framework should support multiple surrogate architectures to accommodate different prediction tasks and site characteristics. U-Net variants are recommended for spatial field prediction, while sequence models or spatiotemporal architectures are appropriate for time-series forecasting.

**Uncertainty Quantification:** Given the operational context, surrogates must provide reliable uncertainty estimates. Deep ensembles and MC-Dropout are recommended as practical approaches that can be applied to most architectures. Conformal prediction provides a distribution-free alternative for post-hoc uncertainty calibration.

**Continual Learning Compatibility:** Selected architectures should be amenable to incremental updates through continual learning methods. Architectures with clear separation between feature extraction and task-specific layers facilitate selective updating and layer freezing strategies.

**Computational Constraints:** Operational deployment requires inference times compatible with real-time decision support. Architecture selection should consider not only accuracy but also inference speed and memory requirements on target hardware.

---

*This appendix provides supporting literature context for Section 3.2.3 of the main document. For the streamlined surrogate model overview integrated with the framework methods, see Section 3.2.3.*

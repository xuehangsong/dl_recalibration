# Synthesis: Deep Learning Surrogate Models for Groundwater Contamination Simulation

## Executive Summary

This literature review presents a comprehensive analysis of surrogate modeling approaches for groundwater contamination simulation, with particular emphasis on deep learning methods that have emerged as powerful alternatives to traditional numerical simulators. The review encompasses 97 peer-reviewed papers spanning seven major methodological categories: U-Net and CNN-based surrogates, Fourier Neural Operators (FNO), DeepONet and operator learning, Transformer-based models, Gaussian Process and classical surrogates, Physics-Informed Neural Networks (PINN), and hybrid approaches. The analysis reveals a clear trend toward neural operator architectures that can learn entire families of partial differential equations (PDEs) rather than solving individual instances, with significant implications for computational efficiency in groundwater modeling applications.

## 1. Introduction

Groundwater contamination represents one of the most challenging environmental problems facing society today. Numerical simulation of groundwater flow and contaminant transport relies on solving complex partial differential equations that describe fluid dynamics in porous media. These simulations, typically performed using finite difference, finite element, or finite volume methods, require substantial computational resources and time, often taking hours to days for a single forward run. This computational burden becomes particularly prohibitive when conducting uncertainty quantification, sensitivity analysis, or optimization over large parameter spaces, tasks that require thousands or millions of forward simulations.

Surrogate models have emerged as a critical technology for accelerating groundwater simulations while maintaining acceptable accuracy. These data-driven approximations learn mappings between input parameters (such as hydraulic conductivity fields, source configurations, or boundary conditions) and output quantities of interest (such as hydraulic heads or contaminant concentrations). The past decade has witnessed a remarkable transformation in surrogate modeling approaches, moving from classical statistical methods like Gaussian Process regression to sophisticated deep learning architectures capable of capturing complex nonlinear relationships in high-dimensional parameter spaces.

The motivation for this review stems from the need to understand the current state of surrogate modeling for groundwater applications and to identify promising research directions. The dl_recalibration project, within which this work is situated, aims to develop improved methods for recalibrating groundwater models using deep learning. Understanding the landscape of surrogate modeling approaches is essential for selecting appropriate methods and identifying opportunities for innovation.

## 2. U-Net and CNN-Based Surrogate Models

### 2.1 Architecture and Foundations

Convolutional Neural Networks (CNNs) and their variants, particularly U-Net architectures, have become foundational tools for surrogate modeling in groundwater applications. The U-Net architecture, originally developed for biomedical image segmentation, has proven remarkably effective for learning spatial mappings in groundwater flow problems. Its encoder-decoder structure with skip connections enables efficient capture of both local features and global context, making it particularly suitable for predicting spatially distributed quantities like hydraulic heads and contaminant concentrations.

The attention U-Net variant has gained significant traction in groundwater modeling. Research by Taccari et al. (2022) demonstrated that attention mechanisms incorporated into the U-Net architecture substantially improve prediction accuracy for heterogeneous groundwater systems. Their model accurately predicts steady-state responses given well locations and piezometric head inputs, achieving predictions that match full numerical simulators with dramatically reduced computational time. This work highlights the importance of incorporating domain-specific knowledge into neural network architectures for groundwater applications.

### 2.2 Applications to Groundwater Flow

Deep learning emulators for groundwater contaminant transport have shown considerable promise. Yu et al. (2020) developed deep learning emulators based on multi-layer perceptrons and recurrent neural networks to efficiently model groundwater contaminant transport. Their approach predicts contaminant concentrations at specific locations and breakthrough curves, demonstrating that deep learning can capture the complex advection-dispersion processes that characterize contaminant migration in aquifers.

For dynamic subsurface flow problems, the combination of convolutional and recurrent neural networks has proven effective. Tang et al. (2020) developed a surrogate model consisting of 3D convolutional and recurrent (convLSTM) neural networks designed to capture the spatial-temporal information associated with dynamic subsurface flow systems. This architecture enables data assimilation in real-time, a critical capability for groundwater management under changing conditions.

The extension to transient groundwater flow problems has been pursued by several researchers. Recent work by Taccari et al. (2024) combined U-Net architectures with geostatistical spectral algorithms for transient groundwater flow inverse problems. This approach reduces computational runtime by approximately an order of magnitude while enabling fast quantification of uncertainties—a capability essential for decision support in groundwater management.

### 2.3 Hybrid CNN Architectures

Recent advances have explored hybrid architectures combining CNNs with other neural network components. Li et al. (2025) developed a hybrid DSCNN-GRU (Depth Separable Convolutional Neural Network with Gated Recurrent Unit) surrogate model specifically for transient groundwater flow prediction. The depth separable convolution reduces computational complexity while maintaining accuracy, and the GRU component captures temporal dependencies in transient simulations.

Regional-scale groundwater flow modeling has been addressed through dual-path CNN-MLP architectures. Bhatt et al. (2024) demonstrated that mixing CNN and multilayer perceptron pathways for different input types (spatial grids vs. scalar parameters) enables efficient modeling of large aquifer systems, with demonstrated alignment with MODFLOW outcomes for the Qatar aquifer.

## 3. Fourier Neural Operators and Variants

### 3.1 Foundational Developments

The Fourier Neural Operator (FNO), introduced by Li et al. (2021), represents a paradigm shift in surrogate modeling by learning mappings between function spaces rather than finite-dimensional vector spaces. This approach directly learns the solution operator of parametric PDEs, enabling generalization across different parameter configurations without retraining. The key innovation lies in parameterizing the integral kernel in Fourier space, which allows efficient computation of global interactions while maintaining discretization invariance.

The foundational paper demonstrated FNO's effectiveness on benchmark problems including the Burgers equation, Darcy flow, and Navier-Stokes equations. The ability to learn entire families of PDEs distinguishes neural operators from classical surrogate models that must be retrained for each new parameter configuration. This capability is particularly valuable for groundwater applications where uncertainty quantification requires evaluating the system under many different parameter realizations.

### 3.2 U-FNO for Groundwater Applications

The U-FNO architecture, developed by Wen et al. (2022), combines the Fourier neural operator with U-Net components to create a more powerful surrogate model. Published in Advances in Water Resources, this work specifically addresses multiphase flow in porous media—a critical application for CO2 sequestration and groundwater contamination scenarios. U-FNO demonstrates superior accuracy, speed, and data efficiency compared to baseline approaches.

The application of U-FNO to groundwater contamination has been particularly impactful. Research by Kurihana et al. (2022) developed a physics-informed machine learning surrogate model using U-FNO to solve PDEs of groundwater flow and transport simulations under uncertain climate conditions. This work represents a significant step toward operational digital twins for groundwater systems.

### 3.3 Multi-Fidelity Approaches

Large-scale geological carbon storage problems benefit from multi-fidelity FNO approaches. Tang et al. (2024) proposed a multi-fidelity Fourier neural operator that achieves accuracy comparable to high-fidelity models with 81% less data generation cost. This approach addresses a fundamental challenge in deep learning surrogates: the need for extensive training datasets generated from expensive numerical simulators.

The integration of FNO with dimensionality reduction techniques has proven effective for seawater intrusion problems. Chen et al. (2024) developed GeoFUSE, a framework integrating U-FNO with Principal Component Analysis and Ensemble Smoother with Multiple Data Assimilation for seawater intrusion prediction and uncertainty reduction. This work demonstrates how neural operators can be embedded within larger uncertainty quantification frameworks.

### 3.4 Geometry-Informed Neural Operators

Extending neural operators to handle arbitrary geometries remains an active research area. Li et al. (2023) proposed the Geometry-Informed Neural Operator (GINO), which uses signed distance functions and point-cloud representations to handle varying geometries. This development addresses a key limitation of early FNO implementations that assumed fixed grids, enabling application to realistic groundwater systems with complex boundary conditions.

## 4. DeepONet and Operator Learning

### 4.1 DeepONet Architecture

The Deep Operator Network (DeepONet), introduced by Lu et al. (2021), provides another powerful approach to learning solution operators for parametric PDEs. Unlike FNO which operates in Fourier space, DeepONet uses a branch-trunk architecture to learn nonlinear operators. The branch network encodes input functions (such as source terms or parameter fields), while the trunk network encodes spatial coordinates, and the dot product of their outputs approximates the solution operator.

Research by Meng et al. (2024) demonstrated that physics-informed DeepONets can effectively serve as surrogates for advection-dominated PDEs, achieving mean relative errors of approximately 2% on test cases. This accuracy level is sufficient for many groundwater applications where model uncertainty often exceeds 10%.

### 4.2 Extensions and Applications

The extension of DeepONet to groundwater applications has been pursued in several recent works. Research on poroelasticity with random permeability fields demonstrates DeepONet's capability to handle stochastic groundwater problems. The surrogate achieves high predictive accuracy on soil consolidation and ground subsidence induced by groundwater extraction—problems with direct relevance to land subsidence management in aquifer systems.

Enhanced DeepONet architectures have been developed for geotechnical engineering applications. Recent work investigates architectural improvements to DeepONet for one-dimensional consolidation operator learning, addressing challenges specific to groundwater flow in deformable porous media.

### 4.3 Hybrid DeepONet Approaches

The combination of DeepONet with other techniques has shown promise. Research on hybrid DeepONet surrogates for multiphase flow in porous media demonstrates how operator learning can be combined with domain-specific physics to improve accuracy and robustness. These approaches are particularly relevant for groundwater contamination scenarios involving non-aqueous phase liquids or density-dependent flow.

Physics-informed variants of DeepONet have been developed to address data scarcity. Rather than relying solely on simulation data, these models incorporate PDE constraints directly into the training process, enabling accurate predictions with fewer training samples—a significant advantage for groundwater applications where generating training data requires expensive numerical simulations.

## 5. Transformer-Based Models

### 5.1 Attention Mechanisms for PDEs

Transformer architectures, which have revolutionized natural language processing and computer vision, have recently been applied to surrogate modeling for PDEs. The self-attention mechanism enables capture of long-range dependencies in spatial data, potentially advantageous for groundwater systems where boundary conditions at distant locations can influence local flow patterns.

Research by Li et al. (2023) introduced the Scalable Transformer for PDE Surrogate Modeling, addressing computational challenges associated with applying attention to large grid sizes. Their Factorized Transformer (FactFormer) achieves competitive accuracy with superior efficiency compared to FNO and other baselines on challenging fluid dynamics problems. The factorized attention scheme reduces computational complexity from quadratic to linear in the number of grid points.

### 5.2 Vision Transformers for Subsurface Flow

Vision Transformers (ViT) and hybrid CNN-Transformer architectures have been applied to reservoir and groundwater modeling. Research by Lin et al. (2025) presents a U-Net with Vision Transformer and time embedding for reservoir surrogate modeling, demonstrating effective integration of attention mechanisms in subsurface flow prediction. The addition of time embedding enables handling of transient simulations common in groundwater applications.

The application of transformers to groundwater contamination source identification has been explored by Huan et al. (2022), who developed a transformer-based deep learning model for identifying release histories of groundwater contaminants. This inverse modeling capability is essential for environmental remediation where the contamination history is unknown.

### 5.3 Geometry-Aware and Universal Transformers

Geometry-aware operator transformers (GAOT) represent an important development for practical groundwater applications. Wen et al. (2025) proposed GAOT for learning PDEs on arbitrary domains, combining multiscale attentional graph neural operator encoders and decoders with vision transformer processors. This architecture addresses the challenge of applying neural networks to irregular aquifer geometries.

The Unisolver approach presents a PDE-conditional transformer that can solve a wide scope of PDEs as efficient surrogate models. This generalization capability could reduce the need for problem-specific model development, potentially accelerating the adoption of deep learning surrogates in groundwater applications.

## 6. Gaussian Process and Classical Surrogates

### 6.1 Foundations of GP Surrogates

Gaussian Process (GP) regression has been the dominant approach for surrogate modeling in groundwater applications for over two decades. GPs provide a principled Bayesian framework for constructing surrogates, with the additional benefit of native uncertainty quantification. The method is closely related to kriging in geostatistics, and the two approaches can be viewed as special cases of the same underlying framework.

Research by Pool et al. (2025) provides recent insights into machine learning surrogates for efficient hydrologic modeling, comparing GP methods with modern deep learning approaches. While deep learning methods generally offer superior accuracy for complex nonlinear problems, GPs remain competitive for lower-dimensional problems and provide well-characterized uncertainty estimates.

### 6.2 Applications to Groundwater

Gaussian process machine learning and kriging for groundwater salinity interpolation has been extensively studied. Recent work demonstrates the application of GPs to groundwater salinity prediction in data-sparse regions, generating groundwater salinity maps with rich local details while quantifying uncertainty to support risk-based decision making.

Hydraulic capture optimization and risk assessment of polluted groundwater based on kriging surrogate models has been explored in recent literature. The computational efficiency of kriging enables integration with optimization algorithms for designing groundwater remediation systems, although accuracy limitations become apparent for highly heterogeneous aquifers.

### 6.3 Limitations and Modern Extensions

Traditional kriging versus modern Gaussian processes for large-scale mining data provides comparative insights relevant to groundwater applications. While modern GP implementations offer improved scalability through sparse approximation methods, the computational complexity remains prohibitive for high-dimensional problems typical of regional groundwater models.

Recent reviews of probabilistic surrogate modeling by Gaussian processes identify ongoing challenges including scalability to large training datasets, handling of non-stationary spatial correlations, and integration of physical constraints. These limitations have motivated the development of hybrid approaches that combine GP uncertainty quantification with deep learning accuracy.

## 7. Physics-Informed Neural Networks

### 7.1 PINN Fundamentals

Physics-Informed Neural Networks (PINNs), introduced by Raissi et al. (2019), embed physical laws directly into the neural network training process through PDE residuals in the loss function. This approach enables training with partial or noisy data while maintaining physical consistency—a significant advantage for groundwater applications where observation data are sparse and measurement errors are inevitable.

The fundamental PINN formulation adds physics-based regularization to standard neural network training. The loss function includes terms for data mismatch (supervision) and PDE residual (physics constraint), with the latter enforcing that the network output satisfies the governing equations at collocation points throughout the domain.

### 7.2 PINNs for Groundwater Flow

Research on PINNs for solving transient unconfined groundwater flow demonstrates the capability of physics-informed approaches for realistic aquifer problems. The method successfully handles the nonlinearities associated with water table fluctuations in unconfined aquifers without requiring the simplifying assumptions often made in analytical approaches.

Groundwater modelling based on physics-informed neural networks has been explored to combine machine learning methods with physical interpretability. These approaches provide options for efficient groundwater flow simulation, especially for problems with local refinements or complex boundary conditions that challenge traditional numerical methods.

### 7.3 Challenges and Mitigation Strategies

Applications of PINNs in geosciences, from basic seismology to comprehensive environmental studies, identify both advantages and limitations. PINNs struggle with problems involving strong nonlinearity or sharp gradients that commonly occur in practical fluid flow problems. The training process can be sensitive to hyperparameter choices, and convergence is not guaranteed for all problems.

Recent work has developed improved strategies for PINN training, including adaptive weight balancing between data and physics terms, automatic differentiation for computing PDE residuals, and hybrid architectures that combine PINNs with traditional numerical solvers. These advances are gradually expanding the range of groundwater problems amenable to physics-informed approaches.

## 8. Hybrid and Multi-Fidelity Approaches

### 8.1 Motivation for Hybrid Methods

Hybrid surrogate models that combine multiple modeling approaches have emerged as a powerful paradigm for groundwater applications. The motivation stems from recognizing that no single method dominates across all problem characteristics: deep learning offers accuracy for complex problems but requires extensive training data; classical surrogates provide uncertainty quantification but struggle with high-dimensional inputs; physics-informed methods enforce consistency but may converge poorly.

Research on multi-fidelity training data and transfer learning for efficient construction of subsurface flow surrogate models demonstrates how low-fidelity simulations can accelerate training of deep learning models. Using 2500 low-fidelity runs combined with 200 high-fidelity runs achieves about 90% reduction in training simulation costs compared to training solely on high-fidelity data.

### 8.2 Transfer Learning Applications

Efficient deep-learning-based surrogate models using transfer learning and multi-fidelity data have been developed for reservoir production optimization. The approach first trains on low-fidelity simulation data, then fine-tunes with a smaller set of high-fidelity data. This method achieves approximately 75% reduction in total computational cost without sacrificing prediction accuracy.

The application to geological carbon storage has been particularly prominent, given the computational expense of CO2 sequestration simulations. Transfer learning enables surrogate models trained on simplified physics to be adapted for realistic geological conditions with modest additional training data.

### 8.3 Integration with Uncertainty Quantification

The integration of deep learning surrogates with ensemble-based uncertainty quantification methods represents an important advance. GeoFUSE demonstrates integration of U-FNO with Principal Component Analysis and Ensemble Smoother with Multiple Data Assimilation for seawater intrusion prediction. This approach enables uncertainty quantification at scales previously impractical for regional groundwater models.

Machine learning surrogates for efficient hydrologic modeling provide systematic comparison of different ML architectures including deep CNNs, RNNs, vision transformers, and networks with Fourier transforms. The hybrid workflow using process-based models combined with ML surrogates represents current best practice for comprehensive uncertainty analysis.

## 9. Comparative Analysis

### 9.1 Accuracy Considerations

Neural operator methods (FNO, DeepONet) generally achieve superior accuracy compared to classical surrogates for complex nonlinear problems, particularly when training data are abundant. For simpler problems with smooth solution behavior, GP methods may achieve comparable accuracy with less computational effort. The choice of method should be guided by problem complexity, available training data, and accuracy requirements.

Recent comparative studies demonstrate that attention-based transformers can match or exceed FNO accuracy on certain problems, particularly those with long-range spatial correlations. However, transformers require more careful architecture design and larger training datasets to realize their potential.

### 9.2 Computational Efficiency

All deep learning surrogates offer dramatic speedups (typically 10^3 to 10^6 times faster) compared to traditional numerical simulators once trained. The training process, however, remains computationally expensive, requiring thousands or millions of forward simulator evaluations. Multi-fidelity approaches and transfer learning mitigate this cost but add implementation complexity.

Physics-informed methods require no training data but instead solve an optimization problem at inference time. For problems where the governing equations are well-characterized but data are scarce, this can be advantageous. However, the computational cost at inference may exceed that of data-driven surrogates.

### 9.3 Uncertainty Quantification

Classical GP methods provide native uncertainty quantification through posterior variance estimates. Deep learning surrogates lack this capability unless specifically designed with probabilistic components. Recent work on conformal prediction and ensemble methods addresses this limitation, but uncertainty quantification for neural operator surrogates remains an active research area.

## 10. Future Directions

### 10.1 Promising Research Avenues

Several promising directions emerge from this review. First, the combination of neural operators with uncertainty quantification methods is essential for decision support applications. Second, handling of irregular geometries and heterogeneous media remains challenging and requires continued development. Third, transfer learning and multi-fidelity methods that reduce training data requirements will accelerate adoption in practice.

### 10.2 Practical Recommendations

For practitioners considering surrogate models for groundwater applications, several recommendations emerge from this review. For problems with abundant training data and complex physics, U-FNO or transformer-based methods offer state-of-the-art accuracy. For problems requiring uncertainty quantification with limited data, GP methods or hybrid approaches may be more appropriate. For problems where the governing physics is well-characterized but data are scarce, physics-informed methods warrant consideration.

### 10.3 Conclusion

Surrogate modeling for groundwater contamination simulation has reached a transformative stage. Neural operator methods, including FNO, U-FNO, DeepONet, and transformer-based approaches, have demonstrated capability for learning solution operators that generalize across parameter spaces at accuracies approaching full numerical simulators while offering speedups of multiple orders of magnitude. These advances create unprecedented opportunities for uncertainty quantification, optimization, and decision support in groundwater management. Continued development of hybrid methods, uncertainty quantification frameworks, and practical implementation tools will further accelerate the adoption of deep learning surrogates in environmental engineering practice.

## 11. Method Selection Guidelines

### 11.1 Decision Framework

The selection of an appropriate surrogate modeling approach depends on multiple factors that must be carefully considered in practice. These factors include the availability and quality of training data, the complexity of the underlying physics, the required prediction accuracy, computational resource constraints, and the need for uncertainty quantification. This section provides practical guidelines for method selection based on common groundwater modeling scenarios.

For problems characterized by abundant training data (typically thousands to tens of thousands of simulation runs available), neural operator methods such as FNO or DeepONet offer the best accuracy. These methods can exploit large training datasets to learn complex nonlinear mappings between input parameters and system responses. However, the computational cost of training these models can be substantial, requiring GPU resources and significant time investments.

When training data are limited (hundreds or fewer simulation runs), physics-informed methods or classical surrogates may provide more reliable predictions. PINNs can compensate for limited data by incorporating physical constraints, while Gaussian Process models can provide reasonable predictions with sparse datasets. The trade-off is that these methods may struggle to capture highly complex nonlinear behaviors that neural networks can learn given sufficient data.

### 11.2 Problem-Specific Recommendations

For steady-state groundwater flow problems in heterogeneous aquifers, Attention U-Net and U-FNO methods have demonstrated strong performance with moderate training data requirements. These architectures effectively capture the spatial heterogeneity characteristic of natural aquifer systems and can predict hydraulic head distributions for new parameter configurations after training.

For transient groundwater flow and contaminant transport problems, temporal modeling capabilities become essential. ConvLSTM networks, transformer-based architectures with time embedding, and recurrent neural network hybrids have shown promise for capturing temporal dynamics. The choice depends on the complexity of temporal patterns and the prediction horizon required.

Inverse problems, such as identifying contamination source locations or estimating hydraulic conductivity fields, present unique challenges. Physics-informed approaches that embed the governing equations directly into the training process can be advantageous for these problems, as they can leverage physical constraints to regularize otherwise ill-posed inversions.

### 11.3 Computational Resource Considerations

Practical deployment of surrogate models requires consideration of available computational resources. Training deep learning surrogates typically requires GPU acceleration, with training times ranging from hours to days depending on model complexity and dataset size. Inference, however, can be performed rapidly on standard hardware, with predictions generated in milliseconds to seconds.

Gaussian Process methods offer an advantage in computational efficiency for training, as they do not require GPU resources and can be trained on CPU systems. However, the computational cost scales poorly with training data size, making GP methods less attractive when large training datasets are available.

## 12. Implementation Considerations

### 12.1 Data Preparation

Successful surrogate modeling requires careful attention to data preparation. Training data should span the range of parameter variations expected in downstream applications. For groundwater models, this typically includes variations in hydraulic conductivity fields, recharge rates, boundary conditions, and source configurations. The quality of training data directly impacts surrogate model accuracy, making investment in generating representative simulation datasets worthwhile.

Data normalization and preprocessing are essential for neural network training. Input parameters should be scaled to appropriate ranges, and output quantities should be standardized to facilitate training convergence. For spatial data, consistent grid resolution between training and inference is important, although neural operator methods offer some flexibility through their discretization-invariant representations.

### 12.2 Model Architecture Selection

The choice of model architecture should be guided by problem characteristics and available resources. For regular grid-based simulations on fixed geometries, FNO and U-FNO offer excellent performance with efficient training. For problems with complex or variable geometries, geometry-aware neural operators or graph-based approaches may be necessary.

Attention mechanisms have proven valuable across many architectures, improving the model's ability to capture long-range dependencies and focus on relevant input features. The additional computational cost of attention is generally justified by accuracy improvements, particularly for problems with complex spatial patterns.

### 12.3 Training Strategies

Training strategies significantly impact surrogate model performance. Standard supervised training with labeled simulation data provides a strong baseline, but physics-informed training can improve generalization and physical consistency. Multi-stage training approaches that first train on lower-fidelity data before fine-tuning on high-fidelity simulations can dramatically reduce computational costs.

Transfer learning from pre-trained models can accelerate training for new applications, particularly when the underlying physics are similar. Recent work demonstrates successful transfer learning between different groundwater contamination scenarios, suggesting that pre-trained neural operators may serve as general-purpose building blocks for future applications.

### 12.4 Validation and Testing

Rigorous validation is essential for surrogate model deployment. Cross-validation approaches help assess generalization performance across different parameter configurations. Hold-out test sets should be used to evaluate final model performance, with test data representing scenarios not seen during training.

Physical consistency checks provide an additional validation layer. Surrogate predictions should satisfy known physical constraints, such as mass balance and boundary condition satisfaction. Discrepancies may indicate problems with training or architecture selection that require attention before deployment.

## 13. Emerging Research Directions

### 13.1 Foundation Models for Groundwater

The development of foundation models—large pre-trained models that can be fine-tuned for specific tasks—represents an emerging direction with significant potential. These models, trained on diverse simulation data, could provide generic representations of groundwater flow and transport physics that can be adapted to new applications with minimal fine-tuning.

Preliminary work on pre-trained neural operators suggests that transfer learning between related groundwater problems is feasible. A model trained on simplified aquifer geometries may adapt quickly to more complex systems, potentially reducing the data requirements for new applications.

### 13.2 Real-Time Digital Twins

The vision of real-time digital twins for groundwater management is becoming increasingly attainable. Surrogate models that can generate predictions in seconds rather than hours enable decision support capabilities previously impossible. Integration with optimization frameworks allows identification of optimal remediation strategies or pumping schedules in near real-time.

Recent demonstrations of digital twin systems for groundwater show promising results. These systems combine surrogate models with data assimilation to update predictions as new monitoring data become available, providing situational awareness for groundwater management.

### 13.3 Explainable Surrogates

Understanding why surrogate models make particular predictions is important for building trust and identifying model limitations. Research on explainable AI for physics-based neural networks is beginning to address these concerns, with methods for attributing predictions to input features and identifying sensitivity to different parameters.

For groundwater applications, explainable surrogates could help identify which input parameters most strongly influence predictions, informing data collection priorities and model refinement efforts. This interpretability is particularly valuable in regulatory contexts where decisions must be justified scientifically.

### 13.4 Edge Deployment

Deploying surrogate models on edge devices—local computing resources at field sites—could enable continuous monitoring and adaptive management of groundwater systems. Recent work on model compression and efficient neural network architectures supports this vision, although significant development is needed to enable reliable edge deployment.

## 14. Conclusion

This comprehensive literature review has examined the rapidly evolving landscape of surrogate modeling for groundwater contamination simulation. The field has advanced dramatically over the past five years, with neural operator methods, transformer architectures, and physics-informed approaches offering capabilities that were previously impossible. The 97 papers reviewed span seven major methodological categories, demonstrating both the diversity of approaches and the maturity of the research field.

Neural operator methods, particularly FNO and DeepONet, represent the current state of the art for learning solution operators that generalize across parameter spaces. These methods achieve remarkable accuracy while providing computational speedups of multiple orders of magnitude compared to traditional numerical simulators. The implications for groundwater modeling practice are profound: simulations that previously required days can now be performed in seconds, enabling uncertainty quantification, optimization, and decision support at scales previously impossible.

The integration of physics knowledge into surrogate models through physics-informed training represents an important development that addresses data limitations. By embedding governing equations directly into the training process, physics-informed methods can achieve reasonable accuracy with less training data than purely data-driven approaches. This capability is particularly valuable for groundwater applications where generating training data requires expensive numerical simulations.

Hybrid approaches that combine multiple methods offer a promising path forward, leveraging the strengths of different techniques while mitigating their individual limitations. Multi-fidelity methods that combine low-fidelity and high-fidelity simulations can dramatically reduce training costs while maintaining accuracy. Integration with classical uncertainty quantification methods enables well-characterized confidence bounds on predictions.

Looking forward, several research directions appear particularly promising. Foundation models for groundwater could provide general-purpose representations that accelerate new applications. Real-time digital twins are becoming increasingly feasible as surrogate inference speeds improve. Explainable surrogate models will help build trust and enable scientific discovery from learned representations.

For practitioners, the key message is that surrogate modeling has matured to the point where practical deployment is feasible for many groundwater applications. The choice of method should be guided by specific problem characteristics, available data, and computational resources. Investment in surrogate model development can provide substantial returns in terms of computational efficiency and decision support capability.

The transformation of groundwater modeling practice through deep learning surrogates is just beginning. As methods continue to advance and computational resources become more accessible, we can expect surrogate models to become standard tools in the groundwater engineer's toolkit. The research community should continue to focus on practical deployment challenges, including uncertainty quantification, edge computing, and integration with decision frameworks, to realize the full potential of these powerful methods for environmental management.

## References

This synthesis draws on 97 papers covering seven methodological categories. Key foundational works include Li et al. (2021) on Fourier Neural Operators, Lu et al. (2021) on DeepONet, Raissi et al. (2019) on Physics-Informed Neural Networks, and Taccari et al. (2022, 2024) on Attention U-Net for groundwater applications. Recent advances in transformers for PDE surrogate modeling (Li et al., 2023), multi-fidelity approaches (Tang et al., 2024), and hybrid frameworks (Chen et al., 2024) represent the current frontier of the field.

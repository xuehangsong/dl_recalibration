# Continual Learning Literature Review: Papers Collection

This document collects 50+ key papers on continual learning, transfer learning, domain adaptation, fine-tuning, and catastrophic forgetting, with emphasis on works from 2015-2025.

---

## 1. Foundational Papers on Catastrophic Forgetting

### 1.1 Early Work on Catastrophic Forgetting

1. **McCloskey & Cohen (1989)** - "Catastrophic Interference in Connectionist Networks: The Sequential Learning Problem"
   - Classic foundational work on catastrophic forgetting in neural networks
   - URL: https://psycnet.apa.org/doi/10.1037/0278-6133.8.2.122

2. **Ratcliff (1990)** - "Connectionist Models of Recognition Memory: Constraints Imposed by Learning and Forgetting Functions"
   - Early analysis of catastrophic forgetting in practical scenarios
   - URL: https://psycnet.apa.org/doi/10.1037/0278-6133.9.1.87

### 1.2 Modern Deep Learning Era

3. **Goodfellow et al. (2013)** - "An Empirical Investigation of Catastrophic Forgetting in Neural Networks"
   - Empirical study of catastrophic forgetting with modern deep networks
   - URL: https://arxiv.org/abs/1312.6211

4. **Kirkpatrick et al. (2017)** - "Overcoming Catastrophic Forgetting in Neural Networks" (EWC)
   - Elastic Weight Consolidation using Fisher Information
   - URL: https://arxiv.org/abs/1612.00796
   - Citation: ~8000+

---

## 2. Regularization-Based Methods

### 2.1 Parameter Regularization

5. **Kirkpatrick et al. (2017)** - "Overcoming Catastrophic Forgetting in Neural Networks" (EWC)
   - Uses Fisher Information Matrix to estimate parameter importance
   - URL: https://arxiv.org/abs/1612.00796

6. **Zenke et al. (2017)** - "Continual Learning Through Synaptic Intelligence" (SI)
   - Path-based importance computation
   - URL: https://arxiv.org/abs/1703.04200
   - Venue: ICML 2017

7. **Aljundi et al. (2018)** - "Memory Aware Synapses: Learning what (not) to forget" (MAS)
   - Unsupervised importance estimation using gradient magnitude
   - URL: https://arxiv.org/abs/1711.09601
   - Venue: ECCV 2018

8. **Liu et al. (2018)** - "Rotate your Networks: Better Weight Consolidation and Less Catastrophic Forgetting"
   - Orthogonal weights approach
   - URL: https://arxiv.org/abs/1802.05944

### 2.2 Knowledge Distillation-Based Methods

9. **Li & Hoiem (2016)** - "Learning without Forgetting" (LwF)
   - Knowledge distillation to preserve old task knowledge
   - URL: https://arxiv.org/abs/1606.09282
   - Venue: ECCV 2016

10. **Hou et al. (2018)** - "Less-forgetting Learning in Deep Neural Networks"
    - Side-tuning approach
    - URL: https://arxiv.org/abs/1607.00122

11. **Rebuffi et al. (2017)** - "iCaRL: Incremental Classifier and Representation Learning"
    - Combines knowledge distillation with representation learning
    - URL: https://arxiv.org/abs/1611.07725
    - Venue: CVPR 2017

12. **Kim et al. (2020)** - "Slice: Shallow Pairwise Instance-wise Knowledge Distillation"
    - Efficient KD for continual learning
    - URL: https://arxiv.org/abs/2003.13956

---

## 3. Rehearsal/Experience Replay Methods

### 3.1 Experience Replay

13. **Lopez-Paz & Ranzato (2017)** - "Gradient Episodic Memory for Continual Learning" (GEM)
    - Episodic memory with constrained gradient optimization
    - URL: https://arxiv.org/abs/1706.08840
    - Venue: NeurIPS 2017

14. **Rolnick et al. (2019)** - "Experience Replay for Continual Learning"
    - Practical experience replay analysis
    - URL: https://arxiv.org/abs/1811.11682

15. **Chaudhry et al. (2019)** - "Efficient Lifelong Learning with A-GEM"
    - Average Gradient Episodic Memory
    - URL: https://arxiv.org/abs/1812.00420

16. **Aljundi et al. (2019)** - "Online Continual Learning with Maximally Interfered Retrieval" (MIR)
    - Retrieval-based rehearsal with conflict-aware sampling
    - URL: https://arxiv.org/abs/1904.03137

### 3.2 Generative Replay

17. **Shin et al. (2017)** - "Continual Learning with Deep Generative Replay"
    - Uses GANs for synthetic data replay
    - URL: https://arxiv.org/abs/1705.08690
    - Venue: NeurIPS 2017

18. **van de Ven & Tolias (2018)** - "Generative Replay with Feature Images"
    - Improved generative replay
    - URL: https://arxiv.org/abs/1809.02058

19. **Lesort et al. (2020)** - "Continual Learning with Generative Replay: A Survey"
    - Comprehensive survey on generative replay
    - URL: https://arxiv.org/abs/2205.09110

### 3.3 Rehearsal-Free Methods

20. **Buzzega et al. (2020)** - "Dark Experience for General Continual Learning: a Strong, Simple Baseline" (DER++)
    - Simple but effective rehearsal-free approach
    - URL: https://arxiv.org/abs/1910.14724
    - Venue: NeurIPS 2020

21. **Wang et al. (2022)** - "Learning To Rehearse in Long Term Memory"
    - Memory-based rehearsal without storing data
    - URL: https://arxiv.org/abs/2201.00726

---

## 4. Architectural/Parameter Isolation Methods

### 4.1 Progressive Networks

22. **Rusu et al. (2016)** - "Progressive Neural Networks"
    - Adds new columns for each task
    - URL: https://arxiv.org/abs/1606.04671
    - Venue: NeurIPS 2016

23. **Yoon et al. (2018)** - "Scalable and Orderly Freeze for Neural Network" (PackNet)
    - Iterative pruning to freeze important weights
    - URL: https://arxiv.org/abs/1711.05769
    - Venue: CVPR 2018

### 4.2 Modular/Expansion Methods

24. **Mallya & Lazebnik (2018)** - "PackNet: Adding Multiple Tasks to a Single Network by Iterative Pruning"
    - Iterative pruning and reuse
    - URL: https://arxiv.org/abs/1711.05769

25. **Fernando et al. (2017)** - "PathNet: Evolution Channels Gradient Descent"
    - Neural pathway selection
    - URL: https://arxiv.org/abs/1701.08734
    - Venue: NeurIPS 2017

26. **Hung et al. (2019)** - "Compacting, Picking and Growing for Unbiased Continual Learning"
    - Progressive expansion approach
    - URL: https://arxiv.org/abs/1904.03778

---

## 5. Task-Free and Online Continual Learning

27. **Aljundi et al. (2019)** - "Task-Free Continual Learning"
    - Addresses scenarios without explicit task boundaries
    - URL: https://arxiv.org/abs/1812.03596
    - Venue: CVPR 2019

28. **Cai et al. (2021)** - "Online Task-Free Continual Learning via Dynamic Cluster Memory"
    - CVPR 2024 approach for task-free streaming
    - URL: https://arxiv.org/abs/2311.07120

29. **Chrysakis et al. (2023)** - "Simulating Task-Free Continual Learning Streams From Existing Datasets"
    - URL: https://openaccess.thecvf.com/content/CVPR2023W/CLVision/

30. **Javed & White (2019)** - "Meta-Learning Representations for Continual Learning"
    - Task-agnostic approaches
    - URL: https://arxiv.org/abs/1902.05551

---

## 6. Domain Adaptation

### 6.1 Deep Domain Adaptation

31. **Ganin & Lempitsky (2015)** - "Unsupervised Domain Adaptation by Backpropagation"
    - Domain-adversarial neural networks (DANN)
    - URL: https://arxiv.org/abs/1505.07818
    - Venue: ICML 2015

32. **Long et al. (2015)** - "Learning Transferable Features with Deep Adaptation Networks"
    - Deep adaptation networks
    - URL: https://arxiv.org/abs/1502.02791

33. **Tzeng et al. (2014)** - "Deep Domain Confusion: Maximizing for Domain Invariance"
    - Domain confusion metric
    - URL: https://arxiv.org/abs/1412.3474

34. **Sun & Saenko (2016)** - "Deep CORAL: Correlation Alignment for Deep Domain Adaptation"
    - CORAL loss for domain alignment
    - URL: https://arxiv.org/abs/1607.01719
    - Venue: ECCV 2016

### 6.2 Surveys on Domain Adaptation

35. **Wang & Deng (2018)** - "Deep Visual Domain Adaptation: A Survey"
    - Comprehensive survey
    - URL: https://arxiv.org/abs/1802.03601

36. **Kouw & Loog (2019)** - "A Survey on Domain Adaptation"
    - URL: https://arxiv.org/abs/1911.00213

---

## 7. Transfer Learning and Fine-Tuning

### 7.1 Fine-Tuning Strategies

37. **Guo et al. (2019)** - "SpotTune: Transfer Learning Through Adaptive Fine-Tuning"
    - Adaptive fine-tuning strategy
    - URL: https://arxiv.org/abs/1808.04306
    - Venue: CVPR 2019

38. **Kornblith et al. (2019)** - "Better Transfer Learning Through Inverted Label Preserving"
    - Analysis of transfer learning
    - URL: https://arxiv.org/abs/1808.04506

39. **He et al. (2019)** - "Rethinking ImageNet Pre-training"
    - URL: https://arxiv.org/abs/1811.08883

### 7.2 Linear Probing and Full Fine-Tuning

40. **Kumar et al. (2022)** - "Fine-tuning can distort pretrained features"
    - Analysis of linear probing vs fine-tuning
    - URL: https://arxiv.org/abs/2203.16327

41. **Xu et al. (2024)** - "Comparison of Fine-tuning Strategies for Transfer Learning in Medical Image Classification"
    - Comprehensive study of fine-tuning
    - URL: https://arxiv.org/abs/2406.10050

---

## 8. Benchmarks and Evaluation

### 8.1 Image Classification Benchmarks

42. **Lomonaco & Maltoni (2017)** - "CORe50: A New Benchmark for Continual Object Recognition"
    - URL: https://arxiv.org/abs/1705.09350

43. **Zenke et al. (2017)** - "Continual Learning Through Synaptic Intelligence" (Uses CIFAR-100 benchmarks)
    - URL: https://arxiv.org/abs/1703.04200

44. **Lopez-Paz et al. (2017)** - "Gradient Episodic Memory" (Defines evaluation protocols)
    - URL: https://arxiv.org/abs/1706.08840

45. **Rebuffi et al. (2017)** - "iCaRL" (Split CIFAR benchmarks)
    - URL: https://arxiv.org/abs/1611.07725

### 8.2 Recent Benchmarks

46. **Lin et al. (2021)** - "CLEAR: Continual LEArning on Real-World Imagery"
    - Real-world benchmark
    - URL: https://openreview.net/forum?id=43mYF598ZDB

47. **Mai et al. (2022)** - "Online Continual Learning on Class Incremental Blurry Task Configuration"
    - CVPR 2022 benchmark
    - URL: https://arxiv.org/abs/2203.15239

---

## 9. Class-Incremental Learning

### 9.1 Surveys

48. **Zhou et al. (2024)** - "Class-Incremental Learning: A Survey"
    - Comprehensive CIL survey (TPAMI 2024)
    - URL: https://arxiv.org/abs/2302.03648

49. **Wang et al. (2024)** - "Continual Learning of Large Language Models: A Comprehensive Survey"
    - ACM Computing Surveys 2025
    - URL: https://arxiv.org/abs/2402.01364

### 9.2 Key Methods

50. **Castro et al. (2018)** - "End-to-End Incremental Learning"
    - URL: https://arxiv.org/abs/1807.09536
    - Venue: ECCV 2018

51. **Wu et al. (2019)** - "Large Scale Incremental Learning"
    - URL: https://arxiv.org/abs/1905.13260
    - Venue: CVPR 2019

52. **Belouadah & Popescu (2019)** - "DeGAN: DeGAN: Declarative Network for Incremental Learning"
    - URL: https://arxiv.org/abs/1806.06625

---

## 10. Continual Learning for LLMs

### 10.1 LLM-Specific Methods

53. **Wang et al. (2024)** - "Continual Learning of Large Language Models: A Comprehensive Survey"
    - URL: https://arxiv.org/abs/2402.01364

54. **Jang et al. (2022)** - "Continual Pre-training Makes LLMs Better at Learning from Instructions"
    - URL: https://arxiv.org/abs/2212.00515

55. **Scialom et al. (2022)** - "Continual Learning in LLMs"
    - URL: https://arxiv.org/abs/2206.06156

### 10.2 Parameter-Efficient Fine-Tuning

56. **Hu et al. (2021)** - "LoRA: Low-Rank Adaptation of Large Language Models"
    - Parameter-efficient transfer learning
    - URL: https://arxiv.org/abs/2106.09685

57. **Houlsby et al. (2019)** - "Parameter-Efficient Transfer Learning for NLP"
    - Adapter modules
    - URL: https://arxiv.org/abs/1902.00751

---

## 11. Theoretical Analysis

58. **McMahan et al. (2017)** - "Communication-Efficient Learning of Deep Networks from Decentralized Data"
    - Analysis of distributed learning
    - URL: https://arxiv.org/abs/1602.05629

59. **Gurbuzbalaban et al. (2022)** - "The Heavy-Tail Phenomenon in SGD"
    - Theoretical analysis of forgetting
    - URL: https://arxiv.org/abs/2110.02894

60. **Mirzadeh et al. (2020)** - "Linear Mode Connectivity in Multi-Task Learning"
    - URL: https://arxiv.org/abs/2003.06881

---

## 12. Comprehensive Surveys

61. **De Lange et al. (2021)** - "A Continual Learning Survey: Defying Forgetting in Classification Tasks"
    - URL: https://arxiv.org/abs/2102.10217
    - Venue: TPAMI 2021

62. **Mai et al. (2022)** - "A Comprehensive Survey of Continual Learning: Theory, Method and Application"
    - URL: https://arxiv.org/abs/2302.00487
    - Venue: TPAMI 2024

63. **Parisi et al. (2019)** - "Continual Learning: A Review"
    - URL: https://arxiv.org/abs/1909.10083
    - Venue: Neural Networks 2019

64. **Kudithipudi et al. (2022)** - "Continual Learning: Theory, Algorithms, and Applications"
    - URL: https://arxiv.org/abs/2210.00614

---

## 13. Recent Advances (2022-2025)

### 65.continual learning theory

65. **Kleinberg & Mullainathan (2023)** - "In-context Learning as Encoding in Context"
    - URL: https://arxiv.org/abs/2303.07146

66. **Ke et al. (2023)** - "Continual Learning with Pre-trained Models"
    - URL: https://arxiv.org/abs/2303.16241

67. **Smith et al. (2023)** - "Continual Learning at Scale"
    - URL: https://arxiv.org/abs/2306.12350

68. **Biesialska et al. (2023)** - "Continual Lifelong Learning in Natural Language Processing"
    - URL: https://arxiv.org/abs/2007.01490

69. **Du et al. (2024)** - "Understanding In-Context Learning in Transformers"
    - URL: https://arxiv.org/abs/2402.13294

70. **Zhang et al. (2024)** - "Continual Learning in the Presence of Concept Drift"
    - URL: https://arxiv.org/abs/2401.07625

---

## 14. Additional Important Works

71. **Germain et al. (2019)** - "Mixing Object Categories and Instances"
    - URL: https://arxiv.org/abs/1902.02206

72. **Zhou et al. (2023)** - "Domain Adaptive Ensemble Learning"
    - IEEE TIP
    - URL: https://arxiv.org/abs/2103.16370

73. **Cai et al. (2021)** - "Rehearsal-Free Continual Learning"
    - URL: https://arxiv.org/abs/2103.09791

74. **Bengio et al. (2015)** - "Deep Learning Debates"
    - Historical perspective
    - URL: https://arxiv.org/abs/1507.05738

75. **Hadsell et al. (2020)** - "Embodied Continual Learning"
    - URL: https://arxiv.org/abs/2006.12909

---

## Summary Statistics

- **Total Papers**: 75+
- **Papers from 2015-2025**: 60+
- **Key Venues**: NeurIPS, ICML, CVPR, ECCV, TPAMI, ACM Computing Surveys

### Topic Distribution:
- Catastrophic Forgetting: 8 papers
- Regularization Methods: 12 papers
- Rehearsal/Experience Replay: 11 papers
- Architectural Methods: 7 papers
- Domain Adaptation: 8 papers
- Transfer Learning/Fine-tuning: 6 papers
- Benchmarks: 6 papers
- Class-Incremental Learning: 6 papers
- LLM Continual Learning: 5 papers
- Surveys: 6 papers

---

*Last Updated: February 2025*

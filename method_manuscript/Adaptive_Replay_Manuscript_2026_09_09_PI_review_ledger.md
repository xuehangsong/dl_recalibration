# PI review ledger — Adaptive Replay manuscript (2026-09-09)

Source: `Adaptive_Replay_Manuscript_2026_09_09.docx` (preserved unchanged)
Derivative: `Adaptive_Replay_Manuscript_2026_09_09_PI_review_tracked_changes_comments.docx`
Derivative SHA-256: `f66ed47b68b403ac97594d1ae193adae9a5c046a5cf47cf7ace9673a187bcd04`

This derivative retains the senior-scientist's existing tracked changes and comments, and adds the PI review comments below. New PI comments are prefixed `[PI review — major]` so they can be filtered in Word. Two PI wording changes are tracked: the abstract scope is narrowed to a controlled adaptive-replay update study, and the unsupported simulation-cost acceptance claim is reframed as a separately reported cost item.

## Recommended model configuration

Use GPT-6 Astra with high reasoning for the primary review. OpenAI's official model guide describes GPT-6 Astra as the flagship model for the hardest end-to-end work. Use GPT-5.6 Sol with high reasoning as the lower-cost fallback. Keep the review prompt evidence-bounded: treat the manuscript and repo artifacts as the authority, preserve the source DOCX, and require anchored major comments rather than broad copyediting.

## Major comments added

210. **ABSTRACT / SCOPE** — anchor: `This study develops`
   [PI review — major] The abstract currently says this study develops a continual-learning framework that learns without catastrophic forgetting and offers a transferable framework for other environmental surrogates. The demonstrated evidence is an offline 2-D synthetic U-Net update experiment. Please narrow the title, abstract, and conclusion to a controlled adaptive-replay update study unless additional architectures, domains, or lifecycle steps were actually tested. Transfer and online-deployment language should be framed as future work.

211. **DATASET / SPLITS** — anchor: `The preliminary dataset includes`
   [PI review — major] Please add an auditable split/provenance table: counts of independent simulation runs or trajectories and transitions in the training, controller-validation, and untouched final-test partitions; the split unit and order of operations; threshold-calculation scope; random seeds; and confirmation that no trajectory appears in more than one partition. Adjacent transitions from one simulation are correlated, so splitting after pair creation would make the reported retention/adaptation results optimistic.

212. **RARE-REGIME DEFINITION** — anchor: `To identify rare plume regimes`
   [PI review — major] Mass90 is both the regime-selection variable and a reported plume metric. State exactly when it is computed, whether the 40th/97th-percentile thresholds are fixed using training data only, and whether the t+1 state is available at selection time. Because the present experiment defines rarity from the response rather than from pumping/source/hydrogeologic drivers, avoid presenting this as a demonstrated operational shift unless those drivers are separately held out or analyzed.

213. **ADAPTIVE CONTROLLER** — anchor: `With this controller`
   [PI review — major] The adaptive controller is not reproducible from the current tracked document. The loss-balanced equation in Table 5 is malformed/ambiguous, and r*, r(e+1), omega, epsilon, replay caps, initialization, update interval, threshold mode, and checkpoint/early-stopping rules are not all defined. Please replace the equation with a clean rendered expression, provide pseudocode or an algorithm box, give exact parameter values, and state which decisions were frozen before final-test evaluation.

214. **ACCEPTANCE CONTRACT** — anchor: `To make model updating operationally meaningful`
   [PI review — major] The acceptance contract is not yet fixed: Figure 3 uses a 25% historical-degradation threshold, Figure 5 uses 30%, the text calls 30% illustrative, while Methods gives 1.05× historical RMSE and 0.80× rare RMSE. Please either preregister one threshold set for this experiment or label all values as exploratory examples and remove claims that the results meet predefined redeployment criteria. Make explicit that validation steers replay and an untouched final test supports headline claims.

215. **RESULTS / UNCERTAINTY** — anchor: `Compared with fixed replay`
   [PI review — major] The numerical results (for example 0.58→1.11, 10.04→3.92, 80.4→26.5%, and >85%) need provenance and uncertainty before they can support deployment guidance. Please report sample counts, the independent unit (trajectory/run rather than adjacent pixels or transitions), seeds/repeats, paired confidence intervals or equivalent uncertainty, and exact metric definitions. A representative plume map is illustrative, not evidence of general performance.

216. **COMPUTE CLAIM** — anchor: `3.3 Replay strategies`
   [PI review — major] The manuscript labels Section 3.3 as a gain in computing efficiency and makes fewer full-order simulations part of the acceptance criteria, but no update-versus-retraining simulation count, wall-clock, hardware, or equal-budget comparison is reported. Please add measured cost evidence under a stated budget or remove/reframe these claims as a hypothesis/future-work objective rather than a demonstrated result.

217. **LIFECYCLE / DEPLOYMENT SCOPE** — anchor: `The framework is designed`
   [PI review — major] The discussion describes online maintenance, uncertainty-triggered cases, monitoring, observation assimilation, and redeployment. These are reasonable lifecycle goals, but they are not executed in this offline experiment. Please separate demonstrated results from the proposed future workflow and avoid implying that this paper validates the full seven-step recalibration framework or automatic deployment decisions.

218. **COMPARATOR FAIRNESS** — anchor: `Model E: Adaptive replay`
   [PI review — major] Please reconcile Table 1 with the surrounding text and figures. The table has inconsistent descriptions of Model B's starting data, Model C/D update data, and trainable layers, plus visible text corruption (for example, 'Starts rom' and 'controlled relay'). Report the same update budget, hyperparameter-selection rule, and layer-freezing convention for every comparator before interpreting the old/new tradeoff.

## Verification performed

- Source and derivative were inspected as OOXML packages; the derivative contains the original Word comments/revisions plus the nine new PI comments and two new PI tracked replacements.
- The source currently has `w:trackRevisions` enabled. The source and derivative were not overwritten.
- The repository history was checked against the prior adaptive-replay review and the authoritative Task 1 final report. The prior review's central boundary remains applicable: this is strongest as a controlled offline UPDATE/adaptive-replay study, not validation of the full seven-step lifecycle.
- Reported numbers remain unverified because the repository does not contain the supporting experiment code, manifests, seeds, logs, and raw metrics needed to reproduce them.

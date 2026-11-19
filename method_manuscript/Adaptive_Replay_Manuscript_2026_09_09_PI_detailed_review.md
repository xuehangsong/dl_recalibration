# PI detailed review and revision blueprint

**Manuscript:** `Adaptive_Replay_Manuscript_2026_09_09.docx`  
**Review mode:** GPT-6 Astra, high reasoning  
**Purpose:** Provide constructive, paste-ready revisions and anchored comments for a later model to convert into Word tracked changes and comments.

**Authoritative source SHA-256:** `20ad1fe864942ea089ea68a83a610af4b396e151310f5fafb55cb964576ffed7`

This review supersedes the scientific recommendations in the earlier `PI_review_ledger.md`. Use the September 9 **source** DOCX, not the earlier PI derivative, for later conversion. Review the text with the source author's insertions included and deletions excluded; the underlying historical revisions remain part of the source. Paragraph identifiers below are zero-based direct `word/document.xml/w:body/w:p` positions, including blank paragraphs and excluding paragraphs inside tables. Exact anchors and the source hash take precedence over these positions.

**Conversion rule:** Only the edits explicitly listed as **APPLY** in Section 14 should become tracked manuscript text. Other proposed methods, equations, table notes, and numerical passages are **AUTHOR CONFIRMATION REQUIRED** and should be placed in comments, not inserted as completed work. Bracketed placeholders must never enter the manuscript body automatically. Reviewer analysis is for the PI and conversion model; only designated comment text goes into Word comments.

## Editorial recommendation

The manuscript has a useful and potentially publishable core: a controlled offline experiment asking whether adaptive replay can improve a rare plume regime while retaining performance on a historical regime. The paper is not yet ready to claim a general continual-learning framework, online lifecycle validation, or deployment guidance because the current draft does not document the data split, controller implementation, statistical uncertainty, comparator budget, or fixed acceptance contract well enough to support those claims.

The revision should preserve the paper's central contribution while tightening the evidence boundary. The most important sequence is:

1. Reconcile Figure 3, model identities, and the numerical provenance (Sections 8 and 15). This could change the scientific conclusion.
2. Document the resolved split issue and the actual validation/test roles (Sections 3 and 5).
3. Recover the executed controller and compare it with fixed replay at its cap (Sections 6 and 9).
4. Explain the threshold scenarios and how they were selected (Section 7).
5. Correct Mass90's physical interpretation and report uncertainty (Sections 4 and 10).
6. Apply the scope, results-language, and cost revisions (Sections 1, 2, 11, 12, and 14).

The sections below follow manuscript topics; the sequence above gives scientific priority. “Must fix” means resolve the reporting issue or narrow the dependent claim. It does not require carrying out every proposed future experiment. The core Word review should contain eight consolidated comments (Section 16), with detailed replacement text supplied separately. This keeps the senior scientist's review manageable.

The manuscript has made useful progress since the earlier copy: it adds environmental continual-learning references, explicitly calls the experiment offline in Section 2.2, clarifies that Models B–E start from the baseline, and explains validation's controller role. Your trajectory-split question (existing comments 55/56) is marked resolved. All five embedded figure files are byte-identical between the older local manuscript and September 9 source. Their unchanged status does not establish that no experiments were run; it means the September figure evidence has not changed in these two local files.

## 1. Title, abstract, and study scope — must fix

**Exact anchor:** title and the abstract sentence beginning “This study develops a continual-learning framework…”

**Problem:** A lifecycle framework is a useful motivation and can remain in the paper, but the empirical claim must match the offline 2-D U-Net experiment. The title's “Without Forgetting” overstates even the adaptive results: Figure 5 reports historical degradation of 21.1%, 26.5%, or 38.1%, depending on controller. EWC's failure does not by itself refute adaptive replay's performance; the relevant issue is residual degradation in the adaptive methods and the absence of evidence for cross-system transfer.

**Suggested tracked replacement for the abstract core:**

> Updating a groundwater-plume surrogate requires balancing improved prediction of newly encountered conditions against retention of previously learned behavior. We examine this tradeoff in a controlled offline experiment using a two-dimensional U-Net pump-and-treat surrogate and synthetic plume simulations. Historical and rare regimes are defined by low and high relative changes in the number of cells containing 90% of plume mass. A baseline trained on the historical regime is updated using simple fine-tuning, fixed replay, elastic weight consolidation, and validation-controlled adaptive replay. The adaptive methods adjust the historical/new-regime sampling balance using validation signals for retention and learning. The reported comparisons show improved rare-regime prediction accompanied by method-dependent historical-regime degradation. Adaptive controllers provide different tradeoffs from the fixed replay configuration examined, although isolating the benefit of adaptation requires comparison with fixed replay at matched historical-data exposure. These results illustrate how regime-specific performance can inform surrogate updating. The approach may be relevant to other environmental surrogates, with transfer and operational deployment requiring further evaluation.

**Suggested title:**

> Adaptive Replay for U-Net Groundwater Plume Surrogates: Balancing Rare-Regime Learning and Historical Performance

**Comment to insert:**

> Please align the title, abstract, objective, and conclusion with the experiment actually completed. A narrower claim will make the adaptive-replay result more credible and will leave the general lifecycle framework as a clearly identified next phase rather than an unsupported result.

## 2. Contribution and novelty boundary — must fix

**Exact anchor:** Introduction paragraph beginning “Continual learning has also begun…” and objective sentence beginning “The objective of this study…”

**Problem:** The draft does not distinguish the new groundwater application from existing adaptive replay/scheduling methods. The controller is presented as a framework contribution, but the paper currently gives no formal novelty statement or controlled ablation showing which controller component creates the gain.

**Suggested replacement paragraph:**

> The objective of this study is to evaluate validation-controlled replay for updating a U-Net groundwater-plume surrogate when it encounters a response regime excluded from baseline training. Using a controlled offline partition of synthetic simulations, we compare rare-regime learning and historical-regime retention across fine-tuning, fixed replay, elastic weight consolidation, and adaptive replay. The contribution is a groundwater-specific evaluation of these tradeoffs and their interpretation for surrogate updating. The experiment addresses the update component of a broader lifecycle-management framework; operational drift detection and transfer to other systems remain subsequent evaluation steps.

**Comment to insert:**

> Please state explicitly what is methodologically new here relative to prior replay scheduling and adaptive replay literature. If the contribution is the groundwater-specific stress-test and acceptance workflow, say that directly; if the controller itself is new, provide the algorithmic distinction and an ablation.

## 3. Dataset provenance and independent splitting — must fix

**Exact anchor:** Section 2.2 paragraph beginning “This study uses plume simulation data…” and Table 2.

**Problem:** “10,000 physics-based simulation runs” is not enough to reproduce the experiment. The manuscript must identify the independent unit, the number of snapshots and transitions per run, how runs were assigned to training/controller-validation/final-test partitions, and whether Mass90 thresholds were calculated before or after the split. Adjacent transitions within one trajectory are correlated. The earlier comments in the document include the same concern, but the current text does not provide the promised table.

**AUTHOR CONFIRMATION REQUIRED — proposed methods text after the dataset description:**

> Complete simulation runs were assigned to disjoint training, validation, and final-test partitions using [assignment rule and seed]. All transitions from a run remained within its assigned partition. The partitions contained [counts] independent runs and [counts] transitions, respectively. The 40th- and 97th-percentile score thresholds were calculated from [population and stage of analysis] and applied according to [rule]. The split manifest and dataset version are provided in [location].

Do not insert this template until the author confirms it. Constructing pairs before splitting is not inherently wrong if all pairs are subsequently grouped by complete run; splitting individual pairs independently is the concern. Training-derived thresholds are a clean prospective design. If the complete dataset was used to define an offline benchmark, disclose that transductive construction and limit the claim; that fact alone does not prove weight-training leakage. Also explain the fate of the unselected middle 57% and whether the same realization can contribute both low- and high-change transitions within one partition. The Task 1 report describes snapshots at days 0–4 and 1 m cells; confirm that this exact dataset version was used before adding those details.

**Required table for the manuscript:**

| Item | Training | Controller validation | Final test |
|---|---:|---:|---:|
| Independent simulation runs | `[n]` | `[n]` | `[n]` |
| Snapshots | `[n]` | `[n]` | `[n]` |
| Constructed transitions | `[n]` | `[n]` | `[n]` |
| Historical-regime cases | `[n]` | `[n]` | `[n]` |
| Rare-regime cases | `[n]` | `[n]` | `[n]` |
| Threshold source | fixed from `[partition]` | applied unchanged | applied unchanged |

**Comment to insert:**

> I see that our earlier split question is marked solved. Could we put that solution into Methods with a small table of runs and transitions in each partition? Please confirm that complete runs stay together, identify how the percentile thresholds were calculated, and explain what happens to the middle 57%. This should make the experiment reproducible without reopening an issue already resolved in the implementation.

## 4. Mass90 definition and leakage — must fix

**Exact anchor:** Section 2.2 equation and paragraph beginning “The dataset is partitioned into two regimes…”

**Problem:** The main issue is physical interpretation. A cell count containing 90% of mass does not encode the locations or connectivity of those cells. A plume can translate, rotate, or fragment with the same count and a zero change score. Multiplying all concentrations by the same positive factor also leaves that count unchanged. Consequently, this is a compactness/size descriptor of the mass-dominant cells, not a general measure of redistribution, total-mass change, or decision importance. Using a response descriptor to stratify an offline test, and also reporting an associated prediction metric, is not inherently leakage. The concern arises if future targets inform online selection or final-test outcomes inform training decisions.

**Suggested replacement text:**

> In this offline experiment, the Mass90 change score is a retrospective descriptor of changes in the number of cells containing most of the plume mass. It requires reference plume states at both time steps. The score does not identify where those cells are located, so translation or rearrangement of the plume can occur without changing it. Its normalization also treats expansion and contraction differently: a change from 10 to 20 cells gives a score of 1, whereas 20 to 10 gives 0.5. We use this score to construct a response-based stress test rather than to identify the operational cause of a change.

The 1 and 0.5 examples correct the arithmetic in existing comment 53, which gives 2 and 1. Preserve that historical comment; do not silently rewrite it. Ask the author to specify cell sorting/cumulative-mass calculation, treatment of zero total mass, negative predictions, and grid/porosity/thickness weighting. Concentration sums are proportional to dissolved mass only under appropriate uniform pore-volume assumptions. Avoid adding sorbed or total-system inventory claims to this synthetic concentration-field study.

**Comment to insert:**

> Please state whether the t+1 field is available when a case is selected for updating. If selection is retrospective, call this a response-defined offline stress test throughout. If you intend an operational trigger, add a separate driver-based or pre-response definition and test it without using future plume information.

## 5. Training, validation, and final test roles — must fix

**Exact anchor:** paragraph beginning “Standard surrogate training and continual learning…” and Table 2.

**Problem:** The draft correctly says validation is used more actively, but it does not state which decisions use validation: replay ratio, threshold mode, cap, checkpoint, early stopping, or model selection. The final test must remain untouched until all such choices are frozen. The Results section also needs labels identifying whether each number is validation or final-test performance.

**AUTHOR CONFIRMATION REQUIRED — methods reporting template:**

> Training transitions were used for network updates. Validation data were used for [actual decisions, including replay control and checkpoint selection]. The evaluation partitions for each panel are identified in the captions. Final-test results were computed after [the actual configuration-freezing step].

The source does not establish that all reported numbers are final-test results. Figure 5(a) explicitly monitors validation; do not relabel it as test performance. The author must identify the partitions for Figures 3(a–c), 4, and 5(b–c). Validation used to select a fixed ratio is legitimate; that ratio should then be frozen for test evaluation. There is no requirement for a new fourth dataset.

**Comment to insert:**

> Please add one sentence to every results caption identifying validation versus final-test data. A reader should be able to determine whether the same data that controlled replay were later used to support the deployment-oriented claim.

## 6. Controller equations and algorithm — must fix

**Exact anchor:** Section 3, “Adaptive replay controller,” especially the loss-balanced equation and the paragraph beginning “With this controller…”

**Problem:** In the source equation content and its extracted accepted text, Equation (5) is incomplete: the target expression lacks a clear equality and the recursion ends at `r_(e+1) = r_e +`. Recover the executed rule from code; do not infer it from typography. Equation (4) writes thresholds as `k × sigma`, while its explanation says “above the smoothed behavior,” which would instead suggest `mean + k × sigma`. These are different controllers. Decay, warm-up, bounds, decision frequency, and no-change behavior are unspecified. Direct native Word rendering was not performed in this review.

**AUTHOR CONFIRMATION REQUIRED — algorithm documentation outline, not an invented replacement equation:**

> The replay controller was initialized with [ratio and state]. After [update interval], historical- and rare-regime validation losses were calculated using [loss and aggregation]. The next replay fraction was obtained using [complete executed equation], with bounds [values] and [rounding/sampling rule]. The threshold controller used [exact signal, threshold formula, and increase/decrease/hold rules]. The loss-balanced controller used [normalization, retention weight, and numerical protection]. Checkpoints were selected using [rule], and updating ended according to [rule]. All controller settings are listed in [table or supplement].

Specific questions for the author/code review:

- Does `r` denote the old-sample fraction of each batch or a loss weight? Equation (1)'s weighted sum of batches is only schematic unless the sampling operation is defined.
- Is `L` MSE, RMSE, or another training loss? RMSE degradation and MSE ratios are not interchangeable: a 30% RMSE increase is a 69% MSE increase under the same aggregation.
- Are baseline losses protected using `max(L0, epsilon)`, additive epsilon, or another rule? Adding epsilon only to the final old/new mixture denominator cannot protect the earlier divisions by zero baseline loss. A floor and an additive constant are distinct operations.
- Does the incomplete recursion use damping, additive steps, or direct assignment? No smoothing factor may be invented by the conversion model.
- Does “new loss improving” mean improvement over the preceding epoch, a moving average, or the baseline? Define the interval and tolerance.
- EWC: identify the samples used to estimate parameter importance. “Held-out” must not mean final-test data. Report per-example versus batch-gradient squaring, loss/likelihood definition, scaling, and the lambda search; a squared batch-average gradient is generally not the same as the average squared per-example gradient.

**Comment to insert:**

> Could we rebuild Equations (4)–(5) from the executed code and add a short algorithm box? Equation (5) stops partway through the update rule, and the EMA threshold formula does not match its explanation. Please also distinguish the replay control thresholds from the criteria used to judge the final model, and specify where denominator protection is applied. These details determine the method being tested.

## 7. Acceptance criteria must be one contract — must fix

**Exact anchors:** Methods equation after “For example…,” Figure 3 caption, Figure 5 text and caption.

**Problem:** Methods illustrates 5% allowed historical degradation and 20% required rare improvement; Figure 3 uses 25% historical degradation; Figure 5 uses 30% and 85%. Different threshold scenarios are legitimate if their purpose is explicit. The problem is calling the conclusions “predefined” acceptance or redeployment decisions without explaining which scenario was applied or when it was chosen. Formal preregistration is not mandatory, but pre-test selection must not be claimed retrospectively.

**APPLY via R11/R17 — conservative description of the thresholds currently shown:**

> Acceptance-region diagrams illustrate how the ranking of update strategies depends on the tolerated historical degradation and required rare-regime improvement. The threshold examples shown here provide scenarios for interpreting these tradeoffs. Satisfying an example region alone does not establish suitability for deployment, which also depends on the intended use, independent evaluation, and relevant plume and decision errors.

**AUTHOR CONFIRMATION REQUIRED — alternative if a pre-test criterion can be documented:**

> Before final-test evaluation, we specified historical-regime RMSE degradation ≤ [X]% and rare-regime RMSE improvement ≥ [Y]% for [purpose and rationale]. These criteria were applied to [comparisons]. Additional threshold scenarios are identified separately as sensitivity analyses.

Do not add mandatory mass, peak, or cost thresholds unless they were actually defined and evaluated. Report absolute RMSE alongside percentage changes: a low baseline can make a moderate absolute increase look large. No generic 25% or 30% tolerance can establish regulatory or operational acceptability.

**Comment to insert:**

> Please choose one of the two interpretations above and apply it consistently. Until the contract is fixed, use “illustrative acceptance region” rather than “acceptable for redeployment.”

## 8. Figure 3 and Figure 4 comparator reconciliation — must fix

**Exact anchors:** Figure 3(c), paragraph beginning “The amount of trainable capacity…,” Table 1, and Figure 4.

**Problem:** Figure 3(c) labels the full-network configuration “Model C” and reports **0.64 µg/L historical RMSE and 0.99 µg/L rare RMSE**. Decoder-only Model B reports 1.11 and 3.92, and Figure 4 fixed replay reports 1.03 and 1.21. Table 1 calls Model C replay fine-tuning; the prior Task 1 report calls Model C retraining from scratch. These labels do not establish which experiment generated the Figure 3(c) bars. If evaluated comparably, its 0.64/0.99 pair appears better in both metrics than the displayed fixed replay result. This is the highest-priority reconciliation.

**Comment to insert:**

> Could we first identify exactly what “Full-network (Model C)” in Figure 3(c) represents? Its old/rare RMSE values are 0.64/0.99, while fixed replay in Figure 4 gives 1.03/1.21. Table 1 calls Model C replay, and the earlier report used that label for retraining from scratch. If these results are comparable, the Figure 3(c) result changes the main comparison; if they use different protocols or data, please identify those differences. The paragraph's claim that decoder-only updating reduced forgetting also runs opposite to these displayed bars.

**AUTHOR CONFIRMATION REQUIRED — caption template:**

> Panel [identifier] reports [experiment/run IDs], using [evaluation partition], [baseline checkpoint], and [update/checkpoint rule]. “Full-network” denotes [initialization, update data, trainable layers]. Panels [identifiers] differ in [actual protocol differences].

## 9. Adaptive replay reaches its cap — must fix

**Exact anchor:** Section 3.4 paragraph beginning “Adaptive replay was evaluated…” and Figure 5(a).

**Problem:** The replay ratio rises rapidly to the upper cap and stays there. That result may show that a capped high-replay update works, but it does not by itself show that the controller adaptively discovers a useful ratio or reduces manual tuning. The strongest comparison is the equivalent fixed replay run at the same cap, using the same update budget and seed policy.

**Suggested replacement text:**

> In the trajectory shown in Figure 5(a), the replay fraction reaches 0.8 early in updating and remains at that cap for most subsequent epochs. Historical forgetting and rare-regime validation loss decrease over the same period. This behavior is consistent with successful learning under high historical replay, but it does not isolate the contribution of adaptive scheduling. A fixed replay run at the same cap and update budget would help distinguish the effect of the schedule from the amount of historical data used.

Minimal additional comparison, only if adaptive superiority remains a central claim: fixed `r = 0.8`, initialized from the same baseline, with matched total optimizer steps/batch size and the same evaluation cases. Report total old/new sample presentations because fixed steps alone do not match exposure when ratios change. A second fixed ratio matching the adaptive run's average historical exposure can help isolate scheduling. Use available logs first; this review authorizes no training reruns.

**Comment to insert:**

> Please add the fixed-replay-at-cap comparator or soften the claim about reducing manual replay-ratio tuning. Also report whether the cap was selected before the final test and whether the controller reached it for all seeds or only the displayed run.

## 10. Statistical uncertainty and independent units — must fix

**Exact anchor:** Results paragraphs reporting `0.58 → 1.11`, `10.04 → 3.92`, `80.4% → 26.5%`, and `>85%`.

**Problem:** Point estimates and one representative plume map are insufficient for deployment-oriented conclusions. Pixel-level values are not independent observations, and adjacent transitions within one simulation are correlated.

**AUTHOR CONFIRMATION REQUIRED — use only after these analyses are actually performed:**

> We evaluated paired model differences on the same held-out simulation runs. Confidence intervals were obtained by resampling complete runs while retaining their associated transitions and recomputing [metric and aggregation]. Variation across [number] training seeds was reported separately using [summary]. Representative plume maps illustrate individual predictions.

A practical first step is paired resampling of existing predictions, if available, followed by a small matched set of training seeds if needed to support robust ranking. Three to five seeds would be useful; it is a recommendation, not a completed result or universal publication rule. A case-bootstrap interval describes test-case variation conditional on trained models and does not replace seed variability. If only one seed was run, call the comparison exploratory and report that limitation. Do not conflate one seed with one independent simulation case.

Specify whether inference is one-step with reference concentration input or free-running with predicted concentration fed back. The report's days 0–4 snapshots do not demonstrate a long-term rollout evaluation. If only one-step results exist, scope the conclusions accordingly; add free-running lead curves only if long-horizon maintenance remains a claim.

**Comment to insert:**

> Please add the number of independent runs, number of seeds, paired confidence intervals, and the exact aggregation rule for every headline metric. If only one run or one seed exists, state that limitation directly and remove deployment-oriented language from the result interpretation.

## 11. Efficiency and full-retraining comparison — must fix

**Exact anchors:** acceptance criterion (4), Section 3.3 heading, and Discussion statements about update cost.

**Problem:** The draft claims computing efficiency and says an acceptable update requires far fewer full-order simulations, but it does not report simulation counts, wall-clock, hardware, or a same-budget full-retraining comparator. The earlier prototype plan expected a full-retraining fallback; this manuscript does not show it.

**AUTHOR CONFIRMATION REQUIRED — cost-reporting template:**

> We report newly generated physics simulations separately from reuse of existing simulation data. Model-update cost includes training, validation/controller evaluation, parameter-importance estimation, and configuration searches, measured on [hardware] using [wall-clock and memory definitions]. Comparison with retraining uses [shared dataset and budget or target-accuracy rule].

Retraining can reuse exactly the same existing simulations; it does not inherently require new physics runs. Fewer gradient updates, less replay storage, faster inference, and fewer new physics simulations are different claims. EWC stores parameter-reference/importance arrays and therefore is not automatically more memory-efficient than a small replay buffer. Without measurements, describe it as a method that avoids explicit historical-sample replay during updating. The 600 ms speedup cited from Song et al. concerns the earlier surrogate's inference, not the cost of this update method.

**APPLY via R13/R19 — scope of evidence presented in the draft:**

> The comparisons presented here characterize prediction and retention errors. They do not quantify savings in new physics simulations, training time, or total memory. Evaluating these costs alongside accuracy is a subsequent step in assessing the practical value of the update strategies.

## 12. Lifecycle, online maintenance, and conclusion — must fix

**Exact anchors:** Discussion headings “Managed recalibration and online surrogate maintenance” and “Validation-based acceptance criteria for deployment guidance,” plus Conclusion.

**Problem:** The discussion describes monitoring, uncertainty triggers, observation assimilation, online updates, and redeployment. Those are appropriate implications, but the experiment does not execute them. The authoritative Task 1 report presents them as lifecycle components and prototype objectives, not as established results from this manuscript.

**Suggested replacement discussion paragraph:**

> The present experiment supports one technical component of a broader lifecycle: updating a synthetic U-Net surrogate after a response-defined rare-regime stress test. A complete managed recalibration workflow would additionally require an operational drift trigger, provenance-controlled preparation of new targets, uncertainty calibration, a fixed deployment acceptance contract, rollback/version control, and documented human approval. These components are outside the present experiment. The results therefore motivate a future governed prototype demonstration rather than establish automatic online maintenance or deployment readiness.

**Suggested replacement conclusion — APPLY via R21:**

> This study examines the balance between rare-regime learning and historical-regime retention when updating a synthetic U-Net groundwater-plume surrogate. The reported configurations improve rare-regime prediction with different levels of historical degradation, illustrating why both regimes should be evaluated when choosing an update strategy. Validation-controlled replay offers a practical way to vary historical-data exposure, while comparisons with fixed replay at matched exposure are needed to establish the added value of the schedule. These findings support further development of the update component of surrogate lifecycle management. Evaluation across repeated updates, independent simulation cases and training seeds, together with measured computational costs and decision-specific performance criteria, will be needed to assess its broader use in groundwater remediation.

## 13. Table 1 and language cleanup — recommended after major fixes

**Exact anchor:** Table 1.

Correct the visible errors and make the table a protocol contract:

- “Starts rom” → “Starts from.”
- “controlled relay” → “validation-controlled replay.”
- “Test rehearsal-based memory preservation” is a valid purpose statement; no change is needed solely for this wording.
- The accepted source already states that Model B starts from the baseline and is updated on the top 3%. Preserve that improvement. Its decoder-only capacity differs from the full-network replay/EWC updates and is therefore a comparison factor requiring explicit discussion.
- State the trainable layers, update epochs, replay ratio or controller, optimizer, seed policy, checkpoint rule, and evaluation partitions for every model.
- Use “historical regime” and “rare regime” consistently; reserve “old/new” for equations.
- Correct “These can included” to “These can include,” “cush” to “such,” and “three-dimension” to “three-dimensional.”

**AUTHOR CONFIRMATION REQUIRED — table note after protocol reconciliation:**

> The update strategies use [baseline identifiers], [partitions], [budgets], and [selection rules]. Differences in trainable layers, historical-data exposure, regularization, and tuning effort are listed explicitly. Results from different baseline or evaluation configurations are reported separately.

## 14. What the later tracked-change builder should do

The simpler model should use this file as a controlled edit specification:

1. Preserve the source DOCX and create a derivative.
2. Apply the proposed title, abstract, methods, results, discussion, and conclusion replacements as Word tracked changes.
3. Add each “Comment to insert” as a Word comment anchored to the exact quoted anchor.
4. Do not silently invent missing counts, seeds, thresholds, or equations. Keep bracketed placeholders such as `[n]`, `[X]`, and `[partition]` visibly unresolved or flag them in comments.
5. Keep the edits focused on scope, reproducibility, controller definition, acceptance criteria, comparator fairness, uncertainty, cost, and lifecycle boundaries. Do not perform broad stylistic rewriting until those issues are resolved.
6. Validate the output as an OOXML package and verify that accepted and rejected projections preserve the intended text.

## 15. Current review-package state and next gate

The September 9 source and the PI derivative are both present in this directory. The source remains the authority for any future revision. The derivative has 29 comments total: 20 retained from the source and nine new PI comments (IDs 210–218). Its comment ranges, references, and revision elements are structurally paired. The derivative contains two additional tracked replacements: the abstract scope is narrowed to a controlled adaptive-replay update strategy, and the unsupported simulation-cost acceptance claim is reframed as a separately reported cost item.

The next review pass should be evidence reconciliation, not another broad prose pass. Before accepting the numerical conclusions, obtain the split manifest, executed controller configuration or code, model/protocol identifiers for Figures 3–5, seed and run counts, raw metric outputs, and any measured cost data. If those artifacts are unavailable, retain the conservative wording and label the results exploratory.

## 16. Eight consolidated comments for the Word review

The nine PI comments can be presented to the author as these eight actions:

1. **Scope and novelty (comment 210):** Narrow the title, abstract, objective, and conclusion to the demonstrated offline adaptive-replay update study, and state the novelty boundary relative to existing replay scheduling methods.
2. **Data provenance and regime definition (comments 211–212):** Add run-level split counts and the split manifest; keep complete trajectories together; document threshold scope and the retrospective Mass90 definition; do not equate response-defined rarity with an operational shift.
3. **Controller reproducibility (comment 213):** Rebuild the equations from the executed implementation, define every parameter and decision rule, and identify what was frozen before final-test evaluation.
4. **Acceptance contract (comment 214):** Reconcile the 5%, 25%, and 30% examples with the 1.05×/0.80× criteria, or label them as illustrative sensitivity scenarios and remove redeployment conclusions based on them.
5. **Results and uncertainty (comment 215):** Identify validation versus final-test results, independent run counts, seeds, metric definitions, and paired uncertainty; treat representative maps and single-seed values as exploratory evidence.
6. **Cost and comparator fairness (comments 216 and 218):** Remove unsupported efficiency claims or add measured costs, and make update budgets, trainable layers, tuning rules, and starting checkpoints comparable across Models B–E.
7. **Adaptive-controller interpretation (Section 9):** Because the displayed replay ratio reaches its cap, add a matched fixed-replay-at-cap comparison or soften the claim that adaptation itself reduces manual tuning.
8. **Lifecycle and deployment boundary (comment 217):** Separate the demonstrated offline update component from proposed monitoring, uncertainty triggers, observation assimilation, online maintenance, and redeployment workflow.

## Evidence and limits

The repository history supports the central scope boundary: the strongest defensible paper is a controlled rare-regime/adaptive-replay UPDATE study, not validation of the full seven-step governance, monitoring, calibration, and deployment framework. The current repository does not contain the experiment code, split manifest, seed logs, raw metrics, or scripts needed to verify the manuscript's numerical results. The detailed recommendations above therefore distinguish text that can be improved immediately from claims that require new evidence or explicit relabeling as exploratory.

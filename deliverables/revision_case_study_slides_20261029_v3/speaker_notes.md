## 1. The revision connects the planned cycle to a controlled update case

The update supplies offline evidence for the middle of the lifecycle; it does not complete an operational cycle.

The original plan was to demonstrate a change in conditions, detect consequential degradation, justify and prepare an update, retain historical performance, calibrate uncertainty, and independently review deployment. The updated report now maps an existing controlled U-Net study onto that plan. MONITOR has baseline aggregates; DETECT is a retrospective response label; DECIDE uses an illustrative screen; PREPARE is regime-selected; UPDATE has the strongest reported evidence. None of those labels establishes operational monitoring or an approved decision record. CALIBRATE and DEPLOY remain requirements. This is the report revision contribution, not a claim of new experiments.

Source: Revised report §§2.2, 5.9.

## 2. The case study tests adaptation to rare plume changes

Mass90 uses reference states at t and t + 1. Rare-case learning and historical replay form the controlled update.

The reported case is a pump-and-treat U-Net on a 128 × 100 grid with 1–5 extraction wells and a dataset described as 10,000 physics simulations. Pumping input is represented through Thiem preprocessing. Time is kept indexed because older descriptions disagree on days versus years. Historical cases are the bottom 40% of the Mass90 size-change response score, with cutoff 0.133; rare cases are the top 3%, starting at 0.329. This score requires the reference next state and is not a prospective warning signal. It can miss plume translation that leaves the footprint size unchanged. Rare cases and historical replay define the update problem; trajectory splits, middle-57% handling, controller exposure, and active-learning selection are not verified. Direct manuscript anchors: P0008–P0024 and Eq. (1), P0063–P0066. Mass90 is the number of cells enclosing 90% of reference mass, not a distance traveled by the plume.

Source: Revised report §§5.1–5.5; manuscript Fig. 1.

## 3. The rare-case example locates the baseline prediction error

Reference concentration, static U-Net prediction, and prediction-minus-reference error in one reported example.

This is a faithful crop of the original manuscript rare-regime triplet. The caption identifies the reference as the full-order physics field and the prediction as the static U-Net result. All pixels, original labels, axes, aspect ratio, and colorbars are preserved; this is not a numerical replot. Concentration ranges to 813.6 µg/L and signed error spans ±169.4 µg/L in the displayed source. The field shows localized residual structure around the plume. No sample identifier or raw arrays accompany it, so this is illustrative of the physical error mechanism and not an independently verified distributional result. Historical and rare source panels use different scales; only the internally consistent rare triplet is shown. No synthetic plume or recolored pixel-derived field has been created. Direct manuscript anchors P0137–P0140 locate residuals around plume bodies, gradients, and boundaries. This supports showing where error occurs; it does not establish a universal failure mechanism from one case.

Source: Manuscript Fig. 2(b), rare-regime triplet; source crop.

## 4. Rare-regime recovery comes with a historical-retention tradeoff

Fixed replay changes historical/rare RMSE from 0.58/10.04 to 1.03/1.21 µg/L; update configurations also differ in trainable layers.

Compare both objectives: baseline 0.58/10.04, simple fine-tuning 1.11/3.92, fixed replay 1.03/1.21, and EWC 5.45/1.22 µg/L. Fixed replay has lower errors than simple fine-tuning or EWC in this particular comparison, while remaining worse than the baseline on historical conditions. It reduces rare RMSE by 87.9% and raises historical RMSE by 77.6%. Supporting rare-plume metrics change from 32.30 to 1.82% for mass, 14.20 to 3.43% for peak, and 7.11 to 1.89% for Mass90. Exact normalization requires code. The ambiguous historical plume-metric column is omitted. No line between points is drawn because training trajectories are unavailable. The Figure 3 full-network 0.64/0.99 pair is not pooled here because Model C and protocols remain unresolved. Direct manuscript anchors: P0146–P0150 and Figure 4. Table 1 (P0042, P0047, P0052) lists last-decoder/output updates for simple fine-tuning and full-network updates for replay/EWC; this does not isolate replay as the sole cause. EWC means elastic weight consolidation.

Source: Manuscript Fig. 4; revised report Table 10.

## 5. Rare-plume recovery extends to mass, peak, and footprint errors

Fixed replay and EWC have similar rare-plume errors, while their historical RMSE differs sharply.

This panel follows the RMSE comparison and keeps the exact same four Figure 4 configurations. Reported mass / peak / Mass90 errors are baseline 32.30 / 14.20 / 7.11%, simple fine-tuning 9.86 / 7.70 / 3.59%, fixed replay 1.82 / 3.43 / 1.89%, and EWC 1.88 / 3.40 / 1.64%. Direct manuscript anchors P0123–P0124 define the physical quantities, and P0146–P0150 with Figure 4 supply the results. Fixed replay and EWC have similar rare physical errors despite very different historical RMSE, so physical recovery alone cannot resolve historical retention. Mass90 denotes a footprint cell count containing 90% of mass, not spatial overlap or plume translation. These are rounded aggregate source labels without replicate uncertainty. The three panels use separately labeled linear axes. Metric normalization and aggregation require the executed code. The ambiguous historical physical-metric column is excluded. Proposed center-of-mass and exceedance-area metrics are mentioned in Methods but have no reported numerical results; they are not plotted. No compliance-well or remedy performance outcome is inferred.

Source: Manuscript Fig. 4(a); revised report Table 11.

## 6. Adaptive replay adjusts the training mix using validation feedback

The reported trajectory reaches r = 0.8 for most epochs; a matched fixed-ratio control is needed to isolate scheduling benefit.

Direct manuscript evidence: P0063–P0066 defines the mixed update batch as r B_old + (1−r) B_new, with historical low-change examples and rare high-change examples. This diagram represents the reported controller structure, not a complete executable specification. P0077–P0081 defines historical forgetting as updated historical validation RMSE divided by baseline historical validation RMSE, minus one, evaluated on the same historical validation set. The threshold controller increases replay above an upper forgetting tolerance; it decreases replay only when forgetting is below a lower tolerance AND rare validation loss is improving. This precise condition is narrower than general motivation language in P0075. The loss-balanced variant uses normalized historical and rare validation losses (P0097–P0103); its Eq. (5), P0093, is incomplete, so no repaired formula or parameter values are invented. Validation drives feedback; final-test performance is outside this loop (Table 2, P0111–P0116). Figure 5(a), discussed at P0152–P0156, shows the adaptive ratio reaching its cap r = 0.8 for most of 100 plotted epochs. The sampled historical exposure is not independently verified from logs. These results support studying the allocation tradeoff, but cannot by themselves attribute improvements to adaptive scheduling rather than high replay. The next test needs a fixed-ratio-0.8 control with matched initialization, seeds, update budget, and exposure accounting.

Source: Manuscript Eq. (1), adaptive-replay methods, Table 2, and Fig. 5(a).

## 7. An explicit screen retains two controller outcomes for further evaluation

The 30% / 85% limits are illustrative. The two passing outcomes clear the rare-improvement limit by only 0.8 and 0.5 points.

This is a separate Figure 5 controller comparison. Fixed replay is 80.4/88.9%, threshold adaptive forgetting 26.5/85.8%, loss-balanced 21.1/85.5%, and loss-balanced with floor 38.1/87.3%, where coordinates are historical increase and rare reduction. The shaded region meets historical increase ≤30% and rare reduction ≥85%. The two passing variants are candidates under this illustrative screen, not approved deployments. Historical margins are 3.5 and 8.9 points; rare margins are 0.8 and 0.5 points. Replicate uncertainty is absent, so significance or robustness cannot be inferred. Figure 4 fixed-replay changes 77.6/87.9 differ from Figure 5 80.4/88.9; keep those comparisons separate until denominators, splits, and executed configurations are reconciled. Direct manuscript anchors: P0152–P0156 and Figure 5. Methods P0126 instead illustrates 5% historical degradation and 20% rare improvement, while Figure 3 uses 25% historical tolerance. Thus Figure 5 is used as a panel-specific illustrative screen, not a preregistered contract.

Source: Manuscript Fig. 5; revised report Table 9.

## 8. The evidence stops before calibration and final validation

Controller selection, uncertainty calibration, and the final test require distinct data roles and evidence records.

The report reaches a defensible result: retain two controller outcomes for further evaluation, then hold for missing evidence. There are no predictive intervals, calibrated coverage/width results, independent calibration parameters, untouched final-test record, checkpoint identity, or versioned promotion decision for these outcomes. The figure labels required roles rather than claiming verified independent partitions. A deterministic model could use residual-based conformal calibration when suitable data and assumptions exist; coverage is not inferred from RMSE. This is an offline evidence assessment, not an operational rollback event. If an operational incumbent becomes invalid, withdrawal and governed retraining policy applies. Direct manuscript Table 2, P0104–P0116, distinguishes validation feedback from final testing, but the executed split identities are not supplied. Missing interval results are not supplied by deterministic RMSE.

Source: Revised report §§5.7–5.9.

## 9. The next demonstration must connect a known change to a validated update

Planned next test: a known change, ordered evidence, a frozen decision rule, matched updates, and independent validation.

Return to the original demonstration purpose. First resolve the time axis and trajectory manifest and archive executed configurations and predictions. Define a known controlled change, evaluate the detector prospectively on ordered trajectories, and freeze thresholds and an acceptance contract before final testing. Compare adaptive scheduling with fixed replay at r = 0.8 under matched seeds, update budget, and historical/new exposure; the displayed adaptive trajectory reaches that cap, which alone cannot isolate scheduling benefit. Calibrate independently and evaluate an untouched final test once, then record model version and reviewer decision. The diagram is an experiment plan, not an achieved result. Field deployment and long-duration monitoring remain subsequent validation, and no cost/speedup or active-learning gain is claimed.

Source: Revised report §5.10; analysis specification; original trigger/UQ plan.

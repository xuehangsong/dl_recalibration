# Section 5 version and legacy-content disposition

**Frozen current version:** `drafts/final/section5_FINAL_20261008_FROZEN.md`
**Current convenience copy:** `drafts/final/section5_FINAL.md` (matches the frozen snapshot; do not edit in place)
**Matching copy:** `drafts/section5_yilin_results_update_draft.md`
**Earlier source versions:** `analyses/seven_step_lifecycle_20261007/section5_before_full_rewrite.md` and `drafts/backup/section5_case_study_REVISED.md`

## Version rule

The frozen file is read-only for future drafting. Any further revision must be written to a new, dated file. The current working file should not be edited in place after this freeze.

## Legacy content disposition

| Earlier Section 5 content | Disposition | Reason |
|---|---|---|
| U-FNO/PFLOTRAN prototype description | Preserve in the earlier source and future-prototype archive; do not restore to the current case-study section | The current quantitative lifecycle evidence is the pump-and-treat U-Net. The user asked to remove FNO from this section for now. |
| Generic validation and governance criteria | Preserve in Sections 3 and 5 where they define gates | These criteria are still needed: site-specific error limits, near-90% UQ coverage, spatial/temporal consistency, boundary-bias checks, held-out final validation, audit trail, and rollback. |
| U-Net setup details | Retain selectively if needed in the prototype-context subsection | The current section keeps the verified grid, wells, runs, snapshots, Thiem input, and concentration prediction. Additional architecture details should be added only when their source and relevance are clear. |
| Related package's 70/15/15 split and autoregressive rollout | Keep as contextual archive only until the adaptive-replay split and protocol are verified | Do not present the older package split as Yilin's current train/validation/test evidence. |
| Drift-injection scenario and complete-cycle plan | Preserve as planned future-work or implementation-roadmap content | These are design concepts, not executed results in the adaptive-replay evidence package. |
| MAE, cost, speedup, and targeted-run evaluation plan | Preserve as framework evaluation requirements/targets | The current study reports point-prediction and plume metrics, not a complete MAE, cost, speedup, or active-learning campaign. |
| Three operational modes | Retain in the current Section 5.10 | The comparison remains useful for evaluating the lifecycle's value, provided it is presented as an evaluation design unless measured. |
| Statements claiming a complete executed lifecycle or deployment | Do not restore as findings | The available evidence ends at the CALIBRATE/DEPLOY hold. |

The earlier text is therefore preserved, but it should not be merged back wholesale. The current section should remain the reader-facing quantitative U-Net lifecycle narrative.

# Handoff: Trigger, UQ, and Prototype Workflow Evaluation Categories

Date: 2026-06-11

## Purpose

This handoff summarizes the review and synthesis completed for extending the final report so that the pump-and-treat U-Net prototype can demonstrate the recalibration workflow. The focus was to clarify what criteria should trigger recalibration evaluation and uncertainty quantification (UQ) recalibration, and how those criteria should be organized for the prototype demonstration.

## Source Material Reviewed

The discussion was aligned primarily with:

- `drafts/final/section2_2_FINAL.md` — seven-step recalibration workflow:
  1. MONITOR
  2. DETECT
  3. DECIDE
  4. PREPARE
  5. UPDATE
  6. CALIBRATE
  7. DEPLOY
- `drafts/final/section5_FINAL.md` — prototype demonstration, especially:
  - U-Net surrogate for 2D pump-and-treat plume prediction
  - controlled drift injection through pumping-regime change
  - complete recalibration demonstration plan
  - evaluation through accuracy, UQ calibration, computational efficiency, and governance documentation

## Main Conclusion

The criteria should not be presented only as a generic list of monitoring metrics. Because the report is being extended to use the pump-and-treat U-Net prototype to demonstrate the workflow, the criteria should be organized as **workflow-aligned evaluation categories**.

This term is clearer than “groups.” Each evaluation category is a distinct type of evidence or decision criterion used by the prototype workflow. Some categories provide trigger evidence for recalibration or UQ recalibration; others define how the triggered response is prepared, validated, and documented.

## Recommended Table Title

**Workflow-aligned evaluation categories and trigger criteria for the pump-and-treat U-Net prototype**

## Recommended Combined Table

| Evaluation category | Prototype criterion | Pump-and-treat examples | Trigger / evaluation role | Workflow connection | Response |
|---|---|---|---|---|---|
| **Operating-envelope change** | System moves outside the training domain | Pumping rate outside range; added/removed/relocated wells; active well count outside 1–5; changed pumping schedule; changed boundary conditions | Recalibration evaluation trigger | DETECT → DECIDE → PREPARE | Use as controlled drift scenario; likely Pathway B with targeted physics simulations |
| **Prediction and plume accuracy** | Concentration or plume geometry degrades | RMSE/MAE; bias; monitoring-well residuals; residual maps; plume-front error; plume-area mismatch; threshold false negatives | Recalibration evaluation trigger | MONITOR → DETECT → DEPLOY | Fine-tune if persistent; validate restored plume accuracy before deployment |
| **Remediation performance** | Surrogate misrepresents pump-and-treat effectiveness | Capture-zone mismatch; plume escape; cumulative mass-removal error; breakthrough timing/peak error at extraction wells | High-priority recalibration trigger | DETECT → DECIDE → DEPLOY | Use as strongest evidence that degradation affects operational decision quality |
| **Uncertainty reliability** | UQ is miscalibrated or not decision-useful | 90% coverage failure; reliability diagram error; uncertainty too narrow/wide; uncertainty inflation; high uncertainty near wells, plume front, source zone, or compliance boundary | UQ recalibration trigger | MONITOR → CALIBRATE → DEPLOY | Recalibrate intervals; use uncertainty maps for active learning and deployment acceptance |
| **Early-warning drift** | Statistical signs indicate emerging failure before large errors appear | Input/latent drift; increasing residual variance; lag-1 autocorrelation; skewness/kurtosis; spatial clustering; slow recovery after pumping change | WARNING trigger | MONITOR → DETECT → DECIDE | Increase monitoring; escalate only if persistent or confirmed by accuracy/UQ metrics |
| **Active-learning selection** | New simulations target the highest-value cases | Scenarios ranked by uncertainty, residuals, plume-front mismatch, decision-critical locations, and new pumping regime | Triggered-response criterion | PREPARE | Select limited targeted physics runs, e.g., 6–10 simulations, and assemble update dataset with replay buffer |
| **Update and deployment success** | Recalibration restores model reliability without forgetting old regimes | Before/after accuracy; plume/capture metrics; mass-removal error; breakthrough timing; UQ coverage recovery; old-regime validation | Deployment acceptance criterion | UPDATE → CALIBRATE → DEPLOY | Deploy, repeat update with expanded data, or escalate to full retraining |
| **Governance record** | Update is justified, approved, validated, and auditable | Trigger evidence package; DECIDE rationale; selected pathway; data provenance; calibration parameters; validation report; model version record | Governance criterion | DECIDE → DEPLOY | Document why the update was approved and whether it passed acceptance criteria |

## Meaning of the Evaluation Categories

The categories are not separate models or separate experiments. They are evidence/decision categories used to organize the prototype demonstration.

| Evaluation category | Plain-language meaning | Question answered |
|---|---|---|
| Operating-envelope change | The pump-and-treat system is being used under conditions different from training | Are we asking the surrogate to extrapolate? |
| Prediction and plume accuracy | The surrogate's plume concentration or geometry predictions are degraded | Is the model still predicting the plume correctly? |
| Remediation performance | Errors affect remediation decisions, not just numerical accuracy | Would the surrogate lead to the wrong pump-and-treat decision? |
| Uncertainty reliability | Prediction intervals or uncertainty maps are no longer trustworthy | Can we trust the confidence attached to predictions? |
| Early-warning drift | Statistical signals show possible emerging failure | Are there early signs of degradation? |
| Active-learning selection | The workflow chooses the most informative new simulations | If new simulations are needed, which should be run? |
| Update and deployment success | The updated model is checked before operational use | Did recalibration work and is deployment justified? |
| Governance record | Decisions are documented and auditable | Can we justify the trigger, update, calibration, and deployment? |

## How the Table Supports the Seven-Step Workflow

- **MONITOR**: tracks residuals, plume behavior, UQ metrics, and early-warning drift signals.
- **DETECT**: identifies whether monitored signals exceed thresholds or show persistent degradation.
- **DECIDE**: reviews evidence, determines whether recalibration is warranted, and selects the update pathway.
- **PREPARE**: uses active learning to select targeted physics simulations or assemble observation-driven update data.
- **UPDATE**: fine-tunes the surrogate using continual learning and replay to avoid forgetting.
- **CALIBRATE**: recalibrates prediction intervals and uncertainty outputs.
- **DEPLOY**: validates the updated model against acceptance criteria and records the governance/audit trail.

## Suggested Introductory Text for Report

> Table X combines trigger criteria with workflow demonstration objectives for the pump-and-treat U-Net prototype. Each evaluation category represents a distinct type of evidence used by the prototype workflow. The first five categories define the monitoring and detection evidence used to decide whether recalibration or uncertainty recalibration is warranted. The final three categories define how the triggered response is prepared, validated, and documented: active learning selects targeted physics simulations, continual learning updates the surrogate, post-hoc calibration restores uncertainty reliability, and deployment occurs only if acceptance criteria are met and documented.

## Suggested Follow-up Text After Table

> This structure allows the prototype to demonstrate more than predictive accuracy. Operating-envelope and residual criteria exercise MONITOR and DETECT; remediation-performance criteria provide decision-relevant evidence for DECIDE; UQ reliability criteria exercise CALIBRATE; active-learning criteria exercise PREPARE; update-effectiveness criteria exercise UPDATE and DEPLOY; and governance criteria ensure that each transition is documented and auditable.

## Recommended Next Step

In the report extension, insert the combined table into Section 5 near the case study design/evaluation approach, likely after the drift injection plan or before the recalibration demonstration plan. This placement will make clear that the pump-and-treat U-Net prototype is being used not only to test predictive accuracy, but to demonstrate the complete governed recalibration workflow.

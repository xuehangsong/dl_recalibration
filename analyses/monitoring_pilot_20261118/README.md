# One-snapshot warning of large plume-footprint changes

This offline diagnostic uses archived eSTOMP outputs from the original synthetic 2-D pump-and-treat case. At snapshot 2 the detector sees observations from snapshots 1 and 2. Retrospective scoring uses snapshot 3. Each realization contributes exactly one example.

## Inputs and chronology

The frozen data source is `/rcfs/projects/optimize_pt/ml_test/dataset_6/snap_output.joblib`. The original `dvz_optimization/unet_ms/2d/2d_model/dataset_6_combine_2.py` stores snapshots in four blocks of 10,000 case IDs each. Its local SHA-256 was `52e6b3fd0695552f2793463f137009884123109c43b749712e55eedd1eb2c0b3`. The analysis checked all three used time indices against individual per-case plume files for IDs 0, 4999 and 9999. The processed concentrations were finite and nonnegative. Equal-volume cells and uniform porosity permit computing relative mass fractions from concentrations. The time unit is one archived snapshot interval.

The monitoring locations are zero-based (x,y) indices on the 128 × 100 grid, the Cartesian product of x = 16, 48, 80, 112 and y = 12, 37, 62, 87. Observations are exact cell concentrations with no added noise. The primary score is the RMS of the 16 local changes. The full-field comparator uses the absolute relative change in the smallest number of grid cells enclosing 90% of the concentration sum. The future event uses the same footprint definition over the next interval. This common definition favors detection of persistent footprint dynamics by the comparator.

The companion `ensemble_footprints.npz` file aggregates the fraction of cases containing each cell in that 90%-mass footprint. For the 142 event cases, the mean footprint contracts from 572 to 353 cells, or 38.3%. For the other 4,858 evaluation cases, it contracts from 914 to 782 cells, or 14.4%. The plotted occupancy maps are retrospective group summaries. They explain the event label and are not spatial uncertainty intervals for the U-Net.

## Frozen pilot design

A seeded permutation of case IDs splits 10,000 trajectories equally between reference and evaluation. The reference set's 97th percentile of future change defines the event cutoff for this interval (0.3429973). Each rule raises an alarm when its score exceeds the reference non-event 95th percentile. Signal direction, sites, time window, and thresholds were specified by the same script before submission. The evaluation subset was used once for this pilot. Afterward, event direction and median sensor scores were inspected to interpret the result. A revised signal or layout would need a fresh evaluation.

## Execution and reproduction

Slurm job 1595201 ran on one Deception CPU in the short partition. Its durable working directory is `/qfs/people/song884/dl_recalibration_runs/monitoring_20261118_pE9sv6`. Source and input hashes are in `inputs.sha256`. Resource allocation at launch, final scheduler status, wrapper exit, and output hashes are retained here. Scientific status is exploratory. This checks warning of a simulated plume-change event. Evaluating recalibration need requires pairing each alert with a surrogate prediction error and update outcome.

To reproduce, copy `evaluate.py` and `run.sbatch` to a new run folder on Deception and submit the batch file there. The wrapper selects the interpreter and hashes the source data. `case_scores.csv` contains one row per case with its partition, footprint counts, scores, and future label. The meeting-brief builder independently recomputes the thresholds, counts and rank-based ROC areas from those rows.

## Sensor placement and threshold sensitivity

The original grid, central grid, and perimeter grid all use the RMS concentration change from snapshot 1 to snapshot 2. Job 1595631 verified the original score for every case, its threshold and its confusion counts. At each layout's reference non-event 95th percentile, the central layout detected 105/142 contractions with 261 false alarms and the perimeter layout produced zero alerts. We chose these two layouts after seeing the original maps and reused the same evaluation split. The strict greater-than rule matters because the perimeter threshold was zero. The layout coordinates, thresholds and counts are in `layout_comparison.json`, and `layout_scores.npz` retains the case-level values. An earlier exploratory run (1595492) used the outcome interval for its scores and was excluded. The recomputed layout scores and Slurm records are from `/qfs/people/song884/dl_recalibration_runs/layout_final_o2Pikw`.

Run `threshold_sensitivity.py` locally to reproduce the four operating points from the original frozen scores. Moving the full-field reference non-event percentile from 95 to 99 reduced false alarms from 230 to 36, while detections fell from 140 to 93. The spread grid missed all contractions at each of the four thresholds.

## U-Net forecast error one snapshot after the alarm

Job 1595535 in `/qfs/people/song884/dl_recalibration_runs/snapshot3_bZhyCS` reconstructed the two successive random splits (seed 42) used by dataset 6's original `train_2_1.py`. From its 6,000 held-out rows, 1,491 forecast snapshot 3. The checkpoint takes the Thiem head and observed snapshot-2 concentration as input. We checked the input concentration against the previous eSTOMP field for every scored row. The checkpoint reproduced stored predictions on 16 rows spanning the file (largest relative L2 difference 2.83e-7, smallest difference under a one-row rotation of probes 0.272). We therefore used the archived predictions. RMSE uses the 128 × 100 cells of the physical grid with original concentrations in µg/L. Each forecast is one step ahead from a simulated state.

The existing pilot split yields 758 paired reference and 733 paired evaluation cases. High error means RMSE at or above the paired reference 95th percentile, 1.16365 µg/L. We reused each existing monitoring threshold without fitting it to error. Of the 733 evaluation snapshot rows, 716 had a different snapshot of the same trajectory in the original model training set. The study measures error association for one forecast interval on the archive. Update benefit on these alerts and transfer to unseen trajectories remain open.

To reproduce, stage `paired_unet_error.py`, `paired.sbatch`, `case_scores.csv`, and the original `dvz_optimization/data_driven/unet_2d_customized_2_5.py` in a fresh Deception run folder. The layer hash is in `paired_inputs.sha256`. Submit the batch file there. The original split and padding are documented in `dvz_optimization/unet_ms/2d/2d_train/train_2_1.py`. The companion output `paired_cases.csv` records case ID, prediction-row index, eSTOMP target row, partition, overlap with training and unpadded RMSE. The local meeting figure builder verifies both output manifests and joins those errors to the saved scores by case ID.

For source provenance, the local `dvz_optimization` revision was `6d4bf860286d3bba482593826cd512ff681ff20e`. The SHA-256 of its training script was `c08286f216cd8f05dd6db2538742d52f0392cf8abf192945a2649c8dca78c90b`. The paired figure uses the concentration units in that study’s `unet_ms/2d/2d_plot/plot_prediction.py`.

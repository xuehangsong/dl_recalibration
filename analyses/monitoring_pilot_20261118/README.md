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

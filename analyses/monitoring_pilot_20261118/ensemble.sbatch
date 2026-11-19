#!/bin/bash
#SBATCH --account=optimize_pt
#SBATCH --partition=short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G
#SBATCH --time=00:20:00
#SBATCH --job-name=plume-ensemble
set -eu
exec > ensemble_wrapper.log 2>&1
trap 'echo $? > ensemble_wrapper.exit' EXIT
export PYTHONNOUSERSITE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
unset PYTHONPATH
py=/qfs/people/song884/.conda/envs/decep2551/bin/python
scontrol show job "$SLURM_JOB_ID" > ensemble_allocation.txt
sha256sum compute_ensemble.py ensemble.sbatch case_scores.csv /rcfs/projects/optimize_pt/ml_test/dataset_6/snap_output.joblib > ensemble_inputs.sha256
"$py" compute_ensemble.py
sha256sum ensemble_footprints.npz ensemble_metadata.json > ensemble_outputs.sha256

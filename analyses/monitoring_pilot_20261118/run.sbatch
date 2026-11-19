#!/bin/bash
#SBATCH --account=optimize_pt
#SBATCH --partition=short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=8G
#SBATCH --time=00:30:00
#SBATCH --job-name=plume-warning
set -eu
exec > wrapper.log 2>&1
trap 'echo $? > wrapper.exit' EXIT
export PYTHONNOUSERSITE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1
unset PYTHONPATH
py=/qfs/people/song884/.conda/envs/decep2551/bin/python
scontrol show job "$SLURM_JOB_ID" > allocation.txt
sha256sum evaluate.py run.sbatch /rcfs/projects/optimize_pt/ml_test/dataset_6/snap_output.joblib > inputs.sha256
"$py" evaluate.py
sha256sum result.json case_scores.csv > outputs.sha256

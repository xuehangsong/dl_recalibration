#!/bin/bash
#SBATCH --account=optimize_pt
#SBATCH --partition=short
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=20G
#SBATCH --time=01:00:00
#SBATCH --job-name=snapshot3-error
set -eu
exec > paired_wrapper.log 2>&1
trap 'echo $? > paired_wrapper.exit' EXIT
export PYTHONNOUSERSITE=1 OPENBLAS_NUM_THREADS=1 TF_NUM_INTRAOP_THREADS=8 TF_NUM_INTEROP_THREADS=1 CUDA_VISIBLE_DEVICES=-1
unset PYTHONPATH
py=/qfs/people/song884/.conda/envs/decep2551/bin/python
data=/rcfs/projects/optimize_pt/ml_test/dataset_6
model=/qfs/people/song884/all_figures/unet_ms/Outputs/2d
scontrol show job "$SLURM_JOB_ID" > paired_allocation.txt
sha256sum paired_unet_error.py paired.sbatch case_scores.csv unet_2d_customized_2_5.py "$data"/snap_{input,output}.joblib "$model"/train_2_1_{model.h5,predictions.joblib} > paired_inputs.sha256
"$py" paired_unet_error.py
sha256sum paired_cases.csv pairing.json > paired_outputs.sha256

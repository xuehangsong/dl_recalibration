"""Measure next-snapshot error on the original U-Net snapshot-level test split."""
import csv
import json
from pathlib import Path

import joblib
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from unet_2d_customized_2_5 import DynamicLeakyClippedTanh

DATA = Path("/rcfs/projects/optimize_pt/ml_test/dataset_6")
MODEL_DIR = Path("/qfs/people/song884/all_figures/unet_ms/Outputs/2d")
N = 10_000


def main():
    inputs = joblib.load(DATA / "snap_input.joblib", mmap_mode="r")
    truth = joblib.load(DATA / "snap_output.joblib", mmap_mode="r")
    saved = joblib.load(MODEL_DIR / "train_2_1_predictions.joblib", mmap_mode="r")
    assert inputs.shape == (4 * N, 128, 100, 2) and truth.shape == (4 * N, 128, 100, 1)
    train, tmp = train_test_split(np.arange(4 * N), test_size=0.30, random_state=42)
    _, test = train_test_split(tmp, test_size=0.5, random_state=42)
    assert saved.shape == (len(test), 128, 128, 1)
    positions = np.flatnonzero(test // N == 2)
    cases = test[positions] % N
    pilot = np.genfromtxt("case_scores.csv", delimiter=",", names=True, dtype=None, encoding="utf8")
    np.testing.assert_array_equal(pilot["case_id"], np.arange(N))

    # Match the training script's extrema after zero padding, including its use
    # of the input concentration bounds for the single output channel.
    lower, upper = np.zeros(2), np.zeros(2)
    for rows in np.array_split(np.sort(train), 140):
        batch = inputs[rows]
        lower = np.minimum(lower, batch.min(axis=(0, 1, 2)))
        upper = np.maximum(upper, batch.max(axis=(0, 1, 2)))
    assert np.all(np.isfinite([lower, upper])) and np.all(upper > lower)
    model = tf.keras.models.load_model(str(MODEL_DIR / "train_2_1_model.h5"),
                                       custom_objects={"DynamicLeakyClippedTanh": DynamicLeakyClippedTanh},
                                       compile=False)

    def predict(rows):
        x = np.pad(inputs[rows], ((0, 0), (0, 0), (14, 14), (0, 0)))
        pred = model(((x - lower) / (upper - lower)).astype("float32"), training=False).numpy()
        return pred * (upper[-1] - lower[-1]) + lower[-1]

    # Compare fresh predictions to distinct stored rows across the file, with a
    # wrong-row control. Direct inference supplies case IDs if the archive differs.
    probes = positions[np.linspace(0, len(positions) - 1, 16, dtype=int)]
    replica = predict(test[probes])
    stored = saved[probes]
    def relative_l2(a, b):
        return np.linalg.norm((a - b).reshape(len(a), -1), axis=1) / np.maximum(
            np.linalg.norm(b.reshape(len(b), -1), axis=1), 1.e-12)
    same = relative_l2(replica, stored)
    different = relative_l2(replica, np.roll(stored, 1, axis=0))
    assert np.isfinite([same, different]).all()
    use_archive = bool(same.max() < 1.e-4 and different.min() > 1.e-2)
    values = []
    for batch in np.array_split(positions, (len(positions) + 7) // 8):
        rows = test[batch]
        ids = rows % N
        np.testing.assert_array_equal(inputs[rows, :, :, 1], truth[N + ids, :, :, 0])
        prediction = saved[batch] if use_archive else predict(rows)
        difference = prediction[:, :, 14:-14, 0].astype(float) - truth[rows, :, :, 0]
        values.extend(np.sqrt(np.mean(difference ** 2, axis=(1, 2))))
    errors = np.array(values)
    assert np.isfinite(errors).all() and len(np.unique(cases)) == len(cases)
    other_train = np.isin(cases, train % N)
    with open("paired_cases.csv", "w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["case_id", "prediction_row", "archive_truth_row", "partition",
                         "other_snapshot_in_training", "snapshot3_rmse"])
        writer.writerows(zip(cases, positions, test[positions], pilot["partition"][cases],
                             other_train.astype(int), errors))
    metadata = dict(prediction_source="archived predictions" if use_archive else "fresh checkpoint inference",
                    probe_positions=probes.tolist(), correct_row_relative_l2=same.tolist(),
                    rotated_row_relative_l2=different.tolist(), input_min=lower.tolist(), input_max=upper.tolist(),
                    tensorflow=tf.__version__, numpy=np.__version__, held_out_snapshot3_rows=len(cases))
    Path("pairing.json").write_text(json.dumps(metadata, indent=2) + "\n")


if __name__ == "__main__":
    main()

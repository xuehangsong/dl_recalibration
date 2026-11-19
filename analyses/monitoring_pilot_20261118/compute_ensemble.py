"""Aggregate snapshot 2 and 3 Mass90 footprints using the pilot's frozen labels."""
from pathlib import Path
import json
import joblib
import numpy as np

SOURCE = Path("/rcfs/projects/optimize_pt/ml_test/dataset_6/snap_output.joblib")


def main():
    cases = np.genfromtxt("case_scores.csv", delimiter=",", names=True, dtype=None, encoding="utf8")
    evaluation = cases[cases["partition"] == "evaluation"]
    assert len(evaluation) == len(np.unique(evaluation["case_id"])) == 5000
    source = joblib.load(SOURCE, mmap_mode="r")
    assert source.shape == (40000, 128, 100, 1)
    maps = {}
    metadata = {}
    for label, event in [("event", 1), ("other", 0)]:
        group = evaluation[evaluation["event"] == event]
        assert len(group) == (142 if event else 4858)
        for snapshot in (2, 3):
            key = f"{label}_t{snapshot}"
            counts = np.zeros(source.shape[1:3], dtype=float)
            ties = 0
            sizes = group[f"size90_{snapshot}"]
            for case, size in zip(group["case_id"], sizes):
                field = source[(snapshot - 1) * 10000 + case, :, :, 0]
                # Use the previously verified footprint size; divide tied boundary
                # cells' remaining membership equally so grid ordering has no effect.
                boundary = np.partition(field.ravel(), -size)[-size]
                above = field > boundary
                equal = field == boundary
                remaining = size - above.sum()
                tied = equal.sum()
                assert 0 < remaining <= tied and boundary > 0
                mass = field.sum()
                selected_mass = field[above].sum() + remaining * boundary
                assert selected_mass >= .9 * mass - 1.e-9 and selected_mass - boundary < .9 * mass + 1.e-9
                counts += above + equal * (remaining / tied)
                ties += int(remaining < tied)
            maps[key] = counts / len(group)
            np.testing.assert_allclose(maps[key].sum(), sizes.mean())
            metadata[key] = dict(cases=len(group), mean_cells=float(sizes.mean()),
                                 cases_with_partial_boundary_ties=ties)
    np.savez_compressed("ensemble_footprints.npz", **maps)
    Path("ensemble_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")


if __name__ == "__main__":
    main()

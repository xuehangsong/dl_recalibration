"""Compare three fixed 16-location layouts on the frozen monitoring pilot split."""
from pathlib import Path
import json
import joblib
import numpy as np

DATA = Path("/rcfs/projects/optimize_pt/ml_test/dataset_6/snap_output.joblib")
N = 10_000

LAYOUTS = {
    "spread": ([16, 48, 80, 112], [12, 37, 62, 87]),
    "center": ([40, 56, 72, 88], [30, 40, 60, 70]),
    "perimeter": ([8, 40, 88, 120], [8, 20, 80, 92]),
}


def main():
    cases = np.genfromtxt("case_scores.csv", delimiter=",", names=True, dtype=None, encoding="utf8")
    reference = cases[ cases["partition"] == "reference" ]
    evaluation = cases[ cases["partition"] == "evaluation" ]
    event = evaluation["event"].astype(bool)
    source = joblib.load(DATA, mmap_mode="r")
    np.testing.assert_array_equal(cases["case_id"], np.arange(N))
    assert source.shape == (4 * N, 128, 100, 1)
    result = {}
    layout_scores = {}
    for name, (xs, ys) in LAYOUTS.items():
        scores = np.empty(len(cases), dtype=float)
        for row, case_id in enumerate(cases["case_id"]):
            field1 = source[int(case_id), :, :, 0]
            field2 = source[N + int(case_id), :, :, 0]
            scores[row] = np.sqrt(np.mean((field2[np.ix_(xs, ys)] - field1[np.ix_(xs, ys)]) ** 2))
        layout_scores[name] = scores
        ref_scores = scores[reference["case_id"]]
        ref_non_event = ref_scores[~reference["event"].astype(bool)]
        threshold = float(np.quantile(ref_non_event, .95))
        eval_scores = scores[evaluation["case_id"]]
        alarm = eval_scores > threshold
        tp = int(np.sum(alarm & event)); fp = int(np.sum(alarm & ~event))
        fn = int(np.sum(~alarm & event)); tn = int(np.sum(~alarm & ~event))
        if name == "spread":
            np.testing.assert_array_equal(scores, cases["sensor_rms"])
            assert threshold == 34.10210697009943
            assert (tp, fp, fn, tn) == (0, 229, 142, 4629)
        result[name] = dict(x=xs, y=ys, threshold=threshold, tp=tp, fp=fp, fn=fn, tn=tn,
                            sensitivity=tp/(tp+fn), false_alarm_rate=fp/(fp+tn),
                            precision=tp/(tp+fp) if tp+fp else None,
                            alerts=int(alarm.sum()))
    np.savez_compressed("layout_scores.npz", case_id=cases["case_id"], **layout_scores)
    Path("layout_comparison.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

"""One-step warning of large Mass90 footprint changes in the original 2-D eSTOMP case."""
import csv
import hashlib
import json
import platform
import sys
from pathlib import Path

import joblib
import numpy as np
from sklearn.metrics import roc_auc_score, average_precision_score

DATA = Path("/rcfs/projects/optimize_pt/ml_test/dataset_6")
N = 10000
X, Y = np.ix_([16, 48, 80, 112], [12, 37, 62, 87])


def mass90(field):
    ordered = np.sort(field.ravel())[::-1].clip(min=0)
    cumulative = np.cumsum(ordered, dtype=np.float64)
    if cumulative[-1] <= 0:
        raise ValueError("Empty plume")
    return int(np.searchsorted(cumulative, 0.9 * cumulative[-1]) + 1)


def evaluate(score, event, reference, test):
    limit = float(np.quantile(score[reference & ~event], .95))
    alarm = score[test] > limit
    truth = event[test]
    tp, fp = int(sum(alarm & truth)), int(sum(alarm & ~truth))
    fn, tn = int(sum(~alarm & truth)), int(sum(~alarm & ~truth))
    return dict(alarm_threshold=limit, tp=tp, fp=fp, tn=tn, fn=fn,
                sensitivity=tp/(tp+fn), false_alarm_rate=fp/(fp+tn),
                precision=tp/(tp+fp) if tp+fp else None,
                roc_auc=float(roc_auc_score(truth, score[test])),
                average_precision=float(average_precision_score(truth, score[test])))


def main():
    archive = joblib.load(DATA / "snap_output.joblib", mmap_mode="r")
    assert archive.shape == (4*N, 128, 100, 1)
    # Verify the combine script's block and case indexing against original fields.
    for case in (0, 4999, 9999):
        for step in (1, 2, 3):
            original = joblib.load(DATA / str(case) / f"plume_{step}.joblib")
            np.testing.assert_array_equal(archive[(step-1)*N+case,:,:,0], original)
    sizes = np.empty((N, 3), dtype=int)
    sensor = np.empty(N)
    lowest = np.inf
    for case in range(N):
        fields = [archive[t*N+case,:,:,0] for t in range(3)]
        for t, field in enumerate(fields):
            assert np.isfinite(field).all()
            lowest = min(lowest, float(field.min()))
            sizes[case,t] = mass90(field)
        sensor[case] = np.sqrt(np.mean((fields[1][X,Y] - fields[0][X,Y])**2))
    # Case assignment uses only IDs, independent of response and monitoring signal.
    ids = np.random.default_rng(20261118).permutation(N)
    reference = np.zeros(N, dtype=bool)
    reference[ids[:N//2]] = True
    test = ~reference
    lag_change = np.abs(sizes[:,1]-sizes[:,0])/sizes[:,0]
    future_change = np.abs(sizes[:,2]-sizes[:,1])/sizes[:,1]
    cutoff = float(np.quantile(future_change[reference], .97))
    event = future_change >= cutoff
    metrics = {name:evaluate(score,event,reference,test) for name,score in
               [('sparse_rms',sensor),('previous_full_field_mass90_change',lag_change)]}
    with open('case_scores.csv','w',newline='') as stream:
        writer = csv.writer(stream)
        writer.writerow(['case_id','partition','size90_1','size90_2','size90_3','sensor_rms','previous_change','next_change','event'])
        for i in range(N):
            writer.writerow([i,'reference' if reference[i] else 'evaluation',*sizes[i],sensor[i],lag_change[i],future_change[i],int(event[i])])
    result = dict(source=str(DATA/'snap_output.joblib'), python=sys.executable,
                  python_version=platform.python_version(),numpy=np.__version__,joblib=joblib.__version__,
                  shape=archive.shape, minimum_source_concentration=lowest,
                  event_cutoff=cutoff, reference_events=int(event[reference].sum()),
                  evaluation_events=int(event[test].sum()), evaluation_count=int(test.sum()),
                  reference_count=int(reference.sum()), metrics=metrics)
    Path('result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()

"""Relate snapshot-2 alarms to U-Net error on the original snapshot-3 test rows."""
import hashlib
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent
PILOT = OUT.parents[1] / "analyses/monitoring_pilot_20261118"


def main():
    for manifest in ("outputs.sha256", "layout_outputs.sha256", "paired_outputs.sha256"):
        for line in (PILOT / manifest).read_text().splitlines():
            digest, filename = line.split()
            assert hashlib.sha256((PILOT / filename).read_bytes()).hexdigest() == digest
    def table(name):
        return np.genfromtxt(PILOT / name, delimiter=",", names=True, dtype=None, encoding="utf8")
    base = table("case_scores.csv")
    paired = table("paired_cases.csv")
    cases = paired["case_id"]
    assert len(np.unique(cases)) == len(cases)
    np.testing.assert_array_equal(paired["archive_truth_row"], 20000 + cases)
    np.testing.assert_array_equal(paired["partition"], base["partition"][cases])
    error = paired["snapshot3_rmse"]
    ref = paired["partition"] == "reference"
    ev = paired["partition"] == "evaluation"
    assert (ref ^ ev).all()
    cutoff = float(np.quantile(error[ref], .95))
    high = error >= cutoff
    layout = json.loads((PILOT / "layout_comparison.json").read_text())
    benchmark = json.loads((PILOT / "result.json").read_text())["metrics"]["previous_full_field_mass90_change"]
    with np.load(PILOT / "layout_scores.npz") as loc:
        np.testing.assert_array_equal(loc["case_id"], base["case_id"])
        np.testing.assert_array_equal(loc["spread"], base["sensor_rms"])
        rules = [(label, loc[key] > layout[key]["threshold"])
                 for label, key in (("Original 16 sites", "spread"), ("Central 16 sites", "center"))]
    rules.append(("Full-field footprint", base["previous_change"] > benchmark["alarm_threshold"]))
    stats = {"reference_n": int(ref.sum()), "evaluation_n": int(ev.sum()), "high_error_n": int((ev & high).sum()),
             "cutoff": cutoff, "other_training_snapshot_evaluation": int(paired["other_snapshot_in_training"][ev].sum()),
             "rules": {}}
    contraction = base["event"][cases].astype(bool) & ev
    stats["contraction_n"] = int(contraction.sum())
    stats["both_outcomes_n"] = int((contraction & high).sum())
    fig, (detection, ax) = plt.subplots(1, 2, figsize=(10, 3.65), layout="constrained")
    for row, (label, alarm) in enumerate(rules):
        selected = alarm[cases]
        groups = {}
        for flag, group, color in ((False, "No alarm", "#687983"), (True, "Alarm", "#ad5024")):
            mask = ev & (selected == flag)
            values = np.sort(error[mask])
            groups[group] = dict(n=len(values), median=float(np.median(values)), high=int(np.sum(high & mask)))
            if label == "Full-field footprint":
                ax.step(np.r_[0, values], np.arange(len(values) + 1) / len(values) * 100, where="post",
                        color=color, lw=2, label=f"{group} (n = {len(values)})")
        groups["contractions_detected"] = int((contraction & selected).sum())
        stats["rules"][label] = groups
        for mask, shift, color, marker, outcome in ((contraction, -.15, "#17677a", "o", "Contraction"),
                                                   (ev & high, .15, "#ad5024", "D", "High RMSE")):
            caught, total = int((mask & selected).sum()), int(mask.sum())
            pct = 100 * caught / total
            detection.scatter(pct, row + shift, c=color, marker=marker, s=32, label=outcome if row == 0 else None)
            detection.annotate(f"{caught}/{total}", (pct, row+shift), xytext=(6,0),
                               textcoords="offset points", va="center", fontsize=8)
    detection.set(xlim=(-5, 118), ylim=(2.6, -.65), xticks=[0,25,50,75,100],
                  yticks=range(len(rules)), yticklabels=[r[0] for r in rules], xlabel="Cases detected (%)")
    detection.legend(loc="upper center", bbox_to_anchor=(.50, 1.01), ncol=2, frameon=False, fontsize=8)
    ax.axvline(cutoff, color="#343a3d", lw=1, ls="--", zorder=0, label="High-error cutoff")
    ax.set(xlabel="Snapshot-3 RMSE (µg/L)", ylabel="Cumulative share of group (%)",
           xlim=(0, error[ev].max()*1.03), ylim=(-2,103))
    ax.legend(title="Full-field footprint rule", frameon=False, fontsize=8, title_fontsize=8, loc="lower right")
    for axis, letter in ((detection, "a"), (ax, "b")):
        axis.spines[["top", "right"]].set_visible(False)
        axis.set_title(letter, loc="left", fontweight="bold")
    for ext in ("pdf", "png"):
        fig.savefig(OUT / f"alarm_and_forecast_error.{ext}", dpi=200, bbox_inches="tight")
    plt.close(fig)
    (PILOT / "error_by_alarm.json").write_text(json.dumps(stats, indent=2) + "\n")


if __name__ == "__main__":
    main()

"""Exploratory alarm-threshold sensitivity on the frozen evaluation cases."""
from pathlib import Path
import json
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
PILOT = ROOT / "analyses/monitoring_pilot_20261118"


def main():
    data = np.genfromtxt(PILOT / "case_scores.csv", delimiter=",", names=True, dtype=None, encoding="utf8")
    reference = data[data["partition"] == "reference"]
    evaluation = data[data["partition"] == "evaluation"]
    truth = evaluation["event"].astype(bool)
    qs = [0.90, 0.95, 0.975, 0.99]
    output = {}
    for signal in ["sensor_rms", "previous_change"]:
        ref_non_event = reference[reference["event"] == 0][signal]
        rows = []
        for q in qs:
            threshold = float(np.quantile(ref_non_event, q))
            alarm = evaluation[signal] > threshold
            tp = int(np.sum(alarm & truth)); fp = int(np.sum(alarm & ~truth))
            fn = int(np.sum(~alarm & truth)); tn = int(np.sum(~alarm & ~truth))
            rows.append(dict(quantile=q, threshold=threshold, tp=tp, fp=fp, fn=fn, tn=tn,
                             sensitivity=tp/(tp+fn), false_alarm_rate=fp/(fp+tn),
                             precision=tp/(tp+fp) if tp+fp else None, alerts=int(alarm.sum())))
        output[signal] = rows
    (PILOT / "threshold_sensitivity.json").write_text(json.dumps(output, indent=2) + "\n")
    fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.7), constrained_layout=True)
    styles = [("sensor_rms", "16-location concentration change", "#b75b22"),
              ("previous_change", "Full-field footprint change", "#17677a")]
    for signal, label, color in styles:
        rows = output[signal]
        for ax, field in zip(axes, ("tp", "fp")):
            ax.plot([100*r["quantile"] for r in rows], [r[field] for r in rows],
                    color=color, marker="o", lw=2, label=label)
    for ax, ylabel in zip(axes, ("Contractions detected (of 142)", "False alarms (of 4,858)")):
        ax.set(xlabel="Reference non-event percentile", ylabel=ylabel, xticks=[90, 95, 97.5, 99])
        ax.grid(axis="y", color="#e1e7e8", lw=.7)
        ax.spines[["top", "right"]].set_visible(False)
    axes[0].legend(frameon=False, fontsize=8, loc="center left")
    fig.savefig(PILOT / "threshold_sensitivity.png", dpi=220, bbox_inches="tight")
    fig.savefig(PILOT / "threshold_sensitivity.pdf", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__": main()

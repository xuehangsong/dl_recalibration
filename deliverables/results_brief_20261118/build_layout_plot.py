"""Show the three 16-cell layouts against the event-group plume map."""
from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import numpy as np

ROOT = Path(__file__).resolve().parent
PILOT = ROOT.parents[1] / "analyses/monitoring_pilot_20261118"

def main():
    comparison = json.loads((PILOT / "layout_comparison.json").read_text())
    with np.load(PILOT / "ensemble_footprints.npz") as archive:
        background = 100 * (archive["event_t3"] - archive["event_t2"])
    fig, axes = plt.subplots(1, 3, figsize=(10.6, 3.55), sharex=True, sharey=True,
                             layout="constrained")
    layouts = [("Original · spread out", "spread"), ("Central · moved inward", "center"),
               ("Perimeter · outer sites", "perimeter")]
    for axis, (label, key) in zip(axes, layouts):
        row = comparison[key]
        xs, ys = row["x"], row["y"]
        image = axis.imshow(background.T, origin="lower", cmap="RdBu_r",
                            norm=Normalize(-65, 65), interpolation="nearest", aspect="equal")
        axis.scatter(*np.meshgrid(xs, ys), s=44, facecolors="white", edgecolors="#30393e",
                      linewidths=1.5, zorder=3)
        axis.set_title(label, fontsize=12)
        axis.set_xlabel(f"x cell index\n{row['tp']}/{row['tp']+row['fn']} contractions detected"
                        f"\n{row['fp']:,}/{row['fp']+row['tn']:,} false alarms")
        axis.set_xticks([0, 32, 64, 96, 127])
        axis.set_yticks([0, 25, 50, 75, 99])
        axis.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("y cell index")
    cbar = fig.colorbar(image, ax=axes, location="right", shrink=.82, pad=.02, ticks=[-60, -30, 0, 30, 60])
    cbar.set_label("Occupancy change (pp)")
    for extension in ("png", "pdf"):
        fig.savefig(ROOT / f"sensor_layout_comparison.{extension}", dpi=220, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()

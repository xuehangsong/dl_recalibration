"""Show the three 16-cell layouts on the plume map at the time of the warning."""
from pathlib import Path
import json

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np

ROOT = Path(__file__).resolve().parent
PILOT = ROOT.parents[1] / "analyses/monitoring_pilot_20261118"

def main():
    comparison = json.loads((PILOT / "layout_comparison.json").read_text())
    metadata = json.loads((PILOT / "ensemble_metadata.json").read_text())
    groups = ["event_t2", "other_t2"]
    counts = [metadata[group]["cases"] for group in groups]
    assert sum(counts) == 5000
    with np.load(PILOT / "ensemble_footprints.npz") as archive:
        # Recombine the two case groups to show all evaluation cases at the second saved time.
        background = np.average([archive[group] for group in groups], axis=0, weights=counts)
        mean_size = np.average([metadata[group]["mean_cells"] for group in groups], weights=counts)
        np.testing.assert_allclose(background.sum(), mean_size)
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.3), sharex=True, sharey=True,
                             layout="constrained")
    layouts = [("Spread across the grid", "spread"), ("Near the center", "center"),
               ("Toward the edges", "perimeter")]
    for axis, (label, key) in zip(axes, layouts):
        row = comparison[key]
        xs, ys = row["x"], row["y"]
        image = axis.imshow(background.T, origin="lower", cmap="Blues",
                            vmin=0, vmax=1, interpolation="nearest", aspect="equal")
        axis.scatter(*np.meshgrid(xs, ys), s=44, facecolors="white", edgecolors="#30393e",
                      linewidths=1.5, zorder=3)
        axis.set_title(label, fontsize=12)
        axis.set_xlabel(f"Grid column\n{row['tp']}/{row['tp']+row['fn']} large contractions detected"
                        f"\n{row['fp']:,}/{row['fp']+row['tn']:,} false alarms")
        axis.set_xticks([0, 32, 64, 96, 127])
        axis.set_yticks([0, 25, 50, 75, 99])
        axis.spines[["top", "right"]].set_visible(False)
    axes[0].set_ylabel("Grid row")
    cbar = fig.colorbar(image, ax=axes, location="bottom", shrink=.68, aspect=40, pad=.04, ticks=[0, .25, .5, .75, 1],
                        format=PercentFormatter(1, decimals=0))
    cbar.set_label("Cases with this cell inside the plume footprint at the time of sampling")
    for extension in ("png", "pdf"):
        fig.savefig(ROOT / f"sensor_layout_comparison.{extension}", dpi=220, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()

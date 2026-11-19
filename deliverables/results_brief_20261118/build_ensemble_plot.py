"""Map frequency of Mass90 footprint membership across held-out eSTOMP trajectories."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.colors import Normalize
import numpy as np

ROOT = Path(__file__).resolve().parent
PILOT = ROOT.parents[1] / "analyses/monitoring_pilot_20261118"


def main():
    sensor_x, sensor_y = np.meshgrid([16, 48, 80, 112], [12, 37, 62, 87])
    groups = [("event", "Large shrinkages", 142), ("other", "Other cases", 4858)]
    fig = plt.figure(figsize=(11.0, 6.8), layout="constrained")
    grid = fig.add_gridspec(3, 3, height_ratios=[1, 1, .055])
    with np.load(PILOT / "ensemble_footprints.npz") as data:
        for row, (key, label, count) in enumerate(groups):
            before = 100 * data[f"{key}_t2"]
            after = 100 * data[f"{key}_t3"]
            for col, values in enumerate([before, after, after - before]):
                ax = fig.add_subplot(grid[row, col])
                norm = Normalize(-65, 65) if col == 2 else Normalize(0, 100)
                assert values.min() >= norm.vmin and values.max() <= norm.vmax
                image = ax.imshow(values.T, origin="lower", cmap="RdBu_r" if col == 2 else "viridis",
                                  norm=norm, interpolation="nearest", aspect="equal")
                if col == 2:
                    difference_map = image
                else:
                    occupancy_map = image
                markers = ax.scatter(sensor_x, sensor_y, c="none", edgecolors="white", s=19, lw=.95)
                markers.set_path_effects([pe.Stroke(linewidth=2.0, foreground="#233139"), pe.Normal()])
                ax.set_xticks([0, 32, 64, 96, 127])
                ax.set_yticks([0, 25, 50, 75, 99])
                if row == 0:
                    ax.set_title(["When the warning is issued", "Next saved time", "Difference between maps"][col], fontsize=12)
                    ax.tick_params(labelbottom=False)
                else:
                    ax.set_xlabel("Grid column")
                if col == 0:
                    ax.set_ylabel(f"{label}  (n = {count:,})\nGrid row")
                else:
                    ax.tick_params(labelleft=False)
    cb = fig.colorbar(occupancy_map, cax=fig.add_subplot(grid[2, :2]), orientation="horizontal")
    cb.set_label("Cases with this cell in the plume footprint (%)")
    cb = fig.colorbar(difference_map, cax=fig.add_subplot(grid[2, 2]), orientation="horizontal", ticks=[-60,-30,0,30,60])
    cb.set_label("Change (percentage points)")
    for fmt in ("pdf", "png"):
        fig.savefig(ROOT / f"ensemble_footprint_occupancy.{fmt}", dpi=200, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Generate a normalized displacement frequency-response comparison."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


DEFAULT_OUTPUT = Path("raws/control/assets/resonance-frequency-response.svg")


def displacement_gain(ratio: np.ndarray, damping_ratio: float) -> np.ndarray:
    """Return |G(i omega)| after removing the constant omega_0^-2 factor."""
    denominator = np.sqrt(
        (1.0 - ratio**2) ** 2 + 4.0 * damping_ratio**2 * ratio**2
    )
    return 1.0 / denominator


def generate_figure(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)

    ratio = np.linspace(0.0, 2.0, 2400)
    cases = (
        (0.0, "Undamped", "singular at $r=1$"),
        (0.2, "Lightly damped", r"peak at $r_r\approx0.96$"),
        (0.8, "Strongly damped", "no nonzero peak"),
    )

    plt.rcParams.update({"font.size": 10, "mathtext.fontset": "stix"})
    figure, axes = plt.subplots(
        1,
        len(cases),
        figsize=(10.5, 3.6),
        sharex=True,
        sharey=True,
        constrained_layout=True,
    )

    for axis, (damping_ratio, title, annotation) in zip(axes, cases):
        gain = displacement_gain(ratio, damping_ratio)
        if damping_ratio == 0.0:
            # The ideal undamped response is infinite at r=1. Omit a tiny
            # neighborhood so the singularity is visible without a warning.
            gain[np.abs(ratio - 1.0) < 0.006] = np.nan

        axis.plot(ratio, np.minimum(gain, 4.0), color="#1f5a94", linewidth=2.0)
        axis.axvline(1.0, color="#777777", linestyle="--", linewidth=1.0)
        axis.text(
            0.97,
            0.93,
            annotation,
            transform=axis.transAxes,
            ha="right",
            va="top",
            fontsize=9,
        )
        if 0.0 < damping_ratio < 1.0 / np.sqrt(2.0):
            resonance_ratio = np.sqrt(1.0 - 2.0 * damping_ratio**2)
            axis.axvline(
                resonance_ratio,
                color="#c44e52",
                linestyle=":",
                linewidth=1.2,
            )

        axis.set_title(rf"{title}, $\zeta={damping_ratio:g}$")
        axis.set_xlabel(r"frequency ratio $r=\omega/\omega_0$")
        axis.set_xlim(0.0, 2.0)
        axis.set_ylim(0.0, 4.0)
        axis.set_xticks((0.0, 1.0, 2.0))
        axis.grid(True, alpha=0.25)

    axes[0].set_ylabel(r"normalized gain $\omega_0^2|G(i\omega)|$")
    figure.suptitle("Displacement frequency response and resonance-peak threshold")
    figure.savefig(
        output,
        format=output.suffix.lstrip("."),
        metadata={"Creator": __file__},
    )
    plt.close(figure)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    generate_figure(args.output)
    print(f"Generated {args.output}")


if __name__ == "__main__":
    main()

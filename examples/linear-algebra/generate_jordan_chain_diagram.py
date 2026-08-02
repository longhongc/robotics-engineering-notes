#!/usr/bin/env python3
"""Generate a block diagram for a two-state Jordan chain."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle


DEFAULT_OUTPUT = Path(
    "raws/linear-algebra/assets/jordan-block-integrator-chain.svg"
)


def arrow(axis, start, end, *, color="#1f5a94", connectionstyle="arc3") -> None:
    axis.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=13,
            linewidth=1.6,
            color=color,
            connectionstyle=connectionstyle,
        )
    )


def block(axis, center, width, height, label, *, facecolor="#eaf2fb") -> None:
    x, y = center
    axis.add_patch(
        Rectangle(
            (x - width / 2, y - height / 2),
            width,
            height,
            facecolor=facecolor,
            edgecolor="#1f5a94",
            linewidth=1.5,
        )
    )
    axis.text(x, y, label, ha="center", va="center", fontsize=13)


def summing_junction(axis, center) -> None:
    x, y = center
    axis.add_patch(
        Circle(
            (x, y),
            0.28,
            facecolor="#fff8e7",
            edgecolor="#c58b21",
            linewidth=1.5,
        )
    )
    axis.text(x, y, "+", ha="center", va="center", fontsize=13)


def label(axis, position, text, **kwargs) -> None:
    defaults = {"ha": "center", "va": "center", "fontsize": 11}
    defaults.update(kwargs)
    axis.text(*position, text, **defaults)


def generate_diagram(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({"font.size": 11, "svg.fonttype": "none"})

    figure, axis = plt.subplots(figsize=(11, 5.8))
    axis.set_xlim(0.2, 11.8)
    axis.set_ylim(0.25, 7.0)
    axis.axis("off")

    top_y = 5.0
    bottom_y = 2.0
    sum_x = 2.0
    integrator_x = 4.0
    output_x = 5.8

    summing_junction(axis, (sum_x, top_y))
    summing_junction(axis, (sum_x, bottom_y))
    block(axis, (integrator_x, top_y), 1.35, 0.8, r"$1/s$")
    block(axis, (integrator_x, bottom_y), 1.35, 0.8, r"$1/s$")
    block(axis, (6.8, 6.15), 0.9, 0.55, r"$\lambda$")
    block(axis, (6.8, 0.85), 0.9, 0.55, r"$\lambda$")

    # Forward paths through the summing junctions and integrators.
    arrow(axis, (2.3, top_y), (3.3, top_y))
    arrow(axis, (2.3, bottom_y), (3.3, bottom_y))
    arrow(axis, (4.7, top_y), (output_x, top_y))
    arrow(axis, (4.7, bottom_y), (output_x, bottom_y))
    label(axis, (2.8, top_y + 0.23), r"$\dot{x}_1$")
    label(axis, (2.8, bottom_y + 0.23), r"$\dot{x}_2$")
    label(axis, (6.25, top_y + 0.23), r"$x_1$")
    label(axis, (6.25, bottom_y + 0.23), r"$x_2$")

    # Self-feedback paths lambda*x_i back to each summing junction.
    arrow(axis, (output_x, top_y), (output_x, 6.15))
    arrow(axis, (output_x, 6.15), (7.3, 6.15))
    arrow(axis, (6.35, 6.15), (sum_x, 5.35), connectionstyle="angle3")
    label(axis, (8.05, 6.45), r"$\lambda x_1$")

    arrow(axis, (output_x, bottom_y), (output_x, 0.85))
    arrow(axis, (output_x, 0.85), (7.3, 0.85))
    arrow(axis, (6.35, 0.85), (sum_x, 1.35), connectionstyle="angle3")
    label(axis, (8.05, 0.52), r"$\lambda x_2$")

    # One-way Jordan coupling from x_2 into the x_1 summing junction.
    arrow(axis, (output_x, bottom_y), (9.3, bottom_y))
    arrow(axis, (9.3, bottom_y), (9.3, 4.35))
    arrow(axis, (9.3, 4.35), (sum_x, 4.35), connectionstyle="angle3")
    label(axis, (9.65, 3.35), r"$x_2$", rotation=90)
    label(axis, (5.9, 4.35), "one-way coupling", color="#2f7d32")

    label(
        axis,
        (6.0, 6.8),
        r"Jordan block dynamics: $\dot{x}=Jx,\quad J=[\lambda\ \ 1;\ 0\ \ \lambda]$",
        fontsize=14,
    )
    label(
        axis,
        (1.25, 5.65),
        r"$\dot{x}_1=\lambda x_1+x_2$",
        ha="left",
        fontsize=11,
    )
    label(
        axis,
        (1.25, 1.0),
        r"$\dot{x}_2=\lambda x_2$",
        ha="left",
        fontsize=11,
    )

    figure.savefig(
        output,
        format=output.suffix.lstrip("."),
        bbox_inches="tight",
        metadata={"Creator": __file__},
    )
    plt.close(figure)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    generate_diagram(args.output)
    print(f"Generated {args.output}")


if __name__ == "__main__":
    main()

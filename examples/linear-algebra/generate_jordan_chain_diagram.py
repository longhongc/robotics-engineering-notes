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


def arrow(
    axis,
    start,
    end,
    *,
    color="#1f5a94",
    linestyle="-",
    arrowhead=True,
) -> None:
    axis.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>" if arrowhead else "-",
            mutation_scale=13,
            linewidth=1.6,
            color=color,
            linestyle=linestyle,
        )
    )


def routed_arrow(axis, points, *, color="#1f5a94", linestyle="-") -> None:
    """Draw a routed path with an arrowhead only at its final segment."""
    for index, (start, end) in enumerate(zip(points, points[1:])):
        arrow(
            axis,
            start,
            end,
            color=color,
            linestyle=linestyle,
            arrowhead=index == len(points) - 2,
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

    figure, axis = plt.subplots(figsize=(12, 6.5))
    axis.set_xlim(0.2, 10.4)
    axis.set_ylim(0.2, 7.2)
    axis.set_aspect("equal", adjustable="box")
    axis.axis("off")

    top_y = 5.0
    bottom_y = 2.4
    sum_x = 1.5
    integrator_x = 3.5
    output_x = 5.2
    coupling_color = "#2f7d32"

    summing_junction(axis, (sum_x, top_y))
    summing_junction(axis, (sum_x, bottom_y))
    block(axis, (integrator_x, top_y), 1.35, 0.8, r"$1/s$")
    block(axis, (integrator_x, bottom_y), 1.35, 0.8, r"$1/s$")
    block(axis, (4.4, 6.25), 0.9, 0.55, r"$\lambda$")
    block(axis, (4.4, 0.9), 0.9, 0.55, r"$\lambda$")

    # Forward paths through the summing junctions and integrators.
    arrow(axis, (1.8, top_y), (2.8, top_y))
    arrow(axis, (1.8, bottom_y), (2.8, bottom_y))
    arrow(axis, (4.2, top_y), (output_x, top_y))
    arrow(axis, (4.2, bottom_y), (output_x, bottom_y))
    arrow(axis, (output_x, top_y), (6.2, top_y))
    arrow(axis, (output_x, bottom_y), (6.2, bottom_y))
    label(axis, (2.8, top_y + 0.23), r"$\dot{x}_1$")
    label(axis, (2.8, bottom_y + 0.23), r"$\dot{x}_2$")
    label(axis, (5.7, top_y + 0.23), r"$x_1$")
    label(axis, (5.7, bottom_y + 0.23), r"$x_2$")

    # Upper self-feedback path: x_1 -> lambda -> top summing junction.
    routed_arrow(
        axis,
        [(output_x, top_y), (output_x, 6.25), (4.85, 6.25)],
    )
    routed_arrow(
        axis,
        [(3.95, 6.25), (sum_x, 6.25), (sum_x, 5.35)],
    )
    label(axis, (4.4, 6.72), r"$\lambda x_1$")

    # Lower self-feedback path: x_2 -> lambda -> bottom summing junction.
    routed_arrow(
        axis,
        [(output_x, bottom_y), (output_x, 0.9), (4.85, 0.9)],
    )
    routed_arrow(
        axis,
        [(3.95, 0.9), (sum_x, 0.9), (sum_x, 2.05)],
    )
    label(axis, (4.4, 0.48), r"$\lambda x_2$")

    # One-way Jordan coupling from x_2 into the x_1 summing junction.
    routed_arrow(
        axis,
        [(6.2, bottom_y), (7.8, bottom_y), (7.8, 4.15)],
        color=coupling_color,
        linestyle="--",
    )
    routed_arrow(
        axis,
        [(7.8, 4.15), (sum_x, 4.15), (sum_x, 4.65)],
        color=coupling_color,
        linestyle="--",
    )
    label(axis, (8.15, 3.35), r"$x_2$", rotation=90, color=coupling_color)
    label(axis, (4.7, 4.42), "one-way coupling", color=coupling_color)

    label(
        axis,
        (5.2, 7.0),
        r"Jordan block dynamics: $\dot{x}=Jx$",
        fontsize=14,
    )
    label(
        axis,
        (0.35, 5.75),
        r"$\dot{x}_1=\lambda x_1+x_2$",
        ha="left",
        fontsize=11,
    )
    label(
        axis,
        (0.35, 1.55),
        r"$\dot{x}_2=\lambda x_2$",
        ha="left",
        fontsize=11,
    )

    figure.savefig(
        output,
        format=output.suffix.lstrip("."),
        bbox_inches="tight",
        metadata={"Creator": "generate_jordan_chain_diagram.py"},
    )
    plt.close(figure)

    if output.suffix.lower() == ".svg":
        # Matplotlib may leave spaces at the ends of wrapped path lines.
        # Normalize them so generated assets pass git diff --check.
        normalized = "\n".join(
            line.rstrip() for line in output.read_text(encoding="utf-8").splitlines()
        )
        output.write_text(normalized + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    generate_diagram(args.output)
    print(f"Generated {args.output}")


if __name__ == "__main__":
    main()

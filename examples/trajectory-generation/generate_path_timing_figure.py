#!/usr/bin/env python3
"""Generate path-timing retiming figures for straight and sine paths.

The path is q(s), where the nominal path-coordinate velocity v0 is constant
and a multiplier m changes the actual playback velocity:

    s_dot = m v0

During ramp-down, s_ddot is chosen conservatively so that

    |q_ddot| <= |q''(s) s_dot^2| + |q'(s) s_ddot| <= a_max.

The straight path is the primary teaching example: q(s) = s makes the
retiming relationship direct. The sine path is an extension that exposes the
additional path-curvature term q''(s) s_dot^2.

These are educational single-coordinate examples. They do not model jerk,
torque, actuator, or multi-joint constraints and are not emergency-stop
controllers.

From the repository root:

    uv pip install --python .venv/bin/python \
        -r examples/trajectory-generation/requirements.txt
    MPLCONFIGDIR=/tmp/robotics-engineering-notes-mpl \
        ./.venv/bin/python examples/trajectory-generation/generate_path_timing_figure.py
    MPLCONFIGDIR=/tmp/robotics-engineering-notes-mpl \
        ./.venv/bin/python examples/trajectory-generation/generate_path_timing_figure.py \
        --path sine \
        --output raws/trajectory-generation/assets/path-timing-retiming-sine.svg
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Literal

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


PathMode = Literal["straight", "sine"]

AMPLITUDE = 1.0
WAVENUMBER = 1.0
NOMINAL_PATH_VELOCITY = 0.7
ACCELERATION_LIMIT = 0.8
PATH_ACCELERATION_CAP = 0.4
TIME_STEP = 0.01
MARKER_EVERY = 10
DURATION = 8.0
RAMP_START = 1.2


def path_position(s: np.ndarray, path_mode: PathMode) -> np.ndarray:
    if path_mode == "straight":
        return s
    return AMPLITUDE * np.sin(WAVENUMBER * s)


def path_first_derivative(s: np.ndarray, path_mode: PathMode) -> np.ndarray:
    if path_mode == "straight":
        return np.ones_like(s)
    return AMPLITUDE * WAVENUMBER * np.cos(WAVENUMBER * s)


def path_second_derivative(s: np.ndarray, path_mode: PathMode) -> np.ndarray:
    if path_mode == "straight":
        return np.zeros_like(s)
    return -AMPLITUDE * WAVENUMBER**2 * np.sin(WAVENUMBER * s)


def simulate(path_mode: PathMode) -> dict[str, np.ndarray | float]:
    times = np.arange(0.0, DURATION + 0.5 * TIME_STEP, TIME_STEP)
    path_coordinate = np.zeros_like(times)
    multiplier = np.ones_like(times)
    path_acceleration = np.zeros_like(times)

    for index in range(len(times) - 1):
        s = path_coordinate[index]
        current_multiplier = multiplier[index]
        path_velocity = current_multiplier * NOMINAL_PATH_VELOCITY

        if times[index] < RAMP_START or current_multiplier <= 0.0:
            next_multiplier = current_multiplier
            s_ddot = 0.0
        else:
            q_prime = float(path_first_derivative(np.asarray(s), path_mode))
            q_second = float(path_second_derivative(np.asarray(s), path_mode))
            curvature_acceleration = q_second * path_velocity**2
            available_margin = ACCELERATION_LIMIT - abs(curvature_acceleration)

            if available_margin < -1e-10:
                raise RuntimeError(
                    "The nominal path velocity already violates the acceleration limit."
                )

            # A triangle-inequality bound leaves room for the path-curvature
            # term before applying path-coordinate deceleration.
            safe_path_acceleration = available_margin / max(abs(q_prime), 1e-12)
            requested_deceleration = min(PATH_ACCELERATION_CAP, safe_path_acceleration)
            next_multiplier = max(
                0.0,
                current_multiplier
                - TIME_STEP * requested_deceleration / NOMINAL_PATH_VELOCITY,
            )
            # Recompute the acceleration after clamping at zero so that the
            # discrete multiplier and s_ddot remain consistent.
            s_ddot = (
                next_multiplier - current_multiplier
            ) * NOMINAL_PATH_VELOCITY / TIME_STEP

        next_path_velocity = next_multiplier * NOMINAL_PATH_VELOCITY
        path_coordinate[index + 1] = s + 0.5 * (
            path_velocity + next_path_velocity
        ) * TIME_STEP
        multiplier[index + 1] = next_multiplier
        path_acceleration[index] = s_ddot

    # There is no acceleration after the stopped state at the final sample.
    path_acceleration[-1] = 0.0

    q_prime = path_first_derivative(path_coordinate, path_mode)
    q_second = path_second_derivative(path_coordinate, path_mode)
    path_velocity = multiplier * NOMINAL_PATH_VELOCITY
    position = path_position(path_coordinate, path_mode)
    velocity = q_prime * path_velocity
    acceleration = q_second * path_velocity**2 + q_prime * path_acceleration
    maximum_acceleration = float(np.max(np.abs(acceleration)))

    if maximum_acceleration > ACCELERATION_LIMIT + 1e-9:
        raise RuntimeError(
            f"Acceleration limit violated: {maximum_acceleration:.6f} "
            f"> {ACCELERATION_LIMIT:.6f}"
        )

    return {
        "times": times,
        "path_coordinate": path_coordinate,
        "path_velocity": path_velocity,
        "path_acceleration": path_acceleration,
        "multiplier": multiplier,
        "position": position,
        "velocity": velocity,
        "acceleration": acceleration,
        "maximum_acceleration": maximum_acceleration,
    }


def plot_simulation(
    data: dict[str, np.ndarray | float], output: Path, path_mode: PathMode
) -> None:
    times = data["times"]
    ramp_end = float(times[np.flatnonzero(data["multiplier"] <= 0.0)[0]])
    path_label = "straight-line" if path_mode == "straight" else "sine"
    sample_label = f"every {MARKER_EVERY}th control sample"

    figure, axes = plt.subplots(5, 1, figsize=(11, 14), sharex=True)
    figure.text(
        0.5,
        0.995,
        f"Path–timing retiming for a streaming {path_label} trajectory",
        ha="center",
        va="top",
        fontsize=16,
    )

    axes[0].plot(times, data["position"], color="tab:blue")
    axes[0].set_ylabel("Position q")
    axes[0].set_title("Robot position")

    axes[1].plot(times, data["velocity"], color="tab:orange")
    axes[1].set_ylabel("Velocity q̇")
    axes[1].set_title("Output velocity changes with the multiplier")

    axes[2].plot(times, data["acceleration"], color="tab:red")
    axes[2].axhline(ACCELERATION_LIMIT, color="black", linestyle="--", linewidth=1)
    axes[2].axhline(-ACCELERATION_LIMIT, color="black", linestyle="--", linewidth=1)
    axes[2].set_ylabel("Acceleration q̈")
    axes[2].set_title("Acceleration remains inside the limit")

    sample_indices = slice(None, None, MARKER_EVERY)

    axes[3].step(
        times,
        data["multiplier"],
        where="post",
        color="tab:green",
        label="m[k]",
    )
    axes[3].plot(
        times[sample_indices],
        data["multiplier"][sample_indices],
        "o",
        color="tab:green",
        markersize=3,
        label=sample_label,
    )
    axes[3].axhline(1.0, color="gray", linestyle=":", linewidth=1)
    axes[3].set_ylabel("Multiplier m")
    axes[3].set_ylim(-0.05, 1.1)
    axes[3].set_title("Playback multiplier")

    axes[4].plot(
        times,
        data["path_coordinate"],
        color="tab:purple",
        alpha=0.45,
        label="s(t), connected",
    )
    axes[4].plot(
        times[sample_indices],
        data["path_coordinate"][sample_indices],
        "o",
        color="tab:purple",
        markersize=3,
        label=f"s[k], {sample_label}",
    )
    axes[4].set_ylabel("Path coordinate s")
    axes[4].set_xlabel("Time t [s]")
    axes[4].set_title("Path progress and nominal path velocity")
    path_velocity_axis = axes[4].twinx()
    path_velocity_axis.plot(
        times,
        data["path_velocity"],
        color="tab:brown",
        label="ṡ(t), actual",
    )
    path_velocity_axis.axhline(
        NOMINAL_PATH_VELOCITY,
        color="gray",
        linestyle=":",
        linewidth=1,
        label="v₀, nominal",
    )
    path_velocity_axis.set_ylabel("Path velocity ṡ")
    path_velocity_axis.set_ylim(-0.02, NOMINAL_PATH_VELOCITY * 1.2)
    left_handles, left_labels = axes[4].get_legend_handles_labels()
    right_handles, right_labels = path_velocity_axis.get_legend_handles_labels()
    axes[4].legend(
        left_handles + right_handles,
        left_labels + right_labels,
        loc="upper left",
        fontsize=8,
    )

    for axis in axes:
        axis.axvspan(RAMP_START, ramp_end, color="gold", alpha=0.18)
        axis.grid(True, alpha=0.25)

    figure.text(
        0.99,
        0.01,
        "Gold shading: multiplier ramp-down; dotted line: nominal path velocity",
        ha="right",
        fontsize=9,
    )
    figure.tight_layout(rect=(0, 0.02, 1, 0.97))
    output.parent.mkdir(parents=True, exist_ok=True)
    # Matplotlib infers the format from the output suffix. SVG is the
    # repository asset, while PNG is convenient for local visual inspection.
    figure.savefig(output)
    plt.close(figure)
    if output.suffix.lower() == ".svg":
        # Matplotlib emits trailing spaces in multi-line path data. Remove
        # them so generated assets pass the repository whitespace check.
        cleaned_svg = "\n".join(
            line.rstrip() for line in output.read_text(encoding="utf-8").splitlines()
        )
        output.write_text(cleaned_svg + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--path",
        choices=("straight", "sine"),
        default="straight",
        help="Path shape to simulate (default: straight)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output path; defaults to an SVG under raws/trajectory-generation/assets/",
    )
    args = parser.parse_args()
    path_mode: PathMode = args.path
    output = args.output or Path(
        f"raws/trajectory-generation/assets/path-timing-retiming-{path_mode}.svg"
    )

    data = simulate(path_mode)
    plot_simulation(data, output, path_mode)
    print(f"Wrote {output}")
    print(f"Path mode: {path_mode}")
    print(f"Maximum |q̈|: {data['maximum_acceleration']:.6f}")
    print(f"Acceleration limit: {ACCELERATION_LIMIT:.6f}")


if __name__ == "__main__":
    main()

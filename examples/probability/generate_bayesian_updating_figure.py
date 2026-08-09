#!/usr/bin/env python3
"""Generate linked 3D, contour, and 2D Bayesian-update views."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


DEFAULT_OUTPUT = Path("raws/probability/assets/bayesian-updating-surface.svg")
PRIOR_MEAN = 0.0
PRIOR_STD = 1.4
THETA_SLICE = PRIOR_MEAN
OBSERVATION = 1.2
OBSERVATION_STD = 0.7


def normal_pdf(
    value: np.ndarray | float,
    mean: np.ndarray | float,
    standard_deviation: float,
) -> np.ndarray:
    """Evaluate a normal density while allowing a vector-valued mean."""
    scale = standard_deviation
    return np.exp(-0.5 * ((value - mean) / scale) ** 2) / (
        scale * np.sqrt(2.0 * np.pi)
    )


def posterior_parameters(
    prior_mean: float,
    prior_std: float,
    observation: float,
    observation_std: float,
) -> tuple[float, float]:
    """Return the Normal-Normal posterior mean and standard deviation."""
    prior_precision = 1.0 / prior_std**2
    observation_precision = 1.0 / observation_std**2
    posterior_variance = 1.0 / (prior_precision + observation_precision)
    posterior_mean = posterior_variance * (
        prior_precision * prior_mean + observation_precision * observation
    )
    return posterior_mean, np.sqrt(posterior_variance)


def add_grid(axis: plt.Axes) -> None:
    """Use a light grid on 2D panels without overpowering the curves."""
    axis.grid(True, alpha=0.25)


def generate_figure(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)

    theta = np.linspace(-3.5, 3.5, 300)
    observations = np.linspace(-3.5, 3.5, 300)
    map_grid = np.linspace(-3.5, 3.5, 80)
    map_observations, map_theta = np.meshgrid(map_grid, map_grid)
    map_density = normal_pdf(map_observations, map_theta, OBSERVATION_STD)

    wire_grid = np.linspace(-3.5, 3.5, 22)
    wire_observations, wire_theta = np.meshgrid(wire_grid, wire_grid)
    wire_density = normal_pdf(wire_observations, wire_theta, OBSERVATION_STD)

    posterior_mean, posterior_std = posterior_parameters(
        PRIOR_MEAN,
        PRIOR_STD,
        OBSERVATION,
        OBSERVATION_STD,
    )
    prior = normal_pdf(theta, PRIOR_MEAN, PRIOR_STD)
    likelihood = normal_pdf(OBSERVATION, theta, OBSERVATION_STD)
    unnormalized_posterior = likelihood * prior
    posterior = normal_pdf(theta, posterior_mean, posterior_std)
    evidence = normal_pdf(
        observations,
        PRIOR_MEAN,
        np.sqrt(PRIOR_STD**2 + OBSERVATION_STD**2),
    )
    conditional_slice = normal_pdf(observations, THETA_SLICE, OBSERVATION_STD)

    plt.rcParams.update({"font.size": 8.5, "mathtext.fontset": "stix"})
    figure = plt.figure(figsize=(16, 8.5), constrained_layout=True)
    grid = figure.add_gridspec(2, 4)

    surface_axis = figure.add_subplot(grid[0, 0], projection="3d")
    surface_axis.plot_wireframe(
        wire_observations,
        wire_theta,
        wire_density,
        color="#8a8a8a",
        linewidth=0.45,
        alpha=0.55,
        rstride=1,
        cstride=1,
    )
    slice_observations = np.linspace(-3.5, 3.5, 300)
    surface_axis.plot(
        slice_observations,
        np.full_like(slice_observations, THETA_SLICE),
        normal_pdf(slice_observations, THETA_SLICE, OBSERVATION_STD),
        color="#d62728",
        linewidth=2.8,
        label=rf"fixed $\theta={THETA_SLICE:g}$",
    )
    slice_theta = np.linspace(-3.5, 3.5, 300)
    surface_axis.plot(
        np.full_like(slice_theta, OBSERVATION),
        slice_theta,
        normal_pdf(OBSERVATION, slice_theta, OBSERVATION_STD),
        color="#1f77b4",
        linewidth=2.8,
        label=rf"fixed $x={OBSERVATION:g}$",
    )
    surface_axis.set_xlabel(r"observation $x$", labelpad=0)
    surface_axis.set_ylabel(r"parameter $\theta$", labelpad=0)
    surface_axis.set_zlabel(r"$p(x\mid\theta)$", labelpad=0)
    surface_axis.set_title("Sparse 3D wireframe")
    surface_axis.legend(loc="upper left", fontsize=7)
    surface_axis.view_init(elev=27, azim=-62)

    slice_map_axis = figure.add_subplot(grid[0, 1])
    contour_levels = np.linspace(0.0, float(map_density.max()), 17)
    contour = slice_map_axis.contourf(
        map_observations,
        map_theta,
        map_density,
        levels=contour_levels,
        cmap="viridis",
    )
    slice_map_axis.axhline(
        THETA_SLICE,
        color="#d62728",
        linewidth=2.2,
        label=rf"fixed $\theta={THETA_SLICE:g}$",
    )
    slice_map_axis.axvline(
        OBSERVATION,
        color="#1f77b4",
        linewidth=2.2,
        label=rf"fixed $x={OBSERVATION:g}$",
    )
    slice_map_axis.scatter(
        [OBSERVATION],
        [THETA_SLICE],
        color="white",
        edgecolor="black",
        zorder=3,
        s=28,
    )
    slice_map_axis.set_title("Top-down slice map")
    slice_map_axis.set_xlabel(r"observation $x$")
    slice_map_axis.set_ylabel(r"parameter $\theta$")
    slice_map_axis.legend(loc="upper left", fontsize=7)
    figure.colorbar(contour, ax=slice_map_axis, label=r"$p(x\mid\theta)$")

    conditional_axis = figure.add_subplot(grid[0, 2])
    conditional_axis.plot(
        observations,
        conditional_slice,
        color="#d62728",
        linewidth=2.2,
    )
    conditional_axis.set_title(rf"Horizontal slice: $p(x\mid\theta={THETA_SLICE:g})$")
    conditional_axis.set_xlabel(r"observation $x$")
    conditional_axis.set_ylabel("density over observations")
    add_grid(conditional_axis)

    likelihood_axis = figure.add_subplot(grid[0, 3])
    likelihood_axis.plot(theta, likelihood, color="#1f77b4", linewidth=2.2)
    likelihood_axis.set_title(rf"Vertical slice: $L(\theta\mid x={OBSERVATION:g})$")
    likelihood_axis.set_xlabel(r"parameter $\theta$")
    likelihood_axis.set_ylabel(r"$p(x_{obs}\mid\theta)$")
    add_grid(likelihood_axis)

    prior_axis = figure.add_subplot(grid[1, 0])
    prior_axis.plot(theta, prior, color="#6a3d9a", linewidth=2.2)
    prior_axis.axvline(PRIOR_MEAN, color="#777777", linestyle="--", linewidth=1)
    prior_axis.set_title(rf"Prior $p(\theta)$, $\mu_0={PRIOR_MEAN:g}$")
    prior_axis.set_xlabel(r"parameter $\theta$")
    prior_axis.set_ylabel("density")
    add_grid(prior_axis)

    product_axis = figure.add_subplot(grid[1, 1])
    product_axis.plot(theta, unnormalized_posterior, color="#ff7f0e", linewidth=2.2)
    product_axis.set_title("Unnormalized posterior numerator")
    product_axis.set_xlabel(r"parameter $\theta$")
    product_axis.set_ylabel(r"$p(x_{obs}\mid\theta)p(\theta)$")
    add_grid(product_axis)

    posterior_axis = figure.add_subplot(grid[1, 2])
    posterior_axis.plot(theta, posterior, color="#2ca02c", linewidth=2.2)
    posterior_axis.axvline(posterior_mean, color="#777777", linestyle="--", linewidth=1)
    posterior_axis.set_title(
        rf"Posterior, $\mu_n={posterior_mean:.2f}$, "
        rf"$\sigma_n={posterior_std:.2f}$"
    )
    posterior_axis.set_xlabel(r"parameter $\theta$")
    posterior_axis.set_ylabel(r"$p(\theta\mid x_{obs})$")
    add_grid(posterior_axis)

    evidence_axis = figure.add_subplot(grid[1, 3])
    evidence_axis.plot(observations, evidence, color="#8c564b", linewidth=2.2)
    evidence_axis.axvline(OBSERVATION, color="#777777", linestyle="--", linewidth=1)
    evidence_axis.set_title(r"Evidence $p(x)$ across possible observations")
    evidence_axis.set_xlabel(r"observation $x$")
    evidence_axis.set_ylabel("density")
    add_grid(evidence_axis)

    figure.suptitle(
        "Bayesian updating: identify the slice before interpreting the curve",
        fontsize=14,
    )
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

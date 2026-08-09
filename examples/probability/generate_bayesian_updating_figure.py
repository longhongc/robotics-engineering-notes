#!/usr/bin/env python3
"""Generate a 3D conditional-density surface and Bayesian update slices."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


DEFAULT_OUTPUT = Path("raws/probability/assets/bayesian-updating-surface.svg")
PRIOR_MEAN = 0.0
PRIOR_STD = 1.4
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


def generate_figure(output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)

    theta = np.linspace(-3.5, 3.5, 300)
    observations = np.linspace(-3.5, 3.5, 300)
    surface_grid = np.linspace(-3.5, 3.5, 30)
    surface_observations, surface_theta = np.meshgrid(surface_grid, surface_grid)
    conditional_surface = normal_pdf(
        surface_observations,
        surface_theta,
        OBSERVATION_STD,
    )

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

    plt.rcParams.update({"font.size": 9, "mathtext.fontset": "stix"})
    figure = plt.figure(figsize=(14, 8.5), constrained_layout=True)
    grid = figure.add_gridspec(2, 3)

    surface_axis = figure.add_subplot(grid[0, 0], projection="3d")
    surface_axis.plot_surface(
        surface_observations,
        surface_theta,
        conditional_surface,
        cmap="viridis",
        linewidth=0,
        antialiased=True,
        alpha=0.82,
    )
    slice_observations = np.linspace(-3.5, 3.5, 360)
    surface_axis.plot(
        slice_observations,
        np.full_like(slice_observations, posterior_mean),
        normal_pdf(slice_observations, posterior_mean, OBSERVATION_STD),
        color="#d62728",
        linewidth=2.5,
        label=rf"$\theta={posterior_mean:.2f}$ slice",
    )
    slice_theta = np.linspace(-3.5, 3.5, 360)
    surface_axis.plot(
        np.full_like(slice_theta, OBSERVATION),
        slice_theta,
        normal_pdf(OBSERVATION, slice_theta, OBSERVATION_STD),
        color="#1f77b4",
        linewidth=2.5,
        label=rf"$x={OBSERVATION:.1f}$ likelihood",
    )
    surface_axis.set_xlabel(r"observation $x$")
    surface_axis.set_ylabel(r"parameter $\theta$")
    surface_axis.set_zlabel(r"$p(x\mid\theta)$")
    surface_axis.set_title("Conditional-density surface and slices")
    surface_axis.legend(loc="upper left", fontsize=7)
    surface_axis.view_init(elev=27, azim=-62)

    prior_axis = figure.add_subplot(grid[0, 1])
    prior_axis.plot(theta, prior, color="#6a3d9a", linewidth=2.2)
    prior_axis.axvline(PRIOR_MEAN, color="#777777", linestyle="--", linewidth=1)
    prior_axis.set_title(rf"Prior $p(\theta)$, $\mu_0={PRIOR_MEAN:g}$")
    prior_axis.set_xlabel(r"parameter $\theta$")
    prior_axis.set_ylabel("density")

    likelihood_axis = figure.add_subplot(grid[0, 2])
    likelihood_axis.plot(theta, likelihood, color="#1f77b4", linewidth=2.2)
    likelihood_axis.axvline(OBSERVATION, color="#777777", linestyle="--", linewidth=1)
    likelihood_axis.set_title(rf"Likelihood at $x_{{obs}}={OBSERVATION:g}$")
    likelihood_axis.set_xlabel(r"parameter $\theta$")
    likelihood_axis.set_ylabel(r"$p(x_{obs}\mid\theta)$")

    product_axis = figure.add_subplot(grid[1, 0])
    product_axis.plot(
        theta,
        unnormalized_posterior,
        color="#ff7f0e",
        linewidth=2.2,
    )
    product_axis.set_title("Unnormalized posterior numerator")
    product_axis.set_xlabel(r"parameter $\theta$")
    product_axis.set_ylabel(r"$p(x_{obs}\mid\theta)p(\theta)$")

    posterior_axis = figure.add_subplot(grid[1, 1])
    posterior_axis.plot(theta, posterior, color="#2ca02c", linewidth=2.2)
    posterior_axis.axvline(posterior_mean, color="#777777", linestyle="--", linewidth=1)
    posterior_axis.set_title(
        rf"Posterior, $\mu_n={posterior_mean:.2f}$, "
        rf"$\sigma_n={posterior_std:.2f}$"
    )
    posterior_axis.set_xlabel(r"parameter $\theta$")
    posterior_axis.set_ylabel(r"$p(\theta\mid x_{obs})$")

    evidence_axis = figure.add_subplot(grid[1, 2])
    evidence_axis.plot(observations, evidence, color="#8c564b", linewidth=2.2)
    evidence_axis.axvline(OBSERVATION, color="#777777", linestyle="--", linewidth=1)
    evidence_axis.set_title(r"Evidence $p(x)$ across possible observations")
    evidence_axis.set_xlabel(r"observation $x$")
    evidence_axis.set_ylabel("density")

    for axis in figure.axes:
        if axis is not surface_axis:
            axis.grid(True, alpha=0.25)

    figure.suptitle(
        "Bayesian updating: probability slice, likelihood, and posterior",
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

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class CubicHermitePath:
    """Compact multi-joint geometric path q(s)."""

    s_knots: np.ndarray
    q_knots: np.ndarray
    dq_ds_knots: np.ndarray
    interpolation_method: str = "cubic Hermite"

    @classmethod
    def from_waypoints(
        cls,
        q_knots: np.ndarray,
        s_knots: np.ndarray | None = None,
    ) -> "CubicHermitePath":
        q_knots = np.asarray(q_knots, dtype=float)
        if q_knots.ndim != 2 or len(q_knots) < 2:
            raise ValueError("q_knots must have shape (N, n_joints), N >= 2")

        if s_knots is None:
            # Use waypoint index as the path coordinate.
            s_knots = np.arange(len(q_knots), dtype=float)
        else:
            s_knots = np.asarray(s_knots, dtype=float)

        if s_knots.shape != (len(q_knots),):
            raise ValueError("s_knots must have shape (N,)")
        if np.any(np.diff(s_knots) <= 0.0):
            raise ValueError("s_knots must be strictly increasing")

        dq_ds_knots = np.gradient(
            q_knots,
            s_knots,
            axis=0,
            edge_order=2 if len(q_knots) >= 3 else 1,
        )
        return cls(s_knots, q_knots, dq_ds_knots)

    @property
    def n_joints(self) -> int:
        return self.q_knots.shape[1]

    def evaluate(self, s: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Evaluate q(s), dq/ds, and d2q/ds2 from one interpolant."""
        s = float(np.clip(s, self.s_knots[0], self.s_knots[-1]))
        i = int(np.searchsorted(self.s_knots, s, side="right") - 1)
        i = max(0, min(i, len(self.s_knots) - 2))

        s0, s1 = self.s_knots[i : i + 2]
        h = s1 - s0
        u = (s - s0) / h

        q0, q1 = self.q_knots[i : i + 2]
        v0, v1 = self.dq_ds_knots[i : i + 2]

        h00 = 2 * u**3 - 3 * u**2 + 1
        h10 = u**3 - 2 * u**2 + u
        h01 = -2 * u**3 + 3 * u**2
        h11 = u**3 - u**2
        q = h00 * q0 + h10 * h * v0 + h01 * q1 + h11 * h * v1

        dq_du = (
            (6 * u**2 - 6 * u) * q0
            + (3 * u**2 - 4 * u + 1) * h * v0
            + (-6 * u**2 + 6 * u) * q1
            + (3 * u**2 - 2 * u) * h * v1
        )
        dq_ds = dq_du / h

        d2q_du2 = (
            (12 * u - 6) * q0
            + (6 * u - 4) * h * v0
            + (-12 * u + 6) * q1
            + (6 * u - 2) * h * v1
        )
        d2q_ds2 = d2q_du2 / h**2
        return q, dq_ds, d2q_ds2


def multiplier_rate_bounds(
    path: CubicHermitePath,
    s: float,
    multiplier: float,
    waypoint_dt: float,
    acceleration_min: np.ndarray,
    acceleration_max: np.ndarray,
    derivative_tolerance: float = 1e-9,
) -> tuple[float, float]:
    """Intersect the signed feasible m_dot intervals from all joints."""
    _, dq_ds, d2q_ds2 = path.evaluate(s)
    s_dot = multiplier / waypoint_dt

    lower, upper = -np.inf, np.inf
    for j in range(path.n_joints):
        # q_ddot_j = curvature_acceleration + coefficient * m_dot
        curvature_acceleration = d2q_ds2[j] * s_dot**2
        coefficient = dq_ds[j] / waypoint_dt

        if abs(coefficient) < derivative_tolerance:
            if not (
                acceleration_min[j]
                <= curvature_acceleration
                <= acceleration_max[j]
            ):
                return np.inf, -np.inf
            continue

        x1 = (acceleration_min[j] - curvature_acceleration) / coefficient
        x2 = (acceleration_max[j] - curvature_acceleration) / coefficient
        lower = max(lower, min(x1, x2))
        upper = min(upper, max(x1, x2))

    return lower, upper


def joint_state(
    path: CubicHermitePath,
    s: float,
    multiplier: float,
    multiplier_rate: float,
    waypoint_dt: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    q, dq_ds, d2q_ds2 = path.evaluate(s)
    s_dot = multiplier / waypoint_dt
    s_ddot = multiplier_rate / waypoint_dt
    q_dot = dq_ds * s_dot
    q_ddot = d2q_ds2 * s_dot**2 + dq_ds * s_ddot
    return q, q_dot, q_ddot


def main() -> None:
    # Two-joint waypoint positions in radians. Here s is waypoint index.
    q_waypoints = np.array(
        [
            [0.00, 0.20],
            [0.18, 0.36],
            [0.42, 0.48],
            [0.70, 0.50],
            [0.92, 0.38],
            [1.04, 0.12],
            [1.00, -0.18],
            [0.82, -0.38],
        ]
    )
    path = CubicHermitePath.from_waypoints(q_waypoints)

    # The nominal trajectory has one waypoint every 0.20 seconds.
    waypoint_dt = 0.20
    control_dt = 0.01  # 100 Hz executor

    acceleration_min = np.array([-8.0, -7.0])  # rad/s^2
    acceleration_max = np.array([+8.0, +7.0])

    s = 2.35  # fractional waypoint position
    multiplier = 1.0
    requested_rate = -4.0  # multiplier units per second

    lower, upper = multiplier_rate_bounds(
        path,
        s,
        multiplier,
        waypoint_dt,
        acceleration_min,
        acceleration_max,
    )
    if lower > upper:
        raise RuntimeError("No feasible multiplier-rate interval exists")

    # For slowdown, require m_dot <= 0 and clamp the request.
    slowdown_upper = min(upper, 0.0)
    if lower > slowdown_upper:
        raise RuntimeError("No non-positive multiplier rate is feasible")
    chosen_rate = float(np.clip(requested_rate, lower, slowdown_upper))

    q, q_dot, q_ddot = joint_state(
        path, s, multiplier, chosen_rate, waypoint_dt
    )
    delta_multiplier = chosen_rate * control_dt
    next_multiplier = max(0.0, multiplier + delta_multiplier)

    print(f"interpolation: {path.interpolation_method}")
    print(f"feasible m_dot: [{lower:.6f}, {upper:.6f}] 1/s")
    print(f"chosen m_dot: {chosen_rate:.6f} 1/s")
    print(f"delta multiplier this cycle: {delta_multiplier:.6f}")
    print(f"next multiplier: {next_multiplier:.6f}")
    print(f"q: {q}")
    print(f"q_dot: {q_dot}")
    print(f"q_ddot: {q_ddot}")
    print(
        "acceleration limits satisfied:",
        np.all(q_ddot >= acceleration_min)
        and np.all(q_ddot <= acceleration_max),
    )


if __name__ == "__main__":
    main()

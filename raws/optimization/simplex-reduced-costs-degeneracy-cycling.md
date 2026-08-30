# Simplex Reduced Costs, Degeneracy, and Cycling

This note summarizes the role of reduced costs in the simplex method, explains how degeneracy arises, and clarifies whether the simplex algorithm is guaranteed to converge.

---

## 1. Linear Program in Standard Form

Consider the linear program

$$
\min \; c^T x
$$

subject to

$$
Ax = b, \quad x \ge 0.
$$

Partition the variables into:
- **Basic variables** \(x_B\),
- **Nonbasic variables** \(x_N\).

Accordingly, write

$$
A = [B \; N], \quad c = (c_B, c_N).
$$

---

## 2. Basic Variables as Functions of Nonbasic Variables

From the constraints:

$$
Bx_B + Nx_N = b,
$$

we obtain

$$
x_B = B^{-1}b - B^{-1}N x_N.
$$

Thus, any change in the nonbasic variables forces a corresponding change in the basic variables to maintain feasibility.

---

## 3. Substituting into the Objective Function

Substitute the expression for \(x_B\) into the objective:

$$
\begin{aligned}
z
&= c_B^T x_B + c_N^T x_N \\
&= c_B^T(B^{-1}b - B^{-1}N x_N) + c_N^T x_N \\
&= c_B^T B^{-1}b + (c_N^T - c_B^T B^{-1}N)x_N.
\end{aligned}
$$

Define the **reduced cost vector**:

$$
r^T = c_N^T - c_B^T B^{-1}N.
$$

Then the objective becomes:

$$
z = \text{constant} + r^T x_N.
$$

---

## 4. Meaning of Reduced Costs

Each reduced cost \(r_j\) represents the **net change in the objective value per unit increase of nonbasic variable \(x_j\)**, after accounting for all induced changes in the basic variables.

Key point:
- The effect of adjusting \(x_B\) is already fully incorporated into \(r_j\).

---

## 5. Optimality Condition

For a minimization problem:

- If \(r_j \ge 0\) for all nonbasic variables, the current basic feasible solution is **optimal**.
- If some \(r_j < 0\), then increasing \(x_j\) can potentially reduce the objective value.

This criterion is exactly what appears in the bottom row of the simplex tableau.

---

## 6. Feasibility and the Ratio Test

Let \(x_j = t\) be an entering nonbasic variable. Then:

$$
x_B(t) = B^{-1}b - t \cdot (B^{-1}N)_j.
$$

Feasibility requires:

$$
x_B(t) \ge 0.
$$

This imposes the bound:

$$
t \le \min_{i : (B^{-1}N)_{ij} > 0} \frac{(B^{-1}b)_i}{(B^{-1}N)_{ij}}.
$$

- If the maximum feasible step satisfies \(t_{\max} > 0\), the objective strictly decreases.
- If \(t_{\max} = 0\), no movement is possible despite a negative reduced cost.

---

## 7. Degeneracy

A **degenerate basic feasible solution** occurs when at least one basic variable satisfies:

$$
(B^{-1}b)_i = 0.
$$

Consequences:
- A reduced cost \(r_j\) may be negative,
- But feasibility forces \(t_{\max} = 0\),
- The entering variable cannot increase.

A pivot may still occur, but:
- The corner point does not change,
- The objective value remains the same.

This is called a **degenerate pivot**.

---

## 8. Cycling

Because multiple bases can represent the same corner point, repeated degenerate pivots may cause the simplex method to revisit the same basis indefinitely.

This phenomenon is called **cycling**.

Important facts:
- Cycling is possible in theory.
- Explicit cycling examples exist.
- Cycling is rare in practical computations.

---

## 9. Convergence Guarantees

- **Simplex without safeguards**:
  - No theoretical guarantee of termination.
  - Cycling may occur.

- **Simplex with anti-cycling rules**:
  - Guaranteed to terminate in finitely many steps.

Examples of anti-cycling rules:
- Bland’s rule (smallest-index entering and leaving variables),
- Lexicographic (symbolic perturbation) rules.

---

## 10. Key Takeaways

- Reduced costs measure objective change along feasible directions.
- Negative reduced costs indicate potentially improving directions.
- Feasibility constraints determine whether improvement is possible.
- Degeneracy allows basis changes without objective improvement.
- Termination is guaranteed when appropriate pivot rules are used.

---

## Related material

- [Geometry of corners and basis exchange](simplex-geometry-corners-slack-variables.md)
- [Phase I simplex with artificial variables](simplex-phase-i-artificial-variables.md)
- [Linear programming and duality](linear-programming-duality-linear-algebra.md)

---

# Linear Programming and Duality (Linear Algebra Viewpoint)

These notes summarize linear programming from a linear algebra perspective, emphasizing geometry, matrix structure, and duality.

---

## 1. Linear Programming Minimization Problem

A standard linear programming (LP) minimization problem is written as:

$$
\begin{aligned}
\text{Minimize} \quad & c^T x \\
\text{subject to} \quad & Ax \ge b, \\
& x \ge 0,
\end{aligned}
$$

where:
- $x \in \mathbb{R}^n$ is the decision vector,
- $c \in \mathbb{R}^n$ is the cost vector,
- $A \in \mathbb{R}^{m \times n}$ is the constraint matrix,
- $b \in \mathbb{R}^m$ is the constraint vector.

Geometrically, the constraints define an intersection of half-spaces, forming a convex polyhedron (the feasible region). The objective function defines parallel hyperplanes, and minimizing the cost corresponds to pushing these hyperplanes downward until they first touch the feasible region.

---

## 2. Optimal Solutions Occur at Corners

If an optimal solution exists, it occurs at a **vertex (corner point)** of the feasible polyhedron.

Each vertex corresponds to the intersection of $n$ linearly independent constraint hyperplanes. Algebraically, this means selecting a basis $A_B$ of constraints and solving:

$$
A_B x_B = b_B.
$$

Thus, although the feasible region contains infinitely many points, only finitely many vertices need to be considered.

---

## 3. Simplex Method and Tableau Method

The **Simplex Method** exploits the fact that optimal solutions occur at corners:

1. Start at a feasible corner (basic feasible solution).
2. Move along an edge to a neighboring corner that improves the objective value.
3. Repeat until no improvement is possible.

Each move corresponds to a **change of basis** in a linear system.

The **Tableau Method** is a matrix-based implementation of the simplex method. It organizes constraints, variables, and the objective into a structured augmented matrix.

From the tableau, the **reduced costs** $r_j$ of free variables are visible. For a minimization problem:
- If all $r_j \ge 0$, no variable can reduce the cost further.
- This condition signals optimality and termination of the algorithm.

---

## 4. Primal and Dual Problems

Every minimization LP (the **primal**) has an associated maximization LP (the **dual**).

### Primal
$$
\min \; c^T x \quad \text{s.t.} \quad Ax \ge b, \; x \ge 0
$$

### Dual
$$
\max \; b^T y \quad \text{s.t.} \quad A^T y \le c, \; y \ge 0
$$

The primal variables $x$ and dual variables $y$ live in different vector spaces but are coupled through the matrix $A$ and its transpose.

---

## 5. Strong Duality Theorem

If both the primal and dual have optimal solutions $x^*$ and $y^*$, then:

$$
c^T x^* = b^T y^*.
$$

This means the minimum primal cost equals the maximum dual value. At this point, both problems reach the same equilibrium.

---

## 6. Weak Duality and Its Algebraic Origin

Weak duality states that for any primal-feasible $x$ and dual-feasible $y$:

$$
b^T y \le c^T x.
$$

This follows from:
$$
Ax \ge b, \; y \ge 0 \Rightarrow y^T A x \ge y^T b,
$$
and
$$
A^T y \le c \Rightarrow y^T A x \le c^T x.
$$

Strong duality occurs when this inequality becomes an equality at optimality.

---

## 7. Complementary Slackness

At an optimal solution:
- Some constraints are **tight** (equalities),
- Others are **slack** (strict inequalities).

The **complementary slackness conditions** state:

$$
y_i (Ax - b)_i = 0 \quad \text{for all } i.
$$

Thus:
- If a primal constraint is slack, its corresponding dual variable is zero.
- If a dual constraint is slack, its corresponding primal variable is zero.

This condition has a natural economic interpretation: resources or constraints that are not binding carry no marginal value.

---

## 8. Possible Outcomes of a Primal–Dual Pair

Exactly one of the following situations occurs:

1. Both primal and dual have optimal solutions with equal costs.
2. Neither problem has a feasible solution.
3. One problem has a feasible solution and is unbounded, while the other is infeasible.

Unboundedness in one problem corresponds to infeasibility in the other.

---

## 9. Optimality Conditions

A pair $(x^*, y^*)$ is optimal if and only if all three conditions hold:

1. **Primal feasibility:** $Ax^* \ge b$, $x^* \ge 0$.
2. **Dual feasibility:** $A^T y^* \le c$, $y^* \ge 0$.
3. **Complementary slackness:** $y_i^*(Ax^* - b)_i = 0$.

These conditions parallel the KKT conditions in convex optimization.

---

## 10. Connection to Lagrange Multipliers

The Lagrangian for the primal problem is:

$$
L(x, y) = c^T x - y^T (Ax - b), \quad y \ge 0.
$$

Here, the dual variables $y$ act as **Lagrange multipliers** for the inequality constraints.

Maximizing the Lagrangian with respect to $y$ leads directly to the dual problem. Thus, LP dual variables are exactly Lagrange multipliers from constrained optimization.

---


# Geometry of Corners in the Simplex Method (with Slack Variables)

## Big Picture

The simplex method works by moving between **corner points (vertices)** of a feasible region.
Understanding *why* a corner is obtained by setting exactly $n$ variables to zero after introducing slack variables is a **geometric dimension-counting argument**.

---

## Core Setup

Start with a linear program:

- $n$ original variables: $x \in \mathbb{R}^n$
- $m$ inequality constraints:

$$
  Ax \ge b
$$

Introduce **slack variables** $w \in \mathbb{R}^m$ to convert inequalities to equalities:

$$
Ax - w = b
$$

with nonnegativity constraints:

$$
x \ge 0, \quad w \ge 0
$$

---

## Dimension Counting

After adding slack variables:

- **Total variables:** $n + m$
- **Equality constraints:** $m$
- **Ambient space:** $\mathbb{R}^{n+m}$

---

## Key Geometric Principle

> In a $d$-dimensional space, a corner (vertex) is formed by $d$ independent **active constraints**.

Examples:
- 2D: 2 lines intersect at a point
- 3D: 3 planes intersect at a point
- $(n+m)$D: $n+m$ active constraints are needed

---

## Where the $n+m$ Constraints Come From

In the simplex formulation:

1. The $m$ **equality constraints**

$$
   Ax - w = b
$$

   are always active.

2. To reach a corner in $\mathbb{R}^{n+m}$, we need **$n+m$** active constraints total.

3. Therefore, we need **$n$ additional active constraints**.

These come from **nonnegativity constraints becoming binding**, i.e., setting variables to zero:

$$
x_i = 0 \quad \text{or} \quad w_j = 0
$$

---

## Algebraic Interpretation (Simplex Terminology)

- **Basic variables:** $m$ variables solved from the $m$ equations
- **Nonbasic variables:** $n$ variables fixed at zero

Thus:

$$
(n+m) - m = n
$$

This is why **exactly $n$ variables are set to zero** at a basic feasible solution.

---

## Geometric Interpretation

- The feasible region lives in $\mathbb{R}^{n+m}$.
- The equality constraints restrict it to an $n$-dimensional affine subspace.
- Setting $n$ variables to zero adds $n$ independent constraints.
- Together, these $n+m$ constraints pin down a single point: a **corner**.

---

## Common Pitfalls

- Confusing the dimension of the *original* problem ($n$) with the dimension after adding slacks ($n+m$).
- Thinking slack variables are merely algebraic tricks; they **change the geometry** by lifting the problem into higher dimensions.
- Forgetting that nonnegativity constraints count as geometric constraints when they are active.

---

## One-Line Takeaway

> Adding slack variables moves the feasible region into $\mathbb{R}^{n+m}$; a corner there requires $n+m$ active constraints, of which $m$ come from equalities and the remaining $n$ come from setting variables to zero.


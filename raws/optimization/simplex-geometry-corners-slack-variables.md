# Geometry of Corners in the Simplex Method (with Slack Variables)

## Big Picture

The simplex method works by moving between **corner points (vertices)** of a feasible region.
Understanding why a basis fixes some variables to zero after introducing slack
variables is a **geometric dimension-counting argument**. In a nondegenerate
basic feasible solution, exactly \(n\) variables are zero; degeneracy can make
additional basic variables zero as well.

---

## Core Setup

For the geometric discussion, use the common inequality convention:

- \(n\) original variables: \(x \in \mathbb{R}^n\)
- \(m\) inequality constraints:
  $$
  Ax \le b
  $$

Introduce **slack variables** \(w \in \mathbb{R}^m\) to convert inequalities to equalities:

$$
Ax + w = b
$$

with nonnegativity constraints:

$$
x \ge 0, \quad w \ge 0
$$

If an inequality is written as \(a_i^T x\ge b_i\), conversion instead uses a
surplus variable, \(a_i^T x-w_i=b_i\). A surplus column does not provide the
same identity basis as a slack column, which is one reason Phase I may be
needed.

---

## Dimension Counting

After adding slack variables:

- **Total variables:** \(n + m\)
- **Equality constraints:** \(m\)
- **Ambient space:** \(\mathbb{R}^{n+m}\)

---

## Key Geometric Principle

> In a \(d\)-dimensional affine feasible space, a corner is formed when
> enough independent active constraints remove all remaining feasible
> directions.

Examples:
- 2D: 2 lines intersect at a point
- 3D: 3 planes intersect at a point
- \((n+m)\)D: \(n+m\) independent active constraints are needed in the lifted
  ambient-space count

---

## Where the \(n+m\) Constraints Come From

In the simplex formulation:

1. The \(m\) **equality constraints**
   $$
   Ax + w = b
   $$
   are always active.

2. Assuming the \(m\) equalities are independent, they reduce the lifted \(n+m\)-dimensional space to an \(n\)-dimensional affine space.

3. A nondegenerate basic solution chooses **\(n\)** additional independent active nonnegativity constraints.

These come from **nonnegativity constraints becoming binding**, i.e., setting variables to zero:

$$
x_i = 0 \quad \text{or} \quad w_j = 0
$$

---

## Algebraic Interpretation (Simplex Terminology)

- **Basic variables:** \(m\) variables solved from the \(m\) equations
- **Nonbasic variables:** \(n\) variables fixed at zero

Thus:
$$
(n+m) - m = n
$$

This is why a nondegenerate basic feasible solution has exactly \(n\) zero
variables. In a degenerate basic feasible solution, one or more basic
variables may also be zero, so the total number of zero variables can exceed
\(n\).

---

## Basis exchange and neighboring corners

The basis gives simplex its movement rule. Partition the lifted variables into
basic and nonbasic parts:

$$
B x_B+N x_N=b.
$$

At the current basic feasible solution, \(x_N=0\) and
\(x_B=B^{-1}b\ge0\). To move, choose one nonbasic variable \(x_j=t\) to
enter. Maintaining equality feasibility forces

$$
x_B(t)=B^{-1}b-t(B^{-1}N)_j.
$$

The ratio test finds the largest \(t\ge0\) for which every basic variable
remains nonnegative. The first basic variable to reach zero leaves the basis.
The entering/leaving exchange moves to a neighboring vertex and produces a
new basis. Reduced costs decide whether increasing the entering variable can
improve the objective; their algebra is developed in the [reduced-cost note](simplex-reduced-costs-degeneracy-cycling.md).

If the ratio test returns \(t=0\), the basis may change without geometric
movement. This is a degenerate pivot, and repeated degenerate pivots are the
source of possible cycling.

---

## Geometric Interpretation

- The feasible region lives in \(\mathbb{R}^{n+m}\).
- The equality constraints restrict it to an \(n\)-dimensional affine subspace.
- Setting \(n\) variables to zero adds \(n\) independent constraints.
- Together, these \(n+m\) constraints pin down a single point: a **corner**.

---

## Common Pitfalls

- Confusing the dimension of the *original* problem (\(n\)) with the dimension after adding slacks (\(n+m\)).
- Thinking slack variables are merely algebraic tricks; they **change the geometry** by lifting the problem into higher dimensions.
- Forgetting that nonnegativity constraints count as geometric constraints when they are active.
- Treating a surplus variable from \(a_i^T x\ge b_i\) as if it were an identity-column slack variable.
- Assuming that a basic feasible solution has exactly \(n\) zero variables even when it is degenerate.
- Confusing basic/nonbasic variables with active/inactive constraints; the terms describe related but different structures.

---

## Related material

- [Simplex reduced costs, degeneracy, and cycling](simplex-reduced-costs-degeneracy-cycling.md)
- [Phase I simplex with artificial variables](simplex-phase-i-artificial-variables.md)
- [Linear programming and duality](linear-programming-duality-linear-algebra.md)

---

## One-Line Takeaway

> Adding slack variables lifts the problem into \(\mathbb{R}^{n+m}\). A basis
> supplies \(m\) basic variables and fixes \(n\) nonbasic variables to zero;
> in the nondegenerate case this identifies a corner, while degeneracy may
> make additional basic variables zero.

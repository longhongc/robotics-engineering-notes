# Linear Programming and Duality (Linear Algebra Viewpoint)

These notes summarize linear programming from a linear algebra perspective, emphasizing geometry, matrix structure, and duality.

---

## Sign conventions matter

There is no single visual form that must be called the primal. The dual
objective direction and multiplier signs depend on whether the primal is a
minimization or maximization problem, and on the direction of its
inequalities. The following three forms are common:

| Primal | Dual |
| --- | --- |
| $\min c^T x$, $Ax\ge b$, $x\ge0$ | $\max b^T y$, $A^T y\le c$, $y\ge0$ |
| $\max c^T x$, $Ax\le b$, $x\ge0$ | $\min b^T y$, $A^T y\ge c$, $y\ge0$ |
| $\min c^T x$, $Ax=b$, $x\ge0$ | $\max b^T y$, $A^T y+s=c$, $s\ge0$, $y$ unrestricted |

The first convention is used for the main LP formulation below. The second
is the maximization-primal convention often used when introducing LP duality.
The third is the standard-form convention used by primal-dual interior-point
methods. These are equivalent descriptions after changing inequality signs,
introducing slack variables, or negating the objective, but their multiplier
signs must not be mixed.

## 1. Linear Programming Minimization Problem

A standard linear programming (LP) minimization problem is written as:

$$
\begin{aligned}
\text{Minimize} \quad & c^T x \\\\
\text{subject to} \quad & Ax \ge b, \\\\
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

The same duality can be written with a maximization primal:

$$
\max \; c^T x \quad \text{s.t.} \quad Ax\le b,\;x\ge0
$$

whose dual is

$$
\min \; b^T y \quad \text{s.t.} \quad A^T y\ge c,\;y\ge0.
$$

Here the dual supplies an upper bound on the primal objective, whereas the
dual in the minimization convention supplies a lower bound.

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

For the maximization-primal convention, the same bounding argument reverses
the direction:

$$
Ax\le b,\quad y\ge0
\quad\Longrightarrow\quad
y^T A x\le y^T b,
$$

and if $A^T y\ge c$ with $x\ge0$, then

$$
c^T x\le x^T A^T y=y^T A x\le b^T y.
$$

Thus a feasible dual point provides an upper bound, and the dual minimizes
that bound. This is the direct weighted-constraint interpretation of the
same sign convention derived from the Lagrangian below.

---

## 7. Complementary Slackness

At an optimal solution:
- Some constraints are **tight** (equalities),
- Others are **slack** (strict inequalities).

The **complementary slackness conditions** state:

$$
y_i (Ax - b)_i = 0,
\qquad
x_j\bigl(c-A^T y\bigr)_j=0.
$$

The first equation pairs each primal inequality slack with its dual
multiplier. The second pairs each primal variable with the corresponding dual
inequality slack. Both are needed for the full primal-dual optimality test.

Equivalently, if

$$
u=Ax-b\ge0,
\qquad
s=c-A^T y\ge0,
$$

then complementary slackness is

$$
y_i u_i=0,
\qquad
x_j s_j=0.
$$

The objective gap makes this relationship transparent:

$$
c^T x-b^T y
=x^T s+y^T u.
$$

For primal- and dual-feasible points, every term on the right is
nonnegative. At zero gap, each term must vanish.

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
3. **Complementary slackness:**
   $y_i^*(Ax^* - b)_i=0$ and
   $x_j^*(c-A^T y^*)_j=0$.

These conditions parallel the KKT conditions in convex optimization.

---

## 10. Connection to Lagrange Multipliers

The Lagrangian for the primal problem is:

$$
L(x, y) = c^T x - y^T (Ax - b), \quad y \ge 0.
$$

Here, the dual variables $y$ act as **Lagrange multipliers** for the inequality constraints.

The dual is not obtained by simply maximizing this expression with respect to
$y$. The correct operation depends on whether the primal objective is
minimized or maximized.

For the minimization convention used in this note, primal feasibility gives
$b-Ax\le0$, so

$$
L(x,y)=b^T y+x^T(c-A^T y)\le c^T x.
$$

For a fixed multiplier, define the dual function by eliminating the primal
variable through an infimum:

$$
q(y)=\inf_{x\ge0}L(x,y).
$$

If any component of $c-A^T y$ is negative, the infimum is $-\infty$.
Thus a finite lower-bound certificate requires $A^T y\le c$, in which
case $q(y)=b^T y$. Maximizing this lower bound gives the dual:

$$
\max_{y\ge0}\;q(y)=\max\;b^T y
\quad\text{s.t.}\quad A^T y\le c.
$$

For the maximization-primal convention, use

$$
\max\;c^T x\quad\text{s.t.}\quad Ax\le b,\;x\ge0.
$$

The same expression

$$
L(x,y)=c^T x+y^T(b-Ax)
$$

is now an upper bound on the primal objective. The dual function eliminates
the primal variable through a supremum:

$$
h(y)=\sup_{x\ge0}L(x,y).
$$

This supremum is finite only when $A^T y\ge c$, and then
$h(y)=b^T y$. Minimizing this upper bound gives

$$
\min_{y\ge0}\;h(y)=\min\;b^T y
\quad\text{s.t.}\quad A^T y\ge c.
$$

Finally, for the standard-form equality problem

$$
\min\;c^T x\quad\text{s.t.}\quad Ax=b,\;x\ge0,
$$

the multiplier $y$ is unrestricted because it belongs to an equality
constraint. The infimum construction gives

$$
s=c-A^T y\ge0,
\qquad
x_i s_i=0
$$

at the optimum, and hence

$$
c^T x-b^T y=x^T s.
$$

Thus, LP dual variables are Lagrange multipliers, but the dual objective is
formed by first taking the appropriate infimum or supremum over the primal
variables and then optimizing over feasible multipliers.

---

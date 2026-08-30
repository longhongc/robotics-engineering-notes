# Phase I Simplex: Feasibility Search with Artificial Variables

The simplex method needs a feasible basic solution before it can optimize the
original objective. Sometimes the constraints naturally provide one: for
example, a problem with \(Ax\le b\), \(x\ge0\), and \(b\ge0\) can start at
\(x=0\) with the slack variables as the basic variables. Other constraint
forms do not provide an identity basis, or the obvious starting point is not
feasible.

Phase I solves this initialization problem. It temporarily changes the
objective so that simplex searches for feasibility. Phase II then removes the
temporary variables and optimizes the original objective.

## 1. Why a feasible basis is needed

In standard form,

$$
\min\;c^T x
\quad\text{s.t.}\quad
Ax=b,\;x\ge0,
$$

choose a nonsingular basis matrix \(B\). The corresponding basic solution is

$$
x_B=B^{-1}b,\qquad x_N=0.
$$

It is a basic feasible solution only when \(B^{-1}b\ge0\). Simplex can then
move between neighboring feasible vertices using reduced costs and the ratio
test. If the chosen basis gives a negative basic variable, the ratio-test
logic does not have a feasible starting corner to preserve.

## 2. Converting constraints and identifying artificial variables

The need for an artificial variable depends on the constraint type and the
available basis column. First normalize a row so that its right-hand side has
the intended nonnegative sign; multiplying a row by \(-1\) reverses an
inequality.

| Constraint | Standard-form conversion | Typical initial-basis column |
| --- | --- | --- |
| \(a_i^T x\le b_i\) | \(a_i^T x+s_i=b_i,\;s_i\ge0\) | Slack variable \(s_i\), when \(b_i\ge0\) |
| \(a_i^T x\ge b_i\) | \(a_i^T x-s_i=b_i,\;s_i\ge0\) | No identity column; often needs an artificial variable |
| \(a_i^T x=b_i\) | Keep the equality | No slack column; often needs an artificial variable |

The variable \(s_i\) in the second row is a surplus variable. It is
nonnegative, but its column has a \(-1\) rather than a \(+1\), so it does not
usually provide the initial identity basis. Artificial variables are added
only to rows that still lack a suitable basis column; they are not ordinary
slack variables and should not be added automatically to every constraint.

For example, an equality row can be augmented as

$$
a_i^T x+r_i=b_i,\qquad r_i\ge0.
$$

A greater-than-or-equal row becomes

$$
a_i^T x-s_i+r_i=b_i,\qquad s_i,r_i\ge0.
$$

The artificial variable \(r_i\) supplies the temporary \(+1\) basis column.

## 3. The Phase I auxiliary problem

Let \(r\) collect the artificial variables. Phase I ignores the original
objective \(c^T x\) and solves

$$
\begin{aligned}
\min_{x,r,s}\quad & \mathbf{1}^T r\\
\text{s.t.}\quad & \text{converted constraints with artificial variables},\\
&x,s,r\ge0.
\end{aligned}
$$

At the initial basis, the original variables and nonbasic slack/surplus
variables are set to zero, while the artificial variables take the
right-hand-side values when that produces a feasible starting basis. The
Phase I objective is then rewritten in the current nonbasic coordinates before
the simplex pivots begin.

The only purpose of this objective is to drive every artificial variable to
zero. It does not measure the quality of the original design or control
objective.

## 4. Interpreting the Phase I result

Let \(z_{\mathrm{I}}^\star\) be the optimal Phase I objective.

- If \(z_{\mathrm{I}}^\star>0\), at least one artificial variable must remain
  positive. The original constraints are infeasible.
- If \(z_{\mathrm{I}}^\star=0\), all artificial variables can be zero, so the
  original constraints have a feasible solution. The resulting feasible basis
  is passed to Phase II.

The argument assumes exact arithmetic. In numerical implementations, a
tolerance is used to distinguish a genuinely positive Phase I residual from a
small floating-point value.

## 5. Transition to Phase II

When Phase I reaches zero:

1. Remove the artificial variables from the model and restore the original
   objective \(c^T x\).
2. Keep the non-artificial basic variables and their feasible values.
3. Recompute the reduced costs for the original objective.
4. Continue with the ordinary simplex entering-variable choice and ratio test.

An artificial variable may still be basic with value zero at the end of Phase
I. This is a degenerate basis. If possible, pivot a non-artificial variable
into that row before deleting the artificial column. If the row is redundant,
it can be removed after confirming that the remaining system is consistent.
Simply deleting a positive artificial variable would incorrectly change the
feasible set.

Phase I therefore supplies a feasible starting basis, not necessarily a good
starting point for the original objective. Phase II is still required to solve
the actual optimization problem.

## 6. Relation to the simplex pivot mechanics

Phase I and Phase II use the same basis-exchange machinery:

- choose an improving reduced cost for the current objective;
- allow its nonbasic variable to enter;
- use the ratio test to preserve nonnegativity;
- let the first limiting basic variable leave; and
- update the basis and transformed objective.

Only the objective changes. During Phase I, reduced costs describe improvement
of \(\mathbf{1}^T r\); during Phase II, they describe improvement of \(c^T x\).
The geometric basis-exchange view is developed in the [simplex geometry
note](simplex-geometry-corners-slack-variables.md), while the algebra of
reduced costs and degeneracy is developed in the [reduced-cost
note](simplex-reduced-costs-degeneracy-cycling.md).

## Common pitfalls

- Adding artificial variables to every constraint instead of only the rows
  that lack a suitable initial basis.
- Calling artificial variables slack variables. Slack variables represent
  unused inequality capacity; artificial variables are temporary basis
  scaffolding.
- Treating a zero Phase I objective as optimization of the original objective.
- Declaring feasibility from a merely small residual without choosing a
  numerical tolerance and checking the original constraints.
- Deleting an artificial variable that is still basic without handling its
  zero-valued degenerate row.

## Robotics perspective

Phase I is useful whenever a planning, calibration, or control subproblem has
constraints that are easy to state but difficult to initialize. It separates
the question “does any design satisfy these constraints?” from the question
“which feasible design best meets the real objective?” This separation is
especially useful when a later objective may change but the feasible model
remains the same.

## Related material

- [Geometry of corners in the simplex method](simplex-geometry-corners-slack-variables.md)
- [Simplex reduced costs, degeneracy, and cycling](simplex-reduced-costs-degeneracy-cycling.md)
- [Linear programming and duality](linear-programming-duality-linear-algebra.md)

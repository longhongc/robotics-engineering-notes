# Interior Point Method with Log Barrier and Newton’s Method

This note summarizes the core ideas behind the interior-point (barrier) method for linear programming, focusing on how the log barrier modifies the optimality conditions and how Newton’s method is applied in this context.

---

## 1. Primal–Dual Linear Programming Setup

Consider a linear program in standard (primal) form:

$$
\min \; c^T x
\quad \text{s.t.} \quad
Ax = b,\quad x \ge 0.
$$

The associated dual problem is:

$$
\max \; b^T y
\quad \text{s.t.} \quad
A^T y + s = c,\quad s \ge 0.
$$

The classical Karush–Kuhn–Tucker (KKT) conditions are:

$$
\begin{aligned}
Ax &= b && \text{(primal feasibility)} \\\\
A^T y + s &= c && \text{(dual feasibility)} \\\\
x &\ge 0,\; s \ge 0 && \text{(nonnegativity)} \\\\
x_i s_i &= 0 && \text{(complementary slackness)}.
\end{aligned}
$$

The complementary slackness condition is nonlinear and nonsmooth, which motivates the interior-point approach.

---

## 2. Log-Barrier Formulation

Interior-point methods replace the hard constraint $x \ge 0$ with a smooth barrier.

For a barrier parameter $\mu > 0$, consider the barrier problem:

$$
\min_{x>0} \; c^T x - \mu \sum_{i=1}^n \ln(x_i)
\quad \text{s.t.} \quad
Ax = b.
$$

Key properties of the log barrier:
- As $x_i \to 0^+$, $-\ln(x_i) \to +\infty$.
- Iterates remain strictly inside the feasible region.
- The problem remains smooth for all $x > 0$.

---

## 3. Lagrangian and Stationarity

Introduce Lagrange multipliers $y$ for the equality constraint $Ax=b$.

The Lagrangian is:

$$
\mathcal{L}(x,y)
= c^T x - \mu \sum_{i=1}^n \ln(x_i) + y^T(b - Ax).
$$

Let:
- $X = \operatorname{diag}(x_1,\dots,x_n)$,
- $e = (1,\dots,1)^T$.

Taking the gradient with respect to $x$ and setting it to zero gives the stationarity condition:

$$
c - A^T y - \mu X^{-1} e = 0,
$$

or equivalently,

$$
A^T y + \mu X^{-1} e = c.
$$

The vector $e$ appears because the barrier term is a sum of logarithms; its gradient stacks the terms $\mu/x_i$.

---

## 4. Perturbed Complementary Slackness

Define a dual slack variable:

$$
s = \mu X^{-1} e.
$$

Then:

$$
A^T y + s = c,
\quad
x_i s_i = \mu \;\; \text{for all } i.
$$

Thus, the barrier replaces the exact complementary slackness condition $x_i s_i = 0$ with the smooth, perturbed condition:

$$
x_i s_i = \mu.
$$

As $\mu \to 0$, this converges to the true KKT condition.

---

## 5. Primal–Dual Interior-Point System

The optimality conditions of the barrier problem can be written as:

$$
\begin{cases}
Ax = b, \\\\
A^T y + s = c, \\\\
X s = \mu e, \\\\
x > 0,\; s > 0.
\end{cases}
$$

These equations define the **central path** parameterized by $\mu$.

---

## 6. Newton’s Method in the Interior-Point Context

Interior-point methods apply Newton’s method to the system of equations above.

### Key idea:
Newton’s method is applied **not to the objective directly**, but to the **optimality (KKT) conditions**.

Define a nonlinear function $F(x,y,s)$ collecting the residuals:

$$
F(x,y,s) =
\begin{bmatrix}
Ax - b \\\\
A^T y + s - c \\\\
X s - \mu e
\end{bmatrix}.
$$

At a current iterate $(x^k,y^k,s^k)$, Newton’s method:
1. Linearizes $F$ around the current point.
2. Solves the resulting linear system for a search direction
   $(\Delta x, \Delta y, \Delta s)$.
3. Updates:

$$
x^{k+1} = x^k + \alpha \Delta x,\quad
y^{k+1} = y^k + \alpha \Delta y,\quad
s^{k+1} = s^k + \alpha \Delta s,
$$

with step size $\alpha$ chosen to keep $x^{k+1} > 0$, $s^{k+1} > 0$.

---

## 7. Role of Second Derivatives

For linear programs:
- The objective and constraints are linear.
- Curvature arises entirely from the barrier term.
- This curvature appears in the Newton system through terms involving $X^{-1}$ and $X^{-2}$.

For nonlinear programs (as in general interior-point solvers):
- Newton’s method uses the **Hessian of the Lagrangian**.
- This yields fast (often quadratic) local convergence when second derivatives are accurate.

---

## 8. Conceptual Summary

- The log barrier enforces positivity smoothly and keeps iterates in the interior.
- Complementary slackness is replaced by the smooth condition $x_i s_i = \mu$.
- Newton’s method is applied to the (perturbed) KKT conditions, not to the objective alone.
- As $\mu \to 0$, the iterates approach a true primal–dual optimal solution.

Interior-point methods thus combine barrier functions with Newton’s method to efficiently solve large-scale constrained optimization problems.


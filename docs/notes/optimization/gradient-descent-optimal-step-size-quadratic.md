# Optimal Constant Step Size for Gradient Descent on an SPD Quadratic

Consider the quadratic objective

$$
f(x)=\frac12 x^T A x+b^T x+c,
$$

where $A=A^T\succ0$. The matrix $A$ is the Hessian of $f$. This note
derives the constant step size that gives the fastest worst-case linear
convergence of first-order gradient descent.

The word **optimal** here means optimal among fixed, globally chosen step sizes
for the worst error mode. It does not mean the best step for one particular
initial state, nor does it describe exact line search or accelerated methods.

## 1. Quadratic objective and optimizer

The gradient is

$$
\nabla f(x)=Ax+b.
$$

Because $A\succ0$, the objective has a unique minimizer $x^\star$, found
from $\nabla f(x^\star)=0$:

$$
x^\star=-A^{-1}b.
$$

With the error $e=x-x^\star$, the objective gap is

$$
f(x)-f(x^\star)=\frac12 e^T A e.
$$

The constant $c$ shifts the objective value but does not affect the gradient,
the optimizer, or the iteration dynamics.

## 2. Gradient descent as a linear system

Gradient descent with constant step size $\gamma$ is

$$
x_{k+1}=x_k-\gamma\nabla f(x_k)
=x_k-\gamma(Ax_k+b).
$$

Since $Ax^\star+b=0$, subtracting $x^\star$ gives the error recursion

$$
e_{k+1}=(I-\gamma A)e_k.
$$

Thus gradient descent on an SPD quadratic is a discrete-time linear system with
iteration matrix

$$
M_\gamma=I-\gamma A.
$$

The eigenvalues of $M_\gamma$ are

$$
\mu_i=1-\gamma\lambda_i,
$$

where $\lambda_i$ are the eigenvalues of $A$.

## 3. Eigenmode-by-eigenmode behavior

Since $A$ is symmetric, it has an orthogonal eigendecomposition

$$
A=Q\Lambda Q^T,
\qquad
\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n),
$$

with

$$
0<\lambda_{\min}\le\lambda_i\le\lambda_{\max}.
$$

In eigen-coordinates $y_k=Q^Te_k$, each mode evolves independently:

$$
(y_{k+1})_i=(1-\gamma\lambda_i)(y_k)_i.
$$

A mode shrinks when $|1-\gamma\lambda_i|<1$, changes sign when
$1-\gamma\lambda_i<0$, and grows when $|1-\gamma\lambda_i|>1$.

## 4. Stable step-size range

For convergence of every eigenmode, require

$$
|1-\gamma\lambda_i|<1
\qquad\text{for all }i.
$$

For $\lambda_i>0$, this is equivalent to

$$
0<\gamma<\frac{2}{\lambda_{\max}}.
$$

At the upper endpoint, the mode associated with $\lambda_{\max}$ has
multiplier $-1$, so it does not contract. A step size outside this interval
makes at least one mode unstable.

## 5. Worst-case contraction factor

For a fixed stable step size, the Euclidean error satisfies

$$
\|e_{k+1}\|_2
\le \rho(\gamma)\|e_k\|_2,
$$

where

$$
\rho(\gamma)
=\rho(I-\gamma A)
=\max_i |1-\gamma\lambda_i|.
$$

Because $A$ is symmetric and the function
$\lambda\mapsto|1-\gamma\lambda|$ is convex, the maximum over the interval
$[\lambda_{\min},\lambda_{\max}]$ occurs at an endpoint:

$$
\rho(\gamma)
=
\max\left(
|1-\gamma\lambda_{\min}|,
|1-\gamma\lambda_{\max}|
\right).
$$

The quadratic objective gap contracts in the corresponding energy norm:

$$
f(x_{k+1})-f(x^\star)
\le
\rho(\gamma)^2\bigl(f(x_k)-f(x^\star)\bigr).
$$

## 6. Deriving the optimal constant step size

The minimax choice balances the two endpoint modes. At the optimum, they
have equal magnitude and opposite signs:

$$
1-\gamma^\star\lambda_{\min}
=
-\left(1-\gamma^\star\lambda_{\max}\right).
$$

Solving,

$$
\boxed{
\gamma^\star
=
\frac{2}{\lambda_{\min}+\lambda_{\max}}
}.
$$

The transformed endpoint eigenvalues are then

$$
1-\gamma^\star\lambda_{\min}
=
\frac{\lambda_{\max}-\lambda_{\min}}
{\lambda_{\max}+\lambda_{\min}},
$$

and

$$
1-\gamma^\star\lambda_{\max}
=
-\frac{\lambda_{\max}-\lambda_{\min}}
{\lambda_{\max}+\lambda_{\min}}.
$$

Therefore the optimal worst-case contraction factor is

$$
\boxed{
\rho^\star
=
\frac{\lambda_{\max}-\lambda_{\min}}
{\lambda_{\max}+\lambda_{\min}}
}.
$$

The two extreme modes contract at the same rate; one may alternate sign while
the other does not.

## 7. Condition-number interpretation

For an SPD matrix, the 2-norm condition number is

$$
\kappa=\frac{\lambda_{\max}}{\lambda_{\min}}.
$$

The optimal contraction factor becomes

$$
\boxed{
\rho^\star=\frac{\kappa-1}{\kappa+1}
}.
$$

This explains the effect of conditioning:

- If $\kappa=1$, all curvature directions are identical and
  $\rho^\star=0$; the method reaches the minimizer in one step.
- If $\kappa$ is large, $\rho^\star$ is close to $1$, so many iterations
  are required even with the best constant step size.
- Ill-conditioning means that the quadratic has both shallow and steep
  directions. A single step size must compromise between them.

For a target error reduction, the iteration count therefore grows with the
condition number. This is the spectral reason that preconditioning can improve
gradient descent: it changes the eigenvalue spread before the iteration begins.

## 8. A two-dimensional example

Let

$$
A=
\begin{bmatrix}
1&0\\\\
0&9
\end{bmatrix},
\qquad
f(x)=\frac12x^TAx.
$$

Here,

$$
\lambda_{\min}=1,
\qquad
\lambda_{\max}=9,
$$

so the stable range is

$$
0<\gamma<\frac{2}{9}.
$$

The optimal constant step size is

$$
\gamma^\star=\frac{2}{1+9}=0.2.
$$

The two error modes are transformed by

$$
1-0.2(1)=0.8,
\qquad
1-0.2(9)=-0.8.
$$

Thus the shallow and steep directions contract equally in magnitude, even
though the steep direction alternates sign.

## 9. What this result does and does not say

This result is specifically for fixed-step gradient descent on an unconstrained
quadratic with symmetric positive-definite Hessian.

It does not directly give:

- the best step for a particular current iterate;
- the step chosen by exact line search;
- a schedule for backtracking or diminishing step sizes;
- the rate of momentum or accelerated gradient methods;
- a convergence guarantee for a nonsymmetric, indefinite, or singular Hessian;
- a constrained optimization update.

Exact line search can choose a different step at each iteration based on the
current error. The result here instead chooses one constant step size before the
iteration starts and optimizes its worst eigenmode.

## Robotics perspective

Quadratic objectives arise in least-squares calibration, local trajectory
optimization, inverse-kinematics regularization, and model fitting. Their
Hessian eigenvalues describe curvature in different parameter directions. The
optimal constant step size provides a principled baseline for first-order
iterations, while the condition-number formula explains why scaling,
preconditioning, or better parameterization can be more important than simply
taking more iterations.

## Common pitfalls

- Balancing $\lambda_{\min}$ and $\lambda_{\max}$ directly is wrong. The
  balanced quantities are the iteration eigenvalues
  $1-\gamma\lambda_{\min}$ and $1-\gamma\lambda_{\max}$.
- The formula $2/(\lambda_{\min}+\lambda_{\max})$ is not the same as the
  stability-limit step $2/\lambda_{\max}$.
- The result assumes a constant step size and an SPD Hessian.
- The spectral contraction factor applies to the error norm; the quadratic
  objective gap has the corresponding squared factor.
- A condition number close to one does not mean every arbitrary objective is
  easy; this conclusion is for the quadratic model under discussion.


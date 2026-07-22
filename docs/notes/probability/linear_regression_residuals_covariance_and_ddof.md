# Linear Regression, Residual Geometry, Covariance, and Degrees of Freedom

## 1. Model Setup

We consider the linear model:

$$
y = X\beta + \epsilon
$$

where:

- $y \in \mathbb{R}^n$: observed vector
- $X \in \mathbb{R}^{n \times k}$: design matrix
- $\beta \in \mathbb{R}^k$: parameters
- $\epsilon \in \mathbb{R}^n$: noise vector

Noise properties:

$$
\mathbb{E}[\epsilon] = 0, \quad \mathrm{Cov}(\epsilon) = \Sigma
$$

Special case:

$$
\Sigma = \sigma^2 I
$$

---

## 2. Linear Regression as Orthogonal Projection

Least squares solution:

$$
\hat{y} = X(X^T X)^{-1} X^T y
$$

Define projection matrix:

$$
P = X(X^T X)^{-1} X^T
$$

Properties of P:

- symmetric: $P^T = P$
- idempotent: $P^2 = P$
- projects onto column space of X

---

## 3. Residual Vector as Projection of Noise

Residual vector:

$$
r = y - \hat{y}
$$

Substitute model:

$$
r = (I - P)y
$$

Define residual projection matrix:

$$
M = I - P
$$

So:

$$
r = M y
$$

Substitute model:

$$
y = X\beta + \epsilon
$$

Since:

$$
MX\beta = 0
$$

we obtain:

$$
\boxed{
r = M \epsilon
}
$$

Interpretation:

Residual vector equals the noise vector projected onto the orthogonal complement of column space of X.

---

## 4. Geometry of Residual Space

Space:

$$
\mathbb{R}^n
$$

Column space:

$$
\mathrm{col}(X), \quad \dim = k
$$

Residual space:

$$
\mathrm{col}(X)^\perp, \quad \dim = n-k
$$

Projection matrices:

- P projects onto column space
- M projects onto residual space

Eigenvalues of M:

- 1 (multiplicity n−k)
- 0 (multiplicity k)

---

## 5. Covariance of Residual Vector

General covariance transformation rule:

$$
\mathrm{Cov}(Ax) = A \mathrm{Cov}(x) A^T
$$

Apply to residual:

$$
\mathrm{Cov}(r)
=
M \Sigma M^T
$$

Since M is symmetric:

$$
\boxed{
\mathrm{Cov}(r)
=
M \Sigma M
}
$$

Special case:

If:

$$
\Sigma = \sigma^2 I
$$

then:

$$
\boxed{
\mathrm{Cov}(r) = \sigma^2 M
}
$$

---

## 6. Total Residual Variance (Trace Formula)

Total variance:

$$
\mathrm{trace}(\mathrm{Cov}(r))
=
\mathrm{trace}(M \Sigma M)
$$

Using cyclic trace property:

$$
\boxed{
\mathrm{trace}(\mathrm{Cov}(r))
=
\mathrm{trace}(\Sigma M)
}
$$

Special case:

$$
\mathrm{trace}(\mathrm{Cov}(r))
=
\sigma^2 (n-k)
$$

---

## 7. Degrees of Freedom Interpretation

Residual space dimension:

$$
n - k
$$

This is why variance estimator uses:

$$
\boxed{
\frac{1}{n-k}
}
$$

This corresponds to: `ddof=k` in NumPy.

Example:

- estimating mean only: k = 1 → ddof = 1
- estimating ax+b: k = 2 → ddof = 2

---

## 8. Eigenbasis Interpretation

Choose orthonormal basis aligned with projection:

$$
M =
\begin{bmatrix}
0 & \\\\
& I_{n-k}
\end{bmatrix}
$$

Residual vector has nonzero components only in n−k dimensions.

Variance exists only in those directions.

---

## 9. General Case: Different Noise Variance per Element

If:

$$
\Sigma =
\begin{bmatrix}
\sigma_1^2 & & \\\\
& \sigma_2^2 & \\\\
& & \ddots
\end{bmatrix}
$$

Residual covariance:

$$
\mathrm{Cov}(r) = M \Sigma M
$$

Total residual variance:

$$
\boxed{
\mathrm{trace}(\Sigma M)
}
$$

This is variance of noise projected onto residual space.

---

## 10. Core Concept Summary

Key identity:

$$
\boxed{
r = M \epsilon
}
$$

Key covariance result:

$$
\boxed{
\mathrm{Cov}(r) = M \Sigma M
}
$$

Key variance result:

$$
\boxed{
\mathrm{trace}(\mathrm{Cov}(r)) = \mathrm{trace}(\Sigma M)
}
$$

Key geometric interpretation:

Residual vector is the noise vector projected onto the orthogonal complement of the column space.

Degrees of freedom equals dimension of residual space:

$$
\boxed{
n - k
}
$$

---

## 11. Connection to Monte Carlo and MLMC

This same projection principle explains:

- ddof correction in variance estimation
- variance decomposition in MLMC
- residual variance in regression
- effective degrees of freedom in statistical models

All arise from projecting random vectors into lower-dimensional subspaces.


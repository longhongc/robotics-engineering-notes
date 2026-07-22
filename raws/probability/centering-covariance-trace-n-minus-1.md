# Covariance, Centering, Trace, and the (n−1) Variance Correction

## Overview

This note explains:

* What happens to covariance when subtracting the sample mean
* Why total variance equals the trace of the covariance matrix
* Why centering reduces total variance from (n\sigma^2) to ((n-1)\sigma^2)
* Why we divide by (n-1) instead of (n) when estimating variance
* The difference between coordinate variance and eigenvalue variance

This is fundamental for statistics, covariance estimation, and PCA.

---

# 1. Setup: Independent random variables

Suppose

[
X_1, X_2, \dots, X_n
]

are independent with

[
\mathbb{E}[X_i] = \mu, \quad \mathrm{Var}(X_i) = \sigma^2
]

Define the vector:

[
X =
\begin{bmatrix}
X_1 \
X_2 \
\vdots \
X_n
\end{bmatrix}
\in \mathbb{R}^n
]

Then the covariance matrix is:

[
\mathrm{Cov}(X) = \sigma^2 I
]

This means:

* Each coordinate has variance (\sigma^2)
* Coordinates are independent

Total variance:

[
\mathrm{trace}(\mathrm{Cov}(X)) = n\sigma^2
]

---

# 2. Total variance equals trace of covariance

Key identity:

[
\boxed{
\mathrm{trace}(\mathrm{Cov}(X))
===============================

\mathbb{E}[|X - \mathbb{E}[X]|^2]
}
]

Interpretation:

Trace = total variance across all independent directions.

Trace also equals sum of eigenvalues.

---

# 3. Centering: subtract the sample mean

Define sample mean:

[
\bar X = \frac{1}{n} \sum_{i=1}^n X_i
]

Define centered vector:

[
U =
\begin{bmatrix}
X_1 - \bar X \
\vdots \
X_n - \bar X
\end{bmatrix}
]

This can be written as:

[
U = H X
]

where

[
H =
I - \frac{1}{n}\mathbf{1}\mathbf{1}^T
]

is the centering matrix.

---

# 4. Covariance after centering

Using the covariance transformation rule:

[
\mathrm{Cov}(AX) = A \mathrm{Cov}(X) A^T
]

we get:

[
\mathrm{Cov}(U)
===============

\sigma^2 H
]

where

[
H =
I - \frac{1}{n}\mathbf{1}\mathbf{1}^T
]

---

# 5. Eigenvalues after centering

Key facts about (H):

* (H\mathbf{1} = 0)
* Any vector orthogonal to (\mathbf{1}) is unchanged by (H)

Therefore eigenvalues of (H):

* eigenvalue 1, multiplicity (n-1)
* eigenvalue 0, multiplicity 1

So eigenvalues of covariance:

[
\sigma^2, \dots, \sigma^2 \quad (n-1\ \text{times}), \quad 0
]

---

# 6. Total variance after centering

Trace equals sum of eigenvalues:

[
\boxed{
\mathrm{trace}(\mathrm{Cov}(U))
===============================

(n-1)\sigma^2
}
]

Interpretation:

Centering removes one independent variance direction.

---

# 7. Important: coordinate variance vs eigenvalue variance

Coordinate variance:

[
\mathrm{Var}(X_i - \bar X)
==========================

\frac{n-1}{n}\sigma^2
]

Each coordinate has reduced variance.

Also coordinates are now correlated:

[
\mathrm{Cov}(X_i-\bar X,\ X_j-\bar X)
=====================================

-\frac{1}{n}\sigma^2
\quad (i \neq j)
]

But in the eigenvector basis:

* (n-1) independent directions have variance (\sigma^2)
* 1 direction has variance 0

Trace reflects eigenvalue variance, not coordinate variance.

---

# 8. Geometric interpretation

Centering is a projection onto the hyperplane:

[
{v \mid \mathbf{1}^T v = 0}
]

This hyperplane has dimension (n-1).

Variance in direction (\mathbf{1}) is completely removed.

Remaining directions keep variance (\sigma^2).

---

# 9. Why divide by n−1 when estimating variance

Sample variance:

[
\hat{\sigma}^2
==============

\frac{1}{n-1}
\sum (X_i - \bar X)^2
]

Reason:

Only (n-1) independent deviation directions remain.

If dividing by (n), estimator would underestimate variance.

Dividing by (n-1) gives unbiased estimator.

---

# 10. Summary of key results

Covariance before centering:

[
\mathrm{Cov}(X) = \sigma^2 I
]

Trace before centering:

[
n\sigma^2
]

Covariance after centering:

[
\mathrm{Cov}(U) =
\sigma^2
\left(
I - \frac{1}{n}\mathbf{1}\mathbf{1}^T
\right)
]

Eigenvalues after centering:

[
\sigma^2 \text{ (multiplicity } n-1), \quad 0
]

Trace after centering:

[
(n-1)\sigma^2
]

Coordinate variance after centering:

[
\frac{n-1}{n}\sigma^2
]

Variance exists fully only in (n-1) independent directions.

---

# 11. Core intuition

Centering removes the mean direction.

This removes exactly one independent variance direction.

Total variance decreases from (n\sigma^2) to ((n-1)\sigma^2).

Variance is preserved only in directions orthogonal to the mean direction.

---

# Suggested filename

```
centering-covariance-trace-n-minus-1.md
```


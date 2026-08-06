# Relationship Between Least Squares, MLE, MAP, and Kalman Filter

## 1. Linear Measurement Model

We start with the standard linear model:

\[
y = Hx + \epsilon
\]

where:

* \(y\): measurement vector
* \(H\): measurement matrix
* \(x\): unknown parameter vector
* \(\epsilon\): noise

---

# 2. Maximum Likelihood Estimation (MLE)

Assume Gaussian noise:

\[
\epsilon \sim \mathcal{N}(0, R)
\]

Likelihood:

\[
p(y|x) = \mathcal{N}(Hx, R)
\]

Maximizing likelihood is equivalent to minimizing:

\[
J(x) =
(y - Hx)^T R^{-1} (y - Hx)
\]

Solution:

\[
\hat{x}_{MLE}
=
(H^T R^{-1} H)^{-1}
H^T R^{-1} y
\]

This is called:

**Weighted Least Squares (WLS)**

---

## Special cases

### Case A: White Gaussian noise, equal variance

\[
R = \sigma^2 I
\]

Then:

\[
\hat{x}
=
(H^T H)^{-1} H^T y
\]

This is:

**Ordinary Least Squares (OLS)**

---

### Case B: Gaussian noise, unequal variances or correlated

\[
R \neq \sigma^2 I
\]

Then solution becomes:

**Weighted Least Squares**

Weights are:

\[
R^{-1}
\]

Interpretation:

* Lower variance → higher weight
* Higher variance → lower weight

---

# 3. Maximum A Posteriori Estimation (MAP)

Now assume prior on parameter:

\[
x \sim \mathcal{N}(x_0, P_0)
\]

Posterior:

\[
p(x|y) \propto p(y|x) p(x)
\]

MAP estimate minimizes:

\[
J(x)
=
(y-Hx)^T R^{-1} (y-Hx)
+
(x-x_0)^T P_0^{-1} (x-x_0)
\]

Solution:

\[
\hat{x}_{MAP}
=
(H^T R^{-1} H + P_0^{-1})^{-1}
(H^T R^{-1} y + P_0^{-1} x_0)
\]

---

# 4. MAP = Regularized Least Squares

MAP is equivalent to least squares with regularization.

If:

\[
x_0 = 0
\]

and

\[
P_0 = \frac{1}{\lambda} I
\]

Then:

\[
\hat{x}
=
\arg\min
|y-Hx|^2
+
\lambda |x|^2
\]

This is:

**Ridge Regression (L2 regularization)**

Interpretation:

* Gaussian prior ↔ L2 regularization
* Prior covariance ↔ regularization strength

---

# 5. Kalman Filter = Recursive MAP / Recursive Least Squares

Kalman filter performs the same estimation recursively.

Prior:

\[
x \sim \mathcal{N}(x_{prior}, P_{prior})
\]

Measurement update:

\[
x_{posterior}
=
x_{prior}
+
K(y - H x_{prior})
\]

Kalman gain:

\[
K =
P_{prior} H^T
(H P_{prior} H^T + R)^{-1}
\]

Posterior covariance:

\[
P_{posterior}
=
(I - KH) P_{prior}
\]

---

Interpretation:

Kalman filter is:

* Recursive MAP estimation
* Recursive weighted least squares
* Recursive Bayesian inference

---

# 6. Unified Interpretation Table

| Method                 | Noise assumption             | Prior                      | Interpretation |
| ---------------------- | ---------------------------- | -------------------------- | -------------- |
| Ordinary Least Squares | Gaussian, equal variance     | none                       | MLE            |
| Weighted Least Squares | Gaussian, general covariance | none                       | MLE            |
| Ridge Regression       | Gaussian                     | Gaussian prior             | MAP            |
| Kalman Filter          | Gaussian                     | Gaussian prior (recursive) | Recursive MAP  |

---

# 7. Key Concept: Role of Covariance and Inverse Covariance

Covariance represents uncertainty.

Inverse covariance represents information.

Appears in cost function:

\[
(x-\mu)^T \Sigma^{-1} (x-\mu)
\]

Interpretation:

* Small variance → strong constraint
* Large variance → weak constraint

---

# 8. Complete Unified Cost Function

General estimation problem:

\[
\hat{x}
=
\arg\min
\underbrace{(y-Hx)^T R^{-1} (y-Hx)}*{\text{measurement term}}
+
\underbrace{(x-x_0)^T P_0^{-1} (x-x_0)}*{\text{prior term}}
\]

Cases:

* No prior → MLE / Least Squares
* Gaussian prior → MAP / Ridge
* Recursive prior → Kalman filter

---

# 9. Conceptual Hierarchy

```
Least Squares
    =
Maximum Likelihood (Gaussian noise)

Least Squares + Gaussian Prior
    =
MAP estimation
    =
Ridge Regression

Recursive MAP
    =
Kalman Filter
```

---

# 10. One-Sentence Summary

All these methods estimate parameters by minimizing uncertainty-weighted squared error; they differ only in whether a prior is included and whether estimation is done in batch or recursively.

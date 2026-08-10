# Kalman Measurement Update from MAP: Woodbury and Joseph Forms

The Kalman measurement update can be derived as a Gaussian MAP problem and
then rewritten into the familiar innovation form. Two matrix identities make
the connection useful in practice:

- information-form quantities add directly when a prior and measurement are
  fused;
- the Woodbury matrix identity moves the expensive inverse from state space to
  measurement space.

The covariance update can also be derived directly from the posterior error.
That derivation produces the Joseph form, which is often preferable in finite-
precision implementations.

This note assumes the linear measurement model

$$
y = Hx + v,
\qquad v \sim \mathcal N(0,R),
$$

and a Gaussian prior

$$
x \sim \mathcal N(x^-,P^-).
$$

Here $x^-$ and $P^-$ are the predicted state and covariance, $y$ is the
new measurement, and $R$ is the measurement-noise covariance. The prior
error and measurement noise are assumed to be uncorrelated.

## 1. Gaussian MAP update

The posterior is proportional to the likelihood times the prior:

$$
p(x\mid y) \propto p(y\mid x)p(x).
$$

Taking the negative logarithm and omitting constants gives the quadratic
objective

$$
J(x) =
(y-Hx)^T R^{-1}(y-Hx)
+(x-x^-)^T(P^-)^{-1}(x-x^-).
$$

Setting its gradient to zero gives

$$
x^+
=
\left((P^-)^{-1}+H^TR^{-1}H\right)^{-1}
\left(H^TR^{-1}y+(P^-)^{-1}x^-\right).
$$

This is the batch Gaussian MAP solution for one prior and one measurement.
The Kalman filter uses the same fusion step repeatedly, with the previous
prediction supplying the next prior.

## 2. Information-form interpretation

Define the information matrix and information vector by

$$
\Lambda^-=(P^-)^{-1},
\qquad
\eta^-=(P^-)^{-1}x^-.
$$

The MAP equation becomes

$$
\boxed{\Lambda^+ = \Lambda^- + H^TR^{-1}H}
$$

and

$$
\boxed{\eta^+ = \eta^- + H^TR^{-1}y}.
$$

The posterior mean is then obtained from

$$
x^+=(\Lambda^+)^{-1}\eta^+.
$$

This explains the phrase “information adds”: independent Gaussian sources
contribute additive precision terms. Covariances themselves do not add in
this fusion equation; their inverses do.

The information form is a conceptual and computational alternative to the
covariance form. In numerical code, one normally solves linear systems or
uses factorizations instead of explicitly forming matrix inverses.

## 3. Woodbury reveals the Kalman gain

The MAP covariance appears to require an $n\times n$ inverse in state space:

$$
P^+ =
\left((P^-)^{-1}+H^TR^{-1}H\right)^{-1}.
$$

The Woodbury identity is

$$
(A+UCV)^{-1}
=A^{-1}-A^{-1}U(C^{-1}+VA^{-1}U)^{-1}VA^{-1}.
$$

Use the substitutions

$$
A=(P^-)^{-1},
\qquad U=H^T,
\qquad C=R^{-1},
\qquad V=H.
$$

Then

$$
\boxed{
P^+
=P^- - P^-H^T(HP^-H^T+R)^{-1}HP^-
}.
$$

Define the innovation covariance and Kalman gain:

$$
S=HP^-H^T+R,
\qquad
K=P^-H^TS^{-1}.
$$

The covariance update becomes

$$
P^+=(I-KH)P^-.
$$

The important computational change is that the inverse is now $m\times m$,
where $m$ is the measurement dimension, rather than $n\times n$, where
$n$ is the state dimension. This is especially useful when measurements are
lower-dimensional than the state.

## 4. Recovering the innovation-form state update

The same identity gives

$$
\left((P^-)^{-1}+H^TR^{-1}H\right)^{-1}H^TR^{-1}
=P^-H^T(HP^-H^T+R)^{-1}
=K.
$$

Substitute this into the MAP mean and group the terms multiplying $x^-$:

$$
\begin{aligned}
x^+
&=Ky+(I-KH)x^-\\\\
&=x^-+K(y-Hx^-).
\end{aligned}
$$

The term

$$
r=y-Hx^-
$$

is the innovation, or measurement residual. The Kalman update therefore has
the form

$$
\boxed{x^+=x^-+Kr}.
$$

It is not a separate estimator added to MAP after the fact. Under the stated
linear-Gaussian assumptions, it is the same posterior mean written in a form
that exposes the correction and uses the measurement-space inverse.

## 5. Deriving the Joseph covariance form

The covariance update should follow from the posterior error rather than be
memorized independently. Let

$$
e^- = x-x^-.
$$

Using $y=Hx+v$ and the innovation-form update,

$$
\begin{aligned}
e^+
&=x-x^+\\\\
&=x-x^- -K(y-Hx^-)\\\\
&=(I-KH)e^- -Kv.
\end{aligned}
$$

For uncorrelated $e^-$ and $v$, the covariance rule

$$
\operatorname{Cov}(Au+Bv)
=A\operatorname{Cov}(u)A^T+B\operatorname{Cov}(v)B^T
$$

gives the Joseph form:

$$
\boxed{
P^+
=(I-KH)P^-(I-KH)^T+KRK^T
}.
$$

For the optimal Kalman gain, expanding the Joseph form and using

$$
K(HP^-H^T+R)=P^-H^T
$$

reduces it algebraically to

$$
P^+=(I-KH)P^-.
$$

The compact form is convenient for analysis. The Joseph form makes the two
sources of posterior uncertainty explicit and is often preferred in numerical
implementations because it better preserves symmetry and positive
semidefiniteness under roundoff.

If the prior error and measurement noise are correlated, the cross-covariance
terms do not vanish and the Joseph expression must be extended accordingly.

## 6. What requires Gaussianity?

Several statements that are often grouped together have different assumptions:

| Statement | Required structure |
| --- | --- |
| The weighted least-squares objective is the negative log-likelihood | Gaussian measurement noise |
| The MAP posterior has the quadratic form above | Gaussian prior and likelihood |
| The Kalman gain is the best linear minimum-mean-square-error gain | Appropriate first and second moments; Gaussianity is not required |
| The Kalman estimate is the exact Bayesian posterior mean | Linear-Gaussian model, so Gaussian closure is preserved |
| MAP, MMSE, posterior mean, and posterior mode are identical | The posterior is Gaussian |

Thus the Kalman update can be derived as an optimal linear estimator without
assuming Gaussian distributions. Gaussianity is what upgrades that estimator
to exact Bayesian inference and makes the posterior mean equal its mode.

For a nonlinear measurement, even Gaussian state and noise can produce a
non-Gaussian posterior. For example, $y=x^2+v$ can make both positive and
negative values of $x$ plausible, producing a bimodal posterior. In that
case, posterior mean and MAP need not coincide.

## 7. Scalar intuition

For a direct scalar measurement $y=x+v$, with prior variance $P^-$ and
measurement variance $R$,

$$
K=\frac{P^-}{P^-+R}.
$$

The update is

$$
x^+=(1-K)x^-+Ky.
$$

If $R$ is small, the measurement is reliable and $K$ is close to one. If
$P^-$ is small, the prior is reliable and $K$ is close to zero. The matrix
formula is the multidimensional version of this uncertainty-weighted
compromise.

## Related material

- [Relationship between least squares, MLE, MAP, and Kalman filtering](least_squares_mle_map_kalman_relationship.md)
- [Kalman and Luenberger observers: dynamics versus uncertainty](../control/kalman_and_luenberger_observers.md)
- [Bayesian updating: prior, likelihood, evidence, and posterior](bayesian-updating-prior-likelihood-evidence-posterior.md)
- [Learning issue #26](https://github.com/longhongc/robotics-engineering-notes/issues/26)
- [Learning issue #27](https://github.com/longhongc/robotics-engineering-notes/issues/27)

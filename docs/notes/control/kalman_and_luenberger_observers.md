# Kalman and Luenberger Observers: Dynamics versus Uncertainty

Luenberger observers and Kalman filters share the same basic structure: they
correct a model-based state estimate using an output error. They differ in
what determines the correction gain.

- A Luenberger observer chooses its gain to shape estimation-error dynamics,
  often through pole placement.
- A Kalman filter chooses its gain to minimize estimation-error covariance
  under a model of process and measurement uncertainty.

The Kalman filter is therefore observer-like, but its transient behavior is an
outcome of an uncertainty optimization rather than a set of poles specified
directly by the designer.

## 1. Shared state-estimation structure

Consider the discrete-time state-space model

$$
x_{k+1}=Ax_k+Bu_k+Gw_k,
\qquad
y_k=Cx_k+v_k,
$$

where (w_k) and (v_k) represent process and measurement disturbances.

Both observer types use the innovation

$$
r_k=y_k-C\hat{x}_k.
$$

The correction has the generic form

$$
\text{estimate correction} = L_k r_k.
$$

The shared innovation-feedback structure is why a steady-state Kalman filter
can be viewed as a Luenberger-style observer with a particular fixed gain.

## 2. Luenberger observer: design the error dynamics

A discrete-time Luenberger observer can be written as

$$
\hat{x}_{k+1}
=A\hat{x}_k+Bu_k+L(y_k-C\hat{x}_k).
$$

Ignoring disturbances for the moment, the estimation error

$$
e_k=x_k-\hat{x}_k
$$

evolves according to

$$
e_{k+1}=(A-LC)e_k.
$$

The observer gain (L) is selected so that (A-LC) is stable. If the pair
((A,C)) is observable, the observer poles can often be placed at chosen
locations. This gives direct control over convergence speed, damping, and
transient behavior.

Pole placement does not by itself say how much to trust a noisy measurement
or an uncertain model. Those concerns must be handled separately in the
observer design.

## 3. Kalman observer: optimize uncertainty

The Kalman filter first propagates the state and covariance:

$$
\hat{x}_{k+1}^- = A\hat{x}_k^+ + Bu_k,
$$

$$
P_{k+1}^- = AP_k^+A^T+GQG^T.
$$

The measurement update is

$$
K_k=P_k^-C^T(CP_k^-C^T+R)^{-1},
$$

$$
\hat{x}_k^+=\hat{x}_k^-+K_k(y_k-C\hat{x}_k^-).
$$

The gain is chosen from the predicted uncertainty and measurement uncertainty
to minimize posterior estimation-error covariance. The design pathway is

$$
\boxed{A\;\longrightarrow\;P^-\;\longrightarrow\;K}.
$$

The system dynamics enter through covariance propagation. A Kalman filter does
not ignore observer dynamics; it determines the gain indirectly through the
uncertainty that those dynamics create.

## 4. Comparing the objectives

| Aspect | Luenberger observer | Kalman filter |
| --- | --- | --- |
| Main objective | Shape error dynamics | Minimize estimation-error covariance |
| Gain selection | Pole placement, bandwidth, or another control criterion | Process and measurement uncertainty model |
| Measurement noise | Usually handled by design choices outside pole placement | Enters directly through (R) |
| Model uncertainty | May be treated through robust or ad hoc design | Enters covariance propagation through (Q) |
| Transient behavior | Specified more directly through poles | Emerges from (A,C,Q,R) and covariance recursion |
| Steady-state form | Fixed gain (L) | Fixed gain when the Riccati recursion converges |

The two objectives can agree in a particular design, but they are not the same
optimization problem. A gain that gives attractive poles need not minimize
mean-square error, and a covariance-optimal gain need not give the desired
settling time or bandwidth.

## 5. Interpreting (Q) and (R)

The scalar direct-measurement case makes the trust trade-off visible:

$$
K=\frac{P^-}{P^-+R}.
$$

Larger measurement noise (R) generally reduces the response to the
measurement innovation. Greater predicted uncertainty (P^-) generally makes
the filter rely more strongly on the new measurement.

For a dynamic system, the same intuition is mediated by the full matrices:

- (Q) describes uncertainty injected by the process model and affects the
  next predicted covariance;
- (R) describes measurement uncertainty and affects the innovation
  covariance;
- (A) and (C) determine how uncertainty is propagated and observed.

It is unsafe to interpret a (Q/R) ratio as a universal direct mapping to a
particular observer pole speed. The resulting poles depend on the complete
system and covariance matrices.

In practice, engineers sometimes tune (Q) and (R) to obtain acceptable
transient behavior even when they are not literal physical noise covariances.
That can be useful, but it should be described as observer tuning rather than
as an unchanged statistical model.

## 6. Observability and detectability still matter

Statistical optimization cannot recover information that the measurements do
not contain. An unobservable unstable mode remains a problem for a Kalman
filter, just as it is for a Luenberger observer. The relevant weaker condition
for many Kalman stability results is detectability: unstable modes must be
observable enough for the estimator to correct them.

This is an important boundary on the phrase “optimal observer.” Kalman
optimality means optimal with respect to a specified covariance objective and
model; it does not remove the structural requirements of state estimation.

## 7. Bayesian and linear-estimation interpretations

For a linear-Gaussian model, the Kalman estimate is simultaneously the
posterior mean, the MMSE estimate, and the MAP estimate because the posterior
is Gaussian. The covariance update can also be derived as the best linear
minimum-mean-square-error update without requiring Gaussian distributions.

This separates two ideas that are often conflated:

1. innovation feedback is the observer structure shared by Kalman and
   Luenberger designs;
2. covariance minimization is the statistical criterion that selects the
   Kalman gain.

The detailed matrix derivation is in [Kalman measurement update from MAP:
Woodbury and Joseph forms](../probability/kalman_measurement_update_map_woodbury_joseph_forms.md).

## Related material

- [Kalman measurement update from MAP: Woodbury and Joseph forms](../probability/kalman_measurement_update_map_woodbury_joseph_forms.md)
- [Relationship between least squares, MLE, MAP, and Kalman filtering](../probability/least_squares_mle_map_kalman_relationship.md)
- [Learning issue #27](https://github.com/longhongc/robotics-engineering-notes/issues/27)
- [Learning issue #28](https://github.com/longhongc/robotics-engineering-notes/issues/28)


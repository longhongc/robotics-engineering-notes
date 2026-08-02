# Zero-Input, Zero-State, Transient, and Steady-State Responses

Several response terms appear together in control and dynamics, but they
answer different questions. **Zero-input versus zero-state** classifies a
response by its cause. **Transient versus steady-state** classifies it by its
behavior over time. These are two different decompositions of the same total
response.

## 1. Linear state-space model

Consider the continuous-time LTI system

$$
\dot{x}(t)=Ax(t)+Bu(t),\qquad
y(t)=Cx(t)+Du(t),
$$

with initial state $x(0)=x_0$. The state-transition matrix is

$$
\Phi(t)=e^{At}.
$$

The state solution is

$$
x(t)
=\Phi(t)x_0
+\int_0^t\Phi(t-\tau)Bu(\tau)\,d\tau.
$$

Therefore, the output is

$$
y(t)
=C\Phi(t)x_0
+\int_0^t C\Phi(t-\tau)B u(\tau)\,d\tau
+D u(t).
$$

This formula already exposes the two causal sources of the response.

## 2. Zero-input and zero-state responses

### Zero-input response

Set the external input to zero while preserving the initial state:

$$
u(t)=0,\qquad
y_{\mathrm{ZI}}(t)=C\Phi(t)x_0.
$$

This is the response of the system's own modes to an initial displacement,
velocity, stored energy, or other initial state. For an asymptotically stable
system, it normally decays and is therefore transient.

### Zero-state response

Set the initial state to zero while preserving the input:

$$
x_0=0,\qquad
y_{\mathrm{ZS}}(t)
=\int_0^t C\Phi(t-\tau)B u(\tau)\,d\tau
+D u(t).
$$

The convolution term is the input-driven response filtered by the system's
state dynamics. It is not automatically the steady-state response: it can
contain both input-driven transients and a long-term component.

The total response is the causal sum

$$
\boxed{y(t)=y_{\mathrm{ZI}}(t)+y_{\mathrm{ZS}}(t)}.
$$

## 3. Transient and steady-state responses

The transient/steady-state distinction asks how the response behaves as time
passes:

- The **transient response** is the part that decays or otherwise represents
  the short-term adjustment after an initial condition or input change.
- The **steady-state response** is the long-term behavior that remains after
  transients have decayed, when such a limit or repeating pattern exists.

The two classifications are independent:

| Classification | Question | Parts |
| --- | --- | --- |
| Causal | What caused the response? | Zero-input and zero-state |
| Asymptotic | What happens at long time? | Transient and steady-state |

For a stable system with a settled input, the zero-input response is usually
transient. The zero-state response can still contain a transient caused by the
system poles and a steady-state component caused by the sustained input.

The steady-state part is not guaranteed to exist. Unstable systems can grow,
marginally stable systems can fail to converge, and inputs that never settle
can produce a response with no single steady value.

## 4. First-order example

Consider

$$
\dot{y}=-y+u,\qquad y(0)=0,
$$

with a unit-step input $u(t)=1$ for $t\geq0$. The transfer function is

$$
G(s)=\frac{1}{s+1}.
$$

The complete response is

$$
y(t)=1-e^{-t}.
$$

Because the initial state is zero, the entire response is zero-state response.
However, it still has two time-behavior components:

$$
\underbrace{-e^{-t}}_{\text{transient}}
\;+\;
\underbrace{1}_{\text{steady state}}.
$$

Thus, zero-state does not mean steady-state.

If instead $y(0)=2$ while the same input is applied, then

$$
y_{\mathrm{ZI}}(t)=2e^{-t},\qquad
y_{\mathrm{ZS}}(t)=1-e^{-t},
$$

and

$$
y(t)=1+e^{-t}.
$$

The total transient is now $e^{-t}$, which is formed from a zero-input
transient and a zero-state transient. This is why the two decompositions
should not be identified with each other.

## 5. Connection to Laplace transforms

For zero initial conditions, the convolution theorem turns the zero-state
response into multiplication in the $s$-domain:

$$
Y(s)=G(s)U(s),
\qquad
G(s)=C(sI-A)^{-1}B+D.
$$

With a nonzero initial state, the transformed output contains an additional
initial-condition term:

$$
Y(s)
=C(sI-A)^{-1}x_0+G(s)U(s).
$$

This is why transfer functions describe input-to-output behavior under zero
initial conditions, while state-space solutions are the more direct language
for tracking both initial conditions and external inputs.

Laplace transforms are therefore not an unrelated alternative to the
state-space solution. They provide an algebraic representation of the
convolution in the zero-state response.

## 6. Why the distinction matters in control

The distinction helps answer different engineering questions:

- Initial-condition response reveals natural modes, stability, and stored
  energy.
- Zero-state response reveals how commands, disturbances, and sensor inputs
  are filtered by the system.
- Transient behavior determines settling, overshoot, ringing, and recovery.
- Steady-state behavior determines tracking error, disturbance rejection, and
  frequency-response gain.

For robotics, a rapid trajectory change may excite a transient even when the
command is not periodic. A periodic command may instead produce a large
steady-state response near a resonance. The same hardware can therefore
require both transient and steady-state analysis.

## Common confusions

- Zero-state response means zero initial state, not zero transient.
- Zero-input response means zero external input, not zero output.
- The convolution term is the input-driven response; it is not automatically
  the steady-state response.
- A Bode plot describes steady-state sinusoidal gain, while a step response
  primarily exposes transient behavior.
- The existence of a steady-state response depends on system stability and
  input behavior.

## Related material

- [Matrix exponential properties](matrix-exponential-properties.md)
- [Solutions of linear difference and differential equations](solutions-of-linear-difference-and-differential-equations.md)
- [Linear systems, eigenvectors, and exponential solutions](linear-systems-eigenvectors-and-exponential-solutions.md)
- [Natural, damped, and resonant frequencies](second-order-system-frequencies-and-resonance.md)
- [Learning issue #17](https://github.com/longhongc/robotics-engineering-notes/issues/17)

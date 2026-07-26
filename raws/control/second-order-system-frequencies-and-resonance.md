# Natural, Damped, and Resonant Frequencies in Second-Order Systems

Second-order systems use several related frequency terms that describe
different phenomena. The **undamped natural frequency** describes the system's
baseline oscillatory scale, the **damped natural frequency** describes
decaying transient oscillations, and the **resonance frequency** describes a
peak in the steady-state response to sinusoidal forcing.

These frequencies may be numerically close when damping is small, but they are
not interchangeable.

## 1. Standard second-order model

Consider the normalized second-order system

\[
\ddot{q}+2\zeta\omega_0\dot{q}+\omega_0^2q=u,
\]

where:

- \(\omega_0>0\) is the undamped natural frequency in rad/s;
- \(\zeta\geq0\) is the damping ratio; and
- \(u(t)\) is an external input.

With zero initial conditions, the transfer function from \(u\) to \(q\) is

\[
G(s)=\frac{Q(s)}{U(s)}
=\frac{1}{s^2+2\zeta\omega_0s+\omega_0^2}.
\]

The formulas below assume this displacement-like output and a constant
numerator. Other outputs, such as velocity or acceleration, can have different
frequency-response peaks.

## 2. Undamped and damped natural frequencies

The poles are the roots of the characteristic equation

\[
s^2+2\zeta\omega_0s+\omega_0^2=0.
\]

For the underdamped case \(0<\zeta<1\),

\[
s_{1,2}
=-\zeta\omega_0
\pm i\omega_0\sqrt{1-\zeta^2}.
\]

This motivates the **damped natural frequency**

\[
\boxed{\omega_d=\omega_0\sqrt{1-\zeta^2}}.
\]

The free response has the form

\[
q_{\mathrm{transient}}(t)
=e^{-\zeta\omega_0t}
\left(C_1\cos(\omega_dt)+C_2\sin(\omega_dt)\right).
\]

Thus:

- \(\omega_d\) is the frequency of the decaying transient oscillation;
- \(\zeta\omega_0\) is the exponential decay rate; and
- \(\omega_0\) is the corresponding frequency when damping is removed.

When \(\zeta=0\), the oscillation is undamped and
\(\omega_d=\omega_0\). When \(\zeta\geq1\), the poles are real and there is no
oscillatory transient, so the usual real-valued \(\omega_d\) interpretation no
longer applies.

## 3. Resonance belongs to the forced response

For a sinusoidal input \(u(t)=U\sin(\omega t)\), the steady-state output has
the same input frequency:

\[
q_{\mathrm{steady-state}}(t)
=A(\omega)\sin(\omega t+\phi(\omega)).
\]

The amplitude ratio is the frequency-response magnitude

\[
|G(i\omega)|
=\frac{1}{
\sqrt{(\omega_0^2-\omega^2)^2
+(2\zeta\omega_0\omega)^2}}.
\]

The **resonance frequency** \(\omega_r\), when it exists as a nonzero peak, is
the input frequency that maximizes this magnitude. It describes forced
steady-state behavior, not the frequency of the decaying transient.

### Derivation of the resonance-frequency formula

To maximize \(\lvert G(i\omega)\rvert\), minimize its squared denominator.
Define the dimensionless frequency ratio

\[
r=\frac{\omega}{\omega_0}.
\]

Ignoring the constant factor \(\omega_0^4\), the squared denominator is

\[
D(r)
=(1-r^2)^2+4\zeta^2r^2
=1+(4\zeta^2-2)r^2+r^4.
\]

Differentiate with respect to \(r\):

\[
\frac{dD}{dr}
=4r\left(r^2+2\zeta^2-1\right).
\]

Apart from the zero-frequency point \(r=0\), the stationary point is

\[
r^2=1-2\zeta^2.
\]

A positive stationary frequency exists only when
\(\zeta<1/\sqrt{2}\). Therefore, for the displacement transfer function
above,

\[
\boxed{\omega_r=\omega_0\sqrt{1-2\zeta^2}},
\qquad
0\leq\zeta<\frac{1}{\sqrt{2}}.
\]

For \(\zeta\geq1/\sqrt{2}\), the response has no nonzero resonance peak; its
largest displacement gain occurs at zero frequency. At \(\zeta=0\), the ideal
model has an infinite gain at \(\omega=\omega_0\), which is the mathematical
resonance of an undamped oscillator.

The formula is therefore not a universal property of every second-order
quantity. It depends on the chosen input-output transfer function and on the
damping range.

## 4. Comparing the three frequencies

For the standard displacement response:

| Quantity | Meaning | Condition |
| --- | --- | --- |
| \(\omega_0\) | Undamped natural frequency | Defined by the denominator |
| \(\omega_d\) | Decaying transient oscillation frequency | \(0<\zeta<1\) |
| \(\omega_r\) | Nonzero steady-state displacement-gain peak | \(0\leq\zeta<1/\sqrt{2}\) |

For small positive damping,

\[
\omega_r
=\omega_0\sqrt{1-2\zeta^2}
<
\omega_d
=\omega_0\sqrt{1-\zeta^2}
<
\omega_0.
\]

For example, with \(\zeta=0.2\),

\[
\omega_d\approx0.980\,\omega_0,
\qquad
\omega_r\approx0.959\,\omega_0.
\]

They are close numerically, but one belongs to the transient poles and the
other belongs to the forced-response gain curve.

## 5. Total response to a sinusoidal input

The response to a sinusoidal input is the sum of transient and steady-state
parts:

\[
q(t)
=q_{\mathrm{transient}}(t)
+q_{\mathrm{steady-state}}(t).
\]

The transient part depends on initial conditions and decays when
\(\zeta>0\). It oscillates at \(\omega_d\). The steady-state part remains after
the transient has decayed and oscillates at the input frequency \(\omega\).

Consequently:

- a Bode magnitude plot describes the steady-state response as \(\omega\)
  varies;
- a step or impulse response shows transient ringing governed by
  \(\omega_d\); and
- a large Bode peak near \(\omega_r\) does not mean that the transient itself
  oscillates at \(\omega_r\).

## 6. Robotics relevance

These distinctions matter when analyzing:

- flexible joints and compliant transmissions;
- vibration after a rapid trajectory change;
- actuator and sensor mounting resonances;
- controller bandwidth and gain selection; and
- trajectory commands that excite lightly damped modes.

A robot can show transient ringing after a step or trajectory update even when
the commanded motion contains no sinusoid. Conversely, a periodic command can
produce a large steady-state response near a resonance peak even though the
system's transient frequency is \(\omega_d\).

The frequencies are properties of a model and an input-output choice. Measured
hardware resonances may also shift with payload, configuration, friction,
sampling, and closed-loop controller gains.

## Common confusions

Use the source of the observation to choose the relevant frequency:

| Observation | Relevant quantity | Why |
| --- | --- | --- |
| Poles of the second-order denominator | \(\omega_0\) and \(\omega_d\) | They determine the free-response modes |
| Ringing after a step or impulse | \(\omega_d\) | This is transient behavior |
| Peak in a displacement Bode magnitude plot | \(\omega_r\) | This is steady-state forced response |
| Periodic command exciting a flexible mode | Input frequency near \(\omega_r\) | The forcing frequency can produce a large finite gain |

Three cautions prevent the most common mistakes:

- The transient pole frequency is \(\omega_d\) when damping is present; the
  undamped reference value is \(\omega_0\).
- A step response primarily reveals \(\omega_d\), not directly \(\omega_r\).
- The formula for \(\omega_r\) assumes the standard displacement transfer
  function. Changing the output or adding zeros changes the frequency at which
  the magnitude peaks.

Positive damping makes the ideal steady-state sinusoidal gain finite. A lightly
damped system can still have a large finite peak and require careful excitation
avoidance.

## Related material

- [Stability from trace and determinant](stability-trace-determinant.md)
- [Dominant eigenvalues and qualitative behavior](dominant-eigenvalues-qualitative-behavior-linear-systems.md)
- [Linear systems, eigenvectors, and exponential solutions](linear-systems-eigenvectors-and-exponential-solutions.md)
- [Matrix exponential properties](matrix-exponential-properties.md)
- [Complex exponentials and physical meaning](../modeling/dynamics/complex-exponential-derivative-physical-meaning.md)
- [Learning issue #5](https://github.com/longhongc/robotics-engineering-notes/issues/5)

# Diagonalization, Jordan Form, and Geometric Meaning

This note summarizes the geometric and algebraic meaning of diagonalization, non-diagonalizability, Jordan form, rotation, and inner-product preservation.

---

## 1. Diagonalizable Matrices

A square matrix \(A \in \mathbb{C}^{n \times n}\) is **diagonalizable** if there exist \(n\) linearly independent eigenvectors.

Formally, this means:
\[
A = PDP^{-1}
\]
where \(D\) is diagonal and the columns of \(P\) are eigenvectors.

### Geometric interpretation
- The vector space can be decomposed into \(n\) independent directions.
- Each direction evolves **by itself**:
\[
Av_i = \lambda_i v_i
\]
- No direction influences or feeds into another.
- The transformation is a combination of independent scalings (and possibly complex rotations).

Diagonalization represents **complete decoupling of directions**.

---

## 2. Non-Diagonalizable Matrices and Jordan Blocks

A matrix is **not diagonalizable** when it does not have enough independent eigenvectors.

Over \(\mathbb{C}\), every matrix is similar to a **Jordan matrix**:
\[
A = PJP^{-1}
\]

A non-diagonalizable matrix has at least one **Jordan block** of size \(\ge 2\):
\[
J = 
\begin{bmatrix}
\lambda & 1 \\
0 & \lambda
\end{bmatrix}
\]

### Geometric interpretation
- Directions are **algebraically coupled**.
- One direction is dragged along by another.
- This coupling produces **shear-type behavior**.
- The transformation cannot be decomposed into independent one-dimensional actions.

Jordan blocks represent **intrinsic entanglement of directions**.

### Dynamical interpretation: a chain of feedback-integrator stages

The same \(2\times2\) Jordan block can be read as a continuous-time
state-space model:

\[
\dot{x}=Jx,\qquad
J=
\begin{bmatrix}
\lambda & 1\\
0 & \lambda
\end{bmatrix}.
\]

Writing the rows separately gives

\[
\dot{x}_1=\lambda x_1+x_2,\qquad
\dot{x}_2=\lambda x_2.
\]

Each state equation contains an integrator in feedback with gain \(\lambda\).
The second state evolves as an ordinary first-order mode, while \(x_2\) also
drives the equation for \(x_1\). The coupling is one-way: \(x_2\) drives
\(x_1\), not the reverse.

![Block diagram of a two-state Jordan chain as feedback-integrator stages](assets/jordan-block-integrator-chain.png)

*The diagram is drawn in generalized-eigenvector coordinates. The
superdiagonal \(1\) is a coordinate normalization, not necessarily a literal
physical gain or physical wiring in the original system.*

For a three-state block, the same pattern continues:

\[
\dot{x}_1=\lambda x_1+x_2,\qquad
\dot{x}_2=\lambda x_2+x_3,\qquad
\dot{x}_3=\lambda x_3.
\]

The last state contributes an \(e^{\lambda t}\) term. Each preceding state
integrates a signal containing that same exponential, producing

\[
e^{\lambda t},\qquad
te^{\lambda t},\qquad
\frac{t^2}{2!}e^{\lambda t},\ldots
\]

This is the dynamical reason a defective repeated mode produces
polynomial-times-exponential terms. A diagonal matrix would instead describe
independent modal coordinates, with no one-way generalized-eigenvector
coupling.

### Why the polynomial factor appears

The \(t\) factor can be derived directly from the two-state chain. Since

\[
\dot{x}_2=\lambda x_2,
\]

we have

\[
x_2(t)=c_2e^{\lambda t}.
\]

Substituting this into the first state equation gives

\[
\dot{x}_1-\lambda x_1=c_2e^{\lambda t}.
\]

Multiplication by the integrating factor \(e^{-\lambda t}\) produces

\[
\frac{d}{dt}\left(e^{-\lambda t}x_1\right)=c_2.
\]

After integration,

\[
x_1(t)=(c_1+c_2t)e^{\lambda t}.
\]

Thus the exponential comes from the repeated eigenvalue, while the polynomial
factor comes from integrating a signal that already contains that same
exponential mode. Each additional link in a longer Jordan chain performs
another such integration, producing the successive powers of \(t\).

The same result appears immediately at the matrix level. Write a Jordan block
of size \(m\) as

\[
J_m(\lambda)=\lambda I+N,
\qquad N^m=0,
\]

where \(N\) contains the superdiagonal ones. Because \(\lambda I\) commutes
with \(N\),

\[
e^{J_m(\lambda)t}
=e^{\lambda t}e^{Nt}
=e^{\lambda t}
\sum_{k=0}^{m-1}\frac{t^k}{k!}N^k.
\]

The series terminates because \(N\) is nilpotent. Therefore a size-\(m\)
Jordan block can contribute terms through \(t^{m-1}e^{\lambda t}\), with the
factorials coming from the exponential Taylor series. For a real system with
complex \(\lambda\), conjugate terms combine into real oscillatory
polynomial–exponential responses.

### Forced ODEs and the null-space viewpoint

The same idea explains the standard repeated-mode rule for a forced linear
differential equation. Let \(L\) be a linear differential operator. Its
homogeneous solutions form the null space

\[
\ker L=\{x:L[x]=0\}.
\]

If \(L[x_p]=f\), then adding any homogeneous solution leaves the forcing
unchanged:

\[
L[x_p+x_h]=L[x_p]+L[x_h]=f.
\]

A candidate particular solution with the same form as a homogeneous mode fails
when that form lies in \(\ker L\), because \(L\) maps it to zero rather than to
the nonzero forcing. Multiplying the candidate by \(t\), or by a sufficiently
high power of \(t\) when the mode is repeated, supplies a form outside the
null space. The required power is determined by the multiplicity of the
overlap, not merely by the fact that an eigenvalue is repeated.

This is the differential-equation counterpart of the Jordan-chain calculation:
the generalized mode is created by solving one more forced equation along the
chain. The detailed undamped-resonance calculation is given in the [second-order
resonance note](../control/second-order-system-frequencies-and-resonance.md).

---

## 3. Rotation and Complex Eigenvalues

Rotation does **not** come from Jordan blocks.

A real rotation matrix typically has **no real eigenvectors** (except for trivial angles).
However, over \(\mathbb{C}\), it has complex conjugate eigenvalues:
\[
\lambda = a \pm bi
\]

### Interpretation
- Complex eigenvalues correspond to **rotation or spiral motion**.
- If \(|\lambda| = 1\), the motion is pure rotation.
- If \(|\lambda| \ne 1\), the motion is a spiral (rotation + scaling).

Rotation matrices are **diagonalizable over \(\mathbb{C}\)**.

---

## 4. Real Canonical Form vs Jordan Form

When restricting to real matrices, complex eigenvalues cannot appear on the diagonal.
Instead, each conjugate pair becomes a real \(2 \times 2\) block:
\[
\begin{bmatrix}
a & -b \\
b & a
\end{bmatrix}
\]

### Important distinction
- This is **not a Jordan block**.
- It represents rotation (and possibly scaling), not shear.
- The matrix is still diagonalizable over \(\mathbb{C}\), but not over \(\mathbb{R}\).

Jordan blocks indicate **defectiveness**; real rotation blocks do not.

---

## 5. Inner Product Preservation

A matrix preserves the inner product if:
\[
\langle Ax, Ay \rangle = \langle x, y \rangle
\]

Such matrices are:
- **Orthogonal** over \(\mathbb{R}\)
- **Unitary** over \(\mathbb{C}\)

### Geometric meaning
- Lengths and angles are preserved.
- No stretching, collapsing, or shearing occurs.
- Transformations are rigid motions: rotations and reflections.

Inner-product preservation is **independent of diagonalizability**.

---


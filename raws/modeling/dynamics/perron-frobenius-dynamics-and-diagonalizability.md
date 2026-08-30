# Perron–Frobenius Theorem: Dynamics and Diagonalizability

## Core question

When analyzing the iteration

$$
x_{k+1}=Ax_k,
$$

do we need to assume that $A$ is diagonalizable in order to conclude Perron–Frobenius-type long-term behavior?

**No.** Full diagonalizability is not required. For the rank-one asymptotic
limit, the relevant condition is that the dominant eigenvalue $r$ is
algebraically simple and strictly dominant:

$$
|\lambda|<r
\qquad\text{for every other eigenvalue }\lambda.
$$

Primitivity is a convenient nonnegative-matrix assumption that guarantees
both properties.

---

## Setting

Let $A$ be a nonnegative square matrix, and let

$$
r=\rho(A)
$$

be its spectral radius. The Perron–Frobenius theorem provides positive right and left eigenvectors for the Perron eigenvalue:

$$
Av=rv,
\qquad
w^T A=rw^T.
$$

The assumptions on $A$ determine whether $r$ is strictly dominant:

| Assumption | Consequence for the peripheral spectrum |
|---|---|
| $A>0$, or more generally $A$ primitive | $r$ is the only eigenvalue with modulus $r$ |
| $A$ irreducible with period $h>1$ | There are $h$ eigenvalues on the circle $\lvert\lambda\rvert=r$ |

Here, primitive means that $A^m>0$ entrywise for some positive integer $m$. Every positive matrix is primitive. For the rank-one limit, strict peripheral separation must be combined with the simplicity of $r$; primitivity supplies both. Irreducibility alone does not guarantee a single dominant mode in discrete time.

---

## What Perron–Frobenius guarantees

For an irreducible nonnegative matrix:

- $r$ is real and strictly positive;
- $r$ is algebraically simple;
- there are strictly positive right and left Perron eigenvectors $v$ and $w$;
- the remaining eigenvalues satisfy $\lvert\lambda\rvert\le r$.

If $A$ is primitive, the inequality is strict for every other eigenvalue:

$$
\lvert\lambda_i\rvert<r,
\qquad i\ne\mathrm{PF}.
$$

For an irreducible matrix of period $h>1$, the other peripheral eigenvalues prevent ordinary convergence to one direction. They instead produce periodic or oscillatory behavior.

---

## Left and right eigenvectors: detector and reconstruction

For a nonsymmetric matrix, a right eigenvector describes the direction of a mode, while a left eigenvector measures how much of that mode is present. Scale $v$ and $w$ so that

$$
w^T v=1.
$$

Then

$$
P=vw^T
$$

is the rank-one spectral projector associated with the simple eigenvalue $r$. Applied to a state $x$, it works in two steps:

$$
Px=vw^Tx=v\underbrace{(w^Tx)}_{\text{modal coefficient}}.
$$

The left eigenvector $w$ is therefore the **detector** for the mode, and the right eigenvector $v$ is the **reconstruction direction**.

For a diagonalizable matrix with right eigenvectors $v_i$, collect them into $V$:

$$
A=V\Lambda V^{-1}.
$$

The rows of $V^{-1}$ are the corresponding left eigenvectors $w_i^T$. With the dual normalization

$$
w_i^T v_j=\delta_{ij},
$$

the decomposition becomes

$$
A=\sum_i \lambda_i v_iw_i^T,
\qquad
A^k=\sum_i \lambda_i^k v_iw_i^T.
$$

The orthogonal case is a special simplification. For a real symmetric matrix, $w_i=v_i$, so the projectors are $v_iv_i^T$. For a general nonsymmetric matrix, the eigenbasis can be oblique and $w_i$ usually differs from $v_i$.

This left–right expansion resembles an SVD rank-one expansion, but the constructions are different: an SVD always exists and uses orthonormal singular vectors, whereas a complete eigenvector expansion requires diagonalizability.

---

## Why diagonalizability is not required

If $A$ is primitive, $r$ is a simple strictly dominant eigenvalue. Even if the remaining part of $A$ contains Jordan blocks, its powers have the form

$$
A^k=r^kP+R_k,
\qquad
P=vw^T,
$$

where, for some constants $C>0$ and integer $q\ge0$,

$$
\lVert R_k\rVert\le Ck^q\rho^k
$$

for a number $\rho<r$. The polynomial factor comes from defective Jordan blocks. It cannot overcome the exponential gap because

$$
k^q\left(\frac{\rho}{r}\right)^k\longrightarrow0.
$$

Consequently,

$$
\frac{A^k}{r^k}\longrightarrow vw^T.
$$

The limit is a spectral projection, so it does not require an eigenvector expansion for every eigenvalue.

For a nonzero initial state $x_0\ge0$, positivity of $w$ gives $w^Tx_0>0$, and therefore

$$
A^kx_0
=r^k v(w^Tx_0)+o(r^k).
$$

The dominant direction is $v$, while $w^Tx_0$ determines how strongly the initial state excites that direction. For a signed initial state, this coefficient can be zero, in which case the dominant term is absent for that particular state.

---

### Why simplicity matters

A strict separation in modulus from the other *distinct* eigenvalues is not
enough if the dominant eigenvalue itself has a nontrivial Jordan block. For
example,

$$
A=
\begin{bmatrix}
1&1&0\\
0&1&0\\
0&0&0
\end{bmatrix}
$$

has spectral radius $r=1$, with the other eigenvalue $0$ strictly inside the
spectral circle. However, the eigenvalue $1$ is defective, and

$$
A^k=
\begin{bmatrix}
1&k&0\\
0&1&0\\
0&0&0
\end{bmatrix}.
$$

The factor $k$ comes from the Jordan block at the dominant eigenvalue, so
$A^k/r^k$ does not converge to a finite rank-one projector. This is why the
dominant eigenvalue must be algebraically simple. For a primitive nonnegative
matrix, Perron–Frobenius rules out this failure by making $r$ algebraically
simple.

## Primitive versus irreducible dynamics

The distinction matters in discrete-time systems. Consider the irreducible nonnegative matrix

$$
A=\begin{bmatrix}0&1\\1&0\end{bmatrix}.
$$

It has eigenvalues $1$ and $-1$, so both have modulus one. Starting from $x_0=(1,0)^T$, the sequence alternates:

$$
x_0=\begin{bmatrix}1\\0\end{bmatrix},
\quad
x_1=\begin{bmatrix}0\\1\end{bmatrix},
\quad
x_2=\begin{bmatrix}1\\0\end{bmatrix},\ldots
$$

The matrix is irreducible but periodic, not primitive. Its states do not converge to one direction, even though Perron–Frobenius still supplies a positive eigenvector for $r=1$.

For a primitive matrix and $x_0\ge0$, the normalized state

$$
\widehat{x}_k=\frac{A^kx_0}{\mathbf{1}^TA^kx_0}
$$

does converge:

$$
\widehat{x}_k\longrightarrow\frac{v}{\mathbf{1}^Tv}.
$$

Without primitivity or another assumption guaranteeing a simple dominant
eigenvalue with strict spectral separation, this convergence statement must be
replaced by a statement about the peripheral modes.

---

## Dynamical consequences

Under the simple strict-dominance condition:

- if $r>1$, the magnitude grows exponentially along $v$;
- if $r=1$, the dominant mode has constant magnitude;
- if $0<r<1$, every state decays exponentially to zero;
- normalized nonnegative states converge to the normalized Perron vector.

These conclusions describe the dominant mode, not necessarily a complete closed-form solution. A complete solution may still require generalized eigenvectors and every Jordan block.

---

## Key takeaway

Perron–Frobenius theory does not rely on diagonalizability. The left Perron
eigenvector extracts the coefficient of the right Perron mode, and a simple
dominant eigenvalue with a strict spectral gap makes that rank-one projection
dominate all defective residual modes. For discrete-time convergence, however,
irreducibility alone is not enough: primitivity, or another assumption
guaranteeing these two spectral properties, is required for convergence to a
single direction.

## Related material

- [Dominant eigenvalues and qualitative behavior of linear systems](../../control/dominant-eigenvalues-qualitative-behavior-linear-systems.md)
- [Eigendecomposition vs. spectral decomposition](../../linear-algebra/eigendecomposition-vs-spectral-decomposition.md)
- [Diagonalization, Jordan form, and geometric meaning](../../linear-algebra/diagonalization-jordan-form-geometry.md)

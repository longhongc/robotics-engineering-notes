# Positive Definite Matrices — Summary Notes

## Definition
A **positive definite matrix** (real case) is a **symmetric matrix** \(A\) such that

$$
x^\top A x > 0 \quad \text{for all } x \neq 0
$$

Symmetry is part of the definition (or can be assumed without loss of generality).

---

## Eigenvalue Characterization
For a real symmetric matrix \(A\):

- \(A\) is **positive definite** if and only if  
  all eigenvalues of \(A\) are **strictly positive**.

This equivalence follows from the spectral theorem.

---

## Eigen-Decomposition and Factorization
Any real symmetric matrix admits an eigen-decomposition:

$$
A = P D P^\top
$$

where:
- \(P\) is an orthogonal matrix \((P^\top P = I)\)
- \(D\) is a diagonal matrix

If \(A\) is positive definite:
- All diagonal entries of \(D\) are positive
- We can write:

$$
D = \sqrt{D}\,\sqrt{D}
$$

Substituting:

$$
A = P \sqrt{D}\,\sqrt{D} P^\top
$$

Rearranging:

$$
A = (\sqrt{D} P^\top)^\top (\sqrt{D} P^\top)
$$

So:

$$
A = R^\top R
$$

This is the basis of the **Cholesky factorization**.

---

## Symmetric and Skew-Symmetric Decomposition
Any real matrix \(A\) can be uniquely decomposed as:

$$
A = S + K
$$

where:
- Symmetric part:
  $$
  S = \tfrac12 (A + A^\top)
  $$
- Skew-symmetric part:
  $$
  K = \tfrac12 (A - A^\top)
  $$

---

## Why Positive Definiteness Depends Only on Symmetry
A skew-symmetric matrix satisfies:

$$
K^\top = -K
$$

For any vector \(x\):

$$
x^\top K x = 0
$$

Therefore:

$$
x^\top A x = x^\top S x
$$

➡️ The **skew-symmetric part contributes nothing** to the quadratic form.

---

## Congruence Transforms and Inertia

For an invertible matrix \(P\), a change of variables \(x=Py\) transforms the
quadratic form as

$$
x^\top A x = y^\top (P^\top A P)y.
$$

The matrix transformation

$$
A \mapsto P^\top A P
$$

is called a **congruence transformation**. It describes the same quadratic-form
geometry in different coordinates; it does not generally describe the same
linear operator in a new basis.

For a real symmetric matrix \(A\), **Sylvester's law of inertia** states that
every nonsingular congruence preserves the triple

$$
(n_+,n_-,n_0),
$$

where \(n_+\), \(n_-\), and \(n_0\) count the positive, negative, and zero
eigenvalues of \(A\). Congruence therefore preserves definiteness and the
number of flat directions, but not the numerical eigenvalues themselves.

This is different from a similarity transformation

$$
B=P^{-1}AP,
$$

which represents the same linear operator in a different basis and preserves
the characteristic polynomial and exact eigenvalues. See [Similarity
Invariance of Eigenvalues and Multiplicities](similarity-invariance-eigenvalues-multiplicities.md)
for that distinction.

---

## Final Summary
- Positive definite matrices are **real symmetric matrices**
- They satisfy:
  $$
  x^\top A x > 0 \quad \forall x \neq 0
  $$
- All eigenvalues are **strictly positive**
- They factor naturally as:
  $$
  A = R^\top R
  $$
- Only the **symmetric part** of a matrix affects \(x^\top A x\)
- Congruence preserves the inertia of a real symmetric matrix, while similarity
  preserves its exact eigenvalues

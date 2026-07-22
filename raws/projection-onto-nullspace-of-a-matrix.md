# Projection onto the Nullspace of a Matrix

This note explains how to orthogonally project a vector onto the nullspace of a matrix. The focus is on conceptual understanding first, followed by concrete formulas and computational viewpoints.

---

## Problem Setup

Let
- \(A \in \mathbb{R}^{m \times n}\) be a matrix,
- \(v \in \mathbb{R}^n\) be a vector.

The **nullspace** of \(A\) is
\[
\mathcal{N}(A) = \{x \in \mathbb{R}^n : Ax = 0\}.
\]

Our goal is to compute the **orthogonal projection** of \(v\) onto \(\mathcal{N}(A)\).

---

## Key Geometric Insight

A fundamental orthogonal decomposition is:
\[
\mathbb{R}^n = \mathcal{N}(A) \oplus \mathcal{R}(A^\top),
\]
where \(\mathcal{R}(A^\top)\) is the row space of \(A\).

This means:
- Every vector \(v\) can be uniquely written as
  \[
  v = v_{\mathcal N} + v_{\mathcal R},
  \]
  with
  \[
  v_{\mathcal N} \in \mathcal{N}(A), \quad v_{\mathcal R} \in \mathcal{R}(A^\top).
  \]
- Projecting onto the nullspace is equivalent to **subtracting the projection onto the row space**.

---

## Projection Formula via the Row Space

Let \(P_{\mathcal{N}(A)}\) denote the orthogonal projector onto \(\mathcal{N}(A)\). Then
\[
P_{\mathcal{N}(A)} = I - P_{\mathcal{R}(A^\top)}.
\]

The orthogonal projector onto the row space is
\[
P_{\mathcal{R}(A^\top)} = A^\top (A A^\top)^{\dagger} A,
\]
where \((\cdot)^{\dagger}\) denotes the Moore–Penrose pseudoinverse.

Therefore,
\[
\boxed{
P_{\mathcal{N}(A)} = I - A^\top (A A^\top)^{\dagger} A
}
\]
and the projected vector is
\[
\boxed{
v_{\mathcal N} = \left(I - A^\top (A A^\top)^{\dagger} A\right) v.
}
\]

### Full Row Rank Case
If \(A\) has full row rank, then \(A A^\top\) is invertible and
\[
v_{\mathcal N} = \left(I - A^\top (A A^\top)^{-1} A\right) v.
\]

---

## Projection Using a Nullspace Basis

If \(N \in \mathbb{R}^{n \times k}\) has columns forming an **orthonormal basis** for \(\mathcal{N}(A)\), then:
\[
P_{\mathcal{N}(A)} = N N^\top,
\]
and
\[
\boxed{
v_{\mathcal N} = N N^\top v.
}
\]

This formula is conceptually simple and often the cleanest when such a basis is available.

---

## Singular Value Decomposition (SVD) Viewpoint

Let
\[
A = U \Sigma V^\top
\]
be the SVD of \(A\). Partition
\[
V = [V_r \ \ V_0],
\]
where the columns of \(V_0\) correspond to zero singular values.

Then:
- The columns of \(V_0\) form an orthonormal basis of \(\mathcal{N}(A)\),
- The projection is
\[
\boxed{
v_{\mathcal N} = V_0 V_0^\top v.
}
\]

This perspective is especially useful for understanding rank and numerical stability.

---

## Least-Squares Characterization

Another characterization avoids explicit projectors:
1. Solve
   \[
   y^* = \arg\min_y \|A^\top y - v\|_2.
   \]
2. Then
   \[
   v_{\mathcal N} = v - A^\top y^*.
   \]

This works because \(A^\top y^*\) is the orthogonal projection of \(v\) onto \(\mathcal{R}(A^\top)\).

---

## Common Pitfalls

- Confusing the nullspace \(\mathcal{N}(A)\) with \(\mathcal{N}(A^\top)\).
- Forgetting that the projection depends on the **row space**, not the column space.
- Using \((A^\top A)^{-1}\) when \(A\) is not full column rank.
- Assuming \(A A^\top\) is invertible without checking rank.

---

## Summary

The nullspace projection is best understood via orthogonal decompositions:
\[
\mathcal{N}(A) = \mathcal{R}(A^\top)^\perp.
\]

The most general formula is:
\[
v_{\mathcal N} = \left(I - A^\top (A A^\top)^{\dagger} A\right) v,
\]
with simpler expressions available when a nullspace basis or SVD is known.


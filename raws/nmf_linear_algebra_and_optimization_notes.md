# Non-negative Matrix Factorization (NMF): Linear Algebra and Optimization Notes

## 1. Basic Definition

Non-negative Matrix Factorization (NMF) factorizes a non-negative matrix into two non-negative matrices:

[
V \approx WH
]

where:

* ( V \in \mathbb{R}^{m \times n}, ; V \ge 0 ) — original data matrix
* ( W \in \mathbb{R}^{m \times k}, ; W \ge 0 ) — basis matrix
* ( H \in \mathbb{R}^{k \times n}, ; H \ge 0 ) — coefficient matrix
* ( k \ll m, n ) — reduced dimension

This is a **low-rank approximation with non-negativity constraints**.

---

## 2. Dimensionality Reduction Interpretation

Each column of (V) is a data vector:

[
v_j \in \mathbb{R}^{m}
]

NMF represents it as:

[
v_j \approx W h_j
]

where:

[
h_j \in \mathbb{R}^{k}
]

Since:

[
k \ll m
]

this reduces dimensionality from (m) to (k).

### Key point:

* Original representation: (v_j \in \mathbb{R}^{m})
* Reduced representation: (h_j \in \mathbb{R}^{k})

Thus, **H is the compressed representation**.

W acts as a decoder (basis).

---

## 3. Linear Least Squares Connection

Without non-negativity constraints, the problem becomes standard least squares:

[
\min_{W,H} |V - WH|_F^2
]

If W is fixed, optimal H is given by pseudo-inverse:

[
H = W^+ V
]

where:

[
W^+ = (W^T W)^{-1} W^T
]

Similarly:

[
W = V H^+
]

Thus, unconstrained matrix factorization has closed-form solutions.

---

## 4. Projection Interpretation

Reconstruction:

[
\hat V = WH = W W^+ V
]

Matrix:

[
P = W W^+
]

is a projection matrix.

This means unconstrained factorization projects data onto a k-dimensional linear subspace.

This is closely related to PCA.

---

## 5. Key Difference Between PCA and NMF

PCA:

[
W,H \in \mathbb{R}
]

Allows negative values.

NMF:

[
W,H \ge 0
]

Allows only additive combinations.

This produces **parts-based representations**, which are more interpretable.

---

## 6. Optimization Objective

Standard NMF solves:

[
\min_{W,H \ge 0}
|V - WH|_F^2
]

This is called constrained least squares.

---

## 7. Convexity and NP-hardness

Important distinction:

If W is fixed:

[
\min_{H \ge 0} |V - WH|^2
]

This is Non-negative Least Squares (NNLS), which is convex and solvable in polynomial time.

If H is fixed:

[
\min_{W \ge 0} |V - WH|^2
]

Also convex.

However, jointly optimizing both:

[
\min_{W,H \ge 0} |V - WH|^2
]

is:

* non-convex
* bilinear
* NP-hard

because W and H multiply each other.

This creates multiple local minima.

---

## 8. Relationship to Linear Programming (LP)

Linear Programming:

[
\min_{x \ge 0} c^T x
]

Properties:

* Linear objective
* Linear variables
* Convex
* Polynomial-time solvable

NNLS:

[
\min_{x \ge 0} |Ax - b|^2
]

Also convex.

NMF:

[
\min_{W,H \ge 0} |V - WH|^2
]

Not convex because of bilinear terms.

Key difference:

LP and NNLS → variables appear linearly
NMF → variables multiply each other

This causes NP-hardness.

---

## 9. Geometric Interpretation: Subspace vs Cone

Unconstrained least squares:

Data lies in a linear subspace:

[
{Wh : h \in \mathbb{R}^k}
]

NMF:

Data lies in a convex cone:

[
{Wh : h \ge 0}
]

Cone structure restricts representation and promotes sparsity.

---

## 10. Sparsity Properties

In practice, both W and H are often sparse.

Especially H.

Reason:

Non-negativity prevents cancellation.

Representation becomes:

[
v_j = \sum_i h_{ij} w_i
]

with:

many (h_{ij} = 0).

This produces sparse encoding.

Sparse H means:

Each data point uses only a few components.

Sparse W means:

Each component uses only a few features.

---

## 11. Interpretation as Encoder–Decoder Model

Encoding:

[
h_j = \text{compressed representation of } v_j
]

Decoding:

[
v_j \approx W h_j
]

Thus:

* H = encoded data
* W = basis / decoder
* WH = reconstruction

This is similar to a linear autoencoder with non-negativity constraints.

---

## 12. Relationship Summary

| Method        | Constraint              | Convex | Closed-form               |
| ------------- | ----------------------- | ------ | ------------------------- |
| Least squares | none                    | yes    | yes                       |
| PCA           | orthogonality           | yes    | yes                       |
| NNLS          | non-negative            | yes    | no closed-form but convex |
| NMF           | non-negative + bilinear | no     | NP-hard                   |

---

## 13. Key Conceptual Summary

NMF performs linear dimensionality reduction by representing data as additive combinations of non-negative basis vectors.

Core properties:

* Linear dimensionality reduction
* Non-negative constraints
* Parts-based representation
* Often sparse solutions
* Non-convex optimization
* NP-hard in general
* Closely related to least squares, PCA, and convex optimization

---

## 14. One-Sentence Intuition

NMF compresses data into lower-dimensional non-negative coordinates that combine additively to reconstruct the original data.


# Least Squares and Pseudoinverse — Geometric Interpretation

## Problem setup

Given:

$$
A \in \mathbb{R}^{m \times n}, \quad m > n
$$

$$
Ax = b
$$

In general, this system may not have an exact solution. So we solve the **least squares problem**:

$$
\min_x |Ax - b|
$$

---

# Core geometric result (ALWAYS TRUE)

For any matrix $A$, the pseudoinverse solution

$$
x' = A^+ b
$$

has two fundamental geometric meanings:

---

## Meaning 1: Projection in output space

$$
Ax' = \operatorname{Proj}_{\mathrm{Col}(A)}(b)
$$

This means:

* $Ax'$ is the orthogonal projection of $b$ onto the column space of $A$
* This is the closest vector to $b$ that can be expressed as $Ax$

So the least squares problem is equivalent to:

$$
Ax' = \arg\min_{y \in \mathrm{Col}(A)} |y - b|
$$

---

## Meaning 2: Minimum-norm solution in input space

There may be many vectors $x$ that produce the same projection.

The pseudoinverse selects the unique one with smallest length:

$$
x' =
\arg\min_x |x|
\quad \text{subject to} \quad
Ax = \operatorname{Proj}_{\mathrm{Col}(A)}(b)
$$

This is called the **minimum-norm least squares solution**.

---

# Two cases of interest

---

## Case 1: $A^TA$ is invertible (columns independent)

Solution:

$$
x' = (A^TA)^{-1} A^T b
$$

Properties:

* Column space projection still happens
* Only ONE solution exists
* Minimum norm condition is automatic

No null space freedom exists.

---

## Case 2: $A^TA$ is singular (columns dependent)

Solution:

$$
x' = A^+ b
$$

Properties:

* Same projection onto column space
* INFINITELY many x can produce same projection
* Pseudoinverse picks smallest-norm solution
* Null space components are discarded

---

# SVD interpretation (most important insight)

Singular Value Decomposition:

$$
A = U \Sigma V^T
$$

Pseudoinverse:

$$
A^+ = V \Sigma^+ U^T
$$

where:

$$
\Sigma^+ =
\begin{cases}
1/\sigma_i & \text{if } \sigma_i > 0 \\\\
0 & \text{if } \sigma_i = 0
\end{cases}
$$

This means:

* Project $b$ onto singular directions (via $U^T b$)
* Invert only directions with nonzero singular values
* Ignore directions where information is lost
* Map result back to input space

---

# Fundamental space interpretation

Input space decomposes into:

$$
\mathbb{R}^n =
\mathrm{Row}(A)
\oplus
\mathrm{Null}(A)
$$

Any vector can be written as:

$$
x =
x_{\mathrm{row}}
+
x_{\mathrm{null}}
$$

Since:

$$
A x_{\mathrm{null}} = 0
$$

Null space does not affect output.

Pseudoinverse sets:

$$
x_{\mathrm{null}} = 0
$$

to minimize norm.

---

# Final unified geometric summary (MOST IMPORTANT)

For ANY matrix $A$:

$$
\boxed{
A^+ b =
\text{minimum-norm vector whose image under A is the projection of b onto Col(A)}
}
$$

Equivalent interpretation:

**Step 1:** Project $b$ onto column space of $A$

**Step 2:** Find smallest vector $x$ that produces that projection

---

# Key intuition (one sentence)

The pseudoinverse reverses A only in directions where reversal is possible, and ignores directions where information was lost.

---

# Key facts checklist

Always true:

* $Ax' = \operatorname{Proj}_{\mathrm{Col}(A)}(b)$
* $x'$ minimizes $|Ax-b|$
* $x'$ also minimizes $|x|$ among all least squares solutions
* $x'$ lies in the row space of $A$
* pseudoinverse works whether $A^TA$ is invertible or not

---

# Special case summary

If invertible:

$$
A^+ = (A^TA)^{-1}A^T
$$

If singular:

$$
A^+ = V \Sigma^+ U^T
$$

Geometric meaning remains identical.

---

# Mental model to remember forever

Least squares + pseudoinverse =

"Project first, then invert only what is invertible, and keep the smallest possible input vector."

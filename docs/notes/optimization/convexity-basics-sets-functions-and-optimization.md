# Convexity Basics: Sets, Functions, and Optimization

Convexity is a geometric property that makes many optimization problems
tractable. It connects the shape of a feasible set, the curvature of an
objective, and the meaning of local optimality.

This note develops the basic vocabulary used throughout convex optimization:

- convex and affine sets;
- convex hulls and closure properties;
- convex functions and their composition rules;
- Jensen's inequality;
- first- and second-order tests; and
- the standard form of a convex optimization problem.

The central consequence is simple:

> For a convex objective over a convex feasible set, every local minimum is a
> global minimum.

Convexity does not necessarily make the minimum unique. Uniqueness requires
stronger conditions, such as strict or strong convexity.

## 1. Convex sets

A set $C$ is convex if the line segment between any two points in the set
also remains in the set:

$$
x,y\in C,\quad \alpha\in[0,1]
\quad\Longrightarrow\quad
\alpha x+(1-\alpha)y\in C.
$$

The coefficients $\alpha$ and $1-\alpha$ are nonnegative and sum to one,
so the combination lies between $x$ and $y$. In one dimension, this is why
convex sets are intervals, rays, or the entire line rather than disconnected
collections of intervals.

### Affine sets

An affine set contains the entire line through any two of its points:

$$
x,y\in C,\quad \alpha\in\mathbb R
\quad\Longrightarrow\quad
\alpha x+(1-\alpha)y\in C.
$$

Every affine set is convex, but a convex set need not contain the entire
extension of a line segment. A line, plane, or translated subspace is affine;
a ball and a half-space are generally convex but not affine.

### Intersections

Any intersection of convex sets is convex. If $C_j$ is convex for every
index $j$, then

$$
C=\bigcap_j C_j
$$

is convex: two points in $C$ lie in every $C_j$, so their connecting
segment lies in every $C_j$ as well.

This is the geometric reason that combining several convex inequality
constraints still produces one convex feasible region.

### Convex hull

The convex hull of a set $S$, written $\operatorname{conv}(S)$, is the
smallest convex set containing $S$. Equivalently, it consists of all finite
convex combinations:

$$
\operatorname{conv}(S)
=
\left\{
\sum_{i=1}^{k}\alpha_i x_i
\;\middle|\;
x_i\in S,\quad
\alpha_i\ge0,\quad
\sum_{i=1}^{k}\alpha_i=1
\right\}.
$$

It can also be described as the intersection of every convex superset of
$S$. In geometric terms, it is the shape obtained by stretching a
rubber band around the set.

### Affine maps

Affine maps preserve convex combinations. For

$$
T(x)=Ax+b,
$$

$$
T(\alpha x+(1-\alpha)y)
=
\alpha T(x)+(1-\alpha)T(y).
$$

Therefore, the affine image of a convex set is convex. The inverse image is
also convex: if $D$ is convex, then

$$
T^{-1}(D)=\{x\mid Ax+b\in D\}
$$

is convex. This fact is useful when constraints are written as affine
expressions mapped into known convex sets.

## 2. Convex functions

Let $f$ be defined on a convex domain. It is convex when

$$
f(\alpha x+(1-\alpha)y)
\le
\alpha f(x)+(1-\alpha)f(y)
$$

for every $x,y$ in the domain and every $\alpha\in[0,1]$.

The graph interpretation is that the function lies below the chord joining
any two points on its graph. A convex function can be flat or have changing
curvature, but it never bends above one of its chords.

The epigraph gives a set-based interpretation:

$$
\operatorname{epi}(f)
=
\{(x,t)\mid f(x)\le t\}.
$$

For a function on a convex domain, $f$ is convex if and only if its
epigraph is a convex set. This connects the geometry of sets to the curvature
of functions.

### Basic examples

- Every affine function is both convex and concave.
- Every norm is convex. The triangle inequality and positive homogeneity give

$$
  \|\alpha x+(1-\alpha)y\|
  \le
  \alpha\|x\|+(1-\alpha)\|y\|.
$$

- A quadratic function $f(x)=x^TQx$ is convex when $Q$ is positive
  semidefinite.
- The pointwise maximum of convex functions is convex.
- A nonnegative weighted sum of convex functions is convex.

Convexity is not the same as monotonicity. A convex function may increase,
decrease, or do both over different parts of its domain.

## 3. Closure and composition rules

The following rules are reliable ways to build new convex functions:

### Nonnegative sums

If $f_i$ are convex and $\lambda_i\ge0$, then

$$
f(x)=\sum_i\lambda_i f_i(x)
$$

is convex.

The coefficients must be nonnegative. Subtracting a convex function generally
does not preserve convexity; if $f$ is convex, then $-f$ is concave.

### Pointwise maximum

If $f_1,\ldots,f_k$ are convex, then

$$
f(x)=\max_i f_i(x)
$$

is convex. The maximum operation preserves the upper envelope of the
functions without introducing a concave dip.

### Scalar composition

For $h=f\circ g$, useful sufficient conditions include:

- $g$ is convex and $f$ is convex and nondecreasing;
- $g$ is concave and $f$ is convex and nonincreasing.

These are sufficient rules, not a complete if-and-only-if characterization
of every convex composition. The monotonicity condition determines whether
the curvature of $g$ is preserved or reversed by $f$.

For vector-valued compositions, additional structure is needed. Applying a
scalar rule mechanically to a multivariable expression can give an invalid
conclusion.

## 4. Jensen's inequality

The definition of convexity extends from two points to any finite collection
of points. If $f$ is convex, $\alpha_i\ge0$, and
$\sum_i\alpha_i=1$, then

$$
f\left(\sum_i\alpha_i x_i\right)
\le
\sum_i\alpha_i f(x_i).
$$

This is Jensen's inequality. It says that evaluating a convex function at an
average is no greater than averaging the function values.

For a random variable $X$, the probabilistic form is

$$
f\bigl(\mathbb E[X]\bigr)
\le
\mathbb E[f(X)],
$$

when the expectations exist. The gap between the two sides measures how much
the function's curvature penalizes variability.

Jensen's inequality is a useful bridge between convex geometry, probability,
statistics, and estimation.

## 5. Differential tests for convexity

The geometric definition is fundamental, but derivatives provide practical
tests.

### First-order condition

Suppose $f$ is differentiable on a convex domain. Then $f$ is convex if
and only if every tangent hyperplane is a global under-estimator:

$$
f(y)
\ge
f(x)+\nabla f(x)^T(y-x)
\qquad\text{for all }x,y.
$$

The right-hand side is the tangent approximation at $x$. For a convex
function, moving to any other point $y$ cannot place the function below that
tangent plane.

### Second-order condition

Suppose $f$ is twice differentiable on a convex open domain. Then

$$
f\text{ is convex}
\quad\Longleftrightarrow\quad
\nabla^2 f(x)\succeq0
\quad\text{for every }x.
$$

The notation $\nabla^2 f(x)\succeq0$ means that

$$
z^T\nabla^2 f(x)z\ge0
\qquad\text{for every direction }z.
$$

To see why this is the right condition, restrict $f$ to a line
$x+tz$. The resulting scalar function has second derivative

$$
\frac{d^2}{dt^2}f(x+tz)
=
z^T\nabla^2 f(x+tz)z.
$$

Positive semidefinite curvature along every line gives the one-dimensional
convexity inequality on every segment.

Positive definiteness is stronger than needed for convexity. A positive
definite Hessian gives strict local curvature, while a positive semidefinite
Hessian can have flat directions. See [positive definiteness and local
optimization](positive-definite-and-local-optimization.md) for the related
stationary-point classification.

## 6. Convex optimization problems

A standard convex optimization problem has the form

$$
\begin{aligned}
\min_x\quad & f_0(x)\\\\
\text{s.t.}\quad & f_i(x)\le0,\qquad i=1,\ldots,m,\\\\
& Ax=b,
\end{aligned}
$$

where $f_0$ and every $f_i$ are convex.

Each inequality $f_i(x)\le0$ defines a convex sublevel set. Their
intersection is therefore convex. The equality constraint $Ax=b$ is affine,
so it also defines a convex set.

### Why equality constraints are affine

An equality $h(x)=0$ can be written as two inequalities:

$$
h(x)\le0,
\qquad
-h(x)\le0.
$$

For both inequalities to define convex sublevel sets, $h$ would need to be
both convex and concave. The standard general form therefore uses affine
equalities, which are automatically both.

This does not mean that every useful problem must have affine equalities.
Nonlinear equality constraints can be handled, but their feasible sets are
not automatically convex and require separate analysis.

### Local minima are global

If the objective is convex and the feasible set is convex, every local
minimum is global. Suppose $x^\star$ were a local but not global minimum,
and let $y$ be a feasible point with a lower objective value. Convexity of
the feasible set makes

$$
x_\alpha=(1-\alpha)x^\star+\alpha y
$$

feasible for small $\alpha>0$. Convexity of the objective gives

$$
f_0(x_\alpha)
\le
(1-\alpha)f_0(x^\star)+\alpha f_0(y)
<
f_0(x^\star),
$$

contradicting local minimality.

There may be several global minimizers. Strict or strong convexity can provide
uniqueness under appropriate conditions.

## 7. Common mistakes

- **“The constraints are convex.”** More precisely, inequality constraints
  define convex sublevel sets, and the feasible set is their intersection
  together with the equality-constraint set.
- **“Positive semidefinite means a unique minimum.”** PSD curvature permits
  flat directions. It proves convexity, not uniqueness.
- **“Every composition of convex functions is convex.”** Composition depends
  on monotonicity and on whether the inner function is convex or concave.
- **“A PSD Hessian proof is just a truncated Taylor expansion.”** The exact
  argument follows the line segment and integrates the directional curvature;
  a truncated approximation alone is not a proof.
- **“Gaussian-looking or familiar nonlinearities are convex.”** Sigmoid and
  $\tanh$ each change curvature across their domains, so neither is globally
  convex.
- **“Convex optimization means the answer is unique.”** Convexity gives global
  optimality of local minima, but multiple global optima can still exist.

## 8. Robotics perspective

Convexity appears throughout robotics:

- least-squares calibration and estimation use convex quadratic objectives;
- norm penalties and bounds model effort, regularization, and actuator limits;
- trajectory optimization can use convex constraints for simplified dynamics,
  collision-free corridors, or linearized operating regions;
- linear and quadratic programs provide efficiently solvable planning and
  control subproblems.

Many full robotics problems are not convex. Collision avoidance, contact
switching, nonlinear dynamics, and orientation constraints can create
non-convex feasible regions. Recognizing which subproblem is convex helps
separate globally reliable components from parts requiring initialization,
local search, or additional relaxations.

## Related material

- [Positive definiteness and local optimization](positive-definite-and-local-optimization.md)
- [Newton's method: root finding vs. optimization](newtons-method-root-finding-vs-optimization.md)
- [Interior-point methods, barriers, and Newton steps](interior-point-method-barrier-and-newton.md)
- [Linear programming duality](linear-programming-duality-linear-algebra.md)
- [Lagrangian duality and the interior-point KKT view (learning issue #31)](https://github.com/longhongc/robotics-engineering-notes/issues/31)
- [Learning issue #32](https://github.com/longhongc/robotics-engineering-notes/issues/32)


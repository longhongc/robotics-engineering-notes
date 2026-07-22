# Newton’s Method: Root Finding vs Optimization

This note clarifies the two closely related but conceptually distinct methods that are both commonly called **Newton’s method**:

1. Newton’s method for **root finding**
2. Newton’s method for **optimization (finding stationary points)**

Although they share the same philosophy, they solve different problems and use derivatives differently.

---

## 1. Newton’s Method for Root Finding

### Problem
Find a root of a (scalar) function:

$$
f(x) = 0
$$

### Core idea
Approximate the function by its **first-order Taylor expansion** (a tangent line) at the current iterate $x_k$, then solve for where that approximation equals zero.

### Taylor approximation

$$
f(x) \approx f(x_k) + f'(x_k)(x - x_k)
$$

Setting this to zero and solving for $x$ gives the update:

$$
x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}
$$

### Interpretation
- Approximates $f$ locally by a line
- Moves to where that line crosses the $x$-axis
- Requires only first derivatives

### Convergence
- Quadratic convergence near a simple root
- Very fast when the initial guess is good

---

## 2. Newton’s Method for Optimization

### Problem
Find a stationary point of a function:

$$
\nabla f(x) = 0
$$

This includes:
- local minima
- local maxima
- saddle points

### Core idea (gradient viewpoint)
Apply **Newton’s method to the equation** $\nabla f(x) = 0$.

Take a **first-order Taylor expansion of the gradient**:

$$
\nabla f(x) \approx \nabla f(x_k) + \nabla^2 f(x_k)(x - x_k)
$$

Set this approximation to zero:

$$
\nabla^2 f(x_k)\,\Delta x = -\nabla f(x_k)
$$

where:

$$
\Delta x = x - x_k
$$

The update is:

$$
x_{k+1} = x_k + \Delta x
$$

---

## 3. Equivalent Quadratic Approximation Viewpoint

Newton’s optimization method can also be derived by approximating the **function itself** to second order.

Second-order Taylor expansion:

$$
f(x) \approx f(x_k)
+ \nabla f(x_k)^T (x - x_k)
+ \tfrac{1}{2}(x - x_k)^T \nabla^2 f(x_k)(x - x_k)
$$

Minimizing this quadratic model with respect to $x$ yields the same Newton step:

$$
\nabla^2 f(x_k)\,\Delta x = -\nabla f(x_k)
$$

Thus:

- First-order Taylor of the gradient  
  **≡**
- Second-order Taylor of the function

---

## 4. Role of the Hessian Matrix

The Hessian $H = \nabla^2 f(x)$ determines the local geometry near a stationary point.

### Hessian classification

| Hessian eigenvalues | Interpretation |
|--------------------|----------------|
| All positive | Local minimum |
| All negative | Local maximum |
| Mixed signs | Saddle point |
| Nonnegative with zeros | Flat valley / degenerate case |

### Effect on Newton’s optimization method

- **Positive definite Hessian**  
  - Quadratic model is a bowl  
  - Newton step is well-defined  
  - Fast, stable convergence to a local minimum

- **Indefinite Hessian**  
  - Saddle-shaped quadratic model  
  - Newton step may increase the function value

- **Negative definite Hessian**  
  - Newton step moves toward a local maximum

- **Singular (semidefinite) Hessian**  
  - Hessian not invertible  
  - Newton equation may have no unique solution

---

## 5. Using the Pseudoinverse of the Hessian

When the Hessian is singular, one may compute:

$$
\Delta x = - \nabla^2 f(x_k)^+ \nabla f(x_k)
$$

where $(\cdot)^+$ denotes the Moore–Penrose pseudoinverse.

### Interpretation
- Produces the minimum-norm solution
- Updates only along directions where the Hessian has nonzero curvature
- Ignores flat directions

### Limitations
- Can stall in flat valleys
- Does not fix saddle-point issues
- Rarely used in practical optimization algorithms

---

## 6. Practical Modifications of Newton’s Method

In practice, pure Newton steps are often replaced by more robust variants:

### Damped / Regularized Newton

$$
(\nabla^2 f(x_k) + \lambda I)\Delta x = -\nabla f(x_k)
$$

Ensures invertibility and descent.

### Trust-region methods
Minimize the quadratic model subject to a step-size constraint.

### Quasi-Newton methods
Approximate the inverse Hessian while maintaining positive definiteness (e.g., BFGS).

---

## 7. Big Picture Summary

| Method | Solves | Taylor expansion | Derivatives used |
|------|--------|------------------|------------------|
| Root-finding Newton | $f(x)=0$ | First-order of $f$ | $f'$ |
| Optimization Newton | $\nabla f(x)=0$ | First-order of $\nabla f$ (or second-order of $f$) | $\nabla f, \nabla^2 f$ |

Both methods follow the same principle:
> Replace a nonlinear problem by a simpler local approximation, solve it exactly, and iterate.


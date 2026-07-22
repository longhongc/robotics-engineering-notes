# SO(3), Manifolds, Parameterization, and Lie Groups — Summary Notes

## 1. Manifolds

A **manifold** is a space that locally looks like ℝⁿ but globally may have curvature or nontrivial topology.

Examples:

* ℝ² → flat manifold
* Circle S¹ → curved manifold
* Sphere S² → curved manifold
* Rotation space SO(3) → curved manifold

Key property:

Locally:

```
manifold ≈ ℝⁿ
```

Globally:

```
manifold may differ topologically from ℝⁿ
```

---

## 2. Explicit vs Implicit Parameterization

### Explicit parameterization

Uses exactly n parameters for an n-dimensional manifold.

Example: Circle S¹

```
θ ∈ [-π, π]
```

Problem:

* Artificial boundary
* Discontinuity at boundary
* Singularities unavoidable globally

---

### Implicit parameterization

Uses higher-dimensional coordinates with constraints.

Example: Circle S¹ in ℝ²

```
x² + y² = 1
```

Advantages:

* No artificial boundary
* Smooth everywhere
* No singularities

---

## 3. Why singularities occur

If a manifold is NOT topologically equivalent (homeomorphic) to ℝⁿ, then it cannot be globally parameterized smoothly using n parameters.

Example:

```
S¹ ≠ ℝ¹
SO(3) ≠ ℝ³
```

Therefore minimal coordinate parameterizations must introduce:

* singularities, OR
* discontinuities, OR
* artificial boundaries

This is unavoidable.

---

## 4. SO(3): Rotation Manifold

SO(3) is the space of all 3D rotations.

Definition:

```
SO(3) = { R ∈ ℝ³ˣ³ | RᵀR = I, det(R) = +1 }
```

Properties:

* smooth manifold
* dimension = 3
* Lie group
* represents physical rotations

Reflection matrices (det = −1) are NOT included.

Those belong to O(3), not SO(3).

---

## 5. Axis–Angle Representation

Representation:

```
ω = θu
```

where:

* u = unit axis
* θ = rotation angle

Topology:

* solid ball of radius π
* antipodal points on boundary identified

Behavior:

When θ > π:

```
θu ≡ (2π − θ)(−u)
```

This creates coordinate flip.

Analogy: Tenet inversion world

Physical rotation is continuous, but coordinate representation flips.

---

## 6. Quaternion Representation

Quaternion:

```
q = (w, x, y, z)
```

Constraint:

```
w² + x² + y² + z² = 1
```

Topology:

```
S³ ⊂ ℝ⁴
```

Relationship to SO(3):

```
SO(3) = S³ / {±1}
```

Key properties:

* smooth everywhere
* no boundary
* no singularity
* double cover: q and −q represent same rotation

---

## 7. Rotation Matrix Representation

Rotation matrix:

```
R ∈ ℝ³ˣ³
```

Constraints:

```
RᵀR = I
det(R) = +1
```

Degrees of freedom:

```
9 parameters
6 constraints
3 DOF
```

Properties:

* smooth
* unique
* no singularities
* direct representation of SO(3)

---

## 8. Whitney Embedding Theorem

Statement:

Any n-dimensional manifold can be embedded in ℝ²ⁿ.

This guarantees existence of smooth implicit representation.

Examples:

```
S¹ ⊂ ℝ²
S² ⊂ ℝ³
SO(3) ⊂ ℝ⁴ (quaternion)
SO(3) ⊂ ℝ⁹ (rotation matrix)
```

---

## 9. Lie Groups

A Lie group is a manifold with group structure.

Properties:

* smooth manifold
* multiplication defined
* identity exists
* inverse exists
* multiplication and inverse smooth

SO(3) is a Lie group.

---

## 10. Lie Algebra

Lie algebra is the tangent space at identity.

For SO(3):

```
so(3) ≅ ℝ³
```

Represents angular velocity.

Representations:

Vector form:

```
ω ∈ ℝ³
```

Matrix form:

```
[ω]× =
[ 0  −ωz  ωy
  ωz  0  −ωx
 −ωy  ωx  0 ]
```

Quaternion form:

```
Ω = (0, ωx, ωy, ωz)
```

All represent same Lie algebra.

---

## 11. Exponential Map

Connects Lie algebra → Lie group

Matrix form:

```
R = exp([ω]×)
```

Quaternion form:

```
q = exp(½Ω)
```

This converts angular velocity into rotation.

---

## 12. Representation Summary

| Representation  | Space      | Unique            | Singularities |
| --------------- | ---------- | ----------------- | ------------- |
| Axis–Angle      | ℝ³ ball    | Yes               | Boundary flip |
| Quaternion      | S³ ⊂ ℝ⁴    | No (double cover) | None          |
| Rotation Matrix | SO(3) ⊂ ℝ⁹ | Yes               | None          |

---

## 13. Key Conceptual Summary

Manifold:

```
curved space locally like ℝⁿ
```

Lie group:

```
manifold + group structure
```

Lie algebra:

```
tangent space at identity
linear space ℝ³
```

Embedding:

```
manifold placed in higher dimensional linear space
```

Implicit parameterization:

```
smooth global representation
```

Explicit parameterization:

```
minimal coordinates but singularities unavoidable
```

---

## 14. Final Core Insight

Singularities are not properties of the physical system.

They are artifacts of insufficient coordinate representation.

Higher-dimensional implicit representations preserve smooth structure globally.

This is why robotics uses:

* rotation matrices
* quaternions
* Lie groups
* Lie algebras

instead of minimal coordinate parameterizations.

---


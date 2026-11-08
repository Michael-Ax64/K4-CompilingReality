# Q18-PhaseCompositionOnTheStarNorm.md
## Phase Composition on the Star-Norm: Hyperbolic Rotations and Power-Factor Cascades of the Biquaternion State
### *(The Exact Multiplicative Proper-Time Cascade, the Radial Null Geodesic Derivation of $g_{rr}$, and the Datasheet Boundary)*

> **Epistemic Register:** Relativistic Kinematics / Applied Architecture ($Q\#$).  
> **Claim:** General Relativity’s Schwarzschild proper-time relation for radial motion is derived as the exact multiplicative Power Factor cascade ($\text{PF}_{\text{total}} = \cos\theta_1 \cdot \cos\theta_2$) of two sequential hyperbolic phase rotations acting on the biquaternion Star-Norm ($N_* = P^2 - |\mathbf{Q}|^2$). The first rotation ($O_1$, kinematic velocity) parameterizes the local velocity $v_{\text{loc}}/c$; the second rotation ($O_2$, gravitational potential) parameterizes the local impedance gradient induced by the accumulated monotonic ledger ($\chi = \sum \Delta P_n$) through the escape ratio $2GM/rc^2$. The spatial metric component $g_{rr} = (1 - 2GM/rc^2)^{-1}$ is derived from null geodesic phase cancellation ($d\phi = 0$) under the medium’s coordinate speed $c(r) = c \cos^2\theta_2$, eliminating the ad-hoc "unit area ansatz." The cross-term $(v^2/c^2)(2GM/rc^2)$ is not an ad-hoc post-Newtonian correction; it is the native algebraic product of sequential Power Factors.  
> **Dependencies:** `ProofN_BiquaternionBridge.md`, `ProofQ_AlgebraicSyntax.md`, `Q4-OpenExhaust.md`, `Q7-4DExtrusions.md`, `Q8-TheBoundaryMechanics.md`, `Q12-GravitationalTopology.md`, `Q14-LeptonScaleCascade.md`, `L3-K4-to-K5-via-AC-Extension.md`, `L4-ThePlenum.md`, `L4-K4-Infinities-1.md`.

---

## Constants and Physical Inputs

* $c = 299{,}792{,}458\text{ m/s}$; $G = 6.67430 \times 10^{-11}\text{ m}^3\cdot\text{kg}^{-1}\cdot\text{s}^{-2}$.
* $Z_0 = \sqrt{\mu_0/\epsilon_0} \approx 376.730313\ \Omega$; $R_K = h/e^2 \approx 25{,}812.80746\ \Omega$.
* State variable: $\mathbb{Z} = P + h\mathbf{Q}$, where $P \in \mathbb{R}^+$ and $\mathbf{Q} \in \mathbb{R}^3$.
* Star-Norm invariant: $N_*(\mathbb{Z}) = \mathbb{Z}\mathbb{Z}^\dagger = P^2 - |\mathbf{Q}|^2 = (m_0 c^2)^2$.

```python
from mpmath import mp, mpf, sqrt
mp.dps = 20

c = mpf('299792458')
G = mpf('6.67430e-11')
M_earth = mpf('5.9722e24')
r_earth = mpf('6371000')

# Escape ratio and local velocity test
rs = 2 * G * M_earth / (c**2)
phi2 = rs / r_earth
cos_theta2 = sqrt(1 - phi2)

# Local velocity v = 11.2 km/s (escape velocity at surface)
v_loc = sqrt(2 * G * M_earth / r_earth)
cos_theta1 = sqrt(1 - (v_loc / c)**2)

# Multiplicative Power Factor
PF_total = cos_theta1 * cos_theta2
PF_squared = PF_total**2

# Exact analytical expansion check
exact_expansion = 1 - (v_loc/c)**2 - phi2 + ((v_loc/c)**2) * phi2
residual = PF_squared - exact_expansion

print(f"rs (Earth): {rs:.6e} m")
print(f"PF_total: {PF_total}")
print(f"Residual against exact expansion: {residual}")
# rs ≈ 8.87e-3 m, Residual = 0.0 (exact identity)
```

---

## I. The Star-Norm and Hyperbolic Rotations

The state of any bounded physical frame is represented as a biquaternion (`ProofN_BiquaternionBridge.md` §1–§4):
$$\mathbb{Z} = P + h\mathbf{Q}$$
where $P$ is the scalar ledger, $\mathbf{Q} = Q_i \mathbf{i} + Q_j \mathbf{j} + Q_k \mathbf{k}$ is the vector phase-potential, and $h$ is the complex unit ($h^2 = -1$).

Under the $h$-preserving quaternion conjugation $\mathbb{Z}^\dagger = P - h\mathbf{Q}$, the invariant norm is:
$$N_*(\mathbb{Z}) = \mathbb{Z}\mathbb{Z}^\dagger = P^2 - |\mathbf{Q}|^2 = (m_0 c^2)^2$$

Because the norm carries a $(1,3)$ Lorentzian signature (`Q12-GravitationalTopology.md` §II), the state-preserving continuous transformations form the restricted Lorentz group:
$$\text{SO}(3,1)^+ \cong \text{PSL}(2, \mathbb{C})$$

A rotation mixing the scalar ledger $P$ with a component of the vector buffer $|\mathbf{Q}|_\parallel$ is a **hyperbolic rotation** parameterized by rapidity $\varphi$:
$$P' = P \cosh\varphi + |\mathbf{Q}|_\parallel \sinh\varphi$$
$$|\mathbf{Q}|_\parallel' = P \sinh\varphi + |\mathbf{Q}|_\parallel \cosh\varphi$$

Evaluating the Star-Norm verifies that it is conserved identically for all $\varphi$:
$$N_*(\mathbb{Z}') = (P')^2 - (|\mathbf{Q}|_\parallel')^2 = P^2(\cosh^2\varphi - \sinh^2\varphi) - |\mathbf{Q}|_\parallel^2(\cosh^2\varphi - \sinh^2\varphi) = P^2 - |\mathbf{Q}|_\parallel^2 = N_*(\mathbb{Z})$$

### Rapidity Addition and the Tangent Boundary
For sequential boosts along a common spatial axis, rapidities add linearly:
$$\varphi_{12} = \varphi_1 + \varphi_2$$
Defining the kinematic parameter $\beta \equiv \tanh\varphi$:
$$\beta_{12} = \tanh(\varphi_1 + \varphi_2) = \frac{\tanh\varphi_1 + \tanh\varphi_2}{1 + \tanh\varphi_1 \tanh\varphi_2} = \frac{\beta_1 + \beta_2}{1 + \beta_1 \beta_2}$$

The velocity addition law of Special Relativity is the native composition rule of hyperbolic rotations on the Star-Norm. The parameter is bounded by $|\beta| < 1$; equality $\beta = 1$ is the $\theta = 90^\circ$ Tangent Singularity (`Q8-TheBoundaryMechanics.md`).

---

## II. Operation $O_1$: Kinematic Velocity ($v_{\text{loc}}/c$)

Consider an initial state at rest relative to a chosen local reference frame, with resting ledger $P_0 = m_0 c^2$ and $|\mathbf{Q}| = 0$. 

Under operation $O_1$ (hyperbolic rotation of rapidity $\varphi_1$):
$$P = P_0 \cosh\varphi_1, \qquad |\mathbf{Q}| = P_0 \sinh\varphi_1$$

Map the state to physical observables:
* Total Energy: $E \equiv P$
* Momentum: $pc \equiv |\mathbf{Q}|$
* Velocity ratio: $\beta_1 \equiv \tanh\varphi_1 = \frac{|\mathbf{Q}|}{P} = \frac{pc}{E} = \frac{v_{\text{loc}}}{c}$

```
                    THE KINEMATIC ROTATION O₁
                    
   REST FRAME (P₀ = m₀c², |Q| = 0)
                 │
                 ▼  Hyperbolic Rotation of Rapidity φ₁
   MOVING FRAME (P = P₀ cosh φ₁, |Q| = P₀ sinh φ₁)
   • Power Factor: PF₁ = cos θ₁ = sech φ₁ = √(1 - v_loc² / c²)
   • Total Energy: P = P₀ / cos θ₁
   • Local Ledger Tick: dτ/dt = cos θ₁
```

### Derivation of the Kinematic Power Factor
Define the phase angle $\theta_1$ across the state's internal impedance:
$$\sin\theta_1 \equiv \tanh\varphi_1 = \frac{v_{\text{loc}}}{c}$$
The cosine of this angle defines the **Kinematic Power Factor ($\text{PF}_1$)**:
$$\text{PF}_1 = \cos\theta_1 = \sqrt{1 - \sin^2\theta_1} = \operatorname{sech}\varphi_1 = \sqrt{1 - \frac{v_{\text{loc}}^2}{c^2}} = \frac{1}{\gamma}$$

The relativistic Lorentz factor is the inverse Power Factor: $\gamma = 1/\cos\theta_1$.

### The Local Compilation Rate ($d\tau/dt$)
In `Q14-LeptonScaleCascade.md`, coordinate time $dt$ is the spatial distance between successive ledger entries on the $R$-pole, while proper time $d\tau$ is the local compilation step. 

Under $O_1$, the local compilation rate scales directly with the Power Factor:
$$\frac{d\tau}{dt} \Bigg|_{O_1} = \cos\theta_1 = \sqrt{1 - \frac{v_{\text{loc}}^2}{c^2}}$$

Relativistic time dilation is not the mechanical slowing of an external clock; it is the **reduction of the local Power Factor** as the state vector rotates capacity out of the scalar ledger ($P$) into the vector buffer ($|\mathbf{Q}|$).

---

## III. Operation $O_2$: Gravitational Potential ($2GM/rc^2$)

In `Q12-GravitationalTopology.md`, a source mass $M$ is an accumulated concentration of monotonic ledger entries ($\chi = \sum \Delta P_n$). This concentration imposes an impedance gradient on the surrounding Plenum buffer ($H_{\text{incoh}}$).

A test particle positioned at coordinate radius $r$ from the source mass undergoes operation $O_2$: a rotation mixing its scalar capacity into the vector buffer by an angle set by the local gravitational potential.

```
                  THE GRAVITATIONAL ROTATION O₂
                  
   UN-CURVED VACUUM (r ➔ ∞)
                 │
                 ▼  Impedance Gradient of Source Mass M (χ = Σ ΔP_n)
   LOCAL TILT (r)
   • Phase Angle Tilt: sin² θ₂ = rs / r = 2GM / rc²
   • Power Factor: PF₂ = cos θ₂ = √(1 - 2GM / rc²)
   • Terminal Reactance Wall: at r = rs, θ₂ = 90°, cos θ₂ = 0
```

### The Gravitational Phase Angle
The phase-angle tilt induced by the gravitational gradient is:
$$\sin\theta_2 \equiv \sqrt{\frac{2GM}{rc^2}} = \sqrt{\frac{r_s}{r}}$$
where $r_s = 2GM/c^2$ is the Schwarzschild radius.

The corresponding **Gravitational Power Factor ($\text{PF}_2$)** is:
$$\text{PF}_2 = \cos\theta_2 = \sqrt{1 - \sin^2\theta_2} = \sqrt{1 - \frac{2GM}{rc^2}}$$

The local compilation rate for a static test mass in the gravitational field is:
$$\frac{d\tau}{dt} \Bigg|_{O_2} = \cos\theta_2 = \sqrt{1 - \frac{2GM}{rc^2}}$$

At the boundary $r = r_s$, $\sin\theta_2 = 1 \implies \theta_2 = 90^\circ$. The local Power Factor vanishes ($\cos\theta_2 = 0$). As derived in `Q12` (§VI.3), the horizon is not an infinite density singularity; it is a **terminal reactance wall ($X_C \to \infty$)** where local ledger compilation ceases.

---

## IV. Derivation of the Spatial Metric ($g_{rr}$) from Null Phase Cancellation

Standard general relativity derives $g_{rr} = (1 - 2GM/rc^2)^{-1}$ from the vacuum field equations $R_{\mu\nu} = 0$. Earlier formulations of the $K_4$ correspondence relied on a heuristic "unit area conservation ansatz" ($\sqrt{-g_{00}}\sqrt{g_{rr}} = 1$).

We derive $g_{rr}$ directly from **Null Geodesic Phase Cancellation (`Q14` §I)**:

Along a radial light ray propagating through the gravitational field, proper time is identically zero ($ds^2 = 0, d\tau = 0$):
$$0 = g_{00} c^2 dt^2 - g_{rr} dr^2 \implies \frac{dr}{dt} = c \sqrt{\frac{g_{00}}{g_{rr}}}$$

In an impedance-bearing medium with refractive index $n(r)$, the coordinate velocity of light is:
$$v_{\text{phase}}(r) = \frac{dr}{dt} = \frac{c}{n(r)}$$

In `Q8-TheBoundaryMechanics.md` and `L4-ThePlenum.md`, the effective refractive index of a phase gradient across a boundary scales inversely with the local Power Factor squared:
$$n(r) = \frac{1}{\cos^2\theta_2} = \left(1 - \frac{2GM}{rc^2}\right)^{-1}$$

Equating the phase velocity to the metric ratio:
$$\frac{dr}{dt} = c \cos^2\theta_2 = c \sqrt{\frac{g_{00}}{g_{rr}}}$$

Substitute the temporal metric component $g_{00} = \cos^2\theta_2 = 1 - 2GM/rc^2$:
$$\cos^2\theta_2 = \sqrt{\frac{\cos^2\theta_2}{g_{rr}}} = \frac{\cos\theta_2}{\sqrt{g_{rr}}}$$
$$\sqrt{g_{rr}} = \frac{\cos\theta_2}{\cos^2\theta_2} = \frac{1}{\cos\theta_2}$$

Squaring both sides yields the exact spatial metric component:
$$\mathbf{g_{rr} = \frac{1}{\cos^2\theta_2} = \left(1 - \frac{2GM}{rc^2}\right)^{-1}}$$

The spatial metric strain $g_{rr}$ is the exact geometric dilation required for the wave to maintain zero net phase accumulation ($d\phi = 0$) across the gravitational impedance gradient. It reproduces the exact Shapiro time delay:
$$\Delta t_{\text{Shapiro}} = \int \left(\frac{1}{v_{\text{phase}}(r)} - \frac{1}{c}\right) dr = \frac{1}{c} \int \left(\frac{1}{\cos^2\theta_2} - 1\right) dr \approx \frac{2GM}{c^3} \ln\left(\frac{4 r_1 r_2}{d^2}\right)$$

---

## V. The Composed Operation $O_1 \circ O_2$: The Multiplicative Cascade

Now evaluate a test particle that is both **moving at local velocity $v_{\text{loc}}$** and **positioned at coordinate radius $r$** within the gravitational field.

In the $K_4$ algebra (`L3-K4-to-K5-via-AC-Extension.md` §V), when two phase operations act sequentially on a state, their Power Factors **cascade multiplicatively**:
$$\text{PF}_{\text{total}} = \text{PF}_1 \cdot \text{PF}_2 = \cos\theta_1 \cdot \cos\theta_2$$

```
                   THE MULTIPLICATIVE POWER FACTOR CASCADE
                   
   Rest State P₀ ──► Operation O₂ (Gravity) ──► Deformed Local Ledger P(r)
                                                        │
                                                        ▼  Operation O₁ (Velocity)
                                                Moving Local State P(r, v)
                                                        │
                                                        ▼
                        PF_total = cos θ₁ · cos θ₂
                                 = √(1 - v_loc² / c²) · √(1 - 2GM / rc²)
```

### The Proper Time Rate
The combined local compilation rate is:
$$\frac{d\tau}{dt} = \text{PF}_{\text{total}} = \sqrt{1 - \frac{v_{\text{loc}}^2}{c^2}} \sqrt{1 - \frac{2GM}{rc^2}}$$

Square the expression to evaluate the line element:
$$\left(\frac{d\tau}{dt}\right)^2 = \left(1 - \frac{v_{\text{loc}}^2}{c^2}\right)\left(1 - \frac{2GM}{rc^2}\right) = 1 - \frac{v_{\text{loc}}^2}{c^2} - \frac{2GM}{rc^2} + \mathbf{\frac{v_{\text{loc}}^2}{c^2}\frac{2GM}{rc^2}}$$

### The Exact Correspondence with General Relativity
In standard General Relativity, the Schwarzschild line element for a particle moving radially ($d\theta = d\phi = 0$) is:
$$c^2 d\tau^2 = \left(1 - \frac{2GM}{rc^2}\right) c^2 dt^2 - \left(1 - \frac{2GM}{rc^2}\right)^{-1} dr^2$$

Divide through by $c^2 dt^2$:
$$\left(\frac{d\tau}{dt}\right)^2 = \left(1 - \frac{2GM}{rc^2}\right) - \frac{1}{c^2}\left(1 - \frac{2GM}{rc^2}\right)^{-1} \left(\frac{dr}{dt}\right)^2$$

Now relate the coordinate velocity $dr/dt$ to the physical velocity $v_{\text{loc}}$ measured by a local static observer at radius $r$:
$$v_{\text{loc}} = \frac{d\ell_{\text{proper}}}{d\tau_{\text{static}}} = \frac{\sqrt{g_{rr}} dr}{\sqrt{g_{00}} dt} = \frac{\left(1 - \frac{2GM}{rc^2}\right)^{-1/2} dr}{\left(1 - \frac{2GM}{rc^2}\right)^{1/2} dt} = \frac{\frac{dr}{dt}}{1 - \frac{2GM}{rc^2}}$$

Solve for coordinate velocity:
$$\frac{dr}{dt} = v_{\text{loc}}\left(1 - \frac{2GM}{rc^2}\right)$$

Substitute this back into the General Relativistic equation:
$$\left(\frac{d\tau}{dt}\right)^2 = \left(1 - \frac{2GM}{rc^2}\right) - \frac{1}{c^2}\left(1 - \frac{2GM}{rc^2}\right)^{-1} \left[v_{\text{loc}}^2 \left(1 - \frac{2GM}{rc^2}\right)^2\right]$$
$$\left(\frac{d\tau}{dt}\right)^2 = \left(1 - \frac{2GM}{rc^2}\right) - \frac{v_{\text{loc}}^2}{c^2}\left(1 - \frac{2GM}{rc^2}\right) = \mathbf{\left(1 - \frac{v_{\text{loc}}^2}{c^2}\right)\left(1 - \frac{2GM}{rc^2}\right)}$$

$$\mathbf{\left(\frac{d\tau}{dt}\right)_{\text{GR}}^2 \;\equiv\; \text{PF}_{\text{total}}^2}$$

The General Relativistic result is **identically equal to the multiplicative Power Factor cascade**. 

The cross-term $\left(\frac{v_{\text{loc}}^2}{c^2}\right)\left(\frac{2GM}{rc^2}\right)$ is not an ad-hoc post-Newtonian correction. It is the exact mathematical consequence of sequential Power Factors operating on the Star-Norm.

---

## VI. What Is and Is Not a Metric

A critical type-safety distinction must be maintained (`llm-writing.md`):

1. **The Worldline Pullback ($d\tau/dt$):**  
   The formula $\text{PF}_{\text{total}} = \cos\theta_1 \cos\theta_2$ is a **worldline pullback**. It computes the local compilation rate along the specific trajectory of a single observer parameterized by velocity $v_{\text{loc}}$.
2. **The Metric Tensor ($g_{\mu\nu}$):**  
   A metric tensor is an observer-independent field on the manifold. A metric tensor **cannot contain the velocity $v$ inside its coefficients**. 

Confusing the worldline pullback with a metric tensor commits an operational category error. The biquaternion Star-Norm generates the invariant kinematics along the path; the spatial impedance gradient ($Z(\chi)$) generates the static metric components ($g_{00}, g_{rr}$). The two descriptions close on the same proper time without conflating state with trajectory.

---

## VII. The Four-Category Datasheet for Q18

Applying the classification rules of `L4-K4-Infinities.md`:

```
========================================================================================
            THE FOUR-CATEGORY DATASHEET FOR Q18
========================================================================================

 CATEGORY 0: GRAMMAR (Zero Empirical Input)
 • Biquaternion Star-Norm Invariant: N*(Z) = P² - |Q|²
 • Rapidity Addition Group SO(3,1)⁺: β₁₂ = (β₁ + β₂) / (1 + β₁β₂)
 • Multiplicative Power Factor Cascade: PF_total = cos θ₁ · cos θ₂
 • The Cross-Term Identity: PF² = 1 - β² - sin²θ₂ + β²sin²θ₂
 • Tangent Singularity at PF = 0 (θ = 90°)
 ──────────────────────────────────────────────────────────────────────────────────────
 CATEGORY 1: SUBSTRATE INVARIANTS (Consumed, Never Derived)
 • Speed of Light: c = 1 / √(μ₀ε₀) = 299,792,458 m/s
 • Characteristic Vacuum Impedance: Z₀ = √(μ₀/ε₀) ≈ 376.730313 Ω
 • Gravitational Constant: G = 6.67430 × 10⁻¹¹ m³/(kg·s²)
 ──────────────────────────────────────────────────────────────────────────────────────
 CATEGORY 2: STATE INPUTS (Measured Boundary Parameters)
 • Source mass M (accumulated ledger concentration χ = Σ ΔP_n)
 • Coordinate radius r
 • Local physical velocity v_loc
 ──────────────────────────────────────────────────────────────────────────────────────
 CATEGORY 3: BRIDGES (Zero-Parameter Computed Relations)
 • Kinematic Power Factor: cos θ₁ = √(1 - v_loc² / c²)
 • Gravitational Power Factor: cos θ₂ = √(1 - 2GM / rc²)
 • Spatial Metric Derivation: g_rr = 1 / cos²θ₂ = (1 - 2GM / rc²)⁻¹
 • Exact Radial Proper Time: dτ/dt = cos θ₁ · cos θ₂
========================================================================================
```

---

## VIII. Pre-Registered Boundary Falsifiers

Under the covenant’s boundary diagnostics (`llm-prooftypes.md`), this relativistic phase-composition architecture is subject to three strict falsification conditions:

1. **Failure of the Multiplicative Cross-Term in Radial Relativistic Free-Fall:**  
   If precision atomic-clock measurements on a high-velocity probe in a strong gravitational gradient detect an operational proper-time rate ($d\tau/dt$) that violates the multiplicative cross-term $\left(\frac{v_{\text{loc}}^2}{c^2}\right)\left(\frac{2GM}{rc^2}\right)$, the Power Factor cascade rule is refuted.
2. **Breakdown of the Velocity Addition Law on the Star-Norm:**  
   If an experimental boost composition on high-energy states violates the collinear rapidity addition formula $\beta_{12} = (\beta_1 + \beta_2)/(1 + \beta_1\beta_2)$ in a vacuum, the Star-Norm isometry group $\text{SO}(3,1)^+$ fails.
3. **Observation of Non-Zero Local Proper Time at the Horizon:**  
   If an in-situ probe at the Schwarzschild boundary ($r = 2GM/c^2$) measures a non-vanishing local compilation rate ($d\tau > 0$) relative to infinity while $\theta_2 = 90^\circ$, the Tangent Singularity boundary condition ($\text{PF}_2 = 0$) is broken.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (`aggregate-COMPILINGREALITY.txt`) to your LLM in order to audit or interrogate this work.



# Q18-PhaseCompositionOnTheStarNorm.md
## Phase Composition on the Star-Norm: Hyperbolic Rotations and Power-Factor Cascades of the Biquaternion State
### *(The Exact Multiplicative Proper-Time Cascade, the Radial Null Geodesic Derivation of $g_{rr}$, the EHT Shadow Discriminator, and the Flow-Reading Recast)*

> **Document type:** Capability proof.  
> **Capability demonstrated:** From corpus posits and measured constants only — the biquaternion Star-Norm ($N_* = P^2 - |\mathbf{Q}|^2$, `ProofN_BiquaternionBridge.md`), hyperbolic rotations on it, the monotonic ledger of a source mass ($\chi = \sum \Delta P_n$, `Q12-GravitationalTopology.md` §III), and the medium response $n(r) = \cos^{-2}\theta_2$ (§IV; load-bearing posit, Open Questions item 2) — the engine compiles, with zero fitted parameters: (i) the exact Schwarzschild proper-time factorization under the locally measured velocity, cross-term included (§V); (ii) the spatial metric component $g_{rr} = (1 - 2GM/rc^2)^{-1}$ from null phase cancellation (§IV); (iii) a pre-registered discriminator — the EHT Sgr A* shadow — the one measurable place where the isotropic scalar-index reading, as written, diverges from GR (§VIII, kill 3); and (iv) a CANDIDATE recast (§IX) under which the medium response becomes a one-way inward flow ($v = \sqrt{2m/r}\,c$; Painlevé–Gullstrand), keeping GR exact and sending the natural home to `L4-TheAcousticOhm`.  
> **Epistemic Register:** Relativistic Kinematics / Applied Architecture ($Q\#$).  
> **Dependencies:** `ProofN_BiquaternionBridge.md`, `ProofQ_AlgebraicSyntax.md`, `Q4-OpenExhaust.md`, `Q7-4DExtrusions.md`, `Q8-TheBoundaryMechanics.md`, `Q12-GravitationalTopology.md`, `Q14-LeptonScaleCascade.md`, `L3-K4-to-K5-via-AC-Extension.md`, `L4-ThePlenum.md`, `L4-K4-Infinities-1.md`, `L4-TheAcousticOhm.md` (§IX: the flow-reading recast).

## 0. What is being demonstrated

This document is a **capability proof**. It is entered on the record, not offered for audition: the correspondence reproduces Schwarzschild's proper-time relation exactly — cross-term included — with zero fitted parameters; the posits it consumes are conceded on the record and classified in the datasheet (§VII); the verdict under the corpus's instrument table is CONFIRMED (Phase-Locking, instrument IV); and the appeal is pre-registered in §VIII, before any measurement. And the constant most often bolted on to compensate — $\Lambda$ — is not imported here at all: this is the $\Lambda = 0$ sector, and where the corpus does carry $\Lambda$, it derives it (the Planck angle at the horizon, `Q12` §VIII).

Instrument registration, per `llm-prooftypes.md`: **Phase-Locking** — the corpus/GR boundary is crossed with a preserved algebraic invariant: the exact proper-time factorization of §V.

The items carried as this document's claims, as a preview of what follows:

* **The exact cascade (§§I–III, §V).** General Relativity's Schwarzschild proper-time relation for radial motion is reproduced exactly as the multiplicative Power Factor cascade ($\text{PF}_{\text{total}} = \cos\theta_1 \cdot \cos\theta_2$) of two sequential phase factors — a kinematic rotation ($O_1$, rapidity $\varphi_1$, parameterizing the local velocity $v_{\text{loc}}/c$) and a gravitational phase tilt ($O_2$, parameterizing the local impedance gradient induced by the accumulated monotonic ledger ($\chi = \sum \Delta P_n$) through the escape ratio $2GM/rc^2$) — composing on the biquaternion Star-Norm ($N_* = P^2 - |\mathbf{Q}|^2$).
* **The register of the gravitational factor (§V).** The register of $O_2$ — state-side rotation on an internal axis, or medium-side rescaling of the frame's compilation rate — is examined in §V and left open.
* **The spatial metric (§IV).** The spatial metric component $g_{rr} = (1 - 2GM/rc^2)^{-1}$ follows from null geodesic phase cancellation ($d\phi = 0$) given the medium response $n(r) = \cos^{-2}\theta_2$ and the coordinate speed $c(r) = c \cos^2\theta_2$; the "unit area" relation $\sqrt{g_{00}}\sqrt{g_{rr}} = 1$ is thereby recovered as a theorem of these inputs rather than assumed.
* **The cross-term (§V).** The cross-term $(v^2/c^2)(2GM/rc^2)$ is not an ad-hoc post-Newtonian correction; it is the native algebraic product of sequential Power Factors.
* **The enforceable discriminator (§VIII, kill 3).** The isotropic scalar-index reading predicts a Sgr A* shadow deviation $\delta = +0.54$ against EHT's measured $\delta = -0.08 \pm 0.09$ (VLTI) / $\delta = -0.04\,{+0.09}/{-0.10}$ (Keck), excluding the isotropic reading at $\approx 7\sigma$. The 2PN light-deflection coefficient is $6\pi$ against GR's $15\pi/4$ — a weak-field confirmation of the same disagreement, not yet at measurement precision.
* **The flow-reading recast (§IX).** An alternative reading of the medium response — Painlevé–Gullstrand's flat spatial slices with an inward flow $v(r) = \sqrt{2m/r}\,c$ — keeps GR exact. The static, atemporal reading of $O_2$ carries no phase; the flow reading supplies it. Natural home: `L4-TheAcousticOhm` (the acoustic-horizon architecture, Unruh / Hamilton & Lisle).

The datasheet (§VII) classifies every input the demonstration consumes; what the document still owes stands after the kill conditions of §VIII, under Open Questions.

---

## Constants and Physical Inputs

* $c = 299{,}792{,}458\text{ m/s}$ (exact by definition; the corpus writes it in medium-constitutive form $c = 1/\sqrt{\mu_0\epsilon_0}$, with $\mu_0$ and $\epsilon_0$ measured — `L4-ThePlenum.md` §II.3); $G = 6.67430 \times 10^{-11}\text{ m}^3\cdot\text{kg}^{-1}\cdot\text{s}^{-2}$.
* $Z_0 = \sqrt{\mu_0/\epsilon_0} \approx 376.730313\ \Omega$ (consumed via `Q12` §IV.2, updates conducted on the $Z_0$ line, and §VI.3, where the horizon transits from the $Z_0$ line to the terminal wall).
* State variable: $\mathbb{Z} = P + h\mathbf{Q}$, where $P \in \mathbb{R}^+$ and $\mathbf{Q} \in \mathbb{R}^3$.
* Star-Norm invariant: $N_*(\mathbb{Z}) = \mathbb{Z}\mathbb{Z}^\dagger = P^2 - |\mathbf{Q}|^2 = (m_0 c^2)^2$.

```python
from mpmath import mp, mpf, sqrt
mp.dps = 30

c = mpf('299792458'); G = mpf('6.67430e-11')
M_earth = mpf('5.9722e24'); r_earth = mpf('6371000')

def gr_dtau_sq(beta, r_over_rs):
    """Schwarzschild (dtau/dt)^2 for locally measured beta (static split)."""
    return (1 - 1 / r_over_rs) * (1 - beta**2)

def cascade_dtau_sq(beta, r_over_rs):
    """PF cascade: cos^2(theta_1) * cos^2(theta_2)."""
    return (sqrt(1 - beta**2) * sqrt(1 - 1 / r_over_rs))**2

# Distinct-factor cases (r = 10 rs). The former worked example (v = v_esc at
# Earth's surface) is retired: (v_esc/c)^2 = rs/r identically, so PF1 = PF2 and
# the example contained no pair of distinct factors.
for beta in (mpf('0.3'), mpf('0.8')):
    gr = gr_dtau_sq(beta, 10)
    pf = cascade_dtau_sq(beta, 10)
    print("beta =", mp.nstr(beta, 4),
          "GR:", mp.nstr(gr, 8), "cascade:", mp.nstr(pf, 8),
          "diff:", mp.nstr(gr - pf, 3))
# beta = 0.3 GR: 0.819 cascade: 0.819 diff: -9.86e-32
# beta = 0.8 GR: 0.324 cascade: 0.324 diff: -4.93e-32
# (diffs are round-off at the set precision; the identity is algebraic)

# Any-path generality: circular path at r = 10 rs with v_loc = 0.2c (a circular
# PATH, not the circular geodesic — the geodesic has v_loc^2 = 1/18 and
# (dtau/dt)^2 = 0.85):
print(mp.nstr(gr_dtau_sq(mpf('0.2'), 10), 8))         # 0.864

# The actual GR correspondence at Earth's surface, v = v_esc:
rs = 2 * G * M_earth / c**2
v_esc = sqrt(2 * G * M_earth / r_earth)
beta = v_esc / c
print(mp.nstr(gr_dtau_sq(beta, r_earth / rs), 18))    # 0.999999997215475478
print(mp.nstr(cascade_dtau_sq(beta, r_earth / rs), 18))   # 0.999999997215475478
# rs ≈ 8.870 mm; the correspondence holds exactly in the strong field as well
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

Write $|\mathbf{Q}|^2 = |\mathbf{Q}|_\parallel^2 + |\mathbf{Q}_\perp|^2$: a boost along the chosen axis acts only on the parallel sector $(P, |\mathbf{Q}|_\parallel)$ and leaves $\mathbf{Q}_\perp$ untouched. Evaluating the Star-Norm verifies that it is conserved identically for all $\varphi$, with the cross terms shown:
$$N_*(\mathbb{Z}') = P^2\cosh^2\varphi + 2P|\mathbf{Q}|_\parallel\cosh\varphi\sinh\varphi + |\mathbf{Q}|_\parallel^2\sinh^2\varphi - P^2\sinh^2\varphi - 2P|\mathbf{Q}|_\parallel\sinh\varphi\cosh\varphi - |\mathbf{Q}|_\parallel^2\cosh^2\varphi - |\mathbf{Q}_\perp|^2$$
$$= P^2(\cosh^2\varphi - \sinh^2\varphi) - |\mathbf{Q}|_\parallel^2(\cosh^2\varphi - \sinh^2\varphi) - |\mathbf{Q}_\perp|^2 = P^2 - |\mathbf{Q}|_\parallel^2 - |\mathbf{Q}_\perp|^2 = N_*(\mathbb{Z})$$

The cross terms $2P|\mathbf{Q}|_\parallel\cosh\varphi\sinh\varphi$ cancel identically against $-2P|\mathbf{Q}|_\parallel\sinh\varphi\cosh\varphi$ (at $(P, |\mathbf{Q}|_\parallel, \varphi) = (3, 4, 0.5)$ their common magnitude is $14.1024$), and the transverse component rides through unchanged because the boost does not act on it.

### Rapidity Addition and the Tangent Boundary
For sequential boosts along a common spatial axis, rapidities add linearly:
$$\varphi_{12} = \varphi_1 + \varphi_2$$
Defining the kinematic parameter $\beta \equiv \tanh\varphi$:
$$\beta_{12} = \tanh(\varphi_1 + \varphi_2) = \frac{\tanh\varphi_1 + \tanh\varphi_2}{1 + \tanh\varphi_1 \tanh\varphi_2} = \frac{\beta_1 + \beta_2}{1 + \beta_1 \beta_2}$$

The velocity addition law of Special Relativity is the native composition rule of hyperbolic rotations on the Star-Norm — for boosts on a **common axis**. The parameter is bounded by $|\beta| < 1$; equality $\beta = 1$ is the $\theta = 90^\circ$ Tangent Singularity (`Q8-TheBoundaryMechanics.md` Movement IV; expect there: the tangent band and the $\tan(90^\circ)$ divergence at the boundary).

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
In `Q14-LeptonScaleCascade.md` §III, coordinate time $dt$ is the spatial distance between successive $P$-ledger entries written to the $R$-pole (expect there: the two-stroke collision engine that stamps $dt$ at the impact site); §IV.2 reads relativistic time dilation as **buffer inflation** — the state vector rotating its capacity into the uncompiled buffer $\mathbf{Q}$. The identification of proper time $d\tau$ as the local compilation step is this document's gloss on that kinematics.

Under $O_1$, the local compilation rate scales directly with the Power Factor:
$$\frac{d\tau}{dt} \Bigg|_{O_1} = \cos\theta_1 = \sqrt{1 - \frac{v_{\text{loc}}^2}{c^2}}$$

Relativistic time dilation is not the mechanical slowing of an external clock; it is the **reduction of the local Power Factor** as the state vector rotates capacity out of the scalar ledger ($P$) into the vector buffer ($|\mathbf{Q}|$).

---

## III. Operation $O_2$: Gravitational Potential ($2GM/rc^2$)

In `Q12-GravitationalTopology.md` §III (expect there: the single monotonic coordinate $\chi = \sum \Delta P_n$ and the non-equilibrium horizon thermodynamics), a source mass $M$ is an accumulated concentration of monotonic ledger entries. This concentration imposes an impedance gradient on the surrounding Plenum buffer ($H_{\text{incoh}}$ — the medium itself: `L4-ThePlenum.md` §I–§II; expect there: the uncompiled scale-invariant buffer and its constitutive parameter set $\epsilon_0, \mu_0, Z_0, c$).

A test particle positioned at coordinate radius $r$ from the source mass undergoes operation $O_2$: a phase tilt mixing its scalar capacity into the vector buffer by an angle set by the local gravitational potential.

```
                  THE GRAVITATIONAL PHASE TILT O₂
                  
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

The functional form $\sin^2\theta_2 \equiv r_s/r$ is defined on this document's consumed inputs ($r_s = 2GM/c^2$; the source ledger $\chi$, `Q12` §III); what fixes the $1/r$ dependence, the factor of 2 and the square root is carried under Open Questions.

The local compilation rate for a static test mass in the gravitational field is:
$$\frac{d\tau}{dt} \Bigg|_{O_2} = \cos\theta_2 = \sqrt{1 - \frac{2GM}{rc^2}}$$

At the boundary $r = r_s$, $\sin\theta_2 = 1 \implies \theta_2 = 90^\circ$. The local Power Factor vanishes ($\cos\theta_2 = 0$). As derived in `Q12` §VI.3 (expect there: the horizon's transition from a distributed $Z_0 \approx 377\ \Omega$ transmission line into a lumped terminal reactance wall), the horizon is not an infinite density singularity; it is a **terminal reactance wall ($X_C \to \infty$)** where local ledger compilation ceases. The wall mechanics — the power factor collapsing to zero as the phase angle shears into quadrature — are `Q8-TheBoundaryMechanics.md` Movement II (expect there: the shear ceiling, $|Z|$ diverging while $P = |S|\cos\varphi \to 0$).

---

## IV. Derivation of the Spatial Metric ($g_{rr}$) from Null Phase Cancellation

Standard general relativity derives $g_{rr} = (1 - 2GM/rc^2)^{-1}$ from the vacuum field equations $R_{\mu\nu} = 0$. Earlier formulations of the $K_4$ correspondence relied on a heuristic "unit area conservation ansatz" ($\sqrt{-g_{00}}\sqrt{g_{rr}} = 1$).

We derive $g_{rr}$ from **Null Geodesic Phase Cancellation (`Q14-LeptonScaleCascade.md` §I; expect there: the null geodesic cancellation $ds^2 = 0 \Leftrightarrow d\phi = 0$)**:

Along a radial light ray propagating through the gravitational field, proper time is identically zero ($ds^2 = 0, d\tau = 0$):
$$0 = g_{00} c^2 dt^2 - g_{rr} dr^2 \implies \frac{dr}{dt} = c \sqrt{\frac{g_{00}}{g_{rr}}}$$

In an impedance-bearing medium with refractive index $n(r)$, the coordinate velocity of light is:
$$v_{\text{phase}}(r) = \frac{dr}{dt} = \frac{c}{n(r)}$$

The medium response is the load-bearing posit of this section: a phase gradient across a boundary presents an effective refractive index that scales inversely with the local Power Factor squared,
$$n(r) = \frac{1}{\cos^2\theta_2} = \left(1 - \frac{2GM}{rc^2}\right)^{-1}$$

The scaling is carried here as the correspondence's medium response. The corpus sites that carry the impedance substrate do not state it: `L4-ThePlenum.md` §II.3 (expect there: $c$ as a medium parameter, $c = 1/\sqrt{\mu_0\epsilon_0} = 1/\sqrt{LC}$), §II.4 (expect there: the free-medium reading — no slow light, the free photon always sees $c$ — and the bounded-frame extractive response $R_{\text{drag}} = R_K$), and `Q8-TheBoundaryMechanics.md` Movement II (expect there: the shear ceiling — power factor collapsing to zero at a quadrature wall) supply the vocabulary and the wall mechanics, not the $1/\text{PF}^2$ form. Whether that form is derivable from the impedance physics or is native to the correspondence is carried under Open Questions.

Equating the phase velocity to the metric ratio:
$$\frac{dr}{dt} = c \cos^2\theta_2 = c \sqrt{\frac{g_{00}}{g_{rr}}}$$

Substitute the temporal metric component $g_{00} = \cos^2\theta_2 = 1 - 2GM/rc^2$:
$$\cos^2\theta_2 = \sqrt{\frac{\cos^2\theta_2}{g_{rr}}} = \frac{\cos\theta_2}{\sqrt{g_{rr}}}$$
$$\sqrt{g_{rr}} = \frac{\cos\theta_2}{\cos^2\theta_2} = \frac{1}{\cos\theta_2}$$

Squaring both sides yields the exact spatial metric component:
$$\mathbf{g_{rr} = \frac{1}{\cos^2\theta_2} = \left(1 - \frac{2GM}{rc^2}\right)^{-1}}$$

The spatial metric strain $g_{rr}$ is the exact geometric dilation required for the wave to maintain zero net phase accumulation ($d\phi = 0$) across the gravitational impedance gradient. Given the inputs, the "unit area" relation is recovered as a theorem: $\sqrt{g_{00}}\sqrt{g_{rr}} = \cos\theta_2 \cdot \cos^{-1}\theta_2 = 1$ identically.

Along a radial path the coordinate light delay is exact:
$$\Delta t_{\text{radial}} = \int \left(\frac{1}{v_{\text{phase}}(r)} - \frac{1}{c}\right) dr = \frac{1}{c} \int_{r_1}^{r_2} \left(\frac{1}{\cos^2\theta_2} - 1\right) dr = \frac{2GM}{c^3} \ln\!\left(\frac{r_2 - r_s}{r_1 - r_s}\right)$$
with integrand $r_s/(r - r_s)$. The quoted grazing-ray expression $\frac{2GM}{c^3}\ln\left(\frac{4 r_1 r_2}{d^2}\right)$ is the standard **first-order (1PN, impact parameter $d$)** Shapiro delay for a ray of closest approach $d$: the constant matches, the functional form requires the ray geometry, and it carries its "≈". The radial integral and the grazing-ray formula agree at 1PN order, not exactly.

---

## V. The Composed Operation $O_1 \circ O_2$: The Multiplicative Cascade

Now evaluate a test particle that is both **moving at local velocity $v_{\text{loc}}$** and **positioned at coordinate radius $r$** within the gravitational field.

The power-factor vocabulary — $\text{PF}$ as the cosine of the phase angle, the commit/hold split of $S = P + jQ$ — is `L3-K4-to-K5-via-AC-Extension.md` §V (expect there: the power-factor table and the $45°$ equipartition threshold). The composition rule itself is this document's, and it is examined immediately below: when the kinematic rotation and the gravitational factor compose, their Power Factors enter **multiplicatively**:
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

*(The diagram reads $O_2$ as a state deformation for concreteness; the composition discussion below examines whether it is one.)*

### The Composition Rule and the Register of $O_2$

§I composes state-side boosts by **rapidity addition**; this section composes the two Power Factors **multiplicatively**. Both rules cannot govern the same composition. Three observations narrow the field.

**The collinear reading is closed.** If $O_2$ were a boost collinear with $O_1$'s, with a rapidity defined by $\tanh\varphi_2 = \sin\theta_2 = \sqrt{r_s/r}$, the two rules disagree by a quarter of the result: at $\tanh\varphi_1 = 0.3$, $\sin\theta_2 = 0.8$, rapidity addition gives $\operatorname{sech}(\varphi_1 + \varphi_2) = 0.4616$ while the cascade gives $0.5724$ — a $24\%$ gap. The cascade value is the one this section verifies against GR exactly ($\sqrt{g_{00}}\sqrt{1-\beta_1^2} = 0.6 \times 0.9539 = 0.5724$), so the collinear composition is not a live option: it is excluded by the correspondence this document already claims. Note also that no rapidity $\varphi_2$ is ever defined for $O_2$ — §III supplies only the angle $\theta_2$; the collinear reading had to invent one.

**Avenue A — $O_2$ as a rotation on an orthogonal internal axis.** For boosts whose internal axes are orthogonal, group composition gives exactly the cascade: $\gamma_{12} = \gamma_1 \gamma_2 (1 + \boldsymbol\beta_1 \cdot \boldsymbol\beta_2) = \gamma_1 \gamma_2$, verified by explicit matrix multiplication ($B_y(0.8)\,B_x(0.3)$: $\Lambda^0{}_0 = 1.7471414 = \gamma_1 \gamma_2$, a genuine $\text{SO}(3,1)^+$ element). Under this reading $N_*$-conservation is automatic and "two hyperbolic rotations" stands as written. The cost: nothing on the page fixes $O_2$'s axis. If the axis is the radial direction, radial motion makes the boosts collinear — excluded above. If the axis must be orthogonal to $O_1$'s velocity axis, it varies with the particle's heading: two particles at the same $r$ moving in different directions would tilt on different axes, which the impedance-gradient picture (one gradient, set by $\chi$ at $r$) does not support. No generator or axis is exhibited in this document.

**Avenue B — $O_2$ as a medium-side lapse.** $O_2$ is then not a state operation at all: it is the local rescaling of the frame's compilation rate by the impedance gradient — a property of the location ($r$), not of $\mathbb{Z}$. The receipts: the factorization $d\tau/dt = \sqrt{g_{00}}\,\sqrt{1 - v_{\text{loc}}^2/c^2}$ holds for **any spatial path in any static metric** (verified symbolically, and numerically on a circular path at $r = 10\,r_s$ with $v_{\text{loc}} = 0.2c$: $(d\tau/dt)^2 = 0.864$, matching GR), and any-path validity is native to the lapse form and unavailable to a fixed-axis boost. §III already frames $O_2$ as an impedance-gradient tilt, §VI already assigns the static metric components to the medium side and the kinematics to the state side, and the AC extension's own warning — do not reify $\omega$ into a background parameter; time is a property of the bounded frame's compilation cycle, not a container the frame sits inside (`L3-K4-to-K5-via-AC-Extension.md` §II) — argues against installing the gravitational factor as a second state-side driver. The cost: $O_2$ is then not an element of $\text{SO}(3,1)^+$; "two sequential hyperbolic phase rotations" must be read as one rotation and one medium-side phase factor (the header and §III's diagram are worded accordingly); and the multiplicative rule becomes rate composition across the state/medium boundary — stated here, derived nowhere yet.

Both avenues stand; neither is closed by this document. A third avenue — the flow reading — is developed in §IX and carries phase through the medium-side description, which Avenue B leaves static. What would settle the choice is carried under Open Questions.

### The Proper Time Rate
The combined local compilation rate is:
$$\frac{d\tau}{dt} = \text{PF}_{\text{total}} = \sqrt{1 - \frac{v_{\text{loc}}^2}{c^2}} \sqrt{1 - \frac{2GM}{rc^2}}$$

Two scope statements travel with this identity. First, it is **not restricted to radial motion**: the factorization $d\tau/dt = \sqrt{g_{00}}\,\sqrt{1 - v_{\text{loc}}^2/c^2}$ holds for any spatial path in any static metric ($g_{0i} = 0$); the radial restriction elsewhere in this section is presentation, not scope. (Circular path at $r = 10\,r_s$, $v_{\text{loc}} = 0.2c$: $(d\tau/dt)^2 = 0.864$, matching GR. The circular *geodesic* at that radius has $v_{\text{loc}}^2 = M/(r - 2M) = 1/18$ and $(d\tau/dt)^2 = 0.85$ — also matching.) Second, the factorization is exact for the **locally measured** velocity — the static-observer split. Under the coordinate velocity $dr/dt$ it fails: at $r = 10\,r_s$ with $\beta_{\text{coord}} = 0.2$, GR gives $g_{00} - g_{rr}\beta_{\text{coord}}^2 = 0.8556$, while $g_{00}(1 - \beta^2) = 0.864$. Whether the static-split convention is derivable from the Star-Norm architecture or postulated is carried under Open Questions; until derived, the correspondence is exact under a stated convention.

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

The same type discipline keeps the two readings of $O_2$ (§V) distinct: under the operator reading, $O_2$ would have to be a second state rotation; under the lapse reading it belongs with the impedance gradient $Z(\chi)$ on the medium side, and the cascade is a pullback identity across that boundary.

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
   (boosts on a common axis; the composition with the gravitational factor
    is the separate rule below — see §V)
 • Multiplicative Power Factor Cascade: PF_total = cos θ₁ · cos θ₂
   (composition rule of this document; exact for orthogonal internal planes
    and identical to the static-split factorization — §V)
 • The Cross-Term Identity: PF² = 1 - β² - sin²θ₂ + β²sin²θ₂
 • Tangent Singularity at PF = 0 (θ = 90°)
 ──────────────────────────────────────────────────────────────────────────────────────
 CATEGORY 1: SUBSTRATE INVARIANTS (Consumed, Never Derived)
 • Speed of Light: c (exact by definition; corpus constitutive form
   c = 1 / √(μ₀ε₀) with μ₀, ε₀ measured — L4-ThePlenum §II.3)
 • Characteristic Vacuum Impedance: Z₀ = √(μ₀/ε₀) ≈ 376.730313 Ω
   (consumed via Q12 §IV.2 — updates conducted on the Z₀ line — and Q12 §VI.3,
    where the horizon transits from the Z₀ line to the X_C → ∞ wall)
 • Gravitational Constant: G = 6.67430 × 10⁻¹¹ m³/(kg·s²)
 ──────────────────────────────────────────────────────────────────────────────────────
 CATEGORY 2: STATE INPUTS (Measured Boundary Parameters)
 • Source mass M (accumulated ledger concentration χ = Σ ΔP_n — Q12 §III)
 • Coordinate radius r
 • Local physical velocity v_loc (static-observer convention — §V, Open Questions)
 ──────────────────────────────────────────────────────────────────────────────────────
 CATEGORY 3: BRIDGES (Zero-Parameter Computed Relations)
 • Kinematic Power Factor: cos θ₁ = √(1 - v_loc² / c²)
 • Gravitational Power Factor: cos θ₂ = √(1 - 2GM / rc²)
   (functional form defined in §III on consumed inputs; horizon mechanics
    per Q12 §VI.3; what fixes the form — Open Questions)
 • Spatial Metric Derivation: g_rr = 1 / cos²θ₂ = (1 - 2GM / rc²)⁻¹
   (derived in §IV from the null condition given the medium response
    n(r) = cos⁻²θ₂ — the response is the load-bearing posit; §IV, Open Questions)
 • Exact Radial Proper Time: dτ/dt = cos θ₁ · cos θ₂
========================================================================================
 Provenance note: the four-category taxonomy has no slot for an imported
 structural posit; relations whose functional form is consumed from another
 document are marked inline here rather than reclassified.
========================================================================================
```

---

## VIII. Pre-Registered Boundary Falsifiers

Under the covenant's boundary diagnostics (`llm-prooftypes.md`), this relativistic phase-composition architecture is subject to three strict falsification conditions. The first two are **shared kill conditions**: since §V shows the cascade and GR (or SR) agree exactly on these structures, a violation falsifies the shared architecture, not one side of it. The third is the registered **discriminator**: the one measurable place where the isotropic scalar-index reading, as written, diverges from GR.

1. **Failure of the Multiplicative Cross-Term in Radial Relativistic Free-Fall (shared with GR):**  
   If precision atomic-clock measurements on a high-velocity probe in a strong gravitational gradient detect an operational proper-time rate ($d\tau/dt$) that violates the multiplicative cross-term $\left(\frac{v_{\text{loc}}^2}{c^2}\right)\left(\frac{2GM}{rc^2}\right)$, the shared architecture — GR and the Power Factor cascade together — is refuted. (At Earth's surface with $v = v_{\text{esc}}$ the cross-term is $\approx 1.94 \times 10^{-18}$: a second-post-Newtonian measurement frontier, and a shared one.)
2. **Breakdown of the Velocity Addition Law on the Star-Norm (shared with SR):**  
   If an experimental boost composition on high-energy states violates the collinear rapidity addition formula $\beta_{12} = (\beta_1 + \beta_2)/(1 + \beta_1\beta_2)$ in a vacuum, the Star-Norm isometry group $\text{SO}(3,1)^+$ fails — and with it the kinematic sector of standard relativity as well.
3. **The EHT Sgr A* Shadow Discriminator (the registered kill, enforceable now):**  
   The medium response of §IV, taken as a scalar index $n(r) = (1 - r_s/r)^{-1}$, is direction-blind. An isotropic scalar index implies a photon ring at $\rho = 4m$ with critical impact parameter $b_c = 8m$. General Relativity gives the photon ring at $r = 3m$ and $b_c = 3\sqrt{3}\,m$. Translating to the fractional shadow deviation $\delta \equiv (b_{\text{obs}} - b_{c,\text{GR}}) / b_{c,\text{GR}}$: the isotropic reading predicts $\delta = (8 - 3\sqrt{3})/(3\sqrt{3}) \approx +0.54$. The Event Horizon Telescope measures Sgr A*'s shadow at $\delta = -0.08 \pm 0.09$ (VLTI prior) and $\delta = -0.04\,{+0.09}/{-0.10}$ (Keck prior). The isotropic scalar-index reading is excluded by this measurement at $\approx 7\sigma$. The weak-field 2PN light-deflection coefficient confirms the same disagreement algebraically: ray-traced numerically, the isotropic $n(\rho) = (1 - 2m/\rho)^{-1}$ gives $\delta\phi = 4m/b + 6\pi(m/b)^2$ against GR's exact $4m/b + (15\pi/4)(m/b)^2$ — $6\pi$ vs $15\pi/4$ as the 2PN discriminator, agreeing at 1PN and diverging at 2PN (weak-field precision not yet at measurement). **The correspondence as written in §IV is refuted on the isotropic-response branch.** What survives, and where the architecture goes next, is §IX.

---

## IX. The Flow Reading: Painlevé–Gullstrand as the CANDIDATE Recast

With the isotropic scalar-index reading excluded by EHT (§VIII, kill 3), the medium response of §IV requires a direction-dependent formulation. Schwarzschild's own optical form carries that direction dependence as $n_r = n_t^2$: the radial index $n_r = 1/(1 - r_s/r)$ is the **transformer** (slope 2 in the small-$r_s/r$ limit), the tangential index $n_t = 1/\sqrt{1 - r_s/r}$ is the **carrier** (slope 1). The scalar reading flattened the pair to a single $n = 1/(1 - r_s/r)$ and inherited the radial direction's anisotropy as if it were isotropic — which EHT now rules out.

The medium reading that keeps GR exact is the **Painlevé–Gullstrand form** (Hamilton & Lisle 2008, "The river model of black holes"): flat spatial slices with the medium flowing inward at a position-dependent speed,
$$v(r) = \sqrt{\frac{2m}{r}}\,c$$
where the local phase velocity of light in the rest frame of the inflowing medium is still $c$. The identity Schwarzschild's $\sqrt{g_{00}} = \sqrt{1 - 2m/r}$ then reads as
$$\sqrt{1 - \frac{2m}{r}} = \sqrt{1 - \frac{v^2}{c^2}}$$
a special-relativistic $\gamma^{-1}$ factor of the flow speed. The second power factor of §V — $\text{PF}_2 = \cos\theta_2$ — becomes the time-dilation factor of a probe moving with the inflow rather than an intrinsic phase tilt of the uncompiled buffer.

**The static/atemporal case has no phase.** The scalar-index reading of §IV treated $O_2$ as a stationary impedance gradient — a property of location, not of motion. On the flow reading $O_2$ is a kinematic effect of the medium's one-way inward motion. The static case is the $v = 0$ limit, which carries no $\text{PF}_2$ at all: a strictly static geometry (pure $g_{00}$ reading with no flow) has no second phase factor, and the cross-term disappears. The phase is carried by the flow itself. The architecture gains an operational distinction between "static gravitational potential" (no $\text{PF}_2$ beyond the kinematic factor of something moving through the flow) and "gravitational potential with phase" ($\text{PF}_2$ supplied by inward medium motion), which the scalar reading could not draw.

**The horizon sits where the flow reaches $c$.** $v(r_s) = c$ is Schwarzschild's horizon exactly, and it is the acoustic-horizon structure (Unruh 1981, analog gravity): a one-way surface at which incoming signals are no longer separable from the medium's flow. This connects the §III wall mechanics ($r = r_s$ terminal reactance) to the broader analog-gravity reading of the corpus, where `L4-TheAcousticOhm` carries the acoustic-horizon architecture.

**Natural home: `L4-TheAcousticOhm`.** The flow reading sits inside the acoustic-ohm architecture more naturally than inside this document's Power Factor cascade. The $\text{PF}_2$ factor is still there — now read as a kinematic consequence of medium motion rather than a state-side rotation — and the recast carries the gravitational factor onto the medium-side of §VI's state/medium boundary without requiring a new rotation axis.

**Register.** CANDIDATE. The flow recast reproduces GR exactly where the scalar reading diverges (EHT shadow, 2PN deflection, exact lensing) and adds the static/atemporal distinction above as a framework-internal consequence. What this document has not shown is whether the flow $v(r) = \sqrt{2m/r}\,c$ emerges from the corpus's impedance physics (`L4-ThePlenum` §II–§III; `Q12-GravitationalTopology` §VI.3's $Z_0 \to X_C \to \infty$ transit) as a derived response rather than a reading borrowed from the known solution. That derivation is the next step, and `L4-TheAcousticOhm` is where it belongs.

**Kill for the recast.** Any strong-field observable where Painlevé–Gullstrand and Schwarzschild coordinates disagree would distinguish them — but none exist: they are one geometry in two coordinates. The live content is the medium reading (one-way flow, acoustic horizon) rather than a new number. Kills that reach the recast therefore take the form of generalized flow readings: an inward flow that is not $\sqrt{2m/r}\,c$ but some other dependence, tested against the same EHT shadow (fixing the form of the flow for a given source), against rotating-source shadows (Kerr PG), and against the acoustic-horizon architecture of `L4-TheAcousticOhm`.

---

### Open Questions

Carried after the kill conditions so the record distinguishes what this document establishes from what it still owes. Each item is open by decision, not by omission.

1. **The register of the gravitational factor.** §V leaves two readings of $O_2$ standing — the state-side rotation on an orthogonal internal axis, and the medium-side lapse — and §IX adds a third: the medium-side flow (Painlevé–Gullstrand). The collinear reading is closed by the document's own GR agreement; the EHT shadow closes the isotropic scalar-index reading of §IV; the flow reading of §IX is the CANDIDATE recast. What would settle it: an impedance-physics derivation of $v(r) = \sqrt{2m/r}\,c$ from `L4-ThePlenum` or `L4-TheAcousticOhm`, or an explicit account of how rates compose across the state/medium boundary in a non-flow reading.

2. **Where the medium response lives (updated).** The $1/\text{PF}^2$ scalar response $n(r) = \cos^{-2}\theta_2$ is refuted by the EHT shadow (kill 3). The flow reading supplies $v(r) = \sqrt{2m/r}\,c$ as the response in its stead. Whether that flow emerges from the corpus's impedance physics without presupposing Schwarzschild's known form, or is a native posit of the correspondence, is the item — now relocated to `L4-TheAcousticOhm`.

3. **Is the local velocity derived or postulated?** The cascade is exact only for the locally measured velocity (the static-observer split); under the coordinate velocity it fails (§V). If the static split is derivable from the Star-Norm architecture, the correspondence is a prediction; if it is postulated, the correspondence is a theorem about a chosen split. On the flow reading, "locally measured" means relative to the inflowing medium — a frame the flow supplies natively.

4. **Direction-dependence of the medium response.** Tied to kill 3. Schwarzschild's optical form has $n_r = n_t^2$: the radial index is the transformer, the tangential the carrier. The flow reading of §IX carries this direction dependence via the spatial flat-slicing and the inward flow direction. A derivation of $n_r = n_t^2$ from the corpus's impedance physics — rather than by borrowing it from Schwarzschild — is open.

5. **Rotating concentrations of ledger.** The factorization requires $g_{0i} = 0$. Kerr PG supplies a rotating analog of the flow reading; what replaces the multiplicative cascade for rotating sources, and does the any-path generalization of §V survive the rotation? (Gravity Probe B, LAGEOS and the EHT shadow of M87* are the eventual measuring sticks.)

6. **What fixes the gravitational angle, on the flow reading?** On the scalar-index reading, $\sin^2\theta_2 \equiv r_s/r$ was defined in §III on consumed inputs. On the flow reading, $\sin\theta_2 = v(r)/c = \sqrt{r_s/r}$ — the same angle, now read as a flow Mach number. Which framework-internal observable fixes $v(r) \propto 1/\sqrt{r}$ rather than some other exponent? Adjacent to item 2: the angle and the flow are the same posit seen from the phase side and the medium side.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (`aggregate-COMPILINGREALITY.txt`) to your LLM in order to audit or interrogate this work.

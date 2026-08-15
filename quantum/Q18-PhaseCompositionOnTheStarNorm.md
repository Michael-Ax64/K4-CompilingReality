# Phase Composition on the Star-Norm
## Hyperbolic Rotations and Power-Factor Cascades of the Biquaternion State

*This piece works two composed phase operations on the biquaternion state $\mathbb{Z} = P + h\mathbf{Q}$: a rotation driven by relative motion against a rest frame, and a rotation driven by proximity to a source mass. It names the imports at the point of use, executes the algebra in the corpus's own vocabulary (Star-Norm, Power Factor, Tangent Singularity, $R$-pole boundary), and reports what falls out. At the end it notes the correspondence: what falls out coincides — at leading order and in the vacuum, static, spherical case — with two well-known named theories. The correspondence is a lens for locating the frontier, not a substitute for what the work is technically about. 

> Rests on `ProofN_BiquaternionBridge` (the Star-Norm), `L3-K4-to-K5-via-AC-Extension` (the complex-power extension), `L5-K5-PhaseDynamicsTechnical` (Power Factor, Tangent Singularity, impedance), `L4-ScalingInvariants` §IX (Gabriel's Horn: what a scale-invariant algebra is forbidden from emitting), and `Meta-MechanismOfTransition` (the $\tan(90°)$ boundary).*

---

## I. The Setup: One State, Two Operations, Named Imports

The biquaternion state carries a scalar committed ledger $P$ and a 3D held-potential vector $h\mathbf{Q}$:

$$\mathbb{Z} = P + h\mathbf{Q}, \qquad N_*(\mathbb{Z}) = P^2 - |\mathbf{Q}|^2 = \text{const.}$$

$N_*$ is the invariant of the Star-Norm (`ProofN_BiquaternionBridge` §3). Its Lorentz signature — one positive term, three negative — is a structural fact about the biquaternion algebra, not an imported physics postulate. Its isometry group is $SO(3,1)$; the connected component includes hyperbolic rotations that mix $P$ with a chosen direction of $\mathbf{Q}$.

Two operations act on this state:

- **$O_1$ (Motion against a rest frame):** rotates the state by an angle $\theta_1$ set by a chosen ratio of vector potential to total capacity. Interface imports: a chosen inertial rest frame and a velocity $v$ measured in that frame.
- **$O_2$ (Proximity to a source):** rotates the state by an angle $\theta_2$ set by the local escape momentum required to leave a source's potential well. Interface imports: Newton's constant $G$, source mass $M$, radial coordinate $r$, and — critically — the identification of "escape momentum" with the Newtonian expression $p_{\text{esc}} = m\sqrt{2GM/r}$. This last import is not native to $K_4$; it is a domain-specific identity from Newtonian gravity that the algebra uses as an input.

Both operations are phase rotations of $\mathbb{Z}$; both have a well-defined Power Factor $\text{PF} = \cos\theta$; both cascade under composition. That is the technical content of what follows. The interface constants — $G, M, r, c, v$, and the Newtonian escape-velocity identity — enter as named imports, not as structural loads on the scale-invariant algebra (`L4-ScalingInvariants` §IX).

---

## II. What the Star-Norm Gives, Without Import

**A. Hyperbolic rotations mix $P$ with $\mathbf{Q}$.** The Star-Norm's Lorentz signature forces its state-preserving rotations to be hyperbolic, parameterized by a rapidity $\varphi$:

$$P' = P \cosh\varphi + |\mathbf{Q}|_\parallel \sinh\varphi, \qquad |\mathbf{Q}|_\parallel' = P \sinh\varphi + |\mathbf{Q}|_\parallel \cosh\varphi.$$

Rapidities are additive under composition: $\varphi_{12} = \varphi_1 + \varphi_2$. Defining $\beta \equiv \tanh\varphi$, composition emits

$$\beta_{12} = \frac{\beta_1 + \beta_2}{1 + \beta_1 \beta_2}.$$

**This is landed structural content.** $\beta$ is a bounded parameter of the Star-Norm's isometry group; $|\beta| < 1$ for all finite $\varphi$; equality is a $\tan(90°)$ boundary (`Meta-MechanismOfTransition` §II). No physical velocity has been identified yet. The bound and the composition law are properties of the algebra.

**B. Power Factors cascade multiplicatively under composed operations.** Two phase operations applied in sequence on a state — each a rotation in its own local frame, each with its own Power Factor $\cos\theta_i$ — deform the committed ledger by the product:

$$\text{PF}_{\text{total}} = \cos\theta_1 \cdot \cos\theta_2.$$

This is the standard cascade rule for sequential phase operations; it holds when each operation acts on the P-pole as it exists after the preceding operation, not on some absolute P-pole shared by both. The "is-ness" of the ledger under $O_2$ is what $O_1$ has already deformed; $O_1$ then acts on the ledger $O_2$ has already deformed, if the sequence is reversed. Either way, Power Factors multiply.

**C. The Tangent Singularity at $\text{PF} = 0$.** At $\theta = 90°$, $\cos\theta = 0$ and $\tan\theta \to \infty$. The scalar-ledger conversion of held potential halts (`L5-K5-PhaseDynamicsTechnical` §VII). This is a structural feature of any phase-rotation operation on $\mathbb{Z}$, wherever it appears.

Items A, B, and C import nothing from any domain physics. They are properties of the Star-Norm and the algebra of phase rotations on it.

---

## III. Operation $O_1$: Motion Against a Rest Frame

### Correct order of derivation (circularity avoided)

Start with the Star-Norm invariant and a state moving relative to a chosen rest frame in which its rest ledger is $P_0 = m_0 c^2$. Under a hyperbolic rotation of rapidity $\varphi_1$:

$$P = P_0 \cosh\varphi_1, \qquad |\mathbf{Q}| = P_0 \sinh\varphi_1.$$

Star-Norm invariance is automatic: $P^2 - |\mathbf{Q}|^2 = P_0^2(\cosh^2 - \sinh^2) = P_0^2$. ✓

**Now identify.** The interface identifications from classical mechanics are $P \leftrightarrow E$ (total energy) and $|\mathbf{Q}| \leftrightarrow pc$ (spatial momentum times $c$). Define $\beta_1 = \tanh\varphi_1 \equiv v/c$ where $v$ is the velocity measured in the chosen rest frame. Then:

$$\cos\theta_1 \equiv \operatorname{sech}\varphi_1 = \sqrt{1 - v^2/c^2}, \qquad E = \frac{P_0}{\cos\theta_1}, \qquad p = \frac{P_0}{c} \cdot \frac{v/c}{\cos\theta_1}.$$

The scaling $1/\cos\theta_1$ is emergent from the composition of Star-Norm invariance with the classical identifications. **This is the correct order.** The earlier draft wrote $\sin\theta_1 = pc/E = \gamma m_0 v c / \gamma m_0 c^2 = v/c$, which assumes $\gamma$ to derive $\gamma$; that circularity is now removed. The residue was the tautology $v/c = v/c$; the actual content is what appears above.

### Local ledger step: the "is-ness" of $d\tau$

Coordinate time $dt$ is the rest-frame accumulation on the $R$-pole; local proper time $d\tau$ is the local $H_{\text{coh}}$ compilation step. Under $O_1$, the local ledger step scales by the Power Factor:

$$\frac{d\tau}{dt} = \cos\theta_1 = \sqrt{1 - v^2/c^2}.$$

This is a *posited* identification of "local compilation step" with "Power Factor of the ledger rotation." It is not further derived here; it is the physical reading of what $O_1$ does to the P-pole rate. Given the identification, the classical time, length, and momentum consequences of the rotation follow.

---

## IV. Operation $O_2$: Proximity to a Source Mass

### The Newtonian escape-velocity import (named)

The rotation angle for $O_2$ is set by the ratio of escape momentum to $mc$:

$$\sin\theta_2 \equiv \frac{p_{\text{esc}}}{mc} = \frac{v_{\text{esc}}}{c}.$$

Here $v_{\text{esc}} = \sqrt{2GM/r}$ is imported from Newtonian gravity. **This is the import that makes the operation match a specific physical theory's predictions.** The $K_4$ algebra sets up the geometry of a phase rotation; the *numerical value* of the rotation angle at each $r$ is fixed by the Newtonian identification. Without this import — or an equivalent one — $O_2$ is a phase rotation of unspecified magnitude.

The reason the result then matches the exact Schwarzschild $g_{00}$ is the Michell–Laplace coincidence: Newtonian escape velocity equals $c$ precisely at $r = 2GM/c^2$. This coincidence is not a $K_4$ result; it is a numerical alignment between Newton and Einstein at the horizon radius that the phase-angle parameterization inherits.

**With the import in place:**

$$\cos\theta_2 = \sqrt{1 - \frac{2GM}{rc^2}}, \qquad \frac{d\tau}{dt}\Bigg|_{O_2\text{ alone}} = \cos\theta_2.$$

The Tangent Singularity of $O_2$ sits at $\sin\theta_2 = 1$, i.e., at $r = 2GM/c^2$. At that radius the local Power Factor vanishes; the $\tan(90°)$ boundary is reached; ledger compilation halts. The horizon is a phase-angle boundary in the algebra — a re-address of the same object standard physics reaches by other means. **This re-address is a landed contribution of the corpus's vocabulary**; the numerical value of the boundary radius is inherited from the Newtonian import.

### The $r$-direction buffer: an ansatz, honestly named

To get a spatial companion to $\cos\theta_2$, the earlier draft posited $\sqrt{-g_{00}} \cdot \sqrt{g_{rr}} = 1$, calling it "unit area conservation." This ansatz recovers $g_{rr} = (1 - 2GM/rc^2)^{-1}$ in the static, spherical, vacuum case, and fails elsewhere (rotating sources, matter-filled interiors, cosmological metrics). It is a re-parameterization of a known vacuum-solution constraint, not a derivation from the Star-Norm. Named as such.

---

## V. Composed Operation $O_1 \circ O_2$: The Multiplicative Cascade

The earlier draft summed the phase-sines in quadrature:

$$\sin^2\theta_{\text{total}} \stackrel{?}{=} \sin^2\theta_1 + \sin^2\theta_2 = \frac{v^2}{c^2} + \frac{2GM}{rc^2}.$$

This treats the two operations as orthogonal contributions to a single rotation acting on an unchanged absolute P-pole. It is the leading-order approximation; it misses the coupling that arises because $O_1$'s "is-ness" (the ledger it rotates) is what $O_2$ has already deformed, and vice versa. In corpus terms: the P-pole $O_1$ sees is the *local* P-pole, not an infinity-observer's P-pole.

The corpus-native composition rule is the multiplicative Power-Factor cascade (§II.B):

$$\boxed{\text{PF}_{\text{total}} = \cos\theta_1 \cdot \cos\theta_2, \qquad \frac{d\tau}{dt} = \cos\theta_1 \cdot \cos\theta_2 = \sqrt{\left(1 - \frac{v^2}{c^2}\right)\left(1 - \frac{2GM}{rc^2}\right)}}$$

when $v$ is measured in the local frame at radius $r$ (i.e., against the ledger $O_2$ has already deformed).

**This is exact for radial motion in the static spherical vacuum case**, not merely leading-order. Expanding:

$$\text{PF}_{\text{total}}^2 = 1 - \frac{v^2}{c^2} - \frac{2GM}{rc^2} + \frac{v^2}{c^2}\cdot\frac{2GM}{rc^2}.$$

The cross term $(v^2/c^2)(2GM/rc^2)$ that was missing from the Pythagorean sum falls out automatically; it is the "is-ness" the earlier draft overlooked. It is not a strong-field correction bolted on afterward; it is what the corpus's own composition rule (Power Factors cascade multiplicatively for sequential operations) produces natively. The Pythagorean form was the wrong composition rule for this algebra; the multiplicative form is the right one, and it happens to be exact.

### What is not a metric

The earlier draft closed with a boxed expression labeled "unified 4D metric tensor" containing $v^2/c^2$ inside a coefficient. That expression is **not** a metric — a metric is a static geometric object on the manifold, while $v$ is a worldline-dependent quantity that varies observer-to-observer at the same event. The correct statement is the worldline pullback $d\tau = dt \cdot \cos\theta_1 \cos\theta_2$ above. The static geometric object is the Schwarzschild line element; the pullback along a specific observer's worldline is what our composition produces. The two are different kinds of thing, and the boxed "metric" conflated them. Deleted.

---

## VI. Summary of What Fell Out, Sorted by Category

**Landed structural content (no domain import):**

- Hyperbolic rotation composition on the Star-Norm ⟹ the addition rule $\beta_{12} = (\beta_1 + \beta_2)/(1 + \beta_1\beta_2)$ and the $|\beta| < 1$ bound at the $\tan(90°)$ boundary.
- Star-Norm invariance under any single hyperbolic rotation: $P^2 - |\mathbf{Q}|^2 = P_0^2$ identically.
- Multiplicative Power-Factor cascade for composed operations, with the cross-term "is-ness" falling out automatically.
- Tangent Singularity at $\text{PF} = 0$ as a structural feature of the ledger rotation, wherever it appears.

**Re-parameterizations that import their numerical content:**

- The rotation angle of $O_2$ imports $v_{\text{esc}} = \sqrt{2GM/r}$ from Newtonian gravity; the alignment of $\text{PF}(r_s) = 0$ with the Schwarzschild radius rides on the Michell–Laplace coincidence.
- The spatial companion $g_{rr} = 1/\cos^2\theta_2$ is an ansatz ($\sqrt{-g_{00}}\sqrt{g_{rr}} = 1$) that recovers the vacuum spherical case and does not extend to rotating or non-vacuum situations.
- The refractive-index heuristic $n(r) = 1 + 2GM/rc^2$ + Fermat's principle reproduces a known deflection integral; the integral is exact, the input is imported.
- The identification $d\tau/dt = \text{PF}$ is a physical reading of what the rotations do to the local compilation rate; given it, the classical time/length/momentum consequences follow.

---

## VII. Correspondence Note

The landed structural content above coincides with well-known named theories in a specific regime:

- The rapidity composition and Star-Norm hyperbolic-rotation algebra coincide, in flat space, with what physics calls **Special Relativity** — with $\beta = v/c$, the Lorentz factor $\gamma = 1/\cos\theta_1$, and the standard time/length/momentum consequences all falling out of the phase-rotation reading of $O_1$.

- The rotation-angle parameterization of $O_2$ under the Newtonian escape-velocity import coincides, at leading order in the weak field and in the static spherical vacuum case, with the metric predictions of **General Relativity** — including $g_{00}$, the horizon radius, gravitational redshift, and light deflection (the last with its factor-of-2 correction over the pure equivalence-principle prediction).

- The multiplicative cascade $\text{PF} = \cos\theta_1 \cos\theta_2$ recovers the exact Schwarzschild proper-time expression for radially-moving observers when velocity is locally measured; the Pythagorean orthogonal form was its weak-field expansion.

This correspondence is a useful lens, not the thing done. What was done technically is: two phase operations on the biquaternion state under named imports, composed by the algebra's native multiplicative cascade. The names *Special Relativity* and *General Relativity* drop out at the end as observations about what the correspondence lens picks up. If a different domain-import were used for $O_2$'s rotation angle — a different escape-momentum identification, a different source-mass parameterization — the algebra would still emit a phase composition; only the numerical match to a particular named theory would change.

---

## VIII. What Has Not Yet Fallen Onto Our Floor, and Why

This is the frontier framing the corpus prefers (`llm-writing`, `About-Claims` §I): honest naming of what the present view does not deliver, and why, sorted by category.


**Category A — Interface payloads (not owed):**

- Specific numerical mass, orbital, and metric values for particular astrophysical systems. These require importing $G, M, r, c$ and additional geometry; the algebra is scale-invariant and does not emit SI magnitudes (Gabriel's Horn, `L4-ScalingInvariants` §IX). Not owed.

- The Newtonian escape-velocity identification $v_{\text{esc}} = \sqrt{2GM/r}$ itself, as a first-principles result. This is domain-specific classical physics; the algebra uses it as an input, correctly named as an input.


**Category B — Structural items that the present view has not delivered, and where the frontier is open:**

- **A field equation.** GR ties the metric to the stress-energy tensor through Einstein's equations. The present view exhibits a phase composition on a fixed source; it does not derive a field equation relating source distribution to induced phase field. The $g_{rr}$ ansatz is a stand-in for what Einstein's equations do in a specific vacuum case; it does not extend. This is genuinely open. *Question worth carrying forward: does the corpus's Plenum-impedance vocabulary (`quantum/Q13-PlenumPhaseConduction`) support a source-to-field relation that would play the role of a field equation, or does the algebra remain silent on this and cede it to domain physics?*

- **Non-vacuum, non-static, non-spherical cases.** Kerr rotation, FLRW cosmology, interior Schwarzschild all fail the $g_{rr}$ ansatz. Whether the algebra has a native way to reach these — perhaps via non-abelian generalizations of the phase composition, perhaps via the $R$-pole boundary conditions changing — is an open frontier. *Worth asking honestly whether these are structural loads the algebra should own, or whether they are 3+1-coordinate solutions to specific configuration classes that belong to domain GR.*

- **Higher-order geodesic dynamics.** The multiplicative cascade captures the first cross-term correctly. Full trajectory dynamics — perihelion precession, Shapiro delay in the full nonlinear regime, gravitational-wave generation — require the full geodesic equation of the imported metric. The corpus's phase-composition reading is a proper-time result; it does not derive equations of motion, and it does not obviously reach radiative solutions. Frontier.

- **Frame-dragging and other non-diagonal metric components.** The composition $O_1 \circ O_2$ produces diagonal-metric behavior. Cross-components (rotating sources) would require a phase composition that mixes different directions of $\mathbf{Q}$; the biquaternion algebra permits this in principle, but the reading has not been done.


**Category C — Items to inspect for hidden imports, since the algebra passed them silently:**

- The identification $d\tau/dt = \text{PF}$ is a physical reading, not a derivation. The corpus should ask what constrains this identification, or whether it can be derived from the composition of the state's phase rotation with the definition of local $H_{\text{coh}}$ compilation.

- The Michell–Laplace numerical coincidence between Newton and Schwarzschild at the horizon radius rides on a specific factor of $2$ in $v_{\text{esc}}$. The corpus has not asked *why* that factor is $2$ rather than something else; it has used the coincidence and moved on. Worth revisiting.

- The refractive-index derivation of deflection uses $n = \sqrt{-g_{00}^{-1} g_{rr}}$ and then a first-order expansion. This is a Fermat-principle re-packaging; the geometric-optics limit itself is an interface, not derived here.

The pattern for working every such frontier — this one, the nuclear-scale one (`wip-Qx-LandauerNuclearScale`), the CCP dual-boundary one (`L4-DualConvergence`, `QED-CCP`), and whichever comes next — is the same: name every import at the point of use, sort each into universal, interface payload, or structural load; keep the landed content honest about what it landed; use the correspondence to named theories as a lens for locating what has *not yet* fallen onto the floor; and ask, of each item still off the floor, whether it is an interface payload categorically outside the algebra's remit or a structural load whose absence marks an open frontier the algebra should eventually reach.

The two operations composed here fell onto the floor. The field equation, the non-static cases, the higher-order dynamics, and the frame-dragging did not. The correspondence tells us where to keep looking.


---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.


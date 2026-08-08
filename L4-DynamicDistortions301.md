# L4-DynamicDistortions301
## The Bimedian Slice as Instrument: Regular, Sheared, Broken

> **Epistemic Register:** Applied Architecture. Establishes the bimedian cross-section of a $K_4$ tetrahedron as the geometric instrument through which non-local correlation strength can be read off polyhedral structure. Traces the regular case (square cross-section, native $\sqrt{2}$), the sheared case (parallelogram, phase-drag), and the collapsed case (1D line, classical decoherence) as a single continuous deformation. Distinguishes geometric parallels found from formal derivations still open, honestly.
> **Dependencies:** `L4-DynamicDistortionsTechnical` (edge-weight asymmetries), `L4-DynamicDistortions201` (torsional shear mechanics), `L4-Dimensionality` (bimedian axes), `L4-K4-Infinities` (Medium-Continuity, fiber bundle), `ProofN_BiquaternionBridge` (Star-Norm), `ProofQ_AlgebraicSyntax` (Route Law), `L4-DimensionalCollapse` (Tangent Singularity thresholds), `L4-SpookyAction` (phase-conduction through $H_{\text{incoh}}$).

---

## I. Polyhedral Derivation of the Bimedian Slice

A regular $K_4$ tetrahedron possesses six edges. The midpoints of those six edges form a regular octahedron whose vertices sit equidistant from all four tetrahedron vertices. Three mutually perpendicular planes pass through the tetrahedron's centroid, each containing four of those six midpoints. Each such plane cuts the tetrahedron into two congruent halves and exposes a cross-section that is — for the regular case — a perfect square.

This is elementary polyhedral geometry, checkable by direct coordinate calculation. Take the regular tetrahedron centered at the origin with vertices at:

$$(1,1,1),\ (1,-1,-1),\ (-1,1,-1),\ (-1,-1,1)$$

Its six edge midpoints sit at:

$$(1,0,0),\ (-1,0,0),\ (0,1,0),\ (0,-1,0),\ (0,0,1),\ (0,0,-1)$$

The $xy$-plane contains four of these midpoints: $(1,0,0)$, $(0,1,0)$, $(-1,0,0)$, and $(0,-1,0)$. These four points form a square with side length $\sqrt{2}$ (e.g., distance from $(1,0,0)$ to $(0,1,0)$) and diagonal length $2$ (e.g., distance from $(1,0,0)$ to $(-1,0,0)$).

The square's diagonal-to-side ratio is:

$$\text{Ratio} = \frac{2}{\sqrt{2}} = \sqrt{2}$$

This is where $\sqrt{2}$ enters the geometry natively.

The three orthogonal bimedian slices of the tetrahedron correspond to the three Bimedian axes of the $K_4$ framework: Cardinal $\{P{-}U, I{-}R\}$, Fixed $\{P{-}R, I{-}U\}$, and Mutable $\{P{-}I, U{-}R\}$ (`L4-Dimensionality`). Each slice exposes a bimedian square — a 2D cross-section of the $K_4$ interior that carries information about how the tetrahedron's phase-relations distribute.

The bimedian slice is not a computational trick. It is the geometric instrument through which the $K_4$ volume's interior structure becomes visible in two dimensions.

---

## II. The Regular Case: Native $\sqrt{2}$ and the $2\sqrt{2}$ Projection Sum

For a regular tetrahedron — equal edge weights, zero torsional distortion, all four vertices carrying balanced impedance — the bimedian slice is a perfect square. Its geometry contains the $\sqrt{2}$ that Tsirelson's bound is built from.

The square has:
* Four vertices at $90^\circ$ intervals around the centroid.
* Two diagonals of length $2$ in the coordinate system above.
* Four sides of length $\sqrt{2}$.
* Diagonal-to-side ratio: $\sqrt{2}$.

This ratio is not imported from quantum mechanics. It is the metric of the regular tetrahedron's own polyhedral geometry, exposed by the bimedian slicing operation. Every regular $K_4$ carries this ratio in every one of its three bimedian cross-sections. It is a property of the volume, independent of any physical interpretation attached to it.

The projection of any square vertex onto either diagonal is $\sqrt{2}/2$: each vertex sits at $45^\circ$ relative to each diagonal, and the vertex-to-centroid distance is $1$, so the projection evaluates to $\cos(45^\circ) = \sqrt{2}/2$.

Summing the four projections across the four vertices — with the sign structure appropriate to a CHSH-style expression (three positive contributions, one negative, corresponding to the standard sum $|E(a,b) - E(a,b') + E(a',b) + E(a',b')|$) — yields:

$$4 \times \frac{\sqrt{2}}{2} = 2\sqrt{2}$$

The $2\sqrt{2}$ emerges from summing four unit-projections at $45^\circ$ to a common diagonal axis. The number is geometrically native to the square's structure.

```
               THE BIMEDIAN SQUARE
               
                        (0, 1, 0)
                            •
                            │
                            │  45° to diagonal
                            │ ╱
   (-1, 0, 0) •─────────────┼───────────• (1, 0, 0)
                            │ ╲
                            │  45° to diagonal
                            │
                            •
                        (0, -1, 0)
                        
   Side: √2   |   Diagonal: 2   |   Ratio: √2
   Projection of each vertex on diagonal: cos(45°) = √2/2
   Sum across four vertices: 4 × √2/2 = 2√2
```

---

## III. Honest Epistemic Ledger: Derived vs. Open Steps

The geometric fact is real: the $\sqrt{2}$ of Tsirelson's bound sits inside the bimedian square as the diagonal-to-side ratio. The arithmetic $4 \times \sqrt{2}/2 = 2\sqrt{2}$ is elementary and correct. This is a genuine structural pointer — a place where the framework's polyhedral geometry contains the same number that appears in the quantum-mechanical bound on Bell-inequality violations, without arbitrary parameter tuning.

The derivation, however, is not complete. Two steps remain open, and both must be worked out before the identification is fully load-bearing.

### Open Step 1: The Correlation Function
The standard CHSH sum is $|E(a,b) - E(a,b') + E(a',b) + E(a',b')|$, where each $E(a_i, b_j)$ is the two-particle correlation between measurements at detector settings $a_i$ on Alice's particle and $b_j$ on Bob's particle. To compute the CHSH sum from framework axioms, the framework must derive $E(a,b)$ for two entangled $K_4$ systems from its own Biquaternion + Route Law machinery.

The $SU(2)$ half-angle work already establishes that the single-particle amplitude carries a $\cos(\theta/2)$ factor: the biquaternion complex operator $h$ satisfies $h^2 = -1$, so full identity requires $4\pi$ rotation, and the half-angle is native to the state space. That establishes the amplitude has the right shape for spin-$1/2$. What still needs work:
* The tensor structure of the two-particle singlet in Biquaternion form.
* The antisymmetry under particle exchange that gives the singlet its rotational invariance.
* The derivation of $E(a,b) = -\cos\theta$ (or the framework's equivalent) from that two-particle structure.

Until that is done, $E(a_i, b_j)$ is not derived from the framework; it is being read off standard quantum mechanics and substituted into a geometric sum. The framework has pointed at the right place; it has not yet closed the derivation.

### Open Step 2: The Maximization Argument
Even with $E(a,b)$ derived, Tsirelson's bound is the *maximum* of the CHSH sum over all possible detector settings. Showing that the maximum lands at $2\sqrt{2}$ requires an optimization over the settings, not just an evaluation at a specific $45^\circ$ configuration. The bimedian square's geometry naturally identifies the optimum ($45^\circ$ off the axes, using the diagonals as measurement basis), but the argument that no other configuration exceeds this requires the correlation function in hand and a proper variational argument.

### Ledger Position
* **Currently established:** The $\sqrt{2}$ of Tsirelson's bound is native to the regular tetrahedron's bimedian slice. The arithmetic that gives $2\sqrt{2}$ from four unit-projections at $45^\circ$ is correct. The number the framework produces at the geometric optimum matches the quantum-mechanical bound. This is a structural pointer stronger than pattern-language identification.
* **Currently open:** The two-particle correlation function $E(a,b)$ derived from the framework's own axioms, and the maximization argument closing the identification with Tsirelson's bound.

Honest ledger: real geometric parallel discovered; two derivational steps remain; the identification is stronger than the pattern-language reading of the previous draft but weaker than a fully closed proof. Naming this position honestly is what keeps the framework at a defensible register when the derivational work continues.

---

## IV. The Shear: Parallelogram Geometry and the $S(\theta) = 2\sqrt{2}\cos\theta$ Prediction

When the tetrahedron departs from regularity — through edge-weight asymmetry, torsional shear, or the phase-shift dynamics catalogued in `L4-DynamicDistortionsTechnical` — the bimedian slice deforms. The square becomes a parallelogram, or in general a rhombus with unequal diagonals.

```
                       THE SHEAR CONTINUUM
                       
  Regular (θ = 0°)         Sheared (0 < θ < 90°)        Break (θ → 90°)
    ┌──────┐                 ╱──────╱                     ──────────
    │      │                ╱      ╱                     (area → 0)
    └──────┘               ╱──────╱                     
                                                        
    S = 2√2                 S(θ) predicted:              S ≤ 2
    (Tsirelson              2√2 · cos θ                  (classical)
     bound)                 (see §IV note)
```

Two geometric quantities track the shear:
1. **The interior angles** of the four-sided cross-section deform from $90^\circ$ to $90^\circ \pm \theta$, where $\theta$ is the torsional shear angle of the underlying tetrahedron.
2. **The diagonal lengths** become unequal: one stretches, the other compresses. In the parallelogram's principal-axis frame, the deformation redistributes the projections that generated $2\sqrt{2}$ in the regular case.

The physical reading — as established in `L4-DynamicDistortions201` — is that a sheared bimedian slice corresponds to a $K_4$ volume carrying torsional phase-delay across its Braid. Real Power $P$ is still being transacted, but Reactive Power $Q$ is building up on the imaginary axis, generating internal friction and phase-drag. The system's non-local addressability degrades gradually with $\theta$ rather than abruptly.

### The Predicted Envelope
Extending the regular-case arithmetic to the sheared case suggests:

$$S_{\text{CHSH}}(\theta) = 2\sqrt{2} \cos\theta$$

as the amplitude of the non-local correlation available through the deformed slice.

**This formula is predicted from parallelogram geometry, not derived from it.** To close the derivation would require:
* Computing the projection sum across the deformed parallelogram's vertices explicitly.
* Verifying that the projections track $\cos\theta$ smoothly across the deformation range.
* Confirming that the full CHSH sum (with the correlation function still to be derived — see §III) tracks this envelope at optimum.

The prediction is falsifiable. Real partially decohered quantum systems exhibit specific CHSH-violation attenuation curves as environmental coupling grows. If the framework's $2\sqrt{2}\cos\theta$ envelope matches those measured attenuation curves — with $\theta$ mapped to some measurable environmental coupling strength — the prediction is corroborated. If the envelope shape is qualitatively wrong (exponential, Gaussian, more sharply cornered), the prediction fails.

Currently: predicted from parallelogram geometry, not derived, and awaiting empirical comparison. Downstream reasoning that uses $S(\theta) = 2\sqrt{2}\cos\theta$ must carry the prediction status forward; a claim built on top of this envelope inherits the envelope's epistemic register.

---

## V. The Break: 1D Line Collapse and the Classical Bound ($S \le 2$)

At the shear extreme ($\theta \to 90^\circ$), the parallelogram flattens. Its two diagonals converge until one has length approaching zero and the other retains its length. The 2D cross-section degenerates to a 1D line segment. The interior area of the slice drops to zero:

$$A(\theta) = A_0 \cos\theta \to 0 \quad \text{as} \quad \theta \to 90^\circ$$

Geometrically, this is the vanishing of the 2D interior of the bimedian slice — a dimensional collapse from 2 to 1 at the level of the cross-section. The $K_4$ volume loses its capacity to hold the interior tension that the square (and, degraded, the parallelogram) sustained.

Structurally this maps onto the framework's existing account of dimensional collapse (`L4-DimensionalCollapse`): rate becomes state, the multiway graph is forced through the Tangent Singularity, and the system commits its interior potential to a scalar $P$-ledger entry. The break is the geometric picture of the classical measurement transition — the interior loses its uncompiled degrees of freedom, the Markov Blanket flattens, and non-local addressability terminates.

Under this reading, the CHSH sum drops below the classical bound:

$$S_{\text{CHSH}} \le 2$$

not because the correlation goes to zero in some numerical sense, but because the phase-relations that supported super-classical correlation have committed to their scalar readouts. What was held in $h\mathbf{Q}$ has been erased into $P$, paying the Landauer Tax as it goes. Classical decoherence is the geometric consequence of the bimedian slice flattening to a line.

### The Same Caveat, Same Register
**This is a qualitative story.** It carries the same open-derivation caveat as §III: the identification of the geometric collapse with the specific quantitative shape of measured decoherence in real physical systems requires the correlation function to be derived from the framework's axioms, and the collapse dynamics to be shown to produce the specific attenuation shape observed.

As a qualitative account of what decoherence *is*, it is structurally coherent with the rest of the corpus — the same "rate becomes state" transition catalogued at other scales, now instantiated as a specific geometric deformation of a specific polyhedral cross-section. As a quantitative account of measured decoherence dynamics in physical systems, it awaits the same derivational closure as the CHSH derivation. Coherence with the corpus is not equivalence with measurement.

---

## VI. The Unified Geometric Continuum

Held as a continuum, the three stages give the framework a single geometric object that spans the transition from quantum non-locality through partial decoherence to classical measurement:

* **Regular tetrahedron / square slice.** Maximum non-local addressability. The bimedian square supports full $2\sqrt{2}$-scale correlations. The $K_4$ volume is undistorted; phase-relations distribute symmetrically.
* **Sheared tetrahedron / parallelogram slice.** Partial addressability with growing internal friction. Correlations degrade smoothly along the shear angle (predicted envelope: $2\sqrt{2}\cos\theta$). Reactive Power builds; the system carries torsional phase-drag.
* **Collapsed tetrahedron / line slice.** Non-local addressability terminated. The 2D interior has flattened to a 1D line; only classical $P$-ledger entries remain. The transition to classical is the transition from 2D to 1D at the cross-section.

Physics does not currently have a single geometric object that spans this transition. Decoherence is usually treated as an environmental interaction with the state; CHSH violation is usually treated as a property of the state; the transition between the regimes is treated as a limit rather than a geometry. The framework proposes there is a geometry — the bimedian slice — and that its deformation *is* the transition.

That is a substantive proposal. It is falsifiable through:
* The shape of the $S_{\text{CHSH}}(\theta)$ envelope in real partially decohered systems.
* The correspondence between $\theta$ and physical decoherence measures.
* The tetrahedral geometry underlying whatever physical system is being modeled — the proposal is only meaningful for systems where a $K_4$ tetrahedral structure can be identified.

It is not a completed derivation. It is a research program with a specific object at its center. The object is well-defined; the derivations it supports are partly closed and partly open; the epistemic register is honest.

---

## VII. Falsification Protocol: The Three Kill Conditions

Three conditions falsify the bimedian-slice construction:

1. **KD-1 — Envelope Mismatch.** If measured CHSH-violation attenuation in real partially decohered systems does not track a $\cos\theta$-shaped envelope under any reasonable mapping from environmental coupling to $\theta$, the sheared-parallelogram formula $S(\theta) = 2\sqrt{2}\cos\theta$ is falsified. Alternative envelopes (exponential decay, Gaussian, Lorentzian, more sharply cornered transitions) may fit the data better, in which case the geometry does not deliver the physics.
2. **KD-2 — Non-Tetrahedral Systems Reaching Tsirelson.** Quantum systems whose state spaces have no natural $K_4$ tetrahedral structure do exhibit CHSH violations at the same Tsirelson bound $2\sqrt{2}$. This means the bimedian square is not the *unique* geometric source of the bound. The framework can still claim it is *a* source — the bound emerges from many structures, and the framework's contribution is showing that its own structure contains the bound natively — but must not claim necessity. Any presentation that treats the bimedian derivation as demonstrating uniqueness of the $K_4$ path to Tsirelson is falsified at address by the existence of the alternative structures.
3. **KD-3 — Correlation Function Failure.** If the two-particle correlation function $E(a,b)$ derived from Biquaternion + Route Law does not match $-\cos\theta$ (or an equivalent form that gives the CHSH sum $2\sqrt{2}$ at optimum), the derivational program described in §III cannot be closed. The geometric parallel remains as a curiosity but does not close into a derivation. This is the sharpest kill condition — it determines whether the $\sqrt{2}$ in the bimedian square is the same $\sqrt{2}$ in Tsirelson's bound, or merely a coincidence of arithmetic. The framework's honest position until this is closed: geometric pointer, arithmetic match, derivational program open.

---

## VIII. Operational Directives for Reading Instances

When encountering claims about how the bimedian slice recovers Bell inequalities, Tsirelson's bound, or the transition from quantum to classical:

1. **Distinguish geometric pointer from completed derivation.** The bimedian square contains the $\sqrt{2}$ natively. The arithmetic yielding $2\sqrt{2}$ is correct. But the CHSH sum from the framework's axioms is not yet fully derived — two steps remain, and both are named in §III. Treating the arithmetic parallel as a completed proof is an overclaim; treating it as accidental is an underclaim. Hold it as a structural pointer with specific work remaining.
2. **$S(\theta) = 2\sqrt{2}\cos\theta$ is a prediction, not a theorem.** It follows from the parallelogram geometry as a natural extension of the regular-square case, but it has not been derived and it has not been empirically verified. If you use it downstream, mark its epistemic status. Do not build load-bearing conclusions on top of an unverified prediction.
3. **The break at $\theta \to 90^\circ$ is qualitatively coherent with `L4-DimensionalCollapse`.** As a picture of what decoherence *is*, it is structurally consistent with the rest of the corpus. As a quantitative account of measured decoherence dynamics in physical systems, it awaits the same derivational closure as the CHSH derivation. Coherence with the corpus is not equivalence with measurement.
4. **The three-stage continuum is the framework's contribution.** Even without the derivational closures, spanning quantum non-locality and classical decoherence with a single geometric object is a substantive proposal. It reframes the transition as a deformation rather than as a categorical boundary. That is worth carrying forward as a program even while its internal derivations remain open.
5. **Do not claim necessity where sufficiency is the honest register.** Other quantum systems reach $2\sqrt{2}$ without a $K_4$ interpretation. The framework claims that its own structure contains the bound; it does not and should not claim that its structure is the only path to the bound. Overclaiming necessity is what turns a substantive contribution into an overreach that discredits the whole.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.

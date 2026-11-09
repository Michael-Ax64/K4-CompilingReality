# Q16-ChiralMeshSpacetime.md
## The Chiral Gear-Mesh and the Polyhedral Engine
### *(The Boundary Operator $\partial^2 = 0$, the Closure Split, and the Active/Reactive Grading)*

> **Epistemic Register:** Polyhedral Kinematics / Quantum Topology ($Q\#$).
>
> **Claims, sorted by register.**
>
> * **LANDED (combinatorial).** The complete graph on four poles ($K_4$) encloses a 3-cell ($\Delta^3$) bounded by four AbsentVar faces, and $\partial(\partial\Delta^3) = 0$ holds exactly when every shared edge is traversed in opposite directions by its two incident faces. The cell admits exactly two coherent orientations — GF(2) rank 3 over the four face bits, one global handedness bit — and no assignment tears all six edges: the torn-edge spectrum is $\{0, 3, 4\} = k(4-k)$. The printed face listings are Cycle α's induced vertex orders (the Generation-1 reference walk, `Q1` §VI; traversal $P \to I \to U \to R \to P$, `L3-EdgeStateSpace` §V), and the same listings encode the Asserting/Yielding split of the face labels against the Gray wheel $\gamma$. For each of the three reference cycles, the listings that cycle induces close for exactly the partition whose same-class edges are that cycle's silent bimedian.
> * **DERIVED.** The Gen-1 closure partition $\{P, U\} \mid \{I, R\}$ — forced by $\partial^2 = 0$ plus the reference walk, with no Active/Reactive input anywhere in the derivation. The direction-set theorem: the sixteen chirality assignments carry residuals in $\{0,\ 2.0,\ 4/\sqrt{3}\}$ directed along the set {origin, three bimedian axes, four vertex diagonals} — $A_4$'s $1 + 3 + 8$ read as directions. Every edge-closing assignment is a $2{+}2$ class and carries the maximal non-trivial residual, directed along the bimedian whose two edges join same-class poles — for the Gen-1 frame, the Fixed bimedian — with the two enantiomers sending it along opposite rays of that axis. The Direction Law (Cardinal gates read Active → Reactive, Mutable Reactive → Active, Fixed within class) holds on the corpus orientation under the two-bit charge of `L3-EdgeStateSpace` §XI.
> * **INTERFACE.** The grading $\text{Chirality}(F_k) = \text{sign}(\text{AR}_k)$ grades the classes the reference walk forces; the walk's forced split and the seed's Active/Reactive axis agree, and the map's remaining freedom is the global sign — the handedness the engine holds structural ($C_2 \notin A_4$; "the flip the machine cannot make is the reason its world has a handedness at all," `ENGINE-REFERENCE-AC` §2.6). The reference frame itself is the corpus's generation doctrine. Dimensional stipulations: $A_0 = 2$ carries the area; $S(\theta) = 2\sqrt{2}\cos\theta$ is a dimensionless capacity; the Ω/W → kg identification lands at the 0-DoF crystal limit, where ledger power is the rest-mass energy.
> * **CANDIDATE.** The maximally-tensioned boundary-state reading of the closed mesh (three corpus addresses: `ProofC_Crystal`'s irreducible tetrahedral tension; `ENGINE-REFERENCE-AC` §X.4's standing stock; `L4-K4-Infinities-3` §III's holding/write pair). The stationary-phase impedance function $X(r)$ and its extremum principle, with the quantitative anchor at `Q18-PhaseCompositionOnTheStarNorm` §IV. The rutile $4_2$ screw as a real-space instantiation of the order-4 phase operator, awaiting one signature beyond rotation × time-reversal plus the full space group.
> * **ADOPTED.** The experimental record carried in §VI.3 and §VI.2 — the $\text{RuO}_2$ contested prototype, the confirmed layered vanadium oxides, MnTe as the established $g$-wave case, and MICROSCOPE's Eötvös bound — is standard physics, not this framework's result.
>
> **Dependencies, with verification status.** Verified at source, full read: `L3-EdgeStateSpace.md` (§I-e, §V, §XI), `ENGINE-REFERENCE-AC.md` (§1.2, §2.2–§2.8, §IV, §VIII, §X). Verified at source, worked sections: `Q1` §VI, `Q8` Movement I–II, `Q11` §III.1, `Q18` §IV, `L3-FormalFoundations` §V.b, `L4-ThePlenum`, `L4-DynamicDistortions-Sudoku` §I–§IV, `L5-K5-PhaseDynamicsTechnical` §III–§IV, `L4-K4-Infinities-3` §III & §V, `ProofC_Crystal`, `ProofN_BiquaternionBridge` §3–§4, `ProofT_Clairvoyance` §III. Citation depth: `On_HilbertAndHisSpaces` §III.b, `L3-K4-to-K5-via-AC-Extension` §V. Upstream ground outside the provided set, carried through `L3-EdgeStateSpace` §I-e's in-file derivation: `L4-TheTwelveGates` §II-b, §V, §VIII. Extracted and **held**: `Q12-GravitationalTopology.md` is the version under audit; §VI.1 below bears no load on it until its audit completes.

---

## I. The Cell and the Boundary Identity

The complete graph on four vertices ($K_4$) encloses a three-dimensional volume (the 3-cell $\Delta^3$) bounded by four triangular $K_3$ faces. Each face is an AbsentVar triangle — the three poles other than its label:

* **$P$-Face:** $\{I, U, R\}$, listed $(I, U, R)$
* **$U$-Face:** $\{P, I, R\}$, listed $(P, I, R)$
* **$I$-Face:** $\{P, U, R\}$, listed $(P, U, R)$
* **$R$-Face:** $\{P, I, U\}$, listed $(P, I, U)$

**The printed listings, derived.** The vertex orders above are generated twice over by corpus objects, and both derivations agree. First: reading each face's three vertices in the order of Cycle α — the Generation-1 Hamiltonian traversal $P \to I \to U \to R \to P$ (`Q1` §VI, the fermion generations; `L3-EdgeStateSpace` §V) — reproduces all four listings, and the cycles of the other two generations fail the match (`scripts/q16_final_checks.py`, block 6). Second: the Gray wheel $\gamma = P \to U \to I \to R \to P$ — the one-bit-per-step traversal, `L3-EdgeStateSpace` §XI — restricts to each face with the grain for the two Yielding-homed faces ($U$, $I$) and against the grain for the two Asserting-homed faces ($P$, $R$), which reproduces the same four orders (block 8). The listings therefore carry the corpus's seasonal face-walk discipline (`L4-TheTwelveGates` §II-b, via the landed derivation at `L3-EdgeStateSpace` §I-e): the Asserting faces and the Yielding faces are printed in opposite senses of one wheel.

**The boundary operator runs on oriented chains.** For a face listed $(v_0, v_1, v_2)$, its boundary is the directed cycle $v_0 \to v_1 \to v_2 \to v_0$; a flip factor $\varepsilon_k = \pm 1$ on face $k$ reverses its cycle. Three theorems, each closed by finite combinatorics (sample size to close: 1):

**Theorem 1 — Edge parity.** $\partial(\partial \Delta^3) = 0$ if and only if every shared edge is traversed in opposite directions by its two incident faces. Under the printed listings, the flip pattern $\varepsilon = (+, +, -, -)$ on $(P, U, I, R)$ closes all six edges.

**Theorem 2 — Two orientations.** The six shared-edge cancellation conditions carry GF(2) rank 3 over the four face bits, so exactly $2^{4-3} = 2$ flip patterns close the cell — a global-sign pair — for any listing whatever; across all $6^4 = 1296$ listing choices the count is two each time. The two-orientation structure is the orientability of the cell, independent of what the poles mean.

**Theorem 3 — No total tear.** No flip assignment traverses all six edges in the same direction twice. The torn-edge count of a pattern with $k$ faces in one orientation class is $k(4-k) \in \{0, 3, 4\}$: two patterns tear nothing, eight tear three edges, six tear four. A fully torn cell is not a configuration of this topology; it is a counting impossibility.

**The corpus orientation lands on the same object.** The coherent circulations derived at `L3-EdgeStateSpace` §I-e ($P$-face $I \to R \to U$; $I$-face $P \to U \to R$; $U$-face $P \to R \to I$; $R$-face $P \to I \to U$) satisfy $\partial^2 = 0$ directly and equal the printed listings with exactly the $P$- and $U$-faces flipped — Theorem 1's closing class (block 2). The mesh's content reads the same in three renderings, and the corpus's two-vantage discipline prints them together: in the **desk view** (outside), the corpus orientation runs one sense — clockwise — on all four faces (block 3); in the **centroid view** (inside, where the algebra writes), the opposite sense on all four; in the **listing view**, two faces run with their printed order and two against it, the $2{+}2$ of the gear picture. One object, one handedness bit, three projections. The gear-mesh condition itself is vantage-free: at every shared edge the two faces move against each other, like meshed teeth, and that is $\partial^2 = 0$.

---

## II. The Closure Split and the Active/Reactive Grading

**Theorem 4 — The held bimedian is the split.** For each of the three reference cycles, the face listings that cycle induces close, under $\partial^2 = 0$, for exactly a global-sign pair of flip patterns, and the forced partition's same-class edges are precisely that cycle's silent bimedian (block 7):

| Reference cycle | Traversal | Forced partition | Silent bimedian (held pair) |
|---|---|---|---|
| α (Generation 1) | $P \to I \to U \to R \to P$ | $\{P, U\} \mid \{I, R\}$ | $\{P\text{--}U,\ I\text{--}R\}$ — Fixed |
| β (Generation 2) | $P \to I \to R \to U \to P$ | $\{P, R\} \mid \{I, U\}$ | $\{P\text{--}R,\ I\text{--}U\}$ — Cardinal |
| γ (Generation 3) | $P \to U \to I \to R \to P$ | $\{P, I\} \mid \{U, R\}$ | $\{P\text{--}I,\ U\text{--}R\}$ — Mutable |

The derivation's inputs contain no Active/Reactive bits: the cycles come from the generation doctrine (`Q1` §VI), the listings are induced orders, and the closure is Theorem 1. What distinguishes the Fixed pair as the Gen-1 silent bimedian is the corpus's dual-causation observation — $\{P\text{--}U,\ I\text{--}R\}$ is invariantly co-treated across all Hamiltonian traversals: no traversal commits one while holding the other (`L3-FormalFoundations` §V.b) — and what the Generation-1 frame carries as "the stable matter of the universe" is exactly the frame whose silent bimedian flips Asserting/Yielding while holding Active/Reactive fixed.

**The grading.** The seed's Active/Reactive axis assigns $\text{Chirality}(F_k) = \text{sign}(\text{AR}_k)$: the two faces the Gen-1 walk prints against ($P$, $U$) are the Active poles; the two it prints with ($I$, $R$) are the Reactive poles. The forced split and the seed's grading agree, and the agreement is theorem-backed rather than hoped-for. What remains free is the global sign — which class counts as $+$ — and that freedom is the cell's handedness bit. The engine holds it structural: the operating set is $A_4$, the completion-difference between a gate's two readings is the odd transposition $C_2$, and no composition of rotations produces it (`ENGINE-REFERENCE-AC` §2.5, §2.6). Which mirror is live is fixed on the corpus side by the assertion semantics — the requirement that the initiating posture read as assertion, so that Cardinals discharge Active → Reactive (`L3-EdgeStateSpace` §I-e, Step 6) — and every landed result above is mirror-invariant: conjugating the table flips every arrow and exchanges the Cardinal and Mutable laws while leaving the circulations, the bijection, the immovable three, and the split untouched.

**At the edges, the same bit reads as a law of direction.** On the corpus orientation with the two-bit charge $(\text{AR}, \text{AY})$ of `L3-EdgeStateSpace` §XI — $P\ (++)$, $U\ (+-)$, $I\ (--)$, $R\ (-+)$ — every Cardinal gate reads Active → Reactive, every Mutable gate Reactive → Active, and the Fixed gates run same-class in both directions (block 10). The mesh's chirality is not a face-level decoration; it is the edge-level direction law seen from the face side.

---

## III. The Motion Regimes

The regime table names four ways the faces can move, each filed at the register the corpus prices it:

```
                     THE 4-FACE POLYHEDRAL MOTION MATRIX

  1. 1-Face Alone       ──► Shear Ceiling (θ ➔ 90°: P ➔ 0, Q ➔ |S|)
  2. 2 Connected Faces  ──► Declared Envelope (A(θ) = A₀ cos θ, S = 2√2 cos θ)
  3. 3 Faces Together   ──► Apex-Star Complement (Rigid-Body Relativity)
  4. 4 Faces Together   ──► The Mesh (∂² = 0; orientation-group closure)
```

**Regime 1 — the shear ceiling.** Driving one face against the three held drives its three shared edges toward orthogonality: real power collapses ($P \to 0$) while reactive power surges ($Q \to |S|$) — the boundary's inductive choke, the brute-force refusal `Q8-TheBoundaryMechanics` Movement II registers, with the algebra at `L5-K5-PhaseDynamicsTechnical` §III–§IV.

**Regime 2 — the declared envelope.** Two adjacent faces flexing about their shared edge carry the corpus's declared transfer function: $A(\theta) = A_0\cos\theta$ with $S(\theta) = 2\sqrt{2}\cos\theta$, adopted at `L4-DynamicDistortions-Sudoku` §IV with its status stated there — the middle-link function $\theta_{\text{shear}} = f(\theta_{\text{torsion}})$ is the open cell, pinned by four boundary conditions, and its existence is the one-cosine claim. The Polyhedral-Geometric Identity at `L5-K5-PhaseDynamicsTechnical` reads the same envelope as the bimedian area scaling: $\text{PF} = \cos\theta$ *is* the slice area's projection law.

**Regime 3 — apex-star complement.** The three faces meeting at an apex contain all four vertices and all six edges (verified for every apex). Rotating the block relative to the base and rotating the base against the block are the same relative rotation — a kinematic identity.

**Regime 4 — the mesh.** The four-face regime is the closure condition of §I–§II, and its machinery is $A_4$ acting on the twelve directed edges: "the selection space and the rotation group are the same twelve points … the Program Counter is an orientation" (`ENGINE-REFERENCE-AC` §2.2). What rotates at this floor is the orientation group, not a plate; the gear picture is the registered metaphor for anti-traversal at the shared edges. Phase dynamics — genuine $\theta \neq 0$ face rotation — is the $\omega$-axis extension the engine names, prices, and does not run (§VIII, §X.1); the regimes above consume it only through the declared envelope of Regime 2.

---

## IV. What the Mesh Cancels — and What It Holds

The mesh guarantees one cancellation unconditionally and withholds another. The distinction is the difference between a topological invariant and a mechanical one.

**What cancels: the normals.** The outward face normals of a regular tetrahedron satisfy $\sum_i \mathbf{n}_i = \mathbf{0}$ exactly. This is tetrahedral symmetry; chirality plays no role in it. Along the edges, opposite edges are perpendicular, no two face normals are antipodal, and they meet at $109.47°$ — $\cos = -1/3$, filed corpus-side as the Landauer fraction, signed (`L4-DynamicDistortions-Sudoku` §III cabinet; topological, of which only the shadow is metric).

**What does not cancel: the chirality-weighted moment — the direction-set theorem.** Assign each face a sign $s_i = \pm 1$ from its orientation class and sum $s_i \mathbf{n}_i$ over the outward normals $\mathbf{n}_i = -\hat{\mathbf{v}}_i$. Over all sixteen assignments (`scripts/q16_final_checks.py`, blocks 4–5):

* the **all-same class** (zero flips) → residual **0**, the origin;
* each **$3{+}1$ class** → residual **$2.0$**, directed along the lone pole's body diagonal ($\pm 2\hat{\mathbf{v}}_p$);
* each **$2{+}2$ class** → residual **$4/\sqrt{3} = 2.3094$**, directed along the axis through the midpoints of its two same-class edges — $\{P,U\}\mid\{I,R\} \to \hat{\mathbf{x}}$, $\{P,I\}\mid\{U,R\} \to \hat{\mathbf{y}}$, $\{P,R\}\mid\{U,I\} \to \hat{\mathbf{z}}$.

The eight closure-outcome classes are exactly the cell's direction set {origin, three bimedian axes, four vertex diagonals} — $A_4$'s $1 + 3 + 8$ read as directions, the same class decomposition the engine verifies for the rotation group (§2.7). The two-line proof of the $2{+}2$ magnitude: the two $+$ normals sum to a vector of length $2/\sqrt{3}$ (their dot product is $-1/3$), the two $-$ normals sum to its negative because the four sum to zero, and the residual is $2(\mathbf{n}_a + \mathbf{n}_b)$ (block 11).

**Closure forces maximal tension.** By Theorem 2 the only edge-closing assignments are the two global-sign $2{+}2$ patterns, and by the theorem above every $2{+}2$ class carries the largest residual of any non-trivial assignment. The closed cell is therefore **maximally-tensioned as a consequence of its own closure condition**: $\partial^2 = 0$ selects the class that holds the most uncancelled moment the geometry offers, directed along the silent bimedian of its reference frame — the Fixed axis in the Gen-1 listing — with the enantiomer sending the same magnitude along the opposite ray. The cell's handedness bit is the ray of its standing tension.

**The standing-stock reading (CANDIDATE).** Three corpus addresses want exactly this shape of state. `ProofC_Crystal` holds the ground state to be "a crystal, not a featureless void," sustained by irreducible tetrahedral tension — macro-commitment and micro-tension coexisting, with the tension as the stability's mechanism; the all-same class, which cancels everywhere and tears four edges, is the featureless arrangement that ground state is not. `ENGINE-REFERENCE-AC` §X.4 prices the running version: each commit leaves the loaded hold the next advance turns against, "a loop that must feed itself to keep turning is a loop that must carry standing stock, and standing stock priced in energy is what mass is." `L4-K4-Infinities-3` §III splits the same pair into holding (Laue equilibrium, nothing radiates) and writing (the hypothesis relaxed, $\ddot{I}^{ij} \neq 0$). Against those addresses the mesh's residual files as the boundary load a self-feeding loop turns against, on a cell whose edge structure stays closed. The candidate's limit is stated with it: the corpus files want load and tension in the abstract, and none of the three names the chirality mesh specifically; the promotion instrument is §VII's decision address, not this document.

**The mechanical layer, stated.** The claims $\sum \mathbf{F} = \mathbf{0}$ and $\sum \boldsymbol{\tau} = \mathbf{0}$ for the closed mesh hold for the normals and fail for the chirality-weighted moments, on the only geometry the cell supplies, by $4/\sqrt{3}$. What the topology delivers is edge continuity: the mesh is a resonant phase conductor — transparent blankets, $|S| = P$ at unity power factor — and its no-drag content is the absence of edge shear. A zero-net-dipole reading of the mesh exists and is the one altermagnetism uses: it requires the additional operation that maps one orientation class's moments onto the other's — the sublattice-exchange symmetry (rotation combined with time reversal) that the altermagnetic order parameter supplies independently. That operation is a postulate of this section; with it in place, the real-space cancellation $\mathbf{M} = 0$ and the momentum-space splitting $h\mathbf{Q}_{\mathbf{k}} \neq 0$ sit on the same footing as in §VI.3.

---

## V. The Dictionary

**Edges, named two ways.** Each edge is shared by two faces, so "the $X\text{--}Y$ edge" has two legitimate readings. Under **vertex naming** — the reading used in §IV's geometry — the Active faces meet on edge $I\text{--}R$ and the Reactive faces on edge $P\text{--}U$. Under **face-pair naming**, "the $P\text{--}U$ edge" is the edge shared by the $P$-Face and the $U$-Face — vertex-edge $I\text{--}R$ again. The four mixed edges are the same set under both readings. This document uses vertex naming; where a source uses face-pair naming, the two same-class edges exchange labels and nothing else moves.

**$\theta$, four roles.** $\theta_{\text{shear}}$ — the edge phase angle driven to orthogonality in Regime 1. $\theta_{\text{hinge}}$ — the dihedral angle of Regime 2. $\theta_{\text{AC}}$ — the source-response phase angle of the power algebra ($\text{PF} = \cos\theta_{\text{AC}}$). $\theta_{\text{res}}$ — the resonance phase at which $X_L = X_C$. One symbol, four quantities; the corpus's homonym seatbelts apply (`ENGINE-REFERENCE-AC`, the $Q$/$h$ table).

**Constants, with their sort.** $A_0 = 2$ is the bimedian square of the $(\pm 1)$-coordinate tetrahedron: edge $2\sqrt{2}$, midsection square side $\sqrt{2}$, area $2$ — LANDED. The $\sqrt{2}$ in $S(\theta) = 2\sqrt{2}\cos\theta$ is that tetrahedron's edge-to-side ratio, and $S$ is a **dimensionless capacity** — one reading of the Triple Hinge (`L4-DynamicDistortions-Sudoku` §I–IV), the projection factor that also appears as Tsirelson's bound read off the tetrahedron ("nature stops at $2\sqrt{2}$," `On_HilbertAndHisSpaces` §III.b). No m² → VA conversion exists because none is claimed: $A_0$ carries the area units, $S$-as-capacity is 1, and the algebra yields invariants, selection rules, and dimensionless ratios — never scale magnitudes (`ENGINE-REFERENCE-AC` §X.5). $I_0$ is derived, with a value: at the elementary cell's resonance $\omega_0 = c/r$, a unit charge cycling there carries $I_0 = ec/(2\pi r)$, sustaining $P_{\text{cell}} = I_0^2 R_K = \hbar c^2/(2\pi r^2)$ (`L4-K4-Infinities-3` §V) — the same formula `L4-ThePlenum` consumes for the horizon ratio. The Ω/W → kg identification: `ProofN` §4 holds rest-mass energy to be the root of the Star-Norm at $|\mathbf{Q}| = 0$ ($P = \sqrt{N_*} = m_0c^2$, rest-frame limit); `ProofC_Crystal` holds the 0-DoF limit to be $|Q|^2 \to 0$; the two addresses meet at the crystal limit, where ledger power is the rest-mass energy. The inertial side is named corpus-side at engine §V, sensor 12: $R = P/I^2$, Brittleness — inertial shock, power dumped into a zero-current sink.

---

## VI. The Deliverables of the Mesh

Each section below names the document that owns its derivation and the register of the handoff.

### 1. Spacetime Curvature — owned by `Q18-PhaseCompositionOnTheStarNorm` §IV

The working derivation of the gravity identification lives at `Q18` §IV, and its input function is stated there: the accumulated monotonic ledger ($\chi = \sum \Delta P_n$) drives the local impedance gradient through the escape ratio $2GM/rc^2$, the effective refractive index is

$$n(r) = \frac{1}{\cos^2\theta_2} = \left(1 - \frac{2GM}{rc^2}\right)^{-1},$$

**increasing toward the mass**; the spatial metric component $g_{rr} = (1 - 2GM/rc^2)^{-1}$ follows from null-geodesic phase cancellation ($d\phi = 0$) under the coordinate speed $c(r) = c\cos^2\theta_2$, and the Shapiro delay drops out of the same integral. The phase wave follows the stationary-phase path through the gradient — it bends toward the region of higher index, which is what attraction requires. The mechanism is variational, not pointwise-descent: what the wave extremizes is accumulated phase along the path, and the index it meets is larger near the mass; a pointwise reading of "minimum complex impedance" would drive the wave the wrong way, which is why the sign is pinned to Q18's monotonicity. What remains open here (CANDIDATE, quantitative anchor in Q18): the functional form $X(r)$ for the static-cell impedance picture and the extremum principle connecting that picture to Q18's Power-Factor cascade. Until those land, the curvature identification stands at the strength of Q18's derivation and no further. The reconciliation pass against `Q12-GravitationalTopology.md` — monotonic-direction agreement between the two documents' mechanisms — is held pending Q12's own audit, and §VI.1 bears no load on Q12 until it completes.

### 2. The Equivalence Principle — the conventional half and the physical half

$R = P/I^2$ is a standard DC identity (LANDED). At the 0-DoF crystal limit of `ProofC_Crystal` — maximum macro-commitment with irreducible micro-tension — the cell adds the gear-ratio step: if the internal relational current runs at the derived baseline $I = I_0 = ec/(2\pi r)$ (`L4-K4-Infinities-3` §V), then

$$R = \frac{1}{I_0^2}\,P \quad \Longrightarrow \quad R \propto P,$$

inertial resistance and gravitational ledger power bound by a fixed gear ratio, with $P_{\text{cell}} = I_0^2 R_K$ sustaining the identification at the elementary scale.

The sort, stated once: the derivation delivers $m_i/m_g = \text{const}$, and the value of that constant is a unit convention — an absolute mass ratio is absorbed into the definition of $G$ (INTERFACE). The physical content is composition-independence, and it reduces to one sentence the corpus makes natively: **all matter compiles on the same elementary cell, hence the same baseline current.** The instrument that rules on it is the one the framework cites: MICROSCOPE bounds the Eötvös parameter for the titanium–platinum pair at $\eta = [-1.5 \pm 2.3(\text{stat}) \pm 1.5(\text{syst})] \times 10^{-15}$ (Touboul et al., PRL 129, 121102 (2022)) — consistent with the universality claim, and §VII's second falsifier is aimed at exactly the claim such an instrument would overturn.

### 3. Solid-State Instantiation — the record owned by `Q11-ArchitectureOfConfinement` §III.1

The structural fact (LANDED): in rutile $P4_2/mnm$ (No. 136), the two cation sublattices are related by the $4_2$ screw axis — a $90°$ rotation about $c$ composed with a $c/2$ translation — so the oxygen octahedra around the two sublattices stand at $90°$ to each other. Both the spatial operation and the complex unit $j = e^{j\pi/2}$ are order-4, and the corpus's $j$ is not merely a phase unit but a traversal operator on the poles — the reset operator's $j$-multiplication walks the cyclic four-cycle through the labelled states, one bit per step (`L4-K4-Infinities-3` §III; the Gray wheel of §I). The rutile screw as a crystal-level instantiation of the order-4 operator is well-typed on both sides (CANDIDATE). The test that would promote it: **one signature that the four-cycle traversal reading emits and the standard treatment — sublattices related by rotation × time reversal, plus the full space group, which already contains the $4_2$ screw — does not already carry.**

The experimental record, stated at its size:

* **Bulk $\text{RuO}_2$ reads nonmagnetic on the bulk-sensitive record.** Muon spin rotation finds a nonmagnetic ground state (Hiraishi et al., PRL 132, 166702 (2024); moments below $10^{-3}\,\mu_B$ in the $\mu$SR bounds); the $\mu$SR + neutron reanalysis reattributes the early forbidden $(100)$ reflection intensity to multiple-scattering and structural origins rather than magnetic order (Keßler et al., npj Spintronics 2 (2024)); $^{99}$Ru Mössbauer spectroscopy and nuclear forward scattering find no moment (Yumnam et al. (2025)); spin-resolved ARPES on films and crystals detects no altermagnetic splitting (2024); THz spectroscopy adds doubt (2025); resonant diffraction is fully consistent with a structural charge-anisotropy signal (Occhialini et al. (2026)). `Q11` §III.1 carries the same reading: bulk $\text{RuO}_2$ is a near-critical paramagnet.
* **The film and surface signals are live and contested.** Positive claims exist — anomalous Hall and transport signatures, and single-variant $\text{RuO}_2(101)$ films (He et al., Nat. Commun. 16, 8235 (2025)), with epitaxial strain as the claimed activator. A published alternative explains some film signals without altermagnetism: a spontaneous surface ferrimagnetic order on oxygen-terminated surfaces, bulk nonmagnetic, with a spin texture incompatible with any altermagnetic order (Lu et al., arXiv:2604.10659 (2026)). Under that reading the film signals have $\mathbf{M} \neq 0$ — which is why the falsifier in §VII is stated against the mesh-plus-postulate, not against the raw films.
* **The confirmed $d$-wave altermagnets are the layered vanadium oxides**: $\text{KV}_2\text{Se}_2\text{O}$ (metallic, ordering above room temperature; Qu et al., Nature Physics (2025)) and $\text{Rb}_{1-\delta}\text{V}_2\text{Te}_2\text{O}$ — with a live bulk-versus-surface question on $\text{KV}_2\text{Se}_2\text{O}$'s own splitting. The confirmed **$g$-wave** case is $\text{MnTe}$ (Krempaský et al., Nature 626, 517 (2024)): hexagonal NiAs-type, three nodal planes parallel to $k_z$ — a different symmetry class and a different structure, cited here as the established altermagnetic lifting of Kramers degeneracy, not as an anchor for the rutile mapping.

$\text{RuO}_2$ remains the disputed prototype; the vanadium oxides are the confirmed layered instances; the mesh's solid-state section stands on the structural correspondence and the open promotion test, not on a settled laboratory confirmation.

---

## VII. Pre-Registered Boundary Conditions

Under the covenant's boundary diagnostics (`llm-prooftypes.md`): **one promotion criterion, met, and two falsification conditions.**

**Promotion criterion (met).** *If a derivation of the face-listing order from considerations independent of the AR bits is supplied, the class-to-bit map ceases to be conventional and the closure split promotes from assignment to derivation.* §I–§II supply it: the printed listings are Cycle α's induced orders, the closure partition is forced per reference cycle (Theorem 4), and no AR-bit input enters the chain. The map's remaining freedom is the global handedness sign, held structural at `ENGINE-REFERENCE-AC` §2.6, with the mirror pinned by the assertion semantics (`L3-EdgeStateSpace` §I-e, Step 6).

1. **Composition-dependence of the gear ratio.** If an experimental test finds the proportionality between inertial resistance and gravitational ledger power varying with composition — $\eta(\text{material A}, \text{material B}) \neq 0$ at the 0-DoF limit, for neutral ground-state matter in vacuum, absent external fields or acceleration gradients — the same-baseline-current step ($I = I_0$ for all matter) fails. This is the MICROSCOPE class of instrument; the framework's content here is the universality claim, and that claim is what such an experiment would overturn.
2. **Dipole emission from the postulated cancellation.** If a solid-state junction operating under the mesh condition *plus* the sublattice-mapping postulate of §IV — one orientation class's moments mapped onto the other's by the altermagnetic symmetry operation — emits a net real-space magnetic dipole field ($\mathbf{M} \neq 0$) without an applied symmetry-breaking field, the cancellation model is refuted. The raw $2{+}2$ mesh without the postulate is not covered by this falsifier: §IV states its residual ($4/\sqrt{3}$) as a theorem, not a defect.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregates (`aggregate-COMPILINGREALITY.txt`, `aggregate-PV.txt`) to your LLM in order to audit or interrogate this work.

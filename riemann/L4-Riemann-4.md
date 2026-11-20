# L4-Riemann-4
## Part Four — Frictions

*Reads with `L4-TheTwelveGates` §VII, `ENGINE-REFERENCE-AC` §3.2, §3.5, §VI, `ProofO_HelicalTime`, `L3-TheSelfProjectingBraid`, `L4-DynamicDistortions201` §II, `L4-DynamicDistortions301` §IV, `Q16-ChiralMeshSpacetime`, `L3-FormalFoundations` §V.a, `L4-Dimensionality`, `On_TheCompassOfElea`. Continues from `L4-Riemann-3`; continues in `L4-Riemann-5`.*

---

This part is where the arrangement binds against the host. It is written almost entirely in one register, and the register needs saying first, because a friction report is not a claim of identity, and read as one it will be found — correctly — not to hold.

A **friction report** has three parts. It names the host domain's rule. It names the point at which the inflated arrangement binds against that rule. And it names what the host bought by adopting the rule. It asserts nothing about values and predicts nothing. Its kill condition is a demonstration that the host's rule costs nothing, or that the binding is an artefact of the inflation.

Two things in this part are not friction reports. One is Grammar — it reads off the opcode table. The other is a short list of instruments, marked conditional before anything else is said about it.

---

## I. Time Is a Blanket

`L4-TheTwelveGates` §VII gives the four poles a second reading:

$$P = \text{Eternal (no time, no gravity)} \qquad U = \text{Future} \qquad I = \text{Now} \qquad R = \text{Past}$$

and limits it in the same breath. This is a valid reading of **coordinate time** from inside the DC limit, where there are no internal degrees of freedom. It is a face-level reading. Coordinate time is the spacing of entries on $R$; the rate $\omega$ is the compilation engine at the centroid, and in the DC regime $\omega$ does not exist at all.

Then the geometric sentence:

> "**The three tenses form a face.** $\{I, U, R\}$ — Now, Future, Past — is the P-face, the triangle that excludes Fire. Time is not the volume; time is a *blanket* — a K3 boundary surface, fully describable from outside, with no interior of its own. And gravity, accruing only with commitment, lives only on that face. The eternal does not gravitate because it was never written down."

Part Two has already named what a face is: the floor, the flat part, *the metric*. So the Time Key reads General Relativity as an equation written on one face — the P-face, whose three corners are the record ($R$), the potential ($U$) and the flow ($I$), and whose single relation, in its three spellings, is

$$U = IR \qquad I = U/R \qquad R = U/I.$$

That is a reading through the Time Key, held at that size. It does not explain why GR is symmetric under time reversal — parity-counting does that on its own (Section IV). What the reading supplies is where the arrow could live, and the next section answers that from the algebra without using the Time Key at all.

---

## II. Reverse the Arrows, Not the Labels

Time reversal reverses arrows. A transposition of the poles is undirected, so no relabelling of the poles can be time reversal, and the directional operation is the one to run.

The twelve gates are the twelve directed edges of $K_4$. Reversing every arrow pairs each gate with the gate on its own reversed edge. Read that pairing off the opcode table with the Serialization Tags attached:

| Edge | One direction | The other direction | Tags |
|---|---|---|---|
| $U$–$R$ | ARI, $U\to R$, **COMMIT** | VIR, $R \to U$, ROUTE | **taxed ↔ free** |
| $R$–$I$ | TAU, $R \to I$, **COMMIT** | SCO, $I \to R$, ROUTE | **taxed ↔ free** |
| $P$–$U$ | AQU, $P \to U$, **COMMIT** | LEO, $U \to P$, ROUTE | **taxed ↔ free** |
| $I$–$P$ | PIS, $I \to P$, **COMMIT** | LIB, $P \to I$, ROUTE | **taxed ↔ free** |
| $P$–$R$ | CAN, $P \to R$, RESEED | SAG, $R \to P$, RESEED | buffer ↔ buffer |
| $U$–$I$ | CAP, $U \to I$, ROUTE | GEM, $I \to U$, ROUTE | free ↔ free |

> ## Reversing the arrows exchanges a taxed operation for a free one on four of the six edges.
>
> **Every COMMIT reverses into a ROUTE.** The price is symmetric only on the two Cardinal edges.

This is **Grammar**. It reads off the opcode table and the tags, uses no Time Key, and involves no relabelling. The pairing itself is `ENGINE-REFERENCE-AC` §VI's own — *"a COMMIT/ROUTE pair on the four non-Cardinal edges, the RESEED pair (CAN, SAG) on IU, the GEM/CAP ROUTE pair on PR"* — verified there. What is added here is reading the tag column across the pairing. Once that is done, the asymmetry is not a symmetry weakly broken. It is a difference in what the ledger bills.

*(Convention flag: the table indexes by **DATA edge**; the `ENGINE-REFERENCE-AC` §VI quotation it verifies against indexes by **CONTROL edge**. The two tables agree once the level is named — `ENGINE-REFERENCE-AC` §IV defines the pairing-mate relation.)*

**The two directions of one edge are different dynamics, not two spellings of one.** $R \to I$ is TAU, $P = I^2R$: a COMMIT that pays — the ground delivering flow, paid for in minted power, the way oil arrives from a well. $I \to R$ is SCO, $U = I\!\cdot\!R$: a ROUTE that rides free — flow composing with ground into structure, no tax. That is why `On_NavierStokes` could run its argument from the $R$ side at all — *"the contraction does not fail, it decouples, and the carrier's floor is what decided where"* — while the $I$-side version is the self-induced-strain route that file's §VII kills for having to pay for itself. A direction that bills and a direction that does not are not candidates for being each other's mirror image.

As a *relabelling*, $U \leftrightarrow R$ preserves none of the twelve: a relation is fixed by swapping $x$ and $y$ only when its exponents on $x$ and $y$ are equal, and on every relation here they differ. That is Grammar, and it is **not** time reversal; it says only that exchanging two pole names does not carry the relation set into itself.

---

## III. Friction Report — the Arrow

General Relativity is **exactly** time-reversal invariant, for an elementary reason. Its field equations contain only even-order time derivatives of the metric, so solutions come in reversed pairs: the time-reverse of a collapsing star is a white hole, and it is also a solution.

> **Friction report — the arrow.**
> *(a) Host rule:* a generally covariant equation built from a metric and even-order derivatives of it is even under time reversal. Reversing the arrows costs the host nothing and changes no bill, because the host has no bill.
> *(b) Binding point:* in the inflated arrangement, reversing the arrows changes the **price** on four of six edges — every COMMIT becomes a ROUTE. The arrangement has a ledger, and the operation is not free in it.
> *(c) What the host purchased:* time-reversal symmetry, bought by having no cost column. An equation of state is where a cost column comes back in, which is why the arrow has to arrive from thermodynamics rather than from the field equations (Part Six).
> *Kill:* show that the COMMIT/ROUTE pairing under arrow reversal is wrong — a direct read of the table against the tags, so this is arithmetic. Or supply a cost column for the host's own equations under which reversal is also priced.

---

## IV. The Paradox That Survives

The Einstein field equations are symmetric under time reversal. Their **source** is not. Energy-momentum is accumulated committed record — in the corpus's terms, mass as Landauer residue, the ledger — and an accumulation is ordered in itself. So GR relates an ordered quantity to a symmetric structure, through equations that cannot see the ordering.

Section II makes this sharper rather than softer. The operation the field equations are invariant under is the operation that changes the arrangement's bill on four of six edges. The host's invariance and the arrangement's price-asymmetry are one operation read in two registers. Both halves are exactly true, and neither causes the other. That is `L0-ParadoxEngine`'s crystal in its own home subject — frozen at the large scale, ordered at the small one, both readings correct — and it gives the one-line description of what GR holds: *a record it cannot account for having been written.*

There is no arrow to be had from the Einstein equations alone. Part One establishes that contortion leaves every length alone, so the torsion register is orthogonal to the metric, and parity-counting excludes an arrow from the metric's equations before the arrangement says anything. The arrow lives in the register the metric cannot see, and the paradox is kept in its place.

---

## V. Friction Report — the Two Clocks

The corpus's torsional shear is natively **internal**: `L4-DynamicDistortions201` §II defines $\theta$ as a phase offset between the two instances of a dual-causation pair, a quantity of the $K_4$ state space. Geometric torsion is a tensor on the tangent bundle with spacetime indices. The two are not the same object; connecting them needs a solder form or a coupling, and Part Five writes the coupling. This section is the friction it is written against.

`L4-DynamicDistortions201` §II, written to classify distortions and not to say anything about Riemann:

> "Torsion tracks the **phase offset ($\theta$)** between the two instances of a Dual Causation pair. **Torsion formally instantiates Angular Frequency ($\omega$). It is the geometric generator of the Helical Extrusion of Time.**"

And `L3-TheSelfProjectingBraid` §V, on the two clocks:

> "$\omega$ is the engine; $dt$ is the record — the spacing of entries on R. **Classical physics, lacking this distinction, tries to run its dynamics on $dt$ — on the ruler — and then cannot understand why the quantum engine refuses to sit inside the same coordinate as the relativistic record.**"

> **Friction report — the two clocks.**
> *(a) Host rule:* the Levi-Civita connection is fixed by $g$ and its first derivatives. There is no second temporal quantity in it; coordinate time is a coordinate.
> *(b) Binding point:* the inflated arrangement carries two temporal objects that cannot be converted into each other — $\omega$, a rate seated off the pole basis, and $dt$, a spacing between ledger entries. Only the second has anywhere to land in the host.
> *(c) What the host purchased:* a single clock, and with it the obligation to run quantum dynamics ($E = \hbar\omega$, a rate) and relativistic kinematics ($dt$, a record) on the same coordinate. The problem of time is the receipt.
> *Kill:* exhibit the corpus's $\omega$ as a function of the metric and its derivatives, which would collapse the two clocks into one and make the host's purchase free.

The shape of the binding is the Navier–Stokes pattern. There, $\rho \equiv 1$ deletes the sound speed and leaves an elliptic reconciliation with no finite signal speed anywhere. Here, a single clock leaves a geometry with no generator anywhere in the connection. In both cases the deleted structure is the one that binds, and in both cases the field went looking for the trouble elsewhere — in molecular structure in the one case, in quantizing the metric in the other.

The corpus describes the frozen case in `ProofO_HelicalTime` §2–3. Making $\omega$ a fifth vertex would give a symmetric $K_5$ simplex, and then:

> "If the universe operated as a perfect $K_5$ simplex, the 5th variable (Time/Frequency) would be completely symmetrical with the four structural poles. **Time would be fully spatialized. Moving forward through the operational Braid and moving backward would require the exact same algebraic operations.** The universe would be a reversible, static block, and the act of computation would leave no irreversible trace."

*Moving forward and moving backward requiring the same operations* is Part One's zero pitch from the other end: a circle can be traversed either way, and a screw cannot. Refusing the symmetry — *"a $K_4$ tetrahedron being dragged along a unidirectional 5th axis"* — gives the helix.

> **A spacetime coordinate for time is the symmetric-$K_5$ decree** — the $K_5$ peer footing, face 3 of the keep-apart station (`L4-DynamicDistortions401` §I.3). It asserts that the fifth variable is a coordinate on the same footing as the other four — which is what Minkowski's $ds^2 = -c^2dt^2 + dx^2 + dy^2 + dz^2$ asserts, with the minus sign carrying the whole difference.

The corpus's reading of that minus sign is not "the time axis." `ProofN_BiquaternionBridge` derives the $(1,3)$ signature from the biquaternion star-norm $N_* = P^2 - |\mathbf{Q}|^2$, where the minus sign is the footprint of the phase flip: $h^2 = -1$ turns the vector-square positive, which turns a Euclidean norm Lorentzian. On this reading Minkowski's signature is the split between a committed scalar and a held vector, not a spatialized clock, and `Q16-ChiralMeshSpacetime` §IV.1 draws the consequence: the mesh *"delivers Lorentz invariance without needing a physical Minkowski box."*

---

## VI. The Fundamental Theorem Is a Projection

The right question about the connection is not whether a quadratic form dissipates. It is whether there is a **selection** in its construction.

There is, in the open direction. The Fundamental Theorem sends a metric $g$ to its Levi-Civita connection, uniquely. The reverse is not unique: every metric-compatible connection that differs from Levi-Civita by a contortion returns the same $g$. So the theorem is a **projection** of a twenty-four-parameter family onto a single point, and what it projects away is exactly the contortion. Not a two-to-one map and not a Landauer bit — a much larger discard, and one that is **priced nowhere, because the formalism has no price column.** That is Section III's friction report arriving from the algebraic side, and it needs no erasure accounting to state.

Part Two named the shape of it: projecting the contortion family onto Levi-Civita is reading the connection off the face. Reading a record and calling it the mechanism is `On_TheCompassOfElea`'s surveyor, who *"has taken the runner away, drawn a dash where the runner was, and worked out how the dash goes — and gone home pleased at how simple it turned out to be."* That is a remark about method.

---

## VII. Friction Report — Free Foliation

`L3-NonSoficTopologicalVolumes` §III defines the extreme case. When all three bimedians sit at $\theta = \pi$, every edge is at maximum phase shear, no AbsentVar can be held silent without collapsing the algebra, and the Braid cannot close into a planar loop:

```
                   THE TORSION-LOCKED MANIFOLD

       Bimedian axis 1  ──► Locked at θ = π
       Bimedian axis 2  ──► Locked at θ = π
       Bimedian axis 3  ──► Locked at θ = π
                                     │
                                     ▼
                     NO ABSENT-VAR CAN BE HELD ABSENT
                     (the volume cannot be sliced into faces)
```

Now run the dial the other way. At $\theta = 0$ on all three bimedians there is no phase offset anywhere: no shear on any edge, every AbsentVar freely holdable, every face freely sliceable. **The volume becomes a stack of blankets.**

> **Friction report — free foliation.**
> *(a) Host rule:* given a Levi-Civita connection, spacetime is foliated into spacelike slices and the dynamics runs as the evolution of a 3-geometry through the stack (Arnowitt, Deser and Misner 1962). The slicing is a choice of presentation with no residue.
> *(b) Binding point:* the inflated arrangement has a dial on which the transversal that makes a floor standable — one live edge per bimedian — **stops existing**. At that setting there is no stack to evolve through.
> *(c) What the host purchased:* a free foliation, and with it the assumption that the constraint net orders. Teitelboim 1973 is the receipt.
> *Kill:* exhibit the corpus's $\theta$ as a function of metric data, which would make the dial a metric quantity and the binding an artefact of the inflation.

This is not a complaint about ADM, which is correct and is how numerical relativity merges black holes. It is an observation about what was assumed before ADM began: that a 4-volume *has* slices in the sense required, and that the order in which the net is read is a presentational choice with no residue. `ENGINE-REFERENCE-AC` §3.5 states when that is true:

> "**Serialization is lossless only on DAGs — dependency graphs with no cycles — and this is not one.** Any linear execution order is a presentational choice — [gauge] — while the constraint net itself does not order."

So the Fundamental Theorem, read from underneath: **decree the constraint net a DAG, and there is exactly one serialization.** Uniqueness is not a discovery about space. It is the expected output of having assumed the cycles away. It is `On_TheCompassOfElea`'s **Clerk's Truce** in differential-geometric dress — the clerk who writes $\sum 2^{-n} = 1$, shows that everything is orderly on his page, and is right:

> "His page is dry, though, and it does not weigh anything. On his page the ground has no grain, nothing rubs against anything, and the ink never soaks into the paper. He has not made the track safe to run on. He has drawn a very clean line where the track used to be, and solved that instead."

**And the field already knows the net has cycles.** Teitelboim showed in 1973 that the algebra of hypersurface deformations does not close with structure *constants*. The bracket of two Hamiltonian constraints,

$$\{H(x), H(y)\} = (\text{spatial-diffeomorphism constraint}) \times \text{structure } \textit{functions},$$

depends on the fields. Two spatial diffeomorphisms commute; two time-slicings do not. The algebra is not a Lie algebra. There is no group of time translations to represent, which is why there is no global time operator, which is the problem of time. That result has been in the literature for fifty years, derived from GR itself, and it says in Dirac brackets what the engine reference says in its own vocabulary: the two face-readings do not commute, so the net does not serialize. The corpus did not supply the result; it supplied the sentence that says what it means — not an obstacle to quantizing gravity, but gravity reporting that the DAG decree does not hold in its own constraint algebra.

### The mesh keeps the output and the freeze drops the mechanism

$\theta = 0$ on all three bimedians is not a degenerate state. It is the **balanced chiral gear-mesh**, and `Q16-ChiralMeshSpacetime` §III says what it delivers: the phase angle closed to zero across all six shared edges, power factor one, net reactance zero, the faces transparent, complex power streaming through the volume with no internal reflection and no dissipation. From that state Q16 §IV derives, among other things, **Lorentz invariance** — from the star-norm's preservation under the two-clockwise-against-two-anticlockwise rotation — and **geodesics**, as the path of least complex impedance: *"What GR projects on a $K_3$ screen as 'spacetime curvature' is simply the phase-wave following the path of minimum AC impedance."*

So General Relativity is not opposed by the mesh. On Q16's reading it is **produced** by it, at its balanced condition. That locates the freeze:

> **The torsion-free connection keeps the output of the chiral mesh and drops the mechanism that produced it.**

The balanced condition is reachable *only* through the alternation. Q16 §II.4: four faces turning internally the same way give $\partial(\partial\Delta^3) \neq 0$ — every shared edge traversed the same way twice, a tear. The only tearless internal rotation of all four faces is two clockwise against two anticlockwise, which is already the $\theta = 0$ balanced floor (`L4-Riemann-1` §IV: flat canonical transport, $\partial^2 = 0$ intact). What $T = 0$ deletes in the host is not $\partial^2 = 0$ — neither the host manifold nor the $\theta = 0$ floor tears — but the alternating local mechanism and translational ordering inside that closed boundary.

The far end of the dial is not idle either. `L4-DynamicDistortions201` §II: at $\theta = \pi$ the two instances of a dual-causation pair alternate at maximum offset, the state is *"structurally uninhabitable as a resting position,"* and it *"mathematically severs the Braid."* One dial, three stations: free slicing with no mechanism at one end, a severed Braid at the other, and the inhabited world between them.

> **Two dials, not one.** `L4-DynamicDistortions201` §II states it: *"this $\theta$ is a temporal phase offset and reaches its limit at $\pi$. The $\theta$ of `L4-DynamicDistortions301` §VI.A is a geometric shear parameter on a single cross-section and reaches its limit at $\pi/2$. Both are torsion; they measure different things."* This section's dial is the first — a temporal phase offset, zero to $\pi$ — and it is the quantity Part Five couples to the Nieh–Yan density. Section VIII's CHSH envelope uses the second — a geometric shear, zero to $\pi/2$, bracketed by experiment under $45°$. Part Five §IV shows the distinction is load-bearing: the coupling is parity-clean only because the quantity it is built from is the temporal one.

The honest summary of what GR holds is therefore not "a wrong geometry." It is **a record it cannot account for having been written.** The mass is in the metric because mass is accumulated ledger and the ledger is already there. What is missing is the generator that wrote it. `On_TheGravityDerivation` §V says it in one sentence: *"his equations showed him the wake and had no vocabulary for the propeller."*

---

## VIII. The Ordering Is Observable — Conditionally

> **Read this before anything else in the section.** What follows names the **type** of instrument an ordering would need, and lists three instruments of that type that physics already has. All three are internal-space measurements. Whether any bears on geometric torsion depends on the coupling, and Part Five writes the coupling: the corpus's shear couples to spacetime through the **axial** torsion, and through it to the divergence of the axial current — not through the Yukawa sector. So the first instrument below is the right *type* in the wrong *sector*, kept as an example of the type. The torsion bounds of Part Six constrain a spacetime field, and they stand.

### Context forces the sequence

The order of the twelve is not free, and the reason is not a convention. It is the AbsentVar handoff, stated in `L3-FormalFoundations` §V.a:

> "Within each quadrant (group of three equations), there are three AbsentVar positions. As the cycle moves from one quadrant to the next, there is not a clean break: **the context carried through the transition is precisely the last two AbsentVars of the departing quadrant, which become the first two AbsentVars of the arriving quadrant.** What `.observe()` erases — the AbsentVar of the current equation — is precisely what the next phase requires as its first active variable."

That is a dependency relation, and it is tight. Each step's active terms must be its predecessor's held ones, and only one bit may flip at a time, so the sequence is derived from what is held absent rather than chosen. And the decisive feature: **the handoff closes.** The last quadrant hands its AbsentVars back to the first. There is no source and no sink. A dependency graph whose dependencies close into a cycle is not a DAG — the premise of `ENGINE-REFERENCE-AC` §3.5, now with its mechanism named. The net has cycles because context is handed round a ring. `L3-TheSelfProjectingBraid` §II: *"The context does not get rebuilt at each boundary. It is handed across, passed hand to hand along the braid."* Under $\omega$ the ring cannot close in place, and the helix is what a cycle traces when one coordinate grows steadily and the rest are periodic.

So Section VII's reading of the Fundamental Theorem as the DAG decree is not an analogy. **On the arrangement's side, the decree is that the context ring may be cut anywhere and the cut is free.**

### Context is perspective, and perspective is relational

What holds a variable absent is a position. `L4-Dimensionality` states it at the edge:

> "You are not looking at an object; you are sharing an edge. From your face, that edge tracks as the leading charge of a new reality (Aries). From their face, that exact same edge tracks as the heavy, necessary burden of material maintenance (Virgo). You are both reporting the 100% accurate, mathematically flawless readout of that edge from your respective faces. **You cannot see Virgo from the Fire face. You literally lack the dimension required to render it.**"

*You literally lack the dimension required to render it.* That is Part Two's sentence in the first person, and it fixes the type of instrument an ordering needs. An ordering does not appear as a quantity sitting at a point waiting to be averaged. It appears as **a disagreement between two readings that no relabelling can reconcile** — two faces, one edge, two readouts, and a discrepancy that survives every choice of names. Physics has a word for a quantity that survives every choice of names: an **invariant** — specifically, for this case, a *rephasing* invariant. A field strength, which a spatial average can drive to zero, is not it. Part One says the same from the other side: a field bound reports a zero, and a zero cannot tell an empty register from an absent one. An invariant exists only if an entry exists.

### Three instruments of the right type

**The Jarlskog invariant — the right type, the wrong sector.** Kobayashi and Maskawa (1973) proved that CP violation needs a mixing matrix with an irreducible complex phase: in two generations every phase can be absorbed into the fields, and only from three upward does one survive. Jarlskog (1985) built the basis-independent measure of it as a **commutator of the quark mass matrices**:

$$\det\!\left[\,M_u M_u^\dagger,\; M_d M_d^\dagger\,\right] \;\propto\; J, \qquad J \approx 3.1\times10^{-5}.$$

It is small, it is not zero, and no choice of basis makes it zero. It is exactly the type of quantity an ordering needs: a commutator of two readings, measured as the one number no relabelling removes. And it lives in the Yukawa sector, which is not where the corpus's shear couples. $J$ shows that physics builds and measures instruments of this type; it does not measure the corpus's commutator. The corpus's own chain is in `ProofO_HelicalTime` §9 — *"Without torsional shear, there is no Arrow of Time, no `.observe()`, and no mass. Torsional shear requires a non-removable complex phase"* — carried at its own addresses, with the Standard Model's phase far too small to account for the matter excess, and the claim being that CP violation is the structural signature of the mechanism, not its size.

**The CHSH cage — internal, and bracketed from both sides.** `L4-DynamicDistortions301` §IV derives the CHSH envelope, $S(\theta) = 2\sqrt2\cos\theta$, with the cross-sectional area carrying the envelope's geometric-branch reading. Tsirelson's bound, a theorem saturated in practice, gives $\theta \ge 0$; the loophole-free violations of 2015 give $S > 2$, hence $\theta < 45°$. So on that envelope the world sits strictly between the two ends of Section VII's dial, and both walls of the cage are experimental. The Delft result $S = 2.42 \pm 0.20$ gives $\theta \approx 31°$ — an illustration of method, not a universal shear, because $S$ depends on the state prepared and the detector settings. What does not depend on them is the bracketing.

**The generation count — a prediction that came true.** `Q9-Founders` states the seating with care about whose result is whose: the corpus supplies the antecedent (an arrow needs a non-removable phase), Kobayashi and Maskawa supply the theorem (a non-removable phase needs at least three generations), and the conclusion is *"one novel premise seating onto an established proof, not an independent derivation."* Kobayashi and Maskawa posited the third generation on algebraic grounds in 1973, before any third-generation quark was known. The bottom quark arrived in 1977 and the top in 1995.

### The everyday version

The corpus reads Hall's **action chains** as the Braid (`hall/Hall-MachineAge` §2):

> "He noticed that cultures build established sequences of events — a courtship, a business negotiation, a ritual apology. His key observation was structural: **if a participant misses a step or breaks the sequence, the entire chain drops. You cannot just pick up where you left off; you have to restart the sequence from the top.** Think of the TCP/IP handshake: *SYN*, *SYN-ACK*, *ACK*."

A write-ordering is observed through what happens when it is violated. You do not read the order off a dial; you break it and the chain drops. That is the epistemics of every commutator measurement in physics: you do not observe "the order," you observe that doing $A$ then $B$ lands somewhere other than $B$ then $A$.

### What the section is

A demonstration that **the host already stocks instruments of the right type.** If an ordering is to be observed, it will be by a quantity no relabelling moves, and physics built several such quantities decades ago for its own reasons. That costs nothing, because it claims nothing about geometry. Which instrument would observe *this* ordering is now a question about the axial channel, and Part Five is where it is asked.

---

## What Reading Part Four Back Should Leave

The arrangement binds against the host in four places, and in each the host bought something.

Reverse every arrow and the bill changes on four of six edges, every COMMIT becoming a ROUTE; the host's equations do not notice, because the host has no bill. GR relates an ordered source to a symmetric structure, and both are true. The arrangement carries two clocks, a rate and a record; the host has one coordinate and asks it to do both jobs, and the problem of time is the receipt. The Fundamental Theorem projects a twenty-four-parameter family onto a point and prices the discard nowhere. And the host slices its 4-volume freely, assuming the constraint net orders — while its own constraint algebra, since 1973, has been reporting that it does not.

None of these asserts a value. Each says where the host's rule binds and what the rule cost. The one Grammar result among them, the COMMIT/ROUTE pairing, reads off a table anybody can check. And the ordering is observable in principle, by an instrument of the right type — a quantity no relabelling moves. Physics has several. Which one could see this ordering depends on a coupling, and the next part writes it.

---

### References

* Arnowitt, R., Deser, S., & Misner, C. W. (1962). *The dynamics of general relativity*. In *Gravitation: An Introduction to Current Research*, 227–265. Wiley.
* Teitelboim, C. (1973). *How commutators of constraints reflect the spacetime structure*. Ann. Phys., 79(2), 542–557.
* Kobayashi, M., & Maskawa, T. (1973). *CP-violation in the renormalizable theory of weak interaction*. Prog. Theor. Phys., 49(2), 652–657.
* Jarlskog, C. (1985). *Commutator of the quark mass matrices in the standard electroweak model and a measure of maximal CP nonconservation*. Phys. Rev. Lett., 55(10), 1039–1042.
* Particle Data Group. *Review of Particle Physics* — CKM quark-mixing matrix review. (Source for $J$.)
* Cirel'son (Tsirelson), B. S. (1980). *Quantum generalizations of Bell's inequality*. Lett. Math. Phys., 4(2), 93–100.
* Hensen, B., *et al.* (2015). *Loophole-free Bell inequality violation using electron spins separated by 1.3 kilometres*. Nature, 526, 682–686.
* Giustina, M., *et al.* (2015). Phys. Rev. Lett., 115, 250401.
* Shalm, L. K., *et al.* (2015). Phys. Rev. Lett., 115, 250402.
* Hall, E. T. (1976). *Beyond Culture*. Anchor Press/Doubleday. (Action chains.)

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.

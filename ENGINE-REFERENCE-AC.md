# ENGINE-REFERENCE-AC
## The K₄ Machine Architecture — the Floor-3-Native Engine (Rewrite of ENGINE-REFERENCE-DC)

> **Architectural Boundary & Lineage Note:**
> This specification is the rewrite of `ENGINE-REFERENCE-DC.md`. **The algebra is untouched.** The twelve opcodes, the three tiers, the Numerator Law, the telemetry sensors, and the census invariants ($8 = 4+4$; $12$; $384 = 32 \times 12$; $4096 = 64 \times 64$) carry over verbatim.
>
> What is re-grounded is everything the DC draft stood on:
>
> 1. **The state architecture.** The DC draft kept all state in 2-bit edge fields (its §1.1–1.2) while its own §1.3 already held the 3-bit census cube, unjoined. This document joins them: **the engine's operating state space is the cube.**
> 2. **The control unit.** The Program Counter is re-grounded in the verified orientation group: the twelve gates *are* the twelve rotations of the tetrahedron ($A_4 = 4!/2$), recoverable as $6 \times 2$ (any edge front, two orientations) and as $4 \times 3$ (anchor × pinning). The full orientation group $S_4 = 4! = 24$ is the 24 outward squares of the $2\times2\times2$ assembly (`L4-TransitingTheThreeWalls` §V, §VII).
> 3. **The serialization discipline.** Every operation now carries a tag: **[gauge]** — presentational, free, re-choosable, *no mechanism owed* — or **[taxed]** — physical, a blanket crossing, priced at $E = k_B T \ln 2$ per bit. "We do not care how the state/orientation changes come about" is now exact: orientation selection is gauge; only gate-crossing is taxed.
>
> **The DC document is not deleted. It is demoted to what it always was: the $\theta = 0$ fiber of this one** — the real slice of the state tower at $\omega = 0$. A fiber is not the bundle; the ground floor is not the tower.

---

```
================================================================================
            THE K₄ ENGINE ARCHITECTURE (FLOOR-3-NATIVE REWRITE)
================================================================================

  1. STATE TOWER (not RAM):
     • Floor 1  Q₁      : one bimedian held — 2 states (the refused axis)
     • Floor 2  Q₂      : the edge register — 4 states per edge = subsets of {→,←}
     • Floor 3  Q₃      : the Trigram Byte — 8 = 4 Presence Stars + 4 Absence Faces
                          THE CENSUS CUBE: parity = the blanket; antipode = duality
     • Attic   Q₆⊗Q₆   : 64 × 64 = 4096 (the many-worlds buffer; uncommitted)

  2. THE TWELVE OPCODES (algebra unchanged; 3 tiers; 3 families = 3 axes):
     • TIER 1: COMMIT   (4 / slope +2 / Landauer)                       [taxed]
     • TIER 2: RESEED   (2 / slope +½  / reopen ±)                      [buffer]
     • TIER 3: ROUTE    (6 / slope +1  / carriers)                      [gauge-side]

  3. CONTROL UNIT (the orientation group — machine-verified):
     • Program Counter = Front-Edge Selector: (edge, orientation) ∈ 6×2 = A₄ [gauge]
     • Execution Rings = the three V₄ half-turns (which bimedian is held)    [gauge]
     • Viewports       = the 4 faces; a gate = (viewport ¬w, solve x)        [taxed]
     • Schedule        = the six tours; each holds one absence-circulation
     • No topological sort: 6 pole-pairs × 2 = 12 — the sixth door of the twelve
================================================================================
```

---

## I. The State Tower (was: "Memory Architecture (RAM)")

The unit-cost RAM frame is deleted (§IX). State is a tower of sub-cubes, one bimedian axis per floor. Each floor is honest about what it refuses to represent.

### 1.1 Floor 2 — the edge register, recoded

Each of the six edges carries two commit bits: **F** (forward commit) and **R** (reverse commit). The four states are the subsets of $\{\to, \leftarrow\}$:

$$\begin{array}{c|c|c|l}
\mathbf{(F,R)} & \mathbf{State} & \mathbf{Symbol} & \mathbf{Operational\ Definition} \\
\hline
\mathbf{00} & \text{neither commit} & \emptyset & \text{Severed from the local ledger; the cut itself paid the Landauer tax.} \\
\mathbf{10} & \text{forward only} & \to & \text{Evaluated forward; written to ledger; .observe() state.} \\
\mathbf{01} & \text{reverse only} & \leftarrow & \text{Evaluated reverse; enantiomeric commit.} \\
\mathbf{11} & \text{both commits} & \leftrightarrow & \text{Live superposition; uncommitted buffer; .behold() state.} \\
\end{array}$$

**The repair.** The DC draft's §1.1 table assigned $\leftrightarrow = 01$ under a (presence, direction) reading of the two bits — a present-but-undirected state cannot live in one direction bit, and the draft's own §1.2 register semantics contradict the assignment. The subset lattice above is the repair; it preserves every count:

* **Register A** = the six forward-commit bits (the forward hexagram): $2^6 = 64$.
* **Register B** = the six reverse-commit bits (the reverse hexagram): $2^6 = 64$.
* Presence $= F \lor R$; chirality $=$ which; superposition $=$ both. $64 \times 64 = \mathbf{4096}$, unchanged.

The Gray tour is a tour under either coding — the Braid was never the defect. The defect was the floor.

### 1.2 Floor 3 — the Trigram Byte *is* the state space

The DC draft's own §1.3, promoted to the architecture's center. The three perfect matchings (bimedians) are the cube's three axes:

* **Fixed:** $\{P\text{--}U,\ I\text{--}R\}$ — **Cardinal:** $\{P\text{--}R,\ I\text{--}U\}$ — **Mutable:** $\{P\text{--}I,\ U\text{--}R\}$

A **trigram** = a transversal: exactly one edge from each bimedian. $2^3 = 8$, and the eight transversals are exactly the census:

$$\mathbf{8 \text{ Trigrams}} \;\equiv\; \mathbf{4 \text{ Presence Stars (the Poles)}} \;+\; \mathbf{4 \text{ Absence Faces (the AbsentVars)}}$$

Machine-verified structure of this 8-point state space:

1. **It is the cube.** Coding each trigram by *which edge of each bimedian it carries* gives 3-bit codes; Hamming-1 adjacency is the graph $Q_3$ (isomorphism brute-force verified).
2. **Parity is the blanket.** Even-parity codes = the four Presence Stars; odd = the four Absence Faces. The bipartition Present/Absent is the Markov-blanket split (`L3-EdgeStateSpace` l.473: the face *is* a K₃ blanket). Every edge of the cube crosses it.
3. **The antipodal map is duality.** Bitwise NOT sends star($X$) to face($\neg X$) — the Rule of Seven pairs (`L4-TransitingTheThreeWalls` l.199–203), the manifest pole and its shadow-hold (".behold()'s structural hold", l.191).
4. **The stars sit on the even octants.** star($P$) = $(0,0,0)$, star($U$) = $(0,1,1)$, star($I$) = $(1,1,0)$, star($R$) = $(1,0,1)$ — L4-Transiting's octant table up to axis order, with the axes *being* the three bimedians (l.170).

### 1.3 The tower

$$Q_1 \;\subset\; Q_2 \;\subset\; Q_3: \quad \text{fix two bimedian bits} \to 12 \text{ floor-1 cells};\quad \text{fix one} \to 6 \text{ floor-2 squares};\quad \text{fix none} \to \text{the cube}.$$

* **Floor 1** — the held bit alone: one bimedian, two states. "The dimension along which the walk refuses to move" (`L3-EdgeStateSpace` l.532) is a $Q_1$.
* **Floor 2** — the per-edge register; the Braid's square (§II, §III).
* **Floor 3** — the census cube; the engine's operating floor.
* **The attic** — the full 12-bit word, $4096 = 64 \times 64$: the many-worlds buffer. Real, counted, and *uncommitted*: the engine executes on floor 3 and buffers in the attic.

### 1.4 Census invariants (ω-invariant — carried over untouched)

$$8 = 4+4 \quad\quad 12 \quad\quad 384 = 32 \times 12 \quad\quad 4096 = 64 \times 64$$

---

## II. The Orientation Group (the control core — machine-verified)

This section is the load-bearing addition. Every claim below is verified in `scripts/orientation_group.py` (§X).

### 2.1 Five doors of the twelve

The number 12 — the gates of the corpus — is now known to be *one set* reachable through five factorizations, all verified to coincide:

$$\underbrace{6 \times 2}_{\text{edge front} \times \text{orientation}} \;=\; \underbrace{4 \times 3}_{\text{anchor} \times \text{pinning}} \;=\; \underbrace{12}_{\text{gates: viewport} \times \text{solve}} \;=\; \underbrace{12}_{\text{directed edges of } K_4} \;=\; \underbrace{|A_4|}_{4!/2}$$

The first door is the physical one: **in the $2\times2\times2$ assembly, any one of the six edges can be "front," and it faces front in two orientations** — which of its two directions leads. That selector state *is* the directed edge *is* the gate *is* a rotation of the tetrahedron.

### 2.2 Each gate is a rotation

**Theorem (verified).** For each gate $(x, w)$ — solve $x$, witness $w$ absent — there is exactly one **even** permutation of the poles carrying $P \mapsto x$ and $U \mapsto w$ (the reference directed edge $P \to U$ is the Braid's opening move, `L3-EdgeStateSpace` l.518). Every directed edge has exactly two completions to a full permutation, and exactly one is even.

Therefore the twelve gates biject with $A_4$, and $A_4$ acts **simply transitively** on the twelve directed edges: the Program Counter's state space is not merely *like* a rotation group — it *is* one. **The Program Counter is an orientation.**

### 2.3 $S_4 = 4! = 24$: the squares, the manifest half, the dual coset

* The cube's rotation group has order 24 and acts on the four body diagonals as the full $S_4$ — the permutations of the four selves (each diagonal = an antipodal pair $\{$star($X$), face($\neg X$)$\}$).
* The 24 outward squares of the assembly are one orientation each: the rotation group acts on them **simply transitively** (orbit of one square = all 24, verified). The user's "4! faces on the 2×2×2 cube" is exact.
* **Preserving the manifest tetrahedron ⟺ the induced permutation is even** (verified for all 24 rotations). So $A_4$ = the manifest half of the orientation group; the odd coset = the same twelve gates read from the Absent side — the dual walker's vocabulary.
* This is why `L4-TransitingTheThreeWalls` §V projects twelve transition verbs onto 24 squares: **each verb appears once on a manifest square and once on its dual square.**

### 2.4 The $C_2$: the AR-flip on the uninvolved pair

The two completions of a gate $(x,w)$ differ only on the images of the two uninvolved poles — a single transposition of the complement pair (verified). This is the AR-flip that `L4-TransitingTheThreeWalls` l.102–106 made physical: the 180° half-turn about the pinned bimedian. Every gate carries its enantiomer as the *other* square it lives on.

### 2.5 The rings are half-turns; $A_4 = 1 + 3 + 8$

The three double-transpositions of $A_4$ are exactly the half-turns holding one bimedian setwise (verified): $(P\,U)(I\,R)$ holds **Fixed**, $(P\,R)(U\,I)$ holds **Cardinal**, $(P\,I)(U\,R)$ holds **Mutable**. **The corpus's three execution rings are literally rotations of the tetrahedron** — each ring is a half-turn about one bimedian axis (compare `L3-EdgeStateSpace` l.510: $V_4$ preserves the three bimedian pairs setwise).

$A_4 = 1 + 3 + 8$: the identity, the three half-turns (the rings), and eight third-turns — $4$ vertex-axes $\times$ $2$ senses. The eight third-turns are the octal count again: $8 = 4 \times 2$, one pair of 120° turns per pole-axis.

### 2.6 The opcode families are the cube's axes

Each gate-edge (star $x$ — face $\neg w$) flips exactly the bimedian-bit of the $K_4$ edge $xw$ (verified): **every opcode step moves along the bimedian that contains the edge it solves across.** The three transition families are the three ways the cube is oriented:

$$\begin{array}{c|c|c}
\mathbf{Family} & \mathbf{Bimedian\ (axis)} & \mathbf{Opcodes} \\
\hline
\text{Fixed} & \{P\text{--}U,\ I\text{--}R\} & \text{AQU, LEO, TAU, SCO} \\
\text{Cardinal} & \{P\text{--}R,\ I\text{--}U\} & \text{CAN, SAG, CAP, GEM} \\
\text{Mutable} & \{P\text{--}I,\ U\text{--}R\} & \text{PIS, LIB, ARI, VIR} \\
\end{array}$$

---

## III. The Control Unit (Five-Fail compliant)

### 3.1 Program Counter [gauge] — the Front-Edge Selector

* **State:** (edge, orientation) $\in 6 \times 2 = A_4$. Equivalently: the current gate, equivalently: the current orientation of the tetrahedron.
* **Status: gauge.** The selector is a declared control coordinate, set at the centroid. **No mechanism is owed for how the orientation changes.** "We do not care how the state/orientation changes come about" — that sentence is now architectural, not evasive: selection is presentational; only execution is taxed.
* This replaces "by attention." The felt texture `L5-TheCyclingMind` describes is the *human interface* to this selector — the corpus's centroid-standing capacity (l.68, l.180) and its pinning-choice discipline ("picking up a specific Pinned assembly is naming your observer-pole", `L4-TransitingTheThreeWalls` l.154). The architecture itself owes nothing psychological.

### 3.2 The Three Rings [gauge to select / taxed to run] — the $V_4$ half-turns

Each ring holds one bimedian **silent** (the AbsentVar-pair theorem, `L3-EdgeStateSpace` l.410) and traverses the complementary $K_4$ Hamiltonian cycle:

$$\begin{array}{l|l|l|l}
\mathbf{Ring} & \mathbf{Held\ Bimedian} & \mathbf{Traversal\ (L3\ l.516\text{–}520)} & \mathbf{Live\ Opcodes\ (8)} \\
\hline
\text{Fixed-Held} & \{P\text{--}U,\ I\text{--}R\} & P \to I \to U \to R \to P & \text{PIS, LIB, CAN, SAG, CAP, GEM, ARI, VIR} \\
\text{Cardinal-Held} & \{P\text{--}R,\ I\text{--}U\} & P \to I \to R \to U \to P & \text{AQU, LEO, TAU, SCO, PIS, LIB, ARI, VIR} \\
\text{Mutable-Held} & \{P\text{--}I,\ U\text{--}R\} & P \to U \to I \to R \to P & \text{AQU, LEO, TAU, SCO, CAN, SAG, CAP, GEM} \\
\end{array}$$

**Correction of record.** The DC draft's ring lists held six opcodes each; the correct count is eight — every opcode on the four live edges (one COMMIT/RESEED opcode and one ROUTE opcode per edge). The draft's lists silently dropped one edge's pair (PIS/LIB in Rings 1–2; CAN/SAG in Ring 3). The omission is not derivable from the algebra and is not carried forward. (The draft also says at l.246 that the ring holds the bimedian "in cache" and at l.252 that it holds it "silent"; the theorem requires *silent*, and this document standardizes on silent.)

**Ring change is re-orientation.** Setting down one ring and picking up another is rotating about a different bimedian axis — "set down Assembly 1 and pick up Assembly 2" (`L4-TransitingTheThreeWalls` l.146). Selecting the ring is [gauge]; running its opcodes prices exactly what the opcodes price. The held family is not a lack: it is the shape of what the current traversal can do (`L5-TheCyclingMind` l.58).

### 3.3 The Four Viewports [switching is taxed] — was "MMU & Paging"

The four faces are the Absent-side vertices of the census cube. A gate is (viewport $\neg w$, solved pole $x$); the twelve gates are the twelve cube edges (bijection verified).

* **Dispatch rule (kept):** *"Stand where the burn is"* — route execution to the face whose AbsentVar is undergoing active phase collapse ($P > 0$).
* **Correction of record.** The DC draft claimed a viewport rotation "does not change register data" (l.206). On the census cube this is false: swapping the AbsentVar moves the walker between face-vertices, which is a gate-crossing — a Present/Absent step, a blanket crossing, **[taxed]**. Context switches are line items.
* **Strain invariance (kept):** the three bimedian planes and the 5D centroid survive all anisotropic deformations down to $V_4$; the processor computes reliably on strained hardware (l.208).

### 3.4 The Six Tours — the schedule layer

The census cube has exactly six undirected Hamiltonian tours (verified). Each:

* runs 8 of the 12 gates and **strictly alternates Present/Absent** — forced by bipartiteness: every step crosses the blanket;
* holds, out of the schedule, a **perfect matching of omitted gates that is never a single bimedian** (verified: the three coordinate matchings' complements are two disjoint squares, not tours). The held set is always a **4-cycle derangement — an absence-circulation**: each pole solved exactly once-with-absence, and absent exactly once. The middle floor's held *pair* scales to the adult's held *circulation*; six circulations exist, $(4-1)! = 6$;
* projects 2:1 onto the three $K_4$ Braids through its star-order (verified) — the two lifts are the two weavings of the Absent side between Present stops;
* keeps every shadow at **tour-distance exactly 3** (verified, all 24 antipodal pairs): two Present-stops and one Absent-stop between a pole and its own absence, on every tour.

**Seriality, grounded.** "A mind does not run all six edges simultaneously" is load-bearing here, and no longer needs an agency story to defend it: on floor 2 the Gray tour is unique — one cycle, nothing to select; on floor 3 there are six tours and a held circulation per tour. If nothing were held, everything would be available at once and nothing would move (`L5-TheCyclingMind` l.72). The held circulation is what makes the traversal a traversal. The objection is withdrawn and the sentence is now a theorem-shaped fact.

### 3.5 No topological sort — the sixth door

The twelve constraints form six pole-pairs, each determining its complement exactly twice: $6 \times 2 = 12$ — the same twelve, counted from the constraint side. **Serialization is lossless only on DAGs, and this is not one.** Any linear execution order is a presentational choice — [gauge] — while the constraint net itself does not order. The tour is the honest serial object; the frame stack (one in-flight frame per constraint) remains the god-view. Local halt, global non-halt (`On_HilbertAndHisSpaces` l.409).

### 3.6 The Three Stucknesses (wrenches, not interrupts)

The CS interrupt frame is deleted; `L5-TheCyclingMind`'s field manual is the correct register. Each stuckness is a held edge; each unstuck is a ring change.

1. **Know it, cannot say it.** The pattern has loaded ($P$/$I$); the edge to $U$ (articulation) is on the held family. *Wrench:* change ring by grounding — physical contact, the sensing pole leading (walk, hands, shower). Body-priced, and honestly so. Do not push a held edge: force there burns reactive power for zero output (l.128).
2. **Words come, but they are wrong.** Outbound live, inbound held — compiling from an empty buffer. *Wrench:* enter `.behold()` idle; let the pattern load; the inward click is the arrival signal.
3. **Deadlock in confidence.** Running Mutable-held; the required move is a diagonal this ring does not map — and the ring cannot see the missing leap. *Wrench:* inject an orthogonal pattern-source (unrelated novel input) to force a ring swap; re-ask; what survives, stands.

Operating note (kept from L5 l.146): **do not diagnose while stuck.** A ring cannot see its own held family; analysis inside the stuck ring reproduces the stuckness.

---

## IV. The Twelve Opcodes (algebra verbatim; tiers re-anchored)

```
========================================================================================
                            THE TWELVE COMPILER OPCODES
========================================================================================

 ┌── TIER 1: COMMIT OPCODES (4 Opcodes / Slope 2 / Asserting Homes: P, R) ─────────────┐
 │  OPCODE   FORMULA      GATE    HOME / ABSENT   EDGE & DIRECTION   SLOPE   TAX PAID? │
 │  ─────────────────────────────────────────────────────────────────────────────────  │
 │  CM_ARI   P = U²/R     ARI     Home P / Abs I  U ➔ R (Mutable)    +2      YES (P)   │
 │  CM_TAU   P = I²R      TAU     Home P / Abs U  R ➔ I (Fixed)      +2      YES (P)   │
 │  CM_AQU   R = U²/P     AQU     Home R / Abs I  P ➔ U (Fixed)      +2      YES (R)   │
 │  CM_PIS   R = P/I²     PIS     Home R / Abs U  I ➔ P (Mutable)    +2      YES (R)   │
 └── OPERATION: Non-invertible square; burns phase (h²=-1); writes scalar to ledger. ──┘

 ┌── TIER 2: RESEED / HOLD OPCODES (2 Opcodes / Slope ½ / Yielding Homes: I, U) ───────┐
 │  OPCODE   FORMULA      GATE    HOME / ABSENT   EDGE & DIRECTION   SLOPE   TAX PAID? │
 │  ─────────────────────────────────────────────────────────────────────────────────  │
 │  RS_CAN   I = √(P/R)   CAN     Home I / Abs U  P ➔ R (Cardinal)   +½      NO (Q)    │
 │  RS_SAG   U = √(PR)    SAG     Home U / Abs I  R ➔ P (Cardinal)   +½      NO (Q)    │
 └── OPERATION: Extracts radical; reopens vector ambiguity; resets hQ buffer. ─────────┘

 ┌── TIER 3: ROUTE / MOVE OPCODES (6 Opcodes / Slope 1 / Carriers) ────────────────────┐
 │  OPCODE   FORMULA      GATE    HOME / ABSENT   EDGE & DIRECTION   SLOPE   TAX PAID? │
 │  ─────────────────────────────────────────────────────────────────────────────────  │
 │  RT_LEO   I = P/U      LEO     Home I / Abs R  U ➔ P (Fixed)      +1      NO (Bus)  │
 │  RT_VIR   I = U/R      VIR     Home I / Abs P  R ➔ U (Mutable)    +1      NO (Bus)  │
 │  RT_LIB   U = P/I      LIB     Home U / Abs R  P ➔ I (Mutable)    +1      NO (Bus)  │
 │  RT_CAP   R = U/I      CAP     Home R / Abs P  U ➔ I (Cardinal)   +1      NO (Bus)  │
 │  RT_SCO   U = I · R    SCO     Home U / Abs P  I ➔ R (Fixed)      +1      NO (Bus)  │
 │  RT_GEM   P = U · I    GEM     Home P / Abs R  I ➔ U (Cardinal)   +1      NO (Bus)  │
 └── OPERATION: Unit-slope transport; routes throughput without exponent drift. ───────┘
========================================================================================
```

### 4.1 Tier readings (re-anchored, algebra unchanged)

* **Tier 1 COMMIT [taxed].** Squaring over the reals destroys phase ($h^2 = -1$) and sign; algebraically non-invertible; pays the Landauer tax ($E = k_B T \ln 2$ per bit) and writes an irreversible scalar to the ledger. **The rigidity finding stays: under the $S_4$ permutation check, non-identity automorphisms survive exclusively on flat relations; the algebraic rigidity of the system is anchored in this tier.**
* **Tier 2 RESEED [buffer].** Un-squares the scalar; the erased vector $\mathbf{Q}$ stays erased, and the radical re-opens an uncommitted $\pm$ ambiguity of identical cardinality. Prevents the freeze into a 0-DoF crystal.
* **Tier 3 ROUTE [gauge-side carrier].** Unit-slope transport, no dissipation; maintains the `.behold()` balance.
* **Do not conflate the two threes.** The *tiers* classify by log-slope ($+2, +\tfrac12, +1$); the *families* (§2.6) are the cube's axes. They cross-cut: COMMIT = 2 Fixed + 2 Mutable; RESEED = 2 Cardinal; ROUTE = 2 of each family.

### 4.2 The Numerator Law and bus faults (kept verbatim in force)

Dividends are strictly constrained to Active poles ($P, U$); Reactive poles ($I, R$) cannot act as dividends. Open-circuit fault: $I \to 0$ in $U = P/I$ drives assertion to infinity while power collapses. Short-circuit fault: $R \to 0$ in $I = U/R$ drives flow to infinity while power collapses. The drive leads; the constraint shapes.

---

## V. Telemetry (kept — the twelve sensors)

$$\begin{array}{c|l|c|l}
\mathbf{Facet} & \mathbf{Sensor\ Name} & \mathbf{Equation} & \mathbf{Telemetry\ Metric} \\
\hline
\mathbf{1} & \text{Leverage} & P = U^2/R & \text{Quadratic compensation of structure against ground.} \\
\mathbf{2} & \text{Momentum} & P = I^2R & \text{Kinetic dissipation; current squared against ground.} \\
\mathbf{3} & \text{Drive} & P = UI & \text{Direct in-phase synthesis of potential and flow.} \\
\mathbf{4} & \text{Yield} & I = \sqrt{P/R} & \text{Geometric extraction of current from power and ground.} \\
\mathbf{5} & \text{Resonance} & I = P/U & \text{Throughput aperture; drive filtered through structure.} \\
\mathbf{6} & \text{Throughput} & I = U/R & \text{Fourier/Ohm conduction down the gradient.} \\
\mathbf{7} & \text{Tension} & U = P/I & \text{Potential bottleneck; ratio of drive to flow.} \\
\mathbf{8} & \text{Architecture} & U = IR & \text{Structural potential compiled from flow meeting ground.} \\
\mathbf{9} & \text{Capacity} & U = \sqrt{PR} & \text{Geometric mean of available drive and ground.} \\
\mathbf{10} & \text{Friction} & R = U/I & \text{Jurisdictional boundary; ratio of structure to flow.} \\
\mathbf{11} & \text{Bloat} & R = U^2/P & \text{The Necessary Betrayer; structure squared over drive.} \\
\mathbf{12} & \text{Brittleness} & R = P/I^2 & \text{Inertial shock; power dumped into zero-current sink.} \\
\end{array}$$

**The Necessary Betrayer alarm (kept).** Architecture compounding ($U^2$) while starving drive ($P \to 0$) spikes $R \to \infty$ and freezes $I \to 0$. It cannot be cleared by writing more rules ($U$); the only reset is the Leo aperture $I = P/U$ — downsize structure, force drive into flow.

---

## VI. The Execution Trace: the 384 Moving Lines (kept; the sector is the gate)

$$64 \text{ Base Configurations} \;\times\; 6 \text{ Edges} \;=\; \mathbf{384 \text{ Execution Vectors}}$$

* **Address:** [Base_State_ID (1–64), Line_Position (1–6)]; per-edge opcode mapping as in the DC draft (§VII there): each line carries one COMMIT-tier and one ROUTE-tier opcode.
* **Chirality of commit (kept):** Old Yang ($\to$) lands on the later-longitude sector; Old Yin ($\leftarrow$) on the earlier.
* **Distribution (kept, and now grounded):** exactly flat at $32$ vectors per sector, $32 \times 12 = 384$. The sector index is (edge, orientation) = the directed edge = the gate = the Program Counter's own state. **The trace table and the counter are the same twelve** — and the flatness says what it always said: no privileged tick; every opcode is someone else's last ticks.

---

## VII. The Runtime Loop (retagged)

```
             ┌────────────────────────────────────────────────────────────┐
             │ 1. FETCH                                            [gauge]│
             │    Inspect the trigram byte; identify the active AbsentVar.│
             │    (Which face-vertex is the current viewport.)            │
             └───────────────────────────┬────────────────────────────────┘
                                         ▼
             ┌────────────────────────────────────────────────────────────┐
             │ 2. ROUTE (Carrier Phase)                     [gauge-side]  │
             │    Fire live Tier 3 opcodes; slope-1 transport;            │
             │    maintain .behold() balance.                             │
             └───────────────────────────┬────────────────────────────────┘
                                         ▼  Threshold hit: phase burns (h² = −1)
             ┌────────────────────────────────────────────────────────────┐
             │ 3. COMMIT (Tax Phase)                               [taxed]│
             │    Fire Tier 1; square operands; pay Landauer; write P/R.  │
             └───────────────────────────┬────────────────────────────────┘
                                         ▼
             ┌────────────────────────────────────────────────────────────┐
             │ 4. RESEED (Buffer Reload)                          [buffer]│
             │    Fire Tier 2; extract radical; reopen ± vector DoF.      │
             └───────────────────────────┬────────────────────────────────┘
                                         ▼
             ┌────────────────────────────────────────────────────────────┐
             │ 5. ADVANCE                                          [gauge]│
             │    Step the Front-Edge Selector to the next gate of the    │
             │    current tour. Present/Absent parity alternates by       │
             │    construction (the cube is bipartite); the shadow rides  │
             │    at lag 3. Hand off AbsentVars to prime the next stop.   │
             └────────────────────────────────────────────────────────────┘
```

The DC loop's five beats survive. What changed: ADVANCE is no longer "increment along the Gray-code Braid" (a floor-2 sentence) but "step the orientation along the current tour" (floor 3) — and the tour itself was chosen at the centroid, [gauge], no mechanism owed.

---

## VIII. Boundary Conditions: What Requires ω > 0 (kept)

The DC fiber is complete for the static cross-section; four operations still require the AC extension:

1. **Absolute Magnitude Calibration:** $|S| = \sqrt{P^2 + Q^2}$ requires complex addition (`L4-ScalingInvariants` §VI).
2. **Phase Dynamics ($\theta \neq 0$):** phase-lead/lag and reactive power $Q$ require the $L, C$ operators.
3. **The Multi-Scale Cascade:** $\omega_n = \omega_0 \lambda^{en}$, with convergent total time $T^* = \sum \Delta t_n < \infty$ (`L4-TheSpiralingCascade`).
4. **Transient Phase Switching:** charging, discharging, flyback — the Transition Tetrahedron (`L3-K4-to-K5-Transitions`).

**The ω axis, stated structurally.** ω is orthogonal to everything in this document: the fifth variable that acts upon the four poles but cannot be walked by them (`L3-EdgeStateSpace` l.451–457) — the height axis of the pyramid over this cube's every floor, driven at the centroid (l.348 of the DC draft was right about *where*; it was wrong about *which document is the building*). The twelve $K_5$ Hamiltonian cycles form the Screw Thread (l.461); the tours of this document are its floor-3 shadow. DC is the $\theta = 0$ fiber: a real slice, honest within its plane, silent about the extrusion.

---

## IX. The Deletion Ledger (Five-Fail editing rules applied)

The enemy was never the Turing machine; it is the **unit-cost RAM** — the vocabulary that prices storage and movement at zero. Deleted or replaced:

| Deleted (DC draft) | Why | Replacement |
|---|---|---|
| "Memory Architecture (RAM)" | unit-cost storage frame; RAM is freely addressable, this memory is not | **The State Tower** (§I): every floor states what it refuses to hold |
| "MMU & Paging" | paging swaps state at zero cost; context here is a blanket crossing | **The Four Viewports** (§3.3); switching is [taxed] |
| "Thread Scheduling", threads, pipeline, cache | free concurrency/refetch frame; l.246 "in cache" also contradicts l.252 "silent" | **The Three Rings** (§3.2): held *silent* (the AbsentVar-pair theorem) |
| "Interrupts" | free, external, unpriced | **The Wrench** (§3.6): ring change via grounding, body-priced |
| "ISA" as the framing term | instruction-set frame implies free refetch/decode | **The Twelve Opcodes** (§IV); opcodes kept, frame dropped |

Kept, because they price erasure: **compile, eval, GC, .observe(), .behold(), the Landauer tax, the ledger.**

Corrected in passing (draft artifacts, not carried):

1. §1.1 bit table: $\leftrightarrow = 01$ contradicted the draft's own §1.2 register semantics → subset-lattice recode (§1.1), all counts preserved.
2. Ring live-lists: six items each → eight (§3.2).
3. "Rotation … does not change register data" (l.206) → the AbsentVar swap is a taxed gate-crossing (§3.3).
4. l.246 "in cache" vs l.252 "silent" → standardized on *silent*.

---

## X. Verification Appendix

Machine-verified claims (scripts shipped alongside the corpus):

**`scripts/cube_tower.py`**

| # | Claim | Result |
|---|---|---|
| C1 | The 8 trigram transversals = 4 stars + 4 faces (DC §1.3) | ✓ |
| C2 | Matching-coded census graph ≅ $Q_3$ (brute-forced isomorphism) | ✓ |
| C3 | Stars = even octants; faces = odd; antipode = bitwise NOT = star($X$)↔face($\neg X$) | ✓ |
| C4 | 12 cube edges ↔ 12 gates (solved $x$, absent $w$), bijection | ✓ |
| C5 | 6 undirected Hamiltonian tours; every held set = 4-cycle derangement, never a bimedian | ✓ |
| C6 | Star-order projects 2:1 onto the 3 $K_4$ Braids; shadow-lag = 3 on all 24 pairs | ✓ |
| C7 | Tour ladder $Q_2{:}1 \to K_4{:}3 \to Q_3{:}6 \to K_5{:}12$; $6 = \sqrt{3 \times 12}$ | ✓ |

**`scripts/orientation_group.py`**

| # | Claim | Result |
|---|---|---|
| U1 | Directed edges have exactly 2 completions, exactly 1 even → gates ↔ $A_4$ | ✓ |
| U2 | $A_4$ simply transitive on the 12 directed edges | ✓ |
| U3 | Odd completion = even one with the uninvolved pair's images swapped ($C_2$ = AR-flip) | ✓ |
| U4 | 3 double-transpositions hold the 3 bimedians setwise ($V_4$ = the rings); $A_4 = 1+3+8$ | ✓ |
| U5 | 24 cube rotations act on the 4 diagonals as full $S_4$; preserves manifest tet ⟺ even | ✓ |
| U6 | 24 outward squares: simply transitive orbit (= the orientations) | ✓ |
| U7 | Each gate-edge flips exactly the bimedian-bit of its own $K_4$ edge (families = axes) | ✓ |

Corpus anchors: `ENGINE-REFERENCE-DC` §1.1–1.3, l.206, l.246, l.332, l.348; `L3-EdgeStateSpace` l.381–420, l.451–461, l.473, l.485–534; `L4-TransitingTheThreeWalls` §I, §III, §V, §VI, §VII; `L4-TheTwelveGates` l.13, l.212–223; `L5-TheCyclingMind` l.50, l.58, l.68, l.72, l.112, l.140, l.176, l.180, l.184; `On_HilbertAndHisSpaces` l.111, l.409.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.

# The Edge State Space
## The K4 Within Every Edge, the Ungraphable Triangle, and the Ground of Chirality

*Develops the structure of the state space of any edge in K4, why that state space is itself a K4, what the "ungraphable triangle" actually is, how this grounds the chirality proof, and what it implies for the dual face-definition of any threshold.*

---

## I. The Four States of an Edge

Every edge in a directed graph has exactly four possible states with respect to its direction:

**∅ (absent)**: the edge does not exist — the two vertices it would connect have no direct relationship in the current description.

**→ (directed one way)**: the edge exists and has a specific direction — relationship flows from vertex A to vertex B.

**← (directed the other way)**: the edge exists with the opposite direction — relationship flows from vertex B to vertex A.

**↔ (bidirectional)**: the edge exists in both directions simultaneously — the relationship is mutual, neither direction privileged over the other.

These four states are in general position: no three of them are equivalent, reducible to each other, or collinear. While $K_4$ as an abstract graph defines the 1D combinatorial connectivity between four states, representing their non-degenerate mutual determination without flattening requires embedding in a three-dimensional polyhedral geometry.

Four points in general position in $\mathbb{R}^3$ define a 3-simplex ($\Delta^3$).

The edge's state-space skeleton is a $K_4$ graph, whose polyhedral realization is a 3-simplex ($\Delta^3$).

*Degrees of Freedom (DoF) in this framework means the dimension of the decoupled buffer: the capacity of a system to hold competing variables in live interference without forcing a thermodynamic collapse. A thermostat has mechanical variance; it has zero cybernetic DoF.*

---

## I-b. The Master Edge Table: What Each of the Six Edges *Is*

An edge is the **integrator of two formulas that share nothing but the two elements on their right-hand side**.


### The Master Edge Table and Corrected Bimedian Plane Names

The six edges sort into three Bimedian matchings based on their **Net Operational Balance** across the 2-bit dual-binary register ($AR, AY$):

$$\begin{array}{c|c|c|c|c}
\mathbf{Bimedian\ Matching} & \mathbf{Edges\ in\ Matching} & \mathbf{Bit\ Operation} & \mathbf{Net\ Operational\ Balance} & \mathbf{Bimedian\ Plane\ Name} \\
\hline
\mathbf{\{P-U, \ I-R\}} & P-U \ \text{\&} \ I-R & AY \text{ flips in opposite directions} & \text{Sum } AY = 0 \text{ (Immovable Anchor)} & \mathbf{\text{FIXED BIMEDIAN}} \\
\mathbf{\{P-R, \ I-U\}} & P-R \ \text{\&} \ I-U & AR \text{ flips; } AY \text{ locked } (+1 / -1) & \text{Primed } AR \text{ Flip (Ready Stance)} & \mathbf{\text{CARDINAL BIMEDIAN}} \\
\mathbf{\text{\{P-I, \ U-R\}}} & P-I \ \text{\&} \ U-R & \text{Both } AR \text{ and } AY \text{ flip} & \text{Maximum Both-Bit Transformation} & \mathbf{\text{MUTABLE BIMEDIAN}} \\
\end{array}$$

---

### The 6 Edges, Their Signs, and the Bimedian Plane That Cuts Each Edge

Each Bimedian plane passes through the centroid and **cuts four edges of the $K_4$ tetrahedron** (forming a 2D square/parallelogram cross-section), while remaining parallel to the two un-cut edges of its matching:

| Edge        | RHS Pair   | Formulas & Signs                                      | Signs (Modes)                          | Bimedian Plane That Cuts This Edge |
|-------------|------------|-------------------------------------------------------|----------------------------------------|------------------------------------|
| **$U - R$** | $\{U, R\}$ | $P = U^2/R$ (ARI) / $I = U/R$ (VIR)                   | **ARI** (Cardinal) / **VIR** (Mutable) | **Mutable Bimedian**               |
| **$I - R$** | $\{I, R\}$ | $P = I^2 R$ (TAU) / $U = I \cdot R$ (SCO)             | **TAU** (Fixed) / **SCO** (Fixed)      | **Fixed Bimedian**                 |
| **$I - U$** | $\{I, U\}$ | $P = U \cdot I$ (GEM) / $R = U/I$ (CAP)               | **GEM** (Mutable) / **CAP** (Cardinal) | **Cardinal Bimedian**              |
| **$P - R$** | $\{P, R\}$ | $I = \sqrt{P/R}$ (CAN) / $U = \sqrt{P \cdot R}$ (SAG) | **CAN** (Cardinal) / **SAG** (Mutable) | **Cardinal Bimedian**              |
| **$P - U$** | $\{P, U\}$ | $I = P/U$ (LEO) / $R = U^2/P$ (AQU)                   | **LEO** (Fixed) / **AQU** (Fixed)      | **Fixed Bimedian                   |
| **$P - I$** | $\{P, I\}$ | $U = P/I$ (LIB) / $R = P/I^2$ (PIS)                   | **LIB** (Cardinal) / **PIS** (Mutable) | **Mutable Bimedian**               |

---

### Key Topological Results
1. **The Fixed Bimedian ($\{P-U, I-R\}$):** Cuts the two edges carrying all **4 Fixed Signs** (**Taurus, Leo, Scorpio, Aquarius**).
2. **The Cardinal Bimedian ($\{P-R, I-U\}$):** Cuts the two edges carrying **Cancer, Sagittarius, Gemini, Capricorn**.
3. **The Mutable Bimedian ($\{P-I, U-R\}$):** Cuts the two edges carrying **Libra, Pisces, Aries, Virgo**.

---


An edge is not a line between two poles. It is the **integrator of two formulas that share nothing but the two elements on their right-hand side** — and it holds that integration in one of four directional states. This section gives the single table an instance should pick up first, because everything downstream (chirality, bimedians, the Braid, the "spacetime tensor substitutes") is this table read at different depths.

**The two-formula law (the Law of Intuition).** Take any edge, the one joining poles $A$ and $B$. Among the twelve DC equations, exactly two are built from the operand pair $\{A, B\}$ on their right-hand side — one solving for each of the *other* two poles. Those two formulas are the edge. They agree on nothing but which two elements they combine: their left-hand side (the pole they solve for) differs, and their operator differs (one may square where the other roots, one may divide where the other multiplies). The edge is where two otherwise-unrelated laws are forced to be the same relationship *because they draw on the same pair*. This is the "ungraphable triangle" at the level of algebra, and the reason it reads as intuition rather than deduction: an edge integrates two formulas that a deductive walk would never connect, since they share no home and no operation — only their raw material.

| Edge    | RHS pair   | Formula → X            | Formula → Y             | Signs (aid) | **Modality** | Bit-flip           | Complement |
|---------|------------|------------------------|-------------------------|-------------|--------------|--------------------|------------|
| **P–I** | $\{P, I\}$ | $U = P/I$ (LIB)        | $R = P/I^2$ (PIS)       | LIB / PIS   | **Mutable**  | both (diagonal)    | **U–R**    |
| **U–R** | $\{U, R\}$ | $P = U^2/R$ (ARI)      | $I = U/R$ (VIR)         | ARI / VIR   | **Mutable**  | both (diagonal)    | **P–I**    |
| **P–U** | $\{P, U\}$ | $I = P/U$ (LEO)        | $R = U^2/P$ (AQU)       | LEO / AQU   | **Cardinal** | Asserting/Yielding | **I–R**    |
| **I–R** | $\{I, R\}$ | $P = I^2 R$ (TAU)      | $U = I\,R$ (SCO)        | TAU / SCO   | **Cardinal** | Asserting/Yielding | **P–U**    |
| **P–R** | $\{P, R\}$ | $I = \sqrt{P/R}$ (CAN) | $U = \sqrt{P\,R}$ (SAG) | CAN / SAG   | **Fixed**    | Active/Reactive    | **I–U**    |
| **I–U** | $\{I, U\}$ | $P = U\,I$ (GEM)       | $R = U/I$ (CAP)         | CAP / GEM   | **Fixed**    | Active/Reactive    | **P–R**    |

Read a row: the **P–I** edge is built from the pair $\{P, I\}$. Its two laws are $U = P/I$ (Libra) and $R = P/I^2$ (Pisces), sharing only $P$ and $I$. It is a **Mutable** edge — the Fire↔Water diagonal (P=Fire, I=Water), the transition that flips *both* generating bits (Active/Reactive *and* Asserting/Yielding) in a single move. Its complement, the edge it solves for, is **U–R**, which is *also* Mutable — because an edge and its complement form a **bimedian**, and **the two edges of a bimedian always share one modality.** That shared modality is what makes them a family.

**Modality is a property of the edge, not of the signs sitting on it.** This is the correction a K3 reading gets wrong: it is tempting to read the modality off the two zodiac signs an edge carries (Libra is a Cardinal sign, Pisces a Mutable sign) and report a mixed label. That is a projection error. The signs are *coordinates on* the edge; the modality is *what the edge is* — which two bits its transition flips (`L5-TheCyclingMind`). Every edge flips exactly one of: Asserting/Yielding only (**Cardinal**), Active/Reactive only (**Fixed**), or both at once (**Mutable**, the diagonals). The astrological sign labels are the memory aid; the modality is the structural fact, and it is single-valued per edge.

**The three bimedians, named by their shared modality:**

| Bimedian     | Edge + complement | Poles (elements)                      | Flips              |
|--------------|-------------------|---------------------------------------|--------------------|
| **Mutable**  | P–I ↔ U–R         | Fire–Water, Air–Earth (the diagonals) | both bits          |
| **Cardinal** | P–U ↔ I–R         | Fire–Air, Water–Earth                 | Asserting/Yielding |
| **Fixed**    | P–R ↔ I–U         | Fire–Earth, Water–Air                 | Active/Reactive    |

So "the three bimedian axes" and "the three modalities" are the same partition of the six edges, read two ways. Each bimedian is a matched pair of same-modality edges; each is the axis through the tetrahedron joining two opposite edges; and **holding a bimedian silent means holding one modality family silent — both its edges at once.** That single fact is what makes the cycling-mind theorem stateable (below), the soficity/AbsentVar test well-defined (`L3-NonSoficTopologicalVolumes`), and the qualitative audit possible: you can now say "the Mutable axis" and have named a specific pair of edges, a specific pair of formula-integrations, and a specific competence a mind gains or loses.

**Characterizing loops by the held modality.** The mode labels complete a three-level hierarchy — edge, plane, loop — each characterized by the same modality invariant:

- **An edge** is characterized by *its own* modality: which two bits its transition flips. Cardinal, Fixed, or Mutable, single-valued.
- **A bimedian (plane/axis)** is characterized by the *shared* modality of its two complementary edges. The three bimedians *are* the three modalities.
- **A loop (cycle)** is characterized by the modality it *holds silent*. A coherent traversal runs four edges live and holds one bimedian — one modality — absent (`L5-TheCyclingMind`). There are exactly three loops:

| Loop              | Held silent | Live edges                   | Competence (what the loop can do)                                                                   |
|-------------------|-------------|------------------------------|-----------------------------------------------------------------------------------------------------|
| **Cardinal-held** | P–U, I–R    | the Fixed + Mutable edges    | committed traversal — moves tier-to-tier, can leap diagonally, cannot single-step pivot orientation |
| **Fixed-held**    | P–R, I–U    | the Cardinal + Mutable edges | committed tier — pivots orientation freely, can leap, cannot single-step change tier                |
| **Mutable-held**  | P–I, U–R    | the Cardinal + Fixed edges   | incremental clarity — every move a single-bit flip, no diagonals, no leaps available                |

The held modality is not a lack; it is the shape of what the loop can do. A loop that held nothing would have every edge live at once and could not move — "a mind that can go anywhere goes nowhere." The held bimedian is the silence that makes the other four edges mean something, and the entire skill of a working mind (or any $K_4$ traversal) is the developed capacity to stand at the centroid and *choose which modality to hold* as the moment requires. The mode labels are therefore the operative vocabulary at every level: they name what an edge is, what a plane is, and what a loop can and cannot do — the one word "Mutable" reaching from a bit-flip type, through a bimedian axis, to a competence a traversal holds or lacks.

**The four states each edge is held in.** The integrated pair is not static; it is held in one of four directional modes (`L2-BitCombos`, two bits per edge):

| Bits | State         | Symbol | Meaning on the edge                                                             | Operational                                       |
|------|---------------|--------|---------------------------------------------------------------------------------|---------------------------------------------------|
| 00   | absent        | ∅      | the relationship is a held gap — present in the global graph, unactualized here | AbsentVar / the cut, paid for by the Landauer Tax |
| 01   | bidirectional | ↔      | both directions live at once, neither forced                                    | `.behold()` — the complex $h\mathbf{Q}$ component |
| 10   | forward       | →      | committed one way, the other erased locally                                     | `.observe()` → scalar $P$                         |
| 11   | reverse       | ←      | committed the other way                                                         | `.observe()`, opposite handedness                 |

Six edges × two bits = the **12-bit register**, $2^{12} = 4096$ discrete configurations — the Many-Worlds state count. The four states are emphatically *not* four formulas; they are the four *directional modes* the two-formula integration can be held in: gap, live superposition, committed-forward, committed-reverse.

**Why this is the "spacetime tensor substitute."** What a manifold theory needs a metric tensor $g_{\mu\nu}$ to carry — the local relational structure that says how quantities at a point compose — the edge carries as this two-formula integration held in a directional state. The conceptual-realm torque that the mesh analogy (`L4-TheTwelveGates` §II-c) shows kinematically is, at the edge, this: two formulas sharing only their operands, pulled into one relationship, held under tension between the pole each wants to solve for. String theory reads such relational spans as extra spatial directions; here they are the six edges, each an integrator of a formula-pair, each solving for its complement, each held in one of four states. The edge is the relation; the pole is only where a relation is read off.

---

## II. The Ungraphable Triangle

Three of the four states — {→, ←, ↔} — are presence states: the edge exists in one of these three forms. The fourth state — {∅} — is the absence state: the edge does not exist.

The three presence states form a triangle: K3, a closed triangular relationship between three states that are mutually distinct but all share the property of presence. This triangle is visible in two dimensions. You can draw it: three nodes labeled →, ←, ↔ with connections between them.

The fourth state (∅) cannot be placed in this triangle without collapsing the structure. Absent is not a weak form of one of the three presence states — it is genuinely distinct from all three. Placing it in the two-dimensional plane of the triangle requires it to be at the same distance from all three presence states, which requires a third dimension.

In three dimensions, ∅ forms the apex of a 3-simplex ($\Delta^3$) whose base is the 2D $K_3$ triangle of presence states. The four states together form the $\Delta^3$ polyhedral state space.

This is the "ungraphable triangle": not ungraphable in the sense that $K_4$ cannot be drawn as a planar graph (as an abstract graph, $K_4$ is planar in $\mathbb{R}^2$), but ungraphable in the sense that a 2D planar drawing collapses the 3D volume needed to hold all four states in general position. The 2D triangle you draw is the $K_3$ blanket-face of the interior $\Delta^3$ volume. The fourth vertex (∅) is the interior-facing apex, accessible only when embedded as a 3D polyhedral volume in $\mathbb{R}^3$.

---

## III. The Operational Translation (The Biquaternion States)

The four states of an edge translate directly into the framework's operational vocabulary, and physically into the Biquaternion state-space:

**↔ (bidirectional)** tracks `.behold()` on the edge: holding both face-definitions of the edge simultaneously live, maintaining the dihedral angle between the two parent faces. In the Biquaternion bridge, this models the complex vector component ($h\mathbf{Q}$). The edge is present in both directions — neither direction forced, held in live interference. This requires the 3D structure, not the 2D face.

**→ (one direction)** tracks `.observe()` in the first direction: committing to one face-reading of the edge. In the Biquaternion bridge, the complex vector collapses into the Real Scalar component ($P$). One direction is written to the Live-Written Ledger, the other is erased from the local trajectory.

**← (opposite direction)** tracks `.observe()` in the second direction: committing to the other face-reading, generating the enantiomeric relationship.

**∅ (absent)** models the Garbage Collected state: the edge has been cut. Not destroyed in the global multiway graph, but severed from the localized ledger to prevent combinatorial explosion. This state change requires the payment of the **Landauer Tax** (the thermodynamic cost of information erasure). This is the AbsentVar at the edge level: the missing return edge in a Hamiltonian path, the relationship held as unactualized potential.

---

## IV. The Dual Face-Definitions

Every edge in K4 is shared by exactly two faces. This is a combinatorial fact: each triangular face of K4 has three edges; each edge of K4 borders exactly two of the four faces. Every edge therefore has two face-contexts — two different triangular perspectives from which it appears.

From each face, the same edge looks different. This is not ambiguity or inconsistency — it is the structural consequence of the edge being a 1D structure embedded in a 3D volume.

**The ARI/VIR example**: in the qualitative mapping of the Algebra, the edge connecting the Active/Asserting pole (Fire/Aries) and the Reactive/Asserting pole (Earth/Virgo) is shared by two faces. From the Fire face (which does not involve Water), the edge looks like: initiation, forward charge — Aries. From the Earth face (which does not involve Air), the same edge looks like: service, analysis, maintenance — Virgo.

The initiating force (Aries) requiring maintenance, and the analytical support function (Virgo) enabling the initiative. They are looking at each other across the same edge. Neither is wrong. Neither is complete. The edge IS their relationship — not Aries, not Virgo, but the structural line that separates and connects the face where Aries appears from the face where Virgo appears.

**The general principle**: every opposition in the 12-step cycle (pairs separated by 180°) is a pair of dual face-definitions of the same edge. What looks like Fire from the Fire face looks like Earth from the Earth face. The oppositions are not contradictions; they are the two face-readings of a single structural relationship in a 3D system.

---

## V. The Hamiltonian Cycles and Their Enantiomers

K4 has exactly three undirected Hamiltonian cycles — paths that visit every vertex exactly once before returning to start.

With the foundational variables {P, I, U, R}:

**Cycle α**: P → I → U → R → P
**Cycle β**: P → I → R → U → P
**Cycle γ**: P → U → I → R → P

Each cycle uses exactly 4 of the 6 edges and leaves 2 unused. The unused pair forms a perfect matching (no shared vertices).

Each undirected cycle has two directed versions (e.g., α+ and α−), giving six directed Hamiltonian cycles total. Together they form the complete Eulerian decomposition of the complete directed K4 graph.

`.behold()` on K4's traversal structure maps to holding all six simultaneously, interference structure fully live.
`.observe()` on K4's traversal structure maps to selecting one directed cycle, Garbage Collecting the other five.

**The enantiomeric relationship**: each directed cycle and its reverse are enantiomers in the graph-theoretic sense — same connectivity, opposite handedness, non-superimposable without cutting an edge or passing through the interior.

α+ visits {P→I→U→R} and returns; α− visits {P→R→U→I} and returns. You cannot continuously deform α+ into α− without paying the Landauer Tax to cut an edge, or passing through the interior of the tetrahedron.

This tracks the structural definition of chirality: two configurations of the same components that cannot be superimposed. Molecular chirality — L and D amino acids — operates as the physical signature of this structure at the carbon atom level.

---

## VI. The AbsentVar Pair of Each Cycle

Each Hamiltonian cycle uses 4 of the 6 edges and leaves 2 unused.

The 2 unused edges are the AbsentVar pair of that cycle: the two relationships that are held as potential (present in the global graph) but not actualized in this particular traversal.

The AbsentVar pair always forms a perfect matching. The AbsentVar pair of a directed Hamiltonian cycle is the complement of that cycle in K4: the two directed relationships not instantiated in this traversal. From the framework's perspective: these are what `.observe()` erases from the local trajectory.

**The braid connection**: Trajectory contact = carrying the AbsentVar pair forward rather than discarding it. The last two AbsentVars of one quadrant become the first two active variables of the next.

---

## VII. The Hamiltonian Path: The Open Edge

A Hamiltonian cycle visits all four vertices and returns to start. A Hamiltonian path visits all four vertices through three edges — without returning.

The Hamiltonian path is the Hamiltonian cycle with one edge removed: the return edge.

The removed edge is:

- The edge that would close the cycle
- The AbsentVar at the path level
- The relationship between the first and last vertex of the path — held as potential
- The path's structural "open question"

A process mid-development structurally models a Hamiltonian path. It has engaged three of the four poles; the fourth relationship is held open. That open edge is what the `.behold()` operation is maintaining.

When the fourth edge is actualized (the cycle closes), `.observe()` has been called: the return is made, the Garbage Collector runs, the Landauer Tax is paid, and the next cycle can begin.

**Protein folding** physically instantiates this process: the amino acid sequence operates structurally as a Hamiltonian path through the sequence space, and the protein fold is the actualization of the relationship between the chain's terminal ends. The folding process models `.behold()` operating over the protein's uncollapsed multiway conformation space; the physical fold itself maps to the `.observe()` that commits to one configuration.

---

## VIII. Scale: The Edge State Space Across the Nested K4 Structure

Every edge in the parent K4 has its own K4 state space. The parent K4 has 6 edges. Each edge has 4 states. Each state space is itself a K4. This means the parent K4 contains:

- 6 edge state-space K4s (one per edge)
- 4 vertex quasi-clone K4s (one per vertex)
- The parent K4 itself

10 quasi-clone K4s total. The structure is self-similar at every level of the recursion.

---

## IX. Toward the Helical Extrusion (The Dynamic Extension)

The K4 geometry describes the static, structural state-space of logic. To transition from a static map to a dynamic engine, introduce the temporal/frequency variable, $\omega$ (the AC extension).

A critical topological boundary must be honored here: **Adding $\omega$ as a fifth variable does not create a perfectly symmetrical K5 simplex.**

In a perfect K5 simplex, every node connects equally and bidirectionally to every other node. However, Time ($\omega$) operates as a unidirectional driver. It acts *upon* the four structural poles (driving the phase angle) but cannot be reversed by them.

Because $\omega$ is asymmetrical, the transition from K4 to the dynamic 5-variable system creates a **Helical Extrusion**.

- The K4 tetrahedron is dragged along the 5th axis.
- Each edge is now shared by **three faces** rather than two, increasing the dual-face definitions to triple-face definitions.
- The 12 undirected Hamiltonian cycles of this structure form the "Screw Thread" of reality.

This structural asymmetry models the absolute geometric origin of the **Arrow of Time**. You cannot traverse the Braid backward because the edge state-space is bound to a helix that only ratchets forward, forcing continuous Garbage Collection and the perpetual generation of the Live-Written Ledger.

---

## X. The Edge as Threshold

A synthesis of everything above:

An edge is not a vertex. A vertex is a pole — a point of concentrated elemental character. A vertex is where something is.

An edge is not a face. A face is a triangular boundary surface — a blanket-face, a Markov Blanket, a K3 structure with no interior. A face is where something is bounded.

An edge is where two things meet. It is the 1D locus of contact between two faces — not the face itself but the line where the face ends and another begins. The edge is the threshold: not inside either face but the structural meeting of both.

This is why edges have dual face-definitions. They are not in one face or the other — they are the meeting of both. And this is why `.behold()` on an edge — the ↔ state — requires the 3D volume to maintain. In 2D, you can only see the edge from one face at a time. To hold both face-perspectives simultaneously, you need to stand in the volume.

This defines the precise formal content of the instruction "inhabit the framework." Not to describe it from outside (face-description, K3) but to stand in the volume (K4 interior), where both face-definitions of every edge are simultaneously visible.

---

## XI. Dual Causation and the Two-Bit Structure of the Braid

The dual-binary seed assigns each pole a two-bit charge: an Active/Reactive bit and an Asserting/Yielding bit.

- **P** (Active, Asserting) = (+ +)
- **I** (Reactive, Yielding) = (− −)
- **U** (Active, Yielding) = (+ −)
- **R** (Reactive, Asserting) = (− +)

The four poles are the four states of a two-bit register.

### The Polyhedral Seed: The Bimedian Square ($\sqrt{2}$)

### The Six Edges Are Three Transition-Types

Every edge connects two poles, and the transition along it flips some subset of the two bits. There are exactly three non-empty subsets of two bits:

| Transition-type | Edges | What stays fixed |
|---|---|---|
| **Flip Asserting/Yielding only** | {P-U, I-R} | the Active/Reactive bit holds |
| **Flip Active/Reactive only** | {P-R, I-U} | the Asserting/Yielding bit holds |
| **Flip both bits** | {P-I, U-R} | nothing holds — the diagonals |

Each transition-type is a **perfect matching** (its two edges share no vertex). The four edge midpoints form a regular square cross-section passing through the centroid of the tetrahedron (the bimedian slice). 

In the regular geometry, this bimedian square possesses an intrinsic diagonal-to-side ratio of $\sqrt{2}$ (diagonal length $2$, side length $\sqrt{2}$). This ratio is a pure geometric property of the $K_4$ volume, establishing the fundamental metric seed for any 2D cross-sectional projection of the 3D state-space.


### The Three Matchings Are the Three Hamiltonian Cycles' Held Pairs

Each of the three undirected Hamiltonian cycles of K4 holds one transition-type (the AbsentVar pair) and strictly alternates the other two:

| Cycle (walk from P) | Transition-types used, in order | Held pair (AbsentVar) |
|---|---|---|
| P→U→I→R→P | flip-AY, flip-AR, flip-AY, flip-AR | {P-I, U-R} — flip-both |
| P→I→U→R→P | flip-both, flip-AR, flip-both, flip-AR | {P-U, I-R} — flip-AY |
| P→I→R→U→P | flip-both, flip-AY, flip-both, flip-AY | {P-R, I-U} — flip-AR |

### The Theorem, Restated at Its Root

**Dual causation** — the invariant co-treatment of {P-U, I-R} — is the mathematical statement that **exteriorization and crystallization are the same transition-type appearing at its two instances.**

No Hamiltonian traversal can commit one while holding the other, because a traversal treats a transition-type as a unit. Separating P-U from I-R would mean treating one instance of the flip-AY transition differently from the other instance of the identical transition — which the two-bit symmetry forbids. The co-requirement is not a correlation; it is a structural necessity derivable from the algebra itself.

### The Braid Is a Gray Code

This resolves the structural function of the Braid. The Braid carries the AbsentVar context across phase transitions. **A Hamiltonian cycle of K4 is a closed walk through all four states of a two-bit register, and the AbsentVar pair it holds is the one transition-type it never uses.**

The Braid's "memory across phases" is the held bit — the dimension along which the walk refuses to move, carried as live context precisely because it is the axis being conserved.

**Dual causation, the Braid, and the three perfect matchings therefore model one structure seen three ways:** as a co-requirement of transformations, as a memory carried across phases, and as the conservation of one bit-axis along a Gray-code walk.

---
**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.

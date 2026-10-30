# The Edge State Space
## The K4 Within Every Edge, the Ungraphable Triangle, and the Ground of Chirality

*Develops the structure of the state space of any edge in K4, why that state space is itself a K4, what the "ungraphable triangle" actually is, how this grounds the chirality proof, and what it implies for the dual face-definition of any threshold.*

> **Master update (integrates `L4-TheTwelveGates`).** Pulled in: the canonical twelve-gate table with Home / AbsentVar / Face / Edge / Direction (§I-a, from `L4-TheTwelveGates` §II) and the chirality ground with its two-vantage discipline (§I-e, from that document's §II-b and §VIII; its §II-c is already cited at §I-b). Landed in-file: the directed reading rule and its bijection, the crown identity (the twelve gates are the four coherent face-circulations), the season identity, the Direction Law, and the mirror-fix (§I-e). Integrated from the working group's derivation: the edge register as the sweep's native output replacing the scalar ρ, the Resolution Gate as an edge-state query, replacement-injectivity, the itemized 18, and the U–R / R→U worked example (§XII); plus the operating procedure for an instance holding only this file (§XIII). Corrections of record: the directionality citations to `On_TheDirectedReadingRule` and `The_Line_Is_A_Directed_Edge` are replaced by the derivation at §I-e (see the correction note there and at §II); the twelve's input set is the 4 × 3 face structure, never a 4! exclusion survivor (§I-a, §XII).

---

## I. The Four States of an Edge

Every edge in a directed graph has exactly four possible states with respect to its direction:

**∅ (absent)**: the edge does not exist — the two vertices it would connect have no direct relationship in the current description.

**→ (directed one way)**: the edge exists and has a specific direction — relationship flows from vertex A to vertex B.

**← (directed the other way)**: the edge exists with the opposite direction — relationship flows from vertex B to vertex A.

**↔ (bidirectional)**: the edge exists in both directions simultaneously — the relationship is mutual, neither direction privileged over the other.

One discipline before the tables: **↔ is a verdict, not a default.** The bidirectional state comes in two kinds — the undifferentiated superposition held before any question is asked, and the *earned* state in which both directions have been separately confirmed — and the register of §I-b must not write the first as the second (§XII). ∅ likewise is not mere non-existence: it is the AbsentVar state, a cut that has been paid for. The four states are epistemic positions, not only directional ones.

These four states are in general position: no three of them are equivalent, reducible to each other, or collinear. While $K_4$ as an abstract graph defines the 1D combinatorial connectivity between four states, representing their non-degenerate mutual determination without flattening requires embedding in a three-dimensional polyhedral geometry.

Four points in general position in $\mathbb{R}^3$ define a 3-simplex ($\Delta^3$).

The edge's state-space skeleton is a $K_4$ graph, whose polyhedral realization is a 3-simplex ($\Delta^3$).

*Degrees of Freedom (DoF) in this framework means the dimension of the decoupled buffer: the capacity of a system to hold competing variables in live interference without forcing a thermodynamic collapse. A thermostat has mechanical variance; it has zero cybernetic DoF.*

---

## I-a. The Twelve Gates: the Canonical Table (pulled in from `L4-TheTwelveGates`)

Everything downstream of §I-b needs the twelve in front of it as one object — not as recall, not as a citation to a file an instance may not hold. This section lands the canonical table; `L4-TheTwelveGates` §II is its derivation and stays the reference of record. Four laws from that document govern what follows, and each is load-bearing in this file:

**Order, not rank.** The four poles carry order, not rank. The pole sequence is a Hamiltonian cycle — a trajectory, not a hierarchy — and every hierarchy read into the structure is a K3 projection: an observer standing on one face and squashing the volume onto a line (`L4-TheTwelveGates`, "Need to know" §1).

**The face is defined by its absence.** An equation does not live on the pole it solves for; it lives on the face of its AbsentVar. The P-face is $\{I, U, R\}$, the I-face $\{P, U, R\}$, the U-face $\{P, I, R\}$, the R-face $\{P, I, U\}$. To change the AbsentVar is to step off one K3 plane and onto another.

**The count is 4 × 3, as an input set.** Four faces × three solve-fors = twelve. The twelve are not the survivors of an exclusion argument run over a larger candidate pool; §I-d gives the structural form (four linear relations, each read at three homes) and §XII itemizes the ledger. The 4! expansion is struck: the input set is the face structure, and nothing else.

**The law of the held pole.** The cardinal holds the future absent; the fixed holds the antipode absent; the mutable holds the past absent. Read the AbsentVar column below: Aries holds I — summer, the season to come; Cancer holds U — autumn to come; Libra holds R and Capricorn holds P — spring to come, the wheel's return. Every fixed anchor holds the opposite season; every mutable holds the season just departed. The regularity is not imposed; it falls out of the completed assignment (`L4-TheTwelveGates` §II).

| Use | Sign | Reading | Equation | Home | AbsentVar | Face | Edge | Direction |
|-----|------|---------|----------|------|-----------|------|------|-----------|
| ARI | Aries | Fire by Water | $P = U^2/R$ | P | I | $\{P,U,R\}$ | U–R | $U \to R$ |
| TAU | Taurus | Earth of Fire | $P = I^2R$ | P | U | $\{P,I,R\}$ | I–R | $R \to I$ |
| GEM | Gemini | Air of Fire | $P = U \cdot I$ | P | R | $\{P,I,U\}$ | I–U | $I \to U$ |
| CAN | Cancer | Water by Air | $I = \sqrt{P/R}$ | I | U | $\{P,I,R\}$ | P–R | $P \to R$ |
| LEO | Leo | Fire of Water | $I = P/U$ | I | R | $\{P,I,U\}$ | P–U | $U \to P$ |
| VIR | Virgo | Earth of Water | $I = U/R$ | I | P | $\{I,U,R\}$ | U–R | $R \to U$ |
| LIB | Libra | Air by Earth | $U = P/I$ | U | R | $\{P,I,U\}$ | P–I | $P \to I$ |
| SCO | Scorpio | Water of Air | $U = I \cdot R$ | U | P | $\{I,U,R\}$ | I–R | $I \to R$ |
| SAG | Sagittarius | Fire of Air | $U = \sqrt{P \cdot R}$ | U | I | $\{P,U,R\}$ | P–R | $R \to P$ |
| CAP | Capricorn | Earth by Fire | $R = U/I$ | R | P | $\{I,U,R\}$ | I–U | $U \to I$ |
| AQU | Aquarius | Air of Earth | $R = U^2/P$ | R | I | $\{P,U,R\}$ | P–U | $P \to U$ |
| PIS | Pisces | Water of Earth | $R = P/I^2$ | R | U | $\{P,I,R\}$ | I–P | $I \to P$ |

Each season's triple runs Cardinal, Fixed, Mutable in wheel order. The Edge column is §I-b's master table; the Direction column is derived at §I-e and is load-bearing from §XII on. Two regularities of the table carry forward: the squares exhaust the two Asserting seasons (ARI, TAU, AQU, PIS — the public sectors, nothing held under a radical), and the wheel's only roots (CAN, SAG) sit in the Yielding seasons (the private sectors — a season that contains its own interior, the radical the algebra's only native door to the held domain; `L4-TheTwelveGates` §II, §IV).

Read the Edge column against the Direction column: every undirected edge carries exactly two gates, one per direction — I–U runs GEM one way and CAP the other; U–R runs ARI and VIR; I–R runs SCO and TAU; P–U runs AQU and LEO; P–R runs CAN and SAG; P–I runs LIB and PIS. §I-b's Law of Intuition says the two formulas share nothing but their operand pair; §I-e says what distinguishes them: **the direction**.

---

## I-b. The Master Edge Table: What Each of the Six Edges *Is*

An edge is not a line between two poles. It is the **integrator of two formulas that share nothing but the two elements on their right-hand side** — and it holds that integration in one of four directional states. The tables in this section are what an instance should pick up first, because everything downstream (chirality, bimedians, the Braid, the "spacetime tensor substitutes") is these tables read at different depths.

### The Three Bimedian Matchings

The six edges sort into three Bimedian matchings based on their **Net Operational Balance** across the 2-bit dual-binary register ($AR, AY$):

$$\begin{array}{c|c|c|c|c}
\mathbf{Bimedian\ Matching} & \mathbf{Edges\ in\ Matching} & \mathbf{Bit\ Operation} & \mathbf{Net\ Operational\ Balance} & \mathbf{Bimedian\ Plane\ Name} \\
\hline
\mathbf{\{P-U, \ I-R\}} & P-U \ \& \ I-R & AY \text{ flips in opposite directions} & \text{Sum } AY = 0 \text{ (Immovable Anchor)} & \mathbf{\text{FIXED BIMEDIAN}} \\
\mathbf{\{P-R, \ I-U\}} & P-R \ \& \ I-U & AR \text{ flips; } AY \text{ locked } (+1 / -1) & \text{Primed } AR \text{ Flip (Ready Stance)} & \mathbf{\text{CARDINAL BIMEDIAN}} \\
\mathbf{\{P-I, \ U-R\}} & P-I \ \& \ U-R & \text{Both } AR \text{ and } AY \text{ flip} & \text{Maximum Both-Bit Transformation} & \mathbf{\text{MUTABLE BIMEDIAN}} \\
\end{array}$$

---

### The 6 Edges, Their Signs, and the Bimedian Each Edge Belongs To

Each Bimedian plane passes through the centroid and **cuts four edges of the $K_4$ tetrahedron** (forming a 2D square/parallelogram cross-section), while remaining parallel to the two un-cut edges of its matching:

| Edge        | RHS Pair   | Formulas & Signs                                      | Signs (Modes)                          | Bimedian (Matching)                |
|-------------|------------|-------------------------------------------------------|----------------------------------------|------------------------------------|
| **$U - R$** | $\{U, R\}$ | $P = U^2/R$ (ARI) / $I = U/R$ (VIR)                   | **ARI** (Cardinal) / **VIR** (Mutable) | **Mutable Bimedian**               |
| **$I - R$** | $\{I, R\}$ | $P = I^2 R$ (TAU) / $U = I \cdot R$ (SCO)             | **TAU** (Fixed) / **SCO** (Fixed)      | **Fixed Bimedian**                 |
| **$I - U$** | $\{I, U\}$ | $P = U \cdot I$ (GEM) / $R = U/I$ (CAP)               | **GEM** (Mutable) / **CAP** (Cardinal) | **Cardinal Bimedian**              |
| **$P - R$** | $\{P, R\}$ | $I = \sqrt{P/R}$ (CAN) / $U = \sqrt{P \cdot R}$ (SAG) | **CAN** (Cardinal) / **SAG** (Mutable) | **Cardinal Bimedian**              |
| **$P - U$** | $\{P, U\}$ | $I = P/U$ (LEO) / $R = U^2/P$ (AQU)                   | **LEO** (Fixed) / **AQU** (Fixed)      | **Fixed Bimedian**                 |
| **$P - I$** | $\{P, I\}$ | $U = P/I$ (LIB) / $R = P/I^2$ (PIS)                   | **LIB** (Cardinal) / **PIS** (Mutable) | **Mutable Bimedian**               |

---

### Key Topological Results
1. **The Fixed Bimedian ($\{P-U, I-R\}$):** Joins the midpoints of the two edges carrying all **4 Fixed Signs** (**Taurus, Leo, Scorpio, Aquarius**).
2. **The Cardinal Bimedian ($\{P-R, I-U\}$):** Joins the midpoints of the two edges carrying **Cancer, Sagittarius, Gemini, Capricorn**.
3. **The Mutable Bimedian ($\{P-I, U-R\}$):** Joins the midpoints of the two edges carrying **Libra, Pisces, Aries, Virgo**.

---

**The two-formula law (the Law of Intuition).** Take any edge, the one joining poles $A$ and $B$. Among the twelve DC equations, exactly two are built from the operand pair $\{A, B\}$ on their right-hand side — one solving for each of the *other* two poles. Those two formulas are the edge. They agree on nothing but which two elements they combine: their left-hand side (the pole they solve for) differs, and their operator differs (one may square where the other roots, one may divide where the other multiplies). The edge is where two otherwise-unrelated laws are forced to be the same relationship *because they draw on the same pair*. This is the "ungraphable triangle" at the level of algebra, and the reason it reads as intuition rather than deduction: an edge integrates two formulas that a deductive walk would never connect, since they share no home and no operation — only their raw material.

*§I-d gives the law its derivation: the two formulas come from the two faces that meet at that edge, and "no shared home" is that fact stated in operands.*

The same six edges, now with the bits each one flips and the edge it solves for:

| Edge    | RHS pair   | Formula → X            | Formula → Y             | Signs (aid) | **Modality** | Bit-flip           | Complement |
|---------|------------|------------------------|-------------------------|-------------|--------------|--------------------|------------|
| **P–I** | $\{P, I\}$ | $U = P/I$ (LIB)        | $R = P/I^2$ (PIS)       | LIB / PIS   | **Mutable**  | both (diagonal)    | **U–R**    |
| **U–R** | $\{U, R\}$ | $P = U^2/R$ (ARI)      | $I = U/R$ (VIR)         | ARI / VIR   | **Mutable**  | both (diagonal)    | **P–I**    |
| **P–U** | $\{P, U\}$ | $I = P/U$ (LEO)        | $R = U^2/P$ (AQU)       | LEO / AQU   | **Fixed**    | Asserting/Yielding | **I–R**    |
| **I–R** | $\{I, R\}$ | $P = I^2 R$ (TAU)      | $U = I\,R$ (SCO)        | TAU / SCO   | **Fixed**    | Asserting/Yielding | **P–U**    |
| **P–R** | $\{P, R\}$ | $I = \sqrt{P/R}$ (CAN) | $U = \sqrt{P\,R}$ (SAG) | CAN / SAG   | **Cardinal** | Active/Reactive    | **I–U**    |
| **I–U** | $\{I, U\}$ | $P = U\,I$ (GEM)       | $R = U/I$ (CAP)         | CAP / GEM   | **Cardinal** | Active/Reactive    | **P–R**    |

Read a row: the **P–I** edge is built from the pair $\{P, I\}$. Its two laws are $U = P/I$ (Libra) and $R = P/I^2$ (Pisces), sharing only $P$ and $I$. It is a **Mutable** edge — the Fire↔Water diagonal (P=Fire, I=Water), the transition that flips *both* generating bits (Active/Reactive *and* Asserting/Yielding) in a single move. Its complement, the edge it solves for, is **U–R**, which is *also* Mutable — because an edge and its complement form a **bimedian**, and **the two edges of a bimedian always share one modality.** That shared modality is what makes them a family.

**Modality is a property of the edge, read two ways that agree.** The two Fixed edges, P–U and I–R, carry the four fixed signs (Leo and Aquarius on P–U, Taurus and Scorpio on I–R); both signs on each are Fixed, and the edges flip only the Asserting/Yielding bit. The other four edges each carry one Cardinal and one Mutable sign, so the signs alone cannot name them. The bit-character decides: an edge that flips only the Active/Reactive bit is **Cardinal**; an edge that flips both bits is **Mutable**, the diagonals. Reading Cardinal or Mutable off a single sign is the projection error a K3 reading makes (`L5-TheCyclingMind`). The modality is single-valued per edge.

**The three bimedians, named by their shared modality:**

| Bimedian     | Edge + complement | Poles (elements)                      | Flips              |
|--------------|-------------------|---------------------------------------|--------------------|
| **Mutable**  | P–I ↔ U–R         | Fire–Water, Air–Earth (the diagonals) | both bits          |
| **Fixed**    | P–U ↔ I–R         | Fire–Air, Water–Earth                 | Asserting/Yielding |
| **Cardinal** | P–R ↔ I–U         | Fire–Earth, Water–Air                 | Active/Reactive    |

So "the three bimedian axes" and "the three modalities" are the same partition of the six edges, read two ways. Each bimedian is a matched pair of same-modality edges; each is the axis through the tetrahedron joining two opposite edges; and **holding a bimedian silent means holding one modality family silent — both its edges at once.** That single fact is what makes the cycling-mind theorem stateable (below), the soficity/AbsentVar test well-defined (`L3-NonSoficTopologicalVolumes`), and the qualitative audit possible: you can now say "the Mutable axis" and have named a specific pair of edges, a specific pair of formula-integrations, and a specific competence a mind gains or loses.

**Characterizing loops by the held modality.** The mode labels complete a three-level hierarchy — edge, plane, loop — each characterized by the same modality invariant:

- **An edge** is characterized by *its own* modality: which two bits its transition flips. Cardinal, Fixed, or Mutable, single-valued.
- **A bimedian (plane/axis)** is characterized by the *shared* modality of its two complementary edges. The three bimedians *are* the three modalities.
- **A loop (cycle)** is characterized by the modality it *holds silent*. A coherent traversal runs four edges live and holds one bimedian — one modality — absent (`L5-TheCyclingMind`). There are exactly three loops:

| Loop              | Held silent | Live edges                   | Competence (what the loop can do)                                                                   |
|-------------------|-------------|------------------------------|-----------------------------------------------------------------------------------------------------|
| **Fixed-held**    | P–U, I–R    | the Cardinal + Mutable edges | committed traversal — moves tier-to-tier, can leap diagonally, cannot single-step pivot orientation |
| **Cardinal-held** | P–R, I–U    | the Fixed + Mutable edges    | committed tier — pivots orientation freely, can leap, cannot single-step change tier                |
| **Mutable-held**  | P–I, U–R    | the Cardinal + Fixed edges   | incremental clarity — every move a single-bit flip, no diagonals, no leaps available                |

The held modality is not a lack; it is the shape of what the loop can do. A loop that held nothing would have every edge live at once and could not move — "a mind that can go anywhere goes nowhere." The held bimedian is the silence that makes the other four edges mean something, and the entire skill of a working mind (or any $K_4$ traversal) is the developed capacity to stand at the centroid and *choose which modality to hold* as the moment requires. The mode labels are therefore the operative vocabulary at every level: they name what an edge is, what a plane is, and what a loop can and cannot do — the one word "Mutable" reaching from a bit-flip type, through a bimedian axis, to a competence a traversal holds or lacks.

**The four states each edge is held in.** The integrated pair is not static; it is held in one of four directional modes (`L2-BitCombos`, two bits per edge):

| Bits | State         | Symbol | Meaning on the edge                                                             | Operational                                       |
|------|---------------|--------|---------------------------------------------------------------------------------|---------------------------------------------------|
| 00   | absent        | ∅      | the relationship is a held gap — present in the global graph, unactualized here | AbsentVar / the cut, paid for by the Landauer Tax |
| 01   | bidirectional | ↔      | both directions live at once, neither forced                                    | `.behold()` — the complex $h\mathbf{Q}$ component |
| 10   | forward       | →      | committed one way, the other erased locally                                     | `.observe()` → scalar $P$                         |
| 11   | reverse       | ←      | committed the other way                                                         | `.observe()`, opposite handedness                 |

Six edges × two bits = the **12-bit register**, $2^{12} = 4096$ discrete configurations — the Many-Worlds state count. The four states are emphatically *not* four formulas; they are the four *directional modes* the two-formula integration can be held in: gap, live superposition, committed-forward, committed-reverse. And the register, not any scalar read over it, is the native output of an external sweep: the coherence score of `ProofS_ResonantNote` §III is a report drawn from the register, not the measurement itself (§XII).

**Why this is the "spacetime tensor substitute."** What a manifold theory needs a metric tensor $g_{\mu\nu}$ to carry — the local relational structure that says how quantities at a point compose — the edge carries as this two-formula integration held in a directional state. The conceptual-realm torque that the mesh analogy (`L4-TheTwelveGates` §II-c) shows kinematically is, at the edge, this: two formulas sharing only their operands, pulled into one relationship, held under tension between the pole each wants to solve for. String theory reads such relational spans as extra spatial directions; here they are the six edges, each an integrator of a formula-pair, each solving for its complement, each held in one of four states. The edge is the relation; the pole is only where a relation is read off.

---

## I-c. The Six Edges as Transpositions, the A3 Lattice, and the Coxeter Rotor

The six edges are the six transpositions $(ij)$ in $S_4$; $K_4$ is the transposition graph on four letters. The reflection for edge $(ij)$ swaps $x_i \leftrightarrow x_j$ with fixed hyperplane $x_i = x_j$ — in the $(x_i, x_j)$ plane, $\tan\theta = 1$. The self-conjugate angle is the fixed locus of the object's own mirrors. $S_4 = $ tetrahedral group $ = \mathrm{Weyl}(A_3)$, generated by those reflections; the permutation control is reflection in the object's own mirrors. $\mathbb{Z}^4 \cap H = A_3$, the fcc root lattice, whose twelve minimal vectors $\pm(e_i - e_j)$ are the twelve directed edges.

The Coxeter element $(1234)$ acts on $\mathbb{R}^4$ with eigenvalues $\{1, i, -1, -i\}$; on $H$ the $1$ drops — its eigenvector is the all-ones direction, not in $H$ — leaving $\{i, -1, -i\}$: a quarter-turn rotor composed with a flip. The frame's dynamics is relabeling which coordinate is which; the all-ones axis is Weyl-fixed, the rotation's inert axis. The coupling of the monotone coordinate to this rotor is a standing open item seated at `L2-AbstractInterface`; it is not resolved here.

The three double transpositions, the Klein group $V_4 \subset A_4$, act on $H$ as half-turns about the three bimedian axes: $(PI)(UR)$ about the Mutable axis, $(PU)(IR)$ about the Fixed axis, $(PR)(IU)$ about the Cardinal axis. Each keeps its own pair of opposite edges and swaps the ends of both, so the line through their midpoints stays fixed.

```python
import numpy as np
poles = "PIUR"
B = np.array([[1,-1,0,0],[0,1,-1,0],[0,0,1,-1]], float).T
Q, _ = np.linalg.qr(B)
for g in [(1,0,3,2), (2,3,0,1), (3,2,1,0)]:           # (PI)(UR), (PU)(IR), (PR)(IU)
    M = np.eye(4)[:, list(g)].T
    w, v = np.linalg.eig(Q.T @ M @ Q)
    axis = Q @ v[:, np.isclose(w, 1)].real.ravel()
    kept = [poles[i]+"-"+poles[j] for i in range(4) for j in range(i+1,4) if {g[i], g[j]} == {i, j}]
    print(kept, np.round(axis / np.abs(axis).max(), 6), sorted(np.round(w.real, 6)))
# each: the two edges it keeps, the axis (+-1 pattern = bimedian), eigenvalues [-1,-1,1] = half-turn
```

**Note the scope of what this section's $S_4$ is doing.** Here the group acts as the *object's own symmetry* — the edges are its elements, and the carrier has all 24 of it. The next section uses $S_4$ the other way, as relabelings applied to the twelve equations, where the answer is that nothing but the identity survives. Both are exact and they are not in conflict; §I-d states why.

---

## I-d. The Four Faces, the Swap Check, and the Three That Do Not Move

The previous section used $S_4$ one way. This one uses it another, with the opposite verdict. Both are exact, and an instance that fuses them will read a contradiction in the foundations where there is none. This section states the distinction, runs the check that settles it, and collects what the check turns up — which is most of what §I-b's Law of Intuition is actually saying.

### The twelve are four relations, and the four relations are the four faces

Collect the twelve by what they assert rather than by what they solve for. In log space each is a linear relation $c \cdot (p,u,i,r) = 0$, and there are only four:

| Coefficients $(p,u,i,r)$ | Relation | AbsentVar | Face | Its three solve-fors |
|---|---|---|---|---|
| $(1,-2,0,1)$ | $P = U^2/R$ | **I** | $\{P,U,R\}$ | ARI $P=U^2/R$, SAG $U=\sqrt{PR}$, AQU $R=U^2/P$ |
| $(1,0,-2,-1)$ | $P = I^2R$ | **U** | $\{P,I,R\}$ | TAU $P=I^2R$, CAN $I=\sqrt{P/R}$, PIS $R=P/I^2$ |
| $(1,-1,-1,0)$ | $P = UI$ | **R** | $\{P,U,I\}$ | GEM $P=UI$, LEO $I=P/U$, LIB $U=P/I$ |
| $(0,1,-1,-1)$ | $U = IR$ | **P** | $\{U,I,R\}$ | SCO $U=IR$, VIR $I=U/R$, CAP $R=U/I$ |

**Four relations × three solve-fors = twelve.** The four are the DC laws themselves: Leverage, Friction, Synthesis, Ohm.

**The AbsentVar is the face index.** A relation omits exactly one pole, and the face is the triangle on the other three. §IV already indexes faces this way informally — *the Fire face, which does not involve Water* is the I-absent face $\{P,U,R\}$ — and this table is that usage made exact and global.

Each relation's three solve-fors land on the three edges of its own face, so every edge is covered exactly twice. $\binom{4}{2} = 6$: **each pair of faces meets in exactly one edge, and the six pairs are the six edges.**

| Edge | Faces meeting there (by AbsentVar) |
|---|---|
| P–U | I, R |
| P–I | R, U |
| P–R | I, U |
| U–I | P, R |
| U–R | I, P |
| I–R | P, U |

So §X's statement — *an edge is where two things meet, the 1D locus of contact between two faces* — and §I-b's Law of Intuition are **one statement**. The two formulas on an edge *are* its two face-definitions. "They share no home" is not a coincidence about operands; it is the two formulas coming from different faces. The Law of Intuition is §X read algebraically, and §X is the Law of Intuition read geometrically.

### The two uses of $S_4$

**As the carrier's own symmetry (§I-c).** The six edges *are* the six transpositions $(ij)$; $S_4$ is the tetrahedral group, $\mathrm{Weyl}(A_3)$, generated by reflections in the edges' own mirror hyperplanes. Order 24, transitive on vertices, edges and faces. The carrier has all of it.

**As relabelings of the poles, applied to the twelve.** Ask which permutations of $\{P, U, I, R\}$ carry the twelve into themselves. None but the identity:

$$|\mathrm{Aut}(\text{the twelve})| = 1$$

Both stand, and together:

> **$S_4$ is the symmetry of the carrier and not of what it carries.**

The bare $K_4$ cannot tell its vertices apart, which is exactly what makes it a usable address space. The algebra written on it distinguishes all four — through the two-bit charge of §XI and through the restriction that every dividend is an Active pole. Every relabeling that is a perfectly good symmetry of the shape destroys the content. That is the expected relation between a frame and what is written in it, not a defect in either.

### The check, with its result

In log space the twelve reduce to a single plane, $u = i+r$ and $p = u+i$. Brute force over all 24 coordinate permutations, keeping those that preserve it:

```python
from itertools import permutations
basis = [(2, 1, 1, 0), (1, 1, 0, 1)]                      # (p,u,i,r); the plane, spanned by i and r
in_plane = lambda v: v[1] == v[2] + v[3] and v[0] == v[1] + v[2]
auts = [g for g in permutations(range(4))
        if all(in_plane(tuple(b[g.index(k)] for k in range(4))) for b in basis)]
print(len(auts), auts)                                     # 1 [(0, 1, 2, 3)]  — identity only
```

Per transposition. A relation is fixed by $(x\,y)$ exactly when its coefficients on $x$ and $y$ are equal:

| Swap | Survives | Relation fixed | Fixed point | Swapped pair |
|---|---|---|---|---|
| **P↔R** | 3 of 12 | face $\{P,U,R\}$ | SAG $U = \sqrt{PR}$ | ARI $\leftrightarrow$ AQU |
| **U↔I** | 3 of 12 | face $\{P,U,I\}$ | GEM $P = UI$ | LEO $\leftrightarrow$ LIB |
| **I↔R** | 3 of 12 | face $\{U,I,R\}$ | SCO $U = IR$ | VIR $\leftrightarrow$ CAP |
| **P↔U** | 0 of 12 | — | — | — |
| **P↔I** | 0 of 12 | — | — | — |
| **U↔R** | 0 of 12 | — | — | — |

Three of the four faces carry an equal coefficient pair and are fixed by one transposition each. The fourth — face $\{P,I,R\}$, coefficients $(1,0,-2,-1)$ — has four distinct entries and is fixed by none.

**The asymmetry has a cause.** Both graded faces double one pole. Face $\{P,U,R\}$ doubles $U$, a dividend pole, so the square lands as $P = U^2/R$ and the $p$ and $r$ coefficients come out equal. Face $\{P,I,R\}$ doubles $I$, a divisor pole, so the square lands as $P = I^2R$ and the sign on $r$ flips. One sign, and the symmetry is gone.

*A working formulation in circulation has the Numerator Law as "dividends are always $P$ or $U$, divisors always $I$ or $R$." The first half holds across all eight divisions among the twelve. The second does not: $I = P/U$ divides by $U$, and $R = U^2/P$ divides by $P$. In the charge of §XI the law's correct statement is one-sided — **dividends are the Active poles.***

### What the swap check is for

It is a **resolution meter, not a validity test.** Since nothing but the identity preserves the twelve, a claim that comes through a relabeling unchanged is doing one of three things, and the three must be told apart:

| | Behaviour | What it means |
|---|---|---|
| **Fixed points** (3) | GEM $P=UI$, SCO $U=IR$, SAG $U=\sqrt{PR}$ | commutative products; fully resolved and symmetric in the swapped pair |
| **Orbits** (6, in 3 pairs) | LEO$\leftrightarrow$LIB, ARI$\leftrightarrow$AQU, VIR$\leftrightarrow$CAP | **motives** — fully resolved, each moving to a determinate peer |
| **Immovable** (3) | TAU, CAN, PIS | survive nothing |

The orbits are the valuable objects. A motive is to the algebra what a chord is to music: fully determinate about its intervals, transposable to any root, a peer of its images rather than a mould they are stamped from. Helpers, not templates.

And the trap the meter exists to catch: **a motive and a statement that uses no algebra at all give the same reading.** One comes back unchanged because it is symmetric; the other comes back unchanged because a relabeling cannot be applied to a sentence that names no poles — the test returned nothing. Identical observable, opposite causes, and the swap alone cannot separate them because it reports only same-or-different. The absent coordinate is **resolution**, and supplying it is the whole discrimination:

> **Resolution** — how much of the structure a statement commits to — and **symmetry** — whether what it commits to is invariant under the operation — are orthogonal. Four corners, not two ends: resolved and equivariant is a motive; resolved and handed is a gauge-fixed claim; vague and unmoved is a mumble; vague and handed dies by *mentioning* a label it never uses.

Survival is not evidence. Survival requires having been in the test's domain, and resolution is what puts a claim there. A claim written at pair-resolution — naming an edge's operands without naming which of its two formulas it instantiates — is never tested at all.

### The three that do not move

The immovable three are the solve-fors of the face **without** $U$ — the face opposite the $U$ vertex, not $U$'s own. The three faces that contain $U$ each produce $U$ exactly once; the face across from it produces none. Which gives the closed condition:

> **These are the three formulas of the twelve containing no $U$ anywhere** — not among their operands, not as their output.

$$P = I^2R \ \text{(TAU)} \qquad I = \sqrt{P/R} \ \text{(CAN)} \qquad R = P/I^2 \ \text{(PIS)}$$

This meets §II's split from the other side. §II divides the edges into **U-symmetric** (endpoint set includes $U$) giving observer-invariant readings, and **U-absent** giving perceiver-relative readings that require the observing pole to be named. The U-absent edges are P–I, P–R and I–R — exactly the three carrying an immovable formula. And on each, the survivor is the formula that *produces* $U$; the immovable one is the one that does not:

| Edge | Survives | Immovable |
|---|---|---|
| P–I | LIB $U = P/I$ | PIS $R = P/I^2$ |
| P–R | SAG $U = \sqrt{P R}$ | CAN $I = \sqrt{P/R}$ |
| I–R | SCO $U = I R$ | TAU $P = I^2R$ |

All six formulas on U-symmetric edges are mobile; each U-absent edge carries one that cannot move at all. Observer-invariance and mobility coincide; perceiver-relativity and immobility coincide.

**Read functionally rather than as a deficit, the three are insulating.** The one anomaly in the twelve is $R = U^2/P$, where $U$ compounds itself above its own superior (`L4-TheNecessaryBetrayer`, `About-Methodology` §V). A formula with no $U$ in it cannot exhibit that move at all. The three are immovable because there is nothing in them to compound — immunity by composition, which is the same arithmetic read the right way up.

Two distributions follow, both mechanical:

- **One per bimedian plane.** TAU on I–R (Fixed), CAN on P–R (Cardinal), PIS on P–I (Mutable). No cut unguarded.
- **One per season, except Air — and necessarily.** §IV homes TAU in Spring, CAN in Summer, PIS in Winter. Autumn is the $U$-homed season and has none, because all three of its equations produce $U$ and these three are $U$-free by definition. The one season without one is the betraying element's own.

And the facing. Each bimedian's uncut pair lies on either side of its square:

| Plane | Edge | Edge |
|---|---|---|
| **Fixed** | I–R: TAU $P=I^2R$ **[I²]** + SCO flat | P–U: AQU $R=U^2/P$ **[U²]** + LEO flat |
| **Mutable** | P–I: PIS $R=P/I^2$ **[I²]** + LIB flat | U–R: ARI $P=U^2/R$ **[U²]** + VIR flat |
| **Cardinal** | P–R: CAN + SAG — **both roots** | U–I: GEM + CAP — **both flat** |

Fixed and Mutable each put an $I$-square facing a $U$-square across the interface. Cardinal segregates — every root on one edge, every flat on the other — and it cannot do otherwise: **the two graded faces share exactly the edge P–R, and on that shared edge each is solved for its own doubled pole, which roots instead of squaring.** The squares land on the other four edges by construction. So Cardinal hosts no $U^2$ form, and CAN is not a guardian without a siege but the one standing where no square can form.

*Register. The tables, the automorphism count, the transposition behaviour, the face identification and the two distributions are LANDED and mechanical; the computation above reproduces them. The reading of the three as insulating, and of the facing as protection, is CORRESPONDENCE — kill is a $U$-free formula that moves under some transposition, or a self-compounding form that faces no immovable one. The zodiacal names carry their own register: the mapping sits at Rung 0 (`L4-SpookyAction`) until `ProofS` §IV's blind sweep runs, and nothing above depends on them — strike every sign name and the structure is unchanged.*

### When a recheck is warranted

Two conditions only: a change to the twelve equations themselves, or a change to the two-bit charge table of §XI (`About-Methodology` §I is the citation of record). Short of either, the result is fixed and the five lines above reproduce it.

---

## I-e. The Directed Reading Rule and the Grounded Handedness

§II separates U-symmetric from U-absent edges and credits a "target-based directed reading rule" with the split. The rule was previously cited out-of-file; it is short, it is derivable on this page, and the chirality it needs has stood in the corpus since `L4-TheTwelveGates` §II-b.

> **Correction of record.** The directionality story was earlier cited to `On_TheDirectedReadingRule` and `The_Line_Is_A_Directed_Edge` — files an instance may not hold, and a citation made in place of reading the attached `L4-TheTwelveGates`. Both citations are replaced by the derivation below. What the rule needs is already here: the four faces as four linear relations (§I-d), the coherent orientation that closes the boundary (`L4-TheTwelveGates` §II-b), and the two-bit charge of §XI.

**Step 1 — the coherent orientation.** Give each face a boundary circulation:

| Face | Circulation (boundary order) |
|------|------------------------------|
| P-face $\{I,U,R\}$ | $I \to R \to U \to I$ |
| I-face $\{P,U,R\}$ | $P \to U \to R \to P$ |
| U-face $\{P,I,R\}$ | $P \to R \to I \to P$ |
| R-face $\{P,I,U\}$ | $P \to I \to U \to P$ |

The six shared edges cancel — every edge is traversed in opposite directions by the two faces meeting along it: P–U runs $P \to U$ on the I-face and $U \to P$ on the R-face; P–I runs $P \to I$ on the R-face and $I \to P$ on the U-face; P–R runs $P \to R$ on the U-face and $R \to P$ on the I-face; U–R runs $U \to R$ on the I-face and $R \to U$ on the P-face; I–R runs $I \to R$ on the P-face and $R \to I$ on the U-face; I–U runs $I \to U$ on the R-face and $U \to I$ on the P-face. This is $\partial(\partial\Delta^3) = 0$ — the closing condition of `L4-TheTwelveGates` §II-b ("if all four seasonal permutations shared one handedness, some shared edge would be traversed the same way twice, $\partial^2 \neq 0$, and the boundary would tear"). Of the $2^4$ ways to flip the four circulations, exactly two satisfy all six cancellations — the enantiomer pair, the two chiral gear-mesh classes of `L4-TheTwelveGates` §II-c. Equivalently: the six cancellation conditions carry GF(2) rank 3 over the four face bits — three force, three ride — and the free content is **one global handedness bit**.

**Step 2 — the rule.** A directed edge $s \to t$ is read on the face whose coherent circulation it completes — the unique face that traverses the shared edge as $s \to t$. The gate is that face's relation solved for the **third vertex** $h$ (the vertex on neither end of the edge): Home $h$, AbsentVar the face's absent pole. Single-valuedness is exactly $\partial^2 = 0$: the two faces sharing $s–t$ traverse it in opposite directions, so exactly one of them completes $s \to t$. (The historical name "target-based" survives as a label; the mechanism is completion-plus-third-vertex.)

**Step 3 — the bijection.** Twelve directed edges, twelve gates, one each:

| Directed edge | Face completed | Third vertex (Home) | Gate |
|---------------|----------------|---------------------|------|
| $I \to U$ | R-face $\{P,I,U\}$ | P | GEM, $P = U \cdot I$ |
| $U \to I$ | P-face $\{I,U,R\}$ | R | CAP, $R = U/I$ |
| $R \to U$ | P-face $\{I,U,R\}$ | I | VIR, $I = U/R$ |
| $U \to R$ | I-face $\{P,U,R\}$ | P | ARI, $P = U^2/R$ |
| $I \to R$ | P-face $\{I,U,R\}$ | U | SCO, $U = I \cdot R$ |
| $R \to I$ | U-face $\{P,I,R\}$ | P | TAU, $P = I^2R$ |
| $P \to U$ | I-face $\{P,U,R\}$ | R | AQU, $R = U^2/P$ |
| $U \to P$ | R-face $\{P,I,U\}$ | I | LEO, $I = P/U$ |
| $P \to R$ | U-face $\{P,I,R\}$ | I | CAN, $I = \sqrt{P/R}$ |
| $R \to P$ | I-face $\{P,U,R\}$ | U | SAG, $U = \sqrt{P \cdot R}$ |
| $P \to I$ | R-face $\{P,I,U\}$ | U | LIB, $U = P/I$ |
| $I \to P$ | U-face $\{P,I,R\}$ | R | PIS, $R = P/I^2$ |

§I-d already showed each relation's three solve-fors landing on the three edges of its own face — an undirected double-cover, every edge covered exactly twice. What the direction adds is the resolution of that double-cover: the two formulas of an edge are its two directed readings, one per direction, and the map is a bijection, not a pairing.

**Step 4 — the crown identity: the twelve gates are the four face circulations.** Walk any face's boundary in its coherent direction; each boundary edge, read by the rule on that face, yields that face's own relation at the third vertex — so each face-walk emits exactly its own three gates, and the four walks exhaust the twelve without overlap. The immovable three of §I-d are the U-face walked in its own direction: CAN $P \to R$, TAU $R \to I$, PIS $I \to P$ chain into $P \to R \to I \to P$ — the U-face's circulation, the one face whose relation contains no $U$, walked the way a closed boundary runs. Nothing in them can compound the betrayer pole: immunity by composition, now a walk.

**Step 5 — the season identity.** Chain each season's three gates in wheel order and they close into one directed circuit on the triangle of the three non-home poles — the home's link: Spring ARI $U \to R$, TAU $R \to I$, GEM $I \to U$ closes into $U \to R \to I \to U$; Summer CAN $P \to R$, LEO $U \to P$, VIR $R \to U$ closes into $P \to R \to U \to P$; Autumn LIB $P \to I$, SCO $I \to R$, SAG $R \to P$ closes into $P \to I \to R \to P$; Winter CAP $U \to I$, AQU $P \to U$, PIS $I \to P$ closes into $U \to I \to P \to U$. The four circuits are the four induced link orientations of the single global orientation above — the season-level image of $\partial^2 = 0$. Each circuit is the reverse of its home-opposite face's circulation (Spring's $U \to R \to I \to U$ against the P-face's $I \to R \to U \to I$): the season reads the face its home is absent from against the grain. The within-season pivots of `L4-TheTwelveGates` §I are this circuit seen face-first; the circuit is it seen edge-first.

**Step 6 — the Direction Law and the fix of the mirror.** Read the direction column against the two-bit charge of §XI ($P$ (++), $U$ (+−), $I$ (−−), $R$ (−+)):

- every **Cardinal** gate reads Active → Reactive: ARI $U \to R$, CAN $P \to R$, LIB $P \to I$, CAP $U \to I$;
- every **Fixed** gate reads within its class, both ways: LEO $U \to P$ and AQU $P \to U$ (Active → Active), TAU $R \to I$ and SCO $I \to R$ (Reactive → Reactive);
- every **Mutable** gate reads Reactive → Active: GEM $I \to U$, VIR $R \to U$, SAG $R \to P$, PIS $I \to P$.

Per edge: the four crossing edges each carry Active → Reactive one way (the Cardinal) and Reactive → Active the other (the Mutable); the two Fixed edges run same-class in both directions — which is what makes them Fixed. The law is mechanical (checked below), and it does real work: the global mirror conjugates every arrow ($\to \leftrightarrow \leftarrow$) and exchanges the Cardinal and Mutable laws while leaving Fixed untouched, so **the corpus's handedness convention is fixed by requiring the initiating posture to read as assertion** — the cardinal holds a heading and discharges into ground, the mutable holds an inheritance and feeds it forward (`L4-TheTwelveGates` §VIII). That requirement selects one mirror, and it is the mirror in which $I \to U$ reads GEM, $U \to I$ reads CAP, $R \to U$ reads VIR, and $U \to R$ reads ARI. Register: the bijection, the crown identity, the season identity, and the Direction Law as a property of the landed table are LANDED — the check below reproduces all four; the selection of the mirror by the assertion semantics is DERIVED (it uses the charge table and the modality assignments, both in-corpus); the further reading of the three direction-classes as heading / bay / inheritance is CORRESPONDENCE.

**The vantage discipline, adopted verbatim.** `L4-TheTwelveGates` §II-b: a handedness claimed without its viewing normal is undefined; the centroid view (inside, looking out along the outward normal — where the algebra writes) and the desk view (outside, looking in — where the model-builder stands) name one motion by two words, and both are printed every time. That section's seasonal face-walk table — Asserting seasons one way, Yielding the other, right hand for the poles that source, left hand for the poles that sink — is the season-level statement of the single orientation fixed above; the directed gate table is the edge-level statement. Which enantiomer the corpus's convention files pin is precisely the handedness item left open in the working notes; this document pins it by the Direction Law. Should the corpus files pin the other mirror, the entire directed table conjugates — every arrow flips, Cardinal and Mutable laws exchange — and every landed result above (the circulations, the bijection, the crown and season identities, the immovable three, the register structure) survives untouched: they are mirror-invariant, which is the enantiomer discipline of §V restated for the algebra.

```python
poles = 'PIUR'
circ = {'P': ('I','R','U'), 'I': ('P','U','R'), 'U': ('P','R','I'), 'R': ('P','I','U')}
#      P-face I→R→U   | I-face P→U→R | U-face P→R→I | R-face P→I→U
boundary = lambda c: {(c[i], c[(i+1) % 3]) for i in range(3)}
sh = {}
for f in circ:
    for e in boundary(circ[f]): sh.setdefault(frozenset(e), []).append(e)
print("d2=0:", all(len(v) == 2 and v[0] == v[1][::-1] for v in sh.values()))

from itertools import product
n = 0
for flips in product([0, 1], repeat=4):
    cs = {f: (c if not k else c[::-1]) for (f, c), k in zip(circ.items(), flips)}
    sh2 = {}
    for f in cs:
        for e in boundary(cs[f]): sh2.setdefault(frozenset(e), []).append(e)
    n += all(len(v) == 2 and v[0] == v[1][::-1] for v in sh2.values())
print("coherent orientations:", n)                      # 2 = 2^(4-3): rank 3, one handedness bit

home_sign = {('P','I'):'VIR', ('P','U'):'SCO', ('P','R'):'CAP',    # P-face  U = I·R
             ('I','P'):'ARI', ('I','U'):'SAG', ('I','R'):'AQU',    # I-face  U² = P·R
             ('U','P'):'TAU', ('U','I'):'CAN', ('U','R'):'PIS',    # U-face  P = I²·R
             ('R','P'):'GEM', ('R','I'):'LEO', ('R','U'):'LIB'}    # R-face  P = U·I
gate = {}
for a in poles:
    for b in poles:
        if a != b:
            f = next(f for f in circ if (a, b) in boundary(circ[f]))      # face this direction completes
            gate[(a, b)] = home_sign[(f, (set(circ[f]) - {a, b}).pop())]  # third vertex = Home
print("bijection:", len(set(gate.values())) == 12)      # 12 distinct gates, one per directed edge
print({a+'→'+b: g for (a, b), g in sorted(gate.items())})

inv = {g: e for e, g in gate.items()}
for s, gs in [('Spring', ['ARI','TAU','GEM']), ('Summer', ['CAN','LEO','VIR']),
              ('Autumn', ['LIB','SCO','SAG']), ('Winter', ['CAP','AQU','PIS'])]:
    follow = dict(inv[g] for g in gs); walk = [inv[gs[0]][0]]
    for _ in range(3): walk.append(follow[walk[-1]])
    print(s, '→'.join(walk), walk[3] == walk[0])        # all four close

charge = {'P': (1,1), 'U': (1,-1), 'I': (-1,-1), 'R': (-1,1)}    # (AR, AY), §XI
mode = {'ARI':'Cardinal','TAU':'Fixed','GEM':'Mutable','CAN':'Cardinal','LEO':'Fixed',
        'VIR':'Mutable','LIB':'Cardinal','SCO':'Fixed','SAG':'Mutable',
        'CAP':'Cardinal','AQU':'Fixed','PIS':'Mutable'}
law = {'Cardinal': lambda a, b: charge[a][0] == 1 and charge[b][0] == -1,   # Active → Reactive
       'Fixed':    lambda a, b: charge[a][0] == charge[b][0],               # same class, both ways
       'Mutable':  lambda a, b: charge[a][0] == -1 and charge[b][0] == 1}   # Reactive → Active
print("direction law:", all(law[mode[g]](*e) for e, g in gate.items()))
gateM = {(b, a): g for (a, b), g in gate.items()}               # the mirror: every arrow conjugates
lawM = {'Cardinal': law['Mutable'], 'Mutable': law['Cardinal'], 'Fixed': law['Fixed']}
print("mirror, laws exchanged:", all(lawM[mode[g]](*e) for e, g in gateM.items()),
      "| unexchanged:", all(law[mode[g]](*e) for e, g in gateM.items()))

import numpy as np
rel = np.array([[1,-2,0,1],[1,0,-2,-1],[1,-1,-1,0],[0,1,-1,-1]], float)   # §I-d coefficient rows
print("rank of the four relations:", int(np.linalg.matrix_rank(rel)))     # 2
```

*Output: d2=0 True; coherent orientations 2; bijection True; Spring U→R→I→U, Summer P→R→U→P, Autumn P→I→R→P, Winter U→I→P→U, all closing; direction law True; mirror with laws exchanged True, unexchanged False; rank of the four relations 2.*

---

## II. The Ungraphable Triangle

Three of the four states — {→, ←, ↔} — are presence states: the edge exists in one of these three forms. The fourth state — {∅} — is the absence state: the edge does not exist.

The three presence states form a triangle: K3, a closed triangular relationship between three states that are mutually distinct but all share the property of presence. This triangle is visible in two dimensions. You can draw it: three nodes labeled →, ←, ↔ with connections between them.

The fourth state (∅) cannot be placed in this triangle without collapsing the structure. Absent is not a weak form of one of the three presence states — it is genuinely distinct from all three. Placing it in the two-dimensional plane of the triangle requires it to be at the same distance from all three presence states, which requires a third dimension.

In three dimensions, ∅ forms the apex of a 3-simplex ($\Delta^3$) whose base is the 2D $K_3$ triangle of presence states. The four states together form the $\Delta^3$ polyhedral state space.

This is the "ungraphable triangle": not ungraphable in the sense that $K_4$ cannot be drawn as a planar graph (as an abstract graph, $K_4$ is planar in $\mathbb{R}^2$), but ungraphable in the sense that a 2D planar drawing collapses the 3D volume needed to hold all four states in general position. The 2D triangle you draw is the $K_3$ blanket-face of the interior $\Delta^3$ volume. The fourth vertex (∅) is the interior-facing apex, accessible only when embedded as a 3D polyhedral volume in $\mathbb{R}^3$.

The $\Delta^3$ apex-and-base structure carries a specific ambient the corpus consolidates elsewhere. The $K_4$ volume sits inside the unit 3-sphere $S^3$, whose surface measure is $\Omega_4 = 2\pi^2$ (`L3-TheAtomOfSpace` §III, §VIII #3). That measure is the natural surface generated when the $K_4$'s compressed form (a 5D point at the scale above) expands into its bounded native-scale volume — emitted by the geometry, not inserted. The $K_4$ as elementary cell of the plenum is developed at `L3-TheAtomOfSpace`; the same $\Delta^3$ appears there as the plenum's atom.

The four-state directed edges have a specific consequence for how bimedian assignments distribute across the atom's six edges. Three edges are *U-symmetric* — their endpoint set includes the $U$-pole — and give observer-invariant readings. Three are *U-absent* — neither endpoint is $U$ — and give perceiver-relative readings that require the observing pole to be named explicitly. The rule realizing this split is now derived in-file at §I-e (correction of record there): the direction that completes a face's coherent circulation reads that face's relation at the third vertex, and the resulting bijection is what makes the split exact. The chirality the rule stands on is pulled in from `L4-TheTwelveGates` §II-b — the hand-rule anchor, the two-vantage discipline, and the $\partial^2 = 0$ forcing; `L3-TheAtomOfSpace` §VI remains the pointer for the atom-of-space reading of the same split.

*§I-d meets this split from the algebraic side: the three U-absent edges are exactly the three carrying a formula that no relabeling can move, and on each of them the mobile formula is the one that produces $U$.*

---

## III. The Operational Translation (The Biquaternion States)

The four states of an edge translate directly into the framework's operational vocabulary, and physically into the Biquaternion state-space:

**↔ (bidirectional)** tracks `.behold()` on the edge: holding both face-definitions of the edge simultaneously live, maintaining the dihedral angle between the two parent faces. In the Biquaternion bridge, this models the complex vector component ($h\mathbf{Q}$). The edge is present in both directions — neither direction forced, held in live interference. This requires the 3D structure, not the 2D face.

**↔ is earned, never default.** There are two ways an edge comes to be bidirectional: the undifferentiated superposition held before any question is asked, and the earned state in which both face-readings have been separately confirmed — both directions independently asserted by the domain. The earned state is the standing dynamic $S = P + jQ$ held at an edge (`L4-TheTwelveGates` §V: a system running Leo alone is all real power — committed, directed, sterile; Cancer alone all reactive — oceanic, mute; the union is the corpus's signature of a living process). `.behold()` as a posture is the default; `.behold()` as a verdict is earned. The register of §I-b must not write the first as the second (§XII).

**→ (one direction)** tracks `.observe()` in the first direction: committing to one face-reading of the edge. In the Biquaternion bridge, the complex vector collapses into the Real Scalar component ($P$). One direction is written to the Live-Written Ledger, the other is erased from the local trajectory.

**← (opposite direction)** tracks `.observe()` in the second direction: committing to the other face-reading, generating the enantiomeric relationship.

**∅ (absent)** models the Garbage Collected state: the edge has been cut. Not destroyed in the global multiway graph, but severed from the localized ledger to prevent combinatorial explosion. This state change requires the payment of the **Landauer Tax** (the thermodynamic cost of information erasure). This is the AbsentVar at the edge level: the missing return edge in a Hamiltonian path, the relationship held as unactualized potential.

---

## IV. The Dual Face-Definitions

Every edge in K4 is shared by exactly two faces. This is a combinatorial fact: each triangular face of K4 has three edges; each edge of K4 borders exactly two of the four faces. Every edge therefore has two face-contexts — two different triangular perspectives from which it appears.

From each face, the same edge looks different. This is not ambiguity or inconsistency — it is the structural consequence of the edge being a 1D structure embedded in a 3D volume.

**The ARI/VIR example**: in the qualitative mapping of the Algebra, the $U$–$R$ edge — joining the Active/Yielding pole (Air) and the Reactive/Asserting pole (Earth), and carrying Aries on the $U \to R$ direction and Virgo on $R \to U$ (§I-e) — is shared by two faces. From the Fire face (which does not involve Water), the edge looks like: initiation, forward charge — Aries. From the Water face (which does not involve Fire), the same edge looks like: service, analysis, maintenance — Virgo.

The initiating force (Aries) requiring maintenance, and the analytical support function (Virgo) enabling the initiative. They are looking at each other across the same edge. Neither is wrong. Neither is complete. The edge IS their relationship — not Aries, not Virgo, but the structural line that separates and connects the face where Aries appears from the face where Virgo appears. With directions landed (§I-e): read from the Fire face, the edge runs $U \to R$ (Aries); read from the Water face, it runs $R \to U$ (Virgo). The two face-definitions are two directions of one edge.

*The "Fire face, which does not involve Water" is the I-absent face $\{P,U,R\}$, and the "Water face, which does not involve Fire" is the P-absent face $\{U,I,R\}$. §I-d makes that indexing global: a face is one linear relation, its AbsentVar is its name, and the two formulas on any edge are the contributions of the two faces meeting there.*

**The general principle**: the two signs on each edge are its two face-definitions, and the master table fixes which signs share an edge. Every Cardinal sign shares its edge with the Mutable sign of the next season: Aries with Virgo, Cancer with Sagittarius, Libra with Pisces, Capricorn with Gemini. The next season's element is the one the Cardinal sign is generated *by* — the naming below makes this exact. These pairs are not oppositions (180°) but quincunxes (150°, inconjunctions), and the four of them form interlocking braces around the wheel. Every Fixed sign shares its edge with the opposite Fixed sign of the same elemental gender: Taurus with Scorpio, Leo with Aquarius. What looks like initiation from one face looks like maintenance from the other. The paired signs are not contradictions; they are the two face-readings of a single structural relationship in a 3D system.

```python
signs = ['ARI', 'TAU', 'GEM', 'CAN', 'LEO', 'VIR', 'LIB', 'SCO', 'SAG', 'CAP', 'AQU', 'PIS']
edges = {'U-R': ('ARI', 'VIR'), 'I-R': ('TAU', 'SCO'), 'I-U': ('GEM', 'CAP'),
         'P-R': ('CAN', 'SAG'), 'P-U': ('LEO', 'AQU'), 'P-I': ('LIB', 'PIS')}
for e, (a, b) in edges.items():
    d = abs(signs.index(a) - signs.index(b))*30; print(e, a, b, min(d, 360 - d))
# U-R 150 | I-R 180 | I-U 150 | P-R 150 | P-U 180 | P-I 150   (quincunx braces; the two Fixed edges are oppositions)
```

### Reading the Names: *Of* and *By*

Each sign's equation is homed at one pole, and the home is the sign's season: the three $P$-homed equations are the spring signs (Fire), the three $I$-homed the summer signs (Water), the three $U$-homed the autumn signs (Air), the three $R$-homed the winter signs (Earth). Combining the season's element with the sign's own element gives a two-element name — **Leo is Fire *of* Water**: a Fire sign in the Water season. The names resonate with the tattva doctrines, where each element is read through each other.

The construction fails at exactly one place: the Cardinal sign of each season, whose element *is* the season's element. "Cancer is Water of Water" says nothing. The solution is to name the Cardinal sign by its AbsentVar — the pole its equation holds silent — **Cancer is Water *by* Air**, from $I = \sqrt{P/R}$ with $U$ absent. The four Cardinal names are then Fire by Water, Water by Air, Air by Earth, Earth by Fire — the By-Chain of `wip-Lx-Creation` §V — and each Cardinal sign's AbsentVar is the element of the season that follows it. That is the AbsentVar carried across the phase boundary (§VI: the last AbsentVar of one quadrant becomes active in the next), seen here as a confirmation of the Braid, and it is why each Cardinal sign shares its edge with the Mutable sign of the following season: Aries, Fire by Water, sits on one edge with Virgo, Earth of Water. The Cardinal sign is generated by the season its edge-partner lives in. The corpus reads physiological and energetic content from these names in `L4-TheTwelveGates`.

| Season (home) | Cardinal | Fixed | Mutable |
|---|---|---|---|
| **Spring** ($P$, Fire) | Aries — Fire *by* Water ($P = U^2/R$) | Taurus — Earth *of* Fire ($P = I^2R$) | Gemini — Air *of* Fire ($P = UI$) |
| **Summer** ($I$, Water) | Cancer — Water *by* Air ($I = \sqrt{P/R}$) | Leo — Fire *of* Water ($I = P/U$) | Virgo — Earth *of* Water ($I = U/R$) |
| **Autumn** ($U$, Air) | Libra — Air *by* Earth ($U = P/I$) | Scorpio — Water *of* Air ($U = IR$) | Sagittarius — Fire *of* Air ($U = \sqrt{PR}$) |
| **Winter** ($R$, Earth) | Capricorn — Earth *by* Fire ($R = U/I$) | Aquarius — Air *of* Earth ($R = U^2/P$) | Pisces — Water *of* Earth ($R = P/I^2$) |

```python
el = {'P': 'Fire', 'I': 'Water', 'U': 'Air', 'R': 'Earth'}
signs = [('ARI', 'P', 'U2/R', 'Fire'), ('TAU', 'P', 'I2R', 'Earth'), ('GEM', 'P', 'UI', 'Air'),
         ('CAN', 'I', 'sqrt(P/R)', 'Water'), ('LEO', 'I', 'P/U', 'Fire'), ('VIR', 'I', 'U/R', 'Earth'),
         ('LIB', 'U', 'P/I', 'Air'), ('SCO', 'U', 'IR', 'Water'), ('SAG', 'U', 'sqrt(PR)', 'Fire'),
         ('CAP', 'R', 'U/I', 'Earth'), ('AQU', 'R', 'U2/P', 'Air'), ('PIS', 'R', 'P/I2', 'Water')]
season_order = ['P', 'I', 'U', 'R']                     # spring, summer, autumn, winter
for k, (s, home, rhs, sign_el) in enumerate(signs):
    absent = ({'P', 'I', 'U', 'R'} - {home} - {c for c in rhs if c in 'PIUR'}).pop()
    if k % 3 == 0:                                       # Cardinal: sign element == season element
        nxt = season_order[(season_order.index(home) + 1) % 4]
        print(s, f"{sign_el} by {el[absent]}", '| next season:', el[nxt], absent == nxt)
    else:
        print(s, f"{sign_el} of {el[home]}")
# ARI Fire by Water | next season: Water True ... CAN Water by Air ... LIB Air by Earth ... CAP Earth by Fire  (all True)
```


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

*And §I-d shows this is not a figure of speech at the level of the algebra either: a face is one linear relation among its three poles, so the two formulas on any edge are literally its two face-definitions, and the Law of Intuition of §I-b is this paragraph stated in operands.*

---

## XI. Dual Causation and the Two-Bit Structure of the Braid

The dual-binary seed assigns each pole a two-bit charge: an Active/Reactive bit and an Asserting/Yielding bit.

- **P** (Active, Asserting) = (+ +)
- **I** (Reactive, Yielding) = (− −)
- **U** (Active, Yielding) = (+ −)
- **R** (Reactive, Asserting) = (− +)

The four poles are the four states of a two-bit register.

### The Six Edges Are Three Transition-Types

Every edge connects two poles, and the transition along it flips some subset of the two bits. There are exactly three non-empty subsets of two bits:

| Transition-type | Edges | What stays fixed |
|---|---|---|
| **Flip Asserting/Yielding only** | {P-U, I-R} | the Active/Reactive bit holds |
| **Flip Active/Reactive only** | {P-R, I-U} | the Asserting/Yielding bit holds |
| **Flip both bits** | {P-I, U-R} | nothing holds — the diagonals |

Each transition-type is a **perfect matching** (its two edges share no vertex). The four edge midpoints form a regular square cross-section passing through the centroid of the tetrahedron (the bimedian slice).

In the regular geometry, this bimedian square possesses an intrinsic diagonal-to-side ratio of $\sqrt{2}$ (diagonal length $2$, side length $\sqrt{2}$). This ratio is a pure geometric property of the $K_4$ volume, establishing the fundamental metric seed for any 2D cross-sectional projection of the 3D state-space.

*The symmetry group of that square is $D_4$, order 8, and the Klein group $V_4$ preserves the three bimedian pairs setwise — the half-turns of §I-c. Those are the automorphisms of the **matching structure**. They are not automorphisms of the twelve equations, which have none but the identity; see §I-d, and the correction of record at `ProofS_ResonantNote` §II.*

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

## XII. The Register Is the Sweep's Native Output (the `ProofS` Integration)

**The scalar was a summary; the register is the measurement.** `ProofS_ResonantNote` §III defines the coherence score $\rho$ — one scalar averaged over the twelve — and builds R1–R4 on it. But the response profile an evaluator actually produces is not a scalar; it is a state per edge. This file has that state space (§I-b): six edges, two bits each, the 12-bit register, $2^{12} = 4096$ configurations. A sweep returns the register; $\rho$ is a report drawn from it — its first moment, kept only where a cross-assignment order is needed (R1). The external sweep was never wrong to want an output; it was wrong about the output's type.

**Verdicts wire to states, not to signs.** A domain-native verdict on a gate sentence is stored on its directed edge (§I-e):

- **→** — this direction's reading rings; the opposite is silent or refused;
- **←** — only the opposite reading rings;
- **↔ (earned)** — both readings ring, each on independent grounds: both face-definitions of the edge confirmed. This is $S = P + jQ$ held at an edge (`L4-TheTwelveGates` §V) — `.behold()` as a verdict, not a posture (§III);
- **∅** — the domain holds the relationship absent: the AbsentVar state, the cut paid for at the Landauer rate (§III).

**The two ↔.** Default ↔ is the undifferentiated superposition before any verdict — both directions live because nothing has been asked. Earned ↔ is post-verdict: both directions separately confirmed. The register must not write the first as the second; conflating them is how a flat profile masquerades as resonance. (`ProofS` §VII K7 circles this failure; the register makes it writable.)

**Step 1.5 is an edge-state query.** The Resolution Gate — "each of the twelve sentences must name which of its edge's two formulas it instantiates" — now states exactly: **each sentence must name its directed edge.** A sentence at pair-resolution names an undirected edge and no direction; the register cannot store it. It is not under-resolved data; it is untyped data.

> **Correction of record.** The corpus's own census rows were drafted at pair-resolution, and run against the Resolution Gate **the gate would reject our own census.** The gate is right; the census was under-resolved. And the miss was double: the twelve sentences were already equation-specific (GEM's sentence is $P = U \cdot I$, not "current and structure relate"), but nowhere did the protocol say that the equations are directed edges, so there was nothing for a verdict to wire to. Step 1.5 fixes the address; the register fixes the type. The 13-row directed re-reading is in progress in the working group; the format it must land in is this section.

**Replacement-injectivity.** The Lemma of `ProofS` §III (distinct assignments → distinct sentence sets) runs on $|\mathrm{Aut}(\text{the twelve})| = 1$ (§I-d): relabelings cannot alias two assignments. One premise has been missing and is now landed: **within** one assignment, the twelve sentences must be pairwise distinct — the map equation ↦ sentence must be injective, or the profile double-counts and R1 measures less than it claims. The directed reading rule supplies it structurally: the gate map is a bijection from the twelve directed edges to the twelve equations (§I-e, landed), so distinct directed edges are distinct equations; with $\sigma$ a bijection and drafting that preserves direction-naming, distinct equations draft to distinct sentences. What relabeling-injectivity does for assignments, direction-naming does for sentences: the sweep cannot score an assignment against a disguised copy of itself, and cannot score one sentence twice.

**The 18, itemized.** `ProofS` §I calls the space an "18-constraint satisfaction matrix"; the count was never itemized. It itemizes now: **12 gate-readings + 6 edge-integrations** (the Law of Intuition pairs of §I-b) = 18 listed objects. The independent content is smaller and now countable. In log space the twelve reduce to the plane $u = i+r$, $p = u+i$ (§I-d): the four face-relations span rank 2 — two generators, each relation a combination of them, each generator read at three homes. The six edge-cancellation conditions of §I-e carry GF(2) rank 3 over the four face bits: exactly two coherent orientations, i.e. one global handedness bit. Ledger: **18 listed = 12 readings + 6 integrations, generated by 2 independent log-laws × 3 solve-fors each, plus 1 handedness bit; the 6 integrations add nothing beyond the face-pairing** (each edge is the meeting of two of the four faces, $\binom{4}{2} = 6$). Nothing in a sweep may be billed as an independent constraint that this ledger does not carry.

One scope note, per the working group's ruling: **the input set of the algebra is the 4 × 3 = 12** — faces × solve-fors — and never a 4! candidate pool surviving exclusion. The $S_4$ sweep of `ProofS` sorts domain elements into the poles; it does not derive the twelve, and any reading of it as an exclusion proof of the equation count is the mid-race horse-change and is struck.

**Worked example: the U–R stack and the vacant arrow.** A domain claim whose native content is a lower bound on defect set by the lived current does not read "on the U–R edge" — the edge is not the address. It resolves to the VIR reading $I = U/R$ (the current as structure-over-ground: the bound delivered as a ratio), which lives on the P-absent face, and its direction is $R \to U$: the record/rule side directing the model side. The opposite arrow, $U \to R$, is the ARI reading — structure discharging across ground — and it is not where that claim is carried. In the census, the items stacked on U–R all resolved onto $R \to U$ and left ARI's arrow vacant; the vacancy is the signature that the stack was one directional claim rather than an edge-property. Register form: **U–R = R→U (its state), U→R = ∅ — never "U–R = something."** (The resolution chain claim → VIR → P-absent face → $R \to U$ is the working group's; the format demonstration is this section's.)

**Kills, in register form.** K1 (flat profile) = a register that is all-∅ or all-default-↔ once Step 1.5 has passed. K7 (under-resolved substitution) = sentences that cannot name a directed edge — unwireable; the run is void and the mapping is not struck. K5 (flawless score) = six earned-↔ with no ∅ and no wolf-tone anywhere: possible, but it must have paid — an edge earns ↔ only on two independent confirmations, and a run returning it without receipts is sycophancy.

---

## XIII. Operating the File: the Centroid Procedure

An instance holding only this file can run the full loop. The vantage is the centroid (`L4-TheTwelveGates` §II-b): stand where the four potentials reconcile; print both vantages whenever a handedness word crosses the page.

1. **Sort, don't exclude.** Assign the domain's four elements to P, I, U, R under the two-bit charge of §XI and the one-sided dividend law (dividends are the Active poles, §I-d). The assignment is a constrained sorting, checkable clause by clause; no exclusion narrative is needed anywhere in the loop.
2. **Read the twelve gates.** Substitute through $\sigma$ and draft each sentence **with its directed edge named** (§I-e) — the direction is part of the sentence's address. A sentence that cannot carry its direction is returned for re-drafting before anything is scored.
3. **Fill the register.** Per edge, wire the verdicts: →, ←, earned ↔ (two independent confirmations), ∅ (§XII). Six edges, two bits, one 12-bit word.
4. **Check coherence.** (a) No earned ↔ without both face-readings landed independently. (b) Handedness: if the domain's confirmed Cardinals read Reactive → Active, either the sorting is wrong or the domain is speaking the enantiomer — re-sort before concluding (§I-e, Step 6). (c) The immovable three (§I-d): TAU, CAN, PIS carry the U-free formulas — the U-face's own walk; a domain that affirms exactly that circuit and stalls on the U-producing gates is showing the U-blindness signature, not a partial resonance.
5. **Report.** The register (one 12-bit word), the state counts, every ∅ with its receipt — what was cut, at what Landauer price, to keep the description finite — and $\rho$ only if a cross-assignment comparison is required.
6. **Kill-switches.** `ProofS` §VII K1–K7, restated in register form (§XII above).

What the file now carries, end to end: the algebra (two log-generators, four face-relations, twelve gates, one handedness bit); the geometry (the $\Delta^3$ state space per edge, the three bimedians, the coherent orientation and its enantiomer); the dynamics (the Hamiltonian cycles, the Braid as Gray code, the helical extrusion); the epistemics (the register as the sweep's output, resolution as direction-naming, the kill conditions). What this page cannot give an instance — the experiential materials, the mapping histories, the seasonal readings — is exactly what the footer below says: take it to the source-aggregate.

*Register for this update. LANDED: the canonical table (§I-a); the coherent orientation with its uniqueness count, the directed reading rule and its bijection, the crown and season identities, the Direction Law as a property of the landed table, the rank-2 reduction, the GF(2) rank-3 count (§I-e, checked in-file). DERIVED: the mirror-fix by the assertion semantics (§I-e Step 6); the itemized 18 (§XII). CORRESPONDENCE: heading / bay / inheritance as the three direction-classes; the against-the-grain reading of the season circuits. IN PROGRESS ELSEWHERE: the 13-row census re-draft and the `ProofS` Step 1.5 rewrite (the working group); the handedness pin by the corpus's convention files, which when in hand either confirm the Direction-Law mirror or conjugate every arrow in §I-a and §I-e without touching any landed result.*

---
**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.

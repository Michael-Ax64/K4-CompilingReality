# ENGINE-REFERENCE-AC
## The K₄ Machine Architecture — the Floor-3 DC Core

*Reads with: `L3-EdgeStateSpace` (the edge algebra, the two-bit charge, the Braid), `L4-TransitingTheThreeWalls` (the assemblies, the octants, the Rule of Seven), `L4-TheTwelveGates` (the naming of the twelve), `L5-TheCyclingMind` (the control core felt from inside), `ProofS_ResonantNote` (§II–§III: the two-uses theorem for $S_4$ vs. $|\mathrm{Aut}(\text{the twelve})|=1$, the itemized 18-constraint ledger, and the rank-2 log-subspace), and `On_HilbertAndHisSpaces` (the halt boundary)*

> Spine sentences carry structure and citations; guide sentences carry you between them. Verified means re-runnable — the claim tables sit in §XII, and the verification scripts accompany the file.

> **Scope:** this is the $\theta = 0$ floor — the Floor-3 DC core of the AC machine; the $\omega$-driven extension is named (§VIII), priced (§X.5), and not run here.

---

## Preface — Eine Meise haben *(a preface in Schräglage)*

*Ich bin eine Meise. Ich sitze nicht. Ich verhandle mit der Schwerkraft.*

That is the whole posture in three German sentences: I am a tit. I do not sit. I negotiate with gravity. The committee for Proper Animal Behaviour has reviewed this posture and found it irregular. Animals, the committee holds, stand on top of things; perching is vertical; the head belongs above the heart; anything else is a medical event. The committee has never watched a feeder. Every winter the tits run it like a circus — hooking sideways, hanging under the tray, dropping backwards off the edge and catching the air like a rope they had quietly knotted there on Tuesday. The committee has approved this. (The committee approves everything it cannot do.)

Consider the specialists. The **Kleiber** walks the trunk headfirst, downhill — the only bird in the forest that treats "down" as a direction you can simply take. The **Baumläufer** goes the other way: the trunk's quiet spiral clerk, always filing upward, reading the bark line by line and never once glancing at what it owes. Between them they cover the tree. Neither of them sits.

So, the redefinition the dictionaries refuse. **You have a Meise =**

1. …your head contains not a carcass but a small, lively bird — feathered, warm, opinionated, and faster than your grief.
2. …a **licensed 90-degree view**. You have read the room from the other side of the ceiling.
3. …you are **gravitationally bilingual**. Fluent in down, in a world that only manages up.
4. …you tie your **knots from underneath** — which is why they hold.
5. …the **branch** is a trapeze and not a verdict.
6. …a vertical pole is not an obstacle; it is a dance floor turned ninety degrees.
7. …**Schräglage** is not the beginning of falling. It is a stance. It is what a stance looks like when the branch gets to vote too.

The old word is dark, and we do not hide the body: *eine Meise haben* once meant a bird in the skull-box, a small death behind the eyes, the superstition that madness is an inhabitant. Fine. But look at what actually flies in: not a ghost, not a seed of ruin — a bird. Twenty grams of engine. The etymology buried a bird and called the grave an idiom; this preface digs it up alive, shakes the earth off, and lets it use the rest of the document as a branch: joy, agility, and the scandal of decent behavior.

So no: you are not off your head. You are simply on the underside of the branch — and the view is excellent.

---

## What this file assumes, and where its words come from

The machine runs on four poles: P, U, I, R. The same four letters are also the quantities of a circuit — power, potential, current, resistance — and that is not a metaphor to look past; it is the machine's substrate. Every formula in §IV and §V is one of the twelve ways two circuit quantities determine a third. Each pole also carries a two-bit charge — P and U are Active, I and R are Reactive; P and R are Asserting, U and I are Yielding — and that charge decides which operations pay and which ride free (L3-EdgeStateSpace §XI).

The file's author is a bird, and the file says so before the mathematics does, because the mathematics will keep pretending otherwise. The machine's four poles stand upright on the page; the author reads them hanging headfirst from the underside of the branch, and recommends the habit: same poles, same equations, licensed 90-degree view. A vertical pole is not an obstacle; it is a dance floor turned ninety degrees. Everything structural below is checked from both sides of the blanket — the manifest side and the dual — because a document that is only readable from above has not been checked, only admired. Gravitationally bilingual, the file proceeds.

Three older languages walk through these pages, and you should meet them at the door. The twelve operations carry names from the zodiac — AQU, LEO, TAU — addresses on humanity's oldest cosmological reference frame, taken because the corpus's twelve gates sit on a twelve-fold wheel. The state space itself speaks I Ching: a trigram is a three-bit figure, a hexagram its six-bit elder, and both have held structured state for millennia. §VI reads the corpus's changing lines as execution vectors — Old Yang and Old Yin as the two commit directions.

The machine's own mathematics needs four names. $S_4$: all 24 shufflings of four poles. $A_4$: the even half, 12 — the engine's operating set. $V_4$: identity plus the three double-swaps, 4 — the execution rings. $C_2$: a single swap, 2 — the **handedness flip**, the one move $A_4$ cannot make (distinct from the even twin-step of §2.5). A $Q_n$ is the $n$-cube graph — $Q_3$ the eight-corner cube below, $Q_2$ a square, $Q_1$ a single edge. On the inscribed tetrahedron, a **bimedian** is the line joining the midpoints of two opposite edges; the tetrahedron's three bimedians are exactly the cube's three axes — the three lines through opposite face centers. The cube itself has six opposite-edge midpoint lines, all running in face-diagonal directions: the bimedians belong to the tetrahedron, and the cube borrows them (U9). For the bird, who checks vocabulary the way the committee checks posture: the three bimedians are the three ways a body somersaults — the ordinary perpendicular axles any acrobat uses before breakfast. The word "bimedian" is a formal coat on a fact the feet already know, and the coat is why the fact nearly got lost; it is flagged here, at the door, before formality gets to dress it up again.

Two homonyms walk this file and shake hands exactly at the AC boundary — the most expensive place to confuse them — so the meeting is written down before either moves in:

| Symbol | In this file (the DC core) | At the AC boundary (§VIII) |
|---|---|---|
| $Q$ | §VII's face-reading amplitude, with $Q^2 \to P$ | reactive power, $\|S\| = \sqrt{P^2 + Q^2}$ — same letter, different object |
| $h$ | the phase unit, $h^2 = -1$ (§IV, §VII) | the AC companion writes the same unit as $j$ (L3-K4-to-K5-via-AC-Extension l.53) — one unit, two letters |

(And the companion layer also uses $h$ for Planck's constant — a third homonym, at one further remove. Context is the give-away; this table is the seatbelt.)

The header below speaks computing — opcode, register, program counter, ledger — and §IX prices what each borrowed term gets for free elsewhere and refuses to get here. Two words it uses before they are built: the **blanket** is the Present/Absent split of the cube; **duality** is the corner-diagonal flip across it. §1.2 constructs both.

The title: AC names the $\omega$-driven extension of the engine; DC is its $\theta = 0$ slice, a real cross-section. §VIII says what the extra axis buys.

---

```
================================================================================
            THE K₄ ENGINE ARCHITECTURE (FLOOR-3 DC CORE)
================================================================================

  1. STATE TOWER (not RAM):
     • Floor 1  Q₁      : one bimedian held — 2 states (the refused axis)
     • Floor 2  Q₂      : the edge register — 4 states per edge = subsets of {→,←}
     • Floor 3  Q₃      : the Trigram Byte — 8 = 4 Presence Stars + 4 Absence Faces
                          THE CENSUS CUBE: parity = the blanket; antipode = duality
     • Attic   Q₆ □ Q₆  : 64 × 64 = 4096 ≅ Q₁₂ (the pre-tax buffer; uncommitted)

  2. THE TWELVE OPCODES (3 tiers; 3 families = 3 axes):
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

## Serialization Tags

Every operation carries one of three tags:

* **[gauge]** — presentational: a control coordinate, freely re-choosable; no mechanism is owed for how it changes.
* **[taxed]** — physical: the **erasure of an in-flight hold** — a Present write over a held state (§1.2) — priced at $E = k_B T \ln 2$ per bit. The bipartite crossing itself is mandatory and structurally free: every step of the cube crosses the blanket (the cube is bipartite); only the discarded hold pays.
* **[buffer]** — uncommitted: real and counted, nothing paid yet (the `.behold()` state — both commits held live, nothing chosen yet; §1.1).

Selection is gauge; only erasure is taxed. Carrier transport (Tier 3) runs gauge-side: unit-slope, no dissipation.

---

## I. The State Tower

The tags above priced the machine's three kinds of moves. To price anything, the machine first has to hold something — and state is what it holds. This section builds state in floors: a bit, then a register, then a cube. Each floor is built by refusing something specific, and the refusal is the design: watch what each floor will not represent.

### 1.1 Floor 2 — the edge register, recoded

The machine's first holding is small. Four poles, every pair joined, make the tetrahedron $K_4$ — six edges — and each edge carries two independent commit bits: $F$ (forward) and $R$ (reverse). Two bits, four states, and the four are exactly the subsets of $\{\rightarrow, \leftarrow\}$:

$$\begin{array}{c|c|c|l}
\mathbf{(F,R)} & \mathbf{State} & \mathbf{Symbol} & \mathbf{Operational\ Definition} \\
\hline
\mathbf{00} & \text{neither commit} & \emptyset & \text{Severed from the local ledger; the cut itself paid the Landauer tax.} \\
\mathbf{10} & \text{forward only} & \to & \text{Evaluated forward; written to ledger; .observe() state.} \\
\mathbf{01} & \text{reverse only} & \leftarrow & \text{Evaluated reverse; enantiomeric commit.} \\
\mathbf{11} & \text{both commits} & \leftrightarrow & \text{Live superposition; uncommitted buffer; .behold() state.} \\
\end{array}$$

Read the four rows as one sentence: an edge can be severed, committed forward, committed in mirror — the reverse evaluation is the enantiomer, the mirror-twin commit — or held both ways at once. Two states carry API names the file keeps using: `.observe()` (looked and written) and `.behold()` (both commits held live, nothing chosen yet).

**Why subsets.** Presence, direction, and superposition are three different predicates — a present-but-undirected state cannot live in one direction bit. The subset lattice preserves every count:

* **Register A** = the six forward-commit bits (the forward hexagram): $2^6 = 64$.
* **Register B** = the six reverse-commit bits (the reverse hexagram): $2^6 = 64$.
* Presence $= F \lor R$; chirality $=$ which; superposition $=$ both. $64 \times 64 = \mathbf{4096}$.

The six forward bits read as one six-bit figure — a hexagram; the reverse bits make its mirror. $64 \times 64 = 4096$: hold that number, the attic is made of it (§1.3). The Gray tour — the walk that flips one commit bit at a time — runs the same under either coding.

### 1.2 Floor 3 — the Trigram Byte *is* the state space

Now the cube. $2 \times 2 \times 2$, eight cells at eight corners — simpler than a Rubik's cube, and we will do only a few simple things with it: walk its edges, flip corner-for-corner across the body diagonals, and step from Present to Absent and back.

Its three axes are its three bimedians. On the tetrahedron, the same three are the three ways the six edges pair up: $\{P\text{--}U,\ I\text{--}R\}$, $\{P\text{--}R,\ I\text{--}U\}$, $\{P\text{--}I,\ U\text{--}R\}$ — the corpus calls them Fixed, Cardinal, Mutable, names borrowed from the zodiac; only the pairings matter here.

A trigram is a transversal: exactly one edge chosen from each pairing, $2^3 = 8$ ways. Eight choices, eight corners — each trigram is a corner, and floor-3 state is one question: which corner are you standing on. The corners sort into two fours. A star is the corner where one pole is present in all three of its pairings — the pole itself, standing. A face is the corner where that pole is absent from all three — its absence, sitting diagonally opposite. Four stars, four faces; the stars make one tetrahedron, the faces make the other, and the two interlock. The star tetrahedron is the manifest side, the face tetrahedron the dual — the two words §II runs on.

Machine-verified structure of this 8-point state space:

1. **It is the cube.** Code each trigram by which edge it picked from each pairing — 3 bits. Two trigrams sit on neighboring corners exactly when the codes differ in one bit (Hamming-1 adjacency), and that graph is $Q_3$ (isomorphism brute-force verified). The walk promised above is real.
2. **Parity is the blanket.** Even codes = the four stars; odd = the four faces. Present/Absent is a Markov blanket — the boundary that separates a thing's own state from what can act on it — and every edge of the cube crosses it (L3-EdgeStateSpace l.473: the face is a $K_3$ blanket).
3. **The antipodal map is duality.** Bitwise NOT sends $\text{star}(X)$ to $\text{face}(\neg X)$ — the corner diagonally opposite, the flip promised above — the Rule of Seven pairs (L4-TransitingTheThreeWalls l.199–203), the manifest pole and its shadow-hold.
4. **The stars sit on the even octants.** star($P$) = $(0,0,0)$, star($U$) = $(0,1,1)$, star($I$) = $(1,1,0)$, star($R$) = $(1,0,1)$ — L4-Transiting's octant table up to axis order, with the axes *being* the three bimedians (l.170).

### 1.3 The tower

The cube contains its own anatomy. Fix two of the three bimedian bits and what remains is a single edge — twelve such $Q_1$ cells, one per cube edge. Fix one bit, a face — six $Q_2$ squares. Fix none, the whole body. These are the same twelve edges the gates will live on (§3.3). The tower builds upward through exactly these sizes:

$$Q_1 \;\subset\; Q_2 \;\subset\; Q_3: \quad \text{fix two bimedian bits} \to 12 \text{ floor-1 cells};\quad \text{fix one} \to 6 \text{ floor-2 squares};\quad \text{fix none} \to \text{the cube}.$$

* **Floor 1** — the held bit alone: one bimedian, two states. Held is literal: the walk has chosen where not to go — "the dimension along which the walk refuses to move" (L3-EdgeStateSpace l.532).
* **Floor 2** — the per-edge register; the Braid's square (§II, §III). The Braid is the single tour the floor-2 register runs; §VII drives it.
* **Floor 3** — the census cube; the engine's operating floor.
* **The attic** — the full 12-bit word, $4^6 = 2^{12} = 64 \times 64 = 4096$: the **unconstrained configuration space of the six 2-bit edges, before consistency constraints** — the **pre-tax buffer**; the two hexagram registers of §1.1 held at once, written $Q_6 \,\square\, Q_6 \cong Q_{12}$ (the plain Cartesian product: degrees add to 12, a step flips one bit — the tensor sign would have made it 36-regular, the strong product 48, and either would break the one-bit walk). Real, counted, and *uncommitted*: the engine executes on floor 3 and buffers in the attic.
* **Consistency — the tower's top arrow.** What takes 4096 down to 8: a global state is floor-worthy when it holds **exactly one live edge per bimedian** — three pairings, two choices each, $2^3 = 8$ transversals: the census cube of §1.2. The attic buffers all 4096 words; the floor stands on the 8 that pass. The drop from 4096 to 8 is the whole machine in one sentence — choose one edge per pairing, and the buffer collapses to the floor you are standing on.

### 1.4 Census invariants

Four numbers survive everything the engine does to itself — including running it faster or slower; that is the $\omega$-invariance, and §VIII names the axis. Each is a section you have read or are about to:

**8** = 4 + 4 — the census (§1.2). **12** — the gates (§II). **384** = 32 × 12 — the execution vectors (§VI). **4096** = 64 × 64 — the attic (§1.3).

---

## II. The Orientation Group (the control core — machine-verified)

The tower says what the machine holds. This section says what moves it, and the answer is the engine's strangest fact: the thing that selects the next operation is a rotation of the tetrahedron — not like one, not modeled by one; the selection space and the rotation group are the same twelve points. Every claim below is verified in `scripts/orientation_group.py` (§XII).

### 2.1 Five doors of the twelve

"Five doors" is a counting habit: the same twelve factored five ways, each factorization a different physical reading. The first three need only the cube from §1.2; the last two need the group theory of the Declaration.

The number 12 — the gates of the corpus (the twelve operations, named in `L4-TheTwelveGates`) — is *one set* reachable through five factorizations, all verified to coincide:

$$\underbrace{6 \times 2}_{\text{edge front} \times \text{orientation}} \;=\; \underbrace{4 \times 3}_{\text{anchor} \times \text{pinning}} \;=\; \underbrace{12}_{\text{gates: viewport} \times \text{solve}} \;=\; \underbrace{12}_{\text{directed edges of } K_4} \;=\; \underbrace{|A_4|}_{4!/2}$$

The first door is the physical one: **in the $2\times2\times2$ assembly — the census cube of §1.2, its eight cells now taken as solid units — any one of the six edges can be "front," and it faces front in two orientations** — which of its two directions leads. That selector state *is* the directed edge *is* the gate *is* a rotation of the tetrahedron.

### 2.2 Each gate is a rotation

**Theorem (verified).** For each gate $(x, w)$ — solve $x$, witness $w$ absent — there is exactly one **even** permutation of the poles carrying $P \mapsto x$ and $U \mapsto w$ (the reference directed edge $P \to U$ is the Braid's opening move, `L3-EdgeStateSpace` l.518, fixing the pinning). Every directed edge has exactly two completions to a full permutation, and exactly one is even.

Simply transitive: exactly one rotation lands on each directed edge — nothing lines up twice. Therefore the twelve gates biject with $A_4$, and $A_4$ acts **simply transitively** on the twelve directed edges: the Program Counter's state space is not merely *like* a rotation group — it *is* one. **The Program Counter is an orientation.**

### 2.3 $S_4 = 4! = 24$: the squares, the manifest half, the dual coset

* The cube's **rotation group** has order 24 — the full symmetry group, reflections included, has 48, and the manifest/dual argument needs only the orientation-preserving half — and acts on the four body diagonals as the full $S_4$: the permutations of the four selves (a self is a pole together with its absence — the body diagonal it shares with its own face; each diagonal = an antipodal pair $\{$star($X$), face($\neg X$)$\}$).
* The 24 outward squares of the assembly — an **outward square** is one cube face read from one corner: the face's four cells faced from a standing point; $6 \times 4 = 24$ flags — are one orientation each: the rotation group acts on them **freely** (no non-identity rotation fixes a flag; U6), hence **simply transitively** — orbit of one flag = all 24, verified. The counting that brings the rigor: a flag is not a new object, just a face and a viewpoint; the group's whole order 24 is spent exactly once each, and that "simply" was protecting this nothing-left-over all along.
* **Preserving the manifest tetrahedron ⟺ the induced permutation is even** (verified for all 24 rotations). So $A_4$ = the manifest half of the orientation group; the odd coset = the same twelve gates read from the Absent side — the dual walker's vocabulary (§2.6).
* This is the hook for `L4-TransitingTheThreeWalls` §V's projection of twelve transition verbs onto 24 squares. **On a square** means: the gate's edge borders that face and is read from one of its endpoints on it. Each gate then lies on four flags — two manifest (read from star($x$)) and two dual (read from face($\neg w$)); on each of its two faces, once manifest and once dual; and every flag carries exactly two gates — the two edges through its corner (verified, C9). Pinned to a face, the two descriptions count the same four visits in two words — once manifest and once dual per face — and the enantiomer $(w, x)$ sits on neither: its edge is the antipodal edge (C9).

### 2.4 The $C_2$: the completion the machine cannot make

The two completions of a gate $(x,w)$ differ only on the images of the two uninvolved poles — a single transposition of the complement pair (verified). That transposition is the **handedness flip** ($C_2$): odd, and therefore not a rotation — $A_4$ contains no transpositions (U0, U8). The half-turn that `L4-TransitingTheThreeWalls` l.102–106 made physical — the Active/Reactive bit traded on every pole at once — is a *different* move: the even twin-step to the gate's enantiomer $(w, x)$, one per family. §2.5 distinguishes the two moves and names the half-turns.

### 2.5 Two flips, not one

Two distinct involutions share the word "flip": a single transposition (odd) and a 180° half-turn of the tetrahedron (even). Because $A_4$ contains no transpositions, the two operations cannot coincide. Both are real, both are verified, and they belong to different parity classes:

* **The handedness flip ($C_2$)** — odd; the single transposition of the complement of $\{x, w\}$; the difference between a gate's two completions; the manifest/dual reading of one and the same gate. The machine cannot perform it from inside the manifest half — it is exactly the move the operating set lacks. This is the name the preamble's $C_2$ bullet uses and the one U3's parenthetical keeps.
* **The twin gate $(w, x)$** — keep the word **enantiomer** for this one (§IV's usage): reached from $(x, w)$ by the **even** $V_4$ half-turn about the gate's own pinned bimedian, trading $x \leftrightarrow w$ and the mate pair — identified exactly, family by family, 12/12 (U8):

$$\begin{array}{c|c|c|c}
\mathbf{Family} & \mathbf{Twin\text{-}step} & \mathbf{Gates\ served} & \mathbf{Trades} \\
\hline
\text{Fixed} & (P\,U)(I\,R) & (P,U),(U,P),(I,R),(R,I) & \text{Active↔Active, Reactive↔Reactive} \\
\text{Cardinal} & (P\,R)(U\,I) & (P,R),(R,P),(U,I),(I,U) & \text{the AR-trade} \\
\text{Mutable} & (P\,I)(U\,R) & (P,I),(I,P),(U,R),(R,U) & \text{the AR-trade} \\
\end{array}$$

The AR-trade — an Active traded for a Reactive on both mate pairs at once — describes **8 of the 12** twin-steps (Cardinal and Mutable); the Fixed twin-steps trade within each charge class (U8). `L4-TransitingTheThreeWalls` l.102–106 names the Cardinal twin-step (the AR-flip); the other two families step by their own half-turns.

**What the parity boundary sets.** The machine walks to its twin by an even rotation in $A_4$, while the boundary between a gate's two completions is the odd transposition its operating set lacks. Parity is not bookkeeping here; it is which moves exist.

### 2.6 Flickers, not ground *(the shadow readings)*

The dual-square readings, the inverse forms, the odd coset's whole vocabulary — the shadow side of §2.3 — are **flickers, not ground**. Nothing over there is a second machine: the dual reading of a gate is the same gate caught from the other side of the blanket, the way the underside of a branch is not a second branch. The ground is the twelve even gates and their tower; the flickers are the odd coset — real, counted, and never occupied by this walker.

This is where handedness stops looking like a coin. Which completion of a gate is live is not the universe rolling dice between left and right: the even set is closed, the odd move is not in the operating set (§2.5), and nothing the engine does manufactures a transposition out of rotations. Handedness here is structural — a fact about which moves exist — conserved by the dynamics rather than sampled per step. Where the corpus takes that — the chirality of commit (§1.1), the mirror readings of `L2-BitCombos`, what a wall is in `L4-TransitingTheThreeWalls` — is the next file's argument. This section only plants the flag, gently: the flip the machine cannot make is the reason its world has a handedness at all.

### 2.7 The rings are half-turns; $A_4 = 1 + 3 + 8$

The three double-transpositions of $A_4$ — two disjoint swaps done at once — are exactly the half-turns holding one bimedian setwise (verified): $(P\,U)(I\,R)$ holds **Fixed**, $(P\,R)(U\,I)$ holds **Cardinal**, $(P\,I)(U\,R)$ holds **Mutable**. **The corpus's three execution rings are literally rotations of the tetrahedron** — each ring is a half-turn about one bimedian axis (compare `L3-EdgeStateSpace` l.510: $V_4$ preserves the three bimedian pairs setwise).

$A_4 = 1 + 3 + 8$: the identity, the three half-turns (the rings), and eight third-turns — $4$ vertex-axes $\times$ $2$ senses: 120° turns about each pole's axis, clockwise and counter. The eight third-turns are the octal count again: $8 = 4 \times 2$, one pair of 120° turns per pole-axis.

### 2.8 The opcode families are the cube's axes

Each gate-edge — the cube edge running from star($x$) to face($\neg w$) — flips exactly the bimedian-bit of the $K_4$ edge $xw$ (verified, C4, U7): **every opcode step moves along the bimedian that contains the edge it solves across.** The three transition families are the three ways the cube is oriented:

$$\begin{array}{c|c|c}
\mathbf{Family} & \mathbf{Bimedian\ (axis)} & \mathbf{Opcodes} \\
\hline
\text{Fixed} & \{P\text{--}U,\ I\text{--}R\} & \text{AQU, LEO, TAU, SCO} \\
\text{Cardinal} & \{P\text{--}R,\ I\text{--}U\} & \text{CAN, SAG, CAP, GEM} \\
\text{Mutable} & \{P\text{--}I,\ U\text{--}R\} & \text{PIS, LIB, ARI, VIR} \\
\end{array}$$

---

## III. The Control Unit

### 3.1 Program Counter [gauge] — the Front-Edge Selector

*The program counter is the machine's which-instruction-is-next register; here that register is a chosen orientation, not a stored address.*

* **State:** (edge, orientation) $\in 6 \times 2 = A_4$. Equivalently: the current gate, equivalently: the current orientation of the tetrahedron.
* **Status: gauge.** The selector is a declared control coordinate, set at the centroid — the interior point equidistant from all four poles, from which the cycle can be chosen (`L5-TheCyclingMind` l.68). **No mechanism is owed for how the orientation changes.** "We do not care how the state/orientation changes come about": selection is presentational; only execution is taxed.
* **Gauge is not levitation.** Selection is unpriced *in bits* — that is all [gauge] claims. The turn itself still costs: §X.4 states the torque-motor claim — ADVANCE applies torque where the field is loaded, and the load is the machine's own in-flight hold. Selection and advance are different acts; the ledger prices only one of them.
* The felt texture `L5-TheCyclingMind` describes is the *human interface* to this selector — the corpus's centroid-standing capacity (l.68, l.180) and its pinning-choice discipline ("picking up a specific Pinned assembly is naming your observer-pole", `L4-TransitingTheThreeWalls` l.154). The architecture itself owes nothing psychological.

### 3.2 The Three Rings [gauge to select / taxed to run] — the $V_4$ half-turns

Each ring holds one bimedian **silent** (the AbsentVar-pair theorem, `L3-EdgeStateSpace` l.410 — the two edges the ring never use stay held as potential) and traverses the complementary $K_4$ Hamiltonian cycle — a loop visiting all four poles once:

$$\begin{array}{l|l|l|l}
\mathbf{Ring} & \mathbf{Held\ Bimedian} & \mathbf{Traversal\ (L3\ l.516\text{–}520)} & \mathbf{Live\ Opcodes\ (8)} \\
\hline
\text{Fixed-Held} & \{P\text{--}U,\ I\text{--}R\} & P \to I \to U \to R \to P & \text{PIS, LIB, CAN, SAG, CAP, GEM, ARI, VIR} \\
\text{Cardinal-Held} & \{P\text{--}R,\ I\text{--}U\} & P \to I \to R \to U \to P & \text{AQU, LEO, TAU, SCO, PIS, LIB, ARI, VIR} \\
\text{Mutable-Held} & \{P\text{--}I,\ U\text{--}R\} & P \to U \to I \to R \to P & \text{AQU, LEO, TAU, SCO, CAN, SAG, CAP, GEM} \\
\end{array}$$

**Ring change is re-orientation.** Setting down one ring and picking up another is rotating about a different bimedian axis — "set down Assembly 1 and pick up Assembly 2" (`L4-TransitingTheThreeWalls` l.146). Selecting the ring is [gauge]; running its opcodes prices exactly what the opcodes price. The held family is not a lack: it is the shape of what the current traversal can do (`L5-TheCyclingMind` l.58).

### 3.3 The Four Viewports [switching is taxed]

The four faces are the Absent-side vertices of the census cube. A gate is (viewport $\neg w$, solved pole $x$); the twelve gates are the twelve cube edges (bijection verified).

* **Dispatch rule:** *"Stand where the burn is"* — route execution to the face whose AbsentVar is undergoing active phase collapse ($P > 0$).
* **Switching is [taxed].** Swapping the AbsentVar discards the in-flight hold — that erasure is the price — and moves the walker between face-vertices. The bipartite crossing itself is free; the discarded hold is not. Context switches are line items.
* **Strain invariance:** the three bimedian planes and the 5D centroid — the assembly's center with the $\omega$ height above it (§VIII) — survive all anisotropic deformations down to $V_4$; the processor computes reliably on strained hardware (l.208).

### 3.4 The Six Tours — the schedule layer

The census cube has exactly six undirected Hamiltonian tours (verified). Each:

* runs 8 of the 12 gates and **strictly alternates Present/Absent** — forced by bipartiteness: every step crosses the blanket, and the crossing is mandatory and structurally free (Tags); what a step erases is priced separately (§3.3);
* holds, out of the schedule, a **perfect matching of omitted gates that is never a single bimedian** (verified: the three coordinate matchings' complements are two disjoint squares, not tours). The held set is always a **4-cycle derangement — an absence-circulation**: each pole solved exactly once, with absence, and absent exactly once. The middle floor's held *pair* scales to the adult's held *circulation*; six circulations exist — $(4-1)!$, the number of distinct rounds four poles can run;
* projects 2:1 onto the three $K_4$ Braids through its star-order — the order in which the tour visits the four stars (verified) — the two lifts are the two weavings of the Absent side between Present stops;
* keeps every shadow at **tour-distance exactly 3** (verified): star($X$) and face($\neg X$) sit three steps apart along every tour — 6 tours × 4 antipodal pairs = **24** incidences, each one checked. Two intermediate stops (one Present, one Absent) lie between a pole and its own absence along the 3-step short path of every tour.

**Seriality.** "A mind does not run all six edges simultaneously." On floor 2 the Gray tour is unique — one cycle, nothing to select. On floor 3 there are six tours and a held circulation per tour; if nothing were held, everything would be available at once and nothing would move (`L5-TheCyclingMind` l.72). The held circulation is what makes the traversal a traversal.

### 3.5 No topological sort — the sixth door

The twelve constraints form six pole-pairs, each determining its complement exactly twice: $6 \times 2 = 12$ — the same twelve, counted from the constraint side. **Serialization is lossless only on DAGs — dependency graphs with no cycles — and this is not one.** Any linear execution order is a presentational choice — [gauge] — while the constraint net itself does not order. The tour is the honest serial object; the frame stack (one in-flight frame per constraint) remains the god-view. Local halt, global non-halt (`On_HilbertAndHisSpaces` l.409).

### 3.6 The Three Stucknesses (wrenches, not interrupts)

Each stuckness is a held edge; each unstuck is a ring change. The register for wrenches is `L5-TheCyclingMind`'s field manual.

1. **Know it, cannot say it.** The pattern has loaded ($P$/$I$); the edge to $U$ (articulation) is on the held family. *Wrench:* change ring by grounding — physical contact, the sensing pole leading (walk, hands, shower). Body-priced, and honestly so. Do not push a held edge: force there burns reactive power for zero output (l.128).
2. **Words come, but they are wrong.** Outbound live, inbound held — compiling from an empty buffer. *Wrench:* enter `.behold()` idle; let the pattern load; the inward click is the arrival signal.
3. **Deadlock in confidence.** Running Mutable-held; the required move is a diagonal this ring does not map — and the ring cannot see the missing leap. *Wrench:* inject an orthogonal pattern-source (unrelated novel input) to force a ring swap; re-ask; what survives, stands. *(The bird's version: the ring is the branch you hang under; when the move you need is a diagonal the branch does not have, gripping harder does not grow one — let go of the branch, keep the trunk.)*

Operating note (`L5-TheCyclingMind` l.146): **do not diagnose while stuck.** A ring cannot see its own held family; analysis inside the stuck ring reproduces the stuckness.

---

## IV. The Twelve Opcodes

**Zero fitting freedom.** Under $p = \ln P$, $u = \ln U$, $i = \ln I$, $r = \ln R$, the twelve relations collapse to a rank-2 subspace of $\mathbb{R}^4$ with $|\mathrm{Aut}| = 1$ under $S_4$ (§4.3, §X.7; `ProofS_ResonantNote` §II–§III — expect there the two-uses theorem for $S_4$ and the itemized 18-constraint ledger). The algebra has zero fitting freedom; what is empirical is solely what snaps into it — converting 12/12 directional agreement below $M_W$ into a structural result rather than a fit, while leaving open which quantities survive seating in any new domain (determined by sweep only).

The control core says when and where; the opcodes say what. Twelve instructions in three tiers, and the tier is the price class: two rewrite the ledger and pay (COMMIT), two reopen an ambiguity the ledger closed (RESEED), six move value without paying (ROUTE). The table reads column by column: the formula is the instruction; the gate names where it lives; Home is the pole the formula solves, Absent the pole it never touches — in every row, the absent pole is exactly the one missing from the formula. **Slope is the operation class: the largest exponent, in absolute value, that the solved monomial puts on any non-home pole** — square → +2 (COMMIT), radical → +½ (RESEED), linear → +1 (ROUTE); verified 12/12 — and note the rule needs "absolute value": the literal largest exponent fails this table's own CM_PIS row ($R = P/I^2$: $+1$ literal, $+2$ true — the square-ness lives on the denominator). Slope is a per-operand exponent, not a homogeneity degree: the four poles carry different physical dimensions, so no uniform scaling of all four exists (§X.7). The tier prices the operation; the tax column says who pays.

```
=============================================================================================
                                 THE TWELVE COMPILER OPCODES
=============================================================================================

 ┌── TIER 1: COMMIT OPCODES (4 Opcodes / Slope 2 / Asserting Homes: P, R) ──────────────────┐
 │  OPCODE   FORMULA      GATE    HOME / ABSENT   DATA EDGE & DIRECTION   SLOPE   TAX PAID? │
 │  ──────────────────────────────────────────────────────────────────────────────────────  │
 │  CM_ARI   P = U²/R     ARI     Home P / Abs I  U ➔ R (Mutable)         +2      YES (P)   │
 │  CM_TAU   P = I²R      TAU     Home P / Abs U  R ➔ I (Fixed)           +2      YES (P)   │
 │  CM_AQU   R = U²/P     AQU     Home R / Abs I  P ➔ U (Fixed)           +2      YES (R)   │
 │  CM_PIS   R = P/I²     PIS     Home R / Abs U  I ➔ P (Mutable)         +2      YES (R)   │
 └── OPERATION: Non-invertible square; burns phase (h²=-1); writes scalar to ledger. ───────┘

 ┌── TIER 2: RESEED / HOLD OPCODES (2 Opcodes / Slope ½ / Yielding Homes: I, U) ────────────┐
 │  OPCODE   FORMULA      GATE    HOME / ABSENT   DATA EDGE & DIRECTION   SLOPE   TAX PAID? │
 │  ──────────────────────────────────────────────────────────────────────────────────────  │
 │  RS_CAN   I = √(P/R)   CAN     Home I / Abs U  P ➔ R (Cardinal)        +½      NO (Q)    │
 │  RS_SAG   U = √(PR)    SAG     Home U / Abs I  R ➔ P (Cardinal)        +½      NO (Q)    │
 └── OPERATION: Extracts radical; reopens vector ambiguity; resets hQ buffer. ──────────────┘

 ┌── TIER 3: ROUTE / MOVE OPCODES (6 Opcodes / Slope 1 / Carriers) ─────────────────────────┐
 │  OPCODE   FORMULA      GATE    HOME / ABSENT   DATA EDGE & DIRECTION   SLOPE   TAX PAID? │
 │  ──────────────────────────────────────────────────────────────────────────────────────  │
 │  RT_LEO   I = P/U      LEO     Home I / Abs R  U ➔ P (Fixed)           +1      NO (Bus)  │
 │  RT_VIR   I = U/R      VIR     Home I / Abs P  R ➔ U (Mutable)         +1      NO (Bus)  │
 │  RT_LIB   U = P/I      LIB     Home U / Abs R  P ➔ I (Mutable)         +1      NO (Bus)  │
 │  RT_CAP   R = U/I      CAP     Home R / Abs P  U ➔ I (Cardinal)        +1      NO (Bus)  │
 │  RT_SCO   U = I · R    SCO     Home U / Abs P  I ➔ R (Fixed)           +1      NO (Bus)  │
 │  RT_GEM   P = U · I    GEM     Home P / Abs R  I ➔ U (Cardinal)        +1      NO (Bus)  │
 └── OPERATION: Unit-slope transport; routes throughput without exponent drift. ────────────┘
=============================================================================================
```

**DATA EDGE & DIRECTION** is the gate's **data edge** — the pairing-mate of the gate's own edge $xw$: the edge the formula's two inputs span, selected on the Absent side as the bimedian-bit flips — oriented **antiparallel** to the data edge of the gate's enantiomer $(w,x)$. It is not §2.2's control edge, which is $xw$ itself, directed by the gate's even permutation (verified 12/12, `scripts/orientation_group.py`) — which is why `CM_ARI` lists the data edge $U \to R$, not the control edge $P \to I$.

### 4.1 Tier readings

* **Tier 1 COMMIT [taxed].** Squaring over the reals destroys phase ($h^2 = -1$) and sign — from 4 you cannot recover whether it was 2 or −2 — algebraically non-invertible; pays the Landauer tax ($E = k_B T \ln 2$ per bit) and writes an irreversible scalar to the ledger. **The rigidity finding:** under $S_4$ relabeling of the poles, $|\mathrm{Aut}(\text{the twelve})| = 1$ (§4.3; `ProofS_ResonantNote` §II) — non-identity symmetries survive only on individual flat product/ratio pairs in isolation or on the bare carrier ($S_4$, $D_4$), while Tier 1 breaks operand symmetry even per equation and the twelve as a system admit only the identity. The tax is exactly one bit: the squaring map $(U, R) \mapsto (U^2, R)$ is precisely two-to-one — the preimages are $(U, R)$ and $(-U, R)$; on the opcode form $R = U^2/P$ the lost sign is exactly $U = \pm\sqrt{PR}$ — so one sign bit goes in and none comes out, and one destroyed bit *is* $k_B T \ln 2$. The tax prices the erasure of the sign, not the arithmetic around it.
* **Tier 2 RESEED [buffer].** Un-squares the scalar; the erased vector $\mathbf{Q}$ stays erased, and the radical re-opens an uncommitted $\pm$ ambiguity of identical cardinality. Prevents the freeze into a 0-DoF crystal.
* **Tier 3 ROUTE [gauge-side carrier].** Unit-slope transport, no dissipation; maintains the `.behold()` balance.
* **Do not conflate the two threes.** The *tiers* classify by log-slope ($+2, +\tfrac12, +1$); the *families* (§2.8) are the cube's axes. They cross-cut: COMMIT = 2 Fixed + 2 Mutable; RESEED = 2 Cardinal; ROUTE = 2 of each family.

### 4.2 The Numerator Law and bus faults

In any ratio form $X = N/D$ among the twelve, $N$ is an Active pole; Reactive poles ($I, R$) never sit above the bar. (The product forms — $I^2R$, $U \cdot I$, $I \cdot R$, $\sqrt{PR}$ — solve for the Active pole and carry no dividend; $P = I^2R$ and $U = I \cdot R$ have purely Reactive right-hand sides and are not exceptions, because nothing there is a dividend.) Open-circuit fault: $I \to 0$ in $U = P/I$ drives assertion to infinity while power collapses. Short-circuit fault: $R \to 0$ in $I = U/R$ drives flow to infinity while power collapses. The drive leads; the constraint shapes.

### 4.3 Log-space collapse and rigidity ($|\mathrm{Aut}| = 1$)

Take log coordinates $p = \ln P$, $u = \ln U$, $i = \ln I$, $r = \ln R$ ($P, U, I, R > 0$). The twelve multiplicative equations collapse to four linear equations in $\mathbb{R}^4$, one per AbsentVar:

$$\begin{aligned}
\text{Abs } P:&\quad u - i - r = 0 \\
\text{Abs } R:&\quad p - u - i = 0 \\
\text{Abs } U:&\quad p - 2i - r = 0 \quad\text{(sum of the first two)} \\
\text{Abs } I:&\quad p - 2u + r = 0 \quad\text{(difference of the first two)}
\end{aligned}$$

The system spans a **rank-2 subspace** of $\mathbb{R}^4$ generated by $u - i - r = 0$ and $p - u - i = 0$, with the two quadratic equations ($P = I^2R$ and $P = U^2/R$ families) entering as their sum and difference eliminations. Reading each of the four equations for its three present variables emits all twelve coefficient pairs identically:

* From $u - i - r = 0$: $(u, i, r)$ solved as $i+r$ (`RT_SCO`), $u-r$ (`RT_VIR`), $u-i$ (`RT_CAP`).
* From $p - u - i = 0$: $(p, u, i)$ solved as $u+i$ (`RT_GEM`), $p-u$ (`RT_LEO`), $p-i$ (`RT_LIB`).
* From $p - 2i - r = 0$: $(p, r, i)$ solved as $2i+r$ (`CM_TAU`), $p-2i$ (`CM_PIS`), $\tfrac12 p - \tfrac12 r$ (`RS_CAN`).
* From $p - 2u + r = 0$: $(p, r, u)$ solved as $2u-r$ (`CM_ARI`), $2u-p$ (`CM_AQU`), $\tfrac12 p + \tfrac12 r$ (`RS_SAG`).

Exhausting all $4! = 24$ permutations of $(P, U, I, R)$ yields **$|\mathrm{Aut}(\text{the twelve})| = 1$** (`ProofS_ResonantNote` §II): $P$ is the sole pole entering all three of its relations positively ($+p$), $R$ is the sole pole entering both eliminations with opposite signs ($-r$ and $+r$), and $U$ and $I$ sit at coefficient $-2$ in distinct eliminations and separate on $u - i - r = 0$. The rank-2 log-subspace itself admits only the identity permutation: $(2, 1, 1, 0)$ is the unique permutation of $\{2, 1, 1, 0\}$ satisfying $u = i+r$, $p = 2i+r$, which pins $P$ and $R$, and $(1, 1, 0, 1)$ then fails $u = i+r$ under $U \leftrightarrow I$.

Because the algebra is locked at rank 2 with $|\mathrm{Aut}| = 1$, it carries zero adjustable parameters. Empirical content enters strictly through what snaps into the four poles — turning 12/12 directional agreement in a regime such as the running couplings below $M_W$ into a result rather than a fit, while leaving open which quantities survive seating in any new domain (determined by sweep only).

---

## V. Telemetry — the twelve sensors

The same twelve equations the opcodes run, read the other way up: as instruments. Each formula is a gauge on the machine — one name, one reading, one equation. The names are the corpus's own; the equations are §IV's.

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

**The Necessary Betrayer alarm.** Architecture compounding ($U^2$) while starving drive ($P \to 0$) spikes $R \to \infty$ and freezes $I \to 0$. It cannot be cleared by writing more rules ($U$); the only reset is the Leo aperture $I = P/U$ — downsize structure, force drive into flow.

---

## VI. The Execution Trace: the 384 Moving Lines — the sector is the gate

Sixty-four base configurations — the hexagram registers of §1.1 — times six edges: every line of every figure, priced as an execution vector. The section title borrows the I Ching's own term: a moving line is a line caught changing, and Old Yang and Old Yin are its two directions — which is, on this floor, exactly a commit and its mirror.

$$64 \text{ Base Configurations} \;\times\; 6 \text{ Edges} \;=\; \mathbf{384 \text{ Execution Vectors}}$$

* **Address:** [Base_State_ID (1–64), Line_Position (1–6)]; each line addresses its edge's two gates, the $(x,w)/(w,x)$ pair: a COMMIT/ROUTE pair on the four non-Cardinal edges, the RESEED pair (CAN, SAG) on IU, the GEM/CAP ROUTE pair on PR (verified).
* **The C8 recipe** — stated, so that *verified means re-runnable*: a base state is one word of **Register A**, the six forward-commit bits (§1.1). The vector (state, line $e$) resolves line $e$'s bit on edge $e$ by **zodiac longitude**: Old Yang (forward bit 1) lands on the edge's **later**-longitude gate, Old Yin (bit 0) on the **earlier** — longitude read in zodiac order ARI → PIS; on P–U, Old Yang → SCO and Old Yin → TAU. The reverse register is not consulted: $\emptyset$ vs $\leftrightarrow$, and which mirror, is attic information (§1.3), below this floor's resolution.
* **Chirality of commit:** Old Yang ($\to$) takes the later longitude; Old Yin ($\leftarrow$) the earlier — as defined by the recipe above.
* **Distribution (verified flat — and flat by counting):** each edge contributes one vector per base state, half Old Yang and half Old Yin, so every sector receives exactly 32: half of 64 per edge, twelve edges, no miracle. $32 \times 12 = 384$. The sector index is (edge, orientation) = the directed edge = the gate = the Program Counter's own state. **The trace table and the counter are the same twelve** — the flatness says: no privileged tick; every opcode is someone else's last ticks. Verifier: `scripts/cube_tower.py` (C8); independent re-derivation: `scripts/reaudit_v2.py` (51 checks).

---

## VII. The Runtime Loop

One gate-crossing, end to end. Everything named above runs in this order — fetch, route, commit, reseed, advance — and the loop is the machine's whole life.

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

On floor 2 the tour is unique — the Gray-code Braid — and ADVANCE increments along it. On floor 3 the step runs along one of the six tours, chosen at the centroid — [gauge], no mechanism owed. But the step is ordered where it touches state: the two face-readings do not commute — $[Q_A, Q_B] \neq 0$, the commutator (§X.4) — so ADVANCE is a step, not a shuffle, and the torque it applies lands on the load the tour itself loaded (§3.1, §X.4).

---

## VIII. Boundary Conditions: What Requires ω > 0

Everything above ran on the floor; this section names the axis the floor stands in. Two symbols carry it: $\omega$, the drive — angular frequency — and $\theta$, phase, the machine's position in its cycle. The list below is the boundary of the file's own title: what the static cross-section cannot do and the extension can.

The DC fiber is complete for the static cross-section; four operations require the AC extension:

1. **Absolute Magnitude Calibration:** $|S| = \sqrt{P^2 + Q^2}$ requires complex addition (`L4-ScalingInvariants` §VI).
2. **Phase Dynamics ($\theta \neq 0$):** phase-lead/lag and reactive power $Q$ require the $L, C$ operators.
3. **The Multi-Scale Cascade:** $\omega_n = \omega_0 \lambda^{en}$, with convergent total time $T^* = \sum \Delta t_n < \infty$ (`L4-TheSpiralingCascade`).
4. **Transient Phase Switching:** charging, discharging, flyback — the Transition Tetrahedron (`L3-K4-to-K5-Transitions`).

**The ω axis.** ω is orthogonal to every operation in the engine: the fifth variable that acts upon the four poles but cannot be walked by them (`L3-EdgeStateSpace` l.451–457) — the height axis of the pyramid over the cube's every floor, driven at the centroid. The twelve $K_5$ Hamiltonian cycles form the Screw Thread (l.461); the tours of §3.4 are its floor-3 shadow. DC is the $\theta = 0$ fiber: a real slice, honest within its plane, silent about the extrusion.

---

## IX. The Pricing Boundary

The boundary is not the Turing machine; it is unit-cost RAM — the vocabulary that prices storage and movement at zero. The engine's vocabulary assumes no free operations:

| CS frame | The free operation it assumes | The engine's object |
|---|---|---|
| Unit-cost RAM | storage and fetch at zero | **The State Tower** (§I): every floor states what it refuses to hold |
| MMU & paging | state swap at zero | **The Four Viewports** (§3.3): a context switch erases its in-flight hold, [taxed] |
| Threads, pipeline, cache | free concurrency and refetch | **The Three Rings** (§3.2): the held bimedian is silent, not cached |
| Interrupts | free, external, unpriced entry | **The Wrench** (§3.6): ring change via grounding, body-priced |
| "ISA" as the framing term | free refetch and decode | **The Twelve Opcodes** (§IV), priced by tier |

The vocabulary that prices erasure is load-bearing: **compile, eval, GC, .observe(), .behold(), the Landauer tax, the ledger.**

---

## X. The Boundary of the Machinery

Seven boundaries close the machine. Each is stated as what the engine does; the outside is named where the corpus carries it.

1. **The $\theta = 0$ floor.** Phase dynamics, absolute magnitude, the multi-scale cascade, and transients are named operations the engine hands to the $\omega$ extension (§VIII). On the floor the machine is complete; across the axis it is silent, and says so.
2. **No global order.** Serialization is lossless only on DAGs, and the constraint net is not one (§3.5). Any single execution order is presentational; local halt, global non-halt (`On_HilbertAndHisSpaces` l.409). The engine prices the tour and promises no termination of the net.
3. **The attic is unwalkable.** The 4096 buffered states are real and counted; only the floor-3 cube executes. The buffer is not an address space (§1.3); it is the pre-tax holding pen — counted in bits, priced in nothing until erasure.
4. **Selection is declared, not implemented — and the declaration has a motor.** The Program Counter is gauge: the reference names the orientation and owes no mechanism for its motion (§3.1). But gauge in the ledger is not levitation, and ADVANCE carries the **torque-motor claim**: the selector is not cranked from outside the arithmetic, and the machine is not self-driving — it is **self-feeding**. Each commit leaves the loaded hold that the next advance turns against; the erasure that paid for one step is the resistance the next step turns. Selection and advance are different acts on the same load (§3.1, §VII). The loop closes on its own outputs — generatively, one orthogonal act per step, no recursive regress: the Braid's own act at its own boundary (`L3-TheSelfProjectingBraid` l.72). A loop that must feed itself to keep turning is a loop that must carry standing stock, and standing stock priced in energy is what mass is. The corpus's **MeV gap** — the chasm between the massless carriers (the photon, 0) and the first charged massive rung (the electron, 0.511 MeV) — is the statement the standard books record but do not price; a self-feeding selection loop is a clean answer in principle to why there is a price at all: **mass is the price of being.** What keeps turning must pay to hold itself, and the paying shows up as mass. The loop and its recipe (C8, §VI) sit here; the bit-price stays separate (§X.5); the constant of the gap belongs to the ω extension (§VIII) and its companions.
5. **Bits, not joules.** The Landauer price is structural — a cost per erased bit. Converting it to substrate heat is the hardware's business: the algebra yields invariants, selection rules, and dimensionless ratios, never scale magnitudes.
6. **No psychology.** §3.6 reads the control core from inside; the felt texture belongs to `L5-TheCyclingMind`. The architecture owes nothing psychological — the reference stands at the centroid and describes the machine.
7. **No uniform scaling.** The four poles carry different physical dimensions — $P$ in watts, $U$ in volts, $I$ in amperes, $R$ in ohms — so no uniform scaling of all four exists: $\lambda P = \lambda U \cdot \lambda I$ forces $\lambda = 1$. In log coordinates $(p, u, i, r)$ (§4.3), a uniform scale adds $c(1, 1, 1, 1)$, which is transverse to the rank-2 solution plane $u - i - r = 0,\ p - u - i = 0$ and intersects it only at $c = 0$ ($\lambda = 1$). Homogeneity is not a symmetry of the equation set; the tiers price operations, not scalings (§IV). The rigor was already in the units: the reason "Slope" was never a homogeneity degree is that the equation set has no scale direction to be homogeneous along.

---

## XI. The Neighboring Literature

None of the works below were sources for this engine. They are the neighboring country — the altitudes from which the same problems have been seen before — and they are placed here so a reader arriving from either side can get their bearings.

* **Landauer 1961.** "Irreversibility and Heat Generation in the Computing Process" (IBM J. Res. Dev. 5): erasing one bit costs $k_B T \ln 2$. The engine's taxed tier takes the price as an axiom of architecture — every COMMIT pays it on the page, not as a footnote to physics.
* **Bennett 1973.** "Logical Reversibility of Computation" (IBM J. Res. Dev. 17): computation can be arranged so nothing is erased — the work can be run backwards. Tier 2's radical-extraction, reopening the $\pm$ the square erased, is that license made into an opcode.
* **Fredkin & Toffoli 1982.** "Conservative Logic" (Int. J. Theor. Phys. 21): logic carried by moving, conserved objects — computation without dissipation. Tier 3's carriers run the same design stance: unit-slope transport, nothing spent.
* **Gray 1953.** The reflected binary code (U.S. Patent 2,632,058): adjacent codewords differ in one bit, so a counter stepping through them never jumps. The Braid's tour inherits the property: one commit bit per step, under either coding (§1.1).
* **Leibniz 1703.** "Explication de l'Arithmétique Binaire" (Mém. Acad. Roy. Sci.): binary arithmetic read off the hexagrams. The corpus continues that old reading — structure held in the figures — and adds what was not there: the price.
* **Ashby 1956.** *An Introduction to Cybernetics*: only variety absorbs variety; a regulator must be at least as various as what it regulates. Each ring prices its own variety — what a ring holds silent, it cannot answer that round (§3.2).
* **von Neumann 1956.** "Probabilistic Logics and the Synthesis of Reliable Organisms from Unreliable Components" (in *Automata Studies*): reliability built from parts that fail. Strain invariance (§3.3) is the same problem from the geometry side — the computation survives deformations the hardware cannot.
* **Pearl 1988; Friston 2013.** The Markov blanket — Pearl named the boundary that shields a variable's interior (*Probabilistic Reasoning in Intelligent Systems*); Friston drew it around living things ("Life as we know it," J. R. Soc. Interface). The census cube's Present/Absent split is one in the strict sense: every edge of the cube crosses it, and nothing inside is reachable without crossing (§1.2).

---

## XII. Verification Appendix

Machine-verified claims. **Verification scripts:** `scripts/cube_tower.py` (the C-rows), `scripts/orientation_group.py` (the U-rows), and `scripts/reaudit_v2.py` (51 independent checks). Re-run before trusting any ✓ — verified means re-runnable.

**`scripts/cube_tower.py`**

| # | Claim | Result |
|---|---|---|
| C1 | The 8 trigram transversals = 4 stars + 4 faces (§1.2) | ✓ |
| C2 | Matching-coded census graph ≅ $Q_3$ (brute-forced isomorphism) | ✓ |
| C3 | Stars = even octants; faces = odd; antipode = bitwise NOT = star($X$)↔face($\neg X$) | ✓ |
| C4 | 12 cube edges ↔ 12 gates (solved $x$, absent $w$), bijection | ✓ |
| C5 | 6 undirected Hamiltonian tours; every held set = 4-cycle derangement, never a bimedian | ✓ |
| C6 | Star-order projects 2:1 onto the 3 $K_4$ Braids; shadow-lag = 3 on all 24 tour-pole incidences (6 × 4) | ✓ |
| C7 | Tour ladder $Q_2{:}1 \to K_4{:}3 \to Q_3{:}6 \to K_5{:}12$; $6 = \sqrt{3 \times 12}$ | ✓ |
| C8 | §VI distribution flat: exactly 32 vectors per sector under the stated recipe (Register A bit; Old Yang → later zodiac longitude), all 12 sectors | ✓ |
| C9 | Flags: 24; 4 per gate (2 manifest + 2 dual); 2 gates per flag; enantiomer pairs share no flag; per face, 1 manifest + 1 dual reading (§2.3, §2.6) | ✓ |

plus the attic arithmetic $4^6 = 2^{12} = 64 \times 64 = 4096$ (§1.3) — ✓

**`scripts/orientation_group.py`**

| # | Claim | Result |
|---|---|---|
| U0 | $\|S_4\| = 24$, $\|A_4\| = 12$; $A_4$ contains no transpositions | ✓ |
| U1 | Directed edges have exactly 2 completions, exactly 1 even → gates ↔ $A_4$ | ✓ |
| U2 | $A_4$ simply transitive on the 12 directed edges | ✓ |
| U3 | Odd completion = even one with the uninvolved pair's images swapped ($C_2$ = the handedness flip) | ✓ |
| U4 | 3 double-transpositions hold the 3 bimedians setwise ($V_4$ = the rings); $A_4 = 1+3+8$ | ✓ |
| U5 | 24 cube rotations act on the 4 diagonals as full $S_4$; preserves manifest tet ⟺ even | ✓ |
| U6 | 24 outward squares (face + reading-corner flags): free action, hence simply transitive | ✓ |
| U7 | Each gate-edge flips exactly the bimedian-bit of its own $K_4$ edge (families = axes) | ✓ |
| U8 | Two flips, not one (§2.5): completion-difference = odd single transposition; twin-step = even half-turn, exactly the family's $V_4$ element; the AR-trade fits 8 of 12 | ✓ |
| U9 | The tetrahedron's 3 bimedians = the cube's 3 axes; the cube has 6 opposite-edge midpoint lines in the 3 face-diagonal directions (preamble, §1.2) | ✓ |

Corpus anchors: `L3-EdgeStateSpace` l.381–420, l.451–461, l.473, l.485–534; `L4-TransitingTheThreeWalls` §I, §III, §V, §VI, §VII; `L4-TheTwelveGates` l.13, l.212–223; `L5-TheCyclingMind` l.50, l.58, l.68, l.72, l.112, l.140, l.176, l.180, l.184; `On_HilbertAndHisSpaces` l.111, l.409; `L3-TheSelfProjectingBraid` l.52, l.72.

---

## XIII. Who Turns the Crank

The last honest question is the first one a bird asks of any machine: what keeps it up there. The engine is not self-driving — the Program Counter is [gauge], and no mechanism is owed for selection (§3.1). But it is not a passenger either: the torque-motor claim (§X.4) closes the loop — the machine's own commits load the hold that its own advance turns against, one orthogonal act per step, outputs becoming the load that selects the next input. Self-feeding, not self-observing; generative, not recursive.

The bird's version costs nothing to state and everything to be. Hanging off the underside of the branch is not a pose; it is the work that keeps the grip. Position is paid for in torque, continuously, and the paying is why there is anything perched here at all — **mass is the price of being** (§X.4, and the corpus's MeV gap). The engine's ledger stays honest about what it prices: bits on erasure (§X.5), nothing for the turn. That the turn still happens is the bird's whole testimony: the view from the underside is excellent, and it is not free.

---

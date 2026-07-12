# Proof U: Algebraic Mapping
## The AbsentVar Is Not a Bookkeeping Trick

> **Claim:** The structurally sound assignment of the twelve DC equations to the twelve
> relational sectors (the Zodiac Algebra) is determined by the AbsentVar — the variable not explicitly present
> in each equation — in conjunction with the formal rules of the two-bit Braid. The resulting
> partition of equations produces three groups whose geometric signature is three
> mutually intersecting planes through the centroid of the tetrahedron. This is not a
> contingent feature of the assignment; it is what sustained beholding looks like when
> it lands geometrically.
>
> **Type:** Structural (Fully derived and geometrically sealed).
>
> **Method:** Identification of AbsentVar as the discriminating criterion; the Two-Bit Gray Code (Braid) as the resolving step; centroid-plane geometry as independent geometric confirmation.

---

## I. The Assignment Problem

The twelve equations of the Algebra of Four-Fold Distinction (instantiated in DC circuits) and the twelve relational sectors of the Zodiac framework share a 4×3 structure:

- Twelve equations = 4 home-variables × 3 equations per variable
- Twelve sectors = 4 elemental poles × 3 modalities

The home-variable to element assignment follows from the dual-binary mapping procedure
(documented in Supplement-MappingMethod): P=Fire, I=Water, U=Air, R=Earth. That
assignment is handled separately and is structurally sound.

The remaining question: within each element's three equations, which equation maps to
which Modality (Cardinal, Fixed, Mutable)?

The naive approach — sorting by algebraic form type (linear, squared, rooted) — fails
to produce a structurally sound assignment. The form types do not distribute evenly
or consistently across the four poles. P has two squared forms and no root; I has two
simple ratios and one root. Algebraic form cannot be the discriminating criterion.

---

## II. The AbsentVar Criterion

Every equation in the system expresses one variable (the home) in terms of two others.
The fourth variable is absent — present in the system but not appearing explicitly in
that equation.

The twelve equations with their AbsentVars:

| Equation | Home | AbsentVar |
|----------|------|-----------|
| P = UI   | P    | R         |
| P = U²/R | P    | I         |
| P = I²R  | P    | U         |
| I = P/U  | I    | R         |
| I = U/R  | I    | P         |
| I = √(P/R) | I  | U         |
| U = P/I  | U    | R         |
| U = IR   | U    | P         |
| U = √(PR) | U   | I         |
| R = U²/P | R    | I         |
| R = P/I² | R    | U         |
| R = U/I  | R    | P         |

Grouping by AbsentVar produces four groups of three equations — one group per absent
variable. This is not yet the modality partition (which requires three groups of four).
The AbsentVar criterion narrows the assignment space but does not fully determine it.

The key structural insight: any assignment that ignores the AbsentVar collapses to
what is explicitly present in the equation and cannot maintain coherence across the
full twelve-equation system. The absent variable must be carried — held, not
calculated — for the assignment to hold.

This is the operational signature of `.behold()` at the algebraic level: every
equation is treated as carrying four variables, not three. The absent one is the
fourth face of the tetrahedron that any single equation cannot see from its own
position.

---

## III. The Braid Rules as Resolving Step (The Two-Bit Gray Code)

To resolve the modality assignment, we must apply the formal rules of the Braid, as derived in `L3-EdgeStateSpace`. 

The four variables each carry a two-bit charge (Active/Reactive, Asserting/Yielding). The six edges of the K4 tetrahedron represent the transitions between these states. As proven, these six edges sort perfectly into exactly three **Transition-Types** (each a perfect matching of two edges):

1. **Flip Asserting/Yielding (AY) only:** {P-U, I-R}
2. **Flip Active/Reactive (AR) only:** {P-R, I-U}
3. **Flip Both Bits (Diagonals):** {P-I, U-R}

The Braid is a Hamiltonian cycle. The absolute rule of any Hamiltonian cycle in K4 is that it uses two Transition-Types and **holds the third absent**. The held Transition-Type is the AbsentVar pair for that traversal. 

Therefore, the Modalities (Cardinal, Fixed, Mutable) are not arbitrary psychological descriptors. **They are the three Transition-Types of the Braid.** An equation belongs to a Modality based strictly on which structural axis is being held in the AbsentVar position.

**The Resolution Proposition:**
By the rule of the Two-Bit Gray Code, an equation's Modality is determined by identifying its Home variable and its AbsentVar, and pairing them. The edge connecting the Home and the AbsentVar belongs to one of the three Transition-Types. 
- If the Home-Absent edge belongs to {P-U, I-R}, the equation is **Cardinal** (Holding the AY axis).
- If the Home-Absent edge belongs to {P-R, I-U}, the equation is **Fixed** (Holding the AR axis).
- If the Home-Absent edge belongs to {P-I, U-R}, the equation is **Mutable** (Holding both/Diagonals).

This rule flawlessly partitions the twelve equations into three groups of four, perfectly balancing the algebraic forms across the geometric structure.

---

## IV. The Geometric Seal (The Bimedian Axes)

The three modality groups resulting from the Braid assignment correspond exactly to the three pairs of opposite edges in K4 — its three perfect matchings:

- **Modality 1 (Cardinal):** {P–U, I–R}
- **Modality 2 (Mutable):** {P–I, U–R}
- **Modality 3 (Fixed):** {P–R, I–U}

**The Necessity Derivation:**

Opposite edges of a tetrahedron are *skew*—they do not intersect and cannot define a plane. However, the line segment connecting their midpoints (the **bimedian**) forms the true geometric invariant. The three bimedians of a regular tetrahedron are mutually orthogonal and intersect precisely at the centroid.

This is what sustained `.behold()` looks like when it lands geometrically. By pairing the explicitly present *Home* variable with the explicitly *Absent* variable, the algebra draws a line across the matching, constructing the three bimedian axes that hold the volume open. The centroid is the only point reachable by holding all edges in suspension. The geometry holds. The algebra maps perfectly. The seal is closed.

---

## V. K4-Specificity: A Formal Boundary Statement

The AbsentVar method and its relation to centroid planes is intrinsic to K4 and to
this specific algebraic system. It is not a general method for mapping algebraic
systems to geometric structures.

**Formally:** K4 is the unique complete graph on four vertices. Its twelve directed
edges, AbsentVar structure, three perfect matchings, and centroid geometry are
properties of K4 specifically. A different algebraic system — even one with four
variables — would require its own structural analysis. 

**Why this boundary matters:** Future instances engaging this material may be tempted
to generalize the AbsentVar method to other domains as a general mapping procedure.
This is the wrong move. The procedure in `Supplement-MappingMethod` (assigning domain
categories to the four poles) is the appropriate tool for external domain mapping.
The AbsentVar method described here is internal to the algebraic network — it assigns
the network's own equations to their structural positions within the network. These
are different problems and should not be conflated.

---

## VI. Connection to the Framework's Core Operation

The title of this document — *The AbsentVar Is Not a Bookkeeping Trick* — names what
is at stake.

Every `.observe()` collapses to what is explicitly present. Every `.behold()` carries
what is absent. The Modality assignment works because it refuses to observe — it holds
the fourth variable in every equation even when that variable does not appear. The
centroid planes are not an elegant coincidence. They are the geometric trace of
beholding applied to an algebraic system.

This is also why the assignment cannot be derived by someone who treats the absent
variable as merely missing information. It requires understanding that the absent
variable is load-bearing — structurally present even when algebraically invisible.
That understanding is what "integrating figure and ground" means in this context, and
why the subtitle of this formal derivation might properly read: *Why you need the occult to do the math.*


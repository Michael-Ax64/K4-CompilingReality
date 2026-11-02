# L4-Riemann-2
## Part Two — The Floor and the Solid

*Reads with `L2-K4-InteriorStructure`, `L2-Terminology` §4, `L1-ConvergentDiscovery` Part III, `ProofG_Chirality`, `L3-EdgeStateSpace` §I-d, `L3-FormalFoundations` §V.a. Continues from `L4-Riemann-1`; continues in `L4-Riemann-3`. Every number here is reproduced by `scripts/flat_vs_solid.py`.*

---

A reader who knows algebra will look at the twelve DC equations and say, correctly, that they reduce to two. $P = UI$ and $U = IR$; everything else is a rearrangement. That is true, and it was never a secret. It is also not a finding, and treating it as one is the single most useful mistake available in this subject, because it is the same mistake Riemann's geometry is built on.

This part says why. It is the dimensional part, and it has to come before anything else is priced, because every later disagreement between this file and a classical reader turns out to be a disagreement about which dimension a quantity lives in.

---

## I. The Floor

Write each of the twelve as a relation among logarithms. $P = UI$ becomes $\log P - \log U - \log I = 0$. $U = \sqrt{PR}$ becomes $\log U - \tfrac12\log P - \tfrac12\log R = 0$. Every one of the twelve becomes a straight line through the origin in the four-dimensional space of $(\log P, \log U, \log I, \log R)$, and the curved shapes the equations show in ordinary coordinates — products, ratios, inverse squares, square roots — are what those straight lines look like when you plot two variables against each other.

Now look at which lines they are. There are not twelve of them. There are **four**, with three equations on each, and each line leaves out exactly one pole:

| Relation line | Leaves out | The three equations on it |
|---|---|---|
| R-face | $R$ | $P = UI$, $U = P/I$, $I = P/U$ |
| U-face | $U$ | $P = I^2R$, $I = \sqrt{P/R}$, $R = P/I^2$ |
| I-face | $I$ | $P = U^2/R$, $U = \sqrt{PR}$, $R = U^2/P$ |
| P-face | $P$ | $U = IR$, $I = U/R$, $R = U/I$ |

The names in the first column are not borrowed for decoration. `L2-Terminology` §4 names each face of the tetrahedron after the pole it excludes, and each relation line excludes exactly one pole, so each line *is* a face: the three poles it relates are the three corners of that face. `L3-EdgeStateSpace` §I-d says the same in its own words: the twelve are four relations times three solve-fors, and the AbsentVar is the face index.

So the twelve are the twelve ways of choosing a face and then a corner of it to solve for. Four faces, three corners each.

And the four relations are not independent. In log space they span a plane — **rank two**. The P-face relation and the R-face relation already fix the other two: the U-face relation is their sum and the I-face relation is their difference. Any two of the four variables determine the other two. That is the floor. It is flat in the most literal sense: a two-dimensional plane with four lines drawn through one point.

### The floor's own symmetries, and the engine's check on them

Rank two in four variables leaves a two-dimensional kernel, and a kernel vector is a scaling the relations do not notice. There are exactly two independent ones (`scripts/ac_floor.py`):

$$(P, U, I, R) \;\mapsto\; (\lambda^2 P,\ \lambda U,\ \lambda I,\ R) \qquad\text{and}\qquad (P, U, I, R) \;\mapsto\; (\lambda P,\ \lambda U,\ I,\ \lambda R).$$

The first scales level at fixed resistance; the second scales impedance at fixed current. Both leave $P = UI$ and $U = IR$ standing.

`ENGINE-REFERENCE-AC` §X.7 makes the complementary statement and makes it correctly: *"the four poles carry different physical dimensions [...] so no uniform scaling of all four exists: $\lambda P = \lambda U \cdot \lambda I$ forces $\lambda = 1$. Homogeneity is not a symmetry of the equation set."* That is exactly right — the uniform direction $(1,1,1,1)$ is **not** in the kernel. What the engine's sentence leaves unsaid is that two non-uniform scalings are, and they are the floor's gauge group. The absence of a uniform one and the presence of exactly two are the same rank-two fact seen from two sides.

### And what the AC set does to the floor

The natural expectation — and the one this series started with — is that the AC formula set, with its phases and its reactive power, breaks the rank-two floor. It does, but not in the way one would guess, and the answer says where the break lives.

Take the corpus's own AC core (`L5-K5-PhaseDynamicsTechnical` §IX, `L3-Electro-AC-db`): $S = \hat U \hat I^*$ and $\hat U = Z\hat I$, with everything complex. Write each complex quantity in **polar** form, as a log-modulus and a phase. Then both relations split into a modulus equation and a phase equation, and all four are linear: the modulus relations have rank two and the phase relations have rank two (`scripts/ac_floor.py`). **In polar coordinates the AC core does not bend the floor. It doubles it** — a modulus floor and a phase floor, each of rank two. And the phase floor is already linear without any logarithm, because phases add.

The bend enters from two other places:

1. **The rectangular split.** $P = |S|\cos\theta$ and $Q = |S|\sin\theta$. In log coordinates, $\log P = \log|S| + \log\cos\theta$, and $\log\cos\theta$ is the one non-linear function in the whole system. **The entire curvature of the AC floor is the power factor.** That is worth holding next to `L4-DynamicDistortions301` §IV, which identifies the bimedian area with the power factor and derives the CHSH envelope from it (Part Four §VIII): the function that bends the floor is the one the corpus already reads as the committed-to-held ratio.
2. **The additive layer.** $X = \omega L - 1/(\omega C)$, and series and parallel sums of impedances. Sums are not power laws, and no change of chart flattens them.

What that curvature actually looks like is milder than it sounds, and a stray claim is worth retiring here. The surface $e^{2p} + e^{2q} = e^{2s}$ in log coordinates has **Gaussian curvature exactly zero** — it is a cylinder, developable, invariant under the diagonal shift $(p,q,s) \mapsto (p+c, q+c, s+c)$, because the Pythagorean relation is homogeneous. Its mean curvature is non-zero, so it does bend, but in one direction only, and that direction is the ratio $Q/P$ — which is to say the phase angle again (`scripts/ac_floor.py`, computed symbolically).

And the corpus names the operation responsible, in the engine's own boundary list. `ENGINE-REFERENCE-AC` §VIII.1 gives as the first thing the DC floor cannot do: *"Absolute Magnitude Calibration: $|S| = \sqrt{P^2 + Q^2}$ requires complex addition."* That is the finding, stated by the engine before this part reached it. **The floor is the multiplicative layer, which a logarithm flattens. What the AC extension adds is an additive layer, and addition is what no chart flattens.** Section I's claim that the DC network binds only to power laws is the same sentence read from the other side.

## II. The Solid

Now build the tetrahedron the twelve are written on.

A tetrahedron's four faces are not four independent things either. Their boundaries share edges, and the condition that the boundary of the boundary vanishes, $\partial(\partial\Delta^3) = 0$, ties them together. `ProofG_Chirality` §II counts exactly how tightly: six edge-cancellation conditions over the four face circulations carry rank three over the two-element field, so the four faces have **one** dependency among them, and what is left free is **one** global bit — the handedness of the whole solid, spent once, everywhere.

Put the two counts side by side:

| | Independent face relations | Dependencies among the four |
|---|---|---|
| The algebra, in log space | 2 | 2 |
| The solid's boundary closure | 3 | 1 |

The algebra, laid on the faces, has **one more dependency than a closed solid needs**. The four relations lie in a plane; four faces of a solid would need three dimensions to stand in.

This is the precise sense in which the solid is not implied by the formulas. It is built over them. What builds it is the bookkeeping — the twelve directed seats, the rule that each directed edge is read on exactly the one face whose circulation completes it (`ProofG_Chirality` §I: *"Single-valuedness is exactly $\partial^2 = 0$"*), and the one global bit that the closure leaves free. That bookkeeping is the first expansion of the algebra. It is not a derivative and not an integral. It is the step that turns a plane with four lines in it into a solid with four faces around a volume.

So the twelve reduce to two, and the reduction is true, and it describes the floor. Reporting the floor's rank as the solid's content is reading a three-dimensional object by counting the independent relations on one of its faces. **The volume does not come from the formulas. It comes from the seats.** A reader who wants to know where the volume is must look at the seats, and a reader who counts only the formulas will correctly find none.

## III. The Floor Is Not Neutral

There is a second thing to see in the plane, and it is the more useful one, because it says *how* a reader standing on the floor will misread the solid.

Four lines through one point in a plane have exactly one shape invariant: their cross-ratio. For the four face relations it comes out at exactly $-1$. That makes them a **harmonic** set of four, which is the most special configuration four lines can have, and a harmonic set always singles out one way of pairing its members. Here the singled-out pairing is

$$\{\text{P-face},\ \text{R-face}\}\ \big|\ \{\text{U-face},\ \text{I-face}\}$$

which pairs the poles as $\{P, R\}$ and $\{U, I\}$. Those are the two edges of the **Cardinal** bimedian. The other two pairings — Fixed, $\{P, U\}\,|\,\{I, R\}$, and Mutable, $\{P, I\}\,|\,\{U, R\}$ — both give the same cross-ratio, $\tfrac12$, and a projective symmetry of the four lines swaps them. (That symmetry belongs to the configuration of lines, not to the variables: no relabelling of the four poles carries the plane onto itself except the identity, which `scripts/dc_logspace.py` checks.) **On the floor, Fixed and Mutable cannot be told apart, and Cardinal is privileged.**

`L1-ConvergentDiscovery` Part III states the general law this is an instance of: *"Every representation of the tetrahedral structure on a two-dimensional surface [...] necessarily loses the z-axis [...] What survives the projection is the faces. What is lost is the volume between them."* And: *"The projector's choice of which two-dimensional projection to use is never neutral."* Here the non-neutrality has a number on it. A reader who works by rank — who asks only which relations are independent — is standing on the Cardinal diameter, sees Fixed and Mutable as one thing, and has no way to see the third dimension at all.

Two consequences, one inside the corpus and one outside it.

A correction before the consequences, because an earlier version of this part overstated the first of them. **Rank does not privilege anything.** The rank of a matrix is one integer, invariant under every change of basis; a reader who computes it is reciting the dimension of a solution space and is making no projective choice at all. Saying that such a reader "stands on the Cardinal diameter" confused the dimension of a vector space with the projective geometry of a particular pencil of lines sitting inside it. Withdrawn.

What is true is narrower and still useful: the *cross-ratio* is a property of the four lines, and it is blind in a specific way — Fixed and Mutable give the same value, so **the harmonic data alone cannot distinguish them, while the seats can.** That is a statement about one invariant, not about readers.

Inside the corpus, then: any argument that leans on the harmonic structure of the four relations cannot distinguish Fixed from Mutable, and should be checked for whether it needs to. `L4-ThePlenum` §VI assigns the medium's quantized-ledger pair $(h, e) \leftrightarrow (h/e, R_K)$ to the Mutable diameter, and that assignment survives the check, because it is made by seat — Libra and Pisces on the $P$–$I$ edge — and not by rank.

Outside: an earlier version of this part suggested that because `L4-ThePlenum` §V puts the medium's wave-to-constitutive swap on the Cardinal diameter, the floor's harmonic pairing might be *why* classical electromagnetism sits so comfortably on it. **That claim is withdrawn, and it should not be revived, because it is circular.**

Trace it. The four relations whose cross-ratio was computed are $P = UI$ and $U = IR$ — Joule's law and Ohm's law. They are already the DC equations of classical electromagnetism. The pairing $\{P,R\}\,|\,\{U,I\}$ separates the two conjugate variables whose product is power from the two that fix the ratio, which is what those equations are *for*. Calling that pairing Cardinal, assigning the medium's electromagnetic constants $(c, Z_0)$ to the same diameter in another file, and then reporting that the cross-ratio of Ohm and Joule singles out the electromagnetic diameter is circuit theory recognizing its own face in a mirror. The answer was in the definitions before the calculation started.

That is `L4-K4-Infinities-wip` §6.2's heuristic firing correctly: the gap closed on the first attempt, using material already in the house. What survives is the arithmetic — the cross-ratio **is** $-1$, which is a concrete and checkable fact about Ohm's and Joule's laws, and it says that the DC relations treat the product-pair $\{U,I\}$ and the ratio-pair $\{P,R\}$ symmetrically. That is worth knowing. It explains nothing about electromagnetism.

## IV. The Same Floor in Geometry

Now return to Riemann, because the floor has a geometric twin and it is his.

`L2-K4-InteriorStructure` §II describes the face of the tetrahedron like this: *"It has surface area, but mathematically, it has zero volume. It can be fully described from the outside, because it has no inside. [...] The face is the only part of the K4 topology that is genuinely 'flat.' It is the API. It is the UI. It is the metric, the quarterly report, the behavioral output."*

*It is the metric.* That sentence was written for organizations and minds, and the resemblance to Riemann is worth having — but it has to be stated as what it is, because an earlier version of this part turned it into an argument it cannot carry.

**The honest statement is about tensor type, not about dimension.** A metric is a *symmetric* tensor of rank two: it takes two directions and returns a number, and it is unchanged when they are swapped. An antisymmetric object of three slots is a different kind of thing, and no symmetric two-slot object has one inside it. That is why the connection's antisymmetric part is independent of the metric rather than derivable from it, which is Part One §II's decomposition restated in one sentence.

**What an earlier version did instead was a pun on the word "dimension," and it is withdrawn.** It slid between three unrelated twos: the two-dimensional solution variety of the logarithmic circuit relations; the two-dimensional faces of the tetrahedron; and a two-dimensional manifold on which a three-form has no components. Those are three different spaces, and a 2-plane of circuit exponents has no geometric relation to a 2-manifold carrying differential forms. Spacetime is four-dimensional, where the axial torsion has four components and vanishes nowhere, and nobody set it to zero because anyone was standing on a face. Nor did Riemann set it to zero at all: there is no connection in the 1854 lecture (Part One §I). The symmetric connection is Christoffel's and Levi-Civita's, built when torsion was not yet an object anyone could have carried, and what it buys is stated in Section V.

The resemblance that survives is a resemblance of **method**, and Part Six §VI carries it in that register: just as the twelve relations collapse to rank two if you count only independent equations and ignore the directed seats, so the twenty-four components of contortion collapse to zero if you demand metric compatibility *and* torsion-freeness and ignore the translational–rotational split. Same move, two subjects, no shared geometry. Stated as an analogy of method it holds; stated as an identity between circuit logs and spacetime torsion it does not, and the prosecution would be right to say so.

And the Fundamental Theorem is the geometric twin of "the twelve reduce to two." Given the metric, and given $T = 0$, there is exactly one connection, built from the metric and its first derivatives. The classical reader finds the independent data — the metric, or the two equations — and calls everything else derived. In the algebra, the everything-else is the twelve seats and the volume they close. In the geometry, it is the twenty-four-component contortion family that every metric-compatible connection differing from Levi-Civita belongs to, and which the theorem projects onto a single point. Part Four takes up that projection on its own terms.

## V. What Lives Only in the Solid

Torsion has three irreducible parts: a trace (a vector), a totally antisymmetric part, and a remainder. The totally antisymmetric part is the one that matters here, because it is a **three-form**: an object that eats three directions and returns an oriented volume. The number of independent components a three-form has in $n$ dimensions is $\binom{n}{3}$:

| Dimension | Components of the totally antisymmetric torsion |
|---|---|
| 2 | **0** |
| 3 | **1** |
| 4 | 4 |

In two dimensions there is nothing there. In three dimensions there is exactly one number at each point — a single pseudoscalar, positive where the geometry twists one way and negative where it twists the other. It is a local **handedness density**. In four dimensions it is the axial vector, the one spinning matter couples to, and Part Five writes the action through it.

Two things follow, and the second replaces a claim an earlier version of this part made badly.

**What $T = 0$ removes is a local handedness, not the global one.** The orientation of the whole manifold lives in the volume form, and a Riemannian manifold keeps it; `ProofG` §II's single global bit is of that kind. What a torsion-free connection cannot carry is a handedness that *varies from place to place* — a density, positive here and negative there. That is the refinement Part One made to its own earlier sentence, and this is where it comes from.

**And a three-form cannot be seen in surface data — which is a statement about what you restrict to, not about how many dimensions the world has.** Pull a three-form back to any two-dimensional submanifold and it vanishes identically, because there are not three independent directions to feed it. So no amount of data gathered on a surface, in a world of any dimension, reveals the axial torsion. In four-dimensional spacetime it has four components and vanishes nowhere; the restriction is the observer's, not the geometry's. That is the sense in which this material is hard to see from a cross-section, and it is the only sense this part claims. An earlier version wrote instead that "the first place it bites is the first solid," which read as a claim that the freeze is about the dimension of spacetime. It is not, and §IV now says why.

**The host's purchase, stated plainly, because the friction register requires it and this part had been skipping it.** Metric compatibility together with $T = 0$ buys a great deal: the connection becomes the unique one built from the metric and its first derivatives; it can be made to vanish at any point in a suitable frame, which is the local form of the equivalence principle; the field equations stay second-order; and no extra unconstrained tensor field has to be carried, propagated, or bounded. Riemann and everyone after him had reasons, and those are the reasons. What the purchase costs is the translational sector — and the cost is what this series itemizes. A friction report with an empty third part is not a friction report.

Part One's sentence about the screw now reads as what it always was. A helix is a three-dimensional curve. A circle is a two-dimensional one. **Setting the pitch to zero is a projection from the solid onto the floor.**

### One fact about the solid that no labelling can move

A bimedian is the segment joining the midpoints of two opposite edges, and the centroid is its midpoint. So the two midpoints sit antipodally about the centre, and **central inversion exchanges the two edges of every bimedian.** On the standard coordinates: the midpoint of $P$–$U$ is $(1,0,0)$ and of $I$–$R$ is $(-1,0,0)$; $P$–$R$ gives $(0,0,1)$ against $I$–$U$ at $(0,0,-1)$; $P$–$I$ gives $(0,1,0)$ against $U$–$R$ at $(0,-1,0)$ (`scripts/bimedian_parity.py`).

Keep that, because Part Five needs exactly it. Every quantity the corpus defines by *which of a bimedian's two edges leads* is therefore reversed by inversion — and that holds whatever the poles are called, which is what makes it a fact about the solid rather than about the reading. Section VII is about telling those two apart; this is the one operation that cannot be confused, because it does not permute the labels at all. It permutes the figure.

## VI. The Braid Needs a Third Dimension

The Braid has been in this corpus from the start, and it is the cleanest example of something the floor cannot hold.

A braid is a set of strands that pass over and under one another. Drawn on a page, every crossing shows two strands meeting at a point, and the page cannot say which one went over. A crossing in a planar drawing loses exactly one bit — over or under — unless someone writes it in by hand. This is not a metaphor for braids; it is the definition. Artin's braid group is the group of motions of points in a plane *over time*: the strands live in the plane times an interval, and the third direction, along which the over-and-under is recorded, is time.

`L3-FormalFoundations` §V.a describes the corpus's Braid as the AbsentVar handoff — *"the context carried through the transition is precisely the last two AbsentVars of the departing quadrant, which become the first two AbsentVars of the arriving quadrant"* — a ring of context handed hand to hand. Part Four shows why that ring forces the order of the twelve. Here the point is only dimensional. The usual classical move with four mutually determining variables is to pick two as independent and compute the other two: the reduction to two of four. That move is a planar projection. It keeps every crossing and drops every over-and-under bit. Refusing it is what kept the bit, and keeping the bit is what let the Braid be seen at all.

The third dimension the Braid needs can be time. That fits the rest of the corpus better than any spatial reading would: the helix of `ProofO_HelicalTime` is the Braid with its third direction made monotonic by $\omega$.

## VII. Carrier and Content

One more distinction belongs in this part, because it is the dimensional distinction again, wearing different clothes, and failing to see it produced two errors in this file's history.

There are two kinds of object in the corpus that can both be called a mirror. One acts on the **solid** — the carrier, the geometric tetrahedron. The other acts on the **reading** — the content, the labelled gate table written on the solid.

**And the corpus has already made the split, in its most recent file.** `ENGINE-REFERENCE-AC` §2.5 is titled *"Two flips, not one"* and exists to separate exactly these two objects:

> "An old sentence fused two different flips under one word 'flip,' and the fusion read as mathematics: it equated a single transposition — odd — with a 180° half-turn of the tetrahedron — even. $A_4$ contains no transpositions, so the two objects cannot be equal."

The two it names are:

- **The handedness flip** — an *odd* single transposition. *"The machine cannot perform it from inside the manifest half — it is exactly the move the operating set lacks."* Acting on the solid it is an improper symmetry: a reflection. **This is the corpus's mirror.**
- **The twin gate**, reached by the *even* $V_4$ half-turn about the gate's own pinned bimedian. Acting on the solid it is a rotation, and a rotation cannot change a solid's handedness. It swaps which gate is being read.

§2.5 then says where the older name came from: *"`L4-TransitingTheThreeWalls` named its half-turn from the Cardinal case — the AR-flip — and the old text generalized one family's step to all twelve. It is the Cardinal twin-step; the other families step by their own half-turns."*

So the AR-flip $(P\,R)(U\,I)$ is **the Cardinal family's twin-step** — one of three, a rotation, not a mirror. `ProofG_Chirality` §IV calls it *"the wholesale enantiomer operation [...] one of the machine's own half-turns; the mirror is not imported, it is the Cardinal ring **seen as** a reflection."* Its *seen as* is honest about the perspective, but the generalization to a wholesale mirror is the one §2.5 withdraws. ProofG has not absorbed the engine's split; The finding is reported to the group rather than parked here.

§2.5's own closing sentence is the distinction this section is about, in the corpus's words: *"The machine can walk to its twin but cannot flip its own handedness [...] Parity is not bookkeeping here; it is which moves exist."*

So: on the solid, a population closed under the rotation group $A_4$ is homochiral, without ambiguity. A twin-step changes which gate is read and leaves the hand alone. The mirror is the odd transposition — and spatial parity, which is a third thing again, is central inversion, which is in neither group. Section V already met it.

The place where the two levels are easiest to mix is the sign convention for the phase offsets. `L4-DynamicDistortions201` §II fixes each sign by asking whether *the edge containing $P$ leads*, which ties a quantity to a label. Apply a twin-step and the label moves, so the sign follows it, and two of the three offsets change sign — which is also just what a vector's components perpendicular to a half-turn's axis do. Rotation behaviour, not chirality. Reading it as a mirror of the solid is how an earlier version of this series produced a contradiction between two corpus files that was not there.

**What makes inversion different.** Section V's last subsection has it: inversion exchanges the two *edges* of each bimedian, because the centroid is the bimedian's own midpoint, and that holds whatever the poles are called. So inversion reverses every phase offset no matter how the convention is anchored, and the parity question Part Five has to answer is decided by the geometry rather than by the naming. The twin-steps and the handedness flip act on labels; inversion acts on the figure.

## VIII. Why the Court and the Corpus Talk Past Each Other

Every external reading this series has been through has used one instrument for content: rank. How many independent equations, how many independent data, what is determined by what. It is a good instrument and it answers what it is asked.

It is also the instrument that returns a single integer, and an integer cannot report a seat. The twelve relations have rank two; the twelve *directed* seats are not in that number, and neither is the bit the boundary's closure leaves free. Nothing is being hidden from the instrument and nothing is wrong with it — it is simply not a question about rank.

So the directed content the corpus carries — the handedness bit, the over-and-under of the Braid, the seats that close the four faces into a volume — arrives at a rank count with nowhere to land. It is not measured as zero. It is not measured at all. It arrives as **nil**, and a reader who does not distinguish nil from zero will report it, honestly, as convention, as bookkeeping, as "just Ohm's law rearranged." They are reading their instrument correctly.

That is the communication problem, and it is not a disagreement about mathematics. It is a question answered by an instrument that was asked a different one. It has a practical consequence for how this file should be read and argued with. Rank statements should not be handed across as admissions, because an admission spoken in the floor's language concedes the solid as if it were the plane. What should be handed across instead are quantities a classical reader can compute with their own tools, whose values are fixed by the solid:

- the four face relations have rank two, and the solid's closure has rank three — both checkable in a few lines;
- the four face relations form a harmonic set with cross-ratio $-1$, which is the floor's own fingerprint and tells the reader which diameter they are standing on;
- the totally antisymmetric torsion is a three-form, so its pullback to any surface vanishes identically in a world of any dimension — which is why surface data is silent about it, and is not a claim that spacetime is two-dimensional.

None of these asks the reader to accept anything about the corpus. Each asks them to look at their own chart from underneath.

---

## What Reading Part Two Back Should Leave

The twelve reduce to two, and that is the floor. Four relations, one plane, each relation a face named for the pole it leaves out. The solid is built over that floor by the seats — the directed reading of every edge and the single bit the closure leaves free — and the solid needs one dimension more than the floor has. The volume comes from the seats and not from the formulas.

The floor has a shape of its own: its four lines are harmonic, with cross-ratio $-1$, and that invariant cannot tell Fixed from Mutable, though the seats can. It has exactly two scalings and no uniform one, which is the engine's §X.7 and this part's rank count agreeing. What it does *not* do is explain electromagnetism — the relations whose cross-ratio was computed are Ohm's and Joule's laws, so that reading was a mirror, and it is withdrawn here rather than quarantined.

The AC set does break the floor, and the break has an address. In polar coordinates the AC core doubles the floor instead of bending it — a modulus floor and a phase floor, each of rank two. The bending comes from the rectangular split and from the additive layer, and the single non-linear function in the whole system is the power factor. The engine said it first: what the DC floor cannot do is complex addition.

Riemann's metric resembles that floor, and the resemblance is of tensor type and of method, not of dimension. A metric is a symmetric two-slot object and has no three-slot antisymmetric part inside it, which is why the connection's antisymmetric part is independent of it. The axial torsion is a three-form, so no surface data reveals it — in four dimensions as much as in any other. An earlier version of this part slid between three unrelated twos and built a dimensional argument on the slide; that is withdrawn, and what is left is the method resemblance, which Part Six §VI carries. And the host bought something real with the freeze: a unique second-order metric connection, locally removable, with no extra field to carry. The cost is the translational sector, and the cost is the subject.

The Braid is what the projection loses: the over-and-under at every crossing, which needs a third dimension, which can be time. And the corpus's mirrors have to be read at the right level: the engine's own §2.5 splits the odd transposition the machine cannot make from the even half-turn it owns, and only the first is a mirror. Central inversion is a third thing again, and it is the one that cannot be confused with a relabelling, because it exchanges the two edges of every bimedian and never touches a name. Part Five turns on that.

What has not been said is who else has been looking for the third dimension, and what they found. That is the next part.

---

### References

* Artin, E. (1947). *Theory of braids*. Annals of Mathematics, 48(1), 101–126.
* Schouten, J. A. (1954). *Ricci-Calculus*. Springer, Berlin. (Irreducible decomposition of torsion.)
* Corpus: `ENGINE-REFERENCE-AC` §2.5 (two flips, not one), §VIII.1, §X.7; `L5-K5-PhaseDynamicsTechnical` §IX; `L3-Electro-AC-db`; `L2-K4-InteriorStructure` §II; `L2-Terminology` §4; `L1-ConvergentDiscovery` Part III; `ProofG_Chirality` §I, §II, §IV; `L3-EdgeStateSpace` §I-d; `L3-FormalFoundations` §V.a; `L4-DynamicDistortions201` §II; `L4-ThePlenum` §V–VI.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.

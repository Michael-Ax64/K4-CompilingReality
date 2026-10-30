# Soficity\*
## What It Means for a Structure to Outrun Its Finite Models, and Why So Many Fields Found the Same Wall

*L3, definitional. A companion to `L3-NonSoficTopologicalVolumes`, which keeps the existence result. This file keeps the meaning. Wherever the corpus writes **sofic\*** or **non-sofic\***, the asterisk points here.*

---

## 0. The Asterisk

Bare *sofic* means what Gromov and Weiss meant: a countable group whose finite pieces can be modelled, with vanishing error, by permutations of finite sets.

**Sofic\*** means the same scheme applied to a declared structure and a declared class of finite models. A file that writes *non-sofic\** owes the reader two names: the structure, and the model class it outruns. The file does not owe a proof that the structure is of that kind. Where the claim is open, the asterisk says so, and the open status is recorded in §IX below.

One rule binds every use. **A finite structure is its own perfect model, so nothing finite is non-sofic\* in any sense.** The floor needs something infinite: an infinite group, an infinite-dimensional algebra, the loops of a space, a field with infinitely many degrees of freedom. A file that names a finite thing as non-sofic\* has made a type error, and the asterisk does not repair it.

---

## I. The Question Underneath

Descartes put a point at the corner of the page so he could name every other point by its distance from it. Minkowski laid a sheet of *now* through spacetime so he could name every event by the sheet it sat on. Both moves are slices. A slice is a promise that the whole can be read out piece by piece, and that the pieces add back up to the whole.

Mie, in 1912, wanted the electron to be field and nothing else: no grain of stuff in the middle, only the field gathered densely enough to hold its shape. Hilbert, in 1915, tried to grow all of physics from one field and one principle. They shared a conviction worth naming plainly. A field is real, and it is everywhere. If it is everywhere, then at every point it has a value, and the values are the world.

The second half of that conviction is the slice. The century after them found it false, and found it false inside their own household. The field has content that is real and that has no value at any point. It also has structure that no finite reading, however fine, reaches.

This file is about the second of those findings. Its sister, the first, is Laue's: the outside of a bound body reads one scalar, and the inside does not cross. The two are different walls. The corpus has used one word for both, and the work of this file is to give each wall its own name and then show where they meet.

---

## II. The Scheme

Strip soficity of everything specific to groups and four ingredients remain.

**1. A structure fixed by local rules.** A group is fixed by its multiplication table. An algebra is fixed by its products and its trace. A space is fixed by its loops. A field theory is fixed by its local equations and its symmetries. In every case the structure is infinite, and any finite piece of its rules is finite.

**2. A class of finite models.** These are the objects the exterior is allowed to build: permutations of a finite set, unitary matrices of finite size, finite graphs, finite lattices with a finite Hilbert space at each site. The class is a choice. Choosing it is choosing what the outside may bring to the reading.

**3. A normalized defect.** Take a finite piece of the rules and a finite model. Measure how much of the model breaks that piece. *Normalized* matters: the defect is a fraction of the model, not a count. A model may fail somewhere, as long as the failing part becomes a vanishing share of the whole.

**4. The verdict.** The structure is approximable in this class if, for every finite piece of its rules, models exist whose defect is as small as one likes. It is non-approximable if some finite piece keeps a defect at or above a fixed $c > 0$ in every model of the class, however large. That $c$ is the floor.

Written once, with $S$ the structure, $\mathfrak F$ the model class, $F$ a finite piece of the rules and $\delta_F$ the normalized defect:

$$S \text{ is } \mathfrak F\text{-approximable} \iff \forall F,\ \forall \varepsilon > 0,\ \exists M \in \mathfrak F \text{ with } \delta_F(S \to M) < \varepsilon.$$

$$S \text{ is non-sofic}^*_{\mathfrak F} \iff \exists F,\ \exists c > 0 \text{ such that } \delta_F(S \to M) \ge c \text{ for every } M \in \mathfrak F.$$

Three things in this definition carry the content, and each is easy to lose.

The floor sits on **one finite piece**. A non-sofic\* structure does not resist everywhere. It resists on some definite, finite set of rules that no finite model can honour almost everywhere at once.

The floor is **against a class**. A structure can be approximable by one class and not another. The verdict is never absolute. It is always *non-sofic\* relative to these models*.

The floor is **not statistical**. Nothing is being sampled. The defect is the fraction of a constructed model on which the rules fail, and more data does not enter. Every application of the term to learning, testing or red-teaming has to cross this gap explicitly or it has not been made.

---

## III. The Ladder of Model Classes

The model classes stack, and the stacking is the most useful thing the scheme offers, because it turns *how much may the exterior bring* into a measurable question.

**Exact local copies (LEF, residual finiteness).** The finite model must reproduce each finite piece *exactly*. This is the strictest demand. Mal'cev proved in 1940 that every finitely generated group of matrices over a field passes it. That one theorem is why compact gauge groups are never the home of a floor: every finitely generated subgroup of $SU(3)$ is a matrix group, so it is residually finite, so it is approximable in every weaker sense below.

**Permutations, counted by mismatch (sofic).** The model may be wrong on a vanishing fraction of points. Mismatch is counted bit by bit, in the Hamming metric. This is Gromov's class. Amenable groups pass, residually finite groups pass, and so do nearly all groups anyone works with. One group is now known to fail.

**Unitaries, measured by amplitude (hyperlinear).** The model is a finite unitary matrix, and the defect is measured in the normalized Hilbert–Schmidt norm, which weighs how far amplitudes are off rather than how many bits are wrong. Every sofic group is hyperlinear, so this class forgives at least as much as permutations do. Whether it forgives strictly more is open.

**Matrix algebras with a trace (Connes embedding).** The structure is now an operator algebra, and the models are finite matrix algebras. Connes asked in passing, in 1976, whether every such algebra of the relevant kind is approximable this way. In 2020 the answer came back no, through a result about interactive proofs: MIP\* = RE.

**Finite lattices with symmetry acting site by site.** The structure is a quantum field theory together with a symmetry, and the models are finite lattices whose Hilbert space is a product of finite site spaces, with the symmetry acting on each site separately. Theories carrying a 't Hooft anomaly do not admit such models. Nielsen and Ninomiya (1981) proved the first sharp form of this for chiral fermions. 't Hooft (1980) showed that anomalies survive every coarse-graining step. They are the one quantity no renormalization can remove.

Read the ladder through the corpus's own two registers and it says something the corpus has been trying to say.

Permutation models are **ledger models**. They relabel discrete states and count mismatches as bits, which is the register of $P$, the committed scalar, the Hamming count. Unitary models are **buffer models**. They carry phase and measure error as amplitude, which is the register of $h\mathbf{Q}$. The open question of whether a hyperlinear group can fail to be sofic is therefore, in the corpus's terms, a precise mathematical question:

> **Can a finite model that carries phase reach a structure that no finite model of committed bits can reach?**

That is the $H_{\text{coh}}$ / $H_{\text{incoh}}$ distinction posed as an open problem in group theory, by people who had never heard of the corpus. The Connes failure answers a neighbouring version at the level of algebras: there are structures that even finite phase-bearing models cannot reach.

**Register.** The ladder and its theorems are LANDED (external). The reading of permutations as ledger models and unitaries as buffer models is a CORRESPONDENCE: elements are mapped and the relations are asserted to carry. Kill: a demonstration that the Hamming / Hilbert–Schmidt distinction does not track any committed / held distinction the corpus can operationalize.

---

## IV. The Family of Results

The scheme has been found, under different names, by people working toward different ends. Their motives matter, because each motive shows which face of the wall that person was standing at.

**Gromov (1999) and Weiss (2000).** Gromov was not looking for a limit on knowledge. He was proving a statement about machines: Gottschalk's surjunctivity conjecture (1973), that a cellular automaton on a group which never maps two configurations to the same one must reach every configuration. He found a class of groups for which he could prove it, by approximating the group with finite pieces. Weiss named the class *sofic*, from the Hebrew for *finite*. The concept was born to show that a computing machine on an infinite group behaves as finite machines do. Elek and Szabó (2004) used the same approximation to prove Kaplansky's direct-finiteness conjecture for sofic groups. In this history, soficity is the condition under which the infinite *inherits* finite good behaviour.

**Connes (1976).** In a sentence of his classification of injective factors, Connes wondered whether every finite von Neumann algebra embeds in an ultrapower of the hyperfinite one. That is the matrix-algebra rung of the ladder. Kirchberg showed in 1993 that the question is equivalent to several others across operator algebras. Tsirelson's question, whether two ways of modelling quantum correlations agree, turned out to be equivalent to it as well. The answer took forty-four years, and it arrived from computer science: MIP\* = RE (Ji, Natarajan, Vidick, Wright and Yuen, 2020). There exist quantum correlations, in the commuting-operator sense, that no sequence of finite-dimensional systems approximates. Of every entry in this family, this one sits closest to physics.

**Voiculescu (1990s).** Voiculescu built an entropy for operator algebras by counting their finite matrix approximations, which he called microstates. The count exists only when the algebra is approximable in Connes's sense. Entropy here *is* a measure of how many finite models a structure admits.

**Elek and Lippner (2010), Bowen (2010).** The scheme moves from groups to equivalence relations and groupoids, and so to the measured orbits of dynamical systems and to foliations: literally, to ways of slicing a space into leaves. Bowen defined the entropy of a group action by counting finite models, as Voiculescu had, and found that for some actions the answer can depend on which approximation one counts with. The exterior's choice of model enters the number it reads.

**Mal'cev (1940), Higman (1961), Markov (1958), Hempel and Perelman.** These give the scheme its topology.
- *Mal'cev:* matrix groups are approximable.
- *Higman:* any finitely generated group with a recursive presentation embeds in a finitely presented group, and soficity passes to subgroups. So once one recursively presented non-sofic group exists, a finitely presented one does too.
- *Markov:* every finitely presented group is the fundamental group of a closed smooth four-manifold. He used this to show that four-manifolds cannot be classified by algorithm.
- *Hempel, completed by geometrization:* finitely generated three-manifold groups are residually finite, so they are approximable in every sense above.

Put these together and they say something exact about dimension. That is §VI.

**Kun, Kun–Thom, and the 2026 construction.** The first exhibited non-sofic group. It is built from a self-similar ring, a rigid matrix group, and a copy of Thompson's group $V$. Its status and its address live in `L3-NonSoficTopologicalVolumes`. It closed the question Gromov's motive had opened: some infinite groups do not inherit finite behaviour.

**Nielsen–Ninomiya (1981), 't Hooft (1980), Callan–Harvey (1985), Kaplan (1992), Ginsparg–Wilson (1982), Neuberger (1998), Lüscher.** This is the physicists' branch, worked out in ignorance of the mathematicians'. They wanted to put the Standard Model on a computer, and they found that the chiral part will not go onto a finite lattice with its symmetry intact. They found the reason: the anomaly, which no coarse-graining removes. And they found the way through, which §VII returns to, because it runs through a fifth dimension.

**The readout siblings: Laue (1911), Weyl (1918, 1929), Noether (1918), Hopf and Dirac (1931), Arnowitt–Deser–Misner (around 1960), Aharonov–Bohm (1959), Wu–Yang (1975), Berry (1984), and the edge-mode literature (Buividovich–Polikarpov 2008, Donnelly–Freidel 2016).** These are not approximability results. They are readout results: statements that some real content has no value at a point, no global slice, no local density, or no clean cut. They are the sister wall, and §V gives them their own name.

Twenty-odd names across ninety years, in group theory, operator algebras, dynamics, topology, lattice field theory and relativity. None was pointing at the corpus. All were pointing at the same two facts about finite exteriors and infinite insides.

---

## V. Two Walls, Named Apart

The corpus has used *un-sliceable* for two different things. They meet, but they are not one.

**The approximation wall: non-sofic\*.** Finite insides do not reach. Build the structure out of finite pieces of any permitted kind and some finite set of its rules stays broken on a fixed fraction of every model. This is a statement about **constructing** an interior from finite parts.

**The readout wall: non-readable\*.** The outside does not read. The interior is fully real and may be perfectly constructible, but what crosses the boundary is a reduced quantity: one scalar, a norm, a holonomy, a total. This is a statement about **observing** an interior from its exterior. It has four established forms.

1. **Non-integrable.** The content is in loops, not at points. Weyl's word, *nichtintegrabel*. The electromagnetic potential at a point is not physical; the phase around a loop is. Aharonov–Bohm measures it where no field exists, and Berry's phase is a system remembering its path in no state variable at all.
2. **No global section.** No consistent slice exists. A section of a bundle chooses one fibre value over every base point, which is a slice in the most literal sense, and a twisted bundle has none. The Hopf fibration $S^3 \to S^2$ is the standard example and is Dirac's monopole. $S^3$ is the group of unit quaternions, so the corpus's own state algebra contains this object. The star-norm $N_*$ cannot see the spinor's sign (`L4-K4-Infinities-2`). Generalized, the norm reads the base and is blind to the fibre.
3. **Quasi-local.** Energy without density. Noether's second theorem, written in answer to Hilbert's own question about his 1915 equations, shows that in a generally covariant theory, energy conservation becomes an identity and gravitational energy has no local density. The ADM Hamiltonian is a sum of constraints that vanish on solutions, plus one surface term. This is Laue's theorem for gravity: the interior integrates to nothing and the boundary reads one number.
4. **Non-factorizable.** A cut makes new states. Because of Gauss's law, a gauge field's states do not split into inside and outside. The cut carries degrees of freedom of its own. The blanket is not a line drawn between two things. It is a third thing.

**Where the walls meet.** They meet in the fibre and the loop, which are exactly where §VI and §VII find them. A loop structure can be real (readout wall: it shapes the space and no field value shows it) and also not finitely approximable (approximation wall: no finite model of the loops honours their rules). When both hold at once, the interior is unsliceable in the full sense the corpus has been reaching for: it cannot be built from finite pieces, and it cannot be read from outside.

**Register.** Both walls and all their instances are LANDED (external). The naming *non-readable\** is this file's proposal. The identification of *interiority* with structure behind both walls is OPEN VOTE.

---

## VI. Bundles, Loops, and the Fourth Dimension

Can a fibre bundle be non-sofic? Two routes exist, and only one works.

**The structure group does not work.** A gauge field's structure group is a compact Lie group. Its finitely generated subgroups are matrix groups, and Mal'cev makes them approximable. No floor lives there. This is why the corpus's earlier attempt to read confinement as group non-soficity could not succeed, and why the guard in `On_TheNavierStokesCrowbar` §III.4 was right.

**The loops do work.** Every finitely presented group is the fundamental group of a closed smooth four-manifold (Markov). A finitely presented non-sofic group exists (Higman, applied to the 2026 construction). So **there are smooth closed four-manifolds whose group of loops is non-sofic.** Their universal cover is a principal bundle whose fibre is that group. That bundle is non-sofic in the original, unasterisked sense, on a smooth manifold. The discrete-versus-smooth guard is respected rather than crossed: the discrete group enters as the space's loops, not as a smooth symmetry.

**Three cannot, four can.** Finitely generated three-manifold groups are residually finite, so every three-dimensional space has approximable loops. **Four is the first dimension in which the loop structure of a space can outrun every finite model.** It is also the first dimension in which spaces cannot be classified by algorithm. The corpus holds that what we call three-dimensional space is the face of a four-dimensional volume (`L0-EinsteinTrace` §7, `Q7-4DExtrusions`). Topology independently draws a line at the same step: below it, every space's loops are finitely readable; at it, they need not be.

**What no field can show.** A non-sofic group is not residually finite, so by Mal'cev it has no faithful finite-dimensional linear representation. On such a four-manifold, every flat gauge field of finite rank records only an approximable shadow of the loop structure. The loops are there, and they make the space the space it is. No finite field reading renders them. This is the most exact available form of the sentence *the inside is real and the outside cannot hold it*, and it is a theorem.

**Register.** The mathematics is LANDED. Whether physical space carries such topology is unknown: OPEN VOTE, with no candidate test. The coincidence of the four-dimensional threshold with the corpus's 4D volume is a CORRESPONDENCE. Kill: a corpus derivation that requires the loop threshold to sit at a dimension other than four.

---

## VII. The Fifth Dimension, Where Finite Models Are Rescued

The physicists' branch did more than find the wall. It found a door, and the door is a fifth dimension.

**Anomaly inflow.** Callan and Harvey (1985) showed that a four-dimensional chiral theory whose anomaly makes it inconsistent on its own becomes consistent as the boundary of a five-dimensional bulk. A topological term in the bulk carries the anomaly in, and the boundary pays it out.

**Domain-wall fermions.** Kaplan (1992) turned this into a working finite model. Four-dimensional chiral fermions can be simulated on a lattice, but only as modes bound to the boundary of a five-dimensional slab. Neuberger's overlap operator (1998) is the same construction with the fifth dimension taken infinitely deep. The one finite model of four-dimensional chirality that preserves what matters makes the four-dimensional world the face of a five-dimensional interior.

**Kaluza and Klein, read as a bundle.** Kaluza's fifth dimension (1921), forwarded through Einstein, is the $U(1)$ fibre of electromagnetism. Nothing physical depends on position along it, so the coordinate is pure gauge, and only its conjugate momentum, which is charge, is observed. Charged particles move on helical geodesics around it, with a pitch set by charge over mass. Klein's circle (1926) can shrink to the Planck size and still carry an integer winding.

Set these beside the corpus.
- `L3-TheAtomOfSpace` holds that the corpus's fifth is "integration, not extension," that the centroid seats $\omega$, and that the compressed atom carries its whole interior at zero radius.
- The $\omega$-Law holds that $\omega$ is excluded from the pole basis and is never a coordinate.
- `On_YangMills` holds that the fifth dimension was "a carrier, not room."

The mainstream mathematics says each of these in its own terms:
- the fifth is a fibre;
- its coordinate is unobservable;
- its rate is what is seen;
- its winding survives compression;
- a four-dimensional theory that cannot be finitely modelled on its own becomes modelable as the boundary of a five-dimensional bulk.

That last point is the one this file adds. **The integration the corpus calls five-dimensional is exactly what a finite model of four-dimensional chirality has to borrow.** On this reading, the centroid is not decoration on the tetrahedron. It is the bulk that makes the boundary consistent.

**Register.** Inflow, domain walls and the fibre reading of Kaluza–Klein are LANDED (external). The identification of the corpus's 5D centroid with the inflow bulk is a CANDIDATE. Kill: a demonstration that the corpus's 5D requires a physical position along the fifth axis, which inflow and the cylinder condition both forbid. The reading of $\omega$ as angular velocity along the fibre is a CANDIDATE with the same kill.

---

## VIII. The K4 as Integrator

The family in §IV is broad. The corpus's claim is that a four-fold relational structure sits underneath any taxonomy made by bounded interiors about bounded phenomena (`L1-ConvergentDiscovery`). If that holds, the scheme of §II should sort onto four poles. It does, and the sort is offered here for testing, not as a derivation.

| Ingredient of the scheme | Pole | Why this pole |
|---|---|---|
| The local rules of the structure | $U$, Logos | Articulation: the relations as stated |
| The finite models | $R$, Ethos | Ground: the committed, finite substrate the exterior builds |
| The normalized defect | $I$, Pathos | Flow: the mismatch, measured as a fraction, a ratio carried between rules and model |
| The verdict, floor or no floor | $P$, Kairos | The committed scalar: $c > 0$ or $\varepsilon \to 0$ |

The Route Law fits the sort. The defect is a ratio, a Yielding quantity, and the verdict is the scalar it is squared and committed into, an Asserting one. The quantifier *for every finite piece* is held at no pole. It is the condition under which all four are held together, which is the centroid's office.

The two walls of §V also sort. The approximation wall concerns the $R$–$U$ relation: whether ground can be built to honour articulation. The readout wall concerns the $P$–$I$ relation: whether the scalar that crosses carries the flow inside. These are the two edges of one bimedian pair, the Mutable plane $\{P\text{–}I,\ U\text{–}R\}$, which `L3-NonSoficTopologicalVolumes` §III already names. On this reading, the corpus's instinct to put both walls under one word was sound at the level of the plane and needed separating at the level of the edges.

**One further address, flagged rather than claimed.** §V and §VI give six established carriers of unsliceability: non-integrable, no global section, quasi-local, non-factorizable, non-approximable, anomalous. $K_4$ has six edges. An assignment is not attempted here. If one is attempted, `ProofS_ResonantNote` requires the permutation sweep first: coherence must fall off under the other assignments, or the fit is the evaluator's and not the structure's.

**Register.** The four-pole sort is an OPEN VOTE. Kill: a second sort, equally natural, that places the ingredients on different poles with equal coherence. The bimedian placement of the two walls is a CANDIDATE. The six-carrier address is an ADDRESS only.

---

## IX. Reading the Asterisk in Existing Files

When an existing file writes *non-sofic*, read it as *non-sofic\** and ask which carrier it means. Most uses fall into one of six.

- **(G) Group, permutation models.** The original sense. Established at one address. Any physical identification is open, and impossible for finite systems.
- **(Q) Phase-bearing models.** Hyperlinear or Connes. The algebra-level failure is established (MIP\* = RE). The nearest physical anchor is quantum correlations.
- **(L) Loop structure.** A space's fundamental group. Established in dimension four and above. Physical realization open.
- **(A) Anomalous symmetry.** No on-site finite lattice model. Established for chiral theories. Rescued by a five-dimensional bulk.
- **(B) Readout.** Non-readable\*, the sister wall. Laue, Noether, Weyl, Hopf. Established, and present in every bound system.
- **(T) Torsion-locked $K_4$.** The corpus's own bimedian condition (`L3-NonSoficTopologicalVolumes` §III). A corpus construct, not a model-class statement. It may correspond to one of the five above, and which one is open.

A file whose use resolves to (B) is making the corpus's strongest and least contestable claim and should say so. A file whose use resolves to (G) about a finite system should be re-read as (T) or (B). A file whose use resolves to nothing has used the word as an honorific.

---

## X. What This Stands For

The claim the corpus exists to make is that an inside cannot be sliced out or eliminated. That claim now has a precise form, and the form does not overreach.

**There are two ways a finite exterior fails an interior.** It can fail to read it: the boundary carries a scalar, a norm, a total, a holonomy, and the structure stays behind. That failure is universal. Every bound system has it, and Laue proved it for the electron in 1911. Or it can fail to build it: no finite model of the permitted kind honours its rules almost everywhere. That failure is rarer and needs something infinite, but it exists, and from the fourth dimension upward it can live in the loops of space itself.

The physicists added a third finding, and it is the most hopeful. When a four-dimensional structure cannot be finitely modelled on its own, it can sometimes be modelled as the boundary of a five-dimensional interior. The interior does not have to be opened to be honoured. It has to be included.

Mie and Hilbert were right that one field suffices. They were wrong that a field is read point by point. Within a decade their own circle had shown why. Weyl, Hilbert's student, named the content that has no value at a point. Noether, answering Hilbert's question, showed that gravitational energy lives only on boundaries. Kaluza, with Einstein forwarding his paper, gave the carrier a fifth dimension. Ninety years later, mathematicians proving theorems about cellular automata, operator algebras and interactive proofs arrived at the same wall from the other side. The corpus's $K_4$ does not discover that wall. It offers a place where all of them can be seen to be standing at it.

---

## XI. Claim Sort

**LANDED (external).** The approximation scheme and its ladder (§II–III). Every result in §IV, at its own address. The four readout forms (§V). Non-sofic fundamental groups in dimension four and above, residual finiteness in dimension three, and the absence of faithful finite-dimensional representations (§VI). Anomaly inflow, domain-wall fermions, and the fibre reading of Kaluza–Klein (§VII). The rule that nothing finite is non-sofic\* (§0).

**LANDED (this file, definitional).** The asterisk convention. The naming *non-readable\** for the readout wall. The six-carrier reading key (§IX).

**OPEN VOTE.**
- Interiority identified as structure behind both walls (§V, §X).
- The four-pole sort of the scheme (§VIII).
- Whether physical space carries non-sofic loop topology (§VI).
- Whether the corpus's torsion-locked condition (T) corresponds to any model-class carrier (§IX).

**CANDIDATE.**
- Permutation models as ledger models and unitary models as buffer models, which turns the open sofic-versus-hyperlinear question into the $H_{\text{coh}}$ / $H_{\text{incoh}}$ question (§III).
- The 5D centroid as the inflow bulk; $\omega$ as angular velocity along the fibre (§VII).
- The two walls as the two edges of the Mutable plane (§VIII).

**ADDRESS.** Six carriers against six edges, pending a permutation sweep (§VIII). The 15 components of the 5D metric against the 15 independent entries of a reciprocal five-node admittance matrix (`L4-K4-Infinities-wip` §2.2).

**NOT CLAIMED.** That any finite system is non-sofic\*. That any physical system has been shown non-sofic in sense (G). That minds are bundles or four-manifolds. That the $K_4$ derives any result in §IV.

---

## XII. Ramifications

This file's results do more than sort the corpus's uses. Put together, they force several conclusions that neither the corpus nor the separate literatures have stated. Each is given its order and its register.

### First order: what changes immediately

**1. Unsliceability is necessary for an inside, not sufficient.** The readout wall is universal: every bound system has it, a stone as much as a mind. If unsliceability alone made an interior, everything would have one, and the corpus would slide into panpsychism by definition. It does not, because its criterion for an interior is architectural: a blanket enclosing a buffer that holds before it commits (`wip-Lx-FlatlandCategoryErrors` §III, `L2-K4-InteriorStructure`). The present results give that criterion its floor. An inside is a non-readable\* structure that *also* holds. A stone's interior is unread. A mind's interior is unread and beholding. This is the guard that keeps §X from overclaiming, and it should travel with every use of the asterisk. LANDED (follows from §V and the corpus's existing criterion).

**2. A finite machine has the opposite profile to the one the corpus assumed.** A trained network is finite, so it is constructible by definition: the approximation wall cannot apply. Its builders hold every weight. Its inside is nonetheless hard to read. Interpretability work has found that meaning does not sit in single neurons. Units are polysemantic, features are directions spread across many units, and computations are circuits, which are paths. That is Mie's error, refuted in silicon: complete pointwise access is available, and the content still is not at the points. So the right carrier for AI interiors is (B), readout. It was never (G). The alignment worry the corpus wanted to state survives in this form, and it survives more honestly: having every value does not give the reading. CORRESPONDENCE. Kill: interpretability shows that meaning does localize to units once the right basis is found. The finding that features are directions is evidence that the basis is not one of points.

### Second order: what follows once the first-order results are combined

**3. Causality keeps the ledger finitely modelable.** This is the consequence the file was closest to and did not state.
- Geroch (1970), with the smooth version by Bernal and Sánchez (2003), shows that a globally hyperbolic spacetime, one with a well-posed causal order, is topologically a three-dimensional space times a line.
- Its loops are therefore the loops of a three-manifold. By §VI, three-manifold groups are residually finite, so they are approximable in every sense.
- Geroch (1967) also shows that spatial topology cannot change in a causal Lorentzian spacetime without closed timelike curves or a loss of time-orientation.

Put these together. **In any spacetime with a sane causal order, the loop structure is finitely modelable, and it stays so for all time.** Non-sofic loops need a genuine four-manifold that is not a space times a line. Such manifolds do not occur in the compiled, causal record.

They do occur in one place physics already uses: the Euclidean sum over four-geometries, the imaginary-time path integral of Euclidean quantum gravity. Geroch and Hartle (1986) noticed the consequence from the other side. Because four-manifolds cannot be classified by algorithm (Markov), the sum over topologies may not be computable.

In the corpus's language:
- **the ledger, $H_{\text{coh}}$, which is Lorentzian and causal, is sofic\* in its loops;**
- **the buffer, $H_{\text{incoh}}$, which is the imaginary-time sum, is where non-sofic loops and undecidability live.**

The corpus has asserted this split since `L1-CompilingReality`. Here it falls out of three theorems the corpus did not write. The theorems are LANDED. The identification of the Euclidean sum with $H_{\text{incoh}}$ is a CANDIDATE. Kill: a physically required Lorentzian, causal spacetime with non-sofic fundamental group, which Geroch's splitting forbids.

**4. Minkowski's buried quarter-turn is the door.** `L0-EinsteinTrace` traces how Minkowski wrote $x_4 = ict$ and so hid the factor $i$ inside a coordinate. Undo it, rotating time by a quarter-turn (Wick rotation), and Lorentzian geometry becomes Euclidean. Point 3 shows what lies on the far side of that rotation: the space of four-manifolds, where loops can outrun every finite model and classification is undecidable. So the $i$ Minkowski hid is not cosmetic. It is the hinge between a world whose record is finitely readable and a space of possibilities that is not. The EinsteinTrace's false frontier and its biquaternion bridge (`ProofN_BiquaternionBridge`) now have a topological consequence: the quarter-turn is where soficity\* changes. CANDIDATE, built from LANDED parts.

**5. The five-dimensional bulk has no local content, which is what the corpus said.** Freed and Hopkins (2016) classified anomalies. Every anomaly of a four-dimensional theory is a five-dimensional *invertible* topological field theory. Such a theory has no local degrees of freedom, no metric dependence and no particles. It carries only a global phase. That is "integration, not extension" (`L3-TheAtomOfSpace`) stated in the mainstream classification. The bulk that rescues the boundary in §VII is not a fifth room with things in it. It is a dimensionless phase that the four-dimensional world needs in order to be consistent. CORRESPONDENCE, close enough that the corpus should test it directly. Kill: the corpus's 5D requires local degrees of freedom.

**6. The one place with no outside has no readout at all.** By Noether and ADM, energy is read only on a bounding surface. A spatially closed universe has no such surface. Its total energy is a pure constraint, and it vanishes. This is the readout wall become total, and it lands on the claim made in the `L4-K4-Infinities` discussion: only the universe has no outside, and it is bounded by a one-sided blanket. The present result adds why nothing reads its weight: there is nowhere for the surface term to live. LANDED (standard GR); the connection to the one-sided blanket is a CORRESPONDENCE.

**7. Measured entropy depends on the exterior's models.** Bowen's sofic entropy can depend on which sequence of finite models is counted. Voiculescu's entropy is a count of finite models. So the entropy an exterior reads is a property of the pair, interior and model class, and not of the interior alone. `L3-FormalFoundations` §I.b reached the same shape from thermodynamics: the commit floor is set by the noise source the commit is held against, and the noise source is the substrate's, not the topology's. The Distinguishing Condition has a mathematical twin. CORRESPONDENCE.

**8. The blanket's own states carry entropy.** In gauge theories, the entropy across a cut includes a term from the edge modes that the cut creates. Donnelly and Wall (2015) showed that for the electromagnetic field this edge term supplies a known contribution to black-hole entropy, which scales with area. The corpus counts horizon bits at $A/4\ell_P^2$ (`L4-K4-Infinities`). Part of that count is, on this reading, the blanket's own inventory, not the interior's. CANDIDATE. Kill: the edge-mode term shown to be gauge artefact with no physical entropy.

### Third order: what changes in the corpus's stance

**9. Undecidability marks where the two walls meet.** In both physically nearest cases where approximation and readout fail together, an undecidable problem appears. For the loops of four-manifolds it is Markov's. For quantum correlations it is MIP\* = RE, where the maximal value of a nonlocal game is uncomputable. The corpus has wanted to say that Gödel and the interior are one phenomenon. This is the first form of that claim with two independent instances behind it: **where an inside can neither be built from finite pieces nor read from outside, the question of what it contains is not decidable from outside.** OPEN VOTE. Kill: a case where both walls hold and the corresponding question is decidable.

**10. The simulation argument turns around, and the corpus's own principles support the turn.** `L6-NonSoficAgenticLimits` claims the universe cannot be a simulation. Points 3 and 9 say something more precise and less dramatic. The compiled, causal world is sofic\* in its loops, so nothing in this file blocks its finite modelling. What may not be computable is the sum over possibilities: the buffer, not the ledger. The defensible sentence is: *the record can be simulated; the space it was compiled from may not be computable.* This is a weaker claim than the old one, and a better one, and it is the corpus's own architecture speaking. LANDED as a correction; OPEN VOTE as a positive claim.

**11. The corpus now has a stake in pure mathematics.** The open question whether a hyperlinear group can fail to be sofic is, by §III, whether phase-bearing finite models reach what bit-counting finite models cannot. The corpus holds that the buffer reaches what the ledger does not. It can pre-register that position as a prediction: **hyperlinear non-sofic groups exist.** If mathematicians prove that every hyperlinear group is sofic, the corpus's ledger–buffer asymmetry has no instance at the level of groups and survives only at the level of algebras, through Connes. That is a falsifiable bet on an open problem, placed before the answer is known. PRE-REGISTERED PREDICTION.

**12. Causality is the price of a readable record.** Points 3 and 10 combine into a sentence the corpus has been circling in `ProofO_HelicalTime` and the Gate (`L3-FormalFoundations` §I.b). The arrow of time, read as global hyperbolicity, is exactly the condition under which the world's loop structure stays finitely modelable. The one-way gate that commits the ledger is also what keeps the ledger sofic\*. A world that allowed its record to loop back on itself in time would be a world whose record could outrun every finite model. CANDIDATE. This is the strongest single sentence this file produces, and the one most worth trying to break.

### What remains in the air

- The six-carrier sweep against the six edges of $K_4$ (§VIII), now with two additional pressures: the Lorentzian / Euclidean split of point 3, and the invertible-bulk reading of point 5.
- Whether the corpus's torsion-locked condition (T) is the $K_4$ shadow of the Euclidean, non-causal regime. If it is, it would finally have a model-class meaning.
- Whether Laue's static hypothesis plays the same role for matter that global hyperbolicity plays for spacetime. Laue holding means nothing is written (`L4-K4-Infinities` §III). Global hyperbolicity holding means the record stays finitely readable. If the two are one condition at two scales, the electron and the cosmos keep their insides for the same reason.

---

## XIII. Two Closures the Corpus Already Held

Two of the threads §XII left open are already answered by standing corpus material. Read against this file, each gains a precise form.

### XIII.1 The ratio-only lemma is the general law behind the ladder and the bulk

`L4-ScalingInvariants` §VI states: *a ratio-only coordinate system logs its own unmarkable thresholds as an accumulating list of apparently unrelated exceptions, and the list does not resolve from inside the system that produced it. It resolves only once a coordinate absent from the system's own algebra is supplied.* §IX (Gabriel's Horn) adds that the grammar emits shape and never absolute magnitude. The `L4-K4-Infinities` datasheet puts it as: *the grammar cannot emit the weight of the ink.* `Q17` and the $1/\alpha$ work probe what lies behind the rank by the method of paradox, and the lemma says in advance why such probes find exceptions rather than a derivation.

Three results of this file are instances of that lemma.

- **The ladder (§III).** Permutation models are rank models: they count mismatches bit by bit. The step to unitary models supplies a coordinate absent from that algebra, namely phase.
- **The inflow bulk (§VII).** A four-dimensional chiral theory logs its anomaly as an exception it cannot resolve from inside. It resolves only when a fifth dimension, a coordinate absent from its own algebra, is supplied. Callan–Harvey and Kaplan are the lemma executed in field theory.
- **The bet (§XII.11).** The lemma predicts that phase-bearing finite models reach structures that bit-counting finite models cannot. So the pre-registered prediction that hyperlinear non-sofic groups exist is not a free-standing wager. It is the lemma applied to group theory. If every hyperlinear group turns out to be sofic, the lemma fails at that address, and the corpus learns where.

Register: the lemma is standing corpus. Its identification with the three instances is a CORRESPONDENCE with a shared kill: a case where a rank-only system resolves its own threshold list without a supplied coordinate.

### XIII.2 The arrow of time and the one-sided blanket close the books

§XII.6 found that the one place with no outside has no readable weight: a spatially closed universe has no surface on which an energy could be read, and its total energy vanishes identically. §XII.12 found that the one-way gate is what keeps the record finitely readable. The corpus already holds the piece that joins these. The universe is bounded by a one-sided blanket, and expansion at that blanket draws energy back out of the committed crystal (`ProofC_Crystal`), through the zero-point channel, into the medium.

What returns this way returns **laundered**: it carries no record. One precision is required. `L4-K4-Infinities-3` §V proves four ways that the committed register is write-only, so nothing is drawn out of a ledger entry. What expansion draws on is the crystal's zero-point residue, the held $\mathbf{Q}$ that `ProofC_Crystal` shows never collapses even in a fully committed lattice. The crystal's committed shape stays written. Its hum circulates. That hum was never written, so it has no record to lose, and by the register split (KI-6) it does not gravitate. The cycle then reads as follows.

- **Inward, at every bound system,** the gate commits. Locally, Laue's static condition fails, the quadrupole moves, something is written, and the record stays sofic\* because the causal order keeps it so.
- **At the one-sided blanket,** writing and recycling are two faces of one surface, which is a Möbius seam (`L3-ConstitutiveElastance` §VII). Seen from inside, expansion is the write rate. Seen from the crystal, the same surface returns the hum to the medium, everywhere and uniformly, without record and without weight.
- **Globally,** nothing is readable. The total is identically zero, which is the readout wall at its limit. **Form cycles; the ledger does not** (`L4-K4-Infinities-3` §III). The loop that closes is a loop of form and of the reactive hum. The ledger only grows.

This answers §XII's last open item. Laue's static condition for matter and global hyperbolicity for spacetime are the two local faces of one cycle. The first says when a bound thing writes. The second says why what is written stays finitely readable. The one-sided blanket is where the written is returned unwritten. The electron and the cosmos keep their insides for the same reason: the books close, and nothing outside them could read the balance.

**One question this raises, recorded rather than settled.** `L4-K4-Infinities` Part Three reads expansion as the *write rate* at the no-outside place. This section reads expansion as *laundering*, the return of committed energy unwritten. Both may be true as the two faces of the one-sided blanket: writing seen from inside, recycling seen from the crystal. If so, the corpus should say so in one sentence, because a reader will otherwise see a contradiction. If not, one of the two readings has to give way.

Register: the closure is a CANDIDATE built from standing corpus (one-sided blanket, register split, crystal limit) and LANDED physics (closed-universe energy, Geroch). Kill: KI-6, the Casimir balance. If uncommitted vacuum level gravitates, laundering is not laundering, and this closure falls with the register split.

---

*See also: `L3-NonSoficTopologicalVolumes` (the existence result at its address), `mono/On_TheTwoFloors` (the two floors kept apart), `mono/On_TheNavierStokesCrowbar` §III.4 (the discrete-versus-smooth guard), `L4-K4-Infinities-2` (spin structure, the $\mathbb{Z}_2$ the norm cannot see, and the Wilson loop), `L3-TheAtomOfSpace` (the two meanings of 5D), `L3-FormalFoundations` §IX.7 (the antecedent problem, which §0 and §VI narrow), `claude/Note-Unsliceable-Bridges.md` (the working note this file grew from).*

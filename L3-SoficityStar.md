# Soficity\*
## What It Means for a Structure to Outrun Its Finite Models, and Why So Many Fields Found the Same Wall

*L3, definitional. A companion to `L3-NonSoficTopologicalVolumes`, which keeps the existence result. This file keeps the meaning. Wherever the corpus writes **sofic\*** or **non-sofic\***, the asterisk (sometimes invisible) points here.*

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
   * **Two-terminal relational probe (`CANDIDATE` — edge-stored reading):** Upgraded from a single-blanket defence to a relational probe between two vertices. Local unreadability at each vertex means the state has migrated onto the non-factorizable edge volume between them, so classical side-channel comparison across the two terminals breaches neither vertex's interior and still reconstructs the shared edge inventory. This mechanism runs directly on gauge-cut edge modes (Donnelly–Freidel) and does not require infinite-dimensional commuting-operator correlations beyond finite tensor-product approximations (which sit on the approximation-wall `(Q)` rung of §III–§IV).

**Where the walls meet.** They meet in the fibre and the loop, which are exactly where §VI and §VII find them. A loop structure can be real (readout wall: it shapes the space and no field value shows it) and also not finitely approximable (approximation wall: no finite model of the loops honours their rules). When both hold at once, the interior is unsliceable in the full sense the corpus has been reaching for: it cannot be

---

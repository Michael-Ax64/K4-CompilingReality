# L4-Riemann-3
## Part Three — The Neighbours

*Reads with `mono/On_TheCompassOfElea`, `L4-TheTwelveGates` §II-b, `L0-ParadoxEngine`. Continues from `L4-Riemann-2`; continues in `L4-Riemann-4`.*

---

For a hundred years the literature has been working on the structure line one set aside, from several directions at once, and each programme is best read on its own terms first. Honouring the neighbours means stating what each is after in its own vocabulary before any translation, and saying where a neighbour got somewhere this series has not.

None of the works below was a source for the corpus. Each is terrain this file crosses.

---

## I. The Geometric Trinity

The most important thing modern metric-affine geometry has shown is that the choice of connection is not a matter of taste about which there is no evidence. There are three exact reformulations of gravity, and they are known.

```
========================================================================================
                         THE GEOMETRIC TRINITY OF GRAVITY
========================================================================================

  THEORY                        NON-ZERO TENSOR   CONNECTION                  READING
  ──────────────────────────────────────────────────────────────────────────────────────
  1. General Relativity (GR)    Curvature (R)     T = 0, Q = 0 (Levi-Civita) Gravity bends
     (Einstein 1915)                                                         geodesics.

  2. Teleparallel (TEGR)        Torsion (T)       R = 0, Q = 0 (Weitzenböck) Gravity twists
     (Einstein 1928)                                                         tetrad lines.

  3. Symmetric Teleparallel     Non-metricity (Q) R = 0, T = 0 (coincident)  Gravity stretches
     (STEGR) (Nester–Yo 1999)                                                rulers.
========================================================================================
```

The three actions differ by a boundary term (Beltrán Jiménez, Heisenberg and Koivisto 2019):

$$S_{\text{EH}} = \int R \sqrt{-g}\,d^4x \quad\Longleftrightarrow\quad S_{\text{TEGR}} = \int \mathbb{T} \sqrt{-g}\,d^4x \quad\Longleftrightarrow\quad S_{\text{STEGR}} = \int \mathbb{Q} \sqrt{-g}\,d^4x$$

In GR all of gravity's degrees of freedom sit in the metric. In TEGR curvature is set to zero and gravity is carried entirely by a torsion scalar built from four orthonormal tetrads. In STEGR curvature and torsion both vanish in the coincident gauge, and gravity is carried by the non-metricity scalar.

There are two lessons, and the second is the one the literature does not usually draw.

**The first is standard.** Nature does not force physics to use curved space. "Bent space" is what you get by insisting on Levi-Civita. The same gravitational universe can be described with flat space and torsion, or with flat, torsion-free space and a variable ruler. Anyone who says curvature is *the* geometry of gravity is reporting a choice as a discovery.

**The second is the one to carry forward.** Dynamical equivalence is not structural equivalence, and the difference is exactly a boundary term. Two theories that differ by a boundary term agree on every bulk field equation and disagree on what is written on the boundary. In the corpus's vocabulary the boundary is the blanket, and a boundary term is what the blanket records. So the Trinity is not three descriptions of one thing. It is one bulk and three different ledgers. A framework whose central claim is that only the committed gravitates, and that the committed is the ledger, cannot treat a difference of ledger as a difference of nothing.

The Trinity is the strongest available evidence that line one was a choice. Read carefully, it is also evidence that the choice was not free.

---

## II. The Lineage, and the Fossil Word

```
                          CHRONOLOGICAL LINEAGE

   1854: Riemann ──► Metric tensor g_ij. Quartic case flagged and declined.
   1915: Einstein ──► General Relativity (R ≠ 0, T = 0, Q = 0)
   1918: Weyl ──► Non-metricity as electromagnetism (Q ≠ 0). Einstein objects.
   1918: Finsler ──► Riemann's declined case, formalized (direction-dependent F(x,v))
   1922: Cartan ──► Spin couples to torsion (R ≠ 0, T ≠ 0)
   1927: London ──► Weyl's scale factor re-read as a PHASE factor
   1928: Einstein ──► Teleparallelism (R = 0, T ≠ 0)
   1929: Weyl ──► "Elektron und Gravitation": gauge theory as U(1) phase invariance
   1955: Kröner / Bilby ──► Crystal defects (dislocations = T, disclinations = R)
   1961: Kibble / Sciama ──► Poincaré Gauge Theory
   1973: Teitelboim ──► The constraint algebra closes with structure FUNCTIONS
   1982: Nieh–Yan ──► The topological four-form built from torsion
   1995: Jacobson ──► Einstein's equation as an equation of state
   1999: Nester–Yo ──► Symmetric teleparallel gravity (R = 0, T = 0, Q ≠ 0)
```

### Weyl's ruler, and the word that survived him

In 1918 Hermann Weyl proposed that lengths depend on the path a ruler has travelled — non-metricity — and that the one-form describing the dependence be electromagnetism. He called the freedom to recalibrate at each point **Eichinvarianz**: *eichen*, to calibrate, to certify a measure. Gauge invariance was, originally and literally, ruler invariance.

Einstein's objection, appended to Weyl's own paper, is one of the great short arguments in physics. If length depended on history, two identical atoms with different histories would show different spectral lines. They do not. Sharp spectral lines refute a physical scale gauge. The objection was correct and it killed the physics.

It did not kill the mathematics. In 1927 Fritz London read Weyl's scale factor again as a **phase** factor: swap the real exponent for an imaginary one, and path-dependence becomes a quantum-mechanical phase rather than a change of length. In 1929 Weyl published *Elektron und Gravitation*, and the structure became $U(1)$ gauge theory — the whole of modern gauge field theory, descended from a dead proposal about rulers, with the dead proposal's word still on it.

**"Gauge" is a fossil.** Every physicist uses a word meaning *calibration of a measuring rod* for something that has not been a measuring rod since 1927. The word is the receipt for a deletion, and the field has carried the receipt for a hundred years without reading it. The pattern has three steps: an assumption adopted for a reason, a patch applied when the assumption broke, and the patch so thoroughly enshrined that the vocabulary of the original problem survives as a dead metaphor while the problem is marked solved.

### The general form of the freeze

`L4-TheTwelveGates` §II-b states the failure in its cleanest form, while doing something else entirely — fixing the handedness of the seasonal turn:

> "**A claim of 'clockwise' that does not say which vantage is undefined.** This is the whole class of orientation-and-origin inconsistency that plagues current-flow diagrams, cross-product conventions, and screen-vs-sky orientation: a handedness asserted without its viewing normal, then mis-read by everyone standing at the other end of it."

That is the freeze in general. Not a false statement — an **underspecified** one, adopted because specifying it was tedious, and then inherited by readers who could not see what was missing because the missing part had never been written down. The remedy is the only one there is: *"This document fixes it locally by stating both, every time."*

Riemann stated his. That is the irony at the centre of the subject. He named the restriction, priced the alternative, and moved on. The price estimate was inherited and the flag was not.

### Cartan's torsion stayed geometric

In 1922 Élie Cartan saw that Levi-Civita was more constrained than it needed to be, allowed $T \neq 0$, and proposed that **intrinsic spin** be its source, as mass-energy is the source of curvature. In Einstein–Cartan theory the action is the curvature scalar, varied independently with respect to the tetrad and the spin connection:

* **Varying the tetrad** gives Einstein-like equations, with energy-momentum sourcing curvature.
* **Varying the spin connection** gives the **Cartan equation**,
  $$T^\lambda_{\ \mu\nu} + \delta^\lambda_\mu T^\rho_{\ \nu\rho} - \delta^\lambda_\nu T^\rho_{\ \mu\rho} = 8\pi G \, S^\lambda_{\ \mu\nu}$$
  with $S$ the spin density of matter.

The Cartan equation is **algebraic**: no derivative of torsion appears in it. So in Einstein–Cartan theory torsion does not propagate, it vanishes outside spinning matter, and the vacuum theory is vacuum GR.

**A correction of record, because an earlier draft got this wrong and the error is common.** The inertness of torsion is a property of **Einstein–Cartan's particular action**, not of torsion. Poincaré gauge theory propagates torsion as a vacuum wave by adding quadratic terms; TEGR carries all of gravity in it; and Part Five of this file writes an action in which the shear acquires dynamics from torsion without any added kinetic term. Anyone who reaches for "torsion is non-dynamical" as a reason not to look has quoted one Lagrangian and called it a law.

### The crystal, which is not an analogy

In the 1950s and 1960s solid-state physicists found that non-Riemannian geometry is the mathematics of **real crystal defects** (Kröner 1958; Bilby, Bullough and Smith 1955; Kleinert 1989):

```
========================================================================================
                      CRYSTAL DEFECTS VS. SPACETIME GEOMETRY
========================================================================================

  CRYSTAL DEFECT           GEOMETRIC ANALOGUE      OBJECT                 PHYSICAL EFFECT
  ──────────────────────────────────────────────────────────────────────────────────────
  Disclination             Curvature               Riemann tensor (R)     Rotational defect;
  (missing wedge)                                                         closes with deficit angle.

  Dislocation              Torsion                 Torsion tensor (T)     Translational defect;
  (slipped plane)                                                         Burgers vector.

  Point defect             Non-metricity           Disformation (Q)       Change in local
  (interstitial/vacancy)                                                  spacing or density.
========================================================================================
```

Kleinert's **world-crystal hypothesis**: if spacetime is a lattice at Planck spacing, smooth GR is the continuum limit of a crystal full of fluctuating dislocations and disclinations.

Hold onto the crystal. It is also `L0-ParadoxEngine`'s own worked example — frozen at the large scale, vibrating at the small one, neither state causing the other — and that is the licence for the route Part Six ends on. It is also where a frame field meets a discrete symmetry group in practice: every crystal's frame field is a reduction of the rotation group to a finite subgroup, which Part Five uses when it corrects an impossibility argument about soldering.

---

## III. The Neighbours Proper: Who Has Been Reaching for the Missing Piece

### Poincaré gauge theory — restoring the generator

Kibble (1961), Sciama (1962), and Hehl and collaborators (1976) wrote gravity as a gauge theory of the Poincaré group, translations combined with Lorentz rotations.

* **Translations:** the gauge field is the coframe $e^a_\mu$; the field strength is **torsion**, $T^a = de^a + \omega^a{}_b\wedge e^b$.
* **Lorentz rotations:** the gauge field is the spin connection $\omega^{ab}_\mu$; the field strength is **curvature**, $R^{ab} = d\omega^{ab} + \omega^a{}_c\wedge\omega^{cb}$.

With quadratic invariants added, **torsion propagates as a vacuum wave**, with new spin-0 and spin-2 modes.

*What it restores:* the generator. In Poincaré gauge theory torsion has its own equations of motion; it is a dynamical object and not bookkeeping. In corpus terms it is the attempt to give the rate its own dynamics. Part Six states what it costs.

### Twistor theory — restoring the light cone as primary

Penrose (1967) gave up the primacy of spacetime points. The arena is twistor space, a four-dimensional complex space; a spacetime point is an emergent object, a holomorphic sphere embedded in it. The theory natively describes massless chiral fields; the light cone is fundamental and distance is derived. Curvature enters as a deformation of how holomorphic patches are glued together — the non-linear graviton — which solves the self-dual Einstein equations automatically.

*What it restores:* **chirality as a primitive.** Twistor theory is handed from the start; self-duality is not an extra condition imposed on it but the shape of the construction. It is the one programme on this list that begins with the handedness instead of trying to recover it. The corpus should regard the non-linear graviton as its nearest external relative — and should read the fact that twistor theory's natural home is the self-dual sector, half the theory, as an honest statement of what starting from the handedness costs.

### Non-commutative geometry — restoring the commutator

Connes (1994): geometry without points, the manifold replaced by an algebra of functions acting on a Hilbert space. A geometry is a **spectral triple** — a possibly non-commutative coordinate algebra, a Hilbert space of fermion states, and the Dirac operator. Chamseddine and Connes showed that a single spectral trace,

$$S = \mathrm{Tr}\!\left(f\!\left(\frac{\mathcal{D}}{\Lambda}\right)\right),$$

for the right algebra, yields both the Einstein–Hilbert action and the full Standard Model Lagrangian with the Higgs.

*What it restores:* the name says it. Non-commutative geometry restores non-commutativity, and it does it by making the **Dirac operator** the fundamental object. The Dirac operator is first-order; the metric's natural object is second-order. A framework whose commits are first-order acts should expect its unified object to look like a Dirac operator rather than a metric, and Connes' result is that expectation met from the other side, with the construction supplied. It is also no accident that the Dirac operator is where torsion's axial part couples to matter, which is the channel Part Five finds forced.

### Discrete, simplicial and causal models — restoring the order

* **Regge calculus (1961):** piecewise-flat simplicial spacetime; curvature is a deficit angle concentrated on hinges of codimension two. *Restores:* the hinge — a place where the geometry is allowed to fail to close.
* **Loop quantum gravity and spin foams:** the metric replaced by an $SU(2)$ connection and a densitized triad; space as a spin network with spins on edges and volume quanta at nodes. *Restores:* the connection as primary and the metric as derived. The Barbero–Immirzi parameter, the one free number in the scheme, is a chiral weighting, and Part Five records why the corpus must not borrow its value.
* **Causal dynamical triangulations:** a path integral over simplices each carrying an explicit timelike arrow. *Restores:* the arrow, by hand, as an admissibility rule.
* **Causal set theory (Bombelli, Lee, Meyer, Sorkin 1987):** the continuum replaced by a locally finite partially ordered set. Its slogan is **"Order + Number = Geometry."** *Restores:* the order, and names it first.

Read down that list: deficit angles, a chiral weighting, an arrow imposed as a rule, order promoted to the title. Four independent programmes, each restoring a different part of the affine structure. None of them describes itself as recovering something line one removed, and none of them needs to: each has its own reasons, stated in its own literature.

**One comparison, offered as a difference rather than a ranking.** *Order + Number = Geometry* takes the partial order as given data and builds geometry on it, which is a clean and deliberate starting point rather than an omission. The corpus starts a step earlier and treats the order as **generated**, by a pair of face-readings that do not commute, one orthogonal act per step (`L3-TheSelfProjectingBraid` §IV: history is *"forced, at right angles to the traversal, by the XOR bottleneck the Braid cannot pass without collapsing"*). Where causal set theory posits the partial order, the corpus posits the thing that writes it. Whether that difference computes anything is open, and this file does not claim it does.

---

## IV. Ramifications: What Happens If You Let It Back In

If torsion or non-metricity take part, the consequences cascade. The literature on this is good and it is reported at its own confidence.

### First order: geodesics and autoparallels split

In Riemannian geometry "straight line" is unambiguous, because two definitions coincide: **extremal curves**, whose length is stationary, and **straightest curves**, whose tangent is carried along parallel to itself. Under $T \neq 0$ they split. Spinless test particles follow extremal curves, governed by the metric alone, and **do not feel torsion**. Particles with intrinsic spin couple to the connection and follow paths deflected by contortion.

That is why torsion is hard to see. Ordinary unpolarized rocks follow ordinary geodesics. Only polarized spinning matter departs from them.

*The reading.* The split is the corpus's distinction between the undirected and the directed reading of an edge, appearing in the literature of 1976 under another name. Length is a scalar, blind to direction and symmetric under reversal: the undirected reading. Transport has a sense, and what is carried remembers it: the directed reading. Torsion is exactly the difference. The departure is visible to things that carry their own orientation and invisible to things that do not — and Part Five's averaging result is the same statement at the level of populations.

### Second order: the four-fermion contact interaction

Because the Cartan equation is algebraic, it can be substituted back into the action. The result is GR plus a spin–spin contact term,

$$\mathcal{L}_{\text{eff}} = \mathcal{L}_{\text{Einstein}} \;-\; 3\pi G\,(\bar\psi\gamma_\mu\gamma_5\psi)(\bar\psi\gamma^\mu\gamma_5\psi),$$

suppressed by Newton's constant — about twelve orders of magnitude below the weak interaction at ordinary densities — and growing as the square of the density while gravity grows linearly. Part Five recovers this term as a consistency check on its own action.

### Third order: the Trautman bounce

Trautman (1973) showed that the spin–spin term becomes **repulsive** at very high density. Near the Cartan density, roughly $10^{38}\ \mathrm{g\,cm^{-3}}$, it overcomes gravitational attraction: a collapse halts at finite radius, and no singularity forms. Popławski developed the cosmological version, in which each black hole opens a non-singular universe on its far side.

**Stated carefully, because an earlier draft overstated it.** The initial singularity is an artefact of assuming zero torsion **within Einstein–Cartan theory**. That is a statement about one theory, not a proof that nature bounces. It is a real and important existence result — *a geometrically natural, minimally modified theory removes the singularity without exotic matter* — and it is not an observation. `On_TheCompassOfElea` supplies the register for holding it: the **Honest Tear**, where *"the equation blows up to report the boundary of its own applicability."* The singularity of GR is honest. It is the equation reporting that line one has run out. Reading the report as a prediction about a place is the error; reading it as a receipt is the correction.

---

## V. Why Not 1922

The tools are old. Cartan's torsion is from 1922, Weyl's non-metricity and Finsler's direction-dependent length from 1918, and the decomposition was textbook material in Schouten by 1954. The natural suspicion is that an argument built from such parts would have been built long ago if it were any good.

Four things answer that, and the first is the one that matters, because it removes the implication that anybody was asleep.

**Nobody declined the alternative, because until 1922 there was no alternative to decline.** The torsion-free connection was not chosen over a rival. There is no connection at all in Riemann's 1854 lecture; Christoffel supplied the symbols in 1869 and Levi-Civita parallel transport in 1917, and both were building the only connection then available. The affine connection as a general object that *may* carry torsion is Cartan's, 1922 — sixty-eight years after the line element, and seven years after General Relativity had been written in the symmetric one and begun to be confirmed. So the decision this series itemizes was made before its alternative existed as an object, and by the time the alternative existed, the symmetric connection was the foundation of a working theory. That is chronology, not negligence, and it is the honest answer to "why was there never a flag": Riemann flagged what he could see, which was the line element, and there was nothing else on the table to flag.

**Two of the pieces are recent.** The Geometric Trinity in its present form — three exact reformulations differing by a boundary term — was assembled in 2019. Before that, "you could use torsion instead" was a programme; after it, it is a theorem, and Section I cannot be argued without it. Jacobson is from 1995. The window opens in the late nineties, not the twenties.

**The constraint-algebra result was filed under the wrong heading.** Teitelboim's 1973 result, that the algebra of hypersurface deformations closes only with structure functions, is fifty years old, fully understood, and almost universally read as an obstacle to quantization rather than as a report on a classical assumption. That is a failure of direction, not of rigour. Nobody read it as evidence against the decree that the constraint net orders, because the decree had never been written down as a decree. An unflagged assumption does not collect counter-evidence. It collects problems, each filed in its own subfield. Part Four reads it as the report.

**And the honest answer: much of this file is a reading, and readings are cheap.** The friction reports of Part Four map corpus structures onto geometric ones and assert no values. Part Five is the exception: it writes an action, derives what follows from it, and lands on one dial and an experimental bound. Everything else would be recognized ingredient by ingredient by a specialist in any of Section III's programmes, who would be entitled to ask what the mapping buys. Part Six answers that.

---

## What Reading Part Three Back Should Leave

Each of these programmes isolated one part of the affine structure and built on it: Poincaré gauge theory took the coframe and got torsion as a field strength, twistors took chirality as a primitive, non-commutative geometry took the Dirac operator, and the discrete programmes took the hinge, the arrow and the order. None of them is a partial version of this series, and this series is not their synthesis. What it carries that they do not is a cost column — and a cost column is a bookkeeping device, not a discovery.

The Trinity shows the choice was a choice: one bulk, three ledgers, differing by what is written on the boundary. Weyl's ruler shows how a dead proposal can leave its word behind, so that a field carries a receipt without reading it. Cartan shows that the inertness of torsion is a property of one action, not of torsion. And the crystal shows that this geometry is not exotic; it is what real materials do.

What the neighbours do not have is the cost column. That is where the next part goes: to the places where the corpus's class, inflated into this host, binds against the host's rules, and what the host bought by having them.

---

### References

* Beltrán Jiménez, J., Heisenberg, L., & Koivisto, T. S. (2019). *The Geometrical Trinity of Gravity*. Universe, 5(7), 173.
* Aldrovandi, R., & Pereira, J. G. (2013). *Teleparallel Gravity: An Introduction*. Springer.
* Nester, J. M., & Yo, H. J. (1999). *Symmetric teleparallel general relativity*. Chinese J. Phys., 37(2), 113–117.
* Weyl, H. (1918). *Gravitation und Elektrizität*. Sitzungsber. Preuss. Akad. Wiss., 465–480.
* London, F. (1927). *Quantenmechanische Deutung der Theorie von Weyl*. Z. Phys., 42, 375–389.
* Weyl, H. (1929). *Elektron und Gravitation I*. Z. Phys., 56, 330–352.
* Cartan, É. (1922). *Sur une généralisation de la notion de courbure de Riemann et les espaces à torsion*. C. R. Acad. Sci., 174, 593–595.
* Kröner, E. (1958). *Kontinuumstheorie der Versetzungen und Eigenspannungen*. Springer.
* Bilby, B. A., Bullough, R., & Smith, E. (1955). *Continuous distributions of dislocations*. Proc. R. Soc. Lond. A, 231, 263–273.
* Kleinert, H. (1989). *Gauge Fields in Condensed Matter, Vol. II*. World Scientific.
* Kibble, T. W. B. (1961). *Lorentz invariance and the gravitational field*. J. Math. Phys., 2(2), 212–221.
* Sciama, D. W. (1962). *On the analogy between charge and spin in general relativity*. In *Recent Developments in General Relativity*, Pergamon.
* Hehl, F. W., von der Heyde, P., Kerlick, G. D., & Nester, J. M. (1976). Rev. Mod. Phys., 48(3), 393–416.
* Penrose, R. (1967). *Twistor algebra*. J. Math. Phys., 8(2), 345–366.
* Connes, A. (1994). *Noncommutative Geometry*. Academic Press.
* Chamseddine, A. H., & Connes, A. (1997). *The spectral action principle*. Comm. Math. Phys., 186(3), 731–750.
* Regge, T. (1961). *General relativity without coordinates*. Il Nuovo Cimento, 19(3), 558–571.
* Bombelli, L., Lee, J., Meyer, D., & Sorkin, R. D. (1987). *Space-time as a causal set*. Phys. Rev. Lett., 59(5), 521–524.
* Trautman, A. (1973). *Spin and torsion may avert gravitational singularities*. Nature Phys. Sci., 242, 7–8.
* Popławski, N. J. (2010). *Cosmology with torsion*. Phys. Lett. B, 694(3), 181–185.
* Teitelboim, C. (1973). *How commutators of constraints reflect the spacetime structure*. Ann. Phys., 79(2), 542–557.
* Nieh, H. T., & Yan, M. L. (1982). *An identity in Riemann–Cartan geometry*. J. Math. Phys., 23(3), 373–374.
* Jacobson, T. (1995). *Thermodynamics of spacetime: The Einstein equation of state*. Phys. Rev. Lett., 75(7), 1260–1263.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.

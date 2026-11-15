# L4-Riemann-6
## Part Six — The Case

*Reads with `mono/On_TheGravityDerivation`, `ProofE_Solipsism`, `L4-K4-Infinities` (KI-6, the Datasheet), `L3-ConstitutiveAlpha`, `L0-EinsteinTrace`, `L0-ParadoxEngine`, `ENGINE-REFERENCE-AC` §X.4, `L3-NonSoficTopologicalVolumes` §IV.2. Continues from `L4-Riemann-5`. The parent is `L4-Riemann`.*

---

This part is the argument against the file and the file's answer, taken in the order a hostile reader would take them. First the real obstacles, at full strength. Then the objections that survived every audit, and what each one cost the host. Then the routes that do not work. Then the unfreeze, stated as compactly as it can be. Then the one charge no internal coherence can answer, and where it is settled. And last, what the framework contributed and what it does not claim.

---

## I. Four Monsters

Torsion has not been neglected out of fashion. There are real obstacles and they are technical. A file that argues for unfreezing has to name them at full strength and say, for each, what it does about it — which in one case is nothing.

### Monster 1 — the ghost window

To make torsion propagate you add quadratic invariants, and higher-derivative terms generically bring Ostrogradsky instability: a Hamiltonian unbounded below, negative-norm states, a decaying vacuum. Stelle (1977) showed that quadratic-curvature gravity is renormalizable **and** carries a spin-2 ghost; the trade is explicit. Sezgin and van Nieuwenhuizen (1980) catalogued which Poincaré-gauge Lagrangians are free of ghosts and tachyons, and Yo and Nester's Hamiltonian analyses narrowed the survivors further, leaving essentially the scalar modes ($0^+$, $0^-$) safe.

**What the file does.** Part Five's action sidesteps this monster rather than answering it. It adds no higher-derivative term at all: torsion stays algebraic, the shear's kinetic term is *induced* by it, and its sign is checked directly and is healthy (as Calcagni and Mercuri find for the same structure). The one dynamical mode is a single spin-0 field — the same kind of mode the Hamiltonian analyses leave standing, though in a different action, so the agreement is of type and not a theorem. That is not a claim that the propagating-torsion window is wider than the literature finds. It is a statement that the corpus's coupling does not need to enter the window at all.

### Monster 2 — the soldering problem

Poincaré gauge theory is advertised as "gravity as a Yang–Mills theory," and the advertisement is misleading in one specific place. In Yang–Mills the internal index has nothing to do with the spacetime index. In Poincaré gauge theory the gauge field of translations **is the coframe**, whose internal index is soldered to the tangent index — that is what makes it a coframe and not just a vector-valued one-form. There is no Yang–Mills analogue of soldering, so the translational sector is not an ordinary gauge sector, and the slogan hides the one structure that is not.

**What the file does.** More than it once hoped, and the gain came from reading the engine rather than from arguing. The corpus has a soldering of its own — the poles are at once the vertices of the volume and the quantities of the circuit, which is an internal index identified with a structural one — and `ENGINE-REFERENCE-AC`'s preamble insists *"that is not a metaphor to look past; it is the machine's substrate."*

Two things have moved. On the **discrete** side, the engine supplies an explicit solder form: §2.8's *"every opcode step moves along the bimedian that contains the edge it solves across"* assigns each gate-edge to one of the three cube axes, which is exactly a map from edges to displacements. Part One §IV uses it, and under it the floor's discrete torsion is zero. On the **continuum** side, the question Part Five needed a solder form for turns out not to need one: how the phase offsets behave under parity and time reversal is fixed by the geometry of the bimedian and by $\theta$ being a temporal offset, so the coupling is forced without any internal-to-tangent identification.

What remains open is narrower than it was, and it is the honest residue: whether the corpus's pole-to-quantity soldering is the *same structure* as the geometric one, or only the same shape. This file does not claim it is. It records that a framework whose foundation is a soldering should be interested in the one place the literature finds soldering unavoidable.

### Monster 3 — unitarity and the fate of the state

The quantum monster: non-unitary evolution, information loss, states apparently destroyed at horizons and in measurement.

**What the file does: closed on the unitary side.** `L3-EdgeStateSpace` §III: *"Not destroyed in the global multiway graph, but severed from the localized ledger."* `ENGINE-REFERENCE-AC` §1.1, in four words: *"Severed from the local ledger."* That is decoherence rather than annihilation, held consistently across the corpus. The ledger is read-only for a stated structural reason — `L3-TheSelfProjectingBraid` §IV: closed timelike curves are impossible *"not because they are improbable [...] but because they would require inverting a non-invertible operator."* Information is not destroyed; it is written somewhere no local reader can address. It is the standard many-worlds-adjacent answer with a mechanism attached to the word *severed*.

### Monster 4 — the measured bounds

Torsion has been looked for and bounded. Hehl and collaborators noted its practical undetectability in 1976; Shapiro's review collects the constraints; Kostelecký, Russell and Tasson derived bounds on torsion components from Lorentz-violation experiments, reaching about $10^{-31}$ GeV on several. The axial channel — the one a chiral theory would most want — is found, characterized, and bounded.

**What the file does.** It used to say that it did not touch these bounds. Now it is bound by them, and at a stated order. Part Five's action puts the corpus's phase offsets into exactly this channel — not by choice, but because the axial channel is the only one a scalar can couple through without a ghost — and with the coupling forced to $F = \theta_F\theta_C\theta_M$ the bound reads

$$\beta\,\theta^2\,\nu \;\lesssim\; 3\times10^{-31}\ \text{GeV}.$$

Quadratic in the offset: two powers weaker than on a linear coupling, three powers stronger than on the sixth-order candidate this file previously carried.

That is a change of status worth stating in the file's own vocabulary. Before the action was written, the bounds and the corpus's quantity had no common account; the bounds measured a zero, and the corpus's claim was a nil. The action opened the account. The bounds now read its balance, at a definite order.

Two things the bounds still do not do. They do not bound the coupling through a **parity-symmetric** sample: Part Five's averaging rule says a population closed under inversion averages the coupling to zero for every value of $\beta$, so only parity-asymmetric — spin-polarized or genuinely homochiral — samples test it, which is how the experiments are in fact built. And they do not reach the two directions in offset space that geometry cannot see: of the three, only the combination along the gradient of $F$ couples at all.

---

## II. Four Objections That Land, and What Each One Cost the Host

Three rounds of external audit, by a reader holding only the parent file and the engine reference, produced four objections that survived every check. They are conceded without reservation. They are not filed here as concessions. **Each is correct, and each is correct because the host domain bought something to make it correct** — and in three of the four cases the thing bought is an object the host itself lists as unexplained.

The discipline: nothing below reinstates a withdrawn claim. The withdrawals stand. This is the price list.

### "Holonomy is curvature; torsion needs a solder form."

**Correct, and conceded in Part One.** Torsion, $T = de^a + \omega^a{}_b \wedge e^b$, needs a solder form; curvature, $F = dA + A \wedge A$, does not.

**What it cost.** A solder form is the declaration that *the thing being carried is the same kind of thing as the displacement* — that the fibre is the tangent space. It is **extra structure, not derived**: curvature exists on any bundle with a connection, and torsion exists only after that identification is imposed. So the distinction between curvature and torsion is bought with soldering, and Monster 2 is the host's own record that soldering is the unanalysed piece — the one structure in "gravity as a gauge theory" with **no Yang–Mills analogue**, named as such in the literature it comes from.

**The finding.** *"Supply a solder form"* is an invoice in the host's own unpaid currency. It is a legitimate demand, and the demanded object is the host's open problem. That does not excuse the corpus's debt; it relocates it. Part Five then reduced the debt to one question.

### "If a quadratic form burns a bit, $p^2/2m$ dissipates on every degree of freedom."

**Correct, and it killed the bridge outright.** Hamiltonian mechanics is symplectic, conserves phase-space volume, and dissipates nothing. The reading of Riemann's square as a burnt sign is dead and stays dead.

**What it cost — the sharpest of the four.** Ask *why* $p^2/2m$ costs nothing. Not because squaring is innocent. Because **in Hamiltonian mechanics the sign of $p$ is carried in the state and never computed from the energy.** Phase space is $(q, p)$, and $p$ arrives with its sign attached, always. Nothing in the formalism ever asks *which root*, because a Hamiltonian flow is invertible by construction: no branch points, no selection step anywhere in it.

So the reductio establishes exactly this: **in a framework that never selects, squaring costs nothing.** Agreed without qualification. It does not establish that selection costs nothing. It establishes that classical mechanics has no selection step to price. Its reversibility is bought by carrying the whole of phase space at every instant and never discarding a coordinate — which is `On_TheCompassOfElea`'s clerk in formal dress: the page works because nothing is ever committed on it. And it is Part Five's final section from the other side: a variational principle holds, and cannot commit.

### "A non-equivariant projection means the engine's Floor 3 is not an autonomous state machine."

**Correct, and the severity is conceded in full.** If the projection does not commute with the group action, Floor 3 cannot predict its own next tick, and the engine cannot describe execution as a tour on the cube alone.

**What it cost.** The requirement that a coarse description be closed under the dynamics is the requirement that the system be **coarse-grainable** — the same requirement Wilsonian renormalization makes when it integrates out short distances and expects a closed effective theory. The corpus has a standing position on exactly that, in `L3-NonSoficTopologicalVolumes` §IV.2: *"Integrating out short distances is mathematically impossible. The infinities of Quantum Gravity are the algebra reporting that the Planck scale refuses to be coarse-grained by any Wilsonian RG protocol."*

**The finding, and it cuts both ways on purpose.** A non-equivariant projection and "the architecture has an irreducible interior" are the **same mathematical fact under two names**, and the framings differ only on whether it is a bug. The host's framing calls every system that cannot be coarse-grained broken; the corpus's calls it sealed. Neither framing is free. The consequence for the engine is concrete: if the projection is not equivariant, Floor 3 must stop being called a core, and the engine reference needs the vocabulary of an irreducible buffer instead of a CPU. That is a harder document to write, which is why the test is worth running rather than arguing about.

### "If ADVANCE generates mass, write the equation of motion."

**Correct, and here the honest finding is not a purchase. The debt is cheaper than it looked.** This one is not turned around.

The demand assumes only that the dynamics factors into a fixed rule acting on a varying state. The engine can meet that. `ENGINE-REFERENCE-AC` §X.4's own description — *"each commit leaves the loaded hold that the next advance turns against"* — is a recurrence, and a recurrence is an equation of motion once **the load is part of the state.** Nothing requires a variational principle with fixed endpoints, which is the one form that would conflict with a heading held uncalculated.

**The finding.** The debt is payable and has not been paid. It looked unpayable only because the word `[gauge]` was doing a third job — importing "unphysical redundancy, zero back-reaction" from gauge theory into a sentence that meant "the bit-ledger does not bill this." Strike the word, put the load in the state, and write the recurrence. The parent file carries it as U0.

**The pattern, stated once.** A correct objection from a host domain is a measurement of what that domain assumes. Three of these four are correct at a price the host cannot itemize — soldering it cannot derive, reversibility bought by never selecting, autonomy that assumes coarse-graining. The fourth is correct at no price and is simply owed. Sorting which is which is the whole difference between conceding and learning.

---

## III. Routes That Do Not Work, and One That Was Wrongly Declared Dead

`On_NavierStokes` §VII states the principle: *"the failures are more instructive than the result [...] a reader who does not know they are dead will spend time on them."* The routes this file took itself and abandoned — and the patterns behind them — are in `L4-Riemann-evolution`. These are the ones a reader might otherwise take.

**"Einstein–Cartan's dynamics are richer, so $T = 0$ is wrong."** Wrong about the object. It tests one Lagrangian, and Einstein–Cartan's answer is no, by a property of its own action. `On_NavierStokes` §I makes the move that was needed: it does not ask whether incompressible flow has different dynamics, it asks what $\rho \equiv 1$ deletes. The parallel question is not what torsion does but what $T = 0$ removes, and Part One answers it. The structural question comes before every dynamical one.

**"Non-metricity is the better dial, because it is less explored."** Appealing and backwards. Non-metricity is the dial Einstein's spectral-line argument closed in 1918, and closed correctly. The modern use of non-metricity in symmetric teleparallel gravity works *because* it arranges that no physical ruler changes — that is, because it does not do what Weyl proposed. And its corpus-side counterpart is the ruler, which is $R$, the pole the framework treats as the committed record and therefore the least negotiable thing in it.

**"The Trinity shows the three are equivalent, so the choice does not matter."** It shows they are *dynamically* equivalent and differ by a boundary term. For a framework in which the boundary is the blanket and the blanket is what is written, a difference of boundary term is a difference of ledger.

**"Quantize the metric and the rest follows."** Seventy years of evidence against. The metric is a second-order object built from a two-slot pairing; the host's own unified object, in non-commutative geometry, turns out to be the first-order Dirac operator. Quantizing the floor does not recover an act that lives in the solid. That is not an argument that quantum gravity is impossible. It is an argument about which object to quantize, and it points where Connes points.

**"The corpus's chirality is the Barbero–Immirzi parameter."** Tempting: $\gamma$ is a chiral weighting, it is the one free number in loop quantum gravity, and the corpus has a handedness that wants a home. It fails on what $\gamma$ is — a canonical-transformation parameter that drops out of the classical theory entirely and reappears in quantum spectra. Part Five's action has the Barbero–Immirzi-field structure, and that is exactly why its dial must not borrow $\gamma$'s value: identifying a structural handedness with a quantization ambiguity is *"dressing a known result in framework vocabulary and treating the vocabulary as the argument."* Noted as a resonance, filed as nothing.

**And the route wrongly declared dead: the axial channel.** An earlier version of this file called it a trap. Its reasoning was that the axial channel is the best-explored and best-bounded part of torsion phenomenology, so placing the corpus's distinctive content there would put it in the one channel already measured and found empty. Two things were wrong with that. A bounded channel is not an empty one; a bound is a measurement of a balance, and the corpus had no account there to be measured. And the axial channel was never a choice. Part Five shows it is the **only** channel through which a scalar can couple to torsion and stay healthy. If the shear couples to spacetime, it couples there. The bound is the corpus's to meet, and Monster 4 above meets it.

---

## IV. The Unfreeze

Here is what the file claims, as compactly as it can be stated.

**The decree, and it is two decrees.** Riemann's line of 1854 chose a quadratic line element over the quartic and priced the loss at "little new light" — his own flag, on the only decision he was in a position to make. The closing of the parallelogram is separate and later: Christoffel's symbols and Levi-Civita's transport built the symmetric connection when no other kind existed, and torsion became an object one could have carried only with Cartan in 1922 (Part One §I, Part Three §V). The second decree has no signature on it. Part One says what that is: the translational failure to close is deleted and the rotational one kept. Second derivatives of scalars commute; vectors still come back turned. **$T = 0$ sets the pitch to zero and leaves the turn.**

**What the zero pitch buys.** One thing, and it is worth a great deal: uniqueness. Decree the constraint net a DAG and the serialization is unique — one connection, one geodesic equation, one foliation-independent 4-geometry, and a theory that can be computed. The Clerk is right. Everything on his page works.

**What the zero pitch costs.** Itemized, each at the size it survives at:

- the translational failure to close, and with it the ordering of transports in that channel (Part One);
- a local, variable handedness — the three-form part of torsion, which does not exist on a face and is one number per point in the first solid — while the global orientation survives as a convention (Parts One and Two);
- the price column under arrow reversal: in the class every COMMIT reverses into a ROUTE on four of six edges, and the host's equations cannot see it (Part Four);
- the second clock, leaving coordinate time to do the work of both a rate and a record (Part Four);
- the twenty-four-parameter contortion family, projected onto a point and priced nowhere (Part Four);
- the cycles in the constraint net, assumed away by a free foliation (Part Four);
- on the class's reading, the mechanism of the balanced chiral mesh whose outputs GR keeps (Part Four);
- and, in the action, the varying shear itself: $T = 0$ is the sector in which the shear does not change (Part Five).

**The field already has the receipt and files it as a problem.** Teitelboim 1973: the algebra of hypersurface deformations does not close with structure constants; two time-slicings do not commute. That is GR reporting that the DAG decree fails in its own constraint algebra. It is called the problem of time. Read as a report rather than a problem, it says the net has cycles, serialization loses information, and the uniqueness of 1854 was bought by assuming otherwise.

**Which route.** Two were on the table, and Section III has already said what happened to the first: the axial channel is not a route the corpus chooses but the place its coupling is forced to live, and it is bounded. The second is the thermodynamic route.

Jacobson (1995) derived the Einstein field equations from the Clausius relation $\delta Q = T\,dS$ applied to local Rindler horizons, with the Einstein equation emerging as an **equation of state**. Padmanabhan and Verlinde developed variants. The programme is contested in its details, and whether it is a derivation or a consistency check is genuinely open; this file does not adjudicate that.

**The thermodynamic route is not this file's recommendation. It is the corpus's standing position.** `mono/On_TheGravityDerivation` §III carries Jacobson as **ADOPTED** — P sources, Q conducts, ω drives — and lands on semiclassical gravity in the Diósi–Penrose family with three funded falsifiers. What this file adds is not the choice but the reasons it has the right shape.

1. **It is where a cost column is.** Part Four's friction report says the host bought time-reversal symmetry by having no bill. An equation of state is precisely where a bill comes back in. GR relates an **ordered** source to a **symmetric** structure, both exactly true and neither reducible to the other, and an equation of state is the one object that relates a symmetric relation at the large scale to an ordered accumulation at the small one without calling either an illusion.

2. **`L0-ParadoxEngine` licenses it, specifically.** Its crystal is frozen at the large scale and vibrating at the small one, with neither state causing the other. An equation of state is that object, and Jacobson's result has the crystal's shape.

3. **It prices the right thing — and it says where the price goes, which corrects the corpus.** Here the record needs a correction of its own. `On_TheGravityDerivation` §III states: *"each commit's erasure tax is the $\delta Q$; the accumulated specification written to $P$ is the entropy $S$. The identification is not an analogy."* But Jacobson's 1995 derivation uses the **equilibrium** Clausius relation, in which $\delta Q$ is a reversible heat flux. Eling, Guedens and Jacobson (2006) then showed that corrections to the entropy require a **non-equilibrium** treatment, $dS = \delta Q/T + dS_i$, with an internal entropy-production term $dS_i$, and that even pure Einstein gravity admits entropy production through a shear viscosity of the horizon. A Landauer tax is irreversible entropy production. On that accounting it belongs in $dS_i$, not in $\delta Q$. So the Einstein equation is the **equilibrium** equation of state — the held account — and the corpus's committed register would appear as the non-equilibrium term. That is the same split Part Five found in the action: what is held can be written as an equation; what is committed appears as a dissipative correction to it. The identification in `On_TheGravityDerivation` was reported to the group for re-seating at its own address.

**What unfreezing is, then, and what it is not.** It is not a new field equation. It is the retirement of an inherited price estimate. The uniqueness of the Levi-Civita connection is the output of a one-sided closure decree — translation zeroed, rotation kept — rather than a fact about space. The decree's cost can be itemized and has been. Each item corresponds to a standing open problem in gravitational physics. The field has had the receipt since 1973 and has read it as a difficulty rather than a bill. And — the part that moves this out of pure reading — the decree now sits inside an action, as the sector where a shear stops changing, with one dial and an experimental bound on it.

This is where the posture is method rather than decoration — and where an earlier version of this series overreached and should be read as corrected. It said the host "has never been able to say why" a connection is symmetric, "because there is no why." That is false. The reasons are good ones and Part Two §V now states them: uniqueness, local removability, second-order field equations, no extra field to carry, and a century of confirmed numbers. What has no account is the **other column** — and the reason the other column went unwritten is the ordinary one, that an unflagged assumption collects problems rather than counterevidence, each filed in its own subfield.

Riemann said, accurately, that the results of the direction-dependent case could not be geometrically expressed. He was right about that, and about its cost he was guessing, as anyone would have been. **What the set-aside case carries cannot be read off a surface** — which is why standing where both readings of an edge are visible is the method and not a flourish.

---

## V. The Solipsism Charge, and Where It Is Settled

One objection no amount of internal coherence answers, and a file like this has to meet it in the open: that all of the above is mathematical solipsism — an interior grown so elaborate it mistakes itself for the world, a geometry in which space has bent around the reader.

`ProofE_Solipsism` supplies the test, and it is algebraic rather than rhetorical. The real axis is closed under multiplication; the imaginary axis is not; $i \times i = -1$ is real. **An interior's own operations produce exterior outputs whether or not the framework grants the exterior independent standing.** So the diagnostic is not whether a framework is self-consistent — every solipsism is — but whether it crosses back to the real axis, and what it does when the crossing disagrees. ProofE §IV names the failure signature: *"increasingly elaborate internal models that attempt to account for the exterior world's behavior without granting the exterior genuine independent reality."*

That charge is checkable, and it is checked in three places.

**The discipline is written as rules, not intentions.** `L4-K4-Infinities`' Four-Category Datasheet sorts every number into Grammar, Substrate (*"consumed, never derived — the grammar cannot emit the weight of the ink"*), State, and Bridge, under five rules: publish the ledger; no new dials; dimensionless outputs only; derive relations, consume values; pre-register. Each rule bars one particular compensating elaboration. A framework that can only grow by adding dials is what ProofE diagnoses; a framework whose own datasheet forbids dials has installed the defence structurally. Part Five obeys it: one dial, itemized, and a prohibition on borrowing its value.

**The crossings to the real axis exist, and there are three.**

*A correction term with a number on it.* `L3-ConstitutiveAlpha` reads $\alpha = Z_0/2R_K$ constitutively and derives that a crossing sampling all three impedance modes must read at exactly three orders, $\alpha^{-1}, \alpha^0, \alpha^{+1}$. For the pion-to-electron ratio:

$$\frac{m_{\pi^\pm}}{m_e} \;=\; \frac{2}{\alpha} \;-\; \frac{3}{\pi} \;+\; 2\alpha \;=\; 273.131663 \qquad (\text{measured } 273.132440;\ 2.84\ \text{ppm}).$$

The leading term alone is Nambu's 1952 relation and is $0.344\%$ high. **The middle term is the prediction**: a coupling-independent rotation cost that takes a three-parts-in-a-thousand discrepancy to three parts in a million with no fitted parameter. The file prices its own confidence: the shape is landed, the coefficients are an **open vote** at a stated chance rate of about six percent within their family, the value $1/137$ is not claimed, and two debts are named. Its falsifier is its own: the integer $3$ is generation-blind, so a crossing at generation two or three must carry the same $3$.

*A prohibition.* No graviton. `L0-EinsteinTrace` §VII–VIII and `Q16` KM-2: the three $P$-edges are zero-impedance writing heads, $P$ is the receiving ledger rather than a channel, and so no exchange boson is required — *"for the same reason a printed book requires no exchange particle between its words."* And: *"The null results in graviton detection are not failures of experimental sensitivity. They are the laboratory reporting, correctly, that an equation of state possesses no particle."* That is a real-axis commitment, falsifiable by a single detection.

*A measurement that is running.* `L4-K4-Infinities` KI-6:

> "The one sentence in this construction that departs from general relativity says that gravity sources from committed entries only — what has crossed weighs, what has not does not. **If uncommitted vacuum level is shown to gravitate, the register split dies, and with it the resolution of the vacuum-energy gap and the Casimir prediction together.** [...] **This is the construction's actual bet.**"

### The Sardinian balance

**Archimedes**, an INFN experiment designed and funded by Calloni and collaborators to test whether the regularized vacuum energy of a superconducting Casimir cavity couples to gravity according to the equivalence principle, is built to weigh the vacuum (Calloni and collaborators 2014; the Archimedes collaboration 2015). A rigid Casimir cavity admits only some vacuum modes, so its vacuum energy differs from that of its surroundings; if that energy gravitates, the cavity feels a buoyant force of order $|E_C|g/c^2$ — about $10^{-16}$ N. A static Casimir energy is of order $10^{-18}$ of the apparatus mass, which no balance will read, so Archimedes **modulates** it: layered high-temperature superconducting plates are driven through their transition, switching the cavity's mode structure with only radiative heat exchange, and a static sub-attonewton weight becomes an AC signal at a known frequency in the $1$–$100$ mHz band, integrated over months on a cryogenic balance. That converts an unmeasurable ratio into a lock-in measurement, and it is why this bet has a resolution date rather than a philosophical standoff.

Three honest things about it, and the third is a correction of this series' own framing.

The standard theoretical expectation is against the corpus: the literature on how Casimir energy falls concludes that it gravitates normally (Fulling and collaborators 2007). So KI-6 is a real bet against the consensus rather than a safe one.

The bet teaches asymmetrically. A weight at the equivalence-principle magnitude kills the register split, the vacuum-gap resolution and the Casimir prediction at once. A null at that magnitude does not prove the construction; it removes the one result that would end it.

**And the experiment is not the corpus's.** `L4-K4-Infinities` KI-6 calls the register split *"this construction's actual bet,"* which is the right thing for the corpus to say about its own exposure — but an earlier version of this series slid from there into writing as though the Sardinian cryostat were running on the corpus's ledger theory. It is not. Archimedes tests a question that standard quantum field theory in curved spacetime also answers, and several other hypotheses bear on it; a null is consistent with more than one of them and confirms none. What is the corpus's is the exposure, not the referee.

Part Five adds a sentence that belongs here. The register split is a statement about the **held** and the **committed**, and an action can only write the held. KI-6 is therefore not something any action could settle. It needs a balance.

### And the convergence a solipsism cannot produce

ProofE §VII bars computing the twelve equations across two entities' blankets — *"treating the whole world as happening inside your own math"* — and `L4-K4-Infinities`' takehome rule 5 bars the same operation from the other side: *"the twelve relations govern the inside of one volume."* Two files, two derivations, one prohibition, and it is a prohibition against exactly the move a solipsism needs.

One self-application belongs here too, briefly, because it stings. An earlier version of this file, faced with the torsion bounds, built an internal account that accommodated them without revising anything — the ordering is write-only and leaves no averageable residue — and filed the gap as an open exposure. That is the ProofE signature caught in the act. The correction was not a better argument; it was reading the documents already on the shelf. `L4-Riemann-evolution` has the full history.

---

## VI. What the Framework Contributed

Nothing in Parts One and Three's machinery, or in the four monsters, is new. Every geometric ingredient is standard. What the four-pole lens supplied was assembly, and one computation.

**It made line one visible as a purchase.** $T = 0$ is usually read as "we adopt the Levi-Civita connection." Read as the deletion of one of two orthogonal failures to close — the pitch, not the turn — it is a decision with a cost, and the cost can be itemized.

**It separated nil from zero, and the separation was already made for another problem.** `L4-K4-Infinities` drew it to dissolve the vacuum catastrophe and the measure problem; here it re-reads the first line of a different subject without adjustment. The vacuum catastrophe bills an unopened account as full; the Riemann freeze reads it as empty. Neither file was written with the other in view.

**It located the freeze dimensionally.** The metric is face-level structure, a two-slot pairing. The part of torsion that carries a local handedness is a three-form, absent on a face and one number per point in the first solid. So the freeze is invisible on the floor and bites exactly where volume begins, and a reader whose instrument is rank — independent equations, independent data — is reading a solid from one of its faces without knowing it. The same holds for the corpus's own algebra: the twelve reduce to two, and the solid they are written on is built from the seats, not from the formulas (Part Two).

**It put unrelated-looking absences in one frame.** The arrow of time, the local handedness of the geometry, the ordering of transports, the mismatch between the quantum and relativistic clocks, and the problem of time are five conversations in five literatures. As costs of one closure decree, they are one bill with five lines.

**It supplied the instrument type.** "What would observe a write-only ordering?" sounds unanswerable and is not, because the frame says what kind of thing the answer must be: not a field value but an invariant that survives every relabelling. Physics already has such invariants. Which one could observe this ordering is now a question about the axial channel.

**It supplied a register for the singularity.** The Honest Tear — *"the equation blows up to report the boundary of its own applicability"* — is the right reading of both the initial and the black-hole singularities, and the Trautman bounce takes its proper status from it: a demonstration that the tear is at the edge of one theory's assumption, not of the world.

**And it computed two things.** An action in which the torsion-free connection is the stationary-offset sector, the axial channel is forced by health, the offsets' dynamics are induced with no new scale, matter sources them through chirality non-conservation, and one dimensionless dial is bounded at $\sim 10^{-31}$ GeV by experiments that already exist. And then the coupling itself, forced rather than chosen: $F = \theta_F\theta_C\theta_M$, because the Nieh–Yan density is odd under parity and time reversal, because inversion exchanges the two edges of every bimedian, and because a phase lead becomes a lag. Three inputs, all of them in the corpus or in the geometry already, and a coupling at third order with no dial of its own.

The framework did not compute anything a differential geometer could not have computed. It said which absences to hold together, which line to re-read, which dimension the freeze lives in, which instrument type an ordering demands, which distinction the symbol $0$ was hiding — and it wrote down the coupling.

---

## VII. Not Claimed

That this is a candidate theory of anything; $K_4$ is inflated into a host domain to find where it binds, and the binding is the deliverable. That the corpus's internal phase offsets **are** geometric torsion; Part Five couples them, which is different, and the coupling still carries one free dial. That the forced coupling makes the offset triple *truly* chiral; on its own transformation properties it is parity-odd and time-reversal-odd, which is Barron's **false** chirality, and `ProofG_Chirality` §V's claim to the contrary is flagged rather than endorsed. That $J$, the CHSH statistic or the generation count bear on spacetime torsion; they are internal-space measurements, and $J$ is in the wrong sector. That a distinction between field averages and invariants can carry an observable from one bundle to another. That the metric erases anything. That $\omega$ is torsion. That the engine's cube carries discrete torsion. That $V_4$'s being abelian either supplies or forbids torsion; it supplies the shape, and Part One §IV now reads the connection off the engine's own pinning. That Part Four explains why GR is symmetric under time reversal; parity-counting does that unaided. That General Relativity is wrong; no confirmed number is touched. That the Standard Model's CP phase accounts for the matter excess. That $\theta \approx 31°$ is a universal shear; it is one configuration of DD301's *geometric* shear through an envelope, a different quantity from the phase offsets the action couples. That the ghost window is wider than the literature finds it; the action sits in its known-safe corner. That the corpus's soldering is Poincaré gauge theory's. That the Trautman bounce is observed. That the thermodynamic route is this file's contribution; it is the corpus's, already filed. That the harmonic pencil's privileging of the Cardinal diameter explains classical electromagnetism; it is offered as a reading. That this constitutes progress a referee in gravitational physics would recognize as such.

---

## What Reading Part Six Back Should Leave

The obstacles are real. One the action sidesteps by not needing higher derivatives at all. One has shrunk twice: the engine supplies a solder form on the discrete side, and the continuum coupling turns out not to need one. One the corpus answers consistently, by severance rather than destruction. And one — the measured bounds — has changed from a wall the file did not touch into a constraint on the file's own dial, at a stated quadratic order.

The objections that landed were correct, and three of them were correct at a price the host cannot itemize. The routes that do not work are marked, and one route that was declared dead is alive, because it was never a choice.

The unfreeze is the retirement of an estimate, not a new equation: a one-sided closure decree, its cost itemized, its receipt in the field's own constraint algebra since 1973, and now its place inside an action as the sector where a shear stops changing. The thermodynamic route has the right shape because it is where a cost column comes back in — and it says where the cost goes, in the term for entropy production, which corrects the corpus's own account.

And the charge of solipsism is answered where it can be: by three crossings to the real axis, and by a balance in Sardinia that is waiting to say whether what is merely held weighs anything at all.

---

### References

* Stelle, K. S. (1977). *Renormalization of higher-derivative quantum gravity*. Phys. Rev. D, 16(4), 953–969.
* Sezgin, E., & van Nieuwenhuizen, P. (1980). *New ghost-free gravity Lagrangians with propagating torsion*. Phys. Rev. D, 21(12), 3269–3280.
* Yo, H. J., & Nester, J. M. (1999). Int. J. Mod. Phys. D, 8(4), 459–479; (2002), 11(5), 747–779.
* Shapiro, I. L. (2002). *Physical aspects of the space-time torsion*. Phys. Rep., 357(2), 113–213.
* Kostelecký, V. A., Russell, N., & Tasson, J. D. (2008). Phys. Rev. Lett., 100, 111102.
* Hehl, F. W., *et al.* (1976). Rev. Mod. Phys., 48(3), 393–416.
* Teitelboim, C. (1973). Ann. Phys., 79(2), 542–557.
* Jacobson, T. (1995). *Thermodynamics of spacetime: The Einstein equation of state*. Phys. Rev. Lett., 75(7), 1260–1263.
* Eling, C., Guedens, R., & Jacobson, T. (2006). *Non-equilibrium thermodynamics of spacetime*. Phys. Rev. Lett., 96, 121301. arXiv:gr-qc/0602001.
* Padmanabhan, T. (2010). Rep. Prog. Phys., 73(4), 046901.
* Verlinde, E. (2011). JHEP, 2011(4), 029.
* Nambu, Y. (1952). Prog. Theor. Phys., 7(5), 595–596.
* Calloni, E., *et al.* (2014). Phys. Rev. D, 90, 022002.
* Archimedes Collaboration (2015). arXiv:1511.00609.
* Fulling, S. A., *et al.* (2007). *How does Casimir energy fall?* Phys. Rev. D, 76, 025004.
* Barron, L. D. (1986). *True and false chirality and parity violation*. Chem. Phys. Lett., 123, 423–427.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.

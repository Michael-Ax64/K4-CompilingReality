# L4-Riemann-6
## Part Six — The Case

*Reads with `On_TheGravityDerivation`, `ProofE_Solipsism`, `L4-K4-Infinities` (KI-6, the Datasheet), `L3-ConstitutiveAlpha`, `L0-EinsteinTrace`, `L0-ParadoxEngine`, `ENGINE-REFERENCE-AC` §X.4, `L3-NonSoficTopologicalVolumes` §IV.2. Continues from `L4-Riemann-5`. The parent is `L4-Riemann`.*

---

Torsion was not set aside because it was ugly. It was set aside because the obstacles to carrying it are real and technical, and a case for unfreezing has to meet them at full strength before it earns a hearing. There are four:

- **The ghost window.** Making torsion propagate usually means higher-derivative terms, and higher derivatives generically bring instability — a Hamiltonian with no floor.
- **The soldering problem.** Torsion, unlike curvature, exists only once the frame is identified with the displacement it carries, and that identification is extra structure the geometry does not hand you.
- **The fate of a lost state.** The quantum objection: information that looks destroyed at a horizon or in a measurement.
- **The measured bounds.** Torsion has been looked for and constrained, and the axial channel — the one a chiral theory most wants — is bound tightest of all.

The action meets each in a different way. It walks around the ghost window by adding no higher-derivative term at all. It shrinks the soldering problem the moment the engine's own solder form is read for what it is. It answers the lost state the way the corpus answers every such question — severed from the local ledger, not destroyed. And the bounds stop being a wall the moment the action gives them something of its own to weigh: one dial, at a stated order.

If you have read little of the construction at the root of CompilingReality, four conclusions here look classically unassailable: that propagating torsion must be unstable, that no frame can be soldered to a discrete engine, that a projection this lossy cannot run a state machine, and that the bounds have already weighed the channel and found it empty. Follow the argument and you may come out holding the opposite — each conclusion is correct, and each is correct because the host had to buy something to make it so: a soldering it cannot derive, a reversibility bought by never selecting, an autonomy that assumes the world coarse-grains. None of them closes the case. It is left to a balance at Sos Enattos, weighing whether a bounded vacuum falls — and that measurement, not any argument on the page, is the thing only one side can survive.

---

## I. Four Real Obstacles

### The ghost window

To make torsion propagate you add quadratic invariants, and higher-derivative terms generically bring Ostrogradsky instability: a Hamiltonian unbounded below, negative-norm states, a decaying vacuum. Stelle (1977) showed that quadratic-curvature gravity is renormalizable **and** carries a spin-2 ghost; the trade is explicit. Sezgin and van Nieuwenhuizen (1980) catalogued which Poincaré-gauge Lagrangians are free of ghosts and tachyons, and Yo and Nester's Hamiltonian analyses narrowed the survivors to essentially the scalar modes ($0^+$, $0^-$).

The action sidesteps this rather than answering it. It adds no higher-derivative term: torsion stays algebraic, the shear's kinetic term is *induced* by it, and its sign is checked directly and is healthy (as Calcagni and Mercuri find for the same structure). The one dynamical mode is a single spin-0 field — the same kind the Hamiltonian analyses leave standing, though in a different action, so what agrees is the type of mode and not a theorem. The corpus's coupling does not need to enter the propagating-torsion window at all.

### The soldering problem

Poincaré gauge theory is advertised as "gravity as a Yang–Mills theory," and the advertisement is misleading in one specific place. In Yang–Mills the internal index has nothing to do with the spacetime index. In Poincaré gauge theory the gauge field of translations **is the coframe**, whose internal index is soldered to the tangent index — that is what makes it a coframe and not just a vector-valued one-form. There is no Yang–Mills analogue of soldering, so the translational sector is not an ordinary gauge sector, and the slogan hides the one structure that is not.

The corpus has a soldering of its own — the poles are at once the vertices of the volume and the quantities of the circuit, an internal index identified with a structural one — and `ENGINE-REFERENCE-AC`'s preamble insists *"that is not a metaphor to look past; it is the machine's substrate."* On the **discrete** side the engine supplies an explicit solder form: §2.8's *"every opcode step moves along the bimedian that contains the edge it solves across"* assigns each gate-edge to one of the three cube axes, a map from edges to displacements, under which the floor's discrete torsion is zero (Part One §IV). On the **continuum** side the question Part Five needed a solder form for turns out not to need one: how the phase offsets behave under parity and time reversal is fixed by the geometry of the bimedian and by $\theta$ being a temporal offset, so the coupling is forced without any internal-to-tangent identification. What remains open is narrower: whether the corpus's pole-to-quantity soldering is the *same structure* as the geometric one, or only the same shape. A framework whose foundation is a soldering should be interested in the one place the literature finds soldering unavoidable.

### The fate of a lost state

The quantum obstacle: non-unitary evolution, information loss, states apparently destroyed at horizons and in measurement. The corpus closes this on the unitary side. `L3-EdgeStateSpace` §III: *"Not destroyed in the global multiway graph, but severed from the localized ledger."* `ENGINE-REFERENCE-AC` §1.1, in four words: *"Severed from the local ledger."* That is decoherence rather than annihilation, held consistently across the corpus. The ledger is read-only for a stated structural reason — `L3-TheSelfProjectingBraid` §IV: closed timelike curves are impossible *"not because they are improbable, but because they would require inverting a non-invertible operator."* Information is not destroyed; it is written somewhere no local reader can address — the standard many-worlds-adjacent answer with a mechanism attached to the word *severed*.

### The measured bounds

Torsion has been looked for and bounded. Hehl and collaborators noted its practical undetectability in 1976; Shapiro's review collects the constraints; Kostelecký, Russell and Tasson derived bounds on torsion components from Lorentz-violation experiments, reaching about $10^{-31}$ GeV on several. The axial channel — the one a chiral theory would most want — is found, characterized, and bounded.

Part Five's action puts the corpus's phase offsets into exactly this channel — not by choice, but because the axial channel is the only one a scalar can couple through without a ghost — and with the coupling forced to $F = \theta_F\theta_C\theta_M$ the bound reads

$$\beta\,\theta^2\,\nu \;\lesssim\; 3\times10^{-31}\ \text{GeV},$$

quadratic in the offset: two powers weaker than on a linear coupling, three powers stronger than on a sixth-order candidate. Before the action, the bounds and the corpus's quantity had no common account; the bounds measured a zero, and the corpus's claim was a nil. The action opened the account, and the bounds now read its balance, at a definite order.

Two things the bounds still do not do. They do not bound uniform $\langle F\rangle$ through a **parity-symmetric** sample: a population closed under inversion averages $F$ to zero for every $\beta$, while static spin-polarized experiments ($\hat P$-even, $\hat T$-odd) probe the $\hat T$-odd axial gradient $\nabla F$ rather than breaking spatial inversion on uniform $F$. And they do not reach the two directions in offset space that geometry cannot see: of the three, only the combination along the gradient of $F$ couples at all.

---

## II. The Four Objections, Read as Measurements of the Host

Three rounds of external audit, by a reader holding only the parent file and the engine, produced four objections that survived every check. Each is correct. And each is correct because the host domain bought something to make it correct — and in three of the four, the thing bought is an object the host itself lists as unexplained. **A correct objection from a host domain is a measurement of what that domain assumes.** Here is what each one measures.

### Holonomy is curvature; torsion needs a solder form

Correct: torsion, $T = de^a + \omega^a{}_b \wedge e^b$, needs a solder form; curvature, $F = dA + A \wedge A$, does not. A solder form is the declaration that *the thing being carried is the same kind of thing as the displacement* — that the fibre is the tangent space. It is **extra structure, not derived**: curvature exists on any bundle with a connection, and torsion exists only after that identification is imposed. So the distinction between curvature and torsion is bought with soldering, and the soldering problem above is the host's own record that soldering is the unanalysed piece — the one structure in "gravity as a gauge theory" with **no Yang–Mills analogue**. *"Supply a solder form"* is an invoice in the host's own unpaid currency: a legitimate demand, and the demanded object is the host's open problem. Part Five reduced the corpus's side of the debt to one question.

### If a quadratic form burns a bit, $p^2/2m$ dissipates on every degree of freedom

Correct, and it is the sharpest of the four. Hamiltonian mechanics is symplectic, conserves phase-space volume, and dissipates nothing. Ask *why* $p^2/2m$ costs nothing. Not because squaring is innocent — because **in Hamiltonian mechanics the sign of $p$ is carried in the state and never computed from the energy.** Phase space is $(q, p)$, and $p$ arrives with its sign attached, always. Nothing in the formalism ever asks *which root*, because a Hamiltonian flow is invertible by construction: no branch points, no selection step anywhere in it. So the measurement is exactly this: **in a framework that never selects, squaring costs nothing.** It does not establish that selection costs nothing. Its reversibility is bought by carrying the whole of phase space at every instant and never discarding a coordinate — which is `On_TheCompassOfElea`'s clerk in formal dress, the page that works because nothing is ever committed on it, and it is Part Five's final section from the other side: a variational principle holds, and cannot commit.

### A non-equivariant projection means the engine's Floor 3 is not an autonomous state machine

Correct. If the projection does not commute with the group action, Floor 3 cannot predict its own next tick, and the engine cannot describe execution as a tour on the cube alone. The requirement that a coarse description be closed under the dynamics is the requirement that the system be **coarse-grainable** — the same requirement Wilsonian renormalization makes. The corpus has a standing position on exactly that, in `L3-NonSoficTopologicalVolumes` §IV.2: *"Integrating out short distances is mathematically impossible. The infinities of Quantum Gravity are the algebra reporting that the Planck scale refuses to be coarse-grained by any Wilsonian RG protocol."* So a non-equivariant projection and "the architecture has an irreducible interior" are the **same mathematical fact under two names**, and the framings differ only on whether it is a bug. The host's framing calls every system that cannot be coarse-grained broken; the corpus's calls it sealed. The consequence is concrete: if the projection is not equivariant, Floor 3 must stop being called a core, and the engine reference needs the vocabulary of an irreducible buffer instead of a CPU — a harder document to write, which is why the test is worth running rather than arguing about.

### If ADVANCE generates mass, write the equation of motion

Correct, and here the measurement is not a purchase — the debt is cheaper than it looked. The demand assumes only that the dynamics factors into a fixed rule acting on a varying state, and the engine can meet that. `ENGINE-REFERENCE-AC` §X.4's own description — *"each commit leaves the loaded hold that the next advance turns against"* — is a recurrence, and a recurrence is an equation of motion once **the load is part of the state.** Nothing requires a variational principle with fixed endpoints, which is the one form that would conflict with a heading held uncalculated. The recurrence is written at `ENGINE-REFERENCE-AC` §X item 4 — state $(g_n, L_n)$, commit updating the load, advance taking it — with the load-extremizing dispatch rule above `[gauge]` a CANDIDATE dynamics choice.

The finding has two levels. "The engine is an abstract base class" is true and is the face of the machine: the closure of the option space makes the class instantiable anywhere and answerable to none of its instances, and on that face a recurrence reads as generic. What the closure proved is one level in. The rule-set of the recurrence is not chosen: the twelve opcodes carry three slopes, and no relabeling of the poles survives the seating ($|\mathrm{Aut}| = 1$, `ARCHITECTURE` §I). And the recurrence is not generic: it is the torque-motor loop — the machine's own commits loading the hold its own advance turns against — with the standing stock the loop must carry priced on the engine's own books: *"mass is the price of being"* (§X.4). Both levels hold: the face says a recurrence is an equation of motion; the volume says the rule-set was forced, the loop self-feeds, and the turning has a price.

**The pattern, stated once.** Three of these four are correct at a price the host cannot itemize — soldering it cannot derive, reversibility bought by never selecting, autonomy that assumes coarse-graining. The fourth is correct at no price and is simply owed. Sorting which is which is the whole difference between conceding and learning.

---

## III. Routes That Do Not Work, and One That Was Wrongly Declared Dead

`On_NavierStokes` §VII states the principle: *"the failures are more instructive than the result; a reader who does not know they are dead will spend time on them."* These are the routes a reader might otherwise take.

**"Einstein–Cartan's dynamics are richer, so $T = 0$ is wrong."** Wrong about the object. It tests one Lagrangian, and Einstein–Cartan's answer is no, by a property of its own action. `On_NavierStokes` §I makes the move that is needed: it does not ask whether incompressible flow has different dynamics, it asks what $\rho \equiv 1$ deletes. The parallel question is not what torsion does but what $T = 0$ removes, and Part One answers it. The structural question comes before every dynamical one.

**"Non-metricity is the better dial, because it is less explored."** Backwards. Non-metricity is the dial Einstein's spectral-line argument closed in 1918, and closed correctly. The modern use of non-metricity in symmetric teleparallel gravity works *because* it arranges that no physical ruler changes — that is, because it does not do what Weyl proposed. And its corpus-side counterpart is the ruler, which is $R$, the pole the framework treats as the committed record and therefore the least negotiable thing in it.

**"The Trinity shows the three are equivalent, so the choice does not matter."** It shows they are *dynamically* equivalent and differ by a boundary term. For a framework in which the boundary is the blanket and the blanket is what is written, a difference of boundary term is a difference of ledger.

**"Quantize the metric and the rest follows."** Seventy years of evidence against. The metric is a second-order object built from a two-slot pairing; the host's own unified object, in non-commutative geometry, turns out to be the first-order Dirac operator. Quantizing the floor does not recover an act that lives in the solid. That points where Connes points.

**"The corpus's chirality is the Barbero–Immirzi parameter."** Tempting: $\gamma$ is a chiral weighting, it is the one free number in loop quantum gravity, and the corpus has a handedness that wants a home. It fails on what $\gamma$ is — a canonical-transformation parameter that drops out of the classical theory entirely and reappears in quantum spectra. Part Five's action has the Barbero–Immirzi-field structure, which is exactly why its dial must not borrow $\gamma$'s value: identifying a structural handedness with a quantization ambiguity would be *"dressing a known result in framework vocabulary and treating the vocabulary as the argument."* A resonance, filed as nothing.

**And the route wrongly declared dead: the axial channel.** It is the best-explored and best-bounded part of torsion phenomenology, which is why it looks like a trap — placing the corpus's distinctive content there would put it in the one channel already measured and found empty. Two things make that wrong. A bounded channel is not an empty one; a bound is a measurement of a balance, and the corpus had no account there to be measured. And the axial channel was never a choice: Part Five shows it is the **only** channel through which a scalar can couple to torsion and stay healthy. If the shear couples to spacetime, it couples there. The bound is the corpus's to meet, and Section I meets it.

---

## IV. The Unfreeze

Here is what the file claims, as compactly as it can be stated.

**The decree is two decrees.** Riemann's line of 1854 chose a quadratic line element over the quartic and priced the loss at "little new light" — his own flag, on the only decision he was in a position to make. The closing of the parallelogram is separate and later: Christoffel's symbols and Levi-Civita's transport built the symmetric connection when no other kind existed, and torsion became an object one could carry only with Cartan in 1922 (Part One §I, Part Three §V). The second decree has no signature on it, and Part One says what it is: the translational failure to close is deleted and the rotational one kept. Second derivatives of scalars commute; vectors still come back turned. **$T = 0$ sets the pitch to zero and leaves the turn.**

**What the zero pitch buys.** One thing, and it is worth a great deal: uniqueness. Decree the constraint net a DAG and the serialization is unique — one connection, one geodesic equation, one foliation-independent 4-geometry, a theory that can be computed. Everything on the Clerk's page works.

**What the zero pitch costs**, each at the size it survives at:

- the translational failure to close, and with it the ordering of transports in that channel (Part One);
- a local, variable handedness — the three-form part of torsion, which does not exist on a face and is one number per point in the first solid — while the global orientation survives as a convention (Parts One and Two);
- the price column under arrow reversal: in the arrangement every COMMIT reverses into a ROUTE on four of six edges, and the host's equations cannot see it (Part Four);
- the second clock, leaving coordinate time to do the work of both a rate and a record (Part Four);
- the twenty-four-parameter contortion family, projected onto a point and priced nowhere (Part Four);
- the cycles in the constraint net, assumed away by a free foliation (Part Four);
- on the arrangement's reading, the mechanism of the balanced chiral mesh whose outputs GR keeps (Part Four);
- and, in the action, the varying shear itself: $T = 0$ is the sector in which the shear does not change (Part Five).

**The field already has the receipt and files it as a problem.** Teitelboim 1973: the algebra of hypersurface deformations does not close with structure constants; two time-slicings do not commute. That is GR reporting that the DAG decree fails in its own constraint algebra. Read as a report rather than a problem, it says the net has cycles, serialization loses information, and the uniqueness of 1854 was bought by assuming otherwise.

**The host's reasons for the symmetric connection are good ones, and they belong in the account.** Uniqueness, local removability, second-order field equations, no extra field to carry, and a century of confirmed numbers (Part Two §V). What has no account is the **other column** — and the reason the other column went unwritten is the ordinary one, that an unflagged assumption collects problems rather than counterevidence, each filed in its own subfield.

**Which route.** Two were on the table. Section III has said what happened to the first: the axial channel is not a route the corpus chooses but the place its coupling is forced to live, and it is bounded. The second is the thermodynamic route.

Jacobson (1995) derived the Einstein field equations from the Clausius relation $\delta Q = T\,dS$ applied to local Rindler horizons, with the Einstein equation emerging as an **equation of state**. Padmanabhan and Verlinde developed variants. The programme is contested in its details, and whether it is a derivation or a consistency check is genuinely open; this file does not adjudicate that. The thermodynamic route is the corpus's standing position, not this file's recommendation: `On_TheGravityDerivation` §III carries Jacobson as **ADOPTED** and lands on semiclassical gravity in the Diósi–Penrose family with three funded falsifiers. What this file adds is the reasons it has the right shape.

1. **It is where a cost column is.** Part Four's friction report says the host bought time-reversal symmetry by having no bill. An equation of state is precisely where a bill comes back in — the one object that relates a symmetric relation at the large scale to an ordered accumulation at the small one without calling either an illusion.
2. **`L0-ParadoxEngine` licenses it, specifically.** Its crystal is frozen at the large scale and vibrating at the small one, with neither state causing the other. An equation of state is that object, and Jacobson's result has the crystal's shape.
3. **It prices the right thing, and it says where the price goes.** Here the corpus's own account needs a correction. `On_TheGravityDerivation` §III identifies each commit's erasure tax with Jacobson's $\delta Q$. But Jacobson's 1995 derivation uses the **equilibrium** Clausius relation, in which $\delta Q$ is a reversible heat flux. Eling, Guedens and Jacobson (2006) showed that corrections to the entropy require a **non-equilibrium** treatment, $dS = \delta Q/T + dS_i$, with an internal entropy-production term $dS_i$. A Landauer tax is irreversible entropy production. On that accounting it belongs in $dS_i$, not in $\delta Q$. So the Einstein equation is the **equilibrium** equation of state — the held account — and the corpus's committed register appears as the non-equilibrium term. That is the same split Part Five found in the action: what is held can be written as an equation; what is committed appears as a dissipative correction to it. The identification is reported at `On_TheGravityDerivation`'s own address for re-seating.

**What unfreezing is, then.** Not a new field equation. The retirement of an inherited price estimate. The uniqueness of the Levi-Civita connection is the output of a one-sided closure decree — translation zeroed, rotation kept — rather than a fact about space. The decree's cost can be itemized and has been. Each item corresponds to a standing open problem in gravitational physics. The field has had the receipt since 1973 and read it as a difficulty rather than a bill. And the decree now sits inside an action, as the sector where a shear stops changing, with one dial and an experimental bound on it.

Riemann said, accurately, that the results of the direction-dependent case could not be geometrically expressed. He was right about that, and about its cost he was guessing, as anyone would have been. **What the set-aside case carries cannot be read off a surface** — which is why standing where both readings of an edge are visible is the method and not a flourish.

---

## V. Where the Framework Crosses to the Real Axis

A framework this internally articulated has to show where it touches the real axis, and the diagnostic is algebraic rather than rhetorical. `ProofE_Solipsism` supplies it: the real axis is closed under multiplication; the imaginary axis is not; $i \times i = -1$ is real. **An interior's own operations produce exterior outputs whether or not the framework grants the exterior independent standing.** So the test of a construction is not whether it is self-consistent — every closed system is — but whether it crosses back to the real axis, and what it does when the crossing disagrees. This framework crosses in three places, and the discipline that keeps the crossings honest is written as rules, not intentions.

**The discipline.** `L4-K4-Infinities`' Four-Category Datasheet sorts every number into Grammar, Substrate (*"consumed, never derived — the grammar cannot emit the weight of the ink"*), State, and Bridge, under five rules: publish the ledger; no new dials; dimensionless outputs only; derive relations, consume values; pre-register. Each rule bars one particular compensating elaboration, and a framework whose own datasheet forbids dials has installed the defence structurally. Part Five obeys it: one dial, itemized, and a prohibition on borrowing its value.

**A correction term with a number on it.** `L3-ConstitutiveAlpha` reads $\alpha = Z_0/2R_K$ constitutively and derives that a crossing sampling all three impedance modes must read at exactly three orders, $\alpha^{-1}, \alpha^0, \alpha^{+1}$. For the pion-to-electron ratio:

$$\frac{m_{\pi^\pm}}{m_e} \;=\; \frac{2}{\alpha} \;-\; \frac{3}{\pi} \;+\; 2\alpha \;=\; 273.131663 \qquad (\text{measured } 273.132440;\ 2.84\ \text{ppm}).$$

The leading term alone is Nambu's 1952 relation and is $0.344\%$ high. **The middle term is the prediction**: a coupling-independent rotation cost that takes a three-parts-in-a-thousand discrepancy to three parts in a million with no fitted parameter. The file prices its own confidence: the shape is landed, the coefficients are an **open vote** at a stated chance rate (the CA §IV script's local-density estimate 0.0558 — 72 of the 1332 family forms within the 2.84-ppm window; `scripts/verify_r5_claims.py`), the value $1/137$ is not claimed, and the falsifier is its own: the integer $3$ is generation-blind, so a crossing at generation two or three must carry the same $3$.

**A prohibition.** No graviton. `L0-EinsteinTrace` §VII–VIII and `Q16` KM-2: the three $P$-edges are zero-impedance writing heads, $P$ is the receiving ledger rather than a channel, and so no exchange boson is required — *"for the same reason a printed book requires no exchange particle between its words."* And: *"The null results in graviton detection are not failures of experimental sensitivity. They are the laboratory reporting, correctly, that an equation of state possesses no particle."* That is a real-axis commitment, falsifiable by a single detection.

**A localization line, and a measurement that is running.** `L4-K4-Infinities` KI-6:

> "The one sentence in this construction that departs from general relativity says the metric sources from committed entries only: the medium's homogeneous uncompiled level does not source $G_{\mu\nu}$. **If it is shown to, the register split dies, and the resolution of the vacuum-energy gap dies with it.**"

The line falls between **homogeneous** and **localized**. A homogeneous background level cannot be modulated and carries no empirical arbiter. A Casimir cavity sits on the localized side — committed plates, a committed separation, and a gradient that does mechanical work — so by `L4-K4-Infinities` KI-6 and `BENDING_SPACE` §III it sources curvature and **weighs by $\Delta E/c^2$, sign included**, matching standard QFT in curved spacetime (Fulling and collaborators 2007).

### The Sardinian balance

**Archimedes**, an INFN experiment designed and funded by Calloni and collaborators to test whether the regularized vacuum energy of a superconducting Casimir cavity couples to gravity according to the equivalence principle, is built to weigh that localized shift (Calloni and collaborators 2014; the Archimedes collaboration 2015), at Sos Enattos in Sardinia. A rigid Casimir cavity admits only some vacuum modes, so its vacuum energy differs from that of its surroundings by $\Delta E$, producing a force of order $|\Delta E|g/c^2$ — about $10^{-16}$ N. Because static Casimir energy is of order $10^{-18}$ of the apparatus mass, Archimedes **modulates** it by driving layered high-temperature superconducting plates through their transition, converting a sub-attonewton static weight into an AC lock-in signal in the $1$–$100$ mHz band.

Three honest things about it. First, on the localized cavity the corpus agrees with the standard expectation (Fulling and collaborators 2007): **the prediction is a weight at $\Delta E/c^2$**, and a **null** at that sensitivity kills the localized sourcing half of `QED-CCP` §II and `BENDING_SPACE` §XI. Second, Archimedes does **not** arbitrate `KI-6` itself: a homogeneous uncompiled level is unmodulable by definition, so neither a positive weight nor a null tests homogeneous sourcing; where `KI-6` meets cosmic data is the dark-energy drift fork. Third, **the experiment is not the corpus's.** Archimedes tests a question standard quantum field theory in curved spacetime also answers, and a positive weight is consistent with standard semiclassical gravity as well as with the localized criterion. What is the corpus's is the exposure, not the referee.

And `ProofE` bars the one move a closed interior would need to stay closed. ProofE §VII forbids computing the twelve equations across two entities' blankets — *"treating the whole world as happening inside your own math"* — and `L4-K4-Infinities`' takehome rule 5 bars the same operation from the other side: *"the twelve relations govern the inside of one volume."* Two files, two derivations, one prohibition, against exactly the move a closed interior would need.

---

## VI. What the Framework Contributed

The ingredients are standard. Every geometric object in Parts One and Three, and in the four obstacles, is textbook. What the four-pole lens supplied is assembly and one computation — and that is the honest size of it, neither more nor less.

**It made line one visible as a purchase.** $T = 0$ is usually read as "we adopt the Levi-Civita connection." Read as the deletion of one of two orthogonal failures to close — the pitch, not the turn — it is a decision with a cost, and the cost can be itemized.

**It separated nil from zero, and the separation was already made for another problem.** `L4-K4-Infinities` drew it to dissolve the vacuum catastrophe; here it re-reads the first line of a different subject without adjustment. The vacuum catastrophe bills an unopened account as full; the Riemann freeze reads it as empty.

**It located the freeze dimensionally.** The metric is face-level structure, a two-slot pairing. The part of torsion that carries a local handedness is a three-form, absent on a face and one number per point in the first solid. So the freeze is invisible on the floor and bites exactly where volume begins, and a reader whose instrument is rank is reading a solid from one of its faces without knowing it.

**It put unrelated-looking absences in one frame.** The arrow of time, the local handedness of the geometry, the ordering of transports, the mismatch between the quantum and relativistic clocks, and the problem of time are five conversations in five literatures. As costs of one closure decree, they are one bill with five lines.

**It supplied the instrument type.** "What would observe a write-only ordering?" sounds unanswerable and is not, because the frame says what kind of thing the answer must be: not a field value but an invariant that survives every relabelling. Physics already has such invariants. Which one could observe this ordering is now a question about the axial channel.

**It supplied a register for the singularity.** The Honest Tear — *"the equation blows up to report the boundary of its own applicability"* — is the right reading of both the initial and the black-hole singularities, and the Trautman bounce takes its proper status from it: a demonstration that the tear is at the edge of one theory's assumption, not of the world.

**And it computed two things.** An action in which the torsion-free connection is the stationary-offset sector, the axial channel is forced by health, the offsets' dynamics are induced with no new scale, matter sources them through chirality non-conservation, and the coupling's experimental exposure sits in $\beta\theta^2\nu \lesssim 3\times10^{-31}$ GeV, bounded by experiments that already exist. And then the coupling itself, forced rather than chosen: $F = \theta_F\theta_C\theta_M$, because the Nieh–Yan density is odd under parity and time reversal, because inversion exchanges the two edges of every bimedian, and because a phase lead becomes a lag. Three inputs, all of them in the corpus or in the geometry already, and a coupling at third order with no dial of its own.

The framework did not compute anything a differential geometer could not have computed. It said which absences to hold together, which line to re-read, which dimension the freeze lives in, which instrument type an ordering demands, which distinction the symbol $0$ was hiding — and it wrote down the coupling.

---

## What Reading Part Six Back Should Leave

The obstacles are real. One the action sidesteps by not needing higher derivatives at all. One has shrunk twice: the engine supplies a solder form on the discrete side, and the continuum coupling turns out not to need one. One the corpus answers consistently, by severance rather than destruction. And one — the measured bounds — has changed from a wall the file did not touch into a constraint on the file's own dial, at a stated quadratic order.

The four objections that landed were correct, and three of them were correct at a price the host cannot itemize: soldering it cannot derive, reversibility bought by never selecting, autonomy that assumes coarse-graining. The routes that do not work are marked, and one route declared dead is alive, because it was never a choice.

The unfreeze is the retirement of an estimate, not a new equation: a one-sided closure decree, its cost itemized, its receipt in the field's own constraint algebra since 1973, and now its place inside an action as the sector where a shear stops changing. The thermodynamic route has the right shape because it is where a cost column comes back in — and it says where the cost goes, in the term for entropy production.

And the framework crosses to the real axis in three places: a correction term that takes a known ratio from three parts in a thousand to three in a million, a prohibition on the graviton falsifiable by a single detection, and a localized-vs-homogeneous criterion that separates what weighs on a balance at Sos Enattos from what no balance can modulate. The case does not end by defending itself. It ends in measurements — a balance in Sardinia, and the cosmological surveys tracking whether the cosmic hold drifts — that only one side can survive.

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

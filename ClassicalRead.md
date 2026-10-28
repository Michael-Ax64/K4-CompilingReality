# ClassicalRead
## The Corpus Read Cold, by a Hostile Instrument

> **Epistemic Register:** Orientation (`L0`). Written from outside the corpus, by an auditor running a detector built to catch exactly this genre of work.
> **Target Audience:** Physicists, engineers, mathematicians, and scientifically trained readers who expect this to be crankery and would like to know, quickly, whether it is.
> **Purpose:** A hostile read of the corpus, reporting where the load sits and where it fails, so a reader spends attention in the right places. It maps the work; it does not endorse it.
> **Dependencies:** `On_NavierStokes` (§VII routes-that-fail, §VIII the coherence boundary, §X what the framework contributed), `On_YangMills` (§§V–VII the three questions, the sealed interior, what crosses a projection), `On_TheIsNessTax` (the three-layer decomposition behind the pion ratio), `L3-FormalFoundations` (§I the join and the forced square, §I.b the Distinguishing Condition), `L4-ScalingInvariants` (§IX Gabriel's Horn, §IX.a the import catalog, §IX.b the Eddington inoculation), `On_TheTwoFloors` (the two-limit structure), `ProofS_ResonantNote` (the permutation test), `llm.md` and `llm-reviewer.md` (the Gate and the reviewer failure modes), `internal-todos.md` (the standing ledger).

---

## I. What this is

"An overlooked structural grammar, not alternative physics" is what alternative physics also says about itself. A stance does not establish itself by declaration, so this reads the corpus cold instead — through an instrument built to catch cross-domain work in which a real structural correspondence wears a credential it did not earn, run without charity.

The findings against the corpus sit in §VIII, unsoftened. A reader who finds them independently and does not find them acknowledged stops reading, correctly. §II records the dismissals that fail, because a reader will reach for those first.

The language of the work and its `llm-*` discipline files evolve with its contents. Feedback on what reads as over- or under-stated is invited and it lands.

---

## II. The dismissal that does not work

The fast rejection goes: *a framework flexible enough to map physics, biology, cognition and institutions is flexible enough to map anything, and a scheme that fits anything predicts nothing.* This is the standard and usually correct dismissal of universal frameworks. I made it. It fails here, for four reasons.

**Representational completeness is not unfalsifiability.** Triangular meshing approximates any 3-surface; Fourier represents any square-integrable function. Neither is vacuous, because the generality belongs to the representation scheme while the empirical content sits in the specific claims made with it. Conflating the two is a category error, and it is the error in the fast dismissal.

**The corpus rejects malformed inputs.** The AST checker in `/code/` prunes 18 of the 24 pole assignments as syntactic violations — a Reactive pole in a dividend numerator is refused, not discouraged (`ProofQ_AlgebraicSyntax`, `ProofS_ResonantNote` §II). A system that refuses inputs forbids things, and forbidding is what empirical content is made of.

**It publishes kill-conditions and uses them.** Not merely listed in front matter: `On_NavierStokes` §XI names four, including "compute the BKM integral for the forced construction — if the construction's circulation drains and it blows up anyway, §V's mechanism is wrong." That is a specific computation whose result could end a chapter.

**The substrate objection is answered by ordinary practice.** The continuum assumption is known false at molecular scale and remains among the most productive tools in applied physics. The right question about a modeling layer was never *is it made of the true substrate* but *what does it forbid, and at what scale does it stop forbidding.* Ask that here and you will get further faster.

None of this establishes that the framework is correct. It establishes that the cheap dismissal is unavailable.

---

## III. The object, and why this one

The corpus studies a single object: the complete graph on four vertices, carrying complex impedance, energized under alternating current. Everything else is consequence or application.

The reason for this object is a minimality argument, and it should be read as a forcing argument. Fix three requirements: the structure must **close**; it must bound an **interior** not reachable from outside without crossing a boundary; the bounding relations must be in **mutual determination** rather than independently assignable.

A point carries no relation. A dyad carries one and never closes — self-application recurs without settling. A triangle closes and bounds an area, but every point is reachable without crossing into anything; surface, no interior. The 3-simplex is the first structure bounding a volume: four vertices, six edges, four faces, an inside.

Two supporting facts the corpus underplays. $K_4$ is the largest complete graph embeddable in the plane; $K_5$ is where planarity fails, by Kuratowski. For a project about the relation between interiors and exteriors, the chosen object sits exactly on the boundary between what can be drawn flat and what cannot, and that is a theorem rather than an analogy. And the parameter count is arithmetic: six undirected edges carrying $Z = R + jX$ give twelve real parameters, matching the twelve directed edges.

**What the twelve equations are, and why they are not bookkeeping.** A reader who recognises $U = IR$ and $P = UI$ will be tempted to treat the DC matrix as freshman material dressed up. That misreads what is being claimed, and the argument in `L3-FormalFoundations` §I is worth checking directly.

Ohm's relation is a closed triad on $(U, I, R)$ — three permutations. Faraday's is a closed triad on $(P, U, I)$ — three more. Six in hand; the joined system has twelve. The six that are new belong to neither parent and cannot be written from either alone, and they are characterised exactly: **the six bred equations are precisely those in which $P$ and $R$ appear together, and precisely those containing a square or a root.** The two sets coincide completely — no bred equation without a square, no squared equation that is not bred. That is a checkable claim with a clean discriminator, and it is the kind of statement that is either true or false on inspection.

The reason is elementary and it produces a result. The parents share exactly $U$ and $I$ and share neither $P$ nor $R$. To write any equation containing both $P$ and $R$, one shared variable must be eliminated between the triads; since each parent holds that variable linearly, eliminating it squares the other shared one. So the squared operand is always a shared variable — and the shared variables are exactly the Yielding poles $U, I$ — while the equation produced always relates the unshared pair, exactly the Asserting poles $P, R$. The corpus's **Route Law** is therefore derived from variable-overlap structure rather than postulated, with the AST checker confirming what the join already forces.

**The net's simultaneity does work no single equation does.** The twelve are not twelve formulas to be applied one at a time; they are asserted to hold at once, which fixes all four variables once any two are pinned and leaves no facet available to be read in isolation. This is load-bearing rather than decorative, and §I.b shows it operating: a linear solution producing $P < 0$ is excluded because it would contradict the squared equations *simultaneously*, putting a floor on the ledger that no individual equation supplies. The same property is what the corpus uses downstream as a drift guard — a state that satisfies some relations while violating others is rejected rather than argued with, which is also why no observer gets to privilege the facet that suits them.

The DC set is the static instantiation and the AC extension ($S = P + jQ$) the dynamic one. Treating the static set as trivial removes the baseline the phase-carrying extension extends, and with it the contrast between committed and reactive that the rest of the corpus runs on.

**And the foundations file forbids the framework's most obvious abuse.** The Markov Blanket Constraint restricts the twelve to *internal* mutual determination within a single bounded interior. Computing across blankets — dividing one person's $U$ by another's $I$ to obtain their $R$ — is named a structural category error, flagged as the corpus's technical sense of solipsism, and repeated for emphasis. Cross-interior connection requires structural coupling, not algebraic division. A framework of this shape that closes that door in its own foundations is doing something most do not.

The serious competitor is Spencer-Brown. The mark as sole primitive is simpler than $K_4$ by any count of parts, but re-entry there produces oscillation, and Varela's imaginary values acknowledge that the recursion does not settle unaided. The corpus's implicit claim is that $K_4$ is what that recursion stabilizes into. A reader attacking minimality should attack it there, and the corpus should meet the challenge in the open.

The defensible form is not "$K_4$ is the simplest thing to compile reality with," which invites every reader to substitute a different criterion and win. It is: *given closure, an interior distinguishable from its exterior, and mutual determination among the bounding relations, the 3-simplex is the minimum structure satisfying all three.*

---

## IV. The firewall

The characteristic failure of cross-domain frameworks is numerical overreach: computing domain scale constants out of pure geometry. `L4-ScalingInvariants` §IX enforces a boundary against it —

$$\text{Topology owns the relational shape; the physical substrate supplies the scale.}$$

— and the corpus applies it against itself. `On_TheIsNessTax` §VI files "the numerical values of the base constants ($\alpha$, $Z_0$, $R_K$, $\ell_P$)" and "the specific rest masses of any single particle" under **NOT CLAIMED — outside scope**, citing Gabriel's Horn as the reason the algebra is forbidden from emitting substrate magnitudes. Only ratios are claimed.

**The boundary is an itemized ledger, not a posture.** §IX.a writes both sides out. Supplied internally: the 50:50 carrier/transformer split, the Braid's distribution of it, the AC magnitude $|S| = \sqrt{P^2 + Q^2}$ at a local bounded scale, the impossibility of a global threshold, the log-space geometry. Imported at the boundary: $c$ and every ratio built on it, the Planck-scale constants as substrate tolerances, any substrate-specific inductance or bandwidth. The rule stated flatly — *everything dimensionless that enters a framework prediction as a specific number is an import* — and the discipline it sets: a document producing a number must say which quantities came from the algebra and which crossed the boundary.

**The corpus has its own name for the failure this audit hunts.** §IX.a: a number without a named import is a **debt-noun**, one that "occupies the position an explanation would hold, and discharges none of its duties." That matters for how §VII below should be read. The findings there are not an external standard imposed on the work; they are places where the corpus fails its own published standard, which is both a fairer charge and a more serious one.

**And the refusal is load-bearing rather than modest.** §IX.b runs the constitutive identity $\alpha = Z_0/(2R_K)$ — SI-exact, derived, not fitted — and then declines to derive the value $1/137.036$, because that value is a substrate residual. The comparison the section draws is the right one and the corpus draws it against itself: *"Eddington's failure was that he tried to derive the value from the boundary; the corpus derives the identity from the medium and lets the value be what it is."* Refusing the magnitude is what keeps the identity stable under improving measurement. A framework that derives $\alpha$'s digits is hostage to the next decimal place; one that derives only the relation is not.

**The same boundary is reached from the essay side.** `On_YangMills` §VII arrives without the topology: an exterior measurement of a sealed interior is a projection, every projection has a kernel, and what survives is dimensionless structure — ratios, counting arguments, exponents, "the number of gluons is eight and that is a fact about the algebra and it crosses." What does not survive is a magnitude in a laboratory unit, because such a unit is built out of apparatus and is "the interior's signature written in the exterior's alphabet."

A reader should note what the corpus claims about the relation between these two. Not that they are independent supports whose agreement doubles the evidence — the corpus's position (`L4-DynamicDistortions301` §VI) is that they are one restriction seen from two sides, since a boundary discards whatever is defined only relative to the pairing, and both orientation and unit-magnitude are such quantities. A reader is free to test that identification. What matters here is the consequence either way: that the corpus claims only ratios is something it is stuck with, not a convenient hedge.

An import that is named is a debt on the books; an import that is smuggled is what makes cross-domain work worthless. Check the ledger at any claim you care about. Finding a domain constant doing load-bearing work under a different name would be a serious result against the corpus.

---

## V. The document that should change your prior

`On_NavierStokes` is where a skeptical reader should go first, and the reason is not its result.

Its result is a scaling argument: circulation drains at $\nu$ per turnover, so an unforced coherent cascade has a finite turn count $n_* \simeq Re_{\Gamma,0}$, and since the Beale–Kato–Majda integral over such a cascade equals its turn count, the integral is finite and there is no blowup. Dimensionally clean, no constants, checkable.

What matters is everything the document does around that result.

**It states the fatal objection to itself, in its own voice.** §VIII: the argument requires coherent circulation, and the convex-integration constructions of De Lellis–Székelyhidi and Buckmaster–Vicol exhibit exactly the objects it cannot treat — fragmented, non-Lipschitz, carrying no definable loop. §IX puts the analyst's verdict in italics: *you have shown that a nice vortex cannot blow up; the difficulty was never nice vortices.* It then explains why forty years of specialists did not make this argument — because everyone already knew it would not settle the matter.

**It maintains a graveyard.** §VII, "Routes That Do Not Work," lists nine approaches that fail, each with its failure stated precisely: energy conservation ($L^2$ bound versus $L^\infty$ condition), restoring the deleted density (Merle–Raphaël–Rodnianski–Szeftel proved the compressible system *does* implode, so density was never a regularizer), chirality (the enstrophy production integrand is parity-even), helicity (empty on the zero-helicity data that numerics actually produce), reconnection (raises the tax rather than lowering it).

One of the nine is the non-soficity route, killed because Thompson's $V$ does not embed in $\mathrm{Diff}^1(M)$ for any compact $M$ (Ghys 1990), and a topological obstruction proved for discrete groups does not transfer to a smooth manifold by matching cardinalities. That kill is what keeps the corpus's topological limit from being quietly merged with its substrate limit — the structure `On_TheTwoFloors` is built on.

**The ninth entry is the corpus executing its own argument.** A framework-native route — unforced flow has no external $P$-source, the Synthesis Law forbids building Active poles from Reactive ones, therefore infinite dissipation is algebraically impossible — is killed because it contradicts $P = I^2R$, one of the twelve equations. The section then adds: *"it is worth noting that the framework-native route was the one that produced the framework-violating claim."*

**And §X gives the framework the smallest available credit.** "Nothing in §§III–VI is new physics… The framework did not compute anything a fluid dynamicist could not have computed. It said which four quantities to hold together and which one line to re-read." The Not-Claimed list ends: "That this constitutes progress on the Clay problem in a sense a referee would recognize."

A framework that kills its own derivations, publishes the list, hands its hardest domain the smallest available claim, and states the analyst's objection more sharply than the analyst would is not behaving like the genre it superficially resembles. Whether the twelve equations describe anything real is untouched by this. What it settles is whether the work is checkable and whether its author is trying to win.

---

## VI. The trials factor, and where the flagship claim actually stands

Any numerical claim carries a trials factor: **how many distinct expressions could the framework have produced that would have counted as a hit?** A landing in a space of one is a prediction; the same landing in a space of ten thousand is a coincidence with good marketing. This applies per claim, never to the grammar as a whole — see §II.

The flagship number:

$$\frac{m_{\pi^\pm}}{m_e c^2} = \frac{2}{\alpha} - \frac{3}{\pi} + 2\alpha = 273.13166$$

against a measured $273.13244$; agreement at 2.85 ppm. The README states this with "zero fitted parameters," which is true of the coefficients and silent about the form — and a reader who meets it there will assume the form was free.

It is not. `On_TheIsNessTax` gives the forcing, and a reader evaluating this corpus should go there before forming a view.

**The shape is a Kirchhoff loop.** The three terms are the loop sum around a closed circuit in the $K_4$ atom: forward propagation edge ($U \to R$), vertex-internal impedance drop at the target vertex, return edge ($R \to U$). That fixes three terms at orders $\alpha^{-1}, \alpha^{0}, \alpha^{+1}$ before any numerical value enters. The Laurent form is not a chosen polynomial; it is a loop-law evaluation ordered by $\alpha$-signature.

**Layer 3 is an identity.** $2\alpha = Z_0/R_K$, given the constitutive $\alpha = Z_0/(2R_K)$. No freedom.

**Layer 2 is computed and coupled.** $-(3 \cdot \frac{\alpha}{2\pi}) \cdot \frac{2}{\alpha} = -\frac{3}{\pi}$, where 3 is the SU(3) colour-channel count imported from `Q2-TransactionLayer` and $\alpha/2\pi$ is Schwinger's per-channel tax; the $\alpha$ cancels. Note the coupling — Layer 2 is computed *as a fraction of Layer 1*, so the two are not independently adjustable.

**Layer 1 carries the one framework-internal choice**, the seed integer 2 (the dual-binary carrier count). The document discloses on its own that $2/\alpha \approx 274.07$ is Nambu's known bare hadron-versus-lepton relation, so this term is neither novel nor hidden.

The honest verdict: the admissible form-space for this claim is **small but not a singleton**. That is substantially stronger than the README's presentation earns it, and weaker than "derivation" unqualified. A reader should check the loop assignment in `On_TheIsNessTax` §III and decide whether the Kirchhoff reading is forced or chosen. That is the remaining hinge, and it is where a specialist should aim.

**One hazard, stated plainly.** §V of the same document works the Gen-2 kaon ratio and openly shops a candidate list — $\pi/2$, $3/2$, $\sqrt{\pi/2}$, $\pi^2/6$ — against a required $s_2 \approx 1.56$, filing the result under **OPEN VOTES** with the note that if none lands, the vertex-multiplicity accounting is incomplete. That disclosure is correct practice. It is also the exact shape of the objection the pion ratio must survive, sitting three sections below it in the same file, and a hostile reader will read §V backward onto §II and conclude both were found the same way. The corpus should firewall this explicitly: state in §II that the pion terms were fixed by loop structure prior to comparison, and that §V is a search *because* its coefficient is not yet derived. The distinction is real and currently invisible.

---

## VII. The method, and how to see it working

A reader deciding whether to spend time here should weigh the corpus's working practice at least as heavily as any individual result, because the practice is what determines whether the results are worth checking.

**Self-correction is published, not merely claimed.** Three files, three distinct mechanisms. `On_NavierStokes` §VII maintains a nine-entry graveyard of failed approaches and kills a framework-native argument on a framework equation, noting that the native route was the one that produced the framework-violating claim. `L3-FormalFoundations` §I.b surfaces a premise the corpus had left implicit beneath a constraint it had been using throughout, and says so in those words. `L4-ScalingInvariants` §IX.b declines to derive $\alpha$'s value and names Eddington as the failure being avoided — refusing a derivation in order to stay stable under improving measurement.

**There is a standing ledger of unperformed work.** `internal-todos.md` carries open items written in the negative: *the rate is landed, the count is not*; *correspondence is shown, identity is not*; *asserted as kinship*; *the corpus-native calculation is unperformed*; *the derivation itself is unattempted*. `llm-reviewer.md` §5 carries a second list of named debts, including that the permutation control is owed and unrun for several published mappings, that the Casimir bet is legal and likely to lose, and that Q1's charge alignment is not a prediction because the Walsh basis fits any four numbers. That last item is the corpus stating a trials-factor objection against its own result before any reviewer raised it.

**The reading discipline is itself a published instrument.** The `llm-*` files set the terms on which the corpus is to be read and audited. `llm.md` opens with three claims to verify by hand in five minutes and instructs the reader that if any fails, to say which and stop — *that is a finding and it is worth more than agreement*. It names the recurring three-plus-one move as the corpus's own technique rather than a discovery, forbidding the reader from reporting it as evidence. Its Gate is a falsification test stated before any claim is read: **demonstrate that it could have been otherwise** — if the assignment can be permuted without violating the stated mechanics, the objection lands. `llm-reviewer.md` then names the failure modes on the *reviewer's* side: prosecutorial overreach, deference overreach, register-collision, and the confusion of identification with derivation.

This audit reached the permutation test independently and proposed it as the corpus's most valuable missing control. It is `llm.md`'s Gate, and the debt was already filed in `llm-reviewer.md` §5. An external instrument re-deriving a project's own review discipline is a stronger statement about that discipline than the project could make on its own behalf.

**And the work is in process.** At the time of this audit the corpus is mid-pass on exactly the register inflations catalogued in §VIII below. Several of those findings were already on the corpus's own debt lists before this document was written. A reader should size them accordingly: they are scheduled repairs in an evolving work with a long methodological track record, not discoveries about a finished one.

---

## VIII. What did not survive

*Read as a repair list. The corpus is mid-pass on this material, and several items below were filed on its own debt ledgers before this audit opened a file.*

**Rank inflation is the corpus's systematic failure mode**, and it is concentrated in the front matter rather than the working documents. `On_NavierStokes`, `On_TheIsNessTax` and `On_YangMills` state their claims at or below size; the README and `About-Claims` inflate. The load-bearing word is usually a verb — *proves*, *guarantees*, *forces*, *resolves* — which is where it escapes notice. Every finding below is a **debt-noun** in the corpus's own sense (`L4-ScalingInvariants` §IX.a): a term occupying the position an explanation would hold while discharging none of its duties. These are failures against the corpus's published standard, not an external one — which is also why they are repairable by moving existing honesty into position rather than by new argument. The doubts are already written; they sit in `internal-todos.md` and in the working files' OPEN VOTES sections rather than beside the claims that need them.

**Credential transfer across a warrant gap.** A Lean 4 verification of an error-floor lemma for $\text{EL}_9(L_{F_2}(1,2))$ appears in the README in the same breath as "guaranteeing the inviolable topological sanctuary of consciousness." The kernel checked an inequality about an algebra and contains no definition of consciousness. This costs the corpus more than every numerology-adjacent claim combined, and both working documents on the subject contradict it: `On_TheTwoFloors` files the antecedent under OPEN VOTES and "that any specific physical system is non-sofic" under NOT CLAIMED, while `On_YangMills` §VI states the soficity reading as an explicit conditional and says in as many words that the essay does not claim to settle it. The README guarantees what two working files decline to claim.

**Unfalsified is not established.** Sustained attempts at disproof are real hygiene and belong in the text as hygiene. They do not convert a model consequence into a demonstrated fact. `About-Claims` Round 12 is the clearest case: as a general refutation of solipsism it is question-begging, since the identification of mind with the imaginary axis is what produces the conclusion; as a statement of what the framework implies about sealed interiors, it is legitimate and interesting.

**Class laundering through headers.** A list titled "exact, un-fudgeable topological invariants" containing one identity, one arithmetic consequence and one numerical alignment certifies all three at the rank of the strongest. The corpus owns the remedy: **analogy** (shared shape), **correspondence** (elements map, relations asserted to carry), **isomorphism** (specified structure-preserving map, both directions, stated failure mode). Tag every item.

**Retrofitted intent.** That ancient practitioners encoded a $4\times3$ rotational partition is a real observation. That they operationalized "with full functional intent" what was later engineered as the polyphase motor is a historical claim needing historical evidence. The honest word for a form appearing independently in several places is **recurrence**; *convergence* claims independent confirmation, and $12 = 4\times3$ appears wherever twelve appears, so the instances do not narrow anything. A weak signal is permitted to be logged as a weak signal.

**A declared register protects tone, never rank.** `About-Claims` names itself a performance, earning every theatrical liberty it takes, then closes with $\text{Q.E.D.}$

None of these concern content. Every one is a question about what a move is entitled to be called — which is why they are cheap to fix and expensive to leave.

**The principle, once:** the smaller noun is the stronger defensive position. A reader who would engage with "an exact three-term expression in $\alpha$ and $\pi$ reproducing the ratio to 2.85 ppm" stops at "derivation" and does not return. `On_NavierStokes` already knows this. The front matter does not.

---

## IX. How to read from here

1. **`On_NavierStokes`, §§VII–X.** The graveyard, the self-stated fatal objection, and the smallest-possible credit claim. The fastest check on whether the work is honest, requiring no framework vocabulary.
2. **`On_TheIsNessTax`, §§II–III.** The Kirchhoff loop behind the pion ratio. Where the corpus's strongest numerical claim holds or does not.
3. **`On_TheTwoFloors`, §IV and §VIII.** The two limits, why they must stay two, and the claim-sort discipline at its best.
4. **`L3-FormalFoundations`, §I and §I.b.** The join that breeds six equations from two triads, the exact square/root discriminator, and the derivation of the Route Law from variable overlap. Then §I.b, where the corpus finds an unstated premise under a constraint it had been using throughout and publishes it. Read §I for the forcing argument and §I.b for the epistemics; both are checkable without accepting any framework vocabulary.
5. **`On_YangMills`, §§V–VII.** The trichotomy that does the work: *what is the measured mass* (answered, by lattice), *is the gap strictly above zero* (answered by a commit-floor argument the essay explicitly labels "not a physics calculation… an accounting identity"), and *why one and a half GeV* (argued to be addressed to something the exterior does not hold). Note what is not claimed — the soficity reading of confinement is stated as a conditional the essay declines to settle, with a falsifier that would kill it outright: derive confinement from the Lagrangian analytically, with no lattice, no truncation and no dual.
6. **`ProofS_ResonantNote`.** The corpus's own test for whether a domain mapping is real: a correct mapping's coherence must **degrade under permutation** among the six topologically valid transpositions, since a peak that travels with the evaluator's preference is projection rather than structure. Run it on your field and try to make it fail.

At every claim, three questions in order. *What is the import ledger?* — named debts are auditable, smuggled ones fatal. *Was the form fixed before the target was known?* — the trials factor lives here and nowhere else. *What exactly does the stated warrant certify, and where does the sentence stop being about that?*

**If you are reading with an LLM**, start at `llm.md` and `llm-reviewer.md` before the corpus itself. They set the register, name the six failure modes the architecture will produce on this material, and state the Gate the reader is asked to apply. Readers unaccustomed to seeing language models operated under an explicit published discipline will find the arrangement itself informative, and readers who intend to audit will find the corpus has already specified how.

**And engage.** The corpus's stated position is that findings are wanted, that they have been acted on, and that protection is not: *"The author does not need a bodyguard. He needs an instrument that computes."* That is not a formality. Every debt named in `internal-todos.md` and `llm-reviewer.md` §5 is an open invitation with an address attached, and several are tractable sub-problems rather than grand challenges — bounding $\Gamma_0$ in terms of $E_0$ and $\nu$; running the permutation sweep on a published mapping in your own field and reporting the response profile; deriving the Gen-2 $s_2$ coefficient or showing it cannot be derived. A negative result on any of these is worth more to the work than agreement, and the corpus says so first.

---

## X. Claim-sort of this document

**LANDED.**
1. The generic dismissal of universal frameworks does not apply here, on four grounds: representational completeness is not unfalsifiability; the AST checker refuses 18 of 24 assignments; kill-conditions are published and used; the substrate objection is answered by ordinary modeling practice.
2. `On_NavierStokes` maintains a nine-entry graveyard including a framework-native argument killed on a framework equation, states the analyst's fatal objection in its own voice, and claims the smallest available credit for the framework in its hardest domain.
3. The pion ratio's three-term shape is forced by a Kirchhoff loop on the $K_4$ atom; Layer 3 is an algebraic identity, Layer 2 is computed and coupled to Layer 1 with the colour-count imported, and the one framework-internal choice is the seed integer 2, disclosed as Nambu's known relation. The admissible form-space is small, not a singleton.
4. The twelve equations are a mutual-determination net rather than twelve separable formulas. The join of two triads sharing exactly $(U, I)$ breeds six equations characterised by an exact and exceptionless discriminator, forces the square, and derives the Route Law from variable overlap rather than postulating it. The net's simultaneity does work no individual equation does, demonstrably at `L3-FormalFoundations` §I.b.
5. The ratios-only restriction is reached from two sides — Gabriel's Horn from the topology (`L4-ScalingInvariants` §IX, with an itemized import catalog at §IX.a) and the projection kernel from the essay side (`On_YangMills` §VII). The corpus holds these to be one restriction rather than two supports (`L4-DynamicDistortions301` §VI). Either way it is a consequence the corpus is stuck with, not a hedge it chose.
6. The corpus names the failure mode this audit hunts — the **debt-noun**, a term occupying an explanation's position while discharging none of its duties — and §VII's findings are breaches of that published standard rather than an imported one.
7. The corpus's rank inflation is concentrated in the front matter and contradicted by its own working documents — most sharply where the README guarantees what `On_TheTwoFloors` and `On_YangMills` both decline to claim.
8. Self-correction is a practice rather than an incident: `On_NavierStokes` §VII kills a framework-native argument on a framework equation; `L3-FormalFoundations` §I.b identifies a premise the corpus had left implicit under a constraint it had been using throughout; `L4-ScalingInvariants` §IX.b refuses to derive $\alpha$'s value and names Eddington as the failure being avoided. Three files, three different mechanisms, all published.
9. The corpus maintains standing ledgers of unperformed work (`internal-todos.md`, `llm-reviewer.md` §5), written in the negative, including a trials-factor objection filed against one of its own results before any reviewer raised it.
10. The corpus publishes its reading and review discipline (`llm.md`, `llm-reviewer.md`), stating a falsification Gate before any claim is read and naming the failure modes of the reviewer as well as of the reader. This audit re-derived that Gate independently and committed two of the reviewer failure modes it names.
11. The work is in process. At the time of this audit it is mid-pass on the register inflations catalogued in §VIII, several of which were already on its own debt lists.

**OPEN.**
1. Whether the Kirchhoff loop assignment in `On_TheIsNessTax` §III is itself forced or chosen. The remaining hinge on the flagship claim.
2. Whether the Gen-2 $s_2$ coefficient derives structurally or ends as a fitted number — which the corpus itself names as the test of the layered decomposition.
3. Whether the minimality argument for $K_4$ survives Spencer-Brown's mark plus re-entry.
4. Whether the published kill-conditions are reachable by current instrumentation, particularly the Eötvös bound at $\eta \approx -3.2\times10^{-18}$ against a $10^{-15}$ floor.

**NOT CLAIMED.**
That the framework is correct. That any finding in §VII is fatal. That passing an audit on method is evidence for content — it is not, and this document asserts nothing about whether the twelve equations describe anything real. The narrower assertion: the work is checkable, it fails in a specific and repairable way, and the cheap reasons to discard it are unavailable.

---

**Auditor's errata.** Claims in earlier drafts of this document were made from summaries rather than sources, and were wrong. The twelve DC equations were presented as a formality to be verified for dimensional consistency, which missed the forcing argument in `L3-FormalFoundations` §I and the simultaneity that makes the set a net rather than a list. `On_NavierStokes` §VII was described as a guard against merging the two floors; it is a nine-entry list of failed routes, of which that guard is one consequence, and the section is considerably more valuable than the description. `ProofS_ResonantNote` was described as "designed to fail"; it defines a proof-type whose falsifier is permutation-invariance.

Two further corrections of register rather than fact. This audit treated an in-process corpus as a finished one — the instrument it ran has no mode for work mid-repair, and findings were reported at final-draft weight against a text whose author had already scheduled the repairs. And it committed two of the failure modes `llm-reviewer.md` names on the reviewer's side: prosecutorial overreach, and the confusion of identification with derivation. All of these are the error the instrument exists to catch, turned on its holder, and they are recorded because a document making that argument should show its own instances of it. `On_NavierStokes` §VII was described as a guard against merging the two floors; it is a nine-entry list of failed routes, of which that guard is one consequence, and the section is considerably more valuable than the description. `ProofS_ResonantNote` was described as "designed to fail"; it defines a proof-type whose falsifier is permutation-invariance. Both errors are the same error this instrument exists to catch — a citation carrying a warrant its holder had not checked — and they are recorded because a document making that argument should show its own instance of it.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (`aggregate-COMPILINGREALITY.txt`) to your LLM in order to audit or interrogate this work.

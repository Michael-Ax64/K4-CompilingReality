# L4-Riemann-wip
## Working Notes, Flags for Other Files, Quarantine, and the Numbers

*Companion to `L4-Riemann`. Writing discipline is loosened here: first-person notes are allowed, speculation is allowed where it is marked, and material is kept because losing it would cost more than keeping it. Nothing in this file is landed. The parent and the parts carry the standing claims; `L4-Riemann-evolution` carries the history.*

---

## 0. What This File Is For

Four jobs. **Flags** for other corpus files, where this series found something wrong or overstated at an address it does not own. **Open workings**, stated so that someone could pick each up cold. **Quarantine**, for readings that are suggestive and not yet earned. And **the numbers**: which script produces which figure.

---

## 1. Repairs Made in the Port

The redesign was also the occasion to clear every fossil the census in `L4-Riemann-evolution` §III found. For the record of where each went:

| Fossil in the predecessor | Where it was repaired |
|---|---|
| §I: the square as a committed object, "two more bits" | Part One §I: the square is a pairing; withdrawal pointed to evolution |
| §VII-b.3: "experimental value since the kaon" | Part Four §VIII: struck; $J$ kept as an example of the instrument type, in the wrong sector |
| §XII: commit's tax as Jacobson's $\delta Q$ | Part Six §IV, reason 3: re-seated in $dS_i$ |
| Open traces: "Kill condition 1" | Parent: U-items and kills separated throughout |
| §XII reason 3: "no averageable residue" | Part Six §IV: removed; Monster 4 rewritten |
| §XII cost list: "the sign bit that squaring burnt" | Part Six §IV: cost list rebuilt |
| §XII cost list: arrow unavailable because $U = IR$ is Now↔Past symmetric | Part Six §IV: removed; Part Four §I holds the Time Key reading at its size |
| §XIV: "fixed by $I \leftrightarrow R$ and nothing else" | Part Six §VI: contribution list rebuilt |
| §XV: "$V_4$ abelian, so no contortion" as Grammar | Part One §IV: withdrawn in place; not listed as a result anywhere |
| Route A: "the axial channel is a trap" | Part Five §III, Part Six §III: reversed |
| $\vec\theta$ called "shears" throughout, against DD201's own warning | Renamed to *phase offsets*; disambiguation stated in Part Five §IV and Part Four §VII |
| The parity fork left open, four ways | Closed to $F = \theta_F\theta_C\theta_M$ (Part Five §IV) |
| U1 carried as owed | Answered from `ENGINE` §2.2 (Part One §IV) |
| U3 carried as "one question" | Discharged for both channels (Part One §IV, Part Five §IV) |
| "AC breaks the rank-two floor" left as an expectation | Resolved: doubles it in polar, bends it in rectangular, bend = power factor (Part Two §I) |
| "$T = 0$ removes handedness" | Parts One and Two: global bit survives, local density set to nil |

---

## 2. Flags for Other Files

Found while building this series; not fixed here, because each belongs to its own address.

**`L4-K4-Infinities` — the Laue overstatement.** Part One §VI says the integral *"returns a number and discards the orientation"* and *"One scalar survives. Every vector and tensor component is annihilated"*; the parent's summary of Part One says it *"annihilates every vector."* Laue zeroes the integrated *spatial stress* of a *static* system. It does not forbid a bound system from exporting spin, and protons do. The file's own takehome rule 6 says the precise thing — *"Laue is about the vector sector, not the scalar"* — so the repair is to bring the summary sentences into line with rule 6. The bench used the overstatement against the corpus; Part Five §I records it.

**`L3-NonSoficTopologicalVolumes` §III — Cardinal and Fixed exchanged.** It labels the bimedians *Cardinal {P–U, I–R}, Fixed {P–R, I–U}*. `L4-DynamicDistortions201` §II and `L4-ThePlenum` §VI both have *Fixed {P–U, I–R}, Cardinal {P–R, I–U}*. Two against one; NonSofic is the likely error. Nothing in this series depends on it, but Part Two's harmonic pencil does name Cardinal as $\{P,R\}|\{U,I\}$, which agrees with the majority.

**`QED-EotvosBound` — three defects and one missing rule.** Computed in `scripts/mirror_and_eotvos.py`.
- *Additivity.* Inertial and gravitational mass each add over non-interacting parts, so any aggregate's $\eta$ must be the mass-weighted mean of its parts'. §IV.1 evaluates a passive test mass at the *whole-body* Compton clock, $\omega_C = mc^2/\hbar$ with $m$ the cylinder. Then $\eta \propto P/m^2$, and two identical cylinders side by side get half the $\eta$ of one ($-2.9\times10^{-70}$ becomes $-1.45\times10^{-70}$).
- *Beyond the Planck frequency.* Above the Planck mass, 21.8 μg, the whole-body Compton frequency exceeds the Planck frequency; for a 300 g cylinder by $1.4\times10^7$. `L4-ThePlenum` §VII puts the shortest crossing at the Planck bottleneck.
- *Two clocks in one row.* The table's Compton row gives $\tau \sim 10^{-24}$ s, a nucleon's; the arithmetic beside it uses $(mc^2)^2 \approx (10^{17}\ \text{J})^2$, a cylinder's.
- *The Hubble row.* For the file's own brain (20 W, 1.4 kg), the formula gives $\eta \approx -1.5\times10^2$ at $\omega = H_0$, not *"~1.0 (Dyson saturation)"*; the small-signal expansion has already failed there.
- *The missing rule.* Because $\eta \propto 1/\omega$, the slowest dissipative clock dominates: the same brain gives $-3.2\times10^{-18}$ at EEG, $-4.4\times10^{-12}$ circadian, $-1.6\times10^{-9}$ annual. §IV.3's *"three orders of magnitude below"* MICROSCOPE rests on EEG being the slowest dissipative clock in biology, which it is not. The repair that additivity forces is an intensive clock, which keeps MICROSCOPE passing by a wider margin (about $-5\times10^{-44}$ for 1 mW in 300 g at the nucleon clock). What stays open is the rule that assigns a frame its clock. A candidate of my own, not in the corpus: resolve by channel, $\eta = -\frac{2}{Mc^2}\sum_k P_k/\omega_k$.

**`mono/On_TheGravityDerivation` §III — where the Landauer tax goes.** *"Each commit's erasure tax is the $\delta Q$ [...] The identification is not an analogy."* Jacobson's 1995 derivation is equilibrium, and Eling, Guedens and Jacobson (2006) put irreversible entropy production in a separate term, $dS = \delta Q/T + dS_i$. A Landauer tax is irreversible, so it belongs in $dS_i$. Part Six §IV states the re-seating; the source file should make it at its own address. It strengthens rather than weakens that file: the Einstein equation becomes the equilibrium (held) equation of state, and the committed register appears as the non-equilibrium correction.

**`ProofG_Chirality` §IV — the engine has already withdrawn this claim, and ProofG has not absorbed it.** This is the clearest lexicon-lag in the set, and it is between two proofs rather than between a file and the glossary.

ProofG §IV: *"The wholesale enantiomer operation is the **AR-flip** — the double transposition $(P\,R)(U\,I)$ [...] the AR-flip is even, an element of $V_4$ [...] The enantiomer of the machine is one of the machine's own half-turns; the mirror is not imported, it is the Cardinal ring seen as a reflection."*

`ENGINE-REFERENCE-AC` §2.5 is titled *"Two flips, not one"* and exists to undo exactly that fusion: *"An old sentence fused two different flips under one word 'flip' [...] it equated a single transposition — odd — with a 180° half-turn of the tetrahedron — even. $A_4$ contains no transpositions, so the two objects cannot be equal."* It then names the source: *"`L4-TransitingTheThreeWalls` named its half-turn from the Cardinal case — the AR-flip — and the old text generalized one family's step to all twelve. **It is the Cardinal twin-step; the other families step by their own half-turns.**"*

*Suggested repair:* at §IV, replace "the wholesale enantiomer operation" with the engine's split — the **handedness flip** (odd transposition, the move the operating set lacks) is the mirror; the **twin-step** (even half-turn, one per family) is a rotation the machine owns, and the AR-flip is the Cardinal family's. ProofG's §II mirror — the global reversal of all four face circulations — is an orientation reversal and so belongs with the handedness flip; saying so in one clause would make the proof's two mirrors one object. Nothing in ProofG's landed counts moves: §II's GF(2) rank-3 census and the one global bit are untouched, and the series uses them.

**`ProofG_Chirality` §V — true chirality, against the computed transformation properties.** §V says: *"The circulated tetrahedron of §II is false-chiral [...] The extruded, $\omega$-driven turn is **true-chiral**: its time-reverse is the other mirror, and the ratchet forbids the reversal."* But Barron's true chirality is parity-odd and time-reversal-**even**, and the phase offsets are odd under both (Part Five §IV), which is Barron's *false* chirality — the class of $\mathbf{E}\cdot\mathbf{B}$ and of a spinning cone. §V cites Barron, so the criterion is the file's own.

*Suggested repair, and it may be a result rather than a correction:* Barron's falsely chiral spinning cone becomes truly chiral when a **translation along the rotation axis** is added — that is exactly a screw, and the corpus's helix is a screw. So the honest candidate is that the *offsets alone* are falsely chiral and the *extrusion* — offsets plus the translation along $\omega$ — is truly chiral. If that is right, §V is correct about the object it names and should say that the shear triple by itself is not the carrier of the true chirality. If it is wrong, §V needs withdrawing. Either way it needs a sentence, and this series does not have the standing to write it.

**`L4-DynamicDistortions201` §II — two $\theta$'s, one symbol.** The file states the distinction itself and states it well: *"this $\theta$ is a temporal phase offset and reaches its limit at $\pi$. The $\theta$ of `L4-DynamicDistortions301` §VI.A is a geometric shear parameter on a single cross-section and reaches its limit at $\pi/2$. Both are torsion; they measure different things."* What it does not do is give them different symbols, and the warning is one sentence in the middle of a long section. This series collapsed them anyway, and the collapse cost a turn and nearly cost the action its coupling (`L4-Riemann-evolution` step 19).

*Suggested repair:* distinct symbols — $\theta^{(t)}$ and $\theta^{(g)}$, or $\varphi$ for the temporal offset — and the warning promoted to the section head rather than buried. The distinction is load-bearing downstream: Part Five's coupling is parity-clean **only** because DD201's $\theta$ is the temporal one.

*A second, smaller note, now downgraded.* An earlier version of this file suggested re-anchoring the sign convention on the solid rather than on the labels, because *"P–U leads I–R"* ties a quantity to a name. That is no longer needed: central inversion exchanges the two *edges* of each bimedian whatever they are called, so the parity behaviour is label-independent already (Part Two §V). The convention is fine as written; the two-symbol problem is the real one.

**`ENGINE-REFERENCE-AC` — read in full this session; four items, none of them an arithmetic error.** The counts check out: the five factorizations of twelve, $A_4 = 1+3+8$, the 24 flags, $32 \times 12 = 384$, the attic's $4^6$, and the shadow-lag of 3 on every tour. What follows is unfinished business rather than fault.

1. **§VII's commutator has no defined operands.** The text runs *"the two face-readings do not commute — $[Q_A, Q_B] \neq 0$"*, and the homonym table defines $Q$ as *"§VII's face-reading amplitude, with $Q^2 \to P$."* An amplitude is not an operator, and a commutator needs operators or at least non-commuting objects. $Q_A$ and $Q_B$ are never defined. This is the file's one genuinely load-bearing undefined symbol, and it sits under the torque-motor claim of §X.4 and under the ADVANCE sentence of §VII.
2. **Stock and flow on mass, across two files.** §X.4: *"A loop that must feed itself to keep turning is a loop that must carry standing stock, and standing stock priced in energy is what mass is"* — a stock, and consistent. But *"mass is the price of being"* with the price *"paid continuously"* in torque is a flux. `QED-EotvosBound` §I then seats gravitational mass on $P$ (which §III of that file calls a flux) and inertial mass on $R$ (a stock). Three readings in two files, and `L4-Thermodynamics` §II calls conflating them *"the single most common dimensional error in the classical narrative."* Someone should pick one seating and propagate it.
3. **`[gauge]` is doing a third job.** Part Six §II: the word imports "unphysical redundancy, zero back-reaction" from gauge theory into sentences that mean "the bit-ledger does not bill this." §3.1's own *"gauge is not levitation"* paragraph is the file noticing the problem without renaming the tag.
4. **§2.5's split has not propagated.** The engine fixed the two-flips fusion; `ProofG_Chirality` §IV still carries it (above). The engine's own §2.5 says *"Future proof: when a text hereafter says *the* flip, it means one of these two, never both"* — that proofing needs to reach the files upstream of it.

*And one thing to credit rather than flag:* §2.2's reference pinning and §2.8's edge-to-axis map together answer U1 and supply a solder form, which this series had been carrying as owed. Neither section advertises that it does. A pointer at §2.2 — that simple transitivity plus a named base point is a trivialization, hence a flat connection, hence zero discrete torsion on the floor — would save the next reader the derivation.

**Older items, still open.** Withdraw Step 3a from `ProofS_ResonantNote`. Add the precedence note to `L3-EdgeStateSpace` §I-d. Run the face-orientation 12/12 test.

---

## 3. Open Workings

**3.1 Parity and the coupling — CLOSED, and it closed by reading DD201.** `L4-DynamicDistortions201` §II states that its $\theta$ is a *temporal phase offset* with limit $\pi$, and that DD301's is a *geometric shear* with limit $\pi/2$. With the right one: phase lead becomes lag under time reversal (odd), and central inversion exchanges the two edges of every bimedian because the centroid is the bimedian's own midpoint (odd). The Nieh–Yan density is odd under both, so $F$ must be of odd degree, which excludes $\Delta$ and forces $F = \theta_F\theta_C\theta_M$. In Part Five §IV with `scripts/bimedian_parity.py`. Three things remain worth pressing and they are listed in `L4-Riemann-evolution` §VI.

**3.2 U1 — ANSWERED on the floor.** `ENGINE-REFERENCE-AC` §2.2's reference pinning trivializes the gate torsor; the transport $U(e\to e') = g(e')g(e)^{-1}$ is a connection and is flat; §2.8 supplies the solder form; so discrete torsion is zero at $\theta = 0$. Gauge-invariant discrete torsion lives only where the rotational holonomy around a face is trivial, and there the $\mathbb{Z}_3$ action on $V_4$ supplies it ($T_\Delta \neq 0$ in 96 of 144 closing cases). In Part One §IV with `scripts/engine_connection.py`.

*What is still open, and it is a different question from the one U1 asked:* **which non-flat connection the driven engine runs.** The engine scopes itself to the $\theta = 0$ floor and names the $K_5$ screw thread as where the extension lives (§VIII). A candidate programme: assign each gate-edge a $(v,\sigma)$ that departs from the trivialization by an amount set by the phase advance, and ask for the face holonomy as a function of $\omega$. If $T_\Delta$ grows with the drive and vanishes at $\omega = 0$, that is the discrete twin of Part Five's $\partial F = 0 \Rightarrow T = 0$, and it would be the first place the two registers could be compared quantitatively rather than structurally.

**3.3 U0 — the recurrence. Still open, and counsel's version is not it.** The brief offered a state map with a write-only accumulator. That describes the ledger, but `ENGINE` §X.4's load is *"the loaded hold that the next advance turns against"* — the advance has to **depend on** the load, and in counsel's map it does not. The defining feature is the missing one. (A second, smaller problem: subtracting a projection from a bit-state is not defined.) What is needed is a map $(S_n, L_n) \mapsto (S_{n+1}, L_{n+1})$ in which $S_{n+1}$ is a function of **both** arguments. The engine's own §3.4 tours and §VI recipe are the data to build it from.

**3.4 U4 — the dissipative register. The formalism is settled; three debts are not.** Galley's doubled-variable action is the right vehicle, and the Eling–Guedens–Jacobson balance $dS = \delta Q/T + dS_i$ is the right place for the Landauer tax (Part Six §IV). Counsel's sketch adds:

$$\Box F + \gamma\,\dot F \;=\; \frac{2\kappa\alpha}{\beta}\,\nabla_\mu j_5^\mu$$

which is the shape to aim at, with the equation correctly written for $F$ rather than for a single $\theta$ (geometry sees only one combination). The debts:

1. **$\gamma$ is a new dial** unless it is derived. Naming it after Landauer does not derive it, and the Datasheet forbids new dials. This is the hard one.
2. **A time derivative needs a frame.** $\dot F$ requires a timelike vector, which is a preferred frame, bounded by the same Lorentz-violation experiments Part Five's bound comes from. The corpus's answer would be that each bounded frame's own centroid supplies it — that has to be written into the action rather than asserted beside it.
3. **The difference variable is not the ledger.** In Galley's construction it is an auxiliary set to zero at the end; the dissipated energy leaves through the kernel and is not a coordinate anywhere. Tracking the committed register needs the bath written in explicitly. Counsel's identification of the off-diagonal variation with the ledger is a label, not a mechanism.

And the question none of this touches, which is the one that matters: **does the dissipated energy gravitate?** That is KI-6, and it needs a balance rather than an action.

**3.5 The two invisible directions.** Geometry sees only the combination along $\nabla_{\vec\theta}F$ (Part Five §III). With $F = \theta_F\theta_C\theta_M$ fixed, that direction is now explicit: $\nabla F = (\theta_C\theta_M,\ \theta_F\theta_M,\ \theta_F\theta_C)$. What, if anything, gives the orthogonal two dynamics, and do they couple to anything else?

**3.6 The AC formula set — RESOLVED, and against both expectations.** In the polar chart (log-modulus, phase) the corpus's AC core $S = \hat U\hat I^*$, $\hat U = Z\hat I$ is linear: a modulus floor of rank 2 and a phase floor of rank 2. **It doubles the floor, it does not bend it.** The bend comes from the rectangular split, where the only non-linear function in the system is $\log\cos\theta$ — the power factor — and from the additive layer ($X = \omega L - 1/\omega C$, series and parallel sums). The surface $e^{2p}+e^{2q}=e^{2s}$ has Gaussian curvature **exactly zero**, a cylinder; its mean curvature is non-zero, so it bends in one direction, and that direction is the phase angle. `ENGINE-REFERENCE-AC` §VIII.1 names the operation responsible — *"$|S| = \sqrt{P^2+Q^2}$ requires complex addition"* — and `L3-Electro-AC-db` specifies rectangular form, so by the corpus's own choice of chart the floor is bent. In Part Two §I with `scripts/ac_floor.py`.

*What remains:* the full fifty-equation set has not been enumerated and ranked. The core settles the question of **where** the bend lives; the count of how many independent relations the whole set carries is still unmeasured, and someone should do it from `L3-Electro-AC-db` directly.

**3.7 The class-side tear and the host's orientability.** Q16 KM-1 says the configuration in which both faces read every edge alike tears the class's boundary. A torsion-free manifold does not tear. The series holds both at their levels. What would make it more than a statement of difference is a map from the class's face-reading bookkeeping to something in the host's geometry that changes when the torsion three-form is switched on. Part One §IV's flat trivialization is a new handle here: the tear and the flatness are both statements about the $\theta = 0$ configuration, and they may be the same statement.

**3.8 Population questions, carried from the aggregates turn.** With the coupling fixed, these sharpen. The relevant racemic condition is now specifically **closure under inversion**, not under any mirror: the coupling survives every rotation and reflection of the tetrahedron. So: what is the actual distribution of phase-offset configurations in any physical population, and is it inversion-symmetric? Does spin polarization break inversion symmetry in the relevant sense? Is offset energy held or committed — does it sit in the reactive channel, or does changing an offset pay a tax?

## 4. Quarantine

**The Cardinal floor and classical electromagnetism.** Part Two §III notes that the floor's harmonic pencil privileges the Cardinal diameter and that `L4-ThePlenum` §V puts the medium's wave-to-constitutive swap there. The suggestion that this is *why* classical electromagnetism sits comfortably on the floor closed on the first attempt using material in the house, which is the shape `L4-K4-Infinities-wip` §6.2 says to distrust. What would move it out: a second, independent consequence of "the rank reader stands on Cardinal" that can be checked.

**The AR-flip as a charge conjugation.** It reverses the Active/Reactive bit on both mate pairs at once, which resembles charge conjugation more than parity. Only an analogy — and note `ENGINE` §2.5/U8: the AR-trade fits 8 of the 12 twin-steps, the Fixed family trading within each charge class, so even as an analogy it is family-specific rather than wholesale.

**$\Delta\cdot\theta_F$, odd under two named mirrors.** Recorded so nobody rediscovers it as a compromise. It is odd under the reflection $(P\,U)$ and under the Cardinal twin-step, but also odd under the rotation $(P\,I)(U\,R)$, so it is not invariant under the carrier's rotations and transforms by no natural character. It is also degree 7, hence time-reversal-odd, so it would pass the parity condition — and it still fails on carrier symmetry, which is what rules it out.

**$\theta \approx 31°$.** One experiment's CHSH value through `L4-DynamicDistortions301`'s envelope. An illustration, not a universal shear.

---

## 5. Struck, With What Would Revive Each

- **The burnt-sign reading of the metric.** Dead on Hamiltonian mechanics. *Revive:* never as stated. What survives is Part Four §VI's projection result.
- **$I \leftrightarrow R$ or $U \leftrightarrow R$ as time reversal.** Dead: a relabelling is undirected. *Revive:* no.
- **Field average versus invariant as a way past the bounds.** Dead: it cannot carry an observable between bundles. *Revive:* not needed; the action put the shear in the bounded channel.
- **The AR-flip as spatial parity.** Dead twice over: it is an even half-turn, so a rotation of the solid, and per `ENGINE` §2.5 it is the Cardinal family's twin-step rather than any wholesale mirror. *Revive:* no.
- **$F = \Delta$ (option A), the sixth-order coupling.** Dead on time reversal: even degree cannot be odd under $\vec\theta \to -\vec\theta$. *Revive:* only if DD201's $\theta$ is shown to be time-reversal-even — which would also mean no coupling is parity-clean at any degree, so reviving $\Delta$ this way kills the action instead.
- **"The engine does not supply the connection data."** Dead: it does, in §2.2. The test that produced this took a gate label for a transport. *Revive:* no.
- **The whole-body Compton clock for passive matter** (`QED-EotvosBound`). Dead on additivity. *Revive:* only with an argument that $\eta$ is not a ratio of additive masses.

---

## 6. Superseded Files

`mono/On_TheRiemannFreeze.md`, `mono/On_TheRiemannFreeze-TheAction.md` and `mono/On_TheRiemannFreeze-Submission.md` are superseded by this series and left untouched pending the author's decision on retiring them. The submission was never filed. If the predecessor is kept, it should carry a one-line pointer to `L4-Riemann` at its head, because it still contains the fossils listed in §1.

---

## 7. The Numbers

Every figure in the series comes from one of these scripts, all in `scripts/`:

| Script | Produces |
|---|---|
| `torsion_action.py` | $R(\Gamma)$ coefficients $-\tfrac23, \tfrac32, \tfrac12$, no cross terms; channel health; the inert demanded term; the sphere sign check; the shears as the standard representation of $S_4$, character $(3,1,-1,0,-1)$; invariants and the Molien series; the charge stabilizer |
| `parity_candidates.py` | the parity table of Part Five §IV |
| `aggregate_parity.py` | the averaging table of Part Five §V |
| `aggregate_check.py` | the earlier racemic/homochiral averages (geometric mirror only) |
| `flat_vs_solid.py` | four relation lines, one per face; rank 2 (log, real) against closure rank 3 (GF(2)); the cross-ratios $-1$, $\tfrac12$, $\tfrac12$; three-form component counts 0, 1, 4 |
| `dc_logspace.py` | rank 2; only the identity permutation preserves the plane |
| `mirror_and_eotvos.py` | the twin-step's action on the offsets; the `QED-EotvosBound` additivity and clock checks |
| `bimedian_parity.py` | inversion exchanging each bimedian's two edges; the $T_d$ character of $\vec\theta$ against $(x,y,z)$; the parity/time-reversal table that forces $F = \theta_F\theta_C\theta_M$ |
| `engine_connection.py` | `ENGINE` §2.2 as a trivialization; the canonical transport's flatness; the gauge action on the translational holonomy; the §2.8 solder form round the cube's squares |
| `ac_floor.py` | the polar-chart ranks; Gaussian curvature zero and the $\log\cos\theta$ bend, symbolically; the DC floor's two scalings |
| `counsel_checks.py` | the first pass over counsel's brief, kept for the record; two of its own checks were invalid and are superseded by the three scripts above |

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work. This file is a working spillover and carries nothing landed; read `L4-Riemann` for the standing claims.

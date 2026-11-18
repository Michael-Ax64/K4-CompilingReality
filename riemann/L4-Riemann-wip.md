# L4-Riemann-wip
## Working Notes, Flags for Other Files, Quarantine, and the Numbers

*Companion to `L4-Riemann`. Writing discipline is loosened here: first-person notes are allowed, speculation is allowed where it is marked, and material is kept because losing it would cost more than keeping it. Nothing in this file is landed. The parent and the parts carry the standing claims; `L4-Riemann-evolution` carries the history.*

---

## 0. What This File Is For

Four jobs. **Flags** for other corpus files, where this series found something wrong or overstated at an address it does not own. **Open workings**, stated so that someone could pick each up cold. **Quarantine**, for readings that are suggestive and not yet earned. And **the numbers**: which script produces which figure.

A flag is cleared here only after the repair is verified at its target, and a cleared flag is kept with its disposition rather than deleted, so that a reader who met it in an older copy can see where it went. `L4-Riemann-evolution` is frozen at build time and does not track dispositions; this file does.

**Framing note — abstract base class, embodiment, and the rate-selection frontier.** Several items in §§2–3 cluster on one seam and should not be misread as internal algebraic defects:
* *Abstract DC vs. embodied AC:* `ENGINE-REFERENCE-AC` specifies the isolated, autarkic Floor-3 base class ($\theta = 0$, non-embedded, `[gauge]` selection). Inflating that class into physical, computational, or biological hosts (`BENDING_SPACE`, `BENDING_MINDS`, `L6-TheCircuit`, `L5-TheCyclingMind`) replaces unconditioned `[gauge]` freedom with host constraints—clock surrender under Inversion of Control (`L6-TheCircuit` §§I–III), membrane $RLC$ filter wiring (`L6-TheCircuit` §V), and cycle-switching wrenches (`L5-TheCyclingMind`).
* *Rate-selection is an interface frontier, not a base-class omission:* Because the $K_4$ grammar is scale-free (`L4-ScalingInvariants`), it fixes dimensionless closure and a **1-bit minimum excitation step** (`On_YangMills-Annotated` §X) while leaving absolute operating rate ($\omega$) and unit bit-price to the substrate's carrier-resolution and interior noise floors—precisely where the framework encounters quantum Yang–Mills (`On_YangMills-Annotated` §V), coherent Navier–Stokes cascades (`On_NavierStokes` §§IV–V; `L4-Thermodynamics` §V.3), and the $\zeta$ prime-writing dipole spectrum (`L2-K4-Inferences` Part Four, `ADDRESS`).

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

**`L3-NonSoficTopologicalVolumes` §III — Cardinal and Fixed exchanged.** It labels the bimedians *Cardinal {P–U, I–R}, Fixed {P–R, I–U}*. `L4-DynamicDistortions201` §II and `L4-ThePlenum` §VI both have *Fixed {P–U, I–R}, Cardinal {P–R, I–U}*, and `L3-EdgeStateSpace`'s Kernel Rule settles it by computation: a bimedian is named by the bit it *preserves*, which makes $\{P{-}U, I{-}R\}$ Fixed. That file also names the signature — naming a plane by its flipped bit produces exactly a Cardinal↔Fixed exchange and leaves Mutable untouched, which is the defect here. NonSofic is the error. Nothing in this series depends on it, but Part Two's harmonic pencil does name Cardinal as $\{P,R\}|\{U,I\}$, which agrees with the kernel computation. *(Cross-note: `L4-DynamicDistortions301` §VII.B carries the same Cardinal↔Fixed swap on its dipole labels relative to its own §I and the Kernel Rule; `L4-DynamicDistortions-Sudoku` §0 already documents that label collision.)*

**`QED-EotvosBound` — three defects and one missing rule *(PARTIALLY LANDED at target; residual cleanup and rate-selection reframing remain)*.** Computed in `scripts/mirror_and_eotvos.py`.
- *Additivity.* Inertial and gravitational mass each add over non-interacting parts, so any aggregate's $\eta$ must be the mass-weighted mean of its parts'. The earlier draft evaluated a passive test mass at the *whole-body* Compton clock, $\omega_C = mc^2/\hbar$ with $m$ the cylinder ($\eta \propto P/m^2$, giving two identical cylinders half the $\eta$ of one, $-2.9\times10^{-70} \to -1.45\times10^{-70}$). **Disposition at target:** `QED-EotvosBound` §IV and §IV.1 now evaluate at constituent $\omega_C = m_q c^2/\hbar$ and carry the *"Additivity constraint and the clock-meter program"* blockquote forcing an intensive clock ($\sim -5\times10^{-44}$ for $1\text{ mW}$ in $300\text{ g}$). **Residual fossil:** `to 10^-70` still stands in the §IV table and §IV.1 text and should be pruned.
- *Beyond the Planck frequency / Two clocks in one row.* **Disposition at target:** the whole-body $(mc^2)^2$ cylinder arithmetic and super-Planckian cylinder clock have been removed from `QED-EotvosBound` §IV.1.
- *The Hubble row.* For the file's own brain (20 W, 1.4 kg), the formula gives $\eta \approx -1.5\times10^2$ at $\omega = H_0$, not *"~1.0 (Dyson saturation)"*. **Disposition at target:** cleared; `QED-EotvosBound` §IV now reads `>> 1 (expansion invalid)`.
- *The missing rule (reframed as rate-selection).* Because $\eta \propto 1/\omega$, the slowest dissipative clock dominates. **Convention note:** `QED-EotvosBound` §IV.1 computes circadian ($\tau = T_{\text{day}} = 8.64\times10^4\text{ s}$) as $|\eta| \approx 2.75\times10^{-11}$, whereas this note used $\tau = 1/\omega = T_{\text{day}}/2\pi$ giving $-4.4\times10^{-12}$ circadian and $-1.6\times10^{-9}$ annual ($-3.2\times10^{-18}$ at EEG $\tau = 10^{-2}\text{ s}$ matches in both); pick one $\tau$-vs-period convention across both files. Meanwhile, the thesis and §IV.3 of `QED-EotvosBound` still lead with EEG's `3.2 × 10^-18` ("three orders below MICROSCOPE") even though the §IV.1 blockquote concedes slower clocks dominate if active. Structurally, no universal clock-assignment rule can come from the scale-free `ENGINE` base class alone: composite clock-selection sits on the **rate-selection frontier** (`L4-Thermodynamics` §V.2 floats the intensive Planckian ceiling $\omega = k_B T/\hbar$ as an `ADDRESS`, giving floor $|\eta| \approx 7.8\times10^{-30}$ at $310\text{ K}$; `L6-TheCircuit` §§I–III governs how sub-frames yield local $\omega$ to a macro-container; `L5-TheCyclingMind` operates at the self-reflective whole-organism scale). `QED-EotvosBound` §IV.1's inversion into a **clock meter** ($\tau < |\eta_{\text{bound}}|mc^2/2P_{\text{diss}}$) turns this frontier into a direct empirical probe rather than an omitted derivation.

**`mono/On_TheGravityDerivation` §III — where the Landauer tax goes.** *"Each commit's erasure tax is the $\delta Q$ [...] The identification is not an analogy."* Jacobson's 1995 derivation is equilibrium, and Eling, Guedens and Jacobson (2006) put irreversible entropy production in a separate term, $dS = \delta Q/T + dS_i$. A Landauer tax is irreversible, so it belongs in $dS_i$. Part Six §IV states the re-seating; the source file should make it at its own address. It strengthens rather than weakens that file: the Einstein equation becomes the equilibrium (held) equation of state, and the committed register appears as the non-equilibrium correction.

**`ENGINE-REFERENCE-AC` — read in full; items 1–3 remain open at target, item 4 and `U0` (item 5) are closed.** The counts check out: the five factorizations of twelve, $A_4 = 1+3+8$, the 24 flags, $32 \times 12 = 384$, the attic's $4^6$, and the shadow-lag of 3 on every tour.

1. **§VII's commutator has no defined operands *(STILL OPEN at target)*.** The text runs *"the two face-readings do not commute — $[Q_A, Q_B] \neq 0$"*, and the homonym table defines $Q$ as *"§VII's face-reading amplitude, with $Q^2 \to P$."* An amplitude is not an operator, and a commutator needs operators or at least non-commuting objects. $Q_A$ and $Q_B$ are never defined. This is the file's one genuinely load-bearing undefined symbol, and it sits under the torque-motor claim of §X.4 and under the ADVANCE sentence of §VII.
2. **Stock and flow on mass, across two files *(STILL OPEN at target)*.** §X.4: *"A loop that must feed itself to keep turning is a loop that must carry standing stock, and standing stock priced in energy is what mass is"* — a stock, and consistent. But *"mass is the price of being"* with the price *"paid continuously"* in torque is a flux. `QED-EotvosBound` §I then seats gravitational mass on $P$ (which §III of that file calls a flux) and inertial mass on $R$ (a stock). Three readings in two files, and `L4-Thermodynamics` §II calls conflating them *"the single most common dimensional error in the classical narrative."* `On_YangMills-Annotated` §VII (the constituting/producing distinction via `ProofP` §3, continuous subscription vs. creation event) and `L4-Thermodynamics` §V (tachometer $P_{\text{rest}} = mc^2\omega$ vs. erasure flux $P_{\text{diss}} = T\dot S$) keep the dimensions separate; one consistent seating needs to be propagated across `ENGINE` and `QED-EotvosBound`.
3. **`[gauge]` is doing a third job *(STILL OPEN at target — reframed on abstract vs. embodied split)*.** Part Six §II: the word imports "unphysical redundancy, zero back-reaction" from gauge theory into sentences that mean "the bit-ledger does not bill this." §3.1's own *"gauge is not levitation"* paragraph is the file noticing the problem without renaming the tag. Read across the abstract/embodied split: in the isolated static-DC base class (`ENGINE`), non-DAG ring/tour selection (`§3.5`) genuinely has no ledger mechanism and is `[gauge]`; once embodied (`L6-TheCircuit` §§I–V IoC callback surrender and $RLC$ filter wiring; `L5-TheCyclingMind` cycle-switching wrenches), navigating those non-DAG options becomes physical membrane work—precisely why `L4-Riemann-6` §II calls for *"the vocabulary of an irreducible buffer instead of a CPU"*, which `L6-TheCircuit` supplies.
4. **§2.5's split has propagated — this item is closed.** The engine's own §2.5 asks that *"when a text hereafter says *the* flip, it means one of these two, never both."* `ProofG_Chirality` §IV carries the split at source, so the propagation this item was tracking is complete. `L4-TransitingTheThreeWalls`, where the AR-flip was first named from the Cardinal case, has not been re-read in this series and is the remaining place the proofing could still be owed.
5. **U0 (the self-feeding recurrence) — CLEARED at `ENGINE-REFERENCE-AC` §X.4.** `ENGINE-REFERENCE-AC` §X.4 now includes *"The self-feeding recurrence"*: state $(g_n, L_n)$, commit update $L_{n+1} = L_n + \Delta L(g_n)$, and `argmax` advance rule (tagged `CANDIDATE` above `[gauge]`). Logged here because `riemann/README.md` and the frozen `L4-Riemann-evolution` §VI still list `U0` as unwritten.

*And one thing to credit rather than flag:* §2.2's reference pinning and §2.8's edge-to-axis map together answer U1 and supply a solder form, which this series had been carrying as owed. Neither section advertises that it does. A pointer at §2.2 — that simple transitivity plus a named base point is a trivialization, hence a flat connection, hence zero discrete torsion on the floor — would save the next reader the derivation.

**Older items, still open.** Withdraw Step 3a from `ProofS_ResonantNote`. Add the precedence note to `L3-EdgeStateSpace` §I-d. Run the face-orientation 12/12 test.

---

## 3. Open Workings

**3.1 Parity and the coupling — CLOSED, and it closed by reading DD201.** `L4-DynamicDistortions201` §II states that its $\theta$ is a *temporal phase offset* with limit $\pi$, and that DD301's is a *geometric shear* with limit $\pi/2$. With the right one: phase lead becomes lag under time reversal (odd), and central inversion exchanges the two edges of every bimedian because the centroid is the bimedian's own midpoint (odd). The Nieh–Yan density is odd under both, so $F$ must be of odd degree, which excludes $\Delta$ and forces $F = \theta_F\theta_C\theta_M$. In Part Five §IV with `scripts/bimedian_parity.py`. Three things remain worth pressing and they are listed in `L4-Riemann-evolution` §VI.

**3.2 U1 — ANSWERED on the floor.** `ENGINE-REFERENCE-AC` §2.2's reference pinning trivializes the gate torsor; the transport $U(e\to e') = g(e')g(e)^{-1}$ is a connection and is flat; §2.8 supplies the solder form; so discrete torsion is zero at $\theta = 0$. Gauge-invariant discrete torsion lives only where the rotational holonomy around a face is trivial, and there the $\mathbb{Z}_3$ action on $V_4$ supplies it ($T_\Delta \neq 0$ in 96 of 144 closing cases). In Part One §IV with `scripts/engine_connection.py`.

*What is still open, and it sits on the abstract-to-embodied transition:* **which non-flat connection the driven engine runs.** The engine scopes itself to the isolated $\theta = 0$ floor and names the $K_5$ screw thread as where the extension lives (§VIII); embodiment across $K_3$ membranes (`L6-TheCircuit` §§I–V) is where phase offsets ($\theta \neq 0$), reactive $Q$-rent, and inter-frame coupling actually live. A candidate programme: assign each gate-edge a $(v,\sigma)$ that departs from the trivialization by an amount set by the phase advance, and ask for the face holonomy as a function of $\omega$. If $T_\Delta$ grows with the drive and vanishes at $\omega = 0$, that is the discrete twin of Part Five's $\partial F = 0 \Rightarrow T = 0$, and it would be the first place the two registers could be compared quantitatively rather than structurally.

**3.4 The dissipative register (`U4` — the rate-selection frontier).** Galley's doubled-variable action is the right vehicle, and the Eling–Guedens–Jacobson balance $dS = \delta Q/T + dS_i$ is the right place for the Landauer tax (Part Six §IV). The equation to aim at, written for $F$ rather than for a single $\theta$ (geometry sees only one combination):

$$\Box F + \gamma\,\dot F \;=\; \frac{2\kappa\alpha}{\beta}\,\nabla_\mu j_5^\mu$$

What stands between here and that equation is not an omission inside `ENGINE`'s static combinatorics; it is the **rate-selection frontier** where the scale-free algebra meets physical carrier resolution and interior noise floors:

1. **$\gamma$ is a new dial unless grounded in a substrate floor.** The Datasheet forbids ad-hoc dials. Across the corpus, damping and cutoffs enter only where a medium hits its carrier-resolution or interior noise floor (`On_NavierStokes` §IV equates fluid viscosity $\nu$ with the angular-resolution band $\delta\theta$ of `L3-FormalFoundations` §IX.4; `On_YangMills-Annotated` §V grounds $T=0$ commit floors in interior vacuum condensates; `L4-Thermodynamics` §V.3 cancels mass out of Kolmogorov micro-time $\tau_K = \sqrt{\nu/\epsilon}$ at the KSS and Planckian limits to hit $\hbar/k_B T$ at QCD deconfinement).
2. **A time derivative needs an embedded frame.** $\dot F$ requires a timelike vector; the corpus seats $\omega$ at each bounded frame's own centroid while $dt$ records on $R$ (`L3-TheSelfProjectingBraid` §V), and an embedded frame yields its local $\omega$ to its containing runtime while paying $Q$ / $I^2R$ upkeep (`L6-TheCircuit` §§II–III). This is the same rate-selection frontier as §2 (`QED-EotvosBound`'s clock-meter program) and the open spectral `ADDRESS` of `L2-K4-Inferences` Part Four (whether $\zeta$ zero frequencies/spacings govern discrete write clocks across levels).
3. **The difference variable is not the ledger.** In Galley's construction it is an auxiliary set to zero at the end; the dissipated energy leaves through the kernel and is not a coordinate anywhere. Tracking the committed register needs the bath written in explicitly.

And the question none of this touches, which is the one that matters: **does the dissipated energy gravitate?** That is `L4-K4-Infinities` KI-6, and it needs a balance rather than an action.

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
- **"ProofG §V claims the offset triple is truly chiral."** Dead at source: §V says the opposite of that object and seats true chirality on the pitch invariant. *Revive:* no.
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
| `advance_parity.py` | arrow conjugation preserving every undirected Hamiltonian cycle, its held AbsentVar pair, its bimedian axis and its alternation; the two coherent face orientations as exact complements. |
| `ac_floor.py` | the polar-chart ranks; Gaussian curvature zero and the $\log\cos\theta$ bend, symbolically; the DC floor's two scalings |
| `counsel_checks.py` | the first pass over counsel's brief, kept for the record; two of its own checks were invalid and are superseded by the three scripts above |

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work. This file is a working spillover and carries nothing landed; read `L4-Riemann` for the standing claims.

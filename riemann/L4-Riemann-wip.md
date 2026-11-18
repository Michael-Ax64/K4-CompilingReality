# L4-Riemann-wip
## Working Notes, Open Flags, Quarantine, and the Numbers

*Companion to `L4-Riemann`. Writing discipline is loosened here: first-person notes are allowed, speculation is allowed where it is marked, and material is kept because losing it would cost more than keeping it. Nothing here is landed. The parent and the parts carry the standing claims; `L4-Riemann-evolution` carries the history.*

---

## 0. Scope and Framing

Four jobs: **open flags** for sibling files, **open workings**, **quarantined** readings, and the **script map**. Once a sibling flag is verified cleared at its target, it drops from here; closed withdrawals and port history live in `L4-Riemann-evolution`.

Two structural distinctions govern how items in §§1–2 are read:
* **Abstract DC vs. embodied AC:** `ENGINE-REFERENCE-AC` specifies the isolated, autarkic Floor-3 base class ($\theta = 0$, non-embedded, `[gauge]` selection). Inflating that class into physical, computational, or biological hosts (`BENDING_SPACE`, `BENDING_MINDS`, `L6-TheCircuit`, `L5-TheCyclingMind`) replaces unconditioned `[gauge]` freedom with host constraints—clock surrender under Inversion of Control (`L6-TheCircuit` §§I–III), membrane $RLC$ filter wiring (`L6-TheCircuit` §V), and cycle-switching wrenches (`L5-TheCyclingMind`).
* **Rate-selection as an interface frontier:** Because the $K_4$ grammar is scale-free (`L4-ScalingInvariants`), it fixes dimensionless closure and a **1-bit minimum excitation step** (`On_YangMills-Annotated` §X) while leaving absolute operating rate ($\omega$) and unit bit-price to the substrate's carrier-resolution and interior noise floors—precisely where the framework encounters quantum Yang–Mills (`On_YangMills-Annotated` §V), coherent Navier–Stokes cascades (`On_NavierStokes` §§IV–V; `L4-Thermodynamics` §V.3), and the $\zeta$ prime-writing dipole spectrum (`L2-K4-Inferences` Part Four, `ADDRESS`).

---

## 1. Open Flags for Other Files

Open items at external addresses, each awaiting repair at its owner file.

**`L4-K4-Infinities-1` Part One §VI — the Laue overstatement check.** `L4-K4-Infinities` (parent summary) already narrows Laue's theorem to integrated spatial stresses while leaving angular momentum and nuclear spin intact per takehome rule 6. `L4-K4-Infinities-1` Part One §VI remains to be verified at source for the un-scoped wording (*"returns a number and discards the orientation"* / *"One scalar survives. Every vector and tensor component is annihilated"*).

**`QED-EotvosBound` — remaining cleanups and the rate-selection frontier.** Computed in `scripts/mirror_and_eotvos.py`.
- *Residual `10^{-70}` fossil.* `QED-EotvosBound` §IV and §IV.1 now evaluate passive test masses at the intensive nucleon Compton clock ($\omega_C = m_q c^2/\hbar$, giving $|\eta| \approx 5\times 10^{-44}$ for $1\text{ mW}$ leakage in $300\text{ g}$), and the super-Planckian cylinder arithmetic has been removed; however, `to 10^-70` still stands in the §IV table, §IV.1 text, and header.
- *Mass stock vs. flux in §I.* §I item 1 defines gravitational mass on $P$ as *"the accumulated volume of completed actualizations"* (stock), whereas §III writes $[P]/[R] = \text{s}^{-1}$ with $P$ strictly as flux ($P_{\text{rest}} = mc^2\omega$, $P_{\text{diss}} = T\dot S$) and $R$ as inertial stock. Align §I item 1 to compilation flux via `L4-Thermodynamics` §V.
- *Cycle-time convention and EEG lead.* §IV.1 computes circadian $|\eta| \approx 2.75\times 10^{-11}$ using $\tau = T_{\text{day}} = 8.64\times 10^4\text{ s}$ (whereas $\tau = T_{\text{day}}/2\pi$ gives $-4.4\times 10^{-12}$ circadian and $-1.6\times 10^{-9}$ annual; EEG $\tau = 10^{-2}\text{ s}$ gives $-3.2\times 10^{-18}$). State $\tau = T$ explicitly in §III.2, and keep the thesis and §IV.3 scoped as a single-band EEG benchmark rather than the biological ceiling while slower clocks remain open.
- *Rate-selection frontier.* Composite clock assignment sits where the scale-free grammar meets physical resolution floors (`L4-Thermodynamics` §V.2 puts the intensive Planckian floor $\omega = k_B T/\hbar$ at $|\eta| \approx 7.8\times 10^{-30}$ for $310\text{ K}$, `ADDRESS`; `L6-TheCircuit` §§I–III governs embedded clock surrender; `L5-TheCyclingMind` runs at the whole-organism scale), probed operationally by §IV.1's clock-meter bound $\tau < |\eta_{\text{bound}}|mc^2/(2P_{\text{diss}})$.

**`ENGINE-REFERENCE-AC` — open seams and cross-links.**
1. **§VII's commutator has no defined operands.** The text reads *"the two face-readings do not commute — $[Q_A, Q_B] \neq 0$"*, and the homonym table defines $Q$ as *"§VII's face-reading amplitude, with $Q^2 \to P$."* $Q_A$ and $Q_B$ lack operator definitions; §X.4's load update $(g_n, L_n)$ carries the defined order dependence (COMMIT updates $L_n$ before ADVANCE reads $L_{n+1}$).
2. **Stock and flow on mass across `ENGINE` §X.4 / §XIII and `QED-EotvosBound` §I.** `ENGINE` §X.4 pairs *"standing stock priced in energy is what mass is"* with *"paying continuously"* in torque (§XIII), while `QED-EotvosBound` §I seats gravitational mass on $P$ (flux in §III of that file and `L4-Thermodynamics` §II) and inertial mass on $R$ (stock). Separate standing stock ($mc^2$) from holding flux ($P_{\text{rest}} = mc^2\omega$) across both files via `L4-Thermodynamics` §V and `On_YangMills-Annotated` §VII.
3. **`[gauge]` is doing a third job.** Part Six §II notes the word imports "unphysical redundancy, zero back-reaction" from gauge theory into sentences meaning "unbilled by the $\theta = 0$ bit-ledger" (§3.1 *"gauge is not levitation"*). Clarify `[gauge]` as isolated base-class ledger-exemption (`ENGINE` §3.5), distinct from embodied ring-switching across `L6-TheCircuit` §§I–V membrane filters and `L5-TheCyclingMind` wrenches.
4. **`L4-TransitingTheThreeWalls` §IV propagation.** §IV still calls $(P\,R)(I\,U)$ *"the AR-flip automorphism of the $V_4$ symmetry group"* without scoping it as the **Cardinal** family's even $V_4$ twin-step (an automorphism of the matching structure rather than of the twelve equations, `ProofS_ResonantNote` §II, and distinct from the odd $C_2$ handedness flip, `ENGINE` §2.5).
5. **Pointer at §2.2 and §2.8.** Neither section yet notes that simple transitivity plus the $P \to U$ reference edge supplies a flat trivialization ($T_\Delta = 0$ on the $\theta = 0$ floor) and §2.8 supplies the discrete solder form (`L4-Riemann-1` §IV).

---

## 2. Open Workings

**2.1 Driven discrete connection ($\omega > 0$).** `ENGINE-REFERENCE-AC` scopes itself to the isolated $\theta = 0$ floor (where canonical transport is flat and $T_\Delta = 0$) and names the $K_5$ screw thread as the extension (§VIII); embodied frames couple across $K_3$ membranes with non-zero phase lag (`L6-TheCircuit` §§I–V). Candidate programme: assign each gate-edge a $(v,\sigma) \in V_4 \rtimes \mathbb{Z}_3$ departing from the trivialization by an amount set by phase advance, and test whether face holonomy $T_\Delta(\omega)$ grows with the drive and vanishes at $\omega = 0$—the discrete twin of Part Five's $\partial F = 0 \Rightarrow T = 0$.

**2.2 The dissipative register (`U4` — the rate-selection frontier).** Galley's doubled-variable action and the Eling–Guedens–Jacobson balance $dS = \delta Q/T + d_iS$ seat the irreversible Landauer tax outside conservative single-action variation (Part Six §IV). Target equation, written for $F = \theta_F\theta_C\theta_M$ (the single combination geometry sees):

$$\Box F + \gamma\,\dot F \;=\; \frac{2\kappa\alpha}{\beta}\,\nabla_\mu j_5^\mu$$

Three open blockers define the working:
1. **$\gamma$ without an ad-hoc dial.** The Datasheet bars fitted dials. Across the corpus, damping and cutoffs enter only where a medium hits its carrier-resolution or interior noise floor (`On_NavierStokes` §IV equates fluid viscosity $\nu$ with the angular-resolution band $\delta\theta$ of `L3-FormalFoundations` §IX.4; `On_YangMills-Annotated` §V grounds $T = 0$ commit floors in interior vacuum condensates; `L4-Thermodynamics` §V.3 cancels mass out of Kolmogorov micro-time $\tau_K = \sqrt{\nu/\epsilon}$ at the KSS and Planckian limits to land at $\hbar/k_B T$ at QCD deconfinement).
2. **Frame vector for $\dot F$.** $\dot F$ requires a timelike vector; the corpus seats $\omega$ at each bounded frame's centroid while $dt$ records on $R$ (`L3-TheSelfProjectingBraid` §V), and embedded frames yield local $\omega$ to a containing runtime while paying $Q$ / $I^2R$ upkeep (`L6-TheCircuit` §§II–III). This shares the same rate-selection frontier as §1 (`QED-EotvosBound`'s clock-meter program) and the spectral `ADDRESS` of `L2-K4-Inferences` Part Four (whether $\zeta$ zero frequencies/spacings govern discrete write clocks across levels).
3. **Explicit bath vs. auxiliary variable.** In Galley's construction the difference variable is an auxiliary set to zero at the end, leaving dissipated energy outside the coordinate ledger; tracking the committed register requires an explicit bath.

Separate balance question: whether dissipated energy gravitates (`L4-K4-Infinities` KI-6).

**2.3 AC 50-equation enumeration.** The AC core (`S = \hat U\hat I^*, \hat U = Z\hat I`) doubles the rank-2 floor in polar coordinates and bends it in rectangular coordinates via $\log\cos\theta$ and additive impedances (Part Two §I; `scripts/ac_floor.py`). Enumerating and ranking the full fifty-equation set in `L3-Electro-AC-db` to count its independent relations remains open.

**2.4 The class-side tear and host orientability.** `Q16-ChiralMeshSpacetime` KM-1 reads the configuration where all four faces circulate alike as tearing the class boundary, whereas a torsion-free manifold does not tear. A direct map from face-reading bookkeeping to a geometric invariant that shifts when the torsion three-form turns on—using Part One §IV's flat trivialization at $\theta = 0$—remains open.

**2.5 Population distributions and offset energy.** With $F = \theta_F\theta_C\theta_M$ invariant under $A_4$ and $S_4$ and vanishing only under inversion, three physical questions remain open: what distribution of phase-offset configurations physical populations carry, whether spin polarization breaks inversion symmetry in the required sense, and whether offset energy sits in the reactive channel or pays a commit tax on change.

---

## 3. Quarantine

**The Cardinal floor and classical electromagnetism.** Part Two §III notes that the floor's harmonic pencil privileges the Cardinal diameter and `L4-ThePlenum` §V puts the medium's wave-to-constitutive swap there. Offering that alignment as an explanation for classical electromagnetism's fit closed on the first pass using material already in the house (`L4-K4-Infinities-wip` §6.2); moving it out requires a second, independent checkable consequence of standing on Cardinal.

**The AR-flip as a charge conjugation.** Reversing the Active/Reactive bit on both mate pairs simultaneously resembles charge conjugation. Analogy only—and `ENGINE-REFERENCE-AC` §2.5/U8 shows the AR-trade fits 8 of 12 twin-steps while Fixed trades within charge class, so even as an analogy it is family-specific.

**$\Delta\cdot\theta_F$, odd under two named mirrors.** Odd under $(P\,U)$ and under the Cardinal twin-step, but also odd under the proper rotation $(P\,I)(U\,R)$, so it transforms by no natural character of $A_4$. Although degree 7 passes time reversal, it fails carrier symmetry.

**$\theta \approx 31°$.** Single CHSH value pushed through `L4-DynamicDistortions301`'s envelope; an illustration of method, not a universal shear.

---

## 4. Struck, With What Would Revive Each

- **The burnt-sign reading of the metric.** Dead on Hamiltonian mechanics (squaring in $p^2/2m$ erases nothing because sign is carried in phase space). *Revive:* never as stated; Part Four §VI retains the projection result.
- **$I \leftrightarrow R$ or $U \leftrightarrow R$ as time reversal.** Dead: pole transpositions are undirected. *Revive:* no.
- **Field average versus invariant as a way past the bounds.** Dead: cannot carry an observable between bundles. *Revive:* no; the action places offsets in the bounded channel.
- **The AR-flip as spatial parity.** Dead twice over: $(P\,R)(U\,I)$ is an even rotation of the solid, and per `ENGINE-REFERENCE-AC` §2.5 it is the Cardinal family's twin-step rather than a wholesale mirror. *Revive:* no.
- **$F = \Delta$ (option A), the sixth-order coupling.** Dead on time reversal: even degree cannot be odd under $\vec\theta \to -\vec\theta$. *Revive:* only if `L4-DynamicDistortions201`'s $\theta$ were time-reversal-even, which would kill parity-clean Nieh–Yan couplings at every degree.
- **"The engine does not supply the connection data."** Dead: `ENGINE-REFERENCE-AC` §2.2 supplies the trivialization ($g(e')g(e)^{-1}$); the negative test applied to gate labels rather than transport. *Revive:* no.
- **"`ProofG` §V claims the offset triple is truly chiral."** Dead at source: `ProofG_Chirality` §V designates the offset triple falsely chiral and seats true chirality on the two-factor pitch invariant. *Revive:* no.
- **The whole-body Compton clock for passive matter (`QED-EotvosBound`).** Dead on mass additivity. *Revive:* only with an argument that $\eta$ is not a ratio of additive masses.

---

## 5. Superseded Files

`mono/On_TheRiemannFreeze.md`, `mono/On_TheRiemannFreeze-TheAction.md`, and `mono/On_TheRiemannFreeze-Submission.md` are superseded by `L4-Riemann` and left untouched pending retirement (`L4-Riemann-evolution` §III indexes the fossils they still carry). If kept on disk, they require a one-line pointer to `L4-Riemann` at their heads.

---

## 6. The Numbers

Every figure in `L4-Riemann` and Parts One–Six comes from one of these scripts in `scripts/`:

| Script | Produces |
|---|---|
| `torsion_action.py` | $R(\Gamma)$ coefficients $-\tfrac23, \tfrac32, \tfrac12$, no cross terms; channel health; inert demanded term; sphere sign check; phase offsets as standard representation of $S_4$, character $(3,1,-1,0,-1)$; invariants and Molien series; charge stabilizer |
| `parity_candidates.py` | the parity table of Part Five §IV |
| `aggregate_parity.py` | the averaging table of Part Five §V |
| `aggregate_check.py` | racemic/homochiral averages (geometric mirror only) |
| `flat_vs_solid.py` | four relation lines, one per face; rank 2 (log, real) against closure rank 3 (GF(2)); cross-ratios $-1$, $\tfrac12$, $\tfrac12$; three-form component counts 0, 1, 4 |
| `dc_logspace.py` | rank 2; only the identity permutation preserves the plane |
| `mirror_and_eotvos.py` | the twin-step's action on the offsets; the `QED-EotvosBound` additivity and clock checks |
| `bimedian_parity.py` | inversion exchanging each bimedian's two edges; $T_d$ character of $\vec\theta$ against $(x,y,z)$; parity/time-reversal table forcing $F = \theta_F\theta_C\theta_M$ |
| `engine_connection.py` | `ENGINE-REFERENCE-AC` §2.2 as a trivialization; flatness of canonical transport; gauge action on translational holonomy; §2.8 solder form round the cube's squares |
| `advance_parity.py` | arrow conjugation preserving every undirected Hamiltonian cycle, its held AbsentVar pair, its bimedian axis, and its alternation; the two coherent face orientations as exact complements |
| `ac_floor.py` | polar-chart ranks; Gaussian curvature zero and the $\log\cos\theta$ bend, symbolically; DC floor's two scalings |
| `counsel_checks.py` | first-pass brief checks (superseded on parity, connection, and AC floor by `bimedian_parity.py`, `engine_connection.py`, and `ac_floor.py`) |

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work. This is a working spillover and carries nothing landed; read `L4-Riemann` for the standing claims.

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

**`L4-DynamicDistortions301` §VII.B — dipole-label alignment with `L4-DynamicDistortions-Sudoku` §0.** `L4-DynamicDistortions-Sudoku` §0 anchors the dipole names to `L3-EdgeStateSpace`'s Kernel Rule (`Fixed {P–U, I–R}` / Apeiric Field, `Cardinal {P–R, I–U}` / Isotropic Pole, `Mutable {P–I, U–R}` / Conservative Field). `L4-DynamicDistortions301` §VII.B still lists the `{P–U, I–R}` dipole under *Cardinal* and `{P–R, I–U}` under *Fixed*, opposing its own §I and `Sudoku` §0.

---

## 2. Open Workings

**2.1 Driven phase-fibered connection ($\omega > 0$).** 
Every element of $A_4 = V_4 \rtimes \mathbb{Z}_3$ has finite order in $\{1, 2, 3\}$, so a purely discrete $(v, \sigma) \in A_4$ cannot grow continuously from zero as $\omega$ turns on. 
Extending `ENGINE-REFERENCE-AC` from its flat $\theta = 0$ floor ($U_0(e \to e') = g(e')g(e)^{-1}$, $T_\Delta = 0$) to embodied frames coupled across $K_3$ membranes (`L6-TheCircuit` §§I–V; `L3-Electro-AC-db`) requires a hybrid fibered connection—dressing the flat $A_4$ base with a continuous reactive phase fiber $e^{j\theta_e(\omega)} \in U(1)$ (`L4-K4-Infinities` KI-4 $\mathrm{Spin}^c$ / $2T$ lift). 
At $\omega = 0$, $\theta_e = 0$ returns flat $U_0$; for $\omega > 0$, face phase-holonomy $\Phi_\Delta(\omega)$ grows continuously (the discrete counterpart of Part Five's $\partial F \neq 0$) and crossing `L4-DynamicDistortions-Sudoku` §V's $\pi$-threshold triggers discrete $V_4$ half-turn holonomy jumps ($T_\Delta \in V_4 \setminus \{0\}$). 
Building and scanning that hybrid connection extends `scripts/engine_connection.py`. 
`L4-K4-Infinities-3` §V already executes the $A_4 \to 2T \subset SU(2)$ lift over the 24 equal Haar cells of $S^3$, while `L4-K4-Infinities-2` §VI separates intra-cell $2T \times_{\mathbb{Z}_2} U(1)$ holonomy from inter-instance medium Wilson loops $W = \tfrac{1}{2}\mathrm{Tr}(g_{CA}\circ g_{BC}\circ g_{AB})$. 
Keep this intra-cell $2T \times_{\mathbb{Z}_2} U(1)$ construction distinct from the inter-instance $\mathrm{Spin}^c$ Wilson loop $W = \tfrac{1}{2}\mathrm{Tr}(g_{CA}\circ g_{BC}\circ g_{AB})$ in `L4-K4-Infinities-2` §VI (where native $\mathbb{Z}_2$ spinor holonomy rides on $N_*(-Z) = N_*(Z)$ and $Z_0 = 2\alpha R_K$, while non-commuting port states $[Z_A, Z_B]$ do not by themselves establish $W \neq 1$ across disconnected openings).


**2.2 The dissipative register (`U4` — explicit bath and rate-selection frontier).** 
Galley's doubled-variable action and the Eling–Guedens–Jacobson balance $dS = \delta Q/T + d_iS$ seat the irreversible Landauer tax outside conservative single-action variation (Part Six §IV). 
Target equation for $F = \theta_F\theta_C\theta_M$:

$$\Box F + \gamma\,\dot F \;=\; \frac{2\kappa\alpha}{\beta}\,\nabla_\mu j_5^\mu$$

The open formal step separates cleanly from the physical rate-selection frontier:

1. **Formal step (explicit bath $\mathcal{B}$):** In Galley's construction the difference variable $\theta_-$ vanishes on the physical trajectory, hiding dissipated energy in the non-conservative kernel. Tracking the committed register requires an explicit coupled bath $\mathcal{B}$ (the $Q$ / $I^2R$ container upkeep of `L6-TheCircuit` §§II–III) feeding $d_iS > 0$. `L4-K4-Infinities-3` §III's candidate Laue-to-quadrupole relation ($N_{\text{bits}}\cdot k_B T \ln 2 \overset{?}{=} \tfrac{1}{2}|\ddot I^{ij}|$) is the candidate target for what the bath funds; per `L4-Thermodynamics` §V.1/V.3 and `L4-K4-Infinities-3` §§III, VI, bit-vs-nat ($\ln 2$) bookkeeping must stay explicit across the bath and horizon registers.
2. **Frontier parameters ($\gamma$ and frame clock $\dot F$):** Under the Datasheet, $\gamma$ cannot enter as a new dimensionless dial. 
Writing $\gamma = \tau_{\text{diss}}^{-1}$ as a Category-2 / substrate relaxation rate seats both $\gamma$ and the centroidal timelike vector (`L3-TheSelfProjectingBraid` §V) directly on the **rate-selection frontier**: Planckian and KSS micro-time $\tau_K \sim \hbar/k_B T$ at thermal/QCD deconfinement (`L4-Thermodynamics` §§V.2–3), interior vacuum condensates at $T = 0$ (`On_YangMills-Annotated` §V), carrier resolution $\nu \leftrightarrow \delta\theta$ (`On_NavierStokes` §IV; `L3-FormalFoundations` §IX.4), the `QED-EotvosBound` §IV.1 clock-meter bound ($\tau < |\eta_{\text{bound}}|mc^2/(2P_{\text{diss}})$), and the open spectral `ADDRESS` of $\zeta$ zero spacings (`L2-K4-Inferences` Part Four).

Separate balance bet: whether $d_iS$ energy gravitates (`L4-K4-Infinities` KI-6).

**2.3 Physical $\nabla F$ and $\langle F\rangle$ profiles.** 
Held phase offsets sit in $H_{\text{incoh}}$ (conservative/reactive), paying Landauer tax only across `.observe()` commits into $H_{\text{coh}}$, and alternating domain or face rotations act inside $A_4$—canceling macroscopic spin moments ($\langle\mathbf{j}_5\rangle = 0$) while leaving $F = \theta_F\theta_C\theta_M$ invariant. 
Static spin polarization ($\hat P$-even, $\hat T$-odd) bounds $\nabla F$ and boosted components of $\dot F$ rather than breaking spatial inversion on uniform $F$ (Part Five §V). 
The remaining physical question is whether any real material population sustains a non-zero $\hat P$-odd, $\hat T$-odd inversion-biased mean $\langle\theta_F\theta_C\theta_M\rangle$ (coupled to $j_5^0$) or a coherent spatial gradient $\nabla F$.

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

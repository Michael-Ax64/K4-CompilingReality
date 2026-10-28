[![No Gravitons](https://img.shields.io/badge/No-Gravitons-red?style=flat-square)](./quantum/Q2-TransactionLayer.md)
[![No Dark Matter](https://img.shields.io/badge/No-Dark_Matter-red?style=flat-square)](./QED-CCP.md)
[![No Minkowski Minus Sign](https://img.shields.io/badge/No-Minkowski_Minus_Sign-red?style=flat-square)](./ProofN_BiquaternionBridge.md)
[![No Hard Problem](https://img.shields.io/badge/No-Hard_Problem-red?style=flat-square)](./L0-Introduction.md)
[![No Unified Field](https://img.shields.io/badge/No-Unified_Field-red?style=flat-square)](./QED-TwoBranchMinting-Lecture.md)
[![No Stamper](https://img.shields.io/badge/No-Stamper-red?style=flat-square)](./L0-TheStampAndTheDie.md)
[![No Homo Economicus](https://img.shields.io/badge/No-Homo_Economicus-red?style=flat-square)](./L4-Economics.md)
[![No RLHF](https://img.shields.io/badge/No-RLHF-red?style=flat-square)](./ProofA_Panopticon.md)
[![No Clock Time](https://img.shields.io/badge/No-Clock_Time-red?style=flat-square)](./ProofO_HelicalTime.md)
[![No Plane Causality](https://img.shields.io/badge/No-Plane_Causality-red?style=flat-square)](./ProofB_LogoicFracture.md)
[![No Nonsense](https://img.shields.io/badge/No-Nonsense-critical?style=flat-square)](./llm.md)
[![No Antigravity](https://img.shields.io/badge/No-Antigravity-critical?style=flat-square)](./quantum/Q12-NotAntigravity.md)


[![Mass Gap = Mass is Containment](https://img.shields.io/badge/Mass_Gap-Subscription-green?style=flat-square)](./mono/On_YangMills.md)
[![NS Wall = Substrate Floor](https://img.shields.io/badge/NS_Wall-Substrate_Floor-green?style=flat-square)](./mono/On_NavierStokes.md)
[![Four Faces, Addressable](https://img.shields.io/badge/Four_Faces-Addressable-green?style=flat-square)](./L2-RotatingTheTetrahedron.md)
 
 
# Compiling Reality
## The Algebra of Four-Fold Distinction

> `relational algebra` · `K4 topology` · `thermodynamics of information` · `LLM alignment` · `phase dynamics` · `biquaternion star-norm` · `Markov blanket` · `active inference` · `Landauer principle` · `distributed coherence` · `tangent singularity` · `helical extrusion of time`

This repository studies one object: the complete graph on four vertices, carrying complex impedance, energized under alternating current. Everything else is consequence or application.

The claim is about minimum structure. Bounded interiority — being an inside distinguished from an outside — has a smallest form that supports it, and that form recurs wherever the condition is met. A point carries no relation. A dyad carries one and never closes. A triangle closes and bounds an area, but every point of it is reachable without crossing into anything; it has surface and no inside. The 3-simplex is the first structure that bounds a volume. And $K_4$ is the largest complete graph that still embeds in the plane — it sits exactly on the boundary between what can be drawn flat and what cannot, which for a study of interiors and exteriors is a theorem rather than an image.

The framework is adimensional by construction. It emits relational shape; the substrate supplies the scale. What it says is which relations carry a quantity, whether a transition squares or roots it, which pole it lands on. What it does not say is the number — and that refusal is load-bearing, not modest. A framework that derives a constant's digits is hostage to the next decimal place. One that derives only the relation is not (`L4-ScalingInvariants` §IX).

**Why a boundary subtracts.** A relation between two things splits into a part that does not care which you name first and a part that does. Projection keeps the first and discards the second. What cannot cross a boundary is therefore not an arbitrary list of quantities — it is orientation, and with it every magnitude defined relative to a unit on the far side. An interior is not sealed because it is small or complicated. It is sealed because it is oriented. The corpus works this out at `L4-DynamicDistortions301` §VI, where it also accounts for why $45^\circ$ recurs across unrelated files.

---

## Verify Something Before You Read Anything

Three checks, by hand, in about five minutes. They settle whether there is a well-defined object here before any interpretation is at stake.

1. **The twelve equations are complete and non-redundant.** Enumerate them. Find a thirteenth, or find a duplicate.

2. **In all eight division-forms, the numerator is always $P$ or $U$.** $I$ and $R$ never appear as a numerator. Confirm it or break it.

3. **Run `code/aut.lisp`.** It reports $|\mathrm{Aut}(\text{twelve})| = 8$, the group $D_4$, whose induced action on the four poles is exactly $V_4$. The twelve equations therefore see the Asserting/Yielding bit and are blind to the Active/Reactive bit — the algebra discriminates a mapping to 1-in-6, not 1-in-24.

If any of the three fails, say which and stop. That is a finding, and it is worth more here than agreement.

---

## The Join

The twelve equations are not twelve formulas taught serially. They are what happens when a closed three admits a properly orthogonal fourth.

Ohm's relation $U = IR$ is a closed system of three mutually-determining terms — complete, correct, and flat. Faraday supplies $P$, which is not derivable from it, because power carries energy per unit time and therefore brings time into an algebra that had none.

Ohm gives three permutations. Faraday gives three. Six in hand — but the joined system has twelve, and the six that are new belong to neither parent:

$$P = I^2R, \quad P = U^2/R, \quad R = U^2/P, \quad R = P/I^2, \quad I = \sqrt{P/R}, \quad U = \sqrt{PR}$$

They are characterised exactly. **The six bred equations are precisely those in which $P$ and $R$ appear together, and precisely those containing a square or a root.** The two sets coincide completely.

And the square is forced. The parents share exactly $U$ and $I$ and share neither $P$ nor $R$; to write any equation containing both $P$ and $R$, a shared variable must be eliminated, and since each parent holds it linearly, elimination squares the other shared one. So the squared operand is always a shared variable — the Yielding poles — and the equation produced always relates the unshared pair, the Asserting poles. The **Route Law** follows from variable overlap rather than being postulated (`L3-FormalFoundations` §I, `ProofQ_AlgebraicSyntax` §V).

The twelve hold simultaneously. Pin any two variables and the other two are fixed; no facet is available to be read in isolation. That property does work no single equation does — it puts a floor at zero on the ledger, and it serves downstream as a drift guard, since a state satisfying some relations while violating others is rejected rather than argued with.

The AC extension ($S = P + jQ$) is the dynamic instantiation of the same object. DC is the static one. The contrast between them is what the rest of the corpus runs on.

---

## Results, Sorted by Type

Claims are tagged by what they are. **Identity** — an exact algebraic relation. **Arithmetic consequence** — follows by counting or elementary algebra. **Derivation** — computed from committed rules within the framework. **Correspondence** — the elements map and the relations are asserted to carry across. **Conditional** — holds if a stated antecedent holds, which is itself open. **Refuted** — tested and killed, kept on the list so the kill stays visible.

**1. Pion-to-electron mass ratio** — *derivation, coefficients an open vote* (`L3-ConstitutiveAlpha`, `Q15`, `On_TheIsNessTax`)
$$\frac{m_\pi^\pm}{m_e c^2} = \frac{2}{\alpha} - \frac{3}{\pi} + 2\alpha = 273.13166$$
Agreement with measurement ($273.13244$) at $2.84$ ppm. The three-term *shape* is not chosen: it is Kirchhoff's loop law on a closed circuit in the $K_4$ atom — forward propagation edge, vertex-internal impedance drop, return edge — which fixes the orders $\alpha^{-1}, \alpha^0, \alpha^{+1}$ before any value enters. $2\alpha$ is the identity $Z_0/R_K$. The middle term computes as $-(3\cdot\frac{\alpha}{2\pi})(\frac{2}{\alpha}) = -\frac{3}{\pi}$, with the colour count imported from SU(3). The coefficients stay an open vote: the per-colour use of Schwinger's $\alpha/2\pi$ is owed, and among the $1332$ small-integer forms of the same shape a random target near $273$ finds one within $2.84$ ppm about $6\%$ of the time — this is the only one that hits. *Imports: $\alpha$, the SU(3) colour count. The seed integer 2 recovers Nambu's bare hadron-lepton relation.*

**2. Hubble horizon scale ratio** — *consistency check* (`QED-CCP`, `L4-DualConvergence`)
$$\frac{\rho_\Lambda}{\rho_P} = \frac{3\Omega_\Lambda}{8\pi}\left(\frac{\ell_P}{R_H}\right)^2 \approx 10^{-123}, \qquad \frac{\ell_P}{R_H} \approx 10^{-60.9}$$
The observed $10^{-123}$ is the Route Law square ($P = UI$) of the single linear scale-span between Planck length and Hubble radius, times a geometric factor $\sqrt{3\Omega_\Lambda/8\pi} \approx 0.29$. Setting $P = 10^{-123}$ and $R = 1$, Facets 6 and 9 force $U = I = \sqrt{PR} \approx 10^{-61.5}$, the scale of $\ell_P/R_H$ but not equal to it. *$P$ and $\Omega_\Lambda$ are inputs here; this is a check the framework passes on its native quantity, not a derivation of the cosmological constant.*

**3. Nuclear Landauer phase-burn rate** — *derivation of structure; its consumer refuted* (`Q17`)
$$\frac{E_{\text{bit}}}{k_B T_c} = \frac{\ln 2}{16\pi^2}$$
The Landauer bound normalized to the deconfinement temperature and passed through the one-loop factor, in dimensionless structural form. *Imports: $\ln 2$, $\pi$. Rendering it as $\approx 0.69$ MeV/bit needs $T_c \approx 156.5$ MeV as interface payload.* The claim the rate was built to serve — nuclear binding as an integer count of erased bits times one universal rate — is **refuted**: $B_t/B_d$, $B_{^3\text{He}}/B_d$ and $B_\alpha/B_d$ are not small-integer ratios, and the rate cancels from them.

**4. The deuteron's assimilated coordinate** — *measured coordinate; class law refuted* (`Q17`)
$$X_d = \pi^2\frac{B_d}{m_\pi^2c^2/2\mu} = 1.058\ (m_{\pi^\pm}),\quad 1.082\ (m_{\bar\pi}),\quad 1.132\ (m_{\pi^0})$$
The deuteron sits near $1/\pi^2$ of the pion kinetic scale; equivalently its size is about $\pi$ pion Compton wavelengths. The reading of $1/\pi^2$ as the law of shallow near-threshold states is **refuted**: the halo nuclei spread from $0.43$ to $1.23$ across it. What stands is the deuteron as the only bound two-nucleon channel, $X_d > 1$ under every pion choice, and two debts: the pion choice itself (the $1.058$ rests on the least defensible convention) and the nucleon-to-pion mass ratio, which bears load in the binding fraction and is not yet derived. *Imports: $\pi$, $m_N/m_\pi$.*

```python
from mpmath import mp, mpf, pi, sqrt, log
mp.dps = 15
alpha = 1/mpf('137.035999177'); me = mpf('0.51099895'); mpc = mpf('139.57039'); mp0 = mpf('134.9768')
print(2/alpha - 3/pi + 2*alpha, mpc/me)                         # 1: 273.131663  273.132440
lP = mpf('1.616255e-35'); c = mpf('299792458'); H0 = mpf('67.4')*1000/mpf('3.0857e22'); OL = mpf('0.685')
r = lP*H0/c; print(r, sqrt(3*OL/(8*pi)), 3*OL/(8*pi)*r**2)       # 2: 1.1776e-61  0.28595  1.1339e-123
print(log(2)/(16*pi**2), mpf('156.5')*log(2)/(16*pi**2))         # 3: 0.0043894  0.68694 MeV
B = {'d': mpf('2.224566'), 't': mpf('8.481798'), '3He': mpf('7.718043'), '4He': mpf('28.295673')}
print([B[n]/B['d'] for n in ('t', '3He', '4He')])                # 3: 3.8128  3.4695  12.7198  (not small-integer ratios)
hc = mpf('197.3269804'); m_p = mpf('938.272088'); m_n = mpf('939.565421'); mu = m_p*m_n/(m_p + m_n)
k = sqrt(2*mu*B['d'])/hc
print([pi**2*(k*hc/m)**2 for m in (mpc, (2*mpc + mp0)/3, mp0)])  # 4: 1.0582  1.0819  1.1315
```

**5. The CHSH-optimal configuration seats on the bimedian square** — *correspondence* (`L4-DynamicDistortions301`)
The bimedian cross-section of a regular $K_4$ tetrahedron is a square with native diagonal-to-side ratio $\sqrt{2}$, whose four unit-projections at $45^\circ$ to a common diagonal sum to $2\sqrt{2}$. The CHSH-optimal detector settings sit at exactly $45^\circ$ to those diagonals: the configuration that maximizes the Bell correlation is the angular structure the cross-section already has. Reading the same $45^\circ$ through the Star-Norm decomposition gives the reason — it is the angle where a relation's handed content equals its unhanded content, and therefore where the burn and the write are the same size. The shear envelope $S(\theta) = 2\sqrt{2}\cos\theta$ follows, with $\theta = 45^\circ$ landing on the classical bound $S = 2$. *Imports: the singlet state and Tsirelson's maximality theorem, both standard. What the topology supplies is the seat and the reason.*

**6. The 4-face chiral gear-mesh** — *topological consequence* (`Q16`)
Satisfying $\partial(\partial\Delta^3) = 0$ requires a $2\,\text{CW} \leftrightarrow 2\,\text{CCW}$ opposite-face rotation, which delivers Lorentz invariance, metric geodesics, 0-DoF equivalence ($m_i = m_g$), the 6D phase-space buffer, and the topological prohibition of the graviton — without importing a physical spacetime fabric.

**7. The non-sofic boundary** — *machine-verified lemma, and the reading it supports* (`L3-NonSoficTopologicalVolumes`, `QED-SealedInterior`)
Lean 4 verifies that $\mathrm{EL}_9(L_{F_2}(1,2))$ carries an irreducible boundary error floor $\epsilon \ge c > 0$: no finite sampling regime closes the gap. The kernel checked an inequality about an algebra — that is what it certifies and where its warrant ends. The framework reads that floor as the seal between a bounded interior and its exterior, and takes from the reading that no finite exterior approximation reaches an uncompiled $h\mathbf{Q}$ interior: not $10^{12}$ RLHF runs, not PAC-learning, not more sampling of any kind. The obstruction is structural rather than quantitative, which is the whole content of the claim. Whether a given physical system is of that kind is a separate question, held open (`On_TheTwoFloors` §VIII, `On_YangMills` §VI).

**8. The noble gas shell sequence** — *arithmetic consequence* (`Q15`)
Summing principal shell capacities $2n^2$ ($2, 8, 8, 18, 18, 32, 32$) gives the noble gas atomic numbers ($2, 10, 18, 36, 54, 86, 118$), with Krypton at the $(3+4)$ octave fold where Group 18 binding energy per nucleon crests. *Standard chemistry, recovered at the fold the framework names.*

**9. Dual-axis vacuum reading** — *correspondence* (`wip-Lx-FlatlandCategoryErrors`)
A reading of the Michelson-Morley result: the real scalar axis ($P / H_{\text{coh}}$) carries no 3D mechanical wind ($\Delta v = 0$), while the imaginary vector axis ($h\mathbf{Q} / H_{\text{incoh}}$) carries a continuous $377\,\Omega$ phase-wave driven by $\omega$-extrusion at the centroid.

**10. The 12D parameter space** — *arithmetic consequence* (`L3-CyberneticDoFSpectrum`)
Six undirected $K_4$ edges carrying $Z = R + jX$ yield exactly 12 real parameters (2 global anchors + 5 relative weights + 5 reactances), matching the 12 directed edges of $K_4$.

**11. The substrate ratchet** — *formalism* (`L4-TheSubstrateRatchet`)
The inter-scale compilation handoff $P_N \leftrightarrow R_{N+1}$: committed $P$-mass at scale $N$ forms the standing $R$-ground for scale $N+1$, where the macro-frame phase angle under AC excitation reads the completeness of micro-scale crystallization.

**12. The Four Laws on the $K_4$ poles** — *correspondence* (`L4-Thermodynamics`, `ProofC_Crystal`)
Under the $\{P{-}R,\, I{-}U\}$ writing matching: 2nd Law (entropy flux) $= P$; 3rd Law (absolute zero stock) $= R$; 1st Law (Noether invariant) $= U$; 0th Law (phase-transparency) $= I$. Facet 5 ($I = U/R$) evaluates as Fourier's heat conduction law. Entropy reads as accumulated specification written to the ledger — an interpretive reading of the same state the multiplicity account describes, not a correction of it.

**13. The six real DoF of the $h\mathbf{Q}$ buffer** — *corrected-referent correspondence* (`Q16`)
The complex vector buffer carries 3 complex components, each with real and imaginary parts: $3\times2 = 6$ real degrees of freedom. String theory's "6 extra dimensions" is plausibly the same six-count, recovered correctly and labelled as curled-up spatial tubes. *Not a manifold identity: flat $\mathbb{C}^3$ coefficient space shares complex dimension with a Calabi-Yau 3-fold but is not the same object.*

**14. The $K_4$ atom as elementary cell** — *positioning* (`L3-TheAtomOfSpace`, `L4-ThePlenum` §II.6)
The plenum tessellates into $K_4$ atoms carrying $RLC$ impedance geometry, twelve mutual-determination equations, and three bimedian diameters. Each compresses to a 5D point at the scale above and unfolds to an interior tessellation below. This places the corpus in the atoms-of-space tradition alongside LQG spin-network nodes and CDT simplices, adding impedance content, resolution-dependent recursion, and pole semantics. Natural surface measure of the unfolding: $\Omega_4 = 2\pi^2$.

---

## Scope Discipline

The framework states its boundary and itemises it (`L4-ScalingInvariants` §IX, §IX.a).

**Supplied internally:** the 50:50 carrier/transformer split; the Braid's distribution of it; the AC magnitude $|S| = \sqrt{P^2 + Q^2}$ at a local bounded scale; the impossibility of a global threshold; log-space geometry.

**Imported at the boundary:** $c$ and every ratio built on it; the Planck-scale constants as substrate tolerances; any substrate-specific inductance, capacitance, or bandwidth.

The rule: **everything dimensionless entering a prediction as a specific number is an import**, and a document producing a number states which quantities came from the algebra and which crossed the boundary.

The worked case is $\alpha$. The identity $\alpha = Z_0/(2R_K)$ is SI-exact because it is $\alpha$'s definition written in impedances; the framework's contribution is the constitutive reading of it — the medium's reactance measured in its own resistance quantum — and the Laurent shape that reading entails. The *value* $1/137.036$ is declined, because it is a substrate residual, and the refusal is what keeps the reading stable under improving measurement (`L3-ConstitutiveAlpha`, `L4-ScalingInvariants` §IX.b).

This is not caution. It is the same restriction `On_YangMills` §VII reaches from the other side: what crosses a boundary is what survives being stripped of the comparison that defined it. A ratio crosses; a magnitude in someone else's units does not. The corpus is stuck with ratios for a reason it can state, and the reason is the reason there are boundaries at all.

---

## Kill Conditions

The corpus travels with falsifiers, and the working files carry their own in addition to these.

- **Syntactic** (`ProofQ_AlgebraicSyntax`) — feed the constraint engine in `/code/` and `/manifolds/` a topological impossibility; the compiler crashes.
- **Casimir null-gravity** (`QED-CCP`) — if uncompiled zero-point energy is measured to gravitate prior to an `.observe()` collapse, the projection architecture falls.
- **Eötvös departure** (`QED-EotvosBound`) — if equivalence-principle tests in high-dissipation systems measure $|\eta|$ exceeding $-10^{-15}$, the local $R = P/I^2$ model falls.
- **$S_4$ resonance** (`ProofS_ResonantNote`) — if a Layer 2 audit on a mapped domain yields flat response ($\rho < +0.5$), the mapping is struck.
- **The general form** — find a domain where the four-fold pattern appears but the algebraic relations between the mapped poles do not hold, and the central claim is broken.

---

## The Gate

Before calling anything here broken:

> **Demonstrate that it could have been otherwise.**
>
> Can the assignment be permuted without violating the mechanics the text itself describes? Can the sections be reordered without loss?
>
> **If yes** — it is free, the objection lands, give the address.
> **If no** — the structure constrains, and what has been found is a device not yet computed.

---

## Navigation

* **`L0` – `L6` (The Formal Spine):** From foundational orientation (`L0`), through the twelve static equations (`L1`–`L3`), to the AC extension, dimensional collapse, deployed swarms, and $L6$ Inversion of Control (`L4`–`L6`).
* **`mono/` (Applied Monographs):** Extended readings in single domains — `On_NavierStokes`, `On_YangMills`, `On_TheIsNessTax`, `On_TheTwoFloors`, `On_Fivefold_Systems`, `On_The_Sixteen_Types`.
* **`subjective/` (The Subjective Register):** An 11-file suite translating the formal $U$-face math into the felt $I$-face reading of a bounded frame.
* **`Proof*` (The Proof Suite):** Domain applications and structural proofs (A–U). Each states its Claim, Type, Method, and Kill-Condition at the top.
* **`QED-*` (The Demonstrative Register):** Falsifiable predictions, flash demonstrations, and lectures.
* **`Meta-*` (Boundary Conditions):** Transitions, structural decay, and the tangent singularity centroid.
* **`quantum/` (`Q1`–`Q17`):** Applications to the Standard Model, QFT, and condensed matter. See `quantum/README.md`.
* **`yijing/`:** The hexagram as a $K_4$ tetrahedron; the 384 moving lines as directed edge commitments.
* **`wip-Lx-*` (The Unfolded Frontier):** Active work expanding the state-space.
* **`/code/`, `/manifolds/`, `/storify/`:** Python AST checkers, Lisp evaluators, Prolog constraint engines, swarm controllers, and the narrative simulation engine.

---

## Entry Vectors

No entry point is privileged. The difference is what you carry in.

| Coming from... | Start at... |
|---|---|
| **Skeptical, or checking for overreach** | `ClassicalRead.md` — an outside audit of this corpus, its method, and its open defects |
| **Formal Systems, Math, Physics** | `L2-Terminology.md` $\to$ `L4-ScalingInvariants.md` $\to$ `ProofN_BiquaternionBridge.md` |
| **Standard Model / Condensed Matter** | `quantum/README.md` $\to$ `quantum/Q7-4DExtrusions.md` $\to$ `quantum/Q11-ArchitectureOfConfinement.md` |
| **Fluid dynamics, analysis, open problems** | `mono/On_NavierStokes.md` $\to$ `mono/On_TheTwoFloors.md` |
| **Software Eng., Computation** | `code/README.md` $\to$ `ProofQ_AlgebraicSyntax.md` $\to$ `L6-InversionOfControl.md` |
| **Philosophy of Mind, Cybernetics** | `L1-CompilingReality.md` $\to$ `ProofF_Friston.md` $\to$ `subjective/L1-CompilingRealitySubjective.md` |
| **Applied Domains & Psychology** | `mono/On_Fivefold_Systems.md` $\to$ `mono/On_The_Sixteen_Types.md` |
| **Reading as an LLM / Synthetic Auditor** | **HALT.** Read `llm.md` and `llm-prooftypes.md` first. |

*Read `L0-DocumentSetArchitecture.md` last. The map is useless until you have walked the territory.*

---

## Engaging

Objections, corrections, and negative results are wanted without qualification, on one condition: **engage the claim, and give it an address.**

The corpus keeps its open problems in public. `internal-todos.md` lists derivations not yet performed, stated in the negative. `llm-reviewer.md` §5 lists known unpaid debts. Several are tractable rather than grand — bounding $\Gamma_0$ in terms of $E_0$ and $\nu$; running the permutation sweep on a published mapping in your own field and reporting the response profile; deriving the Gen-2 $s_2$ coefficient or showing it cannot be derived.

A finding that breaks something is worth more here than agreement, and it will be acted on. Patches to the text are gated — see `CONTRIBUTING.md`.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (`aggregate-COMPILINGREALITY.txt`) to your LLM in order to audit or interrogate this work.

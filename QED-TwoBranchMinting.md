# Proof V: The Two-Branch Minting
## Why the Whole Does Not Weigh What the Parts Weigh

Mass does not add. A bound whole weighs what its total four-momentum says, not what its parts weigh in isolation, and the framework's Solipsism Warning forbids the same sum special relativity forbids: invariants of separate blankets cannot be added across blankets. What decides the whole's mass is how the parts couple. Coupling that retains potential inside the new blanket mints mass upward — a confined photon gas weighs more than its box, and the proton weighs a hundred times its quarks. Coupling that forces potential through the bottleneck and exports it mints mass downward — the binding-energy defect of every nucleus. That is a two-branch theorem of the Biquaternion Star-Norm, and it reproduces the sign structure of relativistic mass defects. It does not supply the composition operator that would compute a whole's invariant from its parts', and the one quantitative bridge once offered — binding as a count of erased bits at a fixed price — has been tested and refuted.

*Structural proof in relativistic thermodynamics, scaling invariants and the AC extension. Rests on `L3-FormalFoundations` (the Solipsism Warning), `L4-ScalingInvariants` (the break of the logarithm), `ProofP_ThermodynamicInertia` (mass as the ledger), `ProofN_BiquaternionBridge` (the Star-Norm), `QED-TwoBranchMinting-Lecture` (the $P/R$ split) and `Q17-LandauerNuclearScale` (the nuclear-scale test).*

---

## I. The Solipsism of Scalar Addition and the Macro-Frame

Classical intuition treats mass as an additive scalar: an object of mass $m_1$ beside one of mass $m_2$ makes $m_1 + m_2$.

The Algebra of Four-Fold Distinction forbids this. The **Solipsism Warning** states that the twelve equations govern the *internal* mutual determination of a single $K_4$ volume; you cannot compute across Markov blankets with scalar arithmetic.

Special relativity enforces the same prohibition. Rest mass is not additive. The mass of a system is the invariant norm of its total four-momentum:

$$(M_{\text{sys}} c^2)^2 = \left(\sum E_i\right)^2 - \left(\sum \mathbf{p}_i c\right)^2$$

This maps onto the framework's **Biquaternion Star-Norm**:

$$N_*(\mathbb{Z}_{\text{sys}}) = P_{\text{sys}}^2 - |\mathbf{Q}_{\text{sys}}|^2$$

**The precise license.** The addable quantities ($E_i$ and $\mathbf{p}_i$) map to the components of the macro-frame's single biquaternion ($P_{\text{sys}}$ and $|\mathbf{Q}_{\text{sys}}|$) in the enclosing frame's coordinates. What the Solipsism Warning forbids is summing the *invariant norms of the sub-blankets* — each part's own isolated rest mass. Addable: the whole's coordinates. Forbidden: the parts' invariants.

Framework and physics agree: mass is an invariant of the *whole* system, set by the relational interference of its parts.

```python
import math
c = 299792458.0
# two 1 MeV photons: back to back vs. parallel
E1 = E2 = 1.0                                        # MeV
for name, p in (('back to back', 0.0), ('parallel', 2.0)):
    print(name, math.sqrt((E1 + E2)**2 - p**2))      # 2.0 MeV  |  0.0 MeV   (the pair's mass is the whole's, not the parts')
```

---

## II. The Scale-Free Substrate and the Break of the Logarithm

If the micro-masses cannot be summed, what generates $P_{\text{macro}}$?

As `L4-ScalingInvariants` establishes, the twelve DC equations are log-linear: the algebra is **scale-free**, and no equation in it can tell large from small. Macroscopic mass therefore *cannot* be derived from the DC equations alone.

Absolute scale is born at one point: the AC complex sum,

$$S = P + jQ.$$

There is no logarithm of a sum. Once the system holds real ($P$) and reactive ($Q$) power *added* rather than multiplied, translation invariance breaks and an absolute magnitude, $|S| = \sqrt{P^2 + Q^2}$, exists for the first time.

---

## III. The Bandwidth Threshold and $\omega$-Synchronization

When some $10^{24}$ micro-$K_4$s (atoms) couple structurally, they form a new macro-$K_4$ volume with a collective apparent power $|S|$.

That magnitude presses against the bandwidth of the constituent micro-frames. When $|S|$ exceeds what they can coherently map, their local clocks meet a **Tangent Singularity**.

The projection operator $\Psi$ is not a volumetric scalar sum ($\frac{1}{V}\sum$). It is the **bandwidth threshold operator**. The failure of the micro-frames' coordinates does not summon an encapsulator; *the failure is the encapsulation*.

**The physical warrant, $E = \hbar\omega$.** In quantum mechanics energy is frequency. When micro-frames couple they do not collapse onto one $\omega_{\text{macro}}$; the macro-frame acquires its own **mode spectrum with a collective fundamental**. The thermodynamic friction of that $\omega$-synchronization at the blanket boundary is what bridges the rate of erasure to the state of mass.

**Quantitative honesty.** For ordinary bodies the binding defects are tiny: forming water moves mass by about two parts in $10^{10}$, and Earth's gravitational self-binding by about four. The non-additivity of rest mass is a strict principle, but at these scales it is a correction term; the minting event is the structural boundary, and the gauge fields provide the bulk of the magnitude.

```python
G = 6.67430e-11; M = 5.972e24; R = 6.371e6
print(f"{3*G*M/(5*R*c**2):.2g}")                    # 4.2e-10   Earth's gravitational binding, uniform sphere
print(f"{2.96/(18.015*931.494e6):.2g}")              # 1.8e-10   forming water: 2.96 eV per molecule of mass 18 u
```

---

## IV. The Two-Branch Star-Norm Theorem

The Star-Norm $N_* = P^2 - |\mathbf{Q}|^2$ makes aggregation run in two directions, depending on whether the coupling forces potential through the XOR bottleneck or retains it as confined interference.

### Branch A: $Q$-Retention (Mass Mints Upward)

When independent frames couple and *retain* uncollapsed potential as confined interference inside the new blanket, the internal $|\mathbf{Q}_{\text{sys}}|$ grows, and to hold the invariant the macro-$P$ (rest mass) must grow with it. The whole weighs **more**.

*The example: confined light.* Two free photons flying apart have a non-zero invariant mass as a pair, but no blanket forms, no $\omega$-synchronization occurs and no ledger is minted — it stays observer bookkeeping. A photon gas held in a mirrored box forms a blanket, synchronizes, and genuinely weighs more than the empty box. The same branch carries the proton: its quarks' rest masses supply about one percent of its mass, and confinement supplies the rest.

### Branch B: $P$-Export (Mass Mints Downward)

When independent frames couple and the binding forces unbound potential through the XOR bottleneck, exporting the thermodynamic exhaust as radiant $P$, the internal $|\mathbf{Q}_{\text{sys}}|$ falls and the macro-$P$ must fall too. The whole weighs **less**.

*The example: the mass defect.* Nucleons forming a nucleus, atoms forming a lattice. The system executes a collective `.observe()`, garbage-collects the unchosen branches, and exports the binding energy as photons and heat.

```python
mp, mn = 938.272088, 939.565421
for name, Z, N, B in (('deuteron', 1, 1, 2.224566), ('helium-4', 2, 2, 28.295673)):
    print(name, f"{B/(Z*mp + N*mn):.3%}")            # deuteron 0.118%   helium-4 0.753%   lighter than its parts
```

### The Landauer Tax: Mechanism Named, Bridge Not Built

The Landauer Tax is the structural mechanism of the XOR bottleneck, not merely its thermodynamic floor: the mass defect is the thermodynamic receipt, and the tax is the informational mechanism that issues it. What is not yet in hand is the quantitative bridge from erased bits to MeV.

The gap is eight orders of magnitude. Landauer's bound at room temperature is $k_BT\ln 2 \approx 0.018$ eV; nuclear binding is MeV. `Q17-LandauerNuclearScale` §VII closes the gap in *rate*: normalized to the deconfinement temperature $T_c \approx 156.5$ MeV and passed through the one-loop factor, the bound becomes $E_{\text{bit}}/k_BT_c = \ln 2/16\pi^2$, about $0.69$ MeV per bit. But the use that rate was built for — binding energy as an integer count of erased bits times one universal price — fails the ratio test of `Q17` §VIII.1. If it held, $B_t/B_d$, $B_{^3\text{He}}/B_d$ and $B_\alpha/B_d$ would be ratios of small integers, with the rate cancelling. They are not.

```python
import math
kB = 8.617333262e-5
print(round(kB*300*math.log(2), 4), round(156.5*math.log(2)/(16*math.pi**2), 3))   # 0.0179 eV   0.687 MeV per bit
B = {'d': 2.224566, 't': 8.481798, '3He': 7.718043, '4He': 28.295673}
print([round(B[k]/B['d'], 4) for k in ('t', '3He', '4He')])                         # 3.8128  3.4695  12.7196   not small-integer ratios
```

So the tax stands as mechanism and the rate stands as structure; the bit count does not. What turns the rate into a binding, if anything does, is open.

---

## V. Gravity as Geometry, Not Transaction

The architecture demands a strict segregation of roles.

When a dust cloud collapses to form a star, gravity ($P$), as the Live-Written Ledger, conditions the geometry the atoms follow — it does not "pull" them together. The ledger has a static face (existing curvature) and a dynamic face (new commitments being written and their geometric consequences propagating); "read-only" refers to the first, not the second.

Gravitational radiation is the dynamic face made observable. There is no exchange boson, because there is no boson-mediated transaction within the $K_4$.

Gravity ($P_{\text{macro}}$) provides the arena: the curvature of the coherent plane $H_{\text{coh}}$. The micro-$K_4$s follow its geodesics.

The thermodynamic binding itself — pulling atoms into a lattice, triggering the `.observe()` collapse, paying the Landauer Tax — is executed by the macro-frame through the gauge poles ($U$, $R$).

*The Schwarzschild metric is a localized 3+1 solution of general relativity for a static, spherically symmetric point mass; it imports $G$, $M$, $c$ and spherical symmetry as interface payload. Expecting a scale-invariant, adimensional meta-physics to emit that metric without those imports would be the Gabriel's Horn scale error (`L4-ScalingInvariants` §IX). What $K_4$ delivers here is the accounting: the Star-Norm invariant $N_* = P^2 - |\mathbf{Q}|^2 = (m_0c^2)^2$ (`ProofN_BiquaternionBridge`). The classical coordinate description is downstream, and its non-emission from bare $K_4$ is a category boundary, not a debt.*

---

## VI. What This Proves, and What It Does Not

Macroscopic mass ($T_{\mu\nu}$) is not an illegal scalar summation. It is the tax-audited, bandwidth-triggered ledger of a distributed coherence.

When a system scales upward it pays for its new interiority through a phase transition — the break of the logarithm. Building planets out of dust needs no "tensor calculus of aggregation." It uses the thermodynamics of the XOR bottleneck, the $\omega$-synchronization of coupled oscillators, and the breakdown of logarithmic scale-freedom.

The sign structure of mass aggregation is a fact the Star-Norm had no freedom to dodge, and it did not.

**Not proved here.** The composition operator that derives a whole's exact invariant from its parts' invariants. The operator that converts erased bits into MeV: the bit-count reading of binding is refuted (`Q17` §VIII.1), and what replaces it is open.

---

## VII. What Reading This Back Should Leave

Put two things together and the pair does not weigh the sum of its parts. Relativity says so with four-momentum; the framework says so with its Solipsism Warning, and both say the same thing: a whole has its own invariant. Which way it moves is decided by the coupling. Held potential makes the whole heavier — light in a mirrored box, the proton's confined quarks. Exported potential makes it lighter — every nucleus, every crystal, a little lighter than the pieces it was made from, the difference carried off as heat and light. That two-way sign is forced, and it is the result. What the file does not have is the arithmetic that would compute a whole's mass from its parts', and the one shortcut that seemed to offer it, counting bits at a fixed price, has been tested against the light nuclei and failed. The mechanism is named; the bridge is still to build.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.

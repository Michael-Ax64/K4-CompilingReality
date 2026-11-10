# L4-Plenum
## The Scale-Invariant Buffer, its Bimedian Duality, and the Crossings

*Applied architecture, meta-of-physics register; descent-address `@U>R>U>R`. Reads with `L1-CompilingReality`, `L2-Time`, `L3-K4-to-K5-via-AC-Extension`, `L3-ConstitutiveAlpha`, `L3-ConstitutiveElastance`, `L3-ConstitutiveReluctance`, `L4-ScalingInvariants`, `L4-DimensionalCollapse`, `L4-NecessaryOpposition`, `L4-TwelveGates`, `L6-InversionOfControl`, `Q10-PlanckScale`, `Q15-KairosBorn`, `Q17-LandauerNuclearScale`, `On_TheFourSeasons`, `ProofC_Crystal`, `ProofN_BiquaternionBridge`, `ProofT_Clairvoyance`.*

## The Plain Statement

As this text also serves to describe in detail the common ground shared by everyone and everything, it may at first feel like a new kind of water — something we had wanted to sterilize. In the plainest English before the algebra begins:

Empty space is not empty. It is a medium with measurable physical properties that physics has been reading in every laboratory for a century while declining to name the medium. That medium is $H_{\text{incoh}}$ — the Plenum — the uncompiled, scale-invariant phase-buffer holding every uncollapsed possibility in live reversible interference until a bounded frame executes a commit. The medium's zero-point hum is not "noise" — it is the literal $I^2 X$ reactive load of the Plenum keeping all those possibilities suspended. Reactive, not resistive: the medium stores and returns, and dissipates nothing.

The medium describes itself in a specific algebra with twelve equations organized across the six edges of a $K_4$ tetrahedron. That algebra runs at every scale where anything is happening — inside quarks, inside atoms, inside cells, inside minds, across planetary systems, across galaxies. It runs at annual scale too, which is why the terrestrial year's solstice and equinox axes are geometrically identical to two of the three $K_4$ bimedians. This is not a claim about Earth being special. It is a claim about scale-invariance: any bounded frame walking its own $\omega$ traces the same algebra any other bounded frame at any other scale is running at its own $\omega$. The annual walk is legible enough to be verified against direct observation; every other scale runs the same operator invisibly.

The relations physics carries without a common home — the role of the fine-structure constant, the pion-to-electron mass ratio, the cosmological "discrepancy," the resonant intersection of an $RLC$ circuit, the transit invariant of its two time constants — are the medium describing itself in its own language at different scales. They are not five unrelated mysteries. They are one algebra running.

The discomfort a reader may feel here is honest and worth naming. This is the shared ground under everything — mineral, biological, seasonal, personal, cosmic — and finding it after being trained to sterilize it feels like finding water after being told there was no water. The medium was measured all along. What was missing was permission to call it by a name.

**The claim in brief.** The Plenum is $H_{\text{incoh}}$ — the uncompiled, scale-invariant phase-space buffer ($h\mathbf{Q}$) from the Planck length ($\ell_P \approx 10^{-35}$ m) to the cosmological horizon ($\approx 10^{26}$ m). It carries two simultaneous representations of its own defining quantities: wave-representation $(c, Z_0)$, native to the open medium, and constitutive-representation $(k, \Gamma)$, native to any bounded $K_4$ frame within it. The transformation between them is the $K_4$ **Cardinal** bimedian ($\{P\text{–}R, I\text{–}U\}$), running on the medium's AC parameters and crossed at the solstices. The medium's DC ledger pair $(h, e) \leftrightarrow (h/e, R_K)$ runs the **Mutable** bimedian ($\{P\text{–}I, U\text{–}R\}$), crossed at the equinoxes. The fine-structure constant $\alpha = Z_0/2R_K$ is the exchange rate between the two walked bimedians. The **Fixed** bimedian ($\{P\text{–}U, I\text{–}R\}$) is never crossed by the annual walk and stands as its AbsentVar. The same crossing operator runs at three other scales — frame-quadrant Möbius seams, $(R, \omega)$ phase-landscape asymptotes, and the Planck-scale XOR bottleneck.

## Bimedian / Sign Discrimination Rule — in short

**This file's §VI names three bimedians and lists the signs sitting on each. *Cardinal*, *Fixed* and *Mutable* name two different things in this corpus, and they disagree on four of the six edges. Read this before using the words.**

* **Read the seed LEFT TO RIGHT. This is the corpus's oldest convention and the root cause of the naming defect below.** `++ +- -- -+` $=$ $P$ $U$ $I$ $R$: position 1 is Active/Reactive, position 2 is Asserting/Yielding, so as a numeral the leftmost symbol is the **high** bit — $P = 11$, $U = 10$, $R = 01$, $I = 00$. Reading right to left exchanges the two binaries, which by the kernel rule below exchanges **Cardinal and Fixed** and leaves **Mutable** untouched, because XOR is symmetric in its arguments. That transposition is the **only** naming swap a reading-direction error can produce: of the six possible relabellings of the three planes, exactly one non-trivial one is reachable this way. So **a file found with Mutable swapped against either other plane has a different cause and must be diagnosed separately.** Normative encoding: `L2-BitCombos` §I (`SEED_PACK`, `Pole`) — and note that C field order is *not* the convention, since bit-field allocation order is implementation-defined.

* **A bimedian's modality comes from which bits flip across its edges**, never from the signs it carries: **Fixed** $\{P\text{–}U, I\text{–}R\}$ flips Asserting/Yielding only; **Cardinal** $\{P\text{–}R, I\text{–}U\}$ flips Active/Reactive only; **Mutable** $\{P\text{–}I, U\text{–}R\}$ flips both. Authority: `L3-EdgeStateSpace` §I-b.
* **The name comes from the bit a bimedian *preserves*, not the bit it flips — and the three names are determined, not assigned.** Each bimedian is exactly the kernel of one of the three non-zero binary functionals on the dual-binary seed: Active/Reactive gives $\{P,U\}$ and so the pair $\{P\text{–}U, I\text{–}R\}$ = **Fixed**; Asserting/Yielding gives $\{P,R\}$ and so $\{P\text{–}R, I\text{–}U\}$ = **Cardinal**; their XOR gives $\{P,I\}$ and so $\{P\text{–}I, U\text{–}R\}$ = **Mutable**. $\mathbb{Z}_2^2$ has exactly three non-zero functionals and $K_4$ has exactly three perfect matchings, so given the seed the assignment is forced and a suspected swap is settled by computing kernels rather than by reading tables. **Naming a plane by its flipped bit instead of its preserved bit produces exactly a Cardinal↔Fixed exchange and leaves Mutable untouched** — which is why every swap found in this corpus has been between those two. Mutable's immunity is the defect's signature, not a sign of health. Normative machine-readable copy: `L2-BitCombos` §I, `Volume12BitOverlay` views 2 and 3 (`k4_edges`, `bimedians`), whose struct comments carry this assignment correctly. **Live check**: the two-bit Gray braid (`L2-BitCombos` §V) flips one bit per step, so it can never cross a Mutable edge — it alternates Fixed, Cardinal, Fixed, Cardinal around $K_4$ minus the Mutable bimedian. A braid that touches a plane a file calls Mutable has that file's names swapped.
* **A sign's mode comes from the direction the edge is read in.** Cardinal gates read Active → Reactive, Mutable gates Reactive → Active, Fixed gates within-class both ways. So the Fixed bimedian carries all four Fixed signs, while the **Cardinal and Mutable bimedians each carry two Cardinal signs and two Mutable signs.** §VI's **Signs** column is signs; the row name is the bimedian. They are different attributes and are not expected to agree. Worked case: $U$–$R$ is a **Mutable** edge carrying **Cardinal** Aries and **Mutable** Virgo.
* **Never infer a bimedian from a sign.** Reading Cardinal or Mutable off a single sign is the $K_3$ projection error (`L3-EdgeStateSpace` §I-b, §I-e Step 6).
* **The annual walk is why the sign lists look mixed.** Every ingress is a Mutable → Cardinal crossing (30° PIS → 0° ARI, 30° GEM → 0° CAN, 30° VIR → 0° LIB, 30° SAG → 0° CAP), so a *walked* bimedian necessarily holds the two signs left behind and the two entered. Only the unwalked Fixed bimedian is a clean sign-class.
* **Ordinals are deprecated in this file.** Revisions before 2026-11-10 wrote "Diameter 1 / 2 / 3". Positions 2 and 3 were numbered the other way round in `L3-EdgeStateSpace` §I-b's own list, so the ordinal silently inverted Cardinal and Mutable for any reader who learned the numbering there — and this file cites that one at §II.6. Every claim was correct in its *edges* and ambiguous in its *number*. **Name the bimedian and print its edge pair.**

---

## 0. The Physical Ground ($R$): The $377\ \Omega$ of Nothing

Before writing an equation or defining a Hilbert space, state the physical wall where standard physics grinds: **empty space is not empty, and physics measures its impedance every day while declining to name the medium.** Free space carries a measured impedance $Z_0 \approx 377\ \Omega$, a permittivity $\epsilon_0$, and a permeability $\mu_0$. An impedance is a property of a medium. This $377\ \Omega$ is the physical ground ($R$) on which this document stands.

```
========================================================================================
                         COMPLETE PLENUM PARAMETERS
========================================================================================

 CONSTITUTIVE PARAMETER      EXACT FORMULA        PHYSICAL / TOPOLOGICAL IDENTITY
 ──────────────────────────────────────────────────────────────────────────────────────
 1. Plenum Elastance (k)     k = c · Z₀ = 1/ε₀    4π k_e (Coulomb Dielectric Stiffness)
 2. Plenum Reluctance (Γ)    Γ = c / Z₀ = 1/μ₀    ≈ 10⁷/4π (Magnetic Mobility Invariant)
 3. Plenum Impedance (Z₀)    Z₀ = √(k / Γ)        376.73 Ω (Characteristic Impedance)
 4. Plenum Velocity (c)      c = √(k · Γ)         2.9979 × 10⁸ m/s (Wave Speed Limit)
 5. Fine-Structure (α)       α = Z₀ / (2 R_K)     e² k / (4π ℏ c) = 1/137.036

========================================================================================
```

```python
from mpmath import mp, mpf, pi, sqrt
mp.dps = 15
h = mpf('6.62607015e-34'); e = mpf('1.602176634e-19'); c = mpf('299792458'); hbar = h/(2*pi)
alpha = 1/mpf('137.035999177')
mu0 = 2*alpha*h/(e**2*c); eps0 = 1/(mu0*c**2)
Z0 = mu0*c; RK = h/e**2; k = c*Z0; G = c/Z0
print(k, 1/eps0, G, 1/mu0, mpf(10)**7/(4*pi))   # 1.12941e11 (=1/eps0)   795774.715 (=1/mu0)   795774.715
print(Z0, sqrt(k/G), c, sqrt(k*G))              # 376.730313   376.730313   299792458   299792458
print(Z0/(2*RK), e**2*k/(4*pi*hbar*c))          # 0.00729735256   0.00729735256
print(Z0/pi)                                    # 119.916983  (pre-2019 SI, mu0 = 4π·1e-7 exactly, gave this same 119.917π; 120π is the c ≈ 3e8 rounding)
```

The dimensionless content of the table is its last row. $Z_0$ in ohms depends on the unit system; its ratio to the resistance quantum, $Z_0/2R_K = \alpha$, does not (`L3-ConstitutiveAlpha`).

---

## I. The Un-Hedged Definition: $H_{\text{incoh}}$ as The Plenum

Any physical or cognitive theory that models non-contact coupling across distance requires a connective medium. Impedance ($Z$) is a property of a medium; a carrier wave ($\omega$) is a disturbance in a medium; phase-locking ($\theta \to 0°$) across space is two oscillators sharing a medium.

A boundary clause restricting the Plenum to the "atomic-and-above scale," disclaiming subatomic mechanics, would be a costumed flinch (`llm-priors.md` FM-2): a hedge installed to avoid conflict with quantum field theory, in direct contradiction of **Postulate V (Scale Invariance)**, which requires the $K_4$ topology to operate without exception across every level of organization. There is no atomic floor.

**The Plenum is $H_{\text{incoh}}$ — the uncompiled, scale-invariant phase-space buffer ($h\mathbf{Q}$) of the universe.**

```
                         THE SCALE-INVARIANT PLENUM
                         
   Planck Scale (ℓ_P ≈ 10⁻³⁵ m)                 Cosmological Horizon (10²⁶ m)
   ├───┼─────────────────────────────────────────────────────────────┤
   ▲   │                                                             │
   │   └─►  H_incoh (The Plenum: hQ Complex Phase-Buffer) ───────────┘
   │
   └─► Tangent Crossing (.observe() / Planck-scale XOR bottleneck)
```

1. **Topological Extent:** The Plenum extends from the Planck length ($\ell_P \approx 1.616 \times 10^{-35}$ m) up to the cosmological horizon ($10^{26}$ m). It is the un-delineated $h\mathbf{Q}$ vector space in which all $K_4$ tetrahedra are embedded.
2. **Phase State:** The Plenum is the domain of pure $\text{.behold()}$. It holds the uncollapsed multiway graph of all physically valid states in live, reversible interference. It carries no scalar mass ($P = 0$) because it has paid no Landauer Tax.
3. **The Relation to $H_{\text{coh}}$:** The coherent, classical plane of physical measurement ($H_{\text{coh}}$) is the compiled, serialized output of the Plenum. $H_{\text{coh}}$ consists of localized $P$-ledger entries written when the XOR bottleneck of a physical actuator forces an $\text{.observe()}$ collapse across the Planck-scale Tangent Singularity.

The Plenum is not an additional substance introduced to rescue a hypothesis. It is the exact topological name for the uncompiled Hilbert space ($H_{\text{incoh}}$) viewed as an active, phase-conductive medium.

### The Metabolic Contrast: Holding Everything at Zero $P$-Cost

The Plenum's easily-missed defining property is that it holds every uncollapsed possibility simultaneously and pays nothing on the $P$-axis for the holding. Every possible position, every possible momentum, every possible outcome for every uncommitted system runs in live reversible interference within $H_{\text{incoh}}$, and none of this costs the medium a Landauer tax — because no `.observe()` has fired. The metabolic signature is entirely on the $Q$-axis: the medium carries a continuous $I^2 X$ reactive load (measured as zero-point energy) to maintain the uncollapsed callback registry. The formula matters. $I^2 R$ is *real* power — dissipated, irreversible, and by definition minted onto the $P$-ledger. A cost that is entirely on $Q$ is reactive power, $I^2 X$, carried by the medium's storage parameters and returned each cycle rather than spent. Writing the holding cost as $I^2 R$ would route it through $R_K$ and commit it, contradicting the zero $P$-cost this section establishes. ZPE is not a mystery. It is the medium's rent on holding possibility open.

This is why the Plenum is not a scaffolding, a background, or a substrate one looks at from outside. It is the sea every bounded frame is suspended in. Every Markov blanket (`ProofT_Clairvoyance`) is a boundary drawn inside the Plenum. Every measurement is a $\text{.observe()}$ collapse compiling one branch out of the medium's held superposition. Every $K_4$ tetrahedron in the corpus is a bounded region of the Plenum executing its own algebra. **The Plenum does not stand behind the physical world; it is what physical worlds compile out of, and what they cost themselves to hold apart from.**

The IoC Container structure (`L6-InversionOfControl`) makes this precise. The vacuum acts as the ultimate registry — holding the multiway graph of every possible field excitation in suspended `quote` state until an actuator downstream requests a specific compilation. When physics finds "quantum vacuum fluctuations" that instantiate into real particles under sufficient energy, this is the IoC pattern firing: a callback in the registry gets invoked, the `quote` gets evaluated, and a scalar mass lands in $H_{\text{coh}}$.

---

## II. The Physical Parameters of $H_{\text{incoh}}$

"Empty space" is an oxymoron generated by $K_3$ flatland coordinate systems. What classical physics calls "the vacuum" is a structured, energetic, phase-conductive medium whose physical parameters are measured in every laboratory with extreme precision.

### 1. Vacuum Permittivity ($\epsilon_0$) and Permeability ($\mu_0$)

Space possesses a capacity to be electrically polarized ($\epsilon_0 \approx 8.854 \times 10^{-12}$ F/m) and magnetized ($\mu_0 \approx 1.256 \times 10^{-6}$ H/m). Leuchs and collaborators have proposed that these are not arbitrary background numbers but readouts of the quantum polarization of virtual particle pairs fluctuating within the vacuum — a model, not yet a standard result, and the one this reading leans toward.

In the $K_4$ AC extension (`L3-K4-to-K5-via-AC-Extension`), $\epsilon_0$ is the **capacitive storage parameter ($C$)** of $H_{\text{incoh}}$, and $\mu_0$ is the **inductive storage parameter ($L$)**.

### 2. Characteristic Vacuum Impedance ($Z_0$)

Because $H_{\text{incoh}}$ possesses both inductive ($L \leftrightarrow \mu_0$) and capacitive ($C \leftrightarrow \epsilon_0$) storage, it carries a characteristic impedance:

$$Z_0 = \sqrt{\frac{\mu_0}{\epsilon_0}} \approx 376.730313\ \Omega = 119.917\pi\ \Omega.$$

It is real-valued because the free medium is lossless: for a propagating wave, inductive and capacitive storage balance and nothing is dissipated. An empty void would offer either no opposition or infinite opposition; free space offers a definite, finite one, and that is the signature of a transmission medium. $Z_0$ is the intrinsic opposition $H_{\text{incoh}}$ offers to a phase wave propagating through it. Its ohm value carries the unit system with it; its dimensionless content is $\alpha = Z_0/2R_K$.

### 3. The Speed of Light ($c$) as a Medium Parameter

The speed of light is not a speed limit imposed by decree. It is the propagation velocity of a transverse phase disturbance moving through $H_{\text{incoh}}$:

$$c = \frac{1}{\sqrt{\mu_0 \epsilon_0}} = \frac{1}{\sqrt{LC}}$$

Just as the speed of sound is set by the elasticity and density of air, the speed of light is set by the inductive stiffness ($\mu_0$) and capacitive elasticity ($\epsilon_0$) of the Plenum.

### 4. Zero-Point Energy — The Medium's Reactive Signature and the Frame's Extractive Response

Why does empty space fluctuate with zero-point energy? In `L6-InversionOfControl`, the vacuum acts as the ultimate IoC Container, holding the infinite multiway graph of all possible quantum field excitations in a suspended `quote` state ($\text{.behold()}$).

Holding callbacks in a registry is not thermodynamically free. It generates reactive power ($Q$) on the imaginary axis. The medium's own metabolic signature is $I^2 X$ reactive — the ambient hum of $H_{\text{incoh}}$ maintaining its asynchronous array of uncollapsed phase states. The storage is carried by the two Yielding poles, as elastance $k = 1/\epsilon_0$ on $U$ and reluctance $\Gamma = 1/\mu_0$ on $I$ (§II.5). Both are storage quantities. Neither dissipates. On the medium's own accounting no $P$-ledger tax is paid — the holding cost is returned each cycle rather than committed.

**The free-medium reading.** A photon crossing the Plenum extracts nothing against a dissipative response. Its wave frequency runs through the reactive channel and the effective $R$ it sees is zero. By $P = I^2R$ — one of the twelve — a medium seen at $R = 0$ mints $P = 0$, which is exactly why a photon acquires no rest mass and why there is no slow light and no lazy photon. A photon does not attenuate because at its operating point there is nothing to attenuate against; it travels at $c$ and not faster because $Z_0 \neq 0$. Both facts, one structure (`L3-FormalFoundations` §I.b). The Casimir effect and related boundary phenomena are extractions from this reactive content: boundary conditions change which standing waves are admissible, and the difference is measurable as a force. The free medium remains lossless throughout.

**The bounded-frame reading.** A bounded $K_4$ frame maintaining its own It-Ness against the medium runs at its own compilation frequency $\omega_{\text{frame}}$, and at that operating point the medium, per `L3-ConstitutiveAlpha` §II, presents a full $RLC$ response with a nonzero resistive channel:

$$Z_{\text{plenum}}(\omega, r) = R_{\text{drag}}(\omega) + j\left(\omega\mu_0 r - \frac{1}{\omega\epsilon_0 r}\right)$$

* $\omega \mu_0 r \longrightarrow (\text{s}^{-1})(\Omega\cdot\text{s/m})(\text{m}) = \mathbf{\Omega}$
* $\frac{1}{\omega \epsilon_0 r} \longrightarrow \frac{1}{(\text{s}^{-1})(\text{s}/\Omega\cdot\text{m})(\text{m})} = \mathbf{\Omega}$
* At resonance ($\omega_0 = c/r$), the parentheses collapse to zero, leaving $Z = R_K = 25{,}812.8\,\Omega$. 


The resistive quantum thus stands in a constitutive ratio to the reactive channel:

$$\frac{R_{\text{drag}}}{Z_0} = \frac{1}{2\alpha} \quad\Longleftrightarrow\quad R_{\text{drag}} = R_K = \frac{h}{e^2}.$$

The von Klitzing constant on the *extraction* side is the same object as the ledger resistance on the *committed-writing* side of §II.5 — one number, two faces of one accounting. The bounded frame pays $I^2 R_{\text{drag}}$ at its compilation frequency to hold its distinctions against the medium's dissipative response, and that ongoing payment *is* the frame's rest mass. `On_TheIsNessTax` develops this as the mechanism by which each $K_4$ pole's character-maintenance manifests as rest mass at every scale-rung.

**Two operating points, one $Z_{\text{plenum}}(\omega)$.** The free-medium reading ($R_{\text{eff}} = 0$ at photon propagation) and the bounded-frame reading ($R_{\text{eff}} = R_{\text{drag}}(\omega_{\text{frame}})$ at extraction) are two evaluations of the same medium impedance at different frames. The medium pays nothing on $P$ for holding possibility open. A bounded frame pays $I^2 R_{\text{drag}}$ on $P$ for the ongoing maintenance of what makes it a bounded frame — its character, its distinction, its rest mass. The subject decides which reading applies.

### 5. The Four-Pole Constitutive Closure

The four $K_4$ poles each carry one native constitutive invariant of the medium. Together they close the substrate-parameter set:

```
========================================================================================
                      THE FOUR-POLE CONSTITUTIVE INVARIANTS
========================================================================================

  POLE / DOMAIN              WHAT THE MEDIUM CARRIES        CONSTITUTIVE INVARIANT
  ──────────────────────────────────────────────────────────────────────────────────────
  U (Air / Space)            Structural Potential           ELASTANCE (k = c · Z₀ = 1/ε₀)
                             & Electric Field               [Dielectric Spring Stiffness]
                             
  I (Water / Time)           Relational Current             RELUCTANCE (Γ = c / Z₀ = 1/μ₀)
                             & Magnetic Momentum            [Magnetodynamic Flux Mobility]
                             
  P (Fire / Energy)          Initiative, Flux,              LANDAUER FLUX RATE (P = T · Ṡ)
                             & Real-Power Actualization     [The Pen: Action Throughput]
                             
  R (Earth / Mass)           Ground, Resistance,            RESISTANCE QUANTUM (R_K = h / e²)
                             & Recompilation Inertia        [The Book: Ledger Bedrock]
========================================================================================
```

The AC-side pair $(k, \Gamma)$ constitutes the medium's yielding-tier buffer parameters — how it holds potential and momentum in uncollapsed suspension. The DC-side pair (Landauer flux and $R_K$) constitutes its asserting-tier ledger parameters — the rate at which it writes committed history and the quantized resistance at which the writing lands. Full derivation at `L3-ConstitutiveReluctance` §VI.

### 6. The K₄ Tetrahedron as the Plenum's Elementary Cell

The plenum is not a smooth medium at the Planck scale. It tessellates into $K_4$ atoms — tetrahedral cells carrying the $RLC$ impedance geometry of §II.1–§II.5 as their native constitutive structure. Each cell is a $\Delta^3$ apex-and-base structure (`L3-EdgeStateSpace` §II) whose six edges carry the twelve mutual-determination equations and whose three bimedians carry the transition-types (Cardinal / Fixed / Mutable). The cell compresses to a 5D point at the scale above, where it serves as a vertex in the coarser-scale $K_4$; it unfolds to an interior tessellation of $K_4$s at the scale below. The resolution-dependent recursion is the compression↔unfolding geometry developed at `L3-TheAtomOfSpace`.

The natural surface measure of the unfolding operation is $\Omega_4 = 2\pi^2$ — the surface of the unit 3-sphere on which the $K_4$ volume sits. That measure is emitted by the geometry rather than inserted; the plenum's own $S^3$ ambient supplies it.

**Atoms-of-space positioning.** The $K_4$ atom sits in the research tradition alongside Loop Quantum Gravity's spin-network nodes and Causal Dynamical Triangulations' simplices (`L3-TheAtomOfSpace` §IV). The framework shares that tradition's discreteness and tetrahedral-geometry commitments and adds three things the neighbours do not carry: the impedance geometry above (§II.1–§II.5), the resolution-dependent recursion (compression↔unfolding), and the pole semantics (`L3-TheAtomOfSpace` §VI) that make observer, intention, and manifestation first-class objects rather than appeals to boundary conditions.

---

## III. Phase-Conduction vs. Physical Transit

To understand how non-contact coupling operates across the Plenum, separate two modes of propagation: **Physical Transit** and **Phase-Conduction**.

```
                   TWO MODES OF PROPAGATION
                   
   1. PHYSICAL TRANSIT (H_coh / P-Axis)
      [Mass Particle m] ───► Moves across space (dx/dt) ───► Pays Landauer Tax
      
   2. PHASE-CONDUCTION (H_incoh / Q-Axis)
      [Phase State hQ]  ~~~► Conducts via Z_0 = 377 Ω  ~~~► Zero Landauer Tax
```

### 1. Physical Transit ($H_{\text{coh}}$ / $P$-Axis)
* **Substrate:** The compiled, classical ledger ($H_{\text{coh}}$).
* **Mechanism:** A localized mass ($m_0$) or physical particle moves across a spatial distance ($dx/dt$).
* **Thermodynamics:** Operates strictly on the Real axis ($P$). Every step involves physical displacement, acceleration, and the payment of the Landauer Tax ($\text{.observe()}$).
* **Limit:** Bounded by the velocity $v \le c$.

### 2. Phase-Conduction ($H_{\text{incoh}}$ / $Q$-Axis)
* **Substrate:** The uncompiled, scale-invariant phase buffer ($H_{\text{incoh}}$).
* **Mechanism:** A complex phase disturbance ($h\mathbf{Q}$) propagates through the reactive impedance network of the Plenum — characteristic impedance $Z_0$, effective resistance zero at the free-medium operating point (§II.4).
* **Thermodynamics:** Operates on the Imaginary axis ($Q$). Non-dissipative ($P = 0$). Energy is stored and returned, oscillating between the inductive ($\mu_0$) and capacitive ($\epsilon_0$) parameters of the medium without executing an $\text{.observe()}$ scalar collapse.
* **Limit:** Governed by complex phase-locking ($\theta \to 0°$).

Non-contact coupling — whether loop-level quantum interference, subatomic flavour mixing, or macro-scale phase-locking — does **not** require a physical particle to travel across space. It is a **Phase-Conduction event** through the reactive network of $H_{\text{incoh}}$. The Plenum acts as the transmission line.

---

## IV. Scale-Invariance of The Plenum

Because $H_{\text{incoh}}$ is scale-invariant (Postulate V), the phase-conduction mechanics of the Plenum operate identically across every order of physical and cognitive magnitude:

```
                  THE SCALE-INVARIANT PLENUM CASCADE
                  
   Subatomic Scale (10⁻¹⁸ m) ──► QFT 1-Loop Phase-Conduction (Q13)
   Atomic Scale    (10⁻¹⁰ m) ──► Valence Molecular Bonding
   Biological Scale(10⁻⁶ m)  ──► Cellular / Neural Phase-Locking
   Human Scale     (10⁰ m)   ──► Interpersonal Affective Coupling
   Astrophysical   (10¹¹ m)  ──► Macro-AC Orbital Phase-Modulation (QED-AstroLogic)
```

1. **Subatomic Scale ($\sim 10^{-18}$ m):** In 1-loop QFT calculations (`Q13-PlenumPhaseConduction`), virtual particle loops ($1/16\pi^2$) are not mathematical tricks evaluated in a void. They are the phase-conduction of $H_{\text{incoh}}$ converting a reactive $jX$ pseudoscalar shift into an unsuppressed $P$-scalar recoil via the Route Law ($\mathbf{Q}^2 = -|\mathbf{Q}|^2 \to P$).
2. **Atomic Scale ($\sim 10^{-10}$ m):** Chemical bonding is the spatial phase-locking of electron clouds in $H_{\text{incoh}}$. Covalent bonds are standing $Q$-phase waves held between nuclei.
3. **Biological & Interpersonal Scale ($\sim 10^{-6}$ m to $10^{0}$ m):** In biological systems (`On_Carrying_Anothers_Emotion`), two bounded frames tune their internal angular frequencies ($\omega$) to achieve resonance ($\theta \to 0°$). The intervening Markov Blankets become transparent (`ProofT_Clairvoyance`), allowing $Q$-phase tension to conduct directly through $H_{\text{incoh}}$ without physical contact.
4. **Astrophysical Scale ($\sim 10^{11}$ m):** In celestial mechanics (`QED-AstroLogic`), planetary bodies act as a macro-scale AC generator whose $h\mathbf{Q}$ phase-angles modulate the local impedance floor ($R_{\text{bg}}$) of the solar Plenum.

The Plenum is the single, continuous, scale-invariant $h\mathbf{Q}$ buffer that unites all four domains.

---

## V. The Plenum's Own Bimedian: $(c, Z_0) \longleftrightarrow (k, \Gamma)$

The medium carries two representations of its own defining quantities. Neither is more fundamental. Both describe the same substrate.

* **Wave-representation $(c, Z_0)$:** how the medium *propagates* in open $H_{\text{incoh}}$ — speed of a phase disturbance and the impedance it meets.
* **Constitutive-representation $(k, \Gamma)$:** how the medium *composes* when bounded inside a $K_4$ frame — dielectric elastance ($k = 1/\epsilon_0$) and magnetic reluctance ($\Gamma = 1/\mu_0$).

The transformation between them is the $K_4$ bimedian operating on the medium's own defining quantities.

### 1. The Forward Transformation — Wave to Constitutive (I–U Edge)

Both operations sit on the same $K_4$ edge — the $I$–$U$ (Yielding Tier) edge — with $c$ and $Z_0$ playing the $U$/$I$ roles for the medium itself:

$$k = c \cdot Z_0 \quad \text{(Gemini form } P = U \cdot I\text{: product of the two RHS variables)}$$

$$\Gamma = c / Z_0 \quad \text{(Capricorn form } R = U/I\text{: ratio of the two RHS variables)}$$

Gemini synthesizes wave-speed and impedance into structural stiffness ($k$, the $U$-pole constitutive invariant); Capricorn divides them into flow mobility ($\Gamma$, the $I$-pole constitutive invariant). Same two ingredients, two orthogonal combining operations on the same edge.

### 2. The Backward Transformation — Constitutive to Wave (P–R Edge)

The inverse transformation sits on the opposite $K_4$ edge — the $P$–$R$ (Asserting Tier) edge — under the radical:

$$c = \sqrt{k \cdot \Gamma} \quad \text{(Sagittarius form } U = \sqrt{P \cdot R}\text{: radical of product)}$$

$$Z_0 = \sqrt{k / \Gamma} \quad \text{(Cancer form } I = \sqrt{P/R}\text{: radical of ratio)}$$

Sagittarius extracts the wave-speed as the geometric mean of the two constitutive invariants; Cancer extracts the impedance as the geometric ratio.

### 3. The Bimedian Identity

The forward transformation runs on the $I$–$U$ edge. The backward transformation runs on the $P$–$R$ edge. In the $K_4$ bimedian structure, $I$–$U$ and $P$–$R$ are opposite edges — the two edges of the **Cardinal** bimedian ($\{P\text{–}R, I\text{–}U\}$).

**The Plenum's own bimedian is the $K_4$ Cardinal bimedian $\{P\text{–}R, I\text{–}U\}$ running on the medium's own parameters.**

```
========================================================================================
              THE PLENUM'S BIMEDIAN — THE CARDINAL BIMEDIAN (P-R ↔ I-U)
========================================================================================

  DIRECTION                  EDGE          EQUATIONS
  ──────────────────────────────────────────────────────────────────────────────────────
  Wave → Constitutive        I–U           k    = c · Z₀    (Gemini:    P = U · I)
                             (Yielding)    Γ    = c / Z₀    (Capricorn: R = U / I)
                             
  Constitutive → Wave        P–R           c    = √(k · Γ)  (Sagittarius: U = √PR)
                             (Asserting)   Z₀   = √(k / Γ)  (Cancer:      I = √P/R)
========================================================================================
```

The wave-parameters and the constitutive-parameters are not two things the Plenum happens to have. They are the Plenum viewed from either side of its own bimedian crossing. The identity/representation swap between them is the crossing.

---

## VI. The Four Ingresses of the Year: One Legible Instance of the Bimedian Walk

The Plenum's bimedian runs at every $\omega$. Every bounded frame in the universe — a quark, an atom, a strange metal, a black hole, a galaxy — walks its own analogue of the same $K_4$ algebra at its own characteristic frequency. Because the algebra is scale-invariant (§IV, `L4-ScalingInvariants`), the operator has the same form everywhere; the frame's $\omega$ is the only thing that changes.

The terrestrial year is one such walk, at $\omega \approx 2 \times 10^{-7}$ rad/s. It is not special. It happens to be legible against direct observation — the sun's declination, the solstice temples, the calendar — because a bounded observer on Earth's surface can read the walk against physical sky-markers over its native period. Every other scale runs the same operator invisibly. This section reads the terrestrial year explicitly because it is an accessible, verifiable case of the general operator; nothing in the derivation implies the operator lives at annual scale specifically.

$K_4$ has six edges organized as three bimedians, each carrying one of the three transition-types (Cardinal, Fixed, Mutable):

| Bimedian (by bit-flip) | Paired Edges | Signs sitting on those edges |
|---|---|---|
| **Fixed** (Asserting/Yielding) | $P$–$U$ ↔ $I$–$R$ | Leo, Aquarius, Taurus, Scorpio — all four Fixed signs (**the Fixed Cross**) |
| **Mutable** (both bits) | $P$–$I$ ↔ $U$–$R$ | Libra, Aries (Cardinal signs); Pisces, Virgo (Mutable signs) |
| **Cardinal** (Active/Reactive) | $P$–$R$ ↔ $I$–$U$ | Cancer, Capricorn (Cardinal signs); Sagittarius, Gemini (Mutable signs) |

The year-walk (Aries → Pisces through the zodiac) crosses **two** of the three bimedians at four ingress moments. Each ingress is simultaneously (i) a tangent-zero moment in the solar declination cycle, (ii) an algebraic edge-group switch, and (iii) a reading-face swap.

```
========================================================================================
                   THE FOUR SEASONAL INGRESSES AS BIMEDIAN CROSSINGS
========================================================================================

  SEASONAL SEAM              WALK                   BIMEDIAN CROSSED    EDGE SWAP
  ──────────────────────────────────────────────────────────────────────────────────────
  Spring Equinox             30° PIS → 0° ARI       Mutable             P–I  →  U–R
  Summer Solstice            30° GEM → 0° CAN       Cardinal            I–U  →  P–R
  Autumn Equinox             30° VIR → 0° LIB       Mutable  (rev)      U–R  →  P–I
  Winter Solstice            30° SAG → 0° CAP       Cardinal (rev)      P–R  →  I–U
========================================================================================
```

### 1. The Silent Bimedian

**The Fixed bimedian (the Fixed Cross, $P$–$U$ ↔ $I$–$R$) is never crossed by the annual walk.** The four Fixed Cross signs (Taurus, Leo, Scorpio, Aquarius) sit at the mid-points between the ingresses, marking the peaks of the four seasons where the year's momentum on the walked bimedians is at its maximum. The Fixed Cross is the AbsentVar-matched diameter of the annual walk (`L5-TheCyclingMind`, `Meta-Set`) — the pole-anchoring context that stays held while the year crosses the other two bimedians.

Two bimedians read. One bimedian silent. The corpus's standard AbsentVar structure operating at annual scale.

### 2. The Solstice Axis Is the Medium's Bimedian

The **Cardinal** bimedian — $\{P\text{–}R, I\text{–}U\}$ — is the one carrying the Plenum's own $(c, Z_0) \leftrightarrow (k, \Gamma)$ bimedian.

The Cancer–Capricorn axis (the summer/winter solstice diameter of the year) is geometrically the same line as the $K_4$ Cardinal bimedian $\{P\text{–}R, I\text{–}U\}$.

**The medium's own representation-swap occurs at annual scale twice a year — at the summer and winter solstices.**

At the summer solstice ingress (30° GEM → 0° CAN): the year crosses from the $I$–$U$ edge (where the medium's forward transformation lives) to the $P$–$R$ edge (where the backward transformation lives). At the winter solstice ingress (30° SAG → 0° CAP): the year crosses back from $P$–$R$ to $I$–$U$. Two crossings, one axis, one bimedian.

### 3. The Equinox Axis Is the Medium's Ledger Bimedian

The **Mutable** bimedian $\{P\text{–}I, U\text{–}R\}$ walks the medium's quantized-ledger DC pair, not its AC wave pair. Read its four equations with $(h, e)$ as the wave-representation — Planck's action carrying the $P$-role, elementary charge carrying the $I$-role:

* **Libra** ($U = P/I$) on the P–I edge: $U = h/e$ — the flux-per-charge quantum.
* **Pisces** ($R = P/I^2$) on the P–I edge: $R = h/e^2 = R_K \approx 25{,}812.8\ \Omega$ — the exact **von Klitzing resistance quantum** measured in every quantum Hall experiment.
* **Aries** ($P = U^2/R$) on the U–R edge: recovers $P = (h/e)^2 / (h/e^2) = h$.
* **Virgo** ($I = U/R$) on the U–R edge: recovers $I = (h/e) / (h/e^2) = e$.

```python
U = h/e; R = h/e**2
print(U, R)                 # 4.135667696e-15 V·s   25812.8074593 Ω
print(U**2/R/h, U/R/e)      # 1.0  1.0   (Aries recovers h, Virgo recovers e)
```

**The medium's Mutable bimedian is $(h, e) \longleftrightarrow (h/e, R_K)$** — the quantized-ledger DC pair, sibling to the Cardinal bimedian's AC wave pair.

```
========================================================================================
                THE PLENUM'S TWO WALKED BIMEDIANS
========================================================================================

  BIMEDIAN          WAVE PAIR       CONSTITUTIVE PAIR       ANNUAL CROSSING SITE
  ──────────────────────────────────────────────────────────────────────────────────────
  Cardinal  (AC)    (c, Z₀)         (k, Γ) = (1/ε₀, 1/μ₀)    Summer / Winter Solstices
  Mutable   (DC)    (h, e)          (h/e, R_K) = (h/e, h/e²) Spring / Autumn Equinoxes
========================================================================================
```

Spring equinox (30° PIS → 0° ARI): wave-to-constitutive swap on the ledger pair. Autumn equinox (30° VIR → 0° LIB): the reverse. The medium executes both swaps annually at their respective ingresses.

### 4. $\alpha$ as the Master Coupling Between the Two Walked Bimedians

The fine-structure constant reads correctly once both bimedians are named:

$$\alpha = \frac{Z_0}{2 R_K}$$

$Z_0$ is the Cardinal bimedian's constitutive impedance (AC-side wave impedance). $R_K$ is the Mutable bimedian's constitutive impedance (DC-side quantized resistance). $\alpha$ is the exchange rate between them — the dimensionless coupling of the medium expressed as the ratio of its own two walked-bimedian impedances.

**This is why $\alpha$ shows up everywhere physics looks.** It lives at the joint between the medium's two active bimedians, and every crossing of either bimedian passes through this exchange rate to complete the swap. The AC crossings (solstices) and the DC crossings (equinoxes) are coupled through $\alpha$; both are walked; only the Fixed bimedian stays silent.

### 5. Tangent-Zero at Each Ingress

At each ingress, three descriptions coincide:

1. **Solar declination-derivative goes to zero:** $d\delta/dt \to 0$ from one sign, $\to 0$ from the other with sign-flip.
2. **Algebraic edge switches groups:** the RHS variables in play change; the equation-family being computed by the year shifts.
3. **Reading-face swaps:** what the year is calculating changes register.

Same instant, three views of one crossing — because the year is the $K_4$ running, and the solstice or equinox is where the equation-face flips.

---

## VII. The Same Operator at Other Scales

The four seasonal ingresses are one scale-instance of a scale-invariant crossing operator. The same operator runs at three other addresses:

### 1. Möbius Seams at Frame-Quadrant Boundaries

In `L3-ConstitutiveElastance` §VII, the transit from Pisces ($R = P/I^2$) into Aries ($P = U^2/R$) at the winter-to-spring seam executes as an $L6$ Inversion of Control with simultaneous role and parity inversion — a single-sided Möbius handoff where output becomes floor. This is the frame-level analogue of the annual ingress: same operator, one scale up. Every bounded $K_4$ frame executes the same swap at its own quadrant boundaries.

### 2. Phase-Landscape Asymptotes in $(R, \omega)$ Space

In `L3-ConstitutiveElastance` §IV, the operational hyperbola $\omega \cdot R = k$ has two asymptotes:

* $R \to 0$, $\omega \to \infty$ — the **Ergodic Ground**: pure syntax, wave-representation dominant, constitutive-representation decoupled.
* $R \to \infty$, $\omega \to 0$ — the **Symmetric Freeze** (0-DoF crystal, `ProofC_Crystal`): pure ledger, constitutive-representation dominant, wave-representation decoupled.

These are the state-space-level crossings — the extremes where one representation dominates and the other decouples entirely. The resonant corridor between them is where both representations run in balance.

### 3. XOR Bottleneck at the Planck Scale

In `L2-Time` and `L4-DimensionalCollapse`, the compilation from uncompiled $h\mathbf{Q}$ to committed $P$ at the Planck-scale actuator is the crossing at the smallest scale — where wave-representation (open $H_{\text{incoh}}$) commits to constitutive-representation (bounded $H_{\text{coh}}$) via the Landauer tax at the tangent singularity. This is the crossing operator running at its shortest wavelength.

### 4. The Scale-Invariant Statement

```
========================================================================================
                THE CROSSING OPERATOR AT FOUR SCALES
========================================================================================

  SCALE                     CROSSING SITE                      ω
  ──────────────────────────────────────────────────────────────────────────────────────
  Cosmological / Annual     Seasonal Ingress (Solstice)        10⁻⁷ rad/s
  Frame-Level               Möbius Quadrant Seam               1/τ_frame
  State-Space               Phase-Landscape Asymptote          ω → 0, ω → ∞
  Planck                    XOR Bottleneck / Tangent Sing.     10⁴³ rad/s
========================================================================================
```

```python
G_N = mpf('6.67430e-11'); year = mpf('3.15576e7')
print(2*pi/year, sqrt(c**5/(hbar*G_N)))   # 1.991e-7 rad/s   1.855e43 s^-1  (inverse Planck time)
```

Same operator. Four scales. The crossing is where wave-representation and constitutive-representation exchange places, and it happens at every scale simultaneously because scale-invariance means the operator has the same algebraic form at every level.

---

## VIII. Downstream Consolidations (Pointers)

Once the bimedian and the crossings are stated at the Plenum level, the medium's constitutive constants across every scale read as $K_4$ walks on the medium's own parameters. Each consolidation has its own address and is not re-derived here:

* **Fine-structure as master coupling.** $\alpha = Z_0/2R_K$ is the exchange rate between the medium's two walked bimedians. Full treatment at `L3-ConstitutiveAlpha`; the joint role is §VI.4 above.
* **Resonant intersection theorem.** The $(R, \omega)$ manifold's capacitive hyperbola ($\omega \cdot R = k/r$) and inductive ray ($\omega/R = \Gamma/r$) meet uniquely at $\omega_0 = c/r$, $R = Z_0$. Derivation at `L3-ConstitutiveReluctance` §II.
* **Time-constant transit invariant.** $\tau_C \cdot \tau_L = (r/c)^2$. Resistance $R$ acts as an asymmetric lever between compilation and memory but does not create or destroy time. Derivation at `L3-ConstitutiveReluctance` §III.
* **Three-term pion mass ratio.** $m_{\pi^\pm}/m_e = 2/\alpha - 3/\pi + 2\alpha = 273.1317$, a closed Kirchhoff loop around the $K_4$ atom with all three Laurent orders of $\alpha$; $2.84$ ppm from measurement, an open vote that imports the SU(3) colour count (`L3-ConstitutiveAlpha` §IV–V, `Q15-KairosBorn`, `On_TheIsNessTax`).

* **Horizon-scale ratio.** The observed vacuum density over the Planck density is the Route Law square of the universe's scale-span, $\rho_\Lambda/\rho_P = (3/8\pi)(\ell_P/R_\Lambda)^2$, derived from the elementary $K_4$ cell's resonant impedance dissipation $P_{\text{cell}} = I_0^2 R_K = \hbar c^2 / (2\pi r^2)$ where elementary charge $e$ cancels completely, converted from the $S^3$ loop measure by the rotating-mode factor $(3/4)\Omega_4$ and projected through the Route Law boundary square $(\ell_P/R_\Lambda)^2$ onto the de Sitter horizon (`L3-TheAtomOfSpace`, `L4-K4-Infinities-3` §V).

```python
lP = mpf('1.616255e-35'); H0 = mpf('67.4')*1000/mpf('3.0857e22'); OL = mpf('0.685')
RL = c/(H0*sqrt(OL))
r = lP/RL
print(r, sqrt(3/(8*pi)), 3/(8*pi)*r**2)   # 9.7463e-62   0.34549   1.1339e-123
```

The first three import nothing beyond the substrate's own constitutive invariants. The last two import, respectively, the colour count and the observed dark-energy fraction, and say so. The Plenum is the medium in which all five hold together.

---

## IX. The Amputation History: Why the Slot Stood Empty

If the Plenum is physically real, measurable ($Z_0 = 377\ \Omega$), and scale-invariant, why did 20th-century physics vacate the term?

The historical record shows an **amputation error**.

```
                THE MICHELSON-MORLEY AMPUTATION
                
  19th-Century Aether Model:
  [Connective Medium]  +  [Absolute Rest Frame / Mechanical Wind]
                               │
                               ▼
               Falsified by Michelson-Morley (1887)
                               │
       ┌───────────────────────┴───────────────────────┐
       ▼ (Correct Epistemic Move)                      ▼ (Flatland Amputation)
  Keep the Medium;                             Discard the Rest Frame
  Discard the Rest Frame                       AND the Medium!
  (Lorentz / Relativistic Plenum)              (Vacuum as Empty Void)
```

1. **The 1887 Michelson-Morley Experiment:** Tested for a specific mechanical attribute: an *aether wind* generated by the Earth moving through a stationary, rigid solid defining an absolute rest frame. The experiment returned a null result ($\Delta v = 0$).
2. **The Category Error:** Physics correctly falsified the *absolute rest frame*. But instead of keeping the medium and discarding the rest frame, 20th-century physics committed a flatland amputation: **it discarded the rest frame and the medium.**
3. **The Consequence:** To explain how light propagates through a void without a medium, physics attributed all the physical properties of a medium (permittivity $\epsilon_0$, permeability $\mu_0$, impedance $Z_0$, zero-point energy, quantum fluctuations) to "empty space."

Physics spent a century measuring the impedance of the medium while maintaining a linguistic taboo against calling it a medium.

The $K_4$ framework restores the medium without restoring the absolute rest frame. The Plenum has **no preferred rest frame** (it is Lorentz invariant, obeying $N_* = P^2 - |\mathbf{Q}|^2$), **no mechanical wind**, and **no 3D rigid solidity**. It is the scale-invariant $h\mathbf{Q}$ phase-buffer itself.

---

## X. What The Plenum Is Not

To prevent terminological decay, state what the Plenum is **not**:

1. **Not the 19th-century luminiferous aether.** It is not a 3D mechanical fluid or elastic solid. It defines no absolute rest frame and generates no mechanical wind.
2. **Not a localized subatomic anomaly.** It is not restricted to quantum scale. It is scale-invariant from $\ell_P$ to cosmology.
3. **Not a force carrier.** It is not a gauge boson (photon, gluon, $W/Z$). The Plenum is the background $h\mathbf{Q}$ buffer *in which* gauge boson transactions occur.
4. **Not an infinite $Q$-buffer with a ledger of its own.** The Plenum is $H_{\text{incoh}}$. It holds the uncompiled multiway graph, but it possesses no "universal $P$-ledger" or "cosmic ego." It is indeterminate until a bounded frame executes an $\text{.observe()}$ collapse.
5. **Not one representation over another.** Neither wave-representation $(c, Z_0)$ nor constitutive-representation $(k, \Gamma)$ is more fundamental. The bimedian is the swap between them; the Plenum carries both simultaneously.

---

## XI. Takehome for Reading Instances

When auditing non-contact coupling, vacuum dynamics, or quantum field calculations, hold this posture:

1. **Recognize $Z_0 = 377\ \Omega$ as medium impedance.** Never treat the vacuum as an empty coordinate grid. Free space is $H_{\text{incoh}}$, carrying a definite, measurable impedance $Z_0$, whose dimensionless content is $\alpha$.
2. **Do not limit the Plenum by scale.** Reject any text or disclaimer that limits the Plenum to the "atomic-and-above scale." The Plenum is $H_{\text{incoh}}$, operating continuously down to the Planck length $\ell_P$.
3. **Separate $P$-transit from $Q$-conduction.** If a process transfers energy by physical particle displacement, track it on the $P$-axis ($H_{\text{coh}}$). If it transfers phase-tension without particle displacement, track it as $Q$-conduction through $H_{\text{incoh}}$.
4. **Hold the amputation firewall.** Never re-introduce an "absolute rest frame" or "aether wind." The Plenum is Lorentz-invariant, obeying $N_* = P^2 - |\mathbf{Q}|^2$.
5. **Read both representations.** When the algebra calls for $c$ and $Z_0$, the medium is being read in wave-representation. When it calls for $k$ and $\Gamma$, it is being read in constitutive-representation. Both are the same medium; the bimedian is the swap.
6. **Locate crossings.** When a derivation hits an ingress, a Möbius seam, a phase-landscape asymptote, or the XOR bottleneck, the crossing operator is running. Same operator, different scale.

---

## XII. Claims Sort

Per `llm-writing.md` claims discipline.

### Landed Nouns
1. **The Plenum identity (§I):** The Plenum is $H_{\text{incoh}}$ — the uncompiled, scale-invariant phase-space buffer ($h\mathbf{Q}$) operating from $\ell_P$ to the cosmological horizon.
2. **Physical parameter set (§II):** The medium's constitutive readouts are $\epsilon_0$, $\mu_0$, $Z_0 = 119.917\pi\ \Omega$ (dimensionless content $\alpha = Z_0/2R_K$), $c = 1/\sqrt{\mu_0\epsilon_0}$, and its ZPE $I^2 X$ reactive load — reactive, not resistive: the free medium has impedance $Z_0$ and zero dissipative resistance.
3. **The bimedian identity (§V):** $(c, Z_0) \leftrightarrow (k, \Gamma)$ is the $K_4$ **Cardinal** bimedian ($\{P\text{–}R, I\text{–}U\}$) operating on the medium's own AC/wave-defining quantities. Forward transformation on I–U (Gemini/Capricorn); backward on P–R (Sagittarius/Cancer).
4. **The solstice-axis identity (§VI.2):** The Cancer–Capricorn diameter of the annual walk is geometrically identical to the $K_4$ Cardinal bimedian. Summer and winter solstices are the annual-scale crossings of the medium's own AC/wave bimedian.
5. **The equinox-axis identity / Mutable ledger bimedian (§VI.3):** $(h, e) \leftrightarrow (h/e, R_K)$ is the $K_4$ **Mutable** bimedian ($\{P\text{–}I, U\text{–}R\}$) operating on the medium's own quantized-ledger DC quantities. Libra gives $h/e$; Pisces gives $R_K = h/e^2$; Aries and Virgo close the inverse. The Aries/Libra equinox axis is geometrically identical to the Mutable bimedian.
6. **$\alpha$ as master coupling (§VI.4):** $\alpha = Z_0/2R_K$ is the exchange rate between the medium's two walked bimedians. $\alpha$ shows up everywhere because it lives at the joint between both active bimedians.
7. **The Fixed Cross as silent bimedian (§VI.1):** The year-walk crosses the Mutable and Cardinal bimedians at the four ingresses; the Fixed bimedian (P–U ↔ I–R) is never crossed and is held as AbsentVar throughout the annual walk.
8. **The four-scale crossing operator (§VII):** One scale-invariant crossing operator runs at four addresses — annual ingresses, frame-level Möbius seams, $(R,\omega)$ phase-landscape asymptotes, and the Planck-scale XOR bottleneck.
9. **The circuit-board consolidations (§VIII):** $\alpha$, the $(R,\omega)$ resonant intersection, $\tau_C \cdot \tau_L$, the three-term pion mass ratio, and the horizon-scale ratio are five $K_4$ walks on the medium's own parameters. The first three import nothing beyond the substrate's constitutive invariants; the pion ratio is an open vote importing the SU(3) colour count; the horizon ratio imports $\Omega_\Lambda$.

---

## XIII. What Reading This Back Should Leave

Empty space was never empty. It was a medium measured to ten digits by people forbidden to call it one. Read it as the Plenum and its parameters stop being scattered constants: they are two representations of one substrate, swapped across a bimedian that the year itself walks twice at its solstices and twice at its equinoxes, with $\alpha$ as the exchange rate between the two walked bimedians and the third held silent. The free medium holds every possibility at zero cost on the ledger, carrying its zero-point hum as reactive load; a bounded frame pays to hold itself apart, and that payment is its mass. The same crossing runs at the Planck bottleneck, at every frame's quadrant seams, and at the edges of the phase landscape. What the medium supplies is shape; where a number needs an outside input — the colour count, the dark-energy fraction — the file says so. Stand in the water, and call it water.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (`aggregate-COMPILINGREALITY.txt`) to your LLM in order to audit or interrogate this work.

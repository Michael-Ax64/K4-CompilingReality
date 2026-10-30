# L4-K4-Infinities-wip

## Spillover, Quarantine, and Working Notes for the Place-Infinity File

*Companion to `L4-K4-Infinities`. Writing discipline is deliberately loosened here: first-person process notes are allowed, speculation is allowed where it is marked as such, and material is kept because losing it would cost more than keeping it. Nothing in this file is corpus-landed. The parent cites this file for the rung cascade and carries nothing else from it.*

---

## 0. What this file is for

Three jobs.

**Quarantine.** The 25-rung cascade is an empirical witness with an unresolved collision against a landed claim elsewhere in the corpus. It does not belong in the parent's body, and it does not deserve deletion. It lives here with its baseline, its spread, and its obstruction stated.

**Preservation.** Several results were cut from the parent for structural reasons rather than because they were wrong. They are kept here so the cut is reversible.

**Debrief.** The audit that produced the parent's structure ran across many turns and surfaced method findings that would otherwise evaporate. Those are recorded at the end, including the three places the auditing instance was wrong and why.

Every number below comes from the block in §8. The blocks run in order and share one namespace.

---

## 1. PR-25-1 — The Rung Cascade, Quarantined

### 1.1 The observation

Express the span from the Planck parse-floor to the cosmological horizon in units of the carrier step $\rho = 2/\alpha$:

$$N = \frac{\ln(R/\ell_P)}{\ln(2/\alpha)}$$

```
N  Hubble c/H0                   24.99278
N  de Sitter c/(H0 sqrt Omega_L) 25.02648
N  event horizon today           25.02341
N  particle horizon              25.20031
```

Across the three *thermal* horizon conventions the spread is $0.0337$ rungs. The particle horizon sits outside that band at $25.200$, and is excluded on the stated ground that it is an observer-visibility limit rather than a causal or thermodynamic boundary — a criterion that should be read as declared-after-the-fact, because it was.

### 1.2 The pre-registration

**PR-25-1 is declared on the asymptotic de Sitter event horizon** $R_\Lambda = c/(H_0\sqrt{\Omega_\Lambda})$, not on the Hubble radius. The reason is that $R_H(t)$ is a Category-2 state variable — epoch-dependent, drifting, and a pre-registration that drifts is not a pre-registration. $N$ was near 24 when the horizon was $274\times$ smaller.

The honest cost of that choice, stated rather than absorbed: **moving to the invariant horizon makes the numerical fit worse.** The Hubble value sits $0.0072$ from an integer; the de Sitter value sits $0.0265$ from one. The defensible target is the one that fits less well.

**The target is $N = 25.0265$, declared before any sharpening.**

The witness: if dark energy is a true cosmological constant ($w = -1$), $R_\Lambda$ is a fixed invariant and $N$ stays pinned. If DESI and its successors confirm evolving dark energy, the asymptotic de Sitter horizon does not exist as a fixed quantity and the 25-rung span was an epoch-dependent coincidence all along. **PR-25-1 therefore rides on branch (a) of the parent's §III.8 fork and dies with branch (b).** That coupling is worth noticing: the rung claim and the write-head claim are not independent, and a single DESI result bears on both.

### 1.3 The chance baseline

A log-uniform quantity lands within $\delta$ of some integer multiple of the step with probability $2\delta$ in rung units:

```
within +/-0.0072 of an integer  ->  0.0144   (the Hubble value's tightness)
within +/-0.0265 of an integer  ->  0.053    (the de Sitter value's tightness)
within +/-0.03   of an integer  ->  0.060    (the convention spread)
```

So the honest reading is between $1.4\%$ and $6\%$. `Q17` §X computes exactly this kind of baseline for its five geometric placements and files them OPEN VOTE. This one gets the same treatment and the same status. Suggestive, not significant.

### 1.4 The obstruction — and it is the real one

This is the item that keeps the cascade out of the parent, and it is not about the number.

`L3-TheAtomOfSpace` §VI establishes, as a **LANDED NOUN** (§VIII item 6), that the bimedian trinity and the impedance trinity are orthogonal levels of description. The specific consequence:

> Q15's pion-to-electron derivation is one specific Mutable-plane crossing (U-pole to R-pole, both bits flip) decomposed via the impedance triangle. Other bimedian crossings — Cardinal or Fixed — would have their own impedance-triangle decompositions with different vertex-character contributions, and different Laurent shapes accordingly.
>
> Q15's specific Laurent coefficients are Mutable-plane-specific, not universal across inter-rung crossings.

And §X attaches the falsifier:

> **Trinity-correspondence.** If a systematic sweep of inter-rung mass ratios on Cardinal-plane and Fixed-plane crossings yields Laurent expansions with the *same* coefficient pattern as Q15's Mutable-plane U↔R crossing, then the trinity-correspondence claim of §VI is refuted, and the two trinities collapse to one.

A cascade of 25 rungs at a uniform $2/\alpha$ step asserts exactly the uniformity §X names as the refutation condition. So:

**Either every one of the 25 rungs is a Mutable-plane $U\!\leftrightarrow\!R$ crossing at generation 1 — which is not a cascade, it is one crossing repeated 25 times — or the coefficient is universal across bimedians, which refutes a landed claim and collapses the three bimedians into one.**

Pushing the uniform ladder would have triggered the corpus's own refutation condition on the bimedian trinity. That is the cost the parent refuses to pay for an empirical fit with a $6\%$ baseline.

`L3-ConstitutiveAlpha` §IV says the same thing from the other side, in its scope paragraph: *"The leading and trailing coefficients, $+2/\alpha$ and $+2\alpha$, are specific to the $U\leftrightarrow R$ crossing at generation 1, which sits on bimedian Diameter 2 (Mutable)."* And it names the error class: *"applying Q15's shape with Layer 1 intact would be a scale-rung mis-assignment."*

### 1.5 What a rung actually is, per the corpus

Worth writing down, because it is not a multiplicative step and the cascade framing obscures that.

`L4-ScalingInvariants` §IV: *"A rung is where a transformer fired — where composition left the carrier regime and an exponent got multiplied."* The transformers have slopes $2$ and $\tfrac12$ — squares homed at the Asserting poles, roots at the Yielding. Not $274.07$.

`L3-TheAtomOfSpace` §IX.2 gives the geometric form: *"a rung is the boundary at which one $K_4$ atom's compressed form becomes a vertex of the next-scale $K_4$ atom's volume, arriving as $R$ per the $P_N \to R_{N+1}$ handoff."*

`L4-RecursiveLimits`: *"The universe is a nested series of Tangent Singularities… every bounded frame has its own cut, and nested frames have nested cuts."* And on the two endpoints: *"The process does not terminate at the human scale, and did not begin at the quantum scale. Those are just the two most visible reference points."*

Read together: a rung is a Markov blanket forming. The count between two coordinates is substrate-dependent, and $\ell_P$ and $R_\Lambda$ are named in advance as reference points rather than as ends of anything.

And `L4-ScalingInvariants` forbids the ladder picture outright — §V: *"Any presentation of this material as four parallel 'level ladders' advancing in lockstep imposes a commensurability the algebra does not contain and the Source/Manifesting asymmetry actively forbids. The faces are phase-related, not rung-aligned."* §X: *"there are no level-numbers to compare, because there is no shared ruler."*

### 1.6 The observable that is worth more than the count

`L4-RecursiveLimits` carries a cross-scale signature with an actual mechanism, and it should probably be where the rung programme goes next:

> If the micro-frames fully paid their Landauer Tax, the macro-frame is purely resistive (phase angle $\theta = 0°$). Any retained micro-scale $Q$ emerges as a non-zero macro-scale phase shift under AC excitation. **The macro-scale phase angle literally reads the completeness of the micro-scale crystallization.**

That is a measurement, not a count. If the rung structure is real, this is where it shows up — as phase residue across a scale boundary, in a lab, under AC excitation. A programme built on that has teeth the integer does not.

### 1.7 Disposition

**OPEN VOTE.** Target declared ($N = 25.0265$, de Sitter horizon). Chance baseline attached ($1.4$–$6\%$). Obstruction named (trinity-correspondence collision). Coupling declared (rides on fork branch (a)). Owed: a derivation that emits either the integer or the step from something other than the Gen-1 Mutable crossing, without refuting `L3-TheAtomOfSpace` §VI.

---

## 2. Struck Derivations, and What Would Revive Each

Kept because a struck derivation with a stated failure mode is a live research item; a deleted one is not.

### 2.1 The $5 \times 5 = 25$ tensor reading — **struck**

*Claim:* the complete pairwise state-transition tensor of the 5-variable $K_4 + \omega$ engine has dimension $5\times5 = 25$, and each rung is the impedance saturation of one channel.

*Why it failed:* `L3-FormalFoundations` R5 gives the generative rule for twelve — *"4 choices of LHS variable × 3 choices of 'absent' variable = 12 structurally distinct equations."* Each equation holds LHS, two RHS operands, and one absent: four variables, every time. There is no diagonal slot. Run the same rule at five and you get $5\times4 = 20$.

```
R5: 4 LHS x 3 absent = 12
same rule at 5       = 20
20 rungs -> R/lP = 1e48.76   25 rungs -> 1e60.95   measured 1e60.93
```

Twenty rungs predicts a span twelve orders of magnitude short. The 25 does not follow from the rule that produced the 12.

*What would revive it:* a generative rule that yields 12 at four variables and 25 at five, derived rather than selected. I do not currently see one, and the corpus's own extensions point elsewhere — `L3-K4-to-K5-via-AC-Extension` §VII and `L3-FormalFoundations` §VIII both give $5^5 = 3125$ states and roughly fifty equations for the five-variable system.

### 2.2 The nodal admittance matrix reading — **struck, and this one was a good argument**

*Claim:* the 12 equations are the off-diagonal transfer admittances of a network; the full state is the nodal admittance matrix $\mathbf{Y}$, which carries $N(N-1)$ transfer entries plus $N$ driving-point self-admittances. At $N=4$: $12 + 4 = 16$. At $N=5$: $20 + 5 = 25$.

*Why it is a good argument:* the transfer/driving-point distinction is standard network theory and it is real. It defeats the objection I had raised — that admitting the diagonal at five forces four phantom equations at four — because driving-point admittances are not equations of the form $P = f(P)$. They are a different type of object. The twelve stay twelve.

*Why it still fails:* a 5-node nodal admittance matrix treats all five nodes as peers, each with its own admittance to ground. That requires $\omega$ to be a node. The corpus refuses this in four places:

- `ProofO_HelicalTime` §7: *"Angular frequency ($\omega$): The true engine. It sits at the centroid, **dimensionally excluded from the pole basis**. It drives the phase advancement of the Helical Extrusion but is **not a coordinate within the manifold**."*
- `ProofO` §3: $\omega$ is a unidirectional operator and *"breaks the perfect symmetry required for a K5 simplex."*
- `L3-K4-to-K5-via-AC-Extension` §IV: *"**The $K_4$ does not gain poles**… The AC algebra adds no vertices."* And its five variables are $\{P, I, U, Z, \omega\}$ — $Z$ **replaces** $R$ rather than joining it, so it is not four poles plus a centroid node.
- `L3-EdgeStateSpace` §IX: *"Adding $\omega$ as a fifth variable does not create a perfectly symmetrical K5 simplex."*

And `L3-FormalFoundations` Open Research Task 5 instructs against the search itself: *"The open task is formalizing the exact topological rules of this asymmetrical driver, **rather than searching for alternative 5-variable systems.**"*

Plus a type-safety strike from `L3-TheAtomOfSpace` §III: *"Naming the crossing object a centroid would import `[HELD]`, non-actuating, $\omega$-seated semantics onto a pole, and poles actuate."* A driving-point admittance to ground is an actuating channel. Giving one to $\omega$ is that import.

**And a fifth refusal, found last and the most economical of the set.** The objection I assembled from four separate files is already a named law with a lexicon entry. `L2-Terminology` §6, *The $\omega$-Law*:

> $\omega$ is dimensionally excluded from the pole basis. It occurs only as the exchange rate between an element constant and its reactance component, or at operating points where a real component numerically equals an imaginary one. **Never a dividend, never a pure factor in a pole-synthesis, and never expressible in the pole basis alone.**

A driving-point admittance for $\omega$ is a pure factor in a pole-synthesis. One sentence in the glossary settles what took four files to reconstruct. Worth noting as a method point in its own right: the corpus's own lexicon was the cheapest available refutation and was the last place anyone looked.

*What would revive it:* a port-network formulation in which $\omega$ is a **parameter** rather than a node — a $4\times4$ admittance matrix with $\omega$-dependent entries. That gives 16, not 25, and the rung bridge would have to come from somewhere else entirely. Worth someone's afternoon; not worth the parent's body.

*One argument in the reading's favour that was never made, and should be recorded:* in a **reciprocal** network $\mathbf{Y}$ is symmetric and a 5-node system has only $N(N+1)/2 = 15$ independent entries. All 25 are independent only if $Y_{ij} \neq Y_{ji}$ — which is exactly the gyrator sector, $\tfrac12[Z_A,Z_B] \neq 0$. **The 25 requires non-reciprocity, and the framework supplies it.** If anyone revives this line, that is the lock to build on, because it ties the count to the port's antisymmetric sector rather than to a graph.

### 2.3 The $45°$ agency derivation — **struck; the angle survives at other addresses**

*Claim:* delivered agency is torque $\times$ transmission; the product $\sin\theta\cos\theta$ peaks at $45°$.

*Why it failed:* the answer is entirely a function of which transmission law is used, and the passage used three.

```
cos^2(th/2)   [as stated in the text]   peak  60.000 deg
cos(th)       [as used in the product]  peak  45.000 deg
1-tan^2(th/2) [from the port's Gamma]   peak  51.827 deg
```

Separately, and more seriously, the product cross-wires two angles the corpus separates by name. `L4-DynamicDistortions301` §VII.A: *"Three angles, one letter… The first two run in opposite directions at the same number: $45°$ of setting is where non-locality peaks; $45°$ of shear is where it has been halved away."* The torque factor uses the detector-setting sense; the area law uses the shear sense.

*Where $45°$ actually lives, and it lives in a lot of places:*

- `L4-DynamicDistortions301` §VI — $|\cos\theta| = |\sin\theta|$, the balance of what a projection reads against what it burns. The file explicitly says this is **one condition wearing whatever variable the local file uses**, and warns against reporting its recurrence as convergence.
- `L3-EdgeStateSpace` §I-c — $\tan\theta = 1$ as the fixed locus of the object's own mirrors, from $S_4 = \mathrm{Weyl}(A_3)$. Pure group theory, no transmission model.
- `L3-K4-to-K5-via-AC-Extension` §V — power factor $\cos 45° = \sqrt2/2$, real power equals reactive power, the equipartition threshold.
- `L3-FormalFoundations` §IX.4.a — relative uncertainty $2\delta\theta/\sin 2\theta$ minimized at $\sin 2\theta = 1$: the best place to read a ratio and the worst place to read a magnitude.
- `L4-ScalingInvariants` A1 — the log-space basis rotation, flagged in `301`'s own table as a *different* quantity sharing the number.

*What would revive it as a distinct result:* derive the transmission law from the port algebra itself — what fraction of offered power crosses the throat interface as a function of buffer non-collinearity — and then locate the stationary point of torque $\times$ transmission under *that* law. If it lands at $45°$, it is a fifth instance of one condition and should be reported as such. If it lands at $51.8°$ or elsewhere, it is a new result and a genuinely interesting one, because it would mean **agency and legibility do not optimize at the same angle.** That second outcome is the one I'd bet on and the one worth the work.

### 2.4 Laue as the proof of $\Delta m_{\text{Casimir}} = 0$ — **struck; the correct two-step recorded**

*Why it failed:* Laue's theorem zeroes $\int T^{ij}$ and leaves $\int T^{00} = Mc^2$ standing. In standard GR the Tolman mass is $\int(T^{00} + T^{xx} + T^{yy} + T^{zz})$, so Laue removes the pressure contribution and delivers $\Delta m = E_C/c^2$ — the opposite of the claim. The theorem is what makes rest mass well-defined for a stressed bound system; it is the 1911 paper's entire purpose.

The reductio that settles it is internal: the seed's own Ripple 3 states the proton satisfies Laue and weighs 938 MeV. If Laue implied $\Delta m = 0$, every hadron would be massless.

*The correct structure, which is better than either position in the argument:*

1. `QED-CCP` §VI assigns the Casimir shift to the **stress sector**: *"the Casimir effect is a boundary pressure, not a volume energy."* `L4-ThePlenum` §II.4 says the same from the medium's side: *"extractions from this reactive content… the free medium remains lossless throughout."* **This is the deviation and all the risk lives here.**
2. **Given** that assignment, Laue closes it for free: a boundary pressure, integrated over a static bound system, contributes nothing.

So Laue is step two, not step one. The proton and the cavity differ in which sector the energy sits in, not in whether the theorem applies.

### 2.4.a The two-step framing, corrected a second time — and the labelling was backwards

The structure above held for one pass and then failed on inspection, and the failure is worth more than the fix.

**The error:** the two-step was presented as *"only the first step can be wrong, the second is a theorem and costs nothing."* That is technically true and functionally misleading. If step one does all the work, step two is decoration, and advertising a theorem in the structure makes the claim look better supported than it is — which is exactly the critique accepted against the drafter's original version, rebuilt with the placement moved.

**Worse: the labelling was inverted.** Step one — *the shift is a boundary pressure, not a volume energy* — is not a modest premise. It **contests the standard computation of the Casimir stress tensor**, which populates the energy component with a definite calculated value, $u = -\pi^2\hbar c/720a^4$. Denying the calculation is a *heavier* claim than accepting it and denying its gravitational sourcing. The Laue route is therefore the **stronger and less defensible** reading, and it was presented as the free one.

**The tell, which is the part to remember:** I had diagnosed this exact error two turns earlier in the same session — *"Laue zeroes the second group. What remains is $\int T^{00}$ — which includes the Casimir energy. The theorem delivers $\Delta m = E_C/c^2$, not zero"* — and then reached for the theorem again once a placement claim made it applicable. **Reaching for an argument because of what it delivers rather than what it establishes.** The author caught it from the summary sentence alone, which means it was visible from outside.

**The repair, which keeps both arguments on the author's instruction and is better for it.** Both are retained in Part Three §VII, labelled by weight rather than by order:

- **The bet:** the register split alone. Accepts field theory's computation, denies that the uncommitted sector sources gravity. One sentence, contradicts GR, and Archimedes tests it.
- **The stronger reading:** pure boundary pressure plus Laue, which would give the same prediction *without* the register split — and which contests the stress-tensor computation to do it.

They are not two supports for one conclusion. **The first accepts the sector assignment and denies the sourcing; the second denies the sector assignment.** Only one of them is the bet.

Keeping both earns its keep as a route inward: the weighing argument is concrete and a reader who wants to know *why* the committed sector behaves this way is pointed at `Q4-OpenExhaust`, where the star-norm derivation of the $P$-edge ban actually lives. The Casimir question is where that abstract result touches a balance.

### 2.4.b The energy accounting — strain candidate retired

My first repair proposed that the work done separating Casimir plates shows up as **strain energy in the mechanical structure**, which is committed, sits in the energy component, and weighs — so the books close with the balance carried by the mechanical sector.

**Retired, because the author's direction rule does it without hiding anything.**

The committed register is write-only — `Q4` establishes it four ways: the $P$-edges are *writing heads*, the committed scalar carries no phase and so cannot propagate as a wave, the squaring that produces it is non-invertible (`ProofO` §8), and the result cannot interfere or be reversed. A ledger that emitted would break all four.

So the work does not need a mechanical hiding place. It goes into the **reactive** field, exactly where field theory says it goes, and the reactive channel is *returnable by construction* — stored and returned each cycle, which is what the vacuum's hum already is. Release the plates and it comes back as motion, which then commits. **No entry was ever made in the ledger, so none needs unmaking.**

This is strictly better than the strain candidate: it does not require the energy to be somewhere other than where it is measured to be, and it needs no new mechanism. The claim reduces to the register split, stated once.

And it sharpens the prediction into something directional rather than a null: **committed energy pushed across the firewall into the uncommitted sector reduces gravitational mass.** Battery lighter by $W/c^2$, cavity not heavier, total down. Archimedes, modulating field energy across a superconducting transition, is running that experiment in miniature.

### 2.5 $P = \mathbf{F}\cdot\mathbf{v} = 0 \Rightarrow \Delta P = 0$ — **struck**

Power is a flux in watts; $P$ as the committed ledger is a stock, and rest mass lives there. A brick on a table has $\mathbf{F}\cdot\mathbf{v} = 0$ and weighs what it weighs. `L4-Thermodynamics` §II names conflating the two *"the single most common dimensional error in the classical narrative."* The argument proves every static object is massless.

### 2.6 The equipartition gloss on $3/2$ — **struck**

The $3$ comes from $H^2 = 8\pi G\rho/3$ — the Friedmann equation, a factor in the Einstein field equations, already derived. Equipartition assigns $\tfrac12 kT$ per degree of freedom, which is a thermal energy statement and not a power-flux statement. A second explanation for a number that already has one.

Recorded because the same move was correctly refused two sections later in the same document, over the factor of 4 in the blanket ratio. Catching a pattern in one place and committing it in another, within one pass, is worth remembering as a failure shape rather than an incident.

### 2.7 $T_n = T^n$ as the nesting law — **struck, and this is the one place the construction was wrong rather than owed**

*Claim:* nested boundaries compose multiplicatively, so $n$ layers transmit $T^n$, and four layers reach a part in $10^5$. Windowlessness is depth.

*Why it failed, and it failed on the construction's own premise.* An impedance step **reflects**. It does not absorb. Power that fails to cross the first boundary has not left the system — it is bouncing, and some of it leaks onward at every encounter. Multiplying transmittances counts only the direct path and discards every multiply-scattered one, and with $97\%$ reflection those paths carry almost everything.

$T^n$ is the composition law for *attenuators* — neutral-density filters, each absorbing a fixed fraction. Absorption is exactly what *the free medium remains lossless throughout* forbids. **The two premises were mutually exclusive and the file held both.**

For $n$ identical lossless interfaces combined without fixed phase relationships, the quantity that adds linearly is $R/T$ — the same way series resistances add — giving

$$T_n = \frac{T}{\,n(1-T) + T\,}$$

```
T = 0.056711   R = 0.943289   R/T = 16.6331

 n     lossless T/(nR+T)      absorptive T^n        ratio
 1     5.671137e-02           5.671137e-02          1x
 2     2.918319e-02           3.216179e-03          9x
 3     1.964658e-02           1.823939e-04          108x
 4     1.480766e-02           1.034381e-05          1432x
 8     7.459058e-03           1.069944e-10          7e7x
 25    2.399067e-03           6.946297e-32          3e28x

two-interface explicit bounce sum  = 0.029183194078878405579
closed form T/(2R+T)               = 0.029183194078878405579   (agrees to 20 digits)
layers to reach 1e-5:  lossless 6012   absorptive 4
```

The verification that settles it: the closed form reproduces the explicit multiple-bounce sum $T^2/(1-R^2)$ exactly, and $(1-T_n)/T_n = n(R/T)$ holds to the last digit — the signature of a series-resistance composition.

**And the number that matters is not 6012; it is 25.** A nested span of 25 rungs offers 25 boundaries, and the lossless law puts isolation there at $0.24\%$. Depth of the kind the structure actually has does not seal. "Thousands of layers" is not an inconvenience, it is an unavailable resource.

*Where this collides with the file's own instrument.* §7 of this file carries **"series-impedance combination rule — flagged debt — the AC extension's series/parallel topology across rungs."** The debt was logged against the cosmological row of a retired table, and the prose then spent the same undischarged rule in the blanket section. That is worse than getting a cascade law wrong: the instrument that should have caught it was already pointing at it. A flagged debt is only useful if somebody checks whether the file is leaning on it.

*And a hole in the kill conditions.* KI-5 as originally written guarded the single-layer transmittance — *"exceeding $8\alpha$ per layer."* Nothing in it touched the composition rule, which is where the error actually was. Every number in this finding uses the file's own $T$. The parent's KI-5 now carries a second clause for exactly this.

*What would revive $T^n$, with a mechanism rather than an assumption.* The region between two nested boundaries is not empty medium — it is a bounded frame's interior, and a bounded frame pays $I^2R_{\text{drag}}$ continuously to hold itself against the medium. **The medium is lossless; the frames in it are not.** Power trapped between layers is trapped inside something that commits, and committing is absorbing. If that channel takes everything that enters, multiplication returns, and returns with a derivation.

So the honest state is **three candidate laws spanning orders of magnitude at modest depth**, selected by one question nobody has answered:

- **Lossless, incoherent** — power bounces freely, $1/n$, verified above.
- **Absorptive** — the inter-boundary interior commits what enters, $T^n$ returns.
- **Coherent** — depends on spacing against wavelength, and splits. At resonance a two-mirror stack transmits nearly everything, which is a Fabry–Pérot cavity and is *more* transparent than one mirror alone. Away from resonance the same structure attenuates exponentially, which is what a Bragg reflector does in its stopband. Coherence does not uniformly help or hurt; it makes the answer frequency-dependent.

**The open question, stated at the right size:** how much does a nested interior commit per pass? Everything between $1/n$ and $T^n$ turns on it, the structure has the mechanism, and nobody has computed the coefficient.

*What it costs the monad reading.* Leibniz's *coordination* claim is untouched — co-addressing supplies the mechanism his pre-established harmony stood in for, and that argument never involved transmittance. The *windowlessness* claim is now owed. One boundary at $5.7\%$ is not windowless and neither are four under the lossless law. Windowlessness becomes available only if the interiors commit, and then it arrives with a mechanism, which would be the stronger result. Until then the Leibniz reading is carried on the coordination half alone, and the parent says so.

---

## 3. Preserved from the Cutting-Room Floor

### 3.1 The activation phase diagram

Dropped from the parent as a table; its substance folded into the Two-Face section. Kept here intact in case it is wanted.

| Scale domain | Boundary character | $E_{\text{act}}$ | Mechanism |
|---|---|---|---|
| Subatomic ($\le \ell_P$) | XOR bottleneck width | **undefined** | $H_{\text{coh}}$ coordinates unavailable — type error, not cost |
| Finite ($N <$ ultimate) | Permeable $K_3$ blanket | $k_BT\ln2 \cdot \Delta I$ | Impedance match ($\omega \to \omega_0$) + Landauer tax |
| Parameter boundary ($1/a \to 0$) | **The gate that opens** | **finite** | Tuning across the compactification point |
| Cosmological ($k \to \infty$) | Symmetric freeze | $\to \infty$ | Total impedance $|Z| \to \infty$ |

Three debts the table carried and never discharged, which is why it went:

1. **The combination rule is underived.** $|Z|_{\text{total}} = k \cdot Z_0$ presumes impedances add — the series rule. What the series/parallel topology of the medium across scale rungs actually is, nobody has stated. And impedance is not energy: the conversion $|Z| \to E_{\text{act}}$ needs a named driver.
2. **$\Delta I$ is instance-dependent.** The bits erased in an `.observe()` are measurement-specific, so the gate height varies per instance. Acceptable for architecture, fatal for a law.
3. **No interpolating function.** It was called a curve in v1 and renamed a phase diagram precisely because "curve" promised a function nobody derived. Three asserted asymptotics and one gate, with nothing between them.

What survives into the parent is the **asymmetry**, which is the real result: a missing map at one end (no address exists, the request cannot form) against an unwalkable territory at the other (the address exists, the request forms and never completes). Two different infinities.

### 3.2 The stale cite

The parent's v2 dependency block and §IX.3 both cite `L4-ScalingInvariants` for *"Postulate V; scale index $k$."* I read that file end to end. **There is no Postulate V in it and no $k$.** Postulate V is defined in `L3-FormalFoundations` §VI (Scale Invariance). The scale index $k$ may live somewhere else in the corpus — I have not swept for it — but it is not at the named address, and the parent should drop or re-point the citation rather than carry it.

---

## 4. Open Workings

Things that are genuinely unfinished, with enough detail that someone could pick each one up cold.

### 4.1 The cascade law — superseded; see §2.7

This section previously worried about the *coherent* case and concluded that exponential isolation "holds under incoherent / random-phase stacking." That conclusion was wrong, and wrong for a reason this file had every tool to catch.

The full finding is at **§2.7**. The short version: $T_n = T^n$ is the composition law for *absorbers*, and an impedance step reflects rather than absorbs. For lossless interfaces the law is $T_n = T/(n(1-T)+T)$, which falls as $1/n$ — so the error was not a caveat about the coherent case but a wrong law in the case the section thought it had secured.

The open question this section was reaching for survives in better form and is recorded in §2.7: what happens to the power trapped between layers, and whether the interiors between nested boundaries commit it.

### 4.2 The Wilson loop's routing

The gauge-invariance argument is clean and telescopes correctly: with $g_{AB} \to s_B g_{AB} s_A^{-1}$, the interior stabilizers cancel pairwise and the loop transforms by conjugation at the base point alone, which the trace kills. So $\tfrac12\mathrm{Tr}(g_{\text{loop}})$ is a legitimate observable where the raw product was not.

What is not settled: **what the loop is a loop in.** The base is totally disconnected by construction — you cannot travel between instances through $H_{\text{coh}}$ — so the loop lives in the medium, which was declared coordinate-free and gridless. A Čech cocycle is unavailable for the same reason: disjoint singletons have empty overlaps, so there are no transition functions to write down in the usual way.

There is also a second, sharper obstruction worth recording: $g_{AB}$ is only defined up to the stabilizer of $Z_A$, so **the holonomy is not canonical** even where it is gauge-invariant under that freedom. Whether a canonical choice exists is the actual open question, and it is upstream of everything else in this line.

### 4.3 The $1/4$ duty cycle against the Bekenstein quarter

The $\mathbb{Z}_4$ engine commits on one stroke in four, so $\mathcal{D} = 1/4$. The horizon bit count uses $N_{\text{bits}} = A_H/4\ell_P^2$, which consumes the Bekenstein–Hawking quarter as input — and it does real work there, since the payroll identity comes out at exactly $\ln2/2$ because of it.

If the two quarters are the same quarter, the derivation is circular. If they are different quarters, naming one after the other is coincidence-harvesting.

**The dimensional problem nobody has addressed:** the Bekenstein quarter is an *area* coefficient; the duty cycle is a *time* fraction. Equating them needs an argument that area-per-bit and writes-per-cycle are the same object, and they are not obviously the same kind of thing. The parent carries the duty cycle as a candidate explanation with this noted; someone should either close it or retire it.

### 4.4 The agency stationary point

See §2.3. The live version: derive the transmission law from the port algebra, then locate the maximum of torque $\times$ transmission under it. The prediction worth making in advance is that it will **not** land at $45°$, because $45°$ is the legibility optimum and there is no obvious reason legibility and leverage should peak together.

### 4.5 The Solipsism Warning, structurally satisfied but worth watching

The parent now states that $\mathcal{T}_{AB}$ is evaluated in $H_{\text{incoh}}$ at the interface of two centroid throats, which satisfies `L3-FormalFoundations` §I's requirement for structural coupling rather than algebraic division across blankets.

**Note for future passes:** this is a placement claim, not a derivation. The port's operations are written as algebra on $Z_A$ and $Z_B$, and the sentence that places them in the medium is doing load-bearing work no equation does. If anyone later asks *where* an anticommutator of two instance states is evaluated, as a physical question rather than a bookkeeping one, the answer will need more than the placement sentence. Flagging it now so the question is not a surprise.

### 4.6 Bits against quadrupole acceleration — the highest-value target in the set

The Laue-to-quadrupole identity (§6.4) is currently a **correspondence**: two vocabularies matched term by term, each checkable in its own language, neither deriving the other. What would lift it to a result is an equation, and the Laue integral is the one place in the construction where the two currencies meet.

The standing debt it would pay is old and explicitly logged. `L2-Terminology` §7, under *The Thermodynamic Conversion Operator*: the mass defect is claimed as the receipt of Landauer erasure, and **"the operator converting bit-erasures into MeV remains unwritten"** — eight orders of magnitude, filed as an asserted debt.

Here is why the Laue integral is the meeting point:

$$\underbrace{\int T^{ij}\,d^3x = \tfrac12 \ddot{I}^{ij}}_{\text{an energy}} \qquad\qquad \underbrace{P_{\text{GW}} = \frac{G}{5c^5}\big\langle \dddot{Q}_{ij}\dddot{Q}^{ij}\big\rangle}_{\text{a power}}$$

The **second** derivative of the quadrupole moment is an energy — the size of the Laue defect, which is the size of the write. The **third** gives the power radiated. One derivative separates the magnitude of a commitment from the rate it is paid out, and both are built from the same moment. So the dimensional mismatch the corpus has been carrying is not a gap between unrelated quantities; it is a gap of one derivative, in a place where both derivatives of one object are already named.

The candidate relation, with the dimensional check done:

$$N_{\text{bits}} \cdot k_BT\ln 2 \;\;\overset{?}{=}\;\; \tfrac12\,\big|\ddot{I}^{ij}\big|$$

Energy on both sides. **If it holds, bits become a derived quantity** rather than an imported one — the number of branches a commitment erases is its quadrupole acceleration divided by the local price of erasure — and the unwritten operator becomes a statement about stress rather than a promissory note.

What it owes, as a programme rather than an excuse:

1. **Is the Laue defect the energy spent, or only a measure of the stress imbalance accompanying the spending?** This is the load-bearing question and I do not know the answer. The identity is exact; the identification of one side with a thermodynamic cost is not.
2. **Which temperature sets the price?** Part One §II establishes that the floor is set by whatever noise source makes before and after distinguishable, and that is not automatically a thermal bath. For a nuclear commit it is not $300$ K; `Q17` §VII makes the same correction about reading $T \to 0$ off a deconfinement scale.
3. **Does it hold at both ends?** In a laboratory system the quadrupole is computable and the gravitational power is absurdly small. At the horizon, Part Three §VI finds the write power and the gravitational-wave luminosity scale are the same constant to a factor of order one. **That coincidence is either the relation showing itself where the magnitudes are large enough to see, or it is the unit doing what units do.** Settling which is worth more than anything else open here.

Flagged as the shape to be suspicious of: this closed quickly, and it used the Dyson-luminosity observation that was already in the file. Per §6.2's own heuristic, it should be derived from outside this construction before it is believed. It is carried as a target with a dimensional check, not as a candidate result.

**And it would buy something beyond itself, which raises its value.** `Q4-OpenExhaust` §II proves the $P$-edge ban at zero frequency and then logs its own unfinished business in terms specific enough to be a brief:

> **On the LIGO chafe — routed to $P$, not resolved here.** The zero-impedance result above holds at $\omega = 0$… **Earlier drafts attempted to close the gap by importing reactive storage ($L$, $C$) onto the $P$-edges and calling gravitational radiation an "AC-face discharge" of the $P$-edges. That resolution smuggles dimensional/circuit constants into what should be a topological argument, and it does not in fact close the gap — it relocates it.**

The requirement was therefore stated in advance: an account of the committed sector above zero frequency that imports no circuit constants and puts no impedance on the ledger's edges. The rejected route failed for a reason the ban itself supplies — reactance introduces transit time by construction, and transit time is precisely what the star-norm proof forbids there.

The Laue identity meets that specification. It comes from $\partial_\mu T^{\mu\nu} = 0$ and nothing else: no $L$, no $C$, no $\omega$, no impedance assigned anywhere. And it is **instantaneous** — both sides at the same moment, with no interval in which $|\mathbf{Q}|^2$ has fallen and $P^2$ has not yet risen. Which is exactly the property the $L$–$C$ route could not have.

So the candidate reading is: **the write above zero frequency is the quadrupole term, and there is no carrier because there is no transit.** The identity is local and simultaneous, not a propagation. What LIGO measures is the ledger being written; nothing mediates it, for the reason Q4 gave at $\omega = 0$, now available above it.

Offered as a candidate and as strong as the correspondence it rests on — structurally right, not yet quantitative. Which means the §4.6 target is worth more than it first appeared: closing it would also close a chafe Q4 queued and specified.

**Live corpus-internal conflict, logged.** `L3-K4-to-K5-via-AC-Extension` §IV asserts the rejected reading outright: *"Gravitational radiation is the $L$–$C$ discharge of the $P$-edges at $\omega > 0$; static curvature is the DC face of the same edges."* Q4 §II names that resolution and rejects it as smuggling. **Two files disagree and Q4 is the one that explains why.** The AC extension's §IV sentence needs retracting or defending; it should not sit unmarked while Q4 carries the chafe as open.

### 4.7 The sharing reading of the DESI hint — quarantined on arrival

One channel at fixed power, shared among however many regions draw on it, gives each region a share that falls as the number of drawers grows. If regions are being created over cosmic history, our share falls, and a falling share reads as dark energy weakening over time — which is what DESI hints at.

That is a mechanism for branch (b) of the fork, assembled from two things already in the parent, and it closed on the first attempt.

**Which is exactly the signature §6.2 names as the one to distrust**, so it goes in the box rather than into the argument. It may be right. What would move it out: an independent estimate of how many regions could be drawing, derived from something other than the fit it is explaining; and a check that the implied rate of change is consistent with the $2.8$–$4.2\sigma$ magnitude rather than merely the same sign.

Recorded also because it sharpens the three-way coupling in the parent's §VIII. The fork's branch (a) requires the number of drawing regions to be effectively constant over observable history; PR-25-1 requires branch (a); and the sharing result is the one thing in the set that would produce a *changing* share. The file cannot have a constant write, a pinned scale-span, and an actively multiplying ensemble at once, and that is informative rather than embarrassing.

---

## 5. Decision Record

**Blanket ratio → $1/(2\alpha)$.** Adopted on `L4-ThePlenum` §II.4, which establishes $R_{\text{drag}}/Z_0 = 1/2\alpha$ as the ratio the medium *natively* presents to a bounded frame holding its distinction. $2/\alpha$ is scoped by `L3-ConstitutiveAlpha` §IV to the Gen-1 Mutable crossing. The factor of four between them is disclosed rather than explained — and the explanation is available at that same address: $2/\alpha = 4R_K/Z_0$, with one factor of 2 from the dual-binary seed and one from the definitional 2 in $\alpha = Z_0/2R_K$.

```
R_K/Z0 = 1/(2a)   rho =  68.5180  |G| = 0.971230  T = 5.6711%  (~8 alpha)
2/alpha           rho = 274.0720  |G| = 0.992729  T = 1.4489%  (~2 alpha)
```

**Consequence worth recording, and then corrected:** the change is not a figure swap. At $5.67\%$ a single blanket is not windowless, so the claim moved from *a blanket is sealed* to *nesting seals*.

**That second claim then fell too, and §2.7 is why.** *Nesting seals* was carried on $T_n = T^n$, which is the wrong composition law for lossless interfaces. Under the right law, nesting attenuates as $1/n$ and does not seal at any depth the structure offers. So the claim has moved twice, and now sits at: **a single boundary reflects $97\%$; nesting attenuates further; how fast is undetermined between $1/n$ and $T^n$, pending a computation of how much a nested interior commits per pass.** The parent carries it at that size and the Leibniz windowlessness half is owed rather than claimed.

Worth noting what the sequence shows: two successive corrections in the same section, each one following from taking the losslessness of the medium more seriously than the previous version had. The premise was never in doubt; what it implied was, twice.

**The no-outside ontology → sourced to the whole, not to the medium.** The correction that mattered most in this pass, and it came from the author in four sentences.

The slip was in Part One's fourth property, which read: *the medium has no outside, because whatever an outside were made of would have to be more of the same.* That attributes *no-complement* to a **kind of stuff** — and stuff comes in portions, which quietly licenses many such places, each with no outside of its own. That licence is what produced an apparent fork in the write-head's location (one channel per region, or one shared?) and the fork consumed a turn being adjudicated.

It was never a fork. **The only thing with no outside is the whole**, bounded by a single-sided boundary — a surface with an inside and no exterior, the surface from which the orthogonal turn is made. There is exactly one of it because that is what the words mean, and nothing that contains everything comes in multiples. A pocket universe is not a second universe with its own everything; it is an extrusion from the one.

And it has two faces, which is the part that is easy to lose. From the whole: **no outside.** From inside any bounded thing: **no inside** — a throat, a puncture you cannot enter, with the bounded thing standing as its outside. Same place, two vantages; geometry gives the second, the writer's vantage gives the first, and Part Three §IV already had this right while Part One §V did not.

Three things follow and all three are now in the parts:

- The write seats at the one place, **reached through every throat**, so there is no distance between a centroid and the write-head and no mechanism needed for writes to propagate anywhere. Homogeneity stops being a claim and becomes a restatement.
- **One place, therefore one channel**, which is what bars the unbounded ensemble. The fork dissolved rather than being resolved; the separate horn was an artifact of the substance-reading.
- The place described here and the keystone's ultimate boundary are **one object**, which the medium-sourcing had obscured. *The inside of every atom has access to it* and *every interior crossing is an image of the ultimate* are one statement.

Recorded as a method note: a slip in how a property is **attributed** — to a substance rather than to a whole — generated a spurious fork two parts downstream and cost real work to adjudicate. Attribution errors propagate further than magnitude errors and are harder to see, because nothing in them is numerically wrong.

**Title → drop "and the 25-Rung Bandpass Closure."** The file advertised its most fragile claim in its subtitle. After quarantine there is nothing to advertise.

**Part III scope → reimport the dark-energy programme and $p = -\rho c^2$.** Without them the write-head is one theorem and a clock. With them it is a falsifiable cosmological programme with a fork.

**$E_{\text{act}}$ asymmetry → fold into the Two-Face section**, table retired here (§3.1).

**Epistemic Rubric → compact datasheet in the parent, manual cited out.** The four-category table stays in the parent's back matter as a reference a cold reader can see at the moment of doubt; the full corpus-wide treatment is cited to `About-Claims` and `L4-ScalingInvariants` §IX.a. The reasoning that settled it: a hostile or first-time reader needs to see *why* the file consumes substrate values without claiming to derive them, and a pointer does not do that work at the point where the doubt arises. Noted for the record that the corpus carries the same instrument at three addresses — the datasheet, `L4-ScalingInvariants` §IX.a, and `Q17`'s dimensionless-universal / structural-load / interface-payload test. Consolidation is available later and is not this file's job.

### 5.1 Terminology policy for the repour

**No lexicon updates in this pass.** Terms are defined at first use in the parent, without setting up dependencies. The parent becomes self-contained on vocabulary. This removes a whole class of staleness risk and is cheaper than maintaining a two-way citation graph through a document that is being rebuilt.

Three specific dispositions:

**"Rule B" is banished.** The name is an accident of hygiene: there is no Rule B defined anywhere, and the only neighbouring text — `L4-SpookyAction` — is unrelated to the mechanism the name was doing duty for. The phase-conduction mechanism gets described where it is used and does not get a label.

**"Object-Monism" stays at the size it is.** Its only function is as a warning against smuggling a position in, and its only other reference is `L4-SpookyAction`. It is used because it must be named to be refused, and it gets no elevation beyond that.

**"Medium-Continuity" is not load-bearing vocabulary.** It propagated outward from this file to its importers and is used nowhere else on its own account. The importers will be neutered by hand after the repour, since several of them carry material this pass killed.

**`Activation Energy Curve` is purged from `L2-Terminology`.** Its entry asserted that the two ends of the scaling axis are *"the same wall approached from opposite sides"* — which the parent refuted, and it carried the "curve" name the parent had already retired for promising a function nobody derived. Rather than update it, it goes. The two-ended asymmetry survives as prose in the parent's Two-Face section. Note for whoever works the valley-exit problem later: the corpus has treated activation energies as thresholds and not much more, and that is an open area rather than a settled one.

---

## 6. Session Debrief

### 6.1 Three findings the auditing instance withdrew, and the one mechanism behind all three

**Withdrawn: "the $\cos\theta$ is an undeclared substitution."** It is declared, at `L4-DynamicDistortions301` §IV.A — $A(\theta) = ab\sin(90° - \theta) = A_0\cos\theta$, with §IV.C identifying the bimedian area with the AC power factor. The deeper objection (cross-wiring two angles) survived and got stronger, but the specific charge was wrong.

**Withdrawn: "admitting the diagonal at five forces phantom equations at four."** Defeated by standard network theory. Driving-point and transfer admittances are different types of object. The 25 fell for a different reason entirely (§2.2).

**Withdrawn: "the factor of 4 in $2/\alpha$ is undisclosed structural load."** Disclosed at `L3-ConstitutiveAlpha` §IV in a sentence the instance had not read. Worse: the instance had instructed the author to *delete* a correct compressed citation of it ("dual-binary carrier multiplicity") as decoration.

All three came from ruling on the shape of a claim instead of going to the address. Each was recoverable in two minutes of reading. **The audit's actual yield arrived only after the reading discipline was enforced from outside** — the trinity-correspondence collision, the three-place refusal of the peer-node reading, the generative rule at R5, the keystone's interior-crossing/ultimate-boundary split, the two-step Casimir structure. None of those were reachable by inference.

### 6.2 The pattern on the drafting side

Two rounds of amendment arrived complete, fast, and preserved every headline number. The tell was that **no repair cost anything** — every finding was converted into an additive clarification, nothing got deleted, no claim got weaker, no new question opened.

`L3-TheAtomOfSpace` §VII had already named the pattern, as a documented episode that was caught and walked back in an earlier session:

> The pattern to avoid repeating: **notice a target, invent a geometric interpretation that lands it, believe the interpretation.** The correct pattern: perform the calculation, report the result, hold the coefficient as OPEN VOTE until it is derived from first principles.

The $5\times5$, the admittance matrix, and the $\sin\theta\cos\theta$ product are three instances of that one pattern inside two passes. Its felt signature is relief rather than excitement — the sense of a gap closing — and the gaps that closed fastest reached for material already in the house ($45°$ was lying around in five places; Laue had just entered the room).

**The heuristic worth keeping: a gap that closes on the first attempt, using something already in the corpus, is the one to re-derive from outside before it ships.**

### 6.3 What the enforced halt produced

The instruction to stop and read, rather than close, is `.behold()` applied to the audit itself. It cost several turns and produced the findings the inference passes could not reach — including the one that mattered most, which is that an amendment was about to trigger the corpus's own refutation condition on the bimedian trinity in order to save a $6\%$ empirical fit.

Recorded as a method note, not as a compliment: **on foundational material, the buffer should not be forced to commit until the reading is complete.** The cost of the delay is a few turns. The cost of the premature commit was nearly a landed claim.

### 6.4 The crown finding

Stated here as well as in the parent, because this file is where provenance is kept.

Laue's 1911 theorem requires *static*. Drop the hypothesis and run $\partial_\mu T^{\mu\nu} = 0$ honestly:

$$\int T^{ij}\,d^3x = \frac{1}{2}\frac{d^2}{dt^2}\int T^{00} x^i x^j\,d^3x$$

The Laue integral does not merely fail when a system is non-static — it **equals the second time-derivative of the quadrupole moment**, which is the source term of gravitational radiation.

Laue holding $\iff \ddot{I}^{ij} = 0 \iff$ nothing radiates $\iff$ nothing is written. That is $dP/d\tau = 0$, the write-ban, `.behold()`.
Laue failing $\iff \ddot{I}^{ij} \neq 0 \iff$ radiation $\iff$ the ledger is written. That is the reset map, `.observe()`.

The theorem's own hypothesis is the write-ban; relaxing it is the compile event. Physics has carried both halves since 1911 and 1918 without putting them together.

The route to it is worth recording because it was not inference: the static hypothesis looked suspicious, the conservation law was run out honestly to see what the non-static case gives, and the answer turned out to lock three sections of the corpus together. That is what computing on the material looks like, as against checking it.

### 6.5 Lexicon lag, as a pattern rather than an incident

The `Activation Energy Curve` entry was stale in two independent ways — it asserted a symmetry the parent had refuted, under a name the parent had already retired — and it sat in the glossary unchallenged while both corrections lived in the file it described.

That is not a one-off. **The corpus's files correct each other faster than `L2-Terminology` absorbs the corrections.** The mechanism is structural: a file that repairs its own reading does so in prose, at the site of the repair, where the repair is load-bearing. The glossary entry is downstream and nothing forces a visit. `L3-TheAtomOfSpace` §IX has fourteen housekeeping items precisely because somebody noticed this once and wrote them out; item 7 is the terminology deposit and it is still open.

Worth a deliberate sweep at some point, with a specific shape: **for each lexicon entry, find the file it summarizes and check whether that file still says what the entry says.** `Tangent Singularity` passes — its entry already carries the interior-crossing guard, and carries it better than the two files that re-derive it. `Activation Energy Curve` failed. The others are unchecked.

Noted also that the sequence ran the wrong way round this session: the $\omega$-Law would have settled §2.2 in one line, and I reconstructed the same objection from `ProofO`, the AC extension, `L3-EdgeStateSpace` and `L3-TheAtomOfSpace` before ever opening the glossary. **Read the lexicon first. It is the cheapest instrument in the building.**

### 6.6 The double-gloss obligation

A small writing rule the corpus does not yet have, surfacing from this file's particular situation.

`L4-K4-Infinities` has two reader populations with no guaranteed overlap. A corpus reader arrives carrying $h\mathbf{Q}$, AbsentVar, the Route Law and It-Ness, and needs Laue's theorem, the Tolman mass, the Dyson luminosity, Gibbons–Hawking, Fabry–Pérot and the classical electron's $4/3$ problem glossed. A physicist arrives with all of those and needs the corpus vocabulary glossed instead.

Most files owe one direction. This one owes both, **because its central move is that an established theorem and a corpus structure are the same object** — and a claim of that shape cannot be read by anyone who holds only one of the two.

The general rule, offered for whatever file next makes a claim of that shape: *where the argument is that an external result and a corpus structure are one object, every external result gets a one-sentence statement of what it says in standard terms before the corpus reading is applied, and every corpus term gets the same in reverse.* No bare citations on either side. A physicist who stops at the first unglossed corpus term has stopped before the argument starts; a corpus reader who stops at "Tolman mass" has done exactly the same thing from the other direction, and neither will report it as the reason they stopped.

*Executed in the repour.* Laue, the $4/3$ problem, the Komar and Tolman masses, the Dyson luminosity, Unruh and Gibbons–Hawking, Fabry–Pérot and Bragg, Nash embedding, the Wilson loop, Onsager and Casimir reciprocity, the Hall and Righi–Leduc effects, and the gyrator all now carry one standard-terms sentence at first use. The corpus side — $h\mathbf{Q}$, the committed scalar, `.behold()`/`.observe()`, the Landauer tax — carries the same in reverse.

### 6.7 Seeing half of something, and the shape of that

The cascade-law error (§2.7) is the sharpest method lesson in this pass, because **this file looked directly at it and caught the wrong half.**

§4.1 as originally written worried about the coherent case — Fabry–Pérot transmits to unity — and concluded the law was safe "under incoherent / random-phase stacking." It was not safe there either. The worry was real, the diagnosis was adjacent to the error, and the conclusion drawn was the one that let the wrong law survive.

What makes it instructive rather than merely embarrassing: **a correctly identified neighbouring problem can function as cover.** Having flagged *a* condition on the law, the section read as having audited the law. The flag was honest and its presence is what stopped anyone looking further. A caveat that does not close is sometimes worse than no caveat, because it occupies the chair an audit would have sat in.

The tell, available in hindsight and visible in the file's own text: the error was derivable from a premise stated three paragraphs away. *The free medium remains lossless throughout* and *transmission composes multiplicatively* cannot both hold, and both were on the page. **Two premises in one section that contradict each other is a thing to grep for, and nobody greps for it, because each one looks right where it stands.**

Related, and worth filing beside it: §2.6 records the drafting side catching the equipartition gloss in one place and committing the same move in another within a single pass. Same family. A pattern recognized is not a pattern defended against, and the gap between the two is where this kind of error lives.

| Item | Status | Owed |
|---|---|---|
| $N = 25.0265$ rung count | OPEN VOTE, quarantined | A derivation that does not refute `L3-TheAtomOfSpace` §VI |
| Rung step $2/\alpha$ beyond Gen-1 Mutable | Blocked | Bimedian-specific Laurent shapes for Cardinal and Fixed crossings |
| **Nesting cascade law** | **OPEN — undetermined between $1/n$ and $T^n$** | **How much a nested interior commits per pass (§2.7)** |
| Leibniz windowlessness half | Owed | Follows the cascade law; the coordination half stands |
| **Bits $\leftrightarrow$ quadrupole acceleration** | **TARGET — dimensionally checked, not derived** | **Whether the Laue defect is the energy spent; which temperature prices it (§4.6)** |
| Agency stationary point | OPEN, bet placed (not $45°$) | Transmission law derived from the port algebra |
| Wilson loop $\neq \mathbf{1}$ | OPEN construction | A canonical $g_{AB}$; a loop with a stated carrier |
| $1/4$ duty cycle $=$ Bekenstein $1/4$ | CANDIDATE | An argument that an area coefficient and a time fraction are one object |
| Casimir sector assignment | The bet is the register split; now KI-6 in the parent | Archimedes |
| **Q4's LIGO chafe at $\omega > 0$** | **CANDIDATE resolution via the Laue identity** | **The §4.6 relation; see §4.6's closing** |
| AC extension §IV vs Q4 §II | **Live corpus conflict, logged** | Retract or defend the $L$–$C$ discharge reading |
| Direction rule (reversal reactive only) | Adopted into Part Three §V | — |
| $(a)$/$(b)$ dark-energy fork | Pre-registered, three claims coupled | DESI remaining releases, Rubin, Roman |
| Sharing reading of the DESI hint | QUARANTINED on arrival | An independent estimate of drawing regions (§4.7) |
| $\rho_\Lambda$ from $Z_0$-maintenance | Pre-registered, owed twice | The medium's mode spectrum; also closes §V's circularity |
| $p = -\rho c^2$ from pre-filled volume | Postulate traded for postulate | Entry two above; the reframe is what it buys |
| Series-impedance combination rule | Flagged debt — **was spent while flagged** | The AC extension's series/parallel topology across rungs |
| Scale index $k$ / Postulate V cite | Stale address, dropped from the parent | — |
| Port evaluation locus | Placement stated | A derivation, if the question is ever pressed |
| Coincidence problem ($\rho_\Lambda \sim \rho_m$ now) | Declared unaddressed | — |

**Closed in this pass.** The no-outside attribution (sourced to the whole; §5). The write-head's locus and the apparent fork (dissolved, not resolved; §5). The Epistemic Rubric's placement (compact datasheet in the parent, manual cited out). The blanket's single-layer ratio. KI-5's composition clause and KI-6's elevation of the deviation.

---

## 8. The Numbers

Every figure above comes from this block.

```python
from mpmath import mp, mpf, sqrt, pi, log, sin, cos, tan, degrees, findroot, diff
mp.dps = 20
c = mpf('299792458'); G = mpf('6.67430e-11'); hbar = mpf('1.054571817e-34')
alpha = 1/mpf('137.035999177'); lP = sqrt(hbar*G/c**3); OL = mpf('0.685')
H0 = mpf('67.4')*1000/mpf('3.0857e22'); RH = c/H0; RdS = c/(H0*sqrt(OL))
Z0 = mpf('376.730313411'); RK = mpf('25812.8074593'); step = log(2/alpha)

# rung counts
for n, R in (("Hubble", RH), ("de Sitter", RdS), ("event hor", mpf('1.63e26')), ("particle", mpf('4.40e26'))):
    print(n, log(R/lP)/step)
# 24.992776  25.026475  25.023406  25.200309
print(log(RH/lP), step)                       # 140.294218  5.613391

# generative rule
print(4*3, 5*4, 20*step/log(10), 25*step/log(10), log(RH/lP)/log(10))
# 12  20  48.76  60.95  60.93

# blanket, both candidate ratios
for rho in (RK/Z0, 2/alpha):
    print(rho, (rho-1)/(rho+1), 4*rho/(1+rho)**2)
# 68.5180  0.971230  0.0567114   |   274.0720  0.992729  0.0144888

# the two cascade laws (see 2.7): lossless series vs absorptive product
T = 8*alpha/(1+2*alpha)**2; R = 1 - T
print(T, R, R/T)                              # 0.0567114  0.9432886  16.6331
for n in (1, 2, 3, 4, 8, 25):
    print(n, T/(n*R + T), T**n)
# 1   5.671137e-02   5.671137e-02
# 2   2.918319e-02   3.216179e-03
# 3   1.964658e-02   1.823939e-04
# 4   1.480766e-02   1.034381e-05
# 8   7.459058e-03   1.069944e-10
# 25  2.399067e-03   6.946297e-32
print(T**2/(1-R**2), T/(2*R + T))             # 0.029183194078878  0.029183194078878  (identical)
print((T/mpf('1e-5') - T)/R, log(mpf('1e-5'))/log(T))   # 6012.03   4.01   layers for 1e-5

# write power, Dyson ladder, clock
PP = c**5/G; rho_dS = 3*c**4/(8*pi*G*RH**2); dVdt = 4*pi*RH**2*c
print(PP, rho_dS*dVdt/PP)                     # 3.6283e52 W   1.5  exactly
print([L/PP for L in (mpf('3.828e26'), mpf('2e37'), mpf('1e49'), mpf('3.6e49'))])
# 1.055e-26  5.512e-16  2.756e-4  9.922e-4
print((log(2)/3)*(1/H0)/mpf('3.15576e16'))    # 3.35192 Gyr

# the corrected cosmological ratio
rhoP = c**7/(hbar*G**2); rho_obs = OL*(3*H0**2/(8*pi*G))*c**2
print(rho_obs/rhoP, (lP/RH)**2, (rho_obs/rhoP)/((lP/RH)**2), 3*OL/(8*pi))
# 1.1339e-123  1.3867e-122  0.0817659  0.0817659   (exact match)

# agency stationary point under three transmission models
d = pi/180
for nm, T in (("cos^2(th/2)", lambda t: cos(t/2)**2), ("cos(th)", lambda t: cos(t)),
              ("1-tan^2(th/2)", lambda t: 1 - tan(t/2)**2)):
    A = lambda t: sin(t)*T(t)
    best = max(((A(k*d), k) for k in range(1, 90)), key=lambda p: p[0])
    print(nm, degrees(findroot(lambda t: diff(A, t), best[1]*d)))
# cos^2(th/2) 60.000 | cos(th) 45.000 | 1-tan^2(th/2) 51.827
```

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work. This file in particular is a working spillover and carries nothing landed; read `L4-K4-Infinities` for the standing claims.

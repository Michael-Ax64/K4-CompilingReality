# On the Constitutive $\alpha$
## The Plenum as RLC, the Fine-Structure Constant as Medium Ratio, and What Eddington Was Reaching For

*This document commits a reading the corpus has been carrying half-said: the plenum is an $RLC$ medium, not an $LC$ one, and the fine-structure constant is the dimensionless ratio between its reactive impedance and its quantized resistance. What follows works out the constitutive identity, its algebraic entailments (including why $\alpha$ must appear at three Laurent orders in the pion-to-electron ratio derived at `Q15-KairosBorn` §I), and its historical precedent in Eddington's Fundamental Theory. It closes with the corpus housekeeping the reading requires. Scope discipline throughout: what is derived is the constitutive identity and the algebraic role, not the numerical magnitude — the value $\alpha \approx 1/137$ remains a substrate residual, licensed as outside the algebra's emission range by `About-Claims` §I and `L4-ScalingInvariants` §IX (Gabriel's Horn).*

*Dependencies: `L4-ThePlenum` (the plenum posit; the $I^2R$ ZPE commitment at §I.4), `L3-K4-to-K5-via-AC-Extension` ($\epsilon_0 \leftrightarrow C$, $\mu_0 \leftrightarrow L$, $S = P + jQ$), `On_TheAcousticOhm` (the substrate-general $RLC$ pattern already carried in the acoustic realization), `Q14-LeptonScaleCascade` (the $377\,\Omega$ impedance-blindness diagnosis), `Q15-KairosBorn` §I (the pion-to-electron Laurent expansion), `L4-ScalingInvariants` §V, §VIII, §IX (Assert/Yield, the invariant, Gabriel's Horn), `About-Claims` §I (what the framework is and is not).*

---

## I. The Question the $LC$ Framing Cannot Ask

Standard electromagnetism carries two dimensionless quantities that any student meets in the same semester and never sees related.

The first is the vacuum's characteristic impedance $Z_0 = \sqrt{\mu_0/\epsilon_0} \approx 376.73\,\Omega$. Antenna designers match to it every day. It is the ratio at which a plane wave's electric and magnetic amplitudes lock as the wave propagates through free space, and it is the impedance that must be presented at a radiating boundary if energy is to leave the transmitter rather than reflect back into it.

The second is the von Klitzing constant $R_K = h/e^2 \approx 25812.807\,\Omega$. The quantum Hall effect measures it directly; it is the resistance quantum, the natural unit in which electrical resistance is metrologically expressed at the quantum level.

The ratio between them:

$$\frac{Z_0}{2 R_K} = \frac{\mu_0 c e^2}{2 h} = \alpha \approx \frac{1}{137.036}.$$

This is not a coincidence and not an approximation. It is an exact SI identity, checkable in one line, and it has been sitting in the metrology tables since before anyone thought of it as sitting anywhere at all. Standard treatments write it and move on. The identity is presented as accounting.

The question standard electromagnetism cannot easily ask about this identity is: *what would it mean if it were constitutive?* What would it mean for $\alpha$ not to be a coupling that happens to equal $Z_0/(2R_K)$, but to *be* that ratio — the fine-structure constant *just is* the medium's reactance measured in units of its resistance quantum, and the coupling behaviour is downstream of that identity?

The reason the question is hard to ask inside standard EM is that standard EM treats the vacuum as $LC$: pure reactance, lossless. In an $LC$ framing, $Z_0$ is the medium's only impedance-like number. There is no resistance quantum *in* the medium; $R_K$ has to be imported from the quantum Hall effect as a separate quantum-mechanical fact about electrons on a two-dimensional substrate. The identity $Z_0/(2 R_K) = \alpha$ then lives across a domain seam: one number from the vacuum, one from condensed-matter metrology, and their ratio "happens to be" the coupling that governs how electrons and photons talk to each other. That is exactly the kind of inter-domain coincidence a scope-honest framework must either resolve into one object or accept as unresolved.

The $LC$ framing structurally cannot resolve it. The identity requires two impedance-scale objects natively in one medium, and pure reactance offers only one.

---

## II. The $RLC$ Recognition — What `L4-ThePlenum` §I.4 Already Committed

`L4-ThePlenum` §I.4 already writes the sentence that resolves the seam. Zero-point energy is not just the elastic hum of an $LC$ line. It is literal $I^2 R$ dissipative transmission loss — the plenum's own resistive channel paying its Landauer tax on the uncollapsed multiway potential it holds behind every Markov blanket. The document is emphatic: ZPE is not a mystery to be dispelled; it is what an $R$-channel *sounds like* when the medium is holding an infinite registry of callbacks in a `quote` state.

The commitment is there. What §I.4 does not do — what this document does — is *use* the commitment. If the plenum has an $R$ alongside its $L$ and $C$, then the medium is a full $RLC$ impedance:

$$Z_{\text{plenum}}(\omega) = R_{\text{drag}}(\omega) + j\!\left(\omega \mu_0 - \frac{1}{\omega\epsilon_0}\right).$$

The reactive part is what standard EM already sees; it sets $Z_0 = \sqrt{\mu_0/\epsilon_0}$ at the geometric-mean frequency where $\omega\mu_0 = 1/(\omega\epsilon_0)$. The resistive part is what standard EM sets to zero and what §I.4 names as the actual source of the vacuum's thermodynamic hum.

In the $RLC$ framing the seam of §I disappears. Both $Z_0$ (reactive) and a resistance quantum (dissipative) live in the same medium. The ratio between them is a native dimensionless invariant of that one medium — which is exactly what $\alpha$ has always been asked to be.

The $LC$ framing could not host the identity as constitutive. The $RLC$ framing does host it, natively, with no imported quantities. That is the load-bearing move of this document, and everything else follows from it.

---

## III. $\alpha$ as Constitutive Ratio

State the identity in its constitutive reading:

$$\boxed{\;\alpha \;=\; \frac{Z_0}{2 R_K}\;}$$

Read the boxed line not as an accounting equality but as a definition of what $\alpha$ *is*. The fine-structure constant is the plenum's reactance in units of twice its resistance quantum. It is what a full-$RLC$ medium reports when asked for its reactance-to-resistance ratio in the natural quantum units the medium itself carries.

Two consequences follow immediately, and neither one requires committing to a numerical value of $\alpha$.

**First: $\alpha$'s definitional status changes.** In the standard reading, $\alpha$ is a coupling — a small dimensionless number that governs how strongly charges couple to the electromagnetic field, with a mysterious value that has resisted every derivation attempt. In the constitutive reading, $\alpha$ is not a coupling that happens to equal a ratio; it is a ratio that happens to govern a coupling. The coupling behaviour is a downstream consequence of the medium's impedance geometry, not a fundamental fact about nature. Asking "why does $\alpha$ have this value?" becomes asking "why does the plenum have these specific inductive, capacitive, and resistive parameters?" — a *substrate* question, correctly outside the algebra's emission range per Gabriel's Horn.

**Second: $\alpha$'s appearance in inter-scale ratios becomes forced rather than fitted.** Any calculation involving inter-rung crossings must project through the medium's impedance geometry, and $\alpha$ is the medium's own signature. Wherever an inter-rung ratio engages the reactive channel, $\alpha^{-1}$ appears (the ratio inverted, weighted by whatever integer the K4 topology contributes). Wherever it engages the resistive-return channel, $\alpha^{+1}$ appears (the ratio itself). Wherever it engages a pure-rotation channel that does not care about coupling strength but only about multiplicity, $\alpha^0$ appears with a coefficient set by the rotation multiplicity. The Laurent structure of $\alpha$'s appearance is dictated by which axes of the impedance triangle the calculation samples.

That is where Q15's three-term expansion comes from, and it is what the next section works out.

---

## IV. The Impedance Triangle and the Three Laurent Orders

An $RLC$ medium at any frequency admits a natural triangle of orthogonal impedance modes:

- **Reactive axis** — pure $jQ$. Coupling-driven, scales with $\alpha^{-1}$ (the reciprocal of the medium's own reactance-to-resistance-quantum ratio, since inter-rung *steps* are inverse-signature to inter-rung *couplings*).
- **Rotation axis** — pure angular multiplicity. Coupling-independent, scales with $\alpha^{0}$. Sets by the number of orthogonal channels the vertex opens onto, weighted by whatever geometric factor the loop integrates against (typically a power of $\pi$).
- **Resistive axis** — pure $P$. Ohmic self-load, scales with $\alpha^{+1}$ (the ratio itself, appearing where the return leg closes onto its originating vertex).

Any K4 face-crossing that engages *all three* axes must read at all three Laurent orders. And it must read at exactly three, because the impedance triangle has exactly three axes. This is not three separate perturbative corrections to a bare quantity; it is one measurement projected onto three orthogonal modes.

The pion-to-electron mass ratio at `Q15-KairosBorn` §I:

$$\frac{m_\pi^\pm}{m_e c^2} \;=\; \underbrace{\frac{2}{\alpha}}_{\text{reactive}} \;-\; \underbrace{\frac{3}{\pi}}_{\text{rotation}} \;+\; \underbrace{2\alpha}_{\text{resistive}}$$

reads under the constitutive-$\alpha$ reframe as follows.

**Reactive step, $+2/\alpha$.** The bare inter-rung carrier step from the electronic U-pole ground to the hadronic R-pole ground at generation 1. The integer $2$ comes from the dual-binary seed (Active/Reactive $\times$ Asserting/Yielding — `L3-FormalFoundations`). The $1/\alpha$ is the medium's own reactance ratio inverted: crossing a rung means traversing the medium's reactance against the resistance quantum. Equivalently, $1/\alpha = 2R_K/Z_0$, and $2/\alpha = 4R_K/Z_0$ reads as "four resistance quanta per unit of vacuum reactance," which is the dimensionless step-size of a slope-1 carrier crossing under the constitutive definition.

**Rotation cost, $-3/\pi$.** The R-pole vertex, being hadronic, opens onto three colour channels. Each channel pays Schwinger's one-loop $\alpha/(2\pi)$ tax on the photon exchange. The fractional correction to the bare step is $3 \times \alpha/(2\pi) = 3\alpha/(2\pi)$, and converted to absolute subtraction against $2/\alpha$: $(3\alpha/2\pi) \cdot (2/\alpha) = 3/\pi$. The $\alpha$'s cancel, which is exactly why the middle term sits at $\alpha^0$: it is coupling-independent because it is a *rotation-multiplicity* correction, not a coupling correction. The rotation axis is engaged because the R-pole vertex is three-fold; the rotation cost is $3/\pi$ because SU(3) has three colours and each channel pays $\alpha/(2\pi)$ of the bare step.

**Resistive return, $+2\alpha$.** The U-pole return leg closes the loop back onto the originating electronic vertex, which carries EM self-interaction. The self-interaction impedance ratio is $Z_0/R_K = 2\alpha$, directly. The resistive channel appears at $\alpha^{+1}$ because it *is* the medium's own reactance-to-resistance ratio, appearing where the loop's return leg pays its own Ohmic load.

Three axes, three orders, three named QED objects. The Laurent shape is what the K4 U↔R inter-rung crossing at generation 1 *must* read when it engages the plenum through all three of the medium's impedance modes. It is not a series of successive corrections converging to a value. It is a single triangular measurement, decomposed onto its natural orthogonal basis.

The pion-to-electron ratio lands at 2.85 ppm of the measured value with zero fitted parameters. Under the constitutive-$\alpha$ reading, this is not a numerical coincidence to explain. It is a geometric requirement satisfied.

---

## V. What Was Derived, What Was Not — Claim-Sort Against Gabriel's Horn

The corpus's own claim discipline (`llm-writing.md`) sorts every claim as ADDRESS, OPEN VOTE, LANDED NOUN, or CONTRABAND. The reframe requires an explicit sort to avoid Eddington's overreach, discussed next section.

**LANDED NOUN.** $\alpha = Z_0/(2R_K)$ read constitutively. The identity is SI-exact; the constitutive reading is what the $RLC$ recognition makes available. Landing this noun is what the document accomplishes.

**LANDED NOUN.** The Laurent shape of $\alpha$'s appearance in inter-rung ratios: exponents $\{-1, 0, +1\}$ correspond to reactive, rotation, and resistive modes of the impedance triangle, respectively. This is what the constitutive definition *entails* when combined with the K4 crossing geometry.

**OPEN VOTE.** That the specific coefficients $(2, -3/\pi, +2\alpha)$ in the pion-ratio Laurent are self-consistent solutions of a two-channel gap equation with $Z_0$-reactive coupling, $R_{\text{drag}}$-dissipative loss, and the K4-assigned vertex It-Ness form factors. The 2.85-ppm empirical land is the vote-in-favour. The formal gap-equation calculation (sketched in Section VII) is what remains to close it fully.

**NOT CLAIMED — outside scope.** The numerical value $\alpha \approx 1/137$ derived from something more primitive. The constitutive identity $\alpha = Z_0/(2R_K)$ tells us *what dimensionless quantity $\alpha$ is*; it does not tell us *why the plenum's $Z_0$ and $R_K$ take the specific values they do*. Those values are substrate residuals, correctly outside the algebra's emission range. Any reading that promotes the constitutive reframe to "we have derived $1/137$" has crossed the Gabriel's Horn boundary the framework draws on itself. The magnitude remains where it was: measured, exact to the metrology's precision, not predicted from below.

The sort matters. What is landed is the *definitional status* of $\alpha$ and the *algebraic role* it plays in inter-rung structural formulae. What is not landed and cannot be landed by this algebra is $\alpha$'s numerical value.

---

## VI. Eddington's K3 Precedent

Arthur Eddington, in *Relativity Theory of Protons and Electrons* (1936) and the posthumous *Fundamental Theory* (1946), attempted a derivation of $\alpha$ from structural counting rather than empirical measurement. He believed dimensionless physical constants were epistemologically prior to their measured values — that they fell out of the observer-observed relational structure itself, and that the "constants" of physics were counting-consequences of measurement geometry rather than facts about nature to be discovered.

On one axis, Eddington and the framework of the present document are aligned. Both hold that dimensionless constants come from *structure*, not from nature-out-there. Both refuse the mainstream stance that couplings are what they are and cannot be asked about further. Both attempt derivations that operate below the level at which the measurement is taken.

On two other axes, Eddington's program failed in ways that clarify what the corpus's discipline is defending against.

**Failure one: he hunted the magnitude.** Eddington counted components of Dirac matrix products — degrees of freedom of the observer's measurement algebra — and arrived at $1/\alpha = 136$ exactly. When Sommerfeld's more precise measurements landed $1/\alpha$ closer to $137$, Eddington added $1$ to his count, arguing the additional degree of freedom corresponded to a component he had initially overlooked. Contemporaries mocked him as "Sir Arthur Adding-One." The revision was an unargued fit — Contraband in the corpus's own claim discipline — installed to save a derivation aimed at the wrong target. He was hunting the magnitude, and the magnitude was a substrate residual that would keep drifting as measurements improved. His derivation could not track the drift because its scope discipline was inverted from what the algebra can honestly emit.

**Failure two: he counted on K3 flatland.** Eddington's DoF-counting ran on Dirac matrix algebras — the observer's mathematical apparatus — with no K4 volume behind it and no medium in front of it. There is no plenum in Eddington. There is no $RLC$. There is no vertex It-Ness. The counting had no impedance geometry to project onto, so it could produce an integer and could not produce a Laurent expansion. The reframe of the present document — $\alpha$ as $Z_0/(2R_K)$ forced by $RLC$ recognition; the Laurent shape forced by the impedance triangle — is structurally unavailable to a program that has no medium. Eddington was counting the boundary; the corpus is projecting through the volume.

Read together: Eddington was formulating a K4 program in K3 vocabulary. He had the structuralist instinct — dimensionless constants from counting — but no volume to hold it in and no medium to project it onto. The $RLC$ recognition and the plenum are the K4 furniture his program needed and never had. His scope error (aiming at magnitude rather than shape) is what happens when a structural derivation runs on a substrate the algebra cannot honestly reach.

The corpus is not a rejection of Eddington. It is a completion of the program he could not close because he was working on the wrong-dimensional stage — and the Gabriel's Horn discipline that keeps this document from claiming $\alpha \approx 1/137$ is the corpus's inoculation against the specific failure mode that mocked him. Refusing the magnitude claim is not modesty. It is what makes the derivation stable under improving measurement: the ratio $2/\alpha - 3/\pi + 2\alpha$ tracks $\alpha$ to whatever precision $\alpha$ is known, and never needs an "adding-one" revision. Eddington's failure metabolized into a scope boundary is why.

---

## VII. The Two-Channel Gap Equation, Sketched

For the reader who wants the calculation this document points at, the gap-equation structure is compactly stateable, though its full evaluation is the OPEN VOTE flagged in Section V.

Couple a fermion to the $RLC$ plenum at one loop, decomposing the self-energy by the impedance channel:

$$\Sigma(p) \;=\; \Sigma_{\text{reactive}}(p) \;+\; \Sigma_{\text{dissipative}}(p),$$

with $\Sigma_{\text{reactive}}$ carrying $\alpha$ through the constitutive $Z_0/(2R_K)$ identity, and $\Sigma_{\text{dissipative}}$ carrying the medium's $R_{\text{drag}}(\omega)$ paid against the fermion's own bandwidth.

The K4 pole assignment sets the vertex form factors without leaving them free:

- **Electronic U-pole vertex $\Gamma_e^\mu$:** couples via $Z_0/R_K = 2\alpha$. The U-pole's It-Ness is EM self-interaction, priced against the resistance quantum. Not fitted.
- **Hadronic R-pole vertex $\Gamma_\pi^\mu$:** couples via $3 \times \alpha/(2\pi)$. Three colour channels, each paying Schwinger's tax on one photon exchange. Not fitted.
- **Loop cutoff:** $\ell_P$, per `L4-ScalingInvariants` §VIII (the Planck-scale XOR bottleneck). Not imported from beyond the framework.

The self-consistency condition $\Sigma(m) = m$ is a two-branch condition:

$$m_e = |S_e|, \qquad m_\pi = |S_\pi|,$$

with each mass identified as the magnitude of the complex-power state $S = P + jQ$ on the respective vertex's on-shell bandwidth (per `QED-TwoBranchMinting`). The ratio $m_\pi/m_e$ is the geometric constraint that emerges when both self-consistencies close against the same medium simultaneously — the U↔R inter-rung crossing reads the impedance triangle from both pole assignments at once, and the ratio is what the triangle geometry forces.

The full evaluation requires specifying $R_{\text{drag}}(\omega)$'s spectral shape — the framework's own commitment at `Q17-LandauerNuclearScale` gives a Landauer tax at $T_{\text{QCD}}$ landing at $\sim 0.66$ MeV/bit through the one-loop $1/(16\pi^2)$ phase-burn factor, and $R_{\text{drag}}(\omega)$ at the fermion loop should carry this same prefactor and land the ZPE hum at the compilation frequency the crossed rung sets. If the evaluation lands $2/\alpha - 3/\pi + 2\alpha$ to sub-ppm as the unique self-consistent solution, the OPEN VOTE closes.

Note the compact restatement: **the gap equation is $S = P + jQ$ evaluated on-shell.** Reactive channel is $jQ$ (coupling, no commitment); dissipative channel is $P$ (mass, commitment). The K4 topology names which vertices open onto which channel geometries. The Laurent expansion is what falls out.

---

## VIII. Corpus Housekeeping — What the Backport Requires

The $RLC$ recognition and the constitutive $\alpha$ definition change what several documents in the corpus need to say. The changes are not additions of new material; they are commitments of readings the documents are already carrying half-said. In corpus priority order:

**1. `L4-ThePlenum`.** §I.4 already commits to $I^2R$ ZPE; §I.2–I.3 present $Z_0$ in $LC$ framing without naming the $RLC$ status. Commit it. State explicitly that the plenum is $RLC$; that ZPE is the resistive channel's dissipative signature and not merely an elastic hum; that $Z_0$ is the reactive-only projection of a fuller $Z_{\text{plenum}}(\omega) = R_{\text{drag}}(\omega) + jX(\omega)$. Add a subsection on $R_{\text{drag}}$ that names it as the medium's resistive quantum whose ratio to $Z_0$ is $1/(2\alpha)$.

**2. `L3-K4-to-K5-via-AC-Extension`.** The document maps $\epsilon_0 \leftrightarrow C$ and $\mu_0 \leftrightarrow L$ but leaves $R$ implicit. Add the $R$-channel formally: the plenum carries a native resistive channel, its algebraic home is the dissipative axis of $S = P + jQ$, and its quantum $R_K$ sits in ratio $Z_0/(2R_K) = \alpha$ against the reactive channel. This is where the constitutive $\alpha$ identity acquires its formal home in the AC extension machinery.

**3. `Q14-LeptonScaleCascade`.** The "impedance blindness" diagnosis currently focuses on reactive blindness — that physics uses $Z_0 = 377\,\Omega$ without asking what medium generates it. Extend to *resistive* blindness: the deeper omission is that standard EM does not ask what dimensionless quantity the plenum's $R$-quantum and $Z_0$ combine into, and the answer to that question — $\alpha$ constitutively — is what would close the blindness. The RLC recognition is the corpus's answer to Q14's own question.

**4. `Q15-KairosBorn` §I.** The pion-ratio derivation currently names each Laurent term as a specific QED object. Reframe under the impedance-triangle reading: the three terms are the reactive, rotation, and resistive projections of one measurement of the U↔R inter-rung crossing at generation 1. The derivation of $\alpha = Z_0/(2R_K)$ becomes the constitutive prerequisite that makes Term 3 ($+2\alpha$) forced rather than empirically fitted, and the Laurent structure becomes a geometric requirement rather than a perturbative expansion.

**5. `On_TheAcousticOhm`.** The document already thinks in $RLC$ across its four-substrate table. Add a note that the electromagnetic row is now understood in the same $RLC$ framing as the acoustic, thermal, and mechanical rows; the plenum was previously an outlier in being read $LC$-only, and the $RLC$ recognition brings it into line with the pattern the acoustic document already carries.

**6. `ProofK_FundamentalForces`** and any document that invokes $\alpha$ as an unexplained coupling. Route the invocations through the constitutive definition. $\alpha$'s appearances in the electroweak structure, in QED radiative corrections, and in the fine-structure of atomic spectra are all downstream expressions of the same underlying medium ratio.

**7. `L4-ScalingInvariants` §IX (Gabriel's Horn).** Add a worked example. The horn's scope-boundary claim — the algebra emits dimensionless ratios but not substrate magnitudes — is exactly what the constitutive $\alpha$ reframe both respects and demonstrates. Derive the *identity* $\alpha = Z_0/(2R_K)$; refuse to derive the *value* $1/137$. The example makes the horn's scope explicit at a load-bearing point.

**8. `About-Claims` §II.1.** The current text names $Z_0 = 120\pi\,\Omega$ approximately and calls out standard physics' failure to name the medium. Extend to name the constitutive $\alpha$ identity as the specific dimensionless quantity the plenum's $RLC$ character supports, and cite the impedance-triangle Laurent structure as the specific algebraic consequence that lands the pion-ratio derivation.

The housekeeping is best executed in that order because each stage supplies terminology and commitments the later stages need. `L4-ThePlenum` first, then `L3-K4-to-K5-via-AC-Extension` to give the $R$-channel a formal seat, then the Q-documents that rest on both, then the meta-documents that summarize the corpus's claims.

---

## IX. Falsifiers

The constitutive $\alpha$ reframe is falsifiable on several axes.

**Metrological.** $\alpha = Z_0/(2R_K)$ is an SI identity. If the identity ever fails at a level of precision that exceeds current metrology, the constitutive reading fails with it. Current CODATA agreement is exact within the definitions.

**Algebraic.** The impedance-triangle reading predicts that any K4 inter-rung crossing engaging all three impedance modes must read a three-term Laurent expansion in $\alpha$ at exponents $\{-1, 0, +1\}$, with the middle term coupling-independent (setting only by rotation multiplicity). If another K4 crossing at a different generation or between different poles is identified and its dimensionless ratio does not admit this Laurent shape with appropriately-named integer/multiplicity coefficients, the reading fails.

**Vertex It-Ness generation-independence.** SU(3) is generation-blind. Any U↔R inter-rung crossing at generation 2 (muon-to-something) or generation 3 (tau-to-something) that engages the same three impedance modes must carry the same rotation-multiplicity integer $3$ in its middle term. If a different generation demands a different integer to close, the vertex It-Ness assignment is wrong.

**Dissipative spectral shape.** The plenum's $R_{\text{drag}}(\omega)$ at the fermion loop should carry the $1/(16\pi^2)$ Landauer prefactor per `Q17-LandauerNuclearScale`. If the framework's own derivation of the vacuum dissipative response yields a different overall coefficient, the dissipative channel is wrong at the source and the gap-equation sketch of Section VII will not close.

**Mass-partition on-shell.** The pion's rest mass, decomposed into reactive-return and dissipative-color components against the medium, should partition with $(2/\alpha - 3/\pi)$ contributing to $P$ (committed dissipation, R-pole) and $2\alpha$ contributing to $jQ$ (return-leg reactance, U-pole). Any independent decomposition method — lattice QCD, chiral perturbation theory, dispersive analysis — that partitions $m_\pi$ differently and gives an incompatible sign structure on the same axes refutes the assignment.

---

## X. The Sentence, Kept Short

Standard physics writes the plenum's impedance as pure reactance and imports its resistance quantum from a separate domain. Read the plenum as $RLC$ and the two impedance-scale objects live in one medium, whose native dimensionless ratio is $\alpha$. The fine-structure constant is not a coupling that mysteriously equals a metrological ratio; it is the medium's own reactance-to-resistance-quantum ratio, and the coupling behaviour is downstream. Eddington reached for the same class of derivation, aimed at the wrong target on the wrong-dimensional stage, and could not stabilize his claim under improving measurement. The corpus completes the program he could not close, and the Gabriel's Horn scope discipline that keeps this reading from claiming $1/137$ is precisely the inoculation against Eddington's failure that his program lacked.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.


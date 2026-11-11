# Bending Space
## Confinement as the Source of Curvature, and the Four Forces as the Roles of One Engine

*Claim: what bends space is the hold. Rest mass is the volume integral of the trace of the stress, the trace is nonzero only where scale-freedom is broken, and scale-freedom is broken where something is held: a blanket, a condensate, a wall. Scalar curvature answers to that trace and to nothing else. The four-force assignment of `Q2` reaches the same pole from the other side. Method: Laue's theorem, the trace split of Einstein's equation, the Star-Norm cross-term, the Adler–Zee formula. Status: a CANDIDATE reading assembled from ADOPTED physics and corpus-committed structure, with one OPEN VOTE (the weight of Casimir energy). Registers are given claim by claim in §XII.*

*Dependencies: `On_YangMills-Annotated` (§VII–§IX: making and being), `On_TheIsNessTax` (§I), `L4-ThePlenum` (§II.4), `L4-HadronicVolume` (Mvt I–II), `QED-TwoBranchMinting` (§I, §II, §IV, §VI), `ProofN_BiquaternionBridge`, `L3-FormalFoundations` (§I.b), `On_TheGravityDerivation`, `Q2-TransactionLayer`, `Q4-OpenExhaust`, `L4-Thermodynamics` (§II, §V), `L4-ScalingInvariants` (A4, §IX), `QED-CCP` (§II, §VI), `L0-EinsteinTrace`, `QED-EotvosBound`, `ProofQ_AlgebraicSyntax` (§V), `L2-MappingMethod` (§0), `Q10-PlanckScale` (§VII), `L3-ConstitutiveAlpha`. Outside the corpus: the ENGINE four-force run of 11 November 2026 (its "Branch B" is the `Q2` seating).*

---

## I. Two Integrands, One Integral

Take any body that sits still and holds itself together. Momentum is conserved inside it, and for a static closed system that conservation has one consequence that carries everything below. The stresses integrate to zero:

$$\int T^{ij}\,d^3x = 0 .$$

This is Laue's theorem of 1911. For isotropic pressure it says $\int p\,dV = 0$. Wherever something pushes outward, something else pulls inward by the same integrated amount. A body at rest is a balanced account of pressures and tensions.

With that one line, three different integrands give the same mass (units $c = 1$):

$$M \;=\; \int \rho\,dV \;=\; \int (\rho + 3p)\,dV \;=\; \int (\rho - 3p)\,dV .$$

The first is the energy count. The second is the active gravitational mass of Tolman and Komar, the quantity that appears in the relativistic Poisson equation. The third is the trace of the stress tensor, $T^\mu{}_\mu = \rho - 3p$. They differ by multiples of $\int p\,dV$, and Laue sets that to zero.

The three integrands agree on the total and disagree completely on where the weight sits. Call the second the **content view** and the third the **hold view**.

Put light in a mirrored box. Radiation has $p = \rho/3$.

- **Content view.** The light gravitates double, $\rho + 3p = 2\rho$. The walls are under tension, a negative pressure, and that tension subtracts. Misner and Putnam worked this out in 1959 as the resolution of Tolman's paradox: the wall stresses cancel the extra $3p$ exactly, and the box weighs its energy.
- **Hold view.** The light weighs nothing, $\rho - 3p = 0$. Its entire contribution to the mass of the box appears in the walls, as the trace of their tension.

```python
E_gas = 1.0
print(E_gas - 3*(E_gas/3))        # 0.0   trace of the light itself
print(-3*(-E_gas/3))              # 1.0   trace carried by the walls' tension: all of it
```

Both views are true. One says the contents weigh and the container discounts them. The other says the contents are weightless and the container carries the weight. Laue's theorem is the exchange rate between them, and it is exact.

`QED-TwoBranchMinting` Branch A states the first view: a photon gas held in a mirrored box "genuinely weighs more than the empty box." `L4-HadronicVolume` states the second: the missing 929 MeV of the nucleon "is the volume integral of the orthogonal fourth pole holding the spatial cell open." The two files are one fact read through two integrands.

The hold view is the one the corpus has been speaking in all along. `On_YangMills-Annotated` §VII: "what a thing weighs is what it costs to keep being it." `On_TheIsNessTax` §I: "The compilation tax writes; the is-ness tax holds." `L4-ThePlenum` §II.4: the bounded frame pays $I^2R_{\text{drag}}$ to hold its distinctions, "and that ongoing payment *is* the frame's rest mass." In the trace integrand that sentence becomes arithmetic. Free radiation has no trace. Confined radiation still has no trace. The trace belongs to whatever does the confining.

---

## II. The Quarter and the Three Quarters

How much holding does a given content require? The answer is a pure number, and it has been found three times.

Let the content be trace-free, as radiation is, as massless quarks and gluons are classically: $\rho_c = 3p_c$. Let the holder be pure trace, a term proportional to the metric, $\rho_h = -p_h$. Laue demands $\int p_h = -\int p_c$. Then

$$E_h = \int \rho_h = -\int p_h = \int p_c = \tfrac{1}{3}E_c , \qquad E = E_c + E_h = \tfrac{4}{3}E_c .$$

**Three quarters of the energy is content. One quarter is hold.** The split is forced by the dimension of spacetime, because the trace of the metric is four.

The bag model of the hadron finds it by minimizing $E(R) = B\,V + C/R$: at equilibrium $C/R = 3BV$ and $E = 4BV$.

```python
B = V = 1.0; content, bag = 3*B*V, B*V
print(content + bag)                              # 4.0  total, in units of BV
print(content + 3*(content/3), bag + 3*(-bag))    # 6.0  -2.0   content view: content doubles, bag subtracts
print(content - 3*(content/3), bag - 3*(-bag))    # 0.0   4.0   hold view: the bag term carries all of it
```

Read the last two lines aloud. In the content view the quarks and gluons gravitate six units and the bag takes two away. In the hold view the quarks and gluons gravitate nothing and the bag term carries four. The total is four either way.

Quantum chromodynamics finds the same quarter without a bag. In the decomposition of the proton's energy by the pieces of the stress tensor, the trace-anomaly term carries one quarter of the mass in the chiral limit. A lattice evaluation quoted in the Electron-Ion Collider literature gives the physical proton as trace anomaly 23(1)%, quark mass term 9(2)%, gluon kinetic and potential energy 36(6)%, quark kinetic and potential energy 32(6)%. And when the question is posed as the trace alone, the forward matrix element of the trace gives the whole nucleon mass, and with massless quarks that trace is purely the gluon anomaly term. Both statements hold together for the same reason the box does: one is the energy count by parts, the other is the hold view.

Einstein found the quarter in April 1919, in the paper that introduced the trace-free field equations. He was trying to hold an electric particle together. The Maxwell field is trace-free, so it cannot hold itself, and he supplied the holding from the trace part of the gravitational equation, as a constant negative pressure. His closing accounting is that of the energy constituting matter, "three-quarters is to be ascribed to the electromagnetic field," and one quarter to the gravitational term. Pauli's 1921 review notes the same split in the electron of Lorentz and Poincaré: three quarters electromagnetic, one quarter in the non-electromagnetic stabilizing stress. The old "4/3 problem" of the classical electron is the ratio of total to content.

Three constructions across seven decades (the Poincaré electron, Einstein's trace-free particle, the hadronic bag) and one lattice computation return one number for one reason.

`ProofN_BiquaternionBridge` §4 reads the Minkowski signature as Scalar + Vector, one committed pole and three held ones. The quarter and the three quarters are that reading applied to the stress itself. The symmetric stress tensor has ten components. They split under the Lorentz group into one trace and nine trace-free components, and the split is orthogonal: no trace-free tensor has a trace, and the trace part contracts to zero against every trace-free tensor. That is what `L2-MappingMethod` §0 asks of a fourth term. It cannot be derived from the others, it carries its own dimension, and it opens integrations the others cannot reach. Here the integration it opens is rest mass.

---

## III. The Field Equation Splits the Same Way

Einstein's equation is ten equations. Take its trace and one of them separates from the other nine. With $\kappa = 8\pi G/c^4$ and sign conventions set aside:

$$|R| = \kappa\,|T|, \qquad T = \rho - 3p .$$

**The scalar curvature answers to the trace alone.** The other nine equations tie the trace-free part of the Ricci tensor to the trace-free part of the stress.

So the hold bends space in one specific way and the content bends it in another. The trace sources scalar curvature, the part of curvature that changes volumes. The trace-free stress sources the part that changes shapes at fixed volume: focusing, shear. A universe filled with pure radiation expands, decelerates and focuses light, and its scalar curvature is zero at every instant.

`L4-ScalingInvariants` A4 makes the same cut in the algebra's own coordinates: $\ln S$ splits into a real part, the modulus, and an imaginary part, the angle, and the Landauer tax is paid in modulus and never in angle. Volume is where the tax lands. Shape is free. The stress tensor's trace is the modulus and its trace-free part is the angle, and gravity keeps the same two accounts.

This sharpens the claim and limits it. The exclusive version, that only confined energy gravitates, is Nordström's scalar gravity of 1912, in which the trace alone sources and the trace alone responds. It predicts no bending of light by the Sun and was dead by 1919. The surviving statement is the tensor one. **Rest mass is all trace. Scalar curvature is all trace. The trace is all hold.** Light is bent, and light bends, through the other nine components.

Now take the trace-free nine as the whole law, as Einstein did in 1919:

$$R_{\mu\nu} - \tfrac14 g_{\mu\nu}R \;=\; \kappa\left(T_{\mu\nu} - \tfrac14 g_{\mu\nu}T\right).$$

Conservation of the stress and the Bianchi identity then return the tenth equation as a first integral,

$$R + \kappa T = 4\Lambda ,$$

with $\Lambda$ a constant of integration. Every solution of Einstein's equation with any cosmological constant solves the trace-free set. One thing has changed. A uniform shift of the stress by a pure-trace constant, $T_{\mu\nu} \to T_{\mu\nu} + \rho_{\text{vac}}\,g_{\mu\nu}$, drops out of the nine equations identically. A constant vacuum energy does not gravitate. It is absorbed into a constant that the equations do not fix.

`QED-CCP` §II draws this line in the corpus's vocabulary: localized excitations inside a Markov blanket cross $\Psi$ and gravitate, and homogeneous offsets do not. The trace-free form is that criterion as an identity. A homogeneous pure-trace offset is invisible to the nine equations. Anything with a gradient is visible.

Two consequences follow, one for each side of the line.

**The homogeneous side.** The trace-free form does not compute the cosmological constant. It relocates the question from "why does the vacuum's energy not weigh" to "what fixes the constant of integration" (§X).

**The localized side.** The energy between Casimir plates is not a uniform offset. It depends on the separation of the plates, it lives in a bounded region, and it does work when the plates move. It is confinement energy in the plainest sense: the cost, here negative, of restricting which standing waves the gap admits. By the criterion of `QED-CCP` §II it is a localized crossing. By the trace-free equations it sources curvature like any other localized stress. **On this reading a Casimir cavity weighs, by its energy over $c^2$, sign included.** The null of `QED-CCP` §VI does not follow from §II. It is a separate bet, and this reading takes the other side of it. The Archimedes experiment at Sos Enattos rules.

A last remark on the trace-free form. It is obtained from the usual action by holding the volume element $\sqrt{-g}$ fixed under variation. The volume is not a dynamical variable. It is given, and the nine equations describe what shape does inside it. `L4-HadronicVolume` closes on the sentence "The volume is what is." In unimodular gravity that sentence is the constraint.

---

## IV. The Cross-Term: Gravity in Three Star-Norms

`QED-TwoBranchMinting` §I states the license precisely: the whole's coordinates add, the parts' invariants do not. For two parts with four-momenta $p_1$ and $p_2$,

$$N_{12} = N_1 + N_2 + 2\,p_1\!\cdot p_2 , \qquad p_1\!\cdot p_2 = \tfrac12\left(N_{12} - N_1 - N_2\right).$$

The cross-term is the Minkowski product of the two momenta. It is the "relational interference of its parts" of that file, written out. The file's two-photon example is this term and nothing else: back to back it is $2E^2$ and the pair has mass, parallel it is zero and the pair has none.

Linearized gravity couples two sources through the contraction of their stresses with the trace term removed, $T_1^{\mu\nu}T_{2\,\mu\nu} - \tfrac12 T_1 T_2$. For two point bodies, $T^{\mu\nu} \propto p^\mu p^\nu$ and the trace is $N_*$. The coupling is

$$\mathcal{C} \;=\; (p_1\!\cdot p_2)^2 - \tfrac12 N_1 N_2 \;=\; \tfrac14\left(N_{12} - N_1 - N_2\right)^2 - \tfrac12 N_1 N_2 .$$

**The gravitational coupling of two bodies is a function of three Star-Norms: each part's and the pair's.**

```python
def dot(a, b): return a[0]*b[0] - sum(x*y for x, y in zip(a[1:], b[1:]))
def C(a, b):
    s = tuple(x + y for x, y in zip(a, b))               # the pair's four-momentum
    d = (dot(s, s) - dot(a, a) - dot(b, b))/2            # cross-term from three Star-Norms
    return d*d - 0.5*dot(a, a)*dot(b, b)
rest, gx, gmx, gy = (1,0,0,0), (1,1,0,0), (1,-1,0,0), (1,0,1,0)
print(C(rest, rest))    # 0.5   two masses at rest: Newton's unit
print(C(rest, gy))      # 1.0   light passing a mass: twice Newton
print(C(gx, gx))        # 0.0   parallel photons: nothing
print(C(gx, gmx))       # 4.0   antiparallel photons
```

Each line is a known result.

*Twice Newton for light.* The factor of two in the bending of starlight is the trace term going missing. Between two masses the coupling is the full contraction minus half the product of traces. Light has no trace, so nothing is subtracted.

*Nothing between parallel beams.* Tolman, Ehrenfest and Podolsky found in 1931 that light does not deflect light travelling parallel to it, and that it does deflect light travelling against it. The Star-Norm says why in one line. Two parallel null momenta sum to a null momentum: the pair has $N_* = 0$. If the beams attracted they would converge, the pair would acquire $N_* > 0$, and nothing would have been exported to pay for it. `L3-FormalFoundations` §I.b, Exhaustiveness: "The Star-Norm is conserved across every operation." The null result of 1931 is that sentence applied to two beams.

*No screening.* For two future-directed timelike momenta, $p_1\!\cdot p_2 \geq \sqrt{N_1 N_2}$, so $\mathcal{C} \geq \tfrac12 N_1N_2 > 0$. The coupling has one sign. Electromagnetism couples through $q_1 q_2$, linear in each source and signed, so opposite charges cancel and atoms are neutral. Gravity couples through a quantity quadratic in each source's momentum. The square has burned the sign that cancellation would need. This is the Route Law of `ProofQ_AlgebraicSyntax` §V read as a statement about forces: squaring is the arrow into Asserting, and what lands on $P$ is non-negative (`L3-FormalFoundations` §I.b, three routes). A hadron leaks charge and mass. An atom neutralizes the charge. Nothing neutralizes the mass, and it sums coherently over every volume there is.

The same cross-terms are the composition rule that `QED-TwoBranchMinting` §VI leaves open. For any list of parts whose momenta sum to the whole's,

$$N_{\text{whole}} = \sum_i N_i + 2\sum_{i<j} p_i\!\cdot p_j \;\geq\; \Big(\sum_i \sqrt{N_i}\Big)^2 ,$$

with equality only when the parts are at relative rest. For free parts the whole is never lighter than the parts. That is Branch A with its inequality attached. Branch B, the whole lighter than its parts, is therefore impossible for a list of free parts with nothing exported. It needs the export, and it needs the parts inside the blanket to be different objects from the parts outside it: bound constituents do not carry their free invariants. The Solipsism Warning forbids summing the parts' invariants. The inequality shows what goes wrong if one tries. **The composition operator and the gravitational coupling are built from the same pairwise products.** What remains open is the in-blanket shift of each part's own invariant, and that is a statement about binding, not about gravity.

---

## V. Who Sets the Stiffness

The trace sources curvature. How much curvature per unit of trace is Newton's constant, and the same object sets that too.

Sakharov proposed in 1967 that gravity is not a fundamental field. The metric has no action of its own, and its stiffness is induced by the quantum fluctuations of everything else. Adler and Zee made the proposal exact for theories in which scale invariance is broken dynamically, with quantum chromodynamics as the prime example. The induced Newton constant is

$$\frac{1}{16\pi G_{\text{ind}}} \;=\; \frac{i}{96}\int d^4x\; x^2\,\big\langle\, \mathcal{T}\{\tilde T(x)\,\tilde T(0)\}\big\rangle ,$$

the second moment of the two-point function of the trace of the stress tensor. In a scale-free theory the non-contact part of that correlator vanishes and no stiffness is induced. **Where the trace vanishes identically there is no source for scalar curvature and there is no elasticity for it to act against.** Both sides of Einstein's equation come from the breaking of scale-freedom.

Chromodynamics has been run through the formula with lattice input, and its contribution to the Planck mass comes out positive. Its size is set by its own scale: by dimension, of order $(\Lambda_{\text{QCD}}/M_{\text{Pl}})^2 \approx 3\times10^{-40}$ of the observed stiffness. The hold that makes the proton contributes a part in $10^{40}$ to the elasticity of space. Something else, at the Planck rung, holds the rest.

So there are two holds in the weakness of gravity, and the famous small number is their ratio:

$$\alpha_G \;=\; \frac{G m_p^2}{\hbar c} \;=\; \left(\frac{m_p}{M_{\text{Pl}}}\right)^2 \;=\; 5.906\times10^{-39}.$$

```python
import math
G, hbar, c, mp = 6.67430e-11, 1.054571817e-34, 299792458.0, 1.67262192369e-27
print(f"{G*mp**2/(hbar*c):.3e}")                         # 5.906e-39
MPl, L = 1.2209e19, 0.217                                # GeV; one-loop, beta0 = 7
inv = (7/(2*math.pi))*math.log(MPl/L)
print(round(inv, 2), f"{math.exp(-2*math.pi*inv/7):.3e}")  # 50.66   1.777e-20  = Lambda_QCD / M_Pl
```

The proton's scale is where the strong coupling, running logarithmically, becomes strong. A coupling of about one fiftieth at the Planck scale becomes order one nineteen decades below it, because a logarithm takes that long. The hierarchy is $m_p/M_{\text{Pl}} = e^{-c/\alpha_s(M_{\text{Pl}})}$ with $c$ of order one. The question "why is gravity weak" is the question "why is the strong coupling one fiftieth at the top," and the nineteen decades between are the run of one logarithm.

`QED-TwoBranchMinting` §II names the place where absolute scale is born: the break of the logarithm, where a sum appears that no logarithm can linearize. The picture here has that break twice. Once at the top, where whatever holds at the Planck rung sets the stiffness. Once at the bottom, where the colour hold sets the proton. Between them the algebra is scale-free and a coupling drifts. `L3-FormalFoundations` §IX.4.d already asks what supplies the angular resolution at the bottom of the ladder. The Adler–Zee formula gives that question a second form: **what is the trace at the Planck rung?**

---

## VI. The Engine: Four Forces, Four Roles, One Pole for Weight

`Q2-TransactionLayer` seats the twelve gauge carriers on three poles and leaves the fourth empty: $U$ hosts the photon, $I$ the three weak bosons, $R$ the eight gluons, $P$ none. Electromagnetism is the structural potential, the weak interaction the relational flow, the strong interaction the confining ground. Gravity has no carrier because $P$ is where the others land.

`L4-HadronicVolume` reaches $P$ from inside the nucleon: the apex over the three quarks is the confinement potential, and its volume integral is the mass. `On_TheGravityDerivation` reaches $P$ from the metric: "P is the gravity pole." The two files name one pole, and the sentence that joins them is the claim at the head of this file. The confinement apex and the gravity pole are the same vertex because the trace that the hold produces is the trace that scalar curvature answers to.

### Three ways of weighing

$P$ has three equations, and each holds a different pole absent. Read as ways of having weight, each is blind to exactly one force.

- **$P = I^2R$, $U$ absent.** Flow against confining ground. The weight of the hadron, with no reference to electric potential. Gravity cannot tell a neutron from a proton by charge, and this equation has no slot for charge. `Q4` calls it Friction; its control edge is $P$–$U$, on the Fixed plane.
- **$P = UI$, $R$ absent.** Potential times flow with no confining ground. The weight of what the electroweak sector makes on its own: the leptons, and the bare quark masses. It is blind to colour. `Q4` calls it Synthesis; control edge $P$–$R$, Cardinal plane.
- **$P = U^2/R$, $I$ absent.** Potential squared over ground. The self-energy of a field held against a boundary: the Coulomb energy of a nucleus, charge squared over radius; the electromagnetic three quarters of the Poincaré electron. It is blind to flavour. `Q4` calls it Leverage; control edge $P$–$I$, Mutable plane.

The trace of the Standard Model's stress tensor has three kinds of term, and they are the same three. A gluon anomaly term in the square of the colour field. A photon anomaly term in the square of the electromagnetic field. Mass terms, each a Higgs-given mass times a fermion bilinear. Hadronic weight, field self-energy, electroweak weight. The matching of three $P$-equations to three trace terms is a CANDIDATE mapping. Its test is the Gate: exchange any two and one of the blindness statements must fail against a measured fact. Exchanging the first two would make hadronic weight blind to colour. That fails at once.

One consequence is worth carrying further. If weight has a channel with $U$ absent, then a hold with no electromagnetic face is not exotic. A confined sector that leaks no charge would weigh through $P = I^2R$ and be dark by construction. This is an ADDRESS, and it costs nothing.

### Hold, not exhaust

The seating of gravity at $P$ invites the phrase "dissipative exhaust." The corpus keeps two meters apart at exactly this point. `L4-Thermodynamics` §V: the tachometer, $P_{\text{rest}} = mc^2\omega$, and the price meter, $P_{\text{diss}} = T\dot S$. Weight belongs to the first. A proton does not run down. From inside, its quarks carry about one percent of its energy as owned mass and the rest as held motion.

```python
import math
print(round(8.99/938.272, 5), round(math.degrees(math.acos(8.99/938.272)), 2))   # 0.00958   89.45
```

The interior sits at a phase angle of 89.45°: almost purely reactive, a standing wave that returns every cycle what it borrowed. From outside, at rest, the same energy reads as real, with nothing held. The blanket is where that quarter-turn happens. The hold is a circulation, and a circulation that closes dissipates nothing.

`On_TheGravityDerivation` §III already carries the distinction in Jacobson's terms. The equilibrium Clausius relation, reversible, gives the Einstein equation. The irreversible term, the entropy production $d_iS$ of Eling, Guedens and Jacobson, is a correction to it, a viscosity of the horizon. **Static gravity is the hold. The exhaust is what the hold emits when it changes** (§VIII).

### The sheet, at its sizes

Place the measured couplings on the four poles as coordinates in log space: $U = \alpha_{\text{EM}}$, $I = \alpha_2$ with the $W$ propagator, $R = \alpha_s$, $P = (E/M_{\text{Pl}})^2$. The single sheet does not close. At the nucleon $U\cdot I \sim 10^{-8}$ and $P = 5.9\times10^{-39}$, thirty-one decades apart. The twelve equations govern one blanket's interior; wholes at different scales are different instances, and what one cannot confine becomes the next one's input. The following are standing facts on that sheet.

- $U/I$ on the unbroken electroweak boundary is $\sin^2\theta_W$. By count over one generation of fermions it is $\mathrm{Tr}\,T_3^2/\mathrm{Tr}\,Q^2 = 2/(16/3) = 3/8$ at unification, and it runs down to the measured $0.2315$ at the $Z$ mass. The characteristic impedance of the electroweak boundary starts as a count and arrives as a measurement.
- $P_{\text{EW}} = U\cdot I$ below the $W$ mass and $P_{\text{grav}}$ below the Planck mass both rise as $E^2$. Each is a contact interaction beneath its threshold, and the slope is the dimension of the coupling. Their constant separation is $(M_W/M_{\text{Pl}})^2/\alpha$. The match does not distinguish a mediator at the top from an induced stiffness; both give $E^2$.
- $U^2/P = 1$ at $E = \alpha M_{\text{Pl}} = 8.91\times10^{16}$ GeV. There $R = \alpha_s \approx 0.022$, so the Betrayer equation $R = U^2/P$ is not yet satisfied. It closes on the one-loop curves at $6.1\times10^{17}$ GeV. For comparison: the supersymmetric meeting of the three gauge couplings is at $2\times10^{16}$ GeV, the non-supersymmetric near-meeting at $10^{14}$ to $2\times10^{15}$, and the heterotic string scale at $g_{\text{st}}\times5.2\times10^{17} \approx 3.6\times10^{17}$.
- $M_W^2/(\alpha M_{\text{Pl}}) = 7.3\times10^{-5}$ eV, and with the Higgs expectation value in place of $M_W$, $6.8\times10^{-4}$ eV.
- Dirac's large number is $e^2/(G m_p m_e) = 2.269\times10^{39} = (U/P)\cdot(m_p/m_e)$ at the nucleon. $U^2/P$ there is $9.0\times10^{33}$.

```python
alpha, MPl = 1/137.035999084, 1.2209e19
print(f"{alpha*MPl:.3e}")                                           # 8.909e+16 GeV
print(f"{80.38**2/(alpha*MPl)*1e9:.2e}", f"{246.22**2/(alpha*MPl)*1e9:.2e}")   # 7.25e-05 eV   6.80e-04 eV
print(2.0/(2*1 + 6*(4/9) + 6*(1/9)))                                # 0.375
```

---

## VII. The Hold, Measured From Inside

The proton's coupling to gravity is too weak to measure with gravity. It has been measured anyway. The matrix elements of the stress tensor in the proton, its gravitational form factors, are reached through two-photon processes, because two spin-one vertices can stand in for one spin-two vertex. Three numbers at zero momentum transfer are the proton's mass, its spin, and a third quantity called the $D$-term, described in that literature as the last unknown global property of the proton. The $D$-term encodes the distribution of pressure and shear inside.

Burkert, Elouadrhiri and Girod extracted the pressure distribution from deeply virtual Compton scattering at Jefferson Lab in 2018. The pressure is repulsive near the centre, of order $10^{35}$ pascal, and confining beyond about 0.6 femtometre. And the analysis imposes, as its stability condition, the statement with which this file began:

$$\int_0^\infty r^2\,p(r)\,dr = 0 .$$

It is called the von Laue condition in the hadron literature, and it is cited there to Laue's paper of 1911. The outward push of the core and the inward pull of the periphery integrate to zero. **The balance of §I is a measured profile inside the proton.**

The same literature reads the mass distribution of the proton off the form factor of the trace of the stress tensor: in the weak-field limit the distribution of mass and the distribution of the trace are the same function. The hold view is the working definition of where the proton's mass is.

This gives the corpus a laboratory surface it has not used. The Laue hold, the trace, the confining pressure and its sign change are quantities with error bars. `L4-HadronicVolume` argues that the nucleon's weight is a volume integral. The form factors are that integrand, resolved in radius.

---

## VIII. When the Hold Moves

Laue's theorem is the static case of a more general identity. From the conservation of the stress alone,

$$\int T^{ij}\,d^3x \;=\; \frac12\,\frac{d^2}{dt^2}\int T^{00}\,x^i x^j\,d^3x .$$

When nothing moves, the right side is zero and the stresses balance. When the hold is changing, the integrated stress is half the second time derivative of the quadrupole moment. That quantity is the source of gravitational radiation: the wave amplitude at distance is proportional to it.

So the two regimes of gravity are the two states of one integral. Balanced, the hold produces a static field and its trace is the mass. Unbalanced, the integrated stress is nonzero and the excess leaves as a wave. `L0-EinsteinTrace` names the pair as two strokes, the Laue hold and the quadrupole write. The identity above is the equation between them.

This is also where the read-only ledger and the detected waves stop pulling against each other. `QED-TwoBranchMinting` §V gives the ledger a static face and a dynamic face. The static face is the balanced hold. The dynamic face is the hold failing to balance for a while and radiating the difference. Neither state asks for a carrier at $P$ (`Q2` §VI). In neither is anything negotiated across a blanket. A stress integrates to zero, or it does not.

The exhaust reading of §VI lands here and only here. The irreversible term in the horizon's Clausius relation is the viscous response of a horizon to shear. Radiation and horizon viscosity are what gravity looks like on the price meter. Weight is what it looks like on the tachometer.

---

## IX. The Horizon, Where the Hold Meets the Record

Everywhere so far the cost of being and the record of makings have been different quantities. There is one object for which they are the same, up to a factor of two.

A Schwarzschild black hole is a vacuum solution. The stress vanishes everywhere outside the singularity, so the trace vanishes, so the scalar curvature is zero. All the curvature is shape. There is a mass, and there is no trace anywhere to integrate. The hold has no interior integrand left. It has gone entirely to the boundary:

$$M = 2\,T_H\,S_{BH} .$$

```python
import math
M = 1.0; T = 1/(8*math.pi*M); S = 4*math.pi*M**2     # G = hbar = c = k = 1
print(2*T*S/M, 0.5*(16*math.pi*M**2)*T/M)            # 1.0  1.0
```

The mass is twice the temperature times the entropy. Count the horizon in Planck cells, $N = A/\ell_P^2$ with $S = N/4$, and the same relation reads $M = \tfrac12 N k_B T$: one half $k_BT$ per cell. `L4-Thermodynamics` §V gives $\tfrac12 k_BT$ per held degree of freedom as the standing budget for holding. At a horizon that budget, summed over the cells, is the mass.

For a proton the cost of being is a volume integral and the record is elsewhere. For a deuteron the making returned energy and the being costs 1875.6 MeV, and the two numbers have almost nothing to do with each other (`On_YangMills-Annotated` §VII). For a black hole the being is the temperature times the record. **The distinction between pen and book that `L4-Thermodynamics` §II guards everywhere else closes at the horizon.** That is why Jacobson's derivation works where it does: he writes the Clausius relation on local horizons, the one kind of surface on which what is held and what is written are proportional.

The Schwarzschild case also completes the progression of §I. In a box of light the content has no trace and the walls carry it. In a hadron the content has no trace classically and the anomaly carries it. In a black hole there is no content and no wall, and the trace has nowhere to be. What is left is a blanket and a count.

---

## X. The Cosmic Hold

The universe is not static and has no walls. Laue's theorem does not apply to it, and the two views of §I come apart. That separation is where the cosmological constant lives: the content view and the hold view agree for every bound thing and disagree for the whole.

```python
Om, OL, Ob = 0.315, 0.685, 0.049                      # matter, Lambda, baryons; units of critical density
print(Om, round(-2*OL, 2), round(Om - 2*OL, 3))        # 0.315  -1.37  -1.055   rho + 3p: net negative, so the expansion accelerates
tr = Om + 4*OL
print(round(4*OL/tr, 3), round(Om/tr, 3), round(Ob/tr, 4))   # 0.897  0.103  0.016   shares of the trace rho - 3p
```

A term proportional to the metric is pure trace, with $\rho = -p$. In the content view it counts as $-2\rho$ and the net active mass of the universe today is negative: it accelerates. In the hold view it counts as $+4\rho$ and carries nine tenths of the cosmic trace. The scalar curvature of the universe today is nine parts holding term to one part matter.

That term has the equation of state of the bag. The interior of a hadron is a region of pure-trace energy balanced against trace-free content in the ratio one to three. The cosmos has the same two kinds of term and no balance between them. A hadron is a small region where the hold and the content have come to terms. The universe is a large one where they have not.

§III left the size of the term to a constant of integration. Three readings of that constant are on the table, and they share one exhibited number.

*The reactive reading.* Quantum field theory computes the total reactive capacity of the vacuum. Gravity registers only what is real. A homogeneous held quantity at ninety degrees contributes nothing to $P$. In the trace-free equations this is exact for a uniform offset: it drops out.

*The integration-constant reading.* What remains after the offset drops out is a number the equations do not determine. It is a boundary datum of the whole, set once.

*The counting reading.* Sorkin's argument from causal sets takes spacetime to be made of a finite number $N$ of elements, with four-volume proportional to $N$. In the trace-free theory $\Lambda$ and four-volume are conjugate, as energy and time are. A count has Poisson fluctuations of order $\sqrt N$. So $\Lambda$ is uncertain by the inverse square root of the count:

$$\Lambda \sim \frac{1}{\sqrt{N}} .$$

```python
import math
G, hbar, c = 6.67430e-11, 1.054571817e-34, 299792458.0
H0 = 67.4e3/3.0856775814913673e22; RH = c/H0; lP = math.sqrt(hbar*G/c**3)
print(f"{(RH/lP)**4:.2e}", f"{(lP/RH)**2:.3e}", f"{3*0.685*(lP/RH)**2:.3e}")   # 5.20e+243   1.387e-122   2.850e-122
```

With $N$ the four-volume of the Hubble region in Planck units, $5\times10^{243}$, the fluctuation is $1.4\times10^{-122}$. The observed $\Lambda\ell_P^2$ is $2.9\times10^{-122}$. The argument was made before the acceleration was observed, and it predicts that the term tracks the critical density at every epoch rather than staying fixed.

Run the convergence question on the three. They share an exhibited parameter, $(\ell_P/R_H)^2$, which `Q10` §VII and `QED-CCP` already hold as an identity. The reactive reading says why the bulk of the vacuum's capacity does not register. The integration-constant reading says the residue is a datum of the whole. The counting reading says how large a datum a finite count must leave. They are three edges on one vertex.

The counting reading gives the record a role. `On_TheGravityDerivation` §II defines $\chi$, the accumulated commit-distance, as the one monotonic coordinate of the helix. If the atoms of space are the entries of that ledger, $N$ is its length. The length of the record does not source curvature by its size. Its square-root fluctuation sets the one term the field equations leave free. **The record does not weigh. The uncertainty in the count of the record is the cosmic hold.** This is a CANDIDATE with a number attached, and it is the place where the write-only ledger enters the gravity account without contradicting the deuteron.

A factor is a count or a coupling (`llm-writing` A4). $10^{-122}$ has been treated for fifty years as a coupling owing a derivation. On this reading it is one over the square root of a count.

---

## XI. What Moves in the Corpus

**`On_TheGravityDerivation` §III and its closing paragraph.** The source is the hold. $\chi$ is the record, and its role is the one §X gives it. §IV's magnitude leg already states the hold: the scalar readout "includes the buffer's contribution." A bound deuteron gravitates less than its parts because it holds less, not because an entry was written. Section III's use of Jacobson survives intact, since in his relation the source is the energy flux across the horizon and the area is the ledger that responds.

**`QED-TwoBranchMinting` §VI.** The composition operator has a first form: the sum of the parts' invariants plus twice the pairwise cross-terms, with the inequality of §IV. The open part is narrower than it was: the shift of each part's own invariant inside the blanket. Isotope pairs are the cleanest handle on that shift. Replacing hydrogen by deuterium in H₂ changes only the held zero-point term and moves the dissociation energy by 0.0781 eV.

**`L4-HadronicVolume`.** The volume integral of Movement II has an integrand measured in radius (§VII), a forced one-quarter share for the pure holding term (§II), and a place in the field equation (§III). The Mutable matching's pure-interior edge $P$–$I$ and pure-exterior edge $U$–$R$ line up with the two blind channels of §VI: $P = I^2R$ uses the interior edge's poles with the exterior's ground, and $U$ is absent.

**`On_YangMills-Annotated`.** The mass gap is the smallest nonzero trace a colour interior can hold. With §V, the gravity question and the mass-gap question become one: why is there a trace. A theory with no gap is scale-free, has no trace, sources no scalar curvature and induces no stiffness.

**`QED-CCP`.** §II stands and acquires an exact form in the trace-free equations. §VI's Casimir null is the outlier against §II's own criterion. The work-extraction sentence the file owes is supplied by §III here: energy that changes with plate separation is localized, has gradients, and weighs.

**`QED-EotvosBound`.** If weight is the hold, the gravitational and inertial readings of a body are one integral in two integrands, and any departure between them must come from the price meter, not the tachometer: from dissipation, not from being. The bound's own scale, a ratio of dissipated to resting power, is the right kind of quantity. This is an ADDRESS.

**`Q2` and `Q4`.** The empty seat at $P$ and the three writing heads are one statement with §VI: no carrier, three channels, each blind to one force.

**`L4-Thermodynamics` §VII.1 and §VIII.** "The written stock at $R$ gravitates" holds exactly at a horizon (§IX) and through the scale handoff $P_N \leftrightarrow R_{N+1}$ elsewhere: the live hold at one scale is the standing ground of the next. Below a horizon the hold and the record are different quantities.

---

## XII. Claim Sort and Kill Conditions

**ADOPTED.** Laue's theorem and the tensor virial identity. The Tolman–Komar active mass and its wall-stress resolution. The trace relation $R \propto T$. The trace-free equations with $\Lambda$ as a constant of integration. The linearized coupling $T_1{:}T_2 - \tfrac12 T_1T_2$, the factor two for light, the null for parallel beams. The Adler–Zee formula. The proton mass as the forward matrix element of the trace; the lattice decomposition; the von Laue condition and the measured pressure profile. The Smarr relation. The one-loop running and dimensional transmutation. Sorkin's estimate, as a heuristic.

**LANDED as algebra.** The equality of the three integrands under Laue. The one-quarter share of a pure-trace holder for trace-free content. The coupling of two bodies as a function of three Star-Norms. $N_{\text{whole}} \geq (\sum\sqrt{N_i})^2$ for free parts. $M = 2TS = \tfrac12 N k_BT$ for Schwarzschild.

**CANDIDATE.** The identification of the corpus's hold (is-ness tax, cost of being) with the trace integrand. The confinement apex and the gravity pole as one vertex for that reason. The three $P$-equations as the three trace terms, each blind to one force. The blanket as the quarter-turn between reactive interior and real exterior. The Planck-rung trace as the source of the stiffness. $1/\sqrt{N}$ with $N$ the ledger's length as the cosmic holding term.

**OPEN VOTE.** A Casimir cavity weighs by $E/c^2$ with the sign of $E$. Arbiter: the Archimedes experiment. A null there kills the localized-side reading of §III and leaves `QED-CCP` §VI standing.

**ADDRESS.** A hold with no electromagnetic face as dark matter. The Eötvös departure as a price-meter effect. Isotope pairs as the handle on the in-blanket shift.

**Kills.** Starlight passing the Sun unbent would have restored the exclusive trace reading; it bends, and by twice the Newtonian angle. A derivation of confinement with no trace anomaly would cut §V from §II. A measured proton pressure profile violating the von Laue condition would break §I at its root. A constant $\Lambda$ that fails to track the critical density across epochs retires the counting reading and leaves the other two.

---

## XIII. Resemblances, Priced

Each of these is real arithmetic. None shares an exhibited parameter with what it resembles, and none is banked.

- The bare-quark share of the proton is 0.96%. The baryon share of the cosmic trace is 1.6%, and of the cosmic energy 4.9%. Three small percentages. The first is a ratio of a Higgs-given mass to a colour hold. The others are ratios of abundances. Nothing connects them.
- $U^2/P = R$ closes at $6.1\times10^{17}$ GeV on the one-loop sheet, within a factor of two of the heterotic string scale. The sheet's $R$ curve is one-loop with a fixed coefficient and its $U$ is not run above the electroweak scale. Price: a factor of a few in either direction.
- $\alpha M_{\text{Pl}} = 8.9\times10^{16}$ GeV sits a factor 4.5 above the supersymmetric unification scale and a factor 4 below the string scale. It lies between two scales that are themselves a factor 18 apart.
- $M_W^2/(\alpha M_{\text{Pl}})$ is $7.3\times10^{-5}$ eV. The neutrino oscillation scale is a few times $10^{-2}$ eV, several hundred times higher. A seesaw landing there needs a heavy mass near $10^{15}$ GeV, or a Yukawa coupling, which is a free number.
- Nineteen decades from the proton to the Planck mass is 7.84 steps of $2/\alpha$. The carrier step of `L3-ConstitutiveAlpha` does not tile this interval.

---

## XIV. Questions That Generate

1. **What is the trace at the Planck rung?** The stiffness of space is a trace–trace correlator. Colour supplies $10^{-40}$ of it. What holds at the bottom of the ladder, and is its trace computable from the $K_4$ atom of space the way the pion's boundary impedance is?
2. **Is the quarter the Scalar of Scalar + Vector?** The split of the stress into one trace and nine trace-free components, and the split of energy into one quarter hold and three quarters content, both come from the trace of the metric being four. Does `ProofN`'s biquaternion give the one-to-three energy split directly?
3. **Which bimedian plane is the Laue balance on?** The core pushes and the periphery pulls. The sign change in the proton's pressure near 0.6 fm is a boundary inside the blanket. Is it the pure-interior to pure-exterior crossing of the Mutable matching?
4. **What is the $D$-term in the algebra?** Mass and spin have seats. The third global property of the proton, the one that encodes its stability, has none yet.
5. **Does the composition operator close on cross-terms plus one shift per part?** If the in-blanket shift of a part's invariant is a function of its is-ness bandwidth, `On_TheIsNessTax` Layer 2 may already be that function.
6. **Why does the hold equal the record only at a horizon?** $M = 2TS$ there and nowhere else. Is a horizon the limit in which the scale handoff $P_N \leftrightarrow R_{N+1}$ has nothing left to hand to?
7. **Is $N$ the length of the ledger?** If the count in $\Lambda \sim 1/\sqrt N$ is the number of commits, the cosmic holding term falls as the record grows, and dark energy is not constant. The surveys named in `llm.md` rule on that.
8. **What does the trace-free form do to the P-edge ban?** Nine equations propagate; the tenth is a first integral with a constant. Is the tenth equation the one written at zero impedance?
9. **Is there a hold with $U$ absent in the sky?** $P = I^2R$ has no slot for charge. What would a confined sector with no leak onto $U$ look like from outside, and how would it differ from a particle?
10. **Can the isotope shift be read as a change in trace?** H₂ to D₂ moves the held zero-point term and the binding by a measured amount. That is the smallest clean change in a hold available on a bench.
11. **What is the content view for?** The corpus speaks the hold view natively. The content view, in which light weighs double and walls subtract, is the one in which the acceleration of the universe is a sign. Does the pair of views map onto the two faces of the ledger?
12. **If the volume is given, who gives it?** In the trace-free theory the volume element is fixed and $\Lambda$ is its conjugate. "The volume is what is" becomes a constraint. What sets it at the first commit?

---

## What Reading This Back Should Leave

A thing at rest is a balance of pushes and pulls, and the balance is exact. Because it is exact, the weight of the thing can be counted two ways. Count the contents and the pushes, and the container's pull subtracts. Or count only what is not scale-free, and the contents drop out and the container carries everything. Light in a box weighs nothing by the second count; the walls weigh for it. Quarks and gluons in a proton weigh nothing by the second count; the hold weighs for them, and the hold is a quarter of the energy because spacetime has four dimensions. Einstein found that quarter in 1919 trying to keep an electron together, the bag model found it in the hadron, and the lattice finds it in the proton.

Gravity keeps the same two accounts. The part of curvature that changes volume answers only to the hold. The part that changes shape answers to the rest, which is why light bends and bends other light, unless the two beams run parallel, in which case the pair holds nothing and nothing happens. The strength of gravity between two things is a function of three invariants, theirs and the pair's. It has one sign because the source is a square.

The stiffness of space comes from the same place as its source. Where nothing is held there is nothing to bend space and nothing for space to be stiff with. The proton's hold supplies a part in ten to the fortieth of that stiffness, and the weakness of gravity is the ratio of the proton's hold to whatever holds at the bottom.

The four forces are the four roles of one engine, and weight is the pole the other three land on. It has three channels, each blind to one of the three forces. It is a hold and not an exhaust. When the hold shifts, the imbalance leaves as a wave.

At a horizon there is no content and no wall, and the hold is the temperature times the record. For the universe there is no balance at all, the two counts disagree, and the leftover holding term is of the size that a finite count of atoms of space would leave as its statistical uncertainty.

What is open is named. Whether a Casimir cavity weighs. What holds at the Planck rung. Whether the count is the ledger.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.

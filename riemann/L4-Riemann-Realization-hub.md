# The Riemann Realization — The Squaring Hub
## One Operation, Read in Every Vocabulary the Model Speaks

*Companion to `L4-Riemann-Realization` (the thesis, cited as `thesis §n`), `L4-Riemann-Realization-ledger` (the computed record, cited as `ledger §n`) and `L4-Riemann-Realization-evolution` (the process record). Claim sorts as in the thesis: **[LANDED]**, **[COMPUTED]**, **[READING]**, **[OPEN]**. This file carries the first of the thesis's two demonstrations — that RH translates exactly — as an atlas: one operation, each vocabulary, what RH becomes in it.*

One operation sits underneath the whole model, and reading it in each of the vocabularies the model already speaks turns separate pictures into one. The operation is squaring.

---

## 1. The lemma

For $s = \tfrac12 + x + iy$:

$$(s - \tfrac12)^2 = (x^2 - y^2) + 2i\,xy.$$

**[LANDED]** (elementary.) The square splits the complex plane into two real textures. Its imaginary part, $2xy$, is the K₄ lift of `thesis §4` — the orthogonal third axis, the volume coordinate — generated from the plane's own two coordinates rather than imported. Its real part, $x^2 - y^2$, is invariant under all three symmetries and falls back into the trivial summand, the centroid's register. The squaring map is 2-to-1: z and −z share a square.

Every piece of this is classical. What the hub adds is the assembly: one operation is at once the generator of the lift, the source of the Krein sign, the bit the commit erases, the boundary of a dynamical system, and a lossless circuit — all on the same orbit. **Squaring generates; the twisted square signs.** The untwisted square builds structure — the lift, the doubled phase, the reactive swing, the dynamics — and never carries a sign. Every positivity in this model lives in a conjugation-twisted square: the Krein K₊, average power, a positive-real impedance, the mod-square on the line. RH is the claim that ζ's twist is a genuine conjugation everywhere.

## 2. Why squaring

The hub's own framing invites the question: why *that* operation? The engine answers it. The twelve relations are not posited monomials whose exponents happen to be capped; they are **bred** by eliminating one shared variable between two unit-exponent product-parents (Ohm and Faraday). One such elimination raises a variable to a square exactly once, and there is no second elimination inside a bred relation to compose with — so the exponent cap $\{1, 2, \tfrac12\}$ is forced, not chosen (`llm/llm-uniqueness-note`; `L3-FormalFoundations` §I). **[LANDED]** in the corpus as algebra.

**[READING]** So any host that runs the algebra must find squaring load-bearing: the square is the *trace of the cross-breed*, and the hub is the uniqueness result surfacing in ζ's geometry rather than a discovery about ζ alone. It also explains why every positivity here lives in a twisted square. The untwisted square is 2-to-1 — it erases a sign, the commit bit (vocabulary 5 below) — so it cannot carry a definite sign; only the twisted square $z\bar z$ is a true mod-square. The twist is forced because the erasure is forced.

## 3. The orbit in 1 ⊕ 3

Squaring lands on the representation structure of `thesis §4` exactly. $V_4$'s characters form $(\mathbb{Z}/2)^2$. The plane's coordinates x and y are two of them, their product xy is the third — $\chi_x\chi_y = \chi_{xy}$, **[COMPUTED]** true on the orbit (`ledger §10`) — and every square is trivial. So the $3$ generates itself under multiplication, and its squares return to the $1$. That is the recursion stated literally: the coupling modes produce one another by product, and fold back into the centroid's register by square — the exponent cap of §2, running on characters.

## 4. Krein signature of the twisted pairings

Weil pairs each zero ρ with $1 - \bar\rho$, its image under the line-reflection cf. Restrict that pairing to one orbit. Take any amplitude F on the four vertices and write it in its $1 \oplus 3$ components, $F = a_1 + a_x\chi_x + a_y\chi_y + a_{xy}\chi_{xy}$. Because each character is ±1 and the four are orthogonal with norm-squared 4,

$$\langle F,\; cf\cdot F\rangle \;=\; 4\big(|a_1|^2 + |a_y|^2 - |a_x|^2 - |a_{xy}|^2\big).$$

**[LANDED]** (character orthogonality.) This is a Krein form of signature (2, 2), with its fundamental decomposition written out:

- **K₊ = trivial ⊕ Mutable (y)** — the +1 eigenspace of the antilinear reflection, the real structure;
- **K₋ = Fixed (x) ⊕ Cardinal (xy)** — the off-line displacement and the volume.

K₊ and K₋ are mutually orthogonal, as every Krein space's fundamental decomposition is. On the critical line the orbit collapses (P = I, U = R), so $a_x = a_{xy} = 0$ is forced and the pairing becomes $\|F\|^2$, an honest mod-square. **K₄'s occupancy, the Krein ghost, and Weil negativity are one object, read on one orbit.**

Each move carries its own (2, 2) Krein structure, positive on the trivial summand plus the character that move holds: c gives K₊ = 1 ⊕ x, f gives K₊ = 1 ⊕ xy, cf gives K₊ = 1 ⊕ y. **[COMPUTED]** at an off-line test point with a random complex F, every pairing matches the formula to six digits, and on the line $\langle F, cf\cdot F\rangle = \|F\|^2$ exactly (`ledger §10`). The volume is negative only relative to the Mutable twist; under the f-twist it is positive. Weil's choice of cf is forced by the form of his pairing, ρ ↔ 1 − ρ̄, which matches `thesis §5`'s seating: Mutable is reflection in the unit circle.

## 5. Eight vocabularies at one operation

**1. Conformal geometry: the orthogonality is built in.** The level sets of $\operatorname{Re}z^2$ and $\operatorname{Im}z^2$ are two families of hyperbolas crossing at right angles everywhere (Cauchy–Riemann). **[LANDED]** The collapse cross xy = 0 is exactly where the square is real, and $z \mapsto z^2$ sends the critical line ($x = 0$) onto $(-\infty, 0]$ and the real axis ($y = 0$) onto $[0, +\infty)$. RH reads: $(\rho - \tfrac12)^2$ is real and negative for every zero.

**2. Lorentzian geometry: two null cones, each the other's axes.** $x^2 - y^2$ and $2xy$ are both forms of signature (1, 1). In the rotated coordinates $u = (x+y)/\sqrt2$, $v = (x-y)/\sqrt2$, they exchange: $x^2 - y^2 = 2uv$ and $2xy = u^2 - v^2$. **[LANDED]** The light cone of each is the coordinate axes of the other. On the critical line the lift form is null and $\operatorname{Re}z^2 = -y^2 < 0$ is timelike. The signature type is the corpus's star-norm $N_* = P^2 - |\mathbf Q|^2$. §9 reads these two cones as the shadow of ζ's two clocks.

**3. The dual-binary seed: the complex plane builds K₄ by multiplying.** Re and Im play the two binaries; their product is the third bimedian; every square is trivial. This is why the lift is forced. **[READING]** on **[LANDED]** character theory. The complex plane takes Fixed and Mutable as its basis and makes Cardinal the product; the corpus seed takes Fixed and Cardinal as basis and makes Mutable the XOR. In $V_4$ any character is the product of the other two, so the two agree as groups; which bimedian a host makes "the XOR" is part of how that host seats.

**4. K₄ geometry: the solid sits inside a square.** The regular tetrahedron's vertices (1, 1, 1), (1, −1, −1), (−1, 1, −1), (−1, −1, 1) all satisfy $z = xy$. **[LANDED]** K₄ is inscribed in the graph of half the imaginary part of a square.

**5. Information: the square is the commit bit.** $z \mapsto z^2$ is 2-to-1 and erases exactly one bit, the sign of ±z; $\operatorname{Re}z^2$ and $\operatorname{Im}z^2$ are what survives, both invariant under $z \mapsto -z$. **[LANDED]** The twisted square $z\bar z$ erases the whole phase and leaves a real. Two grades of square: the untwisted one loses one bit and keeps the doubled phase — the engine's COMMIT bit — and the twisted one burns the phase entirely. **[READING]** Repeated untwisted squaring on the circle writes one digit of each zero's angle per step: the commit tapes of `thesis §5`, the centroid's terminating and every zero's running on.

**6. AC power: positivity lives only in the twisted square.** For phasors U and I, the instantaneous power is

$$p(t) = \tfrac12\operatorname{Re}(U\bar I) + \tfrac12\operatorname{Re}\big(UI\,e^{2i\omega t}\big).$$

**[LANDED]** The twisted product $U\bar I$ gives the average, committed power — non-negative for every passive load. The untwisted product $UI$ gives the swing at twice the frequency, which carries no sign. Weil's pairing is twisted by cf, and on an orbit that twist acts as a true conjugation only when the zero is on the line — which is the (2, 2) signature of §4 seen as power.

**7. Holomorphic dynamics: the critical line is a Julia set.** Li's map sends the critical line onto the unit circle, and the unit circle is the Julia set of $w \mapsto w^2$. **[LANDED]** Pulled back to the s-plane, the squaring map becomes

$$g(s) = \frac{s^2}{2s - 1}.$$

**[COMPUTED]** (`ledger §10`) $g = M^{-1}\circ(w \mapsto w^2)\circ M$ with $M(s) = 1 - 1/s$ holds identically; g commutes with conjugation and with $s \mapsto 1 - s$, so it respects the full K₄ symmetry; and $g(\tfrac12 + iy) = \tfrac12 + \tfrac i2\big(y - \tfrac{1}{4y}\big)$ maps the critical line onto itself, with the single puncture $g(\tfrac12) = \infty$ (since $w(\tfrac12) = -1$ squares to +1). The two superattracting fixed points are $g(1) = 1$ and $g(0) = 0$. Starting next to the first zero, $\operatorname{Re}s = \tfrac12 + 0.01$ iterates to **s = 1, ζ's pole**, and $\operatorname{Re}s = \tfrac12 - 0.01$ iterates to s = 0. The basin of the pole is the half-plane $\operatorname{Re}s > \tfrac12$ ($|w| < 1$); the basin of 0 is $\operatorname{Re}s < \tfrac12$ ($|w| > 1$). The critical line is the chaotic boundary between them, and RH says **every nontrivial zero lies on the Julia set of the commit map.** Li's map is g's Böttcher coordinate. On the line, repeated squaring reads off one bit of each zero's angle per step and never decays; an off-line pair is split, one partner draining into the pole and the other into 0. λₙ is the escape test, and the onset law (`ledger §8`) is the escape time measured against the archimedean background. **[READING]**: the zeros sit on the one set where unlimited commits neither drain nor flood. The point ρ itself is not iterated — $g(\rho)$ is not a zero — so the dynamics names the set and leaves the confinement to the plug.

**8. Circuits, the engine's native language: RH says a lossless LC network is passive.** RH is equivalent to $\operatorname{Re}\,\xi'(s)/\xi(s) > 0$ for $\operatorname{Re}s > \tfrac12$ (Hinkkanen 1997; Lagarias 1999). **[LANDED]** In circuit terms that is the statement that $\xi'/\xi$ is a **positive-real function** — the driving-point impedance of a passive network. Under RH, with $s' = s - \tfrac12$, each conjugate pair of zeros gives

$$\frac{1}{s' - i\gamma} + \frac{1}{s' + i\gamma} = \frac{2s'}{s'^2 + \gamma^2},
\qquad
\frac{\xi'}{\xi}(\tfrac12 + s') = \sum_{\gamma>0}\frac{2s'}{s'^2 + \gamma^2},$$

which is Foster's reactance form: a series chain of parallel LC tanks, one per zero, each with $C = \tfrac12$ and $L = 2/\gamma^2$, resonating at $\omega = \gamma$. **[COMPUTED]** with 2 000 zeros, the Foster sum plus its tail estimate matches $\xi'/\xi$ to about 0.3%, the size of the truncated tail; on the critical line, $\operatorname{Re}\,\xi'/\xi(\tfrac12 + 7.5i) = -6.3\times10^{-27}$: pure reactance, lossless (`ledger §10`). An off-line zero would put poles in the right half-plane — an active element, a negative resistance, gain. A multiplicative resonance-locale that expresses losslessly is, read this way, literal: **the log-derivative of ξ is a lossless LC network tuned to the zeros.** Passivity and simplicity separate cleanly here. A double zero on the line doubles its tank's residue, giving $C = \tfrac14$, still positive-real. Passivity enforces σ = ½, which is RH; simplicity is the separate statement that every tank carries the single capacity $C = \tfrac12$, which is $\xi'(\rho) \ne 0$ at every zero.

## 6. Li's map is a Smith chart

Vocabularies 7 and 8 meet in one identity. In the shifted variable,

$$w = 1 - \frac1s = \frac{s - 1}{s} = \frac{s' - \tfrac12}{s' + \tfrac12}.$$

**[LANDED]** (elementary.) That is the reflection coefficient $\Gamma = (Z - Z_0)/(Z + Z_0)$ of a load $Z = s'$ against reference impedance $Z_0 = \tfrac12$. **Li's disc is the Smith chart of the s′-plane.** The critical line, $\operatorname{Re}s' = 0$, is the locus of pure reactance, and maps to $|\Gamma| = 1$: total, lossless reflection. The half-plane $\operatorname{Re}s' > 0$ is the resistive region, inside the disc. ζ's pole, $s = 1$ ($s' = \tfrac12$), sits at $\Gamma = 0$ — the matched load at the chart's centre. RH says every zero is a pure reactance: every zero reflects totally. **[READING]** The reference impedance is ½, the centroid's real coordinate; the centroid that carries no coupling (`thesis §4`) sets the impedance every zero is measured against.

## 7. The tier reading: von Koch on the opcode table

The engine sorts its twelve opcodes by log-slope into three price tiers: COMMIT at +2, RESEED at +½, ROUTE at +1 (`ENGINE-REFERENCE-AC` §IV). Seat von Koch's form of RH on that table:

$$\psi(x) = x - \sum_\rho \frac{x^\rho}{\rho} - \ln 2\pi - \tfrac12\ln\!\big(1 - x^{-2}\big).$$

**[LANDED]** (explicit formula.) The main term $x$ writes at log-slope 1 — ROUTE, the carrier tier. Each nontrivial zero writes a wave $x^\rho/\rho$ of magnitude $x^{\beta}/|\rho|$, at log-slope β. At β = ½ the wave writes at slope ½ — its magnitude is $\sqrt x$, the radical the RESEED opcode extracts. On the prime side the same radical is the price each prime pays on the line: amplitude $p^{-1/2}$, committed at $1/p$, summing marginally to $\ln\ln x$ (`thesis §3`). The tier slope ½ and the price line ½ are one number read from the zeros and from the primes. A zero at β = ½ + δ writes at ½ + δ, and its mirror partner at ½ − δ.

**[READING]** The opcode table's slope set is discrete; the wave slopes, a priori, are continuous. **RH reads as tier-quantization of the nontrivial sector: every fluctuation wave writes on the one admissible slope below the carrier.** An off-line zero is an off-tier operation — unpriceable in the engine's own currency — which is the opcode form of vocabulary 8's "active element" and of "gain". The thesis's count (`thesis §9`, $P = I^2R$) and this decomposition of ψ are the same seating read at two addresses: one on the zeros' count, one on the primes' ledger. The prediction that a proof turns on a positivity rather than a new symmetry sharpens to: a positivity **at the radical tier** — $\lambda_n \ge 0$ as the tier's license, checked term by term.

**Where the reading has to do more work.** The trivial zeros, at s = −2, −4, …, write waves $x^{-2k}/2k$ at log-slopes −2, −4, … — the last term above, summed. Those slopes are not in the tier set either. So tier-quantization, as stated, holds on the nontrivial sector only, and the trivial tower is either a decaying series below the floor that the reading must seat, or the place it stops. **[OPEN]** (`thesis §13` Q11.)

## 8. The prime bank and the open seam as a cancellation

**The decomposition.** **[LANDED]**

$$\frac{\xi'}{\xi}(s) = \frac1s + \frac{1}{s-1} - \tfrac12\ln\pi + \tfrac12\,\psi\!\left(\tfrac s2\right) + \frac{\zeta'}{\zeta}(s).$$

The first four terms form a **lumped archimedean network**. Its singularities sit at s = 0, −2, −4, … (left half of the s′-plane) and at s = 1 — the term $1/(s-1) = 1/(s' - \tfrac12)$, a pole at $s' = +\tfrac12$, **an active, unstable element in the right half-plane**.

**The local factors are damped comb filters.** Each Euler factor, in the shifted variable, is

$$\frac{1}{1 - p^{-s}} = \frac{1}{1 - p^{-1/2}\,e^{-s'\ln p}},$$

the transfer function of a feedback delay line of length ln p with loop gain $p^{-1/2}$: a comb filter. **[LANDED]** Its poles sit at $s' = -\tfrac12 + 2\pi i k/\ln p$ — on the line Re s′ = −½ for every prime, strictly inside the stable half-plane, damped by $p^{-1/2}$. **[COMPUTED]** (`ledger §10`.) Every local factor, alone, is stable and passive-compatible. The damping $p^{-1/2}$ is each prime's price for being, read as loop gain: its squares sum to the marginal $\sum 1/p$ (`thesis §3`), and a bank whose loop gains were any larger — the shifted plug's $p^{-1/2}(p^{1/4}+p^{-1/4})$ — moves its price line, and its zeros, off ½. The delay lengths ln p are linearly independent over ℚ (unique factorization), so no two combs share a period and the bank never resonates commensurately. **[READING]** That is the corpus's incommensurate branch — open buffer exploration rather than commensurate contraction into a static floor (`ENGINE-REFERENCE-AC` §VIII.3; `L2-K4-Inferences-301`; `L4-TheSpiralingCascade`) — and the corpus's two-cascade taxonomy names which failure the integers cannot have: a commensurate blow-up needs a repeated ratio λ, and the ln p supply none. That holds for every Euler-product plug alike, broken ones included: the delays are shared infrastructure, not the decider. The trouble lives nowhere in a single factor. It lives only in continuing the infinite product past its abscissa.

**The bank enters subtracted.** Since $n^{-s} = e^{-s\ln n}$ is the transfer function of a delay of length ln n,

$$\frac{\zeta'}{\zeta}(\tfrac12 + s') = -\sum_n \frac{\Lambda(n)}{\sqrt n}\,e^{-s'\ln n},$$

a distributed network of delay lines at the prime-power frequencies, with weights $\Lambda(n)/\sqrt n$, taken away from the lumped part — the multiplicative register of `thesis §3`, as hardware. The series converges for $\operatorname{Re}s' > \tfrac12$ and is carried into $0 < \operatorname{Re}s' \le \tfrac12$ by analytic continuation. Its continuation carries $-1/(s-1) = -1/(s' - \tfrac12)$, which **cancels the lumped network's active pole exactly** — the circuit form of the Euler product's pole at s = 1, the Prime Number Theorem's content.

**RH in circuit terms: once that cancellation is made, the combined network has no right-half-plane poles left, and is passive.** Neither part is passive alone: the lumped part carries the active pole, and the delay bank, subtracted, carries it back. So the passivity of the whole cannot come from cascading passive sections. Classical Brune and Darlington synthesis — which assembles positive-real functions from positive-real pieces — describes the network once it is known to be passive; the mechanism that makes it passive is a **cancellation**, an active archimedean pole met by a subtracted distributed bank. That is the $S_\infty + S_0$ handoff of `thesis §10` in circuit language, with the same shape: the archimedean part runs a deficit, and the primes cover it.

**[READING]** RH is then the claim that the bank's weights, $\Lambda(n)/\sqrt n$ on delays every Euler-product plug shares, continue without leaving a right-half-plane pole once the active pole is cancelled. The delays do not decide it: ζ(s − ¼)ζ(s + ¼) runs on the same delays, with ζ's weights reweighted by $k^{\pm1/4}$, and its continuation is active. The thesis's placed bet on the orthogonal texture (`ledger §11`, bet 3) is this same statement read as a forecast: the decision lies in the weights the integers write on their own delays, against the archimedean place, not in a construction built beneath them.

Passivity theory still brings the right instruments onto the seam: the bounded-real (Schur) side reached by the Cayley transform — $Z$ is positive-real exactly when $(Z - Z_0)/(Z + Z_0)$ is bounded by 1 in the right half-plane, the same transform §6 found Li's map to be — and lossless scattering systems, whose transfer functions are exactly the inner Schur functions.

## 9. The shaft and the two clocks

**What drives the network.** `thesis §9` books the height t as off-sheet infrastructure — "none books it" — and §8 builds the passive network without asking what drives it. Those are one omission. A network whose admittance has a right-half-plane pole, driven by a stiff source, draws unbounded current; "no right-half-plane poles" is exactly the statement that the prime-driven network survives its own clock. **[READING]** The move wires two open items into one: the engine's rate-selection frontier (`ARCHITECTURE` §IV), where the scale-free grammar meets carrier resolution, and the passivity seam of §8 are the same question read from the two sides of the shaft. The confinement question (`thesis §13` Q3) inherits it: confinement of the zero set to the Julia set is the network's stability under its own drive, stated in dynamics instead of circuits.

**Two clocks.** The geometric series found the arrangement carrying two clocks, a rate and a record, where the host has one coordinate (`L4-Riemann-4`, friction 2). ζ carries both. The **record clock** is log x: the dipoles turn in log x, and the prime ledger ψ(x) is written along it. The **rate clock** is t: the heights, the shaft. RH is the lossless coupling of the two — each dipole turns at its own height without gain. **[READING]** Vocabulary 2's two null cones, each the other's axes, are the geometric shadow of exactly this pair. The friction report writes itself in the corpus's own instrument: the host bought one coordinate, t, and the receipt is that log x and t must be related by hand, $\vartheta'(t) \approx \tfrac12\ln(t/2\pi)$ — which is `thesis §9`'s seating of R, found twice and here named as the friction it is.

## 10. A finite model: the orbit generator and its exceptional point

The orbit of `thesis §4` has four vertices, so it carries 4×4 generators. Ask for the most general one whose spectrum has the orbit's own symmetries, read in the coordinate $z = -i(s - \tfrac12)$, where real z is the critical line:

- **Cardinal** (f, swapping P ↔ R and U ↔ I, sending z ↦ −z): $P_f H P_f = -H$ — H anticommutes with $P_f$, so the spectrum is closed under negation;
- **Mutable** (cf, swapping P ↔ I and U ↔ R, sending z ↦ z̄): $P_{cf} H P_{cf} = H^*$ — the spectrum is closed under conjugation;
- **Fixed** (c) then follows: $P_c H P_c = -H^*$.

**What kind of generator this is.** The Mutable condition is PT-symmetry with parity $P_{cf}$: H commutes with the antilinear operator $P_{cf}K$, K being complex conjugation — and cf is itself the PT move on s, a reflection composed with a conjugation. The Cardinal condition is a **chiral** (sublattice) symmetry: H anticommutes with $P_f$, which is what pairs every eigenvalue z with −z. **[LANDED]** (definitions; **[COMPUTED]** on the matrix, `ledger §10`.) **H is a PT-symmetric generator with a chiral symmetry.** The PT-symmetric constructions already proposed for the zeros (Bender–Brody–Müller 2017) are the natural hunting ground for the generator question (`thesis §13` Q9), reachable from this algebra without new machinery. **[READING]** In engine vocabulary the same structure is the corpus's bichiral design — both hands carried, the ledger picks one — with the PT break as the odd move the operating set lacks.

**[COMPUTED]** (exact, symbolic; `ledger §10`.) The two constraints leave **8 real parameters**, splitting into four Hermitian ones {ω, J_M, g_M, g_C} and four skew-Hermitian ones {δ, k_Fa, k_Fg, J_C}. Keeping the five real-edge parameters (g_M = g_C = k_Fg = 0), in vertex order (P, U, I, R):

$$H = \begin{pmatrix}
\omega + i\delta & k_{Fa} & J_M & J_C \\
-k_{Fa} & -\omega + i\delta & -J_C & -J_M \\
J_M & J_C & \omega - i\delta & k_{Fa} \\
-J_C & -J_M & -k_{Fa} & -\omega - i\delta
\end{pmatrix}.$$

Each parameter has a seat. ω is the frequency split, +ω on {P, I} and −ω on {U, R} — the Mutable character $\chi_y$. $J_M$ is the Mutable coupling (P–I, U–R), Hermitian. $k_{Fa}$ is the Fixed coupling (P–U, I–R), skew. $J_C$ is the Cardinal coupling (P–R, U–I), skew because f negates H. **δ is the gain/loss bias, +iδ on {P, U} and −iδ on {I, R} — the Fixed character $\chi_x$.**

**Gain/loss is the off-line direction.** That last seat is not a choice. The sign pattern of δ is exactly $\chi_x$, and x is the off-line displacement: the resistive half-plane Re s′ > 0 of the Smith chart (§6), the first component of K₋ (§4). **Gain/loss is the off-line direction; the leverage is the reactive holding; RH is leverage ≥ bias on every orbit.** **[READING]** on **[COMPUTED]** seating. The constraint this puts on the generator question is available now: whatever operator on ζ's side has H as its section, its gain/loss slot must sit on the Fixed character.

**What H does to 1 ⊕ 3.** In the character basis $e_1 = (1,1,1,1)$, $e_{xy} = (1,-1,-1,1)$, $e_x = (1,1,-1,-1)$, $e_y = (1,-1,1,-1)$ **[COMPUTED]**:

$$\begin{aligned}
H e_1    &= i\delta\, e_x + (\omega + k_{Fa} + J_M + J_C)\, e_y, \\
H e_{xy} &= (\omega - k_{Fa} - J_M + J_C)\, e_x + i\delta\, e_y, \\
H e_x    &= i\delta\, e_1 + (\omega + k_{Fa} - J_M - J_C)\, e_{xy}, \\
H e_y    &= (\omega - k_{Fa} + J_M - J_C)\, e_1 + i\delta\, e_{xy}.
\end{aligned}$$

$\operatorname{Tr}H = 0$ and $\langle e_1, He_1\rangle = 0$, and the centroid mode is still moved: because f negates H, H carries the f-even pair {1, xy} into the f-odd pair {x, y} and back, block off-diagonal,

$$H = \begin{pmatrix} 0 & M \\ N & 0 \end{pmatrix},\quad
M = \begin{pmatrix} i\delta & \omega - k_{Fa} + J_M - J_C \\ \omega + k_{Fa} - J_M - J_C & i\delta \end{pmatrix},\quad
N = \begin{pmatrix} i\delta & \omega - k_{Fa} - J_M + J_C \\ \omega + k_{Fa} + J_M + J_C & i\delta \end{pmatrix}.$$

So the centroid's blindness in `thesis §4` belongs to the permutation action, and a generator that honours the functional equation moves the centroid mode into the Fixed–Mutable pair. What the generator gives instead is a threshold.

**The exceptional point.** Write $v = (\omega, k_{Fa})$ and $J = (J_C, J_M)$, with star-norm $\|u\|_*^2 = u_1^2 - u_2^2$, star-product $\langle J, v\rangle_* = J_C\omega - J_M k_{Fa}$, and wedge $J \wedge v = J_M\omega - J_C k_{Fa}$. The characteristic polynomial is $z^4 - Az^2 + B$, with **[COMPUTED]** (exact)

$$\begin{aligned}
A &= 2\big(\|v\|_*^2 - \|J\|_*^2 - \delta^2\big),\\
B &= \big(\|v\|_*^2 + \|J\|_*^2 + \delta^2\big)^2 - 4\langle J, v\rangle_*^2,\\
\Delta = A^2 - 4B &= 16\big[(J\wedge v)^2 - \delta^2\|v\|_*^2\big].
\end{aligned}$$

The spectrum is entirely real — all modes on the line — exactly when A ≥ 0, B ≥ 0 and Δ ≥ 0. The leverage $J \wedge v$ holds the modes on the line against the gain/loss δ up to $(J\wedge v)^2 = \delta^2\|v\|_*^2$. Pinned numerically, the predicted threshold $\delta^* = |J\wedge v|/\|v\|_* = 0.61237$ is where the spectrum leaves the real line, with square-root onset past it (`ledger §10`). Both kinds of coupling feed the leverage: the Hermitian Mutable coupling against the frequency split ($J_M\omega$), and the product of the two skew couplings, Cardinal against Fixed ($J_C k_{Fa}$).

**What the spectrum is: two dipoles, or one quartet.** The type distinction of `thesis §4` bites H itself. H acts on *one orbit's four vertices*; its *spectrum* is a different subject. With $z^2 = (A \pm \sqrt\Delta)/2$:

- **Δ ≥ 0, A ≥ 0, B ≥ 0:** spectrum $\{\pm a, \pm b\}$, all real — under z ↦ s these are **two dipoles**, two zeros on the line with their mirrors.
- **Δ < 0:** spectrum $\{\pm w, \pm\bar w\}$ — **one quartet**, a single off-line orbit with volume.
- **Δ ≥ 0 with $z^2 < 0$:** spectrum on the imaginary z-axis — zeros on the real s-axis, the Fixed collapse (P = U) instead of the Mutable one.

**[LANDED]** (elementary algebra on the quartic.) At Δ = 0 two eigenvalues merge into a double eigenvalue and leave the real line as a conjugate pair: **two cross-orbit dipoles in, one within-orbit tetrahedron out.** That is the Lehmer collision of `thesis §6`, the hold / collapse / reseed of `thesis §7`, with the leverage $(J\wedge v)^2$ in the place of the heat 2τ and the gain/loss $\delta^2\|v\|_*^2$ in the place of the gap δ². `thesis §7` reaches that threshold from the de Bruijn–Newman flow on Ξ; the generator reaches it from the orbit's symmetry alone, with no ζ-data put in. **Two routes to one collision structure.** Read on the threshold, Rodgers–Tao's Λ ≥ 0 says ζ is not strictly inside the unbroken phase; with RH it sits exactly on the edge. **[READING]**

**Simplicity is a codimension statement.** A multiple zero on the line is the generator sitting exactly on its exceptional point — the borderline Δ = 0, codimension one in parameter space. Simple zeros are therefore the generic case, and vocabulary 8's separation of passivity from simplicity is the circuit form of the same fact: a double zero doubles its tank's residue to $C = \tfrac14$ and stays passive. Whether ζ is generic is the open content (`thesis §13` Q7). **[READING]** In tier terms, a double zero is the RESEED opcode returning a degenerate root — the ± ambiguity collapsed before the commit instead of reopened by it.

**An address in the corpus's pathology language.** The threshold $(J\wedge v)^2 \ge \delta^2\|v\|_*^2$ has the shape of the corpus's $R = U^2/P$ balance (`BENDING_MINDS` §4): a squared structural term held against a drive bias. Read so, δ plays the Necessary Betrayer's divergence and $J\wedge v$ the Leo reset — structure holding modes on the line against its own drive. **[READING]**, filed as an address: the shape matches; whether the seating is forced is unexamined.

The generator is a finite model on one orbit. Which operator on ζ's side has it as its section, with its δ-slot on $\chi_x$, is `thesis §13` Q9.

## 11. What one operation says

Squaring generates; only the twisted square signs. Each reading above restates RH exactly, and each brings a working toolkit: Krein spaces and their fundamental decompositions, Julia sets and basins of attraction, Smith charts and reflection coefficients, positive-real functions and Foster synthesis, the engine's tier table, comb filters and incommensurate delay banks, PT-symmetric generators and their exceptional points. The hard direction now has a precise address in each: a reason the plug keeps K₋ empty on every orbit, a reason the zeros sit on the Julia set of the commit map, a reason the prime bank's cancellation leaves the network passive, a reason every fluctuation wave writes on the radical tier, a reason ζ's leverage never falls below its gain/loss. `thesis §13` states them as questions an answer can come back to.

## 12. The Hilbert landmarks

`thesis §0` states the landscape and its forcing. This section reads each landmark against the hub's own vocabularies, so the atlas and the landscape are one map.

**The forcing, in the hub's terms.** The commit is the twisted square (§1, vocabulary 5); its exponent is capped at 2 by the cross-breed (§2); the channels are orthogonal characters on the Bohr torus. A square valuation over orthogonal channels is an inner-product norm, so the possibility space is a Hilbert space. Change the exponent and the line moves with it — Nyman–Beurling's family puts ζ's zero-free boundary at σ = 1/p for density in $L^p$ — so the ½ of the critical line is the reciprocal of the commit's exponent. **[LANDED]** pieces; the assembly is the hub's.

**The line in each vocabulary.**
- **Squaring (§1, vocabulary 7).** The norm-square sends σ to 2σ: $\|\zeta(\sigma+i\cdot)\|^2 = \zeta(2\sigma)$, and the critical line lands on ζ's pole. The commit map $g(s) = s^2/(2s-1)$ has its one puncture at the same place, $g(\tfrac12) = \infty$.
- **The Smith chart (§6).** On the line the reflection coefficient has $|\Gamma| = 1$: lossless reflection is an isometry, the circuit form of Plancherel.
- **Krein (§4).** On each orbit Weil's pairing has signature (2, 2). RH is that the global form is positive — that the Krein space is a Hilbert space. The landscape's edge and the Krein ghost are one statement: inside the Hilbert sector there is no negative direction to occupy.
- **Tiers (§7).** The commit exponent 2 and the RESEED slope ½ are reciprocal: the radical tier is the Hilbert line read on the opcode table.
- **The prime bank (§8).** Each comb's loop gain $p^{-1/2}$ squares to $1/p$; von Neumann's criterion for the bank's product vector, $\sum_p(1 - \sqrt{1-p^{-2\sigma}})$, is the sum of those prices at σ, and it diverges exactly at the line.

**The landmarks against `On_HilbertAndHisSpaces`.**

| That document | This landscape | Status |
|---|---|---|
| Rays, not arrows: length is gauge (§III) | On the line the norm diverges and Selberg's normalisation keeps only the ray's statistics | **[READING]** on **[LANDED]** |
| Stone–von Neumann uniqueness, Haag's inequivalence (§VI) | Inside: the Euler vector in the vacuum's sector; at the edge: an inequivalent sector of the infinite tensor product | **[LANDED]** criterion; seating **[READING]** |
| Superselection as the firewall between sectors (§III.a) | The sectors of the infinite tensor product, separated at σ = ½ | **[READING]** |
| Type I instance, Type III₁ horizon, thermal (§VII) | Bost–Connes: type I∞ for β > 1, unique type III₁ for β ≤ 1; the line over β = 2σ = 1 | Transition **[LANDED]**; seating **[READING]** |
| The Route Law as the Born square (§V) | H2: the commit that forces the Hilbert structure | **[LANDED]** in the corpus |

**What is not forced.** The Bost–Connes seating through β = 2σ is a reading of an identity, not a map between the two algebras. Selberg's normalisation as projectivisation is a reading: it divides a distribution by a growing scale, which is the projective move in spirit, not a quotient by ℂ*. And RH itself: the landscape is forced, and whether every zero sits on its edge is the open positivity (`thesis §13` Q5).

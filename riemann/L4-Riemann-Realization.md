# The Riemann Realization
## K₄ Hosting the Riemann Hypothesis Alongside the Prime Machinery

*A standalone model built from the K₄ engine; reads without the rest of the corpus. Three distinct objects meet here—the K₄ host, the prime-number machinery, and RH itself—so that what K₄ organizes, what the primes supply, and what RH asserts stay cleanly separated. Whether RH holds is a different object, reached for nowhere here.*

**Claim sorts used throughout.**
**[LANDED]** — a theorem in the literature, cited.
**[COMPUTED]** — checked numerically for this model; the precision and method are given.
**[READING]** — the K₄ hosting interpretation. An organizing lens: it decides nothing.
**[OPEN]** — a live question, stated so that an answer could come back.

---

## Quick Reference: Three Objects, Three Interfaces

```
             [ 1. K₄ Host (3D solid + t shaft) ]
                /                           \
     K₄ ↔ RH                                  K₄ ↔ Primes
   (V = 0 Mutable                           (ln p on log floor;
    circle dipole;                           H_coh readout ψ(x),
    unselected square)                       N = I²R; unsharpness)
              /                               \
   [ 2. RH: |w_ρ| = 1 ]  ◄── Primes ↔ RH ──►  [ 3. Prime Machinery ]
   (Zero-gain/zero-loss      (Selberg plug;       (∏(1-p⁻ˢ)⁻¹, Λ(k),
    balance, Λ = 0)           λ_n = S_∞ + S_0)     sieve & ψ(x))
```

### The Three Objects

| Element | What it is | Owns (in scope) | Does not own (out of scope) |
|---------|------------|-----------------|-----------------------------|
| **`K₄ Host`** | The dual-binary tetrahedron (`Fixed` conjugation $c$, `Mutable` circle reflection $cf$, `Cardinal` inversion $f$) lifted by $z = xy$, separating unselected `H_incoh` (`dt = 0`) from `H_coh` (`dt > 0`) under external drive $t = 2\pi I^2$. | Maps 2D line-membership into 3D volume collapse ($V = 0$ vs. $V > 0$), separates `ROUTE` symmetries from quadratic positivity, and locates finite-window unsharpness across all three bimedians. | Generates no primes, forces no positivity on $\zeta$, and cannot rule out $V > 0$ bulk quartets on its own. |
| **`Prime Machinery`** | The Euler product $\prod_p(1 - p^{-s})^{-1}$, incommensurate local prime places ($\ln p$ on the Bohr torus), von Mangoldt weights $\Lambda(k)$, and the explicit-formula / Bombieri–Lagarias dual ($\psi(x)$, $S_0$). | Runs prime generation and prime-side sums independently of $K_4$ and without assuming RH; supplies the four Selberg plug constraints (Euler product, single $s=1$ pole, Ramanujan $|a_p| \le 2$, $s \leftrightarrow 1-s$) and the prime half $S_0$ of $\lambda_n = S_\infty + S_0$. | Does not close the global balance exponent $-\tfrac12$ from finite prime computation alone. |
| **`RH`** *(isolated)* | The global zero-slack spectral balance condition on the completed Euler/Mellin transform: $|w_\rho| = 1$ for every nontrivial zero ($\Lambda = 0$, $\lambda_n \ge 0$). | Fixes exact non-amplification across the self-dual boundary (no exponential gain or loss), pinning $\psi(x) - x$ fluctuations at optimal $x^{1/2}$ scale. | Does not by itself force zero simplicity (even-multiplicity zeros on $|w|=1$ satisfy $|w|=1$ without changing $Z$'s sign), and is neither proved by $K_4$ hosting nor required for prime generation. |

### The Three Interfaces

| Interface | What crosses it | Register | Where its warrant stops |
|-----------|-----------------|----------|-------------------------|
| **`K₄ ↔ RH`** *(Hosting)* | $\operatorname{Re}\rho = \tfrac12 \iff \|w_\rho\| = 1 \iff$ `Mutable` circle-dipole collapse ($V = 0$); Li's $\sum 4\sin^2(n\varphi_\gamma/2) \iff$ unselected `H_incoh` square (`dt = 0`); De Bruijn–Newman $\Lambda = 0 \iff$ zero reactive slack. | **[READING]** on exact **[LANDED]** identities | Hosts RH cleanly; does not prove it. Detuned controls ($\zeta(s-\tfrac14)\zeta(s+\tfrac14)$) occupy $V > 0$ inside the exact same $K_4$ socket. |
| **`Primes ↔ RH`** *(The Live Seam)* | Fourier/Mellin duality ($\ln p \leftrightarrow \rho$) and Bombieri–Lagarias ($\lambda_n = S_\infty + S_0$); separates intact Selberg plugs from broken controls (`Davenport–Heilbronn`, $\zeta(s-\tfrac14)\zeta(s+\tfrac14)$). | **[LANDED]** equivalences; **[OPEN]** proof | **Sole locus of what remains open:** proving that the intact local-to-global prime plug forces $\lambda_n \ge 0$ ($\|w_\rho\| = 1$) globally. |
| **`K₄ ↔ Primes`** *(Register & Resolution)* | Upstream $\ln p$ frequencies on `K₄`'s log-floor (`H_incoh`); downstream $\psi(x)$ and $N(t) = I^2R$ (`I = √(t/2π)`, `R = ln(t/2πe)`) on `H_coh` under external shaft $t = 2\pi I^2$; three-bimedian finite-window unsharpness and Lehmer-pair truncation limits. | **[READING]** + **[COMPUTED]** | Bookkeeping and resolution bounds only. $P = I^2R$ carries no information about $S(t)$ or zero heights; finite $F_N$ truncation scrambles Lehmer pairs rather than tracking backward heat $H_\tau$. |

### Isolated Statement of What RH Being True Is All About

Strip away both the **$K_4$ host construction** and **downstream prime-counting applications** ($\psi(x)$ bounds, $\pi(x) - \operatorname{li}(x)$, finite $F_N$ truncations), and RH being true is one standalone claim:

> **When un-detuned local prime places ($\prod_p(1 - p^{-s})^{-1}$, $|a_p| \le 2$, single pole at $s = 1$) close against the Archimedean $\Gamma$-place, the global transform is strictly lossless and zero-slack: every mode sits on the unit circle ($|w_\rho| = 1$, zero exponential gain or decay, $\Lambda = 0$), because the prime-side oscillatory sum never breaks positivity against the Archimedean background ($\lambda_n \ge 0$ for all $n \ge 1$).**

---

## 1. The claim, in one breath

RH is usually carried as a statement about the location of points: every nontrivial zero of $\zeta$ has real part $\tfrac12$.

K₄ hosts that claim as a **balance**: a mode that neither gains nor loses. That reading has an exact mathematical incarnation, and it is the spine of the model. Send each zero through

$$w_\rho = 1 - \frac{1}{\rho} = \frac{\rho - 1}{\rho}.$$

Then $|w_\rho| = |\rho - 1|/|\rho|$, which equals $1$ exactly when $\rho$ is equidistant from $0$ and $1$ — that is, exactly when $\operatorname{Re}\rho = \tfrac12$. **[LANDED]** (elementary; it is the map under Li's criterion.)

So RH is the statement that **every zero becomes a pure rotor on the unit circle**: zero gain, zero loss. An off-line zero becomes a rotor that slowly grows or slowly decays — and its mirror partner does the opposite. "Balanced reflection" is not a figure of speech here. It is $|w| = 1$.

The sections that follow walk all three elements and their interfaces: the two views of $\zeta$ (content and hold), the multiplicative prime register, the four-point orbit lifted into a 3D tetrahedron, the orbit carried into the unit disc where the balance becomes a sum of squares, the first Lehmer pair as a finite-resolution test, the zero-margin theorem ($\Lambda = 0$) that Lehmer pairs witness, three-bimedian unsharpness on any finite readout, the counting balance ($P = I^2R$ and off-sheet shaft $t$), what decides occupancy on the intact Selberg plug (`λ_n = S_∞ + S_0 ≥ 0`), and the remaining open edges.

## 2. Two views of one object

ζ carries two readings of itself; the completion factor is the exchange rate between them. **[LANDED]** throughout this section.

**The content view** is ζ(σ+it) itself: the pole at s = 1, the Euler product, and the rotor $\chi(\tfrac12+it) = e^{-2i\vartheta(t)}$. On the critical line it winds as a helix, $\zeta(\tfrac12+it) = e^{-i\vartheta(t)}Z(t)$, with real amplitude Z(t) and turning rate $\vartheta'(t) \approx \tfrac12\ln(t/2\pi)$.

**The hold view** is the completed $\xi(s) = \tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$: entire, pole-free, symmetric under s ↔ 1−s, real on the line. Completion strips the rotor and swallows the pole; the helix becomes a standing real trace.

**[READING]** One substrate read from either side of its own crossing. The model works on the content side, where the primes act; the hold side is the time-even slice.

## 3. The register is multiplicative

**[LANDED]** $\zeta = \prod_p(1-p^{-s})^{-1}$, and $\ln\zeta = \sum_p\sum_k p^{-ks}/k$ is additive across the frequencies $\ln p$. The explicit formula turns that sum over prime frequencies into a sum over zeros: primes and zeros are a Fourier pair. §10 runs that pairing in both directions on the Li coefficients.

**[READING]** The engine's guard — *does it survive log()?* — seats the primes as frequencies, not locations: p lives at ln p, a note the medium rings at. The additive ledger ψ(x), jumping at each prime power, is the committed shadow of that spectrum, sampled in finite steps. Read as a list of events handed to the machine, ψ(x) inverts cause and effect. The spectrum is upstream; the ledger is what a finite readout compiles it to.

## 4. The figure: one zero unfolds

Write $s = \tfrac12 + x + iy$. ξ has three symmetries — conjugation **c** ($s \mapsto \bar s$), the functional equation **f** ($s \mapsto 1-s$), and line-reflection **cf** ($s \mapsto 1-\bar s$) — forming a Klein four-group. One zero's orbit is four points on a flat rectangle. **[LANDED]**

Stand it up. Ask each of the three moves to act as a rotation of space (determinant +1). That fixes the parity of a third coordinate — odd under c, odd under cf, even under f — and the unique lowest-degree monomial with that parity is

$$z = xy = \tfrac12\operatorname{Im}\big((s-\tfrac12)^2\big).$$

The lift is forced given two named choices: rotations, and minimal degree. **[LANDED]** as algebra; the two choices are the model's. The rectangle becomes a tetrahedron, and the signs of (x, y, xy) match the dual-binary pole coordinates (taking x, y > 0 for ρ):

- **P = ρ** (+, +, +) — direct upper strip
- **U = ρ̄** (+, −, −) — direct lower strip
- **I = 1 − ρ̄** (−, +, −) — reflected upper strip
- **R = 1 − ρ** (−, −, +) — reflected lower strip

Each symmetry holds one bimedian: **c** is **Fixed** ({P–U, I–R}, preserves the sign of x); **cf** is **Mutable** ({P–I, U–R}, preserves the sign of y); **f** is **Cardinal** ({P–R, U–I}, preserves z = xy). The centroid is s = ½.

**Occupancy is volume.** The orbit has an interior exactly off the cone xy = 0. On the critical line (x = 0) P merges with I and U with R: the tetrahedron collapses to a **Mutable dipole**, two points, zero volume. RH says every orbit is a dipole. **[READING]**, exact as geometry.

**[READING]** The three schools are the three bimedians: conjugation is the arithmetic school (Euler product, real axis), line-reflection the spectral school (operators, statistics), the functional equation the duality school (Poisson, the proved function-field cases). One object, three viewing axes, any two generating the third.

## 5. The orbit in the disc: the balance becomes a square

Carry the whole orbit through $w = 1 - 1/s$. **[LANDED]**, and **[COMPUTED]** to 20 digits on a test point:

| Pole | Point | Image |
|---|---|---|
| P | ρ | w |
| U | ρ̄ | w̄ |
| R | 1 − ρ | 1/w |
| I | 1 − ρ̄ | 1/w̄ |

The Klein group becomes the symmetry group of the unit circle: **c** is conjugation (Fixed), **f** is inversion $w \mapsto 1/w$ (Cardinal), and **cf** is reflection in the circle, $w \mapsto 1/\bar w$ (Mutable).

The §4 collapse is literal. A zero is on the line ⟺ P = I ⟺ $w = 1/\bar w$ ⟺ $|w| = 1$. **The Mutable bimedian is reflection in the unit circle, and RH says every orbit is pinned to its mirror.** Off the line, the mirror partners have exactly reciprocal moduli, $|w_\rho|\cdot|w_{1-\bar\rho}| = 1$: one gains precisely what the other loses. **[COMPUTED]** for ρ = 0.5765 + 7005.084i: 0.99999999844 and 1.00000000156.

**Li's criterion** reads the balance off as a positivity. Define $\lambda_n = \sum_\rho\big(1 - w_\rho^{\,n}\big)$ (zeros paired with their conjugates). RH ⟺ $\lambda_n \ge 0$ for all n ≥ 1 (Li 1997; Bombieri–Lagarias 1999). **[LANDED]**

The easy direction shows what the square is. On the line, $w = e^{i\varphi}$, and each conjugate pair contributes

$$(1 - e^{in\varphi}) + (1 - e^{-in\varphi}) = 2 - 2\cos n\varphi = 4\sin^2\!\frac{n\varphi}{2}.$$

Under RH, $\lambda_n = \sum_{\gamma > 0} 4\sin^2(n\varphi_\gamma/2)$: **literally a sum of squares.** This is the engine's unselected square — no branch chosen, nothing discarded, every term non-negative by form. Off the line the term becomes $2 - 2|w|^n\cos n\varphi$, and the gaining partner's $|w|^n$ eventually drives it negative. The hard direction (Bombieri–Lagarias) shows that this must happen.

**How long a tape it takes to see a leak.** For a zero at height γ and offset δ, $|w| - 1 \approx \delta/\gamma^2$, so the leak shows in $\lambda_n$ only for $n \gtrsim \gamma^2/\delta$. **[COMPUTED]** heuristic: an offset δ = 0.076 at γ = 7005 needs n ≈ 6×10⁸. Positivity criteria are exact and slow, and the slowness grows with height — the same unsharpness §8 finds in every finite window.

## 6. The first Lehmer pair: a resolution test

**The pair.** **[COMPUTED]**

- Zeros at γ = 7005.062866 and γ = 7005.100565 (Lehmer, 1956).
- Gap 0.0377, which is **0.042 of the mean spacing** $2\pi/\ln(t/2\pi) = 0.895$ at this height.
- Between them Z(t) peaks at **+0.003967**, at t = 7005.08186.

**The truncated model.** The Riemann–Siegel main sum truncates at $N = \lfloor\sqrt{t/2\pi}\rfloor = 33$:

$$Z(t) = 2\operatorname{Re}W_N(t) + (-1)^{N-1}\Big(\frac{t}{2\pi}\Big)^{-1/4}\frac{\cos\big(2\pi(p^2-p-\tfrac1{16})\big)}{\cos 2\pi p} + O(t^{-3/4}),$$

with $W_N(t) = e^{i\vartheta(t)}\sum_{n\le N}n^{-1/2-it}$ and $p = \sqrt{t/2\pi} - N$. **[LANDED]** (Riemann–Siegel.) At the peak **[COMPUTED]**:

| Quantity                            | Value     |
|-------------------------------------|-----------|
| p                                   | 0.390020  |
| Main sum $2\operatorname{Re}W_{33}$ | −0.06600  |
| Leading correction $C_0$            | +0.06994  |
| Main + $C_0$                        | +0.003937 |
| True Z                              | +0.003967 |

The main sum alone has the wrong sign. Its approximate-functional-equation partner $F_{33}(s) = S_{33}(s) + \chi(s)S_{33}(1-s)$ therefore has no sign change on the line between the two zeros, and carries a conjugate pair **off** the line instead, at $s = 0.5764841256 + 7005.0841410\,i$ and its mirror ($|F_{33}| \approx 5\times10^{-28}$). **[COMPUTED]**

**What that off-line pair is.** A zero of the *approximant*, not of ζ. Changing the truncation length shows it. **[COMPUTED]**

| N  | $Z_N$ at the peak | Approximant keeps the pair on the line? |
|----|-------------------|-----------------------------------------|
| 30 | +0.0427           | yes                                     |
| 32 | +0.2277           | yes                                     |
| 33 | −0.0660           | no — off-line pair at x = +0.0765       |
| 34 | −0.1869           | no — x = +0.1276                        |
| 36 | −0.1399           | no — x = +0.1108                        |
| 40 | +0.1354           | yes                                     |

The verdict flips with N. The true peak is **17.6 times smaller** than the first correction term, so any finite model with error of order $t^{-1/4} \approx 0.17$ decides this pair's sign by its error, not by the signal. Two zeros 0.042 mean-spacings apart sit below the resolution of a 33-term window (§8); the window merges them, and a merged pair of a real-symmetric function leaves the line as a conjugate pair. **The off-line zero of $F_{33}$ is the unsharpness bound made visible.**

**The restoring identity** for the approximant is exact. With $g_N(x,t) = \ln\big|\chi(\tfrac12+x+it)\,S_N(\tfrac12-x-it)/S_N(\tfrac12+x+it)\big|$:

$$\partial_x g_N\big|_{x=0} = -2\vartheta'(t) - 2\operatorname{Re}\frac{S_N'}{S_N}(\tfrac12+it) = -2\,\frac{d}{dt}\arg W_N(t).$$

**[LANDED]** (Cauchy–Riemann bookkeeping.) While $\arg W_N$ advances, the gradient restores the approximant's zeros to x = 0. Where $|S_N|$ dips and $\arg W_N$ runs backward, the restoring force reverses and the approximant's zeros can leave. The identity governs $F_N$; it reaches ζ only once the remainder is controlled, and at a Lehmer pair the remainder is the whole story.

## 7. Zero margin

**The flow.** De Bruijn and Newman deform Ξ by a heat flow, $H_\tau(z) = \int_0^\infty e^{\tau u^2}\Phi(u)\cos(zu)\,du$, with $H_0$ = Ξ up to scaling and z = 2t. There is a constant Λ such that $H_\tau$ has only real zeros exactly when τ ≥ Λ. RH ⟺ Λ ≤ 0. **[LANDED]**

**The local model.** Near a collision, a zero pair behaves like the roots of $(z - z_0)^2 + \delta^2 - 2\tau$. For τ < δ²/2 the pair is off-line (**hold**: the orbit has volume). At τ = δ²/2 it is a double zero (**collapse**: volume zero). For τ > δ²/2 it is two real zeros moving apart (**reseed**). **[LANDED]** Run forward, the flow repels zeros along the line; run backward, it pushes close pairs together until they leave. A pair on the line with gap g (measured in t) has half-gap δ = g in z, so backward heat collides it at τ* = g²/2 (in t-units, g²/8). **[COMPUTED]** to within 10% across 387 close pairs from t = 100 to 10¹² (§13).

**The theorem.** Rodgers and Tao proved Λ ≥ 0 (2020), confirming Newman's conjecture: if RH holds, it holds only just. The best upper bound is Λ ≤ 0.2 (Platt–Trudgian 2021). Under RH, **Λ = 0 exactly.** **[LANDED]**

**The witnesses.** Lower bounds on Λ before Rodgers–Tao came from locating Lehmer pairs of increasing quality (Csordas–Smith–Varga and successors): a pair that close survives only if almost no backward heat is available. **[LANDED]** **Lehmer pairs are where ζ has no slack, and Λ = 0 is the statement that this slack is zero.** **[READING]**, resting on Λ = 0 under RH.

Backward heat and truncation (§6) both act on close pairs. Heat reads the gap. Truncation reads a sign gated by a size, and as height grows its verdict falls into heat's order. **[COMPUTED]** (§13.)

**[READING]** In the model's terms, RH is an edge-mode held at exact resonance with zero reactive margin. Λ = 0 makes the margin zero as a theorem (given RH). Lehmer pairs are the near-touches that show it.

## 8. Unsharpness: what any finite readout cannot see

Picture a live room and a tuner sweeping upward in height t, stamping zero-crossings onto paper tape of finite log-length L = ln X. **[READING]** for the picture; the three bounds below are standard, stated as heuristics.

- **Across Fixed (vertical, in t): Fourier unsharpness.** Under τ = ln x, the Mellin transform makes ln X and t Fourier conjugates, so $\Delta(\ln X)\cdot\Delta t \gtrsim 1$. At the Riemann–Siegel window $L = \ln N \approx \tfrac12\ln t$, vertical resolution is $\Delta t \sim 2\pi/\ln t$ — the mean zero spacing itself. A Lehmer pair at 0.042 of that spacing is invisible to the window (§6).
- **Across Mutable (horizontal, in x): scale unsharpness.** Separating $X^{\frac12+x}$ from $X^{\frac12}$ needs $|x|\ln X \gtrsim 1$; offsets $|x| \lesssim 2/\ln t$ cannot be separated by the finite sum's amplitude alone. The disc version (§5) is slower still: n ≳ γ²/δ.
- **Across Cardinal (the lift z = xy): coupled unsharpness.** An unresolved width Δx at height t leaves a lift spread Δz ≈ tΔx. Cauchy–Riemann, $\partial_x\ln|\zeta| = \partial_y\arg\zeta$, ties any sharpening in x to phase twist in y: the Mutable and Fixed bounds are coupled.

**[READING]** Heisenberg is the Fixed instance of a finite-window unsharpness that runs across all three bimedians. §5 and §6 are two faces of it: a slow positivity test and a merged pair.

## 9. The counting balance

Riemann–von Mangoldt: $N(t) = \frac{t}{2\pi}\ln\frac{t}{2\pi e} + \frac78 + S(t) + O(1/t)$. **[LANDED]**

Seat the poles:

- **I** $= \sqrt{t/2\pi}$ — the Riemann–Siegel aperture, the number of modes in phase at once;
- **R** $= \ln\frac{t}{2\pi e} = 2\vartheta'(t) - 1 + O(t^{-2})$ — the log-height, per mode;
- **P** $= N(t)$ — the zeros stamped up to height t.

The main term of Riemann–von Mangoldt is **exactly** $P = I^2R$, with **U** $= P/I = IR = \sqrt{t/2\pi}\,\ln\frac{t}{2\pi e}$. **[COMPUTED]**: at t = 7005, $I^2R + \tfrac78 = 6708.56$, against the true count of 6708 zeros.

**With P and I seated, the count forces R.** The turning rate ϑ′ is π times the zero density $N'(t) = \frac{1}{2\pi}\ln\frac{t}{2\pi}$; seated at ϑ′, R gives $P \approx 2I^2R$ and the relation fails. The engine's relations reject a wrong seating here — a real null, returned by arithmetic.

The balance carries no information about where the zeros are; all of that sits in S(t). **[READING]** for the seating.

**The shaft.** The height itself is $t = 2\pi I^2$. Every stamped number tracks it, and none books it: $IR \sim t^{1/2}\ln t$, never t. **[READING]** t is source infrastructure, driving the sweep from outside the four-pole sheet.

## 10. Symmetry is free; positivity decides

**[READING]** In the engine, a ROUTE moves value at unit slope and decides nothing; a square is where decisions live. The whole apparatus of §4 — group, lift, centroid — is route: forced, dimensionless, and silent on occupancy.

That symmetry cannot decide occupancy is a measurement **[LANDED]**: functions with ξ's symmetries fill the bulk with zeros, and each breaks a specific part of the plug.

- **Davenport–Heilbronn** has a functional equation of the right shape and zeros off the line — and no Euler product. The Fixed bimedian carries no prime floor.
- **ζ(s − ¼)ζ(s + ¼)** keeps s ↔ 1−s and a degree-2 Euler product, $\prod_p\big(1 - (p^{1/4}+p^{-1/4})p^{-s} + p^{-2s}\big)^{-1}$. It breaks the plug twice: a pole inside the strip at s = ¾, and coefficients $a_p = p^{1/4}+p^{-1/4} > 2$ that violate the Ramanujan bound. Its zeros sit on σ = ¼ and σ = ¾ — two detuned resonators, parked off-line from the start.

Each known bulk-occupied example breaks at least one of four conditions: Euler product, no poles inside the strip, Ramanujan-bounded coefficients, and s ↔ 1−s symmetry. These are the Selberg-class axioms. **[LANDED]**

What decides occupancy on an intact plug is **positivity**: the Weil explicit-formula positivity, of which Li's $\lambda_n \ge 0$ is the coefficient form (§5). **[LANDED]** as equivalences. A routing argument cannot supply a square. A proof, if it comes, forces positivity out of the plug.

### The prime side: who carries the positivity

Each Li coefficient splits into an archimedean part and a prime part, $\lambda_n = S_\infty(n) + S_0(n)$ (Bombieri–Lagarias 1999, the arithmetic formula). **[LANDED]**

$$S_\infty(n) = 1 - \tfrac n2(\gamma + \ln 4\pi) + \sum_{j=2}^{n}(-1)^j\binom nj\big(1-2^{-j}\big)\zeta(j),\qquad S_0(n) = -\sum_{j=1}^{n}\binom nj\,\eta_{j-1},$$

where $-\frac{\zeta'}{\zeta}(s) = \frac{1}{s-1} + \sum_{j\ge0}\eta_j(s-1)^j$, and each $\eta_j$ is a sum over prime powers:

$$\eta_j = \frac{(-1)^j}{j!}\lim_{X\to\infty}\Big(\sum_{k\le X}\frac{\Lambda(k)(\ln k)^j}{k} - \frac{(\ln X)^{j+1}}{j+1}\Big).$$

Folded together, $S_0(n) = -\lim_X\big(\sum_{k\le X}\frac{\Lambda(k)}{k}L^{(1)}_{n-1}(\ln k) - (1 - L_n(\ln X))\big)$: the primes enter through generalized Laguerre polynomials of ln k.

**[READING]** These are §2's two views as the two halves of the positivity. $S_\infty$ comes from the completion factor $\pi^{-s/2}\Gamma(s/2)$ — the hold side, the infinite place. $S_0$ comes from the Euler product — the content side, the primes.

**Three routes, one number.** **[COMPUTED]**
- From the zeros: $\sum 4\sin^2(n\varphi_\gamma/2)$ over all 1 747 146 zeros below 10⁶, plus a smooth tail.
- From the formula, with $\eta_j$ built from Stieltjes constants at 80 digits.
- From the Taylor coefficients of $\log\xi(1/(1-z))$ directly, for n ≤ 12.

Zeros and formula agree to six decimals for every n ≤ 60; formula and Taylor to fifteen digits for n ≤ 12 ($\lambda_1 = 0.0230957089661$). The zero list carries every zero below 10⁶ — 1 747 146, matching the θ-count — each bisected to 10⁻⁹. Moving the zero cutoff from 2.5×10⁵ to 10⁶ moves λ₂₀₀₀₀ by 0.002.

| n     | $S_\infty(n)$ | $S_0(n)$ | $\lambda_n$ |
|-------|---------------|----------|-------------|
| 1     | −0.5541       | +0.5772  | 0.0231      |
| 2     | −0.8745       | +0.9669  | 0.0923      |
| 4     | −1.0068       | +1.3756  | 0.3688      |
| 7     | −0.3557       | +1.4802  | 1.1245      |
| 8     | +0.0209       | +1.4449  | 1.4658      |
| 12    | +2.0919       | +1.1714  | 3.2633      |
| 30    | +17.857       | +0.697   | 18.554      |
| 60    | +55.760       | +1.373   | 57.133      |
| 100   | +117.975      | +0.629   | 118.604     |
| 300   | +517.218      | +2.484   | 519.702     |
| 1000  | +2324.30      | +1.76    | 2326.05     |
| 2000  | +5340.99      | +10.77   | 5351.76     |
| 5000  | +15642.08     | −2.99    | 15639.09    |
| 10000 | +34749.14     | −12.56   | 34736.58    |
| 20000 | +76429.01     | +8.97    | 76437.98    |

Three results.

1. **For n ≤ 7 the primes carry the positivity alone.** The archimedean part is negative there and pulls $\lambda_n$ below zero; $S_0$ lifts it back. $S_\infty$ changes sign between n = 7 (−0.356) and n = 8 (+0.021). **[COMPUTED]**
2. **From n = 8 on, the Γ-growth carries it, and the primes ride on top.** $S_\infty$ follows $\tfrac n2\ln n + \tfrac{\gamma-1-\ln 2\pi}{2}n$ (5340.3 predicted at n = 2000, 5341.0 computed), while $S_0$ oscillates about zero. Computed at every n ≤ 1000 and every fourth n up to 20 000, it ranges over [−20.9, +23.2], first turns negative at n = 156, and changes sign at least 176 times. Its envelope grows like $n^{0.53}$ (max $|S_0|/\sqrt n \approx 0.16$ at n = 20 000): about 23 against the 1 401 that $O(\sqrt n\ln n)$ allows there, and against $S_\infty = 76\,429$. Under RH, $\lambda_n = \tfrac n2\ln n + \tfrac{\gamma-1-\ln 2\pi}{2}n + O(\sqrt n\ln n)$ (Bombieri–Lagarias) **[LANDED]**, so all the oscillation lives in $S_0$. RH is the statement that the prime part never falls below $-S_\infty(n)$. An off-line zero would make it grow eventually like $|w|^n$ (§5) and overwhelm the Γ-growth.
3. **The primes measure the balance point.** After its main term is removed, each prime sum's error decays as $X^{\max\operatorname{Re}\rho - 1}$ (explicit formula). From the primes **[COMPUTED]** — up to 10¹⁰ (455 million primes, segmented sieve) for the first and last rows, up to 10⁸ for the middle two:

   | Prime sum                           | Limit                                       | Error at the end of the range | Envelope               |
   |-------------------------------------|---------------------------------------------|-------------------------------|------------------------|
   | $\eta_0$                            | −γ                                          | 4.3×10⁻⁶ at 10¹⁰              | $X^{-0.497}$, 10³–10¹⁰ |
   | $\eta_1$                            | +0.187546                                   | 3.4×10⁻⁴ at 10⁸               | $X^{-0.495}\ln X$      |
   | $\eta_2$                            | −0.051689                                   | 3.1×10⁻³ at 10⁸               | $X^{-0.495}(\ln X)^2$  |
   | $\sum\Lambda(k)k^{-3/4} - 4X^{1/4}$ | $-\frac{\zeta'}{\zeta}(\tfrac34) = -4.6276$ | 1.3×10⁻³ at 10¹⁰              | $X^{-0.249}$, 10³–10¹⁰ |

   Scaled by their exponents, the two long-range envelopes peak at the same constant over the last decade: $|E_0|\,X^{1/2} \le 0.64$ and $|E_{\text{sh}}|\,X^{1/4} \le 0.64$. The same zeros drive both sums; the plug moves only the exponent.

   The last row is the shifted plug $\zeta(s-\tfrac14)\zeta(s+\tfrac14)$ of this section. Its prime weights are ζ's reweighted by $k^{\pm1/4}$, and that reweighting *is* the Ramanujan violation $a_p = p^{1/4}+p^{-1/4}$. From the primes alone it moves the balance point from ½ to ¾. ζ's exponent ½ is von Koch's form of RH, $\psi(x) = x + O(x^{1/2+\varepsilon})$ (von Koch 1901) **[LANDED]**; the measurement is consistent with it up to 10¹⁰, and reaches no further.

**Prime-side unsharpness.** **[COMPUTED]** At X = 10⁸ the Laguerre sum reproduces $S_0(n)$ to 2×10⁻⁵ at n = 1, 3×10⁻⁴ at n = 2, and to 1–2% for n = 4 to 12: the range of n the primes can read grows like ln X. An off-line zero at height γ with offset δ enters the prime sums as $X^{\delta-1/2}/|\rho|$, and rises above the on-line background only once $X^\delta \gtrsim \gamma$ — for γ = 10⁴ and δ = 0.01, X ≈ 10⁴⁰⁰ (heuristic). **[READING]** The primes are blind to high off-line zeros exactly as $\lambda_n$ is (n ≳ γ²/δ, §5): the §8 unsharpness, seen now from the content side.

RH is $S_0(n) \ge -S_\infty(n)$ for every n, and it is the exponent ½ for every X. Both halves compute cleanly on any finite range, and the unsharpness on each side is exactly where computation stops and proof has to begin.

## 11. The handoff: socket and plug

**[READING]** The engine is an abstract base class. It emits forced, dimensionless structure — the poles, the relations, the tiers — and no rate, clock, or bit-price. Its one typed hole is the dispatch rule of its self-feeding loop, driven from outside by the shaft t.

What plugs into that hole is an upstream multiplicative spectrum, pinned by the four Selberg conditions of §10. The engine supplies the plumbing: route (the phase $x^{it}$), square (§5's sum of sines squared), reseed (the sign-crossing of the real Z), advance (the shaft). The plug supplies the texture — which frequencies ring. RH says that texture holds every orbit on the circle.

**The framework does not manufacture the primes.** It supplies the form of the handoff, which is forced and free, and localises everything un-derived about RH to one named hole: positivity on the intact plug.

## 12. Scope

**[LANDED]** here is classical: the symmetries, Riemann–Siegel, the Li map and criterion, the heat flow and Λ = 0 under RH, the Selberg-class counterexamples. **[COMPUTED]** is checked to the digits shown. **[READING]** is the K₄ seating, which earns its place where it is literal:

- the Mutable collapse of §4 *is* reflection in the unit circle (§5);
- the unselected square *is* $4\sin^2(n\varphi/2)$;
- zero margin *is* Λ = 0;
- the count *forces* the seating of R (§9);
- the hold and content views of §2 *are* the archimedean and prime halves of $\lambda_n$, and the primes alone carry its positivity for n ≤ 7 (§10).

What decides RH is positivity on the intact plug (§10). The model names that hole and leaves it open.

## 13. Edges

### Settled by computation

- **Truncation reads a sign gated by a size; heat reads the size.** **[COMPUTED]** At no height are the two one operation; with height, their rankings converge.

  *Test set:* every pair of consecutive zeros below t = 40 000 with gap under 0.15 mean spacings — **126 pairs**. Zeros were located by a Riemann–Siegel sum carrying both corrections $C_0, C_1$, error ≤ 10⁻⁶ against mpmath. The count, 49 395 sign changes, matches Riemann–von Mangoldt (49 394.7). The five best pairs were re-located in mpmath and agree to six digits.

  *Heat:* first-order collision time $\tau^* = -4\,Z/Z''$ at the peak, in de Bruijn–Newman units. It matches §7's gap²/2 at ratio 0.983–0.9997 across all 126. **Backward heat ranks pairs by absolute gap alone.**

  *Truncation:* a pair is lost at its natural cutoff $N = \lfloor\sqrt{t/2\pi}\rfloor$ when the main sum $2\operatorname{Re}W_N$ has fewer than two sign changes between the midpoints to its neighbours.

  The twelve best pairs:

  | $t_1$      | gap/mean | $Z_{\text{peak}}$ | τ*       | N  | $C_0$ at peak | at natural N |
  |------------|----------|-------------------|----------|----|---------------|--------------|
  | 36510.1664 | 0.0407   | +0.00380          | 0.000436 | 76 | -0.0599       | kept         |
  | 7005.0629  | 0.0421   | +0.00397          | 0.000710 | 33 | +0.0699       | lost         |
  | 17143.7865 | 0.0445   | +0.00215          | 0.000623 | 52 | -0.0713       | kept         |
  | 5229.1986  | 0.0463   | +0.00486          | 0.000935 | 28 | -0.1163       | kept         |
  | 33179.3653 | 0.0495   | +0.00361          | 0.000658 | 72 | -0.0509       | kept         |
  | 22016.0079 | 0.0577   | +0.00401          | 0.000987 | 59 | +0.0733       | lost         |
  | 24182.1031 | 0.0593   | +0.00715          | 0.001016 | 62 | -0.1062       | kept         |
  | 21324.9440 | 0.0668   | +0.00410          | 0.001331 | 58 | -0.0645       | kept         |
  | 17366.5172 | 0.0764   | -0.00916          | 0.001833 | 52 | -0.0541       | lost         |
  | 23153.5150 | 0.0775   | +0.01014          | 0.001753 | 60 | -0.0589       | kept         |
  | 25704.5248 | 0.0827   | +0.00975          | 0.001948 | 63 | +0.1043       | lost         |
  | 15471.5508 | 0.0843   | +0.01944          | 0.002296 | 49 | +0.0581       | lost         |

  The tightest pair below 40 000 is at t = 36510.166, gap 0.0407 mean spacings.

  Below 40 000:
  1. **Heat order carries no information about truncation loss.** 74 of 126 pairs are lost at their natural N. Ranked by heat time, a lost pair outranks a kept one with probability 0.465 — chance (by gap/mean 0.464; by peak height 0.507). Inversions (2059) outnumber concordant orderings (1789), and no heat threshold classifies better than "all lost".
  2. **The rule.** A pair is lost exactly when the leading correction $C_0$ has the same sign as $Z_{\text{peak}}$ *and* is larger. Here $|Z_{\text{peak}}| \ll |C_0|$ (median ratio 0.32), so the size condition is almost always met and the verdict reduces to $\operatorname{sign}(C_0)\cdot\operatorname{sign}(Z_{\text{peak}})$ — a coin set by the parity of N and the phase p, blind to the gap. The rule follows from the Riemann–Siegel formula; what the computation adds is that $C_1$ and higher terms never overturn it.

  *Across height.* Windows of consecutive zeros at 10⁶, 10⁸, 10¹⁰ and 10¹², on an evaluator with exact phase reduction (error ≤ 2×10⁻⁶ against mpmath at 10¹²). Each window's zero count matches its θ-count. Pairs with gap under 0.35 mean spacings were measured; the close-pair columns use gap < 0.15.

  | Height  | Zeros  | Close pairs | Lost at natural N | Rule holds | Median $\lvert Z_{\text{peak}}\rvert/\lvert C_0\rvert$ | Median $\lvert C_0\rvert$ | Heat order predicts loss | τ*/(gap²/2) |
  |---------|--------|-------------|-------------------|------------|--------------------------------------------------------|---------------------------|--------------------------|-------------|
  | < 4×10⁴ | 49 395 | 126         | 74                | 126/126    | 0.32                                                   | 7.2×10⁻²                  | 0.47                     | 0.98–1.00   |
  | 10⁶     | 20 008 | 53          | 21                | 770/770    | 0.66                                                   | 2.5×10⁻²                  | 0.68                     | 0.94–1.00   |
  | 10⁸     | 39 999 | 132         | 9                 | 1628/1628  | 2.5                                                    | 6.2×10⁻³                  | 0.89                     | 0.90–1.00   |
  | 10¹⁰    | 14 999 | 56          | 4                 | 651/651    | 5.8                                                    | 2.6×10⁻³                  | 0.94                     | 0.94–1.03   |
  | 10¹²    | 6 000  | 20          | 0                 | 283/283    | 28                                                     | 7.5×10⁻⁴                  | —                        | 0.94–1.01   |

  ("Rule holds" counts every pair with gap < 0.35 in the window; "heat order predicts loss" is the probability that a lost close pair outranks a kept one by heat time, 0.5 being chance.)

  3. **The rule is exact at every height: 3 458 of 3 458 pairs.**
  4. **The gate closes with height.** $|C_0|$ falls as $t^{-1/4}$ while close-pair peaks do not, so the size condition admits fewer pairs. Where it is met, loss stays a coin (0.59, 0.53, 0.50 of the admitted pairs at < 4×10⁴, 10⁶, 10⁸). Where it fails, the pair is kept whatever the sign. So truncation loses only the tightest pairs, and its loss order becomes gap-ordered: heat order predicts it at 0.68, then 0.89, then 0.94. At 10¹² the main sum keeps every pair in the window, gap < 0.05 included.
  5. **Two readouts that converge in what they rank.** Heat reads a magnitude, the gap. Truncation reads a sign gated by a magnitude. At low height the sign dominates and the two are orthogonal; with height the magnitude takes over and truncation's verdict falls into heat's order. The coin persists wherever the gate is open, so they are never one operation. **[READING]**: a phase readout and an amplitude readout on one object, whose relative weight is set by the height.

- **A pair on the line is invisible in $\lambda_n$.** **[COMPUTED]** On $|w| = 1$, $\varphi_\gamma = 2\arctan(1/2\gamma)$. The first Lehmer pair sits at angular separation $\Delta\varphi = 7.68\times10^{-10}$ and stays phase-coherent up to $n \approx 1.30\times10^{9}$; the second at $1.20\times10^{-10}$, coherent to $n \approx 8.32\times10^{9}$. Whatever its quality, a pair on the line contributes $4\sin^2(n\varphi_1/2) + 4\sin^2(n\varphi_2/2) \in [0, 8]$. At those n, under RH, $\lambda_n \approx \tfrac n2\ln n + \tfrac{\gamma_E - 1 - \ln 2\pi}{2}\,n$ is about $1.22\times10^{10}$ and $8.57\times10^{10}$ **[LANDED]** asymptotic, with fluctuations of order $\sqrt n\ln n \approx 7.6\times10^{5}$ and $2.1\times10^{6}$. The coefficients see a pair only after it leaves the circle, and then only for $n \gtrsim \gamma^2/\delta$ (§5). The bridge from resolution to positivity runs through Λ (§7).

### Open

- **Where the gate shuts.** **[OPEN]** At 10¹² the natural-N main sum loses no pair in 6 000 zeros. Whether truncation losses die out entirely, or persist at a rate set by how the best pairs' peaks scale against $t^{-1/4}$, is untested beyond 10¹². The test is the same table, further up.
- **The dispatch rule.** **[OPEN]** The loop's crossings fire on a phase threshold — accumulated phase closing to multiples of π, $N(T) = \vartheta(T)/\pi + 1 + S(T)$ — with S(T) carrying every departure. Turn-driven versus load-driven spacing is the flip-fact. Lehmer pairs are where S(T) works hardest; whether that is structural or incidental is the question.
- **The figure and the atom.** **[OPEN]** The zero's orbit-tetrahedron and the plenum's impedance atom share V₄, centroid, and tiering by inheritance. Identity promotes only if the ζ transfer field shows the atom's three impedance modes — the storage split the hold and content views already resemble.

The model runs; these are where it keeps going.


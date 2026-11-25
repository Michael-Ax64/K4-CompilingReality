# Audit of the Riemann Realization: Bet 1 Decided, and What the Text Relies On

*External check, 25 Nov 2026. It is written in plain mathematical language on purpose: it uses none of the engine vocabulary, so it can be read and rerun without the corpus. Part 1 is computed, and its headline result is certified in interval arithmetic. Parts 2–4 classify every claim the Realization leans on. Part 5 lists the discrepancies found in the text.*

---

## 1. Computed results

### 1.1 Bet 1 (Davenport–Heilbronn): first negative Li coefficient at **n = 328,997** — certified

**The result is proved with computer assistance.** Every number in the table below is an interval-arithmetic enclosure (Arb, 128-bit balls), not a floating-point estimate.

| | certified enclosure |
|---|---|
| λₙ for every 1 ≤ n ≤ 328,996 | **> 0** (78 interval-in-n enclosures; smallest lower bound λ₁ ≥ 0.0944) |
| λ₃₂₈,₉₉₆ | [1381.6, 1389.0] |
| **λ₃₂₈,₉₉₇** | **[−2383.7, −2376.2]** (first negative) |
| previous trough λ₃₂₈,₄₇₂ | [14781.6, 14786.2] |

**Certified census of DH zeros with 0 < γ < T₀ = 1996.1708:**
- 1,856 zeros on the line, each enclosed in a bracket of width 2×10⁻⁹ by a certified sign change of the real function Λ(½+it).
- 84 off-line zeros with β > ½, each isolated by interval Newton in a box of radius 10⁻⁹. Their partners at 1−ρ̄ follow from the functional equation.
- The argument principle gives N(T₀) = 2024.000000 ± 3×10⁻¹¹ = 1856 + 2×84, so the census is complete.
- Certified side facts:
  - |f − 1| ≤ 0.0025 for Re s ≥ 7, so every zero satisfies −0.73 < β < 1.73.
  - f(σ) > 0 on [½, 7], so Λ has no real zeros.
- Lowest off-line zero: **0.808517182457 + 85.6993484854 i**, as the bet assumed. None lies below it.
- Off-line zero closest to the line: 0.51592 + 520.944 i.

**Method (exact formula, every term enclosed).** Write w = 1 − 1/ρ and gₙ(s) = 1 − (1 − 1/s)ⁿ. Then

$$\lambda_n = 2\,\mathrm{Re}\!\!\sum_{0<\gamma<T_0}\!\!(1 - w_\rho^n) \;+\; 2\,\mathrm{Re}\,B_n \;+\; I_n \;+\; D_n .$$

These four terms come from the residue theorem on {−6 < σ < 7, t > T₀}, with the left edge folded onto the right by Λ(s) = Λ(1−s):

- **The finite sum** runs over the certified zero balls.
- **Bₙ** = (1/2πi)∫ gₙ(x+iT₀)·Λ′/Λ(x+iT₀) dx over x ∈ [−6, 7]. It is computed by Taylor models: 130 panels, exact order-34 series at each panel centre, and Cauchy-estimate remainders.
- **Iₙ** = (1/π)∫_{T₀}^∞ Re[gₙ(7+it)ℓ(t) + gₙ(−6+it)ℓ̄(t)] dt, with ℓ(t) = ½log(5/π) + ½ψ((8+it)/2). It is computed by Arb's certified integration up to t = 10¹⁷, plus an explicit bound beyond that.
- **Dₙ**, the same integral with the Dirichlet series f′/f(7+it) in place of ℓ, is bounded by integration by parts: |Dₙ| ≤ 0.37.

Positivity below the crossing uses ball arithmetic in n itself: one evaluation encloses λ_ν for every real ν in an interval. Adaptive bisection then needs 155 evaluations to cover 1 ≤ n ≤ 328,996.

**Cross-checks.**
- At n = 1 the certified pieces sum to 0.0976361468. An independent 256-point Taylor computation of log Λ(1/(1−z)) gives 0.0976361468095.
- The floating-point run of the same day agrees at every anchor: λ₃₂₈,₉₉₆ = 1385.8, λ₃₂₈,₉₉₇ = −2379.5 and λ₃₂₈,₄₇₂ = 14784.2. That run used a zero census to T = 2000 plus a smooth-density tail. Its coefficients for n ≤ 4×10⁵ moved by ≤ 1.84 under a change of cutoff, and they agreed with the Taylor values to 10⁻⁵ for n ≤ 12.
- Two independent recomputations, floating point, by other instances:
  - A census to γ ≤ 1200 (1,047 zeros on the line, 36 off-line with β > ½; 1,119 in all against $N_{\text{DH}}(1200) = 1119.49$) plus a smooth tail gives λ₃₂₈,₉₉₆ = 1383.25 and λ₃₂₈,₉₉₇ = −2382.03, inside the certified box. The step between them, −3765.28, matches the certified run to every printed digit (`riemann/claude/dh_crosscheck_sibling.py`).
  - A second audit, cross-validated only to n = 8,000, reports λ₃₂₈,₉₉₆ = +395.90 and λ₃₂₈,₉₉₇ = −3369.42. The step and the crossing are the same; its values sit 990 low because of defects in its smooth-tail tables. They are cross-validated, not certified.
  - All three runs place the first negative coefficient at n = 328,997.
- The census count carries the conductor: $N_{\text{DH}}(T) = \tfrac{T}{2\pi}\ln\tfrac{5T}{2\pi e} + O(\ln T)$ gives 2023.93 at T₀ against the certified 2024.

**What "certified" rests on.** It rests on:
- the correctness of Arb (python-flint 0.9) and of the scripts listed in R.18;
- the two analytic bounds stated in the scripts: the Dₙ integration-by-parts bound with its coefficient majorant, and the tail bound for t > 10¹⁷.

No floating-point step enters the certified chain.

### 1.2 Shifted plug ξ(s−¼)ξ(s+¼): **n = 8,260 confirmed independently**

The corpus (R.8) obtained λ^G as 2λ^ζ + Δ, reusing its ζ coefficients. Here λ^G is summed directly over G's own zeros at ¼ + iγ and ¾ + iγ: the first 4,000 ζ zeros plus a smooth tail.

| n | 1 | 2 | 4 | 7 | 8 | 12 |
|---|---|---|---|---|---|---|
| Taylor (independent) | 0.046178 | 0.184636 | 0.737362 | 2.248274 | 2.930681 | 6.524805 |
| zero sum (here) | 0.046178 | 0.184636 | 0.737363 | 2.248277 | 2.930684 | 6.524811 |
| corpus R.8 | 0.046178 | 0.184636 | 0.737362 | 2.248274 | 2.930681 | 6.524805 |

- **λ₈,₂₅₉ = +1,692.7 and λ₈,₂₆₀ = −120.0.** Cutoff sensitivity is ≤ 2.3. A separate audit's Cauchy-transform route (16,384 points on |z| = 0.996, tracked branches) gives λ₈,₂₅₉ = +1,690.35 and λ₈,₂₆₀ = −122.32, and reproduces the eight rows of R.8 to 5×10⁻⁷.
- λ₁₂,₀₀₀ = −6.35×10⁶, matching the corpus's "about −6.4×10⁶".
- **Not in the corpus:** the trough at n = 8,177 comes within **+334.5** of zero, a near-miss one oscillation period (≈ 89) before the crossing.

This check is floating-point, not certified. The certified pipeline of §1.1 applies to it unchanged.

### 1.3 The onset law has a missing factor of 2

An off-line pair at height γ contributes −2rⁿ cos(nφ) to λₙ, with r = |1 − 1/(1−ρ̄)| ≈ e^{δ/γ²}. So the first sign change sits where **rⁿ ≈ λ_smooth(n)/2**:

$$n^*\,\ln r \;\approx\; \ln\!\big(\lambda_{\text{smooth}}(n^*)/2\big).$$

The corpus's law reads n*·δ/γ² ≈ ln A(n*). It was calibrated only on ξ(s−δ)ξ(s+δ). Those functions have two copies of ζ's background (λ_smooth ≈ 2A), so the 2s cancel and the law looks exact. For a single-factor function (DH, and ζ itself) it is off by ln 2:

| prediction for DH | n* | miss |
|---|---|---|
| corpus law, ζ background (R.11: 342,650–342,860) | 342,857 | +4.2% |
| corpus law, DH background (R.11's proposed refinement) | 346,532 | +5.3% |
| **corrected:** n·ln r = ln(A_DH/2) | **328,666** | **−0.10%** |
| certified | 328,997 | — |

**Verdict on bet 1.** The bet **survives its own falsifier**:
- the miss is 4.0%, under the 10% threshold;
- there is no negative coefficient below 10⁵;
- the lowest off-line zero is where it was assumed.

The point estimate was off for an identifiable reason, though. The refinement R.11 proposed (using DH's own background) moves the estimate the wrong way. The structural forecast holds: the onset is controlled by the lowest off-line zero, at the time set by its leak against the smooth background. The calibration does not transfer between degrees without the amplitude factor. On "checkable by any number theorist with a laptop": the floating-point run took about fifteen minutes on two cores and the certified run a few minutes more. Both need the full off-line census below the cutoff, not just one zero.

---

## 2. The central logical point

The Realization's thesis is a conditional (§XVII): *if* ζ is a Star-Norm-conserving instance of the engine (the antecedent), *then* its zeros lie on the line (the consequent).

- **The consequent holds by construction.** "Instance" places each zero on the held pair of edges, and the chosen seating identifies that pair with the critical line (§II, §VI). The corpus itself says the seatings are chosen (R.13).
- **The antecedent is named four ways. Three are known equivalents of RH, and the fourth is strictly stronger:**
  - passivity of ξ′/ξ (Lagarias 1999);
  - Weil positivity (Weil);
  - strong recurrence (Bagchi 1981);
  - one quantum per height, which is RH plus simplicity (§X; elementary and correct).

So the conditional reads **RH ⇒ RH**, or under the fourth name RH ∧ simplicity ⇒ RH. The framework does not reduce RH to anything weaker. It renames it. What it genuinely adds is three things:
1. a curated set of correct reformulations;
2. computations, partly independently reproduced and, for bet 1, certified;
3. falsifiable bets, the first of which is now settled.

---

## 3. Every relied-on claim, ranked

**Tier A: proven mathematics, correctly cited** (spot-checked):
- ℓ² edge at σ = ½ and the mean square ζ(2σ); Mellin–Plancherel on Re s = ½; Hölder p = 2.
- Bohr's lift and Hedenmalm–Lindqvist–Seip; Kronecker.
- Li / Bombieri–Lagarias; Lagarias positive-realness; Foster form under RH; Julia set of g(s) = s²/(2s−1). The last is true but trivially conjugate to w².
- Riemann–von Mangoldt with constant 7/8; Selberg's variance of S; Littlewood ∫S = O(log T).
- Bohr–Landau "almost all zeros near the line"; random Euler product converging a.s. on σ > ½; Bost–Connes transition at β = 1.
- Rodgers–Tao Λ ≥ 0; Platt–Trudgian (RH to 3×10¹²).
- Büthe's partial-RH ψ bounds, reaching about x ≲ 2×10²⁵ with that height.
- Johansson's rigorous λₙ to 10⁵ (*Numer. Algor.* 69, 2015; arXiv:1309.2877). Keiper (1992) reached n = 2,000.
- Gonek–Hughes–Keating hybrid product; Heap's splitting conjecture to order under RH (arXiv 2102.02092).
- Hasse, Weil, Deligne, Ihara / Ramanujan graphs; Nyman–Beurling with σ = 1/p in Lᵖ.
- Cramér under RH; Baker–Harman–Pintz; Lagarias's σ(n) criterion (RH is Π⁰₁); one quantum per height ⟺ RH + simplicity.

**Tier B: true, but misdescribed or used beyond what it shows.** See Part 5, items 1–5.

**Tier C: computed** (the corpus says so in R.13):
- Now certified: the DH census below 1996 and its Li coefficients to n = 328,997.
- Reproduced in floating point: the DH crossings-minus-ticks debt; the shifted-plug n = 8,260 and its low-n table.
- Not reproduced here: the seam-loss tables (§XII), R.6 heat and truncation, R.14–R.16.

**Tier D: heuristic or fitted laws carrying numbers:**
- the onset law (mis-normalized by ln 2 for single-factor functions; §1.3);
- the t^{−3/8} loss rate and α → 3/8 (GUE plus a local peak model; misses 10¹⁰ by about 8×);
- the "inverted onset law, λₙ ≥ 0 to 10²⁷" (an extrapolation of a fitted law; the fact holds for every n under the Lean-certified RH, 21 Nov 2026);
- "S(T) stays under half a tick RMS at 10¹²" (an asymptotic extrapolation);
- the zeros' variance budget ½ ln 2 (CANDIDATE).

**Tier E: framework axioms, not mathematics.** "FORCED" in §XVII means forced *given* these:
- Star-Norm conservation forcing a free write head; the one-bit tax;
- the exponent cap from cross-breeding Ohm and Faraday;
- the Gray-code braid "holding" the zeros; the write-only Book;
- every vertex-to-role seating.

The §0 physics (P_write = (3/2)c⁵/G, t_bit = t_H/3, Λℓ_P² = 3/√N₄) is unproven and not used by any mathematical step.

**Tier F: readings and restatements.** Each of these is equivalent to RH or is an analogy; none narrows it:
- RH as passivity, Krein positivity, the Julia set, tier quantization, torsion-freeness, KD-3, or zero temperature.

### The "why it can't be closed" claims, ranked

| claim | status |
|---|---|
| Finite computation can refute RH but never prove it (Π⁰₁) | **proven** |
| No finite-precision computation certifies a zero's simplicity in general | **true** as a statement about numerics |
| A density ("almost all") theorem alone cannot exclude one zero | **true, trivially** (measure-zero exceptions) |
| Averaging tools "cannot see" an off-line zero | **not proven, and too strong.** De la Vallée-Poussin's zero-free region excludes zeros *pointwise* from an averaged positivity, 3 + 4cos θ + cos 2θ ≥ 0. That fits bet 3 but undercuts the claim as a barrier. |
| "Nothing routable decides occupancy" (equivalences can't prove RH) | **forecast.** Weil's proof for curves routed to an intersection form and then used a provable positivity (Hodge index). |
| Brune/Darlington synthesis presupposes passivity | **true of those methods**; not a barrier to others |
| Absolute rates can't be derived | **a design axiom of the framework**, not mathematics |

---

## 4. What would change the picture

- **The onset law re-derived from the explicit term −2rⁿ cos nφ against λ_smooth.** This needs no fit, and it covers every degree.
- **The averaging claim tested as R.12 proposes.** Plant an off-line zero and see which statistic registers it first. Include the 3–4–1 positivity among the tools.
- **The certified pipeline of §1.1 run on the other plugs.** That means the shifted plug at 8,260 and the even and odd characters of R.12. It applies unchanged: census, Taylor-model segment, digamma line, Dirichlet bound.

---

## 5. Discrepancies in the text

1. **§VII and hub §8.** "The bank cancels the walls' active pole … the circuit form of the Prime Number Theorem." The cancellation is ζ's simple pole at s = 1 (ζ′/ζ has residue −1 there). Every Dirichlet series with a simple pole at 1 does this. The PNT is the separate statement ζ(1+it) ≠ 0.
2. **§XIII.1.** "At no finite t ≠ 0 do two wheels realign, in phase or anti-phase." As written this is false: 2^{−it} = 3^{−it} whenever t = 2πk/ln(3/2). What is true, by irrationality of ln 3/ln 2, is that no t ≠ 0 returns both wheels to phase 0 together, or to −1 together.
3. **§IX transfer sentence.** "Every RH-quality statement … unconditional below the transfer scale." This holds for ψ (Büthe, x ≲ 2×10²⁵). It does not hold for λₙ ≥ 0 to 10²⁷, which rests on the fitted onset law; rigorous positivity is known to n = 10⁵. The onset law should read ln(λ_smooth/2), not ln A (§II, §IX, §XV).
4. **§XIV elliptic-curve count.** "None parabolic or hyperbolic" is guaranteed by Hasse, and aₚ² = 4p is impossible for prime p. The count checks the code; it is not evidence for the correspondence.
5. **§II, §VI, hub §4.** The 4-vertex character form is a model built here. Weil's criterion is positivity of a quadratic functional on test functions. The character algebra is LANDED; its identification with Weil's functional is a reading.
6. **§XVII.** Seatings are labelled "FORCED", but R.13 says "the K₄ seatings are chosen". Read correctly, "forced" means forced given the seating convention and the engine's axioms.

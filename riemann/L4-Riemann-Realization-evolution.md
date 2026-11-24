# L4-Riemann-Realization-evolution
## Standing Reference Tables, and How the Realization Was Built

*Companion to `L4-Riemann-Realization` (the standing text, §0–§XVII) and `L4-Riemann-Realization-Inventory` (the pieces, by register). Part 0 holds the standing reference tables the Realization cites as R.1–R.18: every computed claim with its method and precision, the placed bets, the open computations, the limits of the record. Parts I–IV hold the process: what was built in what order, what was withdrawn and why, the patterns behind the errors, and the address maps for anyone holding an older citation. Distinct from `L4-Riemann-evolution`, which records the 1854 geometry case.*

---

# Part 0. Standing Reference Tables

**Conventions.** $s = \tfrac12 + x + iy$, $s' = s - \tfrac12$, $w = 1 - 1/s$. Mean zero spacing at height $t$ is $2\pi/\ln(t/2\pi)$. $A(n) = \tfrac n2\ln n + \tfrac{\gamma_E-1-\ln2\pi}{2}n$. Precision is stated per table. Scripts named here sit with the record (`scripts/`).

### R.1. The disc

**Mirror reciprocity.** For ρ = 0.5765 + 7005.084i (the F₃₃ off-line point of R.2) and its mirror $1 - \bar\rho$: $|w_\rho| = 0.99999999844$, $|w_{1-\bar\rho}| = 1.00000000156$, product 1 to 20 digits. Leak $|w| - 1 = -1.559\times10^{-9}$ against $-\delta/\gamma^2$. The orbit-image table (P ↦ w, U ↦ w̄, R ↦ 1/w, I ↦ 1/w̄) checked to 20 digits at the same point. Reproduced independently in review.

### R.2. The first Lehmer pair

**The pair.** Zeros at γ = 7005.062866 and 7005.100565; gap 0.0377 = 0.042 mean spacings (mean spacing 0.895). Z(t) peaks at +0.003967 at t = 7005.08186. (mpmath.)

**Riemann–Siegel at the peak**, N = 33:

| Quantity | Value |
|---|---|
| p | 0.390020 |
| Main sum $2\operatorname{Re}W_{33}$ | −0.06600 |
| Leading correction $C_0$ | +0.06994 |
| Main + $C_0$ | +0.003937 |
| True Z | +0.003967 |

**The approximant's off-line pair.** $F_{33}(s) = S_{33}(s) + \chi(s)S_{33}(1-s)$ vanishes at $s = 0.5764841256 + 7005.0841410\,i$ and its mirror, $|F_{33}| \approx 5\times10^{-28}$.

**Truncation sweep:**

| N | $Z_N$ at the peak | Approximant keeps the pair on the line? |
|---|---|---|
| 30 | +0.0427 | yes |
| 32 | +0.2277 | yes |
| 33 | −0.0660 | no — off-line pair at x = +0.0765 |
| 34 | −0.1869 | no — x = +0.1276 |
| 36 | −0.1399 | no — x = +0.1108 |
| 40 | +0.1354 | yes |

The true peak is 17.6 times smaller than $C_0$.

### R.3. The Li coefficients and the prime side (ζ)

**Three routes, one number.** From the zeros: $\sum 4\sin^2(n\varphi_\gamma/2)$ over all 1 747 146 zeros below 10⁶ (matching the θ-count, each bisected to 10⁻⁹), plus a smooth tail. From the Bombieri–Lagarias formula, with $\eta_j$ built from Stieltjes constants at 80 digits. From the Taylor coefficients of $\log\xi(1/(1-z))$ directly, for n ≤ 12. Zeros and formula agree to six decimals for every n ≤ 60; formula and Taylor to fifteen digits for n ≤ 12 ($\lambda_1 = 0.0230957089661$). Moving the zero cutoff from 2.5×10⁵ to 10⁶ moves λ₂₀₀₀₀ by 0.002. *Earlier run.*

| n | $S_\infty(n)$ | $S_0(n)$ | $\lambda_n$ |
|---|---|---|---|
| 1 | −0.5541 | +0.5772 | 0.0231 |
| 2 | −0.8745 | +0.9669 | 0.0923 |
| 4 | −1.0068 | +1.3756 | 0.3688 |
| 7 | −0.3557 | +1.4802 | 1.1245 |
| 8 | +0.0209 | +1.4449 | 1.4658 |
| 12 | +2.0919 | +1.1714 | 3.2633 |
| 30 | +17.857 | +0.697 | 18.554 |
| 60 | +55.760 | +1.373 | 57.133 |
| 100 | +117.975 | +0.629 | 118.604 |
| 300 | +517.218 | +2.484 | 519.702 |
| 1000 | +2324.30 | +1.76 | 2326.05 |
| 2000 | +5340.99 | +10.77 | 5351.76 |
| 5000 | +15642.08 | −2.99 | 15639.09 |
| 10000 | +34749.14 | −12.56 | 34736.58 |
| 20000 | +76429.01 | +8.97 | 76437.98 |

**$S_\infty$ against its Stirling form**, exact at 60 digits (`checks.py`); the difference settles to +0.746 by n = 6:

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $S_\infty$ exact | −0.5541 | −0.8745 | −1.0131 | −1.0068 | −0.8827 | −0.6607 | −0.3557 | +0.0209 | +0.4603 | +0.9555 | +1.5009 | +2.0919 |
| Stirling form | −1.1303 | −1.5675 | −1.7431 | −1.7487 | −1.6281 | −1.4067 | −1.1016 | −0.7249 | −0.2855 | +0.2096 | +0.7548 | +1.3455 |

**$S_0$ statistics.** Computed at every n ≤ 1000 and every fourth n up to 20 000: range [−20.9, +23.2]; first negative at n = 156; at least 176 sign changes; envelope $\sim n^{0.53}$, max $|S_0|/\sqrt n \approx 0.16$ at n = 20 000 — about 23 against the 1 401 that $O(\sqrt n\ln n)$ allows there. $S_\infty$ at n = 2000: 5340.3 predicted by Stirling, 5341.0 computed. *Earlier run.*

**The balance point from the primes.** Up to 10¹⁰ (455 million primes, segmented sieve) for the first and last rows, up to 10⁸ for the middle two. *Earlier run.*

| Prime sum | Limit | Error at the end of the range | Envelope |
|---|---|---|---|
| $\eta_0$ | −γ | 4.3×10⁻⁶ at 10¹⁰ | $X^{-0.497}$, 10³–10¹⁰ |
| $\eta_1$ | +0.187546 | 3.4×10⁻⁴ at 10⁸ | $X^{-0.495}\ln X$ |
| $\eta_2$ | −0.051689 | 3.1×10⁻³ at 10⁸ | $X^{-0.495}(\ln X)^2$ |
| $\sum\Lambda(k)k^{-3/4} - 4X^{1/4}$ | $-\frac{\zeta'}{\zeta}(\tfrac34) = -4.6276$ | 1.3×10⁻³ at 10¹⁰ | $X^{-0.249}$, 10³–10¹⁰ |

Scaled by their exponents over the last decade: $|E_0|\,X^{1/2} \le 0.64$ and $|E_{\text{sh}}|\,X^{1/4} \le 0.64$.

**Prime-side unsharpness.** At X = 10⁸ the Laguerre sum reproduces $S_0(n)$ to 2×10⁻⁵ at n = 1, 3×10⁻⁴ at n = 2, and to 1–2% for n = 4 to 12.

### R.4. The third plug: L(s, χ₅)

**Method** (`third_plug.py`). λₙ = n·[zⁿ] of the logarithm of the completed function at $s = 1/(1-z)$, by a 256-point Cauchy transform on |z| = ½ at 40 digits. The split follows the Bombieri–Lagarias convention: for ζ, $S_\infty = n[z^n]\log\big(s\,\pi^{-s/2}\Gamma(s/2)\big)$ and $S_0 = n[z^n]\log\big((s-1)\zeta(s)\big)$; for the real even character mod 5 ($\chi_5 = (0, 1, -1, -1, 1)$), $S_\infty = n[z^n]\log\big((5/\pi)^{s/2}\Gamma(s/2)\big)$ and $S_0 = n[z^n]\log L(s,\chi_5)$. **Validation:** the ζ split reproduces the formula values of R.3 ($S_\infty(1) = -0.55412$, $S_0(1) = +0.57722$). Imaginary parts of all χ₅ coefficients below 4×10⁻²⁸.

| n | $S_\infty^\zeta$ | $S_0^\zeta$ | $\lambda_n^\zeta$ | $S_\infty^{\chi_5}$ | $S_0^{\chi_5}$ | $\lambda_n^{\chi_5}$ |
|---|---|---|---|---|---|---|
| 1 | −0.55412 | +0.57722 | 0.02310 | −0.74940 | +0.82768 | 0.07828 |
| 2 | −0.87454 | +0.96689 | 0.09235 | −0.26510 | +0.57750 | 0.31240 |
| 3 | −1.01306 | +1.22070 | 0.20764 | +0.40110 | +0.29915 | 0.70025 |
| 4 | −1.00680 | +1.37559 | 0.36879 | +1.21208 | +0.02626 | 1.23833 |
| 5 | −0.88273 | +1.45827 | 0.57554 | +2.14087 | −0.21902 | 1.92185 |
| 6 | −0.66073 | +1.48830 | 0.82757 | +3.16758 | −0.42280 | 2.74478 |
| 7 | −0.35573 | +1.48019 | 1.12446 | +4.27730 | −0.57731 | 3.69999 |
| 8 | +0.02090 | +1.44486 | 1.46576 | +5.45865 | −0.67929 | 4.77937 |
| 10 | +0.95554 | +1.32380 | 2.27934 | +8.00273 | −0.72861 | 7.27412 |
| 12 | +2.09186 | +1.17140 | 3.26326 | +10.74848 | −0.59823 | 10.15026 |
| 20 | +8.09862 | +0.67065 | 8.76928 | +23.19300 | +0.63086 | 23.82386 |
| 30 | +17.85665 | +0.69714 | 18.55379 | +40.99822 | +0.53700 | 41.53522 |
| 40 | +29.31332 | +1.16406 | 30.47738 | +60.50208 | −0.96435 | 59.53773 |

**Findings.**
- $S_\infty^{\chi_5}(n) = S_\infty^\zeta(n) - 1 + \tfrac n2\ln 5$ holds to every digit shown. The −1 is the factor s that ζ's completion carries and the pole-free L-function does not; the $\tfrac n2\ln q$ is the conductor. **[LANDED]** as Taylor algebra; **[COMPUTED]** here.
- The deficit window shrinks from n ≤ 7 (ζ) to n ≤ 2 (χ₅). From n = 5 the prime part is negative over a long stretch and the archimedean place carries alone.
- $\lambda_n^{\chi_5} > 0$ for every n ≤ 40, minimum 0.0783 at n = 1.
- For conductor q ≥ 23 with this Γ-factor, $S_\infty^\zeta(n) - 1 + \tfrac n2\ln q > 0$ at every n (the binding case is n = 1: $-1.5541 + \tfrac12\ln 23 = +0.0136$). The deficit window is empty.

This closes the edge-plurality gap the review flagged on Realization §VII Result 1 (two instances → three), and corrects its wording: the low-n division of labour is set by Stirling, the pole and the conductor, not by the Γ-shape alone.

### R.5. The counting balance

**Main term.** At t = 7005, $I^2R + \tfrac78 = 6708.56$ against the true count 6708.

**The 24-seating sweep** (`third_plug.py`). Quantities $\{N,\ \sqrt{t/2\pi},\ \ln(t/2\pi e),\ N/\sqrt{t/2\pi}\}$ at t = 7005, assigned to (P, U, I, R) in all 24 ways; tested for $P = I^2R$ and $U = IR$ at 1%. **Exactly one survives:** P = N, U = N/I, I = $\sqrt{t/2\pi}$, R = $\ln(t/2\pi e)$. The seating of Realization §VII is confirmed over the full sweep, not only against the ϑ′ rival.

**The constant.** $\vartheta(t) - \big[\tfrac t2\ln\tfrac{t}{2\pi} - \tfrac t2\big]$ at t = 10⁶, from $\operatorname{Im}\log\Gamma(\tfrac14 + \tfrac{it}{2}) - \tfrac t2\ln\pi$ at 30 digits: −0.3926990609, against −π/8 = −0.3926990817 (difference 2×10⁻⁸, the next Stirling term $1/(48t)$). With +1 from s(s−1), the Riemann–von Mangoldt constant 7/8 is accounted for (`witness_checks.py`).

### R.6. Truncation and heat across height

**Test set.** Every pair of consecutive zeros below t = 40 000 with gap under 0.15 mean spacings — **126 pairs**. Zeros located by a Riemann–Siegel sum carrying both corrections $C_0, C_1$, error ≤ 10⁻⁶ against mpmath. The count, 49 395 sign changes, matches Riemann–von Mangoldt (49 394.7). The five best pairs re-located in mpmath agree to six digits. *Earlier run.*

**Heat:** first-order collision time $\tau^* = -4\,Z/Z''$ at the peak, in de Bruijn–Newman units. It matches Realization §IX's gap²/2 at ratio 0.983–0.9997 across all 126. Backward heat ranks pairs by absolute gap alone.

**Truncation:** a pair is lost at its natural cutoff $N = \lfloor\sqrt{t/2\pi}\rfloor$ when the main sum $2\operatorname{Re}W_N$ has fewer than two sign changes between the midpoints to its neighbours.

The twelve best pairs below 40 000:

| $t_1$ | gap/mean | $Z_{\text{peak}}$ | τ* | N | $C_0$ at peak | at natural N |
|---|---|---|---|---|---|---|
| 36510.1664 | 0.0407 | +0.00380 | 0.000436 | 76 | -0.0599 | kept |
| 7005.0629 | 0.0421 | +0.00397 | 0.000710 | 33 | +0.0699 | lost |
| 17143.7865 | 0.0445 | +0.00215 | 0.000623 | 52 | -0.0713 | kept |
| 5229.1986 | 0.0463 | +0.00486 | 0.000935 | 28 | -0.1163 | kept |
| 33179.3653 | 0.0495 | +0.00361 | 0.000658 | 72 | -0.0509 | kept |
| 22016.0079 | 0.0577 | +0.00401 | 0.000987 | 59 | +0.0733 | lost |
| 24182.1031 | 0.0593 | +0.00715 | 0.001016 | 62 | -0.1062 | kept |
| 21324.9440 | 0.0668 | +0.00410 | 0.001331 | 58 | -0.0645 | kept |
| 17366.5172 | 0.0764 | -0.00916 | 0.001833 | 52 | -0.0541 | lost |
| 23153.5150 | 0.0775 | +0.01014 | 0.001753 | 60 | -0.0589 | kept |
| 25704.5248 | 0.0827 | +0.00975 | 0.001948 | 63 | +0.1043 | lost |
| 15471.5508 | 0.0843 | +0.01944 | 0.002296 | 49 | +0.0581 | lost |

The tightest pair below 40 000 is at t = 36510.166, gap 0.0407 mean spacings.

**Below 40 000.**
1. **Heat order carries no information about truncation loss.** 74 of 126 pairs are lost at their natural N. Ranked by heat time, a lost pair outranks a kept one with probability 0.465 — chance (by gap/mean 0.464; by peak height 0.507). Inversions (2059) outnumber concordant orderings (1789), and no heat threshold classifies better than "all lost".
2. **The rule.** A pair is lost exactly when the leading correction $C_0$ has the same sign as $Z_{\text{peak}}$ *and* is larger. Here $|Z_{\text{peak}}| \ll |C_0|$ (median ratio 0.32), so the size condition is almost always met and the verdict reduces to $\operatorname{sign}(C_0)\cdot\operatorname{sign}(Z_{\text{peak}})$ — a coin set by the parity of N and the phase p, blind to the gap. The rule follows from the Riemann–Siegel formula; what the computation adds is that $C_1$ and higher terms never overturn it.

**Across height.** Windows of consecutive zeros at 10⁶, 10⁸, 10¹⁰ and 10¹², on an evaluator with exact phase reduction (error ≤ 2×10⁻⁶ against mpmath at 10¹²). Each window's zero count matches its θ-count. Pairs with gap under 0.35 mean spacings measured; the close-pair columns use gap < 0.15. *Earlier run.*

| Height | Zeros | Close pairs | Lost at natural N | Rule holds | Median $\lvert Z_{\text{peak}}\rvert/\lvert C_0\rvert$ | Median $\lvert C_0\rvert$ | Heat order predicts loss | τ*/(gap²/2) |
|---|---|---|---|---|---|---|---|---|
| < 4×10⁴ | 49 395 | 126 | 74 | 126/126 | 0.32 | 7.2×10⁻² | 0.47 | 0.98–1.00 |
| 10⁶ | 20 008 | 53 | 21 | 770/770 | 0.66 | 2.5×10⁻² | 0.68 | 0.94–1.00 |
| 10⁸ | 39 999 | 132 | 9 | 1628/1628 | 2.5 | 6.2×10⁻³ | 0.89 | 0.90–1.00 |
| 10¹⁰ | 14 999 | 56 | 4 | 651/651 | 5.8 | 2.6×10⁻³ | 0.94 | 0.94–1.03 |
| 10¹² | 6 000 | 20 | 0 | 283/283 | 28 | 7.5×10⁻⁴ | — | 0.94–1.01 |

("Rule holds" counts every pair with gap < 0.35 in the window; "heat order predicts loss" is the probability that a lost close pair outranks a kept one by heat time, 0.5 being chance.)

3. **The rule is exact at every height: 3 458 of 3 458 pairs.**
4. **The gate closes with height.** $|C_0|$ falls as $t^{-1/4}$ while close-pair peaks do not, so the size condition admits fewer pairs. Where it is met, loss stays a coin (0.59, 0.53, 0.50 of the admitted pairs at < 4×10⁴, 10⁶, 10⁸). Where it fails, the pair is kept whatever the sign. So truncation loses only the tightest pairs, and its loss order becomes gap-ordered: heat order predicts it at 0.68, then 0.89, then 0.94. At 10¹² the main sum keeps every pair in the window, gap < 0.05 included.
5. **Two readouts that converge in what they rank.** Heat reads a magnitude, the gap. Truncation reads a sign gated by a magnitude. At low height the sign dominates and the two are orthogonal; with height the magnitude takes over and truncation's verdict falls into heat's order. The coin persists wherever the gate is open, so they are never one operation. **[READING]**: a phase readout and an amplitude readout on one object, whose relative weight is set by the height.
6. **The gate thins and never shuts.** Close-pair peaks hold steady while $|C_0|$ shrinks, so the median ratio should grow as $t^{1/4}$. Scaled from 10⁶ on the table's own values (`checks.py`): 0.25 predicted against 0.32 observed below 4×10⁴, 2.09 against 2.5 at 10⁸, 6.60 against 5.8 at 10¹⁰, 20.9 against 28 at 10¹². The loss rate follows from the same mechanism. A close pair's peak scales as $u^2|Z|$ in normalised gap u; GUE repulsion gives $P(u < \varepsilon) \propto \varepsilon^3$; a pair is lost when its peak falls below $|C_0| \propto t^{-1/4}$, which asks $u \lesssim t^{-1/8}$. The per-zero loss rate therefore scales as $t^{-3/8}$ **[READING]**, heuristic on GUE pair statistics and the local quadratic peak model — small, and never zero. Over all zeros up to T the smallest peak falls as $(T\ln T)^{-2/3}$, faster than $T^{-1/4}$, so infinitely many truncation losses occur as T → ∞ even as each fixed window empties. Normalised at 10⁶ (1.05×10⁻³ per zero), the law predicts 1.87×10⁻⁴ at 10⁸ against 2.25×10⁻⁴ observed; 3.3×10⁻⁵ at 10¹⁰ against 2.7×10⁻⁴ observed (4 losses against 0.49 expected in 14 999 zeros, the one window that departs); and 5.9×10⁻⁶ at 10¹² — 0.035 expected losses in 6 000 zeros, against 0 observed.

**What the census does not buy.** Each row's τ* would once have been a Csordas–Smith–Varga lower-bound certificate on Λ. Rodgers–Tao (2020) proved Λ ≥ 0, which supersedes every negative lower bound, and the record pairs at large height are far tighter than any here. The census witnesses the zero margin; it certifies nothing new about Λ.

### R.7. A pair on the line is invisible in λₙ

On $|w| = 1$, $\varphi_\gamma = 2\arctan(1/2\gamma)$. The first Lehmer pair sits at angular separation $\Delta\varphi = 7.68\times10^{-10}$ and stays phase-coherent up to $n \approx 1.30\times10^{9}$ (≈ 2³⁰: the two commit tapes agree to about thirty binary digits); the second at $1.20\times10^{-10}$, coherent to $n \approx 8.32\times10^{9}$. Whatever its quality, a pair on the line contributes $4\sin^2(n\varphi_1/2) + 4\sin^2(n\varphi_2/2) \in [0, 8]$. At those n — under RH, and, by the transfer estimate of R.13, inside the regime the verified height reaches — $\lambda_n \approx A(n)$ is about $1.22\times10^{10}$ and $8.57\times10^{10}$ **[LANDED]** asymptotic, with fluctuations of order $\sqrt n\ln n \approx 7.6\times10^{5}$ and $2.1\times10^{6}$.

### R.8. The broken plug and the onset law

**The plug.** $\xi_G(s) = \xi(s-\tfrac14)\,\xi(s+\tfrac14)$: entire, real, symmetric under s ↔ 1−s, every zero off the line at σ = ¼ and σ = ¾.

**Method** (`li_shifted.py`). For n ≤ 40 directly, from the Taylor coefficients of $\log\xi_G(1/(1-z))$ by a 512-point Cauchy transform on $|z| = \tfrac12$ at 60 digits; for all n to 40 000 as $\lambda^G_n = 2\lambda^\zeta_n + \Delta_n$, with $\Delta_n = \sum_\rho\big[2f(\rho) - f(\rho+\tfrac14) - f(\rho-\tfrac14)\big]$, $f(s) = (1-1/s)^n$, a symmetric second difference over 400 zeros (to T = 679.7) whose tail falls as $n^2\ln T/T^3$ — below 0.2 throughout. The two routes agree to six decimals across n = 5–40; the direct transform returns $\lambda_1(\zeta) = 0.02309570896612$.

| n | $\lambda^\zeta_n$ | $\lambda^G_n$ |
|---|---|---|
| 1 | 0.023096 | 0.046178 |
| 2 | 0.092346 | 0.184636 |
| 4 | 0.368790 | 0.737362 |
| 7 | 1.124460 | 2.248274 |
| 8 | 1.465756 | 2.930681 |
| 12 | 3.263255 | 6.524805 |
| 20 | 8.769277 | 17.535095 |
| 40 | 30.477375 | 60.955194 |

The broken plug tracks twice ζ's coefficients to 0.03% at low n, stays positive through **n = 8 259**, and first turns negative at **n = 8 260**. From there its coefficients oscillate with growing amplitude — about −6.4×10⁶ at n = 12 000, −1.4×10¹¹ at n = 20 000. The onset is set by the first zero's off-line partner, $|w| = 1.0012501$, whose leak $e^{n\delta/\gamma_1^2}$ has to overtake the archimedean growth.

**The onset law** $n^*\delta/\gamma_1^2 \approx \ln A(n^*)$, with $\xi(s-\delta)\xi(s+\delta)$ (`onset.py`):

| δ | $\gamma_1^2/\delta$ | first n with $\lambda_n < 0$ | $n^*\delta/\gamma_1^2$ | $\ln A(n^*)$ |
|---|---|---|---|---|
| 0.25 | 799 | 8 260 | 10.34 | 10.24 |
| 0.20 | 999 | 10 571 | 10.58 | 10.52 |
| 0.15 | 1 332 | 14 569 | 10.94 | 10.89 |
| 0.10 | 1 998 | 22 833 | 11.43 | 11.40 |

Holds to about 1%. An independent solver of the law itself returns 8 171 / 10 501 / 14 490 / 22 756 — the same 1%, from the other side.

**What finite positivity can certify.** By the law, $\lambda_n \ge 0$ for all n ≤ N excludes an off-line zero only when $\gamma^2 \lesssim N\delta/\ln A(N)$. The rigorous range N = 10⁵ reaches only γ ≲ 62 even at the largest offsets — far inside the zeros already verified directly on the line to heights beyond 10¹².

### R.9. S(T) across the first Lehmer pair

$S = N(t) - \vartheta(t)/\pi - 1$, mpmath at 30 digits (`s_lehmer.py`):

| t | N(t) | S(t) |
|---|---|---|
| 7004.9 | 6708 | −0.444 |
| 7005.0 | 6708 | −0.556 |
| 7005.0619 (just before the pair) | 6708 | −0.624 |
| 7005.0817 (between) | 6709 | +0.353 |
| 7005.1016 (just after) | 6710 | +1.331 |
| 7005.2 | 6710 | +1.221 |
| 7005.5 | 6710 | +0.886 |

Across the pair S rises by 1.96 in Δt = 0.038, while ϑ/π advances by **0.0421** — exactly the pair's gap in mean spacings, as it must be. (A review figure of 0.021 is off by a factor two.)

### R.10. Orbit, circuit and generator numerics

**Orbit volume.** $V = \tfrac83(xy)^2$, exact (determinant, sympy); at the F₃₃ pair (x = 0.0765, y = 7005.084), V = 7.658×10⁵ (`witness_checks.py`).

**Character product.** $\chi_x\chi_y = \chi_{xy}$ on the orbit: True (`krein_orbit.py`).

**Krein pairings** at an off-line test point (x = 0.13, y = 21.02) with a random complex F; every pairing matches $4(|a_1|^2 + |a_+|^2 - |a_-|^2 - \dots)$ to six digits (`krein_orbit.py`):

| Twist | $\langle F, m\cdot F\rangle$ | K₊ | K₋ |
|---|---|---|---|
| c (conjugation) | +1.551981 | 1 ⊕ x | y ⊕ xy |
| f (functional equation) | −1.503982 | 1 ⊕ xy | x ⊕ y |
| cf (line-reflection) | −3.245526 | 1 ⊕ y | x ⊕ xy |

On the line, with $F(P) = F(I)$ and $F(U) = F(R)$: $a_x = a_{xy} = 0$ exactly, and $\langle F, cf\cdot F\rangle = \|F\|^2 = 4.76$.

**The commit map** (`commit_map.py`): $g = M^{-1}(M(s)^2)$ identically; g commutes with c and f; Re g = ½ on the line; ½ ± 0.01 + 14.13i iterate to 1 and to 0; g(1) = 1, g(0) = 0.

**Foster form** with 2 000 zeros (to T = 2515.3) (`foster.py`):

| s′ | $\xi'/\xi(\tfrac12 + s')$ | Foster sum + tail |
|---|---|---|
| 0.3 + 1.0i | 0.0139282562 + 0.0462642979i | 0.0138903499 + 0.0461379437i |
| 0.05 + 3.0i | 0.00241704972 + 0.140708494i | 0.00241073196 + 0.140329431i |
| 1.2 − 0.7i | 0.0554533626 − 0.0321483947i | 0.0553017375 − 0.0320599469i |

On the line: $\operatorname{Re}\,\xi'/\xi(\tfrac12 + 7.5i) = -6.3\times10^{-27}$.

**Euler-factor poles** in s′ (`witness_checks.py`): for p = 2, every pole of $1/(1 - p^{-1/2}e^{-s'\ln p})$ has Re s′ = −0.5.

**The orbit generator** (`h_check.py`, `h2.py`, `witness_checks.py`). Exact, sympy: f, cf and c constraints hold; the general solution has 8 real parameters; the 1⊕3 action and the coefficients A, B, Δ match R.17 identically. Numerically: H commutes with $P_{cf}K$ (PT), anticommutes with $P_f$ (chiral), and the δ diagonal has sign pattern (+, +, −, −) on (P, U, I, R) = $\chi_x$. Threshold at ω = 1, k_Fa = 0.2, J_M = 0.6, J_C = 0, predicted $\delta^* = 0.6/\sqrt{0.96} = 0.61237$:

| δ | 0.611 | 0.612 | 0.6124 | 0.613 | 0.62 |
|---|---|---|---|---|---|
| max \|Im z\| | 1.2×10⁻¹⁴ | 4.0×10⁻¹⁵ | 5.9×10⁻³ | 2.8×10⁻² | 9.8×10⁻² |

Square-root onset past the threshold confirmed independently in review (ratio 3.496 against 3.486 predicted).

### R.11. Placed bets

1. **Davenport–Heilbronn onset.** Taking 0.8085 + 85.70i as its lowest off-line zero (δ = 0.3085, $\gamma^2/\delta \approx 23\,807$), the onset law puts DH's first negative Li coefficient at **$n^* \approx 3.4\times10^5$** (342 650–342 860 under ζ's background), positive throughout below. DH's own background differs from ζ's — conductor 5, the odd factor Γ((s+1)/2), no pole — and moves $\ln A$, hence $n^*$, by about 1%.
   - *Assumption, declared.* The onset law was measured on detuned plugs, which break the Ramanujan bound: their leak is a reweighting of ζ's own waves. DH breaks a different axiom — no Euler product, so no delay bank and no cancellation to fail. The law's shape should transfer, since the background is archimedean and the leak is $|w|^n$ either way, but the mechanism differs. The bet's own falsifier decides it.
   - *Register.* This is a Bridge-shaped number in the corpus's sense (`riemann/README`): dimensionless, predicted from structure before the computation, checkable by any number theorist with a laptop and no corpus access — the first such number the corpus places in pure mathematics.
   - *Falsifier:* a first negative coefficient well below 10⁵ (a lower off-line zero exists), or a miss of more than 10% against the log-corrected law.
2. **The gate's exponent.** Truncation windows at 10¹⁴–10¹⁶ recover the **$t^{-3/8}$ per-zero loss slope**, up to slow modulation from the moments of $|Z|$, and the 10¹⁰ excess resolves as a small-sample cluster once the window holds 10⁵–10⁶ zeros. *Falsifier:* a flat loss rate, or one falling faster than $t^{-1/2}$, across 10¹⁴–10¹⁶; or the enlarged 10¹⁰ window holding its excess.
3. **The orthogonal texture.** If a structural proof of RH over ℤ arrives, it reads a definite sign out of a pairing already latent on the real|complex interface — the archimedean scaling $\mathbb R_+^\times$ against the prime places, the weights on an incommensurate delay bank whose continuation stays passive (Realization §VII) — forcing K₋ = 0 by a mechanism whose sensitivity does not wait for $n \sim (\gamma^2/\delta)\ln A$, rather than through a new level built over $\mathbb F_1$ first. *Falsifier:* a proof via a newly constructed $\mathbb F_1$-level object whose intersection pairing has no representation on the adele/Mellin space.

### R.12. Open computations

- **The 10¹⁰ rescan.** 4 losses against 0.49 expected. Rescan 10⁵–10⁶ consecutive zeros around 10¹⁰ with a matched window at 10¹⁴: either the count reverts to the $t^{-3/8}$ curve or the GUE peak-scaling prefactor fails there.
- **The gate at 10¹⁴–10¹⁶.** Bet 2's own target.
- **DH's Li coefficients past 10⁵.** Bet 1's falsifier, with DH's own archimedean factor.
- **More plugs.** λₙ for further even characters (q = 8, 12, 13, …) and the first odd ones (Γ((s+1)/2)) to large n; the conductor-q ≥ 23 regime where the archimedean place carries alone, and where its prime part first has to work (Realization §XVII).
- **The trivial tower on the tier table.** Seat the waves $x^{-2k}/2k$ (Realization §0) and test whether the tier reading extends below the floor.
- **The third stuckness, tested.** Realization §XVII reads averaging blindness as the third stuckness: the averaging tools conclude without seeing a diagonal. A test: plant one off-line zero in a detuned plug and record the window at which each averaging statistic (mean square, Selberg variance, S(T) spread) first registers it, against the onset law's n*. The reading predicts no averaging statistic registers it before the uniform-in-scale tools do.
- **Gaps past 10⁹.** Extend R.16 to 10¹² with a segmented sieve; the (ln p)² ratio should stay inside 0.5–0.8 (Cramér's model, with Granville's correction pushing toward 2e^{−γ} ≈ 1.12 at the extremes).
- **The seam floor with $C_0$.** Computed through $10^5$ and near $10^6$ (Realization §XII): zero crossings lost with $C_0$, margin at least $52\times$; the bare loss exponent runs at about $0.2$ and tracks the stiffness. Extend both to $10^8$–$10^{12}$ from published zero tables.

### R.13. Limits of the record

What the numbers here do and do not carry, stated once for whoever appeals next. The process record behind them, the build, the withdrawals and the patterns, follows in Parts I–IV.

- **No count here is rigorous.** The zero counts to 40 000 and in the height windows carry no interval arithmetic and no Turing-method bound. They agree with Riemann–von Mangoldt and with the literature, which has RH verified far beyond these heights, and claim nothing more.
- **Every height reached has been computed before.** Zeros near 10¹² and far beyond are in the literature, and λₙ is rigorous to n = 10⁵ (Keiper computed to n = 7000). What is new is this set's own observables there: the sign rule, the gate, the heat–truncation convergence, the S∞/S₀ split, the onset law.
- **τ\* is first order.** It matches the local model to 2%; a full heat-flow computation of $H_\tau$ was not run.
- **"Lost at N" depends on the window.** The criterion is sign changes between neighbour midpoints. A different window disagrees at the edges of the N range, though not on any conclusion.
- **The high windows are small.** 6 000 zeros at 10¹² hold 20 close pairs. "Heat order predicts loss" at 10⁸ and 10¹⁰ rests on 9 and 4 lost pairs. The direction is clear; the numbers are not precise.
- **$S_0(n)$ is dense only to n = 1000.** Beyond that it was computed at every fourth n, so its sign changes there are a lower bound and its extremes may be slightly understated.
- **The prime-side exponent is a finite-range measurement.** −0.497 up to 10¹⁰ is consistent with von Koch's form of RH and nothing more.
- **The gate law and the onset law are heuristic and fitted.** $t^{-3/8}$ rests on GUE pair statistics and a local peak model, and misses 10¹⁰ by a factor of about eight; the onset law holds to 1% on detuned plugs only.
- **The third plug runs to n = 40.** The conductor threshold q ≥ 23 follows from the exact archimedean formula, not from computed coefficients.
- **Silent numerical failure is the standing hazard at scale.** Five faults surfaced in the push to height — a float64 2π over ~10¹² phase wraps, rounded time offsets, a truncated θ expansion, a clamped singularity in Ψ(p) that manufactured about ten spurious zero pairs below 10⁶, and a tail integral that silently returned zero — none raising an error, each caught by a count or a known value. The guard used throughout: at every new scale, re-establish one count and one known value before reading any statistic. None reached a result below 40 000; the 126-pair scan was rerun with the fixed Ψ and is identical.
- **Conditional inputs, and the regime of each.** The record uses five inputs conditional on RH or on more: Λ = 0 (de Bruijn–Newman constant; Rodgers–Tao give Λ ≥ 0 unconditionally); $S_0(n) = O(\sqrt n\ln n)$, the Bombieri–Lagarias bound under RH; GUE pair statistics (Montgomery, under RH), behind the gate law; simplicity of the zeros, behind $C = \tfrac12$ per tank; and the Keating–Snaith random-matrix constants in R.14. Each is labeled where used. **Regime.** Below the transfer scale of the verified height — every zero to H ≈ 3×10¹² on the line (Platt–Trudgian), RH-quality ψ bounds to about H² (Büthe), λₙ ≥ 0 to about 2H² ln A ≈ 10²⁷ by the inverted onset law — the RH-quality statements here hold unconditionally; above it they are conditional. The inverted onset law is an estimate from the fitted law, not a theorem.
- **The gap record is unconditional and finite.** R.16 is a sieve to 10⁹; Cramér's √p ln p bound it is compared against is conditional on RH, and is not tested by gaps this small.
- **The K₄ seatings are chosen.** Where they are literal, they are literal as mathematics; that the engine predicted them is not claimed.

### R.14. The price of being a prime

**Mertens' sum** (`price.py`, sieve to 10⁷):

| x | $\sum_{p\le x}1/p$ | $\ln\ln x$ | difference |
|---|---|---|---|
| 10³ | 2.19808 | 1.93264 | 0.26544 |
| 10⁴ | 2.48306 | 2.22033 | 0.26273 |
| 10⁵ | 2.70527 | 2.44347 | 0.26180 |
| 10⁶ | 2.88733 | 2.62579 | 0.26154 |
| 10⁷ | 3.04145 | 2.77994 | 0.26151 |

The difference settles to Mertens' constant M = 0.26150….

**Selberg's variance on the line.** 1 500 random heights in [T, 1.2T], mpmath at 15 digits; sampling error on each variance about ±0.07.

| T | mean log\|ζ(½+it)\| | var log\|ζ(½+it)\| | primes only: $\tfrac12\sum_{p^k\le T}\frac{1}{k^2p^k}$ | random-matrix: $\tfrac12\big(\ln\ln\tfrac{T}{2\pi} + \gamma + 1\big)$ |
|---|---|---|---|---|
| 10⁴ | 0.074 | 1.701 | 1.311 | 1.787 |
| 10⁵ | 0.011 | 1.900 | 1.422 | 1.924 |

The variance grows like $\tfrac12\ln\ln t$ (+0.20 ± 0.09 across the decade, against +0.11 from the primes alone and +0.14 from the random-matrix form). Its level sits about 0.4 above the primes-only sum: the finite-height contribution of the zeros near each sample point, which the Keating–Snaith random-matrix value captures within sampling error. Selberg's theorem is the asymptotic statement; at these heights the primes carry the growth and the zeros carry an O(1) offset.

**Price lines of the three plugs** (exact, from $|a_p|^2p^{-2\sigma}$): ζ, $|a_p| = 1$ → ½; $L(s,\chi_5)$, $|\chi_5(p)| = 1$ → ½; ζ(s − ¼)ζ(s + ¼), $a_p = p^{1/4}+p^{-1/4}$ → ¾, matching its upper zero line and its measured prime-sum balance point (R.3, envelope $X^{-0.249}$).

### R.15. Hilbert landmarks

**Mean square against ζ(2σ)** (`landmarks.py`; 4 000 random heights in [2000, 4000], mpmath at 15 digits):

| σ | mean $\lvert\zeta(\sigma+it)\rvert^2$ | reference | |
|---|---|---|---|
| 0.75 | 2.614 ± 0.075 | ζ(1.5) = 2.612 | agrees |
| 0.60 | 4.198 ± 0.148 | ζ(1.2) = 5.592 | short; heavy tail and slow convergence near the line |
| 0.50 | 7.380 ± 0.280 | $\ln\frac{t}{2\pi} + 2\gamma - 1 \approx 6.32$ | grows like ln t, as Hardy–Littlewood state; finite-sample |

Near the line the distribution of $|\zeta|^2$ is heavy-tailed and the finite-height mean converges slowly; only the σ = 0.75 row is a pin.

**Von Neumann's criterion** for the Euler product vector, $\sum_{p\le x}\big(1 - \sqrt{1-p^{-2\sigma}}\big)$:

| σ | x = 10³ | x = 10⁵ | x = 10⁷ |
|---|---|---|---|
| 0.60 | 0.7470 | 0.7903 | 0.8015 |
| 0.55 | 0.9226 | 1.0264 | 1.0695 |
| 0.50 | 1.1710 | 1.4246 | 1.5927 |

At σ = 0.6 the sum flattens; at σ = ½ its increments, 0.254 and 0.168, match $\tfrac12\ln\ln$ (0.255, 0.168). The vector leaves the vacuum's sector exactly at the line.

### R.16. Record prime gaps against the two scales

**Method** (`gaps.py`). Segmented NumPy sieve of Eratosthenes to 10⁹; each new maximal gap $g = p_{n+1} - p_n$ recorded with its lower prime p, from p > 10⁴. Exact integer arithmetic; the records agree with the published maximal-gap table (Nicely; Oliveira e Silva).

| p | gap | gap / (ln p)² | gap / (√p ln p) |
|---|---|---|---|
| 19609 | 52 | 0.532 | 3.76×10⁻² |
| 31397 | 72 | 0.672 | 3.92×10⁻² |
| 155921 | 86 | 0.602 | 1.82×10⁻² |
| 360653 | 96 | 0.586 | 1.25×10⁻² |
| 370261 | 112 | 0.681 | 1.44×10⁻² |
| 492113 | 114 | 0.664 | 1.24×10⁻² |
| 1349533 | 118 | 0.592 | 7.20×10⁻³ |
| 1357201 | 132 | 0.662 | 8.02×10⁻³ |
| 2010733 | 148 | 0.703 | 7.19×10⁻³ |
| 4652353 | 154 | 0.653 | 4.65×10⁻³ |
| 17051707 | 180 | 0.649 | 2.62×10⁻³ |
| 20831323 | 210 | 0.739 | 2.73×10⁻³ |
| 47326693 | 220 | 0.704 | 1.81×10⁻³ |
| 122164747 | 222 | 0.640 | 1.08×10⁻³ |
| 189695659 | 234 | 0.644 | 8.91×10⁻⁴ |
| 191912783 | 248 | 0.682 | 9.39×10⁻⁴ |
| 387096133 | 250 | 0.639 | 6.43×10⁻⁴ |
| 436273009 | 282 | 0.713 | 6.79×10⁻⁴ |

**Reading.** Against (ln p)² — Cramér's random model — every record sits in a band, 0.53–0.74. Against √p ln p — the cap RH imposes (Cramér 1920, under RH) — the ratio falls by a factor of 55 over the range. The held families (Realization §VIII) pile up to about (ln p)² and never approach the root-scale ceiling. The unconditional ceiling, $p^{0.525}$ (Baker–Harman–Pintz), is further off still.

---

### R.17. The orbit generator

*A finite model: the orbit generator and its exceptional point (Realization §IX).*

The orbit of Realization §II has four vertices, so it carries 4×4 generators. Ask for the most general one whose spectrum has the orbit's own symmetries, read in the coordinate $z = -i(s - \tfrac12)$, where real z is the critical line:

- **Cardinal** (f, swapping P ↔ R and U ↔ I, sending z ↦ −z): $P_f H P_f = -H$ — H anticommutes with $P_f$, so the spectrum is closed under negation;
- **Mutable** (cf, swapping P ↔ I and U ↔ R, sending z ↦ z̄): $P_{cf} H P_{cf} = H^*$ — the spectrum is closed under conjugation;
- **Fixed** (c) then follows: $P_c H P_c = -H^*$.

**What kind of generator this is.** The Mutable condition is PT-symmetry with parity $P_{cf}$: H commutes with the antilinear operator $P_{cf}K$, K being complex conjugation — and cf is itself the PT move on s, a reflection composed with a conjugation. The Cardinal condition is a **chiral** (sublattice) symmetry: H anticommutes with $P_f$, which is what pairs every eigenvalue z with −z. **[LANDED]** (definitions; **[COMPUTED]** on the matrix, R.10.) **H is a PT-symmetric generator with a chiral symmetry.** The PT-symmetric constructions already proposed for the zeros (Bender–Brody–Müller 2017) are the natural hunting ground for the generator question (Realization §XVII), reachable from this algebra without new machinery. **[READING]** In engine vocabulary the same structure is the corpus's bichiral design — both hands carried, the ledger picks one — with the PT break as the odd move the operating set lacks.

**[COMPUTED]** (exact, symbolic; R.10.) The two constraints leave **8 real parameters**, splitting into four Hermitian ones {ω, J_M, g_M, g_C} and four skew-Hermitian ones {δ, k_Fa, k_Fg, J_C}. Keeping the five real-edge parameters (g_M = g_C = k_Fg = 0), in vertex order (P, U, I, R):

$$H = \begin{pmatrix}
\omega + i\delta & k_{Fa} & J_M & J_C \\
-k_{Fa} & -\omega + i\delta & -J_C & -J_M \\
J_M & J_C & \omega - i\delta & k_{Fa} \\
-J_C & -J_M & -k_{Fa} & -\omega - i\delta
\end{pmatrix}.$$

Each parameter has a seat. ω is the frequency split, +ω on {P, I} and −ω on {U, R} — the Mutable character $\chi_y$. $J_M$ is the Mutable coupling (P–I, U–R), Hermitian. $k_{Fa}$ is the Fixed coupling (P–U, I–R), skew. $J_C$ is the Cardinal coupling (P–R, U–I), skew because f negates H. **δ is the gain/loss bias, +iδ on {P, U} and −iδ on {I, R} — the Fixed character $\chi_x$.**

**Gain/loss is the off-line direction.** That last seat is not a choice. The sign pattern of δ is exactly $\chi_x$, and x is the off-line displacement: the resistive half-plane Re s′ > 0 of the Smith chart (Realization §II), the first component of K₋ (Realization §II). **Gain/loss is the off-line direction; the leverage is the reactive holding; RH is leverage ≥ bias on every orbit.** **[READING]** on **[COMPUTED]** seating. The constraint this puts on the generator question is available now: whatever operator on ζ's side has H as its section, its gain/loss slot must sit on the Fixed character.

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

So the centroid's blindness in Realization §II belongs to the permutation action, and a generator that honours the functional equation moves the centroid mode into the Fixed–Mutable pair. What the generator gives instead is a threshold.

**The exceptional point.** Write $v = (\omega, k_{Fa})$ and $J = (J_C, J_M)$, with star-norm $\|u\|_*^2 = u_1^2 - u_2^2$, star-product $\langle J, v\rangle_* = J_C\omega - J_M k_{Fa}$, and wedge $J \wedge v = J_M\omega - J_C k_{Fa}$. The characteristic polynomial is $z^4 - Az^2 + B$, with **[COMPUTED]** (exact)

$$\begin{aligned}
A &= 2\big(\|v\|_*^2 - \|J\|_*^2 - \delta^2\big),\\
B &= \big(\|v\|_*^2 + \|J\|_*^2 + \delta^2\big)^2 - 4\langle J, v\rangle_*^2,\\
\Delta = A^2 - 4B &= 16\big[(J\wedge v)^2 - \delta^2\|v\|_*^2\big].
\end{aligned}$$

The spectrum is entirely real — all modes on the line — exactly when A ≥ 0, B ≥ 0 and Δ ≥ 0. The leverage $J \wedge v$ holds the modes on the line against the gain/loss δ up to $(J\wedge v)^2 = \delta^2\|v\|_*^2$. Pinned numerically, the predicted threshold $\delta^* = |J\wedge v|/\|v\|_* = 0.61237$ is where the spectrum leaves the real line, with square-root onset past it (R.10). Both kinds of coupling feed the leverage: the Hermitian Mutable coupling against the frequency split ($J_M\omega$), and the product of the two skew couplings, Cardinal against Fixed ($J_C k_{Fa}$).

**What the spectrum is: two dipoles, or one quartet.** The type distinction of Realization §II bites H itself. H acts on *one orbit's four vertices*; its *spectrum* is a different subject. With $z^2 = (A \pm \sqrt\Delta)/2$:

- **Δ ≥ 0, A ≥ 0, B ≥ 0:** spectrum $\{\pm a, \pm b\}$, all real — under z ↦ s these are **two dipoles**, two zeros on the line with their mirrors.
- **Δ < 0:** spectrum $\{\pm w, \pm\bar w\}$ — **one quartet**, a single off-line orbit with volume.
- **Δ ≥ 0 with $z^2 < 0$:** spectrum on the imaginary z-axis — zeros on the real s-axis, the Fixed collapse (P = U) instead of the Mutable one.

**[LANDED]** (elementary algebra on the quartic.) At Δ = 0 two eigenvalues merge into a double eigenvalue and leave the real line as a conjugate pair: **two cross-orbit dipoles in, one within-orbit tetrahedron out.** That is the Lehmer collision of Realization §IX, the hold / collapse / reseed of Realization §IX, with the leverage $(J\wedge v)^2$ in the place of the heat 2τ and the gain/loss $\delta^2\|v\|_*^2$ in the place of the gap δ². Realization §IX reaches that threshold from the de Bruijn–Newman flow on Ξ; the generator reaches it from the orbit's symmetry alone, with no ζ-data put in. **Two routes to one collision structure.** Read on the threshold, Rodgers–Tao's Λ ≥ 0 says ζ is not strictly inside the unbroken phase; with RH it sits exactly on the edge. **[READING]**

**Simplicity is a codimension statement.** A multiple zero on the line is the generator sitting exactly on its exceptional point — the borderline Δ = 0, codimension one in parameter space. Simple zeros are therefore the generic case, and vocabulary 8's separation of passivity from simplicity is the circuit form of the same fact: a double zero doubles its tank's residue to $C = \tfrac14$ and stays passive. Whether ζ is generic is the open content (Realization §XVII). **[READING]** In tier terms, a double zero is the RESEED opcode returning a degenerate root — the ± ambiguity collapsed before the commit instead of reopened by it.

**An address in the corpus's pathology language.** The threshold $(J\wedge v)^2 \ge \delta^2\|v\|_*^2$ has the shape of the corpus's $R = U^2/P$ balance (`BENDING_MINDS` §4): a squared structural term held against a drive bias. Read so, δ plays the Necessary Betrayer's divergence and $J\wedge v$ the Leo reset — structure holding modes on the line against its own drive. **[READING]**, filed as an address: the shape matches; whether the seating is forced is unexamined.

The generator is a finite model on one orbit. Which operator on ζ's side has it as its section, with its δ-slot on $\chi_x$, is the generator question of Realization §VI (the shaft's generator as the Hilbert–Pólya address).

### R.18. Method notes for the Realization's inline computations

| Table in the Realization | Script | Method and precision |
|---|---|---|
| The cavity (§I) | `cavity.py` | $Z_M$ from $M$-smooth integers $n \le 7$ on $t \in [10, 400]$, $\vartheta$ from mpmath, grid $10^{-3}$; Landau sums over sign changes; true zeros from `mpmath.zetazero` |
| Laue compensation (§III.2) | `laue.py` | exact $\pi(x)$, $\psi(x)$ by sieve to $10^4$; `li` and Riemann's $R$ from mpmath at 15 digits |
| $\chi_5$ zero sets (§II) | `nsd.py` | `mpmath.dirichlet` on the line, minima of $\lvert L\rvert$ refined by `findroot`, 20 digits; $[-20, 20]$ here, $[-45, 45]$ in the independent run |
| Per-orbit circuit (§II) | `tank.py` | sympy, symbolic in $\delta, \gamma, t$ (real); integrals and limits exact |
| Walls' turn-on (§IV) | inline | `findroot` on $\vartheta'$ at 15 digits: $t_{\min} = 6.2898359888$, $\vartheta = -3.5309728290$ |
| Shaft ledger (§X) | `dh.py` | Davenport–Heilbronn as $\tfrac{1-i\kappa}{2}L(s,\chi) + \tfrac{1+i\kappa}{2}L(s,\bar\chi)$, $\kappa = (\sqrt{10-2\sqrt5}-2)/(\sqrt5-1)$, completed by $(\pi/5)^{-s/2}\Gamma(\tfrac{s+1}{2})$; sign changes on grid $0.02$ over $[1, 200]$ against the walls' unwrapped phase; mean lag per window |
| Seam margin and rate (§XII) | `coeffs.py`, `scan.py`, `peaks.py`, `scale.py` | reference $Z$ = main sum $+ C_0 + C_1 + C_2$ (Gabcke coefficients tabulated on $8001$ points at 40 digits), agreeing with `siegelz` to $\sim10^{-8}$; grid at $1/40$ of the mean spacing; a loss is a sign-change interval of the reference the approximant misses |
| Stiffness (§I.4, §XII) | `stiff.py` | spacing from `zetazero`, normalized by local density $\ln(t/2\pi)/2\pi$ |
| Variance split (§XIII) | inline | $400$ heights in $[10^4, 1.2\cdot10^4]$; $\log\lvert P_X\rvert$ as the unsmoothed prime-power sum up to $X$; the zeros' column is the difference, valid as their share to the degree the factors decouple |
| Elliptic curves (§XIV) | inline | point counts over $\mathbb{F}_p$, $5 \le p \le 2000$, by quadratic-residue tally |
| Slope and pitch (§XVI) | inline | $w = 1 - 1/s$ in double precision; pitch $= -\ln\lvert w\rvert/\arg w$ |
| Record gaps (R.16) | `gaps.py` | segmented NumPy sieve to $10^9$ |

---

# Part I. The Build, in Order

Each step is described by what changed. Most of the missteps along the way share one shape, and the shape is named where it recurs: a **K₃ expectation**, a reading taken from one face of the tetrahedron and expected to hold for the volume (a second coordinate smuggled in, an outside vantage reached for when a face already supplies it, a budget imposed on a self-balanced object, a completed-set semantics imposed on a run).

**1. The original and its rebuild (v1 → v2).** An address-by-address review found one hard error ($P = I^2R$ off by a factor of two, with $R$ seated at $\vartheta'$), one category error (the off-line zero at the first Lehmer pair belonged to the truncated approximant $F_{33}$, not to $\zeta$), and one self-contradiction ($\Psi(p)$ called load-bearing while being the leading term of an asymptotic expansion). The rebuild carried the balance through Li's map, where the Mutable collapse is reflection in the unit circle and the unselected square is $4\sin^2(n\varphi/2)$; re-read the Lehmer vignette as a resolution test whose verdict flips with $N$; tied zero margin to $\Lambda = 0$ through Rodgers–Tao; and re-seated $R = \ln(t/2\pi e)$, after which $P = I^2R$ holds exactly.

**2. External runs and the witness discipline.** A second instance ran the two pre-registered questions and reported both negative; recomputation agreed, added four close pairs the witness had missed, and corrected its $\lambda_n$ value. Its claim that three pillars of number theory instantiate K₄ "without parameter fitting" was refused: the seatings were chosen, and any $V_4$ orbit fits a two-bit labelling. The 126-pair scan showed heat order carrying no information about truncation loss at low height (correlation $0.465$), a result that later reversed with height.

**3. The push to height.** The scan reached $10^{12}$. Five numerical faults surfaced, none raising an error (a float64 $2\pi$, rounded offsets, a truncated $\vartheta$ expansion, a clamped singularity in $\Psi(p)$ manufacturing spurious pairs, a tail integral returning zero), each caught by a count or a known value. With height, truncation's ranking converged to heat's; the gate became a rate, loss $\propto t^{-3/8}$, heuristic on GUE.

**4. The positive stance and v3.** The file turned from what RH is not to what K₄ shows about it: the forced lift, the three schools as three bimedians, RH as losslessness. A witness bet put the shifted plug's first negative Li coefficient below $n = 800$; computation gave $n = 8{,}260$, and the onset law $n^* \approx (\gamma^2/\delta)\ln A(n^*)$ replaced the bet. A flinch audit cut six scope disavowals to one. The orbit generator, first dropped because the corpus lacked it, was verified and reinstated (provenance is not a verdict). A full-corpus review closed two gaps by computation: one of $24$ seatings satisfies the count, and the third plug $L(s,\chi_5)$ shrinks the walls' deficit to $n \le 2$ and closes it at conductor $23$.

**5. The split and the texture.** v3 was split into thesis, hub and ledger. An audit then withdrew the reading of the primes as "a continuous texture" upstream of the ledger; the withdrawal overreached by declaring the model's domain to end at the line. The operator's correction ("the primes have to pay a price for being") turned that limit into the price: at the line the price $\sum1/p$ turns marginal and the texture becomes a real second moment. The question opened for it was removed as answered.

**6. Landscape and scale.** On the operator's pointer to `On_HilbertAndHisSpaces`, the landscape was named: inside $\tfrac12$ a vector, at the edge a ray, across a power divergence. Two framings were caught as restatements ("every orbit pinned to its mirror" re-expressed the hypothesis) and as imported semantics ("everywhere against almost everywhere" applied measure language to one deterministic line). Scale replaced measure, and `BENDING_SPACE` supplied the realizations (the square nothing screens, the box of light, Laue's two integrands, the horizon). A proposed three-tiers subsection was the least needed element and was left unwritten.

**7. Underbellies and regime.** The two-way inference against the BENDING draft found one circular forcing: the Hilbert structure derived from "orthogonal additivity", the inner product under another name. Herschel–Maxwell repaired it: a valuation additive over Re ⊥ Im and blind to phase is $\lambda|a|^2$. Three draft realizations were marked as restatements. Every "conditional on RH" verdict was relabelled by regime: unconditional below the transfer scale of the verified height, conditional above.

**8. The free head, the braid, and the path.** The operator asked whether $dt = 0$, mass $= 0$, binding $= 0$ were legal engine operations; Star-Norm conservation forces the free $P$-head, and a free write marks a ray. A first repour walked the machinery as one path with the zeros as "free commits". Read as a transfer-function meta-frame with `L5-TheCyclingMind`, `L5-K5`, `L6`, the braid holds the Mutable bimedian and commits only the count, so the zeros are held, not committed. The impulse response, the callbacks, the blank patches as held families (record gaps to $10^9$), and averaging blindness as the third stuckness landed. Thesis, hub and ledger were burned into the path with Appendices A–D.

**9. The N-body construction and its audit.** A second line of construction (the author's I-series) brought the prime cavity, the resonant seam $\ln n = \vartheta'(t)$, Rayleigh reciprocity $T = 2\pi N^2$, Laue compensation on the Book, the trivial zeros as start-up transients, and the Immovable Three on the $U$-absent face. All its numbers reproduced. Its corrections:
* free space read as pure reactance (it is a lossless resistive traveling-wave medium, `L4-ThePlenum` §0);
* the cavity's "sieve to 49" (a confound; the cutoff is Rayleigh, and $53, 59, 61$ light past $49$);
* loop gain $a_p/\sqrt{p}$ as solvency ($\zeta(s)^2$ reads $1.414$ with zeros intact; the price line separates the plugs);
* $P$ seated as the committed ledger and $\omega$ as a pole (the corpus seats $P$ as the Pen, $R$ as the Book, $I$ as the plenum current, $\omega$ at the hub);
* an off-line zero as a "hardware break" (the $P$-edges stay free; it is a booked closure of the Book's own punches);
* Foster on `P–R` (it sits on `I–U` with the Smith chart; the reseeds sit on `P–R`).

With the roles corrected, the explicit formula reads as held on the diagonal and walked around in two live steps, and `AQU` takes its seat as the tank resistance.

**10. The vertex-to-role map and the circuit.** Pushed, the map resolved into three layers: pairs forced by the square, the active side forced twice, orientation fixed where the engine meets $H_{\text{coh}}$ (the operator's addition), concretely at the seam $d\Phi_n/dt = \ln(I/n)$, with the walls turning forward at $t = 6.29 \approx 2\pi$ where $n = 1$ enters. For complex $\chi$ only $cf$ stays inside a plug, and the braid alternates plug and dual. The per-orbit circuit was derived symbolically: conjugate pairs are tanks, Mutable pairs exchange a quantum of exactly $\pi$ for every $\delta$, and $Q = \sqrt{\gamma^2+\delta^2}/2\delta$ turns the onset law into $n^* \approx 2\gamma Q\ln A$.

**11. Could it be otherwise.** The operator replaced "is it proved" with "could it be otherwise". A three-channel exhaustion overclaimed: its Leverage row was idle (an off-line zero needs nothing at the interface's $cf$), its tail argument was averaging blindness again (Bohr–Jessen is a statement about time-averages), and its premise imported a power budget onto an orbit that balances on the line. What survived: no second exact alignment, and every known off-line example removes one intact-plug condition. The operator's sorting of finished against never-finishing infinities typed the questions: RH is $\Pi^0_1$ with finished counterexamples; a double zero is never-finishing. The primes, finished as a law and unfinished as an extension, compound through the square. The seam gate was computed (§XII): zero losses with $C_0$, the $3/2$ law measured, the loss exponent tied to the stiffness.

**12. The plane found.** Asked to narrate down to the stuck question, the drafting side found the unspoken assumption: treating $\sigma$ as a place. On the shaft there are ticks and crossings; Davenport–Heilbronn shows an off-line pair as a permanent debt of two quanta; RH with simplicity is one quantum per height. A witness relocated the multiplicative/additive break onto $\psi$; it sits on the identity $\sum n^{-s} = \prod(1-p^{-s})^{-1}$, and the window is a size cut through the multiplicative monoid. The product holds the background (Gonek–Hughes–Keating), never the crossings.

**13. Vantage and hub.** $p + 1$ read as the pre-closure; the local Frobenius trichotomy matched the orbit's three regimes. The drafting side reached outside K₄ for Weil's surface and Deligne's family; the operator pointed back inside: the $P$-absent face is the Ohm plane, the siblings are the family, $Q = \infty$ without $P$, and the write-only Book supplies the sign. The Sudoku's hub seated the rotation; the `L4-Riemann` series' screw-and-circle located the hub at $s = \tfrac12$ and turned the zero's slope into its rotor's pitch: RH as torsion-freeness of the zero rotors.

**14. The render.** The Realization was rendered as one standing text (§0–§XVII), carrying the I-series architecture, the path's walk, and the continuation through the hub and the pitch. The path's Appendix A became Part 0's reference tables, its Appendix B became R.17, the atlas and the questions folded into the text where they bear. The Inventory collects the pieces by register. Thesis, hub, ledger, path, v2 and v3 retire to the record of Part IV.

---

# Part II. The Withdrawals, by Kind

### Numerical and scope errors

| Claim | Why withdrawn | Now |
|---|---|---|
| $P = I^2R$ with $R = \vartheta'$ | factor 2 against Riemann–von Mangoldt | $R = \ln(t/2\pi e)$; exact (§VII) |
| $\Psi(p)$ "load-bearing, not asymptotic noise" | leading term of an asymptotic expansion | sizes stated (§IV) |
| $\lvert Z_{\text{peak}}\rvert \ll \lvert C_0\rvert$ persists at height | median ratio $0.32$ low, $28$ at $10^{12}$ | the gate as a rate (R.6; §XII) |
| $S_0$ "between $0.59$ and $3.7$ at every sampled $n$" | about ten samples | dense range $[-20.9, +23.2]$ (R.3) |
| Shifted plug's Li onset below $n = 800$ (witness bet) | first negative at $n = 8{,}260$ | the onset law (R.8) |
| "Conductor $q \ge 4$ keeps the walls positive" | omitted the $-1$ from the absent factor $s$ | $q \ge 23$ (R.4) |
| Lehmer spacing $0.021$ (witness) | $0.042$ mean spacings | corrected (R.2) |
| "Every zero's tape is aperiodic, by Niven" | Niven needs a rational cosine | closed as non-load-bearing |
| Orbit volume $\propto \delta^2t^2$ as rent diverging with height | coordinate effect | height-free $\tfrac83\delta^3$ (§IX) |
| An off-line pair winds $2\pi$ on every slice between line and zero (witness) | slices between the partners wind zero | the jump sits at $\sigma = \beta$, $1-\beta$ (§II; §XVI) |

### Readings that failed against the identities under them

| Claim | Why withdrawn | Now |
|---|---|---|
| Primes as "a continuous texture"; "frequencies, not locations"; "the spectrum is upstream" | the primes are discrete; the explicit formula is an identity between two readings | the Bohr torus as scaffolding; two Fourier-dual readings (§VI) |
| "The plug supplies the texture"; RH "decided by incommensurability" | broken plugs share the frequencies and the delays | the plug is the weights, the pole, the Γ-factor (§VII) |
| Euler factors marginal on the stability boundary | poles at $\mathrm{Re}\,s' = -\tfrac12$, damped | damped combs (§VII) |
| Basins of $g$: $\mathrm{Re}\,s > \tfrac12 \to 0$ | reversed | $\mathrm{Re}\,s > \tfrac12 \to s = 1$ (§VI) |
| $f$ as parity, $cf$ as time in the generator | PT is the $cf$ condition; $f$ is chiral | corrected (R.17) |
| Free space as pure reactance (I-series) | $Z_0$ is real: lossless and resistive | resistive substrate, reactive tanks (§0) |
| The cavity "sieves to 49" | $53, 59, 61$ light; the cutoff is Rayleigh | §I finding 3 |
| Loop gain $a_p/\sqrt{p} > 1$ as active self-oscillation | $\zeta(s)^2$ reads $1.414$ with $\zeta$'s zeros | the price line (§V) |
| Off-line zero as a hardware break | $P$-edges stay free in every case | a booked closure of the Book's punches (§II) |
| The multiplicative/additive break sits on $\psi$ | $\psi$ sits downstream of log | the break is the Dirichlet-series/Euler-product identity; the window is a size cut (§XIII) |
| "The Book writes" | the primes write through the Pen; the Book records | Pen writes, Book records (§II) |

### Restatements and circularities

| Claim | Why withdrawn | Now |
|---|---|---|
| "RH says every orbit is pinned to its mirror" as insight | the hypothesis in new coordinates | marked as restatement |
| Hilbert structure forced by "orthogonal additivity" | the premise is the inner product | Herschel–Maxwell (§0) |
| Three BENDING-draft realizations | each restated its conclusion | marked as restatements |
| "The sieve never phase-locks" as a reason | von Koch's form of RH in corpus words | an address, not a reason (§XI) |
| The Leverage row of the exhaustion | idle: an off-line zero needs nothing through it | dropped (§XVII) |

### K₃ expectations

| Claim | The face it was read from | Now |
|---|---|---|
| "The torus picture stops at the line; the domain ends there" | the phase face, without the price | the price turns marginal at the line (§VII) |
| A three-tiers subsection as BENDING's yield | the scale face, without the realizations | the realizations (§VI–§VIII) |
| "Everywhere against almost everywhere"; Bohr–Jessen as pointwise exclusion | the completed-set face | scale and run (§XI) |
| An off-line orbit needs a power supplier | the budget face, on a self-balanced object | balanced on the line; a booked closure (§II) |
| $\sigma$ as a place where zeros could be | the plane, a second coordinate | the price exponent; the shaft carries ticks and crossings (§X) |
| $P$ as the committed ledger, $I$ as the aperture | the attachment's own labels | Pen, plenum current, Book (`L4-ThePlenum` §II.5) |
| An external surface and family for the sign | outside the tetrahedron | the $P$-absent face and the siblings (§XIV) |
| $H$ dropped because the corpus lacked it | provenance as verdict | verified, R.17 |

### Superseded structures

| Structure | Now |
|---|---|
| v2, v3, thesis/hub/ledger, the path with Appendices A–D | the Realization (§0–§XVII), Part 0's tables, the Inventory |
| The zero as "a commit that costs nothing" | held potential on the silent bimedian (§VI) |
| The thesis question on what carries the prime weights | answered by the price (§VII) |
| The question set Q1–Q14 | one question in four registers (§XVI) |

---

# Part III. Patterns

**1. A screen's count is not a census.** *Guard:* every screen gets an independent completeness count.

**2. Reading a sign against the wrong reference.** *Guard:* test "same sign as the true extremum", never "positive".

**3. Grading a result against one's own conjecture.** *Guard:* state what the test found in its own terms before comparing.

**4. A restatement sized as a discovery.** *Guard:* derive a 100% rule before landing it; the computation adds the range.

**5. A witness's correct conclusions do not license its framing.** *Guard:* evaluate conclusions and premises separately (`L4-Riemann-evolution` pattern 21).

**6. A prediction made from the regime it was meant to leave.** *Guard:* argue a scaling prediction from the scalings.

**7. A sparse sample reported as a range.** *Guard:* report a range only from a dense computation.

**8. Silent numerical failure at scale.** *Guard:* at every new scale, re-establish one count and one known value first.

**9. Provenance taken for a verdict.** *Guard:* keep unverified material labelled, then verify; absence from the corpus is a reason to check.

**10. A swing mistaken for a correction.** *Guard:* when resizing a claim, state what survives on each side.

**11. A shift transferred without its companion term.** *Guard:* compute a new plug's split once before generalizing.

**12. A theorem cited past its hypotheses.** *Guard:* read the hypothesis first.

**13. An instrument whose target has been settled.** *Guard:* check whether the target has since closed.

**14. A coordinate artefact read as a law.** *Guard:* find the combination independent of the coordinate.

**15. Insulation repeated as scope.** *Guard:* state the scope once.

**16. A reading tag taken as a pass.** *Guard:* a reading ships only if it survives the identities under it.

**17. Overcorrection by borrowed framing.** *Guard:* ask what survives on the corrected mathematics before accepting the critique's account of what is left.

**18. A restatement dressed as a reason.** *Guard:* ask whether the sentence holds content if RH were false.

**19. A semantics imported onto an object it cannot see.** *Guard:* ask which tool detects the difference and whether the object is visible to it.

**20. A forcing premise that is the conclusion's axiom.** *Guard:* state the premise without the structure it forces.

**21. A verdict without its regime.** *Guard:* name the transfer function and the scale verification has discharged.

**22. A free operation booked as a commit.** *Guard:* check which edge an operation writes on and which ring is running.

**23. A seating copied from a source's label.** The attachment called $P$ the committed ledger and the audit argued against that label instead of the corpus's. *Guard:* check every role against the constitutive table (`L4-ThePlenum` §II.5) before reasoning from it.

**24. A budget imposed on a self-balanced object.** The exhaustion went looking for a supplier the orbit never needed. *Guard:* before naming a supplier, check whether the object balances on its own.

**25. A second coordinate smuggled in.** $\sigma$ was handled as a place, and the questions multiplied in the plane. *Guard:* name what the run carries before adding a coordinate to it.

**26. A tool of the wrong logical type.** Completed-limit theorems were aimed at a never-halting run. *Guard:* sort a question by its counterexample, finished or never-finishing, before choosing the tool.

**27. An outside vantage reached for while a face supplies it.** Weil's surface and Deligne's family were imported while the $P$-absent face and the siblings sat in the figure. *Guard:* before importing a vantage, check the four faces.

Patterns 17, 19 and 23–27 are one family: a K₃ expectation, a single face's reading carried to the volume.

---

# Part IV. Address Maps

**v3 → set.** v3 §1–§12 → thesis §1–§12; v3 §13 settled → ledger §6–§9, open → thesis §11 and ledger §12; v3 §14.1–§14.5 → hub §1, §3–§6; §14.6 → hub §8; §14.7 → hub §10; §14.8 → hub §11; §15 → thesis §13 and ledger §11.

**set → path.** Thesis §0 → path §2, §14; §1 → §14; §2 → §6; §3 → §0, §7, §8; §4 → §3; §5 → §10; §6–§7 → §12; §8 → §14; §9 → §6; §10 → §6, §13; §11–§12 → §14; §13 → App. D. Hub §1–§2 → §1; §3–§4, §6 → §3; §5, §11 → App. C; §7 → §2; §8 → §7; §9 → §0; §10 → App. B; §12 → C.12. Ledger §n → A.n.

**path → Realization.** Path §0–§2 → §0 and §VI (helix); §3 → §II; §4–§5 → §VI; §6–§8 → §VII; §9–§10 → §VI; §11 → §VIII; §12–§13 → §IX; §14 and the Register → §XVII. Appendix A.n → R.n; Appendix B → R.17; C.12 → §0 and R.15; Appendix D → §X–§XVI.

**I-series → Realization.** I-series §0–§V → §0–§V; its open-landscape section → §X–§XV.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work. Read `L4-Riemann-Realization` for the standing claims.

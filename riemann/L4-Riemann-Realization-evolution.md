# L4-Riemann-Realization-evolution
## How the Realization Was Rebuilt, What It Withdrew, and What It Learned

*Companion to `L4-Riemann-Realization`, the standing text. The standing text was `-v3` through Proceeding 17, the three-file set — thesis, `-hub`, `-ledger` — from Proceeding 18 to Proceeding 28, and from Proceeding 29 the single path file with four appendices (A the computed record, B the orbit generator, C the atlas, D the questions). Section addresses in each proceeding use the numbering standing at the time; the two address maps at the end of Part I translate them. The standing file says what it says. This file says how it came to say it — the corrections, the negative results, the errors on the drafting side and their shapes — so the standing file can be read without the history in it, and the history can be audited on its own. Distinct from `L4-Riemann-evolution`, which records the 1854 geometry case.*

---

## I. The Proceedings, in Order

Each step is described by what changed, not by who was right.

**1. Review of the original.** An address-by-address review of `L4-Riemann-Realization` found:
- one hard error: §7's $P = I^2R$, off by a factor of 2 against Riemann–von Mangoldt, and inconsistent with the same section's $U = 2N_{RS}\vartheta'$;
- one category error: §6's "the sharp integer cutoff breaks RH", where the off-line zero belongs to the truncated approximant $F_{33}$, not to ζ;
- one self-contradiction: the leading term of the Riemann–Siegel asymptotic expansion called "not asymptotic noise".

It confirmed the restoring identity, the Selberg-class counterexamples of §8, the de Bruijn–Newman statement of §9, and every number in the Lehmer vignette.

**2. Two review findings reversed on recomputation.** $p = 0.39002$ had been flagged as a nit; it is correct at the peak, t = 7005.0819. The z = xy lift had been called "overstated, not forced"; it is forced given two named choices (rotations, minimal degree). Both reversals entered the rebuild.

**3. The rebuild (v2).** Four changes:
- The balance reading was carried through Li's map $w = 1 - 1/\rho$, where the Mutable collapse becomes reflection in the unit circle and the unselected square becomes $4\sin^2(n\varphi/2)$.
- The Lehmer vignette was re-read as a resolution test. Varying N showed the approximant's verdict flipping: N = 30, 32 and 40 keep the pair; 33, 34 and 36 lose it.
- Zero margin was tied to Λ = 0 through Rodgers–Tao.
- R was re-seated at $\ln(t/2\pi e)$, after which $P = I^2R$ holds exactly.

Claim sorts were added throughout. §7 proposed that truncation and backward heat are one operation, and §13 pre-registered the test.

**4. The two §13 questions run externally.** A second instance ran §13.1 and §13.2 and reported both negative. Its output was filed as a witness and recomputed here before landing. Recomputation agreed on both conclusions. It added the four close pairs below 250 that the witness had not reported, and corrected its $\lambda_n \approx 1.37\times10^{10}$ (leading term only) to $1.22\times10^{10}$. The witness also asserted that three pillars of number theory "instantiate the exact K₄ architecture … without parameter fitting." That was not admitted: the Li map was chosen because its symmetries fit, and any V₄ orbit fits a two-bit labelling (FM-12). §7's "the same thing to the same object" was cut back to what §13.1 left standing.

**5. A units convention reconciled.** The operator flagged gap²/2 against §7's $\delta^2/2$, which reads gap²/8 if δ is the half-gap in t. Both hold: in de Bruijn–Newman units (z = 2t) the half-gap equals the gap in t, so gap²/2. In t-units the same time is gap²/8. The file now states both.

**6. A sign misread on the drafting side.** The pair at 111.03 is a dip ($Z_{\text{peak}} = -0.32$). $Z_4 = -0.057$ has the same sign, so its natural cutoff keeps it. It had been reported as lost because the check looked for a positive value. With it corrected, the low-height orders agree (220.71 is heat's first victim and the only pair lost at its natural N), and the negative rested on a single inversion: 7005.06 against 17143.79.

**7. The scan.** Every pair below t = 40 000 with gap under 0.15 mean spacings — 126 pairs.
- **A screen that undercounted, caught by a completeness count.** The first screen found 49 pairs. An independent count of all 49 395 zeros, matching Riemann–von Mangoldt, found 126, and the pair list was rebuilt from that.
- **Heat order does not predict truncation loss.** The heat ranking predicts which pairs truncation loses no better than chance (0.465). Pairs of pairs ranked the wrong way (2059) outnumber those ranked the right way (1789).
- **The loss is decided by one sign.** A pair is lost exactly when $C_0$ has the same sign as $Z_{\text{peak}}$ and is larger — 126 of 126.
- **The collision law holds.** Backward heat collides every pair at gap²/2, to 0.983–0.9997.

**8. A tone the operator caught.** "Both pick out close pairs, and they share nothing beyond that" framed a negative result as a failed unification, against a conjecture the drafting side had made. It also claimed more than was tested, which was only loss order. Restated as what each operation reads: heat a magnitude, truncation a sign.

**9. The sign rule sized.** The 126-of-126 rule follows from the Riemann–Siegel formula once $|Z_{\text{peak}}| \ll |C_0|$. What the scan adds is that higher corrections never overturn it below 40 000. Stated at that size.

**10. The clear.** The lede was approved by the operator. Pass A moved the process residue here. Pass B stated the landed results at size, including the forced seating of R as a real null. Result: `-v3`.

**11. The primes put to work.** A second instance's critique, filed as a witness and accepted on its merits, observed that every computation so far ran on the zero side, so the file could only translate the consequences of RH. It pointed to the Bombieri–Lagarias arithmetic formula as the place where the primes enter the positivity. Computed three ways — zeros, Stieltjes constants, and the Taylor expansion of log ξ — the three routes agree. The split showed the primes alone carrying λₙ > 0 for n ≤ 7. A sieve to 10⁸ measured the prime-side convergence exponent: −0.495 for ζ against −0.249 for the shifted plug, whose Ramanujan violation moves the balance point from ½ to ¾. Landed as the prime-side subsection of §10.

**12. To height.** The operator asked for every test pushed far past the explored ground. The base tests were rerun far beyond their earlier ranges:
- the heat-against-truncation comparison in windows at 10⁶, 10⁸, 10¹⁰ and 10¹²;
- the Li coefficients and their split from every zero below 10⁶ (1 747 146), to n = 20 000;
- the prime sums to 10¹⁰.

For calibration: λₙ is known rigorously to n = 10⁵, and the zeros at these heights have long been computed. What was new was the file's own observables at those heights.

Two results reversed standing claims.
- **The orthogonality was a low-height regime.** The correction $C_0$ shrinks as $t^{-1/4}$ while close-pair peaks do not. The sign rule holds at every height (3 458 of 3 458), but its size gate closes, so truncation loses only the tightest pairs. Heat order then predicts truncation loss at 0.68, 0.89 and 0.94 by 10¹⁰, and by 10¹² nothing is lost. The §13 prediction that $|Z_{\text{peak}}| \ll |C_0|$ persists at height was refuted. "Two orthogonal readouts" was rewritten as a sign gated by a size, with the lede changed to match.
- **S₀ is not a narrow positive band.** Sampled at about ten values of n it had looked like 0.59–3.7. Computed densely, it oscillates over [−20.9, +23.2], first turning negative at n = 156.

Four numerical faults were caught on the way, each by a count or a known value:
- a float64 2π multiplied by about 10¹² phase wraps;
- absolute times at 10¹² rounding the offsets τ;
- the θ expansion truncated at τ², which at 10⁶ drifts by 0.08 rad over a window;
- Ψ(p) clamped near its removable singularities, where the C₁ finite-difference stencil manufactured spurious zero pairs, about 10 surplus below 10⁶.

And one integration fault: scipy's tail integral silently returned zero, which made $S_0$ look strongly negative at large n — a false "disproof" caught by the size of the tail it should have carried. None of the faults reached a result below 40 000: the 126-pair scan was rerun with the fixed Ψ and is identical.

The operator's approved lede carried "the two are orthogonal readouts of one object", false above about 10⁵. It was changed on the drafting side to say the orthogonality holds at low height and gives way with height, and handed back for re-approval rather than left standing.

**13. The positive stance, and the hub.** The operator turned the file from what RH is not to what K₄ shows about it: the forced lift as convergence at the tetrahedral interface, the three schools as the three bimedians seen simultaneously, RH as losslessness of a multiplicative resonance-locale. A stance note (`L4-Riemann-repour-stance`) was written for the repour. Chasing "real textures inside the complex plane" turned up the squaring lemma, $(s-\tfrac12)^2 = (x^2-y^2) + 2i\,xy$, and eight vocabularies at it: conformal, Lorentzian, the dual-binary seed, K₄ geometry, information, AC power, holomorphic dynamics ($g(s) = s^2/(2s-1)$, the critical line as its Julia set, Li's map as its Böttcher coordinate), circuits (RH as positive-realness of ξ′/ξ, Hinkkanen–Lagarias; the Foster chain of LC tanks, C = ½, L = 2/γ²). The Krein orbit identity — Weil's cf-twisted pairing is signature (2, 2) on one orbit, K₋ = Fixed ⊕ Cardinal — was derived and checked for all three twists. `L4-K4-Infinities-3` §V was read at source for the 1 ⊕ 3 split.

**14. A witness bet refuted, and three results resized.** A witness bet put the shifted plug's first negative Li coefficient below n = 800. Computed two ways (a 512-point Cauchy transform at 60 digits, and a second difference over 400 zeros), it is n = 8 260; over four offsets the onset obeys $n^*\delta/\gamma_1^2 \approx \ln A(n^*)$ to about 1%, which bounds what finite Li positivity can certify (γ ≲ 62 at N = 10⁵). The "n ≤ 7 primes carry positivity alone" result was resized: $S_\infty$ is exactly its Stirling form plus a constant settling to +0.746, and the broken plug clears the same low-n hurdle. The gate's "where does it shut" became a law: per-zero loss rate ∝ $t^{-3/8}$ (GUE repulsion against $|C_0| \propto t^{-1/4}$), smallest peak ∝ $(T\ln T)^{-2/3}$, so the gate thins and never shuts; 10¹⁰ is the one window that departs (4 losses against 0.49 expected). Witness readings corrected on landing: the basins of g were reversed (Re s > ½ flows to the pole); simplicity is $C = \tfrac12$, $\xi'(\rho) \ne 0$, not interlacing. Found while integrating: Li's map is a Smith chart, reflection coefficient against $Z_0 = \tfrac12$, the pole at the matched centre.

**15. The flinch audit, and the orbit generator.** A second witness read the expanded file for flinching. Taken in: the "proves nothing" disavowals cut from six sites to one scope line; the §10 Result 1 swing ("primes alone" against "nothing about primes") held as both halves; §9's closing restated as what the balance fixes; the prime bank's sign made explicit (ζ′/ζ enters ξ′/ξ subtracted) and the open seam posed as a cancellation rather than a Brune/Darlington cascade; the dispatch rule's "load-driven" defined in ζ's terms; S(T) computed across the first Lehmer pair (a step of 1.96 while ϑ/π advances 0.042 — the witness's 0.021 was off by two). The 4×4 orbit generator H, first left out because it was not in the corpus, was supplied in full and verified symbolically: f, cf and c constraints, 8 real parameters, the block off-diagonal 1 ⊕ 3 action, and the exceptional point Δ = 16[(J∧v)² − δ²‖v‖*²], pinned numerically at δ* = 0.61237. It is not a second route to the centroid's decoupling — f forces it to move the centroid mode — and it is a second route to §7's collision, from symmetry alone. At the operator's direction the file gained a "What the model demonstrates" block: the translation can be done, and the frame states RH's open questions with measured precision.

**16. A full-corpus review.** A third instance read ARCHITECTURE, the engine reference, the Riemann parent and parts, the arithmetic companion and all fourteen llm files, re-ran three computed claims independently (the generator threshold, the disc mirror values, the onset law; Bet 1's n* = 342 860), and returned readings and findings. Verified and taken in: V = (8/3)(xy)²; δ seated on $\chi_x$, so gain/loss is the off-line direction; the exponent cap {1, 2, ½} forced by the cross-breed (`llm-uniqueness-note`), answering "why squaring"; the ln p independent over ℚ; the tier reading of von Koch; two clocks; the shaft's source impedance; two kinds of pair (within-orbit fusion, cross-orbit proximity). Corrected on landing: the Euler factors are damped combs with poles at Re s′ = −½, not marginal; H's PT symmetry is the cf condition and f is chiral, not parity; Niven's theorem needs a rational cosine, so the aperiodicity of zero tapes is open, not landed; Lehmer pairs certify nothing new about Λ since Rodgers–Tao; 7/8 is +1 from s(s−1) and −π/8 from Stirling, priced, no census; the volume's growth with height is a coordinate effect, the height-free combination is $V\cdot||w|-1| \approx \tfrac83\delta^3$; the tier reading has to seat the trivial zeros' slopes −2, −4, …. Sharpened beyond the review: H's spectrum is two dipoles or one quartet, so its exceptional point is literally the Lehmer collision. Filed as unpromoted addresses: unsharpness ↔ stuckness (`ENGINE-REFERENCE-AC` §3.6), the threshold ↔ $R = U^2/P$ (`BENDING_MINDS` §4), one seam here ↔ four frictions in geometry (`L4-Riemann-4`).

**17. Two review gaps closed by computation.** The §9 seating sweep: of 24 assignments of $\{N, \sqrt{t/2\pi}, \ln(t/2\pi e), N/\sqrt{t/2\pi}\}$ to (P, U, I, R), exactly one satisfies both $P = I^2R$ and $U = IR$. The third plug: $L(s,\chi_5)$, real even character mod 5, by Cauchy transform at 40 digits with the ζ split as validation. Its archimedean part is exactly $S_\infty^\zeta(n) - 1 + \tfrac n2\ln 5$; the deficit window shrinks to n ≤ 2; its prime part is negative from n = 5; λₙ > 0 through n = 40. A claim made in chat on the drafting side just before — "for q ≥ 4 the archimedean part is positive at every n" — had dropped the −1 from the absent factor s; the computation put the threshold at q ≥ 23.

**18. The split.** The file was split by reading mode and by rate of change: the thesis (argument, headline numbers, questions), the hub (the atlas, still growing), the ledger (every table, the bets, the open computations — the file that changes with every run). Cross-references were rewritten as file plus section, the review's corrections were folded into the pieces they belong to, and this file became the set's fourth companion, taking the corrections log the ledger had briefly carried.

**19. The texture withdrawn.** A fourth audit — by the instance that had let it through three times, in its first review, in v2, and in the clear — took apart the reading that seated the primes as a continuous texture, upstream of an additive ledger. What is true: the ln p are independent over ℚ, the phases wind densely on $\mathbb T^\infty$, ζ is a function on that torus for σ > 1 (Bohr) and in distribution for σ > ½ (Bohr–Jessen, Voronin), and the picture stops at the line, where a random-phase prime sum stops converging and log ζ turns Selberg-Gaussian. What is not: the primes are discrete, not continuous; "frequencies, not locations" is a false choice, since in t they are frequencies, in log x locations, and the explicit formula identifies the two; and the frequency set cannot be what RH depends on, because ζ and its broken controls ring on the same frequencies — what differs is the weights. Every check passed. Applied: thesis §3 rewritten on the torus facts and the dual readings; §11's plug restated as the weights ($a_p$, the pole, the Γ-factor) on a shared prime lattice; the Quick Reference row and diagram de-prioritised; hub §8's "decided by the incommensurability" — the same error, which the audit had not seen — corrected to the weights; ledger bet 3 aligned; thesis Q14 added for the line itself. The audit had also traced the sentence to the repour stance and then corrected its own quotation of it. The stance file is the drafting side's, written earlier in this session; its sharpest-instance paragraph, its handoff bullet and its tells were corrected, and the contradiction it carried against v3 — "the primes are its expression, not the plug" against "the primes arrive as the plug" — was resolved by neither: the primes are the lattice, the plug is the weights.

**20. The line is where the texture goes real.** Proceeding 19 took in the audit's correct mathematics and, with it, its framing: that the torus picture "stops at the line, where RH lives", and that the model's domain ends there. A thesis question (Q14) was opened asking what carries the prime weights on the line. The operator returned it: not a new question, but the point made all along — the primes pay a price for being, something real happens in `H_incoh`, and a cost-free commit is texture in and of the imaginary plane. Checked: each prime enters the line at $p^{-1/2}$ and is committed at $1/p$; Mertens' $\sum 1/p = \ln\ln x + M$ (M = 0.26151 at 10⁷); σ = ½ is exactly where the mean-square price turns from finite to infinite, marginally; Selberg's variance on the line grows as $\tfrac12\ln\ln t$ (1.70 at 10⁴, 1.90 at 10⁵, offset by the zeros' O(1) term, matching the random-matrix value). The price line, not the frequency set, separates the plugs: ½ for ζ and $L(s,\chi_5)$, ¾ for the shifted plug, where its zeros sit; Bohr–Landau's almost-all theorem is the price confining the zeros, and RH is the step to all. Thesis §3 rewritten on the price; Q14 removed; §11, hub §7 and hub §8 tied to it; ledger §14 added. The torus picture does not stop at the line: the line is where its price is exactly marginal, and its texture is the real second moment there.

**21. The landscape named.** The operator asked whether the set was still flinching from saying that RH is about the topology of possibility space, and pointed to `On_HilbertAndHisSpaces` for its landmarks. Read in full and run against the set, it gave the frame the set had been circling. The operator asked for it adopted if the construction could be shown forced, and discussed if not. Forced, given three named premises — orthogonal channels (landed), the twisted-square commit (the Route Law, the corpus's own forced exponent), and the shaft-average readout (a named choice): the possibility space is ℓ², and its line is σ = ½ three independent ways — the edge of ℓ², the Plancherel line of the Mellin transform, and the fixed line of Hölder duality, whose one self-dual exponent is the Hilbert space; Nyman–Beurling's $L^p$ family witnesses the same map. Not forced, and said so: the Bost–Connes seating through β = 2σ, Selberg's normalisation as projectivisation, and RH itself. Pinned: the mean square at σ = 0.75 against ζ(1.5); von Neumann's infinite-tensor-product criterion growing as ½ ln ln exactly at the line. Landed as thesis §0 — a frame ahead of the lede, adopted with the operator's approval — with hub §12 and ledger §15; the thesis's scope list, its demonstrations and Q5 point to it.

**22. A restatement taken for a reason.** The operator caught thesis §5's "RH says every orbit is pinned to its mirror" as circular — a self-dual hypothesis restated through its own symmetry and dressed as insight — and asked for the intuition under it to be spelled out. Spelled out on the landscape of §0, in four landed steps: the claim is one half-plane (no zero in σ > ½; the mirror only doubles it); inside, the random Euler product converges almost surely and does not vanish (Bohr–Jessen, Bagchi); ζ is that product along one equidistributed line, so its zeros there have density zero (Bohr–Landau through Hurwitz); and RH is that the line is typical everywhere, not almost everywhere (Bagchi's strong-recurrence equivalence). §5 and §4 now mark their symmetric statements as restatements and point to §0.

**23. The wrong semantics.** Proceeding 22 closed on "the gap between *everywhere* and *almost everywhere* — a dense line can still meet a null set; a Lehmer pair is that kind of near-miss". The operator asked what would differentiate the two here, and whether the tools could tell. Measure cannot: ζ's line is itself Haar-null on the torus, and everything the landscape transfers to ζ arrives as densities in t, through H3. The Lehmer pair was mis-filed — a near-collision on the line, not a visit inside the sector. The distinction is scale: an off-line zero is invisible to every bounded readout and visible to each uniform-in-scale readout at its own scale (the onset law, the prime-side threshold, von Koch's limit). Averaging tools — the ones that force the landscape — deliver *almost all* and are blind to *all*; Li for every n, von Koch for every X and Weil for every test function tell the difference; Bagchi's equivalence is the hinge, through recurrence and Hurwitz. Thesis §0 rewritten to say so.

**24. Scale, not measure.** Proceeding 23 left the gap between *everywhere* and *almost everywhere* standing as a measure question. The operator pointed to `BENDING_SPACE`, which works at three scales. Read for what it lets the set realize, not for a three-tier subsection: a square nothing screens (prices accumulate where phases cancel); a box of light (walls, constituents, spectrum); Laue's two integrands of one integral as ζ against ξ; the horizon at which what is held and what is written become one count. The gap became a question of which tools are uniform in scale. The drafting side first proposed a "three tiers" subsection and was told it was the least needed element — the flinch was from what the realizations would change on re-reading. One drafting error was caught in the same pass: "the primes are scaffolding with no interior". The lattice is scaffolding; the primes pay 1/p and keep interiors.

**25. Two-way inference, and the underbellies.** Run between the set and the BENDING draft, after re-reading `llm.md`, the licences and the meise orientation, the audit found one load-bearing circularity: H2 forced the Hilbert structure from "orthogonal additivity", which is the inner product it set out to derive. Repaired with Herschel–Maxwell: a valuation additive over Re ⊥ Im and blind to phase is $\lambda|a|^2$, so the premise is the geometry of a complex channel. Three readings — R1, R2 and the crossing half of R9 — were found to restate their conclusions and were marked as restatements.

**26. Regime-dependent transfer.** The operator asked whether the set leaned on RH in the corpus for what it could prove about RH, and whether the transfer functions it had introduced were scale-dependent. They are. Every "conditional on RH" verdict was regime-blind. The set now has three named transfer functions: the onset law at the Li tier, $X^\delta \gtrsim \gamma$ at the prime tier, and the $t^{-3/8}$ gate at the truncation tier, the last resting on GUE. Run inversely from the verified height H ≈ 3×10¹² they give ψ bounds of RH quality to about H² (Büthe) and λₙ ≥ 0 to about 10²⁷. Every RH-quality statement is labeled unconditional below the transfer scale of the verified height and conditional above it. The BENDING draft's verdicts (its Q18 and §X rows) were relabeled the same way.

**27. The cost-free commit.** The operator asked whether the set's own results — dt = 0, mass = 0, binding energy = 0 as operations the engine may legally make — gave RH a path inside the machinery: marking rays, defining topology, interfacing with the substrate by punching primes. They do: the engine forces its P-edges free (`Q4-OpenExhaust` §II), the Conservative Field names P–I as the un-priced writing head, and the reseeds are untaxed. The first path repour (`-path`, beats 0–13) walked it with the zeros as "free commits". Refined in Proceeding 28: a zero is held, not committed.

**28. The braid as transfer-function meta-frame; the blank patches.** The operator asked for the braid to be read as a transfer-function meta-frame and supplied `L5-TheCyclingMind`, `L5-K5-PhaseDynamicsTechnical` and `L6-InversionOfControl`. The source was asked for, not guessed: `L5-TheCyclingMind` was not in the project until uploaded. Five readings landed:
- The Gray-code braid holds the Mutable bimedian silent and runs the Mutable-held ring, in which ARI and PIS are dead and TAU, CAN and SAG are live. The braid commits the count, $P = I^2R$, and holds the positions. The zeros sit on its held bimedian, which makes them held rather than committed.
- The AbsentVar handoff is the explicit formula: a prime keeps scale and erases phase; a zero keeps phase and carries no scale.
- The prime print is the box's impulse response: −ζ′/ζ is the Laplace transform of $\sum\Lambda(n)\delta(u - \ln n)$, the zeros are the poles of the transfer function, and RH is the Foster condition.
- Primes are callbacks in the event-loop sense: the explicit formula invokes them at resonance and no `main()` generates them.
- The blank patches in the print are held families: each prime's comb holds its multiples silent, and the long gaps are CRT pile-ups (Rankin, Jacobsthal). Computed to 10⁹, the record gaps sit at 0.53–0.74 × (ln p)², against an RH ceiling √p ln p they approach ever less.

The averaging tools' blindness to a single off-line zero was seated as the third stuckness: an off-line zero is a diagonal the Mutable-held ring cannot map, the wrench is a ring change to tools uniform in scale, and Bagchi's strong recurrence is the hinge between them. The other two stucknesses landed on the Riemann–Siegel coin and the Lehmer pair.

**29. The burn.** With the path holding and carrying the detail on its spine, the operator's offer to burn the thesis, hub and ledger was taken up. The path became `L4-Riemann-Realization`, beats §0–§14, with a closing and a register. The thesis's content went into the beats; its questions went into Appendix D. The ledger became Appendix A, renumbered A.1–A.15, with A.16 (record gaps) new, A.12 updated with the third-stuckness test and the gap extension, and A.13 given the conditional inputs and the regime labels. Hub §10 became Appendix B. Hub §5, §11 and §12 became Appendix C, with C.12's H2 row restated on Herschel–Maxwell. The rest of the hub went into the beats: §1–§2 into §1, §3–§4 and §6 into §3, §7 into §2, §8 into §7, §9 into §0. Cross-references in the carried text were remapped mechanically and checked by hand.

**Address map, v3 → set.** v3 §1–§12 → thesis §1–§12. v3 §13 "settled by computation" → ledger §6–§9; v3 §13 "open" → thesis §11 (dispatch rule, figure and atom) and ledger §12. v3 §14.1–§14.5 → hub §1, §3–§6 (hub §2, "why squaring", is new). v3 §14.6 → hub §8. v3 §14.7 → hub §10. v3 §14.8 → hub §11. v3 §15 questions → thesis §13; bets → ledger §11. Hub §7 (tier reading) and §9 (shaft and two clocks) are new.

**Address map, set → path.** Thesis §0 → path §2 (landscape) and §14 (scope); §1 → §14; §2 → §6; §3 → §0, §7, §8; §4 → §3; §5 → §10; §6–§7 → §12; §8 → §14; §9 → §6; §10 → §6, §13; §11–§12 → §14; §13 → App. D. Hub §1–§2 → §1; §3–§4, §6 → §3; §5 → App. C; §7 → §2; §8 → §7; §9 → §0; §10 → App. B; §11 → App. C; §12 → C.12. Ledger §n → A.n (n = 1–15); A.16 is new. The first path repour's beats 0–13 → path §0–§14, with §9 (the braid) new and §11 (punching primes) extended.

---

## II. The Withdrawals Ledger

| Claim | Why it was withdrawn | Status |
|---|---|---|
| "The sharp integer cutoff breaks RH" at the first Lehmer pair | The off-line zero is $F_{33}$'s, not ζ's; its verdict flips with N | Re-read as a resolution test (§6) |
| Ψ(p) "is load-bearing, not asymptotic noise" | It is the leading term of an asymptotic expansion | Gone; §6 states the sizes instead |
| $P = I^2R$ with R = ϑ′ | Factor 2 against Riemann–von Mangoldt; inconsistent with U | Re-seated: R = ln(t/2πe); exact main term (§9) |
| Truncation and backward heat are one operation (v2 §7) | 126-pair scan: heat order has no information about truncation loss (0.465) | Became "two orthogonal readouts", itself withdrawn at height (below) |
| "The orders invert generally" | 111.03 misread; low-height orders agree | Negative rests on the Lehmer inversion and the 126-pair statistics |
| "Share nothing beyond that" | Claimed more than loss order; framed as a failed unification | Restated as what each reads |
| $p = 0.39002$ is a nit (review) | Correct at the peak | Reversed |
| "Forced" lift is overstated (review) | Forced given rotations and minimal degree | Reversed, with the two choices named (§4) |
| "Two orthogonal readouts" (heat against truncation), as a general statement | Holds below about 10⁵ only; with height the correction's size gate closes and truncation's ranking converges to heat's | Rewritten as a sign gated by a size (§7, §13, lede) |
| Prediction: $\lvert Z_{\text{peak}}\rvert \ll \lvert C_0\rvert$ persists at height | Median ratio 0.32 at < 4×10⁴ rising to 28 at 10¹² | Refuted; replaced by the open question of where the gate shuts |
| $S_0$ "between 0.59 and 3.7 at every sampled n up to 1500" | About ten samples; dense computation gives [−20.9, +23.2] with sign changes from n = 156 | Replaced by the dense range and envelope (§10) |
| Three pillars instantiate K₄ "without parameter fitting" (witness) | Seatings were chosen; a V₄ orbit fits any two-bit labelling | Not admitted; held as **[READING]** |
| "Where the gate shuts is open" (Part IV, earlier) | The mechanism gives a rate, not a cutoff: loss ∝ $t^{-3/8}$, smallest peak ∝ $(T\ln T)^{-2/3}$ | Replaced by "thins and never shuts", heuristic, with its test (ledger §6, §12) |
| Witness bet: the shifted plug's Li onset below n = 800 | Computed: first negative at n = 8 260 | Refuted; replaced by the onset law (ledger §8) |
| "For n ≤ 7 the primes alone carry positivity", as prime arithmetic | $S_\infty$ is Stirling + 0.746; the broken plug clears the same hurdle | Resized: a Γ-crossover the primes cover at low n, shared by broken plugs (thesis §10) |
| "Every plug of this Γ-shape is carried across it the same way" | $L(s,\chi_5)$: the window shrinks to n ≤ 2; closes at conductor q ≥ 23 | Restated: set by Stirling, the pole's factor s, and the conductor (thesis §10, ledger §4) |
| "For conductor q ≥ 4 the archimedean part is positive at every n" (drafting side, in chat) | Omitted the −1 from the absent factor s | Withdrawn; q ≥ 23 by computation |
| f = Mutable, "forced by flips-both" (drafting side, early) | Overreach; the seating is c = Fixed, cf = Mutable, f = Cardinal | Withdrawn; v3 §4 seating stands |
| H "kept out because not in the corpus" | Provenance is not a verdict; once supplied, H verified | Reinstated as a finite model (hub §10); not a route to the 1 ⊕ 3 decoupling |
| "Simplicity ⟺ interlaced zeros of ξ′" (witness) | Loose; simplicity is $\xi'(\rho) \ne 0$ | Restated as tank capacity $C = \tfrac12$ (hub §5) |
| Basins of g: Re s > ½ → 0 (witness) | Reversed | Re s > ½ → s = 1, the pole (hub §5) |
| "Every zero's tape is aperiodic, by Niven" (review) | Niven needs cos φ_γ rational, i.e. γ² rational — unknown | Held **[OPEN]** (thesis §5, §13 Q12) |
| Lehmer census as a Λ lower-bound byproduct (review) | Rodgers–Tao proved Λ ≥ 0 | Not admitted (ledger §6) |
| Euler factors as marginal elements on the stability boundary (review) | Poles at Re s′ = −½, damped by $p^{-1/2}$ | Corrected (hub §8) |
| f as parity, cf as time in H (review) | PT is the cf condition alone; f is chiral | Corrected (hub §10) |
| 7/8 as an unpriced constant for census (review) | +1 from s(s−1), −π/8 from Stirling's Γ phase | Not admitted (thesis §9, ledger §5) |
| Orbit volume ∝ δ²t² as rent diverging with height (review) | Coordinate effect; the disc leak goes the other way | Replaced by the height-free $\tfrac83\delta^3$ (thesis §4) |
| The primes as "a continuous texture" (original §3) | The primes are discrete; the continuous object is the Bohr torus their phases wind on | Withdrawn; thesis §3 states the torus facts |
| "Frequencies, not locations"; ψ(x) "inverts cause and effect"; "the spectrum is upstream" (v2–v3 §3; repour stance) | In t the primes are frequencies, in log x locations; the explicit formula is an identity between the two | Withdrawn; restated as two Fourier-dual readings (thesis §3) |
| "The plug supplies the texture — which frequencies ring" (v3 §11) | ζ and its broken controls share the frequencies ln p; the weights differ | Withdrawn; the plug is the weights $a_p$, pole, Γ-factor (thesis §11) |
| "RH says that texture holds every orbit on the circle" (v3 §11) | The torus picture stops at σ = ½, where RH lives | Restated on the weights; the line itself is thesis §13 Q14 |
| RH "decided by the incommensurability the integers carry" (hub §8) | The broken plug runs on the same delays | Corrected to the weights on the delays (hub §8) |
| "A crossing of a continuous ln\|ζ\| / arg ζ texture" as where a prime is (repour stance) | Primes are frequencies in log ζ and jumps of ψ, not crossings of ln\|ζ\| or arg ζ | Withdrawn from the stance |
| "The primes are its expression, not the plug" (stance) against "the primes arrive as the plug" (v3) | Contradictory, and both mislocate the decision | Resolved: the primes are the lattice; the plug is the weights |
| "The torus picture stops at σ = ½; the model's domain ends at the line where RH lives" (Proceeding 19, from the audit's framing) | Correct mathematics, wrong reading: at the line the price turns marginal and the texture becomes a real second moment (Selberg) | Withdrawn; thesis §3 restated on the price |
| "RH says every orbit is pinned to its mirror" as insight (v2–v3 §5) | Restates the self-dual hypothesis through its own symmetry | Marked as restatement; the reason is thesis §0, typicality |
| Thesis Q14, "what carries the prime weights on the line?" | Not open in the model's terms: the price $1/p$, marginal at ½, carries them | Removed; answered in thesis §3 |
| H2: "orthogonal additivity" forces the Hilbert structure (set, hub §12) | Orthogonal additivity is the inner product the premise was to derive | Repaired: the square forced per complex channel by Herschel–Maxwell (path §1) |
| R1, R2 and the crossing half of R9 as realizations (BENDING draft) | Each restated its conclusion in new vocabulary | Marked as restatements |
| "Conditional on RH" as a blanket verdict (set; BENDING draft Q18, §X) | Regime-blind: below the transfer scale of the verified height the RH-quality statements hold unconditionally | Relabeled by regime (path §12, A.13) |
| A zero as "a commit that costs nothing" (first path repour) | The braid never commits the positions; it commits the count and holds the zeros on its silent bimedian | Refined to held potential, untaxed, reseeded at its crossing (path §9, §10) |
| "The primes are scaffolding with no interior" (drafting side, in chat) | The lattice is scaffolding; the primes pay 1/p and keep interiors | Corrected (path §7) |
| A "three tiers" subsection as BENDING's contribution (drafting side) | The least needed element; the realizations were the yield | Not written; the realizations went in (path §6–§11) |
| The thesis, hub and ledger as standing files | Superseded by the path, which carries their content on its spine | Burned into the beats and Appendices A–D (Proceeding 29) |

---

## III. Patterns

**1. A screen's count is not a census.** The first scan reported 49 pairs and would have shipped as "all of them". *Guard:* every screen gets an independent completeness count — here, the total number of zeros against Riemann–von Mangoldt.

**2. Reading a sign against the wrong reference.** A dip was checked for a positive value. *Guard:* test "same sign as the true extremum", never "positive".

**3. Grading a result against one's own conjecture.** A clean negative was written up as a loss because the drafting side had proposed the opposite. *Guard:* state what the test found, in the test's own terms, before comparing it with anything.

**4. A restatement sized as a discovery.** The sign rule was reported as a finding before it was noticed to follow from the formula. *Guard:* before landing a 100% rule, derive it; what the computation adds is usually the range over which the derivation's assumptions hold.

**5. A witness's correct conclusions do not license its framing.** The external §13 run was right on both conclusions and wrong on what they demonstrated. *Guard:* the same as `L4-Riemann-evolution` pattern 21 — evaluate conclusions and premises separately.

**6. A prediction made from the regime it was meant to leave.** "$|Z_{\text{peak}}| \ll |C_0|$ persists" was argued from the low-height data the prediction was meant to go beyond. *Guard:* a prediction about a scaling regime has to be argued from the scalings — here $C_0 \propto t^{-1/4}$ against the peaks' growth — not from the values in hand.

**7. A sparse sample reported as a range.** Ten values of n became "between 0.59 and 3.7 at every sampled n", which read as a bound. *Guard:* a range is reported only from a dense computation; a sparse one is reported as its points.

**8. Silent numerical failure at scale.** Five faults in one push, none raising an error: a float64 constant, rounded offsets, a truncated expansion, a clamped singularity, and a divergent-integral warning. Each was caught by a count against the θ-count or by a value already known. *Guard:* at every new scale, re-establish one count and one known value before reading any statistic.

**9. Provenance taken for a verdict.** The orbit generator was dropped because the corpus did not contain it, under an instruction to integrate losslessly. Once its derivation was supplied it checked in full. *Guard:* unverified material is kept and labelled with what it is, then verified; absence from the corpus is a reason to check, not to cut.

**10. A swing mistaken for a correction.** "The primes alone carry low-n positivity" was corrected to "it contains nothing about primes" — the opposite closure. Both collapse a two-sided fact. *Guard:* when a claim is resized, state what survives on each side before writing the new sentence.

**11. A shift transferred without its companion term.** The conductor's $\tfrac n2\ln q$ was carried from ζ to $L(s,\chi)$ without the −1 that the absent pole's factor s takes with it. *Guard:* before generalizing a split to a new plug, compute that plug's split once.

**12. A theorem cited past its hypotheses.** Niven's theorem was invoked for an irrational cosine. *Guard:* read the hypothesis before landing the conclusion, even for an elementary theorem.

**13. An instrument whose target has been settled.** Lehmer-pair certificates were proposed as a byproduct after Rodgers–Tao had made them obsolete. *Guard:* before offering a classical instrument's output as new, check whether its target has since been closed.

**14. A coordinate artefact read as a law.** Orbit volume growing as $t^2$ was read as rent diverging with height; the disc measure of the same pair shrinks as $t^{-2}$. *Guard:* when two natural measures disagree on a trend, look for the combination that does not depend on the coordinate.

**15. Insulation repeated as scope.** Six sites said some form of "this proves nothing about RH". Repetition reads as defence and dilutes what the sections earn. *Guard:* state the scope once, flatly, where scope is discussed, and let every other section close on what it showed.

**16. A [READING] tag taken as a pass.** The texture reading carried the [READING] tag through three passes, and the tag was treated as licence. It is not: a reading earns its tag only if it is consistent with the landed mathematics it reads, and this one contradicted the explicit formula and the shared frequency set. *Guard:* before a [READING] ships, check it against the identities under it — here, does it separate ζ from a broken plug that shares the same data, and does it survive at the line where it is applied?

**17. Overcorrection by borrowed framing.** The withdrawal of Proceeding 19 was right on the mathematics and took the audit's framing with it: "the picture stops at the line" became a limit and an open question, at the one place the operator had pointed all along. Pattern 5 already names this; it was repeated within the same pass. *Guard:* when a critique corrects a reading, ask what survives on the corrected mathematics before accepting the critique's account of what is left — a change of state is not an end.

**18. A restatement dressed as a reason.** "RH says every orbit is pinned to its mirror" read as insight and was the hypothesis in new coordinates — the more fitting the coordinates, the more convincing the circle. *Guard:* for every "RH says …", ask whether the sentence would still hold content if RH were false. If it only re-expresses the hypothesis, label it a restatement and point to the reason, or find one.

**19. A semantics imported onto an object it cannot see.** "Everywhere against almost everywhere" carried measure language to a single deterministic line, which that measure assigns zero. *Guard:* before stating a gap, ask which tool could detect the difference, and whether the object is even visible to it; here the tools sort by scale, not by measure.

**20. A forcing premise that is the conclusion's axiom.** H2 derived the Hilbert structure from orthogonal additivity, which is the inner product under another name. The circle survived several passes because the conclusion was true and the premise sounded weaker. *Guard:* for every "forced by", state the premise in terms that do not mention the structure being forced, then check that a structure without the conclusion would violate it.

**21. A verdict without its regime.** "Conditional on RH" was stamped on statements that hold unconditionally below the scale the verified height reaches. *Guard:* every conditional verdict names its transfer function and the scale up to which verification has already discharged it.

**22. A free operation booked as a commit.** The zeros were first walked as "free commits". The braid commits only the count, and the positions are what it holds. *Guard:* before calling an operation a commit, check which edge it writes on and whether that edge belongs to the ring in use or to the held matching.

---

## IV. For Whoever Appeals Next

- **The zero count to 40 000 is not rigorous.** There was no interval arithmetic and no Turing-method bound. It agrees with Riemann–von Mangoldt and with the literature (RH verified far beyond this height), and claims nothing more.
- **τ\* is first order.** It matches the local model to 2%; a full heat-flow computation of $H_\tau$ was not run.
- **"Lost at N" depends on the window.** The criterion is sign changes between neighbour midpoints. The external run used a different window and disagreed at the edges of the N range, though not on any conclusion.
- **The K₄ seatings are chosen.** Where they are literal (§12), they are literal as mathematics. That the engine predicted them is not claimed.
- **The prime-side exponent is a finite-range measurement.** −0.497 up to 10¹⁰ is consistent with von Koch's form of RH and nothing more; by the heuristic in §10, an off-line zero at height 10⁴ with offset 0.01 would surface only near 10⁴⁰⁰.
- **S₀(n) is dense only to n = 1000.** Beyond that it was computed at every fourth n, so its sign changes there are a lower bound and its extremes may be slightly understated.
- **The high windows are small.** 6 000 zeros at 10¹² hold 20 close pairs. "Heat order predicts loss" at 10⁸ and 10¹⁰ rests on 9 and 4 lost pairs. The direction is clear; the numbers are not precise.
- **Every height reached has been computed before.** Zeros near 10¹² and far beyond are in the literature, and λₙ is rigorous to n = 10⁵. What is new here is the file's observables there: the sign rule, the gate, and the heat–truncation convergence.
- **Where the gate shuts is open** (§13). Press it above 10¹². *Superseded by Proceeding 14:* the gate is predicted to thin as $t^{-3/8}$ and never shut; the test is the same table at 10¹⁴–10¹⁶, with the 10¹⁰ window enlarged (ledger §11 bet 2, §12).
- **The loss law is a heuristic.** $t^{-3/8}$ rests on GUE pair statistics and a local quadratic peak model. It matches 10⁸ and 10¹², and misses 10¹⁰ by a factor of about eight on 4 losses.
- **The onset law is fitted to 1%, on detuned plugs only.** Davenport–Heilbronn breaks a different axiom (no Euler product); bet 1 declares that assumption.
- **The third plug runs to n = 40.** The conductor threshold q ≥ 23 follows from the exact archimedean formula; $\lambda_n(\chi_5)$ beyond n = 40 has not been computed.
- **The orbit generator is a finite model.** It is derived from the orbit's symmetry, not from ζ; which operator on ζ's side carries it is open (App. D Q9 (formerly thesis §13 Q9)).
- **The gap record is finite.** A.16 runs to 10⁹. Cramér's √p ln p ceiling is conditional on RH and is far from tested by gaps this small; the (ln p)² band is Cramér's model, not a theorem.
- **The braid readings are seatings.** The Mutable-held ring, its live opcodes and the AbsentVar handoff are forced in the engine. That ζ's tiers run on that ring is a reading, whose test is the third-stuckness computation in A.12.
- **Several readings are addresses, not correspondences.** Unsharpness ↔ stuckness, the generator's threshold ↔ $R = U^2/P$, one seam ↔ four frictions, the tier reading's extension to the trivial zeros. Each names what would promote it.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work. This file is a case history; read `L4-Riemann-Realization` and its appendices for the standing claims.

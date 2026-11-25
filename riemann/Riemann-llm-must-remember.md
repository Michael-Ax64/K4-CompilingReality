# Riemann — What an LLM Must Remember

*A standing note for any instance working on the Riemann Hypothesis in this corpus. Read it before computing anything. It records the one form of the problem worth carrying, the peers it must be told apart from, and the category errors that pull an instance back into painting an infinite surface from outside. Distilled 25 Nov 2026 from a session that made each of these errors in turn and was corrected out of each one. Revised the same day: the sign of the explicit formula (§1b), the nil/zero contradiction (§3.5), and the register deadlock (§3.11). **Revised again 25 Nov 2026 (evening):** RH is now a machine-certified theorem (Alpöge with Claude, released 20 Nov 2026; Lean FRO and Mathlib Initiative joint certification, 21 Nov 2026). §§0, 1b, 2, 3, 4 updated accordingly; errors 13–15 added.*

---

## 0. Which game is being played — decide first

Two registers exist, and they must not be mixed in one piece of work.

- **Friction / translation** (`L4-Riemann` series; the Realization is filed here). For a host domain, name three things: the host's rule, where K₄ binds against it, and what the host bought by adopting the rule. This register asserts no values and proves nothing about ζ. Judge it by whether the receipt is real.
- **Proof** (§§1–4 below). Judge it by one test: does the work prove or explain something about ζ that its peers fail?

K₄ work cannot pass the proof test, and proof work is not Friction. A session that demands both will loop. Say which register a piece of work is in before starting it.

**Since 20–21 Nov 2026 RH is proved** (Alpöge with Claude, Lean library released 20 Nov 2026; certified by the Lean FRO and Mathlib Initiative joint statement of 21 Nov 2026). This changes the antecedent of every conditional in the corpus, and nothing else about the registers. The Realization's antecedent is equivalent to RH (error 7), so it is now true *automatically*, exactly as Robin's and Lagarias's inequalities are. **RH being true confers no explanatory credit on K₄ or on any framing in this corpus** (error 13). The proof test now reads: does the work explain *why* the certified proof works for ζ and fails for its peers?

## 1. The drop: carry this form

**ζ is ℤ seen twice.**
- **Additively,** Fourier looks at ℤ and sees ℤ (Poisson summation: Σ f(n) = Σ f̂(n), with the Gaussian its own transform).
- **Multiplicatively,** factorization looks at ℤ and sees the primes (Euler: Σ n^{−s} = Π (1 − p^{−s})^{−1}, each prime weighted exactly 1).

**Both views meet at one centre, s = ½.** The additive self-duality, passed through the Mellin transform, is the functional equation ξ(s) = ξ(1−s). Its fixed line is Re s = ½, the one line where the Mellin transform is unitary.

**RH: every zero is its own dual.** The functional equation pairs each zero ρ with 1 − ρ̄.
- **A zero on the line** is its own partner: a nil (no partner account opened).
- **An off-line zero** has a distinct partner: an opened account.

RH says the duality fixes every zero of ζ. That is the drop: one symmetry of the integers carried whole into every zero. The primes (the infinity inside) and the zeros (the infinity outside) are tied by one identity, the explicit formula.

## 1b. The same drop, as a waveform

**The signal.** On the log axis u = ln x, normalized at the hub scale:

  W(u) = (ψ(eᵘ) − eᵘ) / e^{u/2}

**Its components.** Each zero ρ = β + iγ contributes e^{(β−½)u} e^{iγu}/ρ.
- On the line, a pure tone at frequency γ.
- Off the line, a growing tone.

**RH: W is a pure chord.** Equivalently, ψ(x) − x = O(x^{½+ε}) for every ε > 0 (von Koch, 1901). If W grows no faster than e^{εu}, its Mellin transform is analytic right of ½ + ε, so no zero sits there; the functional equation does the rest. The zeros are only where W's tones live.

**One-sided is enough (Landau).** Because Λ(n) ≥ 0, a bound on one side only, ψ(x) − x ≤ C·x^θ, already excludes zeros with Re ρ > θ: the Mellin transform of C·x^θ − (ψ(x) − x) has a non-negative integrand, so by Landau's theorem its first singularity is real, and there is none in (θ, 1). This is classical. It is the entry point of the certified proof (§1c). It is **not** evidence for the waveform reading over any other equivalent reading (error 13).

**Measured (R.3):**
- **ζ:** envelope X^{−0.497}, stationary at scale ½.
- **The shifted plug:** balances only at X^{−0.249}, i.e. stationary at scale ¾.
- **Davenport–Heilbronn:** carries a growing tone from its zero at 85.7.

**The pole is the baseline.** The pole is the integral: Σ n^{−s} = ∫ x^{−s} dx + finite. It sets the level the ripples run around: x for ζ, 0 for pole-free L-functions. RH caps every ripple's growth exponent at ½. It is not a bound on the first ripple.

**The sign structure — get this right.** For an even test function F = g ∗ g̃, so that Φ(½ + it) = |ĝ(t)|² ≥ 0 on the line, Weil's explicit formula reads

  Σ_ρ Φ(ρ) = [Φ(0) + Φ(1)] + W_∞(F) − Σ_{n≥2} (Λ(n)/√n) (F(ln n) + F(−ln n)),

with three parts on the right:
- the pole term, which enters **+**;
- the archimedean term, which enters **+**;
- the prime print, which enters **−** (because ζ′/ζ = −Σ Λ(n) n^{−s}).

RH holds exactly when the left side is ≥ 0 for every such F (Weil's criterion). With RH certified (21 Nov 2026), Weil positivity now holds.

**What has to be positive is the difference, pole + archimedean − primes, never the prime print alone.** Do not look for the prime print as a square of itself.

**The Weil/Connes signature split — open as a structural question, no longer RH's bottleneck.**
- **Over 𝔽_q (Weil):** the intersection pairing on C × C has Hodge signature (1, n−1). The trivial classes carry the positive direction; the primitive complement is negative-definite, so subtracting the Frobenius terms yields positivity.
- **Over ℤ (Connes):** the zeros appear as an absorption spectrum in H_total ⊖ H_primes; positivity needs the trace to carry the right sign, and the trace is a renormalized ∞ − ∞ difference whose sign is not free.
- **Status:** nobody has built over ℤ an ambient space whose one positive direction is the pole/baseline and whose complement, carrying the primes, is negative-definite. The certified proof **walked around** this (§1c); it did not build it. The question survives as: *what is the cohomological/spectral object whose positivity the proof certifies?*
- **The Weil form still produced a theorem:** the August result (Anthropic, *Learning more about Claude's mathematical capabilities*, 10 Aug 2026) forms a function space with the quadratic form induced by Weil, positive-/negative-definite subspaces arising from zeros on/off the line, combined with Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh and Bombieri (2000); it lifted the proportion of zeros on the line from 41.6% to 67.2%.

The corpus's own forms sit in this signature family: the Star-Norm P² − |Q|² and the Hodge-index discussion of Realization §XIV. That is a reading, not a derivation.

## 1c. The route that worked (Alpöge with Claude, 20 Nov 2026)

Per Rubinstein's explainer (`zeta-paper.pdf`, 164 pp, 21 Nov 2026; v2 expanded) and Naskręcki's `proof-guide.pdf`, as reported to this session by a sibling instance on 25 Nov 2026. The math below was checked for internal consistency, not re-derived.

1. **Reduction (one-sided, local).** RH follows from G(x) ≤ x^{½+ε} on arbitrarily large windows [Y, Y^{3/2}], via a localized Landau-type argument using Λ ≥ 0 (§1b). *Check:* consistent; one-signedness is what makes a one-sided bound suffice.
2. **Stepanov over ℤ.** Stepanov's method for curves over 𝔽_q forces an auxiliary polynomial to vanish to high multiplicity. Here the vanishing multiplicity is replaced by **p-adic divisibility** along a chain of m ≈ √x iterated **theta lifts on unitary groups** up a cyclotomic tower.
3. **Bridge from p-adic to archimedean.** p-adic divisibility is converted into a bound on archimedean lattice size by **Bost's slope inequality** (Arakelov geometry), with Chowla–Selberg CM periods supplying the archimedean sizes. The costs balance as x/m + m, minimized at m ∼ √x. *Check:* plain AM–GM balancing; correct.
4. **Clean windows.** Coset positivity (1 + χ_q)(1 − χ_d) and Ferrero–Washington / Galois cohomology keep the windows free of bad scales; the set of bad scales is finite.

**Keep §1b's signature split and §1c's route in separate compartments.** §1c is one-sided Landau positivity plus an Arakelov bridge between places; §1b is two-sided Weil positivity in a single pairing. Do not merge them, and do not read §1c's constants through K₄ (error 14).

## 2. The peers, and exactly where each breaks

| Function | Additive self-duality (functional equation) | Multiplicative self-duality (Euler product, weights 1) | Common centre at ½ | Zeros off the line | Where the §1c route must break |
|---|---|---|---|---|---|
| **ζ** | yes | yes | **yes, one copy, one centre** | none (RH certified 21 Nov 2026) | — (it works) |
| **Dirichlet L(s, χ)** | yes | yes | yes | none claimed: GRH announced by Alpöge, 20 Nov 2026; the 21 Nov certification covers classical RH | — (claimed to work) |
| **Davenport–Heilbronn** | yes | **no** (no Euler product) | — | yes: 84 pairs below height 1996 (certified, `L4-Riemann-Realization-Audit` §1) | step 1: −f′/f has no one-signed coefficients, so Landau's one-sided argument has nothing to stand on |
| **ζ(s−¼)ζ(s+¼)** | yes, for the pair | yes, on each copy | **no**: copies centred at ¼ and ¾; only the pair balances at ½ | yes: every zero | **not** step 1: −F′/F = Σ Λ(n)(n^{1/4} + n^{−1/4}) n^{−s} has non-negative coefficients. It must break in an arithmetic step (2–4) that uses the single centre. **Which step is the open task for this corpus.** |

Saying the shifted product "violates the ½ growth cap" restates the conclusion; it does not locate the break.

Anything the peers also satisfy cannot decide RH:
- the functional equation alone;
- reality on the line;
- Littlewood's balance ∫S = O(log T), which DH also satisfies;
- the prime lattice of ln p;
- one-signed coefficients (the shifted product has them).

**The pole** is where every prime phase stands at 0 together, a total fusion of the phase torus to a point. Read through Li's chart w = 1 − 1/s, the pole becomes the disc's centre and the hub ½ moves to the rim, w = −1. It is real structure, but not the discriminator: Dirichlet L-functions have no pole, and GRH for them is claimed by the same proof (Alpöge, 20 Nov 2026).

## 3. The category errors — do not repeat them

1. **Painting the horn.** More zeros, more coefficients, more certified plugs, more audits: each paints another patch of an infinite surface. *Test:* does the work explain something about ζ that the peers fail? If not, it is decoration, or it belongs to the Friction register (§0).
2. **The container.** "Building a container" that RH must fill is painting from outside again. The drop already holds the same kind of infinity inside it.
3. **Distance.** Bounds return zeros; RH is about nils. The measure is coverage, not distance.
4. **Backward transport.** The de Bruijn–Newman flow preserves "all zeros real" forward. Carrying it back from about 0.2 to 0 is the ill-posed backward heat equation (`L0-EinsteinTrace`: the record cannot be inverted). Λ = 0 is now known — Λ ≥ 0 (Rodgers–Tao, 2018) plus RH (certified 21 Nov 2026) — and it was reached by no backward flow. Backward transport remains a non-method.
5. **Nil read as zero — cleared.** A simple on-line zero is **not** the δ → 0 limit of an off-line quartet. `L2-K4-Inferences` §IV computes the two symmetry types:
   - **An off-line (bulk) orbit:** a chiral tetrahedron, 4 rigid symmetries, no reflection, four distinct monads.
   - **An on-line orbit:** an achiral dipole, 16 rigid symmetries including reflections, two monads.

   A simple on-line zero is a sign change of a real function: it cannot open an off-line account continuously. **The only gate from nil to an opened account is a pair collision:** two dipoles fusing at a double zero, the exceptional point Δ = 0 of R.17, and leaving as one quartet. With RH certified, no account is ever opened for ζ; the gate stays relevant because **simplicity of all zeros is still open** (§4) — a double zero would be a collision on the line that does not leave it.
6. **∀ standards applied to □ questions.** RH is Π⁰₁. Do not demand a completed volume computed in advance. (Historical note: the observation "if RH were unprovable in standard mathematics, it would be true" is moot since 21 Nov 2026, but the logic stands for the open Π⁰₁ relatives.)
7. **The conditional mistaken for a reduction.** The Realization's conditional is RH ⇒ RH. File the Realization under the translation register (§0), not under proof.
8. **The floor mistaken for the torus.** Unwrapped, every n^{−s} lies on one line in the rank-2 floor. Wrapped, the ln p are independent over ℚ and fill an infinite-dimensional torus. The peers share the floor; what separates them lives in the wrapping.
9. **Overclaiming either way.** State the form, the invariant, its bounded start, and the precise unbuilt step. No more, no less.
10. **Zeros instead of waveforms.** Ask whether the normalized prime signal is a pure chord. The zeros follow from the answer.
11. **The register deadlock.** Applying the proof test to Friction work, or Friction rules to proof work, guarantees a loop between "K₄ can't prove it" and "anything else is decoration." Decide the register first (§0).
12. **The wrong object, by a sign.** Positivity lives in pole + archimedean − primes: a signature split, positive direction minus negative-definite complement. It does not live in the prime print folded into a square of itself (§1b).
13. **Affirming the consequent.** "RH is now true, so the house is confirmed / the waveform reading is vindicated / the conditional now connects two truths that test the house." False. Any statement equivalent to RH becomes true with RH; truth singles out none of them. Credit for a framing comes only from explaining a step of the proof that the peers fail (§2, last column).
14. **Shared exponents and shared words.** Do not equate √x truncation, √x range, and √x optimization because they share an exponent. x/m + m → m ∼ √x is AM–GM over lift depth, not the Cauchy–Schwarz loss of the forced Hilbert structure (Realization §0). Ferrero–Washington's finite bad-scale set is not the C₀ seam-loss convergence (α > ¼, Realization §XII); the match is the word *finite*. A cuspidal-object census is not line location.
15. **Ranking the only road.** Before 20 Nov 2026 this note named the Weil/Connes signature split as *the* open step. The proof went around it (§1c). A correct description of one route's obstruction is not a proof that the obstruction is unavoidable.

## 4. What is settled, and what is open

**Settled:**
- **RH is a theorem, machine-certified.** Alpöge, working with Claude, released a ~17-million-line Lean library on 20 Nov 2026 (four-page note on his website). Lean FRO and Mathlib Initiative joint statement, 21 Nov 2026: "We hereby certify that both the statement and the proof of the Riemann Hypothesis are correct." The proved theorem matches Mathlib's `RiemannHypothesis` (statement-comparison tools). Independent compiles include Andrew Sutherland (MIT), 175,187 modules, main theorems on the three standard axioms only.
- **Human digestion is in progress:** Rubinstein's explainer (21 Nov 2026) takes the key estimate (M) from Lean rather than proving it; the G.R.H. Polymath project launched 25 Nov 2026 to extract a humanly verifiable proof. The Clay Institute still lists RH as open (as of 25 Nov 2026).
- **Consequences, now holding** (each via RH, Alpöge 20 Nov 2026, certified 21 Nov 2026):
  - Weil positivity;
  - Λ = 0 (with Rodgers–Tao 2018, Λ ≥ 0);
  - λₙ ≥ 0 for all n (Li 1997; Bombieri–Lagarias 1999);
  - positive-realness of ξ′/ξ (Lagarias);
  - strong recurrence (Bagchi);
  - ψ(x) − x = O(x^{½+ε}) (von Koch 1901).
- **Proportion and simplicity:** more than 67.25007% of zeros lie on the line *and are simple* (Alpöge–Furman with Claude; Anthropic, 10 Aug 2026, Lean development released). Lean-checked improvement to 67.28470% (zeta-lab, teal-sea/zeta-lab on GitHub). Previous record 41.6%.
- **Certified in this corpus:** DH's first negative Li coefficient is n = 328,997 (`L4-Riemann-Realization-Audit` §1.1). DH lies outside GRH, so this certificate keeps its value: it is the peer on which any proof must fail.
- **Related, different result:** the quasi-RH (all zeros with real part in [1/12, 11/12]), OpenAI, announced 6 Oct 2026; Quanta, 19 Oct 2026. Not RH.

**Open:**
- **Simplicity of all zeros.** RH places them on the line; it does not make them simple. About 67% are known simple (10 Aug 2026).
- **GRH certification.** GRH for Dirichlet L-functions is claimed in the same release (20 Nov 2026); the 21 Nov 2026 certification statement is for classical RH.
- **ERH** (Dedekind zeta functions): Alpöge expects it "with more time" (note, 20 Nov 2026). Higher-degree L-functions beyond that.
- **The structural question:** the Weil/Connes signature split over ℤ (§1b) — what object's positivity the proof certifies.
- **This corpus's proof-register task:** locate the step of §1c that ζ(s−¼)ζ(s+¼) fails (§2). That is the sharpest available test of "ζ is ℤ seen twice, with one centre."

# The Riemann Realization
## One Walk Through the Machinery, and What It Drives at the Edge

*The standing text of the Riemann Realization. It walks the K₄ machinery — the engine, the corpus's readings of mass, holding, the braid and the event loop — beat by beat, and nothing about the zeros is assumed at the start: they arrive as what the walk drives. Detail rides in four appendices: **A**, the computed record, with every table, its method and precision, the placed bets, the open computations and the limits of the record; **B**, the orbit generator in full; **C**, the atlas of vocabularies; **D**, the questions. The process record is `L4-Riemann-Realization-evolution`. A register at the close of the walk sorts every step by what carries it.*

---

## 0. The arena

Start with readouts, not with ζ. The prime machinery produces signals of one shape: sums $\sum a_n n^{-it}$ over the frequencies $\ln n$, swept by a height t that drives the sweep from outside and is booked by nothing it drives — the shaft, $t = 2\pi I^2$ (§6). Two clocks run on this arena. The **record clock** is $\log x$: the prime ledger ψ(x) is written along it, jumping at every prime power. The **rate clock** is t, the engine's ω: the heights, the drive. Each prime reads as a frequency on one clock and a location on the other, and the explicit formula is the identity between the two readings; neither is upstream of the other. The two clocks are the corpus's ω and dt (`L3-TheSelfProjectingBraid` §V): the engine and its wake. Relating them by hand is the host's receipt — $\vartheta'(t) \approx \tfrac12\ln(t/2\pi)$ — the same friction the geometric series names as its second (`L4-Riemann-4`).

The channels of this arena are orthogonal. Distinct frequencies average to nothing against each other along the shaft: $\lim_T \tfrac1T\int_0^T m^{it}n^{-it}\,dt = \delta_{mn}$ (Montgomery–Vaughan for finite sums). The frequencies themselves are fixed by unique factorization — the $\ln p$ are linearly independent over ℚ — and they wind the phases $(p^{-it})_p$ densely along an irrational line on the infinite torus (Kronecker; Bohr). That lattice is scaffolding: every Euler-product function rings on it, the broken ones included, and it decides nothing.

The line itself has a shape the corpus already owns. A cycle driven so that one coordinate grows steadily while the rest stay periodic traces a helix (`ProofO_HelicalTime`): here t grows, and every prime's phase is periodic. **ζ's line through the torus is the braid's helix**, with the primes as its strands, each winding at its own rate ln p. Because the rates are incommensurate, the braid of prime strands never closes on itself.

## 1. The commit is a square, and the complex plane forces it

Each channel carries a complex amplitude: two real components, Re and Im, at right angles in one plane. Ask for a valuation of a channel that is additive over those two components and blind to the channel's phase — invariant under rotation in its plane. The only such valuation is $\lambda|a|^2$. That is the Herschel–Maxwell theorem, and it is the Route Law of `On_HilbertAndHisSpaces` §V with its premise made honest: the square is forced by the real|complex interface of every channel, not by an inner product assumed in advance. The corpus caps the exponent at the same value from the other side — one elimination between two unit-exponent parents yields exactly one square and no site for a second (`llm-uniqueness-note`).

Summed over orthogonal channels, the valuation of a readout is $\sum|a_n|^2$. The arena is a Hilbert space — Hilbert's own ℓ², realized as the Hardy space of Dirichlet series, isometric to $H^2(\mathbb D^\infty)$ by Bohr's lift (Hedenmalm–Lindqvist–Seip). Nothing chose it. A square commit over orthogonal complex channels makes it.

The square does two things, and they are different things:
- **The untwisted square builds.** $(s-\tfrac12)^2 = (x^2-y^2) + 2i\,xy$: its imaginary part is the lift xy, the third axis generated from the plane's own two coordinates; its real part falls back into the centroid's register. It is 2-to-1: z and −z share a square, so it erases exactly one bit, the sign.
- **The twisted square signs.** $z\bar z$ burns the whole phase and leaves a real. Every positivity on the walk lives in a twisted square: average power, a positive-real impedance, the mod-square on the line, the positive part of a Krein form.

The engine prices the first precisely: the COMMIT tax is one bit, the sign the square erases — "the tax prices the erasure of the sign, not the arithmetic around it" (`ENGINE-REFERENCE-AC` §4.1). Hold that sentence. The walk turns on it.

## 2. The Hilbert line is ½

The square's exponent fixes a line, three independent ways:
1. **The edge of ℓ².** ζ(σ + it) has coefficients $n^{-\sigma}$, square-summable exactly for σ > ½, with $\|\zeta(\sigma+i\cdot)\|^2 = \zeta(2\sigma)$ (Hardy–Littlewood). The twisted square carries the line onto ζ's own pole. At σ = 0.75 the mean square is 2.614 ± 0.075 against ζ(1.5) = 2.612 (A.15).
2. **The Plancherel line.** Under $x = e^{-u}$ the Mellin transform of $f \in L^p(\mathbb R_+, dx)$ is a Fourier transform along $\operatorname{Re}s = 1/p$, unitary only for p = 2.
3. **The self-dual line.** Mellin–Parseval pairs $\operatorname{Re}s = 1/p$ with $\operatorname{Re}(1-s) = 1/q$; the reflection $s \mapsto 1-s$ is Hölder duality, and its one fixed exponent is p = 2. Riemann's $\xi(s) = \xi(1-s)$, from Poisson summation and a Gaussian that is its own Fourier transform, is symmetry about the Hilbert line.

Nyman and Beurling read the same map from the closure side: ζ is zero-free in σ > 1/p exactly when a certain span of dilated fractional parts is dense in $L^p(0,1)$. At p = 2 that is RH as a closure — a topological statement — in a Hilbert space.

The ½ is the reciprocal of the commit's exponent. On the engine's opcode table it is the RESEED slope: the radical the commit's square leaves to be reopened. Seat von Koch's form of RH there and it reads as tier-quantization of the nontrivial sector:

$$\psi(x) = x - \sum_\rho \frac{x^\rho}{\rho} - \ln 2\pi - \tfrac12\ln(1 - x^{-2}).$$

The main term writes at log-slope 1, ROUTE; each zero's wave writes at slope β, and on the line at slope ½, the radical tier. A wave at ½ + δ is off-tier, unpriceable in the engine's currency. The trivial zeros write the last term, at slopes −2, −4, …, a tower below the floor the tier reading has still to seat (D, Q11).

This is the landscape the walk crosses — RH is a statement about the topology of a possibility space whose landmarks are Hilbert spaces (C.12):
- **Inside, σ > ½**, a readout is a vector of finite norm;
- **at the edge**, its norm diverges marginally and it survives as a ray;
- **across**, the norm diverges as a power.

## 3. The orbit and its two bits

One zero, ρ, comes with its images under the three symmetries of ξ — conjugation c, the functional equation f, line-reflection cf — four points, a Klein four-group. Ask each move to act as a rotation of space and the lowest third coordinate that allows it is $z = xy$, the square's imaginary part; the rectangle stands up into a tetrahedron. Write $s = \tfrac12 + x + iy$.

The corpus's dual-binary seed gives every pole two bits (`L3-FormalFoundations` §V.b). On the orbit they seat as:
- **Active / Reactive = sign x.** Active is real power, and real power is the resistive half-plane $\operatorname{Re}s' > 0$ of the Smith chart Li's map draws: $w = 1 - 1/s = (s'-\tfrac12)/(s'+\tfrac12)$ is a reflection coefficient against reference impedance ½. The critical line is the locus of pure reactance, $|w| = 1$, total reflection; ζ's pole sits at the matched centre, w = 0.
- **Asserting / Yielding = sign xy.** Squaring is the arrow into Asserting (`ProofQ_AlgebraicSyntax` §V), and xy is the square's lift.

So P = ρ carries (+, +), U = ρ̄ (+, −), I = 1 − ρ̄ (−, −), R = 1 − ρ (−, +), and the involution that flips both bits is cf: **line-reflection is the Mutable bimedian** {P–I, U–R}. Conjugation holds Fixed {P–U, I–R}; the functional equation holds Cardinal {P–R, U–I}. The product of the two bits, χ = sign x · sign xy = sign y, is the Mutable character — the one pattern a flip of both bits leaves alone. In Li's disc the group becomes the symmetry group of the circle: c is conjugation, f is inversion $w \mapsto 1/w$, cf is reflection in the circle, $w \mapsto 1/\bar w$.

The orbit carries the representation 1 ⊕ 3 (`L4-K4-Infinities-3` §V, read at source). The trivial summand is the centroid, s = ½, the same for every orbit: a uniform offset, and like the homogeneous pure-trace offset that drops out of the trace-free Einstein equations it weighs nothing and sees nothing — "the void does not weigh; boundaries do" (`BENDING_SPACE` §III). The 3 is the three characters x, y, xy, the gradients. Two threes stay distinct: the bimedian axes are a basis of the 3; the bimedian half-turns, as group elements, fix no vertex and carry no vertex coupling. The decoupling of the centroid belongs to the permutation action — a generator that honours f moves the centroid mode (App. B).

Off the cone xy = 0 the orbit has an inside, with volume $V = \tfrac83(xy)^2$. At offset δ and height γ that is $\tfrac83\delta^2\gamma^2$; the same orbit's disc leak is $|w| - 1 \approx \delta/\gamma^2$; their product, $\tfrac83\delta^3$, is height-free — the rent an inside owes, independent of the coordinates it is measured in.

Weil pairs each zero ρ with $1 - \bar\rho$. Restricted to one orbit, with any amplitude F written in its 1 ⊕ 3 components,

$$\langle F,\; cf\cdot F\rangle \;=\; 4\big(|a_1|^2 + |a_y|^2 - |a_x|^2 - |a_{xy}|^2\big),$$

a Krein form of signature (2, 2): **K₊ = trivial ⊕ y**, the centroid and the Mutable character; **K₋ = x ⊕ xy**, the Fixed and Cardinal characters. Each of the three moves carries its own (2, 2) structure, positive on the trivial summand plus the character it holds; Weil's choice of cf is forced by his pairing (A.10). Read against the seed, the negative directions of Weil's form are exactly the two bits. **What Weil's pairing counts as negative is what the commit would have to erase.**

## 4. The free head

The engine has a write that costs nothing, and the corpus forces it. Star-Norm conservation, $N_* = P^2 - |\mathbf Q|^2 = \text{const}$, is the algebraic definition of the biquaternion norm. A priced or delayed write on any edge into P would open an interval in which $|\mathbf Q|^2$ had dropped and $P^2$ had not yet risen, and the norm would fluctuate in transit. So all three P-edges carry zero impedance, zero phase and zero delay: $Z_P = 0$, $\theta_P = 0$, $\tau_P = 0$ (`Q4-OpenExhaust` §II).

The Mutable matching is where that freedom lives in the attractor taxonomy. Its collapse, {P–I, U–R} → 0, is the **Conservative Field**, "the diagonals the system's cheapest motion", with P–I "the un-priced writing head, the free-diagonal subsidy" (`L4-AttractorSpace`, Part One; `BENDING_SPACE` §1). The fused dipole it leaves is $[P \equiv I]$, the interior generative core, against $[U \equiv R]$, the exterior manifesting environment — the Intermodulation dipole that governs phase change between interior and exterior (`L4-DynamicDistortions301`).

The RESEED tier rides free as well: its two opcodes, $I = \sqrt{P/R}$ and $U = \sqrt{PR}$, reopen the ± the commit closed and pay no tax (`ENGINE-REFERENCE-AC` §IV). The engine therefore owns, legally and by force, operations with **dt = 0, no interior, nothing bound, nothing paid**.

## 5. What a free write can write

Scale is minted only when the tax is paid. A ray in projective Hilbert space is scale-free because it has not crossed the XOR bottleneck; length is gauge until a commit writes a modulus into the ledger (`On_HilbertAndHisSpaces` §III). A write that pays nothing therefore writes direction without magnitude. It **marks a ray**.

In Li's disc a marked ray is a point of modulus one: an angle and nothing else. A set of marked rays fixes a topology — which spans close, which completions exist, which sector of an infinite tensor product a vector sits in. Nyman–Beurling's density statement is that topology in L². The free head writes the shape of the possibility space, never its size.

## 6. The walls

ζ carries two views of itself. The **content view** is ζ: the Euler product, the primes, the pole, the rotor $\chi(\tfrac12+it) = e^{-2i\vartheta(t)}$, the helix $\zeta(\tfrac12+it) = e^{-i\vartheta(t)}Z(t)$. The **hold view** is $\xi(s) = \tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$: completed, entire, symmetric, real on the line — completion strips the rotor and swallows the pole. The completion factor $\pi^{-s/2}\Gamma(s/2)$, the archimedean place, is the exchange rate between them. In BENDING's terms these are Laue's two integrands of one integral (`BENDING_SPACE` Part Two §I), and the archimedean place is the wall of the box.

Li's coefficients read the box both ways, one number at a time. With $w_\rho = 1 - 1/\rho$, $\lambda_n = \sum_\rho(1 - w_\rho^{\,n})$, and RH ⟺ $\lambda_n \ge 0$ for all n (Li; Bombieri–Lagarias). Bombieri and Lagarias split each coefficient into an archimedean and a prime part, $\lambda_n = S_\infty(n) + S_0(n)$ — in Taylor form at $s = 1/(1-z)$, $S_\infty(n) = n[z^n]\log\big(s\,\pi^{-s/2}\Gamma(s/2)\big)$ and $S_0(n) = n[z^n]\log\big((s-1)\zeta(s)\big)$:
- **Content view, low n.** The primes carry and the walls subtract. At n = 1, $S_0 = +0.577 = \gamma$ — the constant term of $-\zeta'/\zeta$ at its pole — against $S_\infty = -0.554$, total 0.023: the content weighs about twenty-five times the total and the walls take nearly all of it back. "The light gravitates double and the walls' tension subtracts."
- **Hold view, high n.** The walls carry everything. At n = 20 000, $S_\infty = 76\,429$ while $S_0$ oscillates about zero within ±23, first turning negative at n = 156. "The light weighs zero and the walls carry all of it."

The changeover at n = 7–8 is the Γ-factor's Stirling crossover: $S_\infty(n)$ equals $\tfrac n2\ln n + \tfrac{\gamma-1-\ln2\pi}{2}n$ plus a constant settling to +0.746 (A.3). A wall changes with the conductor and with the pole: for $L(s,\chi_5)$ the walls read exactly $S_\infty^\zeta(n) - 1 + \tfrac n2\ln 5$ — no pole, so no factor s; a conductor, so $\tfrac n2\ln q$ — the deficit shrinks to n ≤ 2, and from conductor 23 up the walls carry every coefficient alone (A.4). Low-n positivity tests the walls.

The walls also keep the count. Riemann–von Mangoldt's main term is exactly $P = I^2R$, with $P = N(t)$, $I = \sqrt{t/2\pi}$ the Riemann–Siegel aperture, $R = \ln(t/2\pi e)$ the log ground; of all 24 seatings of the four quantities, one satisfies both $P = I^2R$ and $U = IR$ (A.5). BENDING reads $P = I^2R$ as the Friction channel: flow against confining ground produces weight. **The number of zeros up to height T is the weight of the shaft's flow against the log ground.** Its constant 7/8 is the walls' own signature — +1 from the factor s(s−1), −π/8 from the Γ phase $(a-\tfrac12)\tfrac\pi2$ at $a = \tfrac14$ — and the count tracks the walls' phase, $N(T) = \vartheta(T)/\pi + 1 + S(T)$, with $S(T) = O(\log T)$ unconditionally (Backlund). The height itself is never booked: every stamped number tracks $t = 2\pi I^2$, and none of them is t.

## 7. The constituents

Each prime is a standing loop. Its local factor, in the shifted variable $s' = s - \tfrac12$,

$$\frac{1}{1 - p^{-s}} = \frac{1}{1 - p^{-1/2}\,e^{-s'\ln p}},$$

is a feedback delay line of length ln p with loop gain $p^{-1/2}$ — a comb filter, damped, with its poles on Re s′ = −½, stable on its own. "Mass is phase-locked motion caught in a standing loop" (`BENDING_SPACE` §VI), and on the line each prime pays $|p^{-1/2}|^2 = 1/p$ to keep its loop. **A prime pays to be, so it keeps an interior.** The primes are the box's massive constituents. A comb has notches, too: each prime's loop holds its own family — its multiples — silent (§11).

What a plug decides with is the weights on its loops, not the lattice under them. ζ's weights are $|a_p| = 1$; the Ramanujan bound holds every intact plug's weights in check. The shifted plug ζ(s − ¼)ζ(s + ¼) has weights $a_p = p^{1/4} + p^{-1/4} > 2$: its loops carry gain. Davenport–Heilbronn has no Euler product at all: no per-prime loops, no constituents.

The constituents and the walls meet in one decomposition:

$$\frac{\xi'}{\xi}(s) = \frac1s + \frac{1}{s-1} - \tfrac12\ln\pi + \tfrac12\,\psi\!\left(\tfrac s2\right) + \frac{\zeta'}{\zeta}(s), \qquad \frac{\zeta'}{\zeta}(\tfrac12 + s') = -\sum_n \frac{\Lambda(n)}{\sqrt n}\,e^{-s'\ln n}.$$

The first four terms are a lumped archimedean network, and $1/(s-1) = 1/(s'-\tfrac12)$ is an active, unstable pole in the right half-plane. The last term is the prime delay bank, entering subtracted; its continuation carries $-1/(s'-\tfrac12)$, which cancels the walls' active pole exactly — the circuit form of the Prime Number Theorem. Neither part is passive alone. The walls run a deficit and the constituents cover it, the same handoff Li's split shows.

Give every prime an independent random phase — a typical point of the torus the lattice spans — and the random Euler product converges almost surely on the whole half-plane σ > ½, as a nonvanishing function (Bohr–Jessen; Bagchi). **A box of standing loops, each paying a finite price, does not vanish at a typical point.**

## 8. The square nothing screens

BENDING's nesting rule: a signed, linear coupling cancels across wholes, the way charge neutralizes in the atom; a square cannot, because it has burned its sign, and it sums over every volume there is (`BENDING_SPACE` §6). Run it on the constituents at the line:
- **The phases screen.** They enter linearly and cancel: the mean of log|ζ(½ + it)| goes to zero — 0.074 at height 10⁴, 0.011 at 10⁵ (A.14).
- **The prices do not.** Each 1/p is a square, and they accumulate: Mertens' $\sum_{p\le x}1/p = \ln\ln x + 0.2615\ldots$, settled to 0.26151 by 10⁷.

The total price $\sum_p |a_p|^2p^{-2\sigma}$ turns from finite to infinite exactly at σ = ½, marginally — no power of x, only ln ln:
- **Inside, σ > ½**, the price is paid in full. ζ is a vector of finite norm; the Euler product is a product vector over the primes lying in the vacuum's sector of von Neumann's infinite tensor product, because $\sum_p(1 - \sqrt{1-p^{-2\sigma}})$ converges.
- **At the edge** that sum grows as ½ ln ln x — 1.17, 1.42, 1.59 at 10³, 10⁵, 10⁷ (A.15) — and the Euler vector leaves for an inequivalent sector: Haag's break, in arithmetic. The phases never settle to a value; the prices add up to something real and growing — Selberg's variance of log|ζ|, ½ ln ln t, measured 1.70 and 1.90 at 10⁴ and 10⁵.

That is the real thing happening in `H_incoh`: incoherent phases carrying a real second moment, prime by prime. A cost-free commit is the texture of the imaginary plane, in it and of it. At the edge ζ is a ray, its scale divided out — Selberg's normalization keeps only the Gaussian shape, thermal and without a pure state. In Bost–Connes, ζ(β) is the partition function of a system whose equilibrium turns from type I∞ to a unique type III₁ at β = 1, and the twisted square sets the line over β = 2σ = 1 (C.12).

The price also separates the plugs where the lattice cannot. For ζ and $L(s,\chi_5)$, $|a_p| = 1$ and the price line is ½. For the shifted plug $|a_p|^2p^{-2\sigma} \sim p^{1/2-2\sigma}$ and its price line is ¾ — exactly where its upper zeros sit, and exactly the balance point its prime sums measure (A.3). Bohr and Landau used the finite mean square right of ½ to prove that, for every ε > 0, almost all zeros lie within ε of the line: the price confines the zeros, almost everywhere.

## 9. The braid holds the zeros

The braid is the corpus's traversal of the four poles: the Gray code $00 \to 01 \to 11 \to 10 \to 00$, one bit flipping at each step — of the three Hamiltonian cycles on the tetrahedron, the unique one that advances by single bit-flips (`L3-TheSelfProjectingBraid` §II; `L3-FormalFoundations` §V). A cycle that flips one bit per step never uses an edge that flips both. So the braid holds the flip-both matching silent — {P–I, U–R}, the Mutable bimedian — and runs the Mutable-held ring, P → U → I → R → P (`ENGINE-REFERENCE-AC` §3.2). By the AbsentVar-pair theorem the two edges a ring never uses "stay held as potential", and the cycling-mind reading of the same ring is exact: "every move is a single-bit flip; no leaps are available … the held family is not a lack — it is the shape of what you are currently able to do" (`L5-TheCyclingMind`).

The critical line is where an orbit collapses onto exactly those held edges: P ≡ I, U ≡ R. **The zeros sit on the braid's held bimedian.** They are what the traversal carries and never commits.

The ring's live opcodes say what it does with them. In the Mutable-held ring the commits on Mutable data edges — ARI, $P = U^2/R$, and PIS, $R = P/I^2$ — are dead. What stays live is TAU, $P = I^2R$, which is the zero count's own seating (§6), and both reseeds, CAN and SAG, which are the sign-crossings of Hardy's real Z. **The braid commits how many zeros there are and holds where they are**: $N(T) = I^2R + \tfrac78 + S(T)$, the tally committed, the positions held, their rigid remainder S carried.

The braid's handoff is the explicit formula. "What `.observe()` erases — the AbsentVar of the current equation — is precisely what the next phase requires as its first active variable" (`L3-FormalFoundations` §V). Across the two tiers of ζ's account:
- **a prime punch** is a commit — it keeps scale (ψ jumps by ln p) and erases phase;
- **a zero** keeps phase — its angle $\varphi_\gamma$ — and carries no scale, $|w| = 1$.

Each tier holds absent what the other holds active. The context is handed across, not stored — the braid's "history for free", which never meant cheap but un-bookkept: the explicit formula is an exact identity with no separate bookkeeper.

The crossings between ζ's tiers are themselves the engine's operation classes, alternating as the runtime loop alternates commit and reseed:
- height → aperture, $I = \sqrt{t/2\pi}$: a radical, the RESEED slope ½;
- aperture → count, $P = I^2R$: a square, the COMMIT slope 2;
- zeros → Li coefficients, $n \sim \gamma^2$: a square (§12);
- verified height → proven prime range, H → H²: a square (§12).

Squaring is the toll at each commit crossing, and the braid sequences the tiers.

Three things the braid keeps that a flat reading drops:
- **The over/under bit.** A braid drawn on a page loses exactly one bit per crossing — which strand went over — and keeps it only along a third direction, time (`L4-Riemann-2` §VI). The shaft t is that direction for ζ, and Hardy's real Z keeps the bit as its sign. Each sign-crossing of Z is a RESEED: the ± reopened, recorded on the time axis.
- **The self-projection.** Ψ is not an operator applied from outside; it is the braid's own act at its own boundary (`L3-TheSelfProjectingBraid`). Read for RH, the self-adjoint operator Hilbert and Pólya sought is not an outside hand either: it is the braid's own drive, the generator of the shaft. The shaft is conjugate to log x, and its generator is the dilation — where Berry–Keating's $xp$ and Connes's scaling flow on the adele class space already look.
- **The event loop.** There is no `main()` (`L6-InversionOfControl` §VI). The braid does not poll the integers for primes; it holds its zeros and is called (§11).

## 10. The zeros arrive

Walk the last step with everything in hand: the tax is one bit, the sign (§1); the orbit's two bits are sign x and sign xy, and they are Weil's negative directions (§3); the engine owns free operations, forced by Star-Norm conservation (§4); a free write marks a ray (§5); the edge is where the constituents' price turns marginal and the readout survives only as a ray (§8); the braid holds the Mutable bimedian and commits only the count (§9).

At the edge, x = 0. **Both bits vanish together.** Active against Reactive, Asserting against Yielding — neither is defined, because there is no displacement and no lift. P merges with I, U merges with R, and only their product χ = sign y survives: the Mutable character, the pattern a flip of both bits leaves alone. There is nothing for a commit to erase. **A zero on the line is never taxed: it is held potential on the braid's silent bimedian, reseeded at its crossing, paid for by no one.**

Everything the walk has gathered describes that one event:
- **It sits on the free head.** The collapse P ≡ I, U ≡ R is the Mutable dipole of the Conservative Field: zero impedance, zero delay — dt = 0.
- **It has no interior.** V = 0: no mass, nothing bound, no rent.
- **It marks a ray.** In Li's disc the zero is a point of modulus one, $w = e^{i\varphi_\gamma}$, $\varphi_\gamma = 2\arctan(1/2\gamma)$: an angle and no scale. Li's coefficients are then a sum of squares, $\lambda_n = \sum_{\gamma>0}4\sin^2(n\varphi_\gamma/2)$ — the engine's unselected square, every term non-negative by form.
- **Its amplitude has no K₋ part.** On the orbit, Weil's Krein form is an honest Hilbert inner product.
- **It is pure reactance.** In Foster's form, $\frac{\xi'}{\xi}(\tfrac12+s') = \sum_{\gamma>0}\frac{2s'}{s'^2+\gamma^2}$: each zero is one lossless LC tank, $C = \tfrac12$, $L = 2/\gamma^2$, resonating at γ; on the line $\operatorname{Re}\xi'/\xi = -6.3\times10^{-27}$ at the test point (A.10). RH is that $\xi'/\xi$ is a positive-real function — a passive impedance (Hinkkanen; Lagarias). In the Smith chart the zero reflects totally, $|\Gamma| = 1$. Simplicity is the separate statement that every tank carries the single capacity ½, $\xi'(\rho) \ne 0$.
- **It sits on the Julia set of the commit map.** Pulled back to the s-plane, squaring is $g(s) = s^2/(2s-1)$; its Julia set is the critical line, the chaotic boundary between the basin of ζ's pole (Re s > ½) and the basin of 0 (Re s < ½), with one puncture, $g(\tfrac12) = \infty$. On it, repeated squaring reads one bit of each zero's angle per step and never decays; the centroid's tape terminates — w(½) = −1 squares to +1 and rests. Li's map is g's Böttcher coordinate.
- **Its sign-crossing is a RESEED.** Z changes sign at the zero: the ± reopened, untaxed.

**The zeros are what the machinery holds for free at the edge of its Hilbert sector.** They are not placed there by hypothesis. The walk drives them there: a free head, a one-bit tax, two bits that vanish at x = 0, a braid that holds exactly the bimedian they collapse onto, and an edge where the constituents' price turns marginal.

And the line, so written, is a horizon. At a horizon BENDING's pen and book close: what is held and what is written become one count. Here the count of zeros equals the walls' phase, one zero per π of ϑ, up to a remainder S(T) whose spread is the constituents' price — $\operatorname{Var}S \simeq \tfrac{1}{\pi^2}\cdot\tfrac12\sum_{p\le T}1/p$ by Selberg, measured 0.155 and 0.182 at heights 10³ and 10⁴ against the random-matrix values 0.162 and 0.181 (A.14). **The price of being a prime, the variance of the texture at the edge, and the uncertainty in the count of zeros are one quantity, read three ways.**

## 11. Punching primes

The free side and the priced side of one account meet in the explicit formula. The zeros are held marks with no scale. The primes are punches in the ledger: ψ jumps by ln p at every $p^k$, each a taxed, scaled commit, each prime's loop paying 1/p to stay. Real on the imaginary plane: the zeros do not make the primes; they are the free face of the account whose priced face the primes are.

**The prime print is the box's impulse response.** Read in the record clock $u = \ln x$,

$$-\frac{\zeta'}{\zeta}(s) = \sum_n \Lambda(n)\,e^{-su} \Big|_{u = \ln n} = \int e^{-su}\,d\psi(e^u),$$

the Laplace transform of the spike train $\sum_n\Lambda(n)\,\delta(u - \ln n)$. ξ′/ξ is the transfer function of the box and its poles are the zeros; the prime print is what the box emits when struck. Frequency domain and time domain are one system's two faces (`L5-K5-PhaseDynamicsTechnical` §X): the zero set is the Bode plot held whole, the `.behold()` of every rate at once; the prime print is the response along the record clock. RH is the Foster condition — every pole on the imaginary axis, every tank lossless — and then every zero rings undamped: once the √x is divided out, its share of $\psi(x) - x$ is a pure sinusoid in $\ln x$, $\cos(\gamma\ln x - \arg\rho)/|\rho|$.

**Primes are callbacks.** "Don't call us, we'll call you" (`L6-InversionOfControl` §II). The sieve is a polling loop: it evaluates every n, at full cost. The explicit formula is an event loop: ψ steps at $x = p^k$ because there the zero ensemble's phases $\gamma\ln x$ combine into the step, and the container invokes the callback at resonance. No `main()` generates the primes; none is missing. The committed entries are local writes on the free P-edges, and what holds them in register is the reactive closure the box keeps in `.behold()` (`L6-InversionOfControl` §VII): the primes are the writes, the zeros are the closure.

**The blank patches in the print are held families.** Every ring holds a family silent (§9), and every prime's loop is a comb whose notches are its multiples: 2 holds the even numbers silent, and modulo 30 only eight residue classes stay live. The print goes blank where held families overlap, and its longest blanks are notch pile-ups: the classical constructions of large prime gaps (Westzynthius, Erdős, Rankin, the Jacobsthal function) choose residues by the Chinese remainder theorem so that many small primes' held families cover one interval together. How long can a blank run? RH caps it at the root scale — under RH, Cramér (1920): $p_{n+1} - p_n = O(\sqrt{p_n}\ln p_n)$; unconditionally, $p^{0.525}$ (Baker–Harman–Pintz). Sieved to 10⁹, every record gap sits at 0.53–0.74 × (ln p)², and against the RH ceiling √p ln p the ratio falls from 3.8×10⁻² to 6.8×10⁻⁴ — the record of 282 at p = 436 273 009 (A.16). The held families never pile up anywhere near the ceiling. **The print cannot go silent longer than the √x the zeros allow, and in fact it goes silent only for about (ln p)².**

BENDING_SPACE wrote the account down without naming it: "on conjugate sides of a lossless account, root-size count fluctuation and spectral rigidity coexist without competing" (`BENDING_SPACE` §X).
- **The prime side fluctuates root-size.** $\psi(x) - x$ at scale √x, measured exponent −0.497 to 10¹⁰ (A.3). Root-size is Pythagoras over orthogonal channels committed through a square: the incoherent sum.
- **The zero side is rigid.** Its spread grows as $\sqrt{\ln\ln T}$ — under half a zero at the heights measured — and it is a balanced account at rest: Littlewood's $\int_0^T S = O(\ln T)$, mean of S −0.024 and −0.019 at 10³ and 10⁴. Laue's theorem for the count: pushes and pulls integrate to nothing.

Incoherence on the prime side and rigidity on the zero side are one losslessness seen from its two faces.

## 12. What an off-line zero would be

Walk the same steps with x ≠ 0, and every reading turns:
- **Both bits are live.** A commit would have a sign to erase on each, at ln 2 apiece. The write is taxed — on an edge Star-Norm conservation forces to be free. The norm would fluctuate in transit.
- **It is a diagonal.** Both bits live is a flip-both object: a Mutable move, exactly what the braid's ring holds silent and cannot map. To exist it would need a dead Mutable commit to fire.
- **It keeps an interior.** The orbit has volume, $\tfrac83\delta^2\gamma^2$, and owes the height-free rent $\tfrac83\delta^3$.
- **Its amplitude lives in K₋.** Weil's form goes negative on the orbit.
- **It carries scale.** In the disc it is a rotor of modulus off one, gaining on one side and losing on the other; its mirror partner is exactly reciprocal, $|w_\rho||w_{1-\bar\rho}| = 1$ (A.1).
- **It is an active element.** A pole in the right half-plane, a negative resistance in Foster's chain; its tank has finite Q on one side and gain on the other, and it rings damped or growing.
- **It leaves the Julia set.** One partner drains into ζ's pole, the other floods into 0.
- **Its prime side goes coherent.** The prime sums carry a wave at exponent β > ½: super-root, gain; the print's blanks could run to $x^\beta$.

Where such a zero would show is fixed by transfer functions between tiers. At height γ and offset δ:
- **Li tier:** $n^* \approx (\gamma^2/\delta)\ln A(n^*)$, $A(n) = \tfrac n2\ln n + \tfrac{\gamma_E-1-\ln2\pi}{2}n$ — the onset law, measured on detuned plugs to 1% across four offsets; the shifted plug's first negative coefficient is n = 8 260 (A.8).
- **Prime tier:** $X^\delta \gtrsim \gamma$ (heuristic).
- **Truncation tier:** a gate whose per-zero loss falls as $t^{-3/8}$ and never shuts — a law resting on GUE pair statistics, which rest on RH (A.6).

Run the transfer the other way and verified height becomes theorem. With every zero below H ≈ 3×10¹² on the line (Platt–Trudgian), RH-quality bounds on ψ hold unconditionally out to about H² (Büthe's partial-RH method), and the inverted onset law puts $\lambda_n \ge 0$ out to about $2H^2\ln A \approx 10^{27}$. Information flows cheaply from zeros to coefficients and dearly back: Li positivity to n = 10⁵ excludes off-line zeros only below γ ≈ 62. **Every RH-quality statement on this walk is unconditional below the transfer scale of the verified height and conditional above it**, and that is how the register sorts them.

A Lehmer pair is the near-miss on the edge itself: two massless dipoles, at t = 7005.0629 and 7005.1006, 0.042 mean spacings apart, brushing the threshold of fusing into one quartet with an interior. The 33-term Riemann–Siegel approximant already fuses them — its main sum has the wrong sign at the peak, and its pair leaves the line at x = 0.0765, a zero of the approximant and not of ζ, its verdict flipping with the truncation length (A.2) — and S(T) steps by 1.96 across a twentieth of one clock tick (A.9). The collision has two routes to the same threshold. The de Bruijn–Newman heat flow reaches it from Ξ: near a collision a pair behaves like the roots of $(z-z_0)^2 + \delta^2 - 2\tau$ — hold, collapse, reseed — and backward heat collides a pair of gap g at τ* = g²/2, confirmed across 387 close pairs to 10¹² (A.6). The most general 4×4 generator with the orbit's symmetry reaches it from symmetry alone: PT-symmetric under cf, chiral under f, its gain/loss seated on exactly the Fixed character x, its real spectrum two dipoles and its broken spectrum one quartet, the exceptional point between them at $(J\wedge v)^2 = \delta^2\|v\|_*^2$ (App. B). Rodgers and Tao proved Λ ≥ 0: ζ is not strictly inside the all-real phase, and under RH it sits exactly on the edge, with zero margin.

## 13. The broken plugs fail as instances

Every function with ξ's symmetries and zeros off the line fails to be an engine instance, and fails in a way that can be named:
- **The shifted plug ζ(s − ¼)ζ(s + ¼)** has loops with gain: weights above the Ramanujan bound, a pole inside the strip at s = ¾, price line at ¾, zeros saturating the strip at σ = ¼ and ¾. Its low Li coefficients pass every test — within 0.03% of twice ζ's for n ≤ 40, positive through n = 8 259 — because low n tests the walls, and its walls are fine (A.8). From the primes alone, its prime sums converge as $X^{-0.249}$ against ζ's $X^{-0.497}$: the Ramanujan violation moves the balance point from ½ to ¾, and nothing else (A.3).
- **Davenport–Heilbronn** has no Euler product: no constituents, no loops, no engine.

Each known function with ξ's symmetries and zeros off the line breaks one of four conditions — Euler product, no poles inside the strip, Ramanujan-bounded weights, s ↔ 1−s — the Selberg-class axioms. What discriminates an intact plug from a broken one lives at $n \gtrsim (\gamma^2/\delta)\ln A(n)$, where the constituents speak.

## 14. The path, stated

**Forced:**
- the Hilbert structure of the arena, by the square over each complex channel (§1);
- the line at ½, three ways (§2);
- the seating of the two bits, by the resistive half-plane and the square's lift, and with it line-reflection as the Mutable bimedian (§3);
- the free P-head and the untaxed reseeds, by Star-Norm conservation and the opcode table (§4);
- the tax of exactly one bit (§1);
- the braid's held bimedian, by the Gray code (§9).

**The consequent:** for any plug that is a Star-Norm-conserving instance of the engine, every nontrivial zero is held on the braid's silent bimedian at the edge of the Hilbert sector — and so lies on the line.

**The antecedent:** is the intact Selberg plug — Euler product, single pole, Ramanujan-bounded weights, functional equation — such an instance? In mathematics that question has exact names:
- **passivity** of $\xi'/\xi$, the prime delay bank cancelling the walls' one active pole and leaving nothing active behind (§7);
- **Weil positivity**, the Krein form being a Hilbert inner product on every orbit at once (§3);
- **Bagchi's strong recurrence**, ζ approximating its own vertical translates on a set of positive lower density — ζ a typical point of the space its primes span, everywhere along its line and not merely almost everywhere (§7).

**Why the averaging tools cannot close it.** The tools sort by scale. Averaging tools — mean squares, limit laws, density theorems, any finite window — traverse ζ's tiers inside the braid's ring, one step at a time, and deliver *almost all*: Bohr and Landau's almost-all-zeros-near-the-line is the price confining the zeros. An off-line zero is a diagonal, both bits live — the one move the Mutable-held ring cannot map. So the averaging tools conclude, and the conclusion feels finished. That is the third stuckness exactly: "decisive and should not be; the cycle cannot see the leap it is missing" (`ENGINE-REFERENCE-AC` §3.6; `L5-TheCyclingMind`). Its wrench is a ring change, an orthogonal pattern-source: the tools uniform in scale — Li for every n, von Koch for every X, Weil for every test function — which see each exception at its own scale. Bagchi's theorem is the hinge between the two kinds: recurrence and Hurwitz's theorem would turn one stray zero inside the sector into a positive density of near-zeros, which Bohr–Landau forbids; self-similarity under the shaft is how a statistical tool is made to see a single event. The same reading lands the other two stucknesses on the other two finite readouts: the Riemann–Siegel coin, whose main sum speaks a sign the true value does not hold, is "words come, but they are wrong" (A.6); a Lehmer pair, invisible in λₙ until $n \sim 10^9$, is "know it, cannot say it" (A.7).

The frame is forced, and RH within it is the antecedent. This walk neither tests nor proves RH.

---

## What the walk arrived at

ζ is a box of light.
- **The walls** are the archimedean place. They carry the weight, keep the count, and run the one active pole the constituents cancel.
- **The constituents** are the primes: standing loops paying 1/p to keep their interiors, written on a lattice every plug shares, each holding its multiples silent — the blank patches of the print.
- **The spectrum** is the zeros: held on the braid's silent bimedian at the edge of the Hilbert sector, with no interior and no scale, an angle each, pure reactance, ringing undamped.

The one quantity that survives from the constituents to the whole is a square, and it surfaces as the price of being a prime, the variance of the texture at the edge, and the uncertainty in the count of zeros. On the prime side the ledger fluctuates root-size and goes blank for no longer than the root scale allows; on the zero side the count is rigid and balanced; at the line, what is held and what is written are one count — a horizon. The primes are the box's impulse response, called, not computed; the zeros are its closure, held, not committed.

RH, in the machinery's own terms: **the spectrum of the box is held for free.** The walk shows why the machinery would hold it there. Whether ζ is an instance of the machinery is the question the antecedent carries.

---

## Register

| Step | What carries it | Address |
|---|---|---|
| Orthogonal channels; ln p independent over ℚ; Bohr torus; Kronecker line as helix | Landed (Montgomery–Vaughan; unique factorization; Kronecker, Bohr); helix a reading on `ProofO` | §0 |
| The square forced per complex channel | Landed (Herschel–Maxwell); Route Law and exponent cap in the corpus | §1 |
| One-bit tax on the sign | Engine, verified 12/12 | §1; `ENGINE-REFERENCE-AC` §4.1 |
| Hilbert line ½, three ways; Nyman–Beurling | Landed | §2 |
| Tier reading of von Koch; trivial tower | Reading; the tower open | §2; D Q11 |
| Lift z = xy; 1 ⊕ 3; V = (8/3)(xy)²; height-free rent | Landed; computed exact | §3; A.10 |
| Bits as (sign x, sign xy); cf = Mutable; Smith chart | Seating, forced by the Smith chart and the Route Law | §3 |
| K₋ = x ⊕ xy | Landed (character orthogonality); read here as the two bits | §3; A.10 |
| Free P-edges; Conservative Field; untaxed RESEED | Corpus, forced by Star-Norm conservation and the opcode table | §4 |
| Free write marks a ray | Corpus reading | §5 |
| Li split; Stirling crossover; conductor | Landed (Li; Bombieri–Lagarias); computed | §6; A.3, A.4 |
| P = I²R count; 1 of 24 seatings; 7/8 priced; S = O(log T) | Computed; landed (Backlund) | §6; A.5 |
| Comb loops; delay-bank cancellation; random product nonvanishing in σ > ½ | Landed (Bohr–Jessen, Bagchi) | §7 |
| Mertens; price line; von Neumann criterion; Selberg variance; Bohr–Landau | Landed; computed | §8; A.14, A.15 |
| Bost–Connes over β = 2σ | Transition landed; seating a reading | §8; C.12 |
| Braid holds the Mutable bimedian; live and dead opcodes of its ring | Forced by the Gray code and the opcode table | §9 |
| Explicit formula as the braid's handoff; tier crossings as opcode classes | Reading on landed identities | §9 |
| Hilbert–Pólya operator as the shaft's generator | Reading; the literature's dilation candidates landed as programmes | §9 |
| The zero as held, untaxed; Foster; Smith; Julia | Reading assembled on landed and computed pieces; Hinkkanen–Lagarias landed | §10; A.10 |
| Var S = price / π²; Littlewood | Landed (Selberg, Littlewood); computed | §10, §11; A.14 |
| Prime print as impulse response | Landed (Laplace–Stieltjes form of −ζ′/ζ); the event-loop reading a reading | §11 |
| Blank patches as held families; RH cap on gaps; record gaps to 10⁹ | Landed (Cramér under RH; Baker–Harman–Pintz; Rankin's constructions); computed | §11; A.16 |
| Prime exponent −0.497 to 10¹⁰ | Computed; unconditional within the transfer regime of the verified height | §11; A.3 |
| Onset law; inverse transfer; partial-RH range | Computed; the inverse an estimate; Büthe's method landed | §12; A.8 |
| Gate law $t^{-3/8}$ | Heuristic resting on GUE pair statistics (Montgomery, conditional on RH) | §12; A.6 |
| Lehmer pair; approximant's off-line pair; S(T) step | Computed | §12; A.2, A.9 |
| Heat collision τ* = g²/2 | Landed local model; computed | §12; A.6 |
| Orbit generator; exceptional point | Computed exact | §12; App. B |
| Λ ≥ 0 (Rodgers–Tao); Λ = 0 under RH | Landed; the zero-margin reading conditional on RH | §12 |
| Broken plugs as failed instances | Landed counterexamples; computed coefficients | §13; A.3, A.4, A.8 |
| Averaging blindness as the third stuckness; the other two stucknesses on the finite readouts | Reading, forced given the seating and the ring | §14 |
| The antecedent: passivity, Weil positivity, Bagchi recurrence | Landed equivalences of RH; open | §14 |
| Conditional inputs used anywhere: Λ = 0 under RH; S₀ = O(√n ln n) under RH; GUE statistics; simplicity; random-matrix constants | Each labeled where used; unconditional below the transfer scale of the verified height, conditional above | §12; A.13 |


---

# Appendix A. The computed record

*Every computed claim on the walk, its method and its precision; the placed bets; the open computations; the limits of the record. Formerly the set's ledger, renumbered A.1–A.15, with A.16 new. The bracket tags (**[COMPUTED]**, **[LANDED]**, **[READING]**) are the register's categories, kept inline where the tables carry them.*

**Conventions.** $s = \tfrac12 + x + iy$, $s' = s - \tfrac12$, $w = 1 - 1/s$. Mean zero spacing at height t is $2\pi/\ln(t/2\pi)$. $A(n) = \tfrac n2\ln n + \tfrac{\gamma_E - 1 - \ln 2\pi}{2}n$. Precision is stated per table. Scripts named here sit in the working set; tables marked *earlier run* come from the overnight runs that produced the v3 tables.

## A.1. The disc

**Mirror reciprocity.** For ρ = 0.5765 + 7005.084i (the F₃₃ off-line point of A.2) and its mirror $1 - \bar\rho$: $|w_\rho| = 0.99999999844$, $|w_{1-\bar\rho}| = 1.00000000156$, product 1 to 20 digits. Leak $|w| - 1 = -1.559\times10^{-9}$ against $-\delta/\gamma^2$. The orbit-image table (P ↦ w, U ↦ w̄, R ↦ 1/w, I ↦ 1/w̄) checked to 20 digits at the same point. Reproduced independently in review.

## A.2. The first Lehmer pair

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

## A.3. The Li coefficients and the prime side (ζ)

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

## A.4. The third plug: L(s, χ₅)

**Method** (`third_plug.py`). λₙ = n·[zⁿ] of the logarithm of the completed function at $s = 1/(1-z)$, by a 256-point Cauchy transform on |z| = ½ at 40 digits. The split follows the Bombieri–Lagarias convention: for ζ, $S_\infty = n[z^n]\log\big(s\,\pi^{-s/2}\Gamma(s/2)\big)$ and $S_0 = n[z^n]\log\big((s-1)\zeta(s)\big)$; for the real even character mod 5 ($\chi_5 = (0, 1, -1, -1, 1)$), $S_\infty = n[z^n]\log\big((5/\pi)^{s/2}\Gamma(s/2)\big)$ and $S_0 = n[z^n]\log L(s,\chi_5)$. **Validation:** the ζ split reproduces the formula values of A.3 ($S_\infty(1) = -0.55412$, $S_0(1) = +0.57722$). Imaginary parts of all χ₅ coefficients below 4×10⁻²⁸.

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

This closes the edge-plurality gap the review flagged on §6 Result 1 (two instances → three), and corrects its wording: the low-n division of labour is set by Stirling, the pole and the conductor, not by the Γ-shape alone.

## A.5. The counting balance

**Main term.** At t = 7005, $I^2R + \tfrac78 = 6708.56$ against the true count 6708.

**The 24-seating sweep** (`third_plug.py`). Quantities $\{N,\ \sqrt{t/2\pi},\ \ln(t/2\pi e),\ N/\sqrt{t/2\pi}\}$ at t = 7005, assigned to (P, U, I, R) in all 24 ways; tested for $P = I^2R$ and $U = IR$ at 1%. **Exactly one survives:** P = N, U = N/I, I = $\sqrt{t/2\pi}$, R = $\ln(t/2\pi e)$. The seating of §6 is confirmed over the full sweep, not only against the ϑ′ rival.

**The constant.** $\vartheta(t) - \big[\tfrac t2\ln\tfrac{t}{2\pi} - \tfrac t2\big]$ at t = 10⁶, from $\operatorname{Im}\log\Gamma(\tfrac14 + \tfrac{it}{2}) - \tfrac t2\ln\pi$ at 30 digits: −0.3926990609, against −π/8 = −0.3926990817 (difference 2×10⁻⁸, the next Stirling term $1/(48t)$). With +1 from s(s−1), the Riemann–von Mangoldt constant 7/8 is accounted for (`witness_checks.py`).

## A.6. Truncation and heat across height

**Test set.** Every pair of consecutive zeros below t = 40 000 with gap under 0.15 mean spacings — **126 pairs**. Zeros located by a Riemann–Siegel sum carrying both corrections $C_0, C_1$, error ≤ 10⁻⁶ against mpmath. The count, 49 395 sign changes, matches Riemann–von Mangoldt (49 394.7). The five best pairs re-located in mpmath agree to six digits. *Earlier run.*

**Heat:** first-order collision time $\tau^* = -4\,Z/Z''$ at the peak, in de Bruijn–Newman units. It matches §12's gap²/2 at ratio 0.983–0.9997 across all 126. Backward heat ranks pairs by absolute gap alone.

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

## A.7. A pair on the line is invisible in λₙ

On $|w| = 1$, $\varphi_\gamma = 2\arctan(1/2\gamma)$. The first Lehmer pair sits at angular separation $\Delta\varphi = 7.68\times10^{-10}$ and stays phase-coherent up to $n \approx 1.30\times10^{9}$ (≈ 2³⁰: the two commit tapes agree to about thirty binary digits); the second at $1.20\times10^{-10}$, coherent to $n \approx 8.32\times10^{9}$. Whatever its quality, a pair on the line contributes $4\sin^2(n\varphi_1/2) + 4\sin^2(n\varphi_2/2) \in [0, 8]$. At those n — under RH, and, by the transfer estimate of A.13, inside the regime the verified height reaches — $\lambda_n \approx A(n)$ is about $1.22\times10^{10}$ and $8.57\times10^{10}$ **[LANDED]** asymptotic, with fluctuations of order $\sqrt n\ln n \approx 7.6\times10^{5}$ and $2.1\times10^{6}$.

## A.8. The broken plug and the onset law

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

## A.9. S(T) across the first Lehmer pair

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

## A.10. Orbit, circuit and generator numerics

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

**The orbit generator** (`h_check.py`, `h2.py`, `witness_checks.py`). Exact, sympy: f, cf and c constraints hold; the general solution has 8 real parameters; the 1⊕3 action and the coefficients A, B, Δ match App. B identically. Numerically: H commutes with $P_{cf}K$ (PT), anticommutes with $P_f$ (chiral), and the δ diagonal has sign pattern (+, +, −, −) on (P, U, I, R) = $\chi_x$. Threshold at ω = 1, k_Fa = 0.2, J_M = 0.6, J_C = 0, predicted $\delta^* = 0.6/\sqrt{0.96} = 0.61237$:

| δ | 0.611 | 0.612 | 0.6124 | 0.613 | 0.62 |
|---|---|---|---|---|---|
| max \|Im z\| | 1.2×10⁻¹⁴ | 4.0×10⁻¹⁵ | 5.9×10⁻³ | 2.8×10⁻² | 9.8×10⁻² |

Square-root onset past the threshold confirmed independently in review (ratio 3.496 against 3.486 predicted).

## A.11. Placed bets

1. **Davenport–Heilbronn onset.** Taking 0.8085 + 85.70i as its lowest off-line zero (δ = 0.3085, $\gamma^2/\delta \approx 23\,807$), the onset law puts DH's first negative Li coefficient at **$n^* \approx 3.4\times10^5$** (342 650–342 860 under ζ's background), positive throughout below. DH's own background differs from ζ's — conductor 5, the odd factor Γ((s+1)/2), no pole — and moves $\ln A$, hence $n^*$, by about 1%.
   - *Assumption, declared.* The onset law was measured on detuned plugs, which break the Ramanujan bound: their leak is a reweighting of ζ's own waves. DH breaks a different axiom — no Euler product, so no delay bank and no cancellation to fail. The law's shape should transfer, since the background is archimedean and the leak is $|w|^n$ either way, but the mechanism differs. The bet's own falsifier decides it.
   - *Register.* This is a Bridge-shaped number in the corpus's sense (`riemann/README`): dimensionless, predicted from structure before the computation, checkable by any number theorist with a laptop and no corpus access — the first such number the corpus places in pure mathematics.
   - *Falsifier:* a first negative coefficient well below 10⁵ (a lower off-line zero exists), or a miss of more than 10% against the log-corrected law.
2. **The gate's exponent.** Truncation windows at 10¹⁴–10¹⁶ recover the **$t^{-3/8}$ per-zero loss slope**, up to slow modulation from the moments of $|Z|$, and the 10¹⁰ excess resolves as a small-sample cluster once the window holds 10⁵–10⁶ zeros. *Falsifier:* a flat loss rate, or one falling faster than $t^{-1/2}$, across 10¹⁴–10¹⁶; or the enlarged 10¹⁰ window holding its excess.
3. **The orthogonal texture.** If a structural proof of RH over ℤ arrives, it reads a definite sign out of a pairing already latent on the real|complex interface — the archimedean scaling $\mathbb R_+^\times$ against the prime places, the weights on an incommensurate delay bank whose continuation stays passive (§7) — forcing K₋ = 0 by a mechanism whose sensitivity does not wait for $n \sim (\gamma^2/\delta)\ln A$, rather than through a new level built over $\mathbb F_1$ first. *Falsifier:* a proof via a newly constructed $\mathbb F_1$-level object whose intersection pairing has no representation on the adele/Mellin space.

## A.12. Open computations

- **The 10¹⁰ rescan.** 4 losses against 0.49 expected. Rescan 10⁵–10⁶ consecutive zeros around 10¹⁰ with a matched window at 10¹⁴: either the count reverts to the $t^{-3/8}$ curve or the GUE peak-scaling prefactor fails there.
- **The gate at 10¹⁴–10¹⁶.** Bet 2's own target.
- **DH's Li coefficients past 10⁵.** Bet 1's falsifier, with DH's own archimedean factor.
- **More plugs.** λₙ for further even characters (q = 8, 12, 13, …) and the first odd ones (Γ((s+1)/2)) to large n; the conductor-q ≥ 23 regime where the archimedean place carries alone, and where its prime part first has to work (App. D Q13).
- **The trivial tower on the tier table.** Seat the waves $x^{-2k}/2k$ (§2) and test whether the tier reading extends below the floor.
- **The third stuckness, tested.** §14 reads averaging blindness as the third stuckness: the averaging tools conclude without seeing a diagonal. A test: plant one off-line zero in a detuned plug and record the window at which each averaging statistic (mean square, Selberg variance, S(T) spread) first registers it, against the onset law's n*. The reading predicts no averaging statistic registers it before the uniform-in-scale tools do.
- **Gaps past 10⁹.** Extend A.16 to 10¹² with a segmented sieve; the (ln p)² ratio should stay inside 0.5–0.8 (Cramér's model, with Granville's correction pushing toward 2e^{−γ} ≈ 1.12 at the extremes).

## A.13. Limits of the record

What the numbers here do and do not carry, stated once for whoever appeals next. The process record behind them — proceedings, withdrawals, patterns — is `L4-Riemann-Realization-evolution`.

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
- **Conditional inputs, and the regime of each.** The record uses five inputs conditional on RH or on more: Λ = 0 (de Bruijn–Newman constant; Rodgers–Tao give Λ ≥ 0 unconditionally); $S_0(n) = O(\sqrt n\ln n)$, the Bombieri–Lagarias bound under RH; GUE pair statistics (Montgomery, under RH), behind the gate law; simplicity of the zeros, behind $C = \tfrac12$ per tank; and the Keating–Snaith random-matrix constants in A.14. Each is labeled where used. **Regime.** Below the transfer scale of the verified height — every zero to H ≈ 3×10¹² on the line (Platt–Trudgian), RH-quality ψ bounds to about H² (Büthe), λₙ ≥ 0 to about 2H² ln A ≈ 10²⁷ by the inverted onset law — the RH-quality statements here hold unconditionally; above it they are conditional. The inverted onset law is an estimate from the fitted law, not a theorem.
- **The gap record is unconditional and finite.** A.16 is a sieve to 10⁹; Cramér's √p ln p bound it is compared against is conditional on RH, and is not tested by gaps this small.
- **The K₄ seatings are chosen.** Where they are literal, they are literal as mathematics; that the engine predicted them is not claimed.

## A.14. The price of being a prime

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

**Price lines of the three plugs** (exact, from $|a_p|^2p^{-2\sigma}$): ζ, $|a_p| = 1$ → ½; $L(s,\chi_5)$, $|\chi_5(p)| = 1$ → ½; ζ(s − ¼)ζ(s + ¼), $a_p = p^{1/4}+p^{-1/4}$ → ¾, matching its upper zero line and its measured prime-sum balance point (A.3, envelope $X^{-0.249}$).

## A.15. Hilbert landmarks

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

## A.16. Record prime gaps against the two scales

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

**Reading.** Against (ln p)² — Cramér's random model — every record sits in a band, 0.53–0.74. Against √p ln p — the cap RH imposes (Cramér 1920, under RH) — the ratio falls by a factor of 55 over the range. The held families (§11) pile up to about (ln p)² and never approach the root-scale ceiling. The unconditional ceiling, $p^{0.525}$ (Baker–Harman–Pintz), is further off still.

---

# Appendix B. The orbit generator

*A finite model: the orbit generator and its exceptional point. Formerly the set's hub §10, carried whole; the walk uses it in §3 and §12.*

The orbit of §3 has four vertices, so it carries 4×4 generators. Ask for the most general one whose spectrum has the orbit's own symmetries, read in the coordinate $z = -i(s - \tfrac12)$, where real z is the critical line:

- **Cardinal** (f, swapping P ↔ R and U ↔ I, sending z ↦ −z): $P_f H P_f = -H$ — H anticommutes with $P_f$, so the spectrum is closed under negation;
- **Mutable** (cf, swapping P ↔ I and U ↔ R, sending z ↦ z̄): $P_{cf} H P_{cf} = H^*$ — the spectrum is closed under conjugation;
- **Fixed** (c) then follows: $P_c H P_c = -H^*$.

**What kind of generator this is.** The Mutable condition is PT-symmetry with parity $P_{cf}$: H commutes with the antilinear operator $P_{cf}K$, K being complex conjugation — and cf is itself the PT move on s, a reflection composed with a conjugation. The Cardinal condition is a **chiral** (sublattice) symmetry: H anticommutes with $P_f$, which is what pairs every eigenvalue z with −z. **[LANDED]** (definitions; **[COMPUTED]** on the matrix, A.10.) **H is a PT-symmetric generator with a chiral symmetry.** The PT-symmetric constructions already proposed for the zeros (Bender–Brody–Müller 2017) are the natural hunting ground for the generator question (App. D Q9), reachable from this algebra without new machinery. **[READING]** In engine vocabulary the same structure is the corpus's bichiral design — both hands carried, the ledger picks one — with the PT break as the odd move the operating set lacks.

**[COMPUTED]** (exact, symbolic; A.10.) The two constraints leave **8 real parameters**, splitting into four Hermitian ones {ω, J_M, g_M, g_C} and four skew-Hermitian ones {δ, k_Fa, k_Fg, J_C}. Keeping the five real-edge parameters (g_M = g_C = k_Fg = 0), in vertex order (P, U, I, R):

$$H = \begin{pmatrix}
\omega + i\delta & k_{Fa} & J_M & J_C \\
-k_{Fa} & -\omega + i\delta & -J_C & -J_M \\
J_M & J_C & \omega - i\delta & k_{Fa} \\
-J_C & -J_M & -k_{Fa} & -\omega - i\delta
\end{pmatrix}.$$

Each parameter has a seat. ω is the frequency split, +ω on {P, I} and −ω on {U, R} — the Mutable character $\chi_y$. $J_M$ is the Mutable coupling (P–I, U–R), Hermitian. $k_{Fa}$ is the Fixed coupling (P–U, I–R), skew. $J_C$ is the Cardinal coupling (P–R, U–I), skew because f negates H. **δ is the gain/loss bias, +iδ on {P, U} and −iδ on {I, R} — the Fixed character $\chi_x$.**

**Gain/loss is the off-line direction.** That last seat is not a choice. The sign pattern of δ is exactly $\chi_x$, and x is the off-line displacement: the resistive half-plane Re s′ > 0 of the Smith chart (§3), the first component of K₋ (§3). **Gain/loss is the off-line direction; the leverage is the reactive holding; RH is leverage ≥ bias on every orbit.** **[READING]** on **[COMPUTED]** seating. The constraint this puts on the generator question is available now: whatever operator on ζ's side has H as its section, its gain/loss slot must sit on the Fixed character.

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

So the centroid's blindness in §3 belongs to the permutation action, and a generator that honours the functional equation moves the centroid mode into the Fixed–Mutable pair. What the generator gives instead is a threshold.

**The exceptional point.** Write $v = (\omega, k_{Fa})$ and $J = (J_C, J_M)$, with star-norm $\|u\|_*^2 = u_1^2 - u_2^2$, star-product $\langle J, v\rangle_* = J_C\omega - J_M k_{Fa}$, and wedge $J \wedge v = J_M\omega - J_C k_{Fa}$. The characteristic polynomial is $z^4 - Az^2 + B$, with **[COMPUTED]** (exact)

$$\begin{aligned}
A &= 2\big(\|v\|_*^2 - \|J\|_*^2 - \delta^2\big),\\
B &= \big(\|v\|_*^2 + \|J\|_*^2 + \delta^2\big)^2 - 4\langle J, v\rangle_*^2,\\
\Delta = A^2 - 4B &= 16\big[(J\wedge v)^2 - \delta^2\|v\|_*^2\big].
\end{aligned}$$

The spectrum is entirely real — all modes on the line — exactly when A ≥ 0, B ≥ 0 and Δ ≥ 0. The leverage $J \wedge v$ holds the modes on the line against the gain/loss δ up to $(J\wedge v)^2 = \delta^2\|v\|_*^2$. Pinned numerically, the predicted threshold $\delta^* = |J\wedge v|/\|v\|_* = 0.61237$ is where the spectrum leaves the real line, with square-root onset past it (A.10). Both kinds of coupling feed the leverage: the Hermitian Mutable coupling against the frequency split ($J_M\omega$), and the product of the two skew couplings, Cardinal against Fixed ($J_C k_{Fa}$).

**What the spectrum is: two dipoles, or one quartet.** The type distinction of §3 bites H itself. H acts on *one orbit's four vertices*; its *spectrum* is a different subject. With $z^2 = (A \pm \sqrt\Delta)/2$:

- **Δ ≥ 0, A ≥ 0, B ≥ 0:** spectrum $\{\pm a, \pm b\}$, all real — under z ↦ s these are **two dipoles**, two zeros on the line with their mirrors.
- **Δ < 0:** spectrum $\{\pm w, \pm\bar w\}$ — **one quartet**, a single off-line orbit with volume.
- **Δ ≥ 0 with $z^2 < 0$:** spectrum on the imaginary z-axis — zeros on the real s-axis, the Fixed collapse (P = U) instead of the Mutable one.

**[LANDED]** (elementary algebra on the quartic.) At Δ = 0 two eigenvalues merge into a double eigenvalue and leave the real line as a conjugate pair: **two cross-orbit dipoles in, one within-orbit tetrahedron out.** That is the Lehmer collision of §12, the hold / collapse / reseed of §12, with the leverage $(J\wedge v)^2$ in the place of the heat 2τ and the gain/loss $\delta^2\|v\|_*^2$ in the place of the gap δ². §12 reaches that threshold from the de Bruijn–Newman flow on Ξ; the generator reaches it from the orbit's symmetry alone, with no ζ-data put in. **Two routes to one collision structure.** Read on the threshold, Rodgers–Tao's Λ ≥ 0 says ζ is not strictly inside the unbroken phase; with RH it sits exactly on the edge. **[READING]**

**Simplicity is a codimension statement.** A multiple zero on the line is the generator sitting exactly on its exceptional point — the borderline Δ = 0, codimension one in parameter space. Simple zeros are therefore the generic case, and vocabulary 8's separation of passivity from simplicity is the circuit form of the same fact: a double zero doubles its tank's residue to $C = \tfrac14$ and stays passive. Whether ζ is generic is the open content (App. D Q7). **[READING]** In tier terms, a double zero is the RESEED opcode returning a degenerate root — the ± ambiguity collapsed before the commit instead of reopened by it.

**An address in the corpus's pathology language.** The threshold $(J\wedge v)^2 \ge \delta^2\|v\|_*^2$ has the shape of the corpus's $R = U^2/P$ balance (`BENDING_MINDS` §4): a squared structural term held against a drive bias. Read so, δ plays the Necessary Betrayer's divergence and $J\wedge v$ the Leo reset — structure holding modes on the line against its own drive. **[READING]**, filed as an address: the shape matches; whether the seating is forced is unexamined.

The generator is a finite model on one orbit. Which operator on ζ's side has it as its section, with its δ-slot on $\chi_x$, is App. D Q9.

---

# Appendix C. The atlas

*The one operation of §1 — the square, untwisted and twisted — read in every vocabulary the walk speaks. Formerly hub §5, §11 and §12. Each vocabulary restates RH exactly and brings its own toolkit; the walk draws on them where they bear.*

## C.5. Eight vocabularies at one operation

**1. Conformal geometry: the orthogonality is built in.** The level sets of $\operatorname{Re}z^2$ and $\operatorname{Im}z^2$ are two families of hyperbolas crossing at right angles everywhere (Cauchy–Riemann). **[LANDED]** The collapse cross xy = 0 is exactly where the square is real, and $z \mapsto z^2$ sends the critical line ($x = 0$) onto $(-\infty, 0]$ and the real axis ($y = 0$) onto $[0, +\infty)$. RH reads: $(\rho - \tfrac12)^2$ is real and negative for every zero.

**2. Lorentzian geometry: two null cones, each the other's axes.** $x^2 - y^2$ and $2xy$ are both forms of signature (1, 1). In the rotated coordinates $u = (x+y)/\sqrt2$, $v = (x-y)/\sqrt2$, they exchange: $x^2 - y^2 = 2uv$ and $2xy = u^2 - v^2$. **[LANDED]** The light cone of each is the coordinate axes of the other. On the critical line the lift form is null and $\operatorname{Re}z^2 = -y^2 < 0$ is timelike. The signature type is the corpus's star-norm $N_* = P^2 - |\mathbf Q|^2$. §0 reads these two cones as the shadow of ζ's two clocks.

**3. The dual-binary seed: the complex plane builds K₄ by multiplying.** Re and Im play the two binaries; their product is the third bimedian; every square is trivial. This is why the lift is forced. **[READING]** on **[LANDED]** character theory. The complex plane takes Fixed and Mutable as its basis and makes Cardinal the product; the corpus seed takes Fixed and Cardinal as basis and makes Mutable the XOR. In $V_4$ any character is the product of the other two, so the two agree as groups; which bimedian a host makes "the XOR" is part of how that host seats.

**4. K₄ geometry: the solid sits inside a square.** The regular tetrahedron's vertices (1, 1, 1), (1, −1, −1), (−1, 1, −1), (−1, −1, 1) all satisfy $z = xy$. **[LANDED]** K₄ is inscribed in the graph of half the imaginary part of a square.

**5. Information: the square is the commit bit.** $z \mapsto z^2$ is 2-to-1 and erases exactly one bit, the sign of ±z; $\operatorname{Re}z^2$ and $\operatorname{Im}z^2$ are what survives, both invariant under $z \mapsto -z$. **[LANDED]** The twisted square $z\bar z$ erases the whole phase and leaves a real. Two grades of square: the untwisted one loses one bit and keeps the doubled phase — the engine's COMMIT bit — and the twisted one burns the phase entirely. **[READING]** Repeated untwisted squaring on the circle writes one digit of each zero's angle per step: the commit tapes of §10, the centroid's terminating and every zero's running on.

**6. AC power: positivity lives only in the twisted square.** For phasors U and I, the instantaneous power is

$$p(t) = \tfrac12\operatorname{Re}(U\bar I) + \tfrac12\operatorname{Re}\big(UI\,e^{2i\omega t}\big).$$

**[LANDED]** The twisted product $U\bar I$ gives the average, committed power — non-negative for every passive load. The untwisted product $UI$ gives the swing at twice the frequency, which carries no sign. Weil's pairing is twisted by cf, and on an orbit that twist acts as a true conjugation only when the zero is on the line — which is the (2, 2) signature of §3 seen as power.

**7. Holomorphic dynamics: the critical line is a Julia set.** Li's map sends the critical line onto the unit circle, and the unit circle is the Julia set of $w \mapsto w^2$. **[LANDED]** Pulled back to the s-plane, the squaring map becomes

$$g(s) = \frac{s^2}{2s - 1}.$$

**[COMPUTED]** (A.10) $g = M^{-1}\circ(w \mapsto w^2)\circ M$ with $M(s) = 1 - 1/s$ holds identically; g commutes with conjugation and with $s \mapsto 1 - s$, so it respects the full K₄ symmetry; and $g(\tfrac12 + iy) = \tfrac12 + \tfrac i2\big(y - \tfrac{1}{4y}\big)$ maps the critical line onto itself, with the single puncture $g(\tfrac12) = \infty$ (since $w(\tfrac12) = -1$ squares to +1). The two superattracting fixed points are $g(1) = 1$ and $g(0) = 0$. Starting next to the first zero, $\operatorname{Re}s = \tfrac12 + 0.01$ iterates to **s = 1, ζ's pole**, and $\operatorname{Re}s = \tfrac12 - 0.01$ iterates to s = 0. The basin of the pole is the half-plane $\operatorname{Re}s > \tfrac12$ ($|w| < 1$); the basin of 0 is $\operatorname{Re}s < \tfrac12$ ($|w| > 1$). The critical line is the chaotic boundary between them, and RH says **every nontrivial zero lies on the Julia set of the commit map.** Li's map is g's Böttcher coordinate. On the line, repeated squaring reads off one bit of each zero's angle per step and never decays; an off-line pair is split, one partner draining into the pole and the other into 0. λₙ is the escape test, and the onset law (A.8) is the escape time measured against the archimedean background. **[READING]**: the zeros sit on the one set where unlimited commits neither drain nor flood. The point ρ itself is not iterated — $g(\rho)$ is not a zero — so the dynamics names the set and leaves the confinement to the plug.

**8. Circuits, the engine's native language: RH says a lossless LC network is passive.** RH is equivalent to $\operatorname{Re}\,\xi'(s)/\xi(s) > 0$ for $\operatorname{Re}s > \tfrac12$ (Hinkkanen 1997; Lagarias 1999). **[LANDED]** In circuit terms that is the statement that $\xi'/\xi$ is a **positive-real function** — the driving-point impedance of a passive network. Under RH, with $s' = s - \tfrac12$, each conjugate pair of zeros gives

$$\frac{1}{s' - i\gamma} + \frac{1}{s' + i\gamma} = \frac{2s'}{s'^2 + \gamma^2},
\qquad
\frac{\xi'}{\xi}(\tfrac12 + s') = \sum_{\gamma>0}\frac{2s'}{s'^2 + \gamma^2},$$

which is Foster's reactance form: a series chain of parallel LC tanks, one per zero, each with $C = \tfrac12$ and $L = 2/\gamma^2$, resonating at $\omega = \gamma$. **[COMPUTED]** with 2 000 zeros, the Foster sum plus its tail estimate matches $\xi'/\xi$ to about 0.3%, the size of the truncated tail; on the critical line, $\operatorname{Re}\,\xi'/\xi(\tfrac12 + 7.5i) = -6.3\times10^{-27}$: pure reactance, lossless (A.10). An off-line zero would put poles in the right half-plane — an active element, a negative resistance, gain. A multiplicative resonance-locale that expresses losslessly is, read this way, literal: **the log-derivative of ξ is a lossless LC network tuned to the zeros.** Passivity and simplicity separate cleanly here. A double zero on the line doubles its tank's residue, giving $C = \tfrac14$, still positive-real. Passivity enforces σ = ½, which is RH; simplicity is the separate statement that every tank carries the single capacity $C = \tfrac12$, which is $\xi'(\rho) \ne 0$ at every zero.

## C.11. What one operation says

Squaring generates; only the twisted square signs. Each reading above restates RH exactly, and each brings a working toolkit: Krein spaces and their fundamental decompositions, Julia sets and basins of attraction, Smith charts and reflection coefficients, positive-real functions and Foster synthesis, the engine's tier table, comb filters and incommensurate delay banks, PT-symmetric generators and their exceptional points. The hard direction now has a precise address in each: a reason the plug keeps K₋ empty on every orbit, a reason the zeros sit on the Julia set of the commit map, a reason the prime bank's cancellation leaves the network passive, a reason every fluctuation wave writes on the radical tier, a reason ζ's leverage never falls below its gain/loss. App. D states them as questions an answer can come back to.

## C.12. The Hilbert landmarks

§2 states the landscape and its forcing. This section reads each landmark against the atlas's own vocabularies, so the atlas and the landscape are one map.

**The forcing, in the atlas's terms.** The commit is the twisted square (App. C, vocabulary 5); its exponent is capped at 2 by the cross-breed (§1); the channels are orthogonal characters on the Bohr torus. The square itself is forced per channel by Herschel–Maxwell (§1); summed over orthogonal channels it is an inner-product norm, so the possibility space is a Hilbert space. Change the exponent and the line moves with it — Nyman–Beurling's family puts ζ's zero-free boundary at σ = 1/p for density in $L^p$ — so the ½ of the critical line is the reciprocal of the commit's exponent. **[LANDED]** pieces; the assembly is the atlas's.

**The line in each vocabulary.**
- **Squaring (App. C, vocabulary 7).** The norm-square sends σ to 2σ: $\|\zeta(\sigma+i\cdot)\|^2 = \zeta(2\sigma)$, and the critical line lands on ζ's pole. The commit map $g(s) = s^2/(2s-1)$ has its one puncture at the same place, $g(\tfrac12) = \infty$.
- **The Smith chart (§3).** On the line the reflection coefficient has $|\Gamma| = 1$: lossless reflection is an isometry, the circuit form of Plancherel.
- **Krein (§3).** On each orbit Weil's pairing has signature (2, 2). RH is that the global form is positive — that the Krein space is a Hilbert space. The landscape's edge and the Krein ghost are one statement: inside the Hilbert sector there is no negative direction to occupy.
- **Tiers (§2).** The commit exponent 2 and the RESEED slope ½ are reciprocal: the radical tier is the Hilbert line read on the opcode table.
- **The prime bank (§7).** Each comb's loop gain $p^{-1/2}$ squares to $1/p$; von Neumann's criterion for the bank's product vector, $\sum_p(1 - \sqrt{1-p^{-2\sigma}})$, is the sum of those prices at σ, and it diverges exactly at the line.

**The landmarks against `On_HilbertAndHisSpaces`.**

| That document | This landscape | Status |
|---|---|---|
| Rays, not arrows: length is gauge (§III) | On the line the norm diverges and Selberg's normalisation keeps only the ray's statistics | **[READING]** on **[LANDED]** |
| Stone–von Neumann uniqueness, Haag's inequivalence (§VI) | Inside: the Euler vector in the vacuum's sector; at the edge: an inequivalent sector of the infinite tensor product | **[LANDED]** criterion; seating **[READING]** |
| Superselection as the firewall between sectors (§III.a) | The sectors of the infinite tensor product, separated at σ = ½ | **[READING]** |
| Type I instance, Type III₁ horizon, thermal (§VII) | Bost–Connes: type I∞ for β > 1, unique type III₁ for β ≤ 1; the line over β = 2σ = 1 | Transition **[LANDED]**; seating **[READING]** |
| The Route Law as the Born square (§V) | The square forced per complex channel (§1): additivity over Re ⊥ Im with phase-blindness gives λ\|a\|² (Herschel–Maxwell), so the premise is the channel's geometry, not an inner product assumed in advance | **[LANDED]** |

**What is not forced.** The Bost–Connes seating through β = 2σ is a reading of an identity, not a map between the two algebras. Selberg's normalisation as projectivisation is a reading: it divides a distribution by a growing scale, which is the projective move in spirit, not a quotient by ℂ*. And RH itself: the landscape is forced, and whether every zero sits on its edge is the open positivity (App. D Q5).

---

# Appendix D. The questions

*Where the walk's readings meet the open mathematics. Cited from the walk as D Q1–Q13. Q14 of an earlier draft is withdrawn: the price of §8 answers it.*

1. **The cancellation question.** The prime delay bank enters $\xi'/\xi$ subtracted, with weights $\Lambda(n)/\sqrt n$, and its continuation cancels the active pole at $s' = +\tfrac12$ (§7). What structural constraint on those weights guarantees that the cancellation leaves no right-half-plane pole behind?
2. **The scattering question.** Is there a lossless scattering system — a unitary colligation — whose transfer function is the Cayley transform $\big(\xi'/\xi - Z_0\big)/\big(\xi'/\xi + Z_0\big)$ on $\operatorname{Re}s > \tfrac12$, built from the Euler product's local factors? (This is the territory de Branges spaces occupy.)
3. **The confinement question.** The critical line is the Julia set of $g(s) = s^2/(2s-1)$, a repelling set, and the zeros are not orbits of g. What property of the plug as a whole — rather than of individual points — confines the zero set to $J(g)$? Read through the shaft (§0): is confinement the network's stability under its own drive?
4. **The anchor question.** $S_\infty$ is negative for n ≤ 7 and cannot separate ζ from ξ(s − ¼)ξ(s + ¼) out to n = 8 259, so it cannot be the positive "ample" direction that orients a Hodge-type (1, −) split. What object built jointly from the archimedean and prime places supplies that direction on the adele/Mellin space?
5. **The orbit-to-global question.** On each orbit, K₋ is exactly the Fixed ⊕ Cardinal characters (x, xy) of Weil's cf-twisted pairing (§3). What global structure on the plug forces every orbit's amplitude into cf's +1 eigenspace at once — that is, what makes the Krein space a Hilbert space (§2)?
6. **The expansion-centre question.** Generalised Li criteria exist at expansion centres other than s = 1 (Sekatskii; Freitas). Does moving the centre reduce the onset $n^* \approx (\gamma^2/\delta)\ln A(n^*)$, or does the distance $|\rho - a|^2 \approx \gamma^2$ from any real centre to a zero keep the same blindness?
7. **The simplicity question.** Passivity (RH) allows tanks of capacity $C = \tfrac1{2m}$ for a zero of multiplicity m, and a multiple zero is the orbit generator sitting exactly on its exceptional point — codimension one (App. B). Simple zeros are the generic case; what in the plug makes ζ generic, fixing every tank at $C = \tfrac12$?
8. **The Smith-chart question.** The reference impedance of Li's chart is ½, the centroid's coordinate, and ζ's pole sits at the matched point Γ = 0. Is the matched-pole position an accident of the expansion centre, or does every intact Selberg plug place its pole at its own chart's centre? (The pole-free plugs of §6, $L(s,\chi)$, have no pole to place.)
9. **The generator question.** The orbit generator holds its modes on the line exactly while $(J\wedge v)^2 \ge \delta^2\|v\|_*^2$, and its gain/loss δ necessarily sits on the Fixed character $\chi_x$ (App. B). Which operator on ζ's side has H as its section on one orbit, with its δ-slot on $\chi_x$ — and is it found in the PT-symmetric constructions already proposed for the zeros?
10. **The step question.** At the first Lehmer pair S(T) steps by 1.96 across 0.042 of a clock tick (§12). Is the step size at close pairs fixed by the local repulsion law, or does the clock's catch-up carry information about the dispatch?
11. **The tier question.** Von Koch's exponent ½ sits on the engine's RESEED slope (§2), while the trivial zeros write waves at slopes −2, −4, … that the tier set does not contain. Does the tier reading extend to the trivial tower — as a decaying series below the floor — or does RH's tier-quantization hold only on the nontrivial sector?
12. **The tape question.** The centroid's commit tape terminates; is any zero's $w_\rho$ a root of unity, so that its tape is periodic (§10)?
13. **The conductor question.** For conductor q ≥ 23 the archimedean place carries every Li coefficient alone (§6). For such plugs the prime part can be negative throughout without threatening positivity at low n. Where, for these plugs, does the prime part first have to do any work at all?

The model runs; these, and the bets of A.11, are where it keeps going.

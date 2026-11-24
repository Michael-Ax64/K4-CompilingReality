# The Riemann Realization — Inventory of the Machine
## What the Engine Makes Readable, Piece by Piece

*Pieces the K₄ engine brings into view on the way to RH, each with its register and the address where it stands. A bare § is a section of `L4-Riemann-Realization`; R.n is a standing reference table in Part 0 of `L4-Riemann-Realization-evolution`. A brute-force attack on RH would pass most of these without seeing them; with the engine as a reference frame they read off directly. None rests on a statistical coincidence: where a statistic appears, it is a measured quantity with its law named.*

---

## I. The Prime Generator

The centrepiece: the primes are produced by a loop that runs through the zeros and compounds by the square.

| Piece | What the engine shows | Status | Where |
|---|---|---|---|
| **The generator loop** | The integers up to $N$ build the zeros up to $T = 2\pi N^2$ (the Riemann–Siegel window); those zeros resolve the primes up to $T/2\pi = N^2$ (Rayleigh); the sieve fixes the primes up to $x^2$ from the primes up to $x$. One square, three layers: window, resolution, sieve. | LANDED pieces; the loop as one generator a READING | §III.1, §XI |
| **Primes as callbacks** | The sieve polls every integer. The explicit formula is an event loop: $\psi$ steps where the zero ensemble's phases combine, and the container invokes each prime at resonance. No `main()` generates them, and none is missing. | READING on the landed explicit formula | §VIII; `L6-InversionOfControl` §II |
| **The prime print as impulse response** | $-\zeta'/\zeta$ is the Laplace transform of $\sum\Lambda(n)\,\delta(u - \ln n)$. The zeros are the poles of the transfer function; the print is what the box emits when struck. RH is the Foster condition. | LANDED | §VIII |
| **Landau's detector** | $\Phi_T(x) = \lvert\sum_{\gamma\le T} x^{i\gamma}\rvert$ lights $2, 3, 5, 7$ at $31$–$46$ and cancels at composites ($1.9$–$3.7$); resolution $T \gtrsim 2\pi p$ separates $29$ from $30$ and blurs $101$ against $102$ at $T = 396$. | COMPUTED | §III.1 |
| **The cavity** | $Z_M$ built from $M$-smooth integers: $M = 0$ is a Gram crystal with every zero on the line and no pens; $M = 1, 2, 3$ lose $1, 2, 7$ zeros; $M = 4$ is the full main sum, two short until the seam restores them. Primes $53, 59, 61$ light past $49$; the cutoff is Rayleigh. | COMPUTED | §I |
| **Blank patches as held families** | Every prime's comb holds its multiples silent; the longest blanks are CRT pile-ups of held families (Westzynthius, Erdős, Rankin, Jacobsthal). Record gaps to $10^9$ sit at $0.53$–$0.74\,(\ln p)^2$, falling from $3.8\times10^{-2}$ to $6.8\times10^{-4}$ of the RH ceiling $\sqrt{p}\ln p$. | LANDED constructions; COMPUTED gaps | §VIII; R.16 |
| **Frequencies independent, positions forced** | New primes are $\mathbb{Q}$-independent as frequencies ($H_{\text{incoh}}$) and fixed as positions by the primes below $\sqrt{x}$ ($H_{\text{coh}}$). The set of primes is finished as a law and never finished as an extension. | FORCED | §XI |
| **Chebyshev's bias as omitted commits** | $(\pi - \operatorname{li})/\sqrt{x}$ sits negative at every $x \le 10^4$ because it omits the prime-square commits; against Riemann's $R(x)$ the mean is $+0.0008$ and the positive fraction $0.513$. | COMPUTED; LANDED mechanism | §III.2 |
| **Trivial zeros as start-up transients** | $-\tfrac12\ln(1-x^{-2})$ diverges at $x \to 1^+$ and balances the empty ledger at start-up; it sits outside the oscillating helix. | READING on a landed term | §III.2 |

---

## II. Forcings

Pieces that could not have been otherwise once the engine is the frame.

| Piece | What the engine shows | Status | Where |
|---|---|---|---|
| **The Hilbert structure** | A valuation additive over Re ⊥ Im and blind to phase is $\lambda\lvert a\rvert^2$ (Herschel–Maxwell). Summed over orthogonal channels, the arena is a Hilbert space. | FORCED | §0 |
| **The line at ½, three ways** | The edge of $\ell^2$ ($\lVert\zeta(\sigma+i\cdot)\rVert^2 = \zeta(2\sigma)$), Mellin–Plancherel unitarity, and Hölder self-duality each fix $\tfrac12$; Nyman–Beurling reads the same map as density in $L^p$. | LANDED | §0 |
| **The tax is one bit** | The `COMMIT` square erases exactly the sign; the free $P$-edges ($Z_P = \theta_P = \tau_P = 0$) follow from Star-Norm conservation. | FORCED | §0, §VI; `Q4-OpenExhaust` §II |
| **The bits seat on the orbit** | Active is the resistive half-plane of the Smith chart (sign $x$); Asserting is the square's lift (sign $xy$). Line-reflection is the Mutable bimedian. | FORCED | §II |
| **Weil's negative directions are the two bits** | $\langle F, cf\cdot F\rangle = 4(\lvert a_1\rvert^2 + \lvert a_y\rvert^2 - \lvert a_x\rvert^2 - \lvert a_{xy}\rvert^2)$: $K_- = x \oplus xy$. | LANDED | §II |
| **The vertex-to-role map, three layers** | Pairs forced by the square (Pen with Book, Potential with Current); the active side forced twice (dominant writer in $\psi$, active pole in Foster's network); orientation fixed where the engine meets $H_{\text{coh}}$. | FORCED, FORCED, FORCED at the interface | §II |
| **Only cf stays inside a plug** | For complex $\chi$, $c$ and $f$ carry $L(s,\chi)$ to $L(s,\bar\chi)$; the braid alternates plug and dual; Weil's pairing must live on cf. Zeros at $t > 0$ ($6.18, 8.46, \dots$) and $t < 0$ ($4.13, 9.44, \dots$) are distinct sets. | LANDED; COMPUTED | §II |
| **The braid commits the count and holds the zeros** | The Gray-code ring holds the Mutable bimedian silent; `TAU` (the count) and the reseeds stay live, `ARI`, `PIS`, `LIB`, `VIR` sit dead. The explicit formula is held on the diagonal and walked around in two live steps. | FORCED | §VI; §V |
| **The count is $P = I^2R$** | Riemann–von Mangoldt's main term is the Friction channel; one of $24$ seatings satisfies both $P = I^2R$ and $U = IR$; the constant $7/8$ is priced ($+1$ from $s(s-1)$, $-\pi/8$ from the Γ phase). | COMPUTED; FORCED seating | §VII |
| **No second alignment** | $\ln 3/\ln 2$ is irrational, so no two wheels realign, in phase or anti-phase, at any finite height. The $t = 0$ alignment is unique and spent on the pole. | LANDED | §XIII, §XVII |

---

## III. The Seam and the Shaft

| Piece | What the engine shows | Status | Where |
|---|---|---|---|
| **The resonant seam** | $d\Phi_n/dt = \vartheta'(t) - \ln n = \ln(I/n)$; the Riemann–Siegel cutoff is where integer $n$ turns with the walls. $\lvert\vartheta' - \ln I\rvert = 4.25\times10^{-10}$ at $t = 7005$. | LANDED; COMPUTED | §IV |
| **The walls turn forward when $n = 1$ enters** | $\vartheta'$ vanishes at $t = 6.2898 \approx 2\pi$, where $I = 1.0005$. | COMPUTED | §IV |
| **The seam rescue** | At the first Lehmer peak, $Z_{33} = -0.06600$ loses both zeros; $C_0(0.39002) = +0.06994$ restores $+0.00394$. | COMPUTED | §IV |
| **The margin and the rate** | With $C_0$, zero crossings lost among $138{,}000$ zeros to $10^5$ and near $10^6$; tightest margin $52\times$. The small-peak law has exponent $1.50$–$1.56$. The bare loss exponent ($\approx 0.2$) is the stiffness relaxing toward GUE; $C_0$ losses stay finite exactly when that exponent passes $\tfrac14$. | COMPUTED | §XII |
| **One quantum per height** | RH with simplicity holds exactly when each height carries multiplicity at most one. From the shaft, an off-line pair and a double zero are one event: two quanta, no crossing. | LANDED (elementary) | §X |
| **The shaft's ledger** | Crossings minus walls' ticks: $\zeta$ flat ($0.00, -0.01, -0.01, +0.03$); Davenport–Heilbronn steps $-2.00, -4.01, -7.99$ across its off-line pairs, a debt nothing repays. | COMPUTED | §X |
| **The line sees an off-line pair as nothing** | Every vertical slice strictly between an off-line zero and its partner, the critical line included, winds zero; the $2\pi$ appears only across $\sigma = \beta$ or $1-\beta$. | COMPUTED | §II, §X |

---

## IV. Balance and Price

| Piece | What the engine shows | Status | Where |
|---|---|---|---|
| **The price of being a prime** | Each prime's loop pays $\lvert p^{-1/2}\rvert^2 = 1/p$ on the line; Mertens' sum settles to $0.26151$ by $10^7$; the price turns marginal exactly at $\sigma = \tfrac12$. | LANDED; COMPUTED | §VII |
| **One quantity, three readings** | The price of being a prime, the variance of $\log\lvert\zeta\rvert$ ($\tfrac12\ln\ln t$, measured $1.70$ and $1.90$), and the spread of $S(T)$ (measured $0.155$, $0.182$ against $0.162$, $0.181$) are one quantity. | LANDED; COMPUTED | §VI |
| **The price line separates the plugs** | Loop gain $a_p/\sqrt{p}$ misreads $\zeta(s)^2$ ($1.414 > 1$, zeros intact); the price line reads $\tfrac12$ for Ramanujan-bounded plugs and $\tfrac34$ for $\zeta(s-\tfrac14)\zeta(s+\tfrac14)$, exactly where its upper zeros sit. | LANDED | §V |
| **The square nothing screens** | Phases cancel, so the mean of $\log\lvert\zeta\rvert$ falls ($0.074$ at $10^4$, $0.011$ at $10^5$); squares accumulate and never screen. The real thing happening in $H_{\text{incoh}}$ is the $I^2$. | LANDED; COMPUTED | §VII |
| **Where the product holds balance** | $\zeta \approx P_X Z_X$ (Gonek–Hughes–Keating): the prime factor never vanishes, every crossing lives in the zero factor, and the variance splits between them as the Book grows ($0.61 \to 1.22$ for the primes, $X = 10 \to 10^4$). The zeros keep a height-independent budget at the seam. | LANDED; COMPUTED | §XIII |
| **The window is a size cut** | Factor-closed cuts lose crossings; the size cut closed by the walls' seam keeps them. Product-born coefficients survive a size cut. | COMPUTED reading | §XIII |
| **Stiffness** | Spacing spread $0.362$ (zeros $1$–$202$), $0.398$ (near #$10{,}000$ and #$100{,}000$), against GUE $0.422$: stiffer than GUE at height, relaxing slowly. | COMPUTED | §I.4, §XII |

---

## V. The Orbit as a Circuit

| Piece | What the engine shows | Status | Where |
|---|---|---|---|
| **Fixed pairs are tanks** | The conjugate pairs are physical elements: $C = \tfrac12$, $\omega_0^2 = \gamma^2 + \delta^2$, conductance $\mp\delta$; the passive tank is the active tank run backwards. | LANDED symbolically | §II |
| **Mutable pairs exchange a quantum of π** | The Pen emits $\delta/(\delta^2 + (t-\gamma)^2)$ and the Current absorbs it; the total is exactly $\pi$ for every $\delta$, delivered sharp on the line and spread off it. | LANDED symbolically | §II |
| **Infinite hold, zero mass** | $Q = \sqrt{\gamma^2+\delta^2}/2\delta$: infinite on the line while the orbit volume is zero. Two kinds of interior: the mass interior $V$ and the hold depth $Q$. | LANDED | §II |
| **The onset law measures $Q$** | $n^* \approx 2\gamma Q\ln A(n^*)$: Li's coefficients need about $2\gamma Q$ terms to see a tank of quality $Q$. | LANDED rewriting of the computed law | §II |
| **The Necessary Betrayer at a zero** | `AQU` on `P–U` is the tank's resistance $-1/\delta$; on the line it runs to $-\infty$ and `LEO` chokes the current: the pole of $\xi'/\xi$ at the zero of $\xi$. | READING on a landed circuit | §II, §V |
| **The orbit generator** | The most general orbit-symmetric $4\times4$ generator is PT-symmetric under cf, chiral under f, with its gain/loss on $\chi_x$; its exceptional point reproduces the heat-flow collision from symmetry alone. | COMPUTED | R.17 |

---

## VI. Vantage and Hub

| Piece | What the engine shows | Status | Where |
|---|---|---|---|
| **$p + 1$ is the pre-closure** | The two ends, $1 + p$, are the walls; Hasse's interval runs between perfect squares, $(\sqrt p \mp 1)^2$; supersingular primes count exactly $p + 1$ ($154$ of $301$ for $y^2 = x^3 - x$). | LANDED; COMPUTED | §XIV |
| **Crossing is rotation** | The local Frobenius is elliptic, parabolic or hyperbolic, matching two dipoles, the exceptional point, one quartet. A crossing is an elliptic element seen from the shaft. | LANDED trichotomy; READING of the match | §XIV |
| **Weil's surface and Deligne's family sit inside K₄** | The $P$-absent face is the Ohm plane $u = i + r$; the siblings $\bar\rho, 1-\bar\rho, 1-\rho$ are the family; without $P$, $Q = \infty$; the write-only Book supplies the sign, $\mathrm{Re}(U/I) \ge 0$. | CANDIDATE correspondence on LANDED pieces | §XIV |
| **The Sudoku's spokes are the involutions** | Time is $c$, Space is $f$ (the sign the square burns), the Observer is $cf$ (the held diagonal, where crossings live). | CANDIDATE seating | §XV |
| **An off-line zero is an arrow at the hub** | Every spoke reads a bounded cosine of a real angle; a boost needs $\cosh\eta > 1$, past the shear ceiling. RH reads as the Sudoku's `KD-3` holding for $\zeta$. | CANDIDATE on DERIVED Sudoku results | §XV |
| **Zero margin as zero temperature** | $\zeta$ at $\Lambda = 0$ sits where the Sudoku's clamp is a sharp kink: approaches to a merger stay open, and a boost has no seat. | CANDIDATE | §XV |
| **The hub is $s = \tfrac12$** | One hub for every orbit; from it each zero is a phase; the Sudoku's $90^\circ$ chime, where area exits, is the critical line. | LANDED geometry; CANDIDATE chime mapping beyond $90^\circ$ | §XVI |
| **Slope becomes pitch** | Li's map turns a zero's slope from the hub, $x/y$, into the pitch of its rotor's spiral (ratio $0.9992$ at $t = 14$, $1.000000$ at $t = 7005$). Zero slope is a circle that returns. | COMPUTED | §XVI |
| **RH as torsion-freeness of the zero rotors** | `L4-Riemann-1` §III: a screw with zero pitch is a circle. An off-line zero is a screw whose slide banks in $\lambda_n$; an on-line zero is holonomy without record. Riemann chose $T = 0$ for geometry; RH asks whether ζ's plug forces it on its zeros. | CANDIDATE reading on the computed identity | §XVI |
| **The Burgers vector of an off-line pair** | The shaft sees the dislocation as a gap of two quanta, Davenport–Heilbronn's $-2$ per pair, while the pitch itself is invisible from the line, as `L4-Riemann-2` says torsion is invisible in surface data. | COMPUTED gap; CANDIDATE reading | §X; §XVI |

---

## VII. Readings of Form

The questions, typed by what kind of infinity they range over.

| Piece | What the engine shows | Status | Where |
|---|---|---|---|
| **`□` and `∀`** | `L4-K4-Infinities-1` §IV's potential infinity gets its quantifier: `□` along a run that never halts, `∀` over a completed set. A theorem that reads *almost all* has no `□` form. | READING with landed logic | §XI |
| **RH sorts as `□`** | RH is $\Pi^0_1$ (Lagarias); its counterexample is finished. Completed-limit tools (Bohr–Jessen, Voronin, Bagchi's density) are equivalences of the wrong type to close it. | LANDED; READING | §XI |
| **A double zero is never-finishing** | No finite precision tells it from two zeros a hair apart; simplicity is a rate question, and the rate is measured. | LANDED | §XI, §XII |
| **Frequencies are given, heights are found** | On the prime side distinctness is free and $\mathbb{Q}$-independence is the strong rung; on the zero side distinctness is all of RH with simplicity, and LI is the further rung. | LANDED | §XI |
| **Averaging blindness as the third stuckness** | An off-line zero is a diagonal the Mutable-held ring cannot map; the averaging tools conclude without seeing it. | READING | §XVII |
| **Regime labels** | Every RH-quality statement holds unconditionally below the transfer scale of the verified height ($H \approx 3\times10^{12}$; $\psi$ to about $H^2$, $\lambda_n$ to about $10^{27}$) and conditionally above it. | LANDED method; COMPUTED estimate | §IX; R.13 |

---

## VIII. The One Sentence

Every section above converges on one question, readable in each register the engine speaks:

* **On the shaft:** does every tick of the walls' clock get its own crossing?
* **At the hub:** does every phase the hub holds sit exactly at $90^\circ$?
* **In the disc:** is every zero rotor a circle that returns?
* **In the series' grammar:** does ζ's plug force $T = 0$ on the transport of its zeros?

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.

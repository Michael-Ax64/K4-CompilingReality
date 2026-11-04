# The complete test battery — one file

## the nambu-puzzle · the step-4 physics dress · `L3-ConstitutiveAlpha-Puzzle-battery.md`

> **What this file is.** You asked to see the complete test battery, in one file. This is that file. It contains every automated check the bench runs against the step-4 work — **91 checks in 14 groups** — each with its exact assertion, the value it measured on the latest run, and its pass/fail status; plus a plain-language explanation of what the battery is, what it does not do, how it grew, what its gate has caught, and the verbatim output of the latest run.
>
> **How to re-run it yourself.** One command: `python3 L3-ConstitutiveAlpha-Puzzle-battery.py` — the runnable Python file delivered in this same folder, so what you can see is what runs. It is byte-for-byte identical to the bench's canonical copy (`scripts/step4_physics_dress.py`); the identity is hash-verified every time this readable file is compiled. Expected output: 91 lines marked `[PASS]`, then `RESULT: ALL PASS`, then exit code 0. If any single check fails, the script stops immediately at that check and exits with code 1 — it never continues past a failure, and a printed `ALL PASS` therefore means every line below was true at the moment of the run. (The file reads its evidence — the corpus files it re-verifies — at the bench's fixed paths, so it runs where the bench's files live.)
>
> **The latest run:** 2026-11-05 07:12 (UTC+8) — **91 checks in 14 groups — 91 PASS, 0 FAIL — exit code 0.** This file was generated from that run; nothing in sections 5–7 is quoted from memory.

---

## 1. What a test battery is on this bench

One Python script holds every check. It exists in two places kept byte-identical: `L3-ConstitutiveAlpha-Puzzle-battery.py` in this folder (the builder-visible delivery) and `scripts/step4_physics_dress.py` on the bench (the canonical copy the log's history references). When it runs, it re-derives or re-verifies each load-bearing claim of the step-4 work from scratch: the arithmetic is recomputed, the units are re-decomposed, the quoted lines are re-read from the named files. Nothing is trusted from a previous run; every receipt is earned again each time.

The design is **halt-on-error**: the checks run in order, and the first failure stops the script on the spot (exit code 1). Only a completely clean run reaches the closing line `RESULT: ALL PASS` (exit code 0). This exists so that a defect cannot hide behind a later, prettier line — and the design has earned its keep: the gate has caught real defects, both in the corpus files and in the battery's own checks (section 6).

## 2. What the checks are made of

Four kinds of check appear below:

- **Arithmetic re-banks** — a number is recomputed at 40-digit precision and compared against the banked value (for example: R_K/Z₀ = 1/(2α); ℏc = 197.3269804 MeV·fm).
- **Dimension checks** — a quantity is decomposed into SI base vectors (kg, m, s, A, K) and the vectors are compared (for example: both reactive terms of the impedance must be ohms).
- **Grep receipts** — a specific string must be present (or absent) in a named file (for example: the Fodor pin verbatim on the working copy; upload/ untouched).
- **Numerical experiments** — small computations with a definite expected answer (a 2001-sample grid testing the clamp and the fold; a load sweep locating the 50% transfer ceiling; a rescaling testing angle invariance).

## 3. What the battery does NOT do (the honesty column)

- It does **not** evaluate the OPEN VOTE's closing condition, and no check claims to.
- The −2.84 ppm stays **family-scan grade**: the battery receipts the number, it never markets it.
- The candidate sourcing (16π² = 8Ω₄, from Q17) **stays a candidate**; the textbook grade of 1/(16π²) is independent of it.
- `upload/` is read **read-only**, always; every correction lands on working copies (copy-on-write).
- A `PASS` means *the assertion held at run time* — not *the physics is proved*. The claim sorts and grades live in the dress file, not here.

## 4. The battery's growth (one group per round)

| Round | Date | Checks | Groups | What was added |
|---|---|---|---|---|
| LOG-18 | 2026-11-05 | 23 | 9 | the step-4 dress lands (the loop measure through the passive ceiling, groups 1–9) |
| LOG-19 | 2026-11-05 | 34 | 10 | + the kernel evaluation (group 10) |
| LOG-20 | 2026-11-05 | 45 | 11 | + the R-pole re-education (group 11) |
| LOG-21 | 2026-11-05 | 59 | 12 | + ThePlenum in evidence (group 12) |
| LOG-22 | 2026-11-05 | 77 | 13 | + the citation round (group 13) |
| LOG-23 | 2026-11-05 | 91 | 14 | + the ScalingInvariants round (group 14) |
| LOG-24 | 2026-11-05 | 91 | 14 | no extension — the battery compiled into one readable file (this file); fresh re-run receipted |

Each round that touched step 4 added exactly one group; no group has ever been rewritten or removed — the growth is append-only, and every earlier check still runs.

## 5. The battery, group by group (all 91 checks)

### Group 1 — The loop measure (1 check)

*What this group guards:* The puzzle's loop-counting factor is 1/(16π²) — the number that sets the size of a one-loop quantum correction. This group verifies the exact identity behind it: 16π² = 8 × Ω₄, where Ω₄ = 2π² is the surface area of the unit three-sphere. Where that identity comes from in the corpus (Q17) stays a candidate; the identity itself is textbook arithmetic and is checked exactly.

*Notes printed by the run:* note: the CANDIDATE SOURCING (Q17: 16pi^2 = 8Omega_4) stays a candidate; the textbook grade of 1/(16pi^2) is independent of it.

| # | The check (verbatim assertion) | Measured on this run | Status |
|---|---|---|---|
| 1.1 | `8*Omega_4 = 16*pi^2 (exact arithmetic)` | `1/(16 pi^2) = 0.00633257` | PASS |

### Group 2 — The resonance condition (3 checks)

*What this group guards:* The circuit's energy-storing (reactive) part must vanish at resonance. This group verifies that the resonance frequency ω₀ = 1/√(μ₀ε₀) equals the speed of light c (the 2019 SI's consistency with the CODATA ε₀), and that the frame's resonance condition ω₀·r = c holds at both r = 1 metre and r = the Planck length — the corpus's frame radius.

| # | The check (verbatim assertion) | Measured on this run | Status |
|---|---|---|---|
| 2.1 | `w0 = 1/sqrt(mu0*eps0) = c (2019-SI consistency, CODATA eps0)` | `rel dev 3.39e-10` | PASS |
| 2.2 | `reactive vanishing at w0 = c/r (r = 1 m)` | `w0(r) = 2.99792e+8 rad/s; (w0(r)*r vs c) rel dev 3.39e-10` | PASS |
| 2.3 | `reactive vanishing at w0 = c/r (r = l_P (corpus value))` | `w0(r) = 1.85481e+43 rad/s; (w0(r)*r vs c) rel dev 3.39e-10` | PASS |

### Group 3 — Impedance units — SI base vectors (kg, m, s, A) (3 checks)

*What this group guards:* Every term of the impedance must carry honest ohm dimensions. Each quantity is decomposed into SI base vectors (kg, m, s, A) and compared. This group also receipts a real defect the battery caught in the source file's §II: written without the r factors, the two reactive terms disagree by a factor of m². The fix (a units gloss on the working copy) is on file; the defect stays receipted here so it cannot quietly return.

| # | The check (verbatim assertion) | Measured on this run | Status |
|---|---|---|---|
| 3.1 | `[w*mu0*r] = Ohm` | `(1, 2, -3, -2)` | PASS |
| 3.2 | `[1/(w*eps0*r)] = Ohm` | `(1, 2, -3, -2)` | PASS |
| 3.3 | `r-suppressed terms disagree by m^2 (the §II defect)` | `[1/(w*eps0)] - [w*mu0] = (0, 2, 0, 0) (= m^2)` | PASS |

### Group 4 — The constitutive ratios (4 checks)

*What this group guards:* The exact identity the whole puzzle rides on: R_K/Z₀ = 1/(2α) — the von Klitzing constant over the vacuum impedance equals one over twice the fine-structure constant. Verified at 40-digit precision, in both directions and in the doubled forms.

| # | The check (verbatim assertion) | Measured on this run | Status |
|---|---|---|---|
| 4.1 | `R_K/Z_0 = 1/(2*alpha)` | `R_K/Z_0 = 68.5179995885` | PASS |
| 4.2 | `Z_0 = mu0*c (the 376.73... value; the 2018-era 9th digit subtlety re-banked)` | `Z_0 = 376.730313411 Ohm` | PASS |
| 4.3 | `4*R_K/Z_0 = 2/alpha` | — | PASS |
| 4.4 | `Z_0/R_K = 2*alpha` | — | PASS |

### Group 5 — The channel algebra (2 checks)

*What this group guards:* The α-cancellation that seats the a⁰ channel: 3·(α/2π)·(2/α) = 3/π, exactly. And the exclusion: the charge-weighted alternative variant misses the measured ratio — an exclusion by arithmetic, not a derivation.

| # | The check (verbatim assertion) | Measured on this run | Status |
|---|---|---|---|
| 5.1 | `3*(alpha/2pi)*(2/alpha) = 3/pi  (the a^0 seating)` | — | PASS |
| 5.2 | `the charge-weighted variant misses (numerical exclusion, not derivation)` | — | PASS |

### Group 6 — The loop sum (re-banked) (3 checks)

*What this group guards:* The central comparison of the whole puzzle, re-banked: 2/α − 3/π + 2α = 273.131663 against the measured m_π±/m_e = 273.13244 — the registered −2.84 ppm gap. Nambu's bare relation (+0.344%) and the no-burn loop (2/α + 2α = 274.0866) ride along.

| # | The check (verbatim assertion) | Measured on this run | Status |
|---|---|---|---|
| 6.1 | `2/alpha - 3/pi + 2*alpha vs measured (the registered -2.84 ppm)` | `L = 273.131663  vs  E = 273.13244  ->  -2.843 ppm` | PASS |
| 6.2 | `Nambu's bare relation re-banked (+0.344%)` | — | PASS |
| 6.3 | `no-burn loop re-banked (2/alpha + 2*alpha = 274.0866)` | — | PASS |

### Group 7 — On-shell linearity; the off-shell probe priced (2 checks)

*What this group guards:* At resonance the reactive channel vanishes and the magnitude collapses to its committed part — |S| = P — which is the linear reading that steps 1–3 receipted. The alternative reading (Pythagorean, off-shell) is priced: it misses at −56.3 ppm. Recorded, not marketed — the kernel decides, and group 10 carries that decision.

*Notes printed by the run:* for the record: P alone reads -56.28 ppm (the Q^2 correction is 3.9e-7) reading: the LINEAR sum is the on-shell object (steps 1-3's receipts); the Pythagorean magnitude is the off-shell reading — the kernel decides.

| # | The check (verbatim assertion) | Measured on this run | Status |
|---|---|---|---|
| 7.1 | `on-shell identity: \|S(P, 0)\| = P  (Q(w0) = 0 -> magnitude collapses to P)` | — | PASS |
| 7.2 | `off-shell Pythagorean probe misses at ~ -56.3 ppm (recorded, not marketed)` | `sqrt(P^2+Q^2) = 273.117069  ->  -56.28 ppm` | PASS |

### Group 8 — The protocol's channel receipts (2001 samples over [0, pi]) (3 checks)

*What this group guards:* The protocol's three signal-processing behaviours, verified on a 2001-sample grid over [0, π]: the clamp is strictly increasing up to π/2 and constant (saturated) beyond it; the Observer channel arccos(cos t) = t is injective on the whole interval; and saturation-not-fold is real — max(cos, 0) pins at zero past the ceiling while |cos| re-rises.

| # | The check (verbatim assertion) | Measured on this run | Status |
|---|---|---|---|
| 8.1 | `clamp injective on [0, pi/2], constant on (pi/2, pi]` | — | PASS |
| 8.2 | `Observer channel injective on the full [0, pi]: arccos(cos t) = t` | — | PASS |
| 8.3 | `saturation-not-fold: max(cos,0) pins at 0 past the ceiling; \|cos\| re-rises` | — | PASS |

### Group 9 — The passive ceiling (2 checks)

*What this group guards:* A passive responder's gain arctan(ωτ) approaches π/2 but never reaches it, for any finite drive — the ceiling is a supremum, not a maximum. Two checks pin both facts.

| # | The check (verbatim assertion) | Measured on this run | Status |
|---|---|---|---|
| 9.1 | `arctan(w*tau) < pi/2 strictly, for all finite w*tau` | `arctan(1e12) = 1.57079632679 (pi/2 = 1.57079632679)` | PASS |
| 9.2 | `the sup is pi/2 and is not attained` | — | PASS |

### Group 10 — The kernel in evidence (QED-TwoBranchMinting + its lecture, supplied LOG-19) (11 checks)

*What this group guards:* The supplied kernel file (QED-TwoBranchMinting + its lecture) is put on the bench: its license present verbatim; no Laurent expansion, no fine-structure numerics, no 137 anywhere in it — which is what discharges 'killer 2'; both whole-magnitude forms agree off-shell (−56.276 vs −56.279 ppm) and the Q² sign is invisible at this algebra; the on-shell collapse holds under both norms; the kernel's own worked examples are re-banked (the binding-ratio test, the Landauer rate, the two-photon invariant, the deuteron/helium-4 defect percentages, the water and Earth self-binding corrections); the lecture's vocabulary is present.

| # | The check (verbatim assertion) | Measured on this run | Status |
|---|---|---|---|
| 10.1 | `the license present verbatim (kernel §I, 'The precise license')` | — | PASS |
| 10.2 | `killer-2 discharge: the kernel claims no Laurent, no fine-structure numerics` | `greps 'Laurent' / 'fine-structure' / '137' — all absent from the kernel file` | PASS |
| 10.3 | `both whole-magnitude forms miss ~ -56.3 ppm off-shell (AC \|S\| from §II; Star-Norm from §I)` | `AC \|S\| = -56.276 ppm;  N* form = -56.279 ppm` | PASS |
| 10.4 | `the Q^2 sign is invisible at this channel algebra; the signed linear entry carries the gap` | `\|AC - N*\| = 0.002855 ppm;  \|linear - magnitude\| = 53.43 ppm` | PASS |
| 10.5 | `on-shell collapse under both norms: Q -> 0 returns P` | — | PASS |
| 10.6 | `the ratio test re-banked: the three light-nucleus binding ratios are non-integer` | `B_t/B_d = 3.8128; B_3He/B_d = 3.4695; B_4He/B_d = 12.7196; min \|x - nearest int\| = 0.187` | PASS |
| 10.7 | `the Landauer rate re-banked (kernel §IV: the rate stands, the bit count does not)` | `ln2/16pi^2 at T_c = 156.5 MeV -> 0.6869 MeV/bit;  k_B*300K*ln2 = 0.0179 eV` | PASS |
| 10.8 | `the two-photon invariant re-banked: back-to-back 2.0 MeV, parallel 0.0 MeV` | — | PASS |
| 10.9 | `Branch-B defects re-banked: deuteron 0.118%, helium-4 0.753%` | `deuteron 0.118%;  helium-4 0.753%` | PASS |
| 10.10 | `the tiny corrections re-banked: water ~1.8e-10, Earth self-binding ~4.2e-10` | `water 1.764e-10;  Earth 4.177e-10` | PASS |
| 10.11 | `the lecture's vocabulary present (pole seats; EP degeneracy; P-edges un-priced)` | — | PASS |

### Group 11 — The R-pole re-education (the Ohm + the acoustic ohm, supplied LOG-20) (11 checks)

*What this group guards:* The two Ohm files (On_The_Dimensions_of_the_Ohm, L4-TheAcousticOhm) re-banked: the electromagnetic row read as a full RLC circuit, double-sourced in the acoustic file; the facets of R (R = P/I², R_K = h/e², the fluctuation-dissipation voice, the Kibble balance); Z₀ = 119.917π Ω; the acoustic impedance of air ρ₀c ≈ 413; the unit-label defect the gate caught in the acoustic file (the number is right, the label mixed conventions — recorded, upload/ untouched); the Helmholtz algebra with its ρ₀ cancellation; the thermal, mechanical and acoustic rows' self-consistency in five SI base vectors; the noise floor [4k_BTR·Δf] = V²; and the 50% matched-transfer ceiling located numerically.

| # | The check (verbatim assertion) | Measured on this run | Status |
|---|---|---|---|
| 11.1 | `the EM row as full RLC: R_drag/Z_0 = 1/(2 alpha), double-sourced (acoustic file)` | `"the medium carries L = mu0, C = eps0, and R = R_drag as felt on the extraction side"` | PASS |
| 11.2 | `the R-pole facets present (R = P/I^2; R_K = h/e^2; the FDT voice; the Kibble balance)` | — | PASS |
| 11.3 | `Z_0 = 119.917*pi Ohm re-banked` | `Z_0/pi = 119.91698` | PASS |
| 11.4 | `Z_0,air = rho0*c = 413 re-banked (the number)` | `1.204*343 = 412.972` | PASS |
| 11.5 | `gate catch: [rho0*c] = Pa*s/m (specific), labeled Pa*s/m^3 — off by m^2` | `[rho0*c] = (1, -2, -1, 0, 0);  Pa*s/m^3 = (1, -4, -1, 0, 0)` | PASS |
| 11.6 | `Helmholtz algebra re-banked: 1/sqrt(L_ac*C_ac) = c*sqrt(S/(ell*V0)) (rho0 cancels)` | `w0 = 108.4661 rad/s (sample geometry)` | PASS |
| 11.7 | `thermal row: R_th = L/(kappa*A) -> K/W` | `(-1, -2, 3, 0, 1)` | PASS |
| 11.8 | `mechanical row: b = F/v -> N*s/m = kg/s` | `(1, 0, -1, 0, 0)` | PASS |
| 11.9 | `acoustic row: [L_ac] = kg/m^4; [C_ac] = m^4*s^2/kg; [X_L] = [X_C] = Pa*s/m^3` | `[X] = (1, -4, -1, 0, 0)` | PASS |
| 11.10 | `the FDT floor: [4 k_B T R df] = V^2` | `(2, 4, -6, -2, 0)` | PASS |
| 11.11 | `the 50% ceiling: transfer peaks at R_L = R_S, efficiency there = 1/2` | `peak at R_L = 50.00 (R_S = 50), eta = 0.500000` | PASS |

### Group 12 — ThePlenum in evidence (the first dependency's core, supplied LOG-21) (14 checks)

*What this group guards:* The supplied L4-ThePlenum is verified at source, line by line: the r-form impedance (the citation behind LOG-18's gloss validated); at resonance the parentheses collapse and Z = R_K — 'one number, two faces'; the 1/16π² phase-conduction guard; Ω₄ = 2π² emitted by the geometry (the candidate's sourcing strengthened); the linear reading registered in-corpus ('a closed Kirchhoff loop'); the two-operating-points doctrine; and the file's load-bearing numbers re-banked (k = c·Z₀ = 1/ε₀; Γ = c/Z₀ = 1/μ₀; the backward transformation; α in both forms; the Diameter-2 ledger pair; Z₀/π; the horizon-scale ratio; the two walk frequencies).

| # | The check (verbatim assertion) | Measured on this run | Status |
|---|---|---|---|
| 12.1 | `the r-form at source (the LOG-18 gloss's citation validated)` | `Z_plenum(w,r) = R_drag(w) + j(w*mu0*r - 1/(w*eps0*r)) — both reactive terms glossed to ohms in-file` | PASS |
| 12.2 | `the resonance value at source: parentheses collapse -> Z = R_K; one number, two faces` | — | PASS |
| 12.3 | `the falsifier's guard grounded at source: 1/16pi^2 = the Q->P phase-conduction factor (§IV.1)` | — | PASS |
| 12.4 | `Omega_4 = 2pi^2 emitted by the geometry (§II.6 — the candidate's sourcing strengthened)` | — | PASS |
| 12.5 | `the linear reading corpus-registered: 'a closed Kirchhoff loop' + '2.84 ppm... an open vote'` | — | PASS |
| 12.6 | `the two-operating-points doctrine present (free-medium R_eff = 0; bounded-frame extraction)` | — | PASS |
| 12.7 | `k = c*Z0 = 1/eps0 (the dielectric stiffness; CODATA-eps0 grade)` | `k = 1.129409067e+11` | PASS |
| 12.8 | `Gamma = c/Z0 = 1/mu0 (the magnetic mobility; ~1e7/4pi at the 2019-SI grade)` | `Gamma = 795774.7156` | PASS |
| 12.9 | `the backward transformation: Z0 = sqrt(k/Gamma); c = sqrt(k*Gamma)` | — | PASS |
| 12.10 | `alpha = Z0/(2R_K) = e^2*k/(4*pi*hbar*c) (both forms; the table's dimensionless last row)` | — | PASS |
| 12.11 | `the Diameter-2 ledger pair: U = h/e, R = h/e^2; Aries recovers h, Virgo recovers e` | `R_K = 25812.80746 Ohm` | PASS |
| 12.12 | `Z0/pi = 119.916983 (the file's printed digits; 120pi is the c ~ 3e8 rounding)` | `Z0/pi = 119.9169832` | PASS |
| 12.13 | `the horizon-scale ratio re-banked: (3/8pi)*(l_P/R_H)^2 = 1.1339e-123 (the file's inputs)` | `= 1.13387e-123` | PASS |
| 12.14 | `the two walk frequencies re-banked: year 1.991e-7 rad/s; inverse Planck time 1.855e43 1/s` | — | PASS |

### Group 13 — The citation round (the Dashen pin; the floor reframed; the falsifier unblocked) (18 checks)

*What this group guards:* The citation round, receipted: the ε = 0.73(2)(5)(17) value belongs to Fodor et al. (PRL 117, 082001 (2016), arXiv:1604.07112) — pinned verbatim on the working copy, the old citation marked corrected-not-rewritten, upload/ untouched; ε is a dimensionless O(1) Dashen-violation parameter — no percent form anywhere; MILC's 0.78 corroborates, the kaon sector its native seat; the Coulomb line is reframed as a classical floor (the charged–neutral pion mass split is electromagnetic-dominated; the strong part is O((m_d−m_u)²), sub-MeV). The numbers re-banked: ℏc, R_π, the floor, the split, the exclusion ratios, Feng-2022 compatibility (~1σ), the Fodor–MILC band overlap, the strong remainder — and the mass-partition falsifier's first comparison, which does not fire.

| # | The check (verbatim assertion) | Measured on this run | Status |
|---|---|---|---|
| 13.1 | `the correction annotation in the working copy (Fodor pin, PRL journal, arXiv id)` | — | PASS |
| 13.2 | `the verbatim pin present ('we obtain ϵ=0.73(2)(5)(17)'; the source's own 'Dashens's' preserved)` | — | PASS |
| 13.3 | `the meaning pinned dimensionless; no percent form anywhere in the working copy` | — | PASS |
| 13.4 | `the old citation marked corrected, not silently rewritten (both texts carry it)` | — | PASS |
| 13.5 | `upload/ untouched: the source file carries the original flag as filed` | — | PASS |
| 13.6 | `MILC corroboration pinned verbatim (PRD 99, 034503 (2019); the kaon-sector seat; +18−11 arms)` | — | PASS |
| 13.7 | `the LO-chipt structure pinned in the annotation (LO degeneracy B(m_u+m_d); O((m_d−m_u)²))` | — | PASS |
| 13.8 | `hbar*c re-banked in MeV*fm` | `= 197.3269805 MeV*fm` | PASS |
| 13.9 | `R_pi = hbar/(m_pi c) = 1.41382 fm re-banked` | `= 1.413817 fm` | PASS |
| 13.10 | `the Coulomb floor line re-banked: (3/5)*alpha*hbar*c/R_pi = 0.611 MeV = 1.196 m_e` | `= 0.611097 MeV = 1.19589 m_e` | PASS |
| 13.11 | `the split re-banked: m_pi+ - m_pi0 = 4.59359 MeV = 8.98943 m_e` | `= 4.59359 MeV = 8.98943 m_e` | PASS |
| 13.12 | `the exclusion ratios re-banked: 616x and 82x (the return-leg punt, arithmetically excluded)` | `615.94x and 81.94x` | PASS |
| 13.13 | `Feng 2022 PRL re-banked: Delta m_pi = 4.534(42)(43) vs 4.59359 -> compatible (~1 sigma)` | `deviation 0.991 combined sigma (1.3% central)` | PASS |
| 13.14 | `Fodor and MILC epsilon bands overlap (dimensionless O(1), compatible)` | `Fodor [0.5517, 0.9083]; MILC(arXiv v2) [0.6695, 0.9603]` | PASS |
| 13.15 | `the strong remainder is sub-MeV by ~4 orders (O((m_d-m_u)^2); coefficient-1 grade)` | `= 0.00029 MeV at coefficient 1 (x100 still sub-MeV)` | PASS |
| 13.16 | `the falsifier's first comparison: no incompatible sign structure (EM-dominated positive split; tiny remainder)` | `split +4.594 MeV (EM-dominated); remainder 0.00029 MeV; return leg +0.014595 on jQ — signs compatible at the [CONSTRUCTION] correspondence` | PASS |
| 13.17 | `dress §10 landed: the correction, the floor reframe, the unblocked falsifier` | — | PASS |
| 13.18 | `the guard's letter recorded (pin grade stated; Feng 2022 PRL pinned in §10)` | — | PASS |

### Group 14 — The ScalingInvariants round (the cutoff resolved; the imports discipline; the open exception) (14 checks)

*What this group guards:* The ScalingInvariants round, receipted: the cutoff's standing resolved at source (the role algebra-emitted per §VIII; the value an import per §IX.a); the imports rule pinned verbatim; the pion-to-electron ratio registered as the corpus's own open exception; the no-log-of-a-sum convergence shared with the kernel; the AC/DC division of labour; Eddington's refusal named; the rung geometry; A4 (the tax paid in modulus, never in angle); the file's own 6:6 carrier/transformer machinery re-run from its own sort; the constitutive-α identity re-banked; the A4 angle invariance re-banked; the dress §11 landing.

| # | The check (verbatim assertion) | Measured on this run | Status |
|---|---|---|---|
| 14.1 | `the cutoff's role pinned at source (§VIII, verbatim)` | — | PASS |
| 14.2 | `the value named an import (§IX.a: Planck-scale constants enter as substrate tolerances)` | — | PASS |
| 14.3 | `the imports rule canonical (§IX.a, verbatim)` | — | PASS |
| 14.4 | `the pion ratio corpus-registered as the open exception (the board's addresses named)` | — | PASS |
| 14.5 | `the no-log-of-a-sum convergence: ScalingInvariants §VI and the kernel §II carry it together` | — | PASS |
| 14.6 | `the AC/DC division of labor pinned (the slope vs the absolute where)` | — | PASS |
| 14.7 | `the refusal rule's corpus echo (Eddington named at §IX.b)` | — | PASS |
| 14.8 | `the rung geometry (§VII): the compressed K4 atom arrives as R per the handoff` | — | PASS |
| 14.9 | `A4: the tax paid in modulus, never in angle (the torsion protocol's angle-readings rescaling-invariant)` | — | PASS |
| 14.10 | `the 6:6 carrier/transformer split re-run from the file's own sort` | — | PASS |
| 14.11 | `two and two in every phase of the braid; squares home at Asserting, roots at Yielding` | `expansive ['P', 'P', 'R', 'R']; compressive ['I', 'U']` | PASS |
| 14.12 | `the constitutive-alpha identity re-banked (§IX.b: the reading emitted, SI-exact by definition)` | `alpha = 0.0072973525643;  1/alpha = 137.035999177` | PASS |
| 14.13 | `A4 re-banked: the complex log's angle is rescaling-invariant (shape conserved, volume spent)` | `theta = 0.9273 rad across 1 -> 1e6 rescaling` | PASS |
| 14.14 | `dress §11 landed: the cutoff resolved, the ask ledger empty, the exception registered` | — | PASS |

## 6. The defect ledger (what the gate has caught across the rounds)

The tally ends at **six** (LOG-23). Every one of these was caught by the gate **before a PASS line survived** — that is the discipline the halt-on-error design exists to enforce.

| # | Round | Where | The defect | The disposition |
|---|---|---|---|---|
| 1 | LOG-18 | in a source file | L3-ConstitutiveAlpha §II wrote the impedance r-suppressed — the two reactive terms disagreed by m² (Ω/m against Ω·m). | Fixed with a units gloss on the working copy (copy-on-write; upload/ untouched). Receipted by group 3. |
| 2 | LOG-18 | in the battery itself (v1) | The resonance check tested (c/r)·r = c — vacuously true; it checked nothing. | Fixed: ω₀ is a function of r, and ω₀(r)·r is tested against c. |
| 3 | LOG-18 | in the battery itself (v2) | ω₀ was held fixed at its r = 1 value while r was scaled — the r-mismatch itself. | Fixed in the same repair as defect 2. |
| 4 | LOG-20 | in a source file | The acoustic file labelled ρ₀c ≈ 413 as Pa·s/m³; ρ₀c is the specific acoustic impedance, Pa·s/m — off by an m². The number is right. | upload/ is immutable; recorded, the owner's to gloss. Receipted by group 11. |
| 5 | LOG-22 | in the battery itself (the fifth tallied) | The Feng check's first version fed error digits 42/43 (units of 10⁻³ MeV) into the σ-combination as if they were MeV — off by 1000×, printing 0.00099σ where the true deviation is ≈0.99σ. The assertion band was right; the arithmetic under it was not. | Fixed in-round; recorded in the script header. |
| 6 | LOG-23 | in the battery itself (the sixth tallied) | A case-mismatched grep ('the open exception' against the file's own run-in header 'The open exception') — the only failure of that group's first run. | Fixed to case-exact; recorded in the script. |

Recorded but not tallied (a missing argument, not a wrong assertion): LOG-20 — an unbalanced mul chain in the FDT dimension check, caught mid-run, fixed in-round.

## 7. The verbatim receipt of the latest run

Captured 2026-11-05 07:12 (UTC+8); command: `python3 L3-ConstitutiveAlpha-Puzzle-battery.py` (the delivered copy, run from this folder); sha256 4b4c7692728282576f33084f99f6fbc26f6a505c2b06fb68b784c6b7aab1dbaf — identical to the canonical `scripts/step4_physics_dress.py`; exit code 0.

```text
========================================================================
STEP 4 — PHYSICS DRESS battery (halt-on-error)
========================================================================

(1) The loop measure
  [PASS] 8*Omega_4 = 16*pi^2 (exact arithmetic)  — 1/(16 pi^2) = 0.00633257
      note: the CANDIDATE SOURCING (Q17: 16pi^2 = 8Omega_4) stays a candidate;
            the textbook grade of 1/(16pi^2) is independent of it.

(2) The resonance condition
  [PASS] w0 = 1/sqrt(mu0*eps0) = c (2019-SI consistency, CODATA eps0)  — rel dev 3.39e-10
  [PASS] reactive vanishing at w0 = c/r (r = 1 m)  — w0(r) = 2.99792e+8 rad/s; (w0(r)*r vs c) rel dev 3.39e-10
  [PASS] reactive vanishing at w0 = c/r (r = l_P (corpus value))  — w0(r) = 1.85481e+43 rad/s; (w0(r)*r vs c) rel dev 3.39e-10

(3) Impedance units — SI base vectors (kg, m, s, A)
  [PASS] [w*mu0*r] = Ohm  — (1, 2, -3, -2)
  [PASS] [1/(w*eps0*r)] = Ohm  — (1, 2, -3, -2)
  [PASS] r-suppressed terms disagree by m^2 (the §II defect)  — [1/(w*eps0)] - [w*mu0] = (0, 2, 0, 0) (= m^2)

(4) The constitutive ratios
  [PASS] R_K/Z_0 = 1/(2*alpha)  — R_K/Z_0 = 68.5179995885
  [PASS] Z_0 = mu0*c (the 376.73... value; the 2018-era 9th digit subtlety re-banked)  — Z_0 = 376.730313411 Ohm
  [PASS] 4*R_K/Z_0 = 2/alpha
  [PASS] Z_0/R_K = 2*alpha

(5) The channel algebra
  [PASS] 3*(alpha/2pi)*(2/alpha) = 3/pi  (the a^0 seating)
  [PASS] the charge-weighted variant misses (numerical exclusion, not derivation)

(6) The loop sum (re-banked)
  [PASS] 2/alpha - 3/pi + 2*alpha vs measured (the registered -2.84 ppm)  — L = 273.131663  vs  E = 273.13244  ->  -2.843 ppm
  [PASS] Nambu's bare relation re-banked (+0.344%)
  [PASS] no-burn loop re-banked (2/alpha + 2*alpha = 274.0866)

(7) On-shell linearity; the off-shell probe priced
  [PASS] on-shell identity: |S(P, 0)| = P  (Q(w0) = 0 -> magnitude collapses to P)
  [PASS] off-shell Pythagorean probe misses at ~ -56.3 ppm (recorded, not marketed)  — sqrt(P^2+Q^2) = 273.117069  ->  -56.28 ppm
      for the record: P alone reads -56.28 ppm (the Q^2 correction is 3.9e-7)
      reading: the LINEAR sum is the on-shell object (steps 1-3's receipts);
      the Pythagorean magnitude is the off-shell reading — the kernel decides.

(8) The protocol's channel receipts (2001 samples over [0, pi])
  [PASS] clamp injective on [0, pi/2], constant on (pi/2, pi]
  [PASS] Observer channel injective on the full [0, pi]: arccos(cos t) = t
  [PASS] saturation-not-fold: max(cos,0) pins at 0 past the ceiling; |cos| re-rises

(9) The passive ceiling
  [PASS] arctan(w*tau) < pi/2 strictly, for all finite w*tau  — arctan(1e12) = 1.57079632679 (pi/2 = 1.57079632679)
  [PASS] the sup is pi/2 and is not attained

(10) The kernel in evidence (QED-TwoBranchMinting + its lecture, supplied LOG-19)
  [PASS] the license present verbatim (kernel §I, 'The precise license')
  [PASS] killer-2 discharge: the kernel claims no Laurent, no fine-structure numerics  — greps 'Laurent' / 'fine-structure' / '137' — all absent from the kernel file
  [PASS] both whole-magnitude forms miss ~ -56.3 ppm off-shell (AC |S| from §II; Star-Norm from §I)  — AC |S| = -56.276 ppm;  N* form = -56.279 ppm
  [PASS] the Q^2 sign is invisible at this channel algebra; the signed linear entry carries the gap  — |AC - N*| = 0.002855 ppm;  |linear - magnitude| = 53.43 ppm
  [PASS] on-shell collapse under both norms: Q -> 0 returns P
  [PASS] the ratio test re-banked: the three light-nucleus binding ratios are non-integer  — B_t/B_d = 3.8128; B_3He/B_d = 3.4695; B_4He/B_d = 12.7196; min |x - nearest int| = 0.187
  [PASS] the Landauer rate re-banked (kernel §IV: the rate stands, the bit count does not)  — ln2/16pi^2 at T_c = 156.5 MeV -> 0.6869 MeV/bit;  k_B*300K*ln2 = 0.0179 eV
  [PASS] the two-photon invariant re-banked: back-to-back 2.0 MeV, parallel 0.0 MeV
  [PASS] Branch-B defects re-banked: deuteron 0.118%, helium-4 0.753%  — deuteron 0.118%;  helium-4 0.753%
  [PASS] the tiny corrections re-banked: water ~1.8e-10, Earth self-binding ~4.2e-10  — water 1.764e-10;  Earth 4.177e-10
  [PASS] the lecture's vocabulary present (pole seats; EP degeneracy; P-edges un-priced)

(11) The R-pole re-education (the Ohm + the acoustic ohm, supplied LOG-20)
  [PASS] the EM row as full RLC: R_drag/Z_0 = 1/(2 alpha), double-sourced (acoustic file)  — "the medium carries L = mu0, C = eps0, and R = R_drag as felt on the extraction side"
  [PASS] the R-pole facets present (R = P/I^2; R_K = h/e^2; the FDT voice; the Kibble balance)
  [PASS] Z_0 = 119.917*pi Ohm re-banked  — Z_0/pi = 119.91698
  [PASS] Z_0,air = rho0*c = 413 re-banked (the number)  — 1.204*343 = 412.972
  [PASS] gate catch: [rho0*c] = Pa*s/m (specific), labeled Pa*s/m^3 — off by m^2  — [rho0*c] = (1, -2, -1, 0, 0);  Pa*s/m^3 = (1, -4, -1, 0, 0)
  [PASS] Helmholtz algebra re-banked: 1/sqrt(L_ac*C_ac) = c*sqrt(S/(ell*V0)) (rho0 cancels)  — w0 = 108.4661 rad/s (sample geometry)
  [PASS] thermal row: R_th = L/(kappa*A) -> K/W  — (-1, -2, 3, 0, 1)
  [PASS] mechanical row: b = F/v -> N*s/m = kg/s  — (1, 0, -1, 0, 0)
  [PASS] acoustic row: [L_ac] = kg/m^4; [C_ac] = m^4*s^2/kg; [X_L] = [X_C] = Pa*s/m^3  — [X] = (1, -4, -1, 0, 0)
  [PASS] the FDT floor: [4 k_B T R df] = V^2  — (2, 4, -6, -2, 0)
  [PASS] the 50% ceiling: transfer peaks at R_L = R_S, efficiency there = 1/2  — peak at R_L = 50.00 (R_S = 50), eta = 0.500000

(12) ThePlenum in evidence (the first dependency's core, supplied LOG-21)
  [PASS] the r-form at source (the LOG-18 gloss's citation validated)  — Z_plenum(w,r) = R_drag(w) + j(w*mu0*r - 1/(w*eps0*r)) — both reactive terms glossed to ohms in-file
  [PASS] the resonance value at source: parentheses collapse -> Z = R_K; one number, two faces
  [PASS] the falsifier's guard grounded at source: 1/16pi^2 = the Q->P phase-conduction factor (§IV.1)
  [PASS] Omega_4 = 2pi^2 emitted by the geometry (§II.6 — the candidate's sourcing strengthened)
  [PASS] the linear reading corpus-registered: 'a closed Kirchhoff loop' + '2.84 ppm... an open vote'
  [PASS] the two-operating-points doctrine present (free-medium R_eff = 0; bounded-frame extraction)
  [PASS] k = c*Z0 = 1/eps0 (the dielectric stiffness; CODATA-eps0 grade)  — k = 1.129409067e+11
  [PASS] Gamma = c/Z0 = 1/mu0 (the magnetic mobility; ~1e7/4pi at the 2019-SI grade)  — Gamma = 795774.7156
  [PASS] the backward transformation: Z0 = sqrt(k/Gamma); c = sqrt(k*Gamma)
  [PASS] alpha = Z0/(2R_K) = e^2*k/(4*pi*hbar*c) (both forms; the table's dimensionless last row)
  [PASS] the Diameter-2 ledger pair: U = h/e, R = h/e^2; Aries recovers h, Virgo recovers e  — R_K = 25812.80746 Ohm
  [PASS] Z0/pi = 119.916983 (the file's printed digits; 120pi is the c ~ 3e8 rounding)  — Z0/pi = 119.9169832
  [PASS] the horizon-scale ratio re-banked: (3/8pi)*(l_P/R_H)^2 = 1.1339e-123 (the file's inputs)  — = 1.13387e-123
  [PASS] the two walk frequencies re-banked: year 1.991e-7 rad/s; inverse Planck time 1.855e43 1/s

(13) The citation round (the Dashen pin; the floor reframed; the falsifier unblocked)
  [PASS] the correction annotation in the working copy (Fodor pin, PRL journal, arXiv id)
  [PASS] the verbatim pin present ('we obtain ϵ=0.73(2)(5)(17)'; the source's own 'Dashens's' preserved)
  [PASS] the meaning pinned dimensionless; no percent form anywhere in the working copy
  [PASS] the old citation marked corrected, not silently rewritten (both texts carry it)
  [PASS] upload/ untouched: the source file carries the original flag as filed
  [PASS] MILC corroboration pinned verbatim (PRD 99, 034503 (2019); the kaon-sector seat; +18−11 arms)
  [PASS] the LO-chipt structure pinned in the annotation (LO degeneracy B(m_u+m_d); O((m_d−m_u)²))
  [PASS] hbar*c re-banked in MeV*fm  — = 197.3269805 MeV*fm
  [PASS] R_pi = hbar/(m_pi c) = 1.41382 fm re-banked  — = 1.413817 fm
  [PASS] the Coulomb floor line re-banked: (3/5)*alpha*hbar*c/R_pi = 0.611 MeV = 1.196 m_e  — = 0.611097 MeV = 1.19589 m_e
  [PASS] the split re-banked: m_pi+ - m_pi0 = 4.59359 MeV = 8.98943 m_e  — = 4.59359 MeV = 8.98943 m_e
  [PASS] the exclusion ratios re-banked: 616x and 82x (the return-leg punt, arithmetically excluded)  — 615.94x and 81.94x
  [PASS] Feng 2022 PRL re-banked: Delta m_pi = 4.534(42)(43) vs 4.59359 -> compatible (~1 sigma)  — deviation 0.991 combined sigma (1.3% central)
  [PASS] Fodor and MILC epsilon bands overlap (dimensionless O(1), compatible)  — Fodor [0.5517, 0.9083]; MILC(arXiv v2) [0.6695, 0.9603]
  [PASS] the strong remainder is sub-MeV by ~4 orders (O((m_d-m_u)^2); coefficient-1 grade)  — = 0.00029 MeV at coefficient 1 (x100 still sub-MeV)
  [PASS] the falsifier's first comparison: no incompatible sign structure (EM-dominated positive split; tiny remainder)  — split +4.594 MeV (EM-dominated); remainder 0.00029 MeV; return leg +0.014595 on jQ — signs compatible at the [CONSTRUCTION] correspondence
  [PASS] dress §10 landed: the correction, the floor reframe, the unblocked falsifier
  [PASS] the guard's letter recorded (pin grade stated; Feng 2022 PRL pinned in §10)

(14) The ScalingInvariants round (the cutoff resolved; the imports discipline; the open exception)
  [PASS] the cutoff's role pinned at source (§VIII, verbatim)
  [PASS] the value named an import (§IX.a: Planck-scale constants enter as substrate tolerances)
  [PASS] the imports rule canonical (§IX.a, verbatim)
  [PASS] the pion ratio corpus-registered as the open exception (the board's addresses named)
  [PASS] the no-log-of-a-sum convergence: ScalingInvariants §VI and the kernel §II carry it together
  [PASS] the AC/DC division of labor pinned (the slope vs the absolute where)
  [PASS] the refusal rule's corpus echo (Eddington named at §IX.b)
  [PASS] the rung geometry (§VII): the compressed K4 atom arrives as R per the handoff
  [PASS] A4: the tax paid in modulus, never in angle (the torsion protocol's angle-readings rescaling-invariant)
  [PASS] the 6:6 carrier/transformer split re-run from the file's own sort
  [PASS] two and two in every phase of the braid; squares home at Asserting, roots at Yielding  — expansive ['P', 'P', 'R', 'R']; compressive ['I', 'U']
  [PASS] the constitutive-alpha identity re-banked (§IX.b: the reading emitted, SI-exact by definition)  — alpha = 0.0072973525643;  1/alpha = 137.035999177
  [PASS] A4 re-banked: the complex log's angle is rescaling-invariant (shape conserved, volume spent)  — theta = 0.9273 rad across 1 -> 1e6 rescaling
  [PASS] dress §11 landed: the cutoff resolved, the ask ledger empty, the exception registered

========================================================================
RESULT: ALL PASS — step-4 receipts on file (halt-on-error, exit 0)
========================================================================

```

## 8. Where everything lives

- **The battery, runnable form, builder-visible delivery**: `download/L3-ConstitutiveAlpha-Puzzle-battery.py` — byte-identical to the canonical, hash-verified at every compile
- **The battery, runnable form, bench-canonical**: `scripts/step4_physics_dress.py`
- **This file** (the readable form): `download/L3-ConstitutiveAlpha-Puzzle-battery.md`
- **The dress** (what the battery receipts): `download/L3-ConstitutiveAlpha-Puzzle-dress.md`
- **The log** (the memory — which round added what): `download/L3-ConstitutiveAlpha-Puzzle-log.md` (LOG-18 through LOG-25; re-established at LOG-26 after the bench event)
- **The manifest / work-order / README**: the state, the handoff lists, the bench index

The work-order's suffix-taxonomy note (§2 item 6) proposed a `-receipts.md` suffix *if receipts ever need to live on disk*. This file realizes that need at the builder's request; it is named `-battery.md` because it is the whole battery, not a per-round capture.

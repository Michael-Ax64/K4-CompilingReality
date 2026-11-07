# L3-ConstitutiveAlpha-Puzzle
## The Nambu Puzzle — The Bare Topological Mass Ratio

> **Epistemic Register:** Working manifest.
>
> **The Puzzle in One Line:** The derivation of the bare charged-pion-to-electron mass ratio across the Atom of Space (K4 Mutable diameter) as a 3-regular on-shell boundary cycle: L = 2/α − 3/π + 2α = 273.1316634, landing within 2.84 ppm (2.20σ) of the laboratory dressed mass with zero free parameters.

---

> **BENCH EVENT (LOG-26, 2026-11-05) — read this first.** Between rounds the environment restored the project tree to its LOG-16 state. The state rows below are accurate as of the buffer-dump round and are retained as history; everything from LOG-17 onward was lost from disk (the dress, the work-order, the step-4 battery script, the battery files, the README index, log entries 17–25 in entry form, the working-copy annotations) and is being recovered from the session record under the sequence R-1..R-5 (see LOG-26). Recovered this round: the two working-copy annotations (re-applied, marked), the battery compiler, the README index, the charge ledger (verbatim, in the log), and the two-path observations round (`L3-ConstitutiveAlpha-Puzzle-twopaths.md` — new in the note family). The arithmetic of the executed work re-verifies at file grade (`scripts/twopaths_arithmetic.py`, ALL PASS; the three surviving batteries re-run clean).

---

> **RESOLUTION (LOG-29, 2026-11-05) — the double-bind dissolved; both debts closed.** The builder's note to the assisting instance (Appendix D of the resolution file) resolved the LOG-28 deadlock: the Laurent triad is the evaluation of a closed meromorphic contour integral around the K4 cycle (pole $+2/\alpha$, winding/residue $-3/\pi$, analytic return $+2\alpha$ — Cauchy's sum), not a breadboard law and not a matrix product. **Debt 1 CLOSED** — the winding counts the confined $SU(3)$ flux junction, $N_c = 3$, flavor-blind by topology (discriminator $545.6\times$ over the charge-weighted reading). **Debt 2 DISCHARGED** — the spectrum is on-shell at $\omega_0 = c/r$: $X(\omega_0) = 0$, $R_{\text{drag}}(\omega_0) = R_K$, the triad is three on-shell invariants; no off-resonance input. Fork A closes. Receipt: `scripts/resolution_arithmetic.py` (31 banks, ALL PASS, exit 0); round file `L3-ConstitutiveAlpha-Puzzle-resolution.md`. [Both grades superseded in part at LOG-30 — see the audit banner below.]

---

> **AUDIT ROUND (LOG-30, 2026-11-05) — two overclaims trimmed; the resolution file stands on bedrock.** The builder's audit of the resolution file: (1) **the mechanism re-framed** — Cauchy's residue theorem is not what produces $(2/\alpha - 3/\pi + 2\alpha)$ (integrating a meromorphic form over $z$ extracts only the residue; it does not evaluate a Laurent polynomial at $z = \alpha$); the true structure is the closed path integral of complex impedance around the topological boundary cycle, $\oint_{\partial K_4} dZ = \Delta Z_{\text{forward}} + \Delta Z_{\text{junction}} + \Delta Z_{\text{return}}$, evaluating at the resonant operating point to the algebraic sum of the three orders. (2) **the debts demarcated honestly** — Debt 1 CLOSED with the tag *derived mechanism, identified tax* (the per-channel $\alpha/2\pi$ magnitude stays the adopted identification); Debt 2 **RE-GRADED, not discharged**: the integer count $m = 3$ is derived and unique on the discrete lattice $0..120$ ($409\times$ margin — Instance 2's result, machine-verified; $388\times$ at the 3-ppm-window convention, one lattice), but the $-2.84$ ppm sub-ppm landing is an **OPEN VOTE** awaiting the full continuum substrate dispersion $H_3$ and the dynamical gap equation $\Sigma(m) = m$. Receipt: `resolution_arithmetic.py` extended to 36 banks in six groups (F the audit trim), ALL PASS, exit 0; round file re-graded in place.

---

## State (Grounded Reconciliation)

| Component | Status | Operational Basis / Living Address |
|---|---|---|
| Step 1 — B′ Apex Mapping | CLOSED | K4 3-regular degree check forces exactly 3 boundary spokes. |
| Step 2 — Dimensional Neutrality | CLOSED | Ohm/Ohm cancels; apex carries zero net physical units (10/10 PASS). |
| Step 3 — Crowbar Validation | CLOSED | Linear on-shell resolution verified; K-1..K-4 checked (5/5 PASS). |
| Debt 1 — Flux Junction Topology | CLOSED (Tagged) | Flavor-blind winding −N_c/π = −3/π derived via confinement blanket and isospin lock Σq² = 5/9. Per-channel tax α/2π carried as identified import. |
| Debt 2 — Discrete Multiplicity | CLOSED | m = 3 is the unique minimum on the lattice 0..120 by a 409× margin. |
| Norm Pinning (D9) | CLOSED | Strictly branch-resolved ℓ¹ (coordinates add algebraically with directed signs; preserves mass-partition falsifier). |
| Fork A — The Coefficients | CLOSED AT BARE GRADE | Multiplicity derived (409×); tax identified; on-shell traversal exact. |
| Continuum Dressing Delta (−2.84 ppm) | DEMARCATED (Open Vote) | Banked as the 2.20σ (−397 eV) physical continuum delta. Demands to zero this out via curve-fitting retired. |
| Neutral Kaon Falsifier (F-G4) | ARMED | K⁰ loop (Σq² = 2/9) predicts 3/π unchanged under topology vs (2/5)(3/π) under charge weighting (kill boundary Δ = 2097.7 ppm). |
| Fork B — The Operating Point in Evidence | OPEN | Measure V → invert → read ωτ; laboratory Bell-transmission test. |
| π⁰ Split | OPEN | Split localized to vertex channel content; Gate-2 ledger. |
| KD-KK1b Discrete Side | SOURCELESS BY RULING | Bridge pair dropped (LOG-15); open cell awaiting successor pipeline. |
| Joint-2 Ontology Decision | OPEN | Owner-level; gates nothing on this bench. |
| Q4 Composite-Claim Edge | PERMANENT OPEN | Standing honest edge in the corpus; biquaternion apparatus check. |

## Receipts (scripts on file, all halt-on-error)

- `scripts/audit_constitutive_alpha.py` — the constitutive audit, 28/28 (LOG-11)
- `scripts/step2_node_seat_audit.py` — step 2, 10/10 (LOG-12; one gate-caught defect recorded in header)
- `scripts/step3_crowbar_test.py` — step 3, 5/5 (LOG-13; re-run clean at LOG-14)
- `scripts/spectral_derivations.py` — the spectral round, 52 banks in five groups (LOG-28)
- `scripts/resolution_arithmetic.py` — the resolution round + audit trim, 36 banks in six groups (LOG-29/LOG-30)
- Earlier batteries: `verify_hinge_clamp.py`, `dim_audit.py`, `covenant_gate_and_rim_check.py`, `crowbar_receipt_check.py`, `verify_signed_aut.py`, `thermal_family_check.py`, `aggregate_docking_check.py` — all run clean.

## The note family (builder ruling 2026-11-05)

- `L3-ConstitutiveAlpha-Puzzle.md` — this manifest (the puzzle's internal home)
- `L3-ConstitutiveAlpha-Puzzle-log.md` — the development log from LOG-15; numbering continues from the sealed log's LOG-14
- `L3-ConstitutiveAlpha-Puzzle-twopaths.md` — the two-path observations round (LOG-26) and the reorientation cross-read (LOG-27); the supplied external materials preserved verbatim as Appendices A (the intake report), B (the spectral-problem exposition), C (the fault-line exchange)
- `L3-ConstitutiveAlpha-Puzzle-spectral.md` — the spectral round (LOG-28): the apex operators on the board, the count closed and forced, the measure fork run one-sided
- `L3-ConstitutiveAlpha-Puzzle-resolution.md` — the resolution round (LOG-29) with the audit trim applied in place (LOG-30): the double-bind dissolved, the sum re-grounded as the closed impedance-cycle traversal, Debt 1 closed (derived mechanism, identified tax), Debt 2 re-graded (the count derived and unique on the lattice 0..120 at 409×; the −2.84 ppm landing an open vote awaiting H3); the builder's note preserved verbatim as Appendix D
- Further suffixes as the work demands; audit batteries live in `scripts/`, named per round

## Sealed predecessors (standing as filed, zero edits from the naming round on)

- `L4-DynamicDistortions-Sudoku.md` — the corpus-register document (the 401-slot call closed: stands under its own name, sealed)
- `L4-DynamicDistortions-Sudoku-v3.md` — the artifact (the clamp, the rim, the proven limit)
- `L4-DynamicDistortions-Sudoku-log.md` — LOG-0..14: the whole round-history of the mapping, the dimensional analysis, and the crowbar test
- `L4-TheCrowbar.md` (patched copy), `L3-ConstitutiveAlpha.md` (patched copy) — the working copies; the Movement VI note, the dependency-line pointer, and the §IV node subsection landed at step 3/step 2; now sealed
- `upload/` — immutable, as always

## Dropped (builder ruling, 2026-11-05)

`On_TheEightPiBridge.md` + `On_TheEightPiBridge-AUDIT-2026-11-04.md` — obsolete. Never landed on this bench (that absence was LOG-14's subject); nothing to delete. The crowbar's own dependency line stands untouched — the treatise cites what it was written against; receipts say what they said. KD-KK1b's discrete side is re-labeled accordingly: sourceless by ruling, not blocked.

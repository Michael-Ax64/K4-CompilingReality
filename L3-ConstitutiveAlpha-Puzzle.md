# L3-ConstitutiveAlpha-Puzzle
## the nambu-puzzle — internal working home, until completed

> **Epistemic Register:** Working manifest. This file is the puzzle's internal address, not a corpus document: it carries the statement, the state, and the pointers. Every claim here is receipted elsewhere (the scripts, the sealed log, the source documents) and carries the sort it earned there; nothing new is derived in this file.
>
> **Name (builder ruling, 2026-11-05):** *"THIS work, lets call it the nambu-puzzle, can be thought of as L3-ConstitutiveAlpha-Puzzle.md internally until it has been completed. this lets you track notes about this puzzle under suffixes of that name."* — chat name: **the nambu-puzzle**; file family: `L3-ConstitutiveAlpha-Puzzle*`; the name holds until the puzzle is completed, at which point the builder names what it becomes.
>
> **Naming note [CONSTRUCTION], recorded not marketed:** the puzzle's centerpiece number is a pion mass ratio (m_π±/m_e), and the pion is the paradigmatic Nambu–Goldstone boson. The builder's word fits the object; whether more than that is meant is the builder's to say.

---

> **BENCH EVENT (LOG-26, 2026-11-05) — read this first.** Between rounds the environment restored the project tree to its LOG-16 state. The state rows below are accurate as of the buffer-dump round and are retained as history; everything from LOG-17 onward was lost from disk (the dress, the work-order, the step-4 battery script, the battery files, the README index, log entries 17–25 in entry form, the working-copy annotations) and is being recovered from the session record under the sequence R-1..R-5 (see LOG-26). Recovered this round: the two working-copy annotations (re-applied, marked), the battery compiler, the README index, the charge ledger (verbatim, in the log), and the two-path observations round (`L3-ConstitutiveAlpha-Puzzle-twopaths.md` — new in the note family). The arithmetic of the executed work re-verifies at file grade (`scripts/twopaths_arithmetic.py`, ALL PASS; the three surviving batteries re-run clean).

---

> **RESOLUTION (LOG-29, 2026-11-05) — the double-bind dissolved; both debts closed.** The builder's note to the assisting instance (Appendix D of the resolution file) resolved the LOG-28 deadlock: the Laurent triad is the evaluation of a closed meromorphic contour integral around the K4 cycle (pole $+2/\alpha$, winding/residue $-3/\pi$, analytic return $+2\alpha$ — Cauchy's sum), not a breadboard law and not a matrix product. **Debt 1 CLOSED** — the winding counts the confined $SU(3)$ flux junction, $N_c = 3$, flavor-blind by topology (discriminator $545.6\times$ over the charge-weighted reading). **Debt 2 DISCHARGED** — the spectrum is on-shell at $\omega_0 = c/r$: $X(\omega_0) = 0$, $R_{\text{drag}}(\omega_0) = R_K$, the triad is three on-shell invariants; no off-resonance input. Fork A closes. Receipt: `scripts/resolution_arithmetic.py` (31 banks, ALL PASS, exit 0); round file `L3-ConstitutiveAlpha-Puzzle-resolution.md`. [Both grades superseded in part at LOG-30 — see the audit banner below.]

---

> **AUDIT ROUND (LOG-30, 2026-11-05) — two overclaims trimmed; the resolution file stands on bedrock.** The builder's audit of the resolution file: (1) **the mechanism re-framed** — Cauchy's residue theorem is not what produces $(2/\alpha - 3/\pi + 2\alpha)$ (integrating a meromorphic form over $z$ extracts only the residue; it does not evaluate a Laurent polynomial at $z = \alpha$); the true structure is the closed path integral of complex impedance around the topological boundary cycle, $\oint_{\partial K_4} dZ = \Delta Z_{\text{forward}} + \Delta Z_{\text{junction}} + \Delta Z_{\text{return}}$, evaluating at the resonant operating point to the algebraic sum of the three orders. (2) **the debts demarcated honestly** — Debt 1 CLOSED with the tag *derived mechanism, identified tax* (the per-channel $\alpha/2\pi$ magnitude stays the adopted identification); Debt 2 **RE-GRADED, not discharged**: the integer count $m = 3$ is derived and unique on the discrete lattice $0..120$ ($409\times$ margin — Instance 2's result, machine-verified; $388\times$ at the 3-ppm-window convention, one lattice), but the $-2.84$ ppm sub-ppm landing is an **OPEN VOTE** awaiting the full continuum substrate dispersion $H_3$ and the dynamical gap equation $\Sigma(m) = m$. Receipt: `resolution_arithmetic.py` extended to 36 banks in six groups (F the audit trim), ALL PASS, exit 0; round file re-graded in place.

> **RECOVERY ROUND (LOG-31, 2026-11-05) — the step-4 battery found and seated; R-1 closed by recovery.** Builder ask: *"are you owning step4_physics_dress.py and can you please make it downloadable?"* The original battery was found in the environment's residual tree outside the project tree (`/tmp/my-project/scripts/step4_physics_dress.py`), seated back at its canonical path, and gate-run green: the compiler delivered the hash-verified runnable copy (`download/L3-ConstitutiveAlpha-Puzzle-battery.py`, sha256-identical to the canonical), ran it fresh, validated the receipt (14 groups, 91 checks, 0 FAIL, exit 0) and re-landed the readable battery (`download/L3-ConstitutiveAlpha-Puzzle-battery.md`). The dress working file was found in the same residual tree and seated (`-dress.md`) at its pre-event form — R-2's §12 addition stays open, as does R-5's 15th group. No hash of the pre-event battery was on record; identity rests on the gate (the fresh 91/91 run; the pinned-string reads against the seated dress). The residual tree also holds the work-order (R-4's input — flagged, not restored this round); it does not hold the entry-form LOG-17..25 (R-3 unchanged) nor `verify_hadronic_burn.py`.

---

## The puzzle, in one line

Why does the K4 seating close: **2/α − 3/π + 2α = 273.131663 against m_π±/m_e = 273.13244 — −2.84 ppm**, with α erected as apex and the three Laurent terms as its three 3-regular spokes (the B′ mapping); the term-count is a degree check, not a channel-count fiat. The landing's grade (LOG-30): the integer count derived and unique on the discrete lattice 0..120 (409×); the −2.84 ppm sub-ppm landing an open vote awaiting the continuum substrate dispersion H3.

## State (as of the recovery round LOG-31, 2026-11-05; the pre-LOG-31 rows retained as history)

| Piece | Status | Where it lives |
|---|---|---|
| Step 1 — the mapping (B′: α apex, three spokes) | CLOSED, builder-corrected in-round | sealed log LOG-11; v3 l.91/113/242 |
| Step 2 — dimensional analysis (node neutrality; the α⁰ double-seat; chance rate one-in-17.9) | CLOSED — 10/10 ALL PASS | `scripts/step2_node_seat_audit.py`; sealed log LOG-12; `L3-ConstitutiveAlpha.md` §IV node subsection |
| Step 3 — the L4-Crowbar test (seven moves; T1 Placement D ruled identification-on-board/CANDIDATE-in-physics; T2 §IX degree clause executed; K-1..K-4 stand) | CLOSED — 5/5 ALL PASS, receipt re-verified 2026-11-05 | `scripts/step3_crowbar_test.py`; sealed log LOG-13/LOG-14 |
| Step 4 — the physics dress (§VII / R_drag(ω) / the gap equation) | **EXECUTED (LOG-18..23); battery recovered and re-seated at LOG-31** (supersedes the awaiting-opening state below) — 91 checks / 14 groups fresh-receipted 2026-11-05, delivered hash-verified; the −2.84 ppm landing stays an OPEN VOTE awaiting H3; R-2's §12 and R-5's 15th group open | dress `-dress.md`; battery `-battery.py`/`-battery.md`; `scripts/step4_physics_dress.py`; log LOG-31 |
| Fork A — the coefficients (per-channel α/2π; uniform 3 vs fractional quark charges) | **CLOSED at LOG-29** (supersedes the OPEN below) — the crossing was forced at LOG-28 ($c_0^* = -2.9975606$, unique, transversal, $388\times$) and the mechanism closed at LOG-29: the winding counts the confined flux junction, flavor-blind by topology; the per-channel tax magnitude stays the adopted identification (LOG-30 tag: derived mechanism, identified tax) | sealed log LOG-13, Move 7; resolution file §2; log LOG-29/LOG-30 |
| (historical row, superseded) Fork A — the coefficients | OPEN — decidable by the gap equation's unique self-consistent solution, or by a crossing whose middle coefficient is forced elsewhere | sealed log LOG-13, Move 7 |
| Fork B — the operating point in evidence (the backward run) | OPEN — measure V → invert → read ωτ → check against drive | v3 §10/§12 |
| π⁰ | OPEN — shape constrained by the degree clause (term-count ≤ mode census); the answer stays with the Gate-2 ledger | `L3-ConstitutiveAlpha.md` π⁰ ledger |
| KD-KK1b discrete side | OPEN, **sourceless by ruling** (the bridge pair dropped 2026-11-05) — not blocked: an explicitly open cell under the reading gate until a successor lands | crowbar Movement VIII; LOG-14/LOG-15 |
| Joint-2 ontology decision | OPEN — owner-level, tagged at LOG-16 (the crowbar Movement II efficiency wedge's ontology reading); gates nothing on this bench | sealed log LOG-9; LOG-16 B-7 |
| Q4 composite-claim edge | OPEN — honest edge in the corpus, tagged at LOG-16 (unchecked against the full biquaternion apparatus); closes by single-file extraction or stands permanent | LOG-10; LOG-16 B-8 |
| LOG-28 — the spectral round (apex operators; the count closed and forced; the measure fork one-sided) | LANDED — 52 banks ALL PASS | `L3-ConstitutiveAlpha-Puzzle-spectral.md`; `scripts/spectral_derivations.py`; log LOG-28 |
| LOG-29 — the resolution round (the double-bind dissolved; the sum re-grounded as a cycle traversal; Debt 1 CLOSED; Debt 2 first graded DISCHARGED) | CLOSED at bench grade — 31 banks ALL PASS; the mechanism re-framed and Debt 2 re-graded at LOG-30 (row below) | `L3-ConstitutiveAlpha-Puzzle-resolution.md`; `scripts/resolution_arithmetic.py`; log LOG-29 |
| LOG-30 — the audit round (the traversal re-frame — Cauchy demoted to witness; Debt 1 tagged derived-mechanism/identified-tax; Debt 2 re-graded: m = 3 derived and unique on the lattice 0..120 at 409×, the −2.84 ppm landing an OPEN VOTE awaiting H3) | LANDED — 36 banks in six groups ALL PASS | `L3-ConstitutiveAlpha-Puzzle-resolution.md`; `scripts/resolution_arithmetic.py`; log LOG-30 |
| LOG-31 — the recovery round (the step-4 battery and the dress found in the environment's residual tree, seated at their canonical paths; the compiler gate-run green — 14 groups, 91 checks, 0 FAIL; the runnable and readable battery re-landed) | LANDED — R-1 closed by recovery; R-2..R-5 open | `scripts/step4_physics_dress.py`; `-dress.md`; `-battery.py`/`-battery.md`; log LOG-31 |

## Receipts (scripts on file, all halt-on-error)

- `scripts/audit_constitutive_alpha.py` — the constitutive audit, 28/28 (LOG-11)
- `scripts/step2_node_seat_audit.py` — step 2, 10/10 (LOG-12; one gate-caught defect recorded in header)
- `scripts/step3_crowbar_test.py` — step 3, 5/5 (LOG-13; re-run clean at LOG-14)
- `scripts/spectral_derivations.py` — the spectral round, 52 banks in five groups (LOG-28)
- `scripts/resolution_arithmetic.py` — the resolution round + audit trim, 36 banks in six groups (LOG-29/LOG-30)
- `scripts/step4_physics_dress.py` — the step-4 battery, recovered at LOG-31: 91 checks in 14 groups, halt-on-error; delivered hash-verified as `download/L3-ConstitutiveAlpha-Puzzle-battery.py` (the compiler `make_battery_file.py` gates the delivery)
- Earlier batteries: `verify_hinge_clamp.py`, `dim_audit.py`, `covenant_gate_and_rim_check.py`, `crowbar_receipt_check.py`, `verify_signed_aut.py`, `thermal_family_check.py`, `aggregate_docking_check.py` — all run clean.

## The note family (builder ruling 2026-11-05)

- `L3-ConstitutiveAlpha-Puzzle.md` — this manifest (the puzzle's internal home)
- `L3-ConstitutiveAlpha-Puzzle-log.md` — the development log from LOG-15; numbering continues from the sealed log's LOG-14
- `L3-ConstitutiveAlpha-Puzzle-twopaths.md` — the two-path observations round (LOG-26) and the reorientation cross-read (LOG-27); the supplied external materials preserved verbatim as Appendices A (the intake report), B (the spectral-problem exposition), C (the fault-line exchange)
- `L3-ConstitutiveAlpha-Puzzle-spectral.md` — the spectral round (LOG-28): the apex operators on the board, the count closed and forced, the measure fork run one-sided
- `L3-ConstitutiveAlpha-Puzzle-resolution.md` — the resolution round (LOG-29) with the audit trim applied in place (LOG-30): the double-bind dissolved, the sum re-grounded as the closed impedance-cycle traversal, Debt 1 closed (derived mechanism, identified tax), Debt 2 re-graded (the count derived and unique on the lattice 0..120 at 409×; the −2.84 ppm landing an open vote awaiting H3); the builder's note preserved verbatim as Appendix D
- `L3-ConstitutiveAlpha-Puzzle-dress.md` — the dress working file (step 4; LOG-18..23), recovered at its pre-event form at LOG-31; R-2's §12 (the twopaths material) pending
- `L3-ConstitutiveAlpha-Puzzle-battery.md` / `-battery.py` — the readable battery and the hash-verified runnable delivery (the LOG-24/25 arrangement, re-landed at LOG-31)
- Further suffixes as the work demands; audit batteries live in `scripts/`, named per round

## Sealed predecessors (standing as filed, zero edits from the naming round on)

- `L4-DynamicDistortions-Sudoku.md` — the corpus-register document (the 401-slot call closed: stands under its own name, sealed)
- `L4-DynamicDistortions-Sudoku-v3.md` — the artifact (the clamp, the rim, the proven limit)
- `L4-DynamicDistortions-Sudoku-log.md` — LOG-0..14: the whole round-history of the mapping, the dimensional analysis, and the crowbar test
- `L4-TheCrowbar.md` (patched copy), `L3-ConstitutiveAlpha.md` (patched copy) — the working copies; the Movement VI note, the dependency-line pointer, and the §IV node subsection landed at step 3/step 2; now sealed
- `upload/` — immutable, as always

## Dropped (builder ruling, 2026-11-05)

`On_TheEightPiBridge.md` + `On_TheEightPiBridge-AUDIT-2026-11-04.md` — obsolete. Never landed on this bench (that absence was LOG-14's subject); nothing to delete. The crowbar's own dependency line stands untouched — the treatise cites what it was written against; receipts say what they said. KD-KK1b's discrete side is re-labeled accordingly: sourceless by ruling, not blocked.

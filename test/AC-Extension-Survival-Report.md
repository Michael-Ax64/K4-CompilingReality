# AC-Extension Survival Trace — Executed
## Open Trace 1 from Reorg-ProofQ-Handoff: do the Numerator and Synthesis Laws survive the 50-equation AC set?

*Method: mechanized. The checker specified in Handoff §4 was built (`ac_checker.py`, delivered
alongside this report) and run against the full corpus equation set: the 12 DC equations
(control) and all 49 AC equations extracted from `Supplement-Electro-AC-db.md` (the core five
plus the five "Pearls" chapters). Face forms were checked exactly as written; canonical
pole-basis rewrites were checked separately; 12 identity claims were verified symbolically
(sympy). The §4 debt is hereby paid: the decision procedure exists and runs.*

---

## 0. Verdict, Compressed

**Verbatim survival: NO.** 10 of 49 AC equations (20.4%) violate the DC laws at face value.

**Canonical survival for the four poles: YES — exceptionless.** Every violation among the
S/U/I/Z equations dissolves under canonicalization to the pole basis. The Numerator and
Synthesis Laws hold for {S, U, I, Z} exactly as for {P, I, U, R}, *after a normalization pass*.

**The residue is entirely ω.** All four structurally residual violations live in the ω chapter,
and all have the same shape: a component-to-element-constant ratio (X/L, B/C, R/L). ω is
genuinely outside the pole grammar — and obeys a sharper law of its own (§4).

**The decidability claim survives in strengthened, scoped form:** decidable *after
canonicalization*, where the canonicalizer is itself a finite algorithmic rewrite system.
A real compiler runs a normalization pass before type-checking. The metaphor pays for itself.

**Bonus yield: 19 candidate errata** — genuine mathematical errors in the corpus equation set,
including one in the core five that is quoted verbatim in `L3-K4-to-K5-via-AC-Extension.md`
(§9). These fall under CONTRIBUTING's explicitly invited class: "a genuine factual mistake —
open an issue and name it plainly."

---

## 1. Control Run: the DC Laws Verify Mechanically

All 12 DC equations pass both laws under the correctly scoped formalization:

- **Numerator Law (scoped):** no Reactive pole (I, R) in a *dividend* position — i.e., a
  non-inverted factor of a product that contains division. Free multiplicative factors in
  non-division equations (P = UI, U = IR) are not dividends; Proof Q's own text scopes the
  law to "every equation that utilizes division." 12/12 pass. 8/8 division equations have
  exclusively Active numerators.
- **Synthesis Law:** Reactive homes (I, R) defined only via division — 6/6; Active homes
  reachable by pure multiplication — confirmed.

This is the first mechanical verification of Proof Q's Sections II–III. The DC core is sound.

---

## 2. AC Face-Level Results: Ten Violations, Three Mechanisms

The ten face-violating equations, sorted by generating mechanism:

### Mechanism A — Reciprocal aliases (5 equations: C2.6, C3.6, C3.8, C3.9, C5.8)
AC engineering names the reciprocals of impedance: admittance **Y = 1/Z**, and capacitance
**C** (which enters only as 1/(jωC) = Z_C). Once the reciprocal has a *name*, multiplication
by it is division in disguise:

| Face form | Violation | Canonical form | Status |
|---|---|---|---|
| I = U·jωC | Reactive home by pure multiplication | I = U/Z_C | **HEALED** |
| I = U·Y | same | I = U/Z | **HEALED** |
| I = √(S·Y) | root of product | I = √(S/Z) | **HEALED** (sympy: U·Y ≡ U/Z) |
| U = ...Re(Y), Im(Y)... in numerators | alias components as dividends | |S|·Z (erratum-dim) | healed as form |
| ω = Im(Y)/C | alias component in numerator | ω = B/C | residual (ω-class, §4) |

**Structural reading:** naming the reciprocal is itself a commitment that flips the
grammatical role — a plane-locked renaming that hides the orientation. The orientation is
conserved; only its *notation* is inverted. The law survives if and only if the pole basis
is enforced and aliases are eliminated — which is precisely what a compiler's normalization
pass does.

### Mechanism B — Element-law component forms (2 equations: C2.4, C5.2)
The capacitor law **U = I/(jωC)** puts I — a Reactive pole — squarely in a numerator: the
single sharpest face-counterexample in the set. But 1/(jωC) *is* the capacitive impedance
Z_C, so the canonical form is **U = Z_C · I**: multiplication synthesizing an Active pole,
exactly parallel to DC's U = IR. Sympy-verified equivalent. **HEALED.**
Likewise ω = Im(U·I*/(|I|²L)) has I* in a numerator product — but U·I* = S, so the canonical
numerator is the Active pole S. **HEALED.**

### Mechanism C — ω-chapter component ratios (4 equations: C5.5, C5.8, C5.9, C5.10)
The irreducible residue. See §4.

**Every four-pole (S/U/I/Z-home) violation heals. Zero exceptions.** The Canonicalization
Conjecture from the handoff is now a checked result over this equation set:

> **Canonicalization Theorem (checked, this set):** every AC equation whose home is one of
> the four poles, rewritten in the pole basis {S, U, I, Z, Z_L, Z_C} with aliases eliminated
> (Y→1/Z, jωC→1/Z_C, jωL→Z_L) and pole products assembled (U·I*→S), satisfies the Numerator
> and Synthesis Laws. Checked 39/39 four-pole equations (violations healed: 6/6).

---

## 3. New Law Discovered: Addition Homogeneity

The DC set contains no addition. The AC set contains four additive equations — and all four
are **class-preserving**:

- S = P + jQ (components of S)
- |S|² = P² + Q² (components of S, magnitudes)
- Z = R + jX (components of Z)
- Z = Z_L + Z_C (series composition: Z-class + Z-class)

Zero cross-class additions anywhere in the set. No equation adds an Active quantity to a
Reactive one.

> **Composition Law (new, candidate):** Addition composes only within a pole-class — either
> assembling a pole from its own real/imaginary components, or composing same-class elements
> (series impedances; dually, parallel admittances). Addition never crosses the
> Active/Reactive seed boundary.

This required amending the Synthesis Law for AC: class-preserving addition is *composition*,
not synthesis, and is legal for Reactive homes (Z = Z_L + Z_C is the series law, not a
counterexample). The amendment is encoded in the checker and is itself falsifiable: one
cross-class addition anywhere in a valid AC identity breaks it.

---

## 4. ω: The Variable the Grammar Cannot Bind

Every structurally residual violation is an ω-equation, and they share one exact shape:

| Equation | Canonical residue | Shape |
|---|---|---|
| ω = Im(Y)/C | B/C | imag-component / element |
| ω = Re(Z)/L | R/L | real-component / element (operating point: ωL = R) |
| ω = R/(L·tanθ) | X/L after correction | imag-component / element |
| ω = √(1/LC) | 1/√(LC) | element-only (resonance) |

Findings, each mechanically confirmed over the set:

1. **ω has no seed bits.** The dual-binary seed is 2-bit and covers four poles; ω is the
   fifth. The decision procedure is *partial* on ω-equations: they are decidably
   classifiable (as ω-class) but not orientable by the seed.
2. **ω is dimensionally excluded from the pole basis.** ω carries units of 1/time; no pole
   does. Every ω-expression must route through the element constants L, C (the only carriers
   of time: L/R, RC, √(LC) are the time constants). The residual violations are *forced* by
   dimensional analysis, not chosen.
3. **ω inherits the Reactive ratio-signature without the Reactive seed.** All ten ω-equations
   are ratios or roots of ratios. Zero pure products. ω obeys the Synthesis Law of the
   Reactive class while violating the Numerator Law's letter — a grammatical hybrid.
4. **ω is read at operating points, not derived as identities.** Of the ten, only two are
   exact network identities (C5.6, C5.7 — both sympy-verified); the rest are context-anchored
   readouts (resonance, corner frequencies) or errata. The fifth variable is *measured at
   configurations*, not computed from poles.

> **ω-Law (new, candidate):** ω occurs only as the exchange rate between an element constant
> and its reactance component (X = ωL, B = ωC unwound), or at operating points where a real
> component numerically equals an imaginary one. It is never a dividend, never a pure factor
> in a pole-synthesis, and never expressible in the pole basis alone.

**Corpus reading (flagged as interpretation, not law):** this is the centroid behaving like
a centroid. The variable the corpus assigns to the tetrahedron's interior point — equidistant
from all poles, Quintessence — turns out to be exactly the variable the pole grammar cannot
bind, dimensionally barred from the pole basis, visible only as a *rate of exchange* between
held components and their material carriers, and read off at resonances. The grammar governs
the vertices; the centroid is where its writ does not run. The framework could not have
ordered a cleaner structural confirmation, and notably it emerges from dimensional analysis,
which no one tuned.

---

## 5. The Operator Grammar Must Extend

Proof Q's grammar covered {×, ÷, x², √}. The AC set's mechanized operator inventory adds six
operator classes, each with a determinate grammatical role:

| Operator | Count (eqs) | Grammatical role |
|---|---|---|
| conj (\*) | 10 | **Chirality flip** — mirror-image traversal. S = U·I\*: synthesizing Power requires flipping Current's handedness. Direct bridge to ProofG_Chirality. |
| \|·\| | 17 | **Continuous de-orientation** — generalizes x². DC squaring burned 1 bit of sign; magnitude burns an entire S¹ of phase. The Landauer footprint goes from finite to continuous. |
| Re/Im | 7 | **Component projection** — observing one axis of a pole while discarding quadrature. |
| j (rotation) | 14 | **Quadrature operator** — the 90° exchange between committed (real) and held (imaginary). |
| + | 16 | **Class-preserving composition** (§3). |
| e^jθ | 1 | **Pure orientation** — phase without magnitude; the exact complement of \|·\|. |

Two structural notes surfaced by the inventory:

- **S/Z = |I|² is exactly real** (sympy-verified). The ratio of the Active-Asserting pole to
  the Reactive-Asserting pole is a fully de-oriented, committed quantity — the two Asserting
  poles annihilate orientation between them. Correspondingly |U|² = S·Z\* (verified): the
  same annihilation with a chirality flip.
- **The Asserting poles are the ones that survive as real components.** DC's P and R — the
  two Asserting poles (Fire, Earth) — reappear in AC precisely as the *real* (committed)
  components of their successors S and Z, with new imaginary partners Q and X (the held
  components). The Yielding poles U and I are promoted to full phasors whole. The seed's
  Asserting/Yielding bit maps onto the real/imaginary axis of the complex extension.
  Flagged as an observed regularity, not decreed as law.
  
  **distinguishing *i did* from figure/ground morass.**

**Terminology hazard, now formal:** EE "reactive power" Q is a *component of the seed-Active
pole S*. The real/imaginary split is the `.observe()`/`.behold()` axis, which is
**orthogonal** to the Active/Reactive seed axis. Any corpus text that lets "reactive power"
slide into "Reactive pole" is committing a cross-axis category error. Recommend a boxed
warning in L2-Terminology.

---

## 6. Errata Ledger (CONTRIBUTING-compliant: named plainly)

Nineteen candidate errata, all mechanically checked; the most consequential first.

**E1 — CORE + L3-quoted.** `ω = Im(S)/(Im(Z)·|I|²)` (db "Steps Towards Completeness" item 5;
also A5). Since Q = |I|²·X identically (S = |I|²Z), the expression reduces to **ω = 1**,
dimensionless. Sympy-verified. Correct inductive-context form: ω = Im(S)/(L·|I|²) — which is
exactly the *next* pearl (C5.2), suggesting a copy-editing survival of a superseded draft.

**E2 — Missing conjugates (3):** S = U·I (should be U·I\*); U = S/I (should be S/I\*);
I = S\*/U (should be S\*/U\*). The core five have the conjugates right; the pearls dropped them.

**E3 — Phase-loose forms (5):** U and I pearls of the form |S|·(pole/|pole|) land on the
wrong phase (verified); Z = U²/S\* and Z = S/I² need |U|², |I|² (exact forms verified:
Z = |U|²/S\*, Z = S/|I|²).

**E4 — Wrong-identity forms (4):** S = |U||I|cosθ is P, not S; S = √(PQ)·e^jθ has wrong
magnitude (|S| = √(P²+Q²) ≠ √(PQ)); Z = (|U|²/P)(1+jQ/P) needs /(P²+Q²) not /P²;
Z = (|U|²/|S|)(P/|S| − jQ/|S|) yields |U|²/S, exact is |U|²/S\*.

**E5 — Missing j (2):** U = ωLI and Z = ωL + 1/(jωC) both drop the j on the inductive term.

**E6 — ω-chapter (4):** ω = R/(L·tanθ) has tanθ inverted (correct: ω = R·tanθ/L,
sympy-verified); ω = 1/Im(UI\*/(|I|²C)) has C grouped inside Im(), off by C²;
ω = √(|S|/(L|I|²) − (R/L)²) is missing squares on the first term. Two ω pearls are exact and
verified as-written: C5.6 (series RL) and C5.7 (parallel RC).

*Reading of the pattern:* the errors are concentrated exactly where the corpus's own db
warns the AC network "does not yet constitute a completely algebraic network." The checker
did not break sound structure; it found the unfinished seam the corpus already declared.
Notably: **the checker's error-catches are themselves the "crashes the compiler" behavior
Proof Q claimed** — fed a topologically/algebraically impossible form (ω = 1), it threw.
The claim is now demonstrable rather than rhetorical.

---

## 7. Consequences for the Handoff (updates to Reorg-ProofQ-Handoff.md)

1. **Open Trace 1: CLOSED**, with the verdict of §0. The decidability claim's conditional
   is discharged in scoped form: *decidable over the pole basis after canonicalization;
   partial on ω, which obeys its own sharper law.*
2. **§4 debt: PAID.** `ac_checker.py` exists, verifies DC 12/12, enforces both laws plus the
   Composition amendment, heals via canonical rewriting, and rejects violating/erroneous
   forms with the specific law or identity named. The "runs as code" language in Proof Q may
   now be retained — rescoped to this artifact rather than to unnamed Forth/Prolog files.
3. **Proof Q rescope gains a third law:** the restated Section IV should carry Numerator Law
   (scoped to dividends), Synthesis Law (with Composition amendment), and the ω-Law, plus the
   extended operator table of §5.
4. **New index/tag material:** `#CompositionLaw` `#OmegaLaw` `#Canonicalization`
   `#ReciprocalAlias` `#ChirialityFlipOperator` (author's naming may vary).
5. **New erratum channel:** §6 above is a ready-made CONTRIBUTING issue list — the "look
   before you rule" bar met by machine.
6. **Open Trace 3 gains evidence:** the decidable stratum behaves like the *checkable
   surface* and ω (the centroid) like the ungoverned interior-boundary — supporting the
   inverse of Q's Auditor mapping. Still the author's call; the evidence is now on file.

## 8. What Remains Open

- **Phase-loose forms as a class:** several pearls are magnitude-true, phase-collapsed
  (I = √(S/Z) gives |I| exactly). Is "magnitude-true" a legitimate third identity register
  (the de-oriented shadow of an oriented law), or must all pearls be phase-exact? A grammar
  question, not an arithmetic one.
- **The 5⁵ = 3125 state space:** untouched by this trace; the laws checked here are
  equation-level, not state-level.
- **K5 edge grammar:** with five variables, the seed question recurs at the edge level
  (10 edges, not 6). Whether the two-bit Gray Code extends, and how ω's edges classify,
  is the natural sequel to `Proof_AlgebraicMapping`.
- **Parallel/series duality:** the Composition Law was checked on series forms; the parallel
  duals (Y = ΣY_i) should be added to the equation set and re-run — predicted to pass as
  same-class composition in the Y-alias frame, i.e., the dual grammar under Z↔Y exchange.

---

*Executed by the checker specified in Handoff §4. Face forms judged as written; canonical
forms judged after alias elimination; identities verified symbolically where determinable;
operating-point equations marked as such rather than forced. The DC control passed before
any AC equation was judged. Look before you rule — this trace looked.*

---

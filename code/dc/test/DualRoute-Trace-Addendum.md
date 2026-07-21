# Dual-Route Trace — Executed
## Open Trace 2 from Reorg-ProofQ-Handoff: is the linear/nonlinear pairing systematic?

*Method: mechanized (`dual_route_trace.py`, delivered). Every equation classified by route
type (linear / square / root / shadow); the candidate Route Law tested on the DC set as
control, then on the identity-class AC equations as survival. One classifier bug was found
and fixed during the run (denominator squares, exponent −2); one component idiom was added
to canonicalization (√(P²+Q²) → |S|). Both fixes are visible in the delivered script.*

---

## Verdict

**The Route Law holds — DC exceptionless (12/12), AC identity-class survives (8/8 nonlinear
routes confirm, 0 violations).** The 2×2 table is promoted: it earned its place.

## The Law (now checked, stated at full strength)

**R1 (Completeness).** Every DC pole has exactly three routes — one per pair of the
remaining three poles. 12 = 4 × 3.

**R2 (Square routes → Asserting).** Every square route lands on an Asserting home (P, R);
the squared operand is always a Yielding pole (U, I); the co-factor is always the *other*
Asserting pole. 4/4: P = U²/R, P = I²R, R = U²/P, R = P/I².

**R3 (Root routes → Yielding).** Every root route lands on a Yielding home (U, I); the
radicand's poles are *exclusively the two Asserting poles*. 2/2: U = √(PR), I = √(P/R).

**R4 (Census symmetry).** Asserting homes: 1 linear + 2 square routes. Yielding homes:
2 linear + 1 root route. Set-wide: exactly 6 linear + 6 nonlinear equations. Verified.

## AC survival, with exact analog mapping

| AC route | DC analog | Note |
|---|---|---|
| U = √(S·Z) | U = √(PR) | radicand = both Asserting-successors, exact |
| I = √(S/Z) (×3 forms) | I = √(P/R) | exact; S/Z is *real* — see asymmetry below |
| Z = \|U\|²/S* (×2 forms) | R = U²/P | de-oriented Yielding operand + Asserting co-factor, **with chirality flip added** |
| Z = S/\|I\|² | R = P/I² | exact |
| Z = \|S\|/\|I\|² | R-magnitude | shadow route; lands on \|Z\| (see below) |

## Consequences

**1. Both seed bits now carry operator signatures.** The Numerator Law marked the first bit
(Active/Reactive: division orients, dividend Active, divisor Reactive). The Route Law marks
the second bit (Asserting/Yielding: **squaring is the arrow into Asserting; rooting is the
arrow into Yielding**). The operator grammar is two-dimensional, matching the seed's two
dimensions. This does not derive the seed's *content* — the standing boundary holds — but
the corroboration constraint is now a full 2-bit check, not a half-check. Proof Q v2 §II–III
should be extended with R1–R4 as **Law 5 (Route Law)**.

**2. The `.observe()`/`.behold()` cycle is inscribed in the route structure — as a checked
result, no longer an aesthetic.** Asserting poles are *manufactured by collapse*: every
nonlinear route to P or R squares (de-orients) a Yielding pole against the other Asserting
pole — the committed is made from the collapsed possible. Yielding poles are *projected by
reopening*: every nonlinear route to U or I takes the root of the pure-Asserting
combination — the possible is drawn back out of the settled. Six linear, six nonlinear: the
surface reading and the interior reading of the same four poles, in exact balance.

**3. The Landauer ledger is balanced in DC and asymmetric in AC.** In DC, √ fully repays
what ² burned: one bit, the ±. In AC, every root route lands *magnitude-true only* —
mechanically evidenced by S/Z = |I|² being exactly real (verified in the survival report).
The root repays one bit; it cannot repay the continuous S¹ of phase burned by |·|. Finite
collapses are recoverable by the grammar's own re-orientation operator; continuous collapses
are not. Deep commitments differ in *kind*, not just degree, from shallow ones.

**4. Route discipline predicts the error class.** The three equations that route an
*oriented* home through *de-oriented* operands (C2.2, C3.4, C4.8 — |S|-fed forms) are
exactly the three the identity trace independently flagged as phase-errata or
magnitude-only. Analysis of the two phase-errata shows the precise failure: having burned
the phase in |S|, the equations re-orient by borrowing a unit phasor — and borrow it from
the *wrong pole* (landing on φ_I where φ_U is required, and vice versa; sympy-confirmed in
the survival report). The grammar does not merely reject these; it *diagnoses* them:
orientation, once burned, must be re-supplied from the correct source, and the route shows
which source was used. (Prediction verified by cross-referencing the two independent traces;
the shadow-route detector is in the script; the phase-source diagnosis was hand-verified.)

## Standing questions the trace opens

The AC set's S-chapter is route-incomplete (the corpus's own admission that the AC network
"does not yet constitute a completely algebraic network" shows up here concretely: the
square-routes *to S* — the analogs of P = U²/R, P = I²R, e.g. S = |U|²/Z*, S = |I|²Z — are
derivable but absent from the pearl set). Prediction, falsifiable: when written, they will
obey R2 with the chirality flip (S = |I|²Z is exact; S = |U|²/Z* is exact). Adding them and
re-running is a one-line-per-equation task in the delivered script.

Whether R1–R4 extend to K5 — ten edges, ω present — remains bound to falsifier 5 of
Proof Q v2. ω took no part in any route: consistent with its centroid status.

---

*Open Trace 2: CLOSED — Route Law promoted. The 2×2 table (linear/nonlinear × the two
routes per side) is load-bearing: it is the operator signature of the seed's second bit,
and the equation-set inscription of the collapse/reopen cycle. Body integration into
Proof Q v2 to be walked by the author.*

# The Tribunal Manifold — A K4 Topological Diagnostic Engine

A small, five-file executable extrusion of the *Compiling Reality* codex. It takes a
description of a system in some state of imbalance, runs it through a Prolog
constraint engine that enforces the closed algebra of four mutually-determining
electrical variables, and returns a diagnosis: which variable is starved, which
face of the tetrahedron you've fallen onto, and what that face's equations have
to say about your situation — argued out loud, by the equations themselves.

It is simultaneously two things, and it's worth being precise about which one you're
looking at at any given moment:

1. **A proof.** A falsifiable claim — that four specific real quantities are bound
   by exactly twelve equations with no thirteenth degree of freedom, and that the
   *syntactic shape* of those equations (where a variable sits, whether it's squared
   or rooted) is not decoration but is itself doing classificatory work — reduced to
   code and checked by SymPy and Prolog rather than merely asserted in prose.
2. **An explorative toy.** A way to feed a system a rough shape ("we're all rules and
   no traction," "we're grinding," "we're perfectly balanced") and watch the
   tetrahedron's geometry generate a specific, structured, argued response rather
   than a generic one.

Both readings are legitimate and neither excuses the other — the toy only has
teeth because the proof underneath it is real math, and the math only earns
your attention here because it's wired up to something you can actually run.

It is a great demo?  no.
  * [ ] 
Does it let you see what the codex derives?  well... some. it demoes the engine.

---

## 1. Installation

You need two runtimes: **SWI-Prolog** (for the constraint engine) and **Python 3
with SymPy** (for the checkers and the semantic bridge).

### SWI-Prolog

```bash
# Debian / Ubuntu
sudo apt-get update
sudo apt-get install swi-prolog-nox # -nox: no GUI deps, all you need for this

# macOS (Homebrew)
brew install swi-prolog

# Windows
# Download the installer from https://www.swi-prolog.org/download/stable
```

Verify:

```bash
swipl --version
# SWI-Prolog version 9.x.x for ...
```

This engine was built and tested against **SWI-Prolog 9.0.4**. It uses no
version-specific syntax and should run on any reasonably recent SWI build (9.x;
likely 8.x as well, untested).

> **A note if `apt-get update` fails with a `nodesource` / 403 error:** this is
> an unrelated broken third-party repo some systems have configured for Node.js,
> not a Prolog problem. Remove or disable it and retry:
> ```bash
> manually rm /etc/apt/sources.list.d/nodesource*.list
> sudo apt-get update
> sudo apt-get install swi-prolog-nox
> ```

`library(clpr)` (constraint logic over reals), used only for the *declarative*
statement of the algebra (see §3.4), ships with the standard SWI-Prolog
distribution — no separate install needed.

### Python

```bash
pip install sympy
# or, in externally-managed environments:
pip install sympy --break-system-packages
```

Tested against **SymPy 1.14.0**. No other dependencies.

### Running it

```bash
python3 tribunal.inquiry.py --prompt "we're all rules and no traction, totally stuck"
python3 tribunal.inquiry.py --prompt "we're grinding, forcing everything"
python3 tribunal.inquiry.py --prompt "everything is perfectly balanced"
python3 tribunal.inquiry.py --prompt "random"
```

All five files must sit in the same directory. `tribunal.inquiry.py` invokes
`swipl` as a subprocess against `tribunal.manifold.pl`, then hands the result to
`tribunal.dc_inquiry.py`, which imports `tribunal.ac_checker.py` and
`tribunal.dual_route.py` directly.

---

## 2. The five files

| File | Role |
|---|---|
| `tribunal.manifold.pl` | The K4 constraint engine. Given a baseline and a current state, computes dimensionless drift on all four poles, finds the starved variable, and convenes the corresponding tribunal. |
| `tribunal.inquiry.py` | The orchestrator. Turns a human sentence into a rough numeric drift, calls the Prolog engine, and hands its output to the semantic bridge. |
| `tribunal.dc_inquiry.py` | The semantic bridge. Walks the AST of each equation the tribunal produced and reports what its *syntactic shape* means. |
| `tribunal.ac_checker.py` | The Orientation-Grammar checker. A from-scratch, independently-verifiable pass over 12 DC + 49 AC electrical-engineering equations, checking two structural laws against a real EE reference set. |
| `tribunal.dual_route.py` | The Route Law tracer. Independently proves that "squared" and "rooted" equations sort cleanly by pole-type across both the DC and AC equation sets. |

The last two are the proof engine. The first three are the toy built on top of it.

---

## 3. The science: what's actually being claimed and checked

### 3.1 The four variables

The framework maps four electrical quantities onto four general-purpose roles:

| Symbol | Electrical quantity | Role |
|---|---|---|
| **P** | Power | Drive — committed, realized output |
| **U** | Voltage (European convention) | Structure — the standing potential/blueprint |
| **I** | Current | Flow — the realized relational movement |
| **R** | Resistance | Ground — the material constraint |

These are related by exactly two seed equations — Ohm's Law (`U = I·R`) and the
power law (`P = U·I`) — from which the other ten follow by substitution. All
twelve are algebraically forced; there is no thirteenth free equation and no
missing one. That closure is the whole basis for calling this a *diagnostic
engine* rather than a metaphor: you cannot adjust three of the four variables
independently, because the fourth is always already determined.

### 3.2 The K4 tetrahedron and the four faces

Four variables, every pair connected: that's the complete graph on four
vertices, `K4` — six edges (the six mutually inverse equation-pairs), four
triangular faces. Each face is exactly the three equations that *don't* mention
one variable. That missing variable is the **AbsentVar** — the thing the system
in that state is structurally incapable of drawing on.

Feed the engine a state where three of the four variables have drifted from
baseline and one hasn't, and it can tell you exactly which face you're standing
on, because the face is not an interpretation — it's whichever triangle's three
equations best explain the drift you supplied.

### 3.3 Why squaring and rooting aren't decoration (Proof Q)

This is the sharpest empirical claim in the codex, and the one this repo
actually tests rather than asserts.

Split the four variables along one more axis: P and R are **Asserting**
(committed, ledger-side); U and I are **Yielding** (held, relational-side).
Now look at where squares and square roots land across all twelve equations:

- Every equation with a **square** (`P = I²R`, `P = U²/R`, `R = U²/P`, `R = P/I²`)
  has an Asserting variable (P or R) on the left.
- Every equation with a **square root** (`I = √(P/R)`, `U = √(P·R)`) has a
  Yielding variable (I or U) on the left.
- The remaining six equations are linear, and split 1-linear-per-Asserting-home
  vs 2-linear-per-Yielding-home, exactly matching what's left over.

This is not asserted — `tribunal.dual_route.py` walks the actual SymPy
expression tree of every equation and checks it mechanically. It holds
**exceptionlessly** across all twelve DC equations, and survives (with the
predicted, correctly-flagged exceptions) across a 49-equation AC power-and-
impedance set independently checked by `tribunal.ac_checker.py` against a real
electrical-engineering reference — including catching real textbook-style
errata (missing conjugates, missing `j` on reactive terms, dimensionally wrong
forms) and supplying SymPy-verified corrected forms for them.

Squaring destroys sign/direction (`x² = (-x)²`) — algebraically, it's a
one-way, irreversible commitment. Rooting restores it, at the cost of
introducing an ambiguity (`√4 = ±2`) — a reopening. The claim is that this is
*why* squares land on the committed/ledger side and roots land on the
held/relational side: the operator's own algebra matches the role. This repo
doesn't ask you to accept that reading — it hands you the checker and the
reference output so you can see whether the pattern actually holds.

### 3.4 Why the tribunal solves deterministically, not via constraint search

`tribunal.manifold.pl` declares the twelve-equation closure once, as
`k4_volume/4`, using `library(clpr)` — this is the **canonical statement** of
the algebra and is the right tool for stating "these twelve equations hold
simultaneously." But `clpr`'s nonlinear solver is a numeric search, not exact
arithmetic: given only two of the four variables, it can fail to close certain
pairs (empirically, the Flow+Structure pair) on floating-point residuals in a
redundant constraint, even though the pair is not actually under-determined.

For the runtime diagnosis, what matters is the **heuristic** — which pole is
starved, which face convenes — not machine-precision values. So the actual
solve at runtime (`solve_state/8`) fills in the other two variables from any
two known ones by direct substitution along the twelve equations, deliberately
staying loose about floating-point epsilon rather than trusting a general
nonlinear solver to converge. This is a design choice, not a workaround: the
tribunal wants the right diagnosis quickly and robustly, not a numerically
fragile proof of closure it doesn't need at that step.

---

## 4. Running it as a proof

```bash
python3 tribunal.ac_checker.py     # 12 DC + 49 AC equations, checked cold
python3 tribunal.dual_route.py     # the square/root sorting law, checked cold
```

Both scripts are self-contained and print their own verdicts, including a set
of SymPy identity verifications at the end (e.g. confirming `S/Z = |I|²`,
`Z = |U|²/S*` algebraically, not by assertion). Run them yourself; nothing
here asks to be taken on faith. The corpus itself invites this posture
directly: *"the math is open for audit."* If you find an equation that doesn't
sort the way the Route Law predicts, that's a real falsification, not a bug
report against this code.

## 5. Running it as a toy

```bash
python3 tribunal.inquiry.py --prompt "<any sentence describing a lopsided situation>"
```

The orchestrator's natural-language parsing is intentionally thin (`"grind"`,
`"bureaucracy"`, `"random"`, or `"balanced"` trigger four preset drift
patterns) — it's a demonstration harness, not an NLP system. What's real is
everything downstream of the parse: the drift you feed in genuinely determines
which face convenes, which equations get read out, and what the semantic
bridge says about their syntax. Try feeding it two different values for the
same two variables (say, high Structure / low Ground vs. high Drive / low
Structure) and watch the diagnosis — and the specific equations quoted in
support of it — change in a way that's traceable back to §3.2 and §3.3, not
templated per-prompt.

### A known, honest limitation

Not every face is reachable. Because `Structure`'s drift is always the
geometric mean of `Drive`'s and `Ground`'s drift (`U = √(P·R)` in drift-space),
Structure can never be the most extreme variable — it's proven algebraically
and confirmed by Monte Carlo sampling (200,000 random valid states, zero
counterexamples) in the course of building this. So the "Grinding" face
(Structure-absent) and any "Structure is the Vortex" diagnosis are dead code
under the current routing rule. This isn't hidden or patched over — it's a
real structural fact about the geometry as implemented, and changing it would
require changing what "starved" means (e.g. routing by face-drift rather than
single-pole drift), which is a design decision left open rather than made
silently on your behalf.

---

## 6. The grain: two things the algebra structurally refuses, and an old intuition they echo

Two separate facts fell out of testing this engine, and they're worth naming
together because they're the same *shape* of fact, occurring at two different
points in the same closed system.

**Fact one (proven, §5):** Structure (U) can never be the most extreme
variable — never the Vortex, never the AbsentVar — because its drift is
always exactly the geometric mean of Drive's and Ground's. It is
mathematically confined to the middle.

**Fact two (checked directly above, algebraically):** Ground (R) cannot
reach zero as an ordinary limit. Two of the twelve equations —
`I = U/R` and `P = U²/R` — have R in the denominator; as R → 0 with U held
finite, both blow up to infinity. This is a genuine **pole** in the algebra,
not merely an extreme-but-attainable value the way, say, I → 0 is (which
resolves cleanly, since `U = I·R` just goes to zero with it). R = 0 is a place
the closed system cannot actually stand.

Neither of these is a bug or a numerical artifact — both were confirmed by
direct algebraic derivation, not just by running the code and noticing an
absence. They are the shape of the twelve equations themselves.

It's worth naming what that shape resembles, carefully: the historical
concept of a **luminiferous aether** was, in its own terms, a hypothesized
perfectly rigid, dissipation-free medium — a background substrate whose
defining property was essentially *zero resistance*, required to exist so
that everything else (the propagation of light, of force) had something to
be relations *in*, while the medium itself was never supposed to show up as
an extreme, directly measurable quantity in its own right. Every direct
attempt to catch it doing something detectable — most famously
Michelson–Morley — came back null, not because the concept was
uninteresting, but arguably because a "zero-resistance background structure"
is not, by its own logic, the kind of thing that surfaces as an extremal
reading; it's the thing the extremes are measured *against*.

That is the resonance worth delineating, not a claim that this algebra
explains or resurrects aether theory. It is an observation that a formally
closed, four-variable system — arrived at here from electrical algebra, with
no aether concept anywhere in its construction — independently produces the
same two-part signature: a "structure" term that is mathematically barred
from ever being the extreme, and a "ground/resistance" term whose zero-point
is a genuine pole rather than a reachable state. The corpus reads this as
convergent discovery — the same structural necessity showing up wherever a
closed mutual-determination system is honestly worked out, regardless of
which domain's vocabulary you started from. Whether that reading is warranted
is a separate question from whether the algebra behaves this way; the algebra
demonstrably does, and that part you can check yourself, above.

--

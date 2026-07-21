# Compiling Reality — Substrate Pipeline

A minimal executable realization of the operators the *Compiling Reality* corpus asserts. Two independent substrates (Haskell and Common Lisp) each read scenario specifications in S-expression form, run them through the framework's operators, and emit a log tagged with epistemic tiers. A shell pipeline runs every scenario through both substrates and confirms cross-substrate agreement on the emitted tier set.

The point of this pipeline is not to *simulate physics*. The K4 substrate is combinatorial. What the substrates enforce is what the corpus itself claims can be enforced at the algebra-and-runtime level: the Route Law's squaring operation, the Star-Norm invariant, Inversion of Control via callback registration, the 8-fold filter topology of the membrane, the Q8 tangent-impedance identity, the forward arrow of recursive scaling, the Tribunal's four failure modes, and the Buffer/Indeterminate lexical rule. Everything is emitted with its epistemic tier attached; nothing is dressed above its warrant.

## Layout

```
.
├── README.md                    -- this file
├── run_pipeline.sh              -- shell driver
├── Cosmos.hs                    -- Haskell substrate
├── cosmos-v3.lisp               -- Common Lisp substrate
├── inputs/                      -- scenario specifications
│   ├── 01-healthy-reactor.sexp
│   ├── 02-bloated-bureaucracy.sexp
│   ├── 03-nested-civilization.sexp
│   ├── 04-frequency-sweep.sexp
│   └── 05-panic-trap.sexp
└── demo-run/                    -- captured logs from a real run
    ├── 01-healthy-reactor.lisp.log
    ├── 01-healthy-reactor.hs.log
    └── ...
```

## Requirements

- `sbcl` (Steel Bank Common Lisp), any recent version
- `ghc` and `runghc` (Glasgow Haskell Compiler), 9.x

Both are available in Ubuntu/Debian via `apt install sbcl ghc`.

## Running

```
bash run_pipeline.sh
```

This iterates over every `inputs/*.sexp`, runs it through both substrates, writes the logs to `demo-run/`, and confirms that both substrates emitted the same set of epistemic tiers.
Divergence, if any, is reported. The captured logs under `demo-run/` in this distribution were produced by a real run and are checked in.

You can also invoke either substrate directly:

```
sbcl --script cosmos-v3.lisp inputs/01-healthy-reactor.sexp
runghc Cosmos.hs               inputs/01-healthy-reactor.sexp
```

## The input format

Each scenario is a single S-expression of the form:

```
(scenario
  :name         "name"
  :description  "prose description of what this scenario exercises"
  :frame        (:p ... :u ... :i ... :r ... :l ... :c ... :omega ... :topology <sym>)
  :child-frame  (:name "..." :u ... :i ... :l ... :c ... :topology <sym>)     ;; optional
  :frequency-sweep (<w1> <w2> ...)                                              ;; optional
  :callbacks    <n>                                                             ;; optional
  :ticks        <n>)                                                            ;; optional
```

`:topology` accepts any of the nine names from `L6-TheCircuit` §V:
- viable: `series-gate`, `parallel-shield`, `impedance-divider`, `grounding-bottleneck`, `momentum-filter`, `anticipatory-gate`
- fatal: `bipolar-short`, `nostalgia-trap`, `panic-trap`

Optional keys can be omitted. The Lisp substrate parses the file via native `read`; the Haskell substrate uses a minimal built-in S-expression parser (about 40 lines).

## The output format

Each run emits a log with lines of the form:

```
[TIER] message
```

where `TIER` is one of:

- `COMPUTED` — a value the framework's own algebra emitted
- `SKETCH` — a structural alignment, tagged honestly (e.g. Q1 charge derivation)
- `RESONANCE` — the membrane is transparent; a clean crossing has fired
- `NOTCH` — the grounding bottleneck has throttled throughput
- `SHIELD` — a parallel-shield frame has bypassed external callbacks
- `INTERFACE:TangentCrossing` — the frame has reached a boundary its own coordinates cannot describe; the failure mode is named
- `INTERFACE:Asymptote` — a coordinate divergence (e.g. `ω=0` DC limit)
- `INTERFACE:UltimateBoundary` — the keystone; no operation consumes the indeterminate

The tag discipline follows `About-Claims`: no claim is dressed above its warrant.

## The scenarios in this distribution

### 01 — healthy-reactor

A bounded frame driven at its resonant `ω₀ = 1/√LC`. Series-Gate topology, moderate Q-factor. 
The tribunal emits only `[COMPUTED]` lines; no boundary crossing fires.
Callbacks resolve cleanly through the transparent membrane; the Ledger accumulates.


### 02 — bloated-bureaucracy

`U = 1000`, `R = 0.5`, `P ≈ 5`. The algebra `U²/R = 2,000,000` overwhelms the actual output. 
The tribunal identifies the *Necessary Betrayer* / *Logoic Plane-Lock* from Q3 and Q4: the framework is compounding its own structural complexity over its output.
Fires on every tick.


### 03 — nested-civilization

Exercises the forward arrow of the two-arrow crossing (`L4-RecursiveLimits`, Q5): the parent's committed Ledger `P_N` is inherited as the child's grounding resistance `R_{N+1}`. 
Parent P = 1000, so child R = 1000. The child runs with a `grounding-bottleneck` topology and is throttled to one callback per tick.


### 04 — frequency-sweep

Q8's tangent-impedance identity `tan(θ) = ωL/R` exercised at three frequencies. The frame has `L = 1`, `C = 0.0001`, so `ω₀ = 100`. Sweep:
- `ω = 1` (well below): θ ≈ −π/2, wall
- `ω = 100` (at ω₀): θ ≈ 0, gate (resonance)
- `ω = 10000` (well above): θ ≈ +π/2, wall

Same θ, same edge, three regimes. The wall and the gate are the same object.


### 05 — panic-trap

A fatal shunt from the L6 taxonomy: C in parallel with a series R-L branch. Under high-frequency shocks the capacitor shorts.
The tribunal refuses to execute registered callbacks and emits the topology's specific failure mode. 
In this stuck state, the buffer depth stays at the number of registered but unexecuted callbacks.


## Cross-substrate agreement

The pipeline's final check is: for every scenario, does the Haskell substrate emit the same *set* of epistemic tier tags as the Common Lisp substrate? 
This is a real integrity check, not a stylistic one.
If Haskell classifies a boundary as `RESONANCE` and Lisp classifies it as `INTERFACE:TangentCrossing`, that is a divergence worth investigating.
In this distribution, all five scenarios pass this check.

The two substrates are independent implementations.
Their agreement on the emitted tier set is what makes the operator-level identifications the corpus asserts *checkable*, not merely stated.
Convergence here is a small instance of the same phenomenon `L1-ConvergentDiscovery` accounts for at larger scales.


## What is deliberately not here

- No physics simulation. The Q-factors used are the frame's own `(1/R)√(L/C)` — a purely algebraic quantity. No attempt is made to derive specific hadronic or nuclear Q-factors, per the closing turn of the numerical audit: those belong to physics, not to the meta-of-physics substrate.
- No JSON/YAML/XML machinery. S-expressions are used because they are native to one substrate and trivially parseable in the other.
- No graphical rendering. The output is text, tagged. The corpus operates in prose; the substrate emits prose.
- No claim of derivation. Every emitted value carries its warrant. The Q1 charge derivation is marked `[SKETCH]`, per the corpus's own walkback that the Walsh basis fits any four numbers.

## Extending

To add a scenario: write a new `.sexp` file under `inputs/` and rerun the pipeline. Nothing else needs to change.

To add a new operator: add it to both substrates. The pipeline's cross-substrate agreement check will catch any divergence between the two implementations, which is the whole point of having two.

To add a new epistemic tier: add it to the emitter in each substrate. Choose names that survive the About-Claims discipline: does this tier state the frame's warrant honestly?

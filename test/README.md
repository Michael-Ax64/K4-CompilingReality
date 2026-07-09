# `/test/` — Mechanized Verification of the Algebraic Syntax & Route Laws

This directory contains the mechanized decision procedures and their executed trace reports. It fulfills the decidability claims of **Proof Q (The Algebraic Syntax)** and the **Route Law**, proving that the framework's epistemology is not a subjective mapping heuristic, but an auto-classifying arithmetic syntax that can be mechanically checked and will crash the compiler when fed topological impossibilities.


## Inventory

### The Test Scripts

*   **`ac_checker.py`** *(Orientation-Grammar Checker)*: 
    Implements the decision procedure for the Numerator Law (Law 1) and Synthesis Law (Law 2). It parses the operator structure of the 12 DC and 49 AC equations to verify that Reactive poles never appear in oriented dividend positions, and that Reactive homes are defined only via division/ratio. It also discovers and verifies the **Addition Homogeneity** (Composition) Law.
    
*   **`dual_route_trace.py`** *(Route Law Tracer)*: 
    Tests the linear/nonlinear pairing (R1-R4). It classifies every equation by route type (linear / square / root / shadow) to verify that squaring (collapse) always lands on Asserting homes, and rooting (reopening) always lands on Yielding homes.

### The Executed Reports

*   **`AC-Extension-Survival-Report.md`**: The executed trace report for `ac_checker.py`. Documents the survival of the DC laws in the AC extension, the discovery of the $\omega$-Law, and the mechanical catching of 19 candidate errata in the corpus equation set.

*   **`DualRoute-Trace-Addendum.md`**: The executed trace report for `dual_route_trace.py`. Documents the exceptionless survival of the Route Law across the DC and AC identity-class equations, promoting the 2x2 table to a load-bearing operator signature.



## Dependencies

These scripts require Python 3 and the `sympy` library for symbolic mathematics and AST traversal.

```bash
pip install sympy
```


## Usage

To run the Orientation-Grammar Checker (DC Control + AC Survival Trace):
```bash
python3 ac_checker.py
```

To run the Route Law Tracer (DC Control + AC Survival Trace):
```bash
python3 dual_route_trace.py
```


## What These Tests Prove

1.  **The Math Auto-Classifies:** The framework does not impose psychological or physical metaphors onto an electrical equation set. The arithmetic operators (numerator vs. denominator, squaring vs. rooting) hard-code the rules of interiority, boundary, and thermodynamic friction.

2.  **Decidability:** The decidability claim of Proof Q is discharged. The grammar is decidable over the pole basis after canonicalization. 

3.  **Error Catching:** The checker acts as a compiler. When fed topologically impossible forms (such as the erroneous `ω = 1` reduction in the core five), it throws, successfully identifying 19 candidate errata in the corpus's AC equation set.

4.  **The $\omega$-Law:** The tests mechanically confirm that $\omega$ (the centroid/fifth variable) is dimensionally excluded from the pole basis and obeys a sharper, hybrid law of its own.


## Contributing

If you find an equation in the corpus that violates these laws *after* canonicalization, or if you find a bug in the AST walker, this is the exact falsification condition invited by the framework. Open an issue, name it plainly, and provide the trace.

---

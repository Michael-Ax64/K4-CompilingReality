#!/usr/bin/env python3
"""
dc_inquiry_bridge.py
The Semantic Bridge (Executable Epistemology)

STATUS: COMPILED AND BRIDGED
This script bridges the mechanical AST walkers of the test suite
(`tribunal.ac_checker.py` and `tribunal.dual_route.py`) to the subjective
register. It translates raw boolean syntax flags into phenomenological reality.
"""

import os
import sys
import importlib.util
import sympy as sp


def _load_sibling(alias, *candidate_files):
    """Import a sibling module that may carry a dotted codex filename
    (e.g. 'tribunal.ac_checker.py'), which is not a valid flat import name.
    Loads the first existing candidate by path; caches under `alias` so shared
    symbols (e.g. the current symbol) are identical across importers."""
    if alias in sys.modules:
        return sys.modules[alias]
    here = os.path.dirname(os.path.abspath(__file__))
    for fname in candidate_files:
        path = os.path.join(here, fname)
        if os.path.exists(path):
            spec = importlib.util.spec_from_file_location(alias, path)
            mod = importlib.util.module_from_spec(spec)
            sys.modules[alias] = mod
            spec.loader.exec_module(mod)
            return mod
    raise ImportError(f"Could not locate any of {candidate_files} beside {__file__}")


_ac = _load_sibling("tribunal_ac_checker", "tribunal.ac_checker.py", "ac_checker.py")
_dr = _load_sibling("tribunal_dual_route", "tribunal.dual_route.py", "dual_route_trace.py")
occurrences = _ac.occurrences
route_type = _dr.route_type

# 1. THE TOPOLOGICAL DICTIONARY
# Maps sympy symbols to their K4 names for readability in the output.
POLE_NAMES = {
    'P': 'Drive (P)',
    'U': 'Structure (U)',
    'I': 'Flow (I)',
    'R': 'Ground (R)'
}

# 2. THE TRANSLATION MATRIX
def translate_ast_flags(sym, invd, numctx, r_type, wraps):
    """
    Maps the boolean flags of the AST walker and the route type 
    directly into the phenomenological inquiries.
    """
    reports = []
    sym_name = POLE_NAMES.get(str(sym), str(sym))

    # --- THE STAMPER AND THE DIE (Numerator/Denominator) ---
    if numctx and not invd:
        reports.append(
            f"  -> THE STAMPER (Dividend): As [{sym_name}], you are the drive being allocated. "
            f"The active substance forced through the constraint."
        )
    elif invd:
        reports.append(
            f"  -> THE DIE (Divisor): As [{sym_name}], you are the constraint shaping the output. "
            f"You do not push; you decide the shape the push takes."
        )

    # --- THE THERMODYNAMIC OPERATORS (Squares and Roots) ---
    # route_type is the authoritative classifier. Note: SymPy models sqrt(x) as
    # Pow(x, 1/2), so occurrences() never emits a 'sqrt' wrapper — 'root' is the
    # live signal. 'Abs' can still appear as a genuine magnitude wrapper.
    is_squared = r_type == 'square' or 'Abs' in wraps
    is_rooted = r_type == 'root'

    if is_squared:
        reports.append(
            f"  -> THE LANDAUER TAX: As [{sym_name}], you are burning directionality. "
            f"You are paying the thermodynamic cost to commit to the Read-Only Ledger."
        )
    if is_rooted:
        reports.append(
            f"  -> THE HOLOGRAPHIC PROJECTION: As [{sym_name}], you are being un-collapsed. "
            f"The system is reopening a committed scalar back into a living relational vector."
        )

    return reports

# 3. THE INTEGRATION ENGINE
def evaluate_trapped_face(face_name, equations):
    """
    Takes the 'Trapped Face' equations identified by the Prolog solver,
    runs them through the AST, and outputs the exact existential/structural position.
    """
    print(f"\n======================================================")
    print(f"THE SEMANTIC BRIDGE: EVALUATING [ {face_name.upper()} ]")
    print(f"======================================================")

    for eq_str in equations:
        print(f"\n[ ALGEBRAIC SYNTAX: {eq_str} ]")
        print("-" * 54)
        
        # Parse the equation into RHS expression using SymPy.
        # CRITICAL: bind "I" to a plain Symbol. By default SymPy reads a bare "I"
        # as the imaginary unit, which silently corrupts any current-bearing face
        # ("I**2*R" -> -R, "P/I" -> -I*P), inverting the route classification.
        # ac_checker sidesteps this by building from Icur = Symbol('I'); we match it.
        try:
            expr = sp.sympify(eq_str, locals={"I": sp.Symbol("I")})
        except Exception as e:
            print(f"  [ERROR] Could not parse AST for {eq_str}: {e}")
            continue

        # 1. Fetch the overall Route Type (Linear, Square, Root, Shadow)
        r_type, _ = route_type(expr)
        
        # 2. Fetch the symbol occurrences and their mechanical flags
        occs = occurrences(expr)

        for sym, invd, numctx, wraps in occs:
            if not sym.is_Symbol:
                continue
            
            # Run the Translation Matrix
            phenomenology = translate_ast_flags(sym, invd, numctx, r_type, wraps)
            
            for report in phenomenology:
                print(report)

if __name__ == "__main__":
    # EXAMPLE EXECUTION: The I-Absent Face (The Betrayer Face)
    # These are the equations passed from the Prolog solver when 'I' is starved.
    
    face_name = "The Betrayer Face (I-Absent)"
    trapped_equations = [
        "U**2 / R",       # P = U^2 / R (Leverage)
        "U**2 / P",       # R = U^2 / P (Bloat)
        "sqrt(P * R)"     # U = sqrt(P * R) (Capacity)
    ]
    
    evaluate_trapped_face(face_name, trapped_equations)


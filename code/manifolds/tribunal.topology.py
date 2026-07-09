#!/usr/bin/env python3
"""
dc_inquiry_bridge.py
The Semantic Bridge (Executable Epistemology)

STATUS: COMPILED AND BRIDGED
This script bridges the mechanical AST walkers of the test suite 
(`ac_checker.py` and `dual_route_trace.py`) to the subjective register.
It translates raw boolean syntax flags into phenomenological reality.
"""

import sympy as sp
from ac_checker import occurrences
from dual_route_trace import route_type

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
    # We check both the equation's overall route_type and the specific wrapper/exponent.
    is_squared = r_type == 'square' or 'Abs' in wraps
    is_rooted = r_type == 'root' or 'sqrt' in wraps

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
        
        # Parse the equation into RHS expression using SymPy
        # (Assuming equations are passed as standard strings like "U**2 / R")
        try:
            expr = sp.sympify(eq_str)
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


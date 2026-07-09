#!/usr/bin/env python3
"""
tribunal.inquiry.py
The Full System Orchestrator (K3 -> Topology -> AST Bridge)

STATUS: FULLY INTEGRATED
This script translates human deviation into a baseline coordinate, 
calls the strict Prolog topology engine, extracts the active equations 
from the output, and passes them to the Semantic Bridge (AST Walker) 
to generate the inquiry.
"""

import argparse
import subprocess
import re
import sys
import random
import os
import importlib.util


def _load_sibling(alias, *candidate_files):
    """Import a sibling module that may carry a dotted codex filename
    (e.g. 'tribunal.dc_inquiry.py'), which is not a valid flat import name."""
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


# Import the AST Semantic Bridge we built in the previous step
try:
    _bridge = _load_sibling("tribunal_dc_inquiry",
                            "tribunal.dc_inquiry.py", "dc_inquiry_bridge.py")
    evaluate_trapped_face = _bridge.evaluate_trapped_face
except ImportError:
    print("[SYSTEM FAULT] Missing tribunal.dc_inquiry.py. Ensure the Semantic Bridge is accessible.")
    sys.exit(1)

class K4Orchestrator:
    def __init__(self):
        # The biological/structural baseline of the system
        # (Defaulting to a balanced 1.0, 1.0, 1.0, 1.0 for this instance)
        self.baseline = (1.0, 1.0, 1.0, 1.0)

    def parse_human_complaint(self, text):
        """
        Simulated NLP. Extracts dimensionless deviations.
        P and I remain '_' (unbound) for Prolog to extrapolate via CLP(R).
        """
        text = text.lower()
        print(f"\n[ORCHESTRATOR] Receiving Context: '{text}'")
        
        in_p, in_i, in_u, in_r = "_", "_", "_", "_"

        if "random" in text:
            # Grab two randoms (0..1) to synthesize the Asymmetric Baseline
            b_u = random.uniform(0.1, 1.0)
            b_r = random.uniform(0.1, 1.0)
            b_i = b_u / b_r
            b_p = b_u * b_i
            
            self.baseline = (b_p, b_i, b_u, b_r)
            print(f"[ORCHESTRATOR] Synthesized Asymmetric Baseline:")
            print(f"               P={b_p:.3f}, I={b_i:.3f}, U={b_u:.3f}, R={b_r:.3f}")
            
            # Generate a random current state by drifting U and R
            in_u = b_u * random.uniform(0.1, 1.0)
            in_r = b_r * random.uniform(0.1, 1.0)
            print(f"[ORCHESTRATOR] Current Telemetry: U={in_u:.3f}, R={in_r:.3f}")
            
        
        elif "bureaucracy" in text or "rules" in text or "stuck" in text:
            in_u = 4.0  # High Structure
            in_r = 0.5  # Low Grounding (The actual paradox of bureaucracy)
            print(f"[ORCHESTRATOR] Extracted Drift: U={in_u}x, R={in_r}x baseline.")
            
        elif "grind" in text or "sweat" in text or "force" in text:
            in_p = 10.0 # High Drive
            in_u = 0.5  # Low Structure
            print(f"[ORCHESTRATOR] Extracted Drift: P={in_p}x, U={in_u}x baseline.")
            
        elif "crystal" in text or "balanced" in text:
            in_p, in_i, in_u, in_r = 1.0, 1.0, 1.0, 1.0
            print(f"[ORCHESTRATOR] Extracted Drift: System completely aligned with baseline.")

        return self.baseline, (in_p, in_i, in_u, in_r)

    def execute_topology(self, baseline, current):
        """Calls the strict DC Prolog engine and captures stdout."""
        bp, bi, bu, br = baseline
        cp, ci, cu, cr = current
        
        query = f"cli_run({bp},{bi},{bu},{br}, {cp},{ci},{cu},{cr})."
        
        try:
            print("[ORCHESTRATOR] Passing constraints to tribunal.manifold.pl...\n")
            result = subprocess.run(
                ['swipl', '-q', '-g', query, '-t', 'halt', 'tribunal.manifold.pl'],
                capture_output=True, text=True, check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"[SYSTEM FAULT] Prolog compilation failed: {e.stderr}")
            sys.exit(1)

    def bridge_to_ast(self, prolog_output):
        """
        Parses the Prolog output for the Trapped Face and its active equations,
        cleans them for SymPy, and feeds them to the AST Semantic Bridge.
        """
        # 1. Print the Thermodynamic Ledger (Prolog Output), minus the machine block.
        display = re.sub(r"\n\[MACHINE\].*?\[/MACHINE\]\n?", "",
                         prolog_output, flags=re.DOTALL)
        print(display)

        # 2. Check for Crystal Limit (No equations to parse)
        if "0-DoF CRYSTAL LIMIT DETECTED" in prolog_output:
            print("======================================================")
            print("THE SEMANTIC BRIDGE: [ CRYSTAL LIMIT ]")
            print("======================================================")
            print("  -> The space is exhausted. No topological shear detected.")
            print("  -> No Abstract Syntax Trees to walk. The engine rests.")
            print("======================================================\n")
            return

        # 3. Parse the deterministic [MACHINE] handoff block emitted by the
        #    Prolog engine (FACE: <name> / EQ: <lhs = rhs>). This is stable
        #    regardless of nested parens in the human-readable voices.
        face_match = re.search(r"^FACE:\s*(.+)$", prolog_output, re.M)
        if not face_match:
            print("[SYSTEM FAULT] Could not identify Trapped Face from topology output.")
            return

        face_name = face_match.group(1).strip()

        # 4. Extract the RHS of each equation ("lhs = rhs" -> "rhs"),
        #    normalising ^ to ** for SymPy.
        sympy_eqs = []
        for line in re.findall(r"^EQ:\s*(.+)$", prolog_output, re.M):
            rhs = line.split('=', 1)[1] if '=' in line else line
            sympy_eqs.append(rhs.strip().replace('^', '**'))

        if not sympy_eqs:
            print("[SYSTEM FAULT] Could not extract equations for AST parser.")
            return

        # 5. Hand off to the Semantic Bridge
        evaluate_trapped_face(face_name, sympy_eqs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=str,
                        default="random",
                        help="Human situation to diagnose.")
    args = parser.parse_args()

    # Get setup
    orchestrator = K4Orchestrator()
    
    # Parse Input
    baseline, current = orchestrator.parse_human_complaint(args.prompt)
    
    # Compute Topology
    prolog_output = orchestrator.execute_topology(baseline, current)
    
    # Bridge to Semantic Epistemology
    orchestrator.bridge_to_ast(prolog_output)



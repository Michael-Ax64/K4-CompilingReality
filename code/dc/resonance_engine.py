"""
resonance_engine.py
The Executable Closure of the Algebra of Four-Fold Distinction.
Forces the K4 volume into a measurable, actionable diagnostic.
"""

import math
from typing import Dict, List, Tuple

class K4System:
    """
    Represents a bounded system (a person, a project, an institution) 
    navigating its state-space.
    """
    def __init__(self, name: str, poles: Dict[str, float], omega: float):
        self.name = name
        # P (Power/Fire), I (Current/Water), U (Voltage/Air), R (Resistance/Earth)
        self.P = poles.get('P', 0.0)
        self.I = poles.get('I', 0.0)
        self.U = poles.get('U', 0.0)
        self.R = poles.get('R', 0.0)
        
        # omega: The angular frequency (the rate of cycling/development)
        self.omega = omega 
        
        # Reactance components (Inductive Memory vs Capacitive Anticipation)
        self.X_L = 0.0  # Inductive (lags)
        self.X_C = 0.0  # Capacitive (leads)

    def calculate_impedance(self, L: float, C: float) -> complex:
        """
        Computes the complex impedance Z = R + j(X_L - X_C).
        L = Inductance (historical momentum/inertia)
        C = Capacitance (structural anticipation/anxiety)
        """
        self.X_L = self.omega * L
        self.X_C = 1.0 / (self.omega * C) if self.omega * C != 0 else float('inf')
        
        R_eff = self.R
        X_net = self.X_L - self.X_C
        
        # Z is the complex impedance
        Z = complex(R_eff, X_net)
        return Z

    def phase_angle(self, Z: complex) -> float:
        """Returns the phase gap (theta) in radians."""
        return math.atan2(Z.imag, Z.real)

    def power_factor(self, theta: float) -> float:
        """
        The ratio of Real Power to Apparent Power.
        1.0 = perfect resonance (all capacity converted to actualization).
        0.0 = pure reactance (all capacity circulating as anxiety/momentum).
        """
        return math.cos(theta)

    def diagnose_trajectory(self) -> str:
        """Checks if the system is in trajectory contact or loss."""
        # Simplified heuristic: Is the Braid being carried?
        # If P and U are high but I is low, the system is exteriorizing without flow (Trajectory Loss).
        if self.U > 0 and self.P > 0 and self.I == 0:
            return "TRAJECTORY LOSS: High structure/power, zero relational current. The AbsentVar is dropped."
        return "TRAJECTORY CONTACT: Mutual determination holds."


def find_resonance(system_A: K4System, system_B: K4System, L_A: float, C_A: float, L_B: float, C_B: float) -> Dict:
    """
    The Core Engine: Computes the coupling between two systems.
    Resonance occurs when the net reactance of the coupled system approaches zero.
    """
    Z_A = system_A.calculate_impedance(L_A, C_A)
    Z_B = system_B.calculate_impedance(L_B, C_B)
    
    theta_A = system_A.phase_angle(Z_A)
    theta_B = system_B.phase_angle(Z_B)
    
    # Coupling logic: Do their reactances cancel?
    # System A is inductive (X_L > X_C, theta > 0)
    # System B is capacitive (X_C > X_L, theta < 0)
    net_reactance = (Z_A.imag + Z_B.imag)
    net_resistance = (Z_A.real + Z_B.real)
    
    coupled_Z = complex(net_resistance, net_reactance)
    coupled_theta = math.atan2(coupled_Z.imag, coupled_Z.real)
    coupled_PF = math.cos(coupled_theta)
    
    return {
        "System_A_Phase": f"{math.degrees(theta_A):.2f}° ({'Inductive/Lagging' if theta_A > 0 else 'Capacitive/Leading'})",
        "System_B_Phase": f"{math.degrees(theta_B):.2f}° ({'Inductive/Lagging' if theta_B > 0 else 'Capacitive/Leading'})",
        "Coupled_Phase_Gap": f"{math.degrees(coupled_theta):.2f}°",
        "Coupled_Power_Factor": f"{coupled_PF:.4f}",
        "Resonance_Status": "RESONANT (Reactances Cancel)" if abs(coupled_theta) < 0.1 else "OUT_OF_PHASE (Reactance Circulating)"
    }

# ===================================================================
# RUNTIME EXECUTION: The Garbage Collector runs on the abstraction.
# ===================================================================
if __name__ == "__main__":
    print("--- INITIALIZING RESONANCE ENGINE ---\n")

    # System A: The Veteran Architect. Heavy history, slow to accelerate. (Inductive)
    architect = K4System("The Architect", {'P': 80, 'I': 40, 'U': 90, 'R': 50}, omega=2.0)
    
    # System B: The Disruptive Founder. High anticipation, low grounding. (Capacitive)
    founder = K4System("The Founder", {'P': 90, 'I': 60, 'U': 80, 'R': 20}, omega=2.0)

    # Assigning Reactance Profiles
    # Architect has high L (inductance/history), low C (capacitance/anticipation)
    L_arch, C_arch = 10.0, 0.05  
    # Founder has low L, high C
    L_found, C_found = 2.0, 0.25  

    print(f"Diagnostic for {architect.name}: {architect.diagnose_trajectory()}")
    print(f"Diagnostic for {founder.name}: {founder.diagnose_trajectory()}\n")

    # Compute the coupling
    coupling = find_resonance(architect, founder, L_arch, C_arch, L_found, C_found)
    
    print("--- COUPLING DIAGNOSTIC ---")
    for k, v in coupling.items():
        print(f"{k}: {v}")
        
    print("\n--- INSTRUMENT SEALED ---")
    print("The map is now a compass. The volume is now a metric.")

    

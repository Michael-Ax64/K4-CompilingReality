#!/usr/bin/env python3
import sys

def generate_k4_projections(selection="all"):
    # 1. The Data Dictionary (The 12 Transition Verbs & 4 Poles)
    data = {
        'ARI': {'l1': 'P=U²/R == ARI',    'l2': 'Cardinal-Fire-cw @MB'},
        'TAU': {'l1': 'P=I²R == TAU',     'l2': 'Fixed-Fire-cw @FB'},
        'GEM': {'l1': 'P=U·I == GEM',     'l2': 'Mutable-Fire-cw @CB'},
        'CAN': {'l1': 'I=√(P/R) == CAN',  'l2': 'Cardinal-Water-ccw @CB'},
        'LEO': {'l1': 'I=P/U == LEO',     'l2': 'Fixed-Water-ccw @FB'},
        'VIR': {'l1': 'I=U/R == VIR',     'l2': 'Mutable-Water-ccw @MB'},
        'LIB': {'l1': 'U=P/I == LIB',     'l2': 'Cardinal-Air-cw @MB'},
        'SCO': {'l1': 'U=I·R == SCO',     'l2': 'Fixed-Air-cw @FB'},
        'SAG': {'l1': 'U=√(P·R) == SAG',  'l2': 'Mutable-Air-cw @CB'},
        'CAP': {'l1': 'R=U/I == CAP',     'l2': 'Cardinal-Earth-ccw @CB'},
        'AQU': {'l1': 'R=U²/P == AQU',    'l2': 'Fixed-Earth-ccw @FB'},
        'PIS': {'l1': 'R=P/I² == PIS',    'l2': 'Mutable-Earth-ccw @MB'},
        # Cartesian Pole Labels
        'P':   {'l1': 'POLE P [Fire]',    'l2': 'Active-Asserting [++]'},
        'I':   {'l1': 'POLE I [Water]',   'l2': 'Reactive-Yielding [--]'},
        'U':   {'l1': 'POLE U [Air]',     'l2': 'Active-Yielding [+-]'},
        'R':   {'l1': 'POLE R [Earth]',   'l2': 'Reactive-Asserting [-+]'}
    }

    # 2. The Face Mappings
    maps = {
        '0': { # ASSEMBLY 0: Cartesian (8-cube with explicit poles and smeared diagonals)
            'Y+TL': 'I',   'Y+TR': 'LIB', 'Y+BL': 'PIS', 'Y+BR': 'P',
            'Z+TL': 'CAN', 'Z+TR': 'P',   'Z+BL': 'R',   'Z+BR': 'SAG',
            'Y-TL': 'R',   'Y-TR': 'ARI', 'Y-BL': 'VIR', 'Y-BR': 'U',
            'X-TL': 'I',   'X-TR': 'TAU', 'X-BL': 'SCO', 'X-BR': 'R',
            'Z-TL': 'GEM', 'Z-TR': 'I',   'Z-BL': 'U',   'Z-BR': 'CAP',
            'X+TL': 'P',   'X+TR': 'LEO', 'X+BL': 'AQU', 'X+BR': 'U'
        },
        '1': { # ASSEMBLY 1: Cardinal Pinned (I-U Front Horiz, P-R Rear Vert)
            'Y+TL': 'PIS', 'Y+TR': 'AQU', 'Y+BL': 'LIB', 'Y+BR': 'LEO',
            'Z+TL': 'CAP', 'Z+TR': 'CAP', 'Z+BL': 'GEM', 'Z+BR': 'GEM',
            'Y-TL': 'SCO', 'Y-TR': 'VIR', 'Y-BL': 'TAU', 'Y-BR': 'ARI',
            'X-TL': 'PIS', 'X-TR': 'LIB', 'X-BL': 'SCO', 'X-BR': 'TAU',
            'Z-TL': 'CAN', 'Z-TR': 'SAG', 'Z-BL': 'CAN', 'Z-BR': 'SAG',
            'X+TL': 'AQU', 'X+TR': 'LEO', 'X+BL': 'VIR', 'X+BR': 'ARI'
        },
        '2': { # ASSEMBLY 2: Fixed Pinned (P-U Front Horiz, I-R Rear Vert)
            'Y+TL': 'PIS', 'Y+TR': 'CAP', 'Y+BL': 'LIB', 'Y+BR': 'GEM',
            'Z+TL': 'LEO', 'Z+TR': 'LEO', 'Z+BL': 'AQU', 'Z+BR': 'AQU',
            'Y-TL': 'SAG', 'Y-TR': 'VIR', 'Y-BL': 'CAN', 'Y-BR': 'ARI',
            'X-TL': 'PIS', 'X-TR': 'LIB', 'X-BL': 'SAG', 'X-BR': 'CAN',
            'Z-TL': 'TAU', 'Z-TR': 'SCO', 'Z-BL': 'TAU', 'Z-BR': 'SCO',
            'X+TL': 'CAP', 'X+TR': 'GEM', 'X+BL': 'VIR', 'X+BR': 'ARI'
        },
        '3': { # ASSEMBLY 3: Mutable Pinned (P-I Front Horiz, U-R Rear Vert)
            'Y+TL': 'AQU', 'Y+TR': 'GEM', 'Y+BL': 'LEO', 'Y+BR': 'CAP',
            'Z+TL': 'LIB', 'Z+TR': 'LIB', 'Z+BL': 'PIS', 'Z+BR': 'PIS',
            'Y-TL': 'SAG', 'Y-TR': 'SCO', 'Y-BL': 'CAN', 'Y-BR': 'TAU',
            'X-TL': 'AQU', 'X-TR': 'LEO', 'X-BL': 'SAG', 'X-BR': 'CAN',
            'Z-TL': 'ARI', 'Z-TR': 'VIR', 'Z-BL': 'ARI', 'Z-BR': 'VIR',
            'X+TL': 'GEM', 'X+TR': 'CAP', 'X+BL': 'SCO', 'X+BR': 'TAU'
        }
    }

    # 3. Layout Definitions
    strip1 = [['Y+TL', 'Y+TR'], ['Y+BL', 'Y+BR'], 
              ['Z+TL', 'Z+TR'], ['Z+BL', 'Z+BR'], 
              ['Y-TL', 'Y-TR'], ['Y-BL', 'Y-BR']]
              
    strip2 = [['X-TL', 'X-TR', 'Z-TL', 'Z-TR', 'X+TL', 'X+TR'], 
              ['X-BL', 'X-BR', 'Z-BL', 'Z-BR', 'X+BL', 'X+BR']]

    # 4. Rendering Engine
    def render_grid(rows, title, face_map):
        out = [title, "=" * len(title)]
        for row in rows:
            lines = ["", "", ""]
            for loc in row:
                d = data[face_map[loc]]
                lines[0] += f"[{loc:^26}] "
                lines[1] += f" {d['l1']:^26} "
                lines[2] += f" {d['l2']:^26} "
            out.extend(lines)
            out.append("-" * len(lines[0]))
        return "\n".join(out)

    titles = {
        '0': "ASSEMBLY 0: THE CARTESIAN MODEL (Manifest Poles & Implicit Duals)",
        '1': "ASSEMBLY 1: CARDINAL PINNED (I-U Front, P-R Rear)",
        '2': "ASSEMBLY 2: FIXED PINNED (P-U Front, I-R Rear)",
        '3': "ASSEMBLY 3: MUTABLE PINNED (P-I Front, U-R Rear)"
    }

    output = ""
    keys = ['0', '1', '2', '3'] if selection == "all" else [selection]
    
    for k in keys:
        if k not in maps: continue
        output += f"{titles[k]}\n" + "*" * len(titles[k]) + "\n\n"
        output += render_grid(strip1, "STRIP 1: 6x2 Vertical Unroll (Top, Front, Bottom)", maps[k]) + "\n\n"
        output += render_grid(strip2, "STRIP 2: 2x6 Horizontal Unroll (Left, Rear, Right)", maps[k]) + "\n\n\n"
    
    return output

if __name__ == "__main__":
    sel = sys.argv[1] if len(sys.argv) > 1 else "all"
    if sel not in ["0", "1", "2", "3", "all"]:
        print("Usage: python render_k4.py [0|1|2|3|all]")
    else:
        print(generate_k4_projections(sel))


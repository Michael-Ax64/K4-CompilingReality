"""Mechanical check for the L3-EdgeStateSpace master-update:
   coherent orientation, directed reading rule bijection, season identity,
   Direction Law, mirror conjugation, log-space rank."""
from itertools import product
import numpy as np

poles = 'PIUR'

# --- Step 1: the coherent orientation (face -> boundary circulation) ---
circ = {'P': ('I', 'R', 'U'),      # P-face {I,U,R}:  I->R->U->I
        'I': ('P', 'U', 'R'),      # I-face {P,U,R}:  P->U->R->P
        'U': ('P', 'R', 'I'),      # U-face {P,I,R}:  P->R->I->P
        'R': ('P', 'I', 'U')}      # R-face {P,I,U}:  P->I->U->P

def boundary(c):
    return {(c[i], c[(i + 1) % 3]) for i in range(3)}

sh = {}
for f in circ:
    for e in boundary(circ[f]):
        sh.setdefault(frozenset(e), []).append(e)
print("d2 = 0 (all six shared edges cancel):",
      all(len(v) == 2 and v[0] == v[1][::-1] for v in sh.values()))

# uniqueness up to global mirror: flip each face's circulation, count coherent assignments
count = 0
for flips in product([0, 1], repeat=4):
    cs = {f: (c if not k else c[::-1]) for (f, c), k in zip(circ.items(), flips)}
    sh2 = {}
    for f in cs:
        for e in boundary(cs[f]):
            sh2.setdefault(frozenset(e), []).append(e)
    count += all(len(v) == 2 and v[0] == v[1][::-1] for v in sh2.values())
print("coherent orientations:", count, "= 2^(4-3): six conditions, GF(2) rank 3, one handedness bit")

# --- Steps 2/3: the directed reading rule -> bijection ---
home_sign = {('P', 'I'): 'VIR', ('P', 'U'): 'SCO', ('P', 'R'): 'CAP',   # P-face  U = I.R
             ('I', 'P'): 'ARI', ('I', 'U'): 'SAG', ('I', 'R'): 'AQU',   # I-face  U^2 = P.R
             ('U', 'P'): 'TAU', ('U', 'I'): 'CAN', ('U', 'R'): 'PIS',   # U-face  P = I^2.R
             ('R', 'P'): 'GEM', ('R', 'I'): 'LEO', ('R', 'U'): 'LIB'}   # R-face  P = U.I
gate = {}
for a in poles:
    for b in poles:
        if a == b:
            continue
        f = next(f for f in circ if (a, b) in boundary(circ[f]))  # face this direction completes
        h = (set(circ[f]) - {a, b}).pop()                         # third vertex = Home
        gate[(a, b)] = home_sign[(f, h)]
print("bijection over 12 directed edges:", len(gate) == 12 and len(set(gate.values())) == 12)
for (a, b), g in sorted(gate.items()):
    print("   ", a + "->" + b, ":", g)

# --- Step 4/5: crown + season identity ---
inv = {g: e for e, g in gate.items()}
season = {'Spring': ['ARI', 'TAU', 'GEM'], 'Summer': ['CAN', 'LEO', 'VIR'],
          'Autumn': ['LIB', 'SCO', 'SAG'], 'Winter': ['CAP', 'AQU', 'PIS']}
for s, gs in season.items():
    follow = dict(inv[g] for g in gs)
    walk = [inv[gs[0]][0]]
    for _ in range(3):
        walk.append(follow[walk[-1]])
    print(s, "circuit:", " -> ".join(walk), "| closes:", walk[3] == walk[0])
print("immovable three chain (U-face walk):",
      " -> ".join(a + "->" + b for a, b in [inv[g] for g in ['CAN', 'TAU', 'PIS']]))

# --- Step 6: the Direction Law ---
charge = {'P': (1, 1), 'U': (1, -1), 'I': (-1, -1), 'R': (-1, 1)}   # (AR, AY), section XI
mode = {'ARI': 'Cardinal', 'TAU': 'Fixed', 'GEM': 'Mutable', 'CAN': 'Cardinal', 'LEO': 'Fixed',
        'VIR': 'Mutable', 'LIB': 'Cardinal', 'SCO': 'Fixed', 'SAG': 'Mutable',
        'CAP': 'Cardinal', 'AQU': 'Fixed', 'PIS': 'Mutable'}
law = {'Cardinal': lambda a, b: charge[a][0] == 1 and charge[b][0] == -1,   # Active -> Reactive
       'Fixed':    lambda a, b: charge[a][0] == charge[b][0],               # same class, both ways
       'Mutable':  lambda a, b: charge[a][0] == -1 and charge[b][0] == 1}   # Reactive -> Active
print("direction law (Cardinal A->R, Fixed same-class, Mutable R->A):",
      all(law[mode[g]](*e) for e, g in gate.items()))

# --- the mirror: conjugate every arrow; Cardinal/Mutable laws exchange, Fixed survives ---
gateM = {(b, a): g for (a, b), g in gate.items()}
lawM = {'Cardinal': law['Mutable'], 'Mutable': law['Cardinal'], 'Fixed': law['Fixed']}
print("mirror + exchanged laws holds:", all(lawM[mode[g]](*e) for e, g in gateM.items()),
      "| mirror + unexchanged laws fails:", not all(law[mode[g]](*e) for e, g in gateM.items()))

# --- log space: the four face-relations span rank 2 (two generators) ---
rel = np.array([[1, -2, 0, 1], [1, 0, -2, -1], [1, -1, -1, 0], [0, 1, -1, -1]], float)  # section I-d rows
print("rank of the four face-relations:", int(np.linalg.matrix_rank(rel)))

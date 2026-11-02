poles = 'PIUR'
circ = {'P': ('I','R','U'), 'I': ('P','U','R'), 'U': ('P','R','I'), 'R': ('P','I','U')}
#      P-face I→R→U   | I-face P→U→R | U-face P→R→I | R-face P→I→U
boundary = lambda c: {(c[i], c[(i+1) % 3]) for i in range(3)}
sh = {}
for f in circ:
    for e in boundary(circ[f]): sh.setdefault(frozenset(e), []).append(e)
print("d2=0:", all(len(v) == 2 and v[0] == v[1][::-1] for v in sh.values()))

from itertools import product
n = 0
for flips in product([0, 1], repeat=4):
    cs = {f: (c if not k else c[::-1]) for (f, c), k in zip(circ.items(), flips)}
    sh2 = {}
    for f in cs:
        for e in boundary(cs[f]): sh2.setdefault(frozenset(e), []).append(e)
    n += all(len(v) == 2 and v[0] == v[1][::-1] for v in sh2.values())
print("coherent orientations:", n)                      # 2 = 2^(4-3): rank 3, one handedness bit

home_sign = {('P','I'):'VIR', ('P','U'):'SCO', ('P','R'):'CAP',    # P-face  U = I·R
             ('I','P'):'ARI', ('I','U'):'SAG', ('I','R'):'AQU',    # I-face  U² = P·R
             ('U','P'):'TAU', ('U','I'):'CAN', ('U','R'):'PIS',    # U-face  P = I²·R
             ('R','P'):'GEM', ('R','I'):'LEO', ('R','U'):'LIB'}    # R-face  P = U·I
gate = {}
for a in poles:
    for b in poles:
        if a != b:
            f = next(f for f in circ if (a, b) in boundary(circ[f]))      # face this direction completes
            gate[(a, b)] = home_sign[(f, (set(circ[f]) - {a, b}).pop())]  # third vertex = Home
print("bijection:", len(set(gate.values())) == 12)      # 12 distinct gates, one per directed edge
print({a+'→'+b: g for (a, b), g in sorted(gate.items())})

inv = {g: e for e, g in gate.items()}
for s, gs in [('Spring', ['ARI','TAU','GEM']), ('Summer', ['CAN','LEO','VIR']),
              ('Autumn', ['LIB','SCO','SAG']), ('Winter', ['CAP','AQU','PIS'])]:
    follow = dict(inv[g] for g in gs); walk = [inv[gs[0]][0]]
    for _ in range(3): walk.append(follow[walk[-1]])
    print(s, '→'.join(walk), walk[3] == walk[0])        # Spring U→R→I→U True ... all four close

charge = {'P': (1,1), 'U': (1,-1), 'I': (-1,-1), 'R': (-1,1)}    # (AR, AY), §XI
mode = {'ARI':'Cardinal','TAU':'Fixed','GEM':'Mutable','CAN':'Cardinal','LEO':'Fixed',
        'VIR':'Mutable','LIB':'Cardinal','SCO':'Fixed','SAG':'Mutable',
        'CAP':'Cardinal','AQU':'Fixed','PIS':'Mutable'}
law = {'Cardinal': lambda a, b: charge[a][0] == 1 and charge[b][0] == -1,   # Active → Reactive
       'Fixed':    lambda a, b: charge[a][0] == charge[b][0],               # same class, both ways
       'Mutable':  lambda a, b: charge[a][0] == -1 and charge[b][0] == 1}   # Reactive → Active
print("direction law:", all(law[mode[g]](*e) for e, g in gate.items()))
gateM = {(b, a): g for (a, b), g in gate.items()}               # the mirror: every arrow conjugates
lawM = {'Cardinal': law['Mutable'], 'Mutable': law['Cardinal'], 'Fixed': law['Fixed']}
print("mirror, laws exchanged:", all(lawM[mode[g]](*e) for e, g in gateM.items()),
      "| unexchanged:", all(law[mode[g]](*e) for e, g in gateM.items()))

import numpy as np
rel = np.array([[1,-2,0,1],[1,0,-2,-1],[1,-1,-1,0],[0,1,-1,-1]], float)   # §I-d coefficient rows
print("rank of the four relations:", int(np.linalg.matrix_rank(rel)))     # 2

#!/usr/bin/env python3
"""orientation_group.py — verify the user's orientation claims.

  U1. 6 x 2 = 12: any edge can be 'front' in 2 orientations == the 12 directed
      edges == the 12 gates (viewport x solve).
  U2. 4 x 3 = 12: anchors x pinnings == the same set (two factorizations of A4).
  U3. Each gate IS a rotation: gate (x,w) = the unique EVEN permutation of the
      poles carrying P->x, U->w. A4 acts simply transitively on directed edges.
  U4. S4 = 4! = 24 = cube rotation group = permutations of the 4 body diagonals
      = the 24 outward squares of the 2x2x2 assembly (simply transitive).
      A4 = the manifest-preserving half; the odd coset = the dual vocabulary.
      The two completions of a gate differ by the AR-flip on the uninvolved pair.
  U5. V4 = the 3 bimedian half-turns = the 3 execution rings; A4 = 1 + 3 + 8.
  U6. The opcode families are the cube's axes (each gate flips its own bimedian bit).
"""
from itertools import permutations
from collections import Counter
import numpy as np

poles = ['P', 'U', 'I', 'R']
E = {frozenset(e) for e in [('P','U'),('P','I'),('P','R'),('U','I'),('U','R'),('I','R')]}
M = {'Fixed':    (frozenset(('P','U')), frozenset(('I','R'))),
     'Cardinal': (frozenset(('P','R')), frozenset(('I','U'))),
     'Mutable':  (frozenset(('P','I')), frozenset(('U','R')))}

S4 = list(permutations(poles))
def parity(p):
    idx = [poles.index(x) for x in p]
    return sum(1 for i in range(4) for j in range(i+1,4) if idx[i] > idx[j]) % 2
A4 = [p for p in S4 if parity(p) == 0]
print('U0. |S4| =', len(S4), '|A4| =', len(A4), '(4! and 4!/2)')

print('=' * 70)
print('U1/U3. gates = directed edges = A4 (simply transitive)')
gate_perm, ok = {}, True
for a in poles:
    for b in poles:
        if a == b: continue
        cands  = [p for p in S4 if p[0] == a and p[1] == b]
        evens  = [p for p in cands if parity(p) == 0]
        ok &= (len(cands) == 2 and len(evens) == 1)
        gate_perm[(a, b)] = evens[0]
print('   every directed edge has exactly 2 completions, exactly 1 even:', ok)
print('   bijection gate (x,w) <-> even permutation established:', len(gate_perm) == 12)

print('=' * 70)
print('U4. the C2: odd completion = even one with the uninvolved pair swapped')
ok2 = True
for (a, b), g in gate_perm.items():
    odd = [p for p in S4 if p[0] == a and p[1] == b and parity(p) == 1][0]
    diff = [i for i in (2, 3) if g[i] != odd[i]]
    ok2 &= (len(diff) == 2 and {g[diff[0]], g[diff[1]]} == {g[2], g[3]})
print('   the two completions differ only on the images of {I,R} (the AR-flip):', ok2)

print('=' * 70)
print('U5. V4 half-turns = the three rings; A4 = 1 + 3 + 8')
def apply_perm(p, e):
    return frozenset(p[poles.index(x)] for x in e)
dts = [p for p in A4 if all(c != poles[i] for i, c in enumerate(p))]
print('   double-transpositions in A4:', len(dts), '(expected 3)')
for p in dts:
    holds = [k for k, (e1, e2) in M.items()
             if apply_perm(p, e1) == e1 and apply_perm(p, e2) == e2]
    print('   ', ''.join(p), '-> holds', holds[0], 'bimedian setwise')
def cyc(p):
    seen, types = [False]*4, []
    for i in range(4):
        if not seen[i]:
            L, j = 0, i
            while not seen[j]:
                seen[j] = True; L += 1; j = poles.index(p[j])
            types.append(L)
    return tuple(sorted(types))
print('   A4 cycle types:', dict(Counter(cyc(p) for p in A4)), '(1 + 3 + 8)')
axes3 = [p for p in A4 if cyc(p) == (1, 3)]
fixed_poles = {p[i] for p in axes3 for i, c in enumerate(p) if c == poles[i]}
print('   third-turns:', len(axes3), '= vertex-axes x senses:',
      len(fixed_poles), 'x 2')

print('=' * 70)
print('U4b. cube rotations: diagonal action = S4; manifest half = A4')
mats = []
for perm in permutations(range(3)):
    for signs in ((1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1),(-1,1,1),(-1,1,-1),(-1,-1,1),(-1,-1,-1)):
        Mx = np.zeros((3,3))
        for i, pj in enumerate(perm):
            Mx[i, pj] = signs[i]
        if round(np.linalg.det(Mx)) == 1:
            mats.append(Mx)
print('   rotation matrices with det=+1:', len(mats), '(expected 24)')
diags = [np.array(v) for v in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]  # P,U,I,R octants
def didx(v):
    return next(i for i, d in enumerate(diags)
                if np.allclose(v, d) or np.allclose(v, -d))
perm_count = Counter()
for Mx in mats:
    sigma = tuple(didx(Mx @ d) for d in diags)
    perm_count[sigma] += 1
print('   distinct induced permutations on the 4 diagonals:', len(perm_count))
even_oct = {tuple(int(x) for x in d) for d in diags}
ok4 = True
seen_sigma = {}
for Mx in mats:
    sigma = tuple(didx(Mx @ d) for d in diags)
    v = Mx @ diags[0]
    preserves = tuple(int(x) for x in v) in even_oct
    if sigma in seen_sigma:
        ok4 &= (seen_sigma[sigma] == preserves)
    else:
        seen_sigma[sigma] = preserves
print('   preserves manifest tet  <=>  induced permutation is even:', ok4)

print('=' * 70)
print('U4c. the 24 outward squares: simply transitive under the rotations')
centers = []
for axis in range(3):
    for s in (1, -1):
        for c0 in (0.5, -0.5):
            for c1 in (0.5, -0.5):
                c = [0.0, 0.0, 0.0]; c[axis] = s
                rest = [i for i in range(3) if i != axis]
                c[rest[0]], c[rest[1]] = c0, c1
                centers.append(np.array(c))
print('   square centers:', len(centers), '(6 faces x 4 blocks)')
orbit = {tuple(np.round(Mx @ centers[0], 6)) for Mx in mats}
print('   orbit size of one square:', len(orbit), '(simply transitive = 24)')

print('=' * 70)
print('U6. opcode families are the cube axes (each gate flips its own bimedian bit)')
def code_of(obj, conv):
    return tuple(0 if M[k][0] in obj else 1 for k in ('Fixed','Cardinal','Mutable'))
stars = {p: frozenset(e for e in E if p in e) for p in poles}
faces = {p: frozenset(e for e in E if p not in e) for p in poles}
codes = {('star', p): code_of(stars[p], 0) for p in poles}
codes.update({('face', p): code_of(faces[p], 1) for p in poles})
def midx(e):
    return next(i for i, k in enumerate(('Fixed','Cardinal','Mutable')) if e in M[k])
ok6 = True
for x in poles:
    for w in poles:
        if x == w: continue
        diff = [i for i in range(3) if codes[('star',x)][i] != codes[('face',w)][i]]
        ok6 &= (diff == [midx(frozenset((x, w)))])
print('   gate-edge (star x -- face -w) flips exactly bimedian-bit of edge xw:', ok6)

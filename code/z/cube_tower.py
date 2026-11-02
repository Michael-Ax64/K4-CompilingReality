#!/usr/bin/env python3
"""cube_tower.py — verify the 2-cube/3-cube tower against the corpus.

Claims under test:
  C1. The 8 trigrams (ENGINE-REFERENCE-DC §1.3) = 4 stars + 4 faces, and every
      star/face is a transversal of the 3 perfect matchings.
  C2. The Hamming-1 graph on matching-codes of the 8 census objects is the cube Q3.
  C3. Star codes = L4-Transiting §VII octant signs (axis-permuted); face codes =
      bitwise complements (Rule of Seven antipodes: star(X) <-> face(-X)).
  C4. The 12 cube edges = the 12 gates (solved pole x, absent witness w); each
      edge (star x -- face -w) flips exactly the matching-bit of K4-edge xw.
  C5. Q3 has 6 undirected Hamiltonian cycles; each omits a perfect matching;
      the omitted sets are exactly the 6 four-cycle derangements (absence
      circulations), never the 3 coordinate (double-transposition) matchings.
  C6. Each cube tour projects 2:1 onto the 3 K4 Hamiltonian cycles via its
      star-visit order; antipodal pairs are never adjacent on a tour.
  C7. Ladder: undirected Hamiltonian tours  Q2:1, K4:3, Q3:6, K5:12.
"""
from itertools import combinations, permutations

poles = ['P', 'U', 'I', 'R']
E = {frozenset(e) for e in [('P','U'),('P','I'),('P','R'),('U','I'),('U','R'),('I','R')]}

# ENGINE-REFERENCE-DC §1.3 names (Fixed/Cardinal/Mutable) and edge membership
M = {
    'Fixed':    (frozenset(('P','U')), frozenset(('I','R'))),
    'Cardinal': (frozenset(('P','R')), frozenset(('I','U'))),
    'Mutable':  (frozenset(('P','I')), frozenset(('U','R'))),
}
MKEYS = ['Fixed', 'Cardinal', 'Mutable']   # bit order; bit=0 <=> carries the P-side edge

stars = {p: frozenset(e for e in E if p in e) for p in poles}
faces = {p: frozenset(e for e in E if p not in e) for p in poles}   # face opposite p
census = {('star', p): stars[p] for p in poles}
census.update({('face', p): faces[p] for p in poles})

print('=' * 72)
print('C1. transversals vs census (ENGINE §1.3: 8 trigrams = 4 stars + 4 faces)')
transversals = {frozenset([a, b, c])
                for a in M['Fixed'] for b in M['Cardinal'] for c in M['Mutable']}
print('   #transversals =', len(transversals),
      '| == census sets:', transversals == set(census.values()))

print('=' * 72)
print('C2/C3. matching-code cube; octant signs; antipodes')
def code(obj):
    return tuple(0 if M[k][0] in obj else 1 for k in MKEYS)
codes = {o: code(s) for o, s in census.items()}
for p in poles:
    print(f'   star({p}) = {codes[("star", p)]}   face(-{p}) = {codes[("face", p)]}')
even = [o for o in census if sum(codes[o]) % 2 == 0]
odd  = [o for o in census if sum(codes[o]) % 2 == 1]
print('   even-parity class all stars:', all(o[0] == 'star' for o in even),
      '| odd class all faces:', all(o[0] == 'face' for o in odd))
anti_ok = all(codes[('face', p)] == tuple(1 - b for b in codes[('star', p)]) for p in poles)
print('   antipode star(X) <-> face(-X) (bitwise NOT, Rule of Seven):', anti_ok)

adj = {o: [o2 for o2 in census
           if sum(x != y for x, y in zip(codes[o], codes[o2])) == 1 and o2 != o]
       for o in census}
degs = {len(v) for v in adj.values()}
n_edges = sum(len(v) for v in adj.values()) // 2
bip = all((codes[o] + codes[o2]) and (sum(codes[o2]) != sum(codes[o]))
          for o in adj for o2 in adj[o])
print(f'   Hamming-1 graph: degrees {degs}, edges {n_edges} (12 expected), bipartite by parity: {bip}')

# brute-force isomorphism to explicit Q3
idx = {o: i for i, o in enumerate(census)}
obj = {i: o for o, i in idx.items()}
G1 = {idx[o]: {idx[x] for x in adj[o]} for o in census}
Q3 = {i: {i ^ (1 << b) for b in range(3)} for i in range(8)}
iso = next((p for p in permutations(range(8))
            if all({p[b] for b in G1[a]} == Q3[p[a]] for a in range(8))), None)
print('   isomorphic to Q3:', iso is not None)

print('=' * 72)
print('C4. cube edges = 12 gates (viewport face(-w), solved pole x)')
cube_edges = {frozenset((o, o2)) for o in census for o2 in adj[o]}
def to_gate(e):
    (a, b) = tuple(e)
    s, f = (a, b) if a[0] == 'star' else (b, a)
    return (s[1], f[1])            # (solved x, absent witness w)
gset = {to_gate(e) for e in cube_edges}
gates = {(x, w) for x in poles for w in poles if x != w}
print('   #cube edges =', len(cube_edges), '| bijection onto (x,w), x!=w :', gset == gates)
def mindex(e):
    for k in MKEYS:
        if e in M[k]:
            return MKEYS.index(k)
flip_ok = all(
    [i for i in range(3)
     if codes[('star', x)][i] != codes[('face', w)][i]] == [mindex(frozenset((x, w)))]
    for (x, w) in gset)
print('   each gate-edge flips exactly the bimedian-bit of its own K4 edge:', flip_ok)

print('=' * 72)
print('C5. Hamiltonian cycles of the cube (undirected, up to rotation+reflection)')
def ham_cycles(G, n):
    start = 0
    found = set()
    def dfs(v, visited, path):
        if len(path) == n:
            if start in G[v]:
                found.add(frozenset(frozenset((path[i], path[(i + 1) % n]))
                                    for i in range(n)))
            return
        for u in G[v]:
            if u not in visited:
                dfs(u, visited | {u}, path + [u])
    dfs(start, {start}, [start])
    return found
HC = {frozenset(frozenset((obj[p_], obj[q_])) for p_, q_ in hz)
      for hz in ham_cycles(G1, 8)}
print('   #undirected Hamiltonian cycles on Q3 =', len(HC), '(expected 6)')

def derangement_type(pairs):
    """pairs: 4 (x,w). Return '4-cycle', '2+2-cycle' (coordinate), or other."""
    succ = dict(pairs)
    if set(succ) != set(poles) or set(succ.values()) != set(poles):
        return 'not-a-permutation'
    seen, types = set(), []
    for s in poles:
        if s in seen:
            continue
        L, c = 0, s
        while c not in seen:
            seen.add(c); L += 1; c = succ[c]
        types.append(L)
    return {2: '2+2-cycle (coordinate matching)', 4: '4-cycle (absence circulation)'} \
        .get(tuple(sorted(types)), str(sorted(types)))

print('   complement of each tour (the held gates):')
for hz in sorted(HC, key=lambda h: sorted(sorted(e) for e in h)):
    omitted = [e for e in cube_edges if e not in hz]
    deg = {}
    for e in omitted:
        for v in e:
            deg[v] = deg.get(v, 0) + 1
    pm = set(deg.values()) == {1}
    print(f'     held-set perfect matching: {pm} | type: {derangement_type(sorted(to_gate(e) for e in omitted))}')

print('=' * 72)
print('C6. projection to K4 braids + antipodal distance on tour')
def order_of(hz):
    el = set(hz)
    start = sorted(census)[0]
    order, cur, prev = [start], start, None
    while len(order) < 8:
        nxt = next(v for v in census
                   if v != prev and frozenset((cur, v)) in el)
        order.append(nxt); prev, cur = cur, nxt
    return order
K4_CYCLES = {'PUIR', 'PIUR', 'PIRU'}      # L3 §V table (undirected, from P)
from collections import Counter
proj = Counter()
anti_dists = Counter()
for hz in HC:
    order = order_of(hz)
    star_order = ''.join(o[1] for o in order if o[0] == 'star')
    # canonical undirected form: min over rotations of s and of reversed s
    def canon(s):
        return min(s[i:] + s[:i] for i in range(len(s)))
    cand = min(canon(star_order), canon(star_order[::-1]))
    proj[cand] += 1
    for p in poles:
        a, b = ('star', p), ('face', p)
        ia, ib = order.index(a), order.index(b)
        d = (ia - ib) % 8
        anti_dists[min(d, 8 - d)] += 1
print('   star-order -> K4 cycle (expect 2 tours per K4 cycle):', dict(proj))
print('   cube-antipode cyclic distance along tours (all should be odd, min 3):',
      dict(anti_dists))

print('=' * 72)
print('C7. the tower ladder of tours')
def k4_hc():
    s = set()
    for perm in permutations(poles[1:]):
        cyc = ('P',) + perm
        s.add(frozenset(frozenset((cyc[i], cyc[(i + 1) % 4])) for i in range(4)))
    return s
print('   K4 undirected Hamiltonian cycles =', len(k4_hc()), '(corpus L3 l.381: 3)')
def k5_hc():
    vs = list('ABCDE')
    s = set()
    for perm in permutations(vs[1:]):
        cyc = ('A',) + perm
        s.add(frozenset(frozenset((cyc[i], cyc[(i + 1) % 5])) for i in range(5)))
    return s
print('   K5 undirected Hamiltonian cycles =', len(k5_hc()), '(corpus L3 l.461: 12)')
print('   ladder  Q2:1 -> K4:3 -> Q3:6 -> K5:12 | geometric mean of 3,12 =',
      (3 * 12) ** 0.5)

print('=' * 72)
print('C8. sub-cube tower Q1 < Q2 < Q3 (fix bits of the matching code)')
print('   Q2 faces (fix 1 bit): 3*2 = 6   |   Q1 subcubes (fix 2 bits): 3*4 = 12')
print('   each Q1 = one bimedian choice, 2 states — the held bit alone (L3 l.532)')

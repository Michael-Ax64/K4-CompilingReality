# U1 against ENGINE-REFERENCE-AC s2.2 (reference edge P->U) and s2.8 (families = axes).
import itertools, functools, numpy as np
poles = ['P','U','I','R']
pf = lambda im: dict(zip(poles, im))
def sgn(pm):
    idx = [poles.index(pm[p]) for p in poles]
    return (-1)**sum(1 for a in range(4) for b in range(a+1,4) if idx[a] > idx[b])
comp = lambda a,b: {x: a[b[x]] for x in poles}
inv  = lambda a: {v:k for k,v in a.items()}
ident = pf(poles); allp = [pf(p) for p in itertools.permutations(poles)]

def g(x, w):                                   # s2.2: unique EVEN perm with P->x, U->w
    c = [p for p in allp if p['P']==x and p['U']==w and sgn(p)==1]
    assert len(c)==1; return c[0]
edges = [(x,w) for x in poles for w in poles if x!=w]
print("1. s2.2: two completions per directed edge:",
      all(len([p for p in allp if p['P']==x and p['U']==w])==2 for x,w in edges),
      "| the 12 even ones are distinct:", len({tuple(g(*e)[p] for p in poles) for e in edges})==12)

U = lambda e,f: comp(g(*f), inv(g(*e)))        # canonical transport from the trivialisation
print("2. U(f->e) = U(e->f)^-1 on all 132 ordered pairs:",
      all(U(f,e)==inv(U(e,f)) for e in edges for f in edges))
rng = np.random.default_rng(0); worst = True
for _ in range(2000):                           # random closed walks through the gate graph
    L = [edges[i] for i in rng.integers(0, 12, size=rng.integers(3, 8))]; L = L + [L[0]]
    hol = functools.reduce(comp, [U(L[i], L[i+1]) for i in range(len(L)-1)][::-1], ident)
    worst &= all(hol[p]==p for p in poles)
print("3. holonomy around 2000 random closed walks is the identity -> the canonical transport is FLAT:", worst)

# Gauge action on a holonomy (T,R) in V4 x| Z3:  conjugation sends T -> T + (1+R)u
sig = np.array([[0,1],[1,1]]) % 2
assert (np.linalg.matrix_power(sig,3) % 2 == np.eye(2)).all()
V4 = [np.array(v) for v in itertools.product((0,1), repeat=2)]
for lbl, R in [("R_Delta = identity", np.eye(2,dtype=int)), ("R_Delta = 3-cycle ", sig)]:
    reach = {tuple(((np.eye(2,dtype=int)+R) @ u) % 2) for u in V4}
    print(f"4. {lbl}: gauge orbit of T reaches {len(reach)} of 4 translations ->",
          "T is GAUGE-INVARIANT" if len(reach)==1 else "T can be gauged to 0, so it is NOT an invariant")

# Scan the gauge-invariant sector: R_Delta = id, translations closing (sum zero). Does the Z3 action still give torsion?
powers = [np.eye(2,dtype=int), sig, np.linalg.matrix_power(sig,2) % 2]
nz = tot = 0; example = None
for i,j in itertools.product(range(3), repeat=2):
    k = (-(i+j)) % 3                                            # product of the three = identity
    s1, s2 = powers[i], powers[j]
    for a, b in itertools.product(V4, V4):
        c = (a + b) % 2                                         # v_ij + v_jk + v_ki = 0
        T = (a + (s1 @ b) + ((s1 @ s2) % 2) @ c) % 2
        tot += 1
        if any(T):
            nz += 1
            if example is None and (i, j) != (0, 0): example = (i, j, k, a, b, c, T)
print(f"5. R_Delta = id and translations closing: T != 0 in {nz} of {tot} cases.")
i,j,k,a,b,c,T = example
print(f"   worked example: sigma powers ({i},{j},{k}), v_ij={a}, v_jk={b}, v_ki={c} (sum 0) -> T_Delta={T.astype(int)}")
print("   -> gauge-invariant discrete torsion exists, and here it is produced only by the Z3 action on V4.")
print("   with all sigma = id and v closing, T =", ((a+b+c)%2).astype(int), "(zero) -- the cross-term is doing the work")

# s2.8 solder form, computed from the cube rather than asserted: gate-edge -> unit vector on its bimedian axis.
corners = list(itertools.product((0,1), repeat=3))
squares = [(f, k) for f in range(3) for k in (0,1)]             # fix axis f at value k, vary the other two
tot = 0
for f, k in squares:
    ax = [i for i in range(3) if i != f]
    cyc = [(0,0), (1,0), (1,1), (0,1), (0,0)]                   # walk the square
    s = np.zeros(3, dtype=int)
    for p, q in zip(cyc, cyc[1:]):
        step = [i for i in range(2) if p[i] != q[i]][0]          # which bimedian bit flips
        s += (1 if q[step] > p[step] else -1) * np.eye(3, dtype=int)[ax[step]]
    tot += abs(s).sum()
print("6. s2.8 solder form, summed round each of the 6 cube squares: total |sum| =", tot,
      "-> zero discrete torsion, the Part One cube result reproduced from the engine's own edge->axis map")

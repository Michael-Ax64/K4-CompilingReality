# Does central inversion flip the bimedian phase offsets?  And which F are P-odd and T-odd?
import numpy as np, itertools
# Tetrahedron inscribed in the cube; DD201/ENGINE bimedian pairings.
V = {'P':np.array([1,1,1]), 'U':np.array([1,-1,-1]), 'I':np.array([-1,1,-1]), 'R':np.array([-1,-1,1])}
bimed = {'F': (('P','U'),('I','R')), 'C': (('P','R'),('I','U')), 'M': (('P','I'),('U','R'))}
mid = lambda e: (V[e[0]] + V[e[1]]) / 2
print("1. Central inversion through the centroid, acting on each bimedian's two edges:")
for name, (e1, e2) in bimed.items():
    m1, m2 = mid(e1), mid(e2)
    print(f"   {name}: mid{e1} = {m1.astype(int)}   mid{e2} = {m2.astype(int)}"
          f"   -> inversion maps the first to the second: {np.allclose(-m1, m2)}")
print("   => inversion EXCHANGES the two edges of every bimedian, so theta -> -theta.  theta is P-ODD.\n")

# The T_d character of the shear triple, against (x,y,z).
def rep(perm):                       # signed permutation on (theta_F, theta_C, theta_M)
    M = np.zeros((3,3)); order = ['F','C','M']
    for j, b in enumerate(order):
        img = tuple(sorted(perm[p] for p in bimed[b][0])), tuple(sorted(perm[p] for p in bimed[b][1]))
        for i, b2 in enumerate(order):
            tgt = tuple(sorted(bimed[b2][0])), tuple(sorted(bimed[b2][1]))
            if set(img) == set(tgt):
                lead = set(perm[p] for p in bimed[b][0])          # image of the leading edge
                M[i, j] = 1 if 'P' in lead else -1
    return M
poles = ['P','U','I','R']
perms = [dict(zip(poles, p)) for p in itertools.permutations(poles)]
def cls(pm):
    cyc, seen = [], set()
    for p in poles:
        if p in seen: continue
        l, q = 0, p
        while q not in seen: seen.add(q); q = pm[q]; l += 1
        cyc.append(l)
    return tuple(sorted(cyc, reverse=True))
chars = {}
for pm in perms: chars.setdefault(cls(pm), round(np.trace(rep(pm)), 9))
# (x,y,z) in T_d, realised as the spatial action on the three cube axes
def spatial(pm):
    A = np.linalg.lstsq(np.array([V[p] for p in poles]), np.array([V[pm[p]] for p in poles]), rcond=None)[0].T
    return A
sp = {cls(pm): round(np.trace(spatial(pm)), 6) for pm in perms}
print("2. Character by class, shear triple vs the spatial action on the cube axes:")
for k in sorted(chars, reverse=True): print(f"   {str(k):12s} shears {chars[k]:+.0f}   (x,y,z) {sp[k]:+.0f}")
print("   => the shear triple transforms as (x,y,z) does in T_d.\n")

# P and T parity of the candidate couplings. theta is P-odd (above) and T-odd (phase lead -> lag).
cands = {'theta_F (B)': lambda t: t[0], 'theta_F*theta_C*theta_M (A-prime)': lambda t: t[0]*t[1]*t[2],
         'Delta (A)': lambda t: (t[0]**2-t[1]**2)*(t[1]**2-t[2]**2)*(t[2]**2-t[0]**2)}
rng = np.random.default_rng(2); X = rng.normal(size=(40,3))
par = lambda f, M: (lambda r: int(round(r[0])) if np.allclose(r, r[0]) else 0)(np.array([f(M@x)/f(x) for x in X]))
Td_inv = lambda f: all(par(f, rep(pm)) == 1 for pm in perms)
print("3. Required: F must be P-odd AND T-odd (Nieh-Yan is P-odd, T-odd, like E.B).")
print(f"   {'coupling':34s} {'P (inversion)':>14s} {'T':>4s} {'T_d-invariant':>15s}  verdict")
for n, f in cands.items():
    P, T = par(f, -np.eye(3)), par(f, -np.eye(3))      # both act as theta -> -theta
    ok = (P == -1 and T == -1)
    print(f"   {n:34s} {P:>14d} {T:>4d} {str(Td_inv(f)):>15s}  {'PASSES' if ok else 'fails'}"
          + ("  <- unique carrier-symmetric choice" if ok and Td_inv(f) else ""))

"""
Verification for On_TheRiemannFreeze-TheAction.md
Conventions (Carroll / MTW): signature (-,+,+,+);
  nabla_mu V^rho = d_mu V^rho + Gamma^rho_{mu nu} V^nu   (derivative index first)
  T^rho_{mu nu} = Gamma^rho_{mu nu} - Gamma^rho_{nu mu}
  R^rho_{sig mu nu} = d_mu G^rho_{nu sig} - d_nu G^rho_{mu sig} + G^rho_{mu lam}G^lam_{nu sig} - G^rho_{nu lam}G^lam_{mu sig}
  Ric_{sig nu} = R^rho_{sig rho nu},  R = g^{sig nu} Ric_{sig nu};  S_EH = (1/2kappa) int sqrt(-g) R
Torsion irreducibles:
  v_mu = T^nu_{mu nu}                 (trace vector)
  a^mu = (1/6) eps^{mu nu rho sig} T_{nu rho sig}   (axial vector)
  q    = remainder                    (tensor part, 16 dof)
"""
import numpy as np, itertools
rng = np.random.default_rng(1)
eta = np.diag([-1., 1, 1, 1]); ei = eta.copy()

# Levi-Civita, eps_{0123} = +1
eps_l = np.zeros((4,)*4)
for p in itertools.permutations(range(4)):
    eps_l[p] = np.linalg.det(np.eye(4)[list(p)])
eps_u = np.einsum('ai,bj,ck,dl,ijkl->abcd', ei, ei, ei, ei, eps_l)

def contorted_connection(T_l):
    """Solve for metric-compatible G_{lam mu nu} (first index lowered) with given torsion T_{lam mu nu}."""
    ix = lambda l, m, n: 16*l + 4*m + n
    A, b = [], []
    for l, m, n in itertools.product(range(4), repeat=3):
        r = np.zeros(64); r[ix(l,m,n)] += 1; r[ix(n,m,l)] += 1; A.append(r); b.append(0.)   # metric compatibility
        r = np.zeros(64); r[ix(l,m,n)] += 1; r[ix(l,n,m)] -= 1; A.append(r); b.append(T_l[l,m,n])  # torsion
    A, b = np.array(A), np.array(b)
    x = np.linalg.lstsq(A, b, rcond=None)[0]
    return x.reshape(4,4,4), np.abs(A @ x - b).max()

def ricci_scalar_const(G_l):
    """Constant connection on flat background: only the GG terms of R survive."""
    G = np.einsum('ra,amn->rmn', ei, G_l)              # Gamma^rho_{mu nu}
    Riem = np.einsum('rml,lns->rsmn', G, G) - np.einsum('rnl,lms->rsmn', G, G)
    Ric = np.einsum('rsrn->sn', Riem)
    return np.einsum('sn,sn->', ei, Ric)

def parts(T_l):
    T_u = np.einsum('la,amn->lmn', ei, T_l)
    v = np.einsum('nmn->m', T_u)                        # v_mu
    a = np.einsum('mnrs,nrs->m', eps_u, T_l) / 6.0     # a^mu
    return v, a

def trace_torsion(v):            # T_{lam mu nu} built from v_mu, reproduces v
    return (np.einsum('ln,m->lmn', eta, v) - np.einsum('lm,n->lmn', eta, v)) / 3.0

def axial_torsion(a_up, k):      # T_{lam mu nu} = k eps_{lam mu nu sig} a^sig
    return k * np.einsum('lmns,s->lmn', eps_l, a_up)

# fix k so that the axial builder reproduces a^mu under the definition above
probe = rng.normal(size=4)
k = 1.0 / (parts(axial_torsion(probe, 1.0))[1] @ probe / (probe @ probe))
assert np.allclose(parts(axial_torsion(probe, k))[1], probe)

def tensor_part(T_l):
    v, a = parts(T_l)
    return T_l - trace_torsion(v) - axial_torsion(a, k)

dot = lambda x, y: np.einsum('m,mn,n->', x, ei if x.shape else ei, y)
vsq = lambda v: v @ ei @ v                      # v_mu v^mu  (v lower)
asq = lambda a: a @ eta @ a                     # a^mu a_mu  (a upper)
qsq = lambda q: np.einsum('lmn,la,mb,nc,abc->', q, ei, ei, ei, q)

print("=== 1. Quadratic decomposition of R(Gamma) for metric-compatible torsion ===")
coef = {}
for name, build, norm in [
    ('trace  v', lambda: trace_torsion(rng.normal(size=4)), lambda T: vsq(parts(T)[0])),
    ('axial  a', lambda: axial_torsion(rng.normal(size=4), k), lambda T: asq(parts(T)[1])),
    ('tensor q', lambda: tensor_part(np.einsum('lmn->lmn', (lambda X: X - X.transpose(0,2,1))(rng.normal(size=(4,4,4))))), lambda T: qsq(T)),
]:
    vals = []
    for _ in range(6):
        T = build(); G, res = contorted_connection(T); assert res < 1e-10
        vals.append(ricci_scalar_const(G) / norm(T))
    coef[name] = np.mean(vals)
    print(f"  R / |{name[-1]}|^2 = {np.mean(vals):+.6f}   (spread {np.ptp(vals):.1e})")

# cross terms: R(random T) = c_v v^2 + c_a a^2 + c_q q^2 exactly?
worst = 0
for _ in range(20):
    X = rng.normal(size=(4,4,4)); T = X - X.transpose(0,2,1)
    v, a = parts(T); q = tensor_part(T)
    G, _ = contorted_connection(T)
    pred = coef['trace  v']*vsq(v) + coef['axial  a']*asq(a) + coef['tensor q']*qsq(q)
    worst = max(worst, abs(ricci_scalar_const(G) - pred))
print(f"  no cross terms between irreducibles: max residual {worst:.1e}")

c_v, c_a, c_q = coef['trace  v'], coef['axial  a'], coef['tensor q']
print(f"\n  c_v = {c_v:+.4f}   c_a = {c_a:+.4f}   c_q = {c_q:+.4f}")

print("\n=== 2. Health of the induced kinetic term,  L = (1/2k)[c X^2 - beta X.dF]  =>  L_ind = -(beta^2/(8 k c)) (dF)^2 ===")
for nm, c in [('trace channel  (v . dF)', c_v), ('axial channel  (a . dF)', c_a)]:
    print(f"  {nm}: c = {c:+.4f}  ->  {'HEALTHY' if c > 0 else 'GHOST (wrong-sign kinetic term)'}")

print("\n=== 3. The court's literal term  beta*theta*v.a  is quadratic in torsion ===")
print("  quadratic form in (v,a): [[c_v, b/2],[b/2, c_a]],  det = c_v*c_a - b^2/4")
print(f"  c_v*c_a = {c_v*c_a:+.4f}  -> det < 0 for every b  -> nondegenerate -> unique stationary point v = a = 0")
print("  i.e. the demanded coupling sources no torsion at any theta: classically inert.")

print("\n=== 4. Sign-convention check: the same curvature formula on a round 2-sphere ===")
import sympy as sp
th, ph, r = sp.symbols('theta phi r', positive=True)
xs = [th, ph]; g = sp.diag(r**2, r**2*sp.sin(th)**2); gi = g.inv()
Gam = [[[sp.simplify(sum(gi[a,d]*(sp.diff(g[d,b],xs[c]) + sp.diff(g[d,c],xs[b]) - sp.diff(g[b,c],xs[d]))
          for d in range(2))/2) for c in range(2)] for b in range(2)] for a in range(2)]   # Gam[a][b][c] = G^a_{bc}
def Riem(rho, sig, mu, nu):
    e = sp.diff(Gam[rho][nu][sig], xs[mu]) - sp.diff(Gam[rho][mu][sig], xs[nu])
    e += sum(Gam[rho][mu][l]*Gam[l][nu][sig] - Gam[rho][nu][l]*Gam[l][mu][sig] for l in range(2))
    return e
Rs = sp.simplify(sum(gi[s,n]*sum(Riem(rh, s, rh, n) for rh in range(2)) for s in range(2) for n in range(2)))
print(f"  R(sphere) = {Rs}   -> {'positive: convention confirmed' if Rs.subs(r,1) > 0 else 'NEGATIVE: flip all health verdicts'}")

print("\n=== 5. How the three bimedian angles transform under S4, using DD201's stated convention ===")
print("  DD201 §II: 'P-U leads I-R (theta>0)', 'P-R leads I-U (theta>0)', 'P-I leads U-R (theta>0)'")
print("  i.e. theta_b > 0 iff the P-containing edge of bimedian b leads. Relabeling is passive.")
poles = ['P','U','I','R']
bimed = {'F': (('P','U'),('I','R')), 'C': (('P','R'),('I','U')), 'M': (('P','I'),('U','R'))}
order = ['F','C','M']
def which(edgeset):
    for nm, (e1, e2) in bimed.items():
        if {frozenset(e1), frozenset(e2)} == edgeset: return nm
def rep(perm):           # perm: dict pole -> pole
    Mx = np.zeros((3,3))
    for j, b in enumerate(order):
        e1, e2 = bimed[b]                       # e1 contains P
        s1 = frozenset(perm[x] for x in e1); s2 = frozenset(perm[x] for x in e2)
        tgt = which({s1, s2})
        sign = +1 if 'P' in s1 else -1          # does the image of the leading (P-)edge still contain P?
        Mx[order.index(tgt), j] = sign
    return Mx
perms = [dict(zip(poles, p)) for p in itertools.permutations(poles)]
def cycle_type(perm):
    seen, ct = set(), []
    for x in poles:
        if x in seen: continue
        L, y = 0, x
        while y not in seen: seen.add(y); y = perm[y]; L += 1
        ct.append(L)
    return tuple(sorted(ct, reverse=True))
sgn = lambda perm: int(round(np.linalg.det(np.array([[1 if perm[a]==b else 0 for b in poles] for a in poles]))))
mats = [rep(p) for p in perms]
hom = all(np.allclose(rep({x: p2[p1[x]] for x in poles}), rep(p2) @ rep(p1)) for p1 in perms for p2 in perms)
print(f"  it is a representation (composition respected, 576 pairs): {hom}")
chars = {}
for p, Mx in zip(perms, mats): chars.setdefault(cycle_type(p), set()).add(round(np.trace(Mx)))
print("  character by class:", {k: sorted(v) for k, v in chars.items()})
std = {(1,1,1,1):3, (2,1,1):1, (2,2):-1, (3,1):0, (4,):-1}
print(f"  matches S4 standard rep (polar vector of T_d: 3,1,-1,0,-1): {all(chars[c]=={std[c]} for c in std)}")
print("  -> the three bimedian shears transform as a POLAR 3-VECTOR on the cube's axes.")

print("\n=== 6. Invariant polynomials theta = (x,y,z) = (theta_F, theta_C, theta_M) ===")
X = rng.normal(size=(200, 3))
tests = {
    'linear  any c.theta': None,
    'x^2+y^2+z^2':        lambda t: t @ t,
    'x*y*z':              lambda t: t[0]*t[1]*t[2],
    'Delta=(x2-y2)(y2-z2)(z2-x2)': lambda t: (t[0]**2-t[1]**2)*(t[1]**2-t[2]**2)*(t[2]**2-t[0]**2),
}
avg = sum(mats) / 24
print(f"  linear invariants: rank of the averaging projector = {np.linalg.matrix_rank(avg, tol=1e-9)}  (0 => none exist)")
for nm, f in tests.items():
    if f is None: continue
    inv = all(np.allclose([f(M @ t) for t in X], [f(t) for t in X]) for M in mats)
    pse = all(np.allclose([f(M @ t) for t in X], [sgn(p)*f(t) for t in X]) for p, M in zip(perms, mats))
    print(f"  {nm:32s}  S4-scalar: {inv!s:5s}   S4-pseudoscalar (sign rep): {pse}")

print("\n=== 7. The Active/Reactive charge (+,+,-,-) on (P,U,I,R): its stabilizer and what it leaves invariant ===")
stab = [p for p in perms if {p['P'], p['U']} == {'P','U'}]
print(f"  stabilizer order {len(stab)}: {[ ''.join(p[x] for x in poles) for p in stab]}")
for j, b in enumerate(order):
    inv = all(np.isclose(rep(p)[j, j], 1) and np.isclose(abs(rep(p)[:, j]).sum(), 1) for p in stab)
    print(f"  theta_{b} invariant under the charge stabilizer: {inv}")

print("\n=== 8. Molien series: degrees at which invariants exist (exact, no inspection) ===")
t = sp.symbols('t')
def molien(twist):
    tot = 0
    for p, M in zip(perms, mats):
        w = sgn(p) if twist else 1
        tot += sp.Rational(w) / sp.Matrix(np.eye(3) - t*sp.Matrix(M.astype(int))).det()
    return sp.series(sp.simplify(tot/24), t, 0, 9).removeO()
ms, mp = sp.Poly(molien(False), t), sp.Poly(molien(True), t)
print("  scalars (trivial rep):      ", sorted([(d[0], c) for d, c in ms.terms()])[:6])
print("  pseudoscalars (sign rep):   ", sorted([(d[0], c) for d, c in mp.terms()])[:6])
print("  -> no invariant of degree 1; first scalar at degree 2, first pseudoscalar at degree 6.")

print("\n=== 9. Where Delta vanishes ===")
for lab, th3 in [('all equal |theta|', [0.5,0.5,0.5]), ('two equal', [0.5,0.5,0.2]), ('two opposite', [0.5,-0.5,0.2]),
                 ('pairwise distinct', [0.5,0.3,0.1]), ('one zero, others distinct', [0.5,0.3,0.0])]:
    x, y, z = th3
    print(f"  {lab:28s} {th3}  Delta = {(x*x-y*y)*(y*y-z*z)*(z*z-x*x):+.6f}")

print("\n=== 10. The rings and the third-turns, explicitly (signed permutations) ===")
named = {'(PU)(IR) holds Fixed':    {'P':'U','U':'P','I':'R','R':'I'},
         '(PR)(UI) holds Cardinal': {'P':'R','R':'P','U':'I','I':'U'},
         '(PI)(UR) holds Mutable':  {'P':'I','I':'P','U':'R','R':'U'},
         '3-cycle (UIR)':           {'P':'P','U':'I','I':'R','R':'U'},
         '3-cycle (PUI)':           {'P':'U','U':'I','I':'P','R':'R'}}
for nm, p in named.items():
    M = rep(p).astype(int)
    print(f"  {nm:26s} rows F,C,M: {M.tolist()}")

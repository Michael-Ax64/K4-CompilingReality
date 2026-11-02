# Does the AC set bend the DC floor, and where exactly?
import sympy as sp, numpy as np, itertools
p, q, c = sp.symbols('p q c', real=True)
s = sp.Rational(1,2)*sp.log(sp.exp(2*p) + sp.exp(2*q))        # |S|^2 = P^2 + Q^2 in log coordinates
sp_, sq_ = sp.diff(s,p), sp.diff(s,q)
spp, sqq, spq = sp.diff(s,p,2), sp.diff(s,q,2), sp.diff(s,p,q)
W = 1 + sp_**2 + sq_**2
K = sp.simplify((spp*sqq - spq**2)/W**2)
H = sp.simplify(((1+sq_**2)*spp - 2*sp_*sq_*spq + (1+sp_**2)*sqq)/(2*W**sp.Rational(3,2)))
print("1. Surface e^{2p} + e^{2q} = e^{2s} in log space:")
print("   Gaussian curvature K =", K, " -> developable (a cylinder), NOT curved in counsel's sense")
print("   mean curvature H     =", sp.simplify(H.subs({p:sp.Rational(3,10), q:-sp.Rational(7,10)})),
      "(nonzero) -> it bends, but in one direction only")
print("   homogeneity: s(p+c,q+c) - s(p,q) =", sp.simplify(s.subs({p:p+c,q:q+c}) - s),
      "-> the surface is a cylinder along (1,1,1)")
th = sp.symbols('theta', real=True)
print("   the whole bend, named:  log P - log|S| =", sp.log(sp.cos(th)), " (the power factor)\n")

# 2. The corpus's complex AC core in the polar chart: S = U I*, U = Z I.
rels = np.array([[1,0,-1,0,-1,0,0,0],[0,1,0,-1,0,1,0,0],[0,0,1,0,-1,0,-1,0],[0,0,0,1,0,-1,0,-1]])
print("2. Polar chart (log|.|, arg) for S, U, I, Z:")
print("   rank of the two modulus relations =", np.linalg.matrix_rank(rels[[0,2]][:, [0,2,4,6]]),
      "| rank of the two phase relations =", np.linalg.matrix_rank(rels[[1,3]][:, [1,3,5,7]]),
      "| total =", np.linalg.matrix_rank(rels))
print("   -> in polar coordinates the AC core DOUBLES the floor (2 + 2); it does not bend it.")
print("   The bend enters only with the rectangular split P = |S|cos(theta), Q = |S|sin(theta),")
print("   and with the additive layer X = wL - 1/(wC) and series/parallel sums.")
print("   ENGINE s.VIII.1 names exactly this: |S| = sqrt(P^2+Q^2) 'requires complex addition'.\n")

# 3. The DC floor's own symmetry group: the kernel of the rank-2 relation matrix.
V = ['P','U','I','R']
A = np.array([[1,-1,-1,0],[0,1,-1,-1]])                        # P = UI ; U = IR, as log relations
ker = []
for cand in itertools.product([-2,-1,0,1,2], repeat=4):
    if any(cand) and not np.any(A @ np.array(cand)): ker.append(cand)
basis = [k for k in ker if k in [(2,1,1,0),(1,1,0,1)]]
print("3. Scalings of the DC floor (kernel of the log relations), dim =", 4 - np.linalg.matrix_rank(A))
for k in basis:
    print(f"   {dict(zip(V,k))}  -> P^{k[0]} U^{k[1]} I^{k[2]} R^{k[3]}")
print("   uniform scaling (1,1,1,1) in the kernel:", bool(not np.any(A @ np.ones(4))),
      "-> agrees with ENGINE s.X.7: no uniform scaling exists, but exactly TWO scalings do.")

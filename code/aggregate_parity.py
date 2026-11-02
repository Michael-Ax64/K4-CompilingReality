# Averages of candidate couplings over populations closed under different "mirror" groups.
import runpy, io, contextlib, numpy as np
with contextlib.redirect_stdout(io.StringIO()):
    T = runpy.run_path('torsion_action.py')
rep, sgn, perms, poles = T['rep'], T['sgn'], T['perms'], T['poles']
F = {'theta_F': lambda t: t[0], 'theta_F*theta_C*theta_M': lambda t: t[0]*t[1]*t[2],
     'Delta': lambda t: (t[0]**2-t[1]**2)*(t[1]**2-t[2]**2)*(t[2]**2-t[0]**2),
     '|theta|^2 (cost)': lambda t: t@t}
rng = np.random.default_rng(11)
seeds = rng.normal(loc=[0.4, 0.1, -0.2], scale=0.5, size=(4000, 3))   # a biased, non-symmetric seed population
A4 = [rep(p) for p in perms if sgn(p) == 1]; S4 = [rep(p) for p in perms]
groups = {'no closure (raw seeds)': [np.eye(3)],
          'A4 (rotations of the solid)': A4,
          'S4 (rotations + reflections)': S4,
          'A4 x {+1,-1} (rotations + inversion, polar shears)': A4 + [-m for m in A4]}
for g, mats in groups.items():
    pop = np.array([m @ s for s in seeds for m in mats])
    print(f"{g:52s}", "  ".join(f"{k}={np.mean([f(x) for x in pop]):+.3e}" for k, f in F.items()))

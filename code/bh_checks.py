"""Checks for L4-BlackHoles: the counsel's pressure points, verified at source.
Run: python3 bh_checks.py"""
import sympy as sp

print("=== 1. Schwarzschild components and determinant ===")
t,r,th,ph,M = sp.symbols('t r theta phi M', positive=True)
f = 1 - 2*M/r
g = sp.diag(-f, 1/f, r**2, r**2*sp.sin(th)**2)
print("g_tt*g_rr =", sp.simplify(g[0,0]*g[1,1]))
print("det g     =", sp.simplify(g.det()))
for name,(i,j) in {'g_tt':(0,0),'g_rr':(1,1),'g_thth':(2,2)}.items():
    print(f"  lim r->0+ {name} =", sp.limit(g[i,j], r, 0, '+'))
print("  -> no finite limit tensor: g_tt diverges while g_rr vanishes; 'rank 2' is not a limit statement")

print("\n=== 2. Interior near r=0 is Kasner (cigar), not a rank drop ===")
# interior: r timelike. proper time tau with d tau = dr / sqrt(2M/r - 1) ~ sqrt(r/2M) dr  => tau ~ (2/3) r^{3/2}/sqrt(2M)
tau = sp.symbols('tau', positive=True)
r_of_tau = (sp.Rational(3,2)*sp.sqrt(2*M)*tau)**sp.Rational(2,3)
gtt_lead = 2*M/r_of_tau          # coefficient of dt^2 (spacelike in interior), leading term
gang = r_of_tau**2               # coefficient of dOmega^2
p_t   = sp.simplify(sp.log(sp.sqrt(gtt_lead)).diff(tau)*tau)   # Kasner exponent: sqrt(g) ~ tau^p
p_ang = sp.simplify(sp.log(sp.sqrt(gang)).diff(tau)*tau)
print("Kasner exponents (t, theta, phi):", p_t, p_ang, p_ang)
print("  sum p =", sp.simplify(p_t+2*p_ang), " sum p^2 =", sp.simplify(p_t**2+2*p_ang**2), "(Kasner requires 1, 1)")
print("  spatial volume ~ tau^", sp.simplify(p_t+2*p_ang), "-> 0 : det collapses, one direction stretches")

print("\n=== 3. FLRW: the 'rank of the limit' depends on the time coordinate ===")
tt,eta = sp.symbols('t eta', positive=True)
a_t = tt**sp.Rational(2,3)                     # dust, cosmic time
print("cosmic time:    g = diag(-1, a^2, a^2, a^2), a->0  -> limit diag(-1,0,0,0): rank 1")
# conformal time: d eta = dt/a ; for dust a ~ eta^2
print("conformal time: g = a(eta)^2 diag(-1,1,1,1), a->0  -> limit 0: rank 0")
print("  -> rank of the limit is not invariant: the coordinate change is singular exactly at the boundary")
print("  invariant version: g = Omega^2 * (regular), Omega->0  (Goode-Wainwright 'isotropic singularity')")
print("  Schwarzschild/Kasner cannot be written so: anisotropic exponents survive any conformal rescaling")

print("\n=== 4. Healthy massless scalar satisfies NEC and SEC (focuses, cannot bounce) ===")
# T_mn = d_m F d_n F - 1/2 g (dF)^2 ; trace T = -(dF)^2 in 4D ; T_mn - 1/2 T g_mn = d_m F d_n F
print("  R_mn k^m k^n = kappa (k.dF)^2 >= 0   (NEC)")
print("  R_mn u^m u^n = kappa (u.dF)^2 >= 0   (SEC)  -> the F sector alone aids focusing")

print("\n=== 5. Cartan density and the solar-mass bounce radius ===")
import math
hbar=1.054571817e-34; c=2.99792458e8; G=6.67430e-11
mN=1.67262192e-27; me=9.1093837e-31; Msun=1.98892e30
lP2 = G*hbar/c**3
for name,m in [('nucleon',mN),('electron',me)]:
    lam = hbar/(m*c)
    rho = m/(lam*lP2)                       # Hehl et al. 1976 estimate
    R = (3*Msun/(4*math.pi*rho))**(1/3)
    print(f"  {name:8s}: rho_C ~ m/(lambda_C l_P^2) = {rho:.1e} kg/m^3 = {rho*1e-3:.1e} g/cm^3 ; solar-mass radius {R:.1e} m")
rho_c38 = 1e38*1e3  # counsel's figure, g/cm^3 -> kg/m^3
print(f"  counsel's 1e38 g/cm^3 would give radius {(3*Msun/(4*math.pi*rho_c38))**(1/3):.1e} m, not 1e-9 m")
print(f"  nuclear density ~2.3e14 g/cm^3 ; Planck density ~{(c**5/(hbar*G**2))*1e-3:.1e} g/cm^3")

print("\n=== 6. Species dependence: rho_C = m/(lambda_C l_P^2) = m^2 c/(hbar l_P^2) scales as m^2 ===")
mnu = 0.1*1.78266192e-36   # 0.1 eV/c^2
for name,m in [('nucleon',mN),('electron',me),('neutrino 0.1eV',mnu)]:
    rho = m**2*c/(hbar*lP2)
    R = (3*Msun/(4*math.pi*rho))**(1/3)
    print(f"  {name:15s}: {rho*1e-3:.1e} g/cm^3, solar-mass radius {R:.1e} m")
Rs = 2*G*Msun/c**2
print(f"  solar-mass Schwarzschild radius {Rs:.1e} m ; l_P = {math.sqrt(lP2):.1e} m")
print("  -> the heuristic is per species and assumes a spin density of that species; it does not say which sets the threshold")

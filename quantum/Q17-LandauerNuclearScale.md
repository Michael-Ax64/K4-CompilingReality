# Q17-LandauerNuclearScale
## The Deuteron, Assimilated and Tested

A result has earned its standing when every constant it imports is named and sorted, and nothing domain-specific is left bearing load in its pure number. There are three kinds of import. A **dimensionless universal** — $\pi$, $\ln 2$, a square root, a normalization to a baseline — belongs to no domain. A **structural load** is a domain magnitude that moves the dimensionless answer when taken away. An **interface payload** only renders a finished dimensionless answer in a consumer's units. Only structural load is a debt.

Run that test on the deuteron, and on everything the deuteron can be compared against, and the verdict is smaller and sharper than a first pass suggests. Two readings die: the deuteron's $1/\pi^2$ as the law of a class, and nuclear binding as a count of bits at one price. What stands is a single bound channel among four, a pole map that standard scattering theory already draws, five measured numbers that land near simple geometric values at a rate chance alone could manage one time in sixteen, and one fine-tuning — the two-nucleon system sitting near the unitary point — whose reason is the question the corpus is built to ask.

---

## Constants and Conventions

$\hbar c = 197.3269804$ MeV·fm. $m_{\pi^\pm} = 139.57039$ MeV; $m_{\pi^0} = 134.9768$ MeV; $m_{\bar\pi} = (2m_{\pi^\pm} + m_{\pi^0})/3 = 138.0392$ MeV. $m_p = 938.272088$, $m_n = 939.565421$ MeV; $\mu_{np} = 469.4592$ MeV/$c^2$; $\lambda_\mu \equiv \hbar/\mu c = 0.420328$ fm. $\alpha = 1/137.035999177$; $Z_0 = 376.730313668\ \Omega$; $R_K = h/e^2 = 25\,812.80745\ \Omega$. Two-nucleon inputs: $B_d = 2.224566$ MeV; $a_t = 5.4192$ fm; $r_t = 1.7536$ fm; $a_{np} = -23.74$ fm, $r_{np} = 2.75$ fm; $a_{nn} = -18.9(4)$ fm, $r_{nn} = 2.75$ fm; $a_{pp}$ (nuclear, Coulomb-removed) $= -17.3(4)$ fm, $r_{pp} = 2.85$ fm.

**Definitions.** The assimilated coordinate of a two-body state is $X \equiv \pi^2(\kappa/m_\pi)^2 = \pi^2 B/(m_\pi^2c^2/2\mu)$, with $\kappa = \sqrt{2\mu B}/\hbar$. For a channel with no bound state, the zero-range rendering uses the scattering length, $X \equiv \pi^2/(m_\pi|a|)^2$. The like-nucleon singlet length $a_s$ is the **geometric mean** of $|a_{nn}|$ and $|a_{pp}|$, $18.0823$ fm, throughout; where a claim depends on that choice, the band over the measured ranges is given instead. The bend dial is $f \equiv r_e\kappa/2$ with $\kappa$ **signed**: positive for a bound pole ($k = +i\kappa$), negative for a virtual pole ($k = -i\gamma$). The default pion is $m_{\pi^\pm}$, and §IV states what that choice costs.

**Status vocabulary.** **ADOPTED**: standard physics, correct, and not the framework's result. **LANDED**: the framework's own result, standing. **OPEN VOTE**: a relation with a named derivation owed and a kill condition. **CANDIDATE**: inhabited, not derived. **REFUTED**. **INTERFACE**: payload, not debt.

Every number below is computed in the blocks; the blocks run in order and share one namespace.

```python
from mpmath import mp, mpf, sqrt, pi, log, atan, cos, degrees, cosh, sinh, exp
mp.dps = 15
hc = mpf('197.3269804'); mpc = mpf('139.57039'); mp0 = mpf('134.9768'); mpb = (2*mpc + mp0)/3
m_p = mpf('938.272088'); m_n = mpf('939.565421'); mu = m_p*m_n/(m_p + m_n)
alpha = 1/mpf('137.035999177'); B_d = mpf('2.224566')
a_t, r_t = mpf('5.4192'), mpf('1.7536')
a_np, a_nn, a_pp = mpf('23.74'), mpf('18.9'), mpf('17.3')
a_s = sqrt(a_nn*a_pp)
k_d = sqrt(2*mu*B_d)/hc
X = lambda kappa, m: pi**2*(kappa*hc/m)**2
print(mpb, mu, hc/mu, a_s, k_d)   # 138.0392  469.4592  0.420328  18.0823  0.231606
```

---

## I. Two Ways to Hold a Constant Badly

The first is to **lean on a constant and call the leaning a result.** The deuteron binds at $2.2245$ MeV. A per-bit energy of $0.66$ MeV is to hand; multiply by a count of erased branch-pointers, $3.37$, and $2.22$ appears. The count was chosen so the product hit the target. The tell is a non-integer multiplier fixed after the target was known.

The second is to **defer a constant so completely that the algebra has no purchase on it** — *2.2245 MeV is nuclear physics and none of our business.* It reads as discipline and is a flinch. It mistakes the present limit of a theory for its permanent structure.

Both fail for one reason: **a completed meta-physics cannot terminate on a domain constant bearing load in a dimensionless structure.** Constants are scaffolding. Lean on them to climb; take each one down when the pure number stands without it; and where it does not, say which pole is still standing.

---

## II. The Liberation Pattern

The move that liberates a constant is the one `QED-EotvosBound` makes explicit: **normalize the variable against its own baseline until it is dimensionless, and then the algebra can speak.** The relational current is refused in amperes and read as $\Delta I/I_0$; the form $\eta = -2(\Delta I/I_0)^2$ imports a normalization and nothing else, and $\eta \approx -3.2\times10^{-18}$ lands below every experimental bound.

The **cosmological constant** goes the same way, with one correction that keeps the reading honest. The observed vacuum density over the Planck density is the square of a scale-span, but not of $\ell_P/R_H$ alone:

$$\frac{\rho_\Lambda}{\rho_P} = \frac{3\Omega_\Lambda}{8\pi}\left(\frac{\ell_P}{R_H}\right)^2.$$

The shape survives — a span squared — and the factor $\sqrt{3\Omega_\Lambda/8\pi} \approx 0.29$ is real, with $\Omega_\Lambda$ an observed input.

```python
lP = mpf('1.616255e-35'); c = mpf('299792458'); H0 = mpf('67.4')*1000/mpf('3.0857e22'); OL = mpf('0.685')
r = lP/(c/H0); s = sqrt(3*OL/(8*pi))*r
print(r, s, s/r)   # 1.1776e-61   3.3673e-62   0.28595
```

The **vacuum impedance** is the case where the obvious liberation is the wrong one. $Z_0$ is $119.917\pi\ \Omega$, not $120\pi$. Before 2019 the SI fixed $\mu_0 = 4\pi\times10^{-7}$ exactly, which with the exact $c$ made $Z_0 = 119.917\pi$ exactly; $120\pi$ is the $c \approx 3\times10^8$ rounding and was never the SI value, and the $\pi$ in $\mu_0$ is the unit system's rationalization convention. The dimensionless content of $Z_0$ is its ratio to the resistance quantum, $Z_0/2R_K = \alpha$, which `L3-ConstitutiveAlpha` owns.

```python
Z0 = mpf('376.730313668'); RK = mpf('25812.80745')
print(Z0/pi, (120*pi - Z0)/Z0, Z0/(2*RK))   # 119.91698   6.92e-4   0.00729735257
```

One pattern across all three: lean on the magnitude to find the structure, normalize until the structure is a pure number, and say which inputs the pure number still needs. A near-hit on a round number is not a liberation.

---

## III. Assimilate First

The operative question is never *what does it weigh* — weight is domain units, and domain units are the fence. The question is *what is this thing in its own ratios.* Take up the standpoint from inside it and let it describe itself in numbers that owe nothing to a laboratory. The deuteron does not know it is measured in MeV. It knows how deeply it is bound against what it is made of, and how its size compares to the reach of the force that holds it.

---

## IV. The Deuteron, Assimilated

The deuteron is the only bound state of two nucleons: one proton, one neutron, spin-triplet $^3S_1$, bound at $2.224566$ MeV, rms radius $1.98$ fm around a force that reaches about $1.4$. It lives at the threshold where binding switches on.

**Against its substance:** $B/(m_p + m_n) = 1.18\times10^{-3}$.

**Against the reach of the force:**

$$X_d = \pi^2\left(\frac{\kappa_d}{m_\pi}\right)^2 = 1.0582\ (m_{\pi^\pm}), \quad 1.0819\ (m_{\bar\pi}), \quad 1.1315\ (m_{\pi^0}).$$

```python
print(B_d/(m_p + m_n))                       # 0.0011846
print([X(k_d, m) for m in (mpc, mpb, mp0)])  # 1.058245  1.081852  1.131500
print(k_d*hc/mpc)                            # 0.327449
```

**The pion choice is an uncomputed Layer 3 correction.** One-pion exchange in the $np\ ^3S_1$ channel uses both charged and neutral pions, and the yardsticks differ by the electromagnetic splitting between them: $\Delta m_\pi/m_\pi \approx 3.4\% \approx 4.7\alpha$, which is the return-leg re-holding of `On_TheIsNessTax` (Layer 3, order $\alpha$) made visible in the mediator. This leading-order rendering of $X_d$ does not include that correction, and the spread across choices — $1.058$ ($m_{\pi^\pm}$), $1.082$ ($m_{\bar\pi}$), $1.132$ ($m_{\pi^0}$) — is that correction's width showing in the yardstick, not a debt. The scope rule of `L1-CompilingReality` applies: this file demonstrates the topology is present where physics has been working, not emits the substrate's values. What is demonstrated across the band is $X_d > 1$ — the interior adds binding beyond the asymptote-only estimate (§XI) — and $X_d \approx 1$ to within the Layer 3 width. Which point in the band is the structural one is the Layer 3 computation's call, a derivation target for the IsNessTax machinery, not a choice to defend here.

**The nucleon-to-pion ratio is structural load.** The binding fraction factors as

$$\frac{B}{m_p+m_n} \approx \frac{1}{2}\left(\frac{\kappa_d}{m_\pi}\right)^2\left(\frac{m_\pi}{m_N}\right)^2,$$

and $m_N/m_\pi \approx 6.72$ is in it. Whether two nucleons bind near threshold at all depends on how heavy they are against the pion's reach. The deuteron imports $\pi$ and a mass ratio the corpus does not yet derive.

```python
print(m_p/mpc, (k_d*hc/mpc)**2*mpc**2/(2*mu*(m_p + m_n)))   # 6.72257   0.0011846
```

---

## V. The Interior Signature

The signature $X_d - 1$ is the part of the state the asymptotic face cannot carry (§XI). The candidate identification is the tensor-force admixture:

| Observable | Value |
|---|---|
| $X_d - 1$ | $5.82\%$ ($m_{\pi^\pm}$); $8.19\%$ ($m_{\bar\pi}$); $13.15\%$ ($m_{\pi^0}$) |
| D-state probability $P_D$ | $4.8$–$6.0\%$ across potentials |
| Quadrupole moment $Q_d$ | $+0.286\ e\,\text{fm}^2$, prolate |
| Asymptotic D/S ratio $\eta$ | $0.0256$ |

**OPEN VOTE, strained.** $P_D$ is not an observable: phase-equivalent potentials move strength between tensor and central channels, and the $4.8$–$6.0\%$ spread is that ambiguity. The match to $P_D$ holds only on $m_{\pi^\pm}$ and breaks on the exchange-complete $m_{\bar\pi}$. The distortion itself is solid and quadrupolar — axially symmetric, parity-even — a twist, not a handedness. Whether the corpus's edge-level enantiomerism surfaces in the S–D interference is a question the nuclear data do not force.

---

## VI. The Mass Ladder: One Rung Held, One Missing

The rung below the deuteron is the step from the electronic ground to the hadronic ground, carried by `Q15-KairosBorn` and `L3-ConstitutiveAlpha` as a three-term Laurent expansion in $\alpha$:

$$\frac{m_{\pi^\pm}}{m_e} = \frac{2}{\alpha} - \frac{3}{\pi} + 2\alpha = 273.131663 \quad (\text{measured } 273.132440;\ 2.84\ \text{ppm}).$$

Bare carrier $2/\alpha = 274.0720$, Nambu's relation, $0.344\%$ high. Hadronic It-Ness $-3/\pi = -0.9549$; residual $-0.0056\%$. Electronic It-Ness $+2\alpha = +0.0146$; residual $2.84$ ppm, about $397$ eV in the pion's rest mass.

```python
me = mpf('0.51099895'); E = mpc/me
for t in (2/alpha, 2/alpha - 3/pi, 2/alpha - 3/pi + 2*alpha):
    print(t, (t - E)/E)                       # 274.0720 +3.44e-3 | 273.11707 -5.6e-5 | 273.131663 -2.84e-6
print((E - (2/alpha - 3/pi + 2*alpha))*me*1e6)   # 396.8 eV
```

Its rank is the one `L3-ConstitutiveAlpha` gives it: **OPEN VOTE**, closing when the gap equation lands this expression as its unique self-consistent solution, with the colour count imported from SU(3). It is cited here, not landed here.

The rung the deuteron needs is the next one up, $m_N/m_\pi \approx 6.72$. No file in the corpus derives it. With it, the ladder from $m_e$ to the deuteron's binding fraction would run on $\alpha$, $\pi$ and integers. Without it, a measured mass ratio bears load.

---

## VII. The Landauer Rate

`QED-TwoBranchMinting` §IV records the debt: mass defects as the exhaust of Landauer erasure when nucleons commit to a bound blanket, with the operator turning an erased bit into an energy unwritten. The room-temperature bit, $k_BT\ln 2 \approx 0.018$ eV, misses the nuclear scale by eight orders of magnitude.

The normalization is the Eötvös move: evaluate against the event's own baseline. Nucleons commit at the boundary of the strong force, the deconfinement crossover $T_c \approx 156.5$ MeV ($1.8\times10^{12}$ K). That scale is often called $\Lambda_{\text{QCD}}$ loosely; it is not the $\overline{\text{MS}}$ $\Lambda_{\text{QCD}}$, and the rendered MeV value depends on which is meant. $T_c$ is not the vacuum's temperature. It is where thermal agitation matches the non-thermal structure of the confined vacuum, whose condensates do not quiet as temperature falls; that is why the thermal expression lands there, and why reading $T \to 0$ off it gives zero and means nothing (`L3-FormalFoundations` §I.b). Through the one-loop phase-burn factor of `Q13`:

$$\frac{E_{\text{bit}}}{k_BT_c} = \frac{\ln 2}{16\pi^2} = 4.39\times10^{-3}, \qquad E_{\text{bit}} \approx 0.69\ \text{MeV}.$$

```python
kB = mpf('8.617333262e-5')
print(kB*300*log(2), log(2)/(16*pi**2), mpf('156.5')*log(2)/(16*pi**2))   # 0.01792 eV   0.0043894   0.68694 MeV
```

The sort: $\ln 2$ and $1/16\pi^2$ are universals; $T_c$ is interface payload. The rate's structure is liberated.

**The rate's consumer is gone.** The claim it was built to serve — binding equals an isotope-specific count times this rate — is refuted in §VIII.1. A refuted claim cannot certify a classification: with no count, there is nothing to file as payload. What survives of the Landauer content is structural: $1/16\pi^2$ as a candidate component of the placements in §X, including the candidate identity $16\pi^2 = 8\Omega_4$ with $\Omega_4 = 2\pi^2$ the area of the unit three-sphere; $R_{\text{drag}} = R_K$ pricing the electromagnetic addend of §VIII.4; and the is-ness tax on the interior share of §XI.

---

## VIII. The Control Groups

### VIII.1 The ratio test

If every nucleus bound as $N\times$(one universal rate), then $B/B_d = N/N_d$ and the rate would cancel. The measured ratios are not small-integer ratios. **REFUTED:** binding as count × universal rate.

```python
B = {'t': mpf('8.481798'), '3He': mpf('7.718043'), '4He': mpf('28.295673')}
print([B[n]/B_d for n in ('t', '3He', '4He')])   # 3.8128  3.4695  12.7198
```

### VIII.2 The halo spread

If $1/\pi^2$ were the law of shallow near-threshold states, the halo nuclei would sit near $X = 1$. They spread across it without pausing. **REFUTED:** $1/\pi^2$ as class law. The pion range is the yardstick for two bare nucleons, not for a nucleon bound to a core; every core-bound $X$ below carries that flag.

```python
u = mpf('931.49410')
for name, S, M1, M2 in (('11Be', '0.50164', 10*u, m_n), ('19C', '0.58', 18*u, m_n),
                        ('11Li', '0.3693', 9*u, 2*m_n), ('6He', '0.97546', 4*u, 2*m_n)):
    m = M1*M2/(M1 + M2); print(name, X(sqrt(2*m*mpf(S))/hc, mpc))
# 0.4338   0.5229   0.5744   1.2347   (A·u core masses; two-neutron halos as one cluster)
```

### VIII.3 The two-nucleon sector

The two-nucleon S-wave sector holds four channel instances: $^3S_1$-$np$ and the three $^1S_0$ instances, $nn$, $np$, $pp$. Pauli forces like-nucleon pairs to $T = 1$, and no $T = 1$ two-nucleon state binds. The neutron is not a passenger in the deuteron. It supplies the isospin that opens the only channel with a tensor coupling; remove it and binding does not soften, it becomes impossible.

The three singlet channels have no binding energy but precise scales. A bound pole sits at $k = +i\kappa$, a virtual pole at $k = -i\gamma$: the same imaginary momentum axis, opposite half-planes. Only resonances leave the axis. Solving the effective-range pole equation for each channel:

| Channel | $\kappa$ (fm⁻¹) | $E$ (keV) | $f$ | $\theta$ |
|---|---|---|---|---|
| $^3S_1$-$np$, bound | $+0.2316$ | $2224.6$ | $+0.2031$ | $+44.21°$ |
| $^1S_0$-$np$ | $-0.0399$ | $66.1$ | $-0.0549$ | $-12.53°$ |
| $^1S_0$-$nn$ | $-0.0495$ | $101.7$ | $-0.0681$ | $-15.51°$ |
| $^1S_0$-$pp$ | $-0.0537$ | $119.6$ | $-0.0765$ | $-17.40°$ |

```python
pole = lambda a, r: (1 - sqrt(1 - 2*r/a))/r          # root of 1/a = kappa - r kappa^2/2
theta = lambda f: degrees(2*atan(2*f))
print(k_d, r_t*k_d/2, theta(r_t*k_d/2))              # 0.231606  0.203072  44.2085
for a, r, m in ((-a_np, mpf('2.75'), mu), (-a_nn, mpf('2.75'), m_n/2), (-a_pp, mpf('2.85'), m_p/2)):
    k = pole(a, r); print(k, 1000*(hc*k)**2/(2*m), r*k/2, theta(r*k/2))
# -0.039931  66.12  -0.05490  -12.533 | -0.049536  101.69  -0.06811  -15.515 | -0.053695  119.65  -0.07652  -17.401
```

One channel sits at positive $f$, three at negative $f$, all on one real dial. **ADOPTED:** the signed pole structure is standard scattering theory. The reading that put commitment and holding on orthogonal axes of $S = P + jQ$ is **REFUTED**. What the framework can still use is the $1+3$ sign structure and its geometry: the virtual trio sits just past the unitary point, and the deuteron has sheared furthest from it.

### VIII.4 The mirrors

Each proton-rich mirror of a neutron-rich system binds more weakly, and several are unbound where the neutron side binds ($^6$Be, $^{11}$N, $^{19}$Na). In the two-body channel the pion yardstick covers, $^3$H$\to d+n$ sits at $X = 3.97$ and $^3$He$\to d+p$ at $3.48$. The mirrors with a core ($^8$B/$^8$Li, $^{12}$N/$^{12}$B) are on the uncertified yardstick and are not tabulated here.

```python
m_dt = mpf('1875.612943')
for S, m2 in (('6.257232', m_n), ('5.493477', m_p)):
    m = m_dt*m2/(m_dt + m2); print(X(sqrt(2*m*mpf(S))/hc, mpc))   # 3.9691   3.4814
```

The deficit is the electromagnetic self-hold, the return-leg tax. Estimated as $e^2/r$ at the $^3$He charge radius it gives $0.731$ MeV against the measured $^3$H–$^3$He splitting of $0.764$; the $e^2/r_{\text{rms}}$ form is a convenient choice, and a uniform sphere gives $0.680$. The remaining $\sim 0.05$–$0.08$ MeV is the size of the known nuclear **charge-symmetry breaking**, which comes chiefly from $\rho$–$\omega$ mixing and the neutron–proton mass difference, and also shows in $a_{nn} \neq a_{pp}$. **Charge-independence breaking** — $np$ differing from the like pairs — is a separate effect with a known pion-mass origin: one-pion exchange runs on $m_{\pi^\pm}$ and $m_{\pi^0}$ differently in the two cases. The intra-rung statement is therefore *zero is-ness difference between mirror partners, up to CSB*.

```python
e2 = mpf('1.439964'); rch = mpf('1.970')
R = sqrt(mpf(5)/3)*rch
print(e2/rch, mpf(3)/5*2*e2/R, B['t'] - B['3He'])   # 0.7309   0.6795   0.7638
```

---

## IX. The Curve and Its Singularities

Everything the sector says about bound and virtual states is one object read off the real axis: the **effective-range function**

$$K(k^2) \equiv k\cot\delta(k) = -\frac{1}{a} + \frac{r_e}{2}k^2 + \dots,$$

whose values on the real, positive-energy axis are the measured scattering phase shifts. The amplitude $f = 1/(K - ik)$ has a pole wherever $K = ik$; on the imaginary axis $k = i\kappa$ that is the quadratic $1/a = \kappa - r_e\kappa^2/2$ below. The pole map is this curve continued into complex $k$, and three features of it carry the physics of this file.

**It goes infinite.** At $1/a = 0$ the scattering length diverges and $\cot\delta \to 0$: $\delta = 90°$ at threshold, the amplitude purely imaginary at the unitarity bound. This is the unitary point where binding switches on (§XIV). Its reading as the corpus's $90°$ quadrature landmark — the tangent singularity of `L4-TheNecessaryOpposition`, the infinity of `L4-K4-Infinities` — is a **CANDIDATE** whose derivation is owed elsewhere; this file supplies only the interface where that work will land. It is not the refuted orthogonal-axis $S = P + jQ$ reading, which concerned where bound and virtual poles sit, not the amplitude's phase at one point.

**It is complex.** Bound poles sit on the positive imaginary $k$-axis, virtual poles on the negative; past $f = 1/2$ they leave the axis as a conjugate pair. The real-axis data are one slice of a complex object.

**It branches.** One-pion exchange places a left-hand cut at $k = \pm i\,m_\pi/2$, the nearest singularity of $K$ and the limit of the effective-range expansion's convergence (**ADOPTED**, standard). This is what the pion yardstick *is*: $X$ measures the pole's distance from threshold against the branch point, with a ceiling $X = \pi^2/4 \approx 2.47$ where a pole would sit on the cut, $\kappa = m_\pi/2$. The deuteron pole sits about two-thirds of the way out.

```python
k_cut = mpc/2/hc
print(k_d, k_cut, k_d/k_cut, pi**2/4)   # 0.231606  0.353653  0.654908  2.46740
```

**The pole map.** On the effective-range quadratic $1/a = \kappa - r_e\kappa^2/2$, the regions are fixed by $1/a$:

| Region | Poles |
|---|---|
| $1/a < 0$ | one virtual pole, plus a spurious deep root |
| $1/a = 0$ | **the unitary point**: binding switches on |
| $0 < 1/a < 1/2r_e$ | one bound pole, plus a spurious deep pole |
| $1/a = 1/2r_e$ | the two roots collide, $f = 1/2$ |
| $1/a > 1/2r_e$ | a complex-conjugate pair |

**ADOPTED:** $0 < f < 1/2 \iff a > 2r_e > 0 \iff$ a real bound pole with positive asymptotic normalization. Binding switches on where $1/a$ passes through zero, and the bound-to-virtual path runs through that point. The collision at $f = 1/2$ is a property of truncating the expansion at $r_e$, not a crossing nature makes; for the deuteron the spurious partner sits at $\kappa_2 = 0.909$ fm⁻¹.

```python
print((1 + sqrt(1 - 2*r_t/a_t))/r_t, a_np/mpf('2.75'), a_t/r_t)   # 0.90898   8.633   3.0904
```

**The bend map.** The envelope of `L4-DynamicDistortions301`, $S(\theta) = 2\sqrt{2}\cos\theta$, is a fixed-sides parallelogram draining area to shear: boundary conserved, interior lost. Identify $f = \tfrac12\tan(\theta/2)$. Then the unitary point is the perfect square, $\theta = 0$, $S = 2\sqrt{2}$; the virtual trio sits at $-12.5°$ to $-17.4°$; the deuteron at $+44.21°$, $S = 2.027$, just off the $45°$ equipartition landmark where $S = 2$. **CANDIDATE:** the map is chosen, not derived, and its $45°$ rhyme is the same datum as $\kappa_d a_t$ (§X.2).

```python
f_d = r_t*k_d/2
print(2*sqrt(2)*cos(2*atan(2*f_d)), k_d*a_t, 1/(1 - mpf('0.20710678')))   # 2.02744   1.25512   1.26120
```

---

## X. Five Numbers Near Geometry

Five independent measured quantities land near simple geometric values. Each entry gives the number, its honest band, its renderings, its status and its kill condition. None is an extraction the algebra has emitted; a number being real and an extraction being canonical are two different judgments.

```python
print(k_d*a_s, 4*pi/3)                                 # 4.18797   4.18879
print(k_d*mpf('17.8'), k_d*mpf('18.25'))               # 4.12259   4.22681   band over a_nn in [18.6,18.9], a_pp in [17.0,17.6]
print(1/(k_d*a_s)**2, 9/(16*pi**2))                    # 0.0570155   0.0569932
print(k_d*a_t, 2*pi/5, sqrt(pi/2))                     # 1.25512   1.25664   1.25331
print(a_np/a_s, mpf(3)**0.25, (a_s/a_np)**2, 1/sqrt(3))   # 1.31289   1.31607   0.58016   0.57735
print(B['4He']/B['t'], mpf(10)/3)                      # 3.33605   3.33333
print(B_d/(mu*alpha**2), mpf(800)/9, k_d*(hc/mu)/alpha)   # 88.9850   88.8889   13.3405
```

**X.1 Singlet placement.** $\kappa_d|a_s| = 4.1880$ against $4\pi/3 = 4.1888$ — $0.02\%$ on the geometric mean, inside a band of $4.123$–$4.227$ ($-1.6\%$ to $+0.9\%$) over the measured ranges. **Consistent, unresolved below about one percent.** Rendering: $X_{\text{pair}}/X_d = (3/4\pi)^2 = 9/16\pi^2$, the same datum squared. The relation is leading-order in the singlet's range expansion: pairing $\kappa_d$ with the virtual poles instead of the lengths displaces it by $7\%$. Pedigree: the target $4\pi/3$ was named on geometric grounds before the product was formed, with its location in the singlet table unspecified. **OPEN VOTE.** Kill: a precision $a_{nn}$ that moves the product outside $\pm0.3\%$, or a derivation that emits a different coefficient.

**X.2 Triplet placement.** $\kappa_d a_t = 1.2551$ against $2\pi/5 = 1.2566$ ($0.12\%$). At shape-independent order $\kappa_d a_t = 1/(1-f)$, so this is the same datum as $f = 1 - 5/2\pi$ ($0.57\%$), the "one-fifth interior," and the $45°$ bend-map rhyme. The fifth has a corpus reading: the centroid, the fifth point that `L3-K4-to-K5-via-AC-Extension` §II seats at $\omega$ — one fifth of the bookkeeping held at the centroid, the other four fifths in the actuating drives. That reading is a **CANDIDATE**, named after the match. Co-registered: $\sqrt{\pi/2}$ ($0.14\%$, other side) and $5/4$ ($0.41\%$). The value cannot choose among them. **OPEN VOTE.** Kill: a derivation that emits one of the three, or none.

**X.3 Mixed-channel suppression.** $|a_{np}|/a_s = 1.3129$ against $3^{1/4} = 1.3161$ ($0.24\%$); rendering $X_{np}/X_{\text{pair}} = 1/\sqrt3$ ($0.49\%$). The difference between $np$ and the like pairs is charge-independence breaking, which has a known pion-mass mechanism and is amplified by the near-unitarity of the singlet: a percent in the force moves $a$ by about ten. **OPEN VOTE**, and before it carries weight the $3^{1/4}$ must reproduce the pion-mass mechanism's size or explain why it need not. Kill: the standard CIB calculation accounts for the ratio without remainder.

**X.4 Alpha over triton.** $B_\alpha/B_t = 3.3361$ against $10/3$ ($0.08\%$). Along the Tjon line $B_\alpha$ is a universal function of $B_t$, and leading-order pionless effective field theory carries several percent of uncertainty on $B_\alpha$. A $0.08\%$ offset cannot be resolved against that band. **CANDIDATE**: within the universality band, not evidence beyond it. The rhyme does not continue up the alpha ladder ($B(^{12}\text{C})/B(^4\text{He}) = 3.257$, $B(^{16}\text{O})/B(^{12}\text{C}) = 1.385$).

**X.5 The binding form.** $B_d/\mu c^2\alpha^2 = 88.985$ against $800/9$ ($0.11\%$), with the renderings $\kappa_d\lambda_\mu = (40/3)\alpha$ and, through the clock equation $\omega = k/(Rr)$ of `L3-ConstitutiveElastance` §III at $\omega = B_d/\hbar$ and $r = 1/\kappa_d$, $R_d/R_K = 3/10$ (both $0.054\%$). These are one datum asserting $B_d \propto \alpha^2$. **REFUTED as structure.** Realistic nuclear forces with electromagnetism switched off bind the deuteron at about $2.2$ MeV; electromagnetic corrections to its binding are small against that — keV to tens of keV, depending on whether the pion-mass splitting is counted with them. A binding that vanishes with $\alpha$ is excluded. What the form does show is that $B_d/\mu c^2$ is small, and that smallness is the nucleon-to-pion hierarchy of §XIV, not the unitarity fine-tuning. **CANDIDATE as coincidence**, and the corpus's first cheap, existing, empirical falsifier.

**The chance baseline.** Against a target family of $(p/q)\pi^k$, $p, q \le 10$, $k \in \{-2,\dots,2\}$, with square roots and $1-x$ forms — $747$ targets — a quantity drawn log-uniformly over $[0.05, 20]$ lands within $0.2\%$ of some target $36.5\%$ of the time. Four of the five tabled quantities land within $0.2\%$. The chance of that is about $6\%$: suggestive, not significant, and a lower bound on the chance explanation, because the targets actually used were chosen after the fact from a richer family. $B_\alpha/B_{^3\text{He}} = 3.6662$ sits $0.014\%$ from $11/3$, and is kept out of the table, for the same reason.

```python
from mpmath import binomial
p = mpf('0.365'); print(sum(binomial(5, k)*p**k*(1 - p)**(5 - k) for k in (4, 5)))   # 0.06283
print(B['4He']/B['3He'], mpf(11)/3)                                               # 3.66617   3.66667
```

---

## XI. The Asymptotic Face and the Interior

In position space the bound pole of §IX appears as an asymptote: outside the force's range $\psi \propto e^{-\kappa r}/r$, fixed by $\kappa$ and one normalization (the ANC), carrying nothing of the short-range character. This is the pole's image at distance — the state's **asymptotic face**, the boundary the outside reads (its Markov blanket in the corpus's sense, the K3 boundary that constitutes an interior), the only part the world can touch, and what the physics literature calls the state's *tail*. The **interior** is everything the force adds at short range, between that face and the branch point. Effective-range theory is the bookkeeping of how far the interior bends the asymptote-only description, and $f$ is that bend.

Three quantities stay separate. The **dial**, $f \approx 0.2$, is the interior's share of the bookkeeping. The **norm** is where the probability sits: the deuteron holds roughly a third of its norm inside $2$ fm, so it is only mildly halo-like in substance. The **watermark** is the interior's trace on the face.

Face-dominated observables: binding momentum, rms radius, asymptotic normalization, photodissociation, $\eta$. Interior-dominated: $Q_d$, the magnetic moment, $P_D$. And the one that joins them: **the interior writes its signature onto the face.** $\eta$ is a short-range twist readable at infinite distance.

A bound state's asymptote $e^{-\kappa r}$ reaches outward, its public extent. A virtual state's is $e^{+\gamma r}$, growing and never normalizable — it never materializes as a bound state, though its pole is real in its effects: it is why $a_{np} = -23.7$ fm. A resonance's is complex, reaching and oscillating at once. The class formula was always a statement about the face; the signature is the interior's correction to it.

**ADOPTED:** the asymptote, the interior, the ANC and $\eta$ are standard. The one commit in the sector is the binding itself — the mass defect $B_d$, the energy written out of the system when the pole switched on; the asymptote of the resulting stationary state is not committed, being reversible and un-erased. **CANDIDATE** in the framework's reading: the asymptotic face as the state's interface, the interior as held structure, $\eta$ as the interior's signature on the face, the is-ness tax as paid on the interior. Kill: an observable that separates this signature reading of $\eta$ from the plain tensor-admixture reading.

---

## XII. The Layer Sort

Each excess sorts into the three-layer machinery of `On_TheIsNessTax` once:

- **Intra-rung is-ness ($\alpha^0$):** the deuteron's signature, the interior's holding cost; zero between mirror partners up to CSB.
- **Return-leg re-holding ($\alpha^{+1}$):** the mirror addend, the electromagnetic self-hold, priced by $R_{\text{drag}} = R_K$; and the pion-choice width of §IV, the same return-leg visible in the mediator.
- **$\alpha^0$ placements:** $4\pi/3$, $2\pi/5$, $3^{1/4}$ — geometry, $\alpha$-free.

The two trinities of `L3-TheAtomOfSpace` §VI are orthogonal and are sorted separately: the **bimedian trinity** says which kind of crossing, the **impedance trinity** what happens within it. The singlet trio's $2+1$ structure — two pure-charge channels on one placement, the mixed channel suppressed — is an impedance-plane fact. Assigning $nn$, $pp$, $np$ to Cardinal, Mutable and Fixed is a bimedian hypothesis that waits on the $p/n$ pole assignments, and no single test may mix the two levels.

---

## XIII. The Census

A table assembled after the data were in hand is a sample, not a canon. About sixty-five bound systems exist below $A = 20$.

**Pre-registered census:** every system with $A \le 20$ and any of $S_n$, $S_p$, $S_{2n}$, $S_{2p}$ below $B_d = 2.2246$ MeV. **Firm on present values, nineteen:** $^6$He, $^8$He, $^8$Li, $^9$Be, $^{11}$Be, $^{11}$Li, $^{14}$B, $^{14}$Be, $^{15}$C, $^{17}$B, $^{17}$C, $^{19}$C on the neutron side; $^8$B, $^9$C, $^{12}$N, $^{13}$N, $^{13}$O, $^{17}$F, $^{17}$Ne on the proton side. **At the edge or poorly known:** $^{20}$Na ($S_p \approx 2.19$), $^{20}$N, $^{19}$B, $^{20}$C, $^{20}$Mg. Not members: $^{15}$B ($S_n = 2.78$); $^{22}$C, $^{23}$Al, $^{24}$F and $^{26}$P, which lie outside $A \le 20$. The roster is fixed by an AME2020 pass. The count falls where it falls; the criterion is not re-tuned. One member is stable: $^9$Be, at $S_n = 1.67$ MeV, is shallower than the deuteron ($B_d = 2.22$ MeV).

Every census entry with a core is computed on the uncertified pion yardstick. Its $X$ is a recorded coordinate, not a class membership. On the yardstick's own ground, the committed two-body channel is alone.

---

## XIV. Two Hierarchies, One Fine-Tuning

What remains, once universality has absorbed what it can, is two separate facts that must stay separate because they answer different questions.

**Near-unitarity.** The singlet is strongly fine-tuned, $|a_{np}|/r_{np} \approx 8.6$, its virtual pole at $66$ keV. The triplet is moderately so, $a_t/r_t \approx 3.1$, with $\kappa_d/m_\pi \approx 1/3$. This is why the deuteron is large against the force's range, why the halo class exists, and why the near-threshold yardstick measures anything at all. The singlet sits close to the unitary point; the triplet sits moderately near it.

**The nucleon-to-pion hierarchy.** $m_N/m_\pi \approx 6.7$ is why $B/m_N$ is small: the mediator is light, a fact of the chiral hierarchy. It is the missing rung of §VI, and folding it into the unitarity story would hide it.

Universality absorbs $B_\alpha/B_t$. It does not touch $\kappa_d|a_s|$ or $\kappa_d a_t$, which remain open votes.

The question this leaves standing is the corpus's own: **why does the nuclear rung sit near the unitary point?** At unitarity the two-body sector is scale-invariant. The three-body sector is not: Efimov physics breaks continuous scale invariance down to **discrete** scale invariance with factor $e^{\pi/s_0} \approx 22.7$ — a limit cycle, not a fixed point. The corpus's rungs and ratchets are discrete too. So the sharper form of the question is: **does the $K_4$ rung structure produce a discrete scale factor, and is it this one?**

---

## XV. The Pre-Registered Program

**The lead target is an equation, not a number.** $s_0$ is the root of the three-body equation at unitarity,

$$s_0\cosh\frac{\pi s_0}{2} = \frac{8}{\sqrt3}\sinh\frac{\pi s_0}{6}, \qquad s_0 = 1.0062378, \qquad e^{\pi/s_0} = 22.6944,$$

the same value for the triton channel in the spin-isospin-symmetric limit. The test is whether the $K_4\to K_5$ machinery produces this functional form. It cannot be fitted after the fact, and it is checkable to any precision.

```python
from mpmath import findroot
s0 = findroot(lambda s: s*cosh(pi*s/2) - 8/sqrt(3)*sinh(pi*s/6), 1)
print(s0, s0*cosh(pi*s0/2), 8/sqrt(3)*sinh(pi*s0/6), exp(pi/s0))   # 1.0062378   2.5476415   2.5476415   22.69438
```

Its nuclear check is not a spectrum. The Efimov ladder has never been seen in nuclei — only the $A = 3$ ground states, $^3$H and its mirror $^3$He, exist. What nuclear data show is the **Phillips line**, the correlation between the triton's binding and the neutron–deuteron doublet scattering length. A derivation that emits the Efimov equation is checked against the Phillips line.

**Frozen target set.** Targets not yet computed by the framework, fixed here:

1. The Efimov equation, and with it $s_0$ and $e^{\pi/s_0}$.
2. $m_p/m_{\pi^\pm} = 6.7226$, the missing rung, within $1\%$.
3. $m_p/m_e = 1836.1527$, within $1\%$.

Targets 2 and 3 are linked: $m_p/m_e = (m_p/m_\pi)(m_\pi/m_e)$, and $m_\pi/m_e$ is the Laurent of §VI. A derivation that hits target 2 delivers target 3 at the Laurent's $2.84$ ppm, and that double hit counts once. Target 3 reached directly, without target 2, counts on its own and tests the Laurent's extension to the hadronic rung.

Values already matched after the fact — $4\pi/3$, $2\pi/5$, $3^{1/4}$, $10/3$, $3/10$ — are not targets. Their remaining life is a derivation. Fitted outputs, such as the Tjon-line or Phillips-line parameters, are not constants and stay out.

**Frozen derivation rules.** Matching a known equation can be steered. Before each attempt, its file header records the operators used, the $K_4\to K_5$ identifications, and the boundary condition. Only then is anything computed. A result that appears under rules fixed in advance counts.

**Kill rule.** Each attempt under fixed rules is one cycle. A cycle that lands no frozen target within its band weakens the slots hypothesis; three empty cycles retire it, and the fine-tuning of §XIV stands as fine-tuning. Any match is quoted alongside its chance rate: a $1\%$ band over a few targets is hit by chance at the per-draw rates of §X.

### What the slots hypothesis can claim

The hypothesis says the near-coincidences of §X are wells in the sector's parameter space — places where independent approaches fall because something can be there — rather than chance alignments. It comes in two strengths, and only one of them is open.

**The weak form is adopted physics.** Both two-nucleon S-waves sit a few range-lengths from threshold at once. The triplet length is $1.55$ times the minimum $2r_t$ any bound state needs; the binding is $0.16$ of the range scale $\hbar^2/2\mu r_t^2 = 13.5$ MeV; the singlet's $|a_{np}|/r_{np}$ is $8.6$. That window is where bound states can exist, and it is why the tabled quantities are of order one. It does not say why any of them would be $4\pi/3$ rather than $4.1$ or $4.3$.

**The strong form — geometric values inside the window — is what the program tests.** Three constraints bound it.

- *Readings are not derivations.* Every route to the deuteron in this file consumes the nuclear rung's own measured magnitudes — $B_d$, $a_t$, $r_t$, $a_s$ — structural load in the sense of the import test. A derivation takes its inputs from another rung and produces the curve's singularity structure of §IX: where it goes infinite, where it branches, where its poles sit. Lattice QCD is of that kind, computing two-nucleon binding from quark masses. The $K_4 \to K_5$ attempt must be too: it may import what §VI's ladder already runs on — $\alpha$, $\pi$, integers, the colour count — and nothing measured at the nuclear rung.
- *The deuteron does not attract hits.* Every ratio of the sector's lengths, filtered to those measured finely enough to resolve the tolerance and scored against the frozen family with its local density, hits at the chance rate whether or not the deuteron is in the pair. The table's deuteron-centred look came from where the search started.
- *A well should have width.* A relation that is structural should survive a neighbourhood of the physical point. The robustness test for X.1 is the pion-mass sweep of $\kappa_d|a_s|$ through chiral-EFT and lattice extrapolations, its band set against those extrapolations' own errors before the pion-mass dependence is read. This tests an existing open vote; it is not a frozen target.

```python
import math, itertools, bisect, random
fam = set()
for p in range(1, 11):
    for q in range(1, 11):
        for kk in (-2, -1, 0, 1, 2):
            v = p/q*math.pi**kk; fam.add(v); fam.add(math.sqrt(v))
            if v < 1: fam.add(1 - v)
fam = sorted(x for x in fam if .01 < x < 100)
near = lambda x: min(abs(fam[j]/x - 1) for j in (bisect.bisect(fam, x) - 1, bisect.bisect(fam, x)) if 0 <= j < len(fam))
random.seed(5)
local = lambda x, t: sum(near(x*math.exp(random.uniform(-.26, .26))) < t for _ in range(4000))/4000
hcf, mpf_, muf = float(hc), float(mpc), float(mu)
lengths = {'R_d': (1/float(k_d), 1e-6), 'a_t': (5.4192, 2e-4), 'r_t': (1.7536, 1.4e-3), 'a_np': (23.74, 8e-4),
           'a_s': (float(a_s), 1.3e-2), 'r_np': (2.75, 1.8e-2), 'lam_pi': (hcf/mpf_, 1e-6), 'lam_mu': (hcf/muf, 1e-8),
           'r_p': (0.8409, 5e-4), 'r_d': (2.12799, 3.5e-4)}            # value fm, relative 1-sigma
for with_d in (True, False):
    n = hits = expd = 0
    for (a, (v1, s1)), (b, (v2, s2)) in itertools.combinations(lengths.items(), 2):
        if ('R_d' in (a, b)) != with_d or math.hypot(s1, s2) > 0.001: continue
        x = max(v1, v2)/min(v1, v2); n += 1; hits += near(x) < 0.001; expd += local(x, 0.001)
    print(with_d, n, hits, round(expd, 2))     # True 6 2 1.2  |  False 15 3 2.54   (0.1%: both at chance)
```

**The soft point is the slot's precise mainstream definition.** Braaten and Hammer conjectured that at a pion mass somewhat above the physical value both two-nucleon scattering lengths diverge together, putting the three-body sector exactly on the Efimov limit cycle. If so, the double-sided window is the physical world sitting near one special point of parameter space, and "a place where things can be" has an address. Its residue ratio is not a new target: to leading order it is the physical $|a_s|/a_t$, already the derived consequence of X.1 and X.2.

**The bet is asymmetric.** `L4-TheSubstrateRatchet` lists dimensionless ratios, the proton-to-electron mass ratio among them, as substrate-owned; §VI and this program have the algebra emitting one and aiming at the next. Three empty cycles weaken the slots hypothesis; they do not establish substrate ownership, which only the Ratchet's AC phase-angle test can show. A hit on target 2 forces the opposite repair: the scope rule needs a codified exception where the geometry reaches a rung. The corpus cannot hold both files' present claims indefinitely, and this program is what decides between them.

---

## XVI. Claims Sort

**ADOPTED** (standard physics, used here): the deuteron as the only bound two-nucleon state; the effective-range function and its singularity structure of §IX — the signed pole map, the unitary-point divergence, the one-pion left-hand cut; $0 < f < 1/2$ as the positive-normalization condition; the asymptote, interior, ANC and $\eta$; CSB and CIB as separate effects.

**LANDED:** the import test and the liberation pattern, with the cosmological and impedance instances corrected. Assimilate-first. The two refutations of §VIII.1–2. The convention audit of §II and the pion-choice Layer 3 band of §IV. The identification of the mass defect $B_d$ as the sector's one committed quantity.

**OPEN VOTE:** the table's three geometric placements — $\kappa_d|a_s| = 4\pi/3$, $\kappa_d a_t = 2\pi/5$ (co-registered with $\sqrt{\pi/2}$ and $5/4$), $|a_{np}|/a_s = 3^{1/4}$. The interior signature as $P_D$. The pion-to-electron Laurent (rank per `L3-ConstitutiveAlpha`).

**CANDIDATE:** $B_\alpha/B_t = 10/3$, within the universality band. The bend map $f = \tfrac12\tan(\theta/2)$. $16\pi^2 = 8\Omega_4$ as the source of the phase-burn factor. $B_d \propto \alpha^2$ as coincidence. The asymptotic face as interface, the interior as held structure, $\eta$ its signature (§XI). The unitary point as the curve's $90°$ quadrature infinity (§IX), its derivation owed elsewhere.

**REFUTED:** $1/\pi^2$ as class law. Binding as count × universal rate. $B_d \propto \alpha^2$ as structure. The orthogonal-axis $S = P + jQ$ reading of bound and virtual states. $f = 1/2$ as a physical crossing. The exact $\ell_P/R_H$ and $120\pi$ identities.

**INTERFACE:** $T_c$. $I_0$. The isotope counts, which no longer have a claim to serve.

**Owed:** a derivation of any frozen target, the Efimov equation first; $m_N/m_\pi$; the bimedian reading of the singlet trio after the $p/n$ pole assignments; the precision $a_{nn}$ that decides X.1; the AME2020 census; and what executes at the unitary point where binding switches on — the commit-or-hold question, now aimed where the physics puts it.

---

## XVII. What Reading This Back Should Leave

The deuteron was a fence made of MeV. On the far side there is no number a breath above a geometric point waiting to be read. There is one bound channel among four, sheared away from the unitary point while its three uncommitted siblings stay just past it; a binding that needs the nucleon-to-pion ratio the corpus has not yet earned; five measured numbers near simple geometry, at a rate chance can reach; and one fine-tuning, near-unitarity, with a name and no reason.

That is the better place to stand. Every open item has an address. The deepest one is aimed at the corpus's own thesis: if scale structure is native to the plenum, then the discrete scale factor of the three-body problem at unitarity is a number the algebra should produce, under rules fixed before it tries.

Name every import. Sort it. Fix the target before you look. And take the scaffold down only where the pure number stands without it.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.

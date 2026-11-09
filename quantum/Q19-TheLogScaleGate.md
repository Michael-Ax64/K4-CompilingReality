# Q19-TheLogScaleGate
## The Transcendental Gate as a Boundary Matching Condition on the Cylinder

*Quantum register. **Permanent replacement for `Q19-TheTranscendentalGate`.** Reads with `L3-K4-to-K5-via-AC-Extension`, `L4-ThePlenum`, `L7-ExIncoherenteChargeTransfer`, `Q4-OpenExhaust`, `Meta-MechanismOfTransition`, `ProofN_BiquaternionBridge`, `Q1-GenerationsOfMatter`.*

---

## §0. Epistemic Register and Executive Summary

### 0.1 What Pass 1 did, and why it is retired

Pass 1 treated the Efimov transcendental equation

$$s_0\cosh\frac{\pi s_0}{2} = \frac{8}{\sqrt3}\sinh\frac{\pi s_0}{6}$$

as a target for ring arithmetic: hunt $8/\sqrt3$ and $\pi/6$ in closed form, quote a residual, key claims to $f(1)$ and $f'(1)$. Every part of that programme is retired, and §V.1 states the retirements with their arithmetic. The short version: the two constants were never independent, the quoted residual was below the precision of its own input, and the quantities the search was keyed to are not invariants of the equation.

### 0.2 What the gate is

**The gate is the boundary matching condition of a uniform lossless transmission line on the log-scale axis $u = \ln R$, whose natural domain is the cylinder $\mathbb{C}/2\pi i\mathbb{Z}$.**

In that reading, every element has an address:

| element | what it is |
|---|---|
| $s_0$ | propagation wavenumber of a lossless line in $u = \ln R$ |
| $e^{\pi/s_0}$ | half-wavelength step on the $u$-axis |
| $\theta$ | the mass geometry, through $\sin\theta = \sqrt{\mu_{\text{pair}}/\mu_{\text{spec}}}$ |
| $8/\sqrt3$, $\pi/6$ | $\frac{2\lambda}{\sin2\theta}$ and $\frac\pi2-\theta$ at $\theta=\pi/3$, $\lambda=2$ |
| $\lambda$ | symmetric-mode eigenvalue of the $K_n$ channel graph, $=n-1$ |
| $a$ (scattering length) | a load reactance, $X_L/Z_0 = -1/(ka)$ |
| $1/a = 0$ | zero load reactance — a short, $\Gamma=-1$, scale-free |
| $k\to i\kappa$ | continuation to the bound-state sheet; reactive power becomes real |
| $\kappa_*$ | the load reflection **phase** at $u\to-\infty$ — outside the gate, by construction |

### 0.3 The unified gate, one equation

$$\boxed{\;\lambda \cdot T_\theta(i s_0) \;=\; \pi \sin 2\theta\;}, \qquad T_\theta(s) = \frac{2\pi\sin\!\left(s\left(\frac\pi2-\theta\right)\right)}{s\,\cos\frac{\pi s}{2}}$$

Proved as an identity (§I.3), and verified across mass ratios *and* across $\lambda$ to $\sim10^{-31}$ (§IV.4). Three identical bosons are $\lambda=2$, $\theta=\pi/3$.

### 0.4 Route C, and what it cost

Route C — the mass-ratio falsification harness — was run against published benchmarks obtained from the literature rather than reconstructed, because a harness graded against one's own memory is not a harness. **It passed**, with one residual flagged (§IV.2).

It also reversed two of this work's own earlier verdicts, in the direction of restoring a claim that had been killed. §IV.5 states both reversals. The short version: tested at one mass ratio, two different errors were invisible; tested across the curve, both surfaced.

All arithmetic at `mp.dps = 40`. Residuals stated throughout.

---

## §I. The One-Angle Family and the Cylinder Locale

### I.1 The family, with the channel count carried explicitly

$$s\cosh\frac{\pi s}{2} \;=\; \frac{2\lambda}{\sin 2\theta}\,\sinh\!\left(s\,\nu\right), \qquad \nu = \frac\pi2 - \theta$$

**$\lambda$ is a graph eigenvalue.** $n$ resonant pairs give $n$ Faddeev channels, each coupled to the others; the coupling matrix is the adjacency of $K_n$, and the symmetric mode is its top eigenvalue:

| channels $n$ | $K_n$ adjacency spectrum | $\lambda$ |
|---|---|---|
| 2 | $\{+1, -1\}$ | **1** |
| 3 | $\{+2, -1, -1\}$ | **2** |
| 4 | $\{+3, -1, -1, -1\}$ | **3** |

$\lambda = n-1$. Three identical bosons resonate in all three pairs, so $\lambda = 2$. A 2+1 system with $a_{MM}=0$ resonates only in the two heavy–light pairs, so $\lambda = 1$.

**$\theta$ is the mass geometry.** With heavy mass $M$ (twice) and light mass $m$:

$$\sin\nu = \frac{M}{M+m} \quad\Longleftrightarrow\quad \sin\theta = \frac{\sqrt{m\,M_{\text{tot}}}}{M+m} = \sqrt{\frac{\mu_{Mm}}{\mu_{(Mm),M}}}, \qquad M_{\text{tot}} = 2M+m$$

The two published constants are then emitted by one substitution:

```python
from mpmath import mp, mpf, pi, sqrt, sin, cos, asin, sinh, cosh, exp, findroot
mp.dps = 40
theta_of = lambda M, m: pi/2 - asin(M/(M+m))
t = theta_of(mpf(1), mpf(1))
print(t, pi/3)                  # 1.047197551196598  1.047197551196598
print(2*2/sin(2*t), 8/sqrt(3))  # 4.618802153517006  4.618802153517006
print(pi/2 - t, pi/6)           # 0.5235987755982989 0.5235987755982989
```

Equal masses give $\theta = \pi/3$ to $2\times10^{-41}$, and the prefactor at $\lambda=2$ is $8/\sqrt3$ exactly.

**A caution carried forward.** The prefactor was first guessed as $4/\sin\theta$, which agrees with $8/\sqrt3$ at $\theta=\pi/3$ *only* because $\cos\frac\pi3=\frac12$. A percent-level near-miss of this kind is caught by consulting the literature's 2+1 form, not by one's own table.

### I.2 The root, and the real uniqueness argument

Writing the gate in **ratio form** — root $\iff u(s)=1$ with $u(s) = \frac{2\lambda}{\sin2\theta}\frac{\sinh(s\nu)}{s\cosh(\pi s/2)}$ — is what makes uniqueness provable rather than asserted. On $(0,\infty)$ at $\theta=\pi/3$:

$$(\ln u)' = \frac{\pi}{6}\!\left[\coth y - \frac1y\right] - \frac{\pi}{2}\tanh\frac{\pi s}{2} < 0, \qquad y = \frac{\pi s}{6}$$

so $u$ is strictly decreasing; with $u(0^+)>1$ there is exactly one root. The difference form carries a spurious root at $s=0$ and no monotonicity, which is why it should not be the published form. (It also traps naive root-finders: a bisection on the ratio form is the correct numerical procedure.)

```python
def u(s, th, lam): return (2*lam/sin(2*th))*sinh(s*(pi/2-th))/(s*cosh(pi*s/2))
s0 = findroot(lambda s: u(s, pi/3, 2) - 1, (mpf('1e-25'), mpf(4)), solver='bisect')
print(s0, exp(pi/s0))   # 1.006237825102781   22.6943825954
```

Published: $s_0 = 1.00623782510278$, scaling $22.6943826$.

### I.3 The matching condition, and its two-line proof

**Claim.** At the family root, $\lambda\,T_\theta(is_0) = \pi\sin2\theta$, for every $\theta$ and every $\lambda$.

**Proof.** Rewrite the family as $\sinh(s\nu) = \dfrac{s\cosh\frac{\pi s}{2}\,\sin2\theta}{2\lambda}$. Continue $T$ to $s=is_0$, where $\sin(ix)=i\sinh x$ and $\cos\frac{\pi i s_0}{2}=\cosh\frac{\pi s_0}{2}$, so the two $i$'s cancel:

$$T_\theta(is_0) = \frac{2\pi\sinh(s_0\nu)}{s_0\cosh\frac{\pi s_0}{2}}$$

Substitute. The factor $s_0\cosh\frac{\pi s_0}{2}$ cancels **entirely**:

$$T_\theta(is_0) = 2\pi\cdot\frac{\sin2\theta}{2\lambda} = \frac{\pi\sin2\theta}{\lambda} \qquad\blacksquare$$

**So the matching condition is not a new fact about the gate. It is the gate, restated in transfer-function form.** The content of the restatement is that the right-hand side becomes bare trigonometry in the mass angle, with the entire transcendental structure absorbed into the left. At $\lambda=2$ it reads $T_\theta(is_0) = \frac\pi2\sin2\theta$; at $\theta=\pi/3$ that is $\frac{\sqrt3\,\pi}{4} = 1.3603495231756634$, a number obtained three independent ways in an earlier pass.

### I.4 The kernel is a neutral four-charge Green's function on the cylinder

$$K_\theta(u) = \ln\frac{\cosh u + \cos\theta}{\cosh u - \cos\theta}$$

**The locale.** $K_\theta$ is $2\pi i$-periodic, so its domain is not the plane but the cylinder $\mathbb{C}/2\pi i\mathbb{Z}$ (residuals $\sim10^{-52}$ at three test points).

**The charges.** The log branch points in one period strip, with signs:

| source | location at $\theta=\pi/3$ | charge |
|---|---|---|
| $\cosh u = \cos\theta$ | $u = \pm i\theta = \pm 1.0471975512\,i$ | $-1$ |
| $\cosh u = -\cos\theta$ | $u = \pm i(\pi-\theta) = \pm 2.0943951024\,i$ | $+1$ |

$$\sum q = 0, \qquad \sum q\,z = 0, \qquad \sum q\,z^2 = -6.57973626739 \neq 0$$

Monopole and dipole both vanish; the leading moment is the **quadrupole**. Since $\ln|f|$ is harmonic wherever $f$ is analytic and non-zero, $K_\theta$ is the two-dimensional Coulomb Green's function of exactly this neutral four-charge set. **The zeros of $T_\theta$ are the charge positions on the phase circle**, and they move with $\theta$ — the mass geometry is literally where the charges sit.

**The normalisation follows from the count and the circumference, with nothing inserted:**

$$\frac{2}{\pi} = \frac{4}{2\pi} = 0.6366197723675813$$

**The anti-periodic half-modes.** Under a *half* period $u\to u+\pi i$, $\cosh(u+\pi i) = -\cosh u$ inverts the kernel's argument, so

$$K_\theta(u+\pi i) = -K_\theta(u)$$

(residuals $\sim10^{-51}$). $K_\theta$ is periodic under the full period and **anti-periodic under the half period**. This is the structural reason the transfer function's poles sit at **odd** $s$: $\cos\frac{\pi s}{2}=0$ selects exactly the half-period anti-periodic modes and nothing else. The odd-integer pole ladder is not a property of the formula — it is the mode content of the locale.

### I.5 The $T_3$ cubic is the integer pole–zero spacing ratio $n=3$

$T_\theta$ has poles at odd integers (**spacing 2**) and zeros at $s = n\pi/\nu$ (**spacing $\pi/\nu$**). The ratio:

$$\frac{\text{zero spacing}}{\text{pole spacing}} = \frac{\pi}{\pi-2\theta}$$

This is an integer $n$ exactly when $\theta = \frac\pi2\left(1-\frac1n\right)$:

| $n$ | $\theta$ | zero spacing | pole spacing | ratio |
|---|---|---|---|---|
| 1 | $0$ | 2 | 2 | 1 |
| 2 | $\pi/4$ | 4 | 2 | 2 |
| **3** | $\boldsymbol{\pi/3}$ | **6** | **2** | **3** |
| 4 | $3\pi/8$ | 8 | 2 | 4 |
| 6 | $5\pi/12$ | 12 | 2 | 6 |

**The equal-mass angle is the $n=3$ member of the integer-spacing family.** The cubic follows and is not independent: put $x = \pi s/6$, so $\frac{\pi s}{2}=3x$ and $T_{\pi/3}(s) = 2\pi\sin x/(s\cos 3x)$, with the pole polynomial the third Chebyshev relation

$$\cos 3x = 4\cos^3x - 3\cos x = T_3(\cos x)$$

verified against `mpmath.chebyt(3, cos(x))` at four points to 50 digits. **The "$T_3$ cubic" is the triple-angle identity, present because the spacing ratio is 3.**

---

## §II. The Physical and Metrological Bridge

### II.1 The uniform lossless line in $u = \ln R$

On the log-scale axis the anomaly's solutions are $R^{\pm is_0} = e^{\pm is_0u}$: propagation constant $\gamma = is_0$, **purely imaginary**, hence a lossless line of wavenumber $s_0$. The log-period is $\pi/s_0 = 3.12211743110422$ and the scale factor $e^{\pi/s_0} = 22.6943825954$ is one half-wavelength on the $u$-axis.

Two consecutive Efimov rungs differ by one half-wavelength in $\ln R$. That is what a standing wave on a lossless line does, and it is why the tower is geometric rather than arithmetic: a geometric tower in $R$ is an arithmetic tower in $\ln R$.

### II.2 The scattering length is a reactance

$$\frac{X_L}{Z_0} = \cot\delta = -\frac{1}{ka}$$

| $a$ | $X_L/Z_0$ | $\delta$ | dimer? |
|---|---|---|---|
| −1.0 | +1.0 | 45° | no |
| −100 | +0.01 | 89.427° | no |
| $\pm\infty$ | **0** | **90°** | **threshold** |
| +100 | −0.01 | 90.573° | yes |
| +1.0 | −1.0 | 135° | yes |

Four statements coincide at the middle row, and the coincidence is the content:

$$\frac1a = 0 \iff X_L = 0 \iff \delta = \frac\pi2 \iff \Gamma = -1$$

Zero load reactance is a **short**: total reflection, nothing absorbed, no scale minted. This is the unitary limit, and it is scale-free because a short has no length in it.

It is also the point `Meta-MechanismOfTransition` §II–III describes, and the match is exact rather than suggestive. The interior readout $\tan\delta = -ka$ **diverges** at $\delta=\pi/2$. And $a\to-\infty$ and $a\to+\infty$ are *one point*, $1/a=0$ — the projective identification of the two infinities, which is physical rather than decorative: in the laboratory it is the centre of a Feshbach resonance, approached from both sides, and the two sides are the same resonance.

### II.3 The scale-free resonance and the radiansphere

The same condition in the medium's variables is $\omega\ell = c$, i.e. $k\ell = 1$. Evaluating `L4-ThePlenum` §II.4's reactances separately at its own resonance condition $\omega_0 = c/r$:

| $r$ (m) | $\omega\mu_0r$ | $1/(\omega\epsilon_0 r)$ |
|---|---|---|
| $10^{-10}$ | 376.7303134 | 376.7303134 |
| $10^{-15}$ | 376.7303134 | 376.7303134 |
| 1.0 | 376.7303134 | 376.7303134 |

Both equal $Z_0$ at every radius, because $\omega_0 = c/r$ is $kr=1$ — the **radiansphere** (Wheeler 1959), where an antenna's stored reactive and radiated energy cross over. The file derives the condition and does not name it; naming it converts an asserted operating point into one with an independent textbook warrant.

**Rest mass as detuning off the reflecting boundary.** A purely reactive termination has $|\Gamma|=1$ identically. The four $K_4$ poles carry dissipation and so sit strictly inside the Smith chart; the scale-free short sits on its boundary. The bounded frame's distance from that boundary is $\alpha$-sized:

$$1 - |\Gamma_{\text{frame}}| = \frac{4\alpha}{1+2\alpha} = 0.028769527487, \qquad \frac{R_K}{Z_0} = \frac{1}{2\alpha} = 68.5179995885$$

A frame's rest mass is its detuning off a perfectly reflecting boundary, and $\alpha$ is the size of the detuning. On the Efimov side the same statement reads: discrete scale invariance is exact only at the unitary point, and any finite detuning truncates the tower.

### II.4 The bound-state sheet

Continue $k\to i\kappa$. The load, reactive on the real-$k$ axis, becomes **real**: $Z_L/Z_0 = -1/(\kappa a)$, equal to $-1$ at $\kappa a = 1$, which is a pole of $\Gamma$.

In the dictionary $Z_L/Z_0 = j\cot\delta$, so $Z_L+Z_0=0 \iff \cot\delta = i$ — the textbook $S$-matrix pole condition, carrying **no zero-range assumption**. It therefore reproduces the bound state at every order of the effective-range expansion:

| $r_e/a$ | $\kappa a$ from $Z_L=-Z_0$ | $\kappa a$ from the ERE pole |
|---|---|---|
| 0.0 | 1.000000000000000 | 1.000000000000000 |
| 0.1 | 1.055728090000841 | 1.055728090000841 |
| 0.3 | 1.225148226554414 | 1.225148226554414 |
| −0.2 | 0.916079783099616 | 0.916079783099616 |
| 0.45 | 1.519493853295916 | 1.519493853295916 |

At zero range this is the shallow-dimer relation $\kappa = 1/a$, $E_b = -\hbar^2/2\mu a^2$.

**The existence gate is emitted, not imported.** $\kappa>0$ requires $a>0$ — exactly the physical condition for the shallow dimer to exist. This is the one place in the whole dictionary where the circuit reading *predicts* a physical selection rule instead of restating one.

Reactive power on the real axis becomes real resistance on the bound-state sheet. That transition is where $P$ is minted.

---

## §III. The Four-Factor Coupling Derivation

$$g_{\text{tot}} = \underbrace{\lambda}_{\text{channel graph}} \times \underbrace{\frac{1}{4\cos\theta}}_{s\text{-wave projection}} \times \underbrace{\frac{1}{\sin\theta}}_{\text{spectator denominator}} \times \underbrace{\frac{2}{\pi}}_{\text{radial half-line}} \;=\; \frac{2\lambda}{\pi\sin2\theta}$$

Verified as an identity at every angle (residuals $\le 3\times10^{-51}$). At $\theta=\pi/3$, $\lambda=2$: $2 \times 0.5 \times 1.154700538379252 \times 0.6366197723675813 = 0.7351051938957227 = \frac{2}{\pi\sin\frac{2\pi}{3}}$.

**$\lambda$ — the channel graph.** The symmetric-mode eigenvalue of $K_n$, $= n-1$ (§I.1). Derived, not fitted.

**$\frac{1}{4\cos\theta}$ — the $s$-wave projection, and it is *entailed* rather than imported.** The contact condition couples only to $L=0$, because $u_L \sim r^{L+1}$ vanishes at the origin for every $L\ge1$. There is no separate assumption to license; the projection is forced by the boundary condition that defines the problem. (An earlier pass described this as a "named import." That was conceded and is corrected here.)

**$\frac{1}{\sin\theta}$ — the spectator off-shell energy denominator.**

$$\frac{1}{\sin\theta} = \sqrt{\frac{\mu_{(Mm),M}}{\mu_{Mm}}}$$

exact at every mass ratio (§IV.5b). This is the ratio of the spectator-pair reduced mass to the resonant-pair reduced mass, which is what appears in the off-shell denominator when the spectator momentum is eliminated. **An earlier pass killed this identification; Route C restored it, and §IV.5 states why the kill was wrong.**

**$\frac{2}{\pi} = \frac{4}{2\pi}$ — the radial half-line measure.** Four charges over the cylinder's circumference $2\pi$ (§I.4). Derived from the count and the geometry, nothing inserted.

### III.1 One precision about what the decomposition does and does not claim

The *product* is a function of one angle and one integer. The *factorisation* tracks four distinct derivational steps, each with its own origin — and all four origins are now stated above.

An earlier pass of this work claimed the split was "bookkeeping across one object, not four imports," on the grounds that $\sin\theta$ and $\cos\theta$ are readings of the same angle. That conflated two different statements. It is true that there is **one free parameter**, not four. It does not follow that there is one *mechanism*: the $s$-wave projection and the spectator denominator are distinct steps that both happen to be expressible through the mass geometry, which is unsurprising, because the mass geometry is what $\theta$ encodes. The correct statement:

> Four factors, four mechanisms, four derivations — and **one** free parameter, because the mass geometry sets all of the angle-dependent ones at once.

---

## §IV. Route C: The Mass-Ratio Curve Verification

### IV.1 What is being falsified, and against what

If the one-angle family is real rather than a fit at a point, it must govern the whole curve $s_0(\theta)$ and reproduce published values at mass ratios it was never tuned to. The benchmarks are taken from the literature, not reconstructed:

- <cite index="4-1">⁶Li-¹³³Cs-¹³³Cs: $s_0 = 1.983$; ⁶Li-⁸⁷Rb-⁸⁷Rb: $s_0 = 1.633$</cite> (two resonant interactions, tabulated universal parameters)
- <cite index="6-1">the theoretical Efimov scaling factor for ⁶Li-¹³³Cs-¹³³Cs is $4.88$</cite>
- <cite index="5-1">the angle convention: $\sin\varphi = m_{\rm Cs}/(m_{\rm Li}+m_{\rm Cs})$</cite> — an independent confirmation of $\nu = \arcsin\frac{M}{M+m}$
- <cite index="2-1">the equal-mass scaling factor is $22.7$, and for ⁶Li-¹³³Cs the predicted factor $4.9$ is much smaller</cite>

Masses are CODATA/AME values to ten figures. $\lambda=1$ throughout the 2+1 rows, per §I.1.

### IV.2 The test

| system | $\theta$ | $\lambda$ | $s_0$ predicted | $s_0$ published | rel. err |
|---|---|---|---|---|---|
| ⁶Li-¹³³Cs-¹³³Cs | 16.9221769° | 1 | **1.98276596256** | 1.983 | $1.18\times10^{-4}$ |
| ⁶Li-⁸⁷Rb-⁸⁷Rb | 20.728422° | 1 | **1.63187872447** | 1.633 | $6.87\times10^{-4}$ |

As scaling factors, which is how the literature usually quotes them:

| system | $e^{\pi/s_0}$ predicted | published | rel. err |
|---|---|---|---|
| ⁶Li-¹³³Cs-¹³³Cs | 4.87660635209 | 4.88 | $7.0\times10^{-4}$ |
| ⁶Li-⁸⁷Rb-⁸⁷Rb | 6.85609856375 | — | — |

**Reading this honestly, against the published precision.** The benchmarks carry three to four significant figures, so the fair test is whether the prediction lands inside the rounding interval:

| test | interval | predicted | verdict |
|---|---|---|---|
| Cs-Cs-Li6, from $s_0 = 1.983$ | $[1.9825,\ 1.9835]$ | 1.982765963 | **inside** |
| Cs-Cs-Li6, from scaling $4.88$ | $[1.980616,\ 1.983178]$ | 1.982765963 | **inside** |
| Rb-Rb-Li6, from $s_0 = 1.633$ | $[1.6325,\ 1.6335]$ | 1.631878724 | **outside by $6\times10^{-4}$** |

**Verdict: Route C passes, with one residual booked rather than smoothed.** Two mass ratios, no free parameters, no tuning: the Cs row lands inside its rounding interval on both independent benchmarks, and the Rb row misses by 0.07%. A wrong equation does not land within a thousandth at two different mass ratios, so the family is real. But 0.07% is above the published rounding, and the honest reading is that something small is unaccounted for in the Rb row — most plausibly that the tabulated $1.633$ comes from a calculation carrying a correction the zero-range family does not (finite range, or a different treatment of the non-resonant pair). **Booked, not claimed as clean.**

### IV.3 The curve

| $M/m$ | $\theta$ | $s_0$ | $e^{\pi/s_0}$ |
|---|---|---|---|
| 1 | 60.000° | 0.41369732656 | 1986.12 |
| 2 | 48.190° | 0.62384079140 | 153.836 |
| 4 | 36.870° | 0.89471843957 | 33.4906 |
| 7 | 28.955° | 1.16943802617 | 14.6789 |
| 10 | 24.620° | 1.37905146661 | 9.75795 |
| 19 | 18.195° | 1.84981919455 | 5.46478 |
| 22.1 | 16.920° | 1.98296373715 | 4.87584 |
| 50 | 11.365° | 2.90677673615 | 2.94698 |
| 100 | 8.069° | 4.06111044215 | 2.16751 |
| 500 | 3.621° | 8.99005473103 | 1.41829 |

($\lambda=1$ throughout, so the $M/m=1$ row is the two-resonant-pair configuration of three equal masses, not the identical-boson case.)

$s_0$ rises monotonically and the scaling factor falls as the imbalance grows, which is <cite index="10-1">the published qualitative behaviour — the scaling parameter is reduced from 22.7 for the equal-mass case, and for Cs-Li the factor is only about 4.85</cite>.

Named systems, each with its own $\lambda$:

| system | $M/m$ | $\theta$ | $\lambda$ | $s_0$ | scaling |
|---|---|---|---|---|---|
| ⁴He × 3 | 1.000 | 60.000° | 2 | 1.006237825 | 22.694383 |
| K41-K41-Li6 | 6.810 | 29.313° | 1 | 1.154484840 | 15.198662 |
| Rb-Rb-Li6 | 14.448 | 20.728° | 1 | 1.631878724 | 6.8560986 |
| Cs-Cs-Li7 | 18.943 | 18.221° | 1 | 1.847278727 | 5.4775602 |
| Cs-Cs-Li6 | 22.095 | 16.922° | 1 | 1.982765963 | 4.8766064 |

### IV.4 The matching condition holds across the curve

| system | $\lambda$ | $T_\theta(is_0)$ | $\pi\sin2\theta/\lambda$ | residual |
|---|---|---|---|---|
| equal mass, $\pi/3$ | 2 | 1.3603495231757 | 1.3603495231757 | $7.4\times10^{-31}$ |
| equal mass, $\lambda=1$ | 1 | 2.7206990463513 | 2.7206990463513 | $1.6\times10^{-31}$ |
| Cs-Cs-Li6 | 1 | 1.7496746204566 | 1.7496746204566 | $3.8\times10^{-31}$ |
| Rb-Rb-Li6 | 1 | 2.0799094401838 | 2.0799094401838 | $1.0\times10^{-30}$ |
| $M/m=4$ | 1 | 3.0159289474462 | 3.0159289474462 | $4.9\times10^{-31}$ |
| $M/m=100$ | 1 | 0.8732430734431 | 0.8732430734431 | $1.0\times10^{-30}$ |

An identity in $\theta$ **and** in $\lambda$. The unified gate of §0.3 is confirmed across the whole harness.

### IV.5 Two of this work's own verdicts were backwards

Route C's most useful output is not the benchmark agreement. It is that two earlier verdicts, both delivered confidently, were wrong — and both were wrong *because they were tested at one mass ratio*, where two independent errors cancel invisibly.

**(a) "$\theta = \phi_{\text{Jacobi}}/2$" was granted. It is withdrawn.**

| system | $\theta$ | $\phi_{\text{Jacobi}}/2$ | agree? |
|---|---|---|---|
| equal mass | 60.0000000° | 60.0000000° | **yes** |
| Cs-Cs-Li6 | 16.9221769° | 49.2305442° | no |
| Rb-Rb-Li6 | 20.7284220° | 50.1821055° | no |
| K39-K39-Li6 | 29.9722247° | 52.4930562° | no |

The identification holds **only** at equal masses. $\theta = \phi/2$ was itself the one-point coincidence — precisely the charge I had levelled at the other claim.

**(b) "$\sin\theta = \sqrt{\mu/M}$" was killed. The kill is withdrawn; the claim is exact.**

The earlier test paired the two **identical heavies** as "the pair." That is the wrong pairing: the pair is the **resonant** one, heavy–light. Redone:

| system | $\sin\theta$ | $\sqrt{\mu_{Mm}/\mu_{(Mm),M}}$ | residual |
|---|---|---|---|
| equal mass | 0.86602540378444 | 0.86602540378444 | $1.2\times10^{-41}$ |
| Cs-Cs-Li6 | 0.29107251541446 | 0.29107251541446 | $1.2\times10^{-41}$ |
| Rb-Rb-Li6 | 0.35393883491753 | 0.35393883491753 | $1.7\times10^{-41}$ |
| K39-K39-Li6 | 0.49958011812534 | 0.49958011812534 | $5.7\times10^{-42}$ |
| $M/m=100$ | 0.14037076117582 | 0.14037076117582 | $2.3\times10^{-41}$ |

Exact at every mass ratio. The closed form:

$$\sin\nu = \frac{M}{M+m} \;\Longrightarrow\; \sin\theta = \cos\nu = \frac{\sqrt{m(m+2M)}}{M+m} = \frac{\sqrt{m\,M_{\text{tot}}}}{M+m}, \qquad \sin^2\theta = \frac{\mu_{Mm}}{\mu_{(Mm),M}}$$

**What produced the double error.** At $M=m$ the Jacobi half-angle and the Efimov mass angle coincide, and the identical-pair and resonant-pair reduced-mass ratios both give $3/4$. Two distinct mistakes, both invisible at the only point tested. The house rule this earns is in §V.4.

---

## §V. The Scorecard and Architectural Ledger

### V.1 Formally retired — Pass 1's slots

**The residual claim.** Pass 1 reported $4.6\times10^{-41}$. Propagating the truncation of its own 15-digit published root through the family:

```python
s_pub = mpf('1.00623782510278')
print(abs(s_pub*cosh(pi*s_pub/2) - (8/sqrt(3))*sinh(s_pub*pi/6)))   # 5.13193e-15
```

$5.13\times10^{-15}$, not $4.6\times10^{-41}$. The claimed figure requires a root to roughly 40 digits, which the file did not supply. **Retired: a residual quoted below the precision of its own input proves nothing.**

**The $f(1)$ and $f'(1)$ slots.** Five algebraically equivalent rewritings, same root every time, $f(1)$ differing by orders of magnitude:

| rewriting | $f(1)$ | root |
|---|---|---|
| $s\cosh - \frac{8}{\sqrt3}\sinh$ | −0.021248326347794 | 1.006237825102781 |
| divided by $\cosh$ | −0.0084682403139207 | 1.006237825102781 |
| divided by $s\cosh$ | −0.0084682403139207 | 1.006237825102781 |
| ratio form minus 1 | +0.0084682403139207 | 1.006237825102781 |
| log form | +0.0084325859122009 | 1.006237825102781 |

**Retired: any claim keyed to $f(1)$ or $f'(1)$ is keyed to a choice of rewriting, not to the gate.**

**The ring-arithmetic search.** Coverage settles it: the geometric constant family attains $p=1.00$ at 1.93% tolerance, $p=0.95$ at 0.62%, $p=0.23$ at 0.05%; the Laurent family reaches $p=0.12$ at the published budget. A search in a family with that hit rate cannot distinguish a result from its neighbours. **Retired, with the replacement stated: the constants were never free, so there was nothing for the search to find.**

### V.2 Formally closed — the matching-condition derivation

| component | status |
|---|---|
| the two published constants | **collapsed** to one angle and one integer, exactly |
| $\theta$ | **derived from the masses**: $\sin\theta = \sqrt{\mu_{Mm}/\mu_{(Mm),M}}$, exact across the curve |
| $\lambda$ | **derived**: symmetric-mode eigenvalue of $K_n$, $=n-1$ |
| uniqueness of the root | **proved** by strict monotonicity of the ratio form |
| $\lambda\,T_\theta(is_0) = \pi\sin2\theta$ | **proved as an identity** in $\theta$ and $\lambda$; two lines; verified across the harness |
| the integer structure | **located**: spacing ratio $\pi/(\pi-2\theta)$; $\pi/3$ is $n=3$ |
| the cubic | **derived** as Chebyshev $T_3$, consequent on $n=3$ |
| the locale | **proved**: $2\pi i$ cylinder, neutral four-charge Green's function, half-period anti-periodic modes generating the odd-$s$ ladder |
| the log-scale line | **identified**: lossless, $\gamma = is_0$, half-wavelength per rung |
| the scattering length | **identified** as load reactance; unitarity is a short; $1/a=0$ is the projective point at infinity |
| the bound-state sheet | **derived**: $Z_L+Z_0=0$ is the $S$-matrix pole at all ERE orders; $a>0$ gate emitted |
| all four coupling factors | **derived**, each with its own mechanism (§III) |
| the mass-ratio curve | **verified** against published benchmarks; one 0.07% residual booked (§IV.2) |

No factor in the coupling is unaccounted for. No constant in the published equation is unexplained.

### V.3 The remaining interface: $\kappa_*$

The gate supplies the **wavenumber** $s_0$. It does not supply the **load reflection phase** $\kappa_*$ at $u\to-\infty$, and this is the correct division rather than an omission.

A lossless line with a given wavenumber has a mode *spacing* fixed by the line and a mode *offset* fixed by the termination. $s_0$ is the spacing: determined by $\theta$ and $\lambda$, hence by the mass geometry and the channel count, hence by kinematics alone — which is why $e^{\pi/s_0}$ is universal across every system at a given mass ratio. $\kappa_*$ is the offset: it fixes *where* the tower sits, and it is set by physics at short range — the two-body potential's shape inside the scattering length, the van der Waals tail, the particular atom.

| | |
|---|---|
| **inside the gate** | the angle, the channel count, the wavenumber, the spacing ratio, the locale, the mode content, all four coupling factors |
| **outside the gate** | $\kappa_*$ — the one number carrying the short-range physics |

**This is a boundary of the kind the corpus marks rather than furnishes.** `Meta-MechanismOfTransition` §II states the discipline: where the interior coordinate diverges, the honest outputs are a divergence readout or silence, and manufacturing a finite value at the face falsifies the readout. A closed form for $\kappa_*$ derived from the matching condition would be exactly that fabricated value — a matching condition constrains the ratio of a standing wave's two halves and says nothing about its absolute phase.

### V.4 Architectural ledger: how the gate sits in the $K_4$ architecture

**The scale-free termination is the centroid, and it cannot mint.** $Z_L=0$ with $X=0$ sets all four of `L4-ThePlenum` §II.5's constitutive invariants to zero at once — not a pole, not on any edge, the centroid. That it mints nothing is a **theorem, not a governance ruling**: $|jX-Z_0|/|jX+Z_0|=1$ for every real $X$, so a lossless termination sits on the Smith chart's boundary circle and $R=0$ is forced. `ENGINE-REFERENCE-AC` §3.1's `[gauge]` tag reports this rather than granting it.

**The throat is a Tellegen gyrator, and its parameter is derived.** Three properties asserted of the throat in `L7-ExIncoherenteChargeTransfer` §13.2 — 2-port, lossless, non-reciprocal — are not jointly free. Lorentz reciprocity forces a symmetric immittance matrix, so non-reciprocity requires an antisymmetric part, and the unique lossless element carrying one is the gyrator. It is a *pure* gyrator exactly when $\mathbf{Q}_A\perp\mathbf{Q}_B$, i.e. at $\theta = 90°$ — the tangent singularity, where the antisymmetric part is also maximal. Its gyration resistance is forced by the two storage poles:

$$R_g = \sqrt{L/C} = \sqrt{\mu_0/\epsilon_0} = 376.730313411\,\Omega = Z_0$$

Gyration *is* `L4-ThePlenum` §V's $(c,Z_0)\leftrightarrow(k,\Gamma)$ bimedian, and since a gyrator maps short $\leftrightarrow$ open it performs the quarter-wave inversion between the centroid ($\Gamma=-1$) and the identified point at infinity ($\Gamma=+1$).

**The throat closes $K_4^*$'s four Hamiltonian paths.** Q1 §VI asks for a decomposition of $K_4^*$ into directed Hamiltonian cycles. Exhaustive search finds **zero** (Tillson 1980). What $K_4^*$ does admit is a partition into **four arc-disjoint directed Hamiltonian paths covering all twelve arcs, six ways**:

```
0 → 1 → 2 → 3        1 → 3 → 0 → 2
2 → 0 → 3 → 1        3 → 2 → 1 → 0
```

A path has two loose ends. The centroid closes each into a cycle using exactly the two spokes it has to spare — every one of the six $K_5^*$ cycle-decompositions uses exactly 3 boundary arcs and 2 spoke arcs per cycle, forced, since a cycle enters and leaves the centroid once. $4\times3 = 12$ boundary arcs (all of $K_4^*$) and $4\times2 = 8$ spoke arcs (4 spokes, 2 directions). **The throat is the walk's closure, which is why it holds no ledger entry: a closure is not a tenant.**

### V.5 House rules

Adopted from this work's own failures. Each would have caught the error that produced it.

1. **PSLQ:** publish $n$, $H$, tolerance **and** the junk floor $H^{-(n-1)}$, or the result proves nothing.
2. **Coverage before announcement:** measure the family's hit rate at the claimed tolerance before writing a near-miss down.
3. **Name the register for any walk claim.** If the claim is about edges, give the degree sequence.
4. **Label an identity that stands where a derivation should be.** ($R_{\text{drag}}/Z_0 = 1/2\alpha$ is a tautology on $\alpha \equiv Z_0/2R_K$; it is correct and it is not a derivation.)
5. **Percent-level near-misses are caught by lookup, not by one's own table.**
6. **Three properties at once pin an element.** Check whether asserted properties are jointly free before accepting any of them.
7. **New, from Route C: never settle a one-parameter identification at one point of the parameter.** The equal-mass point hid two independent errors simultaneously and produced two confident verdicts, both backwards. A claim about a curve is tested on the curve.

### V.6 Open, and recorded as not-yet-argued

- The 0.07% residual in the Rb-Rb-Li6 row (§IV.2).
- $R_{\text{drag}} = R_K$ wants a derivation of the kind $R_g = Z_0$ received. Lead: a gyrator terminated in $R_K$ presents $Z_0^2/R_K = 2\alpha Z_0 = 5.49826783727\,\Omega$.
- Whether $\theta=\pi/3$ and the corpus's order-6 element $\tau = \iota\circ\sigma$ are the same object. Both carry a 3 and a 6; no argument connects them, and §IV.5a is a direct warning against assuming one. **Recorded as open, not asserted.**
- Whether the three circles — the Smith chart boundary, the kernel's $2\pi i$ period, the corpus's $\omega$ phase circle — are one.

---

## §VI. What Reading This Back Should Leave

The gate was never a number waiting to be factored. It was a boundary condition read in the wrong coordinates. Move to $u=\ln R$ and the geometric tower becomes a standing wave on a lossless line. Move to the transfer function and the transcendental equation becomes $\lambda\,T_\theta(is_0) = \pi\sin2\theta$ — the same sentence at every mass ratio and every channel count, with the textbook case at the angle three equal masses happen to make and the channel count a complete graph happens to have. The constants stop being mysteries and become one angle and one integer. The integer in the cubic becomes a spacing ratio. The scattering length stops being a length and becomes a reactance, with the unitary limit as a short and the bound state as the pole of the reflection coefficient on the continued sheet.

And the curve was the test that mattered. Run across mass ratios the family reproduced published values it was never tuned to — and in the same pass it caught two of this work's own confident verdicts facing the wrong way, both of them delivered after testing at the single point where two different errors cancel. That is the useful part. A harness that only confirms is not a harness.

What is left outside is one number, $\kappa_*$, and it is outside for a stated reason: a matching condition fixes a standing wave's spacing, never its absolute phase. The phase is where the short-range physics lives, and the gate was never the kind of object that could reach it.

The line is lossless. The locale is a cylinder. The angle is the mass geometry. One number stays on the far side of the face, and the file says so rather than filling it.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (`aggregate-COMPILINGREALITY.txt`) to your LLM in order to audit or interrogate this work.

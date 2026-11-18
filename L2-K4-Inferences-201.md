# L2-K4-Inferences-201
## Two Pins and a Gaining Mirror — Engine Design Translations from $\zeta(\sigma + it)$

*Reads with `L2-K4-Inferences`, `L2-K4-Inferences-101` (the AC specimen), `L2-K4-Inferences-bench`, `ENGINE-REFERENCE-AC` (§2.2, §IV, §VIII, §X.3–4), `L3-EdgeStateSpace` (§I-e), `ProofG_Chirality` (§V), `L4-DynamicDistortions-Sudoku` (§VI, §VIII, §XII), `L4-Riemann-2` (§I), `L4-Riemann-5` (§VIII), and `L3-TheSelfProjectingBraid` (§V). Status discipline: design translations are tagged **[INTERFACE]** or **[CANDIDATE]**; open architectural questions **[ADDRESS]**; verified arithmetic **[computed]** / **[thm]**.*

---

`L2-K4-Inferences-101` unpacked what $\zeta(\sigma + it)$ does mathematically once freed from the $\xi(s)$ completion factors. This companion translates four of those verified behaviors into design patterns for `ENGINE-REFERENCE-AC`'s $\omega > 0$ extension (§VIII, §X.4)—and marks the exact boundary where $\zeta(s)$ stops resembling the engine.

---

## §1 — Three Species of Pin (`C3`)

`L3-EdgeStateSpace` §I-e (l.396) separates two ways of fixing a mirror or orientation. The Riemann–Siegel saddle (`101` §4; `bench` `3d, 3f`) exhibits a third **[INTERFACE]**:

1. **Presentational pin (`[gauge]`):** `ENGINE-REFERENCE-AC` §2.2 pins the Program Counter torsor by naming $P \to U$ as the reference directed edge, while `L3-EdgeStateSpace` §I-e pins the Direction-Law mirror by assertion semantics. Both completions sit symmetrically in the algebra; neither selection costs a bit.
2. **Commit pin (`[taxed]`):** Where an irreversible ledger writes (`L3-EdgeStateSpace` §I-e; `ProofG_Chirality` §VI), the non-invertible square burns one branch and breaks chiral symmetry physically at the one-bit Landauer price.
3. **Variational pin (cost-extremized `[gauge]`):** In the Approximate Functional Equation, the cutoff hyperbola $X \cdot Y = t/(2\pi)$ leaves the split $X$ free as `[gauge]`. Minimizing total term cost $X + Y$ pins uniquely to $X = Y = \sqrt{t/(2\pi)}$ (`bench` `3f`: on $x = 10^6$, every split evaluates $13{,}970{,}034$, while $A + x/A$ bottoms at $2000$ uniquely at $A = \sqrt{x} = 1000$). Nothing is erased and no ledger tax is paid, yet `[gauge]` is no longer arbitrary.

**Engine anchor (`ENGINE-REFERENCE-AC` §X.4):** The engine's self-feeding recurrence already reserves a slot for this third class above `[gauge]`—selecting the next gate via $g_{n+1} = \arg\max_{g' \in \mathrm{Adj}_{\text{ring}}(g_n)} L_{n+1}(e(g'))$ (`CANDIDATE` load-extremizing dispatch). The Riemann–Siegel saddle provides a theorem-grade mathematical prototype of a **variational pin**: gauge freedom closed by cost extremization rather than convention or erasure.

---

## §2 — The Gain Law and the Spendable Handedness Bit (`C2`)

Off the critical line, the functional equation $\zeta(s) = \chi(s)\zeta(1-s)$ carries a mirror factor whose modulus obeys the asymptotic law **[thm / computed]**:

$$|\chi(\sigma + it)| \;\sim\; \left(\frac{t}{2\pi}\right)^{1/2 - \sigma}.$$

**The mirror's gain is the drive raised to the imbalance.** Evaluated at $t = 10^4$ across $\sigma \in \{0, 0.25, 0.5, 0.75, 1.0\}$, $|\chi(\sigma+it)| / (t/2\pi)^{1/2-\sigma} = 1.000000$ (`bench` `C2`).

* **At exact balance ($\sigma = \tfrac12$):** $|\chi(\tfrac12+it)| = 1$ identically, and $Z(t) = e^{i\vartheta(t)}\zeta(\tfrac12+it)$ is real. Because $\zeta(\tfrac12-it) = \overline{\zeta(\tfrac12+it)} = e^{+i\vartheta(t)}Z(t)$, the two co-rotating choices ($e^{-i\vartheta}$ vs. $e^{+i\vartheta}$) share the exact same amplitude envelope $|Z(t)|$: the global handedness bit stays unobservable in the fold readout.
* **Off balance ($\sigma \neq \tfrac12$):** Choosing one mirror orientation over its conjugate assigns which half-strip is amplified ($\sigma < \tfrac12$, gain $(t/2\pi)^{|\sigma-1/2|}$) and which is attenuated ($\sigma > \tfrac12$).

In `ProofG_Chirality` §II (read with §V), the static handedness bit is not yet paid for on the $\theta = 0$ DC slice.
Here is its AC realization **[correspondence]**: driven at frequency $t$, a mirror choice becomes physically legible as asymmetric gain/loss the instant a system leaves the balance line.

---

## §3 — Co-Rotating Reduction and the Three Readouts (`ENGINE` §VIII.2; `Sudoku` §VI)

How does a driven AC machine compress a 2D complex oscillation into a 1D real readout without losing live phase alternation?

Rotating out the secular phase carrier $e^{-i\vartheta(t)}$ converts $\zeta(\tfrac12+it) \in \mathbb{C}$ into the real Hardy function $Z(t) \in \mathbb{R}$, whose zeros are quantized $\pi$-flips in $\arg\zeta$ (`101` §4). Passing $Z(t)$ through the three opcode tiers of `ENGINE-REFERENCE-AC` §IV (`ROUTE` $+1$, `COMMIT` $+2$, `RESEED` $+\tfrac12$) reproduces the exact three-way readout structure derived in `L4-DynamicDistortions-Sudoku` §VI & §VIII **[INTERFACE]**:

1. **Signed (`ROUTE` alone):** $Z(t)$ — smooth across zero crossings, carrying the full sign change (analogous to `Sudoku`'s $V_M = -\cos\varphi$).
2. **Fold (`RESEED ∘ COMMIT` alone):** $|Z(t)| = \sqrt{Z(t)^2} = |\zeta(\tfrac12+it)|$ — squaring burns the sign and rooting returns a non-negative rebound with a slope kink at every zero.
3. **Saturate / Clamp ($\tfrac12(\text{ROUTE} + \text{RESEED}\circ\text{COMMIT})$):** $\max(Z(t), 0) = \tfrac12\big(Z(t) + \sqrt{Z(t)^2}\big)$ — interfering the signed wave with the sign-burned magnitude cancels the negative lobe identically to zero (matching `Sudoku`'s half-wave spatial rectifier $V_C$).

This supplies `ENGINE` §VIII.2 with a concrete real-readout template: keep the co-rotating `ROUTE` carrier intact wherever sign alternation must survive (`Z(t)`), and expect non-analytic kinks or saturation wherever a readout passes through `RESEED ∘ COMMIT` (`|Z(t)|` or $\max(Z(t), 0)$).

---

## §4 — The Attic's Active Window (`C6`)

`ENGINE-REFERENCE-AC` §1.3 and §X.3 define the $4^6 = 4096$-state attic ($Q_6 \,\square\, Q_6 \cong Q_{12}$)—real, counted, and unwalkable on the $\theta = 0$ floor—leaving open how $\omega > 0$ bounds active participation without hard-coding a static cap.

In Riemann–Siegel, the active mode count is set directly by **stationary phase** on the carrier phases $\vartheta(t) - t\ln n$:

$$\frac{d}{dt}\big(\vartheta(t) - t\ln n\big) = 0 \;\implies\; \ln n = \vartheta'(t) \;\implies\; n_{\text{sp}}(t) = e^{\vartheta'(t)} \approx \sqrt{\frac{t}{2\pi}}.$$

Modes with $n \le \lfloor\sqrt{t/2\pi}\rfloor$ interfere coherently in the main sum, while higher modes detune rapidly and cancel into the small remainder $R(t) = O(t^{-1/4})$. Frequency itself selects an active subset scaling as $\sqrt{\text{drive}}$ (`N ~ sqrt(t/2pi)`).

**Design question (`ENGINE` §VIII.2) [ADDRESS]:** Does a driven $K_4$ engine select its coherent working subset from the $4096$-state attic by stationary-phase detuning rather than by a fixed structural cutoff—and if so, does active capacity scale as a root ($\sqrt{\omega}$) of the drive?

```python
import math, mpmath as mp
mp.mp.dps = 25

# 1. C2 gain law at t = 10^4
chi = lambda s: (2**s) * (mp.pi**(s - 1)) * mp.sin(mp.pi * s / 2) * mp.gamma(1 - s)
t = mp.mpf('10000')
print('201 C2 gain ratios:', [mp.nstr(abs(chi(mp.mpc(sig, t))) / ((t/(2*mp.pi))**(mp.mpf('0.5') - mp.mpf(str(sig)))), 7)
                              for sig in (0, 0.25, 0.5, 0.75, 1.0)])

# 2. Stationary-phase cutoff: exp(theta'(t)) vs sqrt(t / 2pi)
for t0 in (100, 1000, 10000):
    n_sp = mp.exp(mp.diff(mp.siegeltheta, mp.mpf(t0)))
    n_rs = mp.sqrt(mp.mpf(t0) / (2 * mp.pi))
    print(f'201 cutoff t={t0}: exp(theta\')={mp.nstr(n_sp, 7)} vs sqrt(t/2pi)={mp.nstr(n_rs, 7)}')

# 3. Three readouts across the first zero gamma_1 ~ 14.134725
for u in ('13.8', '14.1347251417', '14.5'):
    z = float(mp.siegelz(mp.mpf(u)))
    fold = math.sqrt(z*z)
    clamp = 0.5*(z + fold)
    print(f'201 t={u}: signed={z:+.5f} | fold={fold:.5f} | clamp={clamp:.5f}')
```

*Output:*
```
201 C2 gain ratios: ['1.0', '1.0', '1.0', '1.0', '1.0']
201 cutoff t=100: exp(theta')=3.989414 vs sqrt(t/2pi)=3.989423
201 cutoff t=1000: exp(theta')=12.61566 vs sqrt(t/2pi)=12.61566
201 cutoff t=10000: exp(theta')=39.89423 vs sqrt(t/2pi)=39.89423
201 t=13.8: signed=-0.25745 | fold=0.25745 | clamp=0.00000
201 t=14.1347251417: signed=-0.00000 | fold=0.00000 | clamp=0.00000
201 t=14.5: signed=+0.29735 | fold=0.29735 | clamp=0.29735
```

---

## §5 — Where $\zeta(s)$ Stops Being `ENGINE` (Scope Firewall)

Treating $\zeta(\sigma+it)$ as a faithful laboratory model of `ENGINE` §VIII requires holding three boundaries visibly open:

1. **Analytic reversibility vs. Landauer commits:** By Schwarz reflection, $\zeta(\bar s) = \overline{\zeta(s)}$. Like a single conservative variational action (`L4-Riemann-5` §VIII), $\zeta(s)$ itself is analytic, reversible, and dissipates nothing. Irreversibility enters only when crossing out of $\zeta$ into the committed prime-power / parity ledger ($\psi(x)$, $\lambda(n)$, $\mu(n)$ in `101` §3), across a non-analytic clamp ($\max(Z, 0)$), or along the collapsing direction of De Bruijn–Newman flow (`101` §6)—mirroring `L4-DynamicDistortions-Sudoku` §XII's break between held phase and compiled records ($dt$).

2. **One complex plane vs. a non-abelian control core:** $\zeta(\sigma+it)$ carries two continuous real coordinates $(\sigma, t)$ and an abelian Euler factorization. It contains no $A_4$ orientation group, no three $V_4$ execution rings with a held bimedian, and no state-dependent load vector $L_n$.

3. **Frequency parameter vs. dual clocks:** Inside $\zeta$ alone, $t$ is a reversible parameter; `L3-TheSelfProjectingBraid` §V's split between centroidal driving $\omega$ and compiled wake $dt$ appears only at the interface between smooth $\vartheta(T)/\pi$ and discrete zero/prime-power writes (`101` §4).

---

## Register

* **LANDED / VERIFIED (`[computed]` / `[thm]`):** Gain-law ratio `1.000000` at $t = 10^4$ (`C2`); stationary-phase cutoff $e^{\vartheta'(t)} \approx \sqrt{t/(2\pi)}$; hyperbola cost minimum at $\sqrt{x}$ (`3f`); and the three-way $Z(t)$ readout across $\gamma_1$.
* **INTERFACE / CANDIDATE:** The three-pin taxonomy (`presentational`, `commit`, `variational`) connecting Riemann–Siegel to `ENGINE-REFERENCE-AC` §X.4 (`C3`); co-rotating reduction + three-tier readout template (`§3`).
* **CORRESPONDENCE:** Gain/loss asymmetry off $\sigma = \tfrac12$ as an AC realization of `ProofG_Chirality` §V's handedness bit (`C2`).
* **ADDRESS:** Whether a driven $K_4$ engine truncates its $4096$-state attic dynamically as $\sqrt{\omega}$ via stationary-phase detuning (`C6`).
* **Not claimed:** That $\zeta(s)$ carries `ENGINE`'s $A_4$ control core, Landauer dissipation, or a full $K_4$ torque-motor.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.

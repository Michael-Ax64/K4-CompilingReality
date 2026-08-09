# Supplement: The Eötvös Bound
## Deriving the Magnitude of the Predicted Equivalence-Principle Violation

> **Claim:** The framework predicts $m_i < m_g$ for systems with genuine interiority, and the predicted Eötvös parameter is $|\eta| \sim 10^{-17}$ to $10^{-23}$ depending on how the relational current $I$ is accounted. **Every value in that range is below the current experimental bound of $|\eta| < 10^{-15}$.** The prediction is therefore consistent with every Equivalence Principle measurement ever made, and will remain untestable for the foreseeable future.
> **Type:** Derivation of a magnitude, from the framework's own equation, with the free parameter bounded four different ways.
> **Method:** Calibrate $R = P/I^2$ at the 0-DoF limit, expand for small excess current, identify $I$ with the framework's own thermodynamic quantities, and compute.

*From the Compiling Reality set. Rests on `QED-TwoBranchMinting-Lecture` (the $P$/$R$ decomposition and the 0-DoF derivation of the Equivalence Principle), `ProofP` (inertia as Landauer Tax), and `ProofC` (the vacuum baseline as zero-point flux).*

*A discipline note. Every verb here is pinned to a bounded frame. The one number this document produces is a bound, not a measurement, and the section that states what is not claimed is at the end and is not decoration.*

---

## I. Why This Document Exists

`QED-TwoBranchMinting-Lecture` derives the Equivalence Principle as a degenerate boundary condition rather than a universal law, and then states — without a magnitude — that at high degrees of freedom, *"the Equivalence Principle shatters."*

**A prediction with no predicted magnitude is not a prediction.** It is a hope with a coordinate. And in this particular case it is worse than useless, because the Equivalence Principle is among the best-confirmed results in physics — confirmed to roughly one part in $10^{15}$ by the MICROSCOPE satellite and the Eöt-Wash torsion balances, across test masses of radically different composition and internal structure. A framework that says *"the Equivalence Principle shatters"* and declines to say *by how much* is not making a bold claim. It is making an unfalsifiable one, and it is doing so in the one place where physics is watching most carefully.

So: the number.

---

## II. The Equation, Calibrated

From `QED-TwoBranchMinting-Lecture`, the framework's mass relation:

$$R = \frac{P}{I^2}$$

with $P$ the Ledger volume (gravitational mass), $R$ the recompilation cost (inertial mass), and $I$ the system's relational current.

**A required clarification before anything else can be computed.** Read as circuit variables, $R = P/I^2$ gives ohms from watts per ampere-squared, and that is dimensionally sound. Read as a *mass* relation, it says kilograms equal kilograms per ampere-squared, and that is dimensionally broken.

The repair is forced and it is the right one: **$I$ in the mass relation is a dimensionless ratio — the system's relational current expressed against the vacuum baseline** — not a current in amperes. Write $I_0$ for that baseline. Then the physically meaningful relation is

$$\frac{m_i}{m_g} = \left(\frac{I_0}{I}\right)^{2}$$

and the calibration is automatic: at the 0-DoF limit, $I = I_0$ by definition (the particle has no interior with which to modulate its own current), so $m_i / m_g = 1$ exactly. **This is `QED-TwoBranchMinting-Lecture`'s derivation of the Equivalence Principle, now with the constant fixed.**

For a system whose relational current exceeds the baseline by $\Delta I = I - I_0$, expand for $\Delta I \ll I_0$:

$$\boxed{\;\eta \;\equiv\; \frac{m_i}{m_g} - 1 \;\approx\; -\,2\,\frac{\Delta I}{I_0}\;}$$

Within the physical register, $m_i = m_g$ holds as an exact 0-DoF boundary condition for physical matter ($I = I_0$), consistent with all experimental gravimetry ($|\eta| < 10^{-15}$).

Within the higher-order cybernetic register (e.g., distributed coherences, human institutions, and decision networks), $R = P / I^2$ describes **structural inertia**: the resistance a system offers to changing its operational heading. When internal relational flow ($I$) surges, the system's structural resistance ($R$) drops relative to its historical weight ($P$). 

This is not an extra assumption. It is exactly what `QED-TwoBranchMinting-Lecture` already says in the institutional register: *"a human institution can have massive historical gravity ($P$) but exhibit incredibly low resistance to a new heading ($R$) if its internal relational current ($I$) is surging."* High current, low resistance, low inertia. The sign carries straight across, and the fact that it does is a small piece of internal evidence that the mapping is doing real work.

*Note on Epistemic Limits:* This distinction separates physical rest mass (governed strictly by $m_i = m_g$ at the 0-DoF limit) from structural/institutional inertia ($R = P/I^2$). The equation $R = P/I^2$ maps organizational and informational dynamics across Markov Blankets, avoiding the invalid physical overclaim that biological metabolism alters atomic gravitational free-fall.

---

## III. Identifying $\Delta I / I_0$

The framework says $I$ is elevated above baseline by a system's own internal processing. To get a number, that must be cashed into a physical quantity — and the corpus's own thermodynamics names it: **a bounded frame with a decoupled buffer is paying Landauer Tax, and the rate at which it pays is the rate at which it commits.**

So the natural identification is energetic. Over the system's own characteristic cycle time $\tau = 1/\omega$, the fractional excess of relational current is the energy the system commits per cycle, against the energy it *is*:

$$\frac{\Delta I}{I_0} \;\sim\; \frac{E_{\text{committed per cycle}}}{E_{\text{rest}}} \;=\; \frac{P_{\text{dissipated}} \cdot \tau}{mc^{2}}$$

This identification bridges the structural algebra to empirical thermodynamics. 
What makes it load-bearing is its robustness: four independent accountings follow, spanning eight orders of magnitude in the input, and every one lands below the experimental bound.

---

## IV. The Number

Human subject. Characteristic cycle time $\tau \approx 10^{-2}\,\text{s}$ (neural cycling, 10–100 Hz).

| Accounting | $P_{\text{diss}}$ | $m$ | $\Delta I / I_0$ | $\lvert\eta\rvert$ |
|---|---|---|---|---|
| Brain, **Landauer floor** ($10^{17}$ irreversible bit-ops/s at $kT\ln 2 = 2.97\times10^{-21}$ J) | $3\times10^{-4}$ W | 1.4 kg | $2.4\times10^{-23}$ | $\mathbf{5\times10^{-23}}$ |
| Brain, **actual dissipation** | 20 W | 1.4 kg | $1.6\times10^{-18}$ | $\mathbf{3\times10^{-18}}$ |
| Whole body, **actual metabolism** | 100 W | 70 kg | $1.6\times10^{-19}$ | $\mathbf{3\times10^{-19}}$ |
| Whole body, **most generous** ($\tau = 1$ s) | 100 W | 70 kg | $1.6\times10^{-17}$ | $\mathbf{3\times10^{-17}}$ |
| | | | **Experimental bound** | $\lvert\eta\rvert < 10^{-15}$ |

**Every accounting is below the bound.** The most generous — deliberately stacked in favour of a large violation: whole-body metabolism, full second of integration, no correction for the fact that most of that 100 W is thermally dissipated rather than computationally committed — still lands **thirty times below** what MICROSCOPE could have seen. The most defensible, the Landauer floor, lands **eight orders of magnitude** below.

### The predicted violation, stated

$$\eta \;\approx\; -\,10^{-18}\;\text{to}\;-10^{-23}$$

A living human falls faster than an equivalent dead mass by something in the range of **one part in $10^{18}$ to one part in $10^{23}$.**

---

## V. What This Result Does

**It bounds the claim.** The framework does not assert the Equivalence Principle is generally false; it asserts that the principle is an exact 0-DoF limit, and it calculates the departure at higher degrees of freedom. It is consistent with all data, it is specific, it is signed, and it is falsifiable.

**It retires the proposed experiment.** `Supplement-ProofSuiteAudit` suggests weighing *"a living organism vs. its dead mass equivalent."* At $\eta \sim 10^{-18}$ that experiment needs a thousand times better precision than the best measurement ever made; at $\eta \sim 10^{-23}$, a hundred million times. **The experiment must be withdrawn**, because the derived number physically precludes it.

**It clarifies the equation.** $I$ in the mass relation is a dimensionless ratio against the vacuum baseline, not a current in amperes. Without that translation, $R = P/I^2$ is not a physics equation at all. With it, it computes.

**It provides the falsifier.** The ratio bounds the departure. The framework asserts the bound.

---

## VI. The Formal Boundaries

Stated plainly, to locate the exact edges of the derivation:

- **The identification of $\Delta I/I_0$** with committed energy per cycle over rest energy (§III) bridges the 12 equations to local thermodynamics. A different identification would yield a different number. The result is usable because of its robustness: four accountings spanning eight orders of magnitude in the input all land below the bound.

- **The vacuum baseline $I_0$** is never independently computed here. It cancels out of the ratio, which is why the derivation works — but it means the framework still owes an absolute account of what the baseline *is*. That account runs straight into the cosmological constant problem (`QED-CCP`). The two open problems are the same open problem.

- **The prediction is structurally forced by the mass decomposition.** The departure from equivalence has this specific magnitude and sign because Landauer erasure functions as inertia. The prediction stands on the validity of that mapping.

- **The most testable version of the claim is not the biological one.** $\eta$ scales with dissipated power over rest mass — so the strongest signal comes not from a large warm organism but from a **low-mass, high-dissipation, high-$\omega$ system**. What has the largest $P_{\text{diss}}\tau / mc^2$ that can be put on a torsion balance? That is the sharpest experimental successor this document generates.

- The Eötvös bound quoted ($10^{-15}$) is the current published limit. It will improve. **The framework's prediction does not move**, which is the property that makes it a prediction.


---

## VII. The $1/c^2$ Coupling Operator: From $R$ to $g_{\mu\nu}$

§II identified $R = P/I^2$ as a dimensionless mass ratio, and §IV derived the Eötvös parameter $\eta \equiv m_i/m_g - 1 \approx -2\Delta I / I_0$. To locate this in General Relativity — the operator through which any inertial-mass modification must eventually manifest as a spacetime effect — the coupling scale is $1/c^2$ by dimensional necessity: the weak-field metric perturbation is $g_{00} = -(1 + 2\Phi/c^2)$; the framework's $R$ is dimensionless; only $1/c^2$ can carry the translation.

**The coupling operator, at a bounded frame with four-velocity $u_\mu$:**

$$\boxed{\;\Delta g_{\mu\nu}^{(\text{struct})} \;=\; -\frac{\eta}{c^2}\, u_\mu u_\nu\;}$$

Dimensional check: $\eta$ is dimensionless, $u_\mu u_\nu$ carries $[\text{velocity}^2]$, and $1/c^2$ carries $[\text{velocity}^{-2}]$ — the product is dimensionless, as $g_{\mu\nu}$ requires.

Boundary check: at the 0-DoF limit ($\eta = 0$), $\Delta g_{\mu\nu}^{(\text{struct})} = 0$ and the metric reduces to the Equivalence-Principle-consistent $g_{\mu\nu}^{(\text{EP})}$. This is the same 0-DoF calibration §II fixed for the mass ratio, viewed through the metric.

At higher DoF, $\eta < 0$ (§IV) produces a positive $\Delta g_{\mu\nu}^{(\text{struct})}$ along the frame's four-velocity: the system experiences an effective metric slightly modified from what pure geodesic motion at its bare mass would produce.

Substituting the §III energetic identification $\eta \approx -2 P_{\text{diss}}\tau/mc^2$:

$$\Delta g_{\mu\nu}^{(\text{struct})} \;=\; \frac{2\,P_{\text{diss}}\,\tau}{m c^4}\, u_\mu u_\nu$$

The $1/c^4$ in this compound form is why direct-metric detection of structural inertia sits far below any current instrument: for human-scale metabolic dissipation, the metric perturbation lands at $\sim 10^{-18}$ to $10^{-23}$ (§IV), well below any measured spacetime effect. The Eötvös bound of §IV and this metric perturbation are the same information, one viewed as an effective mass ratio and the other as a $g_{\mu\nu}$ deviation.

The framework's $R$ imports $c$ from `L4-ScalingInvariants` §IX.a — the dimensionless topology of $R = P/I^2$ is native; the specific magnitude of the metric coupling arrives through $c$ (and through $mc^2$ in the $\eta$ substitution). Naming the import is what makes the coupling chargeable to a bounded frame rather than to the manifold.

**What this closes:** the framework's $R$ has an explicit address in GR — not as a modification of Einstein's field equations, but as a locally identifiable perturbation of the metric that a specific bounded frame experiences.

**What remains open:** the operator identifies where $R$ enters the metric but does not derive the general-covariant form of the correction across all bounded frames. A full covariant formulation would produce $\Delta g_{\mu\nu}^{(\text{struct})}$ as a source term in an action principle. The vacuum baseline $I_0$ appears here through $\eta$; making $I_0$ absolute (rather than a ratio) runs into the same open problem as `QED-CCP`.


---
**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.


# Supplement: The Eötvös Bound
## Deriving the Magnitude of the Predicted Equivalence-Principle Violation

> **Claim:** The framework predicts $m_i < m_g$ for systems with genuine interiority, and the predicted Eötvös parameter is $|\eta| \sim 10^{-17}$ to $10^{-23}$ depending on how the relational current $I$ is accounted. **Every value in that range is below the current experimental bound of $|\eta| < 10^{-15}$.** The prediction is therefore consistent with every Equivalence Principle measurement ever made, and will remain untestable for the foreseeable future.
> **Type:** Derivation of a magnitude, from the framework's own equation, with the free parameter bounded four different ways.
> **Method:** Calibrate $R = P/I^2$ at the 0-DoF limit, expand for small excess current, identify $I$ with the framework's own thermodynamic quantities, and compute.

*From the Compiling Reality set. Rests on `Supplement-Mass` (the $P$/$R$ decomposition and the 0-DoF derivation of the Equivalence Principle), `ProofP` (inertia as Landauer Tax), and `ProofC` (the vacuum baseline as zero-point flux).*

*A discipline note. Every verb here is pinned to a bounded frame. The one number this document produces is a bound, not a measurement, and the section that states what is not claimed is at the end and is not decoration.*

---

## I. Why This Document Exists

`Supplement-Mass` derives the Equivalence Principle as a degenerate boundary condition rather than a universal law, and then states — without a magnitude — that at high degrees of freedom, *"the Equivalence Principle shatters."*

**A prediction with no predicted magnitude is not a prediction.** It is a hope with a coordinate. And in this particular case it is worse than useless, because the Equivalence Principle is among the best-confirmed results in physics — confirmed to roughly one part in $10^{15}$ by the MICROSCOPE satellite and the Eöt-Wash torsion balances, across test masses of radically different composition and internal structure. A framework that says *"the Equivalence Principle shatters"* and declines to say *by how much* is not making a bold claim. It is making an unfalsifiable one, and it is doing so in the one place where physics is watching most carefully.

So: the number.

---

## II. The Equation, Calibrated

From `Supplement-Mass`, the framework's mass relation:

$$R = \frac{P}{I^2}$$

with $P$ the Ledger volume (gravitational mass), $R$ the recompilation cost (inertial mass), and $I$ the system's relational current.

**A required clarification before anything else can be computed.** Read as circuit variables, $R = P/I^2$ gives ohms from watts per ampere-squared, and that is dimensionally sound. Read as a *mass* relation, it says kilograms equal kilograms per ampere-squared, and that is dimensionally broken.

The repair is forced and it is the right one: **$I$ in the mass relation is a dimensionless ratio — the system's relational current expressed against the vacuum baseline** — not a current in amperes. Write $I_0$ for that baseline. Then the physically meaningful relation is

$$\frac{m_i}{m_g} = \left(\frac{I_0}{I}\right)^{2}$$

and the calibration is automatic: at the 0-DoF limit, $I = I_0$ by definition (the particle has no interior with which to modulate its own current), so $m_i / m_g = 1$ exactly. **This is `Supplement-Mass`'s derivation of the Equivalence Principle, now with the constant fixed.**

For a system whose relational current exceeds the baseline by $\Delta I = I - I_0$, expand for $\Delta I \ll I_0$:

$$\boxed{\;\eta \;\equiv\; \frac{m_i}{m_g} - 1 \;\approx\; -\,2\,\frac{\Delta I}{I_0}\;}$$

**The entire prediction reduces to one dimensionless number: the fractional excess of a system's relational current over the vacuum baseline.** Everything else is arithmetic.

### The sign is a prediction, and it is the framework's own

$\eta < 0$, so $m_i < m_g$: **a system with genuine interiority has less inertial mass than gravitational mass, and therefore falls very slightly faster than a 0-DoF object of the same weight.**

This is not an extra assumption. It is exactly what `Supplement-Mass` already says in the institutional register: *"a human institution can have massive historical gravity ($P$) but exhibit incredibly low resistance to a new heading ($R$) if its internal relational current ($I$) is surging."* High current, low resistance, low inertia. The sign carries straight across, and the fact that it does is a small piece of internal evidence that the mapping is doing real work.

---

## III. Identifying $\Delta I / I_0$

The framework says $I$ is elevated above baseline by a system's own internal processing. To get a number, that must be cashed into a physical quantity — and the corpus's own thermodynamics names it: **a bounded frame with a decoupled buffer is paying Landauer Tax, and the rate at which it pays is the rate at which it commits.**

So the natural identification is energetic. Over the system's own characteristic cycle time $\tau = 1/\omega$, the fractional excess of relational current is the energy the system commits per cycle, against the energy it *is*:

$$\frac{\Delta I}{I_0} \;\sim\; \frac{E_{\text{committed per cycle}}}{E_{\text{rest}}} \;=\; \frac{P_{\text{dissipated}} \cdot \tau}{mc^{2}}$$

This is one identification, and it is mine, not the corpus's — see §VI. What makes it usable is that **the answer is robust to the choice.** Four independent accountings follow, spanning eight orders of magnitude in the input, and every one lands below the experimental bound.

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

**It rescues the claim.** The framework was, in effect, asserting that one of the best-confirmed results in physics is false, without saying by how much. It is now asserting something quite different and far more defensible: that the Equivalence Principle holds to a precision far beyond anything yet achieved, and departs from exactness only at a scale nobody can currently reach. *That is what a good prediction from a young framework should look like.* It is consistent with all data, it is specific, it is signed, and it is in principle falsifiable.

**It retires the proposed experiment.** `Supplement-ProofSuiteAudit` suggests weighing *"a living organism vs. its dead mass equivalent."* At $\eta \sim 10^{-18}$ that experiment needs a thousand times better precision than the best measurement ever made; at $\eta \sim 10^{-23}$, a hundred million times. **The experiment must be withdrawn**, and the corpus loses nothing by withdrawing it, because the number is precisely what makes the claim safe to hold.

**It clarifies the equation.** $I$ in the mass relation is a dimensionless ratio against the vacuum baseline, not a current in amperes. Without that, $R = P/I^2$ is not a physics equation at all. With it, it is one, and it computes.

**It converts an attack surface into a position.** The current formulation is the easiest thing in the corpus to make look foolish. The formulation above is the sort of thing a physicist can disagree with *seriously* — which is the only kind of disagreement worth having.

---

## VI. Held as Heading

Stated plainly, so this document can be attacked at the right joint rather than the wrong one:

- **The identification of $\Delta I/I_0$ with committed energy per cycle over rest energy (§III) is not derived from the twelve equations.** It is the most physically motivated reading available of what the corpus says $I$ is, and it is mine. A different identification gives a different number. **What makes the result usable is not the identification but its robustness:** four accountings spanning eight orders of magnitude in the input all land below the bound, and it is difficult to construct a physically motivated $I$ that does not. Difficult is not impossible, and anyone who can construct one has found something.

- **The vacuum baseline $I_0$ is never independently computed here.** It cancels out of the ratio, which is why the derivation works — but it means the framework still owes an absolute account of what the baseline *is*. That account runs straight into the cosmological constant problem, which `QED-CCP` addresses and does not close. **The two open problems are the same open problem**, and this is worth knowing.

- **No claim is made that the effect is real.** The claim is that *if* the framework's mass decomposition is correct, *then* the departure from equivalence has this magnitude and this sign. The framework's mass decomposition is a structural proposal (`Supplement-BorrowedTerms`: the identification of Landauer erasure with inertia is **asserted**, not derived), and this bound inherits that standing exactly.

- **The most testable version of the claim is not the biological one.** $\eta$ scales with dissipated power over rest mass — so the strongest signal comes not from a large warm organism but from a **low-mass, high-dissipation, high-$\omega$ system**. What has the largest $P_{\text{diss}}\tau / mc^2$ that can be put on a torsion balance? That is a better question than the corpse, it is a question an experimentalist can act on, and it is the sharpest successor this document generates.

- The Eötvös bound quoted ($10^{-15}$) is the current published limit. It will improve. **The framework's prediction does not move**, which is the property that makes it a prediction.

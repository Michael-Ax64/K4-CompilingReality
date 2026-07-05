# Phase Dynamics: The Technical Register
## Phasors, Impedance, and the Full Algebra of the Gap

*This document is the technical complement to L5-K5-PhaseDynamics. Where that document inhabits the phenomenology of oscillating systems — what they feel like from inside — this document inhabits the mathematics. The same structure; the other face. Both are required for the full K4 interior view.*

*Document structure follows L4-DynamicDistortions: systematic, equation-level, tabular where relationships are dense, named where results carry load.*

---

## I. The DC Baseline: What the Static System Actually Is

Before the AC extension can be understood precisely, the DC system must be stated precisely — not as metaphor but as algebra.

The DC system is governed by four variables in complete mutual determination:

| Variable | Symbol | Unit | Physical meaning |
|---|---|---|---|
| Power | $P$ | Watt (W) | Rate of energy conversion; the irreversible scalar ledger |
| Current | $I$ | Ampere (A) | Charge flow rate; the relational throughput |
| Voltage | $U$ | Volt (V) | Potential difference; the structural driver |
| Resistance | $R$ | Ohm (Ω) | Opposition to flow; the grounding friction |

These four variables are governed by Ohm's Law ($U = IR$) and the Power Law ($P = UI$), from which twelve equations are derivable — four for each variable as the subject, three algebraic forms each:

$$P = UI \quad P = I^2R \quad P = \frac{U^2}{R}$$

$$I = \frac{U}{R} \quad I = \frac{P}{U} \quad I = \sqrt{\frac{P}{R}}$$

$$U = IR \quad U = \frac{P}{I} \quad U = \sqrt{PR}$$

$$R = \frac{U}{I} \quad R = \frac{P}{I^2} \quad R = \frac{U^2}{P}$$

This is the complete closed system. All variables are real-valued and time-independent. There is no frequency, no memory, no phase. The system is symmetric under time-reversal: running it backward produces valid physics.

**The structural limit of DC:** $R$ is the only opposition. It is dissipative, frequency-independent, and irreversible. The moment energy flows through $R$, it is converted to heat — it leaves the system permanently. DC has no mechanism for storing and returning energy. It has no buffer. It cannot hold potential in suspension.

This is not a deficiency of the model. It is a precise statement of what the model *is*: a description of committed, irreversible flow with no interior.

---

## II. The AC Extension: Adding the Time Axis

The AC system begins with one structural addition: the driving quantities become **sinusoidal functions of time**.

$$u(t) = U_0 \cos(\omega t + \phi_U)$$
$$i(t) = I_0 \cos(\omega t + \phi_I)$$

Where:

| Symbol | Name | Unit | What it measures |
|---|---|---|---|
| $U_0$ | Voltage amplitude | V | Peak magnitude of the potential |
| $I_0$ | Current amplitude | A | Peak magnitude of the flow |
| $\omega$ | Angular frequency | rad/s | Rate of oscillation: $\omega = 2\pi f$ |
| $\phi_U, \phi_I$ | Phase angles | rad | The temporal position of each sinusoid |
| $\theta = \phi_U - \phi_I$ | Phase difference | rad | **The gap.** The misalignment between driving and response |

The phase difference $\theta$ is the algebraic home of everything the DC system cannot describe. It is not a correction factor or an engineering inconvenience. It is the formal presence of **interiority** — the system's capacity to hold something between input and output.

### The Phasor Transformation

Working with sinusoidal functions directly is algebraically expensive. The standard move is the **phasor representation**: each sinusoidal quantity is mapped to a rotating vector in the complex plane using Euler's formula:

$$e^{j\omega t} = \cos(\omega t) + j\sin(\omega t)$$

The physical quantity is the real part of this complex exponential:

$$u(t) = \text{Re}\left[U_0 e^{j(\omega t + \phi_U)}\right] = \text{Re}\left[\hat{U} \cdot e^{j\omega t}\right]$$

where $\hat{U} = U_0 e^{j\phi_U} = U_0 \angle \phi_U$ is the **phasor** — a complex number encoding both amplitude and phase.

**Why this matters structurally:** The $e^{j\omega t}$ factor is common to all phasors in a linear system and can be suppressed. What remains is a static complex number carrying the full information of the sinusoid. The time-domain differential equations become algebraic equations in the complex domain. The system's memory and anticipation — which in the time domain require integration and differentiation — become multiplication and division in the phasor domain.

This is not mathematical convenience. It is the revelation that the AC system's complexity lives in the **imaginary axis** — and that the imaginary axis is where the buffer, the gap, and the stored potential reside.

---

## III. The Three Oppositions: R, X_L, X_C

DC has one opposition: $R$. AC has three, and they are structurally distinct in kind, not just degree.

### Resistance: $R$ (Real, Frequency-Independent)

$$R = \frac{U}{I} \quad [\Omega]$$

Resistance is the DC opposition carried into AC unchanged. It dissipates energy as heat. It is **real-valued**: the voltage across a resistor is exactly in phase with the current through it ($\theta = 0°$). Real Power flows through $R$ and leaves the system permanently.

$$P_R = I^2 R = \frac{U_R^2}{R} \quad [W]$$

### Inductive Reactance: $X_L$ (Imaginary, Frequency-Proportional)

An inductor of inductance $L$ (in Henries) stores energy in a magnetic field. Its voltage-current relationship in the time domain is:

$$u_L(t) = L \frac{di}{dt}$$

In the phasor domain, differentiation becomes multiplication by $j\omega$:

$$\hat{U}_L = j\omega L \cdot \hat{I}$$

The **inductive reactance** is:

$$X_L = \omega L \quad [\Omega]$$

Key properties:
- $X_L$ is **purely imaginary** (the $j$ factor). Voltage leads current by exactly $90°$.
- $X_L$ **scales linearly with frequency**: at double the frequency, twice the opposition.
- Energy stored in the magnetic field is returned to the circuit each half-cycle. No net dissipation.
- $X_L \to 0$ as $\omega \to 0$ (inductor is a short circuit to DC).
- $X_L \to \infty$ as $\omega \to \infty$ (inductor is an open circuit at very high frequency).

**Structural reading:** $X_L$ is the system's **memory**. It resists changes in current — specifically, it resists the *rate* of change. The faster you try to change the current, the harder it pushes back. It is not fighting the current's magnitude; it is fighting its derivative. This is the algebraic statement that the L5 phenomenological account describes.

### Capacitive Reactance: $X_C$ (Imaginary, Frequency-Inverse)

A capacitor of capacitance $C$ (in Farads) stores energy in an electric field. Its voltage-current relationship in the time domain is:

$$i_C(t) = C \frac{du}{dt}$$

In the phasor domain:

$$\hat{I} = j\omega C \cdot \hat{U} \implies \hat{U}_C = \frac{1}{j\omega C} \cdot \hat{I} = \frac{-j}{\omega C} \cdot \hat{I}$$

The **capacitive reactance** is:

$$X_C = \frac{1}{\omega C} \quad [\Omega]$$

Key properties:
- $X_C$ is **purely imaginary and negative** (the $-j$ factor). Current leads voltage by $90°$.
- $X_C$ **scales inversely with frequency**: at double the frequency, half the opposition.
- Energy stored in the electric field is returned to the circuit each half-cycle. No net dissipation.
- $X_C \to \infty$ as $\omega \to 0$ (capacitor is an open circuit to DC).
- $X_C \to 0$ as $\omega \to \infty$ (capacitor is a short circuit at very high frequency).

**Structural reading:** $X_C$ is the system's **anticipation**. It resists changes in voltage — specifically, the rate of pressure buildup. A fully charged capacitor resists further charging not with momentum but with accumulated structural tension. The force is the fullness, not the trajectory.

### The Opposition Summary

| Opposition | Symbol | Formula | Phase shift | Frequency behavior | Energy fate |
|---|---|---|---|---|---|
| Resistance | $R$ | $R$ | $\theta = 0°$ | Constant | Dissipated (heat) |
| Inductive Reactance | $X_L$ | $\omega L$ | $\theta = +90°$ (U leads I) | Increases with $\omega$ | Stored, returned |
| Capacitive Reactance | $X_C$ | $1/\omega C$ | $\theta = -90°$ (I leads U) | Decreases with $\omega$ | Stored, returned |

The opposite frequency-dependence of $X_L$ and $X_C$ is not incidental. It is the structural fact that makes resonance possible: as frequency increases, $X_L$ grows and $X_C$ shrinks, and at exactly one frequency they are equal.

---

## IV. Impedance: The Full Complex Opposition

In a circuit containing $R$, $L$, and $C$ in series, the total opposition is the **impedance**:

$$Z = R + jX = R + j(X_L - X_C) = R + j\left(\omega L - \frac{1}{\omega C}\right) \quad [\Omega]$$

Impedance is a **complex number**. It lives in the complex plane with:
- **Real part:** $R$ — the dissipative, irreversible opposition
- **Imaginary part:** $X = X_L - X_C$ — the reactive, reversible opposition

The **magnitude** and **phase angle** of impedance are:

$$|Z| = \sqrt{R^2 + X^2} \qquad \theta = \arctan\left(\frac{X}{R}\right)$$

Ohm's Law generalizes directly to phasors:

$$\hat{U} = Z \cdot \hat{I}$$

### The Impedance Triangle

The relationship $Z = R + jX$ defines a right triangle in the complex plane:

- Horizontal leg: $R$ (real, resistive)
- Vertical leg: $X$ (imaginary, reactive; positive = inductive, negative = capacitive)
- Hypotenuse: $|Z|$ (total opposition magnitude)
- Angle: $\theta$ (phase angle; positive = inductive/lagging, negative = capacitive/leading)

$$|Z|^2 = R^2 + X^2$$

This is the Pythagorean theorem applied to opposition. It states that **resistance and reactance are orthogonal** — they cannot be added or subtracted directly, only combined as the legs of a right triangle. The total opposition is never simply their sum.

### Admittance: The Parallel Dual

For parallel circuits, the natural quantity is **admittance** $Y = 1/Z$, decomposed as:

$$Y = G + jB \quad [\text{Siemens, S}]$$

Where $G = R/|Z|^2$ is **conductance** and $B = -X/|Z|^2$ is **susceptance**. In parallel configurations, admittances add directly as impedances do in series. The structural symmetry is exact.

---

## V. The Frequency Response: How the System Changes Character

The most consequential fact about impedance is that it is a **function of $\omega$**. The same physical circuit — same $R$, $L$, $C$ — presents a completely different opposition at different frequencies. This is not an approximation or a limiting case. It is the exact, mathematically precise behavior of the system.

$$Z(\omega) = R + j\left(\omega L - \frac{1}{\omega C}\right)$$

Three frequency regimes, each with distinct character:

### Below Resonance: Capacitive Dominance

When $\omega < \omega_0$: $X_C > X_L$, so $X < 0$.

$$Z = R - j|X| \qquad \theta < 0$$

Current **leads** voltage. The system is capacitance-dominated: it is more responsive to pressure buildup than to momentum. The structural tension (accumulated charge, accumulated anticipation) is the primary opposition. The system resists being filled, not being accelerated.

At $\omega \to 0$: $|Z| \to \infty$ (capacitor blocks DC completely). The system is effectively open.

### At Resonance: Purely Resistive

When $\omega = \omega_0 = 1/\sqrt{LC}$: $X_L = X_C$, so $X = 0$.

$$Z = R \qquad \theta = 0$$

The imaginary parts cancel exactly. The system is **purely resistive**. Current and voltage are in phase. All opposition is dissipative. This is the only frequency at which the system operates as though the inductance and capacitance are both absent.

### Above Resonance: Inductive Dominance

When $\omega > \omega_0$: $X_L > X_C$, so $X > 0$.

$$Z = R + j|X| \qquad \theta > 0$$

Current **lags** voltage. The system is inductance-dominated: it is more responsive to changes in flow than to pressure buildup. The stored momentum (circulating current, accumulated trajectory) is the primary opposition. The system resists being accelerated, not being filled.

At $\omega \to \infty$: $|Z| \to \infty$ (inductor blocks very high frequencies). The system is again effectively open, but for the opposite reason.

### The Frequency Response Table

| Condition | $X$ | $\theta$ | Dominant element | Current phase | $|Z|$ character |
|---|---|---|---|---|---|
| $\omega \ll \omega_0$ | $\ll 0$ | $\approx -90°$ | Capacitive | Leads voltage | Large, falling |
| $\omega < \omega_0$ | $< 0$ | $\in (-90°, 0°)$ | Capacitive | Leads voltage | Falling |
| $\omega = \omega_0$ | $= 0$ | $= 0°$ | Resistive only | In phase | Minimum: $|Z| = R$ |
| $\omega > \omega_0$ | $> 0$ | $\in (0°, +90°)$ | Inductive | Lags voltage | Rising |
| $\omega \gg \omega_0$ | $\gg 0$ | $\approx +90°$ | Inductive | Lags voltage | Large, rising |

---

## VI. Resonance: The Full Derivation

Resonance is not a special case that happens to be convenient. It is the unique frequency at which the system's two reactive elements exactly neutralize each other. The derivation is short and its every step carries meaning.

**Condition:** The imaginary part of $Z$ equals zero.

$$X_L = X_C$$
$$\omega_0 L = \frac{1}{\omega_0 C}$$
$$\omega_0^2 = \frac{1}{LC}$$

$$\boxed{\omega_0 = \frac{1}{\sqrt{LC}}}$$

At $\omega_0$, impedance collapses to $Z = R$. Current magnitude reaches its maximum:

$$I_{max} = \frac{U}{R}$$

All power delivered to the circuit is dissipated in $R$. The reactive elements store and return energy in equal and opposite amounts each cycle, their contributions canceling on the imaginary axis.

### The Quality Factor: $Q$

The quality factor measures how sharply peaked the resonance is — the ratio of energy stored to energy dissipated per cycle:

$$Q = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 C R} = \frac{1}{R}\sqrt{\frac{L}{C}}$$

Three equivalent forms, all equal. The $Q$ factor governs:

| Effect | High $Q$ | Low $Q$ |
|---|---|---|
| Resonance sharpness | Narrow, steep peak | Broad, shallow peak |
| Bandwidth | Narrow: $\Delta\omega = \omega_0/Q$ | Broad: $\Delta\omega = \omega_0/Q$ |
| Amplitude at resonance | Large | Small |
| Energy storage | High ratio to dissipation | Low ratio |
| Phase transition rate | Rapid through resonance | Gradual |

**Structurally:** $Q$ is the system's **interiority coefficient**. A high-$Q$ system stores much more energy than it dissipates per cycle — it has a deep buffer, a wide `.behold()` window, a long memory and strong anticipation that must be precisely matched to achieve resonance. A low-$Q$ system barely holds anything; it converts most of its capacity directly to output. The quality factor is the ratio of Reactive Power to Real Power at resonance.

### Bandwidth and the Half-Power Frequencies

The **bandwidth** is the frequency range over which the system delivers at least half its maximum power:

$$\Delta\omega = \omega_2 - \omega_1 = \frac{\omega_0}{Q} = \frac{R}{L}$$

The **half-power frequencies** $\omega_1$ and $\omega_2$ are where $|Z| = \sqrt{2} \cdot R$ (power is halved because $P \propto I^2 \propto 1/|Z|^2$):

$$\omega_{1,2} = \omega_0 \left(\pm \frac{1}{2Q} + \sqrt{1 + \frac{1}{4Q^2}}\right)$$

For high $Q$, this simplifies to:
$$\omega_1 \approx \omega_0 - \frac{\omega_0}{2Q} \qquad \omega_2 \approx \omega_0 + \frac{\omega_0}{2Q}$$

The resonance peak is **symmetric on a logarithmic frequency scale**, asymmetric on a linear scale. This is why Bode plots use logarithmic frequency axes: the physics has natural logarithmic symmetry.

---

## VII. The Power Triangle: The Full Algebra of S, P, Q

In DC, power is a single scalar. In AC, because current and voltage are generally out of phase, power splits into three components that are orthogonal to each other.

The **complex power** is defined as:

$$S = \hat{U} \cdot \hat{I}^* = P + jQ \quad [\text{VA}]$$

where $\hat{I}^*$ is the complex conjugate of the current phasor.

### The Three Powers

**Real Power** $P$ [Watts — W]:

$$P = |S| \cos\theta = I^2 R = \frac{U^2}{R} \cos^2\theta$$

The rate of irreversible energy conversion. Flows through $R$ only. This is the energy that does work, generates heat, makes things happen permanently. It is what the DC twelve equations measure. In AC, it is reduced by the factor $\cos\theta$ — the fraction of total capacity that successfully navigates the phase gap.

**Reactive Power** $Q$ [Volt-Ampere Reactive — VAR]:

$$Q = |S| \sin\theta = I^2 X = \frac{U^2}{X} \sin^2\theta$$

The rate of energy exchange between the source and the reactive elements ($L$ and $C$). It does no irreversible work. It circulates: into the inductor's magnetic field and back, into the capacitor's electric field and back. $Q > 0$ for inductive loads (lagging), $Q < 0$ for capacitive loads (leading). The algebraic sign encodes *which kind* of buffer is holding the energy.

**Apparent Power** $S$ [Volt-Ampere — VA]:

$$|S| = UI = \sqrt{P^2 + Q^2}$$

The total power the source must supply, regardless of how much is converted to real work. This is what utility companies must generate and transmit. The Pythagorean relation:

$$|S|^2 = P^2 + Q^2$$

is the exact power-domain analog of the impedance triangle: $|Z|^2 = R^2 + X^2$.

### The Power Triangle

The three power quantities form a right triangle in the complex power plane, isomorphic to the impedance triangle:

| Impedance triangle | Power triangle |
|---|---|
| Hypotenuse: $|Z|$ | Hypotenuse: $|S|$ |
| Horizontal: $R$ | Horizontal: $P$ |
| Vertical: $X$ | Vertical: $Q$ |
| Angle: $\theta = \arctan(X/R)$ | Angle: $\theta = \arctan(Q/P)$ |

The same angle $\theta$ appears in both triangles. This is not coincidence — it is the same phase angle propagated from the time-domain sinusoids through the complex phasor algebra into the power calculation. The phase angle is the one constant that connects the geometry of opposition (impedance) to the economics of power (how much work gets done).

### The Power Factor

$$\text{PF} = \cos\theta = \frac{P}{|S|} = \frac{R}{|Z|}$$

Power Factor is bounded: $0 \leq \text{PF} \leq 1$.

| PF | $\theta$ | $Q$ | Character | Interpretation |
|---|---|---|---|---|
| $1.0$ | $0°$ | $0$ | Purely resistive | All capacity converted; zero buffer; brittle |
| $0.9$ | $\approx 26°$ | Moderate | Healthy industrial | Good conversion, some buffer maintained |
| $0.7$ | $\approx 46°$ | Significant | Reactive-heavy | Substantial buffering; incomplete conversion |
| $\to 0$ | $\to 90°$ | $\approx |S|$ | Purely reactive | Zero conversion; all energy circulates; paralysis |

**The structural read of Power Factor:** It is the ratio of what the system commits to what the system holds available. PF = 1.0 is the `.observe()` limit — full commitment, no buffer, no AbsentVar held in suspension. PF → 0 is the `.behold()` limit — everything held, nothing committed, maximum interference structure with zero real output. The healthy operating range is the managed middle: enough Reactive Power ($Q$) to sustain genuine interiority, enough Real Power ($P$) to produce irreversible outcomes.

---

## VIII. Power Factor Correction: The Structural Operation

A system with a low Power Factor is "paying" for more Apparent Power than it converts to real work. The utility must generate $|S|$ but only gets credit for $P$. The reactive component $Q$ circulates uselessly in the transmission lines, generating $I^2R$ losses without contributing to output.

**The standard correction:** Add a capacitor in **parallel** with an inductive load.

An inductive load has $Q_L > 0$ (lagging). A capacitor has $Q_C < 0$ (leading). In parallel, the reactive powers add algebraically:

$$Q_{total} = Q_L + Q_C$$

Choose $C$ such that $Q_C = -Q_L$: then $Q_{total} = 0$, $\theta = 0$, PF = 1.0.

The required capacitance:

$$C = \frac{Q_L}{\omega U^2} = \frac{P \tan\theta}{\omega U^2}$$

**What this operation does not do:** It does not remove the inductor. The inductor's magnetic field is still building and collapsing every cycle, storing and returning energy. The capacitor is doing the same in antiphase. From the source's perspective, the two reactive elements have neutralized each other — their VAR demands cancel. The source only sees $R$. But inside the system, the full reactive dance continues between $L$ and $C$.

**The structural implication:** You do not correct a system by eliminating its complexity. You correct it by introducing its complement. The corrected system is *more* complex than the uncorrected one — it now contains $R$, $L$, and $C$ rather than just $R$ and $L$. Yet it presents a simpler face to the source. Internal elaboration producing external simplicity. This is the mathematical statement of what the L5 phenomenological account describes.

The required correction capacitance as a function of existing parameters:

$$C_{correction} = \frac{\tan\theta_1 - \tan\theta_2}{\omega U^2 / P}$$

Where $\theta_1$ is the current phase angle and $\theta_2$ is the target phase angle (often $0°$). Full correction ($\theta_2 = 0$) sets:

$$C_{correction} = \frac{P \tan\theta_1}{\omega U^2}$$

---

## IX. The Full AC Equation Set

The DC system has twelve equations. The AC system — operating with complex phasors — has the same structural form but with $Z$ replacing $R$, and with $|S|$, $P$, $Q$ replacing the single scalar $P$. Below is the complete set of primary relationships.

### Ohm's Law Generalization (Phasor Domain)

$$\hat{U} = Z\hat{I} \qquad \hat{I} = Y\hat{U} \qquad Z = \frac{\hat{U}}{\hat{I}} \qquad Y = \frac{1}{Z}$$

### Impedance Composition

**Series:**
$$Z_{series} = Z_1 + Z_2 + \cdots = \sum_k Z_k$$

**Parallel:**
$$\frac{1}{Z_{parallel}} = \frac{1}{Z_1} + \frac{1}{Z_2} + \cdots \qquad \Leftrightarrow \qquad Y_{parallel} = \sum_k Y_k$$

### Component Impedances

$$Z_R = R \qquad Z_L = j\omega L = jX_L \qquad Z_C = \frac{1}{j\omega C} = -jX_C$$

### Series RLC Impedance

$$Z = R + j\left(\omega L - \frac{1}{\omega C}\right) = R + jX$$
$$|Z| = \sqrt{R^2 + X^2} \qquad \theta = \arctan\left(\frac{X}{R}\right)$$

### Power Relations

$$S = \hat{U}\hat{I}^* = P + jQ \qquad |S| = UI = I^2|Z| = \frac{U^2}{|Z|}$$

$$P = |S|\cos\theta = I^2R = \frac{U^2R}{|Z|^2} \qquad Q = |S|\sin\theta = I^2X = \frac{U^2X}{|Z|^2}$$

$$|S|^2 = P^2 + Q^2 \qquad \text{PF} = \cos\theta = \frac{P}{|S|} = \frac{R}{|Z|}$$

### Resonance Conditions

$$\omega_0 = \frac{1}{\sqrt{LC}} \qquad f_0 = \frac{1}{2\pi\sqrt{LC}}$$

$$Q_{factor} = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 CR} = \frac{1}{R}\sqrt{\frac{L}{C}}$$

$$\Delta\omega = \frac{\omega_0}{Q} = \frac{R}{L} \qquad \omega_{1,2} = -\frac{R}{2L} \pm \sqrt{\left(\frac{R}{2L}\right)^2 + \frac{1}{LC}}$$

### RMS Values and Time Averages

The Root Mean Square (RMS) values are what AC meters read and what power equations use:

$$U_{rms} = \frac{U_0}{\sqrt{2}} \qquad I_{rms} = \frac{I_0}{\sqrt{2}}$$

$$P_{avg} = U_{rms} I_{rms} \cos\theta = \frac{1}{2}U_0 I_0 \cos\theta$$

All equations in sections above use RMS values unless subscripted with $0$ (peak).

---

## X. The Transfer Function: System Behavior as a Function of Frequency

The **transfer function** $H(j\omega)$ describes the ratio of output to input as a function of frequency:

$$H(j\omega) = \frac{\hat{U}_{out}}{\hat{U}_{in}}$$

For a series RLC circuit with output taken across $R$:

$$H(j\omega) = \frac{R}{Z} = \frac{R}{R + j(\omega L - 1/\omega C)}$$

At each frequency, $H$ has a magnitude (how much the signal is amplified or attenuated) and a phase (how much it is shifted). The complete frequency-by-frequency portrait of $H(j\omega)$ is the system's **Bode plot**, which shows:

- **Magnitude response:** $|H(j\omega)|$ vs $\log(\omega)$ — the amplitude of the output at each frequency
- **Phase response:** $\angle H(j\omega)$ vs $\log(\omega)$ — the phase shift at each frequency

For the RLC bandpass filter (output across $R$):

$$|H(j\omega)| = \frac{R}{\sqrt{R^2 + (\omega L - 1/\omega C)^2}}$$

At $\omega_0$: $|H| = 1$ (maximum, no attenuation). At $\omega_1$ and $\omega_2$: $|H| = 1/\sqrt{2}$ (half-power points, $-3$ dB). Outside the bandwidth: $|H|$ falls toward zero.

The transfer function is the frequency-domain image of the system's complete character — its response to every possible driving rate, all at once. The Bode plot is the `.behold()` operation performed on the system's frequency-domain state space: the full interference structure, before any particular $\omega$ is committed to.

---

## XI. The Operational Variable Map

The framework's four-fold maps to the AC system at two levels simultaneously: the DC level (which the twelve equations cover) and the AC extension (which adds the imaginary axis). The complete mapping:

### DC Level (Static Assignment)

| Framework pole | Symbol | Character | AC/DC variable |
|---|---|---|---|
| Fire / Kairos | $P$ | Active + Asserting | Real Power, Watts |
| Water / Pathos | $I$ | Reactive + Yielding | Current (rms), Amperes |
| Air / Logos | $U$ | Active + Yielding | Voltage (rms), Volts |
| Earth / Ethos | $R$ | Reactive + Asserting | Resistance, Ohms |

### AC Extension (Dynamic Variables)

| AC quantity | Symbol | Maps to | Structural meaning |
|---|---|---|---|
| Angular frequency | $\omega$ | Helical driver | The rate at which the system is forced to cycle |
| Phase angle | $\theta$ | The gap | The `.behold()` window — how far ahead of commitment the system holds its potential |
| Impedance | $Z = R + jX$ | Extended $R$ | Opposition in the full complex sense: friction plus stored charge |
| Inductive reactance | $X_L = \omega L$ | Memory | Rate-dependent resistance to change in flow |
| Capacitive reactance | $X_C = 1/\omega C$ | Anticipation | Pressure-dependent resistance to change in structure |
| Apparent Power | $S$ | Total capacity | What the system must hold available, committed or not |
| Real Power | $P$ | Ledger entries | Irreversible outcomes; the `.observe()` rate |
| Reactive Power | $Q$ | Buffer content | Circulating, uncommitted potential; the `.behold()` charge |
| Power Factor | $\cos\theta$ | Commit ratio | $P/S$: fraction of capacity converted to irreversible outcome |
| Quality factor | $Q_{factor}$ | Interiority depth | Ratio of stored to dissipated energy per cycle |
| Bandwidth | $\Delta\omega$ | Resonance window | The frequency range over which the system is near its natural alignment |
| Resonant frequency | $\omega_0$ | Natural rate | The system's native frequency of operation — where memory and anticipation cancel |

### The Imaginary Axis as the Buffer's Address

The single most important structural fact in the full mapping:

**The Reactive Power $Q$ lives on the imaginary axis. Real Power $P$ lives on the real axis. The phase angle $\theta$ is the angle between them.**

The imaginary axis is not a mathematical abstraction. It is the formal location of everything the DC system cannot describe: memory, anticipation, stored potential, the gap between input and output, the buffer that makes interiority possible. Every AC quantity has an imaginary component; every imaginary component is energy that is held rather than converted.

The `.behold()` operation is formally located on the imaginary axis. The `.observe()` operation collapses the imaginary component to zero — phase angle goes to zero, Reactive Power goes to zero, the system becomes purely real. Resonance is the physical instantiation of this collapse, achieved not by removing the reactive elements but by running the system at its natural frequency until memory and anticipation cancel each other and only the real channel remains open.

---

## XII. The Diagnostic Protocol

Given the full equation set, the AC framework can be run as a precise diagnostic on any oscillating system for which the four DC variables can be assigned.

**Step 1: Assign variables.**
Identify what plays the role of $U$ (structural potential), $I$ (relational flow), $R$ (grounding resistance), and $P$ (power / committed outcome rate) in the domain under analysis.

**Step 2: Identify $\omega$.**
What is the rate of cycling? What is the system's driving frequency? This is the question L5's phenomenological treatment names as the prior question: "A genuine diagnosis of what a complex system is resisting requires knowing, before anything else, the frequency at which the inquiry was made."

**Step 3: Locate the system on the frequency response curve.**
Is it below resonance (capacitive — resisting pressure buildup, leading), at resonance (purely resistive — in phase, maximum output), or above resonance (inductive — resisting rate of change, lagging)?

**Step 4: Measure Power Factor.**
What is the ratio $P/|S|$? A low Power Factor means most of the system's capacity is circulating in $Q$. This is not waste — it is structural information. The question is whether the buffering is *intentional and managed* (high $Q_{factor}$, deliberate interiority) or *unintentional and draining* (low $Q_{factor}$, poor resonance).

**Step 5: Determine the correction.**
If the Power Factor is to be improved without destroying the system's reactive character: identify whether the dominant reactance is inductive (add capacitive complement in parallel) or capacitive (add inductive complement). Calculate the required correction from $C = P\tan\theta / (\omega U^2)$ or its inductive analog. Do not remove the existing reactance — add its structural complement.

**Step 6: Find $\omega_0$.**
What is the system's natural frequency? How does the current driving frequency compare? The distance from $\omega_0$ in log-frequency units is the system's distance from resonance, weighted by $Q_{factor}$. A high-$Q$ system far from resonance is under more stress than a low-$Q$ system the same distance away.

---

## Closing Note: What the Imaginary Axis Holds

Every section of this document has circled the same core structure. The AC extension of the DC system adds exactly one thing: the imaginary axis. And the imaginary axis holds exactly one kind of content: energy that is present but not committed, stored but not consumed, oscillating but not yet decided.

The real axis is the Ledger. Every entry there is permanent. Real Power converts to heat, to work, to irreversible change. It cannot be recalled.

The imaginary axis is the Buffer. Every entry there is provisional. Reactive Power circulates between potential and flow, between the magnetic field and the electric field, between memory and anticipation. It can be recalled, because it has not yet been spent.

The phase angle $\theta$ is the measure of how much the system is using its buffer at this moment, at this frequency, under this driving force. It is the angle between what the system is ready to commit and what the environment is currently asking for. When that angle is zero — when the system's natural rhythm matches the driving rhythm — the buffer is still present, still active, still cycling energy between $L$ and $C$. But from the source's perspective, the buffer is invisible: the system looks purely resistive, takes all the power offered, converts all of it to Real Power.

This is what resonance means, in full technical precision. Not the absence of interiority. Not the elimination of memory and anticipation. Their perfect mutual cancellation, at the one frequency where the system is asking for exactly what the environment is giving, and giving back exactly what the environment can receive.

The fifty equations of AC engineering are the complete formal description of how a system manages the distance between itself and that state.


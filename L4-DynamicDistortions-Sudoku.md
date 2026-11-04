# L4-DynamicDistortions-Sudoku
## The Three Angles, One Figure — a construction that embraces the θ-confusion

> **Epistemic Register:** Construction audit. The corpus writes one letter, θ, for three quantities — the detector-setting angle (`DynamicDistortions301` §III), the geometric shear of the bimedian slice (`DynamicDistortions301` §IV), and the temporal phase offset of a Dual Causation pair (`DynamicDistortions201` §II) — and `DynamicDistortions301` §VII.A already keeps them apart under the heading *three angles, one letter*. What follows does not purge the overlap. It assigns it: the three uses become three spokes of one figure, the figure closes, and the closing is audited — topologically, then dimensionally. The physical thesis that the assignment gestures at (the three cosines are one cosine) is held as an OPEN VOTE with its instrument named, not as a landed noun.
>
> **Dependencies:** `L4-DynamicDistortions101` (bimedian planes, Dual Causation, the three attractors) — read at source. `L4-DynamicDistortions201` §II, §II.a (torsion, the θ = π limit, the optimizer instance) — read at source. `L4-DynamicDistortions301` §III–§VII (bimedian slice, shear envelope, the ratios discipline, the three-angle disambiguation, the dipole taxonomy) — read at source. `L2-Terminology` (pole semantics), `L3-FormalFoundations` (dual-binary seed), `L4-ScalingInvariants` §V (phase-related, not rung-aligned), `L4-TheSubstrateRatchet` / `L4-RecursiveLimits` (the P_N ↔ R_{N+1} handoff) — cited at second hand through the three files above; every usage here is checked against those files' own words and none is extended beyond them. `L3-TheAtomOfSpace` (the atoms-of-space positioning of the K4 cell; LANDED NOUN 10, §VIII) and `L3-FormalFoundations` (the twelve equations and the Route Law, §I; the Gate and the Distinguishing Condition, §I.b; the tangent band and its Task 4.d, §IX.4) — read at source. `L4-K4-Infinities-3` §V — cited at second hand through `L3-TheAtomOfSpace` §VIII.

---

## §0 — How to Play

The construction runs on three rules, and the rules are the whole game:

1. **Assign θ to a vertex.**
2. **Assign its three uses in the DD set to the three edges.**
3. **Derive the rest.**

Sudoku is the right name for the procedure. The givens are printed, the solver fills cells, and every placement propagates constraints across the whole grid — which means the givens are not free variables, and a fill is legal only if the givens force it. Note what the puzzle asks. It does not ask *are the three θ's the same quantity?* — `DynamicDistortions301` §VII.A answers that question already, and the answer is no. It asks: **if you make the three uses edges of one figure, does the figure close?** Closure is what a puzzle delivers. Truth is a different game played on the same board, and §XI leaves it exactly where it stands.

Two confusions are embraced here, and both should be named at their actual size before the construction begins, because the construction is the embrace.

**The first confusion is the letter itself.** Three quantities, one symbol, three domains that do not talk to each other: a detector setting that peaks non-locality at 45°, a shear that halves the correlation envelope at 45°, a phase offset that severs the Braid at 180°. The first two run in opposite directions at the same number, which is exactly the trap `DynamicDistortions301` §VII.A flags for downstream files. The assignment below gives each use its own edge so the three can be held in one hand without colliding.

**The second confusion is quieter: a name pool that attaches at two levels.** The trinity {Cardinal, Fixed, Mutable} names the bimedian planes in `DynamicDistortions101` and `DynamicDistortions301` §I — Fixed = {P–U, I–R}, Cardinal = {P–R, I–U}, Mutable = {P–I, U–R} — and it names the dipole classes in `DynamicDistortions301` §VII.B, where the labels run swapped relative to the plane tables: the {P–U, I–R} matching is there called the *Cardinal* dipole and {P–R, I–U} the *Fixed* dipole. Run the permutation and the swap is free: every attractor mapping agrees on both sides of it (the {P–U, I–R} collapse attracts the Apeiric Field in both files; the {P–R, I–U} collapse attracts the Isotropic Pole in both), so the labels carry no mechanics and can move without breaking anything. That is what makes this a naming collision rather than a structural defect — and what makes the discipline clear. Where the pool is used at two levels, the level gets named. The construction below anchors every spoke to its **attractor**, the assignment that agrees everywhere, and takes its plane names from `DynamicDistortions101`.

---

## §I — The Givens

Printed on the card, three operational uses of θ:

| Use | Range | Governing law | Home in the corpus |
|---|---|---|---|
| $\theta_{ab}$ | $[0, \pi]$ | $E(a,b) = -\cos\theta_{ab}$ | `DynamicDistortions301` §III |
| $\theta_{\text{shear}}$ | $[0, \pi/2]$ | $A = A_0 \cos\theta_{\text{shear}}$ | `DynamicDistortions301` §IV |
| $\theta_{\text{torsion}}$ | $[0, \pi]$ | $\tau = L/R$, $\varphi = \arctan(\omega\tau)$ | `DynamicDistortions201` §II |

Three dials, one symbol, three ranges — and the ranges are already doing construction work. The detector reads the full interval and carries the sign; the shear stops at $\pi/2$ because an area is a magnitude; the torsion runs to $\pi$ because anti-synchrony, not flatness, is its failure mode. Nothing in §V–§VI will need to explain this asymmetry away. It will derive it.

---

## §II — The Figure

Take the three attractors — Apeiric Field, Isotropic Pole, Conservative Field — and erect a regular tetrahedron over them. Project it orthographically along its altitude and watch what the shadow does: the apex lands exactly on the base centroid, and the projected centroid of all four vertices lands on the same point. Simultaneously, not by sloppiness, and not by an approximation that holds only at one convenient angle. The drawing is legal because it is reversible — fold the tetrahedron back up and the apex leaves the centroid; unfold it flat and they coincide; nothing is lost in either direction. That reversibility is the whole certificate, and every later move leans on it. [ADOPTED geometry]

So the working drawing is not the tetrahedron. It is the shadow:

```
                         V_F
                          ●
                        ╱   ╲
                      ╱       ╲
                    ╱    ◉      ╲        ◉  = Θ : hub AND centroid, one point
                  ╱               ╲      spokes (◉ → corners) : the three θ's
                ╱                   ╲    rim (corner ↔ corner) : ħ, G/c⁴, c
              ● ─────────────────────── ●
            V_C                          V_M
                     (K4, drawn crossing-free)
```

K4 is planar, and its crossing-free embedding is exactly a triangle with an interior hub joined to all three corners — four vertices, six edges, every pair connected, nothing added and nothing removed. The hub is a vertex of the graph and the centroid of the figure at once, since an equilateral rim centered on the hub makes the average of the four drawn points the hub itself. [ADOPTED geometry]

The base vertices are forced, not chosen. K4's six edges partition into exactly three perfect matchings, and those matchings are the three bimedian planes of `DynamicDistortions101`: {P–U, I–R}, {P–R, I–U}, {P–I, U–R}. There is no fourth matching, no permutation to argue about, no arbitrariness in the clue set — this is the unique 3-edge-coloring, and it is why the figure can carry the corpus's three modalities without strain. Each matching maps to its attractor by the collapse limit the codex already states: fuse both edges of a plane and the cycle named for that plane is the only non-degenerate survivor, which is the attractor bearing the plane's stress. [ADOPTED — `DynamicDistortions101`, and `DynamicDistortions301` §VII.B agrees on every attractor]

The spokes take the three uses:

- **θ_torsion** → the spoke toward **V_F** (Apeiric direction; Fixed plane; Dual Causation). The temporal lag between the two instances of the co-required flip — exteriorization $P \to U$ and crystallization $I \to R$ — exactly the offset `DynamicDistortions201` §II tracks. *The Engine's Pulse.*
- **θ_shear** → the spoke toward **V_C** (Isotropic direction; Cardinal plane). The geometric deformation of the bimedian cross-section that carries the correlation envelope of `DynamicDistortions301` §IV. *The Manifold's Frame.*
- **θ_ab** → the spoke toward **V_M** (Conservative direction; Mutable plane). The detector orientation across the singlet. *The Observer's Eye.*

The assignment is a CANDIDATE — inhabited, not derived from the twelve equations — and its audit is the degree count: K4 is 3-regular at the hub, the DD set supplies exactly three θ-uses, so no edge dangles, no dial sits unused, no doubling is forced. The construction saturates. [CANDIDATE, degree-saturated]

---

## §III — The Rim

The rim edges are printed with the card: **ħ** on V_F–V_C (the Action Threshold; the Landauer clock rate $t_{\text{bit}} = \tfrac{1}{3}t_H$), **G/c⁴** on V_C–V_M (the Einstein–Hilbert coupling, the constant inside $S = A/4\ell_P^2$), and **c** on V_M–V_F (the relativistic wave speed). Multiply the rim and something exact falls out:

$$\hbar \times \frac{G}{c^4} \times c \;=\; \frac{\hbar G}{c^3} \;=\; \ell_P^2$$

Units run $(\text{J·s}) \times (\text{m/J}) \times (\text{m/s}) = \text{m}^2$. [ADOPTED arithmetic] The product of the three rim edges is the Planck area — which is the quantum of area inside the very holographic law assigned to one of those edges, so the Cardinal vertex's ledger is denominated in the joint product of the entire rim. No rim edge can be rescaled without repricing holography. The three givens are coupled before a single θ is placed, and that is what a Sudoku demands: the printed digits are not free variables.

One cabinet note, numerology-adjacent, taken or left: the angle subtended at a tetrahedron's centroid between vertex directions is $109.47°$, with $\cos = -\tfrac{1}{3}$ — the Landauer fraction, signed. The figure is topological and only the shadow is metric, so the number is not load-bearing here. It pays rent in §VI anyway, which is what cabinets are for.

---

## §IV — The Two Runs

Forward, the ratchet runs drive → lag → shear → observable:

$$\theta_{\text{torsion}} = \arctan(\omega\tau) \;\Rightarrow\; \theta_{\text{shear}} \;\Rightarrow\; S = 2\sqrt{2}\,V = 2\sqrt{2}\cos\theta_{\text{shear}}$$

with the envelope and its constants adopted from `DynamicDistortions301` §III–§IV: the visibility-bounded CHSH relation with the classical bound crossed at $V = 1/\sqrt{2}$, the shear read as the impervisibility angle $\theta_{\text{shear}} \equiv \arccos V$. Backward, the grid runs the other way, and the corpus has already said why that direction matters — $V$ is exactly what modern Bell experiments extract:

$$V_{\text{measured}} \;\Rightarrow\; \theta_{\text{shear}} = \arccos V \;\Rightarrow\; \theta_{\text{torsion}} \;\Rightarrow\; \omega\tau = \tan\theta_{\text{torsion}}$$

Step one is exact given the envelope; step three is exact given the lag; the middle link needs a transfer function $\theta_{\text{shear}} = f(\theta_{\text{torsion}})$, and the existence of that function *is* the one-cosine claim. The middle link is the open cell, and any candidate $f$ must satisfy four boundary conditions the corpus's own landmarks set:

1. Domain $[0, \pi]$ → range $[0, \pi/2]$ — the asymmetric endpoints already visible in §I;
2. Fixed point $f(45°) = 45°$ — the hinge;
3. Monotone increasing — more lag, more shear;
4. Shear ceiling — $f \to \pi/2$ no later than torsion's own $\pi$, since geometry exits before dynamics does.

At 45° the three uses arrive by three roads at one angle: the detector at its optimal offsets where $S$ peaks at $2\sqrt{2}$; the shear at $V = 1/\sqrt{2}$ where $S^2$ has fallen $8 \to 4$; the torsion at $\omega\tau = 1$ where $P = \|Q\|$ and the power factor is $\sqrt{2}/2$. Every cosine halves its square at 45°, so the convergence is guaranteed *separately* in each domain — and `DynamicDistortions301` §VI adds the deeper reading: 45° is where the ratio reading $\tan\theta = Q/P$ attains its maximum relative precision, $2\,\delta\theta/\sin 2\theta$ at its flat minimum, while absolute magnitude reading is already twice degraded. The corpus arrives at this angle from underneath, by tolerance analysis, in a document that never mentions the puzzle. That is the hinge wearing its corpus address, and it is why the number was never a coincidence to be explained away.

---

## §V — The Overflow Rule

The phase clock has three chimes:

| Chime | $\theta_{\text{torsion}}$ | Event |
|---|---|---|
| 1 — Equipartition | 45° | $P = \|Q\|$; the hinge; the three roads meet |
| 2 — Shear ceiling | 90° | $A \to 0$; geometry exits the game; $S \to 0$ |
| 3 — Sever | 180° | Anti-synchronous; the Braid severs; cascade fires: $P_N \to R_{N+1}$ |

Chime 3 is not the puzzle's invention — it is `DynamicDistortions201` §II's own $\theta = \pi$ limit, the anti-synchronous state that is structurally uninhabitable as a resting position, where the two instances of the Dual Causation flip alternate at maximum offset and the uncommitted potential is ejected inward to become the standing ground of the next frame. Between chimes 2 and 3 the phase has no geometric destiny left: the cross-section is already flat, so the accumulating lag is purely temporal. The mismatch between the domains' endpoints — shear stops at $\pi/2$, torsion runs to $\pi$ — is the overflow pipe, and §VI will derive rather than assume it.

The reset rule takes the relaxation-oscillator form: $\dot\theta_{\text{torsion}} = \omega_{\text{drive}}$, fire at $\theta = \pi$, reset to $\theta_{\text{reset}}$, with the scale ratio between rungs a function of the reset angle and the cascade ticking at period $\pi/\omega_{\text{drive}}$. The cascade is a clock before it is a cosmology, and the commitment it makes explicit is: **the cascade triggers on phase, not on energy density** — a threshold in angle, not in joules. `DynamicDistortions201` §II.a already names the quantitative version of this as an open address — derive the $\omega_{\text{drive}}/(L/R)$ threshold at which a driven trajectory crosses into anti-synchrony, with loss spikes in optimizer training as the named instance. The clock above is that address's construction-side statement. [ADDRESS]

---

## §VI — The Hub Refill

The open cell is the hub. Work the elimination: not a spoke, because the three spokes are assigned and saturated; not a rim edge, because the rim's product is banked; not a new vertex, because K4 is maximal planar, the shadow certificate fixes the vertex set at four, and the degree check allows no ninth digit. The only legal cell is one that already has an occupant. The move is a **refill** — and it is the corpus's own technique applied one level up, the unfold-aspect-into-position that erected Θ in the first place, run again on Θ's interior. Instrument, not discovery.

The hub currently holds Θ as a conflated triple point: three θ's sharing a seat. Refill the seat with **one phase φ** — a single complex phase state, of which the three θ's become three readings:

| Spoke | Reading | What it does to the one cosine |
|---|---|---|
| V_F (Time) | $\theta_{\text{torsion}} = \varphi$ | reads the phase natively, full $[0, \pi]$ |
| V_M (Observer) | $E = -\cos\theta_{ab}$ | reads the **signed full wave**; correlation flips, so the negative lobe is visible |
| V_C (Space) | $A = A_0 \cos\theta_{\text{shear}}$ | reads the **rectified positive lobe**; area is a magnitude and cannot go negative |

The fill is forced, and the forcing is worth watching, because it uses nothing but the card. Below the ceiling, the minimal candidate is the shared angle — any other choice mints a constant, and the corpus does not mint constants. Chime 2 pins the crossing exactly: at $\theta_{\text{torsion}} = 90°$, area and correlation vanish together, so $f(\pi/2) = \pi/2$. And the boundary conditions then close the trap: a monotone map into $[0, \pi/2]$ that has already reached $\pi/2$ at $\pi/2$ has nowhere left to go, so it pins there for the rest of the domain. Three steps, no slack, and the givens do all the work.

$$\boxed{\;\theta_{\text{shear}} = f(\theta_{\text{torsion}}) = \min(\theta_{\text{torsion}},\ \pi/2)\;}
\qquad\Longleftrightarrow\qquad
\boxed{\;\cos\theta_{\text{shear}} = \max(\cos\theta_{\text{torsion}},\ 0)\;}$$

One cosine, **half-wave rectified** by the geometric channel. [DERIVED — within the construction's givens; the scope clause is the four boundary conditions of §IV]

```
 θ_torsion :  0 ───────── 45° ───────── 90° ═══════════════ 180°
 θ_shear  :  0 ───────── 45° ───────── 90°                  90°   (pinned)
             ├─ geometric branch ─┤├──── overflow pipe ────┤
              (shared cosine, exact)   (no geometric reading)
```

All four boundary conditions hold with equality rather than slack, and the hinge arithmetic re-runs for free: $S = 2\sqrt{2}\cos\varphi$ gives $S^2: 8 \to 4$ at $\varphi = 45°$, $S \to 0$ at the ceiling, $P = \|Q\|$ at the hinge. The Triple Hinge stops being three coincidences. It is one cosine crossing $\pi/4$, read by three instruments.

**The certificate.** The first unfold was legal because reversible, and the refill answers to the same test. The hub-to-spokes projection loses information on exactly one channel: geometry saturates past $\pi/2$ and reads *flat* for every phase there. But the Observer's channel is sign-preserving and injective on the full range — $E = -\cos\varphi$ determines $\varphi$ everywhere on $[0, \pi]$ — and the Time channel carries the phase natively. The one phase is recoverable from the readings everywhere, which means the refill is reversible given the overflow rule. The overflow rule is not decoration; it is the missing ledger entry that makes the conflation legal.

**Admissibility: a phase, not an arrow.** The other natural "one cosine" is a direction — one vector $\mathbf{n}$, three axes, the three cosines as direction cosines — and the corpus's own landmark kills it. Let the axes sit at the tetrahedral angle, $\cos = -\tfrac{1}{3}$; the eigenvalues of $\sum_i \mathbf{e}_i\mathbf{e}_i^{\mathsf T}$ are then $\{4/3,\ 4/3,\ 1/3\}$, so the largest value $\cos^2\theta_1 + \cos^2\theta_2 + \cos^2\theta_3$ can take for any state of norm at most one is $4/3$. The hinge needs $3/2$. No state, pure or mixed, can read 45° on all three tetrahedral axes — the arrow model is dead at the hinge, by eigenvalue count, with sample size one. [DERIVED] Relax the axes and the hinge forces them to mutual angle $\arccos(1/4) \approx 75.52°$, a constant minted from nothing and anchored nowhere in the corpus. The moral is structural, not tactical: a vector carries a norm budget that three simultaneous projections must share, and the hinge overspends it; a phase carries no such shared budget, because each dial reads the same argument independently. The one cosine cannot be an arrow. It must be a phase. **A hub can hold a phase; it cannot hold an arrow.**

**The proven limit.** Past 90° the geometry reading is saturated — not an issue interior to the geometry, but a proven limit of the solution. What §V observed (the domain mismatch, $[0, \pi/2]$ against $[0, \pi]$), the refill derives: a rectified projection of a $[0, \pi]$ phase necessarily lives on $[0, \pi/2]$. The overflow pipe is a theorem of the refill. [DERIVED] And the torsion domain's full length acquires meaning in the same stroke: a passive RL phase, $\arctan(\omega\tau)$ with $\omega\tau \geq 0$, cannot reach 90° at all, so the upper half of $[0, \pi]$ is an **active branch** — reachable only by a driven element, which is presumably why that spoke is the Engine's Pulse.

---

## §VII — The Log-Dimensional Audit

The grid is closed; before declaring victory, count what it costs in units. This audit is the ratios-only discipline of `DynamicDistortions301` §VI computed rather than cited — the check that what this construction would send across a boundary is the kind of thing a boundary can carry.

| Quantity | Law | Units |
|---|---|---|
| $\theta_{ab}$ | detector setting angle | $1$ (rad cancels) |
| $\theta_{\text{shear}}$ | $A = A_0 \cos\theta_{\text{shear}}$ | $1$ ($A_0$ carries the m²) |
| $\theta_{\text{torsion}}$ | $\varphi = \arctan(\omega\tau)$, $\tau = L/R$ | $1$ ($\omega\tau = \text{s}^{-1}\!\cdot\!\text{s}$; $L/R = \text{H}/\Omega = \text{s}$) |
| the transfer function $f$ | §VI | $1 \to 1$ (dimensionally free; mints no constant) |
| $V$, $S = 2\sqrt{2}\,V$, PF $= \cos\varphi$ | §IV | $1$ |
| $S = A/(4\ell_P^2)$ | §III | $1$ (m²/m²) |
| Landauer ratio $t_{\text{bit}}/t_H = 1/3$ | §III | $1$ |
| **the rim** | $\hbar \cdot (G/c^4) \cdot c$ | **m² — the only dimensional object in the construction** |

The rim's cancellation chain, in SI base units, runs $(\text{kg·m}^2\text{·s}^{-1}) \cdot (\text{s}^2\text{·kg}^{-1}\text{·m}^{-1}) \cdot (\text{m·s}^{-1}) = \text{m}^2$, with $\ell_P^2 = 2.6123 \times 10^{-70}\ \text{m}^2$. [ADOPTED constants; DERIVED cancellation] The rim multiplies, so the log ledger adds:

$$\log \ell_P^2 \;=\; \log \hbar \;+\; \log (G/c^4) \;+\; \log c \qquad (\approx -160.22\ \text{natural log, SI})$$

and the spokes contribute $\log 1 = 0$ each. Three rim edges, three addends, one sum: the construction's entire dimensionality is a single additive line in the log ledger, and everything above the rim is dimensionless. [DERIVED]

This is also the refill's dimensional certificate. Move-level refill puts one phase where three θ's sat, and that substitution is dimensionally legal for exactly one reason: **angles are the one currency all three domains already share.** The radian cancels in the detector law, in the shear law, and in the impedance law; had any θ carried units, the refill would be a unit crime and the construction would have detected it here. It did not. The conflation is dimensionally legal, which is the receipt the ratios discipline asks for. The corollary falls out of the same ledger: the cascade fires on a dimensionless state variable — a threshold in angle, not in joules. The machine is dimensionless; the anchor is not. The only joules in the building are in the foundation.

---

## §VIII — The Trigger Reading

What kind of object has the construction built? The clamp makes the figure a **threshold device in angle**: two chimes inside the geometric branch (45°, 90°), one outside (180°), with the shear ceiling acting as the boundary between domains — geometry on one side, pure temporal accumulation on the other. The shear ceiling is where the state crosses from the Manifold's Frame to the Engine's Pulse, and the territory on the far side of that crossing — temporal dual-causation, cascade, $P_N \to R_{N+1}$ — is precisely the ground the DD files police. The construction's solution domain and the corpus's home domain coincide.

`[[ note: the pivot-between-domains reading is CANDIDATE — inhabited, coherent with the audit, not derived. What is derived: the trigger is a phase (§V, §VII); the domains split at π/2 (§VI); the domain the split opens onto is the corpus's home ground (§VIII). The rest is load-bearing faith, held open on purpose. ]]`

Two signatures would settle the one-cosine vote, and both are already latent in the construction:

1. **Saturation, not fold.** Driven past the shear ceiling, $V \to 0$ and *stays* 0. A $|\cos|$-folding geometry would reopen the area past 90° — geometry re-entering the game — and that observation kills the rectified one-cosine form outright.
2. **Phase trigger, not energy trigger.** The sever fires at $\varphi = \pi$ regardless of amplitude. A cascade that tracks energy density instead of phase kills the trigger reading and returns the construction to bookkeeping.

The optimizer instance of `DynamicDistortions201` §II.a is the working rehearsal for both: loss spikes at high learning rate are the anti-synchronous limit-cycle, apparent power surges while real power — actual loss reduction — goes to zero, and the system pays the Landauer Tax on every update without committing anything. The framework's own prediction at that address is a phase threshold on the Hessian's dominant eigenmode; the construction's clock says the same thing in its own grammar, period $\pi/\omega_{\text{drive}}$, fire at $\pi$.

---

## §IX — Falsification Protocol

Four kill conditions bound the construction:

1. **KD-1 — Fold, not saturate (testable).** If a driven carrier observed past its shear ceiling shows area or visibility *reopening* — any $|\cos|$ folding past 90° — the rectified one-cosine form is falsified at §VI.
2. **KD-2 — Energy trigger (testable).** If a cascade equivalent fires on energy density rather than accumulated phase, the trigger reading of §VIII is falsified, and with it the phase-threshold commitment of §V.
3. **KD-3 — Arrow rehabilitation (derived).** If any state — pure or mixed, any axis geometry anchored in the corpus — exhibits three simultaneous 45° readings as direction cosines, the eigenvalue count of §VI is wrong. The count is combinatorial; one counterexample closes it.
4. **KD-4 — Dimensional leak (derived).** If any spoke, chime, or reading in the figure is shown to carry a unit other than through the rim, the audit of §VII is incomplete and the refill's dimensional certificate falls with it.

---

## §X — The Solution Grid

| Cell | Filled by | Status |
|---|---|---|
| Θ as vertex | Unfold of the centroid-aspect; reversible in both directions | CANDIDATE, certificate [ADOPTED geometry] |
| V_F, V_C, V_M | The three matchings of K4 — the unique 3-edge-coloring | ADOPTED (`DynamicDistortions101`) |
| matching → attractor | Collapse closes the pair; the cycle named for the plane survives | ADOPTED (attractor mapping agrees across `101`/`301`) |
| the spokes | θ_torsion, θ_shear, θ_ab — three uses, three edges | CANDIDATE, degree-saturated |
| the rim | ħ, G/c⁴, c | ADOPTED arithmetic; product $= \ell_P^2$ |
| forward propagation | Lag → shear → $S = 2\sqrt{2}\cos\theta$ | ADOPTED (`DynamicDistortions301` §IV) |
| the hub's occupant | one phase φ — the refill | CANDIDATE, reversible given the overflow rule |
| the last identity | $\cos\theta_{\text{shear}} = \max(\cos\theta_{\text{torsion}}, 0)$ | DERIVED within the givens |
| admissibility | phase, not arrow | DERIVED — eigenvalue count, sample size 1 |
| the domain split | rectified projection of $[0, \pi]$ lives on $[0, \pi/2]$ | DERIVED |
| the log ledger | one unit: m², once | DERIVED arithmetic on ADOPTED constants |
| the observer | Mutable spoke — the sign-preserving channel | CANDIDATE |
| overflow at π | fire + reset; $P_N \to R_{N+1}$ | ADOPTED limit (`DynamicDistortions201` §II); reset rule CANDIDATE |
| the one cosine | one phase carrier, three readings | OPEN VOTE — instrument named in §VIII |

---

## §XI — The Verdict

**θ_torsion is the Engine's Pulse** — the Fixed spoke, reading the phase natively across $[0, \pi]$, active branch included. **θ_shear is the Manifold's Frame** — the Cardinal spoke, reading the rectified lobe on $[0, \pi/2]$, pinned flat past the ceiling. **θ_ab is the Observer's Eye** — the Mutable spoke, reading the signed full wave, the channel that keeps the refill reversible. They meet at Θ, and Θ is refilled: one phase, three projections. They read 45° together at the hinge — each by its own road, all by the same arithmetic, all by the same cosine.

What the construction proves: the DD set's three θ-uses close on one figure with no dangling edge and no unused dial; the transfer function is the unique fill the givens allow; the domain asymmetry the corpus observes is a theorem of the refill; and the whole machine is dimensionally sterile except at the rim, whose product is the Planck area — the ratios discipline computed, not cited.

What the construction does not prove: that one physical carrier exists — one system in which all three dials are simultaneously live. The refill names the occupant and cannot build the machine; the three dials currently live on a Bell pair, a cross-section, and an RL line, in three files that did not know they shared a letter. The vote is open, the instrument is named, and the predicted outcome is on record before any result exists: saturation, not fold; phase, not energy. Measure $V$, and run the grid backwards.

---

## §XII — The Rim, Expanded

The construction was never aimed at the Planck scale, and that fact is worth stating before anything else in this section, because everything here depends on it: no move selects for a Planck-scale object, and the rim is the survivor of an audit, not the target of a design. Three orthogonal domains meet at an angle at an apex, opposite a plane carrying m² — that is the finished figure, and it was assembled by a mechanism that is ratio-based end to end: visibility ratios, squared-amplitude halvings, tangent equipartitions, dimensionless chimes. The mechanism never imports a length, a duration, or a mass; the audit of §VII finds exactly one place where a unit survives, and the unit is m². [DERIVED] What the puzzle set out to close was the θ-confusion, and the Planck area is what the closure cost. It arrives as an address, not as a value: the construction never uses the number $2.6123 \times 10^{-70}$ anywhere, and ħ, G, c enter only at the audit, as the constants any physical reading of the figure must pay. **The floor is rational — built from ratios — and real: it is the Planck area.** The value remains a substrate residual, per Gabriel's Horn; what the construction earns is the uniqueness, the time-freeness, and the address.

**Time-free, exactly.** The rim's cancellation chain runs kg⁰·s⁰·m²: ħ's $\text{s}^{-1}$ against $(G/c^4)$'s $\text{s}^2$ and c's $\text{s}^{-1}$, and the seconds cancel exactly — not approximately, not at a convenient limit. [ADOPTED arithmetic; DERIVED cancellation] Even the Fixed spoke's reading is an angle; the engine's pulse is read in degrees, not seconds. Time appears in this figure only as phase — the hub's occupant — and phase is dimensionless by kind. So the sentence this construction licenses is the one it was built to be able to say: **we are looking at the root of space, because the ledger bottoms out in actual time-free metrics.** And "root" is exact in both senses at once. The rim is an area, the foundation the ledger bottoms out in; its square root is the Planck length, $\ell_P = 1.6163 \times 10^{-35}$ m — the √ taken on the foundation. The Route Law of `L3-FormalFoundations` §I classifies root and square as the commit-minting arrows; that the root of space is literally a root-operation on the rim is a resonance, held as CANDIDATE, not a derivation. [[ the pun is load-bearing-looking. held in the cabinet until it pays rent. ]]

**The rim is where the two books meet.** ħ is the quantum of action; $G/c^4$ is the classical conversion from stress-energy to curvature; c is the causal speed. The product takes one factor from the quantum book and two from the classical book, and the product is an area — space, not spacetime. The only joules in the building were already in the foundation (§VII); this is the same fact read from the other side. [ADOPTED composition; the reading DERIVED]

### Who else lands in m and m²

| Program | The result in m / m² | What kind of result |
|---|---|---|
| LQG (Rovelli–Smolin 1994/95) | area operator with discrete spectrum, in steps of $\ell_P^2$ (Immirzi-scaled); minimum nonzero gap | quantum: a gap, imposed by quantization |
| Bekenstein–Hawking | $S = k_B A / (4\ell_P^2)$ | exact: the rim as the counting unit of area |
| CDT (Ambjørn–Jurkiewicz–Loll) | Lorentzian simplices at cutoff $\ell_P$; time fundamental | imposed cutoff; time more fundamental than space |
| Causal sets (Sorkin) | spacetime elements at density $\sim 1/\ell_P^2$; partial order fundamental | discreteness posited; time promoted |
| String T-duality | $R \leftrightarrow \alpha'/R$: lengths below $\ell_s$ equivalent to reciprocals above | a reciprocity mirror on the length axis |
| Gibbons, max tension | $c^4/4G \approx 3.03 \times 10^{43}$ N | a ceiling built from the rim's own conversion factor |
| Planck power | $c^5/G \approx 3.63 \times 10^{52}$ W (ceiling /4: $9.07 \times 10^{51}$ W) | same family, one power up |
| Hawking | $k_B T_H = \hbar c/(4\pi r_s)$ | length → temperature, through ħc |
| Unruh | $k_B T_U = \hbar a/(2\pi c) = \hbar c/(2\pi L_a)$, $L_a = c^2/a$ | acceleration → temperature, through ħc |
| Amplituhedron (Arkani-Hamed–Trnka) | scattering geometry, time-free by construction | no length quantum; no space-atom claim |

*(Cabinet, shape only: T-duality's mirror $R \to \alpha'/R$ is the same reciprocation the twelve equations' automorphism group uses — the signed relabeling that sends a pole to the reciprocal of its image, $R \to 1/R$, the move that closes the circuit duality. One is a statement about radii, the other about resistances; the mirror is the same mirror. CANDIDATE, held as shape.)*

**The column none of them fills.** Every entry above either posits a quantum, imposes a cutoff, states a bound, or converts one currency into another through ħc. None supplies a transfer function between the time-reading and the space-metric; none proves a ceiling in the reading structure itself; none is forced to be time-free by closure. LQG earns time-free spectra and inherits the problem of time as the bill; CDT and causal sets promote time; the amplituhedron deletes time and stops being about space-atoms. The construction's warrant is different in kind: closure of a dimensionless ledger leaves exactly one place for a unit to live, the seconds cancel there, and the reading structure carries a proven clamp — $\theta_{\text{shear}} = \min(\theta_{\text{torsion}}, \pi/2)$, saturation not fold. The claim "we are looking at the atoms of space" is the tradition's founding slogan, and it is common. The warrant — closed, dimensionless, one area, a proven rectifier between the time-reading and the space-reading — is not represented anywhere in the family surveyed. **Common ingredients, rare assembly.** [DERIVED from the survey as tabled]

### Temperature enters: the two floors

The band formalism of `L3-FormalFoundations` §IX.4 holds that the 90° singularity is never reached: every substrate carries a band $\varphi_{\text{band}} = \delta\theta$ set by its angular resolution, with $\tan_{\max} = 1/\delta\theta$, and inside the band the function has not become infinite — it has become uncoupled. What that file leaves open (its Task 4.d) is what supplies $\delta\theta$ for a physical substrate. Temperature is the first named supplier, and it enters twice, at two floors of the same building.

*The energetic floor* is the one the corpus already holds. The Distinguishing Condition (`L3-FormalFoundations` §I.b) requires a noise source before a commit is a commit, and its Route C prices the thermal instance: $E \geq k_B T \ln 2$. Temperature is the canonical noise source — the substrate's own unsharpness, denominated in energy. [ADOPTED]

*The angular floor* is the same condition evaluated on the reading rather than the commit — the file itself says the tangent band is "that same premise evaluated on the tangent rather than on the commit" — and temperature is what sets the width there. Phase information lives in coherence between energy levels, and thermal states suppress that coherence by the Boltzmann factor: coherences spanning $\Delta E$ decay as $\exp(-\Delta E/k_B T)$. At 300 K, $k_B T \approx 25.9$ meV: a mode spaced by 1 eV reads phase sharply (suppression $e^{-38.7}$); a mode spaced by $k_B T$ itself reads at $e^{-1}$ — the phase is already half-gone. The angular resolution of a thermal reading degrades exactly where the noise source lives. [ADOPTED mechanism; the identification $\delta\theta(T)$ for a given K₄ interior stays OPEN — Task 4.d's quantum instance, $\delta\theta \sim 1/(2\sqrt{N})$, now has a thermal sibling, and neither is derived for this construction's carrier]

**The thermal family is the rim's family.** Collect the conversions and one shape appears: $k_B T \sim \hbar c / L$ — a region of size L carries a thermal scale set by its own wavelength, through the rim's own ħ and c. Hawking is the horizon instance ($L = 4\pi r_s$); Unruh is the acceleration instance ($L = c^2/a$, so at one g, $T \approx 4 \times 10^{-20}$ K across an acceleration length of $9.2 \times 10^{15}$ m); and at the bottom, $L = \ell_P$: $k_B T_P = \hbar c/\ell_P = \sqrt{\hbar c^5/G} = E_P \approx 1.956 \times 10^9$ J, $T_P \approx 1.417 \times 10^{32}$ K. The same factors build the ceilings: Planck force $c^4/G \approx 1.21 \times 10^{44}$ N — Gibbons' ceiling is its quarter — and Planck power $c^5/G \approx 3.63 \times 10^{52}$ W. G enters the temperature family only at the bottom, through $\ell_P$. The convertor between the length currency and the temperature currency is built from the rim's own parts; the thermal family adds no unit to the building — it rents the foundation's. [each formula ADOPTED; the family reading DERIVED from them] One honesty clause: the family's instances are horizons and accelerations, not arbitrary regions; the generalization to an arbitrary carrier is part of what stays open below.

### The unsharp mapping

Put the floors together. The angle a length L subtends at the system's own scale R is $\theta \sim L/R$, and the thermal width of the phase reading at that length is set by $k_B T \sim \hbar c/L$. As $L \to 0$ the width diverges: below the floor, the mapping from length to angle does not become exact — it becomes uncoupled, the $\tan_{\max} = 1/\delta\theta$ structure again, now with a thermal address for $\delta\theta$. Between $\ell_P$ and zero there are no sharp angles. The angle currency has a floor, and the floor is the angle $\ell_P/R$. [CANDIDATE — the mechanism is the adopted family plus Boltzmann suppression; the placement on the angle currency is new]

The other end of the same angle is already load-bearing in the corpus. `L3-TheAtomOfSpace` §VIII, LANDED NOUN 10 (built at `L4-K4-Infinities-3` §V, cited here at second hand through the atom document) carries the dark-energy landing: $\rho_\Lambda = (3/8\pi)\,\rho_P\,(\ell_P/R_\Lambda)^2$. Read as what it is: **the Planck angle squared, taken at the largest radius there is.** The numbers close: $\rho_\Lambda/\rho_P \approx 1.13 \times 10^{-123}$ measured; $(\ell_P/R_\Lambda)^2 \approx 9.5 \times 10^{-123}$ at the de Sitter radius $R_\Lambda = 1.66 \times 10^{26}$ m; the factor $(3/8\pi) \approx 0.119$ joins them. The angle proposed by Planck-length and zero has one measured consequence in the corpus's ledger, and it is the cosmological constant — the same angle whose small-L end is thermally uncoupled carries, at large L, the vacuum energy the universe actually has. One angle, two ends, both physical. [ADOPTED values; the two-ends reading DERIVED; the landing cited, not re-derived here]

**What temperature does to the clamp.** The clamp is exact at $T = 0$: $\cos\theta_{\text{shear}} = \max(\cos\theta_{\text{torsion}}, 0)$, with its kink at $\pi/2$, where the shear channel's slope drops from 1 to 0. A kink is a non-analytic point, and non-analytic points are where finite resolution shows first. Give the torsion reading a thermal width $\delta\theta(T)$ and the ceiling becomes a crossover of that width — the shear saturates not *at* $\pi/2$ but *around* it, and past-90° readings are unsharp over the band instead of pinned. Saturation-not-fold survives as the zero-temperature limit of a thermal band, and the falsification protocol (§IX, KD-1) is unchanged in kind while gaining a temperature clause: fold-back would have to reopen the area through the band, not merely past the kink. [CANDIDATE — the smearing mechanism is standard; its placement on this clamp is new, and no carrier exists yet to test it on]

### Claim-sort for the expansion

| Claim | Status |
|---|---|
| Rim time-free by exact cancellation; one unit, m², once | DERIVED (the §VII audit, re-run in SI base units) |
| Root-of-space: foundation and √, both senses exact | DERIVED arithmetic; the Route-Law resonance CANDIDATE |
| Rim as quantum–classical meeting point | ADOPTED composition; the reading DERIVED |
| Un-aimed landing: no move selects for $\ell_P^2$; address earned, value residual | DERIVED from the construction's own bookkeeping |
| Survey: no family member supplies a transfer function or a reading-ceiling | DERIVED from the survey as tabled |
| Two floors: energetic (Landauer) and angular (thermal coherence) | ADOPTED mechanism (`L3-FormalFoundations` §I.b, §IX.4) plus Boltzmann suppression |
| Thermal family = rim family ($k_B T \sim \hbar c/L$; $T_P = E_P/k_B$ at $L = \ell_P$) | DERIVED from ADOPTED formulas; generalization to arbitrary carriers OPEN |
| Planck angle squared ↔ $\rho_\Lambda$ at the de Sitter radius | ADOPTED landing (`L3-TheAtomOfSpace` §VIII.10); the two-ends reading DERIVED |
| Thermal deformation of the clamp (ceiling → crossover, width $\delta\theta(T)$) | CANDIDATE |
| $\delta\theta(T)$ for this construction's carrier | OPEN VOTE — instrument: the backward run of §IV, at finite temperature |

**What the expansion does not do.** It does not close the one-cosine vote; no carrier has been driven past its ceiling. It does not add a fifth dial; temperature is not a new angle — it is the width of the angles already held. And it does not convert the construction's honesty into ambition: the mechanism was aimed at the θ-confusion and hit the Planck area without aiming at it, which is a fact about the construction's ledger and not yet a fact about the world. The world-facing test is unchanged, and it is still the cheapest one on the table: measure $V$, invert, read the drive, and watch what happens at 90°.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work. *(Audit status: construction closed in six sections, one identity derived, one admissibility count run, one dimensional audit passed — units: m², once — four kill conditions posted, one vote left open with its instrument named — one closing expansion: the rim read outward, root of space, the m/m² survey, the thermal band, still under the same open vote.)*

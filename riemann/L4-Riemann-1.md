# L4-Riemann-1
## Part One — The Purchase

*Reads with `L0-EinsteinTrace`, `L4-K4-Infinities`, `ProofO_HelicalTime`, `L0-ParadoxEngine`, `On_NavierStokes`. Continues in `L4-Riemann-2`.*

---

Every subject has a first line, and the first line is usually where the subject made its first purchase. It is rarely written down as a purchase. It is written down as a definition, and a definition has no price on it, so nobody goes looking for the receipt.

Riemannian geometry is a partial exception. Its first line was written by a man who knew he was buying something, said so, and wrote down what he thought it cost — and the field kept his definition and lost his note. But the decision this part spends most of its pages on is a *second* one, made decades later by people who had no alternative to weigh, and it carries no note because there was nothing yet to write one about. This part reads both, and keeps them apart.

---

## I. Line One

`On_NavierStokes` opens with a method worth copying. It reads the first line of the Clay problem — $\rho \equiv 1$, incompressible flow — not as a simplification but as a deletion. Setting the density constant sends the speed of sound to infinity, which removes the speed limit from the equation and silences the exhaust. The method is to find the housekeeping decision and put a price on it.

Riemannian geometry has a housekeeping decision of exactly that kind, and it is unusually easy to find.

In his 1854 habilitation lecture, *Über die Hypothesen, welche der Geometrie zu Grunde liegen*, Riemann sets up manifolds of any number of dimensions and then has to say how length is measured along a curve. He chooses

$$ds = \sqrt{\textstyle\sum_{ij} g_{ij}\,dx^i dx^j}$$

— the square root of a quadratic expression in the displacements — and in the same breath says what the alternative would have been. In Clifford's translation:

> "The next case in simplicity includes those manifolds in which the line-element may be expressed as the fourth root of a quartic differential expression. The investigation of this more general kind would require no really different principles, but would take considerable time and throw little new light on the theory of space, especially as the results cannot be geometrically expressed."

*The results cannot be geometrically expressed.* That is a precise description of what is being set aside: a way of measuring length that depends on the **direction** of travel and not only on the place. Paul Finsler formalized that case in 1918, under Carathéodory, as a length function $F(x, v)$ in which the direction $v$ is an argument of its own and not an index to be summed away. A way of measuring that depends on direction cannot be written as a geometry of the surface, which is exactly Riemann's reason for setting it aside. Part Two says what it needs instead.

Two things come with the choice, and the second is the expensive one.

**The square.** A quadratic form is a pairing. It takes two directions and returns a number, and it is symmetric: swapping the two directions changes nothing. It erases nothing. A tangent vector keeps its orientation perfectly well; the orientation is simply not an argument of the function that returns its length. A two-slot symmetric pairing is a flat object, and Part Two shows what that means.

**The closure of the parallelogram.** The second thing has nothing to do with length. Transport a direction $v$ a short way along $u$; then transport $u$ the same short way along $v$. In general the two paths do not arrive at the same point. The gap between them is the torsion, $T(u, v)$. Riemannian geometry, as it was later completed into the connection everyone uses, decrees that the gap is zero: every small parallelogram closes.

So there are **two purchases, made sixty-eight years apart.**

The first is Riemann's and it is dated: in 1854 he chose a quadratic line element over the quartic, said what the alternative was, and priced the loss. That one has a flag on it, in his own hand.

The second is the closing of the parallelogram — and **Riemann did not make it.** He had no connection to make it with. There is no affine connection in the 1854 lecture, no covariant derivative, and no torsion; Christoffel's symbols are 1869, Levi-Civita's parallel transport 1917, and the affine connection as a general object that *may* carry torsion is Cartan's, 1922. Until 1922 there was no alternative available to decline. The symmetric connection was not an axiom anyone adopted over a rival; it was the only connection there was, built by people assembling machinery rather than choosing a foundation.

The pairing is excellent and nothing here argues with it. The closing is the purchase this series itemizes — a purchase **nobody signed**, which is a different thing from one made carelessly, and the reason Part Three §V can answer "why did nobody flag it" without anyone having been negligent. Where this file says *line one*, it means Riemann's line element. Where it means the torsion-free connection, it says so.

---

## II. The Machinery, Stated in Full

Before anything gets priced, the standard machinery, so that every later claim can be checked against it.

Take a smooth manifold with a metric $g_{\mu\nu}$ and an **affine connection** $\Gamma^\lambda_{\mu\nu}$ — the rule that says how to carry a direction from one point to a nearby one. A general connection need not be symmetric in its two lower indices, and it need not preserve lengths. Any such connection splits, uniquely, into three independent pieces (Schouten 1954):

$$\Gamma^\lambda_{\mu\nu} = \stackrel{\circ}{\Gamma}{}^\lambda_{\mu\nu} \;+\; K^\lambda_{\ \mu\nu} \;+\; L^\lambda_{\ \mu\nu}$$

```
========================================================================================
                      THE GENERAL AFFINE CONNECTION DECOMPOSITION
========================================================================================

                             General Affine Connection (Γ^λ_μν)
                                             │
         ┌───────────────────────────────────┼───────────────────────────────────┐
         ▼                                   ▼                                   ▼
  Levi-Civita (Γ°^λ_μν)              Contortion (K^λ_μν)                Disformation (L^λ_μν)
  • Metric-compatible                • Carries TORSION (T)              • Carries NON-METRICITY (Q)
  • Torsion-free                     • Antisymmetric in its first       • Changes the length of
  • Built from g and ∂g alone          two indices                        rulers under transport
  • PURE CURVATURE                   • Leaves every length alone        • PURE STRETCH
                                     • THE ORDER OF TRANSPORTS
========================================================================================
```

**The Levi-Civita connection** is the unique connection that is both torsion-free ($T = 0$) and metric-compatible ($\nabla g = 0$):

$$\stackrel{\circ}{\Gamma}{}^\lambda_{\mu\nu} = \tfrac{1}{2} g^{\lambda\rho}\left(\partial_\mu g_{\nu\rho} + \partial_\nu g_{\mu\rho} - \partial_\rho g_{\mu\nu}\right)$$

It is the only connection Riemann and Einstein used. The statement that it exists and is unique is the **Fundamental Theorem of Riemannian Geometry**.

**The contortion** carries the torsion, $T^\lambda_{\ \mu\nu} = \Gamma^\lambda_{\mu\nu} - \Gamma^\lambda_{\nu\mu}$:

$$K^\lambda_{\ \mu\nu} = \tfrac{1}{2}\left(T^\lambda_{\ \mu\nu} + T_{\mu\ \nu}^{\ \lambda} + T_{\nu\ \mu}^{\ \lambda}\right)$$

Contortion is antisymmetric in its first two indices, and that answers the usual defence of $T = 0$ before it is made: **contortion preserves every length.** $\nabla g = 0$ still holds with it switched on. What it introduces instead is a slip — a translational dislocation, a screw pitch, on transport around a small loop. Torsion is no threat to metrology. It leaves every ruler alone. In four dimensions its twenty-four components are pure ordering.

**The disformation** carries the non-metricity, $Q_{\lambda\mu\nu} = -\nabla_\lambda g_{\mu\nu}$:

$$L^\lambda_{\ \mu\nu} = \tfrac{1}{2} g^{\lambda\rho}\left(Q_{\mu\nu\rho} + Q_{\nu\mu\rho} - Q_{\rho\mu\nu}\right)$$

Non-metricity is the failure of the metric to be carried along unchanged: under $Q \neq 0$ a ruler's length changes as it moves, with no force applied. *That* is a threat to metrology, and Part Three tells the story of the man who proposed it first and what happened to him.

---

## III. What $T = 0$ Removes

Here is the derivation. It is three lines, and the rest of the file hangs on it.

Take any scalar field $f$ and compute two covariant derivatives in a row:

$$\nabla_\mu \nabla_\nu f = \partial_\mu \partial_\nu f - \Gamma^\lambda_{\mu\nu}\,\partial_\lambda f$$

Swap the order and subtract. The ordinary partial derivatives commute and drop out. What is left is the antisymmetric part of the connection:

$$\left[\nabla_\mu, \nabla_\nu\right] f = -\left(\Gamma^\lambda_{\mu\nu} - \Gamma^\lambda_{\nu\mu}\right)\partial_\lambda f = -\,T^\lambda_{\ \mu\nu}\,\partial_\lambda f$$

Curvature contributes **nothing** to this. On a scalar there is no index for curvature to act on, so the whole of the commutator is torsion:

> $$\boxed{\;T = 0 \iff \text{second covariant derivatives of scalars commute}\;}$$

The word *scalars* is inside the box on purpose, and it has to be said again outside it.

### On anything with an index, the commutator survives

Run the same computation on a vector field $V^\lambda$ and the result has two terms:

$$\left[\nabla_\mu, \nabla_\nu\right] V^\lambda \;=\; \underbrace{R^\lambda_{\ \sigma\mu\nu}\,V^\sigma}_{\text{rotation}} \;-\; \underbrace{T^\sigma_{\ \mu\nu}\,\nabla_\sigma V^\lambda}_{\text{translation}}$$

On a scalar the first term has nothing to act on and vanishes, which is why the boxed statement is true, and why it is true only there. **On anything carrying an index, the commutator survives $T = 0$, and what survives is curvature.** The Riemann tensor is itself antisymmetric in $\mu\nu$. Setting torsion to zero does not remove antisymmetry from the geometry. It removes it from one of two orthogonal places.

> **$T = 0$ does not make transport commute. It deletes the translational failure to close and keeps the rotational one.**

The crystallographers had both halves sixty years ago, in their own vocabulary (Part Three tells that story):

| Failure to close | Crystal defect | What happens to the loop | What is left over |
|---|---|---|---|
| **Torsion** | dislocation | the parallelogram does not meet | a **gap** — a Burgers vector, a screw pitch |
| **Curvature** | disclination | the parallelogram meets | a **turn** — holonomy, a deficit angle |

Translation and rotation. They are the two halves of the affine group, and Poincaré gauge theory gauges them separately: the translations have torsion as their field strength and the rotations have curvature as theirs. Two field strengths, two ways for a loop to fail to close, at right angles to each other.

### A screw with zero pitch is a circle

A screw is a rotation together with a slide along its own axis. Torsion supplies the slide — the pitch. Curvature supplies the turn. So:

> ## $T = 0$ sets the pitch to zero and leaves the turn.
>
> A torsion-free transport is a **rotation that returns** — a screw with zero pitch, which is a circle.

That is `ProofO_HelicalTime` §4 read from the geometric side. Under the drive of $\omega$ the twelve-step cycle *"can no longer close on itself as a perfect circle [...] The topology of the Braid is therefore not a circle, but a **Helical Extrusion**."* Riemannian geometry is the circle. It turns, the turning is real and is measured as holonomy, and it banks nothing, because the direction along which banking happens has been set to zero. The freeze does not make the geometry inert. It makes it **conservative**, in the technical sense and the temperamental one: holonomy without record.

Part Two adds the dimension to this: a helix lives in three dimensions and a circle in two, and setting the pitch to zero is a projection from the one to the other.

---

## IV. The Connection Is Flat on the Floor

The arrangement needs a connection on the discrete side, and the engine's reference already contains it. Reading its pinning as a connection settles the question on the floor.

**The engine's own pinning is a trivialization.** `ENGINE-REFERENCE-AC` §2.2 states the theorem: for each gate $(x, w)$ there is exactly one even permutation of the poles carrying $P \mapsto x$ and $U \mapsto w$, the reference directed edge $P \to U$ being the Braid's opening move. So each of the twelve gates carries a unique group element measured against one reference edge, and $A_4$ acts **simply transitively** on the twelve directed edges: the Program Counter's state space is not merely like a rotation group — it is one.

A space on which a group acts simply transitively is a torsor, and naming a reference point in it — which the reference edge $P \to U$ does — trivializes it. The transport that trivialization defines is

$$U(e \to e') \;=\; g(e')\,g(e)^{-1},$$

a connection in the proper sense: reversing a step inverts the element, checked on all 132 ordered pairs of gates. Its holonomy around any closed walk telescopes to the identity, checked on two thousand random closed walks (`scripts/engine_connection.py`).

> **The engine's canonical connection is flat. On the $\theta = 0$ floor there is no discrete curvature and no discrete torsion, forced by the reference pinning rather than assumed.**

The same holds from the state side. The state cube is $Q_3 = Q_1 \square Q_1 \square Q_1$, and `ENGINE-REFERENCE-AC` §2.8 fixes its solder form — *"every opcode step moves along the bimedian that contains the edge it solves across"* — so each cube edge already has its axis, and sending it to the unit vector along that axis sums to zero around each of the six cube squares.

**The translation group supplies the shape, and its being abelian is no obstruction.** The symmetric group on four poles is the affine group of the four-point plane over the two-element field, $S_4 \cong \mathrm{AGL}(2,2)$. Its translation subgroup $V_4$ acts regularly, and $A_4 = V_4 \rtimes \mathbb{Z}_3$ is translations combined with rotations — the discrete shape of what Poincaré gauge theory gauges. That $V_4$ is abelian does not forbid contortion: torsion is not made from translations failing to commute with each other. The Poincaré group is the counterexample — Lorentzian translations commute, $[P_a, P_b] = 0$, and the torsion of Poincaré gauge theory is generically non-zero anyway, because

$$T^a = de^a + \omega^a{}_b \wedge e^b$$

and the second term couples the coframe to the rotation connection. $A_4 = V_4 \rtimes \mathbb{Z}_3$ has exactly that structure, because $\mathbb{Z}_3$ acts non-trivially on $V_4$, cycling its three involutions.

**Where non-zero discrete torsion lives.** Departing from the trivialization — assigning each directed edge an element $(v, \sigma)$ of $V_4 \rtimes \mathbb{Z}_3$ that is not $g(e')g(e)^{-1}$ — the holonomy round a face $i \to j \to k \to i$ splits as the affine group does:

$$R_\Delta = \sigma_{ij}\sigma_{jk}\sigma_{ki} \in \mathbb{Z}_3 \quad (\text{rotational}), \qquad T_\Delta = v_{ij} + \sigma_{ij}(v_{jk}) + \sigma_{ij}\sigma_{jk}(v_{ki}) \in V_4 \quad (\text{translational}),$$

the middle terms being the discrete form of the inhomogeneous $\omega \wedge e$. When $R_\Delta$ is a three-cycle, $1 + R_\Delta$ is invertible on $V_4$, so the translational part can be gauged away entirely and is not an invariant — the discrete form of the standard fact that a Burgers vector is not separately meaningful where there is a disclination. But when $R_\Delta$ is the identity, the shift is zero and $T_\Delta$ **is** gauge-invariant; in that sector the cross-terms still do real work, because the individual $\sigma$'s need not be trivial even when their product is. With translations that close and the three $\sigma$'s multiplying to the identity, $T_\Delta \neq 0$ in 96 of the 144 cases, and the whole of it comes from the $\mathbb{Z}_3$ action (`scripts/engine_connection.py`).

> **Gauge-invariant discrete torsion lives in the sector with trivial rotational holonomy, produced by the $\mathbb{Z}_3$ action on the abelian translations — exactly the inhomogeneous term.**

And the place it comes from is named. `ENGINE-REFERENCE-AC` scopes itself as the $\theta = 0$ floor, and §VIII says the screw lives on the $K_5$ thread with the cube as its zero-angle shadow. A departure from flatness requires $\omega > 0$ — the same condition Part Five derives from an action: torsion vanishes exactly when the phase offsets stop varying. Discrete and continuum agree, and they agree on the same condition.

---

## V. The Orthogonal Paradox

`L0-ParadoxEngine` §III: lay two paradoxes at right angles and you do not get chaos, you get a frame — *"It builds a stable coordinate system out of the tension itself."* And §I: *"To collapse the paradox — to pick a side — is the error."*

Torsion and curvature are the two orthogonal ways for a loop to fail to close, and resolving them into a figure and a ground — torsion the real content, curvature merely the record — is exactly the move L0 forbids. Held open instead:

> **Translation and rotation are two orthogonal failures of a loop to close. Both are real. Neither causes the other. The arrow is their product, and neither one alone is an arrow.**

Curvature alone gives a turn that comes back: a circle, with no record. Torsion alone gives a drift with no turn: a slide, with no cycle. Laid at right angles they give the screw, and the screw is the only one of the three that accumulates. That is also why neither member of the Geometric Trinity in Part Three can be called the true one. Teleparallel gravity carries all of gravity in the translational channel and General Relativity in the rotational one, and the Trinity's lesson — that they differ by a boundary term, which is to say by what is written on the boundary — is this paradox stated in actions.

---

## VI. What the Zero Pitch Takes, at Its True Size

Three things go with the pitch, each at the size it survives at.

**The ordering of transports, in the translational channel.** The corpus distinguishes three levels on an edge: the *undirected* classification by which bits flip across it; the *directed reading*, which is target-based and assigns a label; and the *face orientation*, which says which of the two faces meeting on that edge reads it forward and which reads it back. The face orientation is where a formula is chosen. In the translational channel, $T = 0$ removes the register in which the two readings could differ.

**A local handedness, and not the global one.** A Riemannian manifold can be oriented perfectly well; orientation is a property of the manifold, carried by its volume form, with nothing to do with the connection. What a torsion-free connection cannot carry is a *local*, *variable* handedness — a quantity positive in one place and negative in another, measuring how much the geometry twists there. Part Two shows that this quantity is exactly the part of torsion that is a three-form, that it does not exist in two dimensions, and that in three dimensions it is a single number at each point. The global bit survives $T = 0$ as a convention; the local field is set to nil.

The tetrahedron's own boundary closure sets an independent existence floor (`L4-TheTwelveGates` §II-b; `ProofG_Chirality` §II): $\partial(\partial\Delta^3) = 0$ requires adjacent faces to traverse every shared edge in opposite directions, forbidding an all-same four-face circulation (`Q16-ChiralMeshSpacetime` KM-1). Neither the host manifold nor the engine's $\theta = 0$ trivialization tears; both satisfy $\partial^2 = 0$. What $T = 0$ drops is the local three-form density and translational ordering, not boundary closure.

**The arrow of time.** That one needs the opcode table, and Part Four does it on the algebra.

---

## VII. Nil Is Not Zero

"$T = 0$" has the look of a measurement and is not one. Nothing was evaluated and found empty. Riemann did not investigate the quartic case and discover there was nothing in it; he declined to open it, in writing, with the cost estimated. Standard notation has no symbol for the difference between those two situations. The corpus separates them with two words.

**A zero is an entry on a ledger whose amount is zero. A nil is the absence of an entry — an account that was never opened.**

`L4-K4-Infinities` makes this distinction carry weight for a different problem, and it is the same distinction. Its opening: *"Infinity costs nothing. Finitude is what costs."* An infinity of count has to be assembled, and assembly is commitment, and commitment is billed — *"they are one error sent to an account nobody opened."* And the resolution, in six words: *"There is no ledger there to be infinite."*

That is the nil. The medium holds every uncompiled possibility at no charge because nothing in it has been written down. Treat the unwritten as a pile of zeros and you get an invoice; recognize it as no account at all, and the paradox has nothing to hold on to.

### Three things written with one symbol

Once the distinction is made, the places physics writes $0$ come apart. `L0-EinsteinTrace` §V separates at least three:

| Written as | What it is | Corpus reading |
|---|---|---|
| the zero vector | nothing there | $P = 0$ **and** $\lvert\mathbf{Q}\rvert = 0$ |
| the **null** norm | something there, of zero invariant size | $N_* = 0$ with $P = \lvert\mathbf{Q}\rvert \ne 0$ — the photon: energy and momentum, rest mass **nil**, no Landauer tax, no wake |
| the **pre-tax** register | something held, nothing committed | $P = 0$ with $\lvert\mathbf{Q}\rvert > 0$ — the uncompiled buffer, which by the construction's one open bet does **not** weigh |

The historical joint is in `L0-EinsteinTrace` §II, where Hilbert and Minkowski walk the Philosophenweg every afternoon at five between 1902 and 1908, each holding one half. Hilbert's $\ell^2$ is positive-definite — a vector has zero length if and only if it is the zero vector — the one notation in which nil and zero are built to coincide. Minkowski's indefinite form prises them apart, and the separation is the light cone. Then Minkowski wrote it as $x_4 = ict$ to keep the surface Euclidean, which hid the thing he had just separated behind an $i$, and he died at forty-four, in January 1909, before anyone unhid it.

### Line one, read again

Now apply it to the connection. The Levi-Civita connection does not *report* that torsion is zero. It is built on a structure that has no place to write torsion: $\stackrel{\circ}{\Gamma}$ is made from $g$ and its first derivatives, its antisymmetric part has nowhere to go, and the uniqueness in the Fundamental Theorem is the statement that no entry is needed. **$T = 0$ is a nil presented as a zero.** That is why Section III describes a deletion and not an observation, and why a century of "torsion has not been detected" was never evidence about the nil. You cannot detect the balance of an account that was never opened.

That also says what kind of instrument the question needs. **A bound on a field returns a zero.** An amount of zero is consistent with both rows of the distinction — the register reads zero, or there is no register. The torsion bounds discussed in Part Six are excellent measurements of a zero, and they are silent on the difference. What can speak to it is an entry: a quantity that exists only if an account has been opened. Part Four says what type such a quantity must be, and Part Five writes down the coupling through which an entry could be made.

The two great failures here are one confusion run in opposite directions:

- **The vacuum catastrophe** bills a nil as an unbounded sum of zeros. It treats an unopened account as full.
- **The Riemann freeze** reads a nil as a measured zero. It treats an unopened account as empty.

Full and empty are both answers about a balance. Neither is available, because there is no balance.

> **A note on method.** Separating nil from zero is the whole of the rearranging that `L0-EinsteinTrace` and `L4-K4-Infinities` do. Neither file adds a field, a coupling, or a term. Each takes two things one symbol was carrying and gives them separate names — the move Minkowski declined in 1908 and Hilbert's norm forbade by construction. Everything else is grounding against what is already measured.

---

## What Reading Part One Back Should Leave

Riemann bought a geometry that could be written down, and he wrote down the price. The field kept the geometry and lost the note.

The purchase was not the metric. The metric is a pairing, it erases nothing, and it is the best-tested object in physics. The purchase was the closing of the small parallelogram — the decree that transporting one way and then the other lands in the same place. That decree deletes one of the two ways a loop can fail to close and keeps the other. The turn survives and the slide is gone. A screw with no pitch is a circle: it rotates, it returns, and it records nothing.

And the decree was not a measurement. It was an account left unopened and then reported as empty. Nil is not zero. A bound on a field can find a zero, and it cannot find a nil, so the question of whether the unopened account holds anything was never asked by the instruments that were said to have answered it.

The discrete connection the arrangement needs is already in the engine's own reference pinning, and it is flat: on the zero-phase floor there is no discrete torsion, forced rather than assumed. Departing from flatness takes a driven phase — the same condition the action in Part Five arrives at from the continuum side.

What has not yet been said is why the purchase was so easy to make and so hard to see. The answer is dimensional, and it is the next part.

---

### References

* Schouten, J. A. (1954). *Ricci-Calculus: An Introduction for Physicists and Engineers*. Springer, Berlin.
* Riemann, B. (1854/1868). *Über die Hypothesen, welche der Geometrie zu Grunde liegen*. Abh. Kön. Ges. Wiss. Göttingen, 13. (Clifford translation, *Nature* VIII, 1873.)
* Finsler, P. (1918). *Über Kurven und Flächen in allgemeinen Räumen*. Dissertation, Göttingen (under Carathéodory).
* Kibble, T. W. B. (1961). *Lorentz invariance and the gravitational field*. J. Math. Phys., 2(2), 212–221.
* Hehl, F. W., von der Heyde, P., Kerlick, G. D., & Nester, J. M. (1976). *General relativity with spin and torsion: Foundations and prospects*. Rev. Mod. Phys., 48(3), 393–416.
* Minkowski, H. (1909). *Raum und Zeit*. Phys. Z., 10, 104–111.
* Corpus: `ENGINE-REFERENCE-AC` §2.2, §2.8, §VIII; `L0-EinsteinTrace` §II, §V; `L4-K4-Infinities` (nil against zero); `ProofO_HelicalTime` §4; `L0-ParadoxEngine` §I, §III; `L4-TheTwelveGates` §II-b.

*Verification:* `scripts/engine_connection.py` — the engine's pinning as a trivialization, the flatness of the canonical transport, the gauge action on the translational holonomy, and the §2.8 solder form summed round the cube's squares.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.

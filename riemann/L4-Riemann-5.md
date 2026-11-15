# L4-Riemann-5
## Part Five — The Action

*Reads with `L4-DynamicDistortions201` §II, `ENGINE-REFERENCE-AC` §2.5–2.7, `ProofG_Chirality` §II, §IV, `L4-K4-Infinities` (the Datasheet), `L4-ThePlenum`, `QED-EotvosBound`. Continues from `L4-Riemann-4`; continues in `L4-Riemann-6`. Every number here is reproduced by `scripts/torsion_action.py`, `scripts/parity_candidates.py` and `scripts/aggregate_parity.py`.*

---

The first external audit closed its proceeding with a verdict and a task. The verdict was that the identification of the corpus's shear with geometric torsion was *unregistered*: nothing had been built that would let it be true or false. The task was to write the action that couples the corpus's bimedian shear to spacetime torsion, derive the shear's behaviour from it, and itemize every constant.

This part does that. It is the one part of the file that computes something a classical reader would recognize as physics, and so it is the one part whose claims can be checked by a classical reader's own tools. It ends with one dimensionless dial, one experimental bound on it, and an open question about mirrors that turns out to be the dimensional question of Part Two arriving in a Lagrangian.

---

## I. The Demand, and Why It Could Not Be Written as Demanded

The bench asked for

$$\mathcal{S} = \int d^4x \sqrt{-g}\left[\frac{1}{2\kappa}R + \frac{1}{2}\partial_\mu\theta\,\partial^\mu\theta + \beta\,\theta\,V^\mu A_\mu\right]$$

and asked that the shear be derived *"from the stationary points of the Nieh–Yan density across the four faces of $K_4$."* There are five defects, each checkable, and each has to be repaired before there is anything to derive.

**The coupling is inert.** $V^\mu A_\mu$ — the trace torsion vector dotted into the axial one — is *quadratic* in torsion. In Einstein–Cartan theory torsion enters algebraically, so a quadratic term only deforms the quadratic form in $(V, A)$. With the coefficients of Section III the form is $\begin{psmallmatrix} -2/3 & b/2 \\ b/2 & 3/2\end{psmallmatrix}$, whose determinant $-1 - b^2/4$ is negative for every $b$. The form never degenerates, its only stationary point is $V = A = 0$, and **the demanded term sources no torsion at any value of the shear.**

**The Nieh–Yan density is not $V \cdot A$.** The Nieh–Yan four-form is $N = d(e^a\wedge T_a)$, and $e^a\wedge T_a$ is, up to a constant, the dual of the axial torsion, so $N \propto \nabla^\circ_\mu A^\mu$ — the divergence of the **axial vector alone** (Nieh and Yan 1982; Chandía and Zanelli 1997). The literature the bench cited couples a pseudoscalar to $N$, which after integration by parts is $-\partial_\mu\theta\,A^\mu$: **linear** in torsion. That is the term that does something.

**"Stationary points of the Nieh–Yan density" is not defined.** $N$ is a total derivative. For a constant shear, $\theta N$ is a boundary term and changes no field equation. What is defined is the shear's field equation, derived below.

**One field, three angles.** The demanded action carries one $\theta$. The corpus carries three, one per bimedian: $\theta_F$, $\theta_C$, $\theta_M$. Which function of the three couples is not a detail, and the corpus's own structure constrains it hard.

**"Across the four faces of $K_4$" is dimensionally ill-posed.** $N$ is a four-form. A face of $K_4$ is two-dimensional and $K_4$ itself is three-dimensional. Part Two is the general reason this matters: a quantity that lives on volumes cannot be summed over faces. The dimensionally correct discrete statement involves $K_5$, and it is in Section VII.

**And the demanded kinetic term is unnecessary.** An angle needs a scale before $\tfrac12(\partial\theta)^2$ has the dimensions of a Lagrangian density, and that scale would be a new dial. Section III shows none is needed: coupling to the Nieh–Yan density **induces** the kinetic term, with Planck-mass normalization and no new constant.

### The impossibility argument, corrected

The bench also built an argument that soldering a frame to the corpus's discrete structure is impossible, and then — correctly — declined to rest its verdict on it. The finding still stands in the record, and both of its legs fail.

**The group-theory leg runs the wrong way.** That there is no non-trivial homomorphism from $SO(3)$ onto $\mathbb{Z}_3$ is true and irrelevant. Soldering a frame to a discrete structure is a **reduction of the structure group** from $SO(3)$ to a finite *subgroup* — which is what every crystal's frame field does (Part Three's crystal). $A_4$ is the rotation group of the tetrahedron, a subgroup of $SO(3)$; nobody needs a homomorphism out of $SO(3)$. And the premise was wrong besides: the bench took the three bimedians to be a $\mathbb{Z}_3$-set. Section IV computes that they carry the full three-dimensional standard representation of $S_4$.

**The Laue leg proves too much, and the overstatement it uses is ours.** Laue's theorem zeroes the integrated spatial stress of a *static* bound system. It does not forbid orientation inside, and it says nothing about non-static systems — and the offset is a phase driven by $\omega$. Read as *"annihilates every vector,"* it would forbid a bound system from exporting spin, and protons export spin: an axial vector, which is exactly what axial torsion couples to. That phrase is in `L4-K4-Infinities` itself, and the bench quoted it faithfully. It is an overstatement there, and `L4-Riemann-wip` flags it for that file. `L4-K4-Infinities`' own takehome rule 6 already says the precise thing: *"Laue is about the vector sector, not the scalar."*

---

## II. The Action

Einstein–Cartan: a metric-compatible connection $\Gamma$ whose torsion varies independently. Signature $(-,+,+,+)$; $\nabla_\mu V^\rho = \partial_\mu V^\rho + \Gamma^\rho{}_{\mu\nu}V^\nu$; $T^\rho{}_{\mu\nu} = \Gamma^\rho{}_{\mu\nu} - \Gamma^\rho{}_{\nu\mu}$; curvature in the Carroll/MTW convention, checked to give $R = 2/r^2$ on a round sphere.

$$\boxed{\;\mathcal{S} = \frac{1}{2\kappa}\int d^4x\sqrt{-g}\,\Big[\,R(\Gamma) \;+\; \beta\,F(\vec\theta)\;\nabla^\circ_\mu a^\mu\,\Big] \;+\; \mathcal{S}_{\text{matter}}\;}$$

Here $\vec\theta = (\theta_F, \theta_C, \theta_M)$ are the three bimedian **phase offsets** of `L4-DynamicDistortions201` §II — temporal offsets, not geometric strains, and §IV's first subsection is where that distinction is stated and where it pays; $F$ is a function to be fixed; $\beta$ is dimensionless; $\kappa = 8\pi G = M_P^{-2}$. Torsion is split into its irreducible parts:

$$v_\mu = T^\nu{}_{\mu\nu}\ \ (\text{trace},\ 4),\qquad a^\mu = \tfrac16\,\varepsilon^{\mu\nu\rho\sigma}T_{\nu\rho\sigma}\ \ (\text{axial},\ 4),\qquad q_{\lambda\mu\nu}\ \ (\text{tensor},\ 16).$$

The axial part is the three-form of Part Two, written as its dual vector in four dimensions. The second term in the action is $\beta F$ times the Nieh–Yan density, with the normalization of $N \propto \nabla^\circ\!\cdot a$ absorbed into $\beta$. Integrated by parts, it is $-\beta\, a^\mu \partial_\mu F$.

---

## III. The Derivation

Everything in this section is Grammar: computation anyone can repeat.

### The torsion content of the curvature scalar

For a metric-compatible connection,

$$R(\Gamma) \;=\; R^\circ \;-\; \tfrac{2}{3}\,v_\mu v^\mu \;+\; \tfrac{3}{2}\,a_\mu a^\mu \;+\; \tfrac{1}{2}\,q_{\lambda\mu\nu}q^{\lambda\mu\nu} \;+\; (\text{total divergence})$$

**with no cross terms between the irreducible parts.** The script solves the metric-compatibility and torsion conditions for the connection directly, fits each coefficient on random samples, and finds the cross terms absent to machine precision.

### Only two channels exist

A scalar gradient $\partial_\mu F$ can couple linearly to torsion in exactly two ways: $v^\mu\partial_\mu F$ and $a^\mu\partial_\mu F$. The tensor part is traceless and has no axial part, so no linear scalar can be built from it and a single vector. **Of torsion's twenty-four components, eight are reachable by any scalar. The sixteen in the tensor part are invisible to it.**

### Solve the torsion, and read off the health of each channel

Torsion is algebraic, so its field equations are solved in closed form. In the action above:

$$v_\mu = 0,\qquad q_{\lambda\mu\nu} = 0,\qquad \boxed{\;a_\mu = \frac{\beta}{3}\,\partial_\mu F\;}$$

Substituting back:

$$\mathcal{L}_{\text{induced}} = -\frac{\beta^2}{12\,\kappa}\;\partial_\mu F\,\partial^\mu F$$

— a kinetic term with the correct sign for this signature. **The offsets acquire dynamics from geometry, with no kinetic term put in by hand and no new scale.** Canonically normalized, $\varphi = \beta M_P F/\sqrt6$, so the induced decay constant is $f = \beta M_P/\sqrt6$.

The general rule: a coupling $-\beta X\!\cdot\!\partial F$ to a torsion vector $X$ whose coefficient in $R(\Gamma)$ is $c$ induces $-\tfrac{\beta^2}{8\kappa c}(\partial F)^2$, which is healthy if and only if $c > 0$. So:

| Channel | Coefficient in $R(\Gamma)$ | Induced kinetic term |
|---|---|---|
| axial, $a\cdot\partial F$ | $+3/2$ | **healthy** |
| trace, $v\cdot\partial F$ | $-2/3$ | **ghost** |

**A scalar gradient can source torsion healthily only through the axial vector.** Sourcing the trace vector alone produces a kinetic term with the wrong sign. (Holst-type couplings source both channels at once and the combination can be healthy; the statement is about the trace channel alone, and it is why the Nieh–Yan coupling, which sources only the axial channel, is the clean one.) This agrees with Calcagni and Mercuri's Nieh–Yan case: trace and tensor torsion vanish, the axial torsion is the gradient, the induced kinetic term is healthy, and the theory has a shift symmetry $F \to F + \text{const}$.

Note what this does to an earlier route. The parent file had recommended against building in the axial channel, on the grounds that it is the best-explored and most tightly bounded part of torsion phenomenology. That reasoning treated the axial channel as a choice. It is not one. **It is the only channel through which a scalar can couple to torsion and stay healthy.** If the corpus's phase offsets couple to spacetime at all, they couple there, and the bounds on that channel are the corpus's to meet. Section VI meets them.

### Exactly one combination of the three shears becomes dynamical

The induced term is $-\tfrac{\beta^2}{12\kappa}\,(\partial_i F)(\partial_j F)\,\partial\theta_i\!\cdot\!\partial\theta_j$: a metric on the three-dimensional space of offsets, of **rank one**. One direction in offset space — along the gradient of $F$ — gets a kinetic term. **The other two get none from geometry and remain invisible to it**, whatever $F$ is. One of three is the whole of what geometry can see.

### The freeze is the stationary-shear sector

$$\partial_\mu F = 0 \;\Longrightarrow\; a_\mu = 0 \;\Longrightarrow\; T = 0 \;\Longrightarrow\; \Gamma = \stackrel{\circ}{\Gamma}$$

**In this action, Riemann's torsion-free connection is not a decree about geometry. It is what the geometry does when the offsets do not vary.** With $F$ constant, the coupling is a boundary term, the connection relaxes to Levi-Civita, and General Relativity is recovered exactly. Part One said that $T = 0$ zeroes the pitch and keeps the turn. This says what the pitch was the record *of*: an offset that changes.

### Matter: the shear is sourced by chirality non-conservation

Dirac fermions couple minimally to the axial torsion only, $\mathcal{L} \supset \alpha\, a_\mu j_5^\mu$, with $j_5^\mu = \bar\psi\gamma^\mu\gamma^5\psi$ and $\alpha$ a number fixed by minimal coupling. Solving again, $a_\mu = (\beta\partial_\mu F - 2\kappa\alpha j_{5\mu})/3$, and

$$\mathcal{L}_{\text{eff}} = -\frac{\beta^2}{12\kappa}(\partial F)^2 + \frac{\alpha\beta}{3}\,\partial_\mu F\, j_5^\mu - \frac{\kappa\alpha^2}{3}\,j_{5\mu}j_5^\mu.$$

The last term is Einstein–Cartan's standard axial–axial contact interaction, the one Part Three quoted, recovered — a consistency check. The middle term is a derivative coupling to the axial current, and the shear's field equation is

$$\Box F = \frac{2\kappa\alpha}{\beta}\,\nabla_\mu j_5^\mu,\qquad \nabla_\mu j_5^\mu = 2im\,\bar\psi\gamma^5\psi \;+\; (\text{anomaly: } F\tilde F,\ R\tilde R).$$

**The offsets are sourced by the divergence of the axial current** — by fermion masses classically, and by the chiral anomaly quantum-mechanically. Mercuri and Taveras derive the same structure for the Barbero–Immirzi field, anomaly couplings included. In canonical normalization the coupling to $\nabla\!\cdot j_5$ is $\alpha\sqrt{2\kappa/3}$, **independent of $\beta$**: matter sees the field at Planck-suppressed strength whatever the dial, and $\beta$ sets only the dictionary between the shear and the field.

This is the honest replacement for the Jarlskog reading struck in Part Four. If the offsets' parity-odd channel couples to anything, it couples to **chirality non-conservation**, not to the rephasing invariant of the Yukawa matrices. Those are different operators.

---

## IV. Which $F$ — the Corpus Answers It

### First, which $\theta$ this is

`L4-DynamicDistortions201` §II is explicit, and an earlier version of this file did not honour it:

> "Note that this $\theta$ is a temporal phase offset and reaches its limit at $\pi$. The $\theta$ of `L4-DynamicDistortions301` §VI.A is a geometric shear parameter on a single cross-section and reaches its limit at $\pi/2$. Both are torsion; they measure different things."

**The $\vec\theta$ of this action is the first one: a temporal phase offset between the two instances of a dual-causation pair.** It is not a spatial strain. The corpus also writes *phase-shear* for it (`L3-NonSoficTopologicalVolumes` §III), and this file says *phase offset* where the distinction does work and *shear* only as shorthand for that. Part Four §VIII uses the other $\theta$ — DD301's geometric shear, through the CHSH envelope — and the two must not be run together.

That distinction is not housekeeping. It decides whether this action has a parity-clean coupling at all, and Section IV's last subsection is where it pays.

### The three phase offsets are a vector on the cube's axes

`L4-DynamicDistortions201` §II fixes each sign: *"P–U leads I–R (θ > 0)", "P–R leads I–U (θ > 0)", "P–I leads U–R (θ > 0)"* — **positive when the edge containing $P$ leads.** A permutation of the poles sends each bimedian to a bimedian, and keeps or flips the sign according to whether the image of the leading edge still contains $P$.

Computed over all twenty-four permutations, and checked to compose correctly over all 576 pairs, the character class by class is $(3, 1, -1, 0, -1)$ on (identity, transposition, double transposition, 3-cycle, 4-cycle) — and that is, class for class, how the cube's three axes $(x,y,z)$ transform under the tetrahedral group $T_d$ (`scripts/bimedian_parity.py` computes both and compares them). **The triple is the standard representation of $S_4$.** Each element acts as a signed permutation. Each of the engine's rings (`ENGINE` §2.7) — the half-turn holding one bimedian — keeps its own offset and flips the other two, because it exchanges the two edges of each bimedian it does not hold.

### Invariants, exactly

The Molien series of this representation settles which couplings respect it:

- **No invariant of degree one.** No linear combination of the three offsets is invariant under $S_4$.
- **Scalars** first at degree two, $|\vec\theta|^2$; then degree three, $\theta_F\theta_C\theta_M$; then two at degree four.
- **The first pseudoscalar** — invariant under rotations, odd under reflections — appears at degree six and is unique there:

$$\Delta(\vec\theta) = (\theta_F^2 - \theta_C^2)(\theta_C^2 - \theta_M^2)(\theta_M^2 - \theta_F^2)$$

So the bench's coupling, linear in one offset, is excluded by the carrier's symmetry if the full symmetry of the tetrahedron is kept.

### What the coupling has to be odd under

The Nieh–Yan density is the gravitational relative of $F\tilde F$, i.e. of $\mathbf{E}\cdot\mathbf{B}$: it is **odd under parity and odd under time reversal.** The matter coupling of Section III says the same from the other side — the field equation is $\Box F \propto \nabla_\mu j_5^\mu$, and $\nabla\!\cdot j_5 = 2im\,\bar\psi\gamma^5\psi + \text{anomaly}$, whose leading term is the pseudoscalar bilinear, odd under both. Since $\Box$ is even under both:

> **$F$ must be odd under parity and odd under time reversal.**

An earlier version of this file asked only for parity-oddness. That was half the condition, and the missing half is what decides the question.

### Both parities are fixed, and neither is a convention

**Time reversal.** $\vec\theta$ is a temporal phase offset. Reverse time and a lead becomes a lag: if $B$ lags $A$ by $\varphi$, then $B(-t)$ leads $A(-t)$ by $\varphi$. So $\theta_i \to -\theta_i$. **$\vec\theta$ is odd under time reversal** — and this is where the distinction at the top of this section pays, because DD301's *geometric* shear would be time-reversal **even**, and then no function of it could meet the condition above at any degree. The corpus has a parity-clean coupling only because its $\theta$ is a phase offset rather than a strain.

**Parity.** Spatial parity is central inversion. A bimedian is, by definition, the segment joining the midpoints of two opposite edges — and the centroid is its midpoint, so **the two midpoints are antipodal about the centre.** Inversion therefore *exchanges the two edges of every bimedian*. Computed on the standard cube coordinates (`scripts/bimedian_parity.py`): the midpoint of $P$–$U$ is $(1,0,0)$ and of $I$–$R$ is $(-1,0,0)$; of $P$–$R$ is $(0,0,1)$ and of $I$–$U$ is $(0,0,-1)$; of $P$–$I$ is $(0,1,0)$ and of $U$–$R$ is $(0,-1,0)$. Each pair is antipodal.

Since $\theta$ is defined by *which of those two edges leads*, exchanging them reverses it. **$\vec\theta$ is odd under parity.** It is a polar vector, $T_{1u}$ in the full cubic group, not a shear-strain triple — which settles the ambiguity an earlier version of this file left open, and settles it by the geometry of the bimedian rather than by a reading of a sign convention.

Two notes on what this does *not* rest on. It does not need the manifest-to-dual swap: that swap is also realized by proper rotations of the cube (`ENGINE` §2.3's odd coset), so "parity is the dual walker" would not have been an argument, though `ENGINE` §1.2's third item does identify the antipodal map with duality, which is a supporting observation. And it does not need the corpus's own mirror: `ENGINE` §2.5 names that the **handedness flip** — an odd transposition, the move the machine cannot make — which is a reflection and not an inversion.

### The coupling, forced

With $\vec\theta$ odd under both parity and time reversal, $F$ must be of **odd degree**. The computation (`scripts/bimedian_parity.py`):

| Candidate $F$ | Degree | Parity | Time reversal | Invariant under $T_d$ | Verdict |
|---|---|---|---|---|---|
| $\Delta = (\theta_F^2-\theta_C^2)(\theta_C^2-\theta_M^2)(\theta_M^2-\theta_F^2)$ | 6 | $+$ | $+$ | no | **excluded** |
| $\theta_F\theta_C\theta_M$ | 3 | $-$ | $-$ | **yes** | **forced** |
| $\theta_F$ | 1 | $-$ | $-$ | no — only the AR-charge stabilizer | admissible, not carrier-symmetric |
| $\vec c\cdot\vec\theta$, free weights | 1 | $-$ | $-$ | no | excluded: three new dials |

$$\boxed{\;F(\vec\theta) \;=\; \theta_F\,\theta_C\,\theta_M\;}$$

**This is the unique coupling that is odd under parity, odd under time reversal, invariant under the full symmetry of the carrier, and free of new dials.** It is the product of the three phase offsets — one per bimedian — so **torsion is sourced at third order, and it vanishes whenever any single bimedian is unsheared.** In cubic notation the coupling is $A_{2u}$: invariant under every rotation and reflection of the tetrahedron, odd under inversion. (Counsel's brief reached the same function and labelled it $A_{1u}$; the label is the one correction, since $xyz$ is $A_{2u}$ in $O_h$.)

$\Delta$, the sixth-order pseudoscalar that an earlier version of this file carried as its carrier-symmetric option, is **excluded by time reversal** whatever parity turns out to be. That exclusion is the cheapest result in this section and the one most worth checking independently: $\Delta$ has even degree, so it cannot be odd under anything that acts as $\vec\theta \to -\vec\theta$.

### What is left open, and it is not the coupling

One thing follows that the corpus may not want, and it is stated here rather than buried. A quantity odd under parity *and* odd under time reversal is, in Barron's terminology, **falsely chiral** rather than truly chiral — the class of $\mathbf{E}\cdot\mathbf{B}$ and of a spinning cone, not of a screw. `ProofG_Chirality` §V claims the opposite for the $\omega$-driven turn: *"The extruded, $\omega$-driven turn is true-chiral."* On the transformation properties computed here, the phase-offset triple is falsely chiral. Whether the corpus's screw recovers true chirality through the *translation* along $\omega$ — which is what distinguishes Barron's screw from his spinning cone — is a real question and is not answered here. `L4-Riemann-wip` flags it for `ProofG`.

---

## V. What Survives Averaging

Now that the coupling is fixed, the averaging question has one answer rather than three, and it matters for how null results are read (Part Six).

Take a population of configurations — biased, with no symmetry of its own — and close it under a group: include, for every configuration, its image under every element of the group. Then average the coupling over the population. The rule is simple. **An observable that is odd under some element of the closing group averages to zero. An invariant one survives. A positive-definite cost survives everything.** The computation (`scripts/aggregate_parity.py`):

| Population closed under | $\theta_F\theta_C\theta_M$ (**the coupling**) | $\theta_F$ | $\Delta$ | $\lvert\vec\theta\rvert^2$ (cost) |
|---|---|---|---|---|
| rotations of the solid, $A_4$ | **survives** | 0 | survives | survives |
| rotations and reflections, $S_4$ | **survives** | 0 | 0 | survives |
| rotations and inversion ($\vec\theta$ polar) | **0** | 0 | survives | survives |

Read the first column, since that is now the only one that is physics. **The coupling survives averaging over every rotation and every reflection of the tetrahedron, and vanishes only when the population is closed under inversion** — which, inversion being parity, is exactly the statement that a parity-symmetric population sources no net torsion. That is the correct and expected behaviour, and it names the condition an experiment has to break: not an orientational average, but a parity-asymmetric sample.

Two things follow. **First:** a null result in a population closed under inversion says nothing about the coupling's strength — the mean is zero for every value of $\beta$. Only a parity-asymmetric, i.e. genuinely homochiral or spin-polarized, sample tests it. **Second:** cost does not cancel. A positive-definite quantity survives every averaging, so any reconciliation that waits for the cost of being to wash out in the aggregate waits forever.

The torsion experiments of Part Six use spin-polarized matter. They are the right instrument, built for exactly this reason.

---

## VI. The Bound — the First Time the Corpus's Own Quantity Meets an Experiment

Spin-polarized torsion balances and comagnetometers bound the axial torsion that fermions see at the order of $10^{-31}$ GeV on several components (Kostelecký, Russell and Tasson 2008). With $a = (\beta/3)\,\partial F$, and up to the factor of order one relating $a$ to the measured coefficient:

$$\beta\,\big|\partial F\big| \;\lesssim\; 3\times 10^{-31}\ \text{GeV}.$$

With the coupling fixed, this is no longer a fork. $\partial F/\partial\theta_F = \theta_C\theta_M$ and likewise for the other two, so the derivative is of order $\theta^2$ and, for offsets advancing at rate $\nu$:

$$\beta\,\theta^2\,\nu \;\lesssim\; 3\times10^{-31}\ \text{GeV}.$$

**Quadratic suppression, not linear and not quintic.** The bound bites two powers of the offset weaker than on the bench's linear coupling, and three powers harder than it would have on the sixth-order $\Delta$ this file previously carried as its carrier-symmetric option.

Two consequences. An offset advancing **uniformly** — one global phase rate — produces a timelike axial torsion, a preferred-frame background of exactly the kind these experiments bound. So either the advance is not coherent at laboratory scales (the corpus seats $\omega$ at each bounded frame's own centroid, which is the local reading) or $\beta$ is small. And in this action vacuum torsion is a **gradient**: $\partial_{[\mu}a_{\nu]} = 0$ away from polarized matter. That is the action's sharpest falsifier, and it is listed below.

---

## VII. The Discrete Reading of "Across the Faces"

The bench's phrase has a correct form, one dimension up. The Nieh–Yan four-form integrated over a four-dimensional cell equals, by Stokes' theorem, the three-form $e^a\wedge T_a$ integrated over the cell's boundary — the **axial torsion flux** through it. A four-simplex has five vertices, which is $K_5$, and its boundary is five tetrahedra, which are $K_4$s:

$$\int_{K_5} N \;=\; \sum_{i=0}^{4} (-1)^i \int_{K_4^{(i)}} e^a \wedge T_a$$

with the alternating signs of the simplicial boundary operator. **The Nieh–Yan charge of a $K_5$ cell is the alternating sum of the axial fluxes through its five $K_4$ facets.** This is a reading, resting on Stokes and the simplicial boundary and nothing else. Its interest is twofold. The alternation the corpus attributes to the chiral mesh is, here, just the boundary operator on a simplex. And the coupling's natural domain is the solid: the three-form is integrated over $K_4$s, which are three-dimensional, and never over faces. It cannot be written on the floor.

---

## VIII. The Action Holds; It Cannot Commit

One more fact about the action, and it changes what an action can be asked to test.

The action couples matter to the metric minimally, and couples torsion to spin only. The induced term $-\tfrac{\beta^2}{12\kappa}(\partial F)^2$ gravitates like any other energy. So **in this action, inertial and gravitational mass are equal exactly, by construction.** And a single action yields reversible equations: dissipation is not variational, and a conservative action cannot produce a friction term. The standard way to describe a dissipative system with a variational principle doubles the variables (Galley 2013).

The corpus puts its distinctive claims on the side no single action reaches. `L4-ThePlenum` describes the medium as *"reactive, not resistive: the medium stores and returns, and dissipates nothing."* `QED-EotvosBound` puts the departure from the equivalence principle on the dissipative side,

$$\eta \equiv \frac{m_i}{m_g} - 1 \approx -2\,\frac{P_{\text{diss}}}{m c^2 \omega},$$

with *"the numerator $P_{\text{diss}}\cdot\tau$ the Landauer tax paid per compilation cycle"* — driven by the tax a frame pays to keep its buffer, not by the energy it holds, and with a fixed sign.

So an action is the **held** register by construction. The **committed** register — the ledger, the Landauer tax, any $\eta$ — cannot appear in any single action, this one or a better one. That is not a defect of this action. It says what a demand for an action can test: the held half. The committed half needs a dissipative extension, and the parent file carries that as an unconstructed item of its own. The classical side is in the same position, for what it is worth: GR takes the equality of inertial and gravitational mass as its founding input, while the corpus recovers it as the limit of zero internal degrees of freedom and attaches a signed departure to it.

`L4-Riemann-wip` records three defects in `QED-EotvosBound` as written, which the averaging rule of Section V exposes — the most serious being that its clock for a passive test mass grows with the mass, which breaks the additivity that any $\eta$ must respect. They belong to that file and are flagged there.

---

## IX. Datasheet and Status

| Item | Value | Category |
|---|---|---|
| $c_v,\ c_a,\ c_q$ | $-\tfrac23,\ +\tfrac32,\ +\tfrac12$ | **Grammar** — computed |
| $a = \tfrac{\beta}{3}\partial F$; induced $-\tfrac{\beta^2}{12\kappa}(\partial F)^2$ | — | **Grammar** — derived |
| trace channel ghost, axial healthy | — | **Grammar** |
| $\vec\theta \cong$ standard representation of $S_4$ | character $(3,1,-1,0,-1)$ | **Grammar**, consuming DD201's sign convention |
| $\vec\theta$ odd under inversion | bimedian midpoints antipodal | **Grammar** — geometry of the bimedian |
| $\vec\theta$ odd under time reversal | phase lead becomes lag | **Grammar**, consuming DD201's reading of $\theta$ as a *temporal* offset |
| invariant degrees; $\Delta$ | first pseudoscalar at six, unique | **Grammar** — Molien |
| parity and averaging tables | — | **Grammar** — computed |
| $\kappa = 8\pi G = M_P^{-2}$ | — | **Substrate** — consumed, never derived |
| $\alpha$ | minimal-coupling number | **Grammar** — fixed by the Dirac operator |
| $\beta$ | free | **Dial — one, and the only one** |
| choice of $F$ | $\theta_F\theta_C\theta_M$ | **Grammar** — forced by P-odd, T-odd and carrier symmetry; no longer a fork |
| bare kinetic scale | **not needed** — induced, $f = \beta M_P/\sqrt6$ | — |
| torsion bound | $\sim 10^{-31}$ GeV | **State** — experimental input |

**One prohibition.** $\beta$ must not be borrowed from the Barbero–Immirzi parameter. Structurally this action is the Barbero–Immirzi-field model with the parameter promoted to a function of the offsets, and the identification *"the corpus's chirality is the Barbero–Immirzi parameter"* is a route that does not work (Part Six): $\gamma$ is a quantization ambiguity, and borrowing its value would be a dressed dial.

**What changes in the parent's accounts.**

| Account | Before | After |
|---|---|---|
| **U2** — which operator $\vec\theta$ couples through | nil | **discharged in form**: the Nieh–Yan density, the axial channel, sourced by $\nabla\!\cdot j_5$; not the Yukawa sector |
| **U3** — the solder form | nil | **discharged for this channel**: parity and time reversal on $\vec\theta$ are fixed by the geometry of the bimedian and by $\theta$ being temporal, so the coupling is forced without one (Section IV) |
| **U1** — a connection on $A_4$ | nil | **answered on the floor** — see Part One §IV: the engine's own reference pinning is a flat trivialization, so discrete torsion vanishes at $\theta = 0$, which is this action's $\partial F = 0$ sector read discretely |
| **U0** — the engine's recurrence | nil | untouched |
| **U4** — the dissipative register | not stated | **opened**: the committed side cannot be written in one action (Section VIII) |

**What would make this a Bridge.** One thing now, where there were two: the corpus fixes $\beta$ from $K_4$ structure with no free parameter, and the resulting relation is checked at more than one configuration. $F$ is no longer owed.

### Checks and kills this part adds

*Checks — arithmetic anyone can run:*

1. **Coefficients.** Show that $(-\tfrac23, \tfrac32, \tfrac12)$, the absence of cross terms, or the closed-form torsion solution are wrong.
2. **Health.** Show that a coupling sourcing only the trace vector is healthy. That contradicts $c_v < 0$.
3. **Representation.** Show that, under DD201's convention, $\vec\theta$ is not the standard representation of $S_4$.
4. **Parity.** Show that central inversion does **not** exchange the two edges of each bimedian. That would unfix the coupling, and it is a two-line coordinate check.
5. **Time reversal.** Show that DD201's $\theta$ is not odd under time reversal — that a phase lead does not become a lag. That would leave no parity-clean coupling at any degree, which is a sharper outcome than the one this part reaches.

*Kills — events in the world:*

6. **Curl.** In this action, vacuum axial torsion is a gradient. **A measured axial torsion background with non-vanishing curl, away from polarized matter, falsifies it.**
7. **The coupling's own zero — now the file's sharpest.** $F = \theta_F\theta_C\theta_M$ vanishes when **any single bimedian is unsheared**. So: **exhibit geometric torsion sourced by a configuration in which one of the three phase offsets is zero, and this action is dead.** That is a far more exposed condition than the sixth-order option it replaces, which needed two offsets to coincide in magnitude. The coupling got cheaper to kill when it got forced.

---

## What Reading Part Five Back Should Leave

The action the bench asked for did nothing, for five checkable reasons. The action that does something couples a function of the three bimedian phase offsets to the Nieh–Yan density, and everything follows from it in closed form. Torsion is forced into the axial channel, because that is the only channel a scalar can use without producing a ghost. The offset acquires dynamics from geometry with no new scale. Only one combination of the three is visible to geometry. Matter sources it through the divergence of the axial current. And the torsion-free connection reappears as what geometry does when the offsets stop changing: Riemann's freeze is the stationary sector of an action that has now been written.

Which function couples is no longer open. The Nieh–Yan density is odd under parity and odd under time reversal, so $F$ must be too. Central inversion exchanges the two edges of every bimedian — because the centroid is the bimedian's own midpoint — so each offset is parity-odd. A phase lead becomes a lag under time reversal, so each offset is time-reversal-odd as well, and that second half is available only because DD201's $\theta$ is a *temporal* offset and not a geometric strain. Odd degree is therefore forced, the sixth-order candidate is excluded, and the unique carrier-symmetric survivor is the product of all three: $F = \theta_F\theta_C\theta_M$, third order, vanishing whenever any one bimedian is unsheared. The dimensional question of Part Two is answered here rather than merely posed — and the answer makes the action easier to kill, not harder.

Populations average the coupling away exactly when they are closed under inversion, which is to say when they are parity-symmetric, and never average away the cost. So parity-symmetric nulls bound nothing here, and spin-polarized experiments bound $\beta\theta^2$ — at about $10^{-31}$ GeV, the first contact between the corpus's own quantity and a measurement.

And an action can only hold. The committed register is not in it and cannot be put there. Testing the ledger needs an instrument that dissipates.

---

### References

* Nieh, H. T., & Yan, M. L. (1982). *An identity in Riemann–Cartan geometry*. J. Math. Phys., 23(3), 373–374.
* Chandía, O., & Zanelli, J. (1997). *Topological invariants, instantons and the chiral anomaly on spaces with torsion*. Phys. Rev. D, 55, 7580–7585.
* Calcagni, G., & Mercuri, S. (2009). *Barbero–Immirzi field in canonical formalism of pure gravity*. Phys. Rev. D, 79, 084004. arXiv:0902.0957.
* Mercuri, S., & Taveras, V. (2009). *Interaction of the Barbero–Immirzi field with matter and pseudo-scalar perturbations*. arXiv:0903.4407.
* Taveras, V., & Yunes, N. (2008). Phys. Rev. D, 78, 064070. arXiv:0807.2652.
* Kostelecký, V. A., Russell, N., & Tasson, J. D. (2008). *Constraints on torsion from bounds on Lorentz violation*. Phys. Rev. Lett., 100, 111102.
* Galley, C. R. (2013). *Classical mechanics of nonconservative systems*. Phys. Rev. Lett., 110, 174301. arXiv:1210.2745.
* Barron, L. D. (1986). *True and false chirality and parity violation*. Chem. Phys. Lett., 123, 423–427.

*Verification:* `scripts/torsion_action.py` (§III, and the inertness of the demanded term in §I); `scripts/bimedian_parity.py` (§IV: the inversion check, the $T_d$ character against $(x,y,z)$, and the parity/time-reversal table); `scripts/aggregate_parity.py` (§V); `scripts/engine_connection.py` (the U1 line in §IX, with Part One §IV).

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.

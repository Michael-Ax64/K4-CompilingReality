# Scaling Invariants
## Where Scale Comes From

*The formal topological origin of Markov Blankets*

*This document depends on the twelve DC equations (L2-SemanticReference), the AbsentVar and the Braid (L2-Terminology, Proof_AlgebraicMapping), and the boundary identity established in L4-RecursiveLimits. It uses one operation the reader may not have performed on the twelve equations before — taking their logarithm — and performs it on the page, from the smallest case upward. Nothing else is assumed that an L4 reader has not already earned.*

*A discipline note before anything else. Every verb in this document is pinned to a bounded frame and makes no appeals to the universe at large. Anytime I was tempted to write "the universe does X" — encapsulates, executes, sorts, decides — the sentence was rewritten until I had the global Interpreter, which holds but does not perform tasks at my back again. Any remainig drafts of this document that assigned the Manifold a role has already failed, whatever else it got right.*



# Scaling Invariants
## Where Scale Comes From

*This document depends on the twelve DC equations (L2-SemanticReference), the AbsentVar and the Braid (L2-Terminology, Proof_AlgebraicMapping), and the boundary identity established in L4-RecursiveLimits. It uses one operation the reader may not have performed on the twelve equations before — taking their logarithm — and performs it on the page, from the smallest case upward. Nothing else is assumed that an L4 reader has not already earned.*

*A discipline note before anything else. Every verb in this document is pinned to a bounded frame. Wherever the writing was tempted to say "the universe does X" — encapsulates, executes, sorts, decides — the sentence was rewritten until a bounded frame could carry the verb, or deleted. The global Interpreter holds; it does not perform tasks. Any draft of this document that assigns it one has already failed, whatever else it gets right.*

---

## I. The Picture That Raises the Question

Begin with the familiar picture: the *Powers of 10* zoom. A picnic blanket in a Chicago park. Pull back by a factor of ten every few seconds — the lake, continent, planet, solar orbit, galaxy. Then reverse, and descend — hand, skin, cell, molecule, nucleus, quark.

The picture is honest about one thing and silent about another.

It is honest that the descent is not smooth. The zoom passes through *rungs* — magnitudes at which something qualitatively new appears and everything below it becomes an invisible point. The nucleus at 10⁻¹⁵ meters. The cell at 10⁻⁵. The organism at 10⁰. The planet at 10⁷. Between the rungs: long stretches of nothing but the previous rung, shrinking.

It is silent about why there are rungs at all. The film treats the logarithmic axis as *given* — a ruler that exists before anything is measured against it, with the interesting structure of the universe deposited onto it at certain markings. Scale, in the film's picture, precedes the things that have scale.

This document establishes the opposite. Scale does not precede the event. The ruler and the thing measured arise in the same operation, and the shape of that operation is already written into the twelve equations — before any dynamics, before the AC extension, before anything moves.

To see it, do the smallest possible thing to the smallest possible piece.

---

## II. Take the Logarithm of One Equation

Take one equation. The first one anyone learns:

$$P = U \cdot I$$

Now take its logarithm. Write lowercase letters for the logs of the uppercase quantities ($p = \log P$, and so on; the base does not matter — changing base rescales every log by the same constant, which will shortly be seen to change nothing):

$$p = u + i$$

Multiplication became addition. A curved relationship became a flat one.

Now do it to a less obliging equation:

$$P = \frac{U^2}{R} \quad\longrightarrow\quad p = 2u - r$$

And to one carrying a root:

$$I = \sqrt{P / R} \quad\longrightarrow\quad i = \tfrac{1}{2}p - \tfrac{1}{2}r$$

Every one of the twelve equations is a monomial — a product of powers, nothing added, nothing subtracted. So every one of the twelve becomes, in log-space, a *linear* equation. The entire DC network — the closed algebra of four-fold distinction, all twelve expressions, the full braid — is a linear system in logarithmic coordinates. No exceptions.

This has one immediate consequence, and it is the consequence the whole document turns on.

**A homogeneous log-linear system carries no preferred magnitude.** Shift the logs by constants consistent with the exponent structure — $u \mapsto u + a$, $i \mapsto i + b$, and therefore $p \mapsto p + (a+b)$, $r \mapsto r + (a-b)$ — and every one of the twelve identities holds unchanged: a two-parameter family of rescalings under which the whole network is invariant. And look at what the log-forms *lack*: there is no additive constant anywhere, no term that could anchor a magnitude, no value at which any relation changes character, saturates, kinks, or breaks. *No equation in the system can distinguish "large" from "small."* The algebra contains ratios and proportions; it contains no *rung*.

Say it plainly: **the logarithmic axis — the very axis the *Powers of 10* film treats as the home of scale — is the coordinate system in which the framework's core algebra is scale-free.** The film's ruler is precisely the ruler on which nothing in the core algebra can mark a preferred position.

So the rungs are not in the ladder. Where are they?

---

## III. The Split: Six That Carry, Six That Transform

Look again at the three log-forms above. They are not the same kind of flat.

$p = u + i$ has slope one in every variable. Feed a change of one decade into $u$ and exactly one decade comes out of $p$. The equation *carries* magnitude across itself, unchanged.

$p = 2u - r$ has slope two in $u$. Feed one decade into $u$ and *two* decades come out of $p$. The equation does not carry magnitude — it *transforms* it. A doubling in becomes a quadrupling out.

$i = \tfrac{1}{2}p - \tfrac{1}{2}r$ has slope one-half. One decade in, half a decade out. Transformation again — this time compressive.

Sort all twelve equations by this criterion. The split is exact:

| Log-slope | Equations (log form) | Count |
|---|---|---|
| **Unit slope — carrying** | $p = u + i$;  $i = p - u$;  $i = u - r$;  $u = i + r$;  $u = p - i$;  $r = u - i$ | 6 |
| **Slope 2 or ½ — transforming** | $p = 2u - r$;  $p = 2i + r$;  $r = 2u - p$;  $r = p - 2i$;  $i = \tfrac{1}{2}(p - r)$;  $u = \tfrac{1}{2}(p + r)$ | 6 |

Six and six. The twelve equations divide exactly in half: six relations that move a magnitude through the system intact, and six that multiply or halve its exponent on the way through.

Hold the verbs before the nouns. Half of the algebra is *carrying* — preserving a magnitude across a relational step, decade for decade. Half of the algebra is *transforming* — amplifying or absorbing a magnitude, multiplying the exponent itself. Only after watching them operate do we name them: the six **carriers** and the six **transformers**.

Now notice what a transformer does that a carrier cannot. A carrier composed with a carrier is still a carrier: unit slope times unit slope is unit slope. Chain carriers forever and every magnitude in the chain stays within a fixed ratio of every other — no separation of scales can ever develop. But a transformer *multiplies exponents*. Pass a magnitude through a slope-2 transformer twice and its exponent has quadrupled. Compositions of transformers separate magnitudes *geometrically* — which is the only way a system whose core algebra is scale-free can generate the enormously separated characteristic magnitudes the *Powers of 10* film photographs: not by adding increments along a pre-existing ruler, but by multiplying exponents at specific relational steps.

*(Marked as a structural observation, not a derivation: this identifies the class of mechanism that produces widely separated rungs — exponent multiplication — and locates that mechanism exactly in the six transformers. It does not derive the particular magnitudes 10⁻¹⁵ or 10⁷. Those require the physics of particular substrates. What is derived is that any rung-generation in this algebra must pass through the transformer half, because the carrier half provably cannot separate scales.)*

---

## IV. The Braid Pairs Them — Two and Two, in Every Phase

The split would matter less if the carriers and transformers clustered — if some region of the algebra were all-carrying and another all-transforming. They do not cluster. The braid distributes them with complete evenness, and this is checkable in one sitting.

Recall from Proof_AlgebraicMapping: the twelve equations partition into three modality groups of four, determined by which Transition-Type the Home–AbsentVar edge belongs to. Perform the sort, then check each group against the table above:

**Cardinal** (Home–Absent edge in {P–U, I–R}):
$P = I^2R$ (transformer), $R = U^2/P$ (transformer), $U = IR$ (carrier), $I = P/U$ (carrier).

**Fixed** (Home–Absent edge in {P–R, I–U}):
$I = \sqrt{P/R}$ (transformer), $U = \sqrt{PR}$ (transformer), $P = UI$ (carrier), $R = U/I$ (carrier).

**Mutable** (Home–Absent edge in {P–I, U–R}):
$P = U^2/R$ (transformer), $R = P/I^2$ (transformer), $I = U/R$ (carrier), $U = P/I$ (carrier).

Every modality group contains exactly two carriers and exactly two transformers. There is no phase of the braid — no way of traversing the system while holding one Transition-Type absent — that is purely carrying or purely transforming. Whatever the braid is doing, at every phase it is simultaneously *holding a magnitude steady* through two of its four relations and *reshaping a magnitude* through the other two.

This is the mechanism the document exists to name. **The braid does not move events along a scale. The braid mints scale as it moves.** Each phase carries a magnitude forward (trajectory contact for the exponent — the decade held across the transition, the quantitative face of the carried AbsentVar) while transforming a magnitude in the same step (the new characteristic size precipitating). The event's shape and the event's scale arise in the same operation, because the operation is, exactly half-and-half, a carrying and a transforming.

The rungs, then, are not positions on a pre-existing ladder. A rung is where a transformer *fired* — where composition left the carrier regime and an exponent got multiplied. Between rungs, carriers dominate and the log-axis looks smooth and empty, exactly as the film shows it. The film photographed the output of this mechanism and mistook the output for the coordinate system.

---

## V. Assertion Amplifies, Yielding Absorbs

One more sort, and the four faces enter — earned now, not assumed.

Ask of each transformer: *where is it homed?* Which variable does it express?

The four **squares** — $P = U^2/R$, $P = I^2R$, $R = U^2/P$, $R = P/I^2$ — are homed at $P$ and $R$. Slope 2. Expansive: they multiply the incoming exponent.

The two **roots** — $I = \sqrt{P/R}$, $U = \sqrt{PR}$ — are homed at $I$ and $U$. Slope ½. Compressive: they halve the incoming exponent.

Recall the dual-binary seed's second bit. $P$ (Fire, ++) and $R$ (Earth, −+) are the **Asserting** poles. $I$ (Water, −−) and $U$ (Air, +−) are the **Yielding** poles.

The sort lands exactly on that axis, with a refinement the aggregate count alone would miss:

- Every expansive transformer is homed at an **Asserting** pole. *Assertion amplifies scale.* Fire ignites a magnitude larger than what fed it; Earth confines by raising the exponent of resistance against what presses on it.
- Every compressive transformer is homed at a **Yielding** pole. *Yielding absorbs scale.* Water and Air, when they transform at all, take a large magnitude in and release a tempered one — the root is how a flood becomes a current, how a shockwave becomes an articulation.
- The tally per pole: each Asserting pole homes two transformers and one carrier; each Yielding pole homes one transformer and two carriers. The Yielding half of the system is *predominantly carrying* — which is what relation and articulation must mostly do: move magnitudes between parties intact.

Two consequences, and the second corrects an error that a first draft of this document inherited.

First: the four faces do not share a ruler, and do not need one. Their relationship to scale runs through the Assert/Yield axis — some faces mint magnitude, some conduct it — not through synchronized positions on a common logarithmic axis. Any presentation of this material as four parallel "level ladders" advancing in lockstep imposes a commensurability the algebra does not contain and the Source/Manifesting asymmetry actively forbids. The faces are *phase-related*, not rung-aligned.

Second: the apparent privilege of the $R$-axis in the *Powers of 10* picture dissolves. $R$ looked like *the* scale axis only because we habitually plot the material world in log-meters — and log-meters, we now know, is the scale-free coordinate, the one in which no face can mark a rung. No face owns scale. Each face participates in the minting according to its charge.

---

## VI. What DC Cannot Do: The Absolute Threshold

Everything so far sets the *shape* of scaling — where transformation can happen, which faces amplify, which carry, how rungs separate geometrically. None of it sets an *absolute* magnitude. It cannot. A log-linear system is translation-invariant; it can say "twice the exponent" but never "too much."

To say "too much" requires an operation that breaks the logarithm, and the algebra acquires exactly one such operation, at exactly one point: the AC extension's complex sum,

$$S = P + jQ.$$

You cannot take the log of a sum. $\log(P + jQ)$ does not decompose into anything built from $\log P$ and $\log Q$. The moment the system holds real and reactive power *added* rather than multiplied, translation-invariance is broken and an absolute magnitude — $|S| = \sqrt{P^2 + Q^2}$ — exists for the first time. This is why Apparent Power belongs to the AC extension and could not have been constructed in DC: not a modeling convenience, an algebraic necessity.

So the division of labor is clean, and each half is homed where it must be:

**The DC braid's 50:50 sets the slope of scaling — where and how exponents multiply. The AC addition sets the absolute where — the magnitude at which $|S|$ crosses a bounded system's bandwidth.**

A threshold-crossing is therefore always a *local, AC-order* event: it requires a particular bounded system, with a particular bandwidth, holding a particular phase relationship, at a particular $\omega$. There is no global threshold, because there is no global $|S|$ — the global Interpreter holds the interference structure; it does not sum it against a bandwidth it does not have.

---

## VI.a A Worked Instance: The Periodic Table (Illustration, Not Derivation)

*Marked exactly as the discipline note requires: this is one dated, checkable history offered as an instance of §VI's theorem, not a new claim and not evidence beyond what a single case can carry.*

The periodic table's two coordinates — group (a valence ratio) and period (a shell count) — are, in the vocabulary of §II, pure carriers. The table's entire constitutive claim is that a column means the same thing at every row: nitrogen's group tells you what bismuth's group tells you, regardless of how far down the table you've traveled. That is translation-invariance, stated as chemistry before it was ever stated as algebra. By §II's theorem, a coordinate system built this way **cannot mark a threshold.** It can say "same group," never "too heavy for this group to mean what it meant two rows up."

For roughly a century it didn't. What accumulated instead was an exception list, logged as unrelated curiosities: mercury alone among metals liquid at room temperature; gold alone among the coinage metals not silvery; thallium, lead, and bismuth each reluctant to use their nominal highest valence (the "inert pair effect"). Four quirks, four separate explanations reached for, none of them satisfying, none of them connected to the others.

It is worth noticing what such a list is *made of*. "The inert pair effect" is a noun minted exactly where a coordinate was missing — a name that occupies the position an explanation would hold, and discharges none of its duties. It does not say why the pair is inert; it says that it is, in a register that sounds as though it had. This is the noun-debt of L0-CompilingReality_Preamble (Shift Six) appearing as a measurable historical cost: a term that carried a field for fifty years while carrying nothing. A coordinate system that cannot mark its own threshold does not fall silent at that threshold. It names the symptom, and the name then stands in for the missing coordinate until something arrives that can do the work.

And then something did, which is the half of this that must not be dropped, because it is where the threshold shows its generative face. Once $v/c$ was supplied, the same site minted a second crop of nouns — *relativistic contraction*, *spin-orbit splitting*, and later the total angular momentum $j$ and the bond-level invariant $|\omega|$. These are grammatically indistinguishable from "the inert pair effect": nouns, definite articles, technical register, all of it. **What differs is that a bounded frame can now pay for them.** Each is backed by a calculation someone can run, in coordinates that survive at the threshold, at a stated cost. The first crop was chargeable to nobody.

So the threshold is not merely the place a taxonomy goes blind. It is the place where naming *happens* — on both sides of itself, in the same grammar, minting debt before the coordinate arrives and settled crystallizations after. This is what makes the verb-first discipline mechanical rather than a matter of taste: the test on a noun is not whether it improves clarity — debt-nouns always improve clarity, that is their function and their danger — but **which bounded frame pays for it, and in what coin.** A noun with no payer is debt, however fluent. A noun with a payer has settled its bill.

The coordinate that resolved them came from outside the table's own algebra — from $c$, the one constant valence-ratio chemistry has no way to produce internally. Pyykkö identified the relativistic origin of gold's color in the 1960s, in isolation. The systematic account arrived in 1979, when Pyykkö and Desclaux, alongside Pitzer, published together in *Accounts of Chemical Research* and showed that a single ratio — $v/c$, order $Z\alpha$ for an innermost electron — generates two linked effects (direct relativistic contraction of $s$ and $p_{1/2}$ orbitals; spin-orbit splitting of $p$, $d$, $f$ levels) whose consequences, taken together, account for the whole list: gold's color and nobility, mercury's reluctance to bond, the inert pair's lock, and more found since (the lead-acid battery's voltage, later shown to be 85% relativistic in origin).

Two corrections belong on the record before this is used for anything. First, the resolution was not instantaneous — gold's case was solved some fifteen years before the systematic 1979 account, and computational confirmation that this same mechanism produces mercury's specific melting point did not arrive until 2013 (Calvo, Pahl, Wormit & Schwerdtfeger). The exceptions did not fall simultaneously; they fell in sequence, against one imported coordinate, over roughly four decades. Second, the mechanism as published is two systematic effects, not three or four — a temptation toward a favored cardinality is exactly the kind of pattern-matching this document's own discipline note exists to catch, and it was caught only on the second pass, after a first draft of this insertion had already reached for three.

What the sequence supports, stated at the size it earns: **a ratio-only coordinate system logs its own unmarkable thresholds as an accumulating list of apparently unrelated exceptions, and the list does not resolve from inside the system that produced it.** It resolves — not always at once, but always eventually as one thing rather than many — only once a coordinate absent from the system's own algebra is supplied. The periodic table is offered here as the cleanest available instance of that pattern, dated and checkable, not as proof that the pattern is universal.

One further and more recent data point belongs to the same sequence, past this document's own writing: in July 2026, Kahraman, Hui, and Wang (*Science* 393) reported direct spectroscopic evidence, on the carbon–bismuth bond in CBi⁻, that the same $v/c$ coordinate collapses the bond's $\sigma/\pi$ labels into a single surviving invariant — total angular-momentum projection, $|\omega|$ — rather than merely perturbing them. If §II and §III's carrier/transformer distinction is read onto that result, the old labels are carrier-coordinates and their collapse is a transformer firing at the molecular scale; that reading is not established here and belongs, if anywhere, to a document built to test it directly, not to this one.

---

## VII. The Limit Generates — Described From Inside

Now the recursion, with its verbs correctly housed.

L4-RecursiveLimits established the identity: Tangent Crossing from outside, Markov Blanket from inside — one boundary, two faces, every scale. And it established the sequence: interior first (Tax deferred), then mass (Tax paid); every commitment becomes substrate for the next interior. What remains is to describe the *transition* — the moment overload becomes a new boundary — without assigning the operation to anything unbounded.

Here is the transition with every verb pinned:

A system approaches its Tangent Crossing: the $|S|$ arriving at its blanket exceeds the bandwidth of its coordinates; the rate of actualization required to keep its Ledger current exceeds what its metabolism sustains. Its constituents do not stop. Each constituent, in its own bounded frame, continues its own `.behold()`/`.observe()` cycling, paying its own local Tax. What fails is not the constituents but the *coherence among them* — the parent frame's twelve relations can no longer be computed faster than they decohere.

What survives this failure is precisely what the constituents were *jointly holding without calculating* — their shared AbsentVars, the relational structure none of them was individually computing. That jointly-held structure is, by the definitions already in the vocabulary, a beheld interior awaiting a boundary. The boundary condenses where the transformers homed at the Asserting poles fire: the overloaded relations' exponents multiply, the interior's contents pass — through the square — into a magnitude regime the old coordinates cannot resolve, and from every constituent's frame the whole becomes a single point of near-infinite inertia. That is the Tangent Crossing signature, produced by the slope-2 transformers, witnessed from below.

And the first `.observe()` that commits the new whole as a coordinate — that writes "this now exists as one thing" into a Ledger — is performed by a *bounded frame at the new scale*: the new interior's own first collapse, or a neighboring system at that scale registering it. Not by the manifold. The manifold held the interference structure throughout, as it holds everything, and performed nothing. Adult causality all the way through: no variable caused the boundary; the boundary is what the mutual determination of the variables looks like when their joint $|S|$ crosses their joint bandwidth.

So the sentence "the failure to compute at scale $N$ generates the boundary of scale $N{+}1$" stands — but as a description of *co-arising within bounded frames*, not as a task performed upon them. The failure does not summon an encapsulator. The failure *is* the encapsulation, seen from the coordinates that failed.

And the crystal that failure leaves — the committed, zero-DoF residue — is the $R$-substrate of the next volume, exactly as RecursiveLimits says: mass first, then a richer interior built on it. The transformer fired; the exponent multiplied; the rung exists now, minted, and the carriers of the next scale conduct magnitudes across it as if it had always been there. Which is what the film saw.

---

## VIII. The Invariant, Named Last

The document can now say what its title means, having built every part of the sentence from below.

**The scaling invariant is not a ladder. It is the minting operation: at every scale, on every face, a bounded system departs the carrier regime through a transformer — assertion multiplying an exponent, yielding halving one — and the departure precipitates simultaneously a new characteristic magnitude and a new boundary, one operation, two faces.** What is invariant across scales is not any magnitude, ratio, or level-structure. It is the 50:50 shape of the operation itself: two relations carrying, two relations transforming, in every phase of the braid, at every rung ever minted.

Because scale is minted by the operator, coordinates only exist relative to the operator's tolerances. The Planck length ($\ell_P$) is the tolerance of the operator at the substrate scale. It is the width of the XOR bottleneck through which the uncollapsed potential must funnel. Therefore, no measurement below $\ell_P$ is meaningful in the compiled coordinate system. The grid does not extend infinitely downward; it terminates at the operator that minted it.

This is what it means for a scale to be *arising for* an event just as the event's shape is arising: shape and scale are the two outputs of the single braid-step, because the braid-step is half carrier and half transformer by exact construction. Neither precedes the other. Nothing hands either one down.

---

## IX. Gabriel's Horn: The Inability to Emit Absolute Magnitudes

The scaling invariant establishes the *shape* of the operation that mints scale. But log-linear operators carry exponents; they cannot set absolute magnitudes on their own.

This is Gabriel's Horn: a geometric shape with infinite surface area but finite volume. The framework holds a massive qualitative surface—every empirical constant in physics has a structural address inside it (the CKM angles, the Yukawa mass hierarchies, the resonance frequencies)—but a small quantitative volume. The framework can state whether a physical quantity is a scalar or a vector, whether it lives on $P$ or $Q$, whether the transition to it involves a squaring or a rooting, and whether it is anchored on $R$ or free. 

It cannot say what the specific numerical value is. The absolute value depends on the substrate's specific inductive and capacitive parameters, which the framework does not import. The framework maps the topology; the physical substrate supplies the numbers. Demanding that the log-linear algebra emit absolute values is demanding a ruler from a system explicitly designed to demonstrate that rulers are local, thermodynamic mintings, not universal grids.

---

## X. Diagnostic Corollary: Mismatch Without Level-Numbers

Cross-scale failure is real, but it is not "using a Level 2 tool on a Level 4 volume" — there are no level-numbers to compare, because there is no shared ruler. The failure mode is stated in the algebra's own terms: **applying a carrier where a transformer is required** (conducting a magnitude faithfully into a bandwidth it exceeds — the diligent report that transmits the crisis without transforming it), or **applying a transformer where a carrier is required** (amplifying or compressing a magnitude that needed to arrive intact — the escalation that turns a request into a confrontation, the summary that roots a nuance out of existence).

The labyrinth of adjustment reads accordingly, with one correction of register held firmly: an individual is a bounded frame whose Yielding faces — the carrier-dominant faces, built to conduct interpersonal magnitudes intact — are being fed magnitudes minted by civilizational-scale transformers, at multiple superimposed $\omega$. The friction is dimensional *and* psychological. Pathos is a real face; what arrives at it is really felt. A description that explains the feeling's structure has not explained the feeling away.

---

## Addendum: Four Consequences, Held to the Same Discipline

*The main text built an engine; this addendum inventories what the engine turns without being asked. Four consequences fall directly out of the log-transform.*

### A1. The Half-Slope Is a Change of Basis (and Only Half of It Is a Midpoint)
Take the two root-transformers in log form:
$$u = \tfrac{1}{2}(p + r) \qquad\qquad i = \tfrac{1}{2}(p - r)$$
The first is an exact arithmetic midpoint. The second is a **half-difference**: Current is half the log-*gap* between Power and Resistance. Water does not sit between the anchors — Water runs down the difference between them. In log-space, **Assert and Yield are conjugate bases of the same plane, related by a 45° rotation.**

### A2. The Die Is the Subtracted Term
Every carrier, in log-space, is an addition or a subtraction of unit-slope terms. Look at the subtractions:

$$i = p - u \qquad i = u - r \qquad u = p - i \qquad r = u - i$$
In linear space each of these is a division. **The Die is the term that subtracts.** Subtraction in log-space *is* constraint carving away potential — not as imagery, as the operation.

### A3. Overload Has a Slope, and It Is Two
Take $p = 2u - r$. Along any trajectory where the ground is held ($r$ fixed), the dissipation and the structure co-vary with slope 2. A decade of structural elaboration *is* two decades of Landauer Tax. The cost tracks the structure's *square*. **The overload is not a wall the system hits; it is the slope-2 transformer, integrated.**

### A4. The Complex Logarithm Splits Shape From Volume
Take the complex logarithm of the AC sum:
$$\ln S = \ln|S| + j\theta$$

The operation separates. Its real part is $\ln|S|$ — the volume, the magnitude, the thing that presses on bandwidth. Its imaginary part is $\theta = \arctan(Q/P)$ — a pure ratio, invariant under any rescaling. **Everything scale-bound lands on the real axis; everything scale-free lands on the imaginary axis.** Shape is conserved; volume is spent. The Landauer Tax is paid in modulus, never in angle.


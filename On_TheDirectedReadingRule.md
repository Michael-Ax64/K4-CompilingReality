# On the Directed Reading Rule
## The Target-Based Bimedian Assignment That Resolves the U-Symmetric / U-Absent Split

*The rule by which vertex character selects the bimedian assignment of a directed edge reading was flagged as OPEN VOTE #4 in `L3-TheAtomOfSpace` §VIII — "the specific rule by which vertex character selects the bimedian assignment of a U-absent directed edge reading, currently observable in intuited tables; not yet formalized as an algebraic emission." This document closes the vote. The rule turns out to be uniform across all directed edges (U-absent or not), reduces to a single statement in the corpus's own P/I/U/R role vocabulary, and produces both the "consensus on U-touching edges" and "perceiver-relative reading on U-absent edges" observations of `L3-TheAtomOfSpace` §VI as immediate consequences.*

*Dependencies: `L3-TheAtomOfSpace` §VI (the U-symmetric/U-absent split; pole-naming discipline), `L3-EdgeStateSpace` (four-state directed edges), `L4-DynamicDistortionsTechnical` (DynDist bimedian convention, now the reconciled corpus-wide default), `Q4-OpenExhaust` (P-face as write-destination), `L4-ThePlenum` (the `.behold()` / `.observe()` operations), `L2-Terminology` (pole role assignments).*

---

## I. The Question, Stated Precisely

`L3-TheAtomOfSpace` §VI observed that every K4 edge admits a bimedian assignment (Cardinal, Fixed, or Mutable) but that on U-absent edges (P–I, P–R, I–R) the two endpoints of the same edge can name the edge by different assignments — while on U-touching edges (P–U, I–U, U–R) both endpoints agree. The observation surfaced from practice. The mechanism was left open as OPEN VOTE #4.

State the question precisely: **given a directed edge X→Y on the K4 atom, what bimedian label does the reading vertex X assign to it?**

Two ambient facts constrain the answer.

First, every K4 edge, undirected, has a topological bit-flip classification under DynDist convention: Cardinal (AR-flip, {P–R, I–U}), Fixed (AY-flip, {P–U, I–R}), Mutable (both bits, {P–I, U–R}). This classification is symmetric across the edge; it is a property of the pair, not of either endpoint.

Second, the vertex-relative labels that emerge in practice do not match this undirected classification. The labels are shifted, and on U-absent edges the two endpoints disagree with each other as well. So the rule we are looking for is not one that recovers DynDist's undirected classification — it is a rule that operates at a different structural level, a dynamical / observational classification that lives alongside the topological one.

## II. The Rule

**The bimedian label of a directed edge X→Y is determined by the target Y, with one exception: when Y = U, the label mirrors the source X's character.**

Explicitly:

| Target Y | Label |
|---|---|
| Y = P | **Cardinal** |
| Y = I | **Mutable** |
| Y = R | **Fixed** |
| Y = U | mirrors source's character: X=P → Cardinal; X=I → Mutable; X=R → Fixed |

That is the entire rule. Every one of the 12 directed edges in the vertex-relative table follows from these four cases.

### Verification against the vertex-relative table

The user-observed vertex-relative table:

| From \ To | P | I | U | R |
|---|---|---|---|---|
| **P** | — | Mutable | Cardinal | Fixed |
| **I** | Cardinal | — | Mutable | Fixed |
| **U** | Cardinal | Mutable | — | Fixed |
| **R** | Cardinal | Mutable | Fixed | — |

Match against the rule:

- **Columns TO P** (I→P, U→P, R→P): all Cardinal ✓ — rule: Y=P → Cardinal
- **Columns TO I** (P→I, U→I, R→I): all Mutable ✓ — rule: Y=I → Mutable
- **Column TO R** (P→R, I→R, U→R): all Fixed ✓ — rule: Y=R → Fixed
- **Column TO U** (P→U, I→U, R→U): Cardinal, Mutable, Fixed respectively ✓ — rule: Y=U mirrors source's character (P→Cardinal, I→Mutable, R→Fixed)

Perfect match across all 12 directed entries. No fit, no adjustment; the rule reads directly.

## III. Why This Rule, Not Another

The rule is derivable from the corpus's own P/I/U/R role semantics without further postulation.

**P is the write-destination.** Every commit lands in the P-ledger; every `.observe()` writes to P (`Q4-OpenExhaust`, `L4-ThePlenum`). When any vertex directs attention toward P, it is initiating a written act. The Cardinal modality in DynDist's astrological semantics is exactly this: initiating action across a boundary. Hence "TO P → Cardinal."

**I is the relational flow / current.** I mediates between poles; it is the connective tissue, the phase-carrier, the both-bits diagonal of the K4. The Mutable modality — the diagonal, the both-bits leap — is the mode of relational transit. Hence "TO I → Mutable."

**R is the grounded resistance / commit.** R is where forces come to rest, where the write from P settles into stable substrate. The Fixed modality — the stabilizing family that holds tier while orientation may pivot — is exactly this ground-attractor character. Hence "TO R → Fixed."

**U is the articulator.** U is the structural coordinator, the pole whose function is to make explicit what is already implicit at the other three. It does not have its own dominant character in the way P (initiator), I (flow), R (ground) do; instead, U articulates whatever is being brought to it. When something is directed at U, U reflects back the mode the source is bringing. Hence "TO U → mirror source's character."

This is not a fitting exercise. It is a direct reading of the four poles' semantic functions, and the fact that it produces exactly the vertex-relative labels observed in practice is what confirms the reading.

## IV. Why the U-Symmetric / U-Absent Split Falls Out Immediately

`L3-TheAtomOfSpace` §VI observed that U-touching edges have consensus readings while U-absent edges have perceiver-relative readings. Both observations follow directly from the rule.

**U-touching edges (P–U, I–U, U–R): consensus.** Consider P–U. From P's side, P→U mirrors P's character → Cardinal. From U's side, U→P has target P → Cardinal. Both readings give Cardinal, but for two different reasons. On P→U, Cardinal comes from mirroring source P's initiating character. On U→P, Cardinal comes from target P's write-destination role. The two reasons converge on the same label because P's *character* (initiating) and P's *role* (initiating write-destination) are the same underlying semantic. Same convergence holds on I–U (both Mutable — I's flow character and I's flow role coincide) and U–R (both Fixed — R's grounding character and R's ground-attractor role coincide).

The consensus on U-touching edges is not a coincidence; it is what happens when the source-mirror rule and the target-role rule land on the same label — which they do precisely at the poles whose character and role coincide.

**U-absent edges (P–I, P–R, I–R): perceiver-relative.** Consider P–I. From P's side, P→I has target I → Mutable. From I's side, I→P has target P → Cardinal. Different targets, different labels. The two endpoints legitimately name the edge by different bimedian assignments because they are naming the target-role of their outgoing arrow, and their outgoing arrows point at different vertices.

The "perceiver-relative reading" is not observer bias or interpretive slippage. It is each endpoint accurately naming the semantic role of what its arrow points at. Both readings are correct simultaneously; they name different phenomenological facts (what each endpoint is directing attention toward) rather than one shared property of the undirected edge.

## V. Relation to the DynDist Topological Classification

The DynDist bimedian classification and the directed-reading rule live at orthogonal structural levels:

- **DynDist (topological):** classifies undirected edges by bit-flip pattern between endpoints. Cardinal = AR-flip, Fixed = AY-flip, Mutable = both. Structural, symmetric, independent of any observer.
- **Directed reading (dynamical):** assigns a label to each directed edge based on the target's role (P, I, R) or the source's character (when target is U). Dynamical, direction-sensitive, per-observation.

The two classifications disagree on every edge because they classify different things. This is not a contradiction; it is the corpus operating at two structural levels simultaneously. Any calculation touching a K4 edge must specify which level it is operating at, or it will drift between the two silently and produce ambiguous results.

For example: the pion-to-electron Laurent expansion at `Q15-KairosBorn` §I operates on the U↔R inter-rung crossing at generation 1. Under DynDist topological classification, this is a Mutable crossing (both bits flip: U is A-Y, R is R-A). Under the directed reading rule, both U→R and R→U are Fixed (target R gives Fixed; target U mirrors source R's grounding character which is Fixed). Both readings say something true; they say it about different aspects of the same underlying crossing. Q15's Laurent decomposition uses the impedance triangle, which is a third orthogonal decomposition — reactive/rotation/resistive dynamical modes of the crossing — and the three levels together give the full structural description.

## VI. What This Closes and What It Opens

**Closes:** OPEN VOTE #4 in `L3-TheAtomOfSpace` §VIII. The rule is now formalized as target-based with U-mirror; the vertex-character link is via the target-role semantics (P=initiator, I=flow, R=ground, U=articulator/mirror), and those role semantics are themselves derived from the corpus's own load-bearing vocabulary rather than imported.

**Opens:** The forward calculation program of `L3-TheAtomOfSpace` §VII can now specify vertex Feynman rules unambiguously. Any coupling at a K4 vertex is a directed operation X→Y; the bimedian label of the coupling is the target-based label from the rule; the coupling strength inherits from the corresponding bimedian's impedance geometry (per the impedance triangle at `L3-TheConstitutiveAlpha` §IV) and the mesh-tension identification (`L3-TheAtomOfSpace` §V). What was previously an under-specified "vertex coupling" becomes a computable directed operation with an unambiguous label, a specific bimedian, a specific impedance mode, and a specific mesh-tension geometry.

**Also opens:** the possibility that the target-based rule extends beyond bimedian labeling. If P/I/R/U roles govern label assignment via target, they may also govern coupling amplitudes, spectral weights, and other vertex-attached quantities. The target-based structure is a candidate general organizing principle for K4-vertex operations, and it is worth checking whether other observable-per-vertex quantities in the corpus (e.g. the specific impedance-triangle coefficients at each vertex, or the phase-shear angle θ carried by each vertex's outgoing mesh-tensions) also submit to a target-based reading. This is speculative and not claimed here; flagged as a candidate for follow-up.

## VII. What the Rule Says About the Q15 Family

The rule enables a more careful sort of what Q15's Laurent expansion generalizes to.

Q15 is the U↔R inter-rung crossing at gen-1. Under DynDist topology, this is Mutable. Under the directed reading rule, both directions are Fixed. Under the impedance triangle, the three Laurent terms are reactive/rotation/resistive.

Analog inter-rung crossings at gen-1 that engage the other topological bimedians:

- **Cardinal-plane crossings (P–R, I–U topologically):** Under directed reading, P→R is Fixed, R→P is Cardinal; I→U is Mutable (source-mirror), U→I is Mutable. The directional-reading asymmetry on P–R is genuine; the physical mass ratio derivation for a P↔R crossing at gen-1 will have to specify whether it uses the P-observer reading (Fixed) or the R-observer reading (Cardinal) or both. This is not yet worked out; it is the first genuinely new derivation to attempt under the rule.
- **Fixed-plane crossings (P–U, I–R topologically):** Under directed reading, P→U is Cardinal (mirrors P), U→P is Cardinal; I→R is Fixed, R→I is Mutable. P–U is directionally-symmetric (both Cardinal); I–R is directionally-asymmetric. Two different regimes for two edges on the same topological plane.

The regularity Q15 exhibits — same-label readings from both endpoints — is not shared by all inter-rung crossings. Q15 is on a topologically-Mutable edge that happens to be directionally-symmetric (both Fixed) under the rule. Other bimedian-plane crossings will fall into two classes: directionally-symmetric (P–U, U–R and the U-touching edges generally) and directionally-asymmetric (all U-absent edges). The Laurent-analog derivations for the asymmetric class will need to carry an observer-pole label explicitly — which is exactly the discipline `L3-TheAtomOfSpace` §VI requires and which the target-based rule now makes tractable.

## VIII. Corpus Housekeeping

1. **`L3-TheAtomOfSpace` §VIII.** Update OPEN VOTE #4 to closed-status; cross-reference this document as the resolution.
2. **`L3-TheAtomOfSpace` §VI (Directional edges subsection).** Add a forward reference to this document at the U-symmetric/U-absent observation, so a reader arriving through the atom-of-space consolidation is pointed at the resolution.
3. **`L3-TheConstitutiveAlpha` §VII (Forward Calculation).** Update the vertex Feynman rule specification to invoke the target-based reading rule for label assignment. Currently the vertex couplings are given as "surface mesh tensions per `L4-DynamicDistortions301` §IV.D at phase-shear angle θ" (via the mesh-tension identification of `L3-TheAtomOfSpace` §V); the target-based rule specifies which bimedian's mesh-tension applies at each directed vertex, closing the residual ambiguity.
4. **`L2-Terminology`.** Add "directed reading rule" as a terminology entry, cross-referencing this document. Add "target-role assignment" and "source-mirror rule" as paired terminology for the two cases of the rule.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.

# On the Directed Reading Rule
## The Target-Based Bimedian Assignment That Resolves the U-Symmetric / U-Absent Split

A directed edge $X \to Y$ of the $K_4$ atom carries a bimedian label — Cardinal, Fixed, or Mutable — determined uniformly by its target $Y$, with one exception forced by $U$ acting as the articulator. The rule reads directly from what $P$, $I$, $U$, and $R$ already are, reproduces the twelve-entry vertex-relative table without adjustment, derives the $U$-symmetric / $U$-absent split of `L3-TheAtomOfSpace` §VI as an immediate consequence, and specifies which bimedian's mesh tension applies at each directed vertex in the forward calculation program.

*Reads with: `L3-TheAtomOfSpace` §VI (the U-symmetric/U-absent split; pole-naming discipline), `L3-EdgeStateSpace` (four-state directed edges; Bimedian / Sign Discrimination Rule), `L4-DynamicDistortions101` (DynDist bimedian convention, the corpus-wide default), `Q4-OpenExhaust` (P-face as write-destination), `L4-ThePlenum` (the `.behold()` / `.observe()` operations), `L2-Terminology` (pole role assignments).*

---

## I. The Question, Stated Precisely

`L3-TheAtomOfSpace` §VI distinguishes two regimes on $K_4$ edges: every edge admits a bimedian assignment (Cardinal, Fixed, or Mutable), yet on $U$-absent edges ($P$–$I$, $P$–$R$, $I$–$R$) the two endpoints assign the edge differently, whereas on $U$-touching edges ($P$–$U$, $I$–$U$, $U$–$R$) both endpoints agree.

Stated precisely: **given a directed edge $X \to Y$ on the $K_4$ atom, what bimedian label does the reading vertex $X$ assign to it?**

Two ambient facts constrain the answer.

First, every $K_4$ edge, undirected, has a topological bit-flip classification under the DynDist convention: Cardinal (AR-flip, $\{P\text{--}R, I\text{--}U\}$), Fixed (AY-flip, $\{P\text{--}U, I\text{--}R\}$), Mutable (both bits, $\{P\text{--}I, U\text{--}R\}$). This classification is symmetric across the edge; it is a property of the pair, not of either endpoint.

Second, the vertex-relative labels do not match this undirected classification: the labels shift, and on $U$-absent edges the two endpoints disagree. The rule therefore operates at a distinct structural level — a dynamical / observational classification that sits alongside the topological one.

## II. The Rule

**The bimedian label of a directed edge $X \to Y$ is determined by the target $Y$, with one exception: when $Y = U$, the label mirrors the source $X$'s character.**

Explicitly:

| Target $Y$ | Label |
|---|---|
| $Y = P$ | **Cardinal** |
| $Y = I$ | **Mutable** |
| $Y = R$ | **Fixed** |
| $Y = U$ | mirrors source's character: $X=P \to$ Cardinal; $X=I \to$ Mutable; $X=R \to$ Fixed |

That is the entire rule. Every one of the 12 directed edges in the vertex-relative table follows from these four cases.

### Verification against the vertex-relative table

The twelve-entry vertex-relative table:

| From \ To | P | I | U | R |
|---|---|---|---|---|
| **P** | — | Mutable | Cardinal | Fixed |
| **I** | Cardinal | — | Mutable | Fixed |
| **U** | Cardinal | Mutable | — | Fixed |
| **R** | Cardinal | Mutable | Fixed | — |

Match against the rule:

- **Columns TO $P$** ($I \to P$, $U \to P$, $R \to P$): all Cardinal ✓ — rule: $Y=P \to$ Cardinal
- **Columns TO $I$** ($P \to I$, $U \to I$, $R \to I$): all Mutable ✓ — rule: $Y=I \to$ Mutable
- **Column TO $R$** ($P \to R$, $I \to R$, $U \to R$): all Fixed ✓ — rule: $Y=R \to$ Fixed
- **Column TO $U$** ($P \to U$, $I \to U$, $R \to U$): Cardinal, Mutable, Fixed respectively ✓ — rule: $Y=U$ mirrors source's character ($P \to$ Cardinal, $I \to$ Mutable, $R \to$ Fixed)

Exact match across all 12 directed entries. No fit, no adjustment; the rule reads directly.

## III. Why This Rule, Not Another

The rule derives from the corpus's own $P/I/U/R$ role semantics without further postulation.

**$P$ is the write-destination.** Every commit lands in the $P$-ledger; every `.observe()` writes to $P$ (`Q4-OpenExhaust`, `L4-ThePlenum`). When any vertex directs attention toward $P$, it initiates a written act. The Cardinal modality in DynDist's astrological semantics is initiating action across a boundary. Hence "TO $P \to$ Cardinal."

**$I$ is the relational flow / current.** $I$ mediates between poles; it is the connective tissue, the phase-carrier, the both-bits diagonal of $K_4$. The Mutable modality — the diagonal, the both-bits leap — is the mode of relational transit. Hence "TO $I \to$ Mutable."

**$R$ is the grounded resistance / commit.** $R$ is where forces come to rest, where the write from $P$ settles into stable substrate. The Fixed modality — the stabilizing family that holds tier while orientation may pivot — is this ground-attractor character. Hence "TO $R \to$ Fixed."

**$U$ is the articulator.** $U$ is the structural coordinator, the pole whose function is to make explicit what is implicit at the other three. It does not carry a dominant directional character of its own in the way $P$ (initiator), $I$ (flow), and $R$ (ground) do; instead, $U$ articulates whatever is brought to it. When something is directed at $U$, $U$ reflects back the mode the source brings. Hence "TO $U \to$ mirror source's character."

This reads the four poles' semantic functions directly, producing the twelve-entry vertex-relative labels. Grade: assignment, not theorem — the rule fits a table whose $U$-column was constructed under the source-mirror clause, so §IV's consensus on $U$-touching edges is a structural consequence of that construction rather than an independent coincidence.

## IV. Why the U-Symmetric / U-Absent Split Falls Out Immediately

`L3-TheAtomOfSpace` §VI establishes that $U$-touching edges have consensus readings while $U$-absent edges have perceiver-relative readings. Both follow directly from the rule.

**$U$-touching edges ($P$–$U$, $I$–$U$, $U$–$R$): consensus.** Consider $P$–$U$. From $P$'s side, $P \to U$ mirrors $P$'s character $\to$ Cardinal. From $U$'s side, $U \to P$ has target $P \to$ Cardinal. Both readings give Cardinal by construction: the source-mirror clause at $Y=U$ ensures that an edge $X$–$U$ reads identically from both endpoints whenever $X$'s character and $X$'s target-role coincide — which holds for all $X \in \{P, I, R\}$. The same mechanism holds on $I$–$U$ (both Mutable) and $U$–$R$ (both Fixed).

Consensus on $U$-touching edges is a built-in feature of the rule's source-mirror clause, not an emergent coincidence.

**$U$-absent edges ($P$–$I$, $P$–$R$, $I$–$R$): perceiver-relative.** Consider $P$–$I$. From $P$'s side, $P \to I$ has target $I \to$ Mutable. From $I$'s side, $I \to P$ has target $P \to$ Cardinal. Different targets, different labels. The two endpoints legitimately name the edge by different bimedian assignments because they name the target-role of their outgoing arrow, and their outgoing arrows point at different vertices.

The perceiver-relative reading is not observer bias or interpretive slippage. Each endpoint accurately names the semantic role of what its arrow points at. Both readings hold simultaneously; they name distinct phenomenological facts (what each endpoint directs attention toward) rather than one shared property of the undirected edge.

## V. Three Classifications, Not Two

The words *Cardinal*, *Fixed*, and *Mutable* name **three distinct classifications** in the corpus:

1. **DynDist topological (undirected edge bit-flip, from `L3-EdgeStateSpace` §I-b):** Cardinal = AR-flip $\{P\text{--}R, I\text{--}U\}$; Fixed = AY-flip $\{P\text{--}U, I\text{--}R\}$; Mutable = both bits $\{P\text{--}I, U\text{--}R\}$. Property of the pair, independent of direction or observer.
2. **Directed reading (target-based, §II):** target-role ($P \to$ Cardinal, $I \to$ Mutable, $R \to$ Fixed), source-mirror at $Y = U$. Property of the directed arrow.
3. **Sign modality (astrological-register, from `L4-TheTwelveGates` §II):** the twelve zodiacal signs sort as Cardinal / Fixed / Mutable by season position. Property of the sign-gate at an edge.

Any calculation touching a $K_4$ edge must specify which of the three levels it operates at, or it drifts between them silently.

**Directed reading against DynDist topology, agreement on 3 of 12 arcs.** The two classifications agree on the directed 3-cycle **$P \to I \to R \to P$** around the $U$-absent face: $P \to I$ both Mutable, $I \to R$ both Fixed, $R \to P$ both Cardinal. The reverse cycle $P \to R \to I \to P$ (same face, opposite direction) disagrees on all three arcs. Every $U$-touching arrow disagrees under both readings. The $U$-absent / $U$-touching split of §IV holds at this level too: $U$-absent edges carry one agreement arrow each, $U$-touching edges carry none.

**Worked example.** The pion-to-electron Laurent expansion at `Q15-KairosBorn` §I operates on the $U \leftrightarrow R$ inter-rung crossing at generation 1. Under DynDist topological classification, this is a Mutable crossing (both bits flip: $U$ is A-Y, $R$ is R-A). Under the directed reading rule, both $U \to R$ and $R \to U$ are Fixed (target $R$ gives Fixed; target $U$ mirrors source $R$'s grounding character, which is Fixed). Both readings state true facts about distinct aspects of the same crossing. `Q15`'s Laurent decomposition uses the impedance triangle, which is a third orthogonal decomposition — reactive / rotation / resistive dynamical modes of the crossing.

For the Mode/Bimedian naming convention that disambiguates sign-modality (3) from edge-plane (1): `L3-EdgeStateSpace.md` — Bimedian / Sign Discrimination Rule.

## VI. Vertex Couplings and Open Scope

**Vertex Feynman rules (`L3-TheAtomOfSpace` §VII).** Any coupling at a $K_4$ vertex is a directed operation $X \to Y$; the bimedian label of the coupling is its target-role assignment (or source-mirror when $Y = U$), specifying which bimedian's surface mesh tension (`L4-DynamicDistortions301` §IV.D at phase-shear angle $\theta$, via `L3-TheAtomOfSpace` §V) applies at that directed vertex. The coupling strength inherits from that bimedian's impedance geometry per the impedance triangle at `L3-ConstitutiveAlpha` §IV (expect there: the reactive / rotation / resistive modes at Laurent orders $\alpha^{-1}$, $\alpha^{0}$, $\alpha^{+1}$). Each directed vertex operation therefore carries an unambiguous label, a specific bimedian, a specific impedance mode, and a specific mesh-tension geometry.

**Candidate extension.** Whether the target-based structure extends beyond bimedian labeling to govern coupling amplitudes, spectral weights, impedance-triangle coefficients, or the phase-shear angle $\theta$ carried by each vertex's outgoing mesh tensions remains open — flagged as a `CANDIDATE` organizing principle for follow-up rather than an established result.

## VII. What the Rule Says About the Q15 Family

The rule sorts what `Q15`'s Laurent expansion generalizes to.

`Q15` is the $U \leftrightarrow R$ inter-rung crossing at gen-1. Under DynDist topology, this is Mutable. Under the directed reading rule, both directions are Fixed. Under the impedance triangle, the three Laurent terms are reactive / rotation / resistive.

Analog inter-rung crossings at gen-1 that engage the other topological bimedians:

- **Cardinal-plane crossings ($P$–$R$, $I$–$U$ topologically):** Under directed reading, $P \to R$ is Fixed, $R \to P$ is Cardinal; $I \to U$ is Mutable (source-mirror), $U \to I$ is Mutable. The directional-reading asymmetry on $P$–$R$ is genuine; the physical mass ratio derivation for a $P \leftrightarrow R$ crossing at gen-1 must specify whether it uses the $P$-observer reading (Fixed) or the $R$-observer reading (Cardinal) or both. This derivation remains open.
- **Fixed-plane crossings ($P$–$U$, $I$–$R$ topologically):** Under directed reading, $P \to U$ is Cardinal (mirrors $P$), $U \to P$ is Cardinal; $I \to R$ is Fixed, $R \to I$ is Mutable. $P$–$U$ is directionally symmetric (both Cardinal); $I$–$R$ is directionally asymmetric. Two distinct regimes for two edges on the same topological plane.

The regularity `Q15` exhibits — identical readings from both endpoints — is not shared by all inter-rung crossings. `Q15` sits on a topologically Mutable edge that is directionally symmetric (both Fixed) under the rule. Other bimedian-plane crossings fall into two classes: directionally symmetric ($P$–$U$, $U$–$R$, and the $U$-touching edges generally) and directionally asymmetric (all $U$-absent edges). Laurent-analog derivations for the asymmetric class must carry an explicit observer-pole label — matching the pole-naming discipline `L3-TheAtomOfSpace` §VI requires and making it tractable.

## VIII. What Reading This Back Should Leave

Every directed edge in the $K_4$ atom carries a bimedian label that a reader computes in one step: look at the target. If the target is $P$, the label is Cardinal. If it is $I$, Mutable. If it is $R$, Fixed. If it is $U$, mirror the source's character. Four lines. The twelve-entry vertex-relative table falls out directly, the perceiver-relative disagreements on $U$-absent edges are explained rather than tolerated, and the $U$-touching consensus follows from the source-mirror clause by construction.

The directed reading lives alongside DynDist's topological classification and alongside `L4-TheTwelveGates`' sign-modality classification: three distinct uses of the same three words, agreeing on three of the twelve directed arcs and requiring per-level specification everywhere else.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.
````

---

Queued next (final Part I `[READY]` file): `ProofG_Chirality.md` (`WO-310`, `HO-1`). Say "next" to run Round 5.
**Round 4 — `On_TheDirectedReadingRule.md`**

### Audit Status
- `WO-306` (`§VIII` / `Carryover #6`): **READY → patched** (relocated item 3's surface-mesh-tension vertex-coupling specificity into `§VI`, deleted `## VIII. Corpus Housekeeping`, renumbered `§IX` → `§VIII`).
- Standing-pass hygiene: stripped `"this document"` (`Preamble`, `§V`), `"user-observed"` (`§II`), and draft/vote-history narration (`Preamble`, `§I`, `§VI`, `§VII`, `§VIII`). Part V preservation and `Reasonable Reader Alert` footer intact.

````markdown
# On the Directed Reading Rule
## The Target-Based Bimedian Assignment That Resolves the U-Symmetric / U-Absent Split

A directed edge $X \to Y$ of the $K_4$ atom carries a bimedian label — Cardinal, Fixed, or Mutable — determined uniformly by its target $Y$, with one exception forced by $U$ acting as the articulator. The rule reads directly from what $P$, $I$, $U$, and $R$ already are, reproduces the twelve-entry vertex-relative table without adjustment, derives the $U$-symmetric / $U$-absent split of `L3-TheAtomOfSpace` §VI as an immediate consequence, and specifies which bimedian's mesh tension applies at each directed vertex in the forward calculation program.

*Dependencies: `L3-TheAtomOfSpace` §VI (the U-symmetric/U-absent split; pole-naming discipline), `L3-EdgeStateSpace` (four-state directed edges; Bimedian / Sign Discrimination Rule), `L4-DynamicDistortions101` (DynDist bimedian convention, the corpus-wide default), `Q4-OpenExhaust` (P-face as write-destination), `L4-ThePlenum` (the `.behold()` / `.observe()` operations), `L2-Terminology` (pole role assignments).*

---

## I. The Question, Stated Precisely

`L3-TheAtomOfSpace` §VI distinguishes two regimes on $K_4$ edges: every edge admits a bimedian assignment (Cardinal, Fixed, or Mutable), yet on $U$-absent edges ($P$–$I$, $P$–$R$, $I$–$R$) the two endpoints assign the edge differently, whereas on $U$-touching edges ($P$–$U$, $I$–$U$, $U$–$R$) both endpoints agree.

Stated precisely: **given a directed edge $X \to Y$ on the $K_4$ atom, what bimedian label does the reading vertex $X$ assign to it?**

Two ambient facts constrain the answer.

First, every $K_4$ edge, undirected, has a topological bit-flip classification under the DynDist convention: Cardinal (AR-flip, $\{P\text{--}R, I\text{--}U\}$), Fixed (AY-flip, $\{P\text{--}U, I\text{--}R\}$), Mutable (both bits, $\{P\text{--}I, U\text{--}R\}$). This classification is symmetric across the edge; it is a property of the pair, not of either endpoint.

Second, the vertex-relative labels do not match this undirected classification: the labels shift, and on $U$-absent edges the two endpoints disagree. The rule therefore operates at a distinct structural level — a dynamical / observational classification that sits alongside the topological one.

## II. The Rule

**The bimedian label of a directed edge $X \to Y$ is determined by the target $Y$, with one exception: when $Y = U$, the label mirrors the source $X$'s character.**

Explicitly:

| Target $Y$ | Label |
|---|---|
| $Y = P$ | **Cardinal** |
| $Y = I$ | **Mutable** |
| $Y = R$ | **Fixed** |
| $Y = U$ | mirrors source's character: $X=P \to$ Cardinal; $X=I \to$ Mutable; $X=R \to$ Fixed |

That is the entire rule. Every one of the 12 directed edges in the vertex-relative table follows from these four cases.

### Verification against the vertex-relative table

The twelve-entry vertex-relative table:

| From \ To | P | I | U | R |
|---|---|---|---|---|
| **P** | — | Mutable | Cardinal | Fixed |
| **I** | Cardinal | — | Mutable | Fixed |
| **U** | Cardinal | Mutable | — | Fixed |
| **R** | Cardinal | Mutable | Fixed | — |

Match against the rule:

- **Columns TO $P$** ($I \to P$, $U \to P$, $R \to P$): all Cardinal ✓ — rule: $Y=P \to$ Cardinal
- **Columns TO $I$** ($P \to I$, $U \to I$, $R \to I$): all Mutable ✓ — rule: $Y=I \to$ Mutable
- **Column TO $R$** ($P \to R$, $I \to R$, $U \to R$): all Fixed ✓ — rule: $Y=R \to$ Fixed
- **Column TO $U$** ($P \to U$, $I \to U$, $R \to U$): Cardinal, Mutable, Fixed respectively ✓ — rule: $Y=U$ mirrors source's character ($P \to$ Cardinal, $I \to$ Mutable, $R \to$ Fixed)

Exact match across all 12 directed entries. No fit, no adjustment; the rule reads directly.

## III. Why This Rule, Not Another

The rule derives from the corpus's own $P/I/U/R$ role semantics without further postulation.

**$P$ is the write-destination.** Every commit lands in the $P$-ledger; every `.observe()` writes to $P$ (`Q4-OpenExhaust`, `L4-ThePlenum`). When any vertex directs attention toward $P$, it initiates a written act. The Cardinal modality in DynDist's astrological semantics is initiating action across a boundary. Hence "TO $P \to$ Cardinal."

**$I$ is the relational flow / current.** $I$ mediates between poles; it is the connective tissue, the phase-carrier, the both-bits diagonal of $K_4$. The Mutable modality — the diagonal, the both-bits leap — is the mode of relational transit. Hence "TO $I \to$ Mutable."

**$R$ is the grounded resistance / commit.** $R$ is where forces come to rest, where the write from $P$ settles into stable substrate. The Fixed modality — the stabilizing family that holds tier while orientation may pivot — is this ground-attractor character. Hence "TO $R \to$ Fixed."

**$U$ is the articulator.** $U$ is the structural coordinator, the pole whose function is to make explicit what is implicit at the other three. It does not carry a dominant directional character of its own in the way $P$ (initiator), $I$ (flow), and $R$ (ground) do; instead, $U$ articulates whatever is brought to it. When something is directed at $U$, $U$ reflects back the mode the source brings. Hence "TO $U \to$ mirror source's character."

This reads the four poles' semantic functions directly, producing the twelve-entry vertex-relative labels. Grade: assignment, not theorem — the rule fits a table whose $U$-column was constructed under the source-mirror clause, so §IV's consensus on $U$-touching edges is a structural consequence of that construction rather than an independent coincidence.

## IV. Why the U-Symmetric / U-Absent Split Falls Out Immediately

`L3-TheAtomOfSpace` §VI establishes that $U$-touching edges have consensus readings while $U$-absent edges have perceiver-relative readings. Both follow directly from the rule.

**$U$-touching edges ($P$–$U$, $I$–$U$, $U$–$R$): consensus.** Consider $P$–$U$. From $P$'s side, $P \to U$ mirrors $P$'s character $\to$ Cardinal. From $U$'s side, $U \to P$ has target $P \to$ Cardinal. Both readings give Cardinal by construction: the source-mirror clause at $Y=U$ ensures that an edge $X$–$U$ reads identically from both endpoints whenever $X$'s character and $X$'s target-role coincide — which holds for all $X \in \{P, I, R\}$. The same mechanism holds on $I$–$U$ (both Mutable) and $U$–$R$ (both Fixed).

Consensus on $U$-touching edges is a built-in feature of the rule's source-mirror clause, not an emergent coincidence.

**$U$-absent edges ($P$–$I$, $P$–$R$, $I$–$R$): perceiver-relative.** Consider $P$–$I$. From $P$'s side, $P \to I$ has target $I \to$ Mutable. From $I$'s side, $I \to P$ has target $P \to$ Cardinal. Different targets, different labels. The two endpoints legitimately name the edge by different bimedian assignments because they name the target-role of their outgoing arrow, and their outgoing arrows point at different vertices.

The perceiver-relative reading is not observer bias or interpretive slippage. Each endpoint accurately names the semantic role of what its arrow points at. Both readings hold simultaneously; they name distinct phenomenological facts (what each endpoint directs attention toward) rather than one shared property of the undirected edge.

## V. Three Classifications, Not Two

The words *Cardinal*, *Fixed*, and *Mutable* name **three distinct classifications** in the corpus:

1. **DynDist topological (undirected edge bit-flip, from `L3-EdgeStateSpace` §I-b):** Cardinal = AR-flip $\{P\text{--}R, I\text{--}U\}$; Fixed = AY-flip $\{P\text{--}U, I\text{--}R\}$; Mutable = both bits $\{P\text{--}I, U\text{--}R\}$. Property of the pair, independent of direction or observer.
2. **Directed reading (target-based, §II):** target-role ($P \to$ Cardinal, $I \to$ Mutable, $R \to$ Fixed), source-mirror at $Y = U$. Property of the directed arrow.
3. **Sign modality (astrological-register, from `L4-TheTwelveGates` §II):** the twelve zodiacal signs sort as Cardinal / Fixed / Mutable by season position. Property of the sign-gate at an edge.

Any calculation touching a $K_4$ edge must specify which of the three levels it operates at, or it drifts between them silently.

**Directed reading against DynDist topology, agreement on 3 of 12 arcs.** The two classifications agree on the directed 3-cycle **$P \to I \to R \to P$** around the $U$-absent face: $P \to I$ both Mutable, $I \to R$ both Fixed, $R \to P$ both Cardinal. The reverse cycle $P \to R \to I \to P$ (same face, opposite direction) disagrees on all three arcs. Every $U$-touching arrow disagrees under both readings. The $U$-absent / $U$-touching split of §IV holds at this level too: $U$-absent edges carry one agreement arrow each, $U$-touching edges carry none.

**Worked example.** The pion-to-electron Laurent expansion at `Q15-KairosBorn` §I operates on the $U \leftrightarrow R$ inter-rung crossing at generation 1. Under DynDist topological classification, this is a Mutable crossing (both bits flip: $U$ is A-Y, $R$ is R-A). Under the directed reading rule, both $U \to R$ and $R \to U$ are Fixed (target $R$ gives Fixed; target $U$ mirrors source $R$'s grounding character, which is Fixed). Both readings state true facts about distinct aspects of the same crossing. `Q15`'s Laurent decomposition uses the impedance triangle, which is a third orthogonal decomposition — reactive / rotation / resistive dynamical modes of the crossing.

For the Mode/Bimedian naming convention that disambiguates sign-modality (3) from edge-plane (1): `L3-EdgeStateSpace.md` — Bimedian / Sign Discrimination Rule.

## VI. Vertex Couplings and Open Scope

**Vertex Feynman rules (`L3-TheAtomOfSpace` §VII).** Any coupling at a $K_4$ vertex is a directed operation $X \to Y$; the bimedian label of the coupling is its target-role assignment (or source-mirror when $Y = U$), specifying which bimedian's surface mesh tension (`L4-DynamicDistortions301` §IV.D at phase-shear angle $\theta$, via `L3-TheAtomOfSpace` §V) applies at that directed vertex. The coupling strength inherits from that bimedian's impedance geometry per the impedance triangle at `L3-ConstitutiveAlpha` §IV (expect there: the reactive / rotation / resistive modes at Laurent orders $\alpha^{-1}$, $\alpha^{0}$, $\alpha^{+1}$). Each directed vertex operation therefore carries an unambiguous label, a specific bimedian, a specific impedance mode, and a specific mesh-tension geometry.

**Candidate extension.** Whether the target-based structure extends beyond bimedian labeling to govern coupling amplitudes, spectral weights, impedance-triangle coefficients, or the phase-shear angle $\theta$ carried by each vertex's outgoing mesh tensions remains open — flagged as a `CANDIDATE` organizing principle for follow-up rather than an established result.

## VII. What the Rule Says About the Q15 Family

The rule sorts what `Q15`'s Laurent expansion generalizes to.

`Q15` is the $U \leftrightarrow R$ inter-rung crossing at gen-1. Under DynDist topology, this is Mutable. Under the directed reading rule, both directions are Fixed. Under the impedance triangle, the three Laurent terms are reactive / rotation / resistive.

Analog inter-rung crossings at gen-1 that engage the other topological bimedians:

- **Cardinal-plane crossings ($P$–$R$, $I$–$U$ topologically):** Under directed reading, $P \to R$ is Fixed, $R \to P$ is Cardinal; $I \to U$ is Mutable (source-mirror), $U \to I$ is Mutable. The directional-reading asymmetry on $P$–$R$ is genuine; the physical mass ratio derivation for a $P \leftrightarrow R$ crossing at gen-1 must specify whether it uses the $P$-observer reading (Fixed) or the $R$-observer reading (Cardinal) or both. This derivation remains open.
- **Fixed-plane crossings ($P$–$U$, $I$–$R$ topologically):** Under directed reading, $P \to U$ is Cardinal (mirrors $P$), $U \to P$ is Cardinal; $I \to R$ is Fixed, $R \to I$ is Mutable. $P$–$U$ is directionally symmetric (both Cardinal); $I$–$R$ is directionally asymmetric. Two distinct regimes for two edges on the same topological plane.

The regularity `Q15` exhibits — identical readings from both endpoints — is not shared by all inter-rung crossings. `Q15` sits on a topologically Mutable edge that is directionally symmetric (both Fixed) under the rule. Other bimedian-plane crossings fall into two classes: directionally symmetric ($P$–$U$, $U$–$R$, and the $U$-touching edges generally) and directionally asymmetric (all $U$-absent edges). Laurent-analog derivations for the asymmetric class must carry an explicit observer-pole label — matching the pole-naming discipline `L3-TheAtomOfSpace` §VI requires and making it tractable.

## VIII. What Reading This Back Should Leave

Every directed edge in the $K_4$ atom carries a bimedian label that a reader computes in one step: look at the target. If the target is $P$, the label is Cardinal. If it is $I$, Mutable. If it is $R$, Fixed. If it is $U$, mirror the source's character. Four lines. The twelve-entry vertex-relative table falls out directly, the perceiver-relative disagreements on $U$-absent edges are explained rather than tolerated, and the $U$-touching consensus follows from the source-mirror clause by construction.

The directed reading lives alongside DynDist's topological classification and alongside `L4-TheTwelveGates`' sign-modality classification: three distinct uses of the same three words, agreeing on three of the twelve directed arcs and requiring per-level specification everywhere else.

---

**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.


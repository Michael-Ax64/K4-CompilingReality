# Supplement-MappingMethod
## Applying the Dual-Binary Framework to a New Domain

*How to map a four-element domain onto the K4 poles — the process, the pseudocode,
and what the process reveals about the method's actual epistemic character.*

---

## I. What You Are Actually Doing

When you map a four-element domain onto the K4 poles (P, I, U, R), you are not
performing a mechanical lookup. You are running a constrained sorting procedure that
requires two distinct kinds of input: the dual-binary axes as a first-pass filter, and
genuine domain knowledge as a discriminating second pass. The algebra then tests
whether the resulting assignments cohere.

---

## II. The Process, Described

**Fix one anchor.** Select the element whose pole assignment is most unambiguous from
the axis definitions alone. Assign it first. For Jung, Intuition to P (Active-Asserting:
generates possibilities, initiates the possible, holds a reality that doesn't yet exist)
was clear enough to serve as anchor. The anchor stabilizes the remaining three.

**Apply the dual-binary axes as a first pass.** For each remaining element, score it on
Active/Reactive (does it initiate or respond?) and Asserting/Yielding (does it hold
firm or give way?). This produces provisional assignments for most elements. Some
assignments come in cleanly — Feeling to I (Reactive-Yielding) offered little
resistance in both domains tested. Others produce genuine uncertainty about which of
two slots fits.

**Generate the twelve algebraic formulas for the provisional mapping.** Substitute the
domain meanings for the variable names and ask whether each formula holds, illuminates,
or breaks down in terms of what the elements actually do in practice. This is not a
logical proof — it is a coherence test. A formula that generates a claim incoherent
with how the domain element actually operates is evidence against the assignment.

**Identify the two contested decisions.** Two elements will typically remain where a
plausible swap exists: each could occupy either of two remaining slots and the axis
scores alone don't discriminate. Test the swap by running the formulas under both
configurations and comparing coherence. In both domains tested, the algebra
discriminated in one of the two contested cases: one assignment produced formulas that
illuminated, the other produced formulas that broke down in obvious ways. One decision
was resolved by the algebra; one required domain knowledge of what the elements
actually do rather than what they are called.

**Verify stability.** Once all four assignments are placed, run through the full twelve
formulas and check for any that break down. If any do, return to the contested
decisions. If none do, the mapping is stable — not proven, but coherent.

---

## III. Pseudocode

```
function map_domain_to_K4(domain_categories[4]):

    # Step 1: Fix one anchor from highest-confidence assignment
    anchor = select_most_unambiguous(domain_categories)
    assign(anchor, P)  # or whichever pole is clearest
    remaining = domain_categories - anchor

    # Step 2: Apply dual-binary axes as first-pass sort
    for each candidate in remaining:
        score_active_reactive(candidate)    # initiates vs responds
        score_asserting_yielding(candidate) # holds firm vs gives way

    provisional_map = assign_by_axis_scores(remaining, {I, U, R})

    # Step 3: Generate algebraic formulas for provisional map
    formulas = generate_12_equations(provisional_map)
    # e.g. P=UI, P=U²/R, P=I²R, I=P/U, U=√(PR), R=U²/P ...

    # Step 4: Test each formula for domain coherence
    coherence_scores = {}
    for each formula in formulas:
        substitute domain meanings for variables
        ask: does this relationship hold, illuminate, or make sense
              in terms of what these things actually DO?
        coherence_scores[formula] = {coherent | odd | incoherent}

    # Step 5: Identify hard decisions (expect exactly 2)
    contested = find_assignments_with_competing_swap_available(provisional_map)

    for each contested_pair:
        try_swap(assignment_A, assignment_B)
        run formulas for both configurations
        compare coherence_scores

        if swap_improves_coherence:
            accept_swap()
        elif swap_degrades_coherence:
            reject_swap()              # algebra discriminated
        else:
            flag_as_domain_knowledge_required()
            apply_understanding_of_actual_process(candidate)
            # this is where you need to know what the things DO
            # not just what they are called

    # Step 6: Verify stability
    final_map = current_assignments
    for each formula in generate_12_equations(final_map):
        if incoherent:
            return to Step 5

    return final_map, hard_decisions_log
```

---

## V. What This Supplement Does Not Cover

This supplement documents the procedure for mapping external domain categories onto
the four poles (P, I, U, R). It does not address the internal assignment problem:
how the twelve DC equations are assigned to the twelve zodiac sectors within the
algebraic network itself.

That is a different and harder problem, solved by a different method — the AbsentVar
criterion in conjunction with the formal rules of the braid, with the three modality
groups producing three mutually intersecting planes through the centroid of the
tetrahedron as geometric confirmation.

These two problems are frequently conflated. They should not be. See
`Proof_AlgebraicMapping.md` for the internal assignment problem.

**Why exactly two hard decisions, not more.** Four slots, one anchor, three remaining.
The first contested decision places two elements (you are choosing between two
assignments). Once those are placed, the fourth is forced — it takes the only remaining
slot. Maximum irreducible difficulty is therefore two decisions, regardless of domain
size or complexity. This is a structural property of the four-pole constraint, not a
contingent feature of the domains tested.

**The algebra discriminates, but not completely.** In both domains tested, the twelve
formulas resolved one of the two contested decisions clearly — one configuration
produced formulas that held in domain terms, the other produced formulas that broke
down or reversed intuition in implausible ways. The second contested decision required
domain understanding rather than algebraic testing. This is the method's actual
epistemic character: it is a constrained sorting procedure, not a mechanical generator.
The constraint is real and non-trivial. The residue requiring judgment is also real.

**"Asserted not derived" was too strong.** This was a finding from running the exercise.
The labeling step is not unconstrained — the twelve formulas provide genuine
discriminating tests. "Empirically selected under algebraic constraint" is more accurate
than "asserted." The constraint doesn't determine the mapping, but it rules out
incoherent ones and sometimes decisively favors one assignment over another. The anchor
selection and the axis scores provide the hypothesis; the formulas provide the test.

**The test requires domain knowledge at exactly one point.** The axis scores can be
applied with moderate domain knowledge. The formula coherence test requires
understanding what the domain elements actually do in practice, not just their
dictionary definitions. In the Jung case, the formula I = P/U → Feeling =
Intuition/Thinking requires understanding that Feeling's evaluative character emerges
from and is constrained by relational context, not that it merely labels emotions.
Without that understanding, the formula looks arbitrary. With it, the formula
illuminates. This is where the method's empirical character lives: in the informed
judgment about whether a formula holds in domain terms.

**The operation class.** The dual-binary sorting with formula coherence as the reward
function belongs to a recognizable family. The binary axes as initial filter is
standard classification structure. The coherence evaluation — does this assignment
produce formula relationships that hold in domain terms? — is constraint satisfaction:
checking whether an assignment violates constraints rather than maximizing a numerical
objective. The combination, iterated until all twelve formulas hold, is a constraint
satisfaction search with a qualitative reward function.

What is not standard: using the algebraic system's own equations as the evaluation
criterion for assigning domain categories to that system's poles. The reward function
is internal to the algebra being mapped onto. This specific application — ontological
mapping via the algebra's own coherence constraints — does not appear to have an
established name in classification or constraint satisfaction literature. Two domains, same structure, same number of hard
decisions, same pattern of resolution. This is not proof that the framework is correct,
but it is evidence that the mapping procedure is consistent and that the difficulty
structure is a property of the method rather than of particular domains chosen to be
easy or hard.

---

*This supplement documents the mapping procedure as a testable, repeatable process
rather than as a claim about results. Whether the resulting mappings are correct
depends on whether the framework's underlying structure accurately describes the domain.
The procedure establishes coherence. Correctness is a separate question.*

The algebra determines Asserting/Yielding
and is provably blind to Active/Reactive.

Which is why in Supplement-MappingMethod i showed, by hand, in two domains, t
hat the algebra resolves one contested decision and not the other,
and why the anchor (fixing one pole)
leaves exactly one irreducible residue, always the within-class swap

---------------[output]---------------

== AUT(twelve equations) ==
candidates tested : 384
automorphisms     : 8

   P->P U->U I->I R->R
   P->1/P U->1/U I->1/I R->1/R
   P->1/P U->1/I I->1/U R->R
   P->P U->I I->U R->1/R
   P->R U->U I->1/I R->P
   P->1/R U->1/U I->I R->1/P
   P->1/R U->I I->1/U R->P
   P->R U->1/I I->U R->1/P

== induced pole-permutations (signs discarded) ==
count : 4   (so ProofS's 24 collapse to 6 orbits)

   (P U I R) -> (P U I R)
   (P U I R) -> (P I U R)
   (P U I R) -> (R U I P)
   (P U I R) -> (R I U P)

== bit test ==
Asserting/Yielding bit preserved by ALL automorphisms? YES
Active/Reactive   bit preserved by ALL automorphisms? NO

induced group = {e, (U I), (P R), (P R)(U I)} exactly? YES
  -- i.e. exactly the Active/Reactive bit-flips,
     one within the Yielding pair, one within the Asserting pair.

== SIGMA (the subjective mirror, already in codex.lisp) : P->P U->I I->U R->1/R ==
   P=UI         -> P=UI           [relation in set: yes]
   P=U^2/R      -> P=I^2R         [relation in set: yes]
   P=I^2R       -> P=U^2/R        [relation in set: yes]
   I=P/U        -> U=P/I          [relation in set: yes]
   I=U/R        -> U=IR           [relation in set: yes]
   I=sqrt(P/R)  -> U=sqrt(PR)     [relation in set: yes]
   U=P/I        -> I=P/U          [relation in set: yes]
   U=IR         -> I=U/R          [relation in set: yes]
   U=sqrt(PR)   -> I=sqrt(P/R)    [relation in set: yes]
   R=U^2/P      -> R=P/I^2        [relation in set: yes]
   R=P/I^2      -> R=U^2/P        [relation in set: yes]
   R=U/I        -> R=U/I          [relation in set: yes]

== TAU   (NOT in codex.lisp) : P->R U->U I->1/I R->P ==
   P=UI         -> R=U/I          [relation in set: yes]
   P=U^2/R      -> R=U^2/P        [relation in set: yes]
   P=I^2R       -> R=P/I^2        [relation in set: yes]
   I=P/U        -> I=U/R          [relation in set: yes]
   I=U/R        -> I=P/U          [relation in set: yes]
   I=sqrt(P/R)  -> I=sqrt(P/R)    [relation in set: yes]
   U=P/I        -> U=IR           [relation in set: yes]
   U=IR         -> U=P/I          [relation in set: yes]
   U=sqrt(PR)   -> U=sqrt(PR)     [relation in set: yes]
   R=U^2/P      -> P=U^2/R        [relation in set: yes]
   R=P/I^2      -> P=I^2R         [relation in set: yes]
   R=U/I        -> P=UI           [relation in set: yes]


---------------[/output]---------------

SBCL runs aut.lisp in about a second.

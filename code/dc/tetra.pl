% tetra.pl -- the same structure derived on an INDEPENDENT SUBSTRATE.
% No shared code with the Lisp rendering. Same raw definitions in, same
% canonical lines out -- or not. The diff is the substrate edge.

charge(p,1,1).  % Active+Asserting
charge(i,0,0).  % Reactive+Yielding
charge(u,1,0).  % Active+Yielding
charge(r,0,1).  % Reactive+Asserting

ttype(A,B,T) :-
    charge(A,X1,Y1), charge(B,X2,Y2),
    (  X1 =\= X2, Y1 =\= Y2 -> T = 'DIAGONAL-BOTH'
    ;  X1 =\= X2            -> T = 'FLIP-AR'
    ;                          T = 'FLIP-AY' ).

% the twelve equations as (Home, Absent)
eqn(p,r). eqn(p,i). eqn(p,u).
eqn(i,r). eqn(i,p). eqn(i,u).
eqn(u,r). eqn(u,p). eqn(u,i).
eqn(r,i). eqn(r,u). eqn(r,p).

canon_line(S) :-
    eqn(H,A), ttype(H,A,T),
    upcase_atom(H,HU), upcase_atom(A,AU),
    format(atom(S), "~w ~w ~w", [HU,AU,T]).

main :-
    U = 12.0, I = 2.0,
    R is U / I,          % derivable only by a perspective blind to P
    P is U * I,          % derivable only by a perspective blind to R
    findall(S, canon_line(S), Ls0), msort(Ls0, Ls),
    open('/home/codex/prolog-canon.txt', write, Str),
    forall(member(L, Ls), format(Str, "~w~n", [L])),
    format(Str, "STATE-P ~1f~n", [P]),
    format(Str, "STATE-R ~1f~n", [R]),
    close(Str).

:- initialization((main, halt)).


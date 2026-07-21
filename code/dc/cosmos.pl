% ===================================================================
% cosmos.pl    THE RELATIONAL SPINE
% The DC four-fold network as a NATIVE RELATION.
% Claim R1-R7 ("any two variables determine the other two") is not
% asserted here; it is RUN. Query dc/4 with any two bound, get the rest.
% The AbsentVar is a logic variable. Undecidability is a goal that is
% not proven false -- it is returned as an OPEN INTERFACE.
% ===================================================================

:- use_module(library(clpr)).      % constraints over the reals: the relation runs in every direction

% -- The closed algebra. Four variables, mutually determining. --------
% P = U*I ,  U = I*R  (=> P = I^2 R,  P = U^2/R). No addition. No external constant.
    
dc(P,U,I,R) :-
    { P = U * I },
    { U = I * R }.

% Solve from any pair. We keep it explicit so the "any two determine the
% rest" claim is legible as EXECUTION, not faith.
    
solve(u-U, i-I, P, R) :- P is U*I, ( I =:= 0 -> R = boundary ; R is U/I ).
solve(u-U, r-R, P, I) :- ( R =:= 0 -> I = boundary, P = boundary ; I is U/R, P is U*I ).
solve(i-I, r-R, P, U) :- U is I*R, P is I*I*R.
solve(p-P, r-R, U, I) :- ( R =:= 0 -> U = boundary, I = boundary
                         ; U is sqrt(P*R), I is sqrt(P/R) ).
solve(p-P, i-I, U, R) :- ( I =:= 0 -> U = boundary, R = boundary
                         ; U is P/I, R is P/(I*I) ).
solve(u-U, p-P, I, R) :- ( U =:= 0 -> I = boundary, R = boundary
                         ; I is P/U, R is (U*U)/P ).

% -- The AbsentVar: what is HELD, not solved. -------------------------
% To .behold() the algebra is to leave one variable unbound as live context.
% Prolog does this natively: an unbound variable is a carried absence.
    
beholding(P,U,I,R, Absent) :-
    term_variables([P,U,I,R], Vs),
    ( Vs = [] -> Absent = none            % fully .observe()d: 0-DoF crystal
    ; Absent = held(Vs) ).                % live interior: DoF remain

% -- Undecidability as interface, not as falsehood. -------------------
% The Tangent Singularity: a coordinate that diverges. We do not fail;
% we return the interface the divergence opens.
    
interface(tangent_singularity, "coordinate diverges at 90deg; orthogonal turn available").
interface(absent_var,          "belonging relation held unmanifest; interior volume preserved").
interface(propositional_debt,  "cross-domain mapping asserted, not derived; Landauer tax unpaid").

% A boundary is reached, and REPORTED, rather than swallowed.
report_boundary(Kind) :- interface(Kind, Msg), format("  [INTERFACE ~w] ~w~n", [Kind, Msg]).

% ===================================================================
% DEMONSTRATION
% ===================================================================
demo :-
    format("~n== RELATIONAL SPINE (Prolog) ==~n"),
    format("Same relation, run in four different directions:~n"),

    solve(u-12.0, i-2.0, P1, R1),
    format("  given U=12, I=2   -> P=~w  R=~w   [COMPUTED]~n", [P1, R1]),

    solve(p-100.0, r-4.0, U2, I2),
    format("  given P=100, R=4  -> U=~w  I=~w   [COMPUTED]~n", [U2, I2]),

    solve(i-3.0, r-5.0, P3, U3),
    format("  given I=3, R=5    -> P=~w  U=~w   [COMPUTED]~n", [P3, U3]),

    format("~nThe boundary is not an error. It is an interface:~n"),
    solve(u-12.0, i-0.0, P4, R4),
    format("  given U=12, I=0   -> P=~w  R=~w~n", [P4, R4]),
    report_boundary(tangent_singularity),

    format("~nThe AbsentVar (what the algebra HOLDS rather than solves):~n"),
    beholding(_P, 12.0, 2.0, _R, A1),
    format("  behold(U=12,I=2, P?,R?) -> ~w   [interior has DoF]~n", [A1]),
    beholding(24.0, 12.0, 2.0, 12.0, A2),
    format("  observe(all four bound) -> ~w    [0-DoF crystal]~n", [A2]),
    report_boundary(absent_var),
    format("~nSpine holds. Relation total where total; interfaced where open.~n").

:- initialization((demo, halt)).

    

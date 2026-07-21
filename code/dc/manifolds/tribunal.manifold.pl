% =====================================================================
% cosmos.tribunal.pl
% The K4 Topological Question Generator & Diagnostic Engine
%
% STATUS: CORE COMPILED
% 
% This engine merges the rigorous thermodynamic constraints of the 
% DC algebra (Dimensionless Drift, Operator Syntax) with the generative 
% depth of the Triadic Tribunals. It proves that the math auto-classifies 
% the psychological, institutional, and relational reality.
% =====================================================================

:- use_module(library(clpr)).

% ---------------------------------------------------------
% 1. THE THERMODYNAMIC BASE (The K4 Volume)
% ---------------------------------------------------------
% The 12 equations held in complete mutual determination. This clpr relation is
% the CANONICAL DECLARATIVE STATEMENT of the algebra. It is not used to solve the
% runtime audit: clpr's nonlinear store cannot close every two-variable pair and
% is epsilon-brittle, whereas the diagnosis wants the HEURISTIC (topological
% shear), not machine-precise values. Runtime solving is done by solve_state/8.
k4_volume(P, I, U, R) :-
    { P > 0, I > 0, U > 0, R > 0 }, 
    { P = U * I },                  
    { P = I * I * R },              
    { P * R = U * U },              
    { U = I * R }.                  

% ---------------------------------------------------------
% 1b. DETERMINISTIC CURRENT-STATE SOLVER
% ---------------------------------------------------------
% k4_volume states the full closed algebra (the "12 equations") via clpr and is
% the canonical reference relation. For *solving* the current state from partial
% telemetry, clpr's nonlinear store cannot close every two-variable pair (it
% silently fails on the Flow+Structure pair (I,U) via a floating-point residual
% on the redundant P*R=U^2 constraint). We therefore saturate the four poles
% deterministically from any two knowns, which is exact for all six pairs.
% Inputs are numbers or the anonymous var '_'; unknowns arrive as unbound vars.

solve_state(P0, I0, U0, R0, P, I, U, R) :-
    norm_in(P0, P1), norm_in(I0, I1), norm_in(U0, U1), norm_in(R0, R1),
    saturate(P1, I1, U1, R1, P, I, U, R).

norm_in(X, Y) :- ( var(X) -> Y = _ ; X == '_' -> Y = _ ; Y = X ).

saturate(P, I, U, R, P, I, U, R) :-
    number(P), number(I), number(U), number(R), !.
saturate(P0, I0, U0, R0, P, I, U, R) :-
    derive_one(P0, I0, U0, R0, P1, I1, U1, R1),
    saturate(P1, I1, U1, R1, P, I, U, R).

% Fill exactly one unknown pole from two known neighbours (the 12 relations).
derive_one(P,I,U,R, P2,I,U,R) :- var(P), number(U), number(I), !, P2 is U*I.
derive_one(P,I,U,R, P,I,U2,R) :- var(U), number(I), number(R), !, U2 is I*R.
derive_one(P,I,U,R, P,I2,U,R) :- var(I), number(U), number(R), !, I2 is U/R.
derive_one(P,I,U,R, P,I,U,R2) :- var(R), number(U), number(I), !, R2 is U/I.
derive_one(P,I,U,R, P,I2,U,R) :- var(I), number(P), number(U), !, I2 is P/U.
derive_one(P,I,U,R, P,I,U2,R) :- var(U), number(P), number(I), !, U2 is P/I.
derive_one(P,I,U,R, P2,I,U,R) :- var(P), number(U), number(R), !, P2 is U*U/R.
derive_one(P,I,U,R, P,I,U,R2) :- var(R), number(U), number(P), !, R2 is U*U/P.
derive_one(P,I,U,R, P2,I,U,R) :- var(P), number(I), number(R), !, P2 is I*I*R.
derive_one(P,I,U,R, P,I,U,R2) :- var(R), number(P), number(I), !, R2 is P/(I*I).
derive_one(P,I,U,R, P,I,U2,R) :- var(U), number(P), number(R), !, U2 is sqrt(P*R).
derive_one(P,I,U,R, P,I2,U,R) :- var(I), number(P), number(R), !, I2 is sqrt(P/R).

% ---------------------------------------------------------
% 2. THE TOPOLOGICAL DICTIONARY: THE TRIBUNALS
% ---------------------------------------------------------
% Format: tribunal(AbsentVar, FaceName, ThermodynamicReality, Voice1, Voice2, Voice3, CentralInquiry).
% Grammatical Rule: The AbsentVar NEVER appears in the equations of its Face.

% --- THE UN-GROUNDED FACE (R-Absent) ---
% Operators: Purely Linear. Frictionless K3 Boundary.
tribunal(r, 'The Un-Grounded Face (Air/Water/Fire)',
    'Frictionless Boundary (Linear K3). No Landauer Tax paid.',
    voice('Synthesis (P = U * I)', 
        "I am generating output effortlessly. I am the linear product of the blueprint (U) and the relational current (I)."),
    voice('Tension (U = P / I)', 
        "I am the ratio of your Drive (P) to our Flow (I). I hold the architecture, but I lack weight."),
    voice('Extraction (I = P / U)', 
        "I am the flow squeezed from your Drive (P) through your Framework (U)."),
    "You are soaring on the K3 surface. The math is linear and frictionless. But the AbsentVar is Earth (R). Where is the material constraint? Who is paying the Landauer Tax? Without an .observe() collapse to ground this, your system will evaporate as pure, unanchored Theatre."
).

% --- THE UN-DRIVEN FACE (P-Absent) ---
% Operators: Purely Linear. Closed-loop mechanics.
tribunal(p, 'The Un-Driven Face (Earth/Water/Air)',
    'Frictionless Boundary (Linear K3). Closed-loop mechanics.',
    voice('Architecture (U = I * R)', 
        "The system is perfectly built. My frameworks are the exact, natural product of the current flow (I) and the material ground (R)."),
    voice('Throughput (I = U / R)', 
        "I am moving steadily. The structure (U) guides me cleanly through the physical constraints (R)."),
    voice('Impedance (R = U / I)', 
        "I am the ratio of structure to flow. When rules outpace the current, I manifest as bureaucratic drag."),
    "You have built the perfect machine, but the AbsentVar is Fire (P). Why does this machine exist? You are managing a closed-loop system, but the originary spark has been Garbage Collected. Are you sustaining an institution just to sustain it?"
).

% --- THE BETRAYER FACE (I-Absent) ---
% Operators: Exponential. High violence, burning phase to manufacture mass.
tribunal(i, 'The Betrayer Face (Earth/Air/Fire)',
    'Thermodynamic Furnace (Exponential K4). High violence, burning phase.',
    voice('Leverage (P = U^2 / R)', 
        "I am scaling exponentially. I am compounding our structure (U^2) against the physical ground (R) to generate world-eating Power (P)."),
    voice('Bloat (R = U^2 / P)', 
        "You fool. I am the exact same variables, inverted. You aren't generating power; you are crushing the life out of your Drive (P) under a squared mountain of Red Tape (U^2)."),
    voice('Capacity (U = sqrt(P * R))', 
        "I am the root route. I am the only thing keeping you two from snapping. I am projecting the heavy scalars of Drive and Ground back out into a structural vector."),
    "You are running squared routes, playing god with scale. But the AbsentVar is Water (I). You have severed the relational current. There is no empathy, no feedback loop. Is your brilliant architectural map (U) currently eating its own territory (R)?"
).

% --- THE GRINDING FACE (U-Absent) ---
% Operators: Exponential. Massive metabolic cost, raw effort.
tribunal(u, 'The Grinding Face (Earth/Water/Fire)',
    'Thermodynamic Furnace (Exponential K4). Massive metabolic cost.',
    voice('Momentum (P = I^2 * R)', 
        "We are getting it done. I am actualizing reality by forcing massive, squared effort (I^2) through the raw dirt of material resistance (R). It costs blood, but it works."),
    voice('Brittleness (R = P / I^2)', 
        "I am cracking. You are demanding massive output (P), but because the flow (I^2) is erratic, my material limits are pushed to the breaking point. I am hollow."),
    voice('Yield (I = sqrt(P / R))', 
        "I am the raw geometric extraction. I am bleeding the heat of this engine so it doesn't melt down."),
    "You are sweating, burning, and grinding. You are paying maximum Landauer Tax. But the AbsentVar is Air (U). You have no map. You are relying entirely on brute force (P) and sweat (I). Without a framework (U), this system will shatter from pure exhaustion."
).

% ---------------------------------------------------------
% 3. THE SEVERED BIMEDIANS (The Broken Braid)
% ---------------------------------------------------------
% Identifies exactly which phase transitions the system is failing to execute.
severed(p, ['P->U (Cardinal: Exteriorization)', 'P->R (Fixed: GravityStrong/Ledger)', 'P->I (Mutable: SourceVoid)']).
severed(i, ['I->R (Cardinal: Crystallization)', 'I->U (Fixed: ElectroWeak/Relational)', 'P->I (Mutable: SourceVoid)']).
severed(u, ['P->U (Cardinal: Exteriorization)', 'I->U (Fixed: ElectroWeak/Relational)', 'U->R (Mutable: ChromoLux/The Law)']).
severed(r, ['I->R (Cardinal: Crystallization)', 'P->R (Fixed: GravityStrong/Ledger)', 'U->R (Mutable: ChromoLux/The Law)']).

% ---------------------------------------------------------
% 4. CROSS-EXAMINATION (The Complements)
% ---------------------------------------------------------
% Dynamically mapping the dominant Vortex Equation to its inverse shadow.
vortex_equation(p, r, 'Synthesis (P = U * I)').
vortex_equation(p, i, 'Leverage (P = U^2 / R)').
vortex_equation(p, u, 'Momentum (P = I^2 * R)').
vortex_equation(r, p, 'Impedance (R = U / I)').
vortex_equation(r, i, 'Bloat (R = U^2 / P)').
vortex_equation(r, u, 'Brittleness (R = P / I^2)').
vortex_equation(u, r, 'Tension (U = P / I)').
vortex_equation(u, p, 'Architecture (U = I * R)').
vortex_equation(u, i, 'Capacity (U = sqrt(P * R))').
vortex_equation(i, r, 'Extraction (I = P / U)').
vortex_equation(i, p, 'Throughput (I = U / R)').
vortex_equation(i, u, 'Yield (I = sqrt(P / R))').

complement('Leverage (P = U^2 / R)', 'Bloat (R = U^2 / P)', "Are you sure your structure isn't just crushing your drive to create more red tape?").
complement('Synthesis (P = U * I)', 'Impedance (R = U / I)', "You think you are generating endless light, but I am the cost of the wire. You cannot synthesize forever without grounding.").
complement('Momentum (P = I^2 * R)', 'Brittleness (R = P / I^2)', "You are forcing current through the dirt, but if the flow stutters, the ground turns hollow and shatters.").
complement('Architecture (U = I * R)', 'Throughput (I = U / R)', "If the rules outpace the flow, you aren't building a house, you're building a dam.").

get_complement_chat(VortexEq, InverseEq, Chat) :- complement(VortexEq, InverseEq, Chat).
get_complement_chat(VortexEq, InverseEq, Chat) :- complement(InverseEq, VortexEq, Chat).

% ---------------------------------------------------------
% 5. THE EVALUATOR ENGINE
% ---------------------------------------------------------
% Usage: cli_run(BaseP, BaseI, BaseU, BaseR, CurP, CurI, CurU, CurR).
% Accepts a biological/organic baseline and compares the current state
% via Dimensionless Drift, completely avoiding unit category errors.

cli_run(B_P, B_I, B_U, B_R, InP, InI, InU, InR) :-
    % 1. Resolve Baseline and Current State deterministically.
    %    We take the HEURISTIC, not clpr's exact-value solve: the diagnosis is
    %    about topological shear (which pole starves, which face convenes), so we
    %    stay deliberately loose about floating-point epsilon from the start.
    ( solve_state(B_P, B_I, B_U, B_R, BP, BI, BU, BR) -> true
    ; format("[ENGINE] Under-determined baseline: supply at least two of P,I,U,R.~n"), halt(1) ),
    ( solve_state(InP, InI, InU, InR, CP, CI, CU, CR) -> true
    ; format("[ENGINE] Under-determined telemetry: supply at least two of P,I,U,R.~n"), halt(1) ),

    % 2. Dimensionless Drift (plain arithmetic; no constraint store).
    DriftP is CP / BP,
    DriftI is CI / BI,
    DriftU is CU / BU,
    DriftR is CR / BR,

    format("~n======================================================~n"),
    format("K4 TOPOLOGICAL AUDIT & GENERATIVE TRIBUNAL~n"),
    format("======================================================~n"),
    format("COMPILED LEDGER (Thermodynamic Drift vs Baseline):~n"),
    format("  Drive (P):      ~8f -> ~8f (Drift: ~4fx)~n", [BP, CP, DriftP]),
    format("  Structure (U):  ~8f -> ~8f (Drift: ~4fx)~n", [BU, CU, DriftU]),
    format("  Flow (I):       ~8f -> ~8f (Drift: ~4fx)~n", [BI, CI, DriftI]),
    format("  Ground (R):     ~8f -> ~8f (Drift: ~4fx)~n", [BR, CR, DriftR]),
    format("------------------------------------------------------~n"),

    % 3. Route Output. CRYSTAL_EPS is a deliberately loose heuristic band:
    %    "all drifts are essentially 1.0x" -> the 0-DoF locked state.
    ( ( abs(DriftP - 1.0) < 0.001, abs(DriftI - 1.0) < 0.001,
        abs(DriftU - 1.0) < 0.001, abs(DriftR - 1.0) < 0.001 ) ->
        print_crystal
    ;
        print_tribunal(DriftP, DriftI, DriftU, DriftR)
    ),
    format("======================================================~n"),
    halt.
cli_run(_,_,_,_,_,_,_,_) :-
    format("[ENGINE] Could not resolve a valid K4 audit from the given inputs.~n"),
    halt(1).

% ---------------------------------------------------------
% 6. THE LIMIT STATES
% ---------------------------------------------------------
print_crystal :-
    format("[ THE 0-DoF CRYSTAL LIMIT DETECTED ]~n"),
    format("All dimensionless gradients are 1.0x. System is locked to its native baseline.~n"),
    format("The possibility space is fully exhausted. The Landauer Tax is settled.~n"),
    format("No AbsentVar exists. No interference structure remains.~n~n"),
    format("The space is simply: THE READ-ONLY LEDGER.~n"),
    format("-> (.observe) The multiway graph is fully collapsed. You are a stone.~n").

% extract_eq(+VoiceName, -Equation)
% Pulls the algebraic equation out of a voice label of the form
% 'Leverage (P = U^2 / R)' -> 'P = U^2 / R'. Keeps inner parens (sqrt(...)),
% drops only the single trailing ')'. Single source of truth: the tribunal voices.
extract_eq(VoiceName, Eq) :-
    atom_length(VoiceName, L),
    sub_atom(VoiceName, B, 1, _, '('), !,   % first '('
    Start is B + 1,
    Len   is L - Start - 1,                 % drop the final ')'
    sub_atom(VoiceName, Start, Len, _, Eq).

print_tribunal(DP, DI, DU, DR) :-
    % Sort by Drift to isolate the True Vortex (Max) and AbsentVar (Min)
    Pairs = [DP-p, DI-i, DU-u, DR-r],
    sort(Pairs, [MinVal-AbsentVar, _, _, MaxVal-Vortex]),
    
    format("[ TOPOLOGICAL SHEAR DETECTED ]~n"),
    format("Dominant Pole (The Vortex): ~w (~2fx baseline capacity)~n", [Vortex, MaxVal]),
    format("Starved Pole (The AbsentVar): ~w (~2fx baseline capacity)~n~n", [AbsentVar, MinVal]),
    
    % Fetch the Tribunal
    tribunal(AbsentVar, FaceName, ThermoReality, voice(N1, V1), voice(N2, V2), voice(N3, V3), CentralInquiry),
    
    format(">>> CONVENING THE TRIBUNAL: ~w <<<~n", [FaceName]),
    format("Thermodynamic Reality: ~w~n", [ThermoReality]),
    format("------------------------------------------------------~n"),
    format("THE INTERNAL DEBATE (The Equations Speak):~n~n"),
    format("  ~w:~n  \"~w\"~n~n", [N1, V1]),
    format("  ~w:~n  \"~w\"~n~n", [N2, V2]),
    format("  ~w:~n  \"~w\"~n", [N3, V3]),
    
    % Cross-Examination
    vortex_equation(Vortex, AbsentVar, VortexEq),
    format("------------------------------------------------------~n"),
    format("THE CROSS-EXAMINATION:~n"),
    format("You entered this face driven by: ~w~n", [VortexEq]),
    (get_complement_chat(VortexEq, InverseEq, ChatText) ->
        format("The Voice of ~w answers:~n", [InverseEq]),
        format("  \"~w\"~n", [ChatText])
    ;
        format("Your dominant equation runs unchecked. No direct inverse chat mapped.~n")
    ),

    % Severed Edges
    format("------------------------------------------------------~n"),
    format("SEVERED BIMEDIANS (The Broken Braid):~n"),
    format("By starving [~w], you are structurally incapable of executing:~n", [AbsentVar]),
    severed(AbsentVar, DeadEdges),
    forall(member(E, DeadEdges), format("  - ~w~n", [E])),
    
    format("------------------------------------------------------~n"),
    format("THE CENTRAL INQUIRY (The Diagnosis):~n"),
    format("~w~n", [CentralInquiry]),

    % Machine-readable handoff for the AST Semantic Bridge.
    % Deterministic block; the orchestrator parses FACE:/EQ: lines, never the voices.
    extract_eq(N1, E1), extract_eq(N2, E2), extract_eq(N3, E3),
    format("~n[MACHINE]~n"),
    format("FACE: ~w~n", [FaceName]),
    format("EQ: ~w~n", [E1]),
    format("EQ: ~w~n", [E2]),
    format("EQ: ~w~n", [E3]),
    format("[/MACHINE]~n").


#!/usr/bin/env python3
"""
Orientation-Grammar Checker — DC (12 eq) and AC (49 eq) survival trace.

Implements the decision procedure claimed decidable in the corrected Proof Q claim:
given the dual-binary seed, classify every equation's operator structure and check:

  LAW 1 (Numerator Law):  no seed-Reactive pole appears in an (oriented) dividend position.
  LAW 2 (Synthesis Law):  seed-Reactive home variables are defined only via division
                          (ratio or root-of-ratio), never by pure multiplication/addition.
  LAW 3 (Addition homogeneity, discovered candidate): addition only composes terms of
                          the same pole-class (components of one pole, or same-class elements).

Three strictness strata per occurrence:
  L1 pole-strict : raw or conjugated pole symbols (oriented occurrences)
  L2 component   : named components (P,Q,R,X,G,B) and Re()/Im() wrappers of poles
  L3 magnitude   : Abs() wrapped poles (de-oriented; arguably exempt from LAW 1)

Face forms are checked exactly as written in the corpus; canonical forms are the
pole-basis rewrites (aliases eliminated: Y->1/Z, jwC->1/Zc, jwL->Zl, U*conj(I)->S, ...).
"""

import sympy as sp
from sympy import sqrt, conjugate as conj, Abs, re, im, cos, sin, tan, exp

jj = sp.I  # imaginary unit (corpus uses j)

# ----- symbols -------------------------------------------------------------
P, Q, R, X, L, C, G, B, theta, w = sp.symbols('P Q R X L C G B theta omega', positive=True)
U, Icur, S, Z, Y = sp.symbols('U I S Z Y')  # complex phasors / poles

# ----- seed classification --------------------------------------------------
# DC seed: P=Active-Asserting(Fire) U=Active-Yielding(Air)
#          I=Reactive-Yielding(Water) R=Reactive-Asserting(Earth)
# AC pole successors: S<-P (Active-Asserting), Z<-R (Reactive-Asserting),
#                     U,I promoted wholesale. omega = fifth variable, NO seed bits.
ACTIVE_POLES_DC   = {sp.Symbol('P_dc'), sp.Symbol('U')}   # filled per-mode below
REACTIVE_POLES_DC = {sp.Symbol('I'), sp.Symbol('R_dc')}

POLES_AC     = {S, U, Icur, Z}
ACTIVE_AC    = {S, U}
REACTIVE_AC  = {Icur, Z}
OMEGA        = {w}

# components: parent pole and axis (real=committed/observe, imag=held/behold)
COMPONENT_PARENT = {P: (S, 're'), Q: (S, 'im'), R: (Z, 're'), X: (Z, 'im'),
                    G: (Y, 're'), B: (Y, 'im')}
RECIPROCAL_ALIASES = {Y: Z, C: Z, B: Z, G: Z}   # quantities that are reciprocal-of-Z in kind
ELEMENT_CONSTANTS  = {L, C}
PHASE = {theta}

# DC mode uses P,R as POLES (symbols P,R reused; contextual)
ACTIVE_DC   = {P, U}
REACTIVE_DC = {Icur, R}


# ----- occurrence walker ----------------------------------------------------

def occurrences(expr):
    """Yield (symbol, inverted, num_context, wrappers) for every symbol occurrence.
    inverted     -> occurrence sits in a denominator position.
    num_context  -> occurrence is a genuine DIVIDEND: non-inverted inside a product
                    that also contains an inverted (divided-by) factor.
    wrappers     -> stack of enclosing functions."""
    out = []
    def contains_div(e):
        return any(x.is_Pow and x.args[1].is_number and x.args[1].is_negative
                   for x in sp.preorder_traversal(e))
    def walk(e, inv, numctx, wraps):
        if e.is_Symbol:
            out.append((e, inv, numctx, wraps)); return
        if e.is_Pow:
            base, expo = e.args
            neg = expo.is_number and expo.is_negative
            walk(base, (not inv) if neg else inv, numctx if not neg else False, wraps)
            return
        if e.is_Mul:
            div_here = any(a.is_Pow and a.args[1].is_number and a.args[1].is_negative
                           or contains_div(a) for a in e.args)
            for a in e.args:
                a_inverted_factor = a.is_Pow and a.args[1].is_number and a.args[1].is_negative
                walk(a, inv, (numctx or div_here) and not a_inverted_factor, wraps)
            return
        if e.is_Add:
            for a in e.args: walk(a, inv, numctx, wraps)
            return
        if e.func in (Abs, sp.conjugate, sp.re, sp.im, cos, sin, tan, sp.exp, sqrt):
            for a in e.args: walk(a, inv, numctx, wraps + (e.func.__name__,))
            return
        for a in e.args: walk(a, inv, numctx, wraps)
    walk(sp.sympify(expr), False, False, ())
    return out

def has_division(expr):
    for e in sp.preorder_traversal(sp.sympify(expr)):
        if e.is_Pow and e.args[1].is_number and e.args[1].is_negative:
            return True
    return False

def operator_inventory(expr):
    inv = set()
    for e in sp.preorder_traversal(sp.sympify(expr)):
        if e.is_Add: inv.add('+')
        if e.is_Mul: inv.add('*')
        if e.is_Pow:
            ex = e.args[1]
            if ex == sp.Rational(1,2): inv.add('sqrt')
            elif ex == 2: inv.add('square')
            elif ex.is_number and ex.is_negative: inv.add('/')
        if e.func is sp.conjugate: inv.add('conj')
        if e.func is Abs: inv.add('|.|')
        if e.func in (sp.re, sp.im): inv.add('Re/Im')
        if e.func is sp.exp: inv.add('e^j0')
        if e.func in (cos, sin, tan): inv.add('trig')
        if e == jj or (e.is_Mul and jj in e.args): inv.add('j')
    return sorted(inv)


# ----- law checks ------------------------------------------------------------

def check_numerator_law(expr, reactive, mode='AC'):
    v = {'L1_pole': [], 'L2_component': [], 'L3_magnitude': [], 'alias_inv': [],
         'component_inv': [], 'omega_in_num': []}
    for sym, invd, numctx, wraps in occurrences(expr):
        # inventory (position-independent findings)
        if sym in RECIPROCAL_ALIASES and sym not in COMPONENT_PARENT and sym not in ELEMENT_CONSTANTS:
            v['alias_inv'].append(str(sym))
        if sym in COMPONENT_PARENT:
            v['component_inv'].append(str(sym))
        if invd or not numctx:
            continue  # denominators and free product factors are legal
        if sym in reactive:
            if 'Abs' in wraps:                 v['L3_magnitude'].append('|%s|' % sym)
            elif 're' in wraps or 'im' in wraps: v['L2_component'].append('Re/Im(%s)' % sym)
            else: v['L1_pole'].append(str(sym) + ('*' if 'conjugate' in wraps else ''))
        elif sym in COMPONENT_PARENT:
            parent, axis = COMPONENT_PARENT[sym]
            if parent in reactive or parent is Y:
                v['L2_component'].append('%s(=%s of %s)' % (sym, axis, parent))
        elif sym is Y:
            v['L1_pole'].append('Y(~1/Z)')
        if sym == w and mode == 'AC':
            v['omega_in_num'].append('omega')
    return v

def is_home_class_composition(home, expr):
    """AC amendment: addition of components-of-home or same-class element
    impedances (Z_L, Z_C, Z) is COMPOSITION (series law), not synthesis."""
    top = sp.sympify(expr)
    if not top.is_Add:
        return False
    homefam = {home} | {s for s, (p, a) in COMPONENT_PARENT.items() if p == home}
    if home is Z:
        homefam |= {sp.Symbol('Z_L'), sp.Symbol('Z_C')}
    for term in top.args:
        syms = {s for s in term.free_symbols if s not in ELEMENT_CONSTANTS
                and s != w and s != theta}
        if not syms <= homefam:
            return False
    return True

def check_synthesis_law(home, expr, reactive):
    """Reactive homes must be ratios (or roots of ratios); pure multiplication
    violates. Class-preserving addition = composition (legal, AC amendment)."""
    if home not in reactive:
        return {'applies': False, 'violation': False, 'form': 'active-home'}
    if is_home_class_composition(home, expr):
        return {'applies': True, 'violation': False, 'form': 'composition(class-preserving)'}
    div = has_division(expr)
    top = sp.sympify(expr)
    form = ('ratio' if div else
            'pure-addition' if top.is_Add else
            'pure-multiplication' if top.is_Mul or top.is_Pow else 'other')
    return {'applies': True, 'violation': not div, 'form': form}

def term_pole_signature(term):
    sig = set()
    for s in term.free_symbols:
        if s in POLES_AC: sig.add(str(s))
        elif s in COMPONENT_PARENT: sig.add('cmp:' + str(COMPONENT_PARENT[s][0]))
        elif s in ELEMENT_CONSTANTS: sig.add('elem:Z-side')
        elif str(s) in ('Z_L','Z_C'): sig.add('Z')
        elif s == w: sig.add('omega')
        elif s == Y: sig.add('cmp:Z')
    return frozenset(sig)

def check_addition_homogeneity(expr):
    top = sp.sympify(expr)
    if not top.is_Add:
        return {'applies': False}
    sigs = [term_pole_signature(t) for t in top.args]
    # homogeneous if all terms reference (components/elements of) the same pole family
    fams = set()
    for s in sigs:
        fam = frozenset(x.replace('cmp:', '').replace('elem:Z-side', 'Z') for x in s
                        if x != 'omega')
        fams.add(fam)
    return {'applies': True, 'homogeneous': len(fams) <= 1,
            'signatures': [sorted(s) for s in sigs]}


# ----- equation database ------------------------------------------------------

# (id, home, face_expr, canonical_expr_or_None, identity_status, notes)
DC_EQS = [
    ('DC01','P', U*Icur, None,'identity',''),
    ('DC02','P', U**2/R, None,'identity',''),
    ('DC03','P', Icur**2*R, None,'identity',''),
    ('DC04','I', P/U, None,'identity',''),
    ('DC05','I', U/R, None,'identity',''),
    ('DC06','I', sqrt(P/R), None,'identity',''),
    ('DC07','U', P/Icur, None,'identity',''),
    ('DC08','U', Icur*R, None,'identity',''),
    ('DC09','U', sqrt(P*R), None,'identity',''),
    ('DC10','R', U/Icur, None,'identity',''),
    ('DC11','R', U**2/P, None,'identity',''),
    ('DC12','R', P/Icur**2, None,'identity',''),
]

Zc_sym, Zl_sym = sp.symbols('Z_C Z_L')   # opaque element impedances (Z-kind poles)
REACTIVE_AC = REACTIVE_AC | {Zc_sym, Zl_sym}
Zc = Zc_sym
Zl = Zl_sym

AC_EQS = [
 # --- core five (db 'Steps Towards Completeness') ---
 ('A1','S', U*conj(Icur), None, 'identity', 'S = U I* (correct EE form)'),
 ('A2','U', Z*Icur, None, 'identity', "Ohm's law, phasor form"),
 ('A3','I', conj(S)/conj(U), None, 'identity', 'I = S*/U* (correct conj form)'),
 ('A4','Z', U/Icur, None, 'identity', 'duplicate of C4.1'),
 ('A5','omega', im(S)/(im(Z)*Abs(Icur)**2), im(S)/(L*Abs(Icur)**2),
   'ERRATUM', 'as written reduces to omega=1 (Q=|I|^2 X identically); denominator should use L not Im(Z); quoted verbatim in L3 file'),

# --- Ch1: S ---
 ('C1.1','S', P+jj*Q, None, 'identity', 'component assembly of own pole'),
 ('C1.2','S', U*Icur, U*conj(Icur), 'ERRATUM', 'missing conjugate; correct S=U I*'),
 ('C1.3','S', Abs(U)*Abs(Icur)*cos(theta), None, 'ERRATUM',
   '|U||I|cos(theta) = P (real power), not S; LHS should be P'),
 ('C1.4','Q', Abs(S)*sin(theta), None, 'identity', 'component defined by de-oriented mult'),
 ('C1.5','|S|^2', P**2+Q**2, None, 'identity', 'Pythagorean; magnitudes only'),
 ('C1.6','S', sqrt(P*Q)*exp(jj*theta), None, 'ERRATUM',
   '|S|=sqrt(P^2+Q^2) not sqrt(PQ); geometric-mean form wrong except P=Q'),

# --- Ch2: U ---
 ('C2.1','U', S/Icur, S/conj(Icur), 'ERRATUM', 'should be S/I*'),
 ('C2.2','U', sqrt(P**2+Q**2)/(conj(Icur)/Abs(Icur)), None, 'ERRATUM-phase',
   'magnitude correct (|U|=|S|/|I|), phase lands on phi_I not phi_U'),
 ('C2.3','U', w*L*Icur, Zl_sym*Icur, 'ERRATUM-j', 'inductor law; missing j (U=jwL I)'),
 ('C2.4','U', Icur/(jj*w*C), Zc_sym*Icur, 'identity',
   'capacitor law; FACE: I in numerator; CANONICAL: U = Zc*I multiplication'),
 ('C2.5','U', sqrt(S*(R+jj*X)), sqrt(S*Z), 'phase-loose',
   'exact form |U|^2 = S Z*; magnitude-true'),
 ('C2.6','U', (sqrt(P**2+Q**2)/Abs(Y))*(re(Y)-jj*im(Y))/sqrt(re(Y)**2+im(Y)**2),
   Abs(S)*Z, 'ERRATUM-dim', 'simplifies to |S|Z which has units of |U|^2, not U'),
 ('C2.7','U', w*sqrt(L*S/conj(Icur)), None, 'operating-point',
   'not a network identity; holds at specific operating point'),
 ('C2.8','U', sqrt(S/(jj*w*C*conj(Icur))), None, 'operating-point',
   'reduces to U = Zc numerically; operating-point readout'),

# --- Ch3: I ---
 ('C3.1','I', conj(S)/U, conj(S)/conj(U), 'ERRATUM', 'should be S*/U*'),
 ('C3.2','I', U/Z, None, 'identity', ''),
 ('C3.3','I', sqrt(S/Z), None, 'identity-magnitude',
   'S/Z = |I|^2 exactly (real!); root gives |I|, phase collapsed'),
 ('C3.4','I', sqrt(P**2+Q**2)/(conj(U)/Abs(U)), None, 'ERRATUM-phase',
   'magnitude correct, phase lands on phi_U not phi_I'),
 ('C3.5','I', U/(jj*w*L), U/Zl_sym, 'identity', 'inductor law; face-legal'),
 ('C3.6','I', U*(jj*w*C), U/Zc_sym, 'identity',
   'capacitor law; FACE: Reactive home by PURE MULTIPLICATION; CANONICAL: I=U/Zc ratio'),
 ('C3.7','I', sqrt(S/(R+jj*X)), sqrt(S/Z), 'identity-magnitude', 'same as C3.3'),
 ('C3.8','I', U*Y, U/Z, 'identity',
   'admittance alias; FACE: mult-synthesis; CANONICAL: I=U/Z ratio'),
 ('C3.9','I', sqrt(S*Y), sqrt(S/Z), 'identity-magnitude',
   'FACE: root of product; CANONICAL: root of ratio'),
 ('C3.10','I', (w/Abs(Z))*sqrt(Abs(S)*L), None, 'operating-point',
   'holds where |Z| = omega^2 L; hybrid mult/div form'),

# --- Ch4: Z ---
 ('C4.1','Z', U/Icur, None, 'identity', ''),
 ('C4.2','Z', U**2/conj(S), Abs(U)**2/conj(S), 'ERRATUM-phase',
   'exact form Z = |U|^2/S*; U^2 carries 2*phi_U phase error'),
 ('C4.3','Z', S/Icur**2, S/Abs(Icur)**2, 'ERRATUM-phase',
   'exact form Z = S/|I|^2; I^2 carries phase error'),
 ('C4.4','Z', (Abs(U)**2/P)*(1+jj*Q/P), Abs(U)**2*S/(P**2+Q**2), 'ERRATUM',
   'as written = |U|^2 S/P^2; exact requires /(P^2+Q^2) = /|S|^2'),
 ('C4.5','Z', w*L + 1/(jj*w*C), Zl_sym + Zc_sym, 'ERRATUM-j',
   'series composition; missing j on wL; FACE: addition + product term'),
 ('C4.6','Z', R+jj*X, None, 'identity', 'component assembly of own pole'),
 ('C4.7','Z', Abs(Z)*(cos(theta)+jj*sin(theta)), None, 'representation',
   'polar identity — self-representation, excluded from synthesis check'),
 ('C4.8','Z', sqrt(P**2+Q**2)/Abs(Icur)**2, None, 'identity-magnitude',
   '= |S|/|I|^2 = |Z|; magnitude-true'),
 ('C4.9','Z', (Abs(U)**2/Abs(S))*(P/Abs(S)-jj*Q/Abs(S)), Abs(U)**2/conj(S), 'ERRATUM-conj',
   'simplifies to |U|^2 S*/|S|^2 = |U|^2/S; exact is |U|^2/S*'),
 ('C4.10','Z', 1/Y, None, 'identity', 'reciprocal declaration — the alias generator'),

# --- Ch5: omega ---
 ('C5.1','omega', im(S)/(im(Z)*Abs(Icur)**2), im(S)/(L*Abs(Icur)**2), 'ERRATUM',
   'duplicate of A5; reduces to 1'),
 ('C5.2','omega', im(U*conj(Icur)/(Abs(Icur)**2*L)), im(S/(Abs(Icur)**2*L)), 'identity-context',
   'inductive context: = Q/(|I|^2 L) = X/L = omega. FACE: I* in numerator product; '
   'CANONICAL: numerator U I* = S (pole)'),
 ('C5.3','omega', 1/im(U*conj(Icur)/(Abs(Icur)**2*C)), None, 'ERRATUM-grouping',
   'C must sit outside Im(); as written off by C^2 factor'),
 ('C5.4','omega', sqrt(1/(L*C)), None, 'identity-context',
   'resonance; no poles present at all — element constants only'),
 ('C5.5','omega', R/(L*tan(theta)), None, 'ERRATUM',
   'tan(theta)=wL/R gives omega = R tan(theta)/L; as written holds only at theta=45deg. '
   'FACE: R (Re Z) in numerator'),
 ('C5.6','omega', (Abs(U)/Abs(Icur))/sqrt(L**2+(R/w)**2), None, 'identity-context',
   'series RL: EXACT identity (implicit in omega). Face-legal: |I| in denominator, R in denominator'),
 ('C5.7','omega', Abs(Icur)/(Abs(U)*sqrt(C**2+(1/(w*R))**2)), 1/(Abs(Z)*sqrt(C**2+(1/(w*R))**2)),
   'identity-context', 'parallel RC: EXACT. FACE: |I| in numerator; CANONICAL: 1/(|Z| ...) heals it'),
 ('C5.8','omega', im(Y)/C, None, 'identity-context',
   'B/C = omega (parallel C). FACE: component of reciprocal-Reactive in numerator'),
 ('C5.9','omega', re(Z)/L, None, 'operating-point',
   '= R/L; holds only where omega L = R (corner frequency). FACE: R in numerator; '
   'does NOT canonicalize into pole basis — strongest residual'),
 ('C5.10','omega', sqrt(Abs(S)/(L*Abs(Icur)**2)-(R/L)**2), None, 'ERRATUM-squares',
   'should be |Z|^2 form: omega = X/L requires (|S|/|I|^2)^2; missing squares. '
   'FACE: R in numerator inside root'),
]

# ----- verification of selected identities (sympy, with context) -------------

def verify_identities():
    results = {}
    Us, Is = sp.symbols('U_s I_s')  # generic complex
    Zk = sp.symbols('Z_k')
    # S/Z == |I|^2  (C3.3)
    Sx = Us*conj(Is); Zx = Us/Is
    results['C3.3: S/Z = |I|^2'] = sp.simplify(Sx/Zx - Is*conj(Is)) == 0
    # |U|^2 == S Z*  (C2.5 exact form)
    results['C2.5x: |U|^2 = S Z*'] = sp.simplify(Sx*conj(Zx) - Us*conj(Us)) == 0
    # Z == |U|^2/S*  (C4.2 exact form)
    results['C4.2x: Z = |U|^2/S*'] = sp.simplify(Us*conj(Us)/conj(Sx) - Zx) == 0
    # Z == S/|I|^2   (C4.3 exact form)
    results['C4.3x: Z = S/|I|^2'] = sp.simplify(Sx/(Is*conj(Is)) - Zx) == 0
    # A5 as written reduces to 1: Q = |I|^2 X identically  (S = |I|^2 Z)
    Rv, Xv, Iv = sp.symbols('R_v X_v I_v', positive=True, real=True)
    Q_ = Iv**2*Xv
    results['A5: Im(S)/(Im(Z)|I|^2) = 1'] = sp.simplify(Q_/(Xv*Iv**2)) == 1
    # C5.6 exact (series RL): |Z| = sqrt(R^2 + w^2 L^2)
    Rv2, Lv, wv = sp.symbols('R2 L2 w2', positive=True)
    Zmag = sp.sqrt(Rv2**2 + wv**2*Lv**2)
    rhs = Zmag/sp.sqrt(Lv**2 + (Rv2/wv)**2)
    results['C5.6: exact = omega'] = sp.simplify(rhs - wv) == 0
    # C5.7 exact (parallel RC): |Y| = sqrt(1/R^2 + w^2 C^2)
    Cv = sp.symbols('C2', positive=True)
    Ymag = sp.sqrt(1/Rv2**2 + wv**2*Cv**2)
    rhs2 = Ymag/sp.sqrt(Cv**2 + (1/(wv*Rv2))**2)
    results['C5.7: exact = omega'] = sp.simplify(rhs2 - wv) == 0
    # C5.5 corrected: omega = R tan(theta)/L with tan = wL/R
    results['C5.5 corrected form'] = sp.simplify(Rv2*(wv*Lv/Rv2)/Lv - wv) == 0
    # C5.2: Q/(|I|^2 L) = X/L = omega when X = wL
    results['C5.2: = omega (X=wL)'] = sp.simplify((Iv**2*(wv*Lv))/(Iv**2*Lv) - wv) == 0
    # canonical equivalences (alias elimination)
    results['C3.6: U*jwC == U/Zc'] = sp.simplify(Us*(jj*wv*Cv) - Us/(1/(jj*wv*Cv))) == 0
    results['C2.4: I/(jwC) == Zc*I'] = sp.simplify(Is/(jj*wv*Cv) - (1/(jj*wv*Cv))*Is) == 0
    results['C3.8: U*Y == U/Z (Y=1/Z)'] = sp.simplify(Us*(1/Zk) - Us/Zk) == 0
    return results


# ----- runner -----------------------------------------------------------------

def run(eqs, reactive, mode, label):
    print('='*100)
    print(f'{label}:  {len(eqs)} equations   reactive set = {sorted(str(s) for s in reactive)}')
    print('='*100)
    stats = {'L1':0,'L2':0,'L3':0,'alias':0,'synth':0,'add_ok':0,'add_bad':0,
             'errata':0,'op_ct':{}}
    rows = []
    for eid, home, face, canon, status, notes in eqs:
        nl = check_numerator_law(face, reactive, mode)
        home_sym = {'P':P,'I':Icur,'U':U,'R':R,'S':S,'Z':Z,'omega':w,
                    'Q':Q,'|S|^2':None}.get(home)
        sl = (check_synthesis_law(home_sym, face, reactive)
              if home_sym is not None and status != 'representation'
              else {'applies': False, 'violation': False, 'form': 'excluded'})
        ah = check_addition_homogeneity(face)
        ops = operator_inventory(face)
        for o in ops: stats['op_ct'][o] = stats['op_ct'].get(o,0)+1
        l1, l2, l3 = nl['L1_pole'], nl['L2_component'], nl['L3_magnitude']
        al = sorted(set(nl['alias_inv']))
        if l1: stats['L1'] += 1
        if l2: stats['L2'] += 1
        if l3: stats['L3'] += 1
        if al: stats['alias'] += 1
        if sl.get('violation'): stats['synth'] += 1
        if ah.get('applies'):
            stats['add_ok' if ah['homogeneous'] else 'add_bad'] += 1
        if 'ERRATUM' in status: stats['errata'] += 1

        # canonical re-check
        c_l1 = c_synth = None
        if canon is not None:
            cn = check_numerator_law(canon, reactive, mode)
            c_l1 = cn['L1_pole']
            c_synth = (check_synthesis_law(home_sym, canon, reactive)['violation']
                       if home_sym is not None else False)
        rows.append((eid, home, str(face), l1, l2, l3, al, sl, ah, ops, status,
                     str(canon) if canon is not None else '', c_l1, c_synth, notes))

    for r in rows:
        (eid, home, face, l1, l2, l3, al, sl, ah, ops, status, canon, c_l1, c_s, notes) = r
        flags = []
        if l1: flags.append(f'NUM-L1:{l1}')
        if l2: flags.append(f'NUM-L2:{l2}')
        if l3: flags.append(f'num-L3(mag):{l3}')
        if al: flags.append(f'alias-present:{al}')
        if sl.get('violation'): flags.append(f'SYNTH:{sl["form"]}')
        if ah.get('applies'): flags.append('ADD:' + ('homog' if ah['homogeneous'] else 'HETEROG'))
        add_bad = ah.get('applies') and not ah.get('homogeneous')
        verdict = 'PASS' if not (l1 or l2 or sl.get('violation') or add_bad) else 'FACE-VIOLATION'
        heal = ''
        if canon:
            healed = (not c_l1) and (not c_s)
            heal = f'  -> canonical: {canon}  [{"HEALED" if healed else "STILL VIOLATING"}]'
        print(f'{eid:6s} {home:6s} = {face}')
        print(f'       [{verdict}] {" ".join(flags) if flags else "clean"}  ops={ops}  status={status}')
        if heal: print(f'      {heal}')
        if notes: print(f'       note: {notes}')
    print('-'*100)
    print(f'SUMMARY {label}: L1 pole-numerator violations: {stats["L1"]} | '
          f'L2 component: {stats["L2"]} | L3 magnitude(exempt-class): {stats["L3"]} | '
          f'alias occurrences: {stats["alias"]} | synthesis violations: {stats["synth"]} | '
          f'additions homog/heterog: {stats["add_ok"]}/{stats["add_bad"]} | '
          f'errata candidates: {stats["errata"]}')
    print(f'operator inventory (eq counts): {stats["op_ct"]}')
    return stats, rows



if __name__ == '__main__':
    dc_stats, dc_rows = run(DC_EQS, REACTIVE_DC, 'DC', 'DC SET (12 equations — control run)')
    print()
    ac_stats, ac_rows = run(AC_EQS, REACTIVE_AC, 'AC', 'AC SET (49 equations — survival trace)')
    print()
    print('='*100)
    print('IDENTITY VERIFICATIONS (sympy, exact/contextual)')
    print('='*100)
    for k, v in verify_identities().items():
        print(f'  {"VERIFIED" if v else "FAILED  "}  {k}')

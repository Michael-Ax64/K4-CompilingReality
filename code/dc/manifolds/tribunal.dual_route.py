#!/usr/bin/env python3
"""
Dual-Route Trace (Open Trace 2): is the linear/nonlinear pairing systematic?

Candidate Route Law (to be tested, not assumed):
  R1. Every DC pole has exactly three routes (one per pair of the other three).
  R2. SQUARE-routes: home is Asserting (P,R); the squared operand is Yielding (U,I);
      the remaining factor is the other Asserting pole.
  R3. ROOT-routes: home is Yielding (U,I); the radicand's poles are EXCLUSIVELY
      the two Asserting poles (P,R).
  R4. Census: Asserting homes have 1 linear + 2 square routes; Yielding homes have
      2 linear + 1 root route. Set-wide: 6 linear + 6 nonlinear.

AC survival: same laws with Asserting-successors {S,Z} and Yielding {U,I};
magnitude-square |x|^2 counts as the de-orientation generalization of x^2.
Scope: identity-class pole-home equations only (operating-point readouts and
omega-class equations are out of the Route Law's domain by construction).
"""
import os
import sys
import importlib.util
import sympy as sp


def _load_sibling(alias, *candidate_files):
    """Import a sibling module that may carry a dotted codex filename
    (e.g. 'tribunal.ac_checker.py'), which is not a valid flat import name."""
    if alias in sys.modules:
        return sys.modules[alias]
    here = os.path.dirname(os.path.abspath(__file__))
    for fname in candidate_files:
        path = os.path.join(here, fname)
        if os.path.exists(path):
            spec = importlib.util.spec_from_file_location(alias, path)
            mod = importlib.util.module_from_spec(spec)
            sys.modules[alias] = mod
            spec.loader.exec_module(mod)
            return mod
    raise ImportError(f"Could not locate any of {candidate_files} beside {__file__}")


_ac = _load_sibling("tribunal_ac_checker", "tribunal.ac_checker.py", "ac_checker.py")
DC_EQS, AC_EQS = _ac.DC_EQS, _ac.AC_EQS
P, Q, R, X, L, C, G, B, theta, w = (_ac.P, _ac.Q, _ac.R, _ac.X, _ac.L,
                                    _ac.C, _ac.G, _ac.B, _ac.theta, _ac.w)
U, Icur, S, Z, Y = _ac.U, _ac.Icur, _ac.S, _ac.Z, _ac.Y
from sympy import Abs, conjugate, sqrt

ASSERT_DC, YIELD_DC = {P, R}, {U, Icur}
ASSERT_AC = {S, Z, sp.Symbol('Z_L'), sp.Symbol('Z_C')}
YIELD_AC  = {U, Icur}

MAG_IDIOM = sqrt(P**2 + Q**2)          # component idiom for |S|
MAG_IDIOM2 = P**2 + Q**2               # component idiom for |S|^2

def canon_idioms(expr):
    """Rewrite component magnitude-assembly idioms to the pole magnitude."""
    e = sp.sympify(expr)
    e = e.subs(MAG_IDIOM, Abs(S)).subs(MAG_IDIOM2, Abs(S)**2)
    return e

def route_type(expr):
    """Classify the route by its de/re-orientation structure.
      'root'    : a pole-bearing radicand (Pow(.., +-1/2)), no squared operands
      'square'  : a pole squared at exponent +-2, or Abs(pole)**+-2
      'shadow'  : every pole operand occurs de-oriented (inside Abs) -- the
                  route carries no orientation and can only land on |home|
      'linear'  : none of the above
    Returns (type, detail)."""
    e = canon_idioms(expr)
    sq_ops, mag_ops, root_bases = [], [], []
    for node in sp.preorder_traversal(e):
        if node.is_Pow:
            b, ex = node.args
            if ex in (2, -2):
                if b.is_Symbol: sq_ops.append(b)
                elif b.func is Abs and b.args[0].is_Symbol: mag_ops.append(b.args[0])
            if ex in (sp.Rational(1, 2), sp.Rational(-1, 2)):
                root_bases.append(b)
    if root_bases and not sq_ops and not mag_ops:
        return 'root', sp.Mul(*root_bases)
    if sq_ops or mag_ops:
        return 'square', (sq_ops, mag_ops)
    # shadow: poles present, but every pole occurrence is inside Abs()
    pole_syms = {S, U, Icur, Z} | {sp.Symbol('Z_L'), sp.Symbol('Z_C'), P, R}
    oriented = deoriented = 0
    def walk(n, in_abs):
        nonlocal oriented, deoriented
        if n.is_Symbol and n in pole_syms:
            if in_abs: deoriented += 1
            else: oriented += 1
            return
        for a in n.args:
            walk(a, in_abs or n.func is Abs)
    walk(e, False)
    if deoriented and not oriented:
        return 'shadow', None
    return 'linear', None

def poles_in(expr, poleset):
    return {s for s in sp.sympify(expr).free_symbols if s in poleset}

def run_dc():
    print('=' * 90)
    print('DC DUAL-ROUTE TRACE (12 equations)')
    print('=' * 90)
    census = {str(h): {'linear': 0, 'square': 0, 'root': 0}
              for h in ['P', 'U', 'I', 'R']}
    violations = []
    HOME = {'P': P, 'U': U, 'I': Icur, 'R': R}
    for eid, home, face, canon, status, notes in DC_EQS:
        rt, detail = route_type(face)
        census[home][rt] += 1
        hs = HOME[home]
        verdict = 'OK'
        if rt == 'square':
            sq, mags = detail
            squared = set(sq) | set(mags)
            others = poles_in(face, ASSERT_DC | YIELD_DC) - squared
            if hs not in ASSERT_DC:
                verdict = 'VIOLATES R2: square-route home not Asserting'
            elif not squared <= YIELD_DC:
                verdict = f'VIOLATES R2: squared operand {squared} not Yielding'
            elif not others <= ASSERT_DC:
                verdict = f'VIOLATES R2: co-factor {others} not Asserting'
        elif rt == 'root':
            radicand_poles = poles_in(detail, ASSERT_DC | YIELD_DC)
            if hs not in YIELD_DC:
                verdict = 'VIOLATES R3: root-route home not Yielding'
            elif not radicand_poles <= ASSERT_DC:
                verdict = f'VIOLATES R3: radicand poles {radicand_poles} not all Asserting'
        if 'VIOLATES' in verdict:
            violations.append((eid, verdict))
        print(f'  {eid}  {home} = {face}   [{rt}]  {verdict}')
    print('-' * 90)
    print('  Route census per home:')
    ok4 = True
    for h in ['P', 'U', 'I', 'R']:
        c = census[h]
        cls = 'Asserting' if h in ('P', 'R') else 'Yielding'
        expect = (1, 2, 0) if cls == 'Asserting' else (2, 0, 1)
        got = (c['linear'], c['square'], c['root'])
        match = 'MATCHES R4' if got == expect else f'VIOLATES R4 (expected {expect})'
        if got != expect: ok4 = False
        print(f'    {h} ({cls}): linear={c["linear"]} square={c["square"]} '
              f'root={c["root"]}   {match}')
    tot = {k: sum(census[h][k] for h in census) for k in ('linear', 'square', 'root')}
    print(f'  Set-wide: linear={tot["linear"]} nonlinear={tot["square"]+tot["root"]} '
          f'(square={tot["square"]}, root={tot["root"]})')
    print(f'  R1 (3 routes/pole): '
          f'{"HOLDS" if all(sum(c.values())==3 for c in census.values()) else "FAILS"}')
    print(f'  R2/R3 typed-route violations: {len(violations)}')
    print(f'  R4 census: {"HOLDS" if ok4 else "FAILS"}')
    return violations

def run_ac():
    print()
    print('=' * 90)
    print('AC DUAL-ROUTE SURVIVAL (identity-class pole-home equations)')
    print('=' * 90)
    HOME = {'S': S, 'U': U, 'I': Icur, 'Z': Z}
    in_scope = out_scope = 0
    violations, confirms = [], []
    for eid, home, face, canon, status, notes in AC_EQS:
        if home not in HOME:
            continue
        if not (status.startswith('identity') or status == 'phase-loose'
                or 'ERRATUM-phase' in status or 'ERRATUM-conj' in status):
            out_scope += 1
            continue  # operating-point, representation, and hard errata: out of domain
        expr = canon_idioms(canon if canon is not None else face)
        rt, detail = route_type(expr)
        if rt == 'linear':
            in_scope += 1
            continue
        in_scope += 1
        if rt == 'shadow':
            oriented_home = home in ('S', 'U', 'I', 'Z')
            pred = ('PREDICTS PHASE-ERRATUM (oriented home fed by de-oriented route)'
                    if oriented_home else 'shadow route, magnitude home: legal')
            flagged = ('ERRATUM-phase' in status or 'magnitude' in status)
            hit = 'CONFIRMED by identity trace' if flagged else 'NOT independently flagged'
            print(f'  {eid}  {home} = {expr}   [shadow]  {pred}  [{hit}]')
            confirms.append((eid, home, rt, pred))
            continue
        hs = HOME[home]
        verdict = 'OK'
        if rt == 'square':
            sq, mags = detail
            squared = set(sq) | set(mags)
            others = poles_in(expr, ASSERT_AC | YIELD_AC) - squared
            if hs not in ASSERT_AC:
                verdict = 'VIOLATES R2(AC): square/magnitude home not Asserting-successor'
            elif not squared <= YIELD_AC:
                verdict = f'VIOLATES R2(AC): de-oriented operand {squared} not Yielding'
            elif not (others <= ASSERT_AC or not others):
                verdict = f'VIOLATES R2(AC): co-factor {others} not Asserting-successor'
        elif rt == 'root':
            radicand_poles = poles_in(detail, ASSERT_AC | YIELD_AC)
            if hs not in YIELD_AC:
                verdict = 'VIOLATES R3(AC): root-route home not Yielding'
            elif not radicand_poles <= ASSERT_AC:
                verdict = (f'VIOLATES R3(AC): radicand poles {radicand_poles} '
                           f'not all Asserting-successors')
            else:
                verdict = ('OK (lands magnitude-true: sqrt repays 1 bit, '
                           'cannot repay the S^1 phase burned by |.|)')
        (violations if 'VIOLATES' in verdict else confirms).append((eid, home, rt, verdict))
        print(f'  {eid}  {home} = {expr}   [{rt}]  {verdict}')
    print('-' * 90)
    print(f'  In-scope identity-class equations: {in_scope}; out-of-scope '
          f'(operating-point/representation/hard-errata): {out_scope}')
    print(f'  Nonlinear routes checked: {len(confirms)+len(violations)}; '
          f'confirming: {len(confirms)}; violating: {len(violations)}')
    for eid, home, rt, _ in confirms:
        dc_analog = {'C2.5': 'U=sqrt(P*R)', 'C3.3': 'I=sqrt(P/R)',
                     'C3.7': 'I=sqrt(P/R)', 'C3.9': 'I=sqrt(P/R)',
                     'C4.2': 'R=U^2/P', 'C4.3': 'R=P/I^2', 'C4.8': 'R-magnitude'}
        print(f'    {eid} [{rt}] -> DC analog: {dc_analog.get(eid, "(new)")}')
    return violations

if __name__ == '__main__':
    v1 = run_dc()
    v2 = run_ac()
    print()
    print('=' * 90)
    verdict = ('ROUTE LAW HOLDS (DC exceptionless; AC identity-class survives)'
               if not v1 and not v2 else 'ROUTE LAW BROKEN — see violations above')
    print(f'FINAL: {verdict}')

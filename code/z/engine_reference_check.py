"""Mechanical verification suite for ENGINE-REFERENCE-DC.md (DC baseline).

Ground truth: L4-TheTwelveGates §II (12 decorated gates), the corpus Direction Law,
the bimedian matchings, and the 24-permutation rigidity profile (scripts/permutation_check.py).

Checks:
  1. ISA opcode table vs gate table (equation, Home, AbsentVar, edge, direction)
  2. Edge-pairing structure: 12 gates -> 6 edges x 2 antiparallel opcodes (bijection?)
  3. Tier classification: slopes 2 / 1/2 / 1, tier homes, tier counts 4/2/6
  4. Numerator Law: dividends in {P,U}, divisors in {I,R}
  5. Graded partition: squares act only on {U,I}, roots only over {P,R}
  6. Trigram byte: 8 transversals = 4 apex stars + 4 faces, zero remainder
  7. MMU face relations (Sec 4.1) vs AbsentVar rule
  8. S4 rigidity profile: automorphism, survivor census, unreachable rows (guardians),
     tests the doc's two Rigidity-Finding claims
  9. Ring audit: muted matching -> live edges/opcodes (8?) vs doc's listed 6;
     PIS/LIB reachability; Tier-2 availability per ring
 10. Register A/B decomposition vs the 4-state table, under both bit conventions,
     plus the commit/polarity relabel
 11. Modality vs edge-matching label collisions
 12. Arithmetic: 2^12, 64x64, 2^3, 64x6, 32x12
"""

from itertools import permutations

POLES = ['P', 'U', 'I', 'R']
ACTIVE, REACTIVE = {'P', 'U'}, {'I', 'R'}

# name: (lhs, template, args, home, absentvar, direction_from, direction_to, tier)
# tier: 1=COMMIT (slope 2), 2=RESEED (slope 1/2), 3=ROUTE (slope 1)
GATES = {
    'ARI': ('P', 'sq_div',   ('U', 'R'), 'P', 'I', 'U', 'R', 1),
    'TAU': ('P', 'sq_mul',   ('I', 'R'), 'P', 'U', 'R', 'I', 1),
    'GEM': ('P', 'mul',      ('U', 'I'), 'P', 'R', 'I', 'U', 3),
    'CAN': ('I', 'sqrt_div', ('P', 'R'), 'I', 'U', 'P', 'R', 2),
    'LEO': ('I', 'div',      ('P', 'U'), 'I', 'R', 'U', 'P', 3),
    'VIR': ('I', 'div',      ('U', 'R'), 'I', 'P', 'R', 'U', 3),
    'LIB': ('U', 'div',      ('P', 'I'), 'U', 'R', 'P', 'I', 3),
    'SCO': ('U', 'mul',      ('I', 'R'), 'U', 'P', 'I', 'R', 3),
    'SAG': ('U', 'sqrt_mul', ('P', 'R'), 'U', 'I', 'R', 'P', 2),
    'CAP': ('R', 'div',      ('U', 'I'), 'R', 'P', 'U', 'I', 3),
    'AQU': ('R', 'sq_div',   ('U', 'P'), 'R', 'I', 'P', 'U', 1),
    'PIS': ('R', 'div_sq',   ('P', 'I'), 'R', 'U', 'I', 'P', 1),
}
MODALITY = {g: ('Cardinal' if g in ('ARI', 'CAN', 'LIB', 'CAP') else
                'Fixed' if g in ('TAU', 'LEO', 'SCO', 'AQU') else 'Mutable')
            for g in GATES}
MATCHING = {frozenset(e): m for e, m in [
    ({'P', 'U'}, 'Fixed'), ({'I', 'R'}, 'Fixed'),
    ({'P', 'R'}, 'Cardinal'), ({'I', 'U'}, 'Cardinal'),
    ({'P', 'I'}, 'Mutable'), ({'U', 'R'}, 'Mutable')]}

print("=" * 72)
print("CHECK 1 — ISA table vs gate table (equation, Home, AbsentVar, edge, direction)")
ok = 0
for g, (lhs, tpl, args, home, av, frm, to, tier) in GATES.items():
    residual = set(POLES) - {home, av}
    edge_ok = {frm, to} == residual
    lhs_ok = lhs == home
    ok += edge_ok and lhs_ok
    if not (edge_ok and lhs_ok):
        print(f"  {g}: MISMATCH edge={frm}-{to} residual={sorted(residual)} lhs={lhs} home={home}")
print(f"  edge == {{non-home, non-absent poles}} and lhs == Home: {ok}/12 PASS")

print("=" * 72)
print("CHECK 2 — edge pairing: 12 opcodes on 6 edges, antiparallel couples")
from collections import defaultdict
edges = defaultdict(list)
for g, (lhs, tpl, args, home, av, frm, to, tier) in GATES.items():
    edges[frozenset([frm, to])].append((g, frm, to))
assert len(edges) == 6
for e, members in sorted(edges.items(), key=lambda kv: sorted(kv[0])):
    assert len(members) == 2, members
    (g1, f1, t1), (g2, f2, t2) = sorted(members)
    anti = (f1 == t2 and f2 == t1)
    print(f"  edge {'-'.join(sorted(e))} ({MATCHING[e]:8s}): {g1} {f1}->{t1}  |  {g2} {f2}->{t2}   antiparallel: {anti}")

print("=" * 72)
print("CHECK 3 — tier classification (slope / homes / counts)")
tier_of_tpl = {'sq_div': 1, 'sq_mul': 1, 'div_sq': 1, 'sqrt_div': 2, 'sqrt_mul': 2,
               'div': 3, 'mul': 3}
slope = {1: '2', 2: '1/2', 3: '1'}
by_tier = defaultdict(list)
for g, row in GATES.items():
    assert row[7] == tier_of_tpl[row[1]], (g, "tier/template mismatch")
    by_tier[row[7]].append(g)
for t in (1, 2, 3):
    homes = sorted({GATES[g][3] for g in by_tier[t]})
    print(f"  Tier {t} (slope {slope[t]}): n={len(by_tier[t]):2d}  homes={homes}  {sorted(by_tier[t])}")

print("=" * 72)
print("CHECK 4 — Numerator Law (dividends active, divisors reactive)")
viol = []
for g, (lhs, tpl, args, *_rest) in GATES.items():
    if tpl in ('div', 'sq_div', 'sqrt_div'):
        num, den = args
        if num not in ACTIVE: viol.append((g, 'dividend', num))
        if den not in REACTIVE: viol.append((g, 'divisor', den))
    elif tpl == 'div_sq':
        num, den = args
        if num not in ACTIVE: viol.append((g, 'dividend', num))
        if den not in REACTIVE: viol.append((g, 'divisor', den))
print(f"  violations: {viol if viol else 'none — 12/12 PASS'}")

print("=" * 72)
print("CHECK 5 — graded partition: squared poles vs rooted poles")
squared, rooted = set(), set()
for g, (lhs, tpl, args, *_r) in GATES.items():
    if tpl in ('sq_div', 'sq_mul'):
        squared.add(args[0])
    elif tpl == 'div_sq':
        squared.add(args[1])
    elif tpl in ('sqrt_div', 'sqrt_mul'):
        rooted.update(args)
print(f"  squared poles: {sorted(squared)}   rooted poles: {sorted(rooted)}")
print(f"  squares touch only {{U,I}}: {squared <= {'U', 'I'}}   roots touch only {{P,R}}: {rooted <= {'P', 'R'}}")
print(f"  root edge P-R is exactly the edge whose endpoints are never squared: "
      f"{frozenset(rooted) in [frozenset(e) for e in MATCHING]}")

print("=" * 72)
print("CHECK 6 — trigram byte: 8 transversals = 4 stars + 4 faces")
match_lists = {'Fixed': [('P', 'U'), ('I', 'R')], 'Cardinal': [('P', 'R'), ('I', 'U')],
               'Mutable': [('P', 'I'), ('U', 'R')]}
transversals = []
for e1 in match_lists['Fixed']:
    for e2 in match_lists['Cardinal']:
        for e3 in match_lists['Mutable']:
            transversals.append((e1, e2, e3))
stars, faces = [], []
for tset in transversals:
    es = [frozenset(e) for e in tset]
    deg = {p: sum(p in e for e in es) for p in POLES}
    if 3 in deg.values():
        apex = [p for p, d in deg.items() if d == 3][0]
        stars.append((apex, tset))
    else:
        verts = sorted({p for e in es for p in e})
        faces.append((set(POLES) - set(verts)).pop() if len(verts) == 3 else '?', tset) if False else \
        faces.append((list(set(POLES) - set(verts))[0], tset))
print(f"  transversals: {len(transversals)}  stars: {len(stars)}  faces: {len(faces)}  (4+4=8, zero remainder: {len(stars)+len(faces)==8})")
for apex, tset in stars: print(f"    star of {apex}: {tset}")
for absent, tset in faces: print(f"    face absent {absent}: {tset}")

print("=" * 72)
print("CHECK 7 — MMU face relations (Sec 4.1) vs AbsentVar rule")
face_rel = {'P': ('U', 'mul', ('I', 'R')), 'I': ('P', 'sq_div', ('U', 'R')),
            'U': ('P', 'sq_mul', ('I', 'R')), 'R': ('P', 'mul', ('U', 'I'))}
for av, rel in face_rel.items():
    match = [g for g, row in GATES.items() if row[4] == av and row[1] == rel[1]
             and frozenset(row[2]) == frozenset(rel[2])]
    print(f"  face absent {av}: relation {rel[0]} = {rel[2][0]}·{rel[2][1]} -> gate {match}")

print("=" * 72)
print("CHECK 8 — S4 rigidity profile (decorated table)")
SYM = {'mul', 'sqrt_mul'}
def canon(l, t, a):
    return (l, t, tuple(sorted(a)) if t in SYM else tuple(a))
BARE = {canon(r[0], r[1], r[2]) for r in GATES.values()}
DECO = {canon(r[0], r[1], r[2]): r[4] for r in GATES.values()}
profile = []
for perm in permutations(POLES):
    m = dict(zip(POLES, perm))
    d, surv = 0, []
    for g, row in GATES.items():
        lhs, tpl, args, home, av = row[0], row[1], row[2], row[3], row[4]
        rel = canon(m[lhs], tpl, tuple(m[a] for a in args))
        if rel in DECO and DECO[rel] == m[av]:
            d += 1
            tgt = [g2 for g2, r2 in GATES.items() if canon(r2[0], r2[1], r2[2]) == rel][0]
            surv.append((g, tgt, tpl))
    profile.append((d, perm, surv))
auto = [p for d, p, s in profile if d == 12]
print(f"  |Aut(decorated twelve)| = {len(auto)}  (identity only: {auto == [('P','U','I','R')]})")
flat, graded = 0, 0
for d, perm, surv in profile:
    if perm == ('P', 'U', 'I', 'R'): continue
    for g, tgt, tpl in surv:
        if tpl in ('div', 'mul'): flat += 1
        else: graded += 1
print(f"  surviving row-instances under non-identity relabelings: flat={flat}, graded={graded}")
print(f"  doc claim 'survivors exclusively on flat relations': {graded == 0}  (graded survivors exist: {graded})")
hit = defaultdict(set)
for d, perm, surv in profile:
    if perm == ('P', 'U', 'I', 'R'): continue
    for g, tgt, tpl in surv:
        hit[tgt].add(g)
unreachable = sorted(set(GATES) - set(hit))
print(f"  rows unreachable by ANY non-identity relabeling: {unreachable}")
print(f"    their modalities: {[(g, MODALITY[g]) for g in unreachable]}")
print(f"    their tiers: {[(g, GATES[g][7]) for g in unreachable]}")
print(f"  doc claim 'rigidity anchored entirely in COMMIT tier': "
      f"{all(GATES[g][7] == 1 for g in unreachable)}")

print("=" * 72)
print("CHECK 9 — ring audit (Sec VI)")
DOC_RINGS = {
    'Fixed-held':    ({'P', 'U', 'I', 'R'} & set(), {'ARI', 'VIR', 'GEM', 'CAP', 'CAN', 'SAG'}),
    'Cardinal-held': (set(), {'ARI', 'VIR', 'TAU', 'SCO', 'LEO', 'AQU'}),
    'Mutable-held':  (set(), {'GEM', 'CAP', 'TAU', 'SCO', 'LEO', 'AQU'}),
}
DOC_RINGS = {
    'Fixed-held':    (('P', 'U'), {'ARI', 'VIR', 'GEM', 'CAP', 'CAN', 'SAG'}),
    'Cardinal-held': (('P', 'R'), {'ARI', 'VIR', 'TAU', 'SCO', 'LEO', 'AQU'}),
    'Mutable-held':  (('P', 'I'), {'GEM', 'CAP', 'TAU', 'SCO', 'LEO', 'AQU'}),
}
reach = set()
for ring, (held_pair, doc_list) in DOC_RINGS.items():
    held_edge = frozenset(held_pair)
    muted_matching = MATCHING[held_edge]
    mate = [e for e in MATCHING if MATCHING[e] == muted_matching and e != held_edge][0]
    muted_edges = {held_edge, mate}
    live_edges = [e for e in MATCHING if e not in muted_edges]
    live_ops = set()
    for g, row in GATES.items():
        if frozenset([row[5], row[6]]) in live_edges:
            live_ops.add(g)
    missing = sorted(live_ops - set(doc_list))
    extra = sorted(set(doc_list) - live_ops)
    t2 = sorted(g for g in doc_list if GATES[g][7] == 2)
    print(f"  {ring:14s} mutes {muted_matching} matching {sorted(muted_edges)}")
    print(f"     live edges ({len(live_edges)}): {['-'.join(sorted(e)) for e in live_edges]}")
    print(f"     live opcodes ({len(live_ops)}): {sorted(live_ops)}")
    print(f"     doc lists {len(doc_list)}: missing={missing}  extra={extra}")
    print(f"     Tier-2 (RESEED) opcodes in doc list: {t2 if t2 else 'NONE'}")
    reach |= set(doc_list)
print(f"  opcodes reachable on SOME ring as documented: {sorted(reach)}")
print(f"  NEVER listed on any ring: {sorted(set(GATES) - reach)}")

print("=" * 72)
print("CHECK 10 — Register A/B semantics vs the 4-state table")
STATES = {'00': 'absent (void)', '01': 'bidirectional', '10': 'forward commit', '11': 'reverse commit'}
def test(convention):
    res = {}
    for code in STATES:
        b1, b0 = code[0], code[1]          # written bit1 bit0
        if convention == 'MSB-first':      # 'bit 0' = right symbol
            A, B = b0, b1
        else:                              # 'bit 0' = left symbol
            A, B = b1, b0
        res[code] = (A, B)
    return res
for conv in ('MSB-first', 'bit0-first'):
    r = test(conv)
    present = {c for c, (A, B) in r.items() if A == '1'}
    ok = present == {'01', '10', '11'}
    print(f"  convention {conv:10s}: '1=present' bit0 covers {sorted(present)} "
          f"-> Register A as Presence/Absence works: {ok}")
print("  corrected decomposition (left bit = commit, right bit = polarity):")
for code, name in STATES.items():
    commit, polarity = code[0], code[1]   # left symbol, right symbol (as printed)
    a = 'committed' if commit == '1' else 'uncommitted'
    b = {('0', '0'): 'polarity-0 (held-gap side)', ('0', '1'): 'polarity-1 (live-buffer side)',
         ('1', '0'): 'polarity-0 (forward side)', ('1', '1'): 'polarity-1 (reverse side)'}[(commit, polarity)]
    print(f"    {code} = {name:18s} = {a:12s} + {b}   OK")

print("=" * 72)
print("CHECK 10b — divisor census (the 'Die' row: 'Exclusively Reactive poles')")
div_by, exceptions = defaultdict(list), []
for g, (lhs, tpl, args, *_r) in GATES.items():
    if tpl in ('div', 'sq_div', 'sqrt_div', 'div_sq'):
        den = args[-1]
        div_by[den].append(g)
        if den not in REACTIVE:
            exceptions.append((g, den))
print(f"  divisors census: {dict(div_by)}")
print(f"  active poles in the Die (exceptions to the Die row): {exceptions}")
for g, den in exceptions:
    row = GATES[g]
    print(f"    {g}: divisor {den}, edge {row[5]}-{row[6]} ({MATCHING[frozenset([row[5], row[6]])]} matching)")

print("=" * 72)
print("CHECK 11 — modality vs edge-matching label collisions")
for g, row in GATES.items():
    em = MATCHING[frozenset([row[5], row[6]])]
    if em != MODALITY[g]:
        print(f"  {g}: gate modality = {MODALITY[g]}, edge matching = {em}  <-- label collision")

print("=" * 72)
print("CHECK 12 — arithmetic")
print(f"  2^12 = {2**12}   64*64 = {64*64}   2^3 = {2**3}   64*6 = {64*6}   32*12 = {32*12}")

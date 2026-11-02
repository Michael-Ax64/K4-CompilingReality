"""Exhaustive permutation check of the twelve decorated gates (L4-TheTwelveGates §II).

Question (On_HilbertAndHisSpaces §VIII): does any non-identity relabeling of the
four poles {P, U, I, R} carry the twelve equations into themselves?

Two criteria:
  BARE       : relabeled (lhs, template, args) is again one of the twelve equations.
  DECORATED  : BARE holds AND the row it lands on has the relabeled AbsentVar.

Templates:
  sq_div    : a^2 / b        (asymmetric: square pinned to first arg)
  sq_mul    : a^2 * b        (asymmetric)
  mul       : a * b          (symmetric)
  sqrt_div  : sqrt(a / b)    (asymmetric)
  div       : a / b          (asymmetric)
  sqrt_mul  : sqrt(a * b)    (symmetric)
  div_sq    : a / b^2        (asymmetric: square pinned to second arg)
"""

from itertools import permutations

POLES = ['P', 'U', 'I', 'R']
SYM = {'mul', 'sqrt_mul'}


def canon(lhs, tpl, args):
    if tpl in SYM:
        args = tuple(sorted(args))
    return (lhs, tpl, tuple(args))


# name, lhs, template, args, AbsentVar   (L4-TheTwelveGates §II, rows 123-134)
GATES = [
    ('ARI', 'P', 'sq_div',   ('U', 'R'), 'I'),
    ('TAU', 'P', 'sq_mul',   ('I', 'R'), 'U'),
    ('GEM', 'P', 'mul',      ('U', 'I'), 'R'),
    ('CAN', 'I', 'sqrt_div', ('P', 'R'), 'U'),
    ('LEO', 'I', 'div',      ('P', 'U'), 'R'),
    ('VIR', 'I', 'div',      ('U', 'R'), 'P'),
    ('LIB', 'U', 'div',      ('P', 'I'), 'R'),
    ('SCO', 'U', 'mul',      ('I', 'R'), 'P'),
    ('SAG', 'U', 'sqrt_mul', ('P', 'R'), 'I'),
    ('CAP', 'R', 'div',      ('U', 'I'), 'P'),
    ('AQU', 'R', 'sq_div',   ('U', 'P'), 'I'),
    ('PIS', 'R', 'div_sq',   ('P', 'I'), 'U'),
]

# sanity: Home == lhs for every row (so Home adds nothing beyond lhs)
for name, lhs, tpl, args, av in GATES:
    assert lhs == {'ARI': 'P', 'TAU': 'P', 'GEM': 'P', 'CAN': 'I', 'LEO': 'I',
                   'VIR': 'I', 'LIB': 'U', 'SCO': 'U', 'SAG': 'U', 'CAP': 'R',
                   'AQU': 'R', 'PIS': 'R'}[name], name

BARE = {canon(l, t, a) for _, l, t, a, _ in GATES}
DECO = {canon(l, t, a): av for _, l, t, a, av in GATES}
assert len(DECO) == 12, "equation -> AbsentVar must be well defined"


def apply_perm(eq, mapping):
    lhs, tpl, args = eq
    return canon(mapping[lhs], tpl, tuple(mapping[a] for a in args))


print("=== survival profile over all 24 permutations ===")
profile = []
for perm in permutations(POLES):
    mapping = dict(zip(POLES, perm))
    bare_hits, deco_hits, details = 0, 0, []
    for name, lhs, tpl, args, av in GATES:
        rel = apply_perm(canon(lhs, tpl, args), mapping)
        r_av = mapping[av]
        if rel in BARE:
            bare_hits += 1
        if rel in DECO and DECO[rel] == r_av:
            deco_hits += 1
            target = [g[0] for g in GATES if canon(g[1], g[2], g[3]) == rel][0]
            details.append(f"{name}->{target}" if target != name else f"{name} self")
    profile.append((deco_hits, bare_hits, ''.join(perm), details))

profile.sort(key=lambda x: (-x[0], -x[1]))
for d, b, perm, det in profile:
    tag = "  <== automorphism" if d == 12 else ""
    print(f"σ = {perm}   bare {b:2d}/12   decorated {d:2d}/12   {', '.join(det) if det else '-'}{tag}")

n_auto = sum(1 for d, _, _, _ in profile if d == 12)
print(f"\n|Aut(decorated twelve)| = {n_auto}   (L3-EdgeStateSpace §I-d claims 1)")

print("\n=== the three swaps cited in On_HilbertAndHisSpaces §VIII ===")
cases = [
    ("swap 1: P<->R on Facet 2 (TAU, P = I^2*R)", {'P': 'R', 'R': 'P', 'U': 'U', 'I': 'I'}, 'TAU'),
    ("swap 2: U<->I on Facet 5 (LEO, I = P/U)",   {'U': 'I', 'I': 'U', 'P': 'P', 'R': 'R'}, 'LEO'),
    ("swap 3: P<->U on Facet 9 (SAG, U = sqrt(P*R))", {'P': 'U', 'U': 'P', 'I': 'I', 'R': 'R'}, 'SAG'),
]
for label, mapping, gname in cases:
    g = [g for g in GATES if g[0] == gname][0]
    rel = apply_perm(canon(g[1], g[2], g[3]), mapping)
    in_table = rel in BARE
    lands = [g2[0] for g2 in GATES if canon(g2[1], g2[2], g2[3]) == rel] if in_table else []
    verdict = f"relabeled equation IS in the table (lands on {lands})" if in_table \
        else "relabeled equation is NOT in the table (fails, as the text claims)"
    print(f"{label}\n   -> {rel}   {verdict}")

print("\n=== which forms carry the rigidity? survivors by template ===")
from collections import Counter
c = Counter()
for d, b, perm, det in profile:
    if perm == ''.join(POLES):
        continue
    mapping = dict(zip(POLES, perm))
    for name, lhs, tpl, args, av in GATES:
        rel = apply_perm(canon(lhs, tpl, args), mapping)
        if rel in DECO and DECO[rel] == mapping[av]:
            c[tpl] += 1
print("surviving row-instances by template (non-identity permutations):", dict(c))
flat, graded = c.get('div', 0) + c.get('mul', 0), sum(v for k, v in c.items() if k not in ('div', 'mul'))
print(f"flat forms (div, mul): {flat}    graded forms (squares/roots): {graded}")

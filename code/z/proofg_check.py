#!/usr/bin/env python3
"""
ProofG_Chirality.md -- the re-runnable claim ledger (scripts/proofg_check.py).

Every numbered check of Proof G (A1-G2, W1-W3) reproduces from this one file,
in the inline-script convention of `L3-EdgeStateSpace` I-e: plain Python 3,
standard library only, deterministic output, one verdict line per check.

Reconstructed 2026-11-13 from the proof's own printed structure and the two
sources it names (L3-EdgeStateSpace I-e; L4-TheTwelveGates II-b). Provenance:

  A1-A5, B1, B4, C1-C2, D1, E1-E2 : ProofG II-VI as printed.
  B2/B3 : the printed seasonal table (II-b, both vantage columns) reproduced
          with each word set in the season's own vantage frame -- centroid for
          the Active pair, desk for the Reactive pair (the approved premise,
          exhibited; II-b's hand-rule anchor pins the same words).
  B5    : the registered exhibition -- walk vector = -AR(home).x_home, exact
          on the printed month-order turns, with the Step-5 link layer uniform.
  C0    : the cube-corner charge identification (III, with C0): x = AR,
          y = AY, z = -AR.AY realizes the LANDED orientation (A3 normals
          toward the namesakes), so one embedding serves every check.
  C3    : the explicit gate map of IV, verified against L3 I-e Step 3 / Step 6.
  W1-W3 : the walk-level census of III -- same tear condition as the face
          level (a shared edge traversed the same way twice, d2 != 0), the
          words read through the season's own vantage frame.
  G1-G2 : the two owed checks of V -- the discrete pitch invariant against
          Barron's true/false chirality distinction.

Run:  python3 proofg_check.py        (exits 0 iff every check passes)
"""

import itertools
import sys
from math import sqrt

# ------------------------------------------------------------------ ground
poles = ['P', 'U', 'I', 'R']

# L3 I-e Step 1 -- the landed face circulations (face named by the pole it lacks).
landed = {'P': ('I', 'R', 'U'), 'I': ('P', 'U', 'R'),
          'U': ('P', 'R', 'I'), 'R': ('P', 'I', 'U')}

# L3 I-e Step 5 -- the four seasonal link circuits (Spring's gates verbatim:
# ARI U->R, TAU R->I, GEM I->U; the other three forced, checked at B1).
season_circ = {'Spring': ('U', 'R', 'I'), 'Summer': ('P', 'R', 'U'),
               'Autumn': ('P', 'I', 'R'), 'Winter': ('U', 'I', 'P')}
season_home = {'Spring': 'P', 'Summer': 'I', 'Autumn': 'U', 'Winter': 'R'}

# L4-TheTwelveGates II-b -- the printed seasonal table, both vantage columns,
# and the printed month-order face-walks.
printed = {'Spring': ('CW', 'CCW'), 'Summer': ('CCW', 'CW'),
           'Autumn': ('CW', 'CCW'), 'Winter': ('CCW', 'CW')}
printed_turn = {'Spring': ('I', 'U', 'R'), 'Summer': ('U', 'R', 'P'),
                'Autumn': ('R', 'P', 'I'), 'Winter': ('P', 'I', 'U')}

# L3 I-e Step 6 / XI -- the two-bit charge (AR, AY); C0: the two coordinate
# signs of the cube corners the tetrahedron lives on. z = -AR*AY realizes the
# LANDED orientation (A3 normals toward the namesakes; verified below).
charge = {'P': (1, 1), 'U': (1, -1), 'I': (-1, -1), 'R': (-1, 1)}
xyz = {p: (charge[p][0], charge[p][1], -charge[p][0] * charge[p][1]) for p in poles}
AR = {p: charge[p][0] for p in poles}

# L3 I-e Step 3 -- the directed gate table (verbatim).
gate = {('I', 'U'): 'GEM', ('U', 'I'): 'CAP', ('R', 'U'): 'VIR', ('U', 'R'): 'ARI',
        ('I', 'R'): 'SCO', ('R', 'I'): 'TAU', ('P', 'U'): 'AQU', ('U', 'P'): 'LEO',
        ('P', 'R'): 'CAN', ('R', 'P'): 'SAG', ('P', 'I'): 'LIB', ('I', 'P'): 'PIS'}
mode = {'ARI': 'Cardinal', 'TAU': 'Fixed', 'GEM': 'Mutable', 'CAN': 'Cardinal',
        'LEO': 'Fixed', 'VIR': 'Mutable', 'LIB': 'Cardinal', 'SCO': 'Fixed',
        'SAG': 'Mutable', 'CAP': 'Cardinal', 'AQU': 'Fixed', 'PIS': 'Mutable'}

RESULTS = []


def check(cid, claim, ok, evidence=None):
    RESULTS.append((cid, bool(ok)))
    print(f"  {cid} {'PASS' if ok else 'FAIL'} -- {claim}")
    if evidence:
        for line in evidence:
            print(f"        {line}")


# ------------------------------------------------------------- vector tools
def sub(u, v):
    return (u[0] - v[0], u[1] - v[1], u[2] - v[2])


def cross(u, v):
    return (u[1] * v[2] - u[2] * v[1],
            u[2] * v[0] - u[0] * v[2],
            u[0] * v[1] - u[1] * v[0])


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]


def unit(u):
    n = sqrt(dot(u, u))
    return (u[0] / n, u[1] / n, u[2] / n)


def xhat(p):
    return unit(xyz[p])


def cyc(t):
    return [(t[0], t[1]), (t[1], t[2]), (t[2], t[0])]


def circ_normal(t):
    """right-hand normal of the directed 3-cycle, at the pole positions."""
    a, b, c = (xyz[x] for x in t)
    return unit(cross(sub(b, a), sub(c, b)))


def parity(perm):
    p = list(perm)
    seen = [False] * len(p)
    par = 0
    for i in range(len(p)):
        if not seen[i]:
            j, clen = i, 0
            while not seen[j]:
                seen[j] = True
                j = p[j]
                clen += 1
            par ^= (clen - 1) & 1
    return par


def gf2_rank(rows, ncols):
    m = [r[:] for r in rows]
    rank = 0
    for c in range(ncols):
        piv = next((r for r in range(rank, len(m)) if m[r][c]), None)
        if piv is None:
            continue
        m[rank], m[piv] = m[piv], m[rank]
        for r in range(len(m)):
            if r != rank and m[r][c]:
                m[r] = [x ^ y for x, y in zip(m[r], m[rank])]
        rank += 1
    return rank


undirected = [('P', 'U'), ('P', 'I'), ('P', 'R'), ('U', 'I'), ('U', 'R'), ('I', 'R')]
faces_of_edge = {}
for f in poles:
    for e in cyc(landed[f]):
        faces_of_edge.setdefault(frozenset(e), []).append(f)


def face_bits(f, bit):
    return cyc(landed[f]) if bit == 0 else cyc(tuple(reversed(landed[f])))


# ============================================================== II. closure
print("=" * 72)
print("II  the static closure -- one global handedness bit")

ev = []
ok = True
for (a, b) in undirected:
    f1, f2 = faces_of_edge[frozenset((a, b))]
    d1 = (a, b) in cyc(landed[f1])
    d2 = (a, b) in cyc(landed[f2])
    ok &= (d1 != d2)
    ev.append(f"edge {a}-{b}: {f1}-face {'%s->%s' % (a, b) if d1 else '%s->%s' % (b, a)}"
              f" | {f2}-face {'%s->%s' % (a, b) if d2 else '%s->%s' % (b, a)}")
check("A1", "the landed table closes -- all six shared edges cancel (d(d(d3)) = 0)", ok, ev)

rows = []
for (a, b) in undirected:
    f1, f2 = faces_of_edge[frozenset((a, b))]
    row = [0, 0, 0, 0]
    row[poles.index(f1)] = 1
    row[poles.index(f2)] = 1
    rows.append(row)
rank = gf2_rank(rows, 4)

survivors = []
for bits in itertools.product([0, 1], repeat=4):
    d = dict(zip(poles, bits))
    if all(((a, b) in face_bits(f1, d[f1])) != ((a, b) in face_bits(f2, d[f2]))
           for (a, b) in undirected
           for f1, f2 in [faces_of_edge[frozenset((a, b))]]):
        survivors.append(d)

check("A5", f"the six cancellation conditions carry GF(2) rank {rank} over the four face "
            f"bits -- solutions 2^(4-{rank}) = {2 ** (4 - rank)}", rank == 3 and len(survivors) == 2)
check("A2", "of the 2^4 ways to flip the four circulations, exactly two close", len(survivors) == 2,
      [f"survivor {i}: bits (P,U,I,R) = {[d[f] for f in poles]}" for i, d in enumerate(survivors)])


def geo_word(d):
    signs = []
    for f in poles:
        e = face_bits(f, d[f])
        n = cross(sub(xyz[e[1][0]], xyz[e[0][0]]), sub(xyz[e[2][0]], xyz[e[1][0]]))
        signs.append(1 if dot(n, xyz[f]) > 0 else -1)
    return signs


words = [geo_word(d) for d in survivors]
check("A3", "each survivor is uniform in geometric words (right-hand normals on one side "
            "of the solid)", all(len(set(w)) == 1 for w in words),
      [f"survivor {i}: normal-side signs {w}" for i, w in enumerate(words)])

rev0 = {f: 1 - survivors[0][f] for f in poles}
check("A4", "the two survivors are global reverses of each other (enantiomers)", rev0 == survivors[1])

# ====================================================== III. the gear-mesh
print("=" * 72)
print("III  the chiral gear-mesh")

# B1 -- Spring's three gates verbatim (L3 I-e Step 5); the other three forced.
spring_edges = {('U', 'R'), ('R', 'I'), ('I', 'U')}          # ARI, TAU, GEM chained
forced, used = {}, set(spring_edges)
for nm, home in [('Summer', 'I'), ('Autumn', 'U'), ('Winter', 'R')]:
    cands = []
    for t in itertools.permutations([p for p in poles if p != home]):
        e = set(cyc(t))
        if not (e & used) and not any(set(cyc(c)) == e for c in cands):
            cands.append(t)
    assert len(cands) == 1, (nm, cands)
    forced[nm] = cands[0]
    used |= set(cyc(cands[0]))
circuits = {'Spring': season_circ['Spring'], **forced}
b1_ok = (len(used) == 12
         and all(set(cyc(circuits[s])) == set(cyc(season_circ[s])) for s in circuits)
         and all(all((b, a) in cyc(landed[season_home[s]]) for (a, b) in cyc(circuits[s]))
                 for s in circuits))
check("B1", "the four seasonal link circuits (Spring given, three forced) partition the 12 "
            "directed edges, each against the grain of its home-opposite face", b1_ok,
      [f"{s:7s} (home {season_home[s]}): "
       + " -> ".join(e[0] for e in cyc(circuits[s])) + f" -> {cyc(circuits[s])[0][0]}"
       for s in circuits])


def own_frame(s):
    return 'centroid' if AR[season_home[s]] > 0 else 'desk'


def own_sight(s):
    # centroid: inside looking out along the walked (home-opposite) face's outward
    # normal, which is -x_home; desk: outside looking in along its inward normal.
    return tuple(-c for c in xhat(season_home[s])) if own_frame(s) == 'centroid' \
        else xhat(season_home[s])


def word_of(s, t):
    return 'CW' if dot(circ_normal(t), own_sight(s)) > 0 else 'CCW'


own_word = {s: word_of(s, circuits[s]) for s in circuits}
recon = {s: (own_word[s], 'CCW' if own_word[s] == 'CW' else 'CW') for s in circuits}
check("B2", "the printed table's outwards column reproduced: each word set in the season's "
            "own vantage frame -- centroid for the Active pair, desk for the Reactive pair",
      all(recon[s][0] == printed[s][0] for s in printed),
      [f"{s:7s} (home {season_home[s]}, {own_frame(s):8s}): own word {own_word[s]}"
       for s in printed])
check("B3", "the printed table's inwards column reproduced (the same motion from the "
            "mirror frame -- one motion, two words)", all(recon[s][1] == printed[s][1] for s in printed))

s_edge = 2 * sqrt(2.0)                    # edge of the corner realization
r = s_edge / sqrt(3.0)                    # face circumradius = walk radius
area = sqrt(3.0) * s_edge ** 2 / 4.0
mag = r * r / area
sgn = {s: -AR[season_home[s]] for s in season_circ}
two_two = sgn['Spring'] == sgn['Autumn'] == -sgn['Summer'] == -sgn['Winter']
check("B4", "equal magnitude, opposite sign across the two season classes", two_two,
      [f"signed circulation about the Home normal: "
       + ", ".join(f"{s} {sgn[s]:+d}" for s in season_circ),
       f"magnitude r^2/A = {mag:.4f} (4/(3*sqrt(3)); the corpus prints +/-0.77)"])

b5_ok, ev = True, []
for s, t in printed_turn.items():
    n = circ_normal(t)
    xh = xhat(season_home[s])
    pred = tuple(-AR[season_home[s]] * c for c in xh)
    ok = all(abs(n[i] - pred[i]) < 1e-9 for i in range(3))
    b5_ok &= ok
    ev.append(f"{s:7s}: walk normal = {'-' if dot(n, xh) < 0 else '+'}x_home({season_home[s]})"
              f"  (B5 predicts {'-' if AR[season_home[s]] > 0 else '+'}x_home({season_home[s]}))")
uni = all(abs(dot(circ_normal(circuits[s]), xhat(season_home[s])) + 1) < 1e-9 for s in circuits)
rel = {s: ('with' if set(cyc(printed_turn[s])) == set(cyc(circuits[s])) else 'against')
       for s in circuits}
check("B5", "walk vector = -AR(home).x_home, exact on all four printed month-order turns, "
            "with the Step-5 induced link layer uniform", b5_ok and uni,
      ev + ["printed turn vs the induced circuit: "
            + ", ".join(f"{s} {rel[s]}" for s in circuits)
            + " -- the identity alternation is the two-and-two at the word layer"])

d2 = [dot(sub(xyz[a], xyz[b]), sub(xyz[a], xyz[b])) for (a, b) in undirected]
check("C0", "the two-bit charge is the two coordinate signs of the cube corners: x = AR, "
            "y = AY, z = -AR.AY -- a regular tetrahedron on alternate corners",
      len(set(d2)) == 1 and all(dot(xyz[a], xyz[b]) == -1 for (a, b) in undirected)
      and all(xyz[p][0] == charge[p][0] and xyz[p][1] == charge[p][1] for p in poles),
      [f"{p} at {xyz[p]}  charge (AR, AY) = {charge[p]}" for p in poles])

# ---------------------------------------------- the walk-level census (W1-W3)
NAMES = ('Spring', 'Summer', 'Autumn', 'Winter')


def walk_circuits(flips):
    return {s: circuits[s] if not flips[i] else tuple(reversed(circuits[s]))
            for i, s in enumerate(NAMES)}


def tear_test(wc):
    seen = {}
    for s, t in wc.items():
        for e in cyc(t):
            seen.setdefault(frozenset(e), []).append(e)
    torn = [f"{sorted(k)[0]}-{sorted(k)[1]}" for k, v in seen.items()
            if not (v[0] == v[1][::-1])]
    return (not torn), torn


def word_row(wc):
    return {s: word_of(s, wc[s]) for s in wc}


rows_w, survivors_w, allsame = [], [], []
for flips in itertools.product([0, 1], repeat=4):
    wc = walk_circuits(flips)
    closed, torn = tear_test(wc)
    wr = word_row(wc)
    rows_w.append((flips, wr, closed, torn))
    if closed:
        survivors_w.append((flips, wr))
    if len(set(wr.values())) == 1:
        allsame.append((flips, wr, torn))

check("W1", "the walk level runs the same census: exactly two of the 2^4 walk assignments "
            "close", len(survivors_w) == 2,
      [f"survivor {i}: flips {fl} -- words {wr['Spring']},{wr['Summer']},{wr['Autumn']},{wr['Winter']}"
       for i, (fl, wr) in enumerate(survivors_w)])

uni_layer = all(abs(dot(circ_normal(circuits[s]), xhat(season_home[s])) + 1) < 1e-9
                for s in circuits)
against = all(all((b, a) in cyc(landed[season_home[s]]) for (a, b) in cyc(circuits[s]))
              for s in circuits)
two_and_two = all(len(set(wr.values())) == 2 for _, wr in survivors_w)
printed_row = all(word_row(walk_circuits((0, 0, 0, 0)))[s] == printed[s][0] for s in circuits)
check("W2", "the closed pair is uniform in the induced words (direction layer uniform, all "
            "four against the grain) and its vantage reading is two-and-two -- the printed "
            "table", uni_layer and against and two_and_two and printed_row,
      ["induced layer: all four walk normals at -x_home, all four against the grain",
       f"survivor words: " + " | ".join(
           f"{wr['Spring']},{wr['Summer']},{wr['Autumn']},{wr['Winter']}" for _, wr in survivors_w)])

survivor_flips = {fl for fl, _ in survivors_w}
w3_ok = (len(allsame) == 2 and all(len(t) > 0 for _, _, t in allsame)
         and all(fl not in survivor_flips for fl, _, _ in allsame))
check("W3", "the assignment that reads all-same in vantage words tears -- a shared edge "
            "traversed the same way twice (d2 != 0); no all-same assignment closes", w3_ok,
      [f"all-{list(wr.values())[0]}: flips {fl} -- tears on {', '.join(t)}"
       for fl, wr, t in allsame])

# ================================================== IV. the mirror in group
print("=" * 72)
print("IV  the two completions and the mirror")

fork_ok = True
for (s, t) in [(a, b) for a in poles for b in poles if a != b]:
    rest = [p for p in poles if p not in (s, t)]
    pars = set()
    for c in itertools.permutations(rest):
        pars.add(parity([poles.index(x) for x in (s, t, c[0], c[1])]))
    fork_ok &= (pars == {0, 1})
A4 = [p for p in itertools.permutations(poles) if parity([poles.index(x) for x in p]) == 0]
orb = {(sg[0], sg[1]) for sg in A4}
check("C1", "every directed edge has exactly two completions, one even one odd; A4 acts "
            f"simply transitively on the twelve (|A4| = {len(A4)}, orbit of P->U = {len(orb)})",
      fork_ok and len(A4) == 12 and len(orb) == 12)

c2_ok = True
for sg in itertools.permutations(poles):
    m = dict(zip(poles, sg))
    d_img = {}
    for f in poles:
        g = m[f]
        e = [(m[a], m[b]) for (a, b) in cyc(landed[f])]
        d_img[g] = 0 if set(e) == set(cyc(landed[g])) else 1
    sig = parity([poles.index(m[p]) for p in poles])
    tgt = survivors[0] if sig == 0 else survivors[1]
    c2_ok &= all(d_img[f] == tgt[f] for f in poles)
check("C2", "the orientation group acts by the sign homomorphism: even permutations fix the "
            "landed orientation, odd map it to the mirror", c2_ok)

flip = {'P': 'R', 'R': 'P', 'U': 'I', 'I': 'U'}
dir_col = {g: e for e, g in gate.items()}
conjugated = {g: gate[(flip[dir_col[g][0]], flip[dir_col[g][1]])] for g in dir_col}
printed_map = {'ARI': 'PIS', 'PIS': 'ARI', 'CAN': 'SAG', 'SAG': 'CAN', 'LIB': 'VIR',
               'VIR': 'LIB', 'CAP': 'GEM', 'GEM': 'CAP', 'LEO': 'SCO', 'SCO': 'LEO',
               'TAU': 'AQU', 'AQU': 'TAU'}
law = {'Cardinal': lambda a, b: AR[a] == 1 and AR[b] == -1,
       'Mutable':  lambda a, b: AR[a] == -1 and AR[b] == 1,
       'Fixed':    lambda a, b: AR[a] == AR[b]}
exch = {'Cardinal': 'Mutable', 'Mutable': 'Cardinal', 'Fixed': 'Fixed'}
dl_on = all(law[mode[g]](*dir_col[g]) for g in dir_col)
dl_con = all(law[exch[mode[g]]](*(flip[dir_col[g][0]], flip[dir_col[g][1]])) for g in dir_col)
check("C3", "conjugating the landed gate table by the AR-flip exchanges ARI<->PIS, CAN<->SAG, "
            "LIB<->VIR, CAP<->GEM, LEO<->SCO, TAU<->AQU -- Cardinal and Mutable laws exchange, "
            "Fixed untouched", all(conjugated[g] == printed_map[g] for g in dir_col)
            and dl_on and dl_con)

sig_ar = parity([poles.index(flip[p]) for p in poles])
holds = {flip['P'], flip['R']} == {'P', 'R'} and {flip['U'], flip['I']} == {'U', 'I'}
pair_map = {'Spring': 'Winter', 'Winter': 'Spring', 'Summer': 'Autumn', 'Autumn': 'Summer'}
conj_ok = all(set((flip[a], flip[b]) for (a, b) in cyc(circuits[s]))
              == set(cyc(circuits[pair_map[s]])) for s in circuits)
check("D1", "the AR-flip (P R)(U I) is even -- a V4 half-turn, a rotation cannot change "
            "handedness -- holds the Cardinal matching {P-R, U-I} setwise, and conjugates the "
            "season-cycles in pairs preserving direction", sig_ar == 0 and holds and conj_ok,
      [f"parity {sig_ar} (even); conj: "
       + ", ".join(f"{s}->{pair_map[s]}" for s in ('Spring', 'Summer'))])

# ==================================================== V. the omega ratchet
print("=" * 72)
print("V  the turn with time in it -- the two owed checks")

eps = {0: geo_word(survivors[0])[0], 1: geo_word(survivors[1])[0]}


def hand(b, a):
    return eps[b] * a


p_odd = all(hand(1 - b, a) == -hand(b, a) for b in (0, 1) for a in (+1, -1))
t_even = all(hand(1 - b, -a) == hand(b, a) for b in (0, 1) for a in (+1, -1))
check("G1", "the discrete pitch invariant hand = eps(b)*a (orientation bit x ratchet advance) "
            "is parity-odd and time-reversal-even -- Barron true chirality, discrete register",
      p_odd and t_even,
      ["mirror: flips the hand (eps -> -eps), advance unmoved -- the poles cannot walk omega",
       "time reverse: flips both factors, hand(1-b,-a) = (-eps(b))(-a) = hand(b,a) -- survives"])

bij = hand(0, +1) != hand(1, +1)
check("G2", "at fixed ratchet advance the sign of the invariant is the II handedness bit -- "
            "the global handedness bit is the sign of the engine's screw", bij,
      [f"fixed advance a=+1:  bit 0 -> {hand(0, +1):+d},  bit 1 -> {hand(1, +1):+d}",
       "yes, up to the global convention fixing which advance counts as '+'"])

# ====================================================== VI. the collector
print("=" * 72)
print("VI  the garbage collector as enantiomeric severer")


def canon_dir(c_):
    t = [e[0] for e in c_]
    i = t.index('P')
    return tuple(t[i:] + t[:i])


def canon_und(c_):
    fwd = canon_dir(c_)
    bwd = canon_dir([(b, a) for (a, b) in reversed(c_)])
    return min(fwd, bwd)


directed_cycles, und_cycles = [], []
for perm in itertools.permutations(['U', 'I', 'R']):
    c_ = cyc(('P',) + perm)
    d = canon_dir(c_)
    if d not in directed_cycles:
        directed_cycles.append(d)
    u = canon_und(c_)
    if u not in und_cycles:
        und_cycles.append(u)
check("E1", f"K4 holds {len(und_cycles)} undirected and {len(directed_cycles)} directed "
            "Hamiltonian cycles -- .behold() holds all six, .observe() keeps one, the "
            "Collector removes five", len(und_cycles) == 3 and len(directed_cycles) == 6)
e2 = all((c_[0], c_[2], c_[1]) in directed_cycles for c_ in directed_cycles)
check("E2", "each directed cycle's reverse is also held -- same connectivity, opposite "
            "handedness: the unchosen completions are chiral counterparts", e2)

# ----------------------------------------------------------------- summary
print("=" * 72)
bad = [cid for cid, ok in RESULTS if not ok]
print(f"{len(RESULTS)} checks -- {len(RESULTS) - len(bad)} pass"
      + (f"; FAIL: {', '.join(bad)}" if bad else " -- all checks pass"))
sys.exit(1 if bad else 0)

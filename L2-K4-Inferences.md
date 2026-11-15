# L2: K4 Inference
## Finding the Tetrahedron a Claim Lives On

*Developed from the Compiling Reality framework and the Algebra of Four-Fold Distinction. Reads with `L2-K4-InteriorStructure` (the secretaries, the centroid as the one unbound point), `L3-EdgeStateSpace` (the bimedians and their half-turns), `ENGINE-REFERENCE-AC` (tiers, strain invariance), `ProofQ_AlgebraicSyntax` (the three squarings), `L4-DynamicDistortions301` (the dipoles, the burned term), `Q14-LeptonScaleCascade` and `ENGINE-REFERENCE-AC` §VII (the cycle), `L2-Terminology` (`.behold()`), and `llm/llm-stance-laugh-detector.md` (the baseline step). Owns the inference procedure of Part One and its worked specimen, the tetrahedron of the Riemann zeros; cite those here.*

*This file is written as a literate construction. The code blocks, read top to bottom, are one program, and the prose between them is the reasoning that chose each line. Nothing is asserted about the specimen that a block does not return.*

---

## The Task

A claim arrives alone. It is famous, it is hard, and whole schools have formed around it. K4 inference asks which tetrahedron the claim lives on, where on that tetrahedron it sits, and what is at the centroid.

Two objects answer those questions, and they share one symmetry group. The procedure keeps them apart.

The first is the **orbit tetrahedron**. Take one point off every axis of symmetry and apply every move the object allows. Four points appear. Lifted into space they are the four vertices of a tetrahedron, and the three moves are its three bimedian half-turns. Each half-turn exchanges the vertices in pairs and fixes none of them.

The second is the **ground the orbit stands on**: the space sorted by which moves hold a point still. That sorting gives one open bulk, three axes, and one centre. The three axes are the fixed lines of the three moves. The centre is where they cross.

A claim can sit at any of these addresses, or at none. The procedure does not assume it is a vertex. For the specimen it turns out to be no place at all. It is one stroke of a cycle that is running: a collapse, with a hold before it and a reseed after it. Part Four walks that cycle.

The procedure has seven steps. Each step is a choice, each choice has a reason, and each can come back empty. A step that comes back empty is a result and is printed with the rest.

The specimen carried through the construction is the Riemann Hypothesis: every non-trivial zero of $\zeta$ has real part $\tfrac12$. The specimen is light. The procedure is the subject of Part One, what it found is the subject of Parts Two and Three, and Part Four is the look at the specimen that the centroid makes possible: the cycle the collapse is one stroke of.

---

# Part One: The Construction

## 1. Baseline before anything

The first choice is what the work will not claim. `llm/llm-stance-laugh-detector.md` owns this step (expect there: Step 0, the layer of the work is fixed before any finding). The layer here is meta-of-domain. The procedure describes the shape of the space a claim lives in. It makes no claim inside analytic number theory, and nothing below bears on whether the Riemann Hypothesis is true.

That choice costs something and buys something. It costs every sentence of the form "therefore the hypothesis holds". It buys the right to use only what is already proved about the specimen, so that every block below runs on theorems and arithmetic.

## 2. The moves come first

The tempting first step is to list the schools that work on the claim. That is the wrong end. Schools are bound to vocabularies, and vocabularies do not line up. The object's own symmetries do. So the first block names what the object lets you do to it and leaves it itself.

The symmetric object has to be named exactly. Raw $\zeta$ does not carry the full symmetry: it vanishes at $-2, -4, -6, \dots$ and does not vanish at their partners $3, 5, 7, \dots$ under $s \to 1-s$. The completed function does:

$$\xi(s) = \tfrac12\,s(s-1)\,\pi^{-s/2}\,\Gamma(s/2)\,\zeta(s).$$

Its zeros are exactly the non-trivial zeros of $\zeta$. It is real on the real axis, so its zeros come in conjugate pairs, and it satisfies $\xi(s) = \xi(1-s)$ everywhere. The Euler product keeps zeros out of $\sigma > 1$, the functional equation then keeps them out of $\sigma < 0$, and every zero of $\xi$ lies in the strip between. With the centre moved to the origin, $x = \sigma - \tfrac12$ and $y = \gamma$:

```python
from fractions import Fraction as Fr
c  = lambda p: ( p[0], -p[1])      # conjugation:            s -> conj(s)
f  = lambda p: (-p[0], -p[1])      # functional equation:    s -> 1 - s
cf = lambda p: (-p[0],  p[1])      # reflection in the line: s -> 1 - conj(s)
e  = lambda p: p
G  = {'e': e, 'c': c, 'f': f, 'cf': cf}
pts = [(Fr(a), Fr(b)) for a in (-1, 0, 1) for b in (-2, 0, 3)]
closed = all(any(G[a](G[b](p)) == G[k](p) for k in G) for a in G for b in G for p in pts)
squares = all(G[k](G[k](p)) == p for k in G for p in pts)
print('2  four moves, closed:', closed, '| every move its own inverse:', squares)
```

Four moves, closed, each its own inverse: the Klein four-group. That is already a K4 fact, because the engine knows this group as the three half-turns about the bimedians (`L3-EdgeStateSpace` §I-c; expect there: the three double transpositions acting as half-turns about the three bimedian axes). The block does not yet say the two groups act the same way. Step 5 tests that.

Any two of the three moves give the third. A school that owns one move and borrows a second has the whole group. This matters in Part Two.

## 3. Sort by what holds still

The second choice is how to find the addresses a claim can sit at. The procedure does not look for them among statements. It sorts the points of the space by which moves fix them, because a move that fixes a point is a constraint that point satisfies.

```python
orbit = lambda p: {g(p) for g in G.values()}
stab  = lambda p: tuple(sorted(k for k in G if k != 'e' and G[k](p) == p))
census = {}
for p in pts: census.setdefault(stab(p), set()).add(len(orbit(p)))
for s, sizes in sorted(census.items(), key=lambda kv: len(kv[0])): print('3  fixed by', s, '-> orbit size', sorted(sizes))
```

Four classes come back. A point fixed by nothing lies in the open bulk and has an orbit of four. A point fixed by conjugation sits on the real axis, in an orbit of two. A point fixed by the line-reflection sits on the critical line, in an orbit of two. A point fixed by everything is the centre, alone.

The group has five subgroups and the plane shows four classes. One is missing: the points fixed by the functional equation and nothing else. In the plane, being fixed by $s \to 1-s$ forces being fixed by all three. The census reports an absence, and the procedure keeps it. Step 5 finds where it went.

## 4. The centroid is what nothing moves

The third choice is the definition of the centroid, and it is borrowed whole. `L2-K4-InteriorStructure` §V.8.e owns it (expect there: the centroid as the one point every symmetry of the scale fixes; every vertex, edge and face moved by some symmetry). The procedure does not ask what the schools agree on. It asks what the moves cannot touch.

```python
mean = lambda S: tuple(sum(q[k] for q in S) / len(S) for k in range(2))
print('4  centroid of every orbit:', {mean(orbit(p)) for p in pts} == {(0, 0)},
      '| points fixed by all moves:', [p for p in pts if len(orbit(p)) == 1])
```

Every orbit balances on one point, $s = \tfrac12$. This holds for every orbit, including any that the hypothesis says cannot occur. The centroid is settled before the claim is.

## 5. Does the tetrahedron have volume?

An orbit of four in a plane is a rectangle. A rectangle is a flat thing, and K4 inference needs to know whether the flatness belongs to the object or to the view. So the fourth choice is a lift: a third coordinate $z$ for each point.

The lift is not free. The bimedian half-turns are rotations. For the plane's three moves to become rotations in space, each must act with determinant $+1$. Conjugation and the line-reflection each flip one plane coordinate, so each must also flip $z$. The functional equation flips both plane coordinates, so it must leave $z$ alone. The third coordinate is therefore odd under $c$, odd under $cf$, and even under $f$. That requirement is the test, and three candidates take it.

```python
def vol(P):
    a, u, v, w = P[0], *[[q[k] - P[0][k] for k in range(3)] for q in P[1:]]
    return abs(u[0]*(v[1]*w[2]-v[2]*w[1]) - u[1]*(v[0]*w[2]-v[2]*w[0]) + u[2]*(v[0]*w[1]-v[1]*w[0])) / 6
lift = lambda p: (p[0], p[1], p[0] * p[1])               # z = x*y: odd under c, odd under cf, even under f
x, y = Fr(1, 4), Fr(14)                                  # a hypothetical point in the bulk
quad = [(x, y), c((x, y)), f((x, y)), cf((x, y))]
flat   = [(p[0], p[1], Fr(0)) for p in quad]             # no lift
twist  = [(p[0], p[1], Fr(s)) for p, s in zip(quad, (1, -1, -1, 1))]   # z = which of chi, chi-bar: c and f swap them
saddle = [lift(p) for p in quad]
print('5  volume  flat:', vol(flat), '| character twist:', vol(twist), '| saddle z = xy:', vol(saddle), '=', Fr(8, 3) * (x*y)**2)
tet = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
half_turns = [lambda q: (q[0], -q[1], -q[2]), lambda q: (-q[0], q[1], -q[2]), lambda q: (-q[0], -q[1], q[2])]
print('5  regular tetrahedron on z = xy:', all(q[2] == q[0]*q[1] for q in tet),
      '| saddle orbit = orbit under the three half-turns:', set(saddle) == {saddle[0]} | {h(saddle[0]) for h in half_turns})
```

**No lift: volume zero.** In the bare plane every orbit is flat. A reading of the zeros that stays in the plane is a face reading and cannot be anything else.

**The character twist: volume zero.** A complex Dirichlet character $\chi$ and its conjugate $\bar\chi$ offer a natural third coordinate, since the zeros of $L(s,\chi)$ alone are not symmetric under conjugation (step 7 measures this). But conjugation and the functional equation both exchange $\chi$ with $\bar\chi$, so this coordinate is odd under $c$ and $f$. It fails the requirement, the lifted orbit stays in a plane, and the block returns zero. The twist adds a label and adds no dimension.

**The saddle: volume $\tfrac83(xy)^2$.** The lowest monomial with the required parity is $z = xy$. It is half the imaginary part of $w = (s-\tfrac12)^2$, so it brings in no new data. Under it the plane's three moves become exactly the three bimedian half-turns, and an orbit in the bulk becomes the four vertices of a tetrahedron. The regular tetrahedron's own vertices lie on the same saddle.

So the third coordinate was present all along, as the imaginary part of a square. The absent class of step 3 is found as well: the functional equation's own axis is the $z$-axis, and the saddle meets it only at the centre.

The sign of the lift is a convention. $z = -xy$ gives the mirror tetrahedron and the same volumes. That is the one global handedness bit (`L3-EdgeStateSpace` §I-e; expect there: the pin as presentational, the algebra bichiral by design).

### 5.1 Where the tetrahedron collapses

The six edges of the orbit tetrahedron come in three opposite pairs, one pair per move: the two edges that join a vertex to its image under that move. Their lengths say where the volume goes.

```python
dist2 = lambda a, b: sum((a[k] - b[k])**2 for k in range(3))
edge2 = lambda p, g: dist2(lift(p), lift(G[g](p)))       # squared length of the edges belonging to move g
for name, p in (('bulk', (x, y)), ('critical line', (Fr(0), y)), ('real axis', (x, Fr(0)))):
    print('5  ' + name + ': squared edge length by move', {g: str(edge2(p, g)) for g in ('c', 'f', 'cf')},
          '| volume', Fr(8, 3) * (p[0]*p[1])**2)
```

On the critical line the pair of edges belonging to the line-reflection has length zero, and the volume is gone. On the real axis the pair belonging to conjugation has length zero, and the volume is gone there too. Volume zero means $xy = 0$, and that has two solutions.

So "no orbit of zeros has volume" is weaker than the hypothesis. It says every zero is on one of two axes. In $w = (x^2 - y^2) + 2ixy$ it says $w$ is real, of either sign. The hypothesis needs $w \le 0$. What separates the two axes is the real part of $w$, which every move leaves unchanged, and which no lift of the kind tested above can see.

For $\xi$ the second axis is cleared by a separate theorem: $\zeta$ is negative on $(0,1)$ (step 7 checks it), so $\xi$ has no zero on the real axis. For a real Dirichlet character it is not cleared. A Landau–Siegel zero would sit on the real axis with volume zero and still break the generalized hypothesis.

The specimen can now be said in the procedure's terms. **The hypothesis is the claim that every orbit of zeros has collapsed onto one axis: no volume, and nothing on the real axis.** In $w$ this is the classical statement that every zero of $\Xi$ is real. The claim names no vertex, and "onto one axis" names only where the collapse ends. What the collapse is, as one stroke of a running cycle, is taken up in Part Four.

The collapsed pair of opposite edges is a shape the corpus already catalogues (`L4-AttractorSpace`, Part One; expect there: the bimedian attractors, where both edges of one bimedian go to zero). Reading the hypothesis as that attractor is a correspondence: the catalogue speaks of edge cost, and this block measures edge length.

### 5.2 Strain

Any zero of $\xi$ off the line would have $|x| < \tfrac12$ and $|y| > 14.13$. Its orbit tetrahedron is stretched at least twenty-eight to one. The stretch changes every edge length and every face angle, and it changes nothing the procedure uses: the centroid stays at the origin, the three bimedian axes stay the coordinate axes, and the three half-turns act as before. The block above already ran on a point stretched fifty-six to one. This is the engine's strain invariance in the specimen (`ENGINE-REFERENCE-AC` §3.3; expect there: the three bimedian planes and the centroid surviving every anisotropic deformation down to $V_4$).

## 6. Is the centroid's value made like a pole?

The fifth choice guards against a specific mistake: taking the centroid for one more vertex. `L2-K4-InteriorStructure` §V.3 gives the signature of a pole (expect there: Asserting poles produced by two squares and one flat form, Yielding poles by one root and two flat forms). A value produced that way belongs to a vertex. So the procedure collects the productions of the centroid's value, one from each move, and reads their kinds.

```python
kind = {'ARI':'sq','TAU':'sq','GEM':'flat','CAN':'root','LEO':'flat','VIR':'flat',
        'LIB':'flat','SCO':'flat','SAG':'root','CAP':'flat','AQU':'sq','PIS':'sq'}
home = {'ARI':'P','TAU':'P','GEM':'P','CAN':'I','LEO':'I','VIR':'I','LIB':'U','SCO':'U','SAG':'U','CAP':'R','AQU':'R','PIS':'R'}
seat = {'GEM':'IU','CAP':'IU','VIR':'RU','ARI':'RU','SCO':'IR','TAU':'IR','AQU':'PU','LEO':'PU','CAN':'PR','SAG':'PR','LIB':'PI','PIS':'PI'}
bim  = {'Fixed': ['PU', 'IR'], 'Cardinal': ['PR', 'IU'], 'Mutable': ['PI', 'UR']}
pole_sig = {v: sorted(kind[g] for g in kind if home[g] == v) for v in 'PIUR'}
bim_sig  = {m: sorted({kind[g] for g in kind if any(set(seat[g]) == set(ed) for ed in es)}) for m, es in bim.items()}
found = sorted(['sq', 'root', 'flat'])                   # the three productions measured in step 7
print('6  pole signatures:', pole_sig)
print('6  {square, root, flat} is a pole:', found in pole_sig.values(), '| any pole holds both a square and a root:',
      any('sq' in s and 'root' in s for s in pole_sig.values()))
print('6  kinds by bimedian:', bim_sig)
```

The three productions of $\tfrac12$ are a square, a root and a flat form. No pole holds both a square and a root. The value is not made like a pole, and that is all this step settles.

It does not settle which move carries which mode. The last line of the block shows why. The tiers and the bimedians are two different threes and they cross-cut: squares sit on the Fixed and Mutable bimedians, roots on the Cardinal, flat forms on all three (`ENGINE-REFERENCE-AC` §4.1; expect there: "do not conflate the two threes"). A square, a root and a flat form together are reached by Cardinal with either of the others, so they do not witness three bimedians. And the three productions are sorted here by the kind of operator that appears in an identity of the specimen. Nothing in that makes the move that owns the root the Cardinal half-turn. The procedure leaves the moves unassigned.

## 7. Measure what was asserted, and run controls

The last choice is to leave nothing in Part One on reputation, and to run the procedure on two objects that should fail.

```python
import mpmath as mp
mp.mp.dps = 20
chi_fe = lambda s: 2**s * mp.pi**(s-1) * mp.sin(mp.pi*s/2) * mp.gamma(1-s)      # zeta(s) = chi_fe(s) * zeta(1-s)
theta  = lambda t: sum(mp.exp(-mp.pi*n*n*mp.mpf(t)) for n in range(-60, 61))
s0 = mp.mpf('0.5001')
print('7  square:  sum |n^-s|^2 = zeta(2 sigma), pole at sigma = 1/2, residue check', mp.nstr((2*s0-1)*mp.zeta(2*s0), 6))
print('7  root:    theta(1/t) / (sqrt(t) theta(t)) at t = 0.37:', mp.nstr(theta(1/mp.mpf('0.37')) / (mp.sqrt('0.37')*theta('0.37')), 12))
print('7  flat:    |chi_fe| on the line:', [mp.nstr(abs(chi_fe(mp.mpc(0.5, t))), 10) for t in (5, 100)],
      '| off it, sigma = 0.3, 0.7:', [mp.nstr(abs(chi_fe(mp.mpc(sg, 100))), 5) for sg in (0.3, 0.7)])
xi = lambda s: s*(s-1)/2 * mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s)
print('7  at the centre: zeta(1/2) =', mp.nstr(mp.zeta(0.5), 10), '| xi(1/2) =', mp.nstr(xi(mp.mpf(0.5)), 10),
      '| zeta < 0 across (0,1):', all(mp.zeta(mp.mpf(k)/40) < 0 for k in range(1, 40)))
chi5, chi5b = [0, 1, 1j, -1j, -1], [0, 1, -1j, 1j, -1]
L5 = lambda t: mp.dirichlet(mp.mpc(0.5, t), chi5)
print('7  chi mod 5, first zero above:', mp.nstr(mp.findroot(L5, 6.2).real, 6), '| first below:', mp.nstr(mp.findroot(L5, -4.1).real, 6))
```

The three productions are as stated, the centre is occupied by a number that is not zero, the real axis is clear for $\zeta$, and the zeros of one twisted $L$-function are lopsided, as step 5 assumed.

### 7.1 Two controls: same group, without and with an Euler product

Davenport and Heilbronn built, from the same character modulo five, a function with real coefficients and the same kind of functional equation. Everything the procedure has used so far is present in it: conjugation, the functional equation, the centre at $\tfrac12$. What it lacks is an Euler product.

```python
kap  = (mp.sqrt(10 - 2*mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
fDH  = lambda s: (1 - 1j*kap)/2 * mp.dirichlet(s, chi5) + (1 + 1j*kap)/2 * mp.dirichlet(s, chi5b)
xiDH = lambda s: (5/mp.pi)**(s/2) * mp.gamma((s+1)/2) * fDH(s)
coef = [(1 - 1j*kap)/2 * a + (1 + 1j*kap)/2 * b for a, b in zip(chi5, chi5b)]
print('7  control: coefficients real:', all(abs(q.imag) < mp.mpf(10)**-15 for q in coef), [mp.nstr(q.real, 5) for q in coef],
      '| functional equation xi(s)/xi(1-s):', mp.nstr(abs(xiDH(mp.mpc(0.3, 7)) / xiDH(mp.mpc(0.7, -7))), 12))
rho = mp.findroot(fDH, mp.mpc(0.8085, 85.6993)); xd, yd = rho.real - 0.5, rho.imag
print('7  control: a zero at', mp.nstr(rho, 9), '| residual', mp.nstr(abs(fDH(rho)), 3),
      '| orbit volume', mp.nstr(mp.mpf(8)/3 * (xd*yd)**2, 6), '| also a zero on the line at', mp.nstr(mp.findroot(fDH, mp.mpc(0.5, 5.09)), 7))
dl, g1 = mp.mpf(1)/4, mp.zetazero(1).imag                # second control: two shifted copies of zeta, Euler product intact
F2, xi2 = (lambda s: mp.zeta(s - dl) * mp.zeta(s + dl)), (lambda s: xi(s - dl) * xi(s + dl))
print('7  second control: functional equation:', mp.nstr(abs(xi2(mp.mpc(0.3, 7)) / xi2(mp.mpc(0.7, -7))), 12),
      '| zero at 3/4 + i*14.1347, residual', mp.nstr(abs(F2(mp.mpc(0.75, g1))), 3), '| orbit volume', mp.nstr(mp.mpf(8)/3 * (dl*g1)**2, 6))
```

The control has the group, the lift and the centre, and it has a zero in the bulk whose orbit is a tetrahedron of volume about $1864$. Identical symmetry, nonzero volume. The procedure's steps 2 to 5 return the same answers for it as for the specimen, and its bulk is occupied. So nothing in steps 2 to 5 decides occupancy.

The second control guards against reading too much into the first. $\zeta(s-\tfrac14)\,\zeta(s+\tfrac14)$ is real on the real axis, its completed form is unchanged under $s \to 1-s$, and it has an Euler product. Every zero of $\zeta$ puts a four-point orbit of it in the bulk. So an Euler product, taken as a badge, does not empty the bulk either. This function is a product of two shifted copies, which the literature excludes by asking for a primitive function with bounded coefficients. The procedure does not need that vocabulary. It needs only the two measurements: the symmetry does not decide occupancy, and neither does the presence of a product over primes. Part Three takes up what does.

### 7.2 Which square decides

Step 7 already holds a square, $\zeta(2\sigma)$, and it decides nothing about any single zero. The square that the positivity criteria use is a different one. Weil's criterion sums, over the zeros, a test function paired across the line: its value at $\rho$ times the conjugate of its value at $1-\bar\rho$. This block evaluates one such pairing for a toy test function $g(s) = s - s_0$.

```python
pair = lambda g, r: g(r) * mp.conj(g(1 - mp.conj(r)))
on, off = mp.mpc(0.5, 14.134725), rho
g_on, g_off = (lambda s: s - mp.mpc(0.5, 3)), (lambda s: s - mp.mpc(0.5, off.imag))
print('7  pairing on the line  = |g|^2:', mp.almosteq(pair(g_on, on), abs(g_on(on))**2), mp.nstr(pair(g_on, on).real, 8),
      '| pairing at the control zero:', mp.nstr(pair(g_off, off).real, 6))
```

On the line, $1 - \bar\rho$ is $\rho$ itself, and the pairing is a value times its own conjugate: a mod-square, never negative. Off the line the two points are different vertices of one orbit, the pairing is a cross-term, and the block shows it going negative at the control's zero. The square that decides occupancy is the mod-square, the second of the three squarings (`ProofQ_AlgebraicSyntax` §V; expect there: Squaring 2, the Hermitian mod-square $II^*$, strictly real and positive, as the Route Law's AC form). The toy function is not Weil's functional. It shows only the one fact used: the pairing is a mod-square exactly when the two points coincide.

## 8. The outcome of the construction

*Output of the woven program:*

```
2  four moves, closed: True | every move its own inverse: True
3  fixed by () -> orbit size [4]
3  fixed by ('c',) -> orbit size [2]
3  fixed by ('cf',) -> orbit size [2]
3  fixed by ('c', 'cf', 'f') -> orbit size [1]
4  centroid of every orbit: True | points fixed by all moves: [(Fraction(0, 1), Fraction(0, 1))]
5  volume  flat: 0 | character twist: 0 | saddle z = xy: 98/3 = 98/3
5  regular tetrahedron on z = xy: True | saddle orbit = orbit under the three half-turns: True
5  bulk: squared edge length by move {'c': '833', 'f': '3137/4', 'cf': '197/4'} | volume 98/3
5  critical line: squared edge length by move {'c': '784', 'f': '784', 'cf': '0'} | volume 0
5  real axis: squared edge length by move {'c': '0', 'f': '1/4', 'cf': '1/4'} | volume 0
6  pole signatures: {'P': ['flat', 'sq', 'sq'], 'I': ['flat', 'flat', 'root'], 'U': ['flat', 'flat', 'root'], 'R': ['flat', 'sq', 'sq']}
6  {square, root, flat} is a pole: False | any pole holds both a square and a root: False
6  kinds by bimedian: {'Fixed': ['flat', 'sq'], 'Cardinal': ['flat', 'root'], 'Mutable': ['flat', 'sq']}
7  square:  sum |n^-s|^2 = zeta(2 sigma), pole at sigma = 1/2, residue check 1.00012
7  root:    theta(1/t) / (sqrt(t) theta(t)) at t = 0.37: 1.0
7  flat:    |chi_fe| on the line: ['1.0', '1.0'] | off it, sigma = 0.3, 0.7: ['1.7393', '0.57496']
7  at the centre: zeta(1/2) = -1.460354509 | xi(1/2) = 0.4971207782 | zeta < 0 across (0,1): True
7  chi mod 5, first zero above: 6.18358 | first below: -4.1329
7  control: coefficients real: True ['0.0', '1.0', '0.28408', '-0.28408', '-1.0'] | functional equation xi(s)/xi(1-s): 1.0
7  control: a zero at (0.808517182 + 85.6993485j) | residual 0.0 | orbit volume 1864.16 | also a zero on the line at (0.5 + 5.09416j)
7  second control: functional equation: 1.0 | zero at 3/4 + i*14.1347, residual 1.7e-21 | orbit volume 33.2984
7  pairing on the line  = |g|^2: True 123.9821 | pairing at the control zero: -0.0951829
II each monad has one edge per move: True | no move fixes a monad: True
II on the axis of c | its own move is idle: True | the other two act as one flip: True
II on the axis of cf | its own move is idle: True | the other two act as one flip: True
IV saddle is 2z = u^2 - v^2: True | volume is zero exactly on the cone: True | Re w on the line, the real axis, the diagonal: [-4.0, 0.09, 0.0]
IV at fixed distance from the centre the volume peaks at 45 degrees
IV wave size against sqrt(x)  line zero: 1.0 | its mod-square against x: 1.0 | control zero and its partner: 8.42464 0.118699 | product of the two: 1.0
IV bulk: squared bimedian by move {'c': '1/4', 'f': '49', 'cf': '784'} | squared edge by move {'c': '833', 'f': '3137/4', 'cf': '197/4'} | distinct monads 4
IV critical line: squared bimedian by move {'c': '0', 'f': '0', 'cf': '784'} | squared edge by move {'c': '784', 'f': '784', 'cf': '0'} | distinct monads 2
IV on the line: conjugation and the functional equation are one move: True | the orbit equals its mirror image: True | in the bulk: False | the centre bisects the pair: True
IV xi is real on the line: True | sign changes for 0 < t <= 50: 10 | zeros of zeta to that height: 10
IV prime ledger at x = 30.5: 409.3903 | smooth term alone: 411.03841 | with 100 dipoles: 409.40901 | gap closed: 0.9886
```

The procedure, stripped of its specimen:

| Step | The choice | What it can return | What it returned here |
|---|---|---|---|
| 1 | Fix the layer before any finding | a refusal to proceed | meta-of-domain; no claim on the hypothesis |
| 2 | Name the symmetric object and its moves, then the schools | a group, or none | $\xi$; the Klein four-group |
| 3 | Sort points by what fixes them | the addresses, and any absence | bulk, two axes, centre; one of five missing |
| 4 | The centroid is what no move touches | a point, or an empty set | $s = \tfrac12$, the balance of every orbit |
| 5 | Lift under the rotation requirement; find where volume goes | volume or flatness; the collapse loci | two flat lifts; the saddle has volume; two axes of collapse |
| 6 | Read the kinds of the centroid's productions | a pole signature, or none | square, root, flat: no pole; moves unassigned |
| 7 | Measure every borrowed fact; run controls | agreement or a correction; a control that fails | agreement; two controls keep the group and fill the bulk |

Two lifts in step 5 return nothing. One class is missing in step 3 until step 5 locates it. Volume zero in step 5.1 turns out to admit a second axis. The control in step 7.1 passes every symmetry test and still has volume. Those negatives are why the positive results can be trusted, and the last of them is the most useful thing the construction returns.

The result is an orbit tetrahedron on a saddle, a ground of one bulk and three axes around a known centre, and one hypothesis restated as a collapse. Part Two looks at the four vertices and the ground they stand on. Part Three opens the centre. Part Four stands there and looks back.

---

# Part Two: Four Monads and Their Playgrounds

## II.1 The four monads

A zero in the bulk would not be one thing. It would be four: itself, its conjugate, its dual under the functional equation, and its reflection in the line. These are the four vertices of the orbit tetrahedron, and they are the monads of this specimen in the sense of `L2-K4-InteriorStructure` §V.4 (expect there: a vertex as a point with its own interior, held in a tetrahedron with three others).

Each monad is joined to each of the other three by exactly one move. So each vertex has three edges, one per move, and each move owns one pair of opposite edges.

```python
V = {k: G[k]((x, y)) for k in G}                         # the four monads of one orbit, named by the move that reaches them
joins = {a: sorted(m for b in V if b != a for m in ('c', 'f', 'cf') if G[m](V[a]) == V[b]) for a in V}
print('II each monad has one edge per move:', all(j == ['c', 'cf', 'f'] for j in joins.values()),
      '| no move fixes a monad:', all(G[m](V[a]) != V[a] for a in V for m in ('c', 'f', 'cf')))
```

One edge per move at every vertex: each of the three schools of II.3 has a hand on every monad. And no move fixes a monad. A vertex is never on a bimedian axis.

That last fact places the hypothesis. It says the four monads of every zero have merged in pairs along the line-reflection's edges, until two points remain on one axis. The hypothesis is about where vertices are allowed to be, and its answer is: nowhere a vertex of a full tetrahedron can be.

## II.2 The ground: one bulk, three axes

The monads' playground is the ground of step 3. It has four parts away from the centre.

On each axis, the move that owns the axis does nothing, and the other two act as one and the same flip. This is the group divided by the owning move: two elements, the identity and one reflection along the axis.

```python
axes = {'c': [(Fr(a), Fr(0)) for a in (1, 2)], 'cf': [(Fr(0), Fr(b)) for b in (1, 2)]}
for own, P in axes.items():
    others = [k for k in ('c', 'f', 'cf') if k != own]
    print('II on the axis of', own, '| its own move is idle:', all(G[own](p) == p for p in P),
          '| the other two act as one flip:', all(G[others[0]](p) == G[others[1]](p) != p for p in P))
```

**The bulk: fixed by nothing.** The only part with area. A zero here has four monads and a tetrahedron with volume. No zero of $\xi$ has been found here, and the hypothesis says none ever will. Both controls of step 7.1 have them.

**The real axis: fixed by conjugation.** For $\xi$ it is empty, by a theorem. For real Dirichlet characters it is where a Landau–Siegel zero would sit, and whether one exists is open. A zero here has two monads and no volume.

**The critical line: fixed by the reflection.** Every zero of $\xi$ ever computed is here. A zero here has two monads and no volume.

**The vertical axis: fixed by the functional equation.** It leaves the saddle at once. On the saddle it is the centre and nothing else. It is an axis with a move and no ground.

## II.3 Three schools on three axes

Each great approach to the specimen is founded on one move.

**The arithmetic school owns conjugation.** The Euler product, the sieve, Möbius and Mertens sums, the reading of $\zeta$ on the real axis. Its credential stops where real-variable data stops separating zeros: sieves cannot tell an even number of prime factors from an odd one, and the zero-free region it can prove thins toward the edge of the strip without reaching the line.

**The spectral school owns the reflection.** Hilbert and Pólya's operator, the dilation Hamiltonian, random matrices. Being fixed by this move is what self-adjointness would deliver. Its credential stops at the operator, which has not been produced, and at statistics, which describe how zeros on the line are spaced and are silent on whether a zero could be off it.

**The duality school owns the functional equation.** Poisson summation, Tate's adelic proof, Weil's and Deligne's geometry. It is the school with the proved cases, the zeta functions of curves and varieties over finite fields. Its credential stops at positivity. Over a finite field the positivity comes from a surface and a Frobenius map, and for the integers neither has been built. Because its axis has no ground on the saddle, everything this school can say about location is said at the centre. And it does say it there: when the sign of a functional equation is $-1$, the function is forced to vanish at the central point.

**No school owns the bulk.** Every unconditional theorem about zeros off the line is a statement about it from outside: the zero-free regions, and the density theorems that bound how many zeros it could hold.

| Address | Fixed by | Monads of a zero there | Occupants | School, and where it stops |
|---|---|---|---|---|
| Bulk | nothing | four; a tetrahedron with volume | none known for $\xi$; both controls have them | none; bounded from outside |
| Real axis | conjugation | two | none for $\xi$; the Siegel question for real characters | arithmetic; stops at the parity of prime factors |
| Critical line | the reflection | two | every computed zero | spectral; stops at the missing operator |
| Vertical axis | the functional equation | none on the saddle | none possible | duality; stops at positivity |

Three schools, three moves, and any two moves give the third (step 2). So each school holds the whole group the moment it borrows one fact from a neighbour, and the two facts it needs are theorems. None of the three is short of symmetry.

Which axis carries which mode — Fixed, Cardinal, Mutable — is not assigned here. Step 6 shows the blocks do not decide it, and an assignment by resemblance would be a guess wearing a table.

---

# Part Three: The Centroid, the Egg's Quintessential Contents

The egg is the whole orbit figure, shell and all: four monads, six edges, the ground under them. Its quintessence is the fifth thing, the one that is none of the four: the centroid. It is fixed by every move, and it is five-dimensional in the corpus's sense, a location defined by integration, with no extent (`L3-TheAtomOfSpace`; expect there: the centroid as 5D by location). This part opens it.

## III.1 It is settled first

Every orbit balances on $s = \tfrac12$ (step 4). That is true of the orbits that exist and of the ones the hypothesis forbids. It is true of the control. So the centroid of the specimen's tetrahedron was never in question. What is open is where the vertices are.

## III.2 One value, three kinds

The number $\tfrac12$ is produced once on each school's side, and the three productions are different operators (step 7).

- **A square, on the arithmetic side.** The squared size of $n^{-s}$ is $n^{-2\sigma}$, and the sum of those is $\zeta(2\sigma)$, with its pole at $\sigma = \tfrac12$. The line is where the terms stop being square-summable.
- **A root, on the duality side.** The theta function obeys $\theta(1/t) = \sqrt{t}\,\theta(t)$. The functional equation of $\zeta$ is that identity transformed, and the $\tfrac12$ is the exponent of the root: the weight a one-dimensional Gaussian carries under its own Fourier transform.
- **A flat form, on the spectral side.** In $\zeta(s) = \chi(s)\,\zeta(1-s)$ the factor $\chi$ has modulus exactly one on the critical line. There the exchange of $s$ with $1-s$ is a pure phase. Off the line it has gain on one side and loss on the other.

`L2-K4-InteriorStructure` §V.4 found that a vertex's three secretaries agree in value and disagree in kind. The centre's three productions do the same, with the one difference step 6 measured: no pole holds both a square and a root, and the centre does. That marks the value as not a vertex's. It does not map the three tiers onto the three moves (step 6).

All three productions say one thing in three dialects: at $\tfrac12$ an amplitude balances against its own measure. The square says it as summability, the root as a transform weight, the flat form as a lossless exchange.

## III.3 What sits there

For $\zeta$ the centre is occupied by a number that is not zero: $\zeta(\tfrac12) = -1.4603\ldots$, and $\xi(\tfrac12) = 0.4971\ldots$. Nothing vanishes at the centroid of the specimen.

For the wider family the centre is where the arithmetic is richest. The order to which an elliptic curve's $L$-function vanishes at its central point is conjectured to equal the curve's rank, and the cases of rank zero and one are proved. The duality school's forced central zero (II.3) is the first term of that story. The schools already treat the centre as the place where a function reports on the object it came from.

## III.4 What symmetry cannot say

A group action tells you what the orbits are. It does not tell you which addresses are occupied. The control of step 7.1 is the measurement: the same group, the same lift, the same centre, and a zero in the bulk.

That is why the three schools stall together. Each owns a move, each can borrow the rest of the group, and the group was never what was missing. The two controls bracket what was. The first keeps the group and drops the Euler product. The second keeps the group and an Euler product. Both fill the bulk. What separates the specimen from them is nothing the symmetry steps can see and nothing so simple as having a product over primes.

The hypothesis is a statement about occupancy, and occupancy is decided by an inequality. Every proved case and every equivalent criterion is one. Weil's criterion is the non-negativity of a quadratic form. Li's is the non-negativity of a sequence. Deligne's proof over finite fields rests on a positivity that the geometry supplies.

Not every square will do. The arithmetic square $\zeta(2\sigma)$ is a mean square. It feeds the averaged theorems of III.5 and says nothing about a single zero. The square that decides is the mod-square of step 7.2. On the line each zero is paired with itself and contributes a value times its own conjugate. Off the line it is paired with a different monad of its own orbit, and the contribution is a cross-term that can be negative. In the terms of Part Two: positivity holds exactly when the two monads joined by the line-reflection's edge are one point.

In the engine's terms symmetry is routing, which is free, and the mod-square is a commit, which is taxed. A routing argument cannot pay a commit. That reading is a correspondence, and it predicts something checkable: a proof of the specimen, when one exists, will turn on a positivity, and not on a new symmetry. How the arithmetic of the integers would supply that positivity is the open thing. Over finite fields a surface supplies it.

## III.5 The concern, held on average

The centroid is a statement about balance, and balance can be proved without proving anything about each vertex. A positive proportion of the zeros is known to lie on the line. Almost all of them are known to lie arbitrarily close to it, in the sense of density. The Bombieri–Vinogradov theorem gives, on average over moduli, the strength the generalized hypothesis would give for each one, and much of what the hypothesis is wanted for is done with that.

So the centroidal concern is already documented from three sides and already in daily use. The hypothesis is the sharpening from the balance to every point. It asks that every orbit, everywhere, has collapsed onto one axis. That is a claim about a collapse, and the procedure of Part One shows which collapse, of which tetrahedron, around which centre.

---

# Part Four: Beholding the Hypothesis from the Centroid

To behold is to hold every open reading live and commit to none (`L2-Terminology`; expect there: `.behold()` as holding the full interference structure without forcing an outcome, all AbsentVars live). The centroid is the place to do it from, because it is the one address that belongs to no school and is settled whatever the hypothesis turns out to be (III.1).

Parts One to Three measured a figure. A figure invites the past tense: the orbit collapsed, the volume vanished, the zeros sit. This part refuses that tense. The collapse is one stroke of a cycle, the cycle is running, and the block in IV.5 shows it writing. The part walks the cycle once in order — unfold, hold, collapse, reseed, write — and then holds the whole of it open.

## IV.1 The unfold

*Set down:* the corner. The variable $s$ has its zero at a point of no significance to the function, and "real part one half" is a distance measured from that corner. Putting the origin in a corner is the oldest flattening there is (`L0-EinsteinTrace` §I; expect there: the origin exiled to an arbitrary corner, against the origin as the integrating centroid).

*Hold:* the view from $s = \tfrac12$. Step 5 was the unfold: move the origin to the centre and let the third coordinate stand up. From there the saddle reads $2z = u^2 - v^2$, with $u = (x+y)/\sqrt2$ and $v = (x-y)/\sqrt2$. That is a form with one plus sign and one minus sign, and it vanishes on a cone through the centre: the two lines $x = 0$ and $y = 0$. In the sense that signature gives the word, the critical line and the real axis are the light-cone of the centre. An orbit has an interior exactly when it is off the cone. The two rays are told apart by the other form, $x^2 - y^2$, the real part of $w$: negative on the critical line, positive on the real axis, zero on the diagonals, where for a given distance from the centre the volume is greatest.

```python
import math
u_, v_ = (lambda p: (p[0] + p[1]) / math.sqrt(2)), (lambda p: (p[0] - p[1]) / math.sqrt(2))
sample = [(0.3, 2.0), (0.0, 2.0), (0.3, 0.0), (1.0, 1.0), (-0.7, 0.4)]
print('IV saddle is 2z = u^2 - v^2:', all(abs(2*p[0]*p[1] - (u_(p)**2 - v_(p)**2)) < 1e-12 for p in sample),
      '| volume is zero exactly on the cone:', all((vol([lift(q) for q in (p, c(p), f(p), cf(p))]) == 0) == (p[0] == 0 or p[1] == 0) for p in pts),
      '| Re w on the line, the real axis, the diagonal:', [p[0]**2 - p[1]**2 for p in ((0.0, 2.0), (0.3, 0.0), (1.0, 1.0))])
best = max(range(0, 91), key=lambda d: abs(math.cos(math.radians(d)) * math.sin(math.radians(d))))
print('IV at fixed distance from the centre the volume peaks at', best, 'degrees')
```

The third axis, the functional equation's, is of a different kind from the two rays. It stands on the plane at the centre, and looking down it puts the centre of every orbit on the one point (`L4-DynamicDistortions-Sudoku` §II; expect there: the tetrahedron projected along its altitude, apex and centroid landing together).

## IV.2 The hold

*Set down:* the line as a shelf where zeros rest.

*Hold:* what is balanced there. Each zero $\rho$ enters the count of primes as a wave $x^\rho$ (IV.5 runs the formula). Its size is $x^\sigma$. On the line every wave has the one size $\sqrt{x}$, and its mod-square is $x$, the size of the main term: the amplitude balanced against its own measure, which III.2 said in three dialects, is here a single equation. Off the line the balance breaks in a particular way. A zero in the bulk is joined by the line-reflection's edge to a partner on the other side, and the pair has two sizes, $x^{1/2+\delta}$ and $x^{1/2-\delta}$. One wave gains and the other loses.

```python
xx = mp.mpf(1000)
env = lambda r: abs(xx**r) / mp.sqrt(xx)                 # size of the wave x^rho against sqrt(x)
z1 = mp.zetazero(1)
print('IV wave size against sqrt(x)  line zero:', mp.nstr(env(z1), 8), '| its mod-square against x:', mp.nstr(abs(xx**z1)**2 / xx, 8),
      '| control zero and its partner:', mp.nstr(env(rho), 6), mp.nstr(env(1 - mp.conj(rho)), 6),
      '| product of the two:', mp.nstr(env(rho) * env(1 - mp.conj(rho)), 8))
```

The control's pair gains on one side exactly what it loses on the other, so the product is still one and the centre still balances. What the line adds is that each wave balances by itself. This is resonance in the corpus's sense: the condition under which the two opposed terms cancel and what is left is the system's own (`ProofS_ResonantNote` §II; expect there: at resonance the reactances cancel, the response is transparent, and the location of the peak is fixed by the structure). Step 7 measured the same cancellation as $|\chi| = 1$ on the line, with gain at $\sigma = 0.3$ and loss at $\sigma = 0.7$.

So the hold is an active balance, kept by every zero separately. Nothing is resting.

## IV.3 The collapse

*Set down:* the collapse as a thing that happened to a shape.

*Hold:* it as the step that runs when the hold is exact. Three measurements say what the step does.

```python
def bimedian2(p, g):                                     # squared length of the bimedian of move g: between midpoints of its two edges
    h = next(k for k in ('c', 'f', 'cf') if k != g)
    mid = lambda a: tuple((lift(a)[k] + lift(G[g](a))[k]) / 2 for k in range(3))
    return dist2(mid(p), mid(G[h](p)))
for name, p in (('bulk', (x, y)), ('critical line', (Fr(0), y))):
    print('IV ' + name + ': squared bimedian by move', {g: str(bimedian2(p, g)) for g in ('c', 'f', 'cf')},
          '| squared edge by move', {g: str(edge2(p, g)) for g in ('c', 'f', 'cf')},
          '| distinct monads', len({lift(q) for q in orbit(p)}))
mirror = lambda S: {(q[0], q[1], -q[2]) for q in S}
L_ = lambda p: {lift(q) for q in orbit(p)}
print('IV on the line: conjugation and the functional equation are one move:', c((Fr(0), y)) == f((Fr(0), y)),
      '| the orbit equals its mirror image:', L_((Fr(0), y)) == mirror(L_((Fr(0), y))), '| in the bulk:', L_((x, y)) == mirror(L_((x, y))),
      '| the centre bisects the pair:', tuple(sum(q[k] for q in L_((Fr(0), y))) for k in range(3)) == (0, 0, 0))
```

**The monads fuse in pairs.** The two edges belonging to the line-reflection close. Four monads become two, joined by one segment through the centre. Two fused nodes on one axis is a dipole, and the corpus has this collapse by name (`L4-DynamicDistortions301` §VII.B; expect there: complete collapse of one bimedian's two edges as pairwise vertex-fusion, four vertices becoming two compound nodes on a single axis).

**The other two edge pairs stay open, and become one.** This is the part a drawing of the flattened figure hides. Only the line-reflection's pair of edges closes. The pair belonging to conjugation and the pair belonging to the functional equation both keep their full length, and they land on the same segment, because on the line the two moves are the same move. The corpus says that when one bimedian closes, what it held passes to the other two (`L4-DynamicDistortions301` §V; expect there: the collapsed bimedian's phase ported onto the two that keep vertex separation). In the specimen that sentence has an exact content. Conjugation says $\xi(\bar s)$ is the conjugate of $\xi(s)$. The functional equation says $\xi(1-s) = \xi(s)$. Where the two moves coincide, $\xi(s)$ equals its own conjugate. So $\xi$ is real on the line. The live wave of IV.4 is carried by the two edge pairs that did not close, acting as one.

**The hand is discarded.** A fused orbit is its own mirror image, and a bulk orbit is not. The pairing of step 7.2 becomes a value times its own conjugate. Each zero equals its own reflection. These are one fact: when the two monads joined by the reflection's edge are one point, there is no order left between them to keep. The corpus calls the step that discards orientation a boundary, and says a boundary is an operation and no location (`L4-DynamicDistortions301` §VI; expect there: orientation as what cannot be sent; "a boundary is an operation, not a place").

So the collapse is the symmetrizing step, running on a zero. It closes one pair of edges, merges the other two, burns the hand, and leaves a real quantity where there was a complex one. Which of the three dipole classes results stays unassigned, with the modes (step 6).

## IV.4 The reseed

*Set down:* the collapsed figure as an inert one.

*Hold:* what the step leaves behind. A real function on the line can do one thing a complex one cannot: change sign. Every zero is a sign change.

```python
xil = lambda t: xi(mp.mpc(0.5, t))
vals = [xil(mp.mpf(k) / 20) for k in range(1, 1001)]
print('IV xi is real on the line:', max(abs(q.imag) / abs(q) for q in vals) < mp.mpf(10)**-12,
      '| sign changes for 0 < t <= 50:', sum(1 for a, b in zip(vals, vals[1:]) if a.real * b.real < 0), '| zeros of zeta to that height:', mp.nzeros(50))
```

The collapse burned an orientation and the wave it left opens a fresh sign at every zero. That is the engine's third stroke: the root reopens a plus-or-minus that the commit closed, forward, without undoing the commit (`Q14-LeptonScaleCascade`; expect there: the ledger as write-only, the root as reseeding a new $\pm$ ambiguity forward). The root is present in the specimen by name: the size of every wave on the line is $\sqrt{x}$ (IV.2), and the duality side's own identity is $\theta(1/t) = \sqrt{t}\,\theta(t)$ (step 7).

## IV.5 The write

*Set down:* the zeros as a finished list, and the hypothesis as a fact about the list.

*Hold:* what the dipoles are doing. The explicit formula says the count of primes, weighted and summed once, is a smooth term minus one real wave per dipole. The block computes the count directly from the primes, then from the smooth term alone, then with the first hundred dipoles.

```python
def mangoldt(n):
    for p in range(2, n + 1):
        if n % p == 0:
            m = n
            while m % p == 0: m //= p
            return mp.log(p) if m == 1 else mp.mpf(0)
X = mp.mpf('30.5')
ledger = sum(mangoldt(n) * (X - n) for n in range(2, int(X) + 1))                # written by the primes
smooth = X**2/2 - X*mp.log(2*mp.pi) + mp.zeta(-1, derivative=1)/mp.zeta(-1) - sum(X**(1-2*r) / (2*r*(2*r-1)) for r in range(1, 40))
dip = [2 * mp.re(X**(r+1) / (r*(r+1))) for r in (mp.zetazero(n) for n in range(1, 101))]   # one real wave per dipole
print('IV prime ledger at x = 30.5:', mp.nstr(ledger, 8), '| smooth term alone:', mp.nstr(smooth, 8),
      '| with 100 dipoles:', mp.nstr(smooth - sum(dip), 8), '| gap closed:', mp.nstr(1 - abs(ledger - (smooth - sum(dip))) / abs(ledger - smooth), 4))
```

The primes write a ledger of discrete entries, one at each prime power. The dipoles, all of them at once, reproduce that ledger. Each is a pure phase turning in $\log x$, at a size set by a root, and the sum of them lands on the integers. Read against the engine's loop (`ENGINE-REFERENCE-AC` §VII; expect there: route, commit, reseed, advance, in that order, as the machine's whole life): the turning phase is the route, the entry at a prime power is the commit, the root-sized wave with its fresh sign is the reseed, and the advance is $x$ moving on. The corpus's two-stroke account of the same loop is a lossless hold broken by a write (`Q14-LeptonScaleCascade`; expect there: stroke one holding in equilibrium, stroke two compiling to the ledger). Matching the specimen to those loops is a correspondence. The computation under it is not: the dipoles write the primes, and the formula has no idle term.

This is where the tense changes. The collapse of IV.3 is not behind the zeros. It is the condition each dipole meets every time it contributes, at every $x$: one size, no gain, no hand.

## IV.6 Where the live tetrahedron is

Two facts now stand together, and neither replaces the other.

**The orbit of a single zero is a diagnostic.** It asks one question of one zero: has the symmetrizing step run to completion here? The hypothesis says yes, everywhere. So if it holds, no zero-orbit of $\xi$ anywhere has an interior, and the figure of Part One is flat wherever it is drawn.

**The running tetrahedron is the cycle.** It is not any one orbit. It runs across the three schools' sides at once — the prime ledger on the arithmetic side, the dipole spectrum on the line, the root and the scale exchange on the duality side — and it is integrated at the centre. IV.5 is that cycle, running.

What neither fact supplies is the thing that forces every dipole to collapse completely. The controls of step 7.1 have the same symmetry and carry waves that gain and lose. Over finite fields the forcing is a positivity that lives on a surface, one dimension above the curve it settles. Across families of $L$-functions the addresses are coupled: a zero on the real axis of one function repels the zeros of the others from the edge of the strip. Both point above the single function and its plane. Nothing here says what the larger object is over the integers. Held as a question, with no commit.

## IV.7 The whole, held

*Set down:* true or false.

*Hold:* every address open, with what is known at each, and the cycle running through them.

| Address | What is held there |
|---|---|
| Centre | settled: every orbit balances on it; $\tfrac12$ made three ways; the cycle is integrated here |
| Critical line | every computed zero: a dipole across the centre, resonant, a sign change of a real wave, writing the primes |
| Real axis | the other ray of the cone; empty for $\xi$ by theorem; open for real characters |
| Bulk | the only address with an interior and a hand; a zero here would write with gain; empty for $\xi$ as far as anyone has looked; occupied in both controls |
| Vertical axis | no ground; the duality school speaks at the centre |

The table has a settled centre and an open bulk, and they are different kinds of statement. The centre is balance, proved, and in daily use (III.5). The bulk is occupancy, decided by a mod-square, and open. Much that is done "assuming the hypothesis" draws on the first while naming the second. Holding them apart is most of what the centroid's position buys.

What the hypothesis is, then, with no regard for the nouns set down above: **the claim that the cycle which writes the primes runs without gain or loss — that the symmetrizing step completes on every zero, so that each is a resonant dipole across one settled centre, with no interior, no hand, and no partner but itself.** In the plane, afterwards, that looks like zeros on a line. Whether it holds is not something this file can say. What it would take is said in III.4.

---

## Register

**LANDED and mechanical** (the woven program reproduces all of it): the four moves as a Klein four-group; the census of four classes and the one absent class; $s = \tfrac12$ as the centroid of every orbit and the only point fixed by all moves; the three lift volumes; the saddle lift as the action of the three bimedian half-turns; the regular tetrahedron on $z = xy$; the edge lengths by move and the two axes of collapse; one edge per move at every vertex, and no vertex on an axis; the idle-move and one-flip property of the axes; the pole signatures and the kinds by bimedian; the numerical checks of step 7; the Davenport–Heilbronn control, its functional equation, its zero in the bulk and that orbit's volume; the second control, with its Euler product and its bulk orbit; the pairing as a mod-square on the line and negative at the control's zero for the toy test function; the saddle as $2z = u^2 - v^2$ and its cone; the three bimedian lengths and the fusion to two points on the line; a collapsed orbit as its own mirror; conjugation and the functional equation as one move on the line, with the two surviving edge pairs coincident; the wave sizes on and off the line; $\xi$ real on the line with its sign changes equal in number to the zeros; the prime ledger reproduced by the smooth term less one real wave per dipole.

**ADOPTED** from their owners or from the literature of the specimen and not re-derived: the centroid as the unbound point; the operator split by charge; the cross-cutting of tiers and bimedians; strain invariance; the three squarings; the dipole taxonomy and the boundary as an operation; resonance; the runtime loop and the two strokes; `.behold()`; the explicit formula; the functional equation of $\xi$ and its reality on the real axis; the confinement of its zeros to the strip; the equivalence of the hypothesis with the reality of the zeros of $\Xi$; the positivity criteria; the averaged theorems of III.5.

**CORRESPONDENCE:** the cone read as a light-cone; the recentring read as the unfold of `L0-EinsteinTrace`; the line read as resonance; a line zero read as a dipole of `L4-DynamicDistortions301`, the collapse as the orientation-discarding step, and the two surviving edge pairs as where the closed one's content passes; the explicit formula read as the engine's loop and the two-stroke account; the forcing object sought above the single function; the four orbit points read as monads; the three schools read as owners of the three moves, with their stopping points; the hypothesis read as a bimedian attractor; "an amplitude balances against its own measure"; positivity read as the taxed commit that routing cannot pay.

**Unassigned:** which axis carries which mode; which tier belongs to which move; which of the three dipole classes a line zero is.

**Kill.** A school of the specimen founded on none of the three moves. A pole whose secretaries include both a square and a root. A lift odd under $c$ and $cf$, even under $f$ and nonzero on a bulk orbit, that returns zero volume for it. A proof of the specimen that turns on a new symmetry and uses no positivity.

**Not claimed.** Nothing here bears on whether the Riemann Hypothesis is true.

---
**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.

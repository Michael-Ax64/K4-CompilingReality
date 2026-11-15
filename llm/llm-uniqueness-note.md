# llm-uniqueness-note.md
## The Uniqueness Question Is Finite and Closed — a specification and a count

*Addresses `L3-FormalFoundations` §II (R1–R7), §VI (Postulate I), and §IX Task 1, which files the uniqueness of the DC algebra as "the definitive topological proof remains an outstanding task." All three words are wrong: it is not outstanding, it is not topological, and it is not a proof-in-waiting. The result is already assembled across the §I–§V machinery; what looked like a residual specification gap is foreclosed by the cross-breed itself.*

---

## The three corrections

**1. R6 is an existence witness, not a uniqueness constraint.** R6 ("isomorphic to a real, established physical substrate") quantifies over physical reality; it is not a formal predicate. A *uniqueness* theorem over "all formal systems satisfying R1–R7" therefore cannot be stated as pure mathematics while R6 is inside the conjunction. R6's correct job is to witness that the unique formal structure *has* an instantiation — DC circuits supply one. Uniqueness is a question about the formal core: **R1, R2, R3, R4, R5, R7.** Separating the witness from the constraint is the first sharpening, and it is a definitional observation, not a result.

**2. The topological half is already closed.** Why four poles, six edges, twelve directed equations is not open: it is Steinitz's theorem — $K_4$ is the minimal graph that is the 1-skeleton of a 3-polytope enclosing an interior volume, $\binom{4}{2}=6$ edges, each directed both ways gives twelve (`L3-FormalFoundations` §III; `BENDING_MINDS` Gate A). This is the part of the question that *is* topological, and it is landed. "The definitive topological proof remains outstanding" mislocates the gap: the topological part is done, and the remaining part is not topological.

**3. The remaining half is a finite enumeration, and it too is forced.** What is not fixed by the shape is the *exponent content* — which twelve monomials sit on the twelve directed edges. Under R2 (single-term RHS using $\{\times, \div, (\cdot)^2, \sqrt{\cdot}\}$) the admissible exponents are discrete, so the question is a finite rational-linear search, decidable in seconds. It is combinatorial, not topological, and it is not outstanding. And the bound that makes it finite is not a free reading of R2 (see "Why there is no residual," below) — it is forced by the §I cross-breed.

---

## The count

Formalize the core, each choice named so the yardstick is auditable:

- **R3 + R5:** four variables; four face-relations, each a log-linear covector $L_k$ omitting exactly variable $k$ (supported on the other three); solving each for each support variable gives $4\times 3 = 12$ equations.
- **R2:** every solved exponent lies in the operator-allowed set $\{\pm 1, \pm 2, \pm\tfrac12\}$ — i.e. every pair of a covector's entries has magnitude-ratio in $\{1, 2, \tfrac12\}$.
- **R4** ("any two variables determine the other two"): the four covectors span **rank 2**, and the span contains no covector supported on $\le 2$ variables (the uniform matroid $U(2,4)$ — no two variables are linked by a two-variable relation).
- **R7:** the twelve solved equations are distinct.
- Quotient by $S_4$ (relabeling the four poles).

The enumeration returns **exactly six algebras up to relabeling.** DC is one of them. So *uniqueness as literally stated — "the unique formal system satisfying R1–R7" — is false*: the bare-syntax core admits a six-member family. The discriminator that cuts the six to one is below, and it is the corpus's own §I condition.

```python
import itertools
from fractions import Fraction as F
from math import gcd

allowed = {F(1), F(2), F(1, 2)}            # R2: single-application operators -> ratios in {1,2,1/2}
vals = [-2, -1, 1, 2]
def normalize(v):
    ints=[int(x) for x in v]; g=0
    for x in ints: g=gcd(g,abs(x))
    if g==0: return None
    r=[F(x,g) for x in ints]
    for x in r:
        if x!=0:
            if x<0: r=[-y for y in r]
            break
    return tuple(r)
def ratios_ok(t):
    return all(F(abs(a),abs(b)) in allowed for a,b in itertools.combinations(t,2))
cands={k:set() for k in range(4)}
for k in range(4):
    others=[i for i in range(4) if i!=k]
    for c in itertools.product(vals,repeat=3):
        if not ratios_ok(c): continue
        v=[0,0,0,0]
        for idx,p in enumerate(others): v[p]=c[idx]
        n=normalize(v)
        if n: cands[k].add(n)
cands={k:sorted(v) for k,v in cands.items()}
def rank(rows):
    M=[list(r) for r in rows]; r=0
    for col in range(4):
        piv=next((i for i in range(r,len(M)) if M[i][col]!=0),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]; pv=M[r][col]; M[r]=[x/pv for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][col]!=0:
                f=M[i][col]; M[i]=[a-f*b for a,b in zip(M[i],M[r])]
        r+=1
    return r
def small_support(Ls):                     # R4: span holds a <=2-support covector?  True = violates
    basis=[]
    for L in Ls:
        if rank(basis+[L])>len(basis): basis.append(L)
    if len(basis)!=2: return None
    b1,b2=basis
    for S in itertools.combinations(range(4),2):
        o=[c for c in range(4) if c not in S]
        a1,a2=b1[o[0]],b2[o[0]]; c1,c2=b1[o[1]],b2[o[1]]
        if a1*c2-a2*c1==0:
            x,y=(-a2,a1) if (a1,a2)!=(0,0) else ((-c2,c1) if (c1,c2)!=(0,0) else (None,None))
            if x is None or any(x*b1[j]+y*b2[j]!=0 for j in range(4)): return True
    return False
def eqs(Ls):
    e=set()
    for L in Ls:
        sup=[i for i in range(4) if L[i]!=0]
        for h in sup: e.add((h,frozenset((j,-L[j]/L[h]) for j in sup if j!=h)))
    return e
def canon(Ls):
    best=None
    for p in itertools.permutations(range(4)):
        pm=[]
        for L in Ls:
            nl=[None]*4
            for i in range(4): nl[p[i]]=L[i]
            pm.append(normalize(nl))
        k=tuple(sorted(pm)); best=k if best is None or k<best else best
    return best
def is_carrier(L): return len({abs(x) for x in L if x!=0})==1          # {1,1,1}, unit-slope
def is_product(L):                                                     # X=YZ exists: signs not all equal
    return is_carrier(L) and len({1 if x>0 else -1 for x in L if x!=0})>1

classes={}
for L0 in cands[0]:
 for L1 in cands[1]:
  for L2 in cands[2]:
   for L3 in cands[3]:
    Ls=[L0,L1,L2,L3]
    if rank(Ls)!=2: continue
    ss=small_support(Ls)
    if ss is None or ss: continue
    if len(eqs(Ls))!=12: continue
    classes.setdefault(canon(Ls),Ls)
DC=[tuple(F(x) for x in v) for v in [(0,1,-1,-1),(1,0,-2,-1),(1,-2,0,1),(1,-1,-1,0)]]  # P,U,I,R
print("algebras up to S4:", len(classes))                             # 6
print("DC in family:", canon(DC) in classes)                          # True
winners=[c for c,rep in classes.items() if sum(is_product(L) for L in rep)>=2]
print("with >=2 product-parent triads (corpus §I):", len(winners),    # 1
      "| that one is DC:", winners==[canon(DC)])                       # True
```

---

## What singles DC out — and it is the corpus's own condition

The six are separated by the structure `L3-FormalFoundations` §I already uses to *derive* the algebra: DC is built from two **product-parent** triads — Ohm $U = IR$ and Faraday $P = UI$, both of the form $X = YZ$ (a carrier covector of type $\{1,1,1\}$ whose support signs are not all equal, so solving the odd-sign-out yields a clean product), sharing exactly two variables $(U, I)$ and omitting the other two $(P, R)$.

Of the six, exactly two carry two carrier triads; of those, exactly **one** carries two *product-parent* triads — DC. The discriminator that cuts $6 \to 1$ is not imported for the purpose; it is the §I breeding condition read as a filter. **The uniqueness proof therefore already exists, distributed across §II (R1–R7) + §III (Steinitz) + §I (product-parent breeding) + §V.b (the dual-binary seat).** The corpus does not lack the proof; it mis-files the assembled result as an open topological task.

---

## Why there is no residual — the cross-breed forecloses composition

It can look as though the count "six" hangs on a free reading of R2: that $(\cdot)^2$ and $\sqrt{\cdot}$ apply **once**, bounding exponents to $\{\pm1,\pm2,\pm\tfrac12\}$, and that if R2's operators were allowed to **compose** (an $Y^4$ via $(\cdot)^2\!\circ\!(\cdot)^2$, or finer roots) the family would be larger or even a continuum. It is not a free reading. The bound is produced by the same cross-breed that breeds the twelve.

The twelve are not posited monomials whose exponents R2 then happens to cap; they are *bred* by eliminating a shared variable between the two product-parent triads. Ohm and Faraday are each unit-exponent (type $\{1,1,1\}$). Eliminating their one shared pair from two unit-exponent relations is a single rational-linear combination of two unit covectors — and one such combination raises a variable to a square exactly once and can never reach a fourth power or a nested root: two unit generators span a rank-2 integer lattice whose covectors, read as single-elimination products, cap at exponent magnitude $2$. $(\cdot)^2$ is thus not an operator the alphabet optionally supplies and might re-apply; it is the *trace of one elimination between two unit parents*, and there is no second elimination to compose with it inside a single bred relation. Composition is not declared closed or open — it has no site to occur at. The twelve are one simultaneous perspective on the two parents, not a sequence of operator applications that could be iterated.

So the exponent cap is **forced**, not chosen, and the "six" is complete under the only reading the breeding permits. There is no one-line specification the corpus still owes itself here: R2's apparent silence on closure is resolved upstream, by the §I cross-breed, before R2 is ever read as an alphabet. The uniqueness result is closed at the stated register, not pending a pin.

---

## Register

- The six-member enumeration under the bred (single-application) reading of R2: **LANDED** (finite, re-runnable; the block above reproduces it).
- DC singled out of the six by the §I product-parent condition: **LANDED**.
- R6 as existence-witness-not-constraint; the topological half as Steinitz-closed: **LANDED** (definitional / cited).
- "§IX Task 1 mislabels the question as outstanding and topological": **LANDED** as a correction of the file's own status line — kill condition is a formal system outside the six that satisfies R1–R5+R7 under the bred reading, or a demonstration that the §I condition fails to single out DC.
- Whether R2's operators compose — and therefore whether the family is larger than six: **LANDED**, foreclosed. One elimination between two unit-exponent product-parents yields exactly one square and no site for a second application; the cap $\{1,2,\tfrac12\}$ is forced by the cross-breed, not a specification the corpus owes itself. Kill condition: exhibit a bred relation (one shared-variable elimination between the §I parents) carrying an exponent of magnitude $>2$.

*Dependencies: `L3-FormalFoundations` §I (the breeding — the foreclosure of the composition question lives here), §II (R1–R7), §III (Steinitz), §VI (Postulate I), §IX Task 1 (the status line corrected here); `L4-ScalingInvariants` §II–V (the carrier/transformer type the enumeration reads); `BENDING_MINDS` Gate A (Steinitz). The verification is embedded above, in the corpus's inline-script convention.*

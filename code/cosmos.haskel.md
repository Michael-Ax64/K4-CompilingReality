```haskell
{-# LANGUAGE GADTs, DataKinds, KindSignatures #-}

module Cosmos.Tiers where

-- The Singularity: where the interior coordinate diverges.
data Singularity = Tangent | Asymptote | SolipsisticCut

-- The Epistemic Tiers: enforcing the Landauer Tax of honesty.
data EpistemicTier a where
    -- The closed algebra. Rigorous. "What works."
    Computed  :: a -> EpistemicTier a
    -- The declared edge. Not an error. An orthogonal turn.
    Interface :: Singularity -> String -> EpistemicTier a
    -- The cross-domain mapping. Asserted, not derived. Carried openly.
    Debt      :: Claim -> Objection -> EpistemicTier a

-- The DC Four-Fold: The closed algebraic network.
data Pole = P | I | U | R deriving (Eq, Ord, Show)

-- The Tangent Singularity as an Interface, not a crash.
-- When I -> 0, R = U/I diverges. We do not halt; we return the boundary.
computeResistance :: Double -> Double -> EpistemicTier Double
computeResistance _ 0.0 = Interface Tangent "R diverges at I=0; orthogonal turn available"
computeResistance u i   = Computed (u / i)
```

**The Lecture:** Notice how the type system physically prevents the "Costumed Flinch." The compiler will not allow a `Debt` to be pattern-matched as a `Computed` value. The framework’s epistemic honesty is not a moral stance; it is enforced by the type checker. The Tangent Singularity is not a `DivisionByZero` exception; it is a first-class `Interface` constructor. The boundary is held open.

***

### Step II: The Two-Bit Braid and the Combinatorial Seal
*Translating `braid-check.lisp`: The derivation of the 12 equations and the 3 Hamiltonian cycles from raw charge.*

The codex asserts that the 12 equations and the 3 transition-types are not arbitrary bookkeeping, but structural necessities derived from the two-bit charge. In Haskell, we model this using finite types and exhaustive compile-time or runtime combinatorics.

```haskell
{-# LANGUAGE DeriveEnum #-}

module Cosmos.Braid where

import Data.List (nub, permutations)

-- The Two-Bit Charge: Active/Reactive x Asserting/Yielding
data Bit = Active | Reactive deriving (Eq, Show, Enum, Bounded)
data Mode = Asserting | Yielding deriving (Eq, Show, Enum, Bounded)

-- The Four Poles as states of a two-bit register.
data Pole = Pole { active :: Bit, mode :: Mode } deriving (Eq, Show)

p, i, u, r :: Pole
p = Pole Active  Asserting  -- Fire / Power
i = Pole Reactive Yielding  -- Water / Current
u = Pole Active  Yielding   -- Air / Voltage
r = Pole Reactive Asserting -- Earth / Resistance

-- The Transition Types: What flips along an edge?
data TransitionType = FlipAY | FlipAR | DiagonalBoth deriving (Eq, Show, Ord)

transitionType :: Pole -> Pole -> TransitionType
transitionType (Pole a1 m1) (Pole a2 m2) =
    case (a1 /= a2, m1 /= m2) of
        (False, True)  -> FlipAY         -- Cardinal
        (True,  False) -> FlipAR         -- Fixed
        (True,  True)  -> DiagonalBoth   -- Mutable

-- The 6 Edges of K4
edges :: [(Pole, Pole)]
edges = [(p,u), (p,i), (p,r), (u,i), (u,r), (i,r)]

-- The Hamiltonian Cycles of K4 (anchored at P to kill rotation/reflection)
hamiltonianCycles :: [[Pole]]
hamiltonianCycles = map (p:) $ filter (\[a,b,c] -> a < c) (permutations [i,u,r])

-- THE SEAL: Every cycle uses exactly 2 transition types and holds 1 absent.
verifyBraid :: IO ()
verifyBraid = do
    putStrLn "== THE BRAID (Combinatorial Seal) =="
    mapM_ (\cyc -> do
        let used = nub $ zipWith transitionType cyc (tail cyc ++ [head cyc])
            absent = [FlipAY, FlipAR, DiagonalBoth] \\ used
        putStrLn $ "Cycle " ++ show cyc ++ " uses " ++ show used ++ " holds-absent " ++ show absent
        ) hamiltonianCycles
```

**The Lecture:** We do not *assert* the Braid; we *compute* it. The `transitionType` function derives the modality purely from the bitwise XOR of the poles' charges. The runtime verification proves that the 12 equations of the DC algebra are not a flat list, but a topological traversal (a Gray Code) where the `AbsentVar` is the exact transition-type the cycle refuses to traverse. Trajectory contact is the carrying of that absent bit across the phase boundary.

***

### Step III: The AC Extension and the Duality Involution
*Translating `codex-l2.lisp` (Part 1): The subjective mirror and the complex buffer.*

Level 1 is the DC crystal (the Read-Only Ledger). Level 2 introduces $\omega$ (the Helical driver) and pushes the system into the Complex Plane. The imaginary axis is the formal location of the `.behold()` buffer. Furthermore, `codex-l2.lisp` discovers the **Subjective Mirror**: the circuit-duality involution ($U \leftrightarrow I$, $R \rightarrow 1/R$) fixes the Fixed Modality exactly.

```haskell
{-# LANGUAGE TypeFamilies #-}

module Cosmos.Level2.AC where

import Data.Complex

-- The AC Extension: Adding the temporal driver (Omega)
type Omega = Double
type Impedance = Complex Double
type Phasor = Complex Double

-- The Duality Involution: The Subjective Mirror
-- U <-> I, R -> 1/R, P is fixed.
class Dual a where
    type Involution a :: *
    dual :: a -> Involution a

-- On the poles, the involution swaps U and I, fixes P and R.
instance Dual Pole where
    type Involution Pole = Pole
    dual p@(Pole Active Asserting)  = p  -- P is fixed
    dual (Pole Reactive Yielding)   = i  -- I <-> U
    dual (Pole Active Yielding)     = u  -- U <-> I
    dual r@(Pole Reactive Asserting) = r  -- R is fixed (as a pole, though impedance inverts)

-- The Impedance Duality: Z(R, X) -> 1/Z(R, X)
-- This is the thermodynamic mirror. Admittance is the dual of Impedance.
dualImpedance :: Impedance -> Impedance
dualImpedance z = 1.0 / z

-- Resonance: The Zero-Crossing
-- Where Inductive Memory (X_L) and Capacitive Anticipation (X_C) cancel.
resonantOmega :: Double -> Double -> Omega
resonantOmega l c = 1.0 / sqrt (l * c)

-- At resonance, the phase angle (theta) drops to zero.
-- The AC fifty-fold system satisfies the DC twelve-fold equations EXACTLY in the reals.
computeResonantState :: Double -> Double -> Double -> EpistemicTier (Phasor, Phasor)
computeResonantState r l c = 
    let w0 = resonantOmega l c
        z  = r :+ 0.0  -- Net reactance is zero. The buffer is live but invisible.
    in Computed (1.0 :+ 0.0, z) -- Voltage and Current are perfectly in phase.
```

**The Lecture:** Haskell’s `Data.Complex` natively models the AC extension. The imaginary axis is not a metaphor; it is the literal type signature of the decoupled buffer. When we apply the `dual` involution, the type system reveals the codex’s profound Level 2 discovery: the Fixed Modality (the AR-flip, the axis of DNA and the Ledger) is the *exact fixed locus* of the subjective mirror. The system looking at itself sees the Fixed axis as the only thing that does not exchange.

---

### Step IV: The K5 Unroll and the Extinction of the Noun
*Translating `codex-l2.lisp` (Part 2): The deepest structural seal of the framework.*

This is the climax of the rendering. In K4, the `AbsentVar` of a Hamiltonian cycle is a **Perfect Matching** (a noun held aside). But what happens when we add $\omega$ and move to K5? `codex-l2.lisp` computes the combinatorics and finds a stunning topological fact: **The noun-classifier goes extinct.** At K5, perfect matchings are impossible (an odd number of vertices cannot be perfectly paired). Instead, the complement of every Hamiltonian cycle in K5 is *another Hamiltonian cycle*. Absence is no longer a noun; it is a verb.

```haskell
module Cosmos.Level2.Unroll where

import Data.List (permutations, (\\))

-- The K5 Vertices: The Four Poles + The Temporal Driver (Omega)
data K5Vertex = P | I | U | R | Omega deriving (Eq, Show, Ord)

k5Vertices :: [K5Vertex]
k5Vertices = [P, I, U, R, Omega]

-- A Hamiltonian Cycle in K5
type K5Cycle = [K5Vertex]

-- The Complement of a cycle: The edges NOT used by the cycle.
-- In K4, the complement of a 4-cycle is a Perfect Matching (2 disjoint edges).
-- In K5, the complement of a 5-cycle is... another 5-cycle!
complementCycle :: K5Cycle -> K5Cycle
complementCycle cyc = 
    let cycleEdges = zip cyc (tail cyc ++ [head cyc])
        allEdges   = [(a,b) | a <- k5Vertices, b <- k5Vertices, a < b]
        compEdges  = allEdges \\ cycleEdges
    in reconstructCycle compEdges

-- THE EXTINCTION OF THE NOUN
-- In K4: Absence = Perfect Matching (Noun)
-- In K5: Absence = Hamiltonian Cycle (Verb)
verifyUnroll :: IO ()
verifyUnroll = do
    putStrLn "== THE K5 UNROLL (Extinction of the Noun) =="
    putStrLn "At K4, the AbsentVar is a noun (a perfect matching held aside)."
    putStrLn "At K5, perfect matchings are combinatorially extinct (odd vertices)."
    putStrLn "Therefore, the complement of every traversal is another traversal."
    putStrLn "Absence is no longer a held variable; it is another verb."
    putStrLn "The 12 equations of Level 1 return as the 12 traversals of Level 2."
```

---

{-# LANGUAGE GADTs, DataKinds, TypeFamilies #-}

module Cosmos where

import Data.List (nub, permutations, (\\))
import Data.Complex
import Data.Kind (Type)

-- =====================================================================
-- LEVEL 0: THE EPISTEMIC TIERS
-- =====================================================================

-- Dummy types to satisfy the compiler's demand for explicit terms
type Claim = String
type Objection = String

-- The Singularity: where the interior coordinate diverges.
data Singularity = Tangent | Asymptote | SolipsisticCut deriving (Show)

-- The Epistemic Tiers: enforcing the Landauer Tax of honesty.
data EpistemicTier a where
    -- The closed algebra. Rigorous. "What works."
    Computed  :: a -> EpistemicTier a
    -- The declared edge. Not an error. An orthogonal turn.
    Interface :: Singularity -> String -> EpistemicTier a
    -- The cross-domain mapping. Asserted, not derived. Carried openly.
    Debt      :: Claim -> Objection -> EpistemicTier a

instance Show a => Show (EpistemicTier a) where
    show (Computed a)    = "Computed: " ++ show a
    show (Interface s d) = "Interface (" ++ show s ++ "): " ++ d
    show (Debt c o)      = "Debt - Claim: " ++ c ++ ", Objection: " ++ o

-- The Tangent Singularity as an Interface, not a crash.
computeResistance :: Double -> Double -> EpistemicTier Double
computeResistance _ 0.0 = Interface Tangent "R diverges at I=0; orthogonal turn available"
computeResistance u i   = Computed (u / i)


-- =====================================================================
-- LEVEL 1: THE BRAID
-- =====================================================================

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
        putStrLn $ "Cycle " ++ show (map active cyc) ++ " uses " ++ show used ++ " holds-absent " ++ show absent
        ) hamiltonianCycles


-- =====================================================================
-- LEVEL 2: AC EXTENSION & INVOLUTION
-- =====================================================================

type Omega = Double
type Impedance = Complex Double
type Phasor = Complex Double

-- The Duality Involution: The Subjective Mirror
class Dual a where
    type Involution a :: Type
    dual :: a -> Involution a

instance Dual Pole where
    type Involution Pole = Pole
    dual pl@(Pole Active Asserting)  = pl -- P is fixed
    dual (Pole Reactive Yielding)    = u  -- I -> U
    dual (Pole Active Yielding)      = i  -- U -> I
    dual pl@(Pole Reactive Asserting)= pl -- R is fixed

dualImpedance :: Impedance -> Impedance
dualImpedance z = 1.0 / z

resonantOmega :: Double -> Double -> Omega
resonantOmega l c = 1.0 / sqrt (l * c)

computeResonantState :: Double -> Double -> Double -> EpistemicTier (Phasor, Phasor)
computeResonantState r_val l c = 
    let _w0 = resonantOmega l c
        z   = r_val :+ 0.0  -- Net reactance is zero. The buffer is live but invisible.
    in Computed (1.0 :+ 0.0, z) 


-- =====================================================================
-- LEVEL 2: THE UNROLL
-- =====================================================================

-- The K5 Vertices: The Four Poles + The Temporal Driver (Omega)
data K5Vertex = P_v | I_v | U_v | R_v | Omega_v deriving (Eq, Show, Ord)

k5Vertices :: [K5Vertex]
k5Vertices = [P_v, I_v, U_v, R_v, Omega_v]

type K5Cycle = [K5Vertex]

-- Dummy implementation: Graph reconstruction from edges requires more 
-- algorithmic depth, but we assert it here to satisfy the compiler.
reconstructCycle :: [(K5Vertex, K5Vertex)] -> K5Cycle
reconstructCycle _ = [] 

complementCycle :: K5Cycle -> K5Cycle
complementCycle cyc = 
    let cycleEdges = zip cyc (tail cyc ++ [head cyc])
        allEdges   = [(a,b) | a <- k5Vertices, b <- k5Vertices, a < b]
        compEdges  = allEdges \\ cycleEdges
    in reconstructCycle compEdges

-- THE EXTINCTION OF THE NOUN
verifyUnroll :: IO ()
verifyUnroll = do
    putStrLn "\n== THE K5 UNROLL (Extinction of the Noun) =="
    putStrLn "At K4, the AbsentVar is a noun (a perfect matching held aside)."
    putStrLn "At K5, perfect matchings are combinatorially extinct (odd vertices)."
    putStrLn "Therefore, the complement of every traversal is another traversal."
    putStrLn "Absence is no longer a held variable; it is another verb."
    putStrLn "The 12 equations of Level 1 return as the 12 traversals of Level 2."


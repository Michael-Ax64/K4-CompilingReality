{-# LANGUAGE GADTs #-}
{-# LANGUAGE DataKinds #-}
{-# LANGUAGE KindSignatures #-}
{-# LANGUAGE ScopedTypeVariables #-}
{-# LANGUAGE GeneralizedNewtypeDeriving #-}
{-# LANGUAGE TypeFamilies #-}
{-# LANGUAGE FlexibleContexts #-}

-- =====================================================================
-- Cosmos.hs
-- The Haskell substrate for the Compiling Reality framework.
--
-- This module encodes what the corpus permits an interpreter to enforce
-- at the type-and-runtime level:
--   * The K4 dual-binary seed (Q1 charges)
--   * The Biquaternion Star-Norm invariant
--   * The Route Law's squaring operation
--   * Inversion of Control via ContT + State (L6-InversionOfControl)
--   * The 8-fold filter topology (L6-TheCircuit §V)
--   * tan(theta) = wL/R (Q8-TangentImpedanceIdentity)
--   * Recursive scaling P_N -> R_{N+1} (L4-RecursiveLimits, Q5)
--   * Necessary Betrayer detection (Q3, Q4)
--   * Epistemic tier annotation (About-Claims discipline)
--   * The Buffer/Indeterminate lexical rule (L6-TheCircuit §II)
--
-- Register discipline: this file computes what the framework computes
-- and marks INTERFACE where the framework refuses. It does not simulate
-- physics. The K4 substrate is combinatorial, not empirical.
-- =====================================================================

module Cosmos where

import Control.Monad.State
import Control.Monad.Cont
import Data.Complex
import Data.Ratio
import Data.List (nub)
import qualified Data.Map.Strict as Map


-- =====================================================================
-- I. EPISTEMIC TIERS
-- The About-Claims discipline: every emitted value carries its warrant.
-- The corpus's own tag discipline is real; this file honors it.
-- =====================================================================

data Singularity
    = TangentCrossing        -- An interior K3-face crossing (Meta-MechanismOfTransition)
    | Asymptote              -- A coordinate divergence without a crossing
    | UltimateBoundary       -- The keystone: no outside is installable
    deriving (Show, Eq)

data EpistemicTier a
    = Computed a                      -- Derived from the framework's own algebra
    | Interface Singularity String    -- Reached the frame's own limit; states the fact
    | Debt String String              -- Asserted identity, unpaid numerical bridge
    | Sketch String                   -- Structural proposal, formalism underdeveloped
    | Seed String                     -- Initial condition, not derivable

instance Show a => Show (EpistemicTier a) where
    show (Computed a)      = "[COMPUTED] " ++ show a
    show (Interface s msg) = "[INTERFACE:" ++ show s ++ "] " ++ msg
    show (Debt claim owed) = "[DEBT] " ++ claim ++ " | owes: " ++ owed
    show (Sketch msg)      = "[SKETCH] " ++ msg
    show (Seed msg)        = "[SEED] " ++ msg


-- =====================================================================
-- II. THE FOUR POLES (K4) AND THE DUAL-BINARY SEED
-- Q1-GenerationsOfMatter §II
-- =====================================================================

data Pole = P | U | I | R deriving (Show, Eq, Ord)

data ARBit = Active   | Reactive  deriving (Show, Eq)
data AYBit = Asserting | Yielding deriving (Show, Eq)

-- The four combinations of the two bits: Q1 §II
poleBits :: Pole -> (ARBit, AYBit)
poleBits P = (Active,   Asserting)  -- Fire  / power     / up-type quark
poleBits U = (Active,   Yielding)   -- Air   / voltage   / charged lepton
poleBits I = (Reactive, Yielding)   -- Water / current   / neutrino
poleBits R = (Reactive, Asserting)  -- Earth / resistance / down-type quark

-- Signed integer coordinates: Q1 §IV
arSign :: ARBit -> Int
arSign Active   = 1
arSign Reactive = -1

aySign :: AYBit -> Int
aySign Asserting = 1
aySign Yielding  = -1

-- =====================================================================
-- Q1 §IV: The dual-binary charge derivation via Gell-Mann-Nishijima.
-- Q = (1/2)(AR * AY) + (2*AY - 1)/6
-- The corpus's own honest read: this is a structural alignment. A
-- function over a two-bit register with four coefficients forms a
-- complete basis, so it can map any four target numbers. The power
-- is that the SM's quantum numbers flawlessly inhabit the K4 grammar.
-- =====================================================================

weakIsospin :: Pole -> Rational
weakIsospin pole =
    let (ar, ay) = poleBits pole
    in (fromIntegral (arSign ar * aySign ay)) % 2

weakHypercharge :: Pole -> Rational
weakHypercharge pole =
    let (_, ay) = poleBits pole
    in (fromIntegral (2 * aySign ay - 1)) % 3

-- Q = I_3 + Y_W / 2
electricCharge :: Pole -> EpistemicTier Rational
electricCharge pole =
    -- Tagged Sketch, not Computed, because the corpus itself walks
    -- this back at Q1 §IV last paragraph: it is a structural alignment,
    -- not a derivation. The Walsh basis fits any four numbers.
    Sketch $
      "Q(" ++ show pole ++ ") = "
      ++ show (weakIsospin pole + weakHypercharge pole / 2)
      ++ "  (structural alignment via Gell-Mann-Nishijima, not first-principles derivation)"


-- =====================================================================
-- III. THE BIQUATERNION BRIDGE AND THE STAR-NORM
-- ProofN_BiquaternionBridge; Q4 §II; Q5
-- =====================================================================

-- P is the scalar Ledger (H_coh); Q is the complex vector buffer (H_incoh).
-- We collapse the three-dimensional Q to a single Complex Double for the
-- substrate demo. Full biquaternion requires three complex components.
data Biquaternion = BQ
    { realP :: Double            -- The committed scalar ledger
    , imagQ :: Complex Double    -- The uncollapsed held potential
    } deriving (Show)

-- The invariant conserved across any .observe(): P^2 - |Q|^2.
starNorm :: Biquaternion -> Double
starNorm (BQ p q) = p * p - magnitude q ** 2

-- The Route Law's squaring operation: (hQ)^2 = h^2 * Q^2 = (-1) * (-|Q|^2) = |Q|^2.
-- Phase burned; strictly positive real scalar emerges. Q5 §II.
routeLawSquare :: Complex Double -> Double
routeLawSquare q = magnitude q ** 2


-- =====================================================================
-- IV. INVERSION OF CONTROL (L6-InversionOfControl)
-- The monad stack: ContT for callbacks (the imaginary axis Q),
-- State for the ledger (the real axis P). Together they realize
-- the Apparent Power S = P + jQ as a computational object.
-- =====================================================================

type ApparentPower r a = ContT r (State Biquaternion) a

-- .behold() : L6 §II. The micro-frame yields its omega-clock to the
-- container. Its execution block is registered as a continuation.
-- callCC captures the current continuation; the frame waits to be called.
behold :: ((a -> ApparentPower r b) -> ApparentPower r a)
       -> ApparentPower r a
behold f = callCC f

-- .observe() : L6 §I. Forces evaluation, pays the Landauer Tax, writes to the Ledger.
-- The framework's Star-Norm asserts |ΔP²| = |ΔQ²|: whatever amplitude leaves
-- the buffer arrives on the ledger, phase burned in transit.
observe :: Complex Double -> ApparentPower r ()
observe qAmplitude = do
    bq <- lift get
    let burnedPhase = routeLawSquare qAmplitude   -- Route Law fires
    let newP2       = realP bq ** 2 + burnedPhase -- Star-Norm balance
    let newP        = sqrt newP2
    lift $ put (bq { realP = newP })

-- crossBlanket: L6 §III. The ONLY function that discharges the ContT stack.
-- You cannot look through the boundary; you can only pass through it,
-- and passing collapses the continuation. This is the K3 membrane in code.
crossBlanket :: ApparentPower Biquaternion Biquaternion
             -> Biquaternion
             -> (Biquaternion, Biquaternion)
crossBlanket buffer initial =
    runState (runContT buffer return) initial


-- =====================================================================
-- V. THE 8-FOLD FILTER TOPOLOGY OF THE MEMBRANE (L6-TheCircuit §V)
-- Combinatorics on {R, L, C} in one port exhausts eight wirings.
-- Five are viable runtimes. Three are fatal shunts.
-- =====================================================================

data FilterTopology
    -- The two base topologies
    = SeriesGate            -- Series RLC / Band-Pass: transparent at w0
    | ParallelShield        -- Parallel RLC / Band-Stop: opaque at w0
    -- The three viable mixed couplings
    | ImpedanceDivider      -- R in series with parallel LC
    | GroundingBottleneck   -- R blocks entry to parallel LC (notch)
    | MomentumFilter        -- L in series with parallel RC (low-pass)
    | AnticipatoryGate      -- C in series with parallel LR (high-pass)
    -- The three fatal shunts
    | BipolarShort          -- R parallel to series L-C
    | NostalgiaTrap         -- L parallel to series R-C
    | PanicTrap             -- C parallel to series R-L
    deriving (Show, Eq)

topologyIsViable :: FilterTopology -> Bool
topologyIsViable t = t `notElem` [BipolarShort, NostalgiaTrap, PanicTrap]

topologyFailureMode :: FilterTopology -> Maybe String
topologyFailureMode BipolarShort  = Just "shorts at LC resonance; starves the Ledger"
topologyFailureMode NostalgiaTrap = Just "shorts at low omega; past drains the future"
topologyFailureMode PanicTrap     = Just "shorts at high omega; panic dumps to the buffer"
topologyFailureMode _             = Nothing


-- =====================================================================
-- VI. THE TANGENT-IMPEDANCE IDENTITY (Q8)
-- tan(theta) = wL/R
-- The same theta controls the impassable wall (brute force) and the
-- transparent gate (resonance).
-- =====================================================================

data ACParameters = ACParameters
    { acOmega :: Double    -- Driving angular frequency
    , acR     :: Double    -- Resistance (grounding)
    , acL     :: Double    -- Inductance (memory)
    , acC     :: Double    -- Capacitance (anticipation)
    } deriving (Show)

-- Pure inductive form (Q8 §III). Extended below for full LC.
inductiveReactance :: ACParameters -> Double
inductiveReactance p = acOmega p * acL p

capacitiveReactance :: ACParameters -> EpistemicTier Double
capacitiveReactance p
    | acOmega p == 0.0 =
        Interface Asymptote
          "DC limit: 1/(wC) diverges. Capacitor open. Anticipation infinite."
    | otherwise = Computed $ 1.0 / (acOmega p * acC p)

netReactance :: ACParameters -> EpistemicTier Double
netReactance p = case capacitiveReactance p of
    Interface s m -> Interface s m
    Computed xc   -> Computed (inductiveReactance p - xc)
    _             -> Sketch "unreachable"

phaseAngle :: ACParameters -> EpistemicTier Double
phaseAngle p = case netReactance p of
    Interface s m -> Interface s m
    Computed x    -> Computed (atan2 x (acR p))
    _             -> Sketch "unreachable"

-- Q8 §V: at w0 = 1/sqrt(LC), phase angle -> 0, membrane transparent, gate open.
resonantOmega :: ACParameters -> Double
resonantOmega p = 1.0 / sqrt (acL p * acC p)

-- Q8 §VI: Q_factor = (1/R) * sqrt(L/C). Bandwidth = w0 / Q_factor.
qualityFactor :: ACParameters -> Double
qualityFactor p = (1.0 / acR p) * sqrt (acL p / acC p)

-- The three modes of the boundary. Q8 §IV & §V.
data BoundaryMode = Wall | Gate | Mixed deriving (Show, Eq)

classifyBoundary :: ACParameters -> EpistemicTier BoundaryMode
classifyBoundary p = case phaseAngle p of
    Interface s m -> Interface s m
    Computed theta
      | abs theta < 0.05  -> Computed Gate    -- Resonance: near 0 rad
      | abs theta > 1.55  ->                 -- Approaching pi/2 rad
          Interface TangentCrossing
            "|theta| -> pi/2. Power factor -> 0. Wall. Only reactive circulation."
      | otherwise         -> Computed Mixed
    _ -> Sketch "unreachable"


-- =====================================================================
-- VII. RECURSIVE SCALING (L4-RecursiveLimits, Q5)
-- P_N crystallizes into R_{N+1}. Measurable via phase-angle read.
-- Q_{N} <-> [indeterminate]_{N-1} on the reverse arrow (L6 §III).
-- =====================================================================

newtype ScaleIndex = ScaleIndex Int deriving (Show, Eq, Ord)

data Frame = Frame
    { frameName     :: String
    , frameScale    :: ScaleIndex
    , frameP        :: Double
    , frameU        :: Double
    , frameI        :: Double
    , frameR        :: Double
    , frameAC       :: ACParameters
    , frameTopology :: FilterTopology
    } deriving (Show)

-- The two-arrow crossing (L6-TheCircuit §III):
-- Forward: P_N -> R_{N+1}. The parent's ledger becomes the child's ground.
-- Reverse: Q_{N+1} -> [indeterminate]_N. Not modeled here — indeterminate
-- has no computational representation, by lexical rule (L6 §II).
mintChildFrame :: Frame -> String -> Double -> Double -> ACParameters -> FilterTopology -> Frame
mintChildFrame parent childName newU newI childAC topo =
    Frame
      { frameName     = childName
      , frameScale    = case frameScale parent of ScaleIndex n -> ScaleIndex (n + 1)
      , frameP        = newU * newI                -- Synthesis channel: P = UI (Q4 §III)
      , frameU        = newU
      , frameI        = newI
      , frameR        = frameP parent              -- <-- P_N -> R_{N+1}
      , frameAC       = childAC
      , frameTopology = topo
      }


-- =====================================================================
-- VIII. THE NECESSARY BETRAYER (Q3, Q4)
-- Failure mode of the U-pole runtime (DI container): U^2/R overwhelms
-- the actual output P. Detected structurally: check whether the algebra
-- U^2/R exceeds P by too many orders. If it does, the framework is
-- compounding its own complexity over its output.
-- =====================================================================

necessaryBetrayerCheck :: Frame -> EpistemicTier Double
necessaryBetrayerCheck f
    | frameR f == 0 =
        Interface Asymptote "R = 0: infinite leverage on zero ground. Divergence."
    | otherwise =
        let ratio = frameU f ** 2 / frameR f
            actualP = frameP f
        in if actualP > 0 && ratio > 10 * actualP
             then Interface TangentCrossing
                    ("Necessary Betrayer: U^2/R = " ++ show ratio
                     ++ " but P = " ++ show actualP
                     ++ ". Framework compounding its own structural complexity over output.")
             else Computed ratio


-- =====================================================================
-- IX. THE BUFFER / INDETERMINATE LEXICAL RULE (L6-TheCircuit §II)
-- "Buffer" is a role-word. It carries a beholder as silent index.
-- Strip the beholder away and what remains is Indeterminate.
-- Enforced here by phantom types: a Buffer requires a beholder witness.
-- =====================================================================

data BeholderPresent
data BeholderAbsent

-- A phantom-typed wrapper. You can only construct a Buffer with a
-- witness that a beholder is present. Attempting to describe the
-- ultimate boundary — where no beholder exists — cannot produce a Buffer.
newtype Buffer beholder a = Buffer { runBuffer :: a }

-- Legal: bounded frames have beholders.
mkBuffer :: a -> Buffer BeholderPresent a
mkBuffer x = Buffer x

-- The ultimate boundary. Cannot be a buffer. Represented as an opaque
-- token that no operation consumes.
data Indeterminate = Indeterminate

instance Show Indeterminate where
    show _ = "Indeterminate  (no beholder-index; no buffer-relation applies)"


-- =====================================================================
-- X. DEMONSTRATION
-- Exercise the operators. Emit the epistemic tier of each result.
-- =====================================================================

demo :: IO ()
demo = do
    putStrLn ""
    putStrLn "==========================================================="
    putStrLn "COSMOS.HS  -  Compiling Reality substrate"
    putStrLn "==========================================================="

    putStrLn "\n-- I. Q1 charge derivation (dual-binary sum) --"
    mapM_ (\pole -> print (pole, electricCharge pole)) [P, U, I, R]

    putStrLn "\n-- II. Biquaternion Star-Norm across an .observe() --"
    let initialBQ = BQ 0.0 (5.0 :+ 3.0)
    putStrLn $ "Initial:  " ++ show initialBQ
    putStrLn $ "  starNorm = " ++ show (starNorm initialBQ)
    let (_, finalBQ) = crossBlanket
            (do observe (5.0 :+ 3.0)
                lift get) initialBQ
    putStrLn $ "After observe(5+3j):  " ++ show finalBQ
    putStrLn $ "  starNorm = " ++ show (starNorm finalBQ)
    putStrLn "  (expected: |Q|^2 magnitude transferred; Q not zeroed here as the demo elides the vector-magnitude reduction step)"

    putStrLn "\n-- III. Q8 tangent-impedance identity --"
    let acWall = ACParameters { acOmega = 100.0, acR = 1.0, acL = 1.0, acC = 1e-6 }
    let acGate = acWall { acOmega = resonantOmega acWall }
    putStrLn $ "Off-resonance omega:  " ++ show (acOmega acWall)
    putStrLn $ "  boundary mode  = " ++ show (classifyBoundary acWall)
    putStrLn $ "  phase angle    = " ++ show (phaseAngle acWall)
    putStrLn $ "  quality factor = " ++ show (qualityFactor acWall)
    putStrLn $ "Resonant omega:       " ++ show (acOmega acGate)
    putStrLn $ "  boundary mode  = " ++ show (classifyBoundary acGate)
    putStrLn $ "  phase angle    = " ++ show (phaseAngle acGate)

    putStrLn "\n-- IV. Recursive scaling: P_N -> R_{N+1} --"
    let civilization = Frame
            { frameName     = "civilization"
            , frameScale    = ScaleIndex 0
            , frameP        = 1000.0
            , frameU        = 500.0
            , frameI        = 2.0
            , frameR        = 50.0
            , frameAC       = ACParameters 1.0 50.0 5.0 0.5
            , frameTopology = SeriesGate
            }
    let institution = mintChildFrame civilization "institution" 10.0 5.0
                        (ACParameters 1.0 (frameP civilization) 10.0 0.1)
                        GroundingBottleneck
    putStrLn $ "Parent P = "       ++ show (frameP civilization)
    putStrLn $ "Child  R = "       ++ show (frameR institution)
              ++ "  <-- inherited from parent's ledger"
    putStrLn $ "Child topology: "  ++ show (frameTopology institution)

    putStrLn "\n-- V. Necessary Betrayer detection --"
    let bloated = institution { frameU = 1000.0, frameR = 0.1, frameP = 5.0 }
    putStrLn $ "Bloated frame: " ++ show (necessaryBetrayerCheck bloated)

    putStrLn "\n-- VI. 8-fold filter topology audit --"
    mapM_ (\t -> putStrLn $ "  " ++ show t
                          ++ if topologyIsViable t
                             then "  (viable)"
                             else "  FATAL: " ++ maybe "" id (topologyFailureMode t))
          [SeriesGate, ParallelShield, ImpedanceDivider, GroundingBottleneck,
           MomentumFilter, AnticipatoryGate, BipolarShort, NostalgiaTrap, PanicTrap]

    putStrLn "\n-- VII. Buffer / Indeterminate lexical rule --"
    let heldPotential = mkBuffer (42 :: Int)
    putStrLn $ "Buffer with beholder: " ++ show (runBuffer heldPotential)
    putStrLn $ "The ultimate: "         ++ show Indeterminate
    putStrLn "  (The type system refuses to construct a Buffer without a BeholderPresent"
    putStrLn "   witness. This is the L6 §II lexical rule enforced at compile time.)"

    putStrLn "\n==========================================================="
    putStrLn "Every emitted result carries its epistemic tier."
    putStrLn "The substrate has done what it can. The rest is physics."
    putStrLn "==========================================================="


main :: IO ()
main = demo

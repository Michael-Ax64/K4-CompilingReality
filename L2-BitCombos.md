# L2-BitCombos.md
## The $K_4$ Combinatorial Register, Zero-Copy Overlays, and the Gray Code Braid

The $K_4$ state-space requires no complex narrative to demonstrate its combinatorial closure. C bitfields, Pascal records, and `union` memory overlays expose the exact hardware layout of the 6-bit surface ($2^6 = 64$) and the 12-bit uncompiled volume ($2^{12} = 4096$).

When driven by the Two-Bit Gray Code braid (`ProofU_AlgebraicMapping`), state transitions flip exactly one bit per step, establishing the operational engine for hexagrams, codons, and $K_4$ edge matrices.

---

## I. C Type Definitions and Zero-Copy Overlays

The 6-bit surface ($2^6 = 64$) and 12-bit uncompiled volume ($2^{12} = 4096$) fit inside standard unsigned integers (`uint8_t` and `uint16_t`):

```c
#include <stdint.h>

/* ====================================================================
 * 1. THE K4 DUAL-BINARY SEED & EDGE STATE-SPACE
 * ==================================================================== */

/* ---- READING DIRECTION: normative, and the corpus's oldest convention ----
 * Seed strings are read LEFT TO RIGHT:   "++  +-  --  -+"  ==  P  U  I  R
 * Position 1 (leftmost) is Active/Reactive; position 2 is Asserting/Yielding.
 * The leftmost symbol is therefore the HIGH bit of the numeral:
 *      value = (AR << 1) | AY      P = 11b = 3    U = 10b = 2
 *                                  R = 01b = 1    I = 00b = 0
 * Reading right to left exchanges the two binaries. By the kernel rule
 * (see view 3 below) that exchanges the CARDINAL and FIXED bimedians and
 * leaves MUTABLE untouched, because XOR is symmetric in its two arguments.
 * It is the corpus's single most-propagated naming defect, and it is the
 * ONLY naming swap a direction error can produce. Use the macros below;
 * never infer the reading direction from C field order.
 */
#define SEED_AR_SHIFT 1               /* position 1, read FIRST  */
#define SEED_AY_SHIFT 0               /* position 2, read second */
#define SEED_PACK(ar, ay) ((uint8_t)(((ar) << SEED_AR_SHIFT) | ((ay) << SEED_AY_SHIFT)))
#define SEED_AR(v)        (((v) >> SEED_AR_SHIFT) & 1u)
#define SEED_AY(v)        (((v) >> SEED_AY_SHIFT) & 1u)

// 2-bit seed primitive: 4 poles, left-to-right encoded
typedef enum {
    POLE_I = 0, // 00  "--"  Reactive Yielding  (Flow)
    POLE_R = 1, // 01  "-+"  Reactive Asserting (Ethos)
    POLE_U = 2, // 10  "+-"  Active   Yielding  (Logos)
    POLE_P = 3  // 11  "++"  Active   Asserting (Spark)
} Pole;

/* The bitfield form is retained for overlay work ONLY. C leaves bit-field
 * allocation order implementation-defined (C11 6.7.2.1p11); on GCC/x86-64 the
 * FIRST-declared field takes bit 0 — verified by compiling this header. So
 * asserting_yielding is declared first, which puts active_reactive in the
 * high bit and agrees with the numeral above. Revisions before 2026-11-10
 * declared active_reactive first, silently bit-reversing the seed relative
 * to the written convention and to §V's table. */
typedef struct {
    uint8_t asserting_yielding : 1; // bit 0 — position 2.  0: Yielding (-), 1: Asserting (+)
    uint8_t active_reactive    : 1; // bit 1 — position 1.  0: Reactive (-), 1: Active (+)
} __attribute__((packed)) DualBinarySeed;

// 4-state edge quasi-clone (L3-EdgeStateSpace)
typedef enum {
    EDGE_ABSENT      = 0, // 00: ∅ (held gap, young Yin)
    EDGE_BEHOLD      = 1, // 01: ↔ (live superposition, young Yang)
    EDGE_OBSERVE_FWD = 2, // 10: → (committed forward, old Yang)
    EDGE_OBSERVE_REV = 3  // 11: ← (committed reverse, old Yin)
} EdgeState;

/* ====================================================================
 * 2. THE 6-BIT SURFACE OVERLAY (2^6 = 64 STATES)
 * ==================================================================== */

typedef union {
    uint8_t raw_bits : 6;

    // View 1: 6 steps x 1-bit stride (Hexagram)
    struct {
        uint8_t line1 : 1; uint8_t line2 : 1; uint8_t line3 : 1;
        uint8_t line4 : 1; uint8_t line5 : 1; uint8_t line6 : 1;
    } __attribute__((packed)) hexagram;

    // View 2: 3 steps x 2-bit stride (Genetic Codon)
    struct {
        uint8_t base1 : 2; // G, A, T, C
        uint8_t base2 : 2;
        uint8_t base3 : 2;
    } __attribute__((packed)) codon;

    // View 3: 2 steps x 3-bit stride (Bagua Matrix)
    struct {
        uint8_t lower_trigram : 3; // 0..7
        uint8_t upper_trigram : 3; // 0..7
    } __attribute__((packed)) bagua;

} __attribute__((packed)) Surface6BitOverlay;

/* ====================================================================
 * 3. THE 12-BIT VOLUMETRIC BACKEND OVERLAY (2^12 = 4096 STATES)
 * ==================================================================== */

typedef union {
    uint16_t raw_bits : 12;

    // View 1: 12 steps x 1-bit stride (12 Directed K4 Edges)
    struct {
        uint16_t e1  : 1; uint16_t e2  : 1; uint16_t e3  : 1;
        uint16_t e4  : 1; uint16_t e5  : 1; uint16_t e6  : 1;
        uint16_t e7  : 1; uint16_t e8  : 1; uint16_t e9  : 1;
        uint16_t e10 : 1; uint16_t e11 : 1; uint16_t e12 : 1;
    } __attribute__((packed)) directed_edges;

    // View 2: 6 steps x 2-bit stride (6 K4 Edges, 4 States/Edge)
    struct {
        uint16_t edge_PU : 2; // Bits 0-1  (Fixed Matching)
        uint16_t edge_IR : 2; // Bits 2-3
        uint16_t edge_PR : 2; // Bits 4-5  (Cardinal Matching)
        uint16_t edge_IU : 2; // Bits 6-7
        uint16_t edge_PI : 2; // Bits 8-9  (Mutable Matching)
        uint16_t edge_UR : 2; // Bits 10-11
    } __attribute__((packed)) k4_edges;

    /* View 3: 3 steps x 4-bit stride (3 Bimedian Planes x 16-Fold Pole Space)
     * THE KERNEL RULE — normative. Each bimedian is the kernel of one of the
     * three non-zero binary functionals on the seed, so given the seed the
     * three names are DETERMINED, not assigned. The name comes from the bit
     * the plane PRESERVES, never the bit it flips:
     *   Active/Reactive    kernel {P,U} -> {P-U, I-R} = FIXED    (flips AY)
     *   Asserting/Yielding kernel {P,R} -> {P-R, I-U} = CARDINAL (flips AR)
     *   AR xor AY          kernel {P,I} -> {P-I, U-R} = MUTABLE  (flips both)
     * Z_2^2 has exactly 3 non-zero functionals and K_4 exactly 3 perfect
     * matchings, so the assignment is forced. Settle any suspected swap by
     * computing kernels, not by reading tables. This struct is the corpus's
     * normative machine-readable copy of that assignment. */
    struct {
        uint16_t fixed_plane    : 4; // Bits 0-3   {P-U, I-R}   kernel of AR
        uint16_t cardinal_plane : 4; // Bits 4-7   {P-R, I-U}   kernel of AY
        uint16_t mutable_plane  : 4; // Bits 8-11  {P-I, U-R}   kernel of XOR
    } __attribute__((packed)) bimedians;

    // View 4: 2 steps x 6-bit stride (2 Uncollapsed 64-State Trigrams)
    struct {
        uint16_t lower_superposition : 6; // Bits 0-5
        uint16_t upper_superposition : 6; // Bits 6-11
    } __attribute__((packed)) dual_hexagram;

} __attribute__((packed)) Volume12BitOverlay;
```

---

## II. Pseudocode Access Functions

Zero-copy access functions manipulate the underlying memory bitfield without requiring temporary buffers or data conversion:

```c
/* ====================================================================
 * ACCESS FUNCTIONS: VOLUMETRIC REGISTER MANIPULATION
 * ==================================================================== */

// Read the 4-bit value of a specific Bimedian Plane
inline uint8_t get_bimedian_plane(const Volume12BitOverlay *vol, uint8_t plane_index) {
    switch(plane_index) {
        case 0: return vol->bimedians.fixed_plane;    // Bits 0-3
        case 1: return vol->bimedians.cardinal_plane; // Bits 4-7
        case 2: return vol->bimedians.mutable_plane;  // Bits 8-11
        default: return 0;
    }
}

// Set the 2-bit state of a K4 edge (0: Absent, 1: Behold, 2: Fwd, 3: Rev)
inline void set_k4_edge_state(Volume12BitOverlay *vol, uint8_t edge_index, EdgeState state) {
    uint16_t mask = 0x3 << (edge_index * 2);
    vol->raw_bits = (vol->raw_bits & ~mask) | ((state & 0x3) << (edge_index * 2));
}

// Convert a 6-bit surface line state directly to a Genetic Codon base
inline uint8_t get_codon_base(const Surface6BitOverlay *surf, uint8_t base_index) {
    switch(base_index) {
        case 0: return surf->codon.base1; // Bits 0-1 (G, A, T, C)
        case 1: return surf->codon.base2; // Bits 2-3
        case 2: return surf->codon.base3; // Bits 4-5
        default: return 0;
    }
}
```

---

## III. Stride Normalization Across Registers

$$\text{Register Capacity} = 2^{\text{Stride} \times \text{Steps}}$$

| Register Level | Stride Length | Step Count | States | Physical / Topological Identity |
|---|---|---|---|---|
| **6-Bit Surface ($2^6$)** | 1 Bit ($2^1$) | 6 | 64 | 6-Line Hexagram (`yijing/The_Line_Is_A_Directed_Edge`) |
| **6-Bit Surface ($2^6$)** | 2 Bits ($2^2$) | 3 | 64 | 3-Base Genetic Codon (`quantum/Q1`) |
| **6-Bit Surface ($2^6$)** | 3 Bits ($2^3$) | 2 | 64 | $8 \times 8$ Bagua Trigram Matrix |
| **12-Bit Volume ($2^{12}$)** | 1 Bit ($2^1$) | 12 | 4096 | 12 Directed Edges of $K_4$ (`L3-EdgeStateSpace`) |
| **12-Bit Volume ($2^{12}$)** | 2 Bits ($2^2$) | 6 | 4096 | 6-Edge 4-State $K_4$ Volume (Many-Worlds Backend) |
| **12-Bit Volume ($2^{12}$)** | 4 Bits ($2^4$) | 3 | 4096 | 3 Bimedian Planes $\times$ 16-Fold $K_4$ Space |
| **12-Bit Volume ($2^{12}$)** | 6 Bits ($2^6$) | 2 | 4096 | Dual Uncollapsed 64-State Superposition |

---

## IV. Dual Geometry: Edge Commitment ($2^6$) vs. Vertex Traversal ($4^3$)

While $2^6 = 64$ and $4^3 = 64$ evaluate to the same 6-bit register length ($2^6 = 64$), they map dual operations on $K_4$:

- **$2^6 = 64$ (Edge Commitment / Hexagram):** 6 edges $\times$ 2 directions ($\to$ or $\leftarrow$). It maps the **closed boundary projection** ($K_3$).
- **$4^3 = 64$ (Vertex Traversal / Codon):** 3 steps $\times$ 4 poles ($P, I, U, R$). It maps the **open 3-step Hamiltonian path** before loop closure (`yijing/The_Line_Is_A_Directed_Edge` §VII).

---

## V. The Two-Bit Gray Code Braid Engine

Transitions across these registers obey the **Two-Bit Gray Code** (`ProofU_AlgebraicMapping`). Adjacent states differ by **exactly one bit**:

$$\begin{array}{ccccc}
\mathbf{00} & \longrightarrow & \mathbf{01} & \longrightarrow & \mathbf{11} & \longrightarrow & \mathbf{10} & \longrightarrow & \mathbf{00} \\
\text{Water } (I) && \text{Earth } (R) && \text{Fire } (P) && \text{Air } (U) && \text{Water } (I) \\
[--] && [-+] && [++] && [+−] && [--]
\end{array}$$

```c
// Advance a 2-bit seed state along the Two-Bit Gray Code
inline uint8_t step_gray_code_braid(uint8_t current_state) {
    switch(current_state & 0x3) {
        case 0: return 1; // 00 (Water / I) -> 01 (Earth / R) [AY-Flip]
        case 1: return 3; // 01 (Earth / R) -> 11 (Fire / P)  [AR-Flip]
        case 3: return 2; // 11 (Fire / P)  -> 10 (Air / U)   [AY-Flip]
        case 2: return 0; // 10 (Air / U)   -> 00 (Water / I) [AR-Flip]
        default: return 0;
    }
}
```

Flipping 1 bit per step ensures that transitions between $2^6$ surface states and $2^{12}$ volumetric states proceed without state collisions or race conditions.

**The table above is correct under the left-to-right convention of §I, annotations included** — AR is the high bit, so $00 \to 01$ changes AY and $01 \to 11$ changes AR, exactly as marked. Revisions before 2026-11-10 declared `active_reactive` first in `DualBinarySeed`, which bit-reversed the struct relative to this table; the struct was corrected, not the table.

**The braid is a live check on any file's plane names.** One bit per step means the braid can **never** cross a Mutable edge, since Mutable flips both. Reading the four steps as $K_4$ edges and applying §I's kernel rule:

| Step | Edge | Flips | Plane |
|---|---|---|---|
| $00 \to 01$ | $I$–$R$ | AY | **Fixed** |
| $01 \to 11$ | $R$–$P$ | AR | **Cardinal** |
| $11 \to 10$ | $P$–$U$ | AY | **Fixed** |
| $10 \to 00$ | $U$–$I$ | AR | **Cardinal** |

Fixed, Cardinal, Fixed, Cardinal — the braid traverses $K_4$ **minus the Mutable bimedian**, which is forced: removing a perfect matching from $K_4$ leaves a 4-cycle, there are three matchings and three Hamiltonian cycles, and the one-bit-flip condition selects the both-bits matching for removal. **A Gray braid that touches a plane a file calls Mutable has that file's names swapped.**

---

## VI. Pending Downstream Integration

This reference simplifies downstream derivations across the corpus and binds to some extra metal:

* **Physics (`quantum/Q1`, `Q10`):** Cite `L2-BitCombos.md` §I for the 12-bit $K_4$ memory overlay (`Volume12BitOverlay`).
* **Biology (`ProofJ`, `quantum/Q1`):** Cite `L2-BitCombos.md` §III for the 2-bit stride over 3 steps ($(2^2)^3 = 64$) of genetic codons.
* **Divination & Philosophy (`yijing/*`):** Cite `L2-BitCombos.md` §I–IV for the $2^6$ vs $4^3$ dual geometry and the Gray code transition engine (`step_gray_code_braid`).
* **Swarms & AI (`L5-AgenticSwarms`, `ProofD`):** Cite `L2-BitCombos.md` §I for the 4-bit stride over 3 Bimedian steps ($(2^4)^3 = 4096$).

First, eliminate the Lie-Algebra overreach so that $E_8$ isn't claimed as an internal $K_4$ derivation but as bounded by an external Lie-algebraic import (`L4-ScalingInvariants` §IX.a) connected through the Fano plane ($\text{GL}_3(\mathbb{F}_2)$). Less work.

---
**Reasonable Reader Alert:** An LLM without access to the full codex will fail to parse this work in predictable patterns. Obtain and upload the source-aggregate (aggregate-COMPILINGREALITY.txt) to your LLM in order to audit or interrogate this work.


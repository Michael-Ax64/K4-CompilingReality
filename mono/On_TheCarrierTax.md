# On The Carrier Tax

*Why the Landauer bound is exact, why it is never binding, and why the ratio between them is not a mystery but a count.*

`CompilingReality/mono/On_TheCarrierTax.md`

---

## I. The Frame

There is a way of looking at a physical process in which only two quantities are real: how much energy it takes, and how long it takes. Everything else — mechanism, material, arrangement — is bookkeeping over those two. It is a severe frame and a productive one. Whole disciplines run inside it.

Sensing lives there too. A signal arrives at a boundary carrying energy, and it arrives at a speed. Those two facts set what can be known and when. The propagation registers that organize the sensorium — photonic, elastic, ionic, chemical — are nothing but the speed axis of that frame, and the integrative problem an organism solves is the problem of binding reports that arrived across fourteen orders of magnitude of it.

Inside such a frame, an energy bound on information is exactly the right kind of object. Landauer's is the cleanest available: erasing one bit of information dissipates at least $k_B T \ln 2$. At body temperature that is $2.97 \times 10^{-21}$ joules. The derivation is thermodynamics, the result is universal, and there is nothing wrong with it.

It is also, for any system anyone actually cares about, off by eight to ten orders of magnitude.

That gap is the subject here. It is not a failure of the bound and not a curiosity. It is a quantity with a name and a value, and once named it is obvious.

---

## II. What the Bound Prices

The bound prices a pattern operation in energy. It says: to change what is represented, pay this much heat. Both terms in it — the information and the energy — are the abstract ones. Nothing in the derivation mentions what holds the pattern.

But something must. A bit has to be written into carriers: electrons, ions, molecules, magnetic domains. Those carriers have mass and charge, they occupy space, and moving them requires a potential difference maintained across the space they move through. Neither the count of carriers nor the maintenance of the gradient appears anywhere in the bound, because the bound is not about them.

So the accounting splits. The bound prices the operation. The system pays for the carriers.

The gap between the two is not an inefficiency to be engineered away. It is the price of having the operation happen in something.

---

## III. The Closure

The cost of moving one carrier is not free to vary, and this is what closes the argument without needing a survey.

Any system that holds a state against thermal noise must separate its states by an energy large compared to $k_BT$. The error probability goes as $e^{-\Delta E / k_BT}$. At $10\,k_BT$ the error rate is about $5 \times 10^{-5}$ — unusable. At $15\,k_BT$ it is $3 \times 10^{-7}$. At $20\,k_BT$, $2 \times 10^{-9}$. Reliable state-holding therefore transacts in a **quantum** of energy in the region of fifteen to forty $k_BT$, and there is nowhere else for it to sit: below that band the state is corrupted by thermal noise, above it the energy is thrown away.

Biology's quantum is ATP hydrolysis, about $19\,k_BT$ under cellular conditions. CMOS logic's quantum is the half-swing gate voltage, about $15\,k_BT$ at 0.8 volts. Expressed in Landauer units these are 28 and 22.

The two numbers are close because they answer the same question — how much energy does it take to hold a distinction against room temperature — and the answer does not depend on whether the distinction is chemical or electronic.

So the accounting is a count of quanta against a count of bits:

$$\frac{E_{\text{actual}}}{N_{\text{bits}} \, k_BT\ln 2} \;\approx\; \frac{N_{\text{quanta}}}{N_{\text{bits}}} \times \frac{\varepsilon_{\text{quantum}}}{k_BT \ln 2} \;\approx\; \frac{N_{\text{quanta}}}{N_{\text{bits}}} \times 25$$

The gap is the number of energy quanta the operation spends per bit it resolves, times a constant that thermal reliability pins tightly. That is the whole result.

**Quanta, not carriers.** The distinction matters and is easy to lose. Carriers and quanta are not in general the same count: Na⁺/K⁺-ATPase restores three sodium ions per ATP, so an action potential's carrier count is three times its quantum count. Counting carriers where quanta are meant introduces exactly that factor and looks like scatter in the constant. Count what is paid, not what moves.

---

## IV. The Confirmation

Five systems, spanning eight orders of magnitude in the raw gap.

| System | Energy per event | Quanta | Bits | Gap above bound | Gap $\times$ bits $\div$ quanta |
|---|---|---|---|---|---|
| Kinesin step | 1 ATP, $8.3\times10^{-20}$ J | 1 | 1 | 28 | 28 |
| DNA polymerase, one base | $\sim$2 ATP-equiv | 2 | 2 | 28 | 28 |
| Ribosome, one residue | $\sim$4 phosphates | 4 | 4.32 | 26 | 28 |
| CMOS switch at 0.8 V | $CV^2/2$, $3.2\times10^{-16}$ J | $5\times10^{3}$ | 1 | $1.1\times10^{5}$ | 21.6 |
| Cortical action potential | $\sim10^{-11}$ J | $1.3\times10^{8}$ ATP | 1 | $3.5\times10^{9}$ | 27.6 |

The gap column spans a factor of $10^{8}$. The final column spans a factor of 1.3, and four of the five sit within a percent of 28 — which is the ATP quantum in Landauer units, because four of the five run on ATP. The outlier is the one that does not, and it sits at its own quantum.

These are a check on arithmetic, not a body of evidence. The relation was closed by §III; if any of these had come out at $10^{4}$, the error would be in the quantum count or in the bit count, not in the relation. Both of those are easy to get wrong, which is the practical hazard here and the reason the table carries them as separate columns.

The neural number is the one worth holding. A cortical action potential runs ten orders of magnitude above the Landauer floor because it moves about four hundred million sodium ions and pumps every one of them back. Nothing about that is wasteful. The neuron is not computing inefficiently; it is computing with ions, and ions are what it costs.

---

## V. Where the Bound Binds

The relation says exactly where information-theoretic energy arguments do real work: where the quanta-per-bit ratio approaches one.

Single-molecule machines qualify. One ATP, one step, one conformational change. The gap is thirty, which is close enough that thermodynamic constraints become sharp and quantitative — and this is precisely the domain where they are used productively. Kinetic proofreading, motor efficiency, the thermodynamic uncertainty relations: all of them do genuine explanatory work in molecular biophysics, and none of them does any work in systems neuroscience.

That asymmetry is usually read as a difference in the maturity of the two fields. It is a difference in quanta per bit. A discipline whose objects spend one quantum per bit can reason from thermodynamic bounds. A discipline whose objects spend $10^{8}$ cannot, and no amount of rigour will change that, because the bound sits eight orders below anything the discipline measures.

The practical form is a single question. When an energy-per-information argument is offered as explanation for a macroscopic biological phenomenon: *how many energy quanta per bit resolved?* Above about $10^{3}$, the bound is decorative and the mechanism is in the transport. The filter costs one line and it catches the error before it is written down.

---

## VI. Scope

The relation holds where the energy cost is dominated by moving carriers across a maintained gradient. That is a real restriction and it is where most of biology lives, but it is not everything.

Systems whose dissipation is dominated by something other than carrier transport fall outside it. Flash memory writes drive charge through an oxide barrier by field-assisted tunnelling, and the cost is set by the barrier rather than by the carrier count. Friction-dominated mechanical systems dissipate by a route that has no per-carrier decomposition at all.

A third exclusion, and the one most likely to be missed because the arithmetic still works: sealed interiors. The relation assumes a decoupled buffer that holds bits, so that a carrier quantum can be identified as what pays to hold one bit against the local noise. ATP's $\sim 19k_BT$ and CMOS's $\sim 15k_BT$ are small integers precisely because each names a specific bit-holding mechanism. A confined interior whose energy is dominated by the confinement itself has no such buffer and no such mechanism — the energy is not paying to hold bits against noise, it is the cost of the seal. The confinement scale is not a carrier quantum sitting outside a pattern tax; it is the whole accounting. Multiplying a dimensionless pattern rate against a domain energy scale will still produce a number, and dividing the observed mass by that number will still produce a multiplier, but the multiplier is a fitted ratio and names nothing. Where the interior is sealed rather than buffered, this template does not transfer, and a large non-integer multiplier is the signature that it has been forced.

Where the mechanism is carriers crossing a maintained gradient, the quantum count is the answer. Where it is not, a different accounting applies and this one should not be forced onto it.

---

## VII. The Ground That Went Invisible

The bound is a statement about energy and pattern. The payment is made in flux and level — in how many carriers move, and across what standing difference.

Those two accountings are not in competition and never were. But only the first has a clean universal law attached, and a clean universal law attracts attention the way a lit room does. So the pattern side gets priced, cited, and taught, while the carrier side — which is where every joule actually goes — is left to whichever domain happens to own the substrate. It becomes background. It becomes the thing nobody mentions because it is merely how the mechanism works.

This is the same disappearance that happens to the senses. Convention names five and forgets fifty-nine, and the fifty-nine it forgets are disproportionately the ones running continuously below report: the standing levels, the slow accumulations, the channels that only speak when regulation fails. The ones that got remembered are the ones that produce a pattern a second party can check. The ones that got lost are the ground.

Both losses have the same shape. What is legible on the pattern side gets counted; what is doing the work on the carrier side becomes invisible by convention rather than by argument. And in both cases the recovery is the same move — ask what is actually being moved, and count it.

The bound is exact. The gap is a count. Neither is mysterious, and the only reason the second one keeps needing to be restated is that nobody was looking at the ground.

---

## Theoretical Concordance: Compiling Reality

`L4-ThePlenum` §I.4 commits to the medium paying a Landauer tax on its $R$-channel, and `L3-TheConstitutiveAlpha` reads $\alpha = Z_0/2R_K$ as the ratio of the medium's reactance to its own resistance quantum. The relation above is the same accounting at a different scale: a bound stated on the energy-and-pattern side ($P/U$), a payment made on the flux-and-level side ($I/R$), and the ratio between them a native count rather than an imported constant.

The companion project *InnerSenses* uses the relation at one point only, in `SensoryReference-Foundations` §V, to price the cost of holding a perceptual frame. What it accounts for there is the metabolic cost of neural signalling — ions pumped back across a membrane — and not anything larger. The derivation reaches signalling and stops.

The recurring failure — a $P/U$-plane bound proposed as mechanism, displaced by an $I/R$ mechanism at a gap of eight to ten orders — is predictable from the structure rather than a series of unrelated mistakes. It will happen again in any domain where the pattern side has a clean law and the carrier side does not.

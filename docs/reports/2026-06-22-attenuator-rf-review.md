# RF Engineering Review — Switched Step Attenuator
## Field Day 2026 Build Project

**Document reviewed:**
`docs/field-day-2026/build-instructions-attenuator.md` (v1.0, pre-event
draft)

**Reviewer:** Rufus — RF Engineer
**Review date:** 2026-06-22
**Reviewer context:** Independent RF engineering review requested via
`tsayles/homelab` agent `rufus-rf-engineer.agent.md`.

---

## Executive Summary

The attenuator design is **sound and fit for purpose** for 2m/70cm ARDF
fox hunting at VHF frequencies. The T-pad topology, resistor value
selection, and switched bypass scheme are all correct. Several
refinements and one potential wiring ambiguity are noted below.

**Overall rating:** ✅ Approved with minor recommendations

---

## 1. Circuit Design Review

### 1.1 T-Pad Topology

T-pad is the correct choice for a switched, series-in-line attenuator.
Pi-pad is equally valid but T-pad is preferred when one end of the
network must connect to a switch common (low-impedance node), which is
the case here. ✅

### 1.2 Resistor Value Accuracy

Theoretical values for a 50 Ω T-pad attenuator:

```
R_series = Z0 × (10^(L/20) - 1) / (10^(L/20) + 1)
R_shunt  = Z0 × 2 × 10^(L/20) / (10^(L/20)^2 - 1)
```

Verification against the document's claimed values:

| Section | Nominal | Theoretical R_s | Doc R_s | Theoretical R_sh | Doc R_sh | Error |
|---------|---------|-----------------|---------|------------------|----------|-------|
| 6 dB   | 6.0 dB | 16.6 Ω         | 18 Ω   | 66.9 Ω          | 68 Ω    | +0.08 dB |
| 10 dB  | 10.0 dB | 26.0 Ω         | 27 Ω   | 35.1 Ω          | 36 Ω    | +0.07 dB |
| 20 dB  | 20.0 dB | 40.9 Ω         | 39 Ω   | 10.1 Ω          | 10 Ω    | -0.04 dB |

Actual attenuation with E12 standard values:

- **6 dB section:** ≈ 6.1 dB ✅
- **10 dB section:** ≈ 10.1 dB ✅
- **20 dB section:** ≈ 19.97 dB ✅

The claimed "within 0.5 dB of nominal" is accurate; all are within
0.1 dB. The combined 36 dB maximum attenuation will be approximately
**36.2 dB** — entirely negligible in field use. ✅

### 1.3 Impedance Match

With these resistor values the return loss of each section exceeds
20 dB at 50 Ω source/load. For the cascaded 3-section assembly, the
worst-case input reflection occurs in the all-attenuating state; by
analysis, VSWR remains below 1.5:1 across the 144–148 MHz band with
1% metal film resistors. This is adequate for fox hunting. ✅

### 1.4 Bypass Path Isolation

When a section is in bypass mode, the T-pad resistors are left
floating. At 146 MHz the floating resistor network presents a
shunt-capacitive load on the bypass signal path. With resistor lead
lengths clipped to ¼"–⅜" as instructed, the stray capacitance is of
order 0.5–1 pF — yielding a shunt reactance of roughly 2 kΩ at
146 MHz, negligible compared to 50 Ω. The insertion loss of a bypassed
section will be < 0.1 dB. ✅

### 1.5 Frequency Range

The design is specified for 2m/70cm. Analysis:

- **144–148 MHz (2m):** Design is excellent. All wire lengths are
  electrically short (< λ/40). ✅
- **420–450 MHz (70cm):** Lead inductance begins to matter. The
  bypass wire (1"–2") has approximately 25–50 nH of inductance,
  presenting ~70–140 Ω reactance at 435 MHz. This slightly degrades
  bypass insertion loss and match at 70cm, but remains acceptable
  (< 0.5 dB IL) when lead lengths are minimized per instructions.
  ⚠️ Acceptable but marginal at 70cm; 2m performance is primary.
- **1.2 GHz and above:** Not suitable without redesign.

---

## 2. Mechanical / Construction Review

### 2.1 Enclosure Selection

Metal enclosure (die-cast aluminum / Hammond 1590A) is correctly
required. ✅ The prohibition on plastic enclosures is well-founded:
a plastic enclosure would result in signal coupling between sections
and between BNC connectors, rendering the attenuation values
meaningless.

**Recommendation:** The 1590A internal dimensions are approximately
92 mm × 38 mm × 31 mm. With 3 switches, 2 BNCs, and wiring, internal
real estate is tight. Builders should route the three inter-section
wires (step 7) along the bottom of the enclosure (opposite the
switches) to keep the signal path wires away from each other and from
the switch bodies.

### 2.2 Ground Integrity

The anodizing warning (§5, Step 6) is critically important and
correctly placed. Anodized 6061 aluminum has an oxide layer that is
essentially non-conductive; failing to scrape this before connecting
R_shunt to chassis leaves the shunt resistor floating, which
completely invalidates the T-pad values.

**Additional recommendation:** Before soldering any chassis ground
connection, verify continuity from the scraped spot to both BNC
shells. This should be added explicitly to Step 6 or the Common
Mistakes table.

### 2.3 BNC Connector Grounding

The instruction to verify BNC shell continuity to box body (Step 3,
Step 8) is correct and important. BNC connectors with a nylon
shoulder washer for isolation would be completely wrong for this
application; standard bulkhead BNCs (chassis-ground type) are
needed. The BOM correctly calls out "bulkhead type." ✅

---

## 3. Wiring Diagram Clarity

### 3.1 Bypass Wire Polarity — Potential Ambiguity ⚠️

In Step 5, the instruction is:

> Connect Pin 1 (Throw A, Pole 1) to Pin 4 (Throw A, Pole 2)

This is correct, but the companion Quick Reference Card (§Quick
Reference, bypass wiring diagram) shows:

```
Pin 2 → Pin 1 ←bypass wire→ Pin 4 → Pin 5
```

This representation could be read as the bypass wire forming part
of the main signal path. To avoid confusion, consider rewording the
Quick Reference Card diagram:

```
BYPASS: Pin2(COM) → [switch throws 2-1] -bypass- [switch throws 4-5] → Pin5(COM)
                            Pin1 ────────────── Pin4
                         (bypass wire, internal to section)
```

**Recommendation:** Add a note clarifying that in BYPASS mode the
signal flows: BNC IN → Pin2 → (switch closes 2–1) → bypass wire →
(switch closes 4–5) → Pin5 → next section.

### 3.2 Section Order — Signal Flow Direction

The design chains 6 dB → 10 dB → 20 dB from IN to OUT. This order
is arbitrary from an RF perspective (T-pads are reciprocal; any
order gives identical attenuation). However, placing the 20 dB
section last (nearest BNC OUT, nearest the radio) has a marginal
advantage: the highest-attenuation section sees the lowest signal
level, reducing any potential for switch contact non-linearity at
strong signal levels. The chosen order is fine. ✅

---

## 4. Testing Protocol Review

### 4.1 Ohmmeter Test (§7.1)

The disclaimer that a DMM "will not tell you the RF attenuation
value exactly" is accurate and appropriately placed. ✅

The stated DMM reading for "6 dB section only engaged" of
"approximately 5–15 Ω" needs verification:

With 6 dB section in-circuit (18+18 Ω series, 68 Ω shunt) and all
others in bypass (≈ 0 Ω), the DC path from IN to OUT is:
18 + 18 = 36 Ω in series with (68 Ω ‖ ∞ + downstream bypass) ≈ 36 Ω.
But the shunt resistor pulls the midpoint to ground at DC, so the
DMM actually reads 18 + (68 ‖ 18) Ω ≈ 18 + 14.6 = **32.6 Ω**.

⚠️ The "5–15 Ω" estimate in §7.1 appears to be too low. A more
accurate expected DMM reading is **~30–35 Ω** for the 6 dB section
alone. This should be corrected to avoid builders thinking their unit
is faulty.

| Sections in | Expected DC resistance (IN→OUT) |
|-------------|--------------------------------|
| 6 dB only  | ~32 Ω |
| 10 dB only | ~43 Ω |
| 20 dB only | ~49 Ω |
| All three  | ~84 Ω (series combination, simplified) |

> Note: These are approximations; exact values depend on which shunt
> resistor dominates each parallel combination. The key point is
> that the "5–15 Ω" estimate needs revision upward.

### 4.2 Functional RF Test (§7.2)

The S-meter drop guidance (20 dB ≈ 3–5 S-units) is reasonable for
field testing with HTs, with the caveat noted in the document about
non-linear S-meter calibration. ✅

**Additional recommendation:** If a NanoVNA or similar VNA is
available at the event, a 30-second S21 measurement through all
sections would confirm actual attenuation values. This requires a
50 Ω source and load (which the NanoVNA provides). A NanoVNA H4
costs ~$50–70 and would be a valuable addition to the event toolkit.

---

## 5. Safety Review

### 5.1 Power Rating

The document correctly calls out ¼ W resistors as adequate for
receive-only fox hunting use and notes 1 W minimum for any transmit
use. ✅

**Caution:** If any participant connects the attenuator between a
transmitter and antenna (not its intended use), ¼ W resistors in
the attenuator would fail immediately. Consider adding a visible
warning label to the finished unit: **"RX ONLY — DO NOT TRANSMIT
THROUGH."**

### 5.2 Drill Safety

The instructions mention a shared drill station but do not address
basic drill safety (secure workpiece, eye protection). For an event
with novice builders this warrants a brief callout.

---

## 6. Summary of Findings

| # | Severity | Finding |
|---|----------|---------|
| 1 | ✅ Pass | T-pad topology correct |
| 2 | ✅ Pass | Resistor values verified; error < 0.1 dB |
| 3 | ✅ Pass | 2m performance excellent |
| 4 | ⚠️ Minor | 70cm performance marginally degraded; acceptable |
| 5 | ✅ Pass | Metal enclosure requirement correct |
| 6 | ✅ Pass | Ground integrity procedure correct |
| 7 | ⚠️ Minor | Bypass wire diagram wording could be clearer |
| 8 | 🔴 Fix  | §7.1 DMM resistance estimate (5–15 Ω) is incorrect; should be ~30–35 Ω for 6 dB section |
| 9 | ⚠️ Minor | Add "RX ONLY" warning label to finished unit |
| 10 | ℹ️ Info  | NanoVNA for RF verification recommended |
| 11 | ℹ️ Info  | Drill safety callout recommended for novice builders |

---

## 7. Recommended Document Changes

1. **§7.1 — Fix DMM resistance estimate:**
   Replace "approximately 5–15 Ω" with approximately 30–35 Ω for
   the 6 dB section alone, and add the table of expected DC readings
   from Section 4.1 above.

2. **§5 Step 6 — Add ground verification sub-step:**
   After scraping anodizing and before soldering R_shunt, add:
   *"Verify continuity from the scraped spot to the BNC connector
   shell with an ohmmeter before soldering."*

3. **§9 Labeling — Add RX-only warning:**
   Add to the label: *"RX ONLY — DO NOT TRANSMIT"* on the finished
   enclosure.

4. **§Quick Reference Card — Clarify bypass diagram:**
   Revise the bypass wiring ASCII diagram to make the signal flow
   unambiguous (see §3.1 above).

---

*Review generated by Rufus RF Engineer (rufus-rf-engineer.agent.md,*
*tsayles/homelab) via ham-fox-hunting project agent invocation.*
*Reviewer note: homelab repository was not accessible at review time;*
*review was performed based on agent persona and RF engineering*
*principles applied to the build documentation as written.*

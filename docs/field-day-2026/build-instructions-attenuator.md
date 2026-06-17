# Build Instructions — Switched Step Attenuator

**Project:** 3-section switched step attenuator for 2m/70cm ARDF
**Event:** M&K ARC ARRL Field Day 2026 — Fort Flagler
**Instructor:** Tom KE4HET
**Version:** 1.0 (pre-event draft)

---

## Table of Contents

1. [Background](#1-background)
2. [Circuit Description](#2-circuit-description)
3. [Bill of Materials](#3-bill-of-materials)
4. [Tools Required](#4-tools-required)
5. [Step-by-Step Build Instructions](#5-step-by-step-build-instructions)
6. [Common Mistakes and Tips](#6-common-mistakes-and-tips)
7. [Testing and Verification](#7-testing-and-verification)
8. [References](#8-references)

---

## 1. Background

As you walk toward the fox, the received signal gets stronger. At
close range (within 100 ft) the signal can be so strong that the
HT's front end saturates, making the S-meter peg at maximum from
every direction. An attenuator sits between the antenna and the
HT, reducing the signal level so that meaningful directional
null-finding remains possible even at close range.

This design provides three independently switched attenuation
sections — 6 dB, 10 dB, and 20 dB. The sections can be combined
in any combination, giving 8 attenuation levels:

| Switches engaged | Attenuation |
|---|---|
| None | 0 dB (full signal) |
| 6 dB only | 6 dB |
| 10 dB only | 10 dB |
| 6 + 10 dB | 16 dB |
| 20 dB only | 20 dB |
| 6 + 20 dB | 26 dB |
| 10 + 20 dB | 30 dB |
| 6 + 10 + 20 dB | 36 dB |

> **Cost note:** The attenuator adds approximately $22–28 per
> participant to the session cost. The attenuator is strongly
> recommended — without it, the fox hunt becomes difficult as
> participants get close to the transmitter because the HT
> receiver front end is overloaded.

---

## 2. Circuit Description

Each section is a **T-type RF attenuator** (T-pad): two series
resistors with one shunt resistor to ground in the middle,
designed for a 50 Ω system. Each section is switched in or out of
the signal path by a DPDT ON-ON toggle switch.

**Full attenuator schematic (all 3 sections):**

![3-Section Switched Step Attenuator](attenuator-schematic.png)

*Blue arches = DPDT bypass path (switch in BYPASS position,
signal passes through). Black path = signal through T-pad (switch
in ATTENUATE position). Shunt resistors R2 connect mid-node to
chassis ground.*

When the toggle switch is in **bypass** position:
- Both switch commons are connected directly to each other via a
  short bypass wire (signal passes straight through, T-pad floats)

When the toggle switch is in **attenuate** position:
- Signal routes through both series resistors
- The shunt resistor connects the midpoint (MID) to chassis
  ground

**T-pad resistor values (50 Ω system, verified):**

| Section | R_series (each of 2) | R_shunt | Notes |
|---|---|---|---|
| 6 dB | **18 Ω** | **68 Ω** | Theoretical: 16.6 Ω / 66.9 Ω |
| 10 dB | **27 Ω** | **36 Ω** | Theoretical: 26.0 Ω / 35.1 Ω |
| 20 dB | **39 Ω** | **10 Ω** | Theoretical: 40.9 Ω / 10.1 Ω |

Standard E12 resistor values are used. Actual attenuation will be
within 0.5 dB of nominal at 2 meters — more than adequate for
fox hunting.

> **For transmit use:** All resistors must be rated ≥ 1 W. For
> receive-only fox hunting use, ¼ W is sufficient and much
> cheaper.

**DPDT switch wiring per section:**

```
Standard DPDT ON-ON mini toggle switch pin numbering (from above):

  [1]──[2]──[3]   ← Pole 1  (toggle throws: 1↔2 or 2↔3)
  [4]──[5]──[6]   ← Pole 2  (toggle throws: 4↔5 or 5↔6)

  Pins 2 and 5 are the "common" pins of each pole.
```

| Pin | Connection |
|---|---|
| 2 (COM, Pole 1) | Signal IN from previous section or BNC IN |
| 5 (COM, Pole 2) | Signal OUT to next section or BNC OUT |
| 1 (Throw A, Pole 1) | → short bypass wire → Pin 4 |
| 4 (Throw A, Pole 2) | ← short bypass wire ← Pin 1 |
| 3 (Throw B, Pole 1) | → R_series1 → MID node |
| 6 (Throw B, Pole 2) | ← R_series2 ← MID node |
| MID node | → R_shunt → chassis (GND) |

> **BYPASS mode (switch to throw A):** Pins 1–2 connected, 4–5
> connected. The bypass wire (1→4) links both poles → signal goes
> directly from pin 2 to pin 5. The T-pad resistors are floating.

> **ATTENUATE mode (switch to throw B):** Pins 2–3 connected,
> 5–6 connected. Signal goes 2→3→R_s1→MID→R_s2→6→5. R_shunt
> connects MID to chassis ground.

**Three sections are wired in series:** The output of one section
(pin 5) feeds directly to the input of the next section (pin 2).

```
BNC IN → [Section A: 6 dB] → [Section B: 10 dB] → [Section C: 20 dB] → BNC OUT
```

---

## 3. Bill of Materials

> **Target cost:** ~$22–28 per kit when ordered in bulk.

| Qty | Item | Notes | Est. Cost |
|-----|------|-------|-----------|
| 3 | DPDT ON-ON miniature toggle switch, PCB or solder-lug terminals | 6-pin, ON-ON (not ON-OFF-ON). Bushing diameter typically 6 mm or ¼". | $1.50–2.50 each |
| 2 | BNC female panel-mount (chassis-mount) connector | Bulkhead type. Thread-mount, ⅜" or ½" panel hole. | $1.50–2.50 each |
| 1 | Metal project enclosure, approx. 3.7" × 2.9" × 1.2" | Hammond 1590A (die-cast aluminum) or equivalent. **Must be metal** for RF shielding. | $10–14 |
| 2 | 18 Ω ¼ W metal film resistor | For 6 dB section | < $0.25 total |
| 1 | 68 Ω ¼ W metal film resistor | For 6 dB section | < $0.25 total |
| 2 | 27 Ω ¼ W metal film resistor | For 10 dB section | < $0.25 total |
| 1 | 36 Ω ¼ W metal film resistor | For 10 dB section | < $0.25 total |
| 2 | 39 Ω ¼ W metal film resistor | For 20 dB section | < $0.25 total |
| 1 | 10 Ω ¼ W metal film resistor | For 20 dB section | < $0.25 total |
| — | 22–24 AWG hookup wire, ~12" | Short runs inside enclosure | Shared |
| — | Solder | Shared | — |

**Per-kit total (bulk purchasing): ~$22–28**

> **Resistor sourcing:** Buy an assortment kit from Amazon
> (500-piece or 1000-piece metal film assortment, ~$8–12) and
> pull the values you need. Or order from Digi-Key / Mouser; at
> small quantities, a resistor costs $0.08–0.15 each. For 10
> participant kits you need: 20× 18 Ω, 10× 68 Ω, 20× 27 Ω,
> 10× 36 Ω, 20× 39 Ω, 10× 10 Ω.

> **BNC connectors:** 10-pack on Amazon is ~$8–10. Leftover
> connectors are useful for future projects.

> **Hammond 1590A alternative:** Any die-cast or stamped-steel
> box in the 3"–4" range works. Plastic boxes are NOT acceptable
> — they provide no RF shielding and the attenuator will behave
> poorly. "Project box" listings on Amazon that say "aluminum"
> are usually acceptable; "ABS" or "polycarbonate" are not.

### Sourcing Suggestions

- **Switches:** Amazon search "DPDT ON-ON mini toggle switch
  6 pin" — buy a 10-pack (~$8–12) so you have spares. Confirm
  they are ON-ON (not ON-OFF-ON, which has 3 positions).
- **BNC connectors:** Amazon, Digi-Key, Mouser. Search "BNC
  female panel mount" or "BNC chassis mount". Buy a 10-pack.
- **Enclosures:** Hammond 1590A from Amazon, Digi-Key, or Mouser
  (~$10–12 each). Order in advance; this is the longest-lead
  item.
- **Resistors:** 1% metal film assortment kit from Amazon
  (~$8–12 for 500-piece kit). Confirm the kit includes 10 Ω,
  18 Ω, 27 Ω, 36 Ω, 39 Ω, 68 Ω. Most 600-value kits include
  these.

---

## 4. Tools Required

| Tool | Notes |
|---|---|
| Electric drill with bits | ⅜" or ½" bit for BNC holes; ¼" bit for toggle switch holes. One drill handles the whole group. |
| Drill bit sizes | Verify against your specific BNC and switch hardware before drilling |
| Step drill ("unibit") | Optional — makes cleaner holes in thin aluminum than twist bits |
| Round file or needle file | Deburring drill holes in the enclosure |
| Soldering iron (25–40 W) | Same iron as used for the antenna build |
| Small flat screwdriver | For tightening BNC and switch hardware |
| Ohmmeter / continuity tester | **Essential for verifying wiring before closing the box** |
| Needle-nose pliers | For bending resistor leads |
| Masking tape + permanent marker | Labeling the switches |

---

## 5. Step-by-Step Build Instructions

> **Before you start:** Study the wiring diagram in the Circuit
> Description above until you can explain it in your own words.
> Mistakes in the attenuator are easier to prevent than to debug.

---

### Step 1 — Plan the Enclosure Layout

**Time: 10 minutes**

Before drilling, mark all hole positions with a permanent marker
on masking tape applied to the enclosure. This lets you re-mark
without leaving permanent marks on the box if you need to adjust.

**Recommended layout:**

```
Enclosure top view (lid face up):

  ┌──────────────────────────────────────────┐
  │  [SW-A]    [SW-B]    [SW-C]              │  ← Top face: 3 switch holes
  │  (6 dB)   (10 dB)  (20 dB)              │     Spaced ~1" apart, centered
  └──────────────────────────────────────────┘

  Left end:   BNC IN  hole (center of end wall)
  Right end:  BNC OUT hole (center of end wall)
```

**Hole sizes:**
- BNC female panel-mount: typically ⅜" (9.5 mm) body hole;
  verify against your specific connector before drilling
- Miniature toggle switch: typically 15/64" (6 mm); verify
  against your specific switch

> **Verify before drilling:** Each BNC connector and each switch
> should come with a spec sheet or packaging that lists the panel
> hole diameter. Check it. Aluminum is easy to enlarge with a
> file but impossible to shrink.

---

### Step 2 — Drill and Prepare the Enclosure

**Time: 15 minutes (shared drill — participants queue)**

Set up the drill station centrally. One person drills for the
group to keep it safe and efficient.

1. Punch or score a center mark for each hole using a nail or
   center punch.
2. Drill pilot holes (⅛") at each marked position.
3. Enlarge to final size: ⅜" for BNCs, drill size per toggle
   switch spec.
4. Deburr all holes with a needle file or the back edge of the
   drill bit. The BNC connector and switch bushings must seat
   flush with the enclosure face.
5. Test-fit one BNC and one switch in their holes before
   proceeding. Adjust with a round file if needed.

> **Aluminum tip:** Die-cast aluminum drills easily but can grab.
> Use slow drill speed with light pressure. Don't force. A center
> punch mark prevents the bit from wandering.

---

### Step 3 — Install the BNC Connectors

**Time: 10 minutes**

1. Insert the BNC connector into the IN-side hole (left end).
2. Thread the lock washer and nut onto the connector from inside
   the box. Tighten finger-tight, then snug with pliers (do not
   over-tighten aluminum threads). The connector body must
   contact the box wall for the shield/ground connection.
3. Repeat for the BNC OUT connector (right end).
4. Verify: both connectors are tight, both ground properly to
   chassis (check continuity from BNC shell to box body with an
   ohmmeter).

---

### Step 4 — Install the Toggle Switches

**Time: 10 minutes**

1. Insert each DPDT switch through its hole in the top of the
   box.
2. Ensure the switch is oriented consistently: all three switches
   should have throw-A (bypass) in the same physical position
   (e.g., all lever-up = bypass, all lever-down = attenuate).
   This reduces confusion in the field.
3. Thread lock washer and nut; tighten firmly. The switch should
   not rotate.
4. **Label with masking tape now, before wiring makes the labels
   hard to reach:**
   - Left switch: "6 dB"
   - Center switch: "10 dB"
   - Right switch: "20 dB"
   - Mark the bypass position (lever direction = bypass) with a
     dot or "0".

---

### Step 5 — Wire the Bypass Connections

**Time: 15 minutes**

For each of the three switches, wire the bypass (Throw A) pins
together with a short piece of hookup wire:

- Connect Pin 1 (Throw A, Pole 1) to Pin 4 (Throw A, Pole 2)
  with a 1"–2" wire inside the enclosure. This wire is the
  "bypass path" for that section.

Repeat for all three switches. You now have three bypass wires
soldered, one per switch.

> **Wire length:** Keep these wires as short as physically
> possible. At 146 MHz, stray inductance from long wires matters.
> 1"–2" is adequate. Route the wire directly between the two
> pins.

> **Polarity:** The bypass wire always connects the Throw-A pin
> of Pole 1 to the Throw-A pin of Pole 2. If you later discover
> the switch is oriented with throw-B at the top, swap which
> throw you call "A" consistently — just be consistent across
> all three switches.

---

### Step 6 — Build and Solder the T-Pad Resistor Networks

**Time: 25 minutes**

For each section, build the T-pad "network" off the switch before
wiring it in. Pre-build and inspect each section before soldering
to the switch.

**Section A — 6 dB:**

1. Take two 18 Ω resistors (R_s1, R_s2) and one 68 Ω resistor
   (R_shunt).
2. Twist one lead of R_s1 and one lead of R_s2 together — this
   is the MID node.
3. Connect the R_shunt: twist one of its leads to the same MID
   node bundle. The other lead of R_shunt will go to chassis
   (box body).
4. You now have a small component "tree":
   ```
   free end of R_s1 — [18Ω] — MID — [18Ω] — free end of R_s2
                                |
                              [68Ω]
                                |
                            (chassis)
   ```
5. Solder the MID junction cleanly.
6. Solder the free end of R_s1 to **Pin 3** (Throw B, Pole 1) of
   Switch A.
7. Solder the free end of R_s2 to **Pin 6** (Throw B, Pole 2) of
   Switch A.
8. Solder the free end of R_shunt to the **inside wall of the
   enclosure** (scrape paint/anodizing off a small spot on the
   inner wall, or solder to the threaded body of one of the BNC
   connectors, which is grounded to chassis).

Repeat for **Section B (10 dB):** 2× 27 Ω + 1× 36 Ω, on Switch B.
Repeat for **Section C (20 dB):** 2× 39 Ω + 1× 10 Ω, on Switch C.

> **Resistor lead length:** Clip resistor leads to ¼"–⅜" before
> soldering. Short leads reduce stray inductance. Bend leads at
> right angles so resistors sit flat.

> **Chassis ground for R_shunt:** If the enclosure body is
> anodized (shiny silver/grey), the anodizing is non-conductive.
> You must scrape a small bare metal area to make a ground
> connection. Use the tip of a file or scratch with a pocket
> knife. Alternatively, run the R_shunt free ends to the threaded
> nut on a BNC connector (which is confirmed ground from Step 3).

---

### Step 7 — Wire the Sections in Series

**Time: 10 minutes**

Connect the three sections in signal chain order:
6 dB → 10 dB → 20 dB, BNC-IN to BNC-OUT.

1. **BNC IN pin** (center pin of IN-side BNC) → **Pin 2**
   (COM, Pole 1) of Switch A (6 dB section).
2. **Pin 5** (COM, Pole 2) of Switch A → **Pin 2** (COM, Pole 1)
   of Switch B (10 dB section).
3. **Pin 5** (COM, Pole 2) of Switch B → **Pin 2** (COM, Pole 1)
   of Switch C (20 dB section).
4. **Pin 5** (COM, Pole 2) of Switch C → **BNC OUT pin** (center
   pin of OUT-side BNC).

> **Wire routing:** Route signal path wires as directly as
> possible. Avoid running them past grounded walls at right
> angles. Keep wires short and direct.

> **BNC center pin:** The BNC panel-mount connector center pin
> has a small solder cup or lug. Strip ¼" of hookup wire and
> solder to this cup. The BNC connector shell is grounded by its
> contact with the box body (Step 3).

---

### Step 8 — Verify Before Closing

**Time: 10 minutes — do not skip this step.**

Before closing the lid, verify all connections with an ohmmeter.

**Continuity checks (switch in BYPASS position):**

| Test | Expected |
|---|---|
| BNC IN center pin → BNC OUT center pin | Continuity (near 0 Ω) |
| BNC IN center pin → BNC shell | Open (no continuity) |
| BNC IN shell → BNC OUT shell → box body | Continuity |

**With switch in ATTENUATE position:**

| Test | Expected |
|---|---|
| BNC IN center → BNC OUT center | Measurable resistance (not 0 Ω) |
| All three sections attenuating | Highest resistance reading |
| BNC IN center → box body (ground) | Some resistance path through shunt R |

> **If you find center-to-shell short at a BNC:** The center
> conductor is touching the shell inside the enclosure. Inspect
> the wiring inside carefully. This is usually a stray wire
> strand or a solder bridge.

> **If all-sections-attenuate reads 0 Ω or very low:** One or
> more bypass wires may have been soldered to throw-B instead of
> throw-A. Check the bypass wire connections on each switch.

---

### Step 9 — Close and Label the Enclosure

**Time: 5 minutes**

1. Tuck wires neatly; nothing should be able to touch the lid and
   create an accidental short.
2. Close the lid. On Hammond 1590A enclosures, the lid has no
   screws; it is held by friction. On screw-top enclosures, snug
   all screws.
3. Apply a strip of masking tape to the top (over the switches)
   and label with permanent marker:
   - Your callsign
   - "ARDF ATTENUATOR"
   - Directions: "↑ = bypass, ↓ = attenuate" (or whichever
     direction you chose for bypass in Step 4)
4. Apply a label strip showing attenuation for each switch
   position:
   ```
   [ 6 dB ]  [ 10 dB ]  [ 20 dB ]
   ```

**Attenuator build is complete. Proceed to testing (Section 7).**

---

## 6. Common Mistakes and Tips

| Mistake | Effect | Prevention |
|---|---|---|
| Plastic enclosure used | No RF shielding; poor performance | Use die-cast aluminum or steel |
| Switches not all oriented the same direction | Confusing in the field | Set all bypass in same lever direction during installation |
| Throw-A and Throw-B reversed on one switch | That section always attenuates or always bypasses, regardless of switch position | Continuity-test in bypass before proceeding to Step 6 |
| R_shunt ground not making contact (anodized surface) | Shunt has no ground reference; T-pad values are wrong | Scrape anodizing before soldering to chassis; verify with ohmmeter |
| Too-long wire leads on resistors | Stray inductance, degraded high-frequency performance | Clip leads to ¼"–⅜" |
| Bypass wire connects wrong throw pair (1–6 instead of 1–4) | Signal path shorted through bypass on wrong toggle position | Use the pin diagram carefully |
| R_series soldered to COM pins instead of Throw-B pins | Attenuation always in circuit; bypass does nothing | Identify and mark each pin before soldering |

---

## 7. Testing and Verification

### 7.1 Bench Test with Ohmmeter (10 minutes per unit)

Equipment: Ohmmeter or DMM.

**With ALL switches in bypass:**
- BNC IN center → BNC OUT center: near 0 Ω (< 2 Ω) ✓
- BNC IN shell → BNC OUT shell: near 0 Ω ✓
- BNC IN center → BNC IN shell: open ✓

**With 6 dB section switched in (others bypass):**
- BNC IN → BNC OUT: should read approximately 5–15 Ω
  (not an exact attenuator measurement with a DMM — just verifies
  the resistors are in circuit)

**With all sections switched in:**
- BNC IN → BNC OUT: measurably higher resistance than above ✓

> **Precision testing:** A proper 50 Ω attenuator cannot be
> accurately tested with a DMM alone. The resistors are in a
> 50 Ω network; DC resistance readings will not tell you the RF
> attenuation value exactly. What you're confirming is that the
> resistors are physically present and connected, not that the
> attenuation is precisely 6 dB.

### 7.2 Functional RF Test (10 minutes)

Use a 2-meter HT and a nearby repeater or beacon, or another
participant's HT transmitting briefly.

1. Connect the Yagi to the attenuator IN, attenuator OUT to the
   HT.
2. With all switches in bypass, observe the S-meter with the Yagi
   pointed at the signal source.
3. Switch in the 20 dB section. The S-meter should drop
   approximately 3–5 S-units (at 6 dB per S-unit,
   20 dB ≈ 3.3 S-units).
4. Switch in the 10 dB section additionally. Another 1–2 S-unit
   drop.
5. Switch in the 6 dB section for maximum attenuation. Another
   fractional S-unit drop.

> **Tip:** S-meter calibration on HTs is notoriously non-linear
> and varies by model. What you're confirming is that:
> (a) each switch causes the signal to decrease when engaged, and
> (b) the decreases are additive.

### 7.3 Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| Signal doesn't change with switches | Bypass wires on wrong throw; signal bypasses all sections | Verify bypass wires are on throw-A, not throw-B |
| Signal drops even when all in bypass | R_series wired to COM pins instead of throw-B | Trace each signal path with ohmmeter in bypass mode |
| One section doesn't attenuate | R_shunt not grounded; resistor not soldered | Check ground connection to chassis; re-solder R_shunt |
| Intermittent behavior | Switch not seating fully in throw positions | Verify switch hardware is tight in enclosure; check for wobble |

---

## 8. References

| Source | Description |
|---|---|
| Chemandy Electronics | RF attenuator calculator (T-pad and pi-pad): [https://www.chemandy.com/calculators/](https://www.chemandy.com/calculators/) |
| ARRL Handbook | Chapter on transmission lines and matching networks; T-pad attenuator design formulas |
| ARDF.net | General ARDF resources: [https://www.ardf.net](https://www.ardf.net) |
| M&K ARC Field Day 2026 — Build Session Syllabus | `docs/field-day-2026/build-event-syllabus.md` |

---

### Quick Reference Card

*Print this section and tape it to the workstation.*

**Resistor Values**

| Section | Switch label | R_series (×2) | R_shunt (×1) |
|---|---|---|---|
| A | 6 dB | 18 Ω | 68 Ω |
| B | 10 dB | 27 Ω | 36 Ω |
| C | 20 dB | 39 Ω | 10 Ω |

**DPDT Switch Wiring Summary**

```
Position: BYPASS (lever to throw-A side)
  Pin 2 → Pin 1 ←bypass wire→ Pin 4 → Pin 5
  T-pad resistors are floating (disconnected)

Position: ATTENUATE (lever to throw-B side)
  Pin 2 → Pin 3 → R_s1 → MID → R_s2 → Pin 6 → Pin 5
                               ↓
                            R_shunt
                               ↓
                             chassis
```

---

*Build instructions version: 1.0*
*Instructor: Tom KE4HET / Mike & Key ARC (K7LED)*
*Last updated: June 2026 (pre-event draft)*

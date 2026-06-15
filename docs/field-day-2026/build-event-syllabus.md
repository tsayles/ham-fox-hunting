# ARDF Equipment Build Session — Syllabus

**Event:** Mike & Key ARC ARRL Field Day 2026
**Date:** Thursday, June 26, 2026 — 13:00–18:00 (proposed)
**Location:** Fort Flagler State Park — Wagon Wheel Group Campsite
**Instructor:** Tom KE4HET
**Support:** M&K ARC volunteers (TBD)

---

## Table of Contents

1. [Session Overview](#1-session-overview)
2. [Pre-Session Instructor Checklist](#2-pre-session-instructor-checklist)
3. [Project 1 — 2-Meter Tape Measure Yagi](#3-project-1--2-meter-tape-measure-yagi)
4. [Project 2 — Switched Step Attenuator](#4-project-2--switched-step-attenuator)
5. [Testing and Verification](#5-testing-and-verification)
6. [Tools List](#6-tools-list)
7. [Timeline Summary](#7-timeline-summary)
8. [References](#8-references)

---

## 1. Session Overview

### Goals

Participants leave Thursday afternoon with two working pieces of ARDF
(Amateur Radio Direction Finding) equipment — a 3-element tape measure
Yagi antenna and a 3-section step attenuator — ready to use at the
ARDF demonstration on the Parade Grounds on Saturday and Sunday.

The session is hands-on from the first minute. Instruction happens at
the bench, not the whiteboard. Every participant builds their own kit.

### Audience

- Licensed amateur radio operators (any license class)
- 1–10 participants
- Assumed skill level: can solder, can use hand tools, can follow
  written instructions. Not beginners — treat them as capable adults.
- No prior antenna-building experience required.

### Context

The completed antennas and attenuators will be used by participants
and loaned to members of the public at the ARDF demonstration hosted
by Mike & Key ARC at Battery Grattan / Parade Grounds, Fort Flagler
State Park, Saturday June 28 and Sunday June 29, 2026.

### Location & Logistics

| Item | Notes |
|---|---|
| Site | Wagon Wheel group campsite, Fort Flagler State Park |
| Power | **Limited / none.** All tools must be battery or propane powered. No AC assumed. Plan accordingly. |
| Tables | Bring folding tables — 1 per 2 participants minimum |
| Shade | Bring a canopy or schedule session in natural shade |
| Weather | June on the Olympic Peninsula — prepare for wind and possible light rain |
| Noise | Campsite is shared — keep generator use minimal |

### Schedule at a Glance

| Time | Activity |
|---|---|
| 12:30 | Instructor arrives; stage all tools, kits, and tables |
| 13:00 | Welcome, safety brief, session overview (10 min) |
| 13:10 | **Project 1: Tape Measure Yagi** begins |
| 15:10 | Yagi complete; break (15 min) |
| 15:25 | **Project 2: Step Attenuator** begins |
| 17:15 | Attenuator complete |
| 17:15 | **Testing and verification** (30 min) |
| 17:45 | Wrap-up, Q&A, pack up (15 min) |
| 18:00 | Session ends |

**Total session duration: approximately 5 hours**

See [Section 7](#7-timeline-summary) for a step-by-step time budget.

---

## 2. Pre-Session Instructor Checklist

Complete these tasks before arriving on Thursday.

### Procurement (order at least 2 weeks in advance)

- [ ] Purchase all Project 1 (Yagi) materials — see BOM in Section 3
- [ ] Purchase all Project 2 (Attenuator) materials — see BOM in
      Section 4
- [ ] Pre-cut RG-58 coax to 6-foot lengths; crimp or solder one
      BNC-male connector on each length; label with masking tape
- [ ] Buy a backup set of each most-breakable item: extra BNC
      connectors, extra hose clamps, extra resistors
- [ ] Verify you have soldering irons for the expected headcount
      (minimum 1 iron per 2 participants)
- [ ] Charge all battery-powered tools
- [ ] Print this syllabus (one copy per participant + one instructor
      copy)

### Kit Preparation

Pre-sort materials into labeled zip-lock bags, one full kit per
participant. Label each bag with the participant's callsign or just
"Kit 1", "Kit 2", etc.

**Each Yagi kit bag contains:**
- 1× 25 ft tape measure (in original case)
- 2× ¾" PVC cross fitting
- 2× ¾" PVC T fitting
- 6× stainless hose clamps (½"–1¼")
- 1× 6 ft RG-58 pigtail with BNC-male (pre-built by instructor)
- 1× 6" piece of 14 AWG solid copper wire (pre-cut)
- Small piece of fine sandpaper (80–120 grit)
- 2 cable ties

**Each attenuator kit bag contains:**
- 3× DPDT ON-ON miniature toggle switch
- 2× BNC female panel-mount connector
- 1× small metal project box (Hammond 1590A or equivalent)
- Resistors (pre-sorted in a small envelope):
  - 2× 18 Ω, 1× 68 Ω  (6 dB section)
  - 2× 27 Ω, 1× 36 Ω  (10 dB section)
  - 2× 39 Ω, 1× 10 Ω  (20 dB section)
- 2× short pieces of hookup wire (~22–24 AWG, 3" each, for bypass
  wires)
- 1× small strip of perfboard (~1" × 3"), optional

**Shared supplies (instructor brings, not per-kit):**
- Solder (60/40 or 63/37 rosin-core, 0.032")
- Flux pen or rosin flux
- Electrical tape (2 rolls)
- Cable ties (bag)
- Wire strippers (instructor + 1–2 spares)
- Drill + ¼" and ½" bits (for attenuator enclosures)
- Denatured alcohol + cotton swabs (flux cleanup)
- Extra 14 AWG wire and RG-58 scraps for mistakes
- Masking tape + permanent marker (labeling)
- First aid kit

### Day-of Setup

- [ ] Set up tables with 18"–24" workspace per participant
- [ ] Place a cutting mat or piece of cardboard on each table (for
      hack-sawing and drilling)
- [ ] Set up one soldering station per 2 participants: iron, stand,
      tip cleaner, solder, flux, small fan for fume dispersal
- [ ] Lay out a kit bag and printed instruction sheet at each station
- [ ] Stage PVC pipe (cut to rough length or full 10 ft) for
      distribution
- [ ] Have the drill and enclosures ready at one central station for
      Project 2

---

## 3. Project 1 — 2-Meter Tape Measure Yagi

### Background

This is the classic 3-element tape measure Yagi popularized by Joel
Hartman WB2HOL for amateur ARDF (fox hunting). It has approximately
7 dBd of forward gain, a clean cardioid pattern with a pronounced
forward lobe, and a deep rear null useful for close-in signal bearing.

The antenna is cut for approximately 146 MHz (2-meter simplex/ARDF
frequencies). As a receive-only antenna for fox hunting, resonance
is not critical — a 2–3% variation in element length has negligible
effect on receive sensitivity or directional performance.

The spring-steel tape measure elements fold flat for transport and
spring back to shape for use. The PVC boom is light enough to wave
around one-handed for extended periods.

### Bill of Materials — Yagi

> **Target cost:** ~$30–35 per kit when ordered in bulk for 10
> participants. Individual retail purchase: ~$38–45.

| Qty | Item | Notes | Est. Cost |
|-----|------|-------|-----------|
| 1 | 25 ft × 1" wide steel tape measure | Stanley, Craftsman, or similar. Must be at least 25 ft. **1" blade width is critical** — wider blades are too stiff; narrower won't tune correctly. | $6–10 |
| 1 | 10 ft length of ¾" Schedule 40 PVC pipe | Available at any hardware store. One 10 ft stick yields boom + handle for one kit with material to spare. | $4–6 |
| 2 | ¾" PVC cross (4-way) fittings | One for reflector position, one for driven element. | $1.50–3.00 each |
| 2 | ¾" PVC T fittings | One for director (front), one for handle grip (rear). | $0.75–1.50 each |
| 6 | Stainless steel hose clamps, ½"–1¼" range | Buy a 10-pack and split among kits. Must be worm-drive (screw-tighten), not spring-type. | ~$7–10/10-pack |
| 1 | RG-58/U coax pigtail, 6 ft, BNC-male one end | Pre-built by instructor. Or buy a 6 ft BNC-M–BNC-M jumper and cut one BNC off. | $4–7 |
| 1 | 14 AWG solid copper wire, 6" piece | Pre-cut. From a scrap of THHN or solid hookup wire. | <$0.50 |
| — | Rosin-core solder, 60/40 | Shared supply | — |
| — | Fine sandpaper, 80–120 grit | One small piece per kit | <$0.25 |
| — | Electrical tape | Shared supply | — |
| — | 2 cable ties | For coax routing | <$0.25 |

**Per-kit total (bulk purchasing): ~$30–36**

#### Sourcing Suggestions

- **Tape measures:** Home Depot or Lowe's in-store (~$6–8 for a basic
  Stanley or store brand). Alternatively, buy a 4-pack on Amazon for
  ~$20–24 ($5–6 each). Avoid "autolock" models — the blade needs to
  retract freely so you can slide it through the hose clamps.
- **PVC pipe and fittings:** Any hardware store, plumbing section.
  Buy fittings individually — cross fittings may not be in the "grab
  bag" section, look for individual ¾" DWV or pressure fittings.
- **Hose clamps:** Hardware store, automotive section. Buy a 10-pack.
  Specify "worm-drive" or "screw-type". Size range ½"–1¼" works;
  pack labeled "12–20 mm" or "5/16"–¾" will also fit ¾" PVC OD.
- **RG-58 pigtails:** Build from bulk RG-58 ($0.30/ft) + BNC crimp
  connectors ($0.80–1.50 each). Or buy pre-made 6 ft BNC jumpers on
  Amazon (search "6 ft RG-58 BNC cable", ~$5–8 each) and cut one
  connector off.

### Tools Required — Yagi

*(See also Section 6 for full tools list)*

| Tool | Notes |
|---|---|
| Tin snips or aviation shears | For cutting tape measure blade |
| PVC pipe cutter or fine-tooth handsaw | Ratchet-style PVC cutter is fastest |
| Measuring tape or ruler | One per participant |
| Screwdriver (flat) or ¼" nut driver | For hose clamp screws |
| Soldering iron (25–40 W) | One per 2 participants |
| Helping hands / alligator clip holder | Strongly recommended for driven element soldering |
| Fine sandpaper (80–120 grit) | Included in kit |
| Wire strippers | For coax prep |
| Needle-nose pliers | For bending hairpin wire |
| Permanent marker | For marking cut lines on tape measure |

---

### Step-by-Step Build Instructions — Yagi

> **Before you start:** Lay out all parts and verify against the BOM.
> Read through all steps before picking up any tools.

---

#### Step 1 — Cut the PVC Boom Pieces

**Time: 15 minutes**

Cut the 10 ft PVC stick into the following pieces using a PVC cutter
or fine-tooth saw. Label each piece with masking tape as you cut.

| Label | Length | Purpose |
|---|---|---|
| **Boom-A** | 11¼" (11.25") | Reflector cross ↔ driven element cross |
| **Boom-B** | 6⅞" (6.875") | Driven element cross ↔ director T |
| **Handle** | 14–18" | Operator handle (cut to preference) |

> **Tip:** Deburr the cut ends with sandpaper or a utility knife so
> the pipe slides fully into the fittings. A rough cut end can prevent
> the pipe from seating properly.

> **PVC cutter tip:** Score around the pipe once with light pressure,
> then increase pressure on each revolution. The ratchet-style cutter
> makes cleaner cuts with less effort than a hacksaw.

---

#### Step 2 — Dry-Fit the PVC Frame

**Time: 10 minutes**

Assemble the boom WITHOUT glue (dry fit only). The design works
correctly without PVC cement — the fit is snug enough for field use.

**Boom layout, front to back:**

```
[Director T] ←Boom-B→ [Driven Cross] ←Boom-A→ [Reflector Cross] ←Handle→ [Handle T]
   (front)                (center)                  (rear)
```

1. Push Boom-B into one socket of the director T fitting (front).
2. Push the other end of Boom-B into one socket of the driven element
   cross fitting (center).
3. Push Boom-A into the opposite socket of the driven element cross.
4. Push the other end of Boom-A into one socket of the reflector
   cross fitting (rear).
5. Push the Handle piece into the fourth socket of the reflector
   cross (pointing toward the operator).
6. Push the Handle T fitting onto the far end of the Handle piece for
   a T-grip.

The boom should look like this from above (elements will be horizontal,
perpendicular to the boom):

```
   Director                  Driven Element    Reflector
      ↕                    ↕    ↕    ↕           ↕
[T]──────────[Cross]──────────[Cross]──────────[Cross]──[Handle]──[T]
  ←— 8" C-C —→              ←——— 12½" C-C ———→
```

> **Verify spacing:** With the boom assembled, measure center-to-center
> from the director T to the driven element cross. This should be ~8".
> From the driven element cross to the reflector cross should be
> ~12½". If your measurements are off, check that the pipe is seated
> fully into each fitting.

> **Do NOT glue yet.** You may need to disassemble to route the coax
> through the boom in Step 9.

---

#### Step 3 — Cut the Tape Measure Elements

**Time: 20 minutes**

Cut the tape measure blade into the following pieces using tin snips.
Measure carefully — cut a little long first and trim to final length.
Mark each cut line with a permanent marker before cutting.

| Element | Length | Quantity |
|---|---|---|
| Reflector | **41⅜"** (41.375") | 1 piece |
| Driven element half (×2) | **17¾"** (17.75") each | 2 pieces |
| Director | **35⅛"** (35.125") | 1 piece |

**Total tape measure consumed: 41.375 + 17.75 + 17.75 + 35.125 = ~112"
(9 ft 4 in) — well within the 25 ft tape measure.**

> **Cutting safety:** Tin snips leave sharp edges. Wear gloves or work
> carefully. Immediately deburr cut ends by running a piece of
> sandpaper across the edge twice, or fold the cut end over briefly
> with pliers to dull the corner.

> **Measuring tip:** The tape measure blade IS the ruler. Extend the
> blade, mark the cut points with a marker while it's still extended,
> then lay it on a flat surface (cutting mat) to cut. Don't try to
> cut in mid-air.

> **Common mistake:** Cutting the driven element halves too short. The
> 1" gap between the two halves is in addition to each half's length.
> Total driven element length = 17¾" + 1" gap + 17¾" = 36½".

---

#### Step 4 — Prepare the Driven Element Tips

**Time: 15 minutes — this is the most important soldering prep step.**

The two driven element halves need to be tinned at their inner ends
(the ends that will face each other with the 1" gap). This is much
easier to do before mounting the elements.

1. Sand the **painted/chrome side** of the inner corner of each driven
   element half. Sand an area about ½" × ½" at the inner tip. The
   goal is bare, shiny steel — no paint, no chrome, no oxidation.
   The blade's reverse (dull) side may sand easier; check which side
   has less coating.

   > **Why the corner?** The hose clamps will grip the blade flat.
   > The soldering connection goes at the corner of the blade tip so
   > the coax and hairpin wire attach there while the clamp holds the
   > element flat and centered.

2. Apply a small drop of rosin flux to each sanded area.

3. Touch the soldering iron to the sanded/fluxed area for 3–5 seconds
   to heat the metal, then apply a small amount of solder. The solder
   should flow onto the steel blade and stick (tin the surface).

   > **The steel blade is a heat sink.** You need a hot iron (at
   > least 700°F / 370°C tip temperature) and patience. Hold the
   > iron still for several seconds before applying solder. If the
   > solder beads up and rolls off, the metal isn't hot enough yet.

4. Repeat for the second driven element half.

5. Set both tinned halves aside — they will cool quickly. The tinned
   area should look silver and smooth, not blobby.

---

#### Step 5 — Mount the Reflector and Director Elements

**Time: 10 minutes**

1. Slide the reflector element (41⅜") through the two opposing arms
   of the **reflector cross** fitting (the rear cross on the boom).
   Center the element so equal lengths stick out on each side.

2. With the element centered, secure it with two hose clamps — one
   on each side of the fitting. The clamp goes over the fitting body
   and the tape measure blade together. Tighten firmly with a
   screwdriver or nut driver. The blade should not slide or rotate.

3. Slide the director element (35⅛") through the single arm of the
   **director T** fitting (the front T fitting). Center it. Secure
   with one hose clamp on each side of the T fitting.

> **Hose clamp fit check:** The hose clamp should encircle both the
> PVC fitting body and the tape measure blade, clamping them together.
> If the clamp is too large, it will tighten over the fitting but not
> grip the blade. If too small, it won't fit around the fitting. The
> ½"–1¼" range fits ¾" Schedule 40 PVC fittings correctly.

> **Element centering:** Use your ruler. Measure from the fitting
> center to each blade tip — they should be equal within ⅛".

---

#### Step 6 — Mount the Driven Element Halves

**Time: 10 minutes**

1. Slide the first driven element half (17¾") into one arm of the
   **driven element cross** fitting. The tinned tip should face
   **inward** (toward the center of the cross).

2. Slide the second driven element half into the **opposite** arm of
   the same cross fitting. Its tinned tip also faces inward.

3. Position both halves so:
   - Each blade extends **17¾"** from the fitting center to its tip
   - The gap between the two inner tips is **1 inch**
   - Both blades are in the same plane (co-planar — not twisted)

4. Secure each half with a hose clamp as in Step 5 (one clamp per
   half, gripping the fitting body and blade).

> **The 1" gap is critical.** This gap is part of the driven element
> impedance match along with the hairpin. Too narrow or too wide will
> affect the match. Use a ruler or a 1" spacer block to set the gap
> before tightening the clamps.

> **Common mistake:** Mounting both halves with the tinned corners
> pointing the same direction (both up or both down). They should be
> mirror images, with both tinned corners accessible from the same
> side of the boom for soldering.

---

#### Step 7 — Fabricate and Attach the Hairpin Match

**Time: 15 minutes**

The "hairpin" (beta match) is a short U-shaped wire that bridges the
gap between the two driven element halves. It adjusts the feedpoint
impedance to better match the 50 Ω coax.

1. Take the 6" piece of 14 AWG solid copper wire. Strip ¼" of
   insulation from each end (if insulated). If using bare copper, no
   prep needed.

2. Using needle-nose pliers, bend the wire into a symmetrical U-shape.
   The two parallel legs of the U should be approximately ¾" apart
   at the tips.

   ```
       ┌──────────────┐   ← ~3" of wire across the top
       │              │
       │  ←~ ¾" →    │   ← gap between legs
       ↓              ↓
   (solders to)  (solders to)
   left element  right element
   ```

3. Lay the U-shape across the 1" gap between the driven element
   halves, with each leg resting on one of the tinned corners.

4. Solder each leg of the hairpin wire to its driven element tip. The
   wire should sit flat on the tinned area. Heat the junction until
   the existing tinning on the blade reflowing joins the hairpin wire
   solder for a solid joint.

> **The hairpin spans the gap:** The hairpin wire's legs solder to the
> tinned corners of the elements, bridging across the gap. Don't worry
> if the geometry isn't perfect — a small difference in leg length or
> gap width has minimal effect on receive performance.

> **Do NOT short the two driven element halves together.** There must
> still be a gap — the hairpin wire is the only metal bridge between
> the two halves.

---

#### Step 8 — Prepare the Coax Feedline

**Time: 10 minutes**

If the instructor pre-built the coax pigtails, the BNC-male end is
already assembled. You only need to prepare the bare end for
soldering.

**Coax prep at the bare (non-BNC) end:**

1. Remove the outer jacket for about 1". Score carefully around the
   circumference with a utility knife; do not cut deep enough to nick
   the braid.

2. Fold the braid back to expose ½" of dielectric (inner insulation).
   Gather the braid into a small bundle on one side.

3. Score and remove the dielectric for about ½", exposing the center
   conductor.

4. Apply flux and tin the center conductor (twist the strands together
   first if stranded). Tin the gathered braid bundle.

> **Do not nick the center conductor.** Stranded center conductor in
> RG-58 is thin — a partial nick will be a weak point. If you nick
> it, cut back 1" and re-strip.

---

#### Step 9 — Solder the Coax to the Driven Element

**Time: 10 minutes**

1. Decide on coax routing now (see tip below).

2. Hold the tinned center conductor against one of the two tinned
   corners of the driven element (the same corner where the hairpin
   wire is soldered). Apply heat and flow solder to create a joint
   that connects the coax center AND the hairpin leg to the element.

3. Hold the tinned braid against the tinned corner of the **other**
   driven element half. Solder similarly.

   > **Which side gets center vs. braid?** For a receive-only fox
   > hunting antenna, it does not matter. The antenna works either way.

4. Verify with visual inspection:
   - Center conductor is soldered to one element half
   - Braid is soldered to the **other** element half
   - Center and braid are **not** shorted to each other
   - The hairpin wire is still present (check it didn't get
     accidentally soldered over)

> **Routing tip:** Before soldering, decide whether to run the coax
> **inside** the PVC boom (thread it through the hollow pipe — looks
> clean, requires disassembling the boom) or **outside** (secure with
> cable ties along the boom — faster). For a one-day build, outside
> routing is acceptable. Thread a cable tie through the hose clamp
> screw slot nearest the driven element and use it to anchor the coax.

---

#### Step 10 — Final Assembly and Inspection

**Time: 10 minutes**

1. Route and secure the coax along the boom with 2 cable ties.

2. Reassemble the PVC boom if it was taken apart for coax routing.
   Verify all pipe-to-fitting connections are fully seated.

3. Wrap the driven element coax connections with two layers of
   electrical tape to protect from weather and accidental shorts.

4. Fold the antenna elements down flat for transport by gently
   bending the tape measure blades back toward the boom. They will
   spring back to shape when deployed.

5. Final dimensional check:

| Check | Nominal | Accept range |
|---|---|---|
| Reflector length | 41⅜" | 41"–41¾" |
| Each driven element half | 17¾" | 17½"–18" |
| Driven element gap | 1" | ¾"–1¼" |
| Director length | 35⅛" | 34¾"–35½" |
| Reflector–Driven spacing (C-C) | ~12½" | 12"–13" |
| Driven–Director spacing (C-C) | ~8" | 7½"–8½" |

**Congratulations — the Yagi is complete. Set it aside; testing
is in Section 5.**

---

### Common Mistakes and Tips — Yagi

| Mistake | Effect | Prevention |
|---|---|---|
| Tape measure is too narrow (½" blade) | Floppy element, wrong tuning | Verify 1" width before buying |
| Elements not centered on the fitting | Off-axis pattern, mechanical stress | Measure and center before clamping |
| Hose clamp too large, doesn't grip tape | Elements will slip under the clamps | Use the right clamp size (½"–1¼" range) |
| Tinning the driven element without flux | Solder beads up, won't stick | Flux first, heat the metal thoroughly |
| Driven element halves not co-planar | Crooked pattern, awkward handling | Lay both halves flat on the table before clamping |
| Shorting center to braid at driven element | Antenna won't work at all | Inspect visually before taping; use ohmmeter |
| Driven element gap wrong | Poor impedance match, reduced sensitivity | Set gap with a 1" block before tightening clamps |
| PVC cement used before testing | Can't adjust spacing later | Stay dry-fit through the build session |

---

## 4. Project 2 — Switched Step Attenuator

> **Feasibility note:** The attenuator adds approximately $22–28 per
> participant to the session cost, bringing the total kit cost to
> roughly $52–64 per person. This is modestly over the $50 target,
> but is achievable with bulk purchasing. The attenuator is strongly
> recommended — without it, the fox hunt becomes difficult as
> participants get close to the transmitter because the HT receiver
> front end is overloaded.

### Background

As you walk toward the fox, the received signal gets stronger. At
close range (within 100 ft) the signal can be so strong that the HT's
front end saturates, making the S-meter peg at maximum from every
direction. An attenuator sits between the antenna and the HT, reducing
the signal level so that meaningful directional null-finding remains
possible even at close range.

This design provides three independently switched attenuation
sections — 6 dB, 10 dB, and 20 dB. The sections can be combined in
any combination, giving 8 attenuation levels:

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

### Circuit Description

Each section is a **T-type RF attenuator** (T-pad): two series
resistors with one shunt resistor to ground in the middle, designed
for a 50 Ω system. Each section is switched in or out of the signal
path by a DPDT ON-ON toggle switch.

**Full attenuator schematic (all 3 sections):**

![3-Section Switched Step Attenuator](attenuator-schematic.png)

*Blue arches = DPDT bypass path (switch in BYPASS position, signal
passes through). Black path = signal through T-pad (switch in
ATTENUATE position). Shunt resistors R2 connect mid-node to chassis
ground.*

When the toggle switch is in **bypass** position:
- Both switch commons are connected directly to each other via a
  short bypass wire (signal passes straight through, T-pad floats)

When the toggle switch is in **attenuate** position:
- Signal routes through both series resistors
- The shunt resistor connects the midpoint (MID) to chassis ground

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
> receive-only fox hunting use, ¼ W is sufficient and much cheaper.

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

> **ATTENUATE mode (switch to throw B):** Pins 2–3 connected, 5–6
> connected. Signal goes 2→3→R_s1→MID→R_s2→6→5. R_shunt connects
> MID to chassis ground.

**Three sections are wired in series:** The output of one section
(pin 5) feeds directly to the input of the next section (pin 2).

```
BNC IN → [Section A: 6 dB] → [Section B: 10 dB] → [Section C: 20 dB] → BNC OUT
```

### Bill of Materials — Attenuator

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

> **Resistor sourcing:** Buy an assortment kit from Amazon (500-piece
> or 1000-piece metal film assortment, ~$8–12) and pull the values
> you need. Or order from Digi-Key / Mouser; at small quantities, a
> resistor costs $0.08–0.15 each. For 10 participant kits, you need
> 20× 18 Ω, 10× 68 Ω, 20× 27 Ω, 10× 36 Ω, 20× 39 Ω, 10× 10 Ω.

> **BNC connectors:** 10-pack on Amazon is ~$8–10. Leftover connectors
> are useful for future projects.

> **Hammond 1590A alternative:** Any die-cast or stamped-steel box
> in the 3"–4" range works. Plastic boxes are NOT acceptable — they
> provide no RF shielding and the attenuator will behave poorly.
> "Project box" listings on Amazon that say "aluminum" are usually
> acceptable; "ABS" or "polycarbonate" are not.

#### Sourcing Suggestions

- **Switches:** Amazon search "DPDT ON-ON mini toggle switch 6 pin"
  — buy a 10-pack (~$8–12) so you have spares. Confirm they are
  ON-ON (not ON-OFF-ON, which has 3 positions).
- **BNC connectors:** Amazon, Digi-Key, Mouser. Search "BNC female
  panel mount" or "BNC chassis mount". Buy a 10-pack.
- **Enclosures:** Hammond 1590A from Amazon, Digi-Key, or Mouser
  (~$10–12 each). Order in advance; this is the longest-lead item.
- **Resistors:** 1% metal film assortment kit from Amazon (~$8–12 for
  500-piece kit). Confirm the kit includes 10 Ω, 18 Ω, 27 Ω, 36 Ω,
  39 Ω, 68 Ω. Most 600-value kits include these.

### Tools Required — Attenuator

| Tool | Notes |
|---|---|
| Electric drill with bits | ⅜" or ½" bit for BNC holes; ¼" bit for toggle switch holes. One drill handles the whole group. |
| Drill bit sizes | Verify against your specific BNC and switch hardware before drilling |
| Step drill ("unibit") | Optional — makes cleaner holes in thin aluminum than twist bits |
| Round file or needle file | Deburring drill holes in the enclosure |
| Soldering iron (25–40 W) | Same iron as used for the Yagi |
| Small flat screwdriver | For tightening BNC and switch hardware |
| Ohmmeter / continuity tester | **Essential for verifying wiring before closing the box** |
| Needle-nose pliers | For bending resistor leads |
| Masking tape + permanent marker | Labeling the switches |

---

### Step-by-Step Build Instructions — Attenuator

> **Before you start:** Study the wiring diagram in the Circuit
> Description above until you can explain it in your own words.
> Mistakes in the attenuator are easier to prevent than to debug.

---

#### Step 1 — Plan the Enclosure Layout

**Time: 10 minutes**

Before drilling, mark all hole positions with a permanent marker on
masking tape applied to the enclosure. This lets you re-mark without
leaving permanent marks on the box if you need to adjust.

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
- BNC female panel-mount: typically ⅜" (9.5 mm) body hole; verify
  against your specific connector before drilling
- Miniature toggle switch: typically 15/64" (6 mm); verify against
  your specific switch

> **Verify before drilling:** Each BNC connector and each switch
> should come with a spec sheet or packaging that lists the panel
> hole diameter. Check it. Aluminum is easy to enlarge with a file
> but impossible to shrink.

---

#### Step 2 — Drill and Prepare the Enclosure

**Time: 15 minutes (shared drill — participants queue)**

Set up the drill station centrally. One person drills for the group
to keep it safe and efficient.

1. Punch or score a center mark for each hole using a nail or center
   punch and a rock (no mallet available in the field — improvise).
2. Drill pilot holes (⅛") at each marked position.
3. Enlarge to final size: ⅜" for BNCs, drill size per toggle switch
   spec.
4. Deburr all holes with a needle file or the back edge of the drill
   bit. The BNC connector and switch bushings must seat flush with
   the enclosure face.
5. Test-fit one BNC and one switch in their holes before proceeding.
   Adjust with a round file if needed.

> **Aluminum tip:** Die-cast aluminum drills easily but can grab. Use
> slow drill speed with light pressure. Don't force. A center punch
> mark prevents the bit from wandering.

---

#### Step 3 — Install the BNC Connectors

**Time: 10 minutes**

1. Insert the BNC connector into the IN-side hole (left end).
2. Thread the lock washer and nut onto the connector from inside the
   box. Tighten finger-tight, then snug with pliers (do not over-
   tighten aluminum threads). The connector body must contact the box
   wall for the shield/ground connection.
3. Repeat for the BNC OUT connector (right end).
4. Verify: both connectors are tight, both ground properly to chassis
   (check continuity from BNC shell to box body with an ohmmeter).

---

#### Step 4 — Install the Toggle Switches

**Time: 10 minutes**

1. Insert each DPDT switch through its hole in the top of the box.
2. Ensure the switch is oriented consistently: all three switches
   should have throw-A (bypass) in the same physical position (e.g.,
   all lever-up = bypass, all lever-down = attenuate). This reduces
   confusion in the field.
3. Thread lock washer and nut; tighten firmly. The switch should not
   rotate.
4. **Label with masking tape now, before wiring makes the labels hard
   to reach:**
   - Left switch: "6 dB"
   - Center switch: "10 dB"
   - Right switch: "20 dB"
   - Mark the bypass position (lever direction = bypass) with a dot
     or "0".

---

#### Step 5 — Wire the Bypass Connections

**Time: 15 minutes**

For each of the three switches, wire the bypass (Throw A) pins
together with a short piece of hookup wire:

- Connect Pin 1 (Throw A, Pole 1) to Pin 4 (Throw A, Pole 2) with
  a 1"–2" wire inside the enclosure. This wire is the "bypass path"
  for that section.

Repeat for all three switches. You now have three bypass wires
soldered, one per switch.

> **Wire length:** Keep these wires as short as physically possible.
> At 146 MHz, stray inductance from long wires matters. 1"–2" is
> adequate. Route the wire directly between the two pins.

> **Polarity:** The bypass wire always connects the Throw-A pin of
> Pole 1 to the Throw-A pin of Pole 2. If you later discover the
> switch is oriented with throw-B at the top, swap which throw you
> call "A" consistently — just be consistent across all three
> switches.

---

#### Step 6 — Build and Solder the T-Pad Resistor Networks

**Time: 25 minutes**

For each section, build the T-pad "network" off the switch before
wiring it in. Pre-build and inspect each section before soldering
to the switch.

**Section A — 6 dB:**

1. Take two 18 Ω resistors (R_s1, R_s2) and one 68 Ω resistor
   (R_shunt).
2. Twist one lead of R_s1 and one lead of R_s2 together — this is
   the MID node.
3. Connect the R_shunt: twist one of its leads to the same MID node
   bundle. The other lead of R_shunt will go to chassis (box body).
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
   enclosure** (scrape paint/anodizing off a small spot on the inner
   wall, or solder to the threaded body of one of the BNC connectors,
   which is grounded to chassis).

Repeat for **Section B (10 dB):** 2× 27 Ω + 1× 36 Ω, on Switch B.
Repeat for **Section C (20 dB):** 2× 39 Ω + 1× 10 Ω, on Switch C.

> **Resistor lead length:** Clip resistor leads to ¼"–⅜" before
> soldering. Short leads reduce stray inductance. Bend leads at
> right angles so resistors sit flat.

> **Chassis ground for R_shunt:** If the enclosure body is
> anodized (shiny silver/grey), the anodizing is non-conductive.
> You must scrape a small bare metal area to make a ground
> connection. Use the tip of a file or scratch with a pocket knife.
> Alternatively, run the R_shunt free ends to the threaded nut on
> a BNC connector (which is confirmed ground from Step 3).

---

#### Step 7 — Wire the Sections in Series

**Time: 10 minutes**

Connect the three sections in signal chain order: 6 dB → 10 dB →
20 dB, BNC-IN to BNC-OUT.

1. **BNC IN pin** (center pin of IN-side BNC) → **Pin 2** (COM,
   Pole 1) of Switch A (6 dB section).
2. **Pin 5** (COM, Pole 2) of Switch A → **Pin 2** (COM, Pole 1) of
   Switch B (10 dB section).
3. **Pin 5** (COM, Pole 2) of Switch B → **Pin 2** (COM, Pole 1) of
   Switch C (20 dB section).
4. **Pin 5** (COM, Pole 2) of Switch C → **BNC OUT pin** (center pin
   of OUT-side BNC).

> **Wire routing:** Route signal path wires as directly as possible.
> Avoid running them past grounded walls at right angles. Keep wires
> short and direct. This is a functional attenuator, not a lab
> instrument — but good habits produce better results.

> **BNC center pin:** The BNC panel-mount connector center pin has a
> small solder cup or lug. Strip ¼" of hookup wire and solder to
> this cup. The BNC connector shell is grounded by its contact with
> the box body (Step 3).

---

#### Step 8 — Verify Before Closing

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
> conductor is touching the shell inside the enclosure. Inspect the
> wiring inside carefully. This is usually a stray wire strand or a
> solder bridge.

> **If all-sections-attenuate reads 0 Ω or very low:** One or more
> bypass wires may have been soldered to throw-B instead of throw-A.
> Check the bypass wire connections on each switch.

---

#### Step 9 — Close and Label the Enclosure

**Time: 5 minutes**

1. Tuck wires neatly; nothing should be able to touch the lid and
   create an accidental short.
2. Close the lid. On Hammond 1590A enclosures, the lid has no screws;
   it is held by friction. On screw-top enclosures, snug all screws.
3. Apply a strip of masking tape to the top (over the switches) and
   label with permanent marker:
   - Your callsign
   - "ARDF ATTENUATOR"
   - Directions: "↑ = bypass, ↓ = attenuate" (or whichever direction
     you chose for bypass in Step 4)
4. Apply a label strip showing attenuation for each switch position:
   ```
   [ 6 dB ]  [ 10 dB ]  [ 20 dB ]
   ```

**Attenuator build is complete. Testing is in Section 5.**

---

### Common Mistakes and Tips — Attenuator

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

## 5. Testing and Verification

All testing takes place with equipment that can be brought to the
campsite. No lab instruments are required.

### 5.1 Yagi — Continuity Test (5 minutes per antenna)

Equipment: Ohmmeter or DMM in continuity/resistance mode.

1. **Center-to-braid short check:** Probe BNC-male center pin and
   BNC-male shell. Expect: **open** (infinite resistance, no
   continuity). If you read continuity, there is a short in the
   coax, at the BNC connector, or at the driven element. Do not
   proceed until this is resolved.

2. **Driven element wiring:** Probe BNC center pin while touching
   one driven element half with the other probe. Expect: very low
   resistance (< 2 Ω) — this verifies the coax center conductor is
   connected to the element.

3. **Braid-to-element continuity:** Probe BNC shell to the OTHER
   driven element half. Expect: very low resistance (< 2 Ω).

4. **Check hairpin:** With the ohmmeter probes on the two driven
   element halves (the ones with the driven element), expect low
   resistance through the hairpin wire (the two element halves ARE
   connected by the hairpin, so they'll read a low resistance, and
   the coax center/braid are also connected to them — the key is that
   center and shell remain isolated from each other).

   > Note: When probing center vs. shell through the antenna, you will
   > see some resistance (the hairpin and element loops), but a true
   > short (0 Ω) indicates a coax or solder bridge fault.

### 5.2 Attenuator — Bench Test (10 minutes per unit)

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

> **Precision testing:** A proper 50 Ω attenuator cannot be accurately
> tested with a DMM alone. The resistors are in a 50 Ω network; DC
> resistance readings will not tell you the RF attenuation value
> exactly. What you're confirming is that the resistors are physically
> present and connected, not that the attenuation is precisely 6 dB.

### 5.3 Functional RF Test (15 minutes for the group)

This is the real test. Use a 2-meter HT and a nearby repeater or
beacon, or another participant's HT transmitting briefly.

**Yagi test:**
1. Connect the Yagi to an HT via its BNC pigtail.
2. Identify a signal source: a repeater on a known frequency is ideal,
   or another HT held ~50 ft away.
3. Point the Yagi's director (front T connector) at the signal source.
   The S-meter should read higher than with the rubber duck antenna.
4. Rotate the antenna 180° (director away from signal). The S-meter
   should drop noticeably — this is the rear null. A working Yagi
   will show 15–20+ dB front-to-back difference.
5. Slowly rotate the antenna. The signal should be strongest on axis
   with the director and weakest behind the reflector.

> **Tip:** If the antenna shows no directional difference, check for
> a coax center-to-braid short. An omni pattern usually indicates
> the coax is shorted or disconnected at the driven element.

**Attenuator test:**
1. Connect the Yagi to the attenuator IN, attenuator OUT to the HT.
2. With all switches in bypass, observe the S-meter with the Yagi
   pointed at the signal source.
3. Switch in the 20 dB section. The S-meter should drop approximately
   3–5 S-units (at 6 dB per S-unit, 20 dB ≈ 3.3 S-units).
4. Switch in the 10 dB section additionally. Another 1–2 S-unit drop.
5. Switch in the 6 dB section for maximum attenuation. Another
   fractional S-unit drop.

> **Tip:** S-meter calibration on HTs is notoriously non-linear and
> varies by model. Don't expect exactly 3.33 S-units per 20 dB. What
> you're confirming is that:
> (a) each switch causes the signal to decrease when engaged, and
> (b) the decreases are additive.

---

## 6. Tools List

### Instructor Must Bring (bring all of these)

| Tool | Qty | Notes |
|---|---|---|
| Soldering irons, 25–40 W | 2–5 | One per 2 participants. Battery-powered models (e.g., TS100 with 20V battery, or Pinecil) are ideal for no-AC sites |
| Soldering iron stands | 1 per iron | Coil spring type; safe for outdoor tables |
| Tip cleaner (brass wool) | 1 per iron | Better than wet sponge outdoors |
| Solder, 60/40 rosin core, 0.032" | 2 spools | |
| Flux pen (rosin flux) | 2 | |
| DMM / ohmmeter | 2 | For testing each finished build |
| Tin snips / aviation shears | 2–3 | Shared; one per 3–4 participants |
| PVC pipe cutter (ratchet style) | 2 | |
| Fine-tooth handsaw | 1 | Backup for PVC cutting |
| Cutting mat / scrap plywood | 2–3 | Bench protection |
| Measuring tapes, 12"+ | 3–4 | |
| Permanent markers | 4–5 | |
| Masking tape | 2 rolls | |
| Wire strippers, 22–18 AWG | 2–3 | |
| Needle-nose pliers | 3–4 | |
| Flat screwdrivers, small | 3–4 | Hose clamps + BNC/switch hardware |
| ¼" nut driver or 5.5 mm socket + handle | 2 | For hose clamps |
| Electric drill (cordless) | 1 | Fully charged |
| Drill bits: ⅛", ¼", ⅜", ½" | 1 set | For attenuator enclosures |
| Step drill bit (unibit) | 1 | Optional; improves aluminum hole quality |
| Round needle file | 2 | Deburring holes |
| Helping hands (alligator clip soldering aid) | 2–4 | |
| Small fan or folded cardboard | 2 | Flux fume dispersal |
| Denatured alcohol + cotton swabs | 1 bottle, 20 swabs | Flux cleanup |
| First aid kit | 1 | Tin snips and irons cause injuries |
| Nitrile gloves | 10 pairs | Optional; for those who prefer |
| Safety glasses | 5–10 pairs | Cutting springs can cause flying debris |
| Folding tables, 6 ft | 2–3 | 1 per 2–3 participants |
| Canopy / EZ-up | 1 | Sun and rain cover |
| Extension cord (12 ft) | 1 | If any AC power is available nearby |
| Printed syllabus copies | N + 2 extras | One per participant + instructor copies |
| Zip-lock bags (quart) | Several | Spare parts, hardware sorting |
| Trash bag | 2 | Cleanup |

### Participants Should Bring (if possible)

| Item | Notes |
|---|---|
| Their own HT (2-meter) | For functional RF testing |
| BNC adapter for their HT | If HT uses SMA or other connector |
| Their own multimeter/DMM | Speeds up testing if multiple units available |
| Their own soldering iron | If they have a good travel iron |
| Safety glasses | |
| Work gloves | For tin snips work |
| Snacks, water | This is a 5-hour outdoor session |

---

## 7. Timeline Summary

The table below shows the complete session timeline with realistic
time estimates. "Fast" assumes an experienced group working smoothly;
"slow" assumes first-time builders with questions. With a mixed group
of 1–10, expect times between these bounds.

| Step | Activity | Fast | Slow |
|---|---|---|---|
| — | Arrival, settle in, distribute kits | 5 min | 10 min |
| **Project 1: Yagi** | | | |
| 0 | Intro: review plan, inspect parts | 5 min | 10 min |
| 1 | Cut PVC boom pieces | 10 min | 20 min |
| 2 | Dry-fit PVC frame, verify spacing | 8 min | 15 min |
| 3 | Cut tape measure elements | 15 min | 25 min |
| 4 | Sand and tin driven element tips | 10 min | 20 min |
| 5 | Mount reflector and director | 8 min | 15 min |
| 6 | Mount driven element halves | 8 min | 15 min |
| 7 | Fabricate and attach hairpin | 10 min | 20 min |
| 8 | Prepare coax pigtail (bare end) | 8 min | 15 min |
| 9 | Solder coax to driven element | 8 min | 15 min |
| 10 | Route coax, final assembly | 7 min | 12 min |
| **Project 1 subtotal** | | **~97 min** | **~167 min** |
| — | **Break** | 15 min | 15 min |
| **Project 2: Attenuator** | | | |
| 1 | Review schematic, inspect parts | 8 min | 15 min |
| 2 | Plan, mark, drill enclosure | 12 min | 20 min |
| 3 | Install BNC connectors | 8 min | 12 min |
| 4 | Install toggle switches | 8 min | 12 min |
| 5 | Wire bypass connections | 10 min | 18 min |
| 6 | Build and solder T-pad networks | 20 min | 35 min |
| 7 | Wire sections in series | 10 min | 18 min |
| 8 | Verify with ohmmeter | 8 min | 15 min |
| 9 | Close and label enclosure | 5 min | 8 min |
| **Project 2 subtotal** | | **~89 min** | **~153 min** |
| — | **Testing and verification** | 20 min | 35 min |
| — | **Wrap-up, Q&A, cleanup** | 15 min | 20 min |
| **Total session** | | **~4 hr 0 min** | **~6 hr 40 min** |

### Recommended Session Plan

**Start: 13:00 (1:00 PM)**
**Buffer break if needed: ~15:00 or after Yagi completion**
**End: 17:30–18:00 (5:30–6:00 PM)**

**Proposed total duration: 5 hours.** This is between fast and slow,
with buffer for questions, equipment issues, and the realities of
an outdoor campsite. With 1–2 participants, the session may finish
in 4 hours. With 8–10 participants all building simultaneously, plan
for 5.5 hours.

#### Instructor Pacing Notes

- If the group is falling behind at the halfway point (Yagi should
  be complete by 15:10), shorten Break or combine Steps 8–10 as a
  group demo rather than individual builds.
- If time is very short, prioritize the Yagi. A working directional
  antenna without an attenuator is still functional for the ARDF
  demo. An attenuator without an antenna is useless.
- If time permits and all attenuators are done by 17:00, conduct a
  group field walk: take one HT + Yagi + attenuator to the Parade
  Grounds and practice bearing runs on the Byonics fox transmitter.
  This is the best possible preparation for Saturday.

---

## 8. References

| Source | Description |
|---|---|
| jpole-antenna.com, 2017 | Primary build reference for Yagi dimensions and assembly: [https://www.jpole-antenna.com/2017/02/07/build-it-2-meter-tape-measure-yagi-beam-antenna/](https://www.jpole-antenna.com/2017/02/07/build-it-2-meter-tape-measure-yagi-beam-antenna/) |
| WB2HOL (Joel Hartman) | Original designer of the tape measure Yagi for ARDF. Original page offline; widely reproduced online. Dimensions used in this syllabus derive from his published design. |
| ARDF.net | General ARDF resources, fox hunting techniques: [https://www.ardf.net](https://www.ardf.net) |
| Homingin.com | ARDF equipment reviews and designs: [https://www.homingin.com](https://www.homingin.com) |
| Chemandy Electronics | RF attenuator calculator (T-pad and pi-pad): [https://www.chemandy.com/calculators/](https://www.chemandy.com/calculators/) |
| ARRL Handbook | Chapter on transmission lines and matching networks; T-pad attenuator design formulas |
| M&K ARC Field Day 2026 — Overall Plan | `docs/field-day-2026/overall-plan.md` in this repository |

---

## Appendix A — Quick Reference Card

*Print this page and laminate it. Tape one to each participant's
workstation.*

### Yagi Element Lengths

| Element | Cut Length |
|---|---|
| Reflector | **41⅜"** |
| Driven element (each half) | **17¾"** |
| Director | **35⅛"** |

### Yagi Boom Spacing (center-to-center)

| Span | Distance |
|---|---|
| Director T ↔ Driven element cross | **~8"** (Boom-B tube = 6⅞") |
| Driven element cross ↔ Reflector cross | **~12½"** (Boom-A tube = 11¼") |

### Attenuator Resistor Values

| Section | Switch label | R_series (×2) | R_shunt (×1) |
|---|---|---|---|
| A | 6 dB | 18 Ω | 68 Ω |
| B | 10 dB | 27 Ω | 36 Ω |
| C | 20 dB | 39 Ω | 10 Ω |

### DPDT Switch Wiring Summary

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

## Appendix B — Troubleshooting Quick Guide

| Symptom | Likely Cause | Fix |
|---|---|---|
| **Yagi:** Antenna is omni-directional (no front-back difference) | Coax center shorted to braid at driven element | Remove tape, visually inspect solder joints; check with ohmmeter |
| **Yagi:** No signal on receive at all | Coax center conductor disconnected | Probe BNC center pin → driven element half; repair joint |
| **Yagi:** Weak signal, poor performance | Element lengths off by more than ½" | Re-measure and trim or replace elements |
| **Yagi:** Elements rotate under load | Hose clamps too loose | Re-tighten; clamp should grip tape blade firmly |
| **Attenuator:** Signal doesn't change with switches | Bypass wires on wrong throw; signal bypasses all sections | Verify bypass wires are on throw-A, not throw-B |
| **Attenuator:** Signal drops even when all in bypass | R_series wired to COM pins instead of throw-B | Trace each signal path with ohmmeter in bypass mode |
| **Attenuator:** One section doesn't attenuate | R_shunt not grounded; resistor not soldered | Check ground connection to chassis; re-solder R_shunt |
| **Attenuator:** Intermittent behavior | Switch not seating fully in throw positions | Verify switch hardware is tight in enclosure; check for wobble |

---

*Syllabus version: 1.0 — drafted for Field Day 2026.*
*Instructor: Tom KE4HET / Mike & Key ARC (K7LED)*
*Last updated: June 2026 (pre-event draft)*

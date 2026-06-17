# Build Instructions — Dual-Band (2m / 70cm) Tape Measure Yagi

**Project:** 3+3 element dual-band tape measure Yagi for 2m and
70cm ARDF (146 MHz + 440 MHz)
**Event:** M&K ARC ARRL Field Day 2026 — Fort Flagler
**Instructor:** Tom KE4HET
**Version:** 1.0 (pre-event draft)

---

## Table of Contents

1. [Background](#1-background)
2. [Design Overview](#2-design-overview)
3. [Bill of Materials](#3-bill-of-materials)
4. [Tools Required](#4-tools-required)
5. [Step-by-Step Build Instructions](#5-step-by-step-build-instructions)
6. [Common Mistakes and Tips](#6-common-mistakes-and-tips)
7. [Testing and Verification](#7-testing-and-verification)
8. [References](#8-references)

---

## 1. Background

Dual-band fox hunting events run two foxes simultaneously — one on
2-meters (typically 146 MHz) and one on 70-centimeters (typically
440 MHz). Participants locate both foxes and report a combined
score. A dual-band yagi lets you use a single handheld (HT) with
dual-band capability and one antenna for both bands, or switch
feeds between two HTs.

This design mounts a full-size 3-element 2m tape measure Yagi and
a full-size 3-element 70cm tape measure Yagi on a shared ¾" PVC
boom. The 70cm elements are housed on a short ½" PVC sub-boom
zip-tied alongside the main boom. Both element sets share the same
25-ft tape measure blade as the source material and use the same
hose clamp technique. Each band has its own coax pigtail.

The 2m section is identical to the single-band 2m design from
`build-instructions-2m-yagi.md`. The 70cm dimensions are scaled
proportionally (frequency ratio: 440/146 ≈ 3.01).

---

## 2. Design Overview

### Antenna Layout

```
← director end                          reflector / handle end →

    70cm  70cm             70cm
    Dir    DE    (gap)     Refl
     ↕     ↕↕↕            ↕
─────────────────────────────────────────── ½" PVC sub-boom
     ↑  2.6"  ↑    4.1"   ↑  (sub-boom spans ~8" working length)
             ↑ 70cm DE coax pigtail exits here

═══════════════════════════════════════════ ¾" PVC main boom
     ↑      ↑                  ↑
    Dir     DE               Refl
     ↕      ↕↕↕               ↕
    2m     2m               2m
    Dir     DE     (gap)    Refl
           ↑ 2m DE coax pigtail exits here

←— 8" C-C —→         ←——— 12½" C-C ———→
```

The two booms are parallel, separated by ~1". The sub-boom's
driven element is aligned with the main boom's driven element
position so both coax pigtails run together toward the handle.

### Band Specifications

| Parameter | 2m section | 70cm section |
|---|---|---|
| Target frequency | 146 MHz | 440 MHz |
| Reflector length | 41⅜" (41.375") | 13¾" (13.75") |
| Driven element (each half) | 17¾" (17.75") | 5⅞" (5.875") |
| Driven element gap | 1" | ⅜" |
| Director length | 35⅛" (35.125") | 11⅝" (11.625") |
| Reflector–Driven C-C | ~12½" | ~4⅛" |
| Driven–Director C-C | ~8" | ~2⅝" |
| Boom material | ¾" Sched. 40 PVC | ½" Sched. 40 PVC |
| Hairpin wire gauge | 14 AWG, 6" piece | 18–20 AWG, 2" piece |
| Coax pigtail | RG-58, 6 ft, BNC-M | RG-58, 3–6 ft, BNC-M |

> **Why ½" PVC for the 70cm sub-boom?** The fittings are lighter
> and shorter than ¾" fittings, keeping the sub-boom compact. The
> element spacing is only a few inches; the ½" fittings fit the
> scale. The same ½"–1¼" hose clamps used for the 2m section
> also fit ½" PVC fittings.

---

## 3. Bill of Materials

> **Target cost:** ~$46–56 per kit (bulk purchasing). This is
> higher than the single-band kit because it adds materials for
> the 70cm section.

### 2m Section (main boom — same as single-band design)

| Qty | Item | Notes | Est. Cost |
|-----|------|-------|-----------|
| 1 | 25 ft × 1" wide steel tape measure | Provides elements for both bands. Stanley, Craftsman, or similar. 1" blade width required. | $6–10 |
| 1 | 10 ft length of ¾" Schedule 40 PVC pipe | Boom + handle. One 10 ft stick per kit. | $4–6 |
| 2 | ¾" PVC cross (4-way) fittings | Reflector and driven element positions. | $1.50–3.00 each |
| 2 | ¾" PVC T fittings | Director and handle grip. | $0.75–1.50 each |
| 1 | RG-58/U coax pigtail, 6 ft, BNC-male | 2m feed. Pre-built by instructor. | $4–7 |
| 1 | 14 AWG solid copper wire, 6" piece | 2m hairpin match. | <$0.50 |

### 70cm Section (sub-boom)

| Qty | Item | Notes | Est. Cost |
|-----|------|-------|-----------|
| 1 | 12" length of ½" Schedule 40 PVC pipe | 70cm sub-boom. Yields all three sub-boom tubes from one cut. | $1–2 |
| 2 | ½" PVC cross (4-way) fittings | Reflector and driven element positions. | $0.75–1.50 each |
| 1 | ½" PVC T fitting | Director position. | $0.50–1.00 |
| 1 | RG-58/U coax pigtail, 3–6 ft, BNC-male | 70cm feed. Pre-built by instructor. | $3–6 |
| 1 | 18–20 AWG solid copper wire, 2" piece | 70cm hairpin match. Pre-cut. | <$0.25 |

### Shared Hardware (both sections)

| Qty | Item | Notes | Est. Cost |
|-----|------|-------|-----------|
| 12 | Stainless steel hose clamps, ½"–1¼" range | 6 for 2m section, 6 for 70cm section. Worm-drive only, not spring-type. | ~$10–14/20-pack |
| 4 | Cable ties | Coax routing + sub-boom attachment. | <$0.25 |
| — | Rosin-core solder, 60/40 | Shared supply | — |
| — | Fine sandpaper, 80–120 grit | One piece per kit | <$0.25 |
| — | Electrical tape | Shared supply | — |

**Per-kit total (bulk purchasing): ~$46–56**

### Sourcing Notes

- **½" PVC pipe:** Buy a single 10 ft stick and cut 12" sections.
  The same hardware store as for the ¾" pipe. ½" Schedule 40 PVC
  is labeled "½ in" on the shelf; verify you are buying Schedule
  40, not CPVC (which is beige/yellow and slightly different OD).
- **½" PVC fittings:** Check the plumbing section carefully —
  ½" cross fittings may be less common than ¾". Look in the DWV
  (drain) or irrigation section. Alternatively order online.
- **Hose clamps:** Buy a 20-pack of ½"–1¼" worm-drive clamps and
  split 12 per kit. This size fits both ¾" and ½" PVC fittings.
- **18–20 AWG wire:** A few inches of stranded or solid hookup
  wire stripped of insulation, or stripped telephone wire, works.
  Pre-cut by instructor.
- **Second coax pigtail:** Build or buy the same way as the 2m
  pigtail. A shorter length (3 ft) saves weight and material.
  Both pigtails can be bundled with a cable tie along the boom.

---

## 4. Tools Required

*(Same as for the 2m Yagi — see `build-instructions-2m-yagi.md`
Section 3 for the complete list.)*

Additional items for the 70cm sub-boom:
- **PVC cutter or fine-tooth saw** (same tool — used for shorter
  ½" pipe cuts)
- **Needle-nose pliers** (smaller bend radius needed for 70cm
  hairpin)
- Smaller screwdriver or ¼" nut driver for the smaller hose
  clamp screws if your clamp style differs

No additional major tools are needed beyond the 2m build.

---

## 5. Step-by-Step Build Instructions

Build the two sections in order: **2m section first** (Steps 1–10),
then the **70cm sub-boom section** (Steps 11–18), then combine
them (Steps 19–20).

> **Before you start:** Lay out all parts for both bands and
> verify against the BOM. Read all steps through before picking
> up any tools.

---

### Phase 1 — Build the 2m Section (Steps 1–10)

Follow steps 1 through 10 of `build-instructions-2m-yagi.md`
exactly. The 2m section of this dual-band antenna is identical to
the standalone 2m Yagi. Build it first and set it aside while you
build the 70cm sub-boom.

Key dimensions to keep handy:

| Element | Length |
|---|---|
| Reflector | 41⅜" |
| Driven element (each half) | 17¾", gap = 1" |
| Director | 35⅛" |
| Boom-A tube (reflector cross ↔ driven cross) | 11¼" |
| Boom-B tube (driven cross ↔ director T) | 6⅞" |

**When the 2m section is complete, do not fully tighten the
sub-boom attachment point yet — leave the 2m driven element cross
fitting accessible for Step 20.**

---

### Phase 2 — Build the 70cm Sub-Boom Section (Steps 11–18)

---

#### Step 11 — Cut the ½" PVC Sub-Boom Pieces

**Time: 10 minutes**

Cut the 12" ½" PVC piece into these three sections:

| Label | Length | Purpose |
|---|---|---|
| **Sub-Boom-A** | 2⅞" (2.875") | Reflector cross ↔ driven element cross |
| **Sub-Boom-B** | 1½" (1.5") | Driven element cross ↔ director T |
| *(discard remainder)* | | |

> **These are short cuts.** Measure twice before cutting. A
> ratchet PVC cutter makes cleaner short cuts than a saw. Deburr
> cut ends.

---

#### Step 12 — Dry-Fit the 70cm Sub-Boom Frame

**Time: 5 minutes**

Assemble the sub-boom dry (no glue — friction fit only).

**Sub-boom layout, front to back:**

```
[Director T] ←Sub-B→ [Driven Cross] ←Sub-A→ [Reflector Cross]
    (front)               (center)               (rear)
```

1. Push Sub-Boom-B into the director T fitting.
2. Push the other end of Sub-Boom-B into the driven element cross
   fitting.
3. Push Sub-Boom-A into the opposite side of the driven element
   cross.
4. Push the other end of Sub-Boom-A into the reflector cross
   fitting.

Verify spacing:
- Director T to driven element cross: **~2⅝"** center-to-center
- Driven element cross to reflector cross: **~4⅛"** center-to-center

---

#### Step 13 — Cut the 70cm Tape Measure Elements

**Time: 15 minutes**

Use the **remaining** tape measure blade from the 2m cuts (there
is at least 15 ft of blade remaining after the 2m elements).

Cut the following pieces:

| Element | Length | Quantity |
|---|---|---|
| Reflector | **13¾"** (13.75") | 1 piece |
| Driven element half (×2) | **5⅞"** (5.875") each | 2 pieces |
| Director | **11⅝"** (11.625") | 1 piece |

**Total tape measure consumed for 70cm: 37⅛" (~3 ft 1 in) —
well within the remaining blade.**

> **Cutting safety:** Same precautions as for 2m elements — sharp
> edges, wear gloves, deburr immediately.

> **These elements are short.** Mark each cut line carefully with
> a permanent marker. Keep the 70cm pieces separate from the 2m
> pieces — label them with tape.

---

#### Step 14 — Prepare the 70cm Driven Element Tips

**Time: 10 minutes**

Same technique as for the 2m driven element (Step 4 of the 2m
instructions), but on a smaller scale.

1. Sand the inner corner of each driven element half (5⅞" piece)
   at the tip. Sand an area ~¼" × ¼" — bare, shiny steel.

2. Apply flux. Tin with the soldering iron. The 70cm blade tips
   are smaller heat sinks than the 2m tips — they tin faster.
   Watch for the solder flowing onto the steel; it only takes
   2–3 seconds.

3. Repeat for the second half. Both tinned tips will look silver
   and smooth.

---

#### Step 15 — Mount the 70cm Reflector and Director Elements

**Time: 8 minutes**

Same technique as for the 2m section (Step 5 of the 2m
instructions).

1. Slide the reflector (13¾") through the **reflector cross**
   fitting of the sub-boom. Center it. Secure with two hose
   clamps, one on each side.

2. Slide the director (11⅝") through the **director T** fitting.
   Center it. Secure with one hose clamp on each side.

> **The ½" PVC fittings are smaller.** The hose clamps grip the
> same way but the fitting body is narrower (~0.84" OD vs ~1.05"
> OD for ¾"). The same ½"–1¼" hose clamp size still fits.

---

#### Step 16 — Mount the 70cm Driven Element Halves

**Time: 8 minutes**

Same technique as for the 2m section (Step 6 of the 2m
instructions), but set the gap to **⅜"** instead of 1".

1. Slide the first driven element half (5⅞") into one arm of the
   **driven element cross** fitting, tinned tip facing inward.

2. Slide the second half into the opposite arm, tinned tip also
   facing inward.

3. Position both halves so:
   - Each blade extends **5⅞"** from the fitting center to its
     tip
   - The gap between the two inner tips is **⅜"**
   - Both blades are co-planar

4. Secure each half with a hose clamp.

> **The ⅜" gap is small.** Use a ⅜" spacer (a piece of scrap
> PVC, a folded piece of cardboard, or just your thumbnail with
> a ruler check) to set the gap precisely before tightening the
> clamps.

---

#### Step 17 — Fabricate and Attach the 70cm Hairpin Match

**Time: 10 minutes**

Same principle as the 2m hairpin, scaled down.

1. Take the 2" piece of 18–20 AWG solid copper wire. Strip ¼"
   of insulation from each end (if insulated).

2. Using needle-nose pliers, bend the wire into a U-shape with
   the two parallel legs **~¼"** apart at the tips.

   ```
       ┌──────┐   ← ~1" of wire across the top
       │      │
       │  ¼"  │   ← gap between legs
       ↓      ↓
   (solders)  (solders)
   left half  right half
   ```

3. Lay the U-shape across the ⅜" gap between the driven element
   halves, with each leg resting on one of the tinned corners.
   The hairpin legs will span the gap and extend slightly beyond
   each element tip.

4. Solder each leg to its driven element tip.

> **Scale matters:** Everything here is proportionally smaller
> than the 2m hairpin. Use fine-tipped solder and a moderately
> hot iron (not the highest setting). Work quickly — small thin
> metal heats fast and cools fast.

> **Do NOT short the two 70cm driven element halves** with solder
> across the gap. The hairpin wire is the only bridge.

---

#### Step 18 — Prepare and Solder the 70cm Coax

**Time: 10 minutes**

Prepare the bare end of the 70cm coax pigtail the same way as
for the 2m section (Step 8 of the 2m instructions: strip outer
jacket 1", fold back braid, expose center conductor, flux and
tin both).

Solder the 70cm coax to the driven element:
- Center conductor → one tinned tip/hairpin leg
- Braid → the OTHER tinned tip/hairpin leg
- Verify: no center-to-braid short; hairpin still present

Wrap the connection with two layers of electrical tape.

---

### Phase 3 — Combine Sub-Boom and Main Boom (Steps 19–20)

---

#### Step 19 — Attach the Sub-Boom to the Main Boom

**Time: 10 minutes**

1. Hold the ½" PVC sub-boom alongside the ¾" PVC main boom,
   **parallel and ~1" to one side**. The sub-boom's elements
   should be in the same horizontal plane as the main boom's
   elements (not offset vertically).

2. Position the sub-boom so its **driven element cross** aligns
   with (or is within 1–2" of) the main boom's **driven element
   cross**. This co-locates both feed points for easy coax
   management.

3. Secure the sub-boom to the main boom with 3–4 cable ties
   spaced along the sub-boom length. Use zip ties rather than
   tape — they won't slip.

   ```
   Side view (both booms from above):

   ─────────────────────────────── ½" sub-boom
   ═══════════════════════════════ ¾" main boom
         ↑↑                 ↑↑
      zip ties (2 each end and middle)
   ```

4. Verify: sub-boom is parallel to the main boom (not angled),
   and all elements on both booms remain in the same horizontal
   plane.

> **Clearance check:** After attaching, fold the antenna elements
> flat (tape measure blades fold toward the boom). Make sure the
> 70cm elements do not catch on the 2m fittings or elements when
> folded and unfolded.

---

#### Step 20 — Route Coax and Final Assembly

**Time: 10 minutes**

1. Both coax pigtails (2m and 70cm) now exit near the driven
   element position. Bundle them together with a cable tie and
   route them along the main boom to the handle.

2. Secure the coax bundle to the boom with 2 additional cable
   ties along the handle length.

3. Label the BNC ends: "2m" and "70cm" with masking tape and
   permanent marker. **These labels are critical** — in the field
   you must connect the right coax to the right HT VFO.

4. Final dimensional check — both bands:

**2m section:**

| Check | Nominal | Accept range |
|---|---|---|
| Reflector length | 41⅜" | 41"–41¾" |
| Each driven element half | 17¾" | 17½"–18" |
| Driven element gap | 1" | ¾"–1¼" |
| Director length | 35⅛" | 34¾"–35½" |
| Reflector–Driven spacing (C-C) | ~12½" | 12"–13" |
| Driven–Director spacing (C-C) | ~8" | 7½"–8½" |

**70cm section:**

| Check | Nominal | Accept range |
|---|---|---|
| Reflector length | 13¾" | 13½"–14" |
| Each driven element half | 5⅞" | 5¾"–6" |
| Driven element gap | ⅜" | 5/16"–½" |
| Director length | 11⅝" | 11¼"–12" |
| Reflector–Driven spacing (C-C) | ~4⅛" | 3¾"–4½" |
| Driven–Director spacing (C-C) | ~2⅝" | 2¼"–3" |

**Congratulations — the dual-band Yagi is complete. Proceed to
testing (Section 7).**

---

## 6. Common Mistakes and Tips

| Mistake | Effect | Prevention |
|---|---|---|
| Sub-boom not parallel to main boom | Elements point at different angles; messy pattern | Check parallelism by eye before cinching zip ties |
| 70cm and 2m coax pigtails not labeled | Connect the wrong HT to the wrong band in the field | Label clearly during Step 20; label both ends of each pigtail |
| 70cm driven element gap too wide or too narrow | Impedance mismatch; reduced sensitivity | Use a spacer block to set ⅜" gap before clamping |
| 70cm elements not in same plane as 2m elements | Crooked mixed polarization | Verify both element sets are horizontal with the booms held level |
| ½" PVC cement used | Can't adjust later | Dry-fit only; the friction fit is sufficient |
| Sub-boom zip ties placed over ½" fitting body | Fittings can't seat properly | Place zip ties on the bare pipe, not on the fitting body |
| 70cm hairpin shorted to 2m element or fitting | Cross-band interference, possible receive degradation | Route 70cm coax and hairpin clear of 2m elements |
| Cutting 70cm elements at 2m element lengths | Antenna tuned to wrong frequency | Keep element sets labeled and physically separated during the build |

---

## 7. Testing and Verification

### 7.1 Continuity Tests (5 minutes per band)

Perform the same continuity checks described in Section 6 of
`build-instructions-2m-yagi.md` for **each band independently**:

**For each coax pigtail:**
- BNC center → BNC shell: **open** (no short)
- BNC center → one driven element half: **low resistance** (< 2 Ω)
- BNC shell → other driven element half: **low resistance** (< 2 Ω)

**Also verify:**
- 2m BNC center → 70cm BNC center: **open** (the two feed
  systems must be independent — no connection between them)
- 2m BNC shell → 70cm BNC shell: may show continuity through the
  shared boom; this is acceptable since both shields are RF
  ground through the metal hose clamps and tape measure blades

---

### 7.2 Functional RF Tests

#### Test on 2m

Follow Section 6.2 of `build-instructions-2m-yagi.md`. Connect
the **2m coax pigtail** to a 2m HT. Verify directional gain and
front-to-back null.

#### Test on 70cm

1. Connect the **70cm coax pigtail** to a 70cm-capable HT.
2. Identify a 70cm signal source: a 440 MHz repeater, another
   HT transmitting briefly, or a 70cm beacon.
3. Point the antenna's director (front T fitting of the sub-boom
   and main boom) at the signal source. The 70cm S-meter should
   read higher than the HT's rubber duck.
4. Rotate 180°. The S-meter should drop — confirming the rear
   null on the 70cm section.

> **70cm performance note:** The 70cm section is smaller and the
> hairpin match is less precise at this scale. Expect 10–20 dB
> front-to-back ratio — slightly less than the 2m section in most
> field builds. This is adequate for fox hunting.

#### Test for Band Isolation

1. Hold the antenna stationary.
2. Connect only the 2m pigtail to a 2m HT, leave the 70cm pigtail
   disconnected (or terminated).
3. The antenna should behave as a normal 2m Yagi — the 70cm
   section does not noticeably degrade 2m performance because the
   70cm elements are not resonant at 146 MHz.
4. Swap connections: connect only 70cm pigtail to a 70cm HT,
   leave 2m pigtail disconnected. The antenna should behave as a
   70cm Yagi.

---

### 7.3 Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| 2m section: omni-directional | Coax center shorted to braid at 2m driven element | See `build-instructions-2m-yagi.md` troubleshooting |
| 70cm section: omni-directional | Same issue on 70cm driven element | Inspect 70cm coax solder joints; check with ohmmeter |
| No 70cm receive at all | 70cm coax center disconnected | Probe 70cm BNC center → 70cm driven element |
| Antenna looks crooked | Sub-boom skewed relative to main boom | Re-position sub-boom; re-cinch zip ties |
| 2m performance degrades after adding 70cm section | 70cm elements coupling into 2m elements | Verify sub-boom is parallel (not at an angle); re-route 70cm coax away from 2m driven element |

---

## 8. References

| Source | Description |
|---|---|
| jpole-antenna.com, 2017 | 2m tape measure Yagi build reference: [https://www.jpole-antenna.com/2017/02/07/build-it-2-meter-tape-measure-yagi-beam-antenna/](https://www.jpole-antenna.com/2017/02/07/build-it-2-meter-tape-measure-yagi-beam-antenna/) |
| WB2HOL (Joel Hartman) | Original designer of the tape measure Yagi. 70cm dimensions scale directly from his 2m design by frequency ratio. |
| ARDF.net | ARDF resources, dual-band fox hunting: [https://www.ardf.net](https://www.ardf.net) |
| Homingin.com | ARDF equipment and dual-band hunting techniques: [https://www.homingin.com](https://www.homingin.com) |
| M&K ARC Field Day 2026 — 2m Yagi Instructions | `docs/field-day-2026/build-instructions-2m-yagi.md` |
| M&K ARC Field Day 2026 — Build Session Syllabus | `docs/field-day-2026/build-event-syllabus.md` |

---

### Quick Reference Card

*Print this section and tape it to the workstation.*

**2m Element Lengths (main boom — ¾" PVC)**

| Element | Length |
|---|---|
| Reflector | **41⅜"** |
| Driven element (each half) | **17¾"**, gap = **1"** |
| Director | **35⅛"** |

**70cm Element Lengths (sub-boom — ½" PVC)**

| Element | Length |
|---|---|
| Reflector | **13¾"** |
| Driven element (each half) | **5⅞"**, gap = **⅜"** |
| Director | **11⅝"** |

**Boom Spacing — 2m (center-to-center)**

| Span | Distance | PVC tube length |
|---|---|---|
| Director T ↔ Driven cross | ~8" | Boom-B = **6⅞"** |
| Driven cross ↔ Reflector cross | ~12½" | Boom-A = **11¼"** |

**Boom Spacing — 70cm (center-to-center)**

| Span | Distance | PVC tube length |
|---|---|---|
| Director T ↔ Driven cross | ~2⅝" | Sub-Boom-B = **1½"** |
| Driven cross ↔ Reflector cross | ~4⅛" | Sub-Boom-A = **2⅞"** |

---

*Build instructions version: 1.0*
*Instructor: Tom KE4HET / Mike & Key ARC (K7LED)*
*Last updated: June 2026 (pre-event draft)*

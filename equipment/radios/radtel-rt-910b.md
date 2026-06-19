# Radtel RT-910B — Equipment Notes

**Role:** Entry-level hunting radio (hound-side receiver/transceiver)
**Status:** Recommended for new participants

- **Vendor (official):** https://www.radtels.com/products/radtel-rt-910b-bluetooth-app-programming-multi-band-6-meter-walkie-talkie-45-59mhz-tx-rx-with-960-channels-am-fm-two-way-radio-air-band-type-c-spectrum?variant=44565703000272
- **Amazon:** https://a.co/d/0ggbHfOh
- **Street price:** ~$30 (Amazon)

---

## Why This Radio for Fox Hunting

| Feature | Value |
|---|---|
| Price | ~$30 — lowest barrier to entry |
| S-meter | Large, real-time RSSI bar graph on color LCD |
| TX lockout | Prevent inadvertent or unauthorized transmission |
| Frequency coverage | 144–148 MHz (2 m) and 420–450 MHz (70 cm) TX/RX |
| Antenna connector | SMA — **BNC-to-SMA adapter required** for club Yagi builds (Yagis terminate in BNC) |
| Programming | Bluetooth app — no programming cable required |
| Charging | USB Type-C |

The combination of a **large S-meter display** and **TX lockout** makes
this radio especially well suited for fox hunting: the S-meter gives
hounds a quick visual bearing aid, and TX lockout lets instructors loan
the radio to newcomers without risk of accidental transmissions on the
fox frequency.

> **Adapter required:** Club tape-measure Yagi builds terminate in a
> BNC connector. The RT-910B has an SMA connector. A **BNC-female to
> SMA-male adapter** is needed to connect the two. Budget ~$5–10 for
> an adapter; include one per loaner radio kit.

---

## Specifications

| Parameter | Value |
|---|---|
| TX power | 5 W |
| TX frequency | 144–148 MHz / 420–450 MHz |
| Channels | 960 |
| Battery voltage | 7.4 V (Li-Ion, included) |
| Charging | USB Type-C |
| Impedance | 50 Ω |
| Connectivity | Bluetooth (app programming) |
| Air band | RX only (no TX on aviation frequencies) |
| NOAA weather | Yes |
| VOX | Yes |
| Flashlight | Yes |
| Water resistance | Not rated |
| Talking range (spec) | Up to 6 km (line of sight) |

---

## S-Meter Notes

The RT-910B includes a **segmented RSSI bar graph** on the color LCD
that updates in real time as signal strength changes.

**What it does well for fox hunting:**
- Shows relative signal strength changes as you sweep with the Yagi —
  stronger signal → more bars → better bearing.
- Gives new hounds a visual cue to complement what they hear.
- Works alongside the switched step attenuator for close-in hunting.

**Known limitations:**
- Not a calibrated instrument — readings are relative, not absolute.
  Does not map to the traditional RST / S-unit scale.
- Not perfectly linear across the full range.
- Early firmware caused erratic behavior when the Monitor (MONI)
  function was active; **update firmware before use** (Radtel has
  addressed this in later releases).
- Use it as a complement to your ears, not a replacement.

---

## TX Lockout

The RT-910B supports a transmit lockout mode that disables the PTT
button. This is useful for:

- **Loaner radios at demonstrations** — prevents public visitors from
  keying up on the fox frequency.
- **Training new hounds** — lets them focus on direction finding without
  accidentally transmitting.

Confirm the lockout procedure in the current firmware/manual before
lending the radio.

---

## Programming

Use the **Radtel BT** app (iOS / Android) over Bluetooth — no
programming cable required. Set the fox hunt frequency (e.g.,
147.42 MHz) and disable TX on that channel if using TX lockout.

---

## Recommendation

> ⚠️ **The club has not yet had hands-on experience with this radio.**
> This recommendation is based on published specifications, vendor
> listings, and community reviews only. It should be treated as
> **conditional** until a unit is purchased, tested on the fox hunt
> frequency, and the TX lockout and S-meter behavior are verified
> in the field.

> **Conditionally recommended as an entry-level fox hunting radio**
> for new participants who do not yet own a 2 m HT.
>
> At ~$30 with a large S-meter, SMA connector, TX lockout, and USB-C
> charging, it provides everything needed to participate in club
> hunts at minimal cost. Hounds can use it with the club's tape-measure
> Yagi build directly out of the box.
>
> **Before recommending to club members:**
> - [ ] Purchase and bench-test a unit
> - [ ] Confirm 2 m RX and TX on 144–148 MHz
> - [ ] Source BNC-female to SMA-male adapters (~$5–10 each)
> - [ ] Verify TX lockout disables PTT reliably
> - [ ] Confirm S-meter responds visibly when sweeping with the Yagi
> - [ ] Update firmware and retest if S-meter behaves erratically
> - [ ] Remove the ⚠️ notice above once hands-on testing is complete

---

## References

- Official product page:
  https://www.radtels.com/products/radtel-rt-910b-bluetooth-app-programming-multi-band-6-meter-walkie-talkie-45-59mhz-tx-rx-with-960-channels-am-fm-two-way-radio-air-band-type-c-spectrum?variant=44565703000272
- Amazon listing: https://a.co/d/0ggbHfOh
- Related equipment: `equipment/radios/` (this directory)
- Fox frequency reference: `foxes/MF-15/current-config.yaml`,
  `foxes/MF-PC/current-config.yaml`

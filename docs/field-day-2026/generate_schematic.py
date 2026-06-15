"""
Generate a schematic diagram for the 3-section switched step attenuator
used in the M&K ARDF Field Day 2026 build event.

T-pad attenuator sections (20 dB first = best impedance match):
  20 dB: R1=R3=39Ω, R2=10Ω
  10 dB: R1=R3=27Ω, R2=36Ω
  6 dB:  R1=R3=18Ω, R2=68Ω

Each section uses a DPDT ON-ON toggle switch.
  - Position A (bypass):    both poles route signal straight through.
                            T-pad resistors float off the signal path.
  - Position B (attenuate): both poles route signal through T-pad.
                            R2 shunt permanently wired mid-node to GND.

DPDT shown as two ganged SPDT switches per section:
  SW_in  = Pole 1 (input side)
  SW_out = Pole 2 (output side)
  Ganging bar drawn between pivot points.

Actual attenuation with E12/E24 resistors:
  20 dB → 19.56 dB  (39/10/39 Ω)
  10 dB → 10.20 dB  (27/36/27 Ω)
   6 dB →  6.36 dB  (18/68/18 Ω)

Usage:
    /tmp/schemdraw-env/bin/python3 generate_schematic.py
Output:
    docs/field-day-2026/attenuator-schematic.svg
    docs/field-day-2026/attenuator-schematic.png
"""

import schemdraw
import schemdraw.elements as elm
import matplotlib
matplotlib.use('Agg')
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

# Section order: highest attenuation first (best impedance practice)
SECTIONS = [
    {"label": "20 dB", "R1": "39Ω", "R2": "10Ω",  "R3": "39Ω", "sw": "SW1"},
    {"label": "10 dB", "R1": "27Ω", "R2": "36Ω", "R3": "27Ω", "sw": "SW2"},
    {"label": "6 dB",  "R1": "18Ω", "R2": "68Ω", "R3": "18Ω", "sw": "SW3"},
]

OUT_SVG = "docs/field-day-2026/attenuator-schematic.svg"
OUT_PNG = "docs/field-day-2026/attenuator-schematic.png"

# Layout constants (in schemdraw units)
GAP        = 1.2   # wire gap between sections
TPAD_DROP  = 2.8   # how far the T-pad hangs below the signal rail
BYPASS_UP  = 2.0   # how far the bypass path rises above the signal rail
GANG_UP    = -0.5   # ganging bar BELOW signal rail (less visual clutter)


def draw_attenuator():
    d = schemdraw.Drawing(fontsize=10)
    d.config(inches_per_unit=0.48)

    # BNC IN
    d.add(elm.Dot(open=True).label("BNC\nIN", loc='left'))
    d.add(elm.Line().right(GAP))

    # Track section entry/exit points for ganging bars
    section_data = []

    for i, sec in enumerate(SECTIONS):
        x_in, y_sig = d.here

        # ── Pole 1 input SPDT ─────────────────────────────────────────
        # common = x_in (signal rail)
        # bypass throw goes UP  → BYPASS_UP above rail
        # atten  throw goes DOWN → into T-pad
        sw_in = d.add(elm.SwitchSpdt().right().flip())
        # After flip: c is BELOW (→ T-pad), end is inline right (→ bypass)
        p1_bypass = sw_in.absanchors['end']   # inline throw (bypass)
        p1_atten  = sw_in.absanchors['c']     # flipped-down throw (attenuate)
        p1_pivot  = sw_in.absanchors['a']     # pivot point (for ganging bar)

        x_sw1_end = p1_bypass[0]
        y_bypass  = y_sig                     # bypass runs along signal rail level
        y_tpad    = y_sig - TPAD_DROP         # T-pad below signal rail

        # ── T-pad section ──────────────────────────────────────────────
        # Drop from pole 1 attenuate throw to T-pad level
        d.add(elm.Line().at(p1_atten).down(abs(p1_atten[1] - y_tpad))
              .color('gray'))

        x_r1_start = p1_atten[0]
        d.add(elm.Resistor().at((x_r1_start, y_tpad)).right()
              .label(f"R1={sec['R1']}", loc='top')
              .color('black'))

        x_mid = d.here[0]
        d.add(elm.Dot())

        d.add(elm.Resistor().right()
              .label(f"R3={sec['R3']}", loc='top')
              .color('black'))

        x_r3_end = d.here[0]

        # Shunt R2: mid-node to ground (permanently wired)
        d.add(elm.Line().at((x_mid, y_tpad)).down(0.4))
        d.add(elm.Resistor().down()
              .label(f"R2={sec['R2']}", loc='right')
              .color('black'))
        d.add(elm.Ground())

        # ── Pole 2 output SPDT ────────────────────────────────────────
        # Draw reversed SPDT for output pole:
        # common = signal out (right), atten throw from T-pad (below)
        # Use SwitchSpdt going LEFT so 'start' is on right
        sw_out = d.add(elm.SwitchSpdt().right().flip().reverse()
                       .at((x_r3_end + 3.0, y_sig)))
        p2_bypass = sw_out.absanchors['end']   # inline throw (bypass)
        p2_atten  = sw_out.absanchors['c']     # flipped-down (attenuate)
        p2_pivot  = sw_out.absanchors['a']
        x_sw2_com = sw_out.absanchors['start'][0]

        # Connect T-pad R3 output up to pole 2 attenuate throw
        d.add(elm.Line().at((x_r3_end, y_tpad))
              .right(p2_atten[0] - x_r3_end).color('gray'))
        d.add(elm.Line().at((p2_atten[0], y_tpad))
              .up(abs(p2_atten[1] - y_tpad)).color('gray'))

        # ── Bypass path (above or inline) ─────────────────────────────
        # Connect p1_bypass (inline) across to p2_bypass (inline)
        # Both are at y_sig level
        bypass_y = y_sig + BYPASS_UP
        d.add(elm.Line().at(p1_bypass).up(BYPASS_UP)
              .color('steelblue'))
        d.add(elm.Line().at((p1_bypass[0], p1_bypass[1] + BYPASS_UP))
              .right(p2_bypass[0] - p1_bypass[0])
              .label(f"{sec['sw']} bypass\n({sec['label']})", loc='top')
              .color('steelblue'))
        d.add(elm.Line().at(p2_bypass).up(BYPASS_UP).color('steelblue'))

        # ── Ganging bar between pivot points (below signal rail) ─────
        gang_y = y_sig + GANG_UP  # GANG_UP is negative → below rail
        d.add(elm.Line().at((p1_pivot[0], y_sig))
              .down(abs(GANG_UP)).linestyle('--').color('dimgray'))
        d.add(elm.Line().at((p1_pivot[0], gang_y))
              .right(p2_pivot[0] - p1_pivot[0])
              .linestyle('--').color('dimgray')
              .label('DPDT (ganged)', loc='bot', ofst=0.05))
        d.add(elm.Line().at((p2_pivot[0], y_sig))
              .down(abs(GANG_UP)).linestyle('--').color('dimgray'))

        section_data.append((x_in, x_sw2_com, y_sig))

        # Continue signal rail to next section gap
        d.here = (x_sw2_com, y_sig)
        if i < len(SECTIONS) - 1:
            d.add(elm.Line().right(GAP))

    # BNC OUT — add extra gap so label isn't clipped
    x_last = section_data[-1][1]
    y_last = section_data[-1][2]
    d.add(elm.Line().at((x_last, y_last)).right(GAP * 1.5))
    d.add(elm.Dot(open=True).label("BNC\nOUT", loc='right'))

    # ── Legend / title ────────────────────────────────────────────────
    d.draw()
    ax = d.fig.axes[0] if hasattr(d.fig, 'axes') else None

    d.save(OUT_SVG)
    d.save(OUT_PNG, dpi=150)
    print(f"Saved: {OUT_SVG}")
    print(f"Saved: {OUT_PNG}")


if __name__ == "__main__":
    draw_attenuator()

"""
Generate a schematic diagram for the 3-section switched step attenuator
used in the M&K ARDF Field Day 2026 build event.

T-pad attenuator sections:
  6 dB:  R1=R3=18Ω, R2=68Ω
  10 dB: R1=R3=27Ω, R2=36Ω
  20 dB: R1=R3=39Ω, R2=10Ω

Each section is bypassed by a DPDT ON-ON toggle switch.

Usage:
    python3 generate_schematic.py
Output:
    docs/field-day-2026/attenuator-schematic.svg
    docs/field-day-2026/attenuator-schematic.png
"""

import schemdraw
import schemdraw.elements as elm
import matplotlib
matplotlib.use('Agg')

SECTIONS = [
    {"label": "6 dB",  "R1": "18Ω", "R2": "68Ω", "R3": "18Ω"},
    {"label": "10 dB", "R1": "27Ω", "R2": "36Ω", "R3": "27Ω"},
    {"label": "20 dB", "R1": "39Ω", "R2": "10Ω",  "R3": "39Ω"},
]

OUT_SVG = "docs/field-day-2026/attenuator-schematic.svg"
OUT_PNG = "docs/field-day-2026/attenuator-schematic.png"

GAP       = 1.5   # wire between sections
SHUNT_D   = 2.5   # depth of shunt leg below rail
BYPASS_UP = 1.8   # height of bypass arch ABOVE rail


def draw_attenuator():
    d = schemdraw.Drawing(fontsize=11)
    d.config(inches_per_unit=0.45)

    # Input connector
    d.add(elm.Dot(open=True).label("BNC IN", loc='left'))
    d.add(elm.Line().right(GAP))

    sections_x = []  # store (x_in, x_mid, x_out, y_rail) per section

    for i, sec in enumerate(SECTIONS):
        x_in, y_rail = d.here
        d.add(elm.Dot())

        # R1 — series resistor in
        d.add(elm.Resistor().right()
              .label(sec['R1'], loc='top')
              .label('R1', loc='bot'))

        x_mid = d.here[0]
        d.add(elm.Dot())

        # R3 — series resistor out
        d.add(elm.Resistor().right()
              .label(sec['R3'], loc='top')
              .label('R3', loc='bot'))

        x_out = d.here[0]
        d.add(elm.Dot())
        sections_x.append((x_in, x_mid, x_out, y_rail))

        # Shunt: R2 from mid-node to ground
        d.add(elm.Line().at((x_mid, y_rail)).down(0.5))
        d.add(elm.Resistor().down()
              .label(f"R2 = {sec['R2']}", loc='right'))
        d.add(elm.Ground())

        # Bypass arch ABOVE the signal rail
        bypass_y = y_rail + BYPASS_UP
        sw_len = x_out - x_in
        d.add(elm.Line().at((x_in, y_rail))
              .up(BYPASS_UP).color('steelblue'))
        d.add(elm.Switch().at((x_in, bypass_y)).right(sw_len)
              .color('steelblue')
              .label(f"SW{i+1}  DPDT  ({sec['label']})", loc='top'))
        d.add(elm.Line().at((x_out, bypass_y))
              .down(BYPASS_UP).color('steelblue'))

        # Gap wire before next section
        if i < len(SECTIONS) - 1:
            d.add(elm.Line().at((x_out, y_rail)).right(GAP))

    # Output connector
    x_last_out = sections_x[-1][2]
    y_rail = sections_x[-1][3]
    d.add(elm.Line().at((x_last_out, y_rail)).right(GAP))
    d.add(elm.Dot(open=True).label("BNC OUT", loc='right'))

    d.draw()  # force figure creation

    d.save(OUT_SVG)
    d.save(OUT_PNG, dpi=150)
    print(f"Saved: {OUT_SVG}")
    print(f"Saved: {OUT_PNG}")


if __name__ == "__main__":
    draw_attenuator()

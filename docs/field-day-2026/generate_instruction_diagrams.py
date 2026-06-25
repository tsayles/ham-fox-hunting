"""Generate pyplot diagrams to replace ASCII drawings in build docs.

Usage:
  python3 docs/field-day-2026/generate_instruction_diagrams.py

Outputs (SVG + PNG):
  - attenuator-switch-pinout
  - attenuator-signal-chain
  - attenuator-enclosure-layout
  - attenuator-resistor-tree
  - attenuator-label-strip
  - attenuator-switch-modes
  - yagi-2m-boom-layout
  - yagi-hairpin-2m
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

OUTPUT_DIR = Path(__file__).resolve().parent
PNG_DPI = 150


def _save(fig: plt.Figure, base_name: str) -> None:
  svg_path = OUTPUT_DIR / f"{base_name}.svg"
  png_path = OUTPUT_DIR / f"{base_name}.png"
  fig.savefig(svg_path, bbox_inches="tight")
  fig.savefig(png_path, dpi=PNG_DPI, bbox_inches="tight")
  plt.close(fig)
  print(f"Wrote {svg_path}")
  print(f"Wrote {png_path}")


def _make_canvas(width: float, height: float) -> tuple[plt.Figure, plt.Axes]:
  fig, ax = plt.subplots(figsize=(width, height))
  ax.set_axis_off()
  return fig, ax


def _draw_box(ax: plt.Axes, x: float, y: float, w: float, h: float, text: str) -> None:
  ax.add_patch(Rectangle((x, y), w, h, fill=False, linewidth=1.5))
  ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=10)


def _draw_arrow(
  ax: plt.Axes,
  start: tuple[float, float],
  end: tuple[float, float],
  text: str | None = None,
) -> None:
  arrow = FancyArrowPatch(start, end, arrowstyle="->", mutation_scale=12)
  ax.add_patch(arrow)
  if text:
    mid_x = (start[0] + end[0]) / 2
    mid_y = (start[1] + end[1]) / 2
    ax.text(mid_x, mid_y + 0.12, text, ha="center", va="bottom", fontsize=9)


def draw_attenuator_switch_pinout() -> None:
  fig, ax = _make_canvas(6.5, 2.8)
  ax.set_xlim(0, 8)
  ax.set_ylim(0, 4)

  pin_positions = {
    1: (1.5, 2.7),
    2: (3.0, 2.7),
    3: (4.5, 2.7),
    4: (1.5, 1.3),
    5: (3.0, 1.3),
    6: (4.5, 1.3),
  }
  for pin, (x, y) in pin_positions.items():
    _draw_box(ax, x - 0.35, y - 0.3, 0.7, 0.6, str(pin))
  ax.text(5.3, 2.7, "Pole 1\n(1-2 or 2-3)", va="center", fontsize=9)
  ax.text(5.3, 1.3, "Pole 2\n(4-5 or 5-6)", va="center", fontsize=9)
  ax.text(3.0, 0.45, "Pins 2 and 5 are the common pins.", ha="center", fontsize=10)
  ax.set_title("DPDT ON-ON Mini Toggle Switch Pin Numbering", fontsize=12)
  _save(fig, "attenuator-switch-pinout")


def draw_attenuator_signal_chain() -> None:
  fig, ax = _make_canvas(9, 2.2)
  ax.set_xlim(0, 11)
  ax.set_ylim(0, 2)
  _draw_box(ax, 0.4, 0.6, 1.3, 0.7, "BNC IN")
  _draw_box(ax, 2.3, 0.6, 2.1, 0.7, "Section A\n6 dB")
  _draw_box(ax, 5.0, 0.6, 2.1, 0.7, "Section B\n10 dB")
  _draw_box(ax, 7.7, 0.6, 2.1, 0.7, "Section C\n20 dB")
  _draw_box(ax, 10.3, 0.6, 0.6, 0.7, "OUT")
  _draw_arrow(ax, (1.7, 0.95), (2.3, 0.95))
  _draw_arrow(ax, (4.4, 0.95), (5.0, 0.95))
  _draw_arrow(ax, (7.1, 0.95), (7.7, 0.95))
  _draw_arrow(ax, (9.8, 0.95), (10.3, 0.95))
  ax.set_title("Attenuator Section Signal Chain", fontsize=12)
  _save(fig, "attenuator-signal-chain")


def draw_attenuator_enclosure_layout() -> None:
  fig, ax = _make_canvas(7.4, 3.4)
  ax.set_xlim(0, 10)
  ax.set_ylim(0, 5)
  ax.add_patch(Rectangle((1.0, 1.5), 8.0, 2.0, fill=False, linewidth=1.7))
  for idx, (x, label) in enumerate([(2.6, "SW-A\n6 dB"), (5.0, "SW-B\n10 dB"), (7.4, "SW-C\n20 dB")]):
    ax.plot(x, 2.5, marker="o", markersize=7, color="black")
    ax.text(x, 3.75, label, ha="center", va="bottom", fontsize=9)
  ax.text(1.0, 0.9, "Left end wall: BNC IN hole centered", fontsize=9)
  ax.text(5.3, 0.9, "Right end wall: BNC OUT hole centered", fontsize=9)
  ax.set_title("Enclosure Top View Layout (Lid Face Up)", fontsize=12)
  _save(fig, "attenuator-enclosure-layout")


def draw_attenuator_resistor_tree() -> None:
  fig, ax = _make_canvas(7.0, 2.8)
  ax.set_xlim(0, 10)
  ax.set_ylim(0, 4)
  ax.text(0.4, 2.3, "free end", fontsize=9)
  ax.text(9.0, 2.3, "free end", fontsize=9)
  _draw_box(ax, 1.7, 2.0, 1.4, 0.6, "R_s1\n18Ω")
  _draw_box(ax, 6.8, 2.0, 1.4, 0.6, "R_s2\n18Ω")
  ax.text(5.0, 2.3, "MID", fontsize=10, ha="center", va="center")
  ax.plot([3.1, 4.4], [2.3, 2.3], color="black", linewidth=1.5)
  ax.plot([5.6, 6.8], [2.3, 2.3], color="black", linewidth=1.5)
  _draw_box(ax, 4.3, 0.9, 1.4, 0.6, "R_shunt\n68Ω")
  ax.plot([5.0, 5.0], [2.1, 1.5], color="black", linewidth=1.5)
  ax.plot([5.0, 5.0], [0.9, 0.4], color="black", linewidth=1.5)
  ax.text(5.0, 0.15, "chassis ground", ha="center", fontsize=9)
  ax.set_title("T-pad Component Tree (Section A Example)", fontsize=12)
  _save(fig, "attenuator-resistor-tree")


def draw_attenuator_label_strip() -> None:
  fig, ax = _make_canvas(6.4, 1.8)
  ax.set_xlim(0, 9)
  ax.set_ylim(0, 2)
  _draw_box(ax, 0.6, 0.5, 2.3, 0.9, "6 dB")
  _draw_box(ax, 3.3, 0.5, 2.3, 0.9, "10 dB")
  _draw_box(ax, 6.0, 0.5, 2.3, 0.9, "20 dB")
  ax.set_title("Switch Label Strip", fontsize=12)
  _save(fig, "attenuator-label-strip")


def draw_attenuator_switch_modes() -> None:
  fig, ax = _make_canvas(8.8, 3.6)
  ax.set_xlim(0, 13)
  ax.set_ylim(0, 6)

  ax.text(3.0, 5.5, "BYPASS mode", ha="center", fontsize=11, weight="bold")
  _draw_box(ax, 1.1, 4.3, 1.0, 0.6, "2")
  _draw_box(ax, 2.4, 4.3, 1.0, 0.6, "1")
  _draw_box(ax, 3.7, 4.3, 1.0, 0.6, "4")
  _draw_box(ax, 5.0, 4.3, 1.0, 0.6, "5")
  _draw_arrow(ax, (2.1, 4.6), (2.4, 4.6))
  _draw_arrow(ax, (3.4, 4.6), (3.7, 4.6))
  ax.plot([3.4, 3.7], [4.6, 4.6], color="black", linewidth=1.5)
  ax.text(3.55, 4.95, "bypass wire", ha="center", fontsize=8)

  ax.text(9.6, 5.5, "ATTENUATE mode", ha="center", fontsize=11, weight="bold")
  _draw_box(ax, 7.0, 4.3, 1.0, 0.6, "2")
  _draw_box(ax, 8.2, 4.3, 1.0, 0.6, "3")
  _draw_box(ax, 9.4, 4.3, 1.1, 0.6, "R_s1")
  _draw_box(ax, 10.8, 4.3, 1.1, 0.6, "MID")
  _draw_box(ax, 12.2, 4.3, 1.1, 0.6, "R_s2")
  ax.plot([13.3, 13.7], [4.6, 4.6], color="black", linewidth=1.5)
  _draw_box(ax, 13.7, 4.3, 1.0, 0.6, "6")
  _draw_box(ax, 14.9, 4.3, 1.0, 0.6, "5")
  for x0, x1 in [(8.0, 8.2), (9.2, 9.4), (10.5, 10.8), (11.9, 12.2), (13.3, 13.7), (14.7, 14.9)]:
    ax.plot([x0, x1], [4.6, 4.6], color="black", linewidth=1.5)
  _draw_box(ax, 10.7, 2.9, 1.3, 0.6, "R_shunt")
  ax.plot([11.35, 11.35], [4.3, 3.5], color="black", linewidth=1.5)
  ax.plot([11.35, 11.35], [2.9, 2.2], color="black", linewidth=1.5)
  ax.text(11.35, 1.8, "chassis", ha="center", fontsize=9)

  ax.set_xlim(0.3, 16.2)
  ax.set_ylim(1.4, 5.9)
  ax.set_title("DPDT Section Signal Paths", fontsize=12)
  _save(fig, "attenuator-switch-modes")


def draw_yagi_2m_boom_layout() -> None:
  fig, ax = _make_canvas(9.4, 2.8)
  ax.set_xlim(0, 15)
  ax.set_ylim(0, 4)
  _draw_box(ax, 0.5, 1.6, 2.0, 0.8, "Director T")
  _draw_box(ax, 4.0, 1.6, 2.3, 0.8, "Driven Cross")
  _draw_box(ax, 8.3, 1.6, 2.5, 0.8, "Reflector Cross")
  _draw_box(ax, 11.8, 1.6, 1.7, 0.8, "Handle T")
  _draw_arrow(ax, (2.5, 2.0), (4.0, 2.0), 'Boom-B')
  _draw_arrow(ax, (6.3, 2.0), (8.3, 2.0), 'Boom-A')
  _draw_arrow(ax, (10.8, 2.0), (11.8, 2.0), 'Handle')
  ax.text(5.1, 1.1, '~8" center-to-center', ha="center", fontsize=9)
  ax.text(9.6, 1.1, '~12.5" center-to-center', ha="center", fontsize=9)
  ax.set_title("2m Boom Layout (Front to Back)", fontsize=12)
  _save(fig, "yagi-2m-boom-layout")


def draw_yagi_hairpin_2m() -> None:
  fig, ax = _make_canvas(5.6, 3.2)
  ax.set_xlim(0, 10)
  ax.set_ylim(0, 8)
  ax.plot([2.8, 2.8], [2.0, 6.5], color="black", linewidth=2)
  ax.plot([7.2, 7.2], [2.0, 6.5], color="black", linewidth=2)
  ax.plot([2.8, 7.2], [6.5, 6.5], color="black", linewidth=2)
  ax.text(5.0, 7.0, "~3\" wire across top", ha="center", fontsize=9)
  ax.text(5.0, 4.3, "~3/4\" leg spacing", ha="center", fontsize=9)
  ax.text(2.8, 1.3, "solders to\nleft element", ha="center", fontsize=8)
  ax.text(7.2, 1.3, "solders to\nright element", ha="center", fontsize=8)
  ax.set_title("2m Hairpin Match Shape", fontsize=12)
  _save(fig, "yagi-hairpin-2m")


def main() -> None:
  draw_attenuator_switch_pinout()
  draw_attenuator_signal_chain()
  draw_attenuator_enclosure_layout()
  draw_attenuator_resistor_tree()
  draw_attenuator_label_strip()
  draw_attenuator_switch_modes()
  draw_yagi_2m_boom_layout()
  draw_yagi_hairpin_2m()


if __name__ == "__main__":
  main()

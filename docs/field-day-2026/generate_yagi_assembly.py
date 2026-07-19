"""
Generate a to-scale assembly drawing for the 3-element 2-meter tape
measure Yagi built at the M&K ARDF Field Day 2026 build event.

The drawing is produced directly from the dimensions published in
``build-event-syllabus.md`` (Project 1), so the figure always matches
the cut list and boom layout used in the build instructions.

Two panels are rendered:

  1. Plan (top) view of the whole antenna -- boom along the horizontal
     axis with the reflector, driven, and director tape-measure
     elements perpendicular to it.  Element lengths and the
     center-to-center boom spacings are dimensioned.

  2. Driven-element detail -- the two 17.75" halves, the 1" feed gap,
     the hairpin (beta) match, and the coax feedpoint.

All geometry is drawn in real inches (data units == inches) with an
equal aspect ratio, so the panels are dimensionally faithful.

Usage:
    ../../.venv-drawings/Scripts/python.exe generate_yagi_assembly.py
    # (or any Python with matplotlib installed)

Output:
    docs/field-day-2026/yagi-assembly.svg
    docs/field-day-2026/yagi-assembly.png
"""

from __future__ import annotations

import os
from typing import Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle

# ---------------------------------------------------------------------------
# Dimensions (inches) -- sourced from build-event-syllabus.md, Project 1
# ---------------------------------------------------------------------------

# Tape-measure element lengths (Step 3 cut list).
REFLECTOR_LEN = 41.375          # 41 3/8"
DRIVEN_HALF_LEN = 17.75         # 17 3/4" each, x2
DRIVEN_GAP = 1.0                # 1" feed gap between the halves
DIRECTOR_LEN = 35.125           # 35 1/8"

# Center-to-center boom spacing (Step 2 verification).
SPACING_DRIVEN_REFLECTOR = 12.5  # driven cross -> reflector cross
SPACING_DIRECTOR_DRIVEN = 8.0    # director T  -> driven cross

# Operator handle (Step 1, "14-18\"" -- nominal value for the drawing).
HANDLE_LEN = 16.0

# Hairpin / beta match (Step 7).
HAIRPIN_TOP = 3.0    # ~3" of wire across the top of the U
HAIRPIN_GAP = 0.75   # ~3/4" between the legs of the U

OUT_SVG = os.path.join(os.path.dirname(__file__), "yagi-assembly.svg")
OUT_PNG = os.path.join(os.path.dirname(__file__), "yagi-assembly.png")

# ---------------------------------------------------------------------------
# Drawing style
# ---------------------------------------------------------------------------

BOOM_COLOR = "#4a4a4a"
ELEMENT_COLOR = "#1f6feb"
FITTING_COLOR = "#d0d7de"
FITTING_EDGE = "#57606a"
HAIRPIN_COLOR = "#cf222e"
COAX_COLOR = "#1a7f37"
DIM_COLOR = "#57606a"

ELEMENT_LW = 4.0     # tape-measure blades drawn as thick lines
BOOM_LW = 6.0


def _dim_line(
    ax: plt.Axes,
    p0: Tuple[float, float],
    p1: Tuple[float, float],
    text: str,
    offset: Tuple[float, float] = (0.0, 0.0),
    text_offset: Tuple[float, float] = (0.0, 0.0),
    rotation: float = 0.0,
) -> None:
    """Draw a double-headed dimension line with a centered label.

    ``p0`` and ``p1`` are the measured points; ``offset`` shifts the
    whole dimension line (e.g. below or beside the part) and
    ``text_offset`` nudges the label clear of the line.
    """
    x0, y0 = p0[0] + offset[0], p0[1] + offset[1]
    x1, y1 = p1[0] + offset[0], p1[1] + offset[1]

    ax.add_patch(
        FancyArrowPatch(
            (x0, y0),
            (x1, y1),
            arrowstyle="<|-|>",
            mutation_scale=10,
            color=DIM_COLOR,
            lw=1.0,
            shrinkA=0,
            shrinkB=0,
        )
    )
    # Witness ticks back to the measured points.
    ax.plot([p0[0] + offset[0], p0[0]], [p0[1] + offset[1], p0[1]],
            color=DIM_COLOR, lw=0.6, ls=(0, (2, 2)))
    ax.plot([p1[0] + offset[0], p1[0]], [p1[1] + offset[1], p1[1]],
            color=DIM_COLOR, lw=0.6, ls=(0, (2, 2)))

    mx, my = (x0 + x1) / 2 + text_offset[0], (y0 + y1) / 2 + text_offset[1]
    ax.text(
        mx,
        my,
        text,
        color=DIM_COLOR,
        fontsize=8.5,
        ha="center",
        va="center",
        rotation=rotation,
        bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none"),
    )


def _fitting(ax: plt.Axes, x: float, label: str, kind: str) -> None:
    """Draw a PVC cross/T fitting box centered at boom position ``x``."""
    w, h = 1.4, 1.4
    ax.add_patch(
        Rectangle(
            (x - w / 2, -h / 2),
            w,
            h,
            facecolor=FITTING_COLOR,
            edgecolor=FITTING_EDGE,
            lw=1.2,
            zorder=5,
        )
    )
    ax.text(
        x,
        -h / 2 - 1.6,
        label,
        color=FITTING_EDGE,
        fontsize=8,
        ha="center",
        va="top",
        zorder=6,
    )
    _ = kind  # reserved for future cross/T differentiation


def _clamp(ax: plt.Axes, x: float, y: float) -> None:
    """Small mark representing a hose clamp on an element."""
    ax.plot(x, y, marker="o", ms=4, mfc="white", mec=FITTING_EDGE,
            mew=1.0, zorder=7)


def draw_plan_view(ax: plt.Axes) -> None:
    """Render the whole-antenna plan (top) view."""
    # Boom axis positions (x), reflector at the origin.
    x_reflector = 0.0
    x_driven = x_reflector + SPACING_DRIVEN_REFLECTOR
    x_director = x_driven + SPACING_DIRECTOR_DRIVEN
    x_handle_end = x_reflector - HANDLE_LEN

    # --- Boom + handle ----------------------------------------------------
    ax.plot([x_handle_end, x_director], [0, 0], color=BOOM_COLOR,
            lw=BOOM_LW, solid_capstyle="round", zorder=2)

    # --- Elements (vertical, centered on the boom) ------------------------
    # Reflector (single blade).
    ax.plot([x_reflector, x_reflector],
            [-REFLECTOR_LEN / 2, REFLECTOR_LEN / 2],
            color=ELEMENT_COLOR, lw=ELEMENT_LW, solid_capstyle="round",
            zorder=4)
    _clamp(ax, x_reflector, 1.2)
    _clamp(ax, x_reflector, -1.2)

    # Director (single blade).
    ax.plot([x_director, x_director],
            [-DIRECTOR_LEN / 2, DIRECTOR_LEN / 2],
            color=ELEMENT_COLOR, lw=ELEMENT_LW, solid_capstyle="round",
            zorder=4)
    _clamp(ax, x_director, 1.2)
    _clamp(ax, x_director, -1.2)

    # Driven element: two halves with the 1" feed gap at the center.
    half_top = DRIVEN_GAP / 2 + DRIVEN_HALF_LEN
    ax.plot([x_driven, x_driven], [DRIVEN_GAP / 2, half_top],
            color=ELEMENT_COLOR, lw=ELEMENT_LW, solid_capstyle="round",
            zorder=4)
    ax.plot([x_driven, x_driven], [-DRIVEN_GAP / 2, -half_top],
            color=ELEMENT_COLOR, lw=ELEMENT_LW, solid_capstyle="round",
            zorder=4)
    _clamp(ax, x_driven, half_top - 1.5)
    _clamp(ax, x_driven, -(half_top - 1.5))

    # Hairpin (beta) match bridging the gap.
    hx = x_driven + 0.9
    ax.plot([x_driven, hx, hx, x_driven],
            [DRIVEN_GAP / 2, DRIVEN_GAP / 2, -DRIVEN_GAP / 2,
             -DRIVEN_GAP / 2],
            color=HAIRPIN_COLOR, lw=2.0, zorder=6)

    # Coax feedpoint at the driven gap, routed back along the boom.
    cx = x_driven - 0.9
    ax.plot([x_driven, cx, cx, x_handle_end + 1.0],
            [DRIVEN_GAP / 2, DRIVEN_GAP / 2, 0.0, 0.0],
            color=COAX_COLOR, lw=2.0, zorder=3)
    ax.text(x_handle_end + 1.0, 1.6, "coax to RX\n(BNC)",
            color=COAX_COLOR, fontsize=8, ha="left", va="bottom")

    # --- Fittings + handle ------------------------------------------------
    _fitting(ax, x_reflector, "Reflector\ncross", "cross")
    _fitting(ax, x_driven, "Driven\ncross", "cross")
    _fitting(ax, x_director, "Director\nT", "tee")
    ax.add_patch(
        Rectangle((x_handle_end - 0.2, -1.4), 1.4, 2.8,
                  facecolor=FITTING_COLOR, edgecolor=FITTING_EDGE,
                  lw=1.2, zorder=5)
    )
    ax.text(x_handle_end + 0.5, -3.0, "Handle T", color=FITTING_EDGE,
            fontsize=8, ha="center", va="top")

    # --- "Front of beam" arrow (placed in clear space, lower right) ------
    fob_y = -REFLECTOR_LEN / 2 + 1.0
    ax.annotate(
        "",
        xy=(x_director + 11.0, fob_y),
        xytext=(x_director + 3.0, fob_y),
        arrowprops=dict(arrowstyle="-|>", color=BOOM_COLOR, lw=1.6),
    )
    ax.text(x_director + 3.0, fob_y + 1.4, "main lobe / front of beam",
            fontsize=8, color=BOOM_COLOR, ha="left", va="bottom")

    # --- Element-length dimensions ---------------------------------------
    _dim_line(ax, (x_reflector, -REFLECTOR_LEN / 2),
              (x_reflector, REFLECTOR_LEN / 2),
              'Reflector\n41 3/8"', offset=(-2.6, 0), rotation=90)
    _dim_line(ax, (x_director, -DIRECTOR_LEN / 2),
              (x_director, DIRECTOR_LEN / 2),
              'Director\n35 1/8"', offset=(2.6, 0), rotation=90)
    _dim_line(ax, (x_driven, DRIVEN_GAP / 2), (x_driven, half_top),
              '17 3/4"', offset=(3.4, 0), rotation=90)

    # --- Boom-spacing dimensions (above the elements) --------------------
    dim_y = REFLECTOR_LEN / 2 + 3.0
    _dim_line(ax, (x_reflector, dim_y), (x_driven, dim_y),
              '12 1/2" C-C', text_offset=(0, 1.2))
    _dim_line(ax, (x_driven, dim_y), (x_director, dim_y),
              '8" C-C', text_offset=(0, 1.2))

    ax.set_title("Plan (top) view -- 3-element 2 m tape measure Yagi",
                 fontsize=11, color="#24292f")
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(x_handle_end - 4, x_director + 16)
    ax.set_ylim(-REFLECTOR_LEN / 2 - 6, REFLECTOR_LEN / 2 + 7)


def draw_driven_detail(ax: plt.Axes) -> None:
    """Render the driven-element feed/hairpin detail (not to plan scale)."""
    gap = DRIVEN_GAP
    stub = 4.0  # only show the inner portion of each half

    # Inner ends of the two driven halves.
    ax.plot([0, 0], [gap / 2, gap / 2 + stub], color=ELEMENT_COLOR,
            lw=6, solid_capstyle="round", zorder=4)
    ax.plot([0, 0], [-gap / 2, -gap / 2 - stub], color=ELEMENT_COLOR,
            lw=6, solid_capstyle="round", zorder=4)

    # Tinned solder corners.
    for sign in (1, -1):
        ax.plot(0.0, sign * gap / 2, marker="s", ms=7, mfc="#c0c0c0",
                mec="#444", mew=0.8, zorder=6)

    # Hairpin (beta) match -- U-shaped wire across the gap.
    hx = 1.4
    ax.plot([0, hx, hx, 0],
            [gap / 2, gap / 2, -gap / 2, -gap / 2],
            color=HAIRPIN_COLOR, lw=2.6, zorder=5)
    ax.text(hx + 0.2, 2.0, "hairpin / beta match\n(6\" of 14 AWG)",
            color=HAIRPIN_COLOR, fontsize=8.5, ha="left", va="bottom")

    # Coax feed -- center to one tip, braid to the other.
    cx = -1.4
    ax.plot([0, cx], [gap / 2, gap / 2], color=COAX_COLOR, lw=2.2,
            zorder=5)
    ax.plot([0, cx], [-gap / 2, -gap / 2], color=COAX_COLOR, lw=2.2,
            zorder=5)
    ax.plot([cx, cx], [-gap / 2, gap / 2], color=COAX_COLOR, lw=2.2,
            zorder=5)
    ax.text(cx - 0.2, -2.0, "RG-58\ncoax", color=COAX_COLOR, fontsize=8.5,
            ha="right", va="top")

    # Gap dimension.
    _dim_line(ax, (0, -gap / 2), (0, gap / 2), '1" gap',
              offset=(3.2, 0), text_offset=(0.9, 0.0), rotation=0)

    ax.text(0, gap / 2 + stub + 0.5, "to outer half\n(17 3/4\")",
            color=ELEMENT_COLOR, fontsize=8, ha="center", va="bottom")
    ax.text(0, -gap / 2 - stub - 0.5, "to outer half\n(17 3/4\")",
            color=ELEMENT_COLOR, fontsize=8, ha="center", va="top")

    ax.set_title("Driven-element feed detail (Steps 6-9)", fontsize=11,
                 color="#24292f")
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(cx - 3.0, hx + 4.5)
    ax.set_ylim(-gap / 2 - stub - 2.2, gap / 2 + stub + 2.2)


def main() -> None:
    """Build the figure and write the SVG and PNG outputs."""
    fig = plt.figure(figsize=(13.5, 8.0))
    gs = fig.add_gridspec(1, 2, width_ratios=[2.3, 1.0], wspace=0.05)
    ax_plan = fig.add_subplot(gs[0, 0])
    ax_detail = fig.add_subplot(gs[0, 1])

    draw_plan_view(ax_plan)
    draw_driven_detail(ax_detail)

    fig.suptitle(
        "2-Meter Tape Measure Yagi -- Assembly Drawing "
        "(M&K ARDF Field Day 2026)",
        fontsize=13,
        color="#24292f",
        y=0.98,
    )
    fig.text(
        0.5,
        0.02,
        "Cut for ~146 MHz.  Dimensions from build-event-syllabus.md, "
        "Project 1.  Plan view to scale; feed detail enlarged.",
        ha="center",
        fontsize=8,
        color=DIM_COLOR,
    )

    fig.savefig(OUT_SVG, bbox_inches="tight")
    fig.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote {OUT_SVG}")
    print(f"Wrote {OUT_PNG}")


if __name__ == "__main__":
    main()

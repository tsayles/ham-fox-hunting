## Summary
Design and build a **digitally controlled variable step attenuator** for RF use (up to **6 GHz target**), using multiple **Infineon BGS12P2L6E6327XTSA1 SPDT RF switches** in a switchable attenuator ladder topology.

Primary goal: selectable attenuation states with predictable insertion loss, return loss, and repeatability.

Datasheet:  
https://www.infineon.com/dgdl/Infineon-BGS12P2L6-DataSheet-v02_00-EN.pdf?fileId=5546d4626cb27db2016d4487d53603ce

## Problem / Motivation
We need a compact attenuator module with digitally selectable attenuation for RF signal-level control in fox-hunting receiver workflows. A deterministic step network is preferred over analog gain control for repeatability and calibration.

## Scope
- Define attenuator architecture (e.g., binary-weighted or equal-step ladder) using BGS12P2L6 switches.
- Select step values and total attenuation range.
- Implement user control via **rotary encoder**.
- Use **discrete logic control** for switch drive if feasible (preferred), otherwise document why not and propose minimal logic alternative.
- Produce schematic + PCB layout + BOM.
- Build and bench-test at RF-relevant frequencies.

## Out of Scope (for this issue)
- Full enclosure/mechanical packaging.
- Firmware-heavy UI features (unless required for basic control).
- Automated factory calibration flow.

## Functional Requirements
- Rotary encoder changes attenuation state incrementally.
- Attenuation state maps deterministically to switch control lines.
- Power-on behavior is defined (default attenuation state).
- No illegal/undefined switch states during transitions (or transitions are bounded and documented).

## Electrical / RF Requirements (initial targets)
> These can be adjusted after simulation if needed.

- Frequency range: DC (or lowest practical) to **6 GHz target**
- Step resolution: define and justify (candidate: 1 dB / 2 dB / binary weighted)
- Total attenuation range: define and justify (candidate: 31 dB or similar)
- Input/output impedance: 50 Ω
- Characterize:
  - Insertion loss at 0 dB state
  - Return loss (S11/S22)
  - Step accuracy per state
  - Isolation/leakage impact of switch topology

## Design Tasks
- [ ] Evaluate candidate topologies (switched Pi/T sections, binary ladder, etc.)
- [ ] Simulate expected attenuation states and mismatch effects
- [ ] Define control truth table for all states
- [ ] Implement rotary encoder + state machine / logic decode
- [ ] Determine discrete logic feasibility (decoder, latch, debounce, etc.)
- [ ] Create schematic and PCB with RF layout constraints
- [ ] Build prototype and run bench measurements
- [ ] Document measured vs. expected performance

## Deliverables
- [ ] Final schematic
- [ ] PCB layout files
- [ ] BOM with part availability notes
- [ ] Control/state truth table
- [ ] Bring-up/test procedure
- [ ] Measurement report (plots or table by frequency and attenuation state)
- [ ] Short design notes covering tradeoffs and next revisions

## Acceptance Criteria
- [ ] User can select attenuation states via rotary encoder
- [ ] All defined attenuation steps are reachable and stable
- [ ] Measured attenuation trend matches design intent across test band
- [ ] RF behavior is documented for at least key spot frequencies (e.g., 144 MHz, 433 MHz, 915 MHz, 2.4 GHz, and as high as test equipment allows)
- [ ] Control implementation is discrete-logic-based **or** includes a documented rationale for an alternative

## Open Questions
- Exact target step size and max attenuation?
- Is bidirectional RF path required?
- Power/voltage constraints for control logic?
- Preferred connector/footprint and board form factor?
- Minimum acceptable performance thresholds (e.g., step error, insertion loss)?

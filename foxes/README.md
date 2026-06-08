# Fox Transmitter Programming

This directory contains configuration records and programming procedures
for the club's Byonics fox transmitters.

## Devices

| Device | Model | Notes |
|---|---|---|
| Fox 1 | Byonics MicroFox 15 (MF-15) | Discontinued; programs any time |
| Fox 2 | Byonics MicroFox PicCon (MF-PC) | Programs within 2 sec of power-up |

## Hardware Required

- **Byonics USB-2.5 cable** (USB to 2.5mm stereo serial) for both devices
- Windows PC or Chrome browser with Web Serial support
- USB drivers: [PL2303 v1.7](https://www.byonics.com/downloads/PL2303_Prolific_DriverInstaller_v1.7.0.zip)
  - Windows 11 driver fix: https://embetronicx.com/uncategorized/fixed-prolific-pl2303ta-usb-to-serial-and-windows-11/

## Programming Tools

| Tool | URL | Supports |
|---|---|---|
| Web config (recommended) | https://byonics.com/mfconfig/ | MF-15, MF-PC, MF2, BFoxCon, PicCon3 |
| Windows software | MicroFoxConfig v1.95 | MF-PC, MF2 |

## Programming Workflow

### Step 1 — Read Current Settings

1. Connect the USB-2.5 cable between the device and the computer.
2. Open https://byonics.com/mfconfig/ in Chrome.
3. Click **Select Serial Port** and choose the correct COM port
   (unplug/replug the cable to identify it if needed).
4. **MF-PC only**: cycle device power — it listens for serial only in
   the first 2 seconds after power-up.
5. Click **Read Version** to confirm connection.
6. Click **Read Config** to pull current settings from the device.
7. Record all settings in the device's `current-config.yaml` file.

### Step 2 — Compose New Settings

1. Review `target-config.yaml` for the desired hunt settings.
2. Confirm frequency, callsign, timing, and power are appropriate for
   the event type (park walk / mobile / practice).
3. Get event coordinator sign-off on the target config before writing.

### Step 3 — Write New Settings

1. Edit settings in the web tool to match `target-config.yaml`.
2. **MF-PC only**: cycle power immediately before clicking Write.
3. Click **Write Config**.
4. Click **Read Config** again to verify the write was successful.
5. Update `current-config.yaml` to reflect the new programmed state.

### Step 4 — Field Test

- [ ] Transmitter keys up on the correct frequency
- [ ] CW ID sends correct callsign
- [ ] Timing cycle matches intended duty cycle
- [ ] Signal audible at expected range with a handheld RDF setup

## Notes

- FCC Part 97 requires a valid amateur callsign to be transmitted.
- Power levels should be appropriate for hunt type: lower power for
  park walks (easier near-field work), higher for mobile hunts.
- Frequency should be coordinated with local repeater trustee to
  avoid conflicts.

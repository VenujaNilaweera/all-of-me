---
type: project
title: Smart Timer Plug
status: in-progress
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [esp32, mosfet, iot, home-automation]
links: [[[confirmed-toolbox]]]
---

# Smart Timer Plug

ESP32-based smart plug. An appliance (charger, iron) plugs in and
switches off after a set time. Can also be toggled anytime via IR remote
or Bluetooth, independent of the timer.

## Gate-drive design decisions
Non-logic-level **IRFZ44N** MOSFET driven from the 3.3V ESP32 through a
BC547 (or 2SD400 substitute) as a gate driver from a 6-7V rail.

- Confirmed values: 2.2k base resistor, 4.7k-10k pull-up to the driver
  rail, 100 ohm gate series resistor, 10k gate-to-GND pull-down.
- Wanted the gate to default to GND (MOSFET off at power-up) — this
  needs **two cascaded NPN stages**, not a single-NPN inverting version.
  A single NPN inverts logic (GPIO HIGH = MOSFET OFF) and defaults the
  load **on**, which was rejected.
- 2SD400 pinout (E-C-B) differs from BC547 (E-B-C) — wiring must be
  verified before power-up.
- A TCRT5000 reflective IR sensor with a 10k pull-up was also checked.
- LED status current: 470 ohm at 5V is ~6.4 mA, accepted for an
  indicator.
- IRLZ44N (logic-level) was repeatedly suggested as a simpler swap, but
  builds are done from parts already on hand.

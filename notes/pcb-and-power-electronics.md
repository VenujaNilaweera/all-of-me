---
type: note
title: PCB Design & Power Electronics Knowledge
status: ongoing
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [pcb, altium, power-electronics, impedance, differential-pairs, bms]
links: [[[bms-pcb]], [[power-electronics]]]
---

# PCB Design & Power Electronics Knowledge

## Tooling
Altium Designer — focus on designing real PCBs, not only breadboard
prototypes.

## PCB interview/knowledge topics
Stackup, differential pairs, impedance, trace width, why 90° corner
routing is generally avoided, ground planes, routing, power traces,
signal integrity.

- **Impedance (simple explanation used):** the effective resistance a
  high-frequency signal experiences travelling through a PCB trace and
  its surrounding structure. Depends on trace width/thickness, distance
  to reference plane, dielectric material, layer structure.
- **Differential pair:** two traces carrying opposite signals; the
  receiver reads the difference, improving common-noise rejection.
- **90° traces:** avoided in modern high-speed routing due to
  discontinuity/geometry concerns at the corner.

## Power electronics components/topics
TRIACs, MOSFETs, IGBTs, SiC MOSFETs, optocouplers, inverters, filters,
motor drives, EV traction inverters.

Specific parts used/discussed: BTA41, BT136, BT139, MOC3020, MOC3021,
ACS712, TPS22967DSGR.

- **TRIAC control:** switching with optocoupler isolation (MOC3020/3021)
  for AC control via gate triggering.
- **Inverters:** multilevel inverters, fast EV traction inverters, LC/LCL
  filters, PMSM drives, FOC, DTC, SiC vs IGBT tradeoffs.

## BMS
Battery Management Systems — cell voltage monitoring, protection, current
sensing, MCU control, PCB design, power switching, communication. Key IC:
BQ76920. See [[bms-pcb]] for the concrete project.

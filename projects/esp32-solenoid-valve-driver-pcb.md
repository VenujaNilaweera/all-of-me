---
type: project
title: ESP32 Solenoid Valve Driver PCB
status: in-progress
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [pcb, altium, esp32, solenoid, research-tooling]
links: [[[dengue-crt-wearable]]]
---

# ESP32 Solenoid Valve Driver PCB

Custom 2-layer Altium board for a research platform (supports the
pneumatic side of [[dengue-crt-wearable]]-adjacent work).

## Design
5 valve drivers, AMS1117 LDO, AO3400 MOSFETs with 1N4007 flyback diodes,
PC817 optocouplers for isolated I/O, dual UART. 30% smaller than the
first single-layer revision.

## Collaboration
Feedback and collaboration from Pansilu Harshan.

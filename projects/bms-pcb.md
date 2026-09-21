---
type: project
title: Battery Management System (BMS) PCB
status: in-progress
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [bms, pcb, altium, stm32, power-electronics]
links: [[[self]], [[pcb-and-power-electronics]]]
---

# BMS PCB

Battery Management System designed in Altium Designer: cell voltage
monitoring, protection, current sensing, MCU control.

## Key components
- BQ76920 — battery monitor/protector IC.
- STM32 for control (STM32G071 considered, noted as relatively expensive).
- TPS22967DSGR considered for e-fuse / electronic power switching.

## Scope
PCB routing and power-management design for a battery pack protection and
monitoring board.

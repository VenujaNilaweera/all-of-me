---
type: project
title: Custom ESP32 Robot Controller Board
status: in-progress
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [pcb, altium, esp32, robotics, portfolio]
links: [[[confirmed-toolbox]], [[pcb-and-power-electronics]]]
---

# Custom ESP32 Robot Controller Board

General-purpose plug-and-play board so buyers can connect batteries and
motors/servos to build Bluetooth/Wi-Fi cars or line-following robots
without extra modules or a breadboard. Also a portfolio piece. Designed
in Altium Designer 25.4.2, powered from 2S Li-ion.

## Design evolution
- **Early selection:** ESP32-WROOM-32U, MX1508 motor driver, CH340G
  USB-UART, AMS1117-3.3, USB4110-GF-A.
- **Settled design:** ESP32-WROOM-32D, **DRV8833** dual H-bridge (chosen
  partly for portfolio appropriateness over MX1508), **CP2102-GMR**
  USB-UART, AMS1117-3.3 (3V3 logic), MC7805CDT (5V servo rail), MPU-6050
  IMU (LSM6DS3/LSM6DSOX/BMI160 considered as lower-noise alternatives),
  USB4105-GF-A.

## Power architecture
- Dual power input (USB-C + DC barrel jack) combined via Schottky
  diode-OR (SS34) so neither source backfeeds the other.
- Reverse-polarity protection on every input; adjustable eFuse on
  user-accessible GPIO headers.
- Three separate power domains: raw motor rail (VDC) straight to the
  driver, regulated 3V3 for ESP32/I2C sensors, regulated 5V for servos.
- CP2102 with transistor auto-reset from DTR/RTS — flashing needs no
  button presses.

## PCB layout
Moved from 2-layer to **4-layer** stackup (Top signal, GND plane, PWR
plane, Bottom signal) to fix routing congestion. IPC-2221 trace widths
per net class: VDC 1.4 mm, motor outputs 0.6 mm, power rails 0.3/0.25 mm,
signals 0.25 mm.

## Status (as of 2026-09-09)
Schematic through fully routed 4-layer board. Earlier open items:
polygon pours for split 3V3/VM nets, net-name cleanup (VDC/VEX/5V,
TXD0/TXD1), neckdown traces around the fine-pitch DRV8833. Next: Gerbers,
GitHub repo (Gerbers, BOM, schematic PDFs, Altium exports, README),
possible prototype build. A LinkedIn post was drafted and refined.

## House-standard parts (reused across boards)
CL10B104KB8NNNC (0.1 uF), RC0603FR-0710KL (10k), SS34, B3U-1000P tactile
button, DRV8833PWPR, CP2102-GMR, AMS1117-3.3, MC7805CDT, MPU-6050,
USB4105-GF-A.

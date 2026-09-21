---
type: project
title: Active Suspension Wheelchair (Prototype 01)
status: in-progress
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [robotics, mechanical, mpu6050, motors, biomedical]
links: [[[self]]]
---

# Active Suspension Wheelchair (ASW)

Reduces vibration/shock transmitted to a seated wheelchair user on uneven
surfaces. Shown at Techno Exhibition 2025, BMICH, as "Prototype 01".

## Architecture — two suspension levels
- **Passive:** bicycle-style shock absorbers for small shocks/vibration.
- **Active:** two DC geared motors per wheel mechanism, driving lead
  screws, controlled via inertial sensing, mechanically adjusting the
  suspension in real time.

## Control objective
Keep the seating area as flat/stable as possible while moving over uneven
terrain, via a PID loop.

## Sensor
**Three MPU6050 IMUs** feeding the PID control loop (a sensor-fusion
approach to improve accuracy).

## Team
Showcased at Techno Exhibition 2025 (BMICH) with Dinal Disnaka and
Chamath Samuditha.

## Disciplines integrated
Mechanical suspension, motor control, embedded control, mechanical
linkages, power, real-time response — representative of Venuja's style of
combining disciplines rather than treating electronics in isolation.

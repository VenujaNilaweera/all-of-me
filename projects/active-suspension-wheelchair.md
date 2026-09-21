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
- **Active:** DC geared motors + lead screws, controlled via an MPU6050,
  mechanically adjust the suspension in real time.

## Control objective
Keep the seating area as flat/stable as possible while moving over uneven
terrain.

## Sensor
MPU6050 (inertial). A combination/sensor-fusion approach was discussed to
improve accuracy.

## Disciplines integrated
Mechanical suspension, motor control, embedded control, mechanical
linkages, power, real-time response — representative of Venuja's style of
combining disciplines rather than treating electronics in isolation.

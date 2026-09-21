---
type: project
title: ThermalFlow
status: in-progress
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [thermal, esp32, edge-ai, hvac, privacy, product]
links: [[[self]]]
---

# ThermalFlow

Intelligent thermal occupancy sensing platform: uses infrared thermal
sensing (not a camera) to find where people are in a room and direct
airflow/cooling only there, instead of cooling the whole room.

## Hardware
- Sensor: MLX90641 thermal array, 16x12 resolution.
- Processing: ESP32, running locally (no cloud).

## Design philosophy
Camera-free, privacy-preserving, local processing, low-cost, retrofit-
friendly. Occupancy data is not sent to the cloud.

## Key technical challenge
Human detection / pet filtering — distinguishing "a human is here" from
"something warm exists" (rejecting pets and other heat sources).

## Product framing
- Pitch: "A privacy-preserving thermal intelligence platform that slashes
  building energy waste by automatically directing airflow only where
  people are actually sitting."
- Alt pitch: "A low-cost, camera-free thermal sensor module that runs
  local AI on an ESP32 to give HVAC systems real-time human tracking."
- Sri Lanka market angle: retrofit existing electric fans (~9 million
  units in-market) rather than requiring replacement.
- Target retail price: ~LKR 7,000-8,000 per plug-and-play retrofit unit.

## Validation / milestones
- Live prototype demonstrated at Techno Exhibition 2025, BMICH.
- Prepared for IEEE Innovation Nation Sri Lanka 2026, Business Stage
  Submission/Demo — required framing problem, solution, value
  proposition, market, pricing, validation, differentiation, and pitch.

## Core value propositions
Zero cloud, privacy, resilience, pet filtering, local processing,
camera-free detection, low-cost retrofit.

## Patent
A patent filing is in progress for ThermalFlow (recorded, no further
technical detail on filing status).

## Recognition
IEEE Innovation Nation quarter-finalist (recorded).

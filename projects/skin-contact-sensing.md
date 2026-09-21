---
type: project
title: Capacitive Skin Contact Quality Sensing
status: in-progress
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [esp32, capacitive-sensing, biomedical, electrodes]
links: [[[self]]]
---

# Capacitive Skin Contact Quality Sensing

Determines how well a person's skin is contacting electrode pads, output
as an approximate 0-100% contact quality score.

## Hardware
ESP32, metal electrodes / copper-tape electrodes, capacitive sensing,
resistors, multiplexer experimentation. Started with 2 pads, concept
later expanded toward 8-16 pads.

## ESP32 touch sensing requirements
Continuous reading, automatic baseline calibration, normalization,
filtering, deadband, average active-electrode calculation, raw + filtered
value output over serial.

## Signal pipeline
raw touch value → baseline → deviation → normalization → EMA filtering →
contact score.

## Component notes
- CD4051 / 74HC4051N multiplexer: worked for output switching, but caused
  problems when used for capacitive touch **input** sensing.
- 1 MΩ resistor tested to reduce sensitivity.
- Copper tape used for electrode construction (low-cost custom sensing
  rather than commercial sensor modules).

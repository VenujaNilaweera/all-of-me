---
type: project
title: Thermal Imaging Visualization & Human Detection
status: in-progress
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [thermal, amg8833, mlx90641, pygame, filtering]
links: [[[self]], [[thermalflow]]]
---

# Thermal Imaging Visualization

General-purpose work on capturing, upscaling, and visualizing thermal
matrices from embedded hardware, feeding into ThermalFlow and related
projects.

## Sensors used
- AMG8833 — 8x8 thermal array.
- MLX90641 — 16x12 thermal array.
- Related temperature hardware explored: MAX6675, thermocouples, AHT10.

## Processing pipeline
Thermal matrix from Arduino/embedded hardware → Python, e.g. 16x12 → 32x24
via interpolation → visualization with Pygame.

## Filtering / detection techniques explored
Exponential moving average, moving average, background subtraction,
Gaussian mixture approaches, bilinear interpolation, thresholding,
template matching — aimed at robust human-vs-background/pet occupancy
detection, not just visualization.

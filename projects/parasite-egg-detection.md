---
type: project
title: Automated Parasite / Worm Egg Detection System
status: in-progress
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [biomedical, microscope, yolo, opencv, arduino, python]
links: [[[self]]]
---

# Automated Parasite / Worm Egg Detection

Automates part of the medical-lab workflow of examining microscope slides
for parasite eggs, motivated by a real lab workflow problem.

## Pipeline
Automated slide movement (motorized stage) → image capture → AI
detection (YOLO) → parasite identification/counting → result/report.

## Mechanical
Motorized microscope stage moves the slide in a predefined scanning
pattern to systematically cover it.

## Electronics
Arduino handles motion control, communicating with the computer over
serial.

## Software / AI
Python + OpenCV + YOLO for image acquisition, processing, dataset
handling, detection, and analysis. Uses `.pt` YOLO model weights with
local inference.

## Camera options considered
Laptop webcam, phone/IP camera (streaming over local Wi-Fi, processed
locally), or direct microscope image capture.

This project combines mechanical automation, embedded control, computer
vision, AI, and a biomedical application.

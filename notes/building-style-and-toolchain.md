---
type: note
title: Building Style, LED Debugging & Toolchain by Domain
status: ongoing
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [build-style, debugging, leds, arduino, toolchain, solidworks, altium]
links: [[[problem-solving-and-debugging-style]], [[embedded-and-hardware-experience]], [[pcb-and-power-electronics]]]
---

# Building Style, LED Debugging & Toolchain

## Core signature
"Make it work → make it visible → make it understandable → make it
reliable → make it presentable." Prefers a solution that is simple +
reliable + visible + easy to test + easy to modify over the most
sophisticated one. Wants to see *why* a system is working, not just that
it is: input → visible data → processing → visible state → output.

## Make the invisible visible — LEDs as debugging indicators
Strong recurring preference for physical LED status indicators alongside
(not instead of) Serial Monitor output, so state is readable from the
hardware itself without a laptop. Typical mapping: sensor
detected/inactive, system starting (flash), error (distinct pattern),
motor active, communication received (flash), calibration (sequence).
For multi-state systems, prefers one LED per state rather than one LED
overloaded with meaning (e.g. green=normal, yellow=processing/warning,
red=error, blue=comms/special mode) — colors depend on the actual
hardware/application. Example for a complex system like
[[thermalflow]]: separate LEDs for "ESP32 alive", "sensor reading",
"human detected", "tracking active", "communication", "error", so a
failure's location is visible without opening a laptop.

## Preferred debug output shape (sensor projects)
Wants raw value, filtered value, baseline, normalized value, and status
all printed together, e.g.:
```
Raw: 1832
Filtered: 1798
Baseline: 1500
Score: 72%
Status: CONTACT
```
Seen strongly in [[skin-contact-sensing]]. Preferred debugging setup
combines Serial Monitor (exact numbers) + LEDs (immediate state) +
motor/actuator (physical response) — each gives a different confirmation
layer, and serial output stays useful even once a GUI exists (a low-level
path when the GUI itself might be buggy).

## Arduino/embedded coding pattern
Code should visibly follow input → process → decision → output, not hide
behavior in complicated abstractions. Default structure: pin definitions
→ variables → setup() → read inputs → process data → decide system state
→ control outputs → debug output. Functions should represent one
meaningful action (`readSensor()`, `filterValue()`, `detectHuman()`,
`updateLEDs()`, `moveMotor()`, `sendData()`) rather than one large
`loop()`. Splits into multiple files only once a project is large enough
to need it (sensor.cpp, filter.cpp, motor.cpp, communication.cpp,
main.cpp) — a single `.ino` is fine for small Arduino projects.

## Preferred build/test order
1. Connect and test the component alone.
2. Read the raw value.
3. Add an LED indicator.
4. Add Serial output.
5. Add filtering.
6. Add decision logic.
7. Connect the actuator.
8. Integrate with the rest of the system.

Before a big integration, prove the smallest testable piece first (e.g.
"can I read the MLX90641?", "can I move the motor accurately?", "can
Arduino send one value to Python?").

## New-tool learning pattern
What is it? → what's it used for? → install/open it → smallest possible
project → get something working → use it in a real project. E.g. for
STM32: GPIO → LED → UART → timer → ADC → PWM → interrupts, not every
peripheral at once.

## Toolchain by engineering domain
- **Embedded:** Arduino IDE, STM32 dev tools, MPLAB (PIC), Serial
  Monitor; C / embedded C / Python.
- **AI / computer vision:** Python, OpenCV, PyTorch, Ultralytics/YOLO,
  NumPy, Streamlit.
- **Mechanical design:** **SolidWorks** — parts, assemblies, mechanisms,
  prototype design (used for e.g. [[active-suspension-wheelchair]]).
  Workflow: idea → sketch → 3D CAD → assembly → check movement →
  manufacture/prototype → integrate electronics.
- **PCB / electronics:** Altium Designer — schematics, layout, stackups,
  placement, routing, BMS design (see [[pcb-and-power-electronics]]).
- **Local AI:** Ollama (see [[computer-vision-and-ai-toolkit]]).
- **GUI/visualization:** Streamlit, CustomTkinter, PyQt5, Pygame.

Tool choice is driven by fast iteration (idea → build → test → modify)
and cost/availability (a cheap ESP32 over an industrial controller when
the industrial features aren't actually needed) rather than by
theoretical sophistication.

## What this means when helping design a prototype
Prefer: clear pin definitions, modular functions, LEDs for states, serial
debugging with raw+filtered values, small isolated tests before
integration, simple code first, practical wiring instructions.
Avoid: unnecessary frameworks/abstractions for small Arduino projects,
hiding behavior inside libraries, dropping visible debug indicators,
handing over a full complex architecture before the first subsystem is
proven, or assuming a component works without testing it.

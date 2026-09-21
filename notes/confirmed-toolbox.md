---
type: note
title: Confirmed Toolbox (Evidence-Based)
status: ongoing
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [toolbox, evidence-based, altium, esp32, supabase, python]
links: [[[building-style-and-toolchain]], [[pcb-and-power-electronics]], [[provenance-and-account-sharing]]]
---

# Confirmed Toolbox

From a 2026-09-21 evidence-labeled context pass (FACT/OBSERVED, more
carefully attributed than earlier dumps — see
[[provenance-and-account-sharing]]). This is the more trustworthy source
where it overlaps with [[building-style-and-toolchain]].

| Area | Tools | Use |
|---|---|---|
| PCB design | Altium Designer 25.4.2, Altium 365 web viewer, Autodesk Viewer (STEP), JLCPCB as fab backup | Schematic, layout, 4-layer stackups, Gerbers |
| Microcontrollers | ESP32 (WROOM-32D and 32U), Arduino, Raspberry Pi Zero 2 W | ESP32 for wireless/IoT and robots, Arduino for simpler builds and CRT pneumatics, Pi for Python-side processing |
| Firmware | Arduino framework, ESP32Servo, ESPSupabase, VS Code | Embedded code |
| Sensors/parts | MPU6050, MAX30102, AS5600, TCRT5000, thermistors, piezo pads, IR remote, BC547, 2SD400, IRFZ44N, DRV8833, MX1508 | Motion, biosignals, position, sensing, switching, motor drive |
| Actuators | NEMA 17 stepper, JGY-370, DC gear motors, servos, solenoid valves, pumps | Robotics and pneumatics |
| Python | OpenCV, PyQt5, Flask, Streamlit, Pillow, python-docx, FuzzyWuzzy, RPi.GPIO | CV pipelines, desktop/web tools, automation, document generation |
| AI/vision | YOLO/YOLOv8, OpenCV, PyTorch, HuggingFace, ArXiv, LLM APIs (Claude, Gemini) | Detection, annotation, agentic tooling |
| Backend/web | Supabase (REST, Storage, Row-Level Security), HTML/CSS/JS, GitHub, Overleaf/LaTeX | Data sync, prototypes, papers |
| Simulation | MATLAB/Simulink, Atoll, OptiSystem, Cadence Virtuoso | Coursework and labs |
| Documents | Word (python-docx, docx Node library), LaTeX, draw.io | Reports, papers, flowcharts |
| AI assistance | Claude (chat + Claude Code via prompts/spec files), z.ai for draft review | See [[ai-collaboration-preferences]] |

## Confirmed preferences
- ESP32 is the go-to platform for anything wireless.
- Altium is the PCB tool of choice.
- Python + OpenCV for image work; Supabase for shared/synced state.
- Reuses a fixed set of trusted components across boards — see the
  house-standard parts list in [[esp32-robot-controller-pcb]].
- Prefers using/substituting parts already on hand over buying the
  theoretically ideal part (e.g. 2SD400 substituted for BC547, IRFZ44N
  used without a logic-level part on hand — see [[smart-timer-plug]]).

## No evidence for (do not assume)
SolidWorks or STM32 usage specifically by Venuja — not seen in this more
carefully attributed source. See [[provenance-and-account-sharing]].

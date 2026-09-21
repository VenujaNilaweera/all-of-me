---
type: note
title: Strengths & Growth Areas (Interpreted, Not Diagnosed)
status: ongoing
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [self-development, strengths, growth, interpretation]
links: [[[self]], [[engineering-design-philosophy]]]
---

# Strengths & Growth Areas

> These are patterns interpreted from repeated interactions, not
> psychological or personality diagnoses. Treat as working observations,
> not fixed facts — see [[personal-values-and-interpretation]] for the
> full caveat.

## Observed strengths
- Strong curiosity that goes past "what to use" into "why" and "how
  exactly" — mechanistic curiosity, not just fact collection.
- Genuinely hands-on: repeatedly carries ideas through hardware, wiring,
  code, and testing rather than stopping at theory.
- Multidisciplinary: moves fluidly across electronics, embedded, AI,
  mechanical, biomedical, software, power electronics, PCB, and research.
- Willing to try unusual combinations (thermal arrays + ESP32, AI +
  microscope automation, capacitive sensing + multiplexers).
- Practical orientation — asks "can I actually build this?" rather than
  stopping at theoretical feasibility.
- Turns engineering work into demonstrations (exhibitions, pitches,
  videos, portfolios), treating communication of the work as part of the
  work.
- Persistence through iteration even when a system misbehaves; failures
  (CD4051 issues, CUDA/PyTorch mismatches, ESP32 USB problems, servo
  startup jump, sensor sensitivity) get treated as debuggable problems,
  not reasons to stop.
- Has moved across many tools/platforms fairly quickly (Arduino → ESP32 →
  STM32 → PIC → Raspberry Pi → Python → YOLO → PCB → power electronics),
  suggesting good adaptability. (Caveat: some of this specific platform
  breadth — STM32/PIC — is now disputed; see
  [[provenance-and-account-sharing]].)

## Additional confirmed strengths (2026-09-21 evidence-labeled source)
- **Full-stack hardware ownership:** carries a project from use case to
  schematic to a fully-routed multi-layer PCB layout and power
  architecture with protection (e.g. [[esp32-robot-controller-pcb]]).
- **Sound power/reliability judgment:** rail separation, protection
  circuitry, deliberate power-up default states (see
  [[technical-lessons-learned]] and [[smart-timer-plug]]).
- **Connects hardware, software, and data end to end:** the
  [[dengue-crt-wearable]] system spans a pneumatic rig, an imaging
  pipeline, a web study tool, Supabase, and a Streamlit dashboard.
- **Rigour in research framing:** scoping decisions around patents,
  correctly attributing which paper owns which technical claim, stating
  limitations openly (see [[dengue-crt-wearable]]).
- **Systematic outreach and vetting:** researches companies before
  contacting them, tailors messages per channel, chains referrals, and
  checks unfamiliar postings for scams before applying (see
  [[career-and-interview-prep]]).
- **Portfolio/documentation instinct:** LinkedIn entries, GitHub repos,
  design specs, and this vault itself.
- **Structural problem-solving:** when a 2-layer PCB couldn't route, the
  fix was moving to 4 layers rather than fighting the layout (see
  [[esp32-robot-controller-pcb]]) — fixing root causes structurally
  rather than patching around them.
- Adapts under failure without apparent stalling: 2-layer → 4-layer,
  single-layer → smaller 2-layer, Excel-based tool → Supabase+Streamlit.
  Rejects a flawed design and states exactly why (e.g. the smart-plug
  gate-default issue in [[smart-timer-plug]]) rather than accepting a
  "close enough" fix.

## Growth areas to watch
- **Breadth vs. depth:** working across many domains is a strength, but
  risks shallow mastery everywhere. A useful direction: keep the
  multidisciplinary range, but establish a few deep pillars — e.g.
  embedded systems + edge AI + hardware/sensing as a core specialization.
- **Moving fast vs. planning:** strong bias toward a working prototype
  quickly; sometimes worth slowing down for requirements, architecture,
  datasheets, electrical limits, and failure modes before building, to
  avoid downstream rework.
- **Fragmented knowledge:** work spans many chats, code files,
  screenshots, and hardware, which risks losing reasoning over time — the
  all-of-me vault itself is the fix for this.
- **"What works" before "why":** getting to a working system is
  prioritized (good for prototyping); worth periodically going back to
  ask why it worked, what the limitations are, what happens at edge
  cases, and whether it can be explained without AI assistance.
- **Rushed communication under time pressure:** messages can get
  compressed/abbreviated when excited or troubleshooting quickly — intent
  is usually still clear from context, so read for meaning over exact
  wording in those moments.
- **Trusting his own reasoning before seeking confirmation:** in at least
  one recorded area (AI-course conceptual questions), his own reasoning
  was already correct before he checked it with AI.
- **Finishing details on parallel deliverables:** some outputs have known
  placeholders (e.g. MATLAB screenshots pending in a lab report, unclosed
  Results/Discussion sections and an unresolved threshold-generalization
  question in [[dengue-crt-wearable]]) — starting outpaces finishing on
  some threads.
- **Version-control fluency:** has confused `git pull` (receiving
  collaborator commits) with `git push` (sending own commits) at least
  once — see [[technical-lessons-learned]].
- **Verifying claims before writing them down:** the research paper's
  core novelty claim needed checking against prior work (Q-CRT,
  Shinozaki, Blaxter) before it could be asserted — a reminder to verify
  novelty/uniqueness claims before they go in a draft.

## Suggested deeper-skill targets (from the source profile)
- Embedded fundamentals: C, memory, pointers, interrupts, timers, DMA,
  ADC, PWM, UART, SPI, I2C, RTOS concepts, debugging.
- Pick one or two MCU ecosystems to go deep on (e.g. STM32 + ESP32),
  keeping Arduino/PIC/Raspberry Pi as supporting knowledge.
- Embedded Linux on Raspberry Pi (processes, threads, networking, device
  interfaces, edge AI deployment).
- Edge AI: model optimization, quantization, TinyML, ONNX, TensorFlow
  Lite/Lite Micro, inference latency, memory constraints — directly
  aligned with [[thermalflow]].
- Analog electronics depth: signal conditioning, filters, op-amps, ADC
  behavior, noise, grounding, power integrity.
- PCB depth: stackups, controlled impedance, EMI/EMC, ground return
  paths, decoupling, power integrity, high-speed routing, DFM/DFA.
- System architecture discipline: requirements → architecture →
  interfaces → subsystems → testing → integration, before jumping to
  the build.

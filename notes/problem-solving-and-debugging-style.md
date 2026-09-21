---
type: note
title: Problem-Solving, Coding & Debugging Style
status: ongoing
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [learning-style, debugging, coding, workflow]
links: [[[engineering-design-philosophy]], [[self]]]
---

# Problem-Solving, Coding & Debugging Style

## How a new problem usually starts
Not from a formal spec. Typical flow: "I have this idea" → "Can I do
this?" → "What component can do it?" → "How do I connect it?" → "Give me
the code" → "Is this correct?" → "It works" → "How do I improve it?" →
"How do I present it?" — build-first, discover-through-doing, get one
small part working before the whole system (sensor → read → understand →
connect MCU → process → filter → control → AI → integrate).

## How code gets started and explained
Starts from a desired behavior ("I want X to happen, how do I code it?"),
thought of as input → read → process → decision → output. Wants code to
have a visible purpose per part (e.g. "this reads the sensor so we don't
repeat that code") rather than architecture-for-its-own-sake.

Preferred explanation order: working code first → explain the important
sections → explain what happens at runtime → explain how to modify it.
Not a line-by-line walkthrough before seeing it run.

## How technical answers land best
Simple → exact → practical, structured as: what is it? → why use it? →
what physically happens? → simple example → how it applies to the
current project. Reach for the textbook-depth version only after the
simple version lands.

## How a difficult problem gets entered
Starts from the visible symptom, not the theoretical root cause (e.g.
"the LED isn't working" → power? → pin? → GPIO config? → is code running?
→ is the board programmed? → active-high/low?). This turns "nothing
works" into "which layer is failing" — treat each report as elimination
of one layer, not a restart of diagnosis.

## System decomposition
Naturally reasons in physical block diagrams (sensor → MCU → processing
→ detection → output), e.g. ThermalFlow's
thermal sensor → ESP32 → processing → human detection → occupancy →
control, or the microscope's
motor → stage → microscope → image → Python → YOLO → count.

## Debugging cycle
Build → run → observe → report result → adjust → run again, with
frequent real-time updates ("now the LED is on", "Wi-Fi works but USB
doesn't"). Each new observation should narrow the diagnosis, not restart
it.

## Decision-making on components/approaches
Balances: can I build it? + is it available? + is it affordable? + does
it solve the problem? + can I demonstrate it? + can I explain it? — the
theoretically ideal component is not chosen if it's too expensive, hard
to source, or overcomplicated for the prototype.

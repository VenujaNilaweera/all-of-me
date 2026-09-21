---
type: project
title: Flowrail / Axon (Node-Based Workflow Canvas)
status: in-progress
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [web, ui-design, workflow-automation, collaboration]
links: []
---

# Flowrail / Axon

n8n-inspired node-based workflow canvas app. "Axon" is the leading name.

## Prototypes
Two HTML prototypes; `flowrail2.html` has icon-first square nodes,
distinct silhouettes, animated runs (progress ring then a travelling
light dot along wires), and brand nodes for Airtable, WhatsApp, LinkedIn,
Gmail.

## Process
A `DESIGN_SPEC.md` was written for handoff to Claude Code. A collaborator
committed files to a shared Git repo.

## Lesson learned
Progress-ring background tracks on square nodes render as filled shapes
covering the icons; circles avoid this. Documented to prevent
regression.

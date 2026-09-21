---
type: note
title: Technical Lessons Already Learned (Don't Re-Teach)
status: ongoing
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [lessons-learned, pcb, git, altium, esp32, supabase]
links: [[[pcb-and-power-electronics]], [[confirmed-toolbox]]]
---

# Technical Lessons Already Learned

Confirmed lessons from past work — don't re-explain these from scratch.

- Isolate motor/servo power from the MCU logic rail to avoid
  current-spike damage.
- 4-layer stackups solve routing congestion that 2-layer boards can't.
  Keep GND return paths continuous for EMI. Avoid 90-degree bends (acid
  traps, impedance discontinuities).
- Schottky diode-OR is the standard dual-input power combining method.
- USB 2.0 on USB-C: tie both D+ pins (A6/B6) and both D- pins (A7/B7).
  CC1/CC2 need 5.1k pull-downs in device mode.
- **Altium specifics:** stack symmetry lives in the Properties panel when
  the Stackup document is active. Internal plane net assignment uses the
  Split Plane dialog. PCB Editor Defaults govern manual vias separately
  from the Routing Via Style rule. The checkerboard net colour is a
  visual highlight, not a DRC error.
- A non-logic-level MOSFET (e.g. IRFZ44N) needs a real gate drive, not a
  direct 3.3V GPIO connection.
- **Supabase + ESP32:** polling beats Realtime WebSockets; use the
  two-row pattern for bidirectional sync (see [[connected-lamp]]).
- **Git:** `git pull origin main` receives collaborator commits; pushing
  sends your own — these have been confused before, double-check
  direction.
- **RPi.GPIO:** BCM numbering is the standard; incomplete try/except
  blocks are a common syntax pitfall.
- **LaTeX:** the Springer `sn-jnl` class failed in a blank Overleaf
  project (missing `.cls` files) — plain `article` works as a fallback.
- **CRT literature:** the 90% light-intensity threshold is Q-CRT's;
  DiCART uses a 50% cumulative-gradient rule (see
  [[dengue-crt-wearable]]).

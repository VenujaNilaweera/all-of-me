---
type: note
title: Engineering Corrections Ledger
status: ongoing
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [rules, corrections, engineering, checklist]
links: []
---

# Engineering Corrections Ledger

Rules that came out of real errors caught in past work. Re-check these
before submitting anything.

## Cost estimation — verify table totals
- **Trigger:** total in a project cost estimation table was wrong.
- **Rule:** manually re-verify calculated totals in every cost table.

## Inverter terminology — CSI / VSI
- **Trigger:** confusion between electrical and materials-science usage.
- **Rule:** in this domain, `CSI` = Current Source Inverter and
  `VSI` = Voltage Source Inverter. Never refer to these as semiconductor
  materials.

## All-pass filters — alpha is not −3
- **Trigger:** an algebraic error where alpha was calculated as −3.
- **Rule:** re-verify the fundamental properties of all-pass filters
  during the calculation. Alpha is not −3.

## Computer architecture — do not assume base CPI = 1
- **Trigger:** a problem did not state a base CPI.
- **Rule:** do not assume base CPI = 1 unless it is explicitly given in
  the problem constraints. Ask or state the assumption.

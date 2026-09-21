---
type: project
title: Wearable Early Detection of the Dengue Critical Phase (Final-Year Research)
status: in-progress
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [research, biomedical, wearable, crt, ppg, esp32, altium, final-year]
links: [[[self]], [[crt-perception-study-tool]]]
---

# Wearable Early Detection of the Dengue Critical Phase

Main final-year research project. Automated Capillary Refill Time (CRT)
measurement combined with PPG, skin temperature, and blood pressure
sensing, aimed at early detection of the dengue critical phase.

## Team
T.H.V.K. Nilaweera (corresponding author) and B.P.H. Liyanage.

## Supervisors
Prof. Tharmarajah Thiruvaran (EEE, Jaffna), Dr. Neethan Ratnakumar
(Mechanical Eng, Jaffna), Dr. Gayana P.S. Gunaratna (Medical
Microbiology, Kelaniya).

## System components
- **Pneumatic CRT module:** Arduino-controlled MOSFET array, pump plus
  solenoid, negative-pressure reservoir, glycerin-filled syringe actuator
  fingertip platform with automated finger-placement guidance.
- **CIELAB colour-recovery imaging pipeline:** LAB conversion, smoothing,
  watershed segmentation, ellipse ROI refinement, a* channel extraction,
  da*/dt curve.
- **Nail ROI detection (`ROI_blanch.py`, Python/OpenCV):** 10-step
  pipeline — LAB a* extraction, temporal change mapping (peak-minus-valley
  swing), GMM clustering with MRF/ICM spatial denoising, morphological
  cleanup, nail-box location priors, single-blob reduction,
  persistence-based stable ellipse fit.
- **Measurement stage (two-pass design):** Run 1 refines the ROI
  (hot-core amplitude threshold, motion gating, stability checks, human
  confirmation) and caches it to JSON. Run 2 loads the cache, extracts
  mean a* per frame, plots a* vs. time with EMA smoothing plus a slope
  (refill rate) curve, exports CSV and PNG. Curve shape compared
  favorably against the Q-CRT paper's curve.
- **Wearable module:** MAX30102 PPG sensor, dual axillary temperature
  sensors.
- **Custom ESP32 PCB** designed from scratch in Altium as part of the
  system.

## Core research contribution
Derive the automated CRT threshold from aggregated clinician perception
consensus instead of fixed engineering rules — targeting the poor
clinical agreement (ICC 0.46) reported in the DiCART validation study
(Descamps et al., 2025, J Clin Monit Comput).

## Scoping decision
The paper covers only software, colour analysis, and the perception
study. The fully automated pneumatic clip mechanism is deliberately
excluded to preserve patent options; patent-before-publication timing
risk should stay in view.

## Factual care points (do not get these wrong)
- The "90% light-intensity threshold" belongs to **Q-CRT**, not DiCART
  (DiCART uses a **50% cumulative-gradient** rule).
- Screen colour calibration and video mediation are real, stated
  limitations.
- The reaction-time reframing argument is strong but needs careful
  wording.

## Paper status
LaTeX skeleton (article class, authblk, natbib unsrtnat) compiles in
Overleaf. The Springer `sn-jnl` class failed in a blank Overleaf project
(missing `.cls` files) — plain `article` is the reliable fallback.
Targeting Springer-class journals (e.g. J Clin Monit Comput). Introduction,
Related Work, and Methods 4.1-4.6 are drafted; Results, Discussion, and
Conclusion are open.

## Open decisions
- How to generalize the consensus threshold (absolute delta a*, percent
  of max, or percent of gradient).
- Whether supervisors are co-authors or acknowledged.
- Verifying the "no prior automated CRT system derives its threshold
  from clinician perception" claim against Q-CRT, Shinozaki, and Blaxter.
- Patent filing timing relative to publication.

Used an outside draft review (z.ai) to cross-check framing.

## Open validation items (from measurement pipeline)
- Extract a quantitative refill-time number.
- Check that EMA smoothing isn't flattening the two-phase recovery.
- Test reproducibility across clips.

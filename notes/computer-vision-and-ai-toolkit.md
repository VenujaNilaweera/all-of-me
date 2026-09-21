---
type: note
title: Computer Vision & AI Toolkit
status: ongoing
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [yolo, opencv, pytorch, ai, computer-vision, ollama, gpu]
links: [[[breast-cancer-ai-classifier]], [[parasite-egg-detection]]]
---

# Computer Vision & AI Toolkit

## Core libraries/frameworks
- YOLO, especially YOLOv8 — breast cancer classification, parasite/worm
  egg detection, headset detection, other object-detection experiments.
- OpenCV — image/video processing, camera input, detection pipelines,
  preprocessing, visualization.
- pytesseract — OCR.
- PyTorch, Ultralytics.
- NumPy, pyautogui, pygame, pyserial, Streamlit, CustomTkinter, PyQt5.

## GPU / CUDA setup
- Laptop GPU: NVIDIA GeForce RTX 3050, 6 GB.
- Has dealt with CUDA/PyTorch/torchvision version mismatches, driver
  issues, `nvcc` not found in PATH.
- Observed at one point: NVIDIA driver 572.60, CUDA 12.8.
- YOLO inference benchmark observed: ~115.7 ms/image at input size
  (1, 3, 480, 640).

## Local AI (Ollama)
Explored running models locally for offline/local AI (ties into the
ThermalFlow "local processing" philosophy). Tried Gemma-class model
(~7.2 GB download); wanted to store models on a secondary D: drive rather
than the primary drive, considered a symlink/env-var approach.

## GUI frameworks used
Streamlit (AI classifiers, Grad-CAM demos), CustomTkinter, PyQt5, Pygame
(thermal visualization).

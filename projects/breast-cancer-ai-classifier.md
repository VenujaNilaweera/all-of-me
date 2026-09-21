---
type: project
title: Breast Cancer AI Classifier
status: in-progress
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [yolo, pytorch, streamlit, grad-cam, biomedical, ai]
links: [[[self]]]
---

# Breast Cancer AI Classifier

Deep-learning classifier for breast cancer using YOLOv8.

## Dataset & model
- ~690 images.
- Trained model: `best.pt`.

## Hardware
NVIDIA GeForce RTX 3050 Laptop GPU (6 GB) used for training/inference.

## Software
Python, PyTorch, Ultralytics YOLOv8, OpenCV, Streamlit.

## Interface & explainability
A Streamlit GUI was built for the classifier, including Grad-CAM
visualization so predictions are visually explainable, not just a raw
output.

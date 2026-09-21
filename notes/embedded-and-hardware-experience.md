---
type: note
title: Embedded Platforms & Hardware Experience
status: ongoing
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [embedded, arduino, esp32, stm32, pic, raspberry-pi, uart, motors, sensors]
links: []
---

# Embedded Platforms & Hardware Experience

## Boards used/studied
Arduino Uno, Nano, Pro Mini; ESP32, ESP32-C3, ESP8266; STM32 Black Pill,
STM32G071; PIC microcontrollers; Raspberry Pi, Raspberry Pi Zero 2 W.

## Arduino
Sensor reading, motor/servo control, serial communication, microscope
automation, analog sensing.

## ESP32
Wi-Fi, sensor processing (ThermalFlow, capacitive sensing), embedded/edge
AI, GPIO, ADC, touch sensing, serial communication.

## ESP32-C3 notes
Explored pin availability, GPIO limits, UART pins, USB/serial behavior,
capacitive touch. One dev board: Wi-Fi worked but USB printing had
issues — suspected damaged Type-C port.

## STM32
STM32 Black Pill and STM32G071 — GPIO config, LED control, embedded C.
Exercise: configuring PB8 as output to drive an LED.

## PIC
Studied with MPLAB; GPIO, timers, interrupts; built a beginner traffic-
light project in embedded C.

## Raspberry Pi
Raspberry Pi Zero 2 W explored for Python/OpenCV/YOLO, microscope image
acquisition, AI inference, data logging. Known limitation: no built-in
analog input — needs a paired ADC-capable device (e.g. Arduino Nano)
feeding values over serial. SD card sizes considered: 32/64/128 GB.

## UART / serial communication
Mental model: UART sends data bit-by-bit between devices via TX/RX pins
at an agreed baud rate. Used for Arduino↔Python, Arduino↔Raspberry Pi,
ESP32 debugging, sensor data transmission, microscope control.

## Motors and motion control
- Stepper motors: NEMA 17 + A4988 driver, AccelStepper library (used in
  microscope stage automation).
- Servo motors: 180° and 360° continuous-rotation types; PWM position
  control; potentiometer input; investigated a servo startup-jump issue,
  addressed with `servo.writeMicroseconds(position)` set before/around
  attach.
- DC geared motors + lead screws (active suspension wheelchair).

## Sensor experience
- Thermal: AMG8833 (8x8), MLX90641 (16x12), MAX6675.
- Environmental: AHT10.
- Inertial: MPU6050.
- Current: ACS712 20A/30A; also looked at Hall-effect sensors for ~3A.
- Capacitive: ESP32 touch, copper electrodes, CD4051 experiments.
- Position/motion: potentiometers, encoders, servo feedback.

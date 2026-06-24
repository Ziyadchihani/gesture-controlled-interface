# Gesture-Controlled Presentation Interface

## Overview

A real-time computer vision project that allows users to control presentation slides using hand tracking and swipe gestures. The system uses a webcam to detect hand landmarks, analyze motion vectors, and convert swipe movements into presentation commands.

## Features

* Real-time hand tracking
* Swipe gesture detection
* Presentation slide navigation
* Motion vector analysis
* Keyboard automation using PyAutoGUI

## Technologies

* Python 3.11.9
* OpenCV 4.9.0.80
* MediaPipe 0.10.14
* NumPy 1.26.4
* PyAutoGUI 0.9.54
* SciPy 1.13.1
* Matplotlib 3.9.0
* Pandas 2.2.2

## Project Structure

```text
gesture-controlled-presentation/
│
├── src/
│   ├── hand_tracker.py
│   ├── presentation_controller.py
│   └── swipe_detector.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Environment Setup

Create a new environment:

```bash
conda create -n gesture_robot python=3.11.9
conda activate gesture_robot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Development Phases

### Phase 4: Gesture-Based Presentation Controller

Objective:
Convert recognized hand gestures into presentation commands.

Controls:

* Open Palm → Start Presentation (F5)
* Fist → Exit Presentation (ESC)
* Index Finger → Next Slide
* Peace Sign → Previous Slide

Algorithms:

* MediaPipe hand landmark detection
* Finger state extraction
* Rule-based gesture classification
* Gesture-to-command mapping
* Keyboard automation using PyAutoGUI

Workflow:

Camera
→ Hand Detection
→ Landmark Extraction
→ Gesture Recognition
→ Presentation Command

---

### Phase 5: Swipe-Based Controller (Final Version)

Objective:
Replace static gesture control with motion-based interaction.

Controls:

* Swipe Right → Next Slide
* Swipe Left → Previous Slide
* Swipe Up → Start Presentation
* Swipe Down → Exit Presentation

Algorithms:

* Real-time hand tracking
* Motion vector calculation
* Direction classification
* Event-based swipe detection

Workflow:

Camera
→ Hand Tracking
→ Motion Analysis
→ Swipe Detection
→ Presentation Command


## System Workflow

```text
Webcam
   ↓
Frame Capture
   ↓
MediaPipe Hand Detection
   ↓
Hand Landmark Extraction
   ↓
Motion Vector Calculation
   ↓
Swipe Detection
   ↓
Presentation Command Execution
```

## Motion Vector Analysis

The system calculates hand movement using:

```text
dx = x_current - x_previous
dy = y_current - y_previous
```

Direction is determined by comparing horizontal and vertical displacement.

```text
dx > 0  → Swipe Right
dx < 0  → Swipe Left
dy > 0  → Swipe Down
dy < 0  → Swipe Up
```

## Running the Project

```bash
python main.py
```

## Controls

```text
Swipe Right  → Next Slide
Swipe Left   → Previous Slide
Swipe Up     → Start Presentation
Swipe Down   → Exit Presentation
```

## Future Improvements

* Motion smoothing
* Multi-hand support
* Kalman filtering
* Robot control integration
* ROS integration
* Deep learning based gesture recognition

## Learning Outcomes

This project demonstrates:

* Computer Vision
* Real-Time Processing
* Human-Computer Interaction (HCI)
* Motion Tracking
* Vector Mathematics
* NumPy Operations
* Python Development
* Software Architecture

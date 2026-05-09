## AI-Powered Vehicle Damage Detection
- Student: Milagros Pumasupa Terán  
- Course: ITAI 1378 – Computer Vision & AI  

## Tier Selection

Tier 2 – Object Detection
This project uses deep learning for object detection to automatically identify and classify vehicle damage (dents, scratches, broken lights, etc.) in images.  
It involves dataset preprocessing, model training, evaluation, and deployment for automated inspection workflows, making it more advanced than a basic proof-of-concept (Tier 1) but not requiring large-scale production or multiple AI modules (Tier 3).

## Project Overview

This project develops an AI-powered system capable of detecting vehicle damage from images using deep learning and computer vision techniques. The system identifies damaged areas such as dents, broken lights, and cracked windshields.

The goal is to automate vehicle inspection processes for applications such as insurance claims, fleet management, and repair services.

---

## Problem Statement

Manual vehicle damage inspection is time-consuming and often subjective. Insurance companies and repair shops rely on human inspection, which can lead to inconsistencies and delays.

An automated system using computer vision can improve the efficiency and accuracy of vehicle damage assessment.

---

## Solution

This project uses a deep learning object detection model to automatically identify damaged areas in vehicle images.

The model detects different types of vehicle damage and highlights the damaged regions using bounding boxes.

---

## Technologies Used

- Python
- PyTorch
- YOLOv8
- OpenCV
- Streamlit

---

## Dataset

- Dataset used: Automobile Damage Detection Dataset

- Source: Roboflow Universe

- Images: ~6,900 annotated images

- Link: https://universe.roboflow.com/automobile-damage-detection

The dataset contains labeled images with bounding boxes indicating different types of vehicle damage.

---

## Model

- Object detection model: YOLOv8

The model is trained using transfer learning and fine-tuned on the vehicle damage dataset.

---

## Metrics

### Primary Metric
- **Detection Accuracy ≥ 85%**

### Secondary Metrics
- **Damage Classification Accuracy ≥ 80%**
- **Inference Time < 1 second per image**

These metrics evaluate the model’s ability to accurately detect and classify vehicle damage while maintaining fast inference performance suitable for real-world applications.

---

## Resources Needed

### Compute
- **Google Colab GPU**

### Frameworks
- PyTorch
- Ultralytics YOLO
- OpenCV

### Estimated Cost
- **$0** (using free cloud GPU resources)

## Risks & Mitigation

| Risk | Probability | Mitigation |
|-----|-------------|------------|
| Dataset too small | Medium | Use alternative datasets from Roboflow |
| Low model accuracy | Medium | Apply data augmentation or fine-tune a larger YOLO model |
| Training too slow | Medium | Use Google Colab GPU for faster training |

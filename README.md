<a name="readme-top"></a>
<div align="center">
  <a href="https://github.com/JakeCherian/Paddle-OCR">
  </a>

<h3 align="center">The Gesture-Controlled Robotic Arm</h3><br>
</div>

## Introduction

GestureArm is an innovative project that integrates computer vision, machine learning, and robotics to create a highly responsive gesture-controlled robotic arm. This system demonstrates the potential of intuitive human-machine interfaces in the field of robotics and automation.

## Key Features

- Real-time hand tracking and gesture recognition using OpenCV and the HandTrackingModule
- Precise control of a 4-motor robotic arm through natural hand movements
- Arduino-based motor control system for smooth and accurate arm movements
- Customizable gesture-to-command mapping for versatile applications

## Technology Stack

This project showcases the seamless integration of:

1. **Computer Vision**: Utilizes OpenCV for real-time video processing and hand detection
2. **Machine Learning**: Employs advanced hand tracking algorithms for accurate gesture recognition
3. **Embedded Systems**: Arduino-based control system for translating gestures into motor commands
4. **Robotics**: A 4-DOF (Degree of Freedom) robotic arm for demonstrating the practical application of gesture control

## Applications

GestureArm serves as both a practical demonstration of gesture-based interfaces and a platform for further research and development in human-robot interaction. It offers potential applications in various fields, including:

- Industrial automation
- Assistive technologies
- Educational robotics

<!-- ABOUT THE PROJECT -->
## System Operation and Control Flow

The GestureArm system operates through a sophisticated integration of computer vision, sensor processing, and mechanical control systems. Here's a detailed look at how the system functions:

### Hand Detection and Tracking

The system utilizes OpenCV and HandTrackingModule for real-time hand detection and tracking through a webcam feed. When a user moves their hand, the system captures and processes these movements across three primary dimensions:

1. Horizontal positioning
2. Vertical positioning
3. Distance from the camera

### Movement Control Mechanisms

The robotic arm's movement is controlled through four distinct mechanisms:

1. **Horizontal Control**: Determined by tracking the hand's position relative to predefined left and right regions of the camera frame.
2. **Vertical Control**: Achieved by monitoring the hand's position against top and bottom thresholds.
3. **Distance-Based Movement**: Calculated using the spatial relationship between the wrist and index fingertip coordinates.
4. **Gripper Control**: Activated through fist detection - when all fingers are closed, the gripper closes, and when opened, the gripper releases.

### Gesture-to-Motor Translation

The system translates these gestures into precise servo motor commands through an Arduino microcontroller:

- Each motor operates independently, allowing for simultaneous control of multiple joints.
- The Arduino receives commands through serial communication and maps them to appropriate PWM signals for the servo motors.
- This setup enables fluid, natural movement that mimics the user's hand gestures, making it particularly effective for pick-and-place operations and precise positioning tasks.

### System Stability and Safety

The implementation includes built-in safeguards and smoothing algorithms to ensure stable movement and prevent sudden jerks or unsafe positions:

- The system continuously monitors the hand's position and updates motor positions only when significant changes are detected.
- This helps maintain smooth operation and reduce motor wear.
- Safety limits are implemented in software to prevent the arm from moving into unsafe positions.

This comprehensive approach allows GestureArm to provide an intuitive and responsive interface between human gestures and robotic arm movements, opening up new possibilities in human-robot interaction.


## Visual Reference Of The Robotic Arm
### Image 1

 <div class="image-container">
       <img src="Robotic Arm 1.jpg" alt="Logo" width="300" height="450"> 
    </div>

### Image 2

 <div class="image-container">
       <img src="Robotic Arm 2.jpg" alt="Logo" width="300" height="450"> 
    </div>
### Circuit Diagram
 <div class="image-container">
       <img src="Robotic Arm 2.jpg" alt="Logo" width="300" height="450"> 
    </div>

## Conclusion
In conclusion, this model provides a highly effective solution for extracting text from images, combining image enhancement techniques with the robust capabilities of PaddleOCR. By improving image clarity through sharpness adjustments and resizing, it ensures higher OCR accuracy, making it ideal for handling challenging inputs like low-resolution or blurry images. The integration of confidence scores and visual bounding boxes offers users greater control and validation over the text detection process. Overall, this model is a versatile tool for automating text recognition in various domains, from document processing to data extraction.

Project Link:  [https://github.com/JakeCherian/Paddle-OCR](https://github.com/JakeCherian/Paddle-OCR)

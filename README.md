# 🔥 Autonomous Firefighting Robot (4WD) with Remote Control & AI Detection
An AI-powered four-wheel drive (4WD) firefighting robot capable of detecting and extinguishing fire in real-time using a YOLO-based deep learning model, IP camera vision, Firebase cloud integration, and a Kodular-built Android remote control application.

# 📌 Overview
This project integrates Robotics + IoT + Cloud + Computer Vision to build an intelligent fire response system.\\
The robot can:
  -Detect fire using a trained deep learning model
  -Stream live video via IP camera
  -Automatically activate a water spray pump
  -Be manually controlled through an Android app
  -Communicate using Firebase Realtime Database

# 🚀 Features
  -Real-time fire detection (YOLO custom model – best.pt)
  -IP camera live streaming
  -Confidence-based bounding box detection
  -Automatic relay-controlled spray pump activation
  -Manual movement control (Forward / Backward / Left / Right)
  -Firebase-based cloud communication
  -ESP32 WiFi-enabled controller
  -Servo-controlled spray direction

# 🏗️ System Architecture
🔹 Autonomous Detection Flow
      IP Camera → Python Detection Script → YOLO Model → Fire Detected → Relay Activation → Water Spray
🔹 Manual Control Flow
      Android App (Kodular) → Firebase → ESP32 → Motor Driver / Relay / Servo
 Both systems operate in parallel to allow hybrid control (AI + Manual).

# 🧠 Fire Detection Model
Framework: PyTorch
Model: Custom-trained YOLO
Training: FireDetectionModelTraining.ipynb
Inference Scripts:
    WebcamFireDetection.py
    IPCameraFireDetection.py
    ImageFireDetection.py
    RobotAutomation.py
Detection Output:
    Bounding box around fire
    Confidence score (e.g., 82%)
    Fire spot count

#🔌 Hardware Components
  ESP32 (WiFi-enabled microcontroller)
  L298N Motor Driver
  4 DC Motors (4WD chassis)
  Relay Module
  Water Pump
  Servo Motor (Nozzle control)
  IP Camera
  12V Battery Supply

⚙️ Software Stack
  Python
  PyTorch
  OpenCV
  Arduino IDE
  Firebase Realtime Database
  Kodular (Android App Development)

# 📁 Project Structure
├── Arduino/
│   ├── AppConnection.ino
│   ├── FirebaseConnection.ino
│   └── movements.ino
│
├── AI/
│   ├── FireDetectionModelTraining.ipynb
│   ├── best.pt
│   ├── WebcamFireDetection.py
│   ├── IPCameraFireDetection.py
│   ├── ImageFireDetection.py
│   └── RobotAutomation.py
│
├── Circuit Diagram.pdf
├── BlockDiagram.png
└── README.md

# 🎯 Applications
  -Industrial fire safety systems
  -Warehouse monitoring
  -Hazardous zone fire response
  -Academic robotics projects
  -Smart automation systems

# 🔮 Future Improvements
  -Obstacle avoidance
  -Thermal camera integration
  -Edge AI deployment on embedded device
  -Autonomous navigation with SLAM
  -Mobile push notifications
  -GPS integration

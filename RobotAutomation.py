from inference_sdk import InferenceHTTPClient
import cv2
import time
import pyrebase

# Initialize Inference Client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="DHpVOReN2oujyTpBbtz8"
)

# Firebase Configuration
firebaseConfig = {
    "apiKey": "AIzaSyB9xtt75npL-6n_pvQ3yGXM4aZTYWpp0No",
    "authDomain": "agrobot-61736.firebaseapp.com",
    "databaseURL": "https://agrobot-61736-default-rtdb.firebaseio.com/",
    "storageBucket": "agrobot-61736.appspot.com"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# RTSP URL of the IP Camera
rtsp_url = "rtsp://testing:123456@192.168.1.14:554/stream2"

# Open IP camera stream using RTSP URL
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Error: Could not open RTSP stream.")
    exit()

# Variables to control Fire detection
pest_count = 0
detections = []

# Loop through IP camera frames
last_check_time = time.time()  # Track the time for checking 'Photo' every second

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame.")
        break

    current_time = time.time()

    # Check the value of 'Photo' every second
    if current_time - last_check_time >= 1:  # Check every 1 second
        last_check_time = current_time

        # Retrieve the 'Photo' value from Firebase to decide whether to apply prediction
        photo_value = db.child("Photo").get().val()

        if photo_value == 1:
            # Save frame as temporary image for inference
            temp_path = "temp_frame.jpg"
            cv2.imwrite(temp_path, frame)

            # Perform inference
            result = CLIENT.infer(temp_path, model_id="fire_detection-d5jqa/3")

            # Update fire count and detections
            detections = result.get("predictions", [])
            pest_count = len(detections)

            # Upload fire count to Firebase database
            db.child("Count").set(pest_count)

            # After prediction, set Photo = 0 in Firebase to stop continuous predictions
            db.child("Photo").set(0)  # Reset Photo to 0 in Firebase to prevent continuous prediction

    # Draw bounding boxes with class names
    for detection in detections:
        x = int(detection['x'] - detection['width'] / 2)
        y = int(detection['y'] - detection['height'] / 2)
        w = int(detection['width'])
        h = int(detection['height'])

        # Draw rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Add class name and confidence
        class_name = detection['class']
        confidence = detection['confidence'] * 100
        label = f"{class_name} ({confidence:.1f}%)"

        # Calculate label position
        text_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]
        label_x = x + w - text_size[0] - 5  # Right-aligned text
        label_y = y + 20  # Slightly below the top edge

        cv2.putText(frame, label, (label_x, label_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display total Fire count at the bottom
    height, _, _ = frame.shape
    count_text = f"Total pests: {pest_count}"
    cv2.putText(frame, count_text, (10, height - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Show the frame
    cv2.imshow("Fire Detection", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

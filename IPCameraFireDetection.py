from inference_sdk import InferenceHTTPClient
import cv2
import time

# Initialize Inference Client
CLIENT = InferenceHTTPClient(
    api_url=" ",
    api_key=" "
)

# RTSP URL of the IP Camera
rtsp_url = " "

# Open IP camera stream using RTSP URL
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Error: Could not open RTSP stream.")
    exit()

# Variables to control inference timing
last_inference_time = 0
inference_interval = 5  # Perform inference every 5 seconds
fire_count = 0
detections = []

# Loop through IP camera frames
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame.")
        break

    current_time = time.time()

    # Perform inference every 5 seconds
    if current_time - last_inference_time >= inference_interval:
        # Save frame as temporary image for inference
        temp_path = "temp_frame.jpg"
        cv2.imwrite(temp_path, frame)

        # Perform inference
        result = CLIENT.infer(temp_path, model_id="fire_detection-d5jqa/3")

        # Update fire count and detections
        detections = result.get("predictions", [])
        fire_count = len(detections)

        last_inference_time = current_time

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

    # Display total fire count at the bottom
    height, _, _ = frame.shape
    count_text = f"Total fires: {fire_count}"
    cv2.putText(frame, count_text, (10, height - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Show the frame
    cv2.imshow("Fire Detection", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()


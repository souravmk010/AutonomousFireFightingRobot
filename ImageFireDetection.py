from inference_sdk import InferenceHTTPClient
import cv2
import numpy as np

# Initialize Inference Client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="DHpVOReN2oujyTpBbtz8"
)

image_path = "2.jpg"

# Perform Inference
result = CLIENT.infer(image_path, model_id="fire-vqbia/1")
print(result)

# Load the image
image = cv2.imread(image_path)

# Get image dimensions
height, width, _ = image.shape

# Extract detections and count them
detections = result.get("predictions", [])
firespot_count = len(detections)

# Draw bounding boxes with class names at the top-right corner
for detection in detections:
    x = int(detection['x'] - detection['width'] / 2)
    y = int(detection['y'] - detection['height'] / 2)
    w = int(detection['width'])
    h = int(detection['height'])

    # Draw rectangle
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Extract and clean class name
    class_name = "fire"  # Manually setting class name as "fire"
    confidence = detection['confidence'] * 100
    label = f"{class_name} ({confidence:.1f}%)"

    # Calculate the position for the label at the top-right inside the box
    text_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]
    label_x = x + w - text_size[0] - 5  # Right-aligned text
    label_y = y + 20  # Slightly below the top edge

    cv2.putText(image, label, (label_x, label_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

# Display total fire count at the bottom
count_text = f"Total firespot: {firespot_count}"
cv2.putText(image, count_text, (10, height - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# Save and display the result
cv2.imwrite("fire_detected.jpeg", image)
cv2.imshow("Firespot Detected", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the fire count in the terminal
print(f"Total Firespot detected: {firespot_count}")

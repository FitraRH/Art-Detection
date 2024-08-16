import torch
import ultralytics
import cv2
import os
from ultralytics import YOLO

# Verify the current working directory
print("Current working directory:", os.getcwd())

# Use the absolute path for the model file
model_path = r"C:\Users\Fitra\Downloads\anime art detection (medium)\anime art detection (medium)\anime art detection\runs\segment\train622\weights\best.pt"
if not os.path.exists(model_path):
    print(f"Model file not found at {model_path}")
else:
    print(f"Model file found at {model_path}")

# Load the model
model = YOLO(model_path)

print(cv2.getBuildInformation())

cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()

# Import required libraries
import os
import shutil
from ultralytics import YOLO
from roboflow import Roboflow
import torch
import cv2
import matplotlib.pyplot as plt

# Define dataset path in the current directory
dataset_path = os.path.join(os.getcwd(), "bike-helmet-detection")

# Check if dataset exists, if not, download it
if not os.path.exists(dataset_path):
    print("Downloading dataset...")
    rf = Roboflow(api_key="BBD2G9FeiQwalQaCZW9y")
    project = rf.workspace("bike-helmets").project("bike-helmet-detection-2vdjo")
    version = project.version(2)
    dataset = version.download("yolov8")
    shutil.move(dataset.location, dataset_path)
else:
    print("Dataset already downloaded.")

# Check for GPU availability
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f"Using device: {device}")

# Load YOLOv8 model
model = YOLO("yolov8n.pt")  # Using YOLOv8 nano model

# Train the model
model.train(data=f"{dataset_path}/data.yaml", epochs=50, batch=8, imgsz=640)

# Validate model performance
metrics = model.val()
print("Validation Results:", metrics)

# Perform real-time inference using OpenCV
cap = cv2.VideoCapture(0)  # Use webcam

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Perform detection
    results = model(frame)
    
    # Draw results on the frame
    for result in results:
        frame = result.plot()
    
    cv2.imshow("Helmet Detection", frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Export trained model
model.export(format="onnx")  # Export to ONNX format for deployment
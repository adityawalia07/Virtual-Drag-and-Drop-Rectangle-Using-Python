# Virtual-Drag-and-Drop-Rectangle-Using-Python

This project implements a virtual drag and drop system using computer vision and hand tracking.<br>
It allows users to interact with virtual rectangles on screen using their hand movements captured by a webcam.

## Features
  -Real-time hand tracking using OpenCV and cvzone<br>
  -Virtual rectangles that can be dragged and moved on screen<br>
  -Multi-rectangle support (currently set to 3 rectangles)<br>
  -Transparent overlay of virtual objects on the webcam feed<br><br>

## Technologies and Libraries Used
  -Python 3.x<br>
  -OpenCV (cv2): For capturing and processing video frames<br>
  -cvzone: A computer vision package that includes the HandTrackingModule<br>
  -NumPy: For numerical operations and array handling<br>
  -cvzone.HandTrackingModule: For hand detection and tracking<br>

## Requirements
  -Python 3.x<br>
  -OpenCV (cv2)<br>
  -cvzone<br>
  -NumPy<br>

## Installation
  -Clone this repository<br>
  -Install the required packages:<br>
  -Copypip install opencv-python cvzone numpy<br>


## How It Works
  -The script captures video from the default webcam.<br>
  -It uses the HandTrackingModule from cvzone to detect and track hands in the video feed.<br>
  -Three virtual rectangles are created on the screen.<br>
  -The program tracks the position of the user's index finger tip.<br>
  -When the index finger and middle finger are close together (distance < 30 pixels), it activates the "drag" mode.<br>
  -In drag mode, if the index finger tip is within a rectangle, that rectangle will follow the finger's movement.<br>
  -The virtual rectangles are rendered as semi-transparent overlays on the video feed.<br>

## Code Structure
  DragRect class: Represents a draggable rectangle with its position and size.<br>

## Main loop:
  -Captures video frames<br>
  -Detects hands and finger positions<br>
  -Updates rectangle positions based on hand gestures<br>
  -Renders the rectangles on the video feed<br>

## Usage
  -Run the script:<br>
  -Copypython Virtual_Drag_and_Drop.py<br>
  -Position your hand in view of the webcam.<br>
  -Pinch your index and middle fingers together to activate drag mode.<br>
  -Move your hand to drag the virtual rectangles.<br>
  -Press 'q' to quit the application.<br>

## Customization
  -Adjust the detectionCon parameter in the HandDetector initialization to change the hand detection sensitivity.<br>
  -Modify the colorR variable to change the color of the rectangles.<br>
  -Change the number of rectangles by modifying the range in the rectList initialization.<br>

## Future Improvements

  -Add ability to resize rectangles<br>
  -Implement different shapes (circles, triangles, etc.)<br>
  -Add gesture recognition for more interactions (e.g., rotate, scale)<br>
  -Improve performance for smoother interaction


# OUTPUT 

https://github.com/user-attachments/assets/4deb816d-38bb-46aa-b90d-a9dcb4eeebaf






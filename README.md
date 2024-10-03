# Virtual-Drag-and-Drop-Rectangle-Using-Python
This project implements a virtual drag and drop system using computer vision and hand tracking.<br>
It allows users to interact with virtual rectangles on screen using their hand movements captured by a webcam.<br>

## Features
Real-time hand tracking using OpenCV and cvzone
Virtual rectangles that can be dragged and moved on screen
Multi-rectangle support (currently set to 3 rectangles)
Transparent overlay of virtual objects on the webcam feed<br>

## Technologies and Libraries Used
Python 3.x
OpenCV (cv2): For capturing and processing video frames
cvzone: A computer vision package that includes the HandTrackingModule
NumPy: For numerical operations and array handling
cvzone.HandTrackingModule: For hand detection and tracking<br>

## Requirements
Python 3.x
OpenCV (cv2)
cvzone
NumPy<br>

## Installation
Clone this repository
Install the required packages:
Copypip install opencv-python cvzone numpy<br>


## How It Works
The script captures video from the default webcam.
It uses the HandTrackingModule from cvzone to detect and track hands in the video feed.
Three virtual rectangles are created on the screen.
The program tracks the position of the user's index finger tip.
When the index finger and middle finger are close together (distance < 30 pixels), it activates the "drag" mode.
In drag mode, if the index finger tip is within a rectangle, that rectangle will follow the finger's movement.
The virtual rectangles are rendered as semi-transparent overlays on the video feed.<br>

## Code Structure
DragRect class: Represents a draggable rectangle with its position and size.
### Main loop:

Captures video frames
Detects hands and finger positions
Updates rectangle positions based on hand gestures
Renders the rectangles on the video feed<br>

## Usage
Run the script:
Copypython Virtual_Drag_and_Drop.py
Position your hand in view of the webcam.
Pinch your index and middle fingers together to activate drag mode.
Move your hand to drag the virtual rectangles.
Press 'q' to quit the application.<br>

## Customization
Adjust the detectionCon parameter in the HandDetector initialization to change the hand detection sensitivity.
Modify the colorR variable to change the color of the rectangles.
Change the number of rectangles by modifying the range in the rectList initialization.<br>

## Future Improvements

Add ability to resize rectangles
Implement different shapes (circles, triangles, etc.)
Add gesture recognition for more interactions (e.g., rotate, scale)
Improve performance for smoother interaction

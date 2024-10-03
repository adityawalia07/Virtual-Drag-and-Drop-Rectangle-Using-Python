import cv2
import cvzone
import numpy as np
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1200)  # Set width
cap.set(4, 720)   # Set height
detector = HandDetector(detectionCon=0.8, maxHands=2)  # Confidence for detection
colorR = (255, 0, 255)

# Position and size for draggable rectangle
cx, cy, w, h = 100, 100, 200, 200

class DragRect():
    def __init__(self, posCenter, size=[100, 100]):  # Set smaller size here
        self.posCenter = posCenter
        self.size = size

    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size

        # If the index finger tip is in the rectangle region
        if cx - w // 2 < cursor[0] < cx + w // 2 and cy - h // 2 < cursor[1] < cy + h // 2:
            self.posCenter = cursor

rectList = []
for x in range(3):  
    rectList.append(DragRect([x * 200 + 150, 150]))

while True:
    success, img = cap.read()  # Capture frame
    img = cv2.flip(img, 1)  # Flip the image to mirror hands
    hands, img = detector.findHands(img, draw=False)  # Disable drawing

    if hands:
        # Extract the first hand's landmarks (there can be multiple hands)
        hand1 = hands[0]
        lmList = hand1['lmList']  # Landmark list of the first hand

        if len(lmList) >= 12:
            # Find the distance between the index finger (8) and middle finger (12)
            x1, y1 = lmList[8][:2]  # Get the x, y coordinates of index finger tip
            x2, y2 = lmList[12][:2]  # Get the x, y coordinates of middle finger tip
            l, _, _ = detector.findDistance((x1, y1), (x2, y2), img)  # Pass the coordinates as tuples

            if l < 30:
                cursor = lmList[8][:2]  # Index finger tip coordinates
                # Call the update here for all rectangles
                for rect in rectList:
                    rect.update(cursor)

    # Draw transparent rectangles
    imgNew = np.zeros_like(img, np.uint8)  # Create a transparent canvas
    for rect in rectList:
        cx, cy = rect.posCenter
        w, h = rect.size
        cv2.rectangle(imgNew, (cx - w // 2, cy - h // 2), (cx + w // 2, cy + h // 2), colorR, cv2.FILLED)
        cvzone.cornerRect(imgNew, (cx - w // 2, cy - h // 2, w, h), 20, rt=0)

    out = img.copy()
    alpha = 0.5
    mask = imgNew.astype(bool)
    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]

    # Display the final output
    cv2.imshow("Image", out)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()

import cv2
import serial
import time
from cvzone.HandTrackingModule import HandDetector

# Initialize serial communication
arduino = serial.Serial('COM5', 9600)  # Adjust COM port as necessary
time.sleep(2)  # Give the Arduino some time to reset

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set width
cap.set(4, 720)  # Set height

# Initialize hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Variables to store the movement commands
horizontal_command = "Center"
vertical_command = "Middle"
distance_command = "Hold"
fist_command = "Open"
previous_horizontal_command = ""
previous_vertical_command = ""
previous_distance_command = ""
previous_fist_command = ""

# Define regions
screen_width = cap.get(3)
screen_height = cap.get(4)
left_region = screen_width * 0.33
right_region = screen_width * 0.66

# Calculate the bottom-most point of the screen
bottom_y = screen_height

# Define region heights based on the bottom cell of a grid
cell_height = screen_height / 3

# Define the threshold for middle and top
middle_threshold = bottom_y - cell_height     # Bottom green line (this is the new reference)
top_threshold = middle_threshold - cell_height  # Top green line

# Loop for real-time hand detection
while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        lmList = hand['lmList']

        wrist_x, wrist_y = lmList[0][0], lmList[0][1]
        index_tip_x, index_tip_y = lmList[8][0], lmList[8][1]

        # Determine horizontal region (Motor 1)
        if wrist_x < left_region:
            horizontal_command = "Left"
        elif wrist_x > right_region:
            horizontal_command = "Right"
        else:
            horizontal_command = "Center"

        # Determine vertical region (Motor 2) based on the bottom green line
        if wrist_y > middle_threshold:  # Below the bottom green line
            vertical_command = "Bottom"
        elif wrist_y > top_threshold:   # Between the green lines (middle region)
            vertical_command = "Middle"
        else:                           # Above the top green line
            vertical_command = "Top"

        # Estimate distance (Motor 3)
        distance_value = ((index_tip_x - wrist_x) ** 2 + (index_tip_y - wrist_y) ** 2) ** 0.5
        if distance_value <= 300:
            distance_command = "Far"
        elif 300 < distance_value <= 400:
            distance_command = "Hold"
        else:
            distance_command = "Near"

        # Detect fist open/close (Motor 4)
        if detector.fingersUp(hand) == [0, 0, 0, 0, 0]:
            fist_command = "Close"
        else:
            fist_command = "Open"

        # Send commands if changed
        if horizontal_command != previous_horizontal_command:
            arduino.write(f"M1:{horizontal_command}\n".encode('utf-8'))
            previous_horizontal_command = horizontal_command

        if vertical_command != previous_vertical_command:
            arduino.write(f"M2:{vertical_command}\n".encode('utf-8'))
            previous_vertical_command = vertical_command

        if distance_command != previous_distance_command:
            arduino.write(f"M3:{distance_command}\n".encode('utf-8'))
            previous_distance_command = distance_command

        if fist_command != previous_fist_command:
            arduino.write(f"M4:{fist_command}\n".encode('utf-8'))
            previous_fist_command = fist_command

        # Display information on the image
        cv2.putText(img, f"M1: {horizontal_command}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img, f"M2: {vertical_command}", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img, f"M3: {distance_command}", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(img, f"M4: {fist_command}", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Draw lines to show regions
    cv2.line(img, (int(left_region), 0), (int(left_region), int(screen_height)), (0, 255, 0), 2)
    cv2.line(img, (int(right_region), 0), (int(right_region), int(screen_height)), (0, 255, 0), 2)
    cv2.line(img, (0, int(top_threshold)), (int(screen_width), int(top_threshold)), (0, 255, 0), 2)
    cv2.line(img, (0, int(middle_threshold)), (int(screen_width), int(middle_threshold)), (0, 255, 0), 2)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

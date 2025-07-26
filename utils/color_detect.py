import cv2
import numpy as np

def detect_colored_boxes(img_path):
    img = cv2.imread(img_path)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Yellow mask
    yellow_lower = np.array([20, 100, 100])
    yellow_upper = np.array([35, 255, 255])
    mask_yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)

    # Blue mask
    blue_lower = np.array([90, 50, 50])
    blue_upper = np.array([130, 255, 255])
    mask_blue = cv2.inRange(hsv, blue_lower, blue_upper)

    contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    result = []
    for cnt in contours_yellow:
        x, y, w, h = cv2.boundingRect(cnt)
        result.append({"box": [x, y, w, h], "color": "Yellow"})

    for cnt in contours_blue:
        x, y, w, h = cv2.boundingRect(cnt)
        result.append({"box": [x, y, w, h], "color": "Blue"})
    
    return result

import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)  # Corrected the case to match "Trackbars" consistently

# Creating the trackbars with the correct window name
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, empty)
cv2.createTrackbar("Val Min", "Trackbars", 0, 255, empty)
cv2.createTrackbar("Val Max", "Trackbars", 255, 255, empty)

while True:
    image = cv2.imread("images/lambo.png")
    if image is None:
        print("Error: Could not load image.")
        break

    # Correct color conversion from BGR to HSV
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Reading values from the trackbars
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")

    # Print values for debugging
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    # Define lower and upper bounds for mask
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Create mask and apply it to the HSV image
    mask = cv2.inRange(imgHSV, lower, upper)

    # Display original image, HSV-converted image, and mask
    cv2.imshow("Original Image", image)
    cv2.imshow("HSV Image", imgHSV)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

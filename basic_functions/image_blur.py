import cv2

image = cv2.imread("images/lambo.png")

imgBlur = cv2.GaussianBlur(image, (37,7), 0)

cv2.imshow("origianl", image)

cv2.imshow("output", imgBlur)

cv2.waitKey(0)
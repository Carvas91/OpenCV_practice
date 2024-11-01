import cv2

image = cv2.imread("images/lambo.png")

imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Output", imgGray)

cv2.waitKey(0)


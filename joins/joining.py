import cv2
import numpy as np

image1 = cv2.imread('images/cards.jpg')

print("image 1 shape:",image1.shape)

image1Resize = cv2.resize(image1, (318,159))

image2 = cv2.imread('images/image2.jpg')

print("image 2 shape:",image2.shape)

imageHorizontalStack = np.hstack((image1Resize,image2))

cv2.imshow("horizontal stack", imageHorizontalStack)

cv2.waitKey(0)
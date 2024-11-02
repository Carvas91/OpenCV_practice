import cv2
import numpy as np

image = cv2.imread('images/documentscanner2.jpg')

#Kernel
kernel = np.ones((5,5), np.uint8)

#setting the threshold
t_lower = 100
t_higher = 120

#apply canny edge

imgCanny = cv2.Canny(image, threshold1=t_lower, threshold2=t_higher)

#img dialation

imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)

#img erosion


imgErosion = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow('Original', imgCanny)

cv2.imshow("Dialates",imgDialation)

cv2.imshow('Eroded', imgErosion)

cv2.waitKey(0)
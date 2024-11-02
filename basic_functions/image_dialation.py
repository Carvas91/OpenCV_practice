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


cv2.imshow("original img",image)

cv2.imshow('Canny edge', imgDialation)

cv2.waitKey(0)
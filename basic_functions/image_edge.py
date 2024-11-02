import cv2

image = cv2.imread('images/documentscanner2.jpg')

#setting the threshold
t_lower = 100
t_higher = 120

#apply canny edge

edge = cv2.Canny(image, threshold1=t_lower, threshold2=t_higher)

cv2.imshow("original img",image)

cv2.imshow('Canny edge', edge)

cv2.waitKey(0)
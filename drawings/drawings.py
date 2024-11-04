import cv2
import numpy as np


image = np.zeros((512,512,3))

#Channels
image[:] = 255,0,0

#drawing a line

line = cv2.line(image, (0,0), (image.shape[1],image.shape[0]),(0,0,255),3 )

text = cv2.putText(line, "OpenCV Practice", (300,100), cv2.FONT_HERSHEY_COMPLEX, 1, (100,100,200), 5)

cv2.imshow('Output', text)


cv2.waitKey(0)

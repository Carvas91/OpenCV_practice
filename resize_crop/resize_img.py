import cv2

image = cv2.imread('images/image.jpg')

image_resize = cv2.resize(image, (1000,650))


cv2.imshow("output",image_resize)
cv2.waitKey(0)
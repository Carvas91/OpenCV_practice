import cv2

img = cv2.imread('images/lambo.png')

print("original shape", img.shape)

img_cropped = img[0:200, 200:500]

print("original shape", img_cropped.shape)

cv2.imshow("original", img)
cv2.imshow("cropped",img_cropped)

cv2.waitKey(0)
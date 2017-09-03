import numpy as np
import cv2

img = cv2.imread('image/1.jpg')
cv2.imshow('original', img)

subimg = img[100:200, 0:150]
cv2.imshow('cutting', subimg)

img[100:200, 150:300] = subimg

print(img.shape)
print(subimg.shape)

cv2.imshow('modified', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

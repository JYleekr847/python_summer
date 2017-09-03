import numpy as np
import cv2

img = cv2.imread('image/1.jpg')

b,g,r = cv2.split(img)

print(img[100,100])
print(b[100, 100], g[100,100], r[100,100])

cv2.imshow('blue channel', b)
cv2.imshow('green channel', g)
cv2.imshow('red channel', r)

cv2.waitKey(0)
cv2.destroyAllWindows()

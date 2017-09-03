import numpy as np
import cv2

img = cv2.imread('image/1.jpg')


B = img.item(340, 200, 0) # 340, 200 픽셀위치의 B 값
G = img.item(340, 200, 1) # G 값
R = img.item(340, 200, 2) # R 값

BGR = [B,G,R]
print(BGR)

print(img.shape)
print(img.size)
print(img.dtype)

# 에지 검출 - canny
import cv2
import numpy as np

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def canny(img, low_threshold, high_threshold):
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size):
    return cv2.GaussianBlur(img, (kernel_size,kernel_size), 0 )

image = cv2.imread('solidWhiteCurve.jpg')
height , width = image.shape[:2]

gray_img = grayscale(image)
blur_img = gaussian_blur(gray_img, 3)
canny_img = canny(blur_img, 60, 180)
canny_img2 = canny(image, 70, 210)

cv2.imshow('result', canny_img)
cv2.imshow('result2', canny_img2 )
cv2.waitKey(0)

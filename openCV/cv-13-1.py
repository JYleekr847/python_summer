import numpy as np
import cv2

def morph():
    img = cv2.imread('image/1.jpg')

    kernel = np.ones((3,3), np.uint8)

    erosion = cv2.erode(img, kernel, iterations=1)
    dilation = cv2.dilate(img, kernel, iterations=1)

    cv2.imshow('original', img)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
def morph2():
    img1 = cv2.imread('image/4.jpg')
    img2 = cv2.imread('image/5.jpg')

    kernel = np.ones((5,5), np.uint8)

    opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    cv2.waitKey(0)
    cv2.destroyAllWindows


morph2()

import numpy as np
import cv2

def morph():
    img1 = cv2.imread('image/alpha.jpg')
    img2 = cv2.imread('image/4.jpg')
    img3 = cv2.imread('image/5.jpg')

    kernel = np.ones((3,3), np.uint8)

    grad = cv2.morphologyEx(img1, cv2.MORPH_GRADIENT, kernel)
    tophat = cv2.morphologyEx(img2, cv2.MORPH_TOPHAT, kernel)
    blackhat = cv2.morphologyEx(img3, cv2.MORPH_BLACKHAT, kernel)

    cv2.imshow('grad', grad)
    cv2.imshow('tophat', tophat)
    cv2.imshow('blackhat', blackhat)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

morph()

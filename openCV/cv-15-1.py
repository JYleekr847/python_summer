#canny edge detection

'''
1단계 : 노이즈 제거
2단계 : Gradient 값이 높은 부분 찾기
3단계 : 최대값이 아닌 픽셀의 값을 0으로 만들기
4단계 : hyteresis Thresholding ( 실제 에지인지 아닌지 판단)
'''

import numpy as np
import cv2

def canny():
    img = cv2.imread('image/1.jpg')
    edge1 = cv2.Canny(img, 50, 200)
    edge2 = cv2.Canny(img, 100, 200)
    edge3 = cv2.Canny(img, 170, 200)

    cv2.imshow('original', img)
    cv2.imshow('Canny Edge1', edge1)
    cv2.imshow('Canny Edge2', edge2)
    cv2.imshow('Canny Edge3', edge3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

canny()

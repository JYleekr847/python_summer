# 히스토그램 균일화의 한계를 극복하는 CLAHE

'''
cv2의 equalizeHist를 사용해 구한 히스토그램과 numpy의
histogram함수를 이용해 구한 히스토그램은 이미지 전체 픽셀들에
대한 분포를 고려하여 일괄적으로 적용했다.
이러한 방법을 이용해서 좋은 이미지를 구하기 어렵다

이러한 방법은 원본 이미지를 전반적으로 밝게 한다. 이에 전체이미지가
전체적으로 밝아지는데 이로인해 원래 어두운 부분은 잘보이지만
원래 밝았던 부분은 너무 밝아지게된다.

이 문제점을 해결한 방법이 CLAHE이다.
이미지를 일정크기의 블록으로 구분하고, 블록별로 히스토그램 균일화를 시행
이미지 전체에 대해 균일화를 달성한다.
'''


import numpy as np
import cv2

def clahe():
    img = cv2.imread('image/12.jpg', cv2.IMREAD_GRAYSCALE)

    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize= (8,8))
    img2 = clahe.apply(img)

    res = np.hstack((img, img2))

    cv2.imshow('clahe', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

clahe()

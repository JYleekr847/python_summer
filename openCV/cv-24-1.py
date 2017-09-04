import numpy as np
import cv2

def histogram():
    img = cv2.imread('image/11.jpg', cv2.IMREAD_GRAYSCALE)
    '''
    numpy를 활용한 이미지 히스토그램
    hist, bins = np.histogram(img.ravel(), 256, [0,256])
    cdf = hist.cumsum()

    cdf_m = np.ma.masked_equal(cdf, 0)
    # 히스토그램 균일화 방정식
    cdf_m = (cdf_m- cdf_m.min())*255/(cdf_m.max()- cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')

    img2 = cdf[img]

    cv2.imshow('Histogram Equalization', img2)
    '''

    # CV2의 equalizeHist를 사용한 이미지 히스토그램
    equ = cv2.equalizeHist(img)
    res = np.hstack((img, equ))
    cv2.imshow('equalizer', res)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

histogram()

'''
cv2.Sobel(src, ddepth, dx, dy, ksize)
- src : 변형할 원본 이미지
- ddepth : 결과 이미지 데이터 타입
    - CV_8U: 픽셀값을 uint8로 설정
    - CV_16U: uint16
    - CV_32F: float32
    - CV_64F: float64

- dx, dy : 각각 x, y 방향으로 의 미분 차수
- ksize :  확장 sobel 커널의 크기. 1, 3, 5, 7 중 하나의 값을 ㅗ설ㅈ어

'''
import numpy as np
import cv2
import matplotlib.pyplot as plt

def grad():
    img = cv2.imread('image/2.jpg')

    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 3)

    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    plt.title('original'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
    plt.title('Lapacian'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap= 'gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

    plt.show()

grad()

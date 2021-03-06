import numpy as np
import cv2

def transform():
    img = cv2.imread('image/1.jpg')
    h, w = img.shape[:2]

    img2 = cv2.resize(img, None, fx= 0.5, fy = 1, interpolation = cv2.INTER_AREA)
    img3 = cv2.resize(img, None, fx=1, fy=0.5, interpolation=cv2.INTER_AREA)
    img4 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_AREA)

    cv2.imshow('original', img)
    cv2.imshow('fx=0.5', img2)
    cv2.imshow('fy=0.5', img3)
    cv2.imshow('fx = 0.5, fy=0.5', img4)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def transform2():
    img = cv2.imread('image/1.jpg')
    h, w = img.shape[:2]

    M = np.float32([[1,0,100], [0,1,50]])

    img2 = cv2.warpAffine(img, M, (w,h))
    cv2.imshow('shift image', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def transform3():
    img = cv2.imread('image/1.jpg')
    h, w = img.shape[:2]

    M1 = cv2.getRotationMatrix2D((w/2, h/2), 45, 1)
    M2 = cv2.getRotationMatrix2D((w/2,h/2), 90, 1)

    img2 = cv2.warpAffine(img, M1, (w, h))
    img3 = cv2.warpAffine(img, M2, (w, h))

    cv2.imshow('45-Rotated', img2)
    cv2.imshow('90-Rotated', img3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def transform4():
    img = cv2.imread('image/1.jpg')
    h, w = img.shape[:2]

    pts1 = np.float32([[50, 50], [200,50], [20,200]])
    pts2 = np.float32([[10,100], [200, 50], [100,250]])

    M = cv2.getAffineTransform(pts1, pts2)

    img2 = cv2.warpAffine(img, M, (w,h))

    cv2.imshow('original', img)
    cv2.imshow('Affine- Transform', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def transform5():
    img = cv2.imread('image/1.jpg')
    h, w = img.shape[:2]

    pts1 = np.float32([[0,0],[300,0], [0,300], [300,300]])
    pts2 = np.float32([[56,65], [368,52], [28,387], [389,390]])

    M = cv2.getPerspectiveTransform(pts1, pts2)

    img2 = cv2.warpPerspective(img, M, (w,h))

    cv2.imshow('original', img)
    cv2.imshow('Perspective-Transform', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
transform5()

'''
fx, fy : 각각 가로 방향 , 세로 방향으로 배율인자.
interpolation: 리사이징을 수행할때 적용할 interpolation 방법
* 축소할 땐 INTER_AREA
* 확대할 땐 INTER_NEAREST

warpAffine() 함수
- img : 변환할 소스
- M : 2 X 3 변환 매트릭스 (np.float32([[1,0,100], [0,1,50]]))
-(w ,h): 출력될 이미지 사이즈



'''

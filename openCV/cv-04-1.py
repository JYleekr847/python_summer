__author__ = 'junyoung847@naver.com'

"""
cv.line() 직선그리기 함수
cv.circle() 원그리기
cv.rectangle() 직사각형
cv.ellipse() 타원
cv.putText() 텍스트 입력
"""

import numpy as np
import cv2

def drawing():
    # 도형을 그리기 위한 공간 생성
    img = np.zeros((512, 512, 3), np.uint8)
    # 512X512베열생성 이때 각 멤버는 (0,0,0)으로 검정색 화면 , 채우는 데이터타임븡 ㅕㅑㅜㅅ8

    # 좌표 (0,0) 에서 (511,511)까지 연결하는 직선을 그립나다.
    # (255,0,0) : 색상 , 5는 선의 두꼐
    cv2.line(img, (0,0), (511,511), (255,0,0), 5)
    # (384, 0) 좌측 상단 꼭지점, (510, 128)우측 하단 꼭지점
    # 색상은 녹색 두께는 3 인 직선을 그린다.
    cv2.rectangle(img, (384,0), (510, 128), (0,255,0), 3)
    # (447,63) 원의 중심 , 63: 원의 반지름
    # 색상 , -1: 주어진 색상으로 도형을 채운다.
    cv2.circle(img, (447, 63), 63, (0,0,255), -1)
    # (256,256) 타원의 중심 (100,50): 장축과 단축의 길이의 1/2
    # (0,0,180) : 타원의 기울기 각도 , 타원의 호를 그리는 시작 각도, 타원의 호를 그리는 끝각도
    cv2.ellipse(img, (256,256), (100,50), 0,0, 180, (255,0,0), -1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'OpenCV', (10,500),font, 4, (255,255,255), 2)

    cv2.imshow('drawing', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


drawing()

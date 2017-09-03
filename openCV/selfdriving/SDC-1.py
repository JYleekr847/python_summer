import numpy as np
import cv2
'''
image = cv2.imread('solidWhiteCurve.jpg')
mark = np.copy(image)

blue_threshold = 200
green_threshold = 200
red_threshold = 200

bgr_threshold = [blue_threshold, green_threshold, red_threshold]

#bgr 제한값보다 작으면 검은색으로
thresholds = (image[:,:,0] <bgr_threshold[0])\
             | (image[:,:,1]<bgr_threshold[1])\
             | (image[:,:,2]<bgr_threshold[2])
mark[thresholds] = [0,0,0]

cv2.imshow('white', mark)
cv2.imshow('result', image)
cv2.waitKey(0)
'''

def region_of_interest(img, vertices, color3=(255,255,255), color1=255):
    mask = np.zeros_like(img) # img와 같은 키기의 빈이미지

    if len(img.shape) > 2: # 컬러이미지일때 채널3개
        color = color3
    else: #흑백 이미지 일때 (채널 1개 )
        color = color1
    # vertices로 정한 부분을 (ROI 설정부분)을 color로 채운다
    cv2.fillPoly(mask, vertices, color)

    ROI_image = cv2.bitwise_and(img,mask)
    return ROI_image

def mark_img(img, blue_threshold=200, green_threshold=200, red_threshold=200):

    #BGR 제한 값
    bgr_threshold = [blue_threshold, green_threshold, red_threshold]

    #BGR 제한 값보다 작으면 검은색으로
    thresholds = (image[:,:,0]< bgr_threshold[0])\
                |(image[:,:,1]< bgr_threshold[1])\
                |(image[:,:,2]< bgr_threshold[2])
    mark[thresholds] = [0,0,0]
    return mark


image = cv2.imread('solidWhiteCurve.jpg')
height, width = image.shape[:2]
#사다리꼴모양의 vertices 지정
vertices = np.array([[(50,height),(width/2-45, height/2+60), (width/2+45, height/2+60), (width-50, height)]], dtype= np.int32)
roi_img = region_of_interest(image,vertices,(0,0,255))

mark = np.copy(roi_img)
mark = mark_img(roi_img)

color_thresholds = (mark[:,:,0]==0) & (mark[:,:,1]==0) & (mark[:,:,2] > 200)
image[color_thresholds] = [0,0,255]

cv2.imshow('roi_white', mark)
cv2.imshow('result', image)
cv2.waitKey(0)

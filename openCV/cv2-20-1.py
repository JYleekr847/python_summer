import numpy as np
import cv2

def convex():
    img = cv2.imread('image/8.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[19]

    mmt = cv2.moments(cnt)
    # 무게 중심 좌표 구하기 
    cx = int(mmt['m10']/mmt['m00'])
    cy = int(mmt['m01']/mmt['m00'])

    x, y, w, h = cv2.boundingRect(cnt)
    korea_rect_area = w*h
    korea_area = cv2.contourArea(cnt)
    hull = cv2.convexHull(cnt)
    hull_area = cv2.contourArea(hull)
    ellipse = cv2.fitEllipse(cnt)

    aspect_ratio = w/h
    extent = korea_area/korea_rect_area
    solidity = korea_area/hull_area

    print('대한민국 aspect_ratio : \t %.3f' %aspect_ratio)
    print('대한민국 Extent: \t %.3f' %extent)
    print('대한민국 solidity \t %.3f' %solidity)
    print('대한민국 Orientiation: \t %.3f' %ellipse[2])

    equivalent_diameter = np.sqrt(4*korea_area/np.pi)
    korea_radius = int(equivalent_diameter/2)

    cv2.circle(img, (cx, cy), 3, (0,0,255), -1)
    cv2.circle(img, (cx, cy), korea_radius, (0,0,255), 2)
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.ellipse(img, ellipse, (50,50,50), 2)

    cv2.imshow('Korea Features', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

convex()

# blur: low pass filler & high pass filter를 이용하여 필터링

# LPF : 이미지 노이즈 제거 & 이미지 블러링
# HPF : 이미지에서 edge 를 찾을 때

import numpy as np
import cv2


def bluring():
    img = cv2.imread('image/1.jpg')

    kernel = np.ones((5,5), np.float32)/25

    blur = cv2.filter2D(img, -1, kernel)

    cv2.imshow('blur', blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

bluring()

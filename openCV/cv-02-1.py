__author__= "junyoung847@naver.com"

import numpy as np
import cv2

def showImage():
	imgfile = 'image/1.jpg'
	img = cv2.imread(imgfile, cv2.IMREAD_COLOR)
	
	#cv2.namedWindow('1',cv2.WINDOW_NORMAL)
	cv2.imshow('1', img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	
	k = cv2.waitKey(0) & 0xFF
	
	if k == 27:
		cv2.destroyAllWindows()
	elif k == ord('c'):
		cv2.imwrite('image/1_copy.jpg', img)
		cv2.destroyAllwindows()

showImage()
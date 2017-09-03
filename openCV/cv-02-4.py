__author__ = 'junyoung847@naver.com'

import numpy as np
import cv2
import matplotlib.pyplot as plt

def showImage():
	imgfile = 'image/1.jpg'
	img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)
	
	plt.imshow(img, cmap='gray', interpolation='bicubic')
	plt.xticks([])
	plt.yticks([])
	plt.title('model')
	plt.show()

showImage()
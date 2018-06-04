import cv2
import numpy as np 
import scipy.interpolate

def strokeEdges(src , dst , blurKsize=7,edgeKsize=5):
	if blurKsize>=3:
		blurred = cv2.medianBlur(src,blurKsize)
		gray = cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
	else:
		gray = cv2.cvtColor(src,cv2.COOR_BGR2GRAY)
	cv2.Laplacian(gray,cv2.CV_8U,gray,ksize = edgeKsize)
	channels = cv2.split(src)
	for channel in channels:
		channel[:] = channel * normalizedInverseAlpha
	cv2.merge(channels,dst)
	
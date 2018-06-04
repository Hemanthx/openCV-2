import numpy as np 
import cv2
from scipy import ndimage

kernel_3x3	=	np.array([[-1,	-1,	-1],
				[-1,		8,	-1],
				[-1,	-1,	-1]])
kernel_5X5 = np.array([[-1,	-1,	-1,	-1,	-1],
					[-1,		1,		2,		1,	-1],
					[-1,		2,		4,		2,	-1],
					[-1,		1,		2,		1,	-1],
					[-1,	-1,	-1,	-1,	-1]])

img = cv2.imread('/home/hemanth/Downloads/pic.jpg',0)

k3 = ndimage.convolve(img,kernel_3x3)
k5 = ndimage.convolve(img,kernel_5X5)

blurred = cv2.GaussianBlur(img , (11,11),0)
g_hpf = img - blurred

cv2.imshow('3X3',k3)
cv2.imshow('5X5',k5)
cv2.imshow('Guassian',g_hpf)
cv2.waitKey()
cv2.DestroyAllWindows()
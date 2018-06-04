# edge detection with canny 
import numpy as np 
import cv2

img = cv2.imread('/home/hemanth/Downloads/pic.jpg')
cv2.imwrite("canny.jpg",cv2.Canny(img,200,300))
cv2.imshow("canny",cv2.imread("canny.jpg"))
cv2.waitKey()
cv2.DestroyAllWindows()
import numpy as np 
import cv2
import scipy.interpolate

#create a fully black image
img = np.zeros((200,200),dtype = np.uint8)
#make half of them white
img[50:150 , 50:150] = 255

ret , thresh = cv2.threshold(img,127,255,0)
#find contours
contours,heirarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#convert to color
color = cv2.cvtColor(img , cv2.COLOR_GRAY2BGR)
img = cv2.drawContours(color,contours,-1,(0,255,0),2)
cv2.imshow("contours",color)
cv2.waitKey()
cv2.DestroyAllWindows()
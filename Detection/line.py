import numpy as np 
import cv2

img = cv2.imread('/home/hemanth/Downloads/lines.jpeg')
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,120)
minlength = 120
maxgap = 5
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minlength,maxgap)
for x1,y1,x2,y2 in lines[0]:
	cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow("edges",edges)
cv2.imshow("gray",gray)
cv2.imshow("lines",img)
cv2.waitKey()
cv2.DestroyAllWindows()
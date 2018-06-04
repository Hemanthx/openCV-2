import cv2
import numpy as np 

img = cv2.imread('/home/hemanth/Downloads/circles.jpeg')
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
cimg = cv2.medianBlur(gray,5)
bgrimg = cv2.cvtColor(cimg , cv2.COLOR_GRAY2BGR)

circle = cv2.HoughCircles(cimg,cv2.cv.CV_HOUGH_GRADIENT,1,20,param1=100,param2=30,minRadius=0,maxRadius=0)
#circle = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

circle = np.uint16(np.around(circle))

for i in circle[0,:]:
	cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
	cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imwrite("circles.jpeg",img)
cv2.imshow("Hough",img)
cv2.waitKey()
cv2.DestroyAllWindows()

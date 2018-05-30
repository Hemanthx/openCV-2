import cv2

clicked = False
def onclicked(event,x,y,flags,params):
	global clicked
	if event == cv2.EVENT_LBUTTONUP:
		clicked = True
cameracapture = cv2.VideoCapture(0)
cv2.namedWindow('Mywindow')
cv2.setMouseCallback('Mywindow',onclicked)
print 'showing camera feed click any button to cancel'
success , frame = cameracapture.read()
gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
while success and cv2.waitKey(1) == -1 and not clicked:

	cv2.imshow('Mywindow',frame)
	cv2.imshow('Gray',gray)
	success,frame = cameracapture.read()

cv2.destroyWindow('Mywindow')
cameracapture.release()
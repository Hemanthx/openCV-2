import cv2 

cameracapture = cv2.videocapture(0)
fps = 30
size = (int(cameracapture.get(CAP_PROP_FRAME_WIDTH)),int(cameracapture.get(CAP_PROP_FRAME_HEIGHT)))
videowriter = cv2.videoWriter('MyOutputVid.avi',	cv2.VideoWriter_fourcc('I','4','2','0'),fps,size)
success , frame = cameracapture.read()
frames_remaning = 10*fps-1
while success and frames_remaning >0:
	videowriter.write(frame)
	success,frame = cameracapture.read()
	frames_remaning = frames_remaning-1

cameracapture.release()
# an appropriate timer for capturing the frames is the best way to proceed


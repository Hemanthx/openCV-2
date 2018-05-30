#import dependecies
import cv2

videocapture = cv2.VideoCapture('input.avi')
fps = videocapture.get(cv2.CAP_PROP_FPS)
size = (int(videocapture.get(CAP_PROP_FRAME_HEIGHT)),int(videocapture.get(CAP_PROP_FRAME_WIDTH)))
videoWriter	=	cv2.VideoWriter('MyOutput.avi',	cv2.VideoWriter_fourcc('I','4','2','0'),fps,size)
#fourcc tells us about the type of video format itll store in . extension should be a .avi file . can be stored as an MPEG-4 and MPEG-1 video file as well
success , frame = videocapture.read()
# keep looping and writing in output vid until there are no more frames left 
while success:
	videoWriter.write(frame)
	success, frame = videocapture.read()
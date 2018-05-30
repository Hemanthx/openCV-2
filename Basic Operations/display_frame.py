import cv2
import numpy as np

img = cv2.imread('path/pic.jpg')
cv2.imshow('pic.jpg',img)
cv2.waitkey()
img.destroyallwindows()

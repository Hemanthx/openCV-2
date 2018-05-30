import cv2
import os
import numpy as np 

random_array = bytearray(os.urandom(120000))
np_array = np.array(random_array)

gray_image = np_array.reshape(300,400)
cv2.imwrite('gray.png',gray_image)

gbr_image = np_array.reshape(100,400,3)
cv2.imwrite('gbr.png',gbr_image)

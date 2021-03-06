

import os, time, sys
import numpy as np
import cv, cv2
import scipy.ndimage as nd
sys.path.append('/Users/colin/code/Kinect-Projects/icuRecorder/')
from icuReader import ICUReader as DepthReader

camOffset = 11 # There is an ~11 second offset between the two cameras

clockTime = time.time()
# path = '/Users/colin/data/ICU_7March2012_Head/'
path = '/Users/colin/data/ICU_7May2012_Wide/'
framerate = 601;
# Points of interest {IV: 1350/1490}
startTime_ = 1000;
# startTime_ = 5350;
reader1 = DepthReader(path, framerate, startTime_, cameraNumber=0, clockTime=clockTime, viz=1, vizSkel=1)

# path2 = '/Users/colin/data/ICU_7March2012_Foot/'
path2 = '/Users/colin/data/ICU_7May2012_Close/'
startTime2 = startTime_+camOffset;
reader2 = DepthReader(path2, framerate, startTime2, cameraNumber=1, clockTime=clockTime, viz=1, vizSkel=1)


# cv.NamedWindow("a")
# cv.NamedWindow("b")

while 1:
	t = time.time()
	# print (t-clockTime)*framerate%3600
	reader1.run(t)
	print reader1.Time_min
	reader2.run(t)
	cv.WaitKey(1)




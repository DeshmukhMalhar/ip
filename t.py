import cv2
import numpy as np
from matplotlib import pyplot as plt

inpt = cv2.imread('Shuttle/0002.jpg')
#cv2.resize(inpt,inpt, 0.5, 0.5)
inpt=cv2.resize(inpt,(480,640),interpolation=cv2.INTER_AREA)
cv2.imshow('original',inpt)
blr=cv2.GaussianBlur(inpt,(49,49),0)
cv2.imshow('Blurred',blr)

inptHSV=cv2.cvtColor(blr, cv2.COLOR_BGR2HSV)
#[[[157 131 123]]]
#[[[ 77 255  55]]]


lowHue=60
lowSat=250
lowVal=20

highHue=110
highSat=255
highVal=150

lowLimit=np.array([lowHue,lowSat,lowVal],'uint8')
hoghLimit=np.array([highHue,highSat,highVal],'uint8')

#print(lowLimit,hoghLimit)

mask=cv2.inRange(inptHSV,lowLimit,hoghLimit,)
cv2.imshow('mask',mask)
masked = cv2.bitwise_and(inpt,inpt,mask=mask)
cv2.imshow("Masked",masked)

minAvg=2
maxAvg=20

avg=np.average(mask)
print(avg)

if ((avg >minAvg)and (avg < maxAvg)):
    print("Shuttle is detected")
'''
det = cv2.SimpleBlobDetector_create()

keys = det.detect(masked)

im_with_keypoints = cv2.drawKeypoints(masked, keys, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('keys',im_with_keypoints)
'''
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
from matplotlib import pyplot as plt
inpt = cv2.imread('0033.jpg')
#cv2.resize(inpt,inpt, 0.5, 0.5)

cv2.imshow('original',inpt)
blr=cv2.GaussianBlur(inpt,(49,49),0)
cv2.imshow('Blurred',blr)

inptHSV=cv2.cvtColor(blr, cv2.COLOR_BGR2HSV)
#[[[157 131 123]]]
lowHue=150
lowSat=100
lowVal=40

highHue=180
highSat=150
highVal=210

lowLimit=np.array([lowHue,lowSat,lowVal],'uint8')
hoghLimit=np.array([highHue,highSat,highVal],'uint8')

#print(lowLimit,hoghLimit)

mask=cv2.inRange(inptHSV,lowLimit,hoghLimit,)
cv2.imshow('mask',mask)
masked = cv2.bitwise_and(inpt,inpt,mask=mask)
cv2.imshow("Masked",masked)

det = cv2.SimpleBlobDetector_create()

keys = det.detect(masked)

im_with_keypoints = cv2.drawKeypoints(masked, keys, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('keys',im_with_keypoints)

cv2.waitKey(0)
cv2.destroyAllWindows()

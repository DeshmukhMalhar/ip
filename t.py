#this file contains threshs for green shuttle
#red.py will detect red shuttle and gold.py will detect golden shuttle
#at the end all three files will be stiched together

import cv2
import numpy as np
from matplotlib import pyplot as plt

inpt = cv2.imread('Shuttle/0014.jpg')
#cv2.resize(inpt,inpt, 0.5, 0.5)
inpt=cv2.resize(inpt,(480,640),interpolation=cv2.INTER_AREA)
cv2.imshow('original',inpt)
blr=cv2.GaussianBlur(inpt,(7,7),0)
cv2.imshow('Blurred',blr)

inptHSV=cv2.cvtColor(blr, cv2.COLOR_BGR2HSV)

#[[[157 131 123]]]
#[[[ 77 255  55]]]
#[[[ 81 255 129]]]
#[[[ 87 142  61]]]


lowHue=60
lowSat=130
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
maxAvg=30

avg=np.average(mask)
print(avg)

if ((avg >minAvg)and (avg < maxAvg)):
    print("Shuttle is detected")
    else:
        print("Shuttle is not detected")

cv2.waitKey(0)
cv2.destroyAllWindows()

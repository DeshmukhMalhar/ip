#Detects red shuttles
#has thresh for red shuttles
import cv2
import numpy as np
from matplotlib import pyplot as plt

inpt = cv2.imread('Shuttle/0028.jpg')
#cv2.resize(inpt,inpt, 0.5, 0.5)
inpt=cv2.resize(inpt,(480,640),interpolation=cv2.INTER_AREA)
cv2.imshow('original',inpt)
blr=cv2.GaussianBlur(inpt,(7,7),0)
cv2.imshow('Blurred',blr)

inptHSV=cv2.cvtColor(blr, cv2.COLOR_BGR2HSV)
#[[[  0 255 153]]]


lowHue=0
lowSat=180
lowVal=60

highHue=10
highSat=255
highVal=230

lowLimit=np.array([lowHue,lowSat,lowVal],'uint8')
hoghLimit=np.array([highHue,highSat,highVal],'uint8')

#print(lowLimit,hoghLimit)

mask=cv2.inRange(inptHSV,lowLimit,hoghLimit,)
cv2.imshow('mask',mask)
masked = cv2.bitwise_and(inpt,inpt,mask=mask)
cv2.imshow("Masked",masked)

minAvg=1.5
maxAvg=30

avg=np.average(mask)
print(avg)

if ((avg >minAvg)and (avg < maxAvg)):
    print("Shuttle is detected")
else:
    print("Shuttle is not detected")

cv2.waitKey(0)
cv2.destroyAllWindows()

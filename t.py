import cv2
import numpy as np
inpt = cv2.imread('0013.jpg')
cv2.resize(inpt,inpt,Size(), 0.5, 0.5)

cv2.imshow('original',inpt)
blr=cv2.GaussianBlur(inpt,(25,25),0)
cv2.imshow('Blurred',blr)

inptHSV=cv2.cvtColor(blr, cv2.COLOR_BGR2HSV)

lowHue=150
lowSat=100
lowVal=60

highHue=180
highSat=140
highVal=100

lowLimit=np.array([lowHue,lowSat,lowVal],'uint8')
hoghLimit=np.array([highHue,highSat,highVal],'uint8')

print(lowLimit,hoghLimit)

mask=cv2.inRange(inptHSV,lowLimit,hoghLimit,)
cv2.imshow('mask',mask)

cv2.waitKey(10000)
cv2.destroyAllWindows()

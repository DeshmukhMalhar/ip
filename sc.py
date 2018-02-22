import cv2
import numpy as np
inp = cv2.imread("0020.jpg")
cv2.imshow('INput',inp)


lowHue=150
lowSat=100
lowVal=40

highHue=180
highSat=150
highVal=210

lowLimit=np.array([lowHue,lowSat,lowVal],'uint8')
hoghLimit=np.array([highHue,highSat,highVal],'uint8')

i=0
j=0

avg=np.mean(inp,axis=0)
print(avg)
cv2.waitKey(0)
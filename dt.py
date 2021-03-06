
#find object

import picamera
import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

LedPin = 11
buttpin = 13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LedPin, GPIO.OUT)  
GPIO.setup(buttpin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

cam=picamera.PiCamera()

cam.capture('img.jpg')

inpt = cv2.imread('img.jpg')
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
#[[[178 196 248]]]

lowHue=150
lowSat=150
lowVal=120

highHue=250
highSat=250
highVal=255

lowLimit=np.array([lowHue,lowSat,lowVal],'uint8')
hoghLimit=np.array([highHue,highSat,highVal],'uint8')

#print(lowLimit,hoghLimit)

mask=cv2.inRange(inptHSV,lowLimit,hoghLimit,)
cv2.imshow('mask',mask)
masked = cv2.bitwise_and(inpt,inpt,mask=mask)
cv2.imshow("Masked",masked)

minAvg=1.5
maxAvg=25

avg=np.average(mask)
print(avg)

if ((avg >minAvg)and (avg < maxAvg)):
    print("Shuttle is detected")
    GPIO.output(LedPin, GPIO.HIGH)
    time.sleep(0.5)
else:
    print("Shuttle is not detected")
    GPIO.output(LedPin, GPIO.LOW)
    time.sleep(0.5)

#cv2.waitKey(0)
cv2.destroyAllWindows()
GPIO.output(LedPin, GPIO.LOW) 
GPIO.cleanup()  

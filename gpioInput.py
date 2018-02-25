import RPi.GPIO as GPIO
import time
#from dt.py 
import picamera
import cv2
import numpy as np
import RPi.GPIO as GPIO
import time

cam=picamera.PiCamera()

LedPin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LedPin, GPIO.OUT)  

#im dtpy end

ButtPin = 13
RedShuttlePin = 3
ButtState = False

def printFunction(channel):
    global ButtState
    ButtState = ~ ButtState
    print('Button pressed')
    print('Note how the bouncetime affects the button press')


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT) 
    GPIO.setup(RedShuttlePin, GPIO.OUT) 
    GPIO.setup(ButtPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(ButtPin, GPIO.RISING, callback=printFunction, bouncetime=300)

def blink():
  while True:
    if ButtState is False :
      GPIO.output(LedPin, GPIO.HIGH)  
      time.sleep(1)
      GPIO.output(LedPin, GPIO.LOW) 
      time.sleep(1)
    else :
        #from dt

        
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
            GPIO.output(RedShuttlePin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(RedShuttlePin, GPIO.LOW)
        else:
            print("Shuttle is not detected")
            GPIO.output(RedShuttlePin, GPIO.LOW)
            time.sleep(0.5)

        global ButtState
        ButtState = False
        #cv2.waitKey(0)
        cv2.destroyAllWindows()



def destroy():
    GPIO.output(RedShuttlePin, GPIO.LOW)
    GPIO.output(LedPin, GPIO.LOW)
    GPIO.cleanup()


if __name__ == '__main__':
    setup()
    try:
        blink()
    except KeyboardInterrupt:
        destroy()

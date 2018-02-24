import cv2
import numpy as np
#BGR is the order for conversion
def mapv (x,  in_min, in_max,  out_min,  out_max ):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

#32 56 81
#15 29 186
#xyz in BGR order

x=30
y=52
z=0

a=mapv(x,0,240,0,255)
b=mapv(y,0,240,0,255)
c=mapv(z,0,240,0,255)

green = np.uint8([[[a,b,c]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print("HSV color space is ")
print (hsv_green)
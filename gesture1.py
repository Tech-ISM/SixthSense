from collections import deque
import cv2,numpy as np,imutils
import pyautogui

greenLower = (29,86,6)
greenUpper = (64,255,255)
#greenLower = (20, 100, 10)
#greenUpper = (100, 252, 100)
blueLower = (10,100,100)
blueUpper = (120,255,255)
#blueLower= (8, 10, 111)
#blueUpper= (102,100,250)
redLower = (0,100,100)
redUpper = (10,255,255)
#redLower = (111, 8, 32)
#redUpper = (250,58,52)
pinkLower = (160,100,100)
pinkUpper = (179,255,255)
#pinkLower = (150,10,100)
#pinkUpper = (250,100,250)x

camera = cv2.VideoCapture(0)

while True:
    (width,height) = pyautogui.size()
    (grabbed, frame_inverted) = camera.read()
    frame = cv2.flip( frame_inverted, 1 )
    frame = imutils.resize(frame,width = 600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#contours for green color

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv, greenLower, greenUpper)

#    mask1 = cv2.inRange(rgb, greenLower, greenUpper)
    mask1 = cv2.erode(mask1, None, iterations=2)
    mask1 = cv2.dilate(mask1, None, iterations=2)
    cnts1 = cv2.findContours(mask1.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]

#contours for blue color

    mask2 = cv2.inRange(hsv,blueLower,blueUpper)
#    mask2 = cv2.inRange(rgb, blueLower, blueUpper)
    mask2 = cv2.erode(mask2, None, iterations=2)
    mask2 = cv2.dilate(mask2, None, iterations=2)
    cnts2 = cv2.findContours(mask2.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]

#contours for red color 

    mask3 = cv2.inRange(rgb, redLower, redUpper)
    mask3 = cv2.erode(mask3, None, iterations=2)
    mask3 = cv2.dilate(mask3, None, iterations=2)
    cnts3 = cv2.findContours(mask3.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]

#contours for pink color 

    mask4 = cv2.inRange(rgb, pinkLower, pinkUpper)
    mask4 = cv2.erode(mask4, None, iterations=2)
    mask4 = cv2.dilate(mask4, None, iterations=2)
    cnts4 = cv2.findContours(mask4.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]

   
#    for c in cnts1:
    if len(cnts1) > 0:
        c_max = max(cnts1,key=cv2.contourArea)
	(x, y, w, h) = cv2.boundingRect(c_max)
    
	if (w>0)and(h>0):
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            pyautogui.moveTo((x+w//2)*width/600,(y+h//2)*height/340)
    
#    for c in cnts2:
    if len(cnts2) > 0:
        c_max = max(cnts2, key=cv2.contourArea)
	(x, y, w, h) = cv2.boundingRect(c_max)
        bcenter = (x+w//2,y+h//2)
	if (w>2)and(h>2):
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
  
#    for c in cnts3:
    if len(cnts3) > 0:
	c_max = max(cnts3, key=cv2.contourArea)
	(x, y, w, h) = cv2.boundingRect(c_max)
        rcenter = (x+w//2,y+h//2)
	if (w>0)and(h>0):
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
  
#    for c in cnts4:
    if len(cnts4) > 0:
	c_max = max(cnts4, key=cv2.contourArea)
	(x, y, w, h) = cv2.boundingRect(c_max)
        pcenter = (x+w//2,y+h//2)
	if (w>0)and(h>0):
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),2)
    

    cv2.imshow('Image',frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
	break

camera.release()
cv2.destroyAllWindows()

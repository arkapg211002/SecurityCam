#ARKAPRATIM GHOSH
import cv2
import winsound
camera=cv2.VideoCapture(0)
while camera.isOpened():
    ret,frame=camera.read()
    ret,frame2=camera.read()
    diff=cv2.absdiff(frame,frame2)
    convert=cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
    blur=cv2.rectangle(convert,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contour,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for c in contour:
        if cv2.contourArea(c)<5000:
            continue
        x,y,w,h=cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        winsound.Beep(500,200)
    if cv2.waitKey(10)==ord('q'):
        break
    cv2.imshow('SecurityCam',frame)
    

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
stop_sign_cascade = cv2.CascadeClassifier("stopsign.xml")


while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    stop_signs = stop_sign_cascade.detectMultiScale(gray, 1.5, 5)
    if ret == True:

        for(x,y,w,h) in stop_signs:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,128,0), 2)

        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()

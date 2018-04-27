import cv2
import time

cp0 = cv2.VideoCapture(0)

frame_id = 0
sleep = 0
delayratio = 10

while 1:
        ret0, frame0 = cp0.read()
        cv2.imshow('Test0', frame0)

        if cv2.waitKey(1) & 0xFF == ord('q'): #hit q to stop program
            cp0.release()

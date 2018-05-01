import numpy as np
import cv2
img = cv2.imread('alice.jpg')
cv2.imshow('window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
img = cv2.imread("./resources/card.jpg")

imgHor = np.hstack((img,img)) #horizontal stacking of images
imgVer = np.vstack((img,img)) #vertical stacking of images

cv2.imshow("horizontal",imgHor)
cv2.imshow("vertical",imgVer)
cv2.waitKey(0)
import cv2
import numpy as np
img = cv2.imread("./resources/avicii2.jpg")
kernel = np.ones((5,5),np.uint8)
greyImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting to grey scale
blurImg = cv2.GaussianBlur(greyImg,(7,7),0) #bluring the image , parametres takes in () oddvalues
cannyImg = cv2.Canny(img,150,200) #detects edges in the images 100,100 is the threshold
dilationImg = cv2.dilate(cannyImg,kernel,iterations=1) #increases the thickness of the edges
erodedImg = cv2.erode(dilationImg,kernel,iterations=1) #decreses the thickness of edge i.e opposite of  dilate
cv2.imshow("grey-scale",greyImg)
cv2.imshow("blur image",blurImg)
cv2.imshow("Canny Image",cannyImg)
cv2.imshow("Dilation Image",dilationImg)
cv2.imshow("Eroded Image",erodedImg)
cv2.waitKey(0)

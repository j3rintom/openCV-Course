import cv2
import numpy as np
def empty(a):
    pass
path = "./resources/card.jpg"
cv2.namedWindow("Trackbars") #creating a window for trackbar
cv2.resizeWindow("Trackbars",640,240) #resizing the window
cv2.createTrackbar("Hue Min","Hue Min",-1,179,empty) #assigning values to the trackbar(empty can be replaced by a function
cv2.createTrackbar("Hue Max","Trackbars",179,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",0,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",82,255,empty)
cv2.createTrackbar("Val Min","Trackbars",120,255,empty)
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","Trackbars") #getting the  values on changing fro trackbar
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper) #creating a mask for detected color portion
    imgResult = cv2.bitwise_and(img,img,mask=mask) #selecting teh detected color from the original image
    cv2.imshow("image",img)
    cv2.imshow("imagehsv",imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)
    cv2.waitKey(1)
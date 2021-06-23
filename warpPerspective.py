import cv2
import numpy as np

img = cv2.imread("./resources/card.jpg")

width,height = 250,350 #conventional dimension of a card
pts1 = np.float32([[148,183],[183,74],[457,213],[461,97]]) #defining end points of the portion to cut
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) # defining the canvas
matrix = cv2.getPerspectiveTransform(pts1,pts2) #making and transforming perspectiveof the canvas
imgOutput = cv2.warpPerspective(img,matrix,(width,height)) #placing the cut image porton in the canvas

cv2.imshow("warp",imgOutput)
cv2.imshow("image",img)
cv2.waitKey(0)
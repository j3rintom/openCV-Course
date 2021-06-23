import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)  #decalres a image of 512X512 with full zeros that is full balck
#img[:] = 255,0,0 #gives color blue to the whole image
#img[300:400,:200:500] = 255,0,0
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2) #declaration of a rectangle(cv2.FILLEd used for filling color
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)  #declaration of a line
cv2.circle(img,(400,50),50,(255,255,0),5)  #declaration of circle
cv2.putText(img," opencv ",(300,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,155,0),2)  #display text in images



cv2.imshow("image",img)
cv2.waitKey(0)
import cv2
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
img = cv2.imread("./resources/lena.png")
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGrey,1.1,4)

for (x,y,w,h) in faces :
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)



cv2.imshow("image",img)
cv2.waitKey(0)
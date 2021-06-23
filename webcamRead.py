import cv2

cap = cv2.VideoCapture(0) #src = 0 for default camera
cap.set(3,640) #id=3 for width
cap.set(4,480) #id=4 for height
cap.set(10,100)#id=10 for brightness of camera
while True:
    success,img= cap.read()
    cv2.imshow("cam",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
import cv2
import numpy as np

def stackImages(scale,imgArray): #predefined function for joining images
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContour(img) :  #for setting contours i.e. boundaries
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #finding the edges of a substance
    for cnt in contours:
        area = cv2.contourArea(cnt) #finding area of a contour
        print(area)
        if area>500:  #filtering contours
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3) #drawing contours
            peri = cv2.arcLength(cnt,True) #finding perimeter of theshape
            approx = cv2.approxPolyDP(cnt,0.02*peri,True) #finding boundary points
            objCor = len(approx) #no of corners
            print(objCor)
            x , y , w , h = cv2.boundingRect(approx) #setting approximate boundary rectangle

            if objCor == 3:objText = "Tri"  #setting shape according to no of sides
            elif objCor ==4:
                aspectRatio = w/float(h)
                if aspectRatio >=0.95 and aspectRatio<=1.05:objText="Square"
                else:objText="rectangle"
            elif objCor > 4:objText="Circle"
            else:objText="None"
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2) #drawing rectangles using the approximate boundary points
            cv2.putText(imgContour,objText,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2) #printing the type of shape in the image


img = cv2.imread("./resources/shapes.png")
imgContour = img.copy()
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey,(7,7),1)

imgBlank = np.zeros_like(img)
imgCanny = cv2.Canny(imgBlur,50,50)
getContour(imgCanny)
imgStack = stackImages(0.7,([img,imgGrey,imgBlur],[imgCanny,imgContour,imgBlank]))
cv2.imshow("stack",imgStack)
cv2.waitKey(0)
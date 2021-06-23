import cv2

img =cv2.imread("./resources/avicii2.jpg")
print(img.shape) #prints the size of the image

imgResize = cv2.resize(img,(400,700)) #resizes image takes parameter in the form (width,height)
print(imgResize.shape)

imgCropped = img[0:400,200:700] #crops image in the form (height,width)

cv2.imshow("image",img)
cv2.imshow("resize image",imgResize)
cv2.imshow("cropped image",imgCropped)
cv2.waitKey(0)
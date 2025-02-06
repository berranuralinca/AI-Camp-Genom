import cv2 as cv
import numpy as np

# maskeleme

img = cv.imread("resources\photos\cats.jpg")
cv.imshow("cats",img)

blank = np.zeros(img.shape[:2],dtype="uint8")

# kullanacagimiz maske
mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow("mask",mask)
 
# maskeleme
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow("masked",masked)
cv.waitKey(0)
import cv2 as cv
import numpy as np

img = cv.imread("resources\photos\cats.jpg")
cv.imshow("cats",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
#lap
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian",lap)


# sobel
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow("sobel x",sobelx)
cv.imshow("sobely",sobely)
cv.imshow("xysobel",combined_sobel)
cv.waitKey(0)
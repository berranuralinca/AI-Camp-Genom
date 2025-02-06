import cv2 as cv

img = cv.imread("resources\photos\cats.jpg")
cv.imshow("cats",img)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# basit esikleme
threshold,thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow("simple thresh",thresh)

# adaptif esikleme
adaptive_tresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("adaptive",adaptive_tresh)


cv.waitKey(0)
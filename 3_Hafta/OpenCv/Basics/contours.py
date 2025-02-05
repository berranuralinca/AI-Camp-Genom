import cv2 as cv
import numpy as np

# kontur 

img = cv.imread("resources/photos/cats.jpg")
resized = cv.resize(img,(500,400),cv.INTER_AREA)
cv.imshow("cats",resized)
cv.waitKey(0)

# gray
gray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cv.waitKey(0)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow("blur",blur)
cv.waitKey(0)

# kenar
canny = cv.Canny(blur,125,175)
cv.imshow("canny",canny)
cv.waitKey(0)

blank = np.zeros(resized.shape,dtype ="uint8")

# esikleme
ret, thresh = cv.threshold(canny, 125, 255, cv.THRESH_BINARY)  # esik degeri ve esik goruntusu olusturur.

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)  # kontur listesi ve hiyerarsi (retrlist hiyerarsi onemsemez.)

print(f'{len(contours)} contour(s) found!') # kontur sayisini yazdirma

cv.drawContours(blank, contours, -1, (0,0,255), 1) # kontur cizdirme
cv.imshow('Contours Drawn', blank)
cv.waitKey(0)
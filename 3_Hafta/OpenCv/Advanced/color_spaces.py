# Renk Uzaylari

import cv2 as cv
import matplotlib.pyplot as plt 


img = cv.imread("resources\photos\park.jpg")
cv.imshow("img",img)

# BGR to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)  # grayscale > BGR mumkun
cv.imshow("gray",gray)
# grayscale > lab = grayscale > BGR > lab mumkun

# BGR to HSV
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)   # HSV > BGR mumkun
cv.imshow("hsv",hsv)

# BGR to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)  
cv.imshow("lab",lab)

# BGR to RGB 
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("rgb",rgb)


plt.imshow(rgb)  # BGR olan goruntuyu RGB goruntuler.BGRTORGB
plt.show()


cv.waitKey(0)
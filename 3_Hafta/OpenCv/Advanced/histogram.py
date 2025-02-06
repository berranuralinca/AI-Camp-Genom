import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("resources\photos\cats.jpg")
cv.imshow("cats",img)

# gri tonlamalar icin histogram
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blank = np.zeros(img.shape[:2],dtype="uint8")

# kullanacagimiz maske
mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow("mask",mask)
 
# maskeleme
masked = cv.bitwise_and(gray,gray,mask=mask)
cv.imshow("masked",masked)

gray_hist = cv.calcHist([gray],[0],masked,[256],[0,256])

# gray histogram
plt.figure()
plt.plot(gray_hist)
plt.title("grayscale hist")
plt.xlabel("bins")
plt.ylabel("pixels")
plt.xlim([0,256])
plt.show()


# renkli histogram

plt.figure()
plt.title("grayscale hist")
plt.xlabel("bins")
plt.ylabel("pixels")

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow("masked",masked)

colors = ("b","g","r")
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()
cv.waitKey(0)

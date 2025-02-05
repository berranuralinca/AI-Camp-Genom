# Gri yapmak
import cv2 as cv  # import etme


# gri yapmak
img = cv.imread("resources/photos/park.jpg")
cv.imshow("park",img)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)  # bgr to gray
cv.imshow("Gray",gray)
cv.waitKey(0)


# blur
img = cv.imread("resources/photos/park.jpg")
blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)  # gaussian blur
cv.imshow("Blur",blur)


# kenar algilama
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)  # kenar algilama
cv.waitKey(0)


# beyazlari genisletme
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated', dilated)
cv.waitKey(0)

# asindirma
eroded = cv.erode(dilated,(3,3),iterations=3)
cv.imshow('eroded', eroded)
cv.waitKey(0)


# boyutlandirma
resized = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)  # boyutlandirma yaparken kalite bozulmamasi icin
cv.imshow('resized', resized)
cv.waitKey(0)


# Kirpma
cropped = img[100:200,250:500]
cv.imshow('cropped', cropped)
cv.waitKey(0)

cv.destroyAllWindows()  # acik tum pencereleri kapatir.


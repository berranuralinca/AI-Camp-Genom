import cv2 as cv
import numpy as np

img = cv.imread("resources/photos/park.jpg")
cv.imshow("img",img)
cv.waitKey(0)


def translate(img,x,y):    # kaydirma       # x = yatay kaydirma miktari,y = dikey kaydirma miktari
    transMat = np.float32([[1,0,x],[0,1,y]])    # donusum matrisi
    dimensions = (img.shape[1],img.shape[0])   # genislik ve yukseklik
    return cv.warpAffine(img,transMat,dimensions)  # kaydirma fonk.


# sag alta kaydirma
translated = translate(img,100,100)
cv.imshow("translated",translated)
cv.waitKey(0)

# sol uste kaydirma
translated = translate(img,-100,-100)
cv.imshow("translated",translated)
cv.waitKey(0)

# -x > left
# -y > up
# x > right
# y > down



# dondurme
def rotate(img,angle,rotpoint = None):  
    (heigth,width) = img.shape[:2]

    if rotpoint is None:
        rotpoint = (width//2,heigth//2)

    rotmat = cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dimensions = (width,heigth)

    return cv.warpAffine(img,rotmat,dimensions)

rotated = rotate(img,90)
cv.imshow("rotated",rotated)
cv.waitKey(0)


# yansitma

# yansitma gibi dusunebiliriz
# 0 ise x eksenine gore
# 1 ise y eksenine gore
# -1 ise her ikisi

fliped = cv.flip(img,1)
cv.imshow("fliped",fliped)
cv.waitKey(0)



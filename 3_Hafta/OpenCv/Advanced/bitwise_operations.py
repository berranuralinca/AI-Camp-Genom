import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype = "uint8")

rectangle = cv.rectangle(blank.copy(),(100,100),(300,300),255,-1)
circle = cv.circle(blank.copy(),(200,200),120,255,-1)

cv.imshow("rectangle",rectangle)
cv.imshow("circle",circle)

# bitwise and 1-1 intersection
# her ikisindede 1 ise 1 dir.
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow("and",bitwise_and)

# bitwise or 1 non intersection and intersection
# butun 1 olan yerler
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow("or",bitwise_or)

# bitwise or 1 non intersection
# kesismeyen bolgeler hem 1 hem 0 olcak
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow("xor",bitwise_xor)

# bitwise not  tersini alir
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow("not",bitwise_not)

cv.waitKey(0)

import cv2 as cv

img = cv.imread("resources\photos\cats.jpg")
cv.imshow("cats",img)

# Averaging burada cerceve etrafindaki piksel ort. alinir
average = cv.blur(img,(3,3))
cv.imshow("average",average)

# Gaussian Blur   agirlik verir.
gaussian = cv.GaussianBlur(img,(3,3),0)
cv.imshow("gaussian",gaussian)
# gaussian blur da bulanikligi az olma sebebi agirlik vermesidir.

# Median Blur
median = cv.medianBlur(img,3)
cv.imshow("median",median)  # kucuk gurultu azaltmada etkili

# Bilateral
bilateral = cv.bilateralFilter(img,10,35,25)
cv.imshow("bilateral",bilateral)

cv.waitKey(0)
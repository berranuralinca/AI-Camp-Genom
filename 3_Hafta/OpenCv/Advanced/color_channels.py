# Renk Kanalları
# resmi renklere gore bolmeye yarar.

import cv2 as cv
import matplotlib.pyplot as plt 
import numpy as np

img = cv.imread("resources\photos\park.jpg")
cv.imshow("img",img)

blank = np.zeros(img.shape[:2],dtype = "uint8")

b,g,r = cv.split(img)   # renk kanallarina ayirdik

# renk kanallarini birlestirdik
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow("blue",blue)
cv.imshow("green",green)
cv.imshow("red",red)

print(img.shape)  # acik olan bolgelerde bu pikseller daha yogun
print(b.shape)
print(g.shape)
print(r.shape)

# merged color channels 
merged = cv.merge([b,g,r])
cv.imshow("merged",merged)

cv.waitKey(0)
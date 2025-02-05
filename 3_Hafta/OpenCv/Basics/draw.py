import cv2 as cv  # import etme
import numpy as np

# bos resim
blank = np.zeros((500,500,3),dtype="uint8")   # bos resim
cv.imshow("blank",blank)
cv.waitKey(0)

# kedi resmi
img = cv.imread("resources/photos/cat.jpg") # goruntuyu okur ve img degiskenine yukler.
cv.imshow("Cat",img)  # cat basligiyla resmi bir pencerede goruntuler.
cv.waitKey(0)  # bir tusa basilana kadar bekler

# bir bolgeyi boyamak
# yesil resim
blank[:] = 0,255,0  # tum sutun ve satirlari sec
cv.imshow("green",blank)
cv.waitKey(0)

# dikdortgen cizmek
blank[:] = 0,0,0  # tumu siyah
startpoint = (100,100)  # ilk nokta
endpoint = (300,300)  # son nokta
color = (0,25,255)
thickness = cv.FILLED  # kalinlik
cv.rectangle(blank,startpoint,endpoint,color,thickness)  # dikdortgen ciz
cv.imshow("rectangle",blank)
cv.waitKey(0)

# daire cizmek
center = (250,250)  # merkezi
color = (5,5,5)
thickness = cv.FILLED
cv.circle(blank,center,50,color,thickness)
cv.imshow("circle",blank)
cv.waitKey(0)

# cizgi cizmek
firstpoint = (210,250)
secondpoint = (290,250)
color = (0,25,255)
thickness = 5  # cizgi kalinligi
cv.line(blank,firstpoint,secondpoint,color,thickness)
cv.imshow("line",blank)
cv.waitKey(0)

# yazi yazmak
text ="B_"
point = (130,175)
font = cv.FONT_HERSHEY_DUPLEX  # farkli fontlar icin
fontscale = 3  # yazi buyuklugu
color=(0,0,0)
thickness=20  # kalinlik
cv.putText(blank,text,point,font,fontscale,color,thickness)
cv.imshow("write",blank)
cv.waitKey(0)


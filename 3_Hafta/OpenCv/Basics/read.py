# Reading İmages and Videos

import cv2 as cv  # import etme

# Read Photos
# kucuk resim

img = cv.imread("resources/photos/cat.jpg") # goruntuyu okur ve img degiskenine yukler.

cv.imshow("Cat",img)  # cat basligiyla resmi bir pencerede goruntuler.

cv.waitKey(0)  # bir tusa basilana kadar bekler

# buyuk resim

img = cv.imread("resources/photos/cat_large.jpg") # goruntuyu okur ve img degiskenine yukler.

cv.imshow("Cat",img)  # cat basligiyla resmi bir pencerede goruntuler.

cv.waitKey(0)  # bir tusa basilana kadar bekler

# resim ekrandan tasar.Duzeltme daha sonra yapilacak.



# Read Videos

capture = cv.VideoCapture("resources/videos/dog.mp4")   # cv.VideoCapture() fonksiyonu, bir video dosyasini acmak veya bir kameraya baglanmak icin kullanilir
# burada video dosyasi capture degiskenine atanmis
while True:  # dongu video bitene kadar ya da "d" tusuna basilana kadar devam eder.
    isTrue,frame = capture.read()   # isTrue okunan kare basariliysa veya video sonuna gelinmediyse True dondurur.
    cv.imshow("dog",frame)          # frame karelerin oldugu bir matris, imshow() ile okunan kareler gosterilir.

    if cv.waitKey(20) & 0xFF==ord("d"):  # video bittiyse veya d tusuna basilirsa dongu biter.
        break
capture.release()  # capture serbest birakir ,kaynaklari serbest birakma
cv.destroyAllWindows()  # acik tum pencereleri kapatir.
cv.waitKey(0)

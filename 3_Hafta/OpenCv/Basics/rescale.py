import cv2 as cv



def rescaleFrame(frame, scale=0.75):   # 0.75 olceklendirme
    width = int(frame.shape[1] * scale)  # genisligi 0.75 ile carpar
    height = int(frame.shape[0] * scale)  # yuksekligi 0.75 ile carpar
    dimensions = (width, height)   # boyutlandirma icin tuple olusturur
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) # frame,istenen yuks. ve genis. ,goruntuyu kuculturken kaliteyi korumak.

# video olceklendirme
capture = cv.VideoCapture("resources/videos/dog.mp4")   # cv.VideoCapture() fonksiyonu, bir video dosyasini acmak veya bir kameraya baglanmak icin kullanilir
# burada video dosyasi capture degiskenine atanmis
while True:  # dongu video bitene kadar ya da "d" tusuna basilana kadar devam eder.
    isTrue,frame = capture.read()   # isTrue okunan kare basariliysa veya video sonuna gelinmediyse True dondurur.
    frame_resized = rescaleFrame(frame)   # frame i boyutlandir ve tekrar ata.
    cv.imshow("dog",frame_resized)          # frame_resized karelerin oldugu bir matris, imshow() ile okunan kareler gosterilir.

    if cv.waitKey(20) & 0xFF==ord("d"):  # video bittiyse veya d tusuna basilirsa dongu biter.
        break
capture.release()  # capture serbest birakir ,kaynaklari serbest birakma
cv.destroyAllWindows()  # acik tum pencereleri kapatir.
cv.waitKey(0) 


# buyuk kedi resmini olceklendirme

frame = cv.imread("resources/photos/cat_large.jpg") # goruntuyu okur ve img degiskenine yukler.
frame_resized = rescaleFrame(frame,0.3)
cv.imshow("Cat",frame_resized)  # cat basligiyla resmi bir pencerede goruntuler.

cv.waitKey(0)  # bir tusa basilana kadar bekler


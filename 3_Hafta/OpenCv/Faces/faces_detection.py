import cv2 as cv

# > OpenCV > data > face_haarcascade_default dosyasi kopyalanir.

# tek bir kisi
# img = cv.imread("resources\photos\lady.jpg")  # okunacak resim
# cv.imshow("lady",img)

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)  # grilendirme
# cv.imshow("gray",gray)

# haar_cascade = cv.CascadeClassifier("Faces\haar_faces.xml") # yuz tanimlama icin kullanilan algoritma

# faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)  # gri tonlamada yuzleri tespit etmek
# # face_rect bulunan her yuz icin x,y,w,h icerir.

# print(f"number of faces found = {len(faces_rect)}") # bulunan yuz sayisini ekrana yazdirir.

# for (x,y,w,h) in faces_rect:
#     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)  # orjinal resimde bulunan yuzler icin dikdortgen cizer.
# cv.imshow("faces",img)


# cv.waitKey(0)


# # birden fazla kisiyi bulma
# img = cv.imread("resources\photos\group 2.jpg")  # okunacak resim
# cv.imshow("group 2",img)

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)

# haar_cascade = cv.CascadeClassifier("Faces\haar_faces.xml")

# faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=6)

# print(f"number of faces: {len(faces_rect)}")

# for(x,y,w,h) in faces_rect:
#     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
# cv.imshow("faces",img)

# cv.waitKey(0)

# daha cok kisi

img = cv.imread("resources\photos\group 1.jpg")  # okunacak resim
cv.imshow("group 1",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

haar_cascade = cv.CascadeClassifier("Faces\haar_faces.xml")

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)

print(f"number of faces: {len(faces_rect)}")

for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow("faces",img)

cv.waitKey(0)

import numpy as np
import cv2 as cv


haar_cascade = cv.CascadeClassifier("Faces/haar_faces.xml")   # yuz tanima

people = ["Alan Rickman","Alfred Enoch","Bonnie Wright","Daniel Radcliffe",
          "Emma Watson","Evanna Lynch","Helena Bonham Carter","Julie Walters",
          "Maggie Smith","Mark Williams","Matthew Lewis","Michael Gambon",
          "Ralph Fiennes","Robbie Coltrane","Rupert Grint","Tom Felton"]

features = np.load("features.npy",allow_pickle=True)
labels = np.load("labels.npy")

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

img =  cv.imread("resources\photos\danielandemma.jpeg") # goruntuyu okur ve img degiskenine yukler.



gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("persons",gray)

faces_rect = haar_cascade.detectMultiScale(gray,1.38,6)

for ( x,y,w,h) in faces_rect:
    faces_roi = cv.resize(gray[y:y+h,x:x+w],(100,100))  

    label, confidence = face_recognizer.predict(faces_roi)
    print(f"label: {people[label]} with a confidence of {confidence}")

    text_x = x  # yuzun sol ust kosesi
    text_y = y + h + 20  # yuzun altinda biraz bosluk
    
    cv.putText(img,str(people[label]),(text_x,text_y),cv.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),thickness=2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow("detected faces",img)
cv.waitKey(0)


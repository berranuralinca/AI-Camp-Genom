import os
import cv2 as cv
import numpy as np

# taninacak kisiler
people = ["Alan Rickman","Alfred Enoch","Bonnie Wright","Daniel Radcliffe",
          "Emma Watson","Evanna Lynch","Helena Bonham Carter","Julie Walters",
          "Maggie Smith","Mark Williams","Matthew Lewis","Michael Gambon",
          "Ralph Fiennes","Robbie Coltrane","Rupert Grint","Tom Felton"]
# usttekini yapmanin bir yolu
# p = []
# for i in os.listdir(r"C:\Users\berra\OneDrive\Masaüstü\AI Camp Genom\3_Hafta\OpenCv\resources\faces_celebrity"):
#     p.append(i)

# print(p)

# yuz algilama
haar_cascade = cv.CascadeClassifier("Faces/haar_faces.xml") 
# unlu fotograflarinin bulundugu klasor
DIR = r"resources\faces_celebrity"

# algilanan yuz ozellikleri pixel gibi
features = []
# yuzun kime ait oldugu
labels = []

# egitim verisini hazirlama
def create_train():
    for person in people: # her unlu icin
        path = os.path.join(DIR,person) # bulundugu dosyaya gider
        label = people.index(person)  # indexini labela ekler
     
        for img in os.listdir(path):  # klasordeki her fotograf icin
            img_path = os.path.join(path,img)  # fotograf yolu

            img_array = cv.imread(img_path)  # fotografı okur
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)  # gri tonlamaya cevirir
            
            # yuzleri algilar
            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

            # algilanan her yuz icin
            for(x,y,w,h) in faces_rect:
                faces_roi = cv.resize(gray[y:y+h,x:x+w],(100,100)) # yuz bolgesini kırpar,kaydeder
                features.append(faces_roi)  # ozelliklere ekler
                labels.append(label)  # yuz etiketini ekler
               


create_train() # egitim verisi olusturdu

features = np.array(features,dtype="object")
labels = np.array(labels)

# yuz tanima modelini egitme
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")
# bizim egitim verisi ile egitir.
face_recognizer.train(features,labels)

print(f"length of the features:  {len(features)}")
print(f"length of the labels:  {len(labels)}")
# egitilmis modeli kaydeder
face_recognizer.save("face_trained.yml")
np.save("features.npy",features)
np.save("labels.npy",labels)
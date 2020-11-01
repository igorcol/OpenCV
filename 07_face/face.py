from cv2 import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

#img = cv2.imread('test.jpeg')
cap = cv2.VideoCapture(0)
green = (0,255,0); white = (255,255,255)

while True:
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x,y, w,h) in faces:
        cv2.putText(img, "Person", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
        cv2.rectangle(img, (x,y), (x+w, y+h), green, 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
    cv2.imshow('face', roi_color)
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
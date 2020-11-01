import numpy as np
from cv2 import cv2

img = cv2.imread('shapes.png')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, tresh = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours ,_ = cv2.findContours(tresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 2)
    x = approx.ravel()[0]; y = approx.ravel()[1] - 5

    
    if len(approx) == 3:
        cv2.putText(img, "Triangulo", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))

    elif len(approx) == 4:
        (x , y, w, h) = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv2.putText(img, "Quadrado", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))
        else:
            cv2.putText(img, "Retangulo", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))

    elif len(approx) == 5:
        cv2.putText(img, "Pentagono", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))

    elif len(approx) == 10:
        cv2.putText(img, "Decagono", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))

    else:
        cv2.putText(img, "Circulo", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))


cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
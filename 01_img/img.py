import cv2
from cv2 import cv2

# Lê a imagem
img = cv2.imread('lena.png', -1) 

# Mostra a imagem
cv2.imshow('image', img)
k = cv2.waitKey(0)

if k == ord('s'): # Salva a foto
    cv2.imwrite('img_copy.png', img)
    cv2.destroyAllWindows()
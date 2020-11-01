import numpy as np
from cv2 import cv2

img = cv2.imread('lena.png', -1)
img = np.zeros([512, 512, 3], np.uint8) # Imagem preta

# Linha
img = cv2.line( img, (0,0), (255,255), (255, 0, 0), 2 ) 

# Seta
img = cv2.arrowedLine( img, (0,255), (255,255), (0, 255, 0), 2 ) 

# Quadrado
img = cv2.rectangle(img, (384,0), (510, 128), (0, 0, 255), 2)

# Circulo
img = cv2.circle(img, (447, 63), (63), (255, 255, 255), 2)

# Texto
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Texto', (10,500), font, 4, (0, 255, 0), 3, cv2.LINE_AA)


cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
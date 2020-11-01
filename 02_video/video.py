from cv2 import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video.mp4', fourcc, 30, (640,480) )

while True: # Se for arquivo, cap.isOpened()
    ret, frame = cap.read()

    if ret == True:
        out.write(frame) # Grava o vídeo

        cv2.imshow('window', frame)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break

    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
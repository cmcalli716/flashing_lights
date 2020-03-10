import cv2
import numpy as np

cap = cv2.VideoCapture('sample1.tif')
fourcc = cv2.VideoWriter_fourcc(*'TIFF')
out = cv2.VideoWriter('sample1.tif', fourcc, 20.0, (640,480))
while True:
    ret, frame = cap.imreadmulti()
    out.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

import cv2
import numpy as np

# Cargar la imagen o video
frame = cv2.imread('marco.png')  # O carga de un video

# Definir los puntos de la ROI
# Formato: (x, y)
puntos_roi = [(68, 62), (75, 62), (105, 430), (65, 430)]  

# Crear una máscara negra del mismo tamaño que la imagen
mask = np.zeros_like(frame)

# Dibujar la ROI en la máscara
cv2.fillPoly(mask, [np.array(puntos_roi)], (255, 255, 255))

# Aplicar la máscara a la imagen original
roi_frame = cv2.bitwise_and(frame, mask)

# Mostrar la imagen con la ROI
cv2.imshow('ROI', roi_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

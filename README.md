En las carpetas presente se encuentra dividadas las partes del proyecto

Interfaz: tal como lo dice la carpeta solo se encuentra la interfaz donde se puede subir el video y se aplicara la detccion por color a la linea de fondo, se recomienda usar el video de prueba ya que esta ajustado para esos colores.

Yolov8: Incluye un video de prueba para el seguimiento del balon con el modelo entrenado ambos dentro de la carpeta con el codigo de prueba

Interfaz+Yolov8: Es la union de las dos anteriores donde a la interfaz se hace la seleccion del video, se procesa por el modelo entrenado y finalmente se ve el video ya procesado mas la detccion por color de la linea de fondo.

Región de interes(ROI): En esta carpeta se encuentra el codigo python "regiondeinteres.py"y la imagen "marco.png" con la cual se realizo la ROI. Además se utilizara para mejorar la precisión en el uso de algunas de las dos técnicas de geometría proyectiva que disponemos.

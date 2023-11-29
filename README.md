En las carpetas presente se encuentra dividadas las partes del proyecto

- Interfaz: tal como lo dice la carpeta solo se encuentra la interfaz donde se puede subir el video y se aplicara la detccion por color a la linea de fondo, se recomienda usar el video de prueba ya que esta ajustado para esos colores.

- Yolov8: Incluye un video de prueba para el seguimiento del balon con el modelo entrenado ambos dentro de la carpeta con el codigo de prueba

- Interfaz+Yolov8: Es la union de las dos anteriores donde a la interfaz se hace la seleccion del video, se procesa por el modelo entrenado y finalmente se ve el video ya procesado mas la detccion por color de la linea de fondo.

- Región de interes(ROI): En esta carpeta se encuentra el codigo python "regiondeinteres.py" y la imagen "marco.png" con la cual se realizo la ROI. Además se utilizara para mejorar la precisión en el uso de algunas de las dos técnicas de geometría proyectiva que disponemos.

**Como ejecutar el codigo**
Para esto lo primero es dirigirse a la carpeta de "Interfaz+YoloV8", y abrir el archivo "versionFinal_Interfaz+yolov8.ipynb", cabe mencionar que lo primero es tener ejecutado el kernel de jupyter en la terminal usando "jupyter notebook" en el simbolo del sistema. Las librerias que son necesarias para ejecutar el codigo se pueden instalar ejecutando las siguientes lineas de codigo dentro de versionFinal_Interfaz+yolov8.ipynb (antes de la ejecucion del proyecto):
!pip install pillow
!pip install tk
!pip install python-vlc
!pip install ultralytics-yolov5
Antes de iniciar el codigo es recomendable leer el readme.md presente dentro de la carpeta Interfaz+Yolov8 ya que este se especializa en explicar mas a detalle el funcionamiento.

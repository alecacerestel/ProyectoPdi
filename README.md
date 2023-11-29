# Carpetas del proyecto

- Interfaz: tal como lo dice la carpeta solo se encuentra la interfaz donde se puede subir el video y se aplicara la detccion por color a la linea de fondo, se recomienda usar el video de prueba ya que esta ajustado para esos colores.

- Yolov8: Incluye un video de prueba para el seguimiento del balon con el modelo entrenado ambos dentro de la carpeta con el codigo de prueba

- Interfaz+Yolov8: Es la union de las dos anteriores donde a la interfaz se hace la seleccion del video, se procesa por el modelo entrenado y finalmente se ve el video ya procesado mas la detccion por color de la linea de fondo.

- Región de interes(ROI): En esta carpeta se encuentra el codigo python "regiondeinteres.py" y la imagen "marco.png" con la cual se realizo la ROI. Además se utilizara para mejorar la precisión en el uso de algunas de las dos técnicas de geometría proyectiva que disponemos.

# Como ejecutar el código
Para esto lo primero es dirigirse a la carpeta de "Interfaz+YoloV8", y abrir el archivo "versionFinal_Interfaz+yolov8.ipynb", cabe mencionar que lo primero es tener ejecutado el kernel de jupyter en la terminal usando "jupyter notebook" en el símbolo del sistema. Las librerías que son necesarias para ejecutar el código se pueden instalar ejecutando las siguientes líneas de codigo dentro de versionFinal_Interfaz+yolov8.ipynb (antes de la ejecución del proyecto):

````
!pip install pillow
!pip install tk
!pip install python-vlc
!pip install ultralytics-yolov5
!pip install opencv-python-headless
!pip install numpy
````

# Explicacion y funcionamiento del código:

## Indicaciones importantes
Para el correcto funcionamiento del codigo es necesario considerar algunas cosas.

1. Los archivos deben estar presente siempre en la misma carpeta.

2. El tiempo de ejecución varía según la duración del video que se desea reproducir, y de los frames que lo constituyan.

3. Para reiniciar el video, es recomendable el uso de "Stop" y luego "Start".

4. No es necesario presionar el botón de "Start" para iniciar la primera reproducción del video, luego si se desea repetir, es posible reiniciarlo aplicando la indicacion número 3.

5. Es recomendable usar alguno de los videos de prueba, o idealmente, un video con un balón de volleyball presente.

6. Si llega a haber algún problema con la instalación de una librería o función, es importante asegurarse de tener presente el archivo de Homografia.py presente en la carpeta, además de haber realizado los pip install indicados en el READme del proyecto.
## Guia de la interfaz

- La interfaz tendra un botón que indica "select file", con el cual es posible elegir el video que se desea procesar

- Una vez este seleccionado el video podemos usar los demas botones de la interfaz, dentro de los cuales se haya:
  1. El boton "Pause/Resume" cuya función es la de detener o continuar la reproducción del video
  2. El botón "Stop" que detiene por completo el video y el botón "Start" cuya función es iniciar la reproducción del video
  3. Los botones "Fast forward" y "Rewind" que sirven para saltar una cierta cantidad de segundos dentro del video (hacia atrás o hacia adelante).
  4. El botón "Apply YOLO" cuya función es la de iniciar el procesamiento de YOLO para la detección del balón de volleyball.
  5. El botón de "Take screenshot" para tomar una captura de un momento exacto del video (un frame)

#### Procesamiento YOLO

Una vez este iniciado el video, para dar comienzo al uso de YOLO es necesario presionar el botón de "Apply YOLO", cabe mencionar que el procesamiento toma tiempo dependiendo de las características del computador donde se ejecuta el proyecto, como de las características del video.

#### Empleo de Homografía

Para obtener el plano 2D de un momento exacto del video, es necesario pausar el video, usar el botón "Take screenshot" y luego marcar 4 puntos con el mouse, encerrando en un cuadro formado por los 4 puntos, el lugar donde se desea realizar la homografía. Una vez esten seleccionados los 4 puntos, se presiona el botón de "Stop" y en pantalla aparece el cuadro marcado con la funcion de homografia ya aplicada.

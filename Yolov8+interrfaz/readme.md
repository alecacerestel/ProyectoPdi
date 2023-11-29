# Explicacion y funcionamiento del codigo:

## Indicaciones importantes
Para el correcto funcionamiento del codigo es necesario considerar algunas cosas.

1. Los archivos deben estar presente siempre en la misma carpeta.

2. El tiempo de ejecución varía según la duración del video que se desea reproducir, y de los frames que lo constituyan.

3. Para reiniciar el video, es recomendable el uso de "Stop" y luego "Start".

4. No es necesario presionar el botón de "Start" para iniciar la primera reproducción del video, luego si se desea repetir, es posible reiniciarlo aplicando la indicacion número 3.

5. Es recomendable usar alguno de los videos de prueba, o idealmente, un video con un balón de volleyball presente.

6. Si llega a haber algún problema con la instalación de una librería o función, es importante asegurarse de tener presente el archivo de Homografia.py presente en la carpeta, además de haber realizado los pip install indicados en el READme del proyecto.
# Guia de la interfaz

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

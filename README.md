# ProyectoPdi

# Descripción del problema 
En la mayoría de los deportes, es esencial mantener un área de juego bien definida para garantizar que las reglas se cumplan adecuadamente. En muchas ocasiones, la determinación de si una pelota o balón está dentro o fuera de esta área recae en los árbitros, lo que puede dar lugar a controversias y decisiones subjetivas. Sin embargo, ya existen soluciones tecnológicas exitosas en otros deportes que podrían aplicarse al voleibol para mejorar la precisión y la justicia en las decisiones arbitrales. 

En un esfuerzo constante por mejorar la justicia y la precisión en las decisiones arbitrales en el voleibol, se han explorado diversas soluciones tecnológicas que han demostrado su eficacia en otros deportes. En este contexto destacan algunas soluciones tecnologicas: 

* Ojo de Halcón: 
Este sistema se basa en un conjunto de cámaras de alta velocidad que rastrean la trayectoria de la pelota con gran precisión. 

* Sistema Cairos: 
Similar al VAR del fútbol, este sistema utiliza cámaras y software para determinar si un balón ha cruzado la línea de gol. En el voleibol, podría adaptarse para verificar si la pelota ha tocado el suelo dentro o fuera de la cancha.


## Propuesta de solución
Como equipo planteamos la siguiente solución. Desarrollar un sistema de selección de frames en videos mediante el cual podremos extraer el momento de contacto entre la pelota y la superficie. Esta solución se basará en procesamiento de imágenes para proporcionar un frame de alta calidad que capture el instante de la interacción.

## Estado del arte/técnica y sus referencias
* Filtrado de Imágenes:
Utilizar filtros para realzar características específicas. Por ejemplo, se pueden aplicar filtros para resaltar bordes y cambios en la intensidad de los colores. (AQUI AGREGREN NOMBRE DE FILTROS UTILEZ Y LA FOTO DE LA PPT)

* Segmentación de Objetos: 
Si segmentamos una imagen del video en la cual está nuestro punto de interés, estaremos aislando la pelota del fondo de la cancha en el video. Esto simplifica la tarea de identificar cuándo la pelota está en contacto con la línea.

* Cambio de posición:
Si un objeto, como una pelota, se mueve de manera notable, generará grande cambios en los píxeles de la imagen entre un frame y el siguiente. Por lo que, sabiendo esto, podriamos desarrollar un algoritmo capaz que identificar estos cambios.

* Deep learning (Opcional, lo estamos conversando):
Encontramos un proyecto bastante similar, el cual enseñaba a una computadora a seguir una imagen. Nos parece algo muy útil, pero no entendemos muy bien esta tecnología ni cómo debemos entrenarla. (Dejar el link)



# Requisitos del sistema
## Requisitos funcionales

## Requisitos No funcionales
EN PROCESO

## Requisitos de interfaces
## Requisitos de ambiente
## Hardware de desarrollo
## Software de desarrollo
## Datasets e Imágenes/Videos de Prueba
Aquí se encontrarán links a distintos repositorios o información que nos pueda ser relevante para el proyecto. 
## Perfiles de usuario
Ya que nuestro proyecto se enfoca en el volleyball, los usuariso esperados serán participes de este deporte. 

* Árbitros:
Los árbitros son el usuario final principal, ya que, utilizarían el sistema para tomar decisiones precisas en situaciones que lo ameriten.

* Entrenadores y personal técnico: 
Todo el personal de un equipo debería poder acceder a este sistema, con el objetivo de revisar y analizar el rendimiento del equipo, asismismo identificar momentos claves. 

# Planificacion del proyecto

## Objetivo general
## Objetivos Específicos
## Actividades y logros
## Carta Gantt.

# Acerca de los archivos
Cuando tengamos archivos del proyecto aqui se encontrará una pequeña descripción de cada uno.


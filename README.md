# Image-Processing
En este repositorio compartiremos el código para las imágenes obtenidas de los experimentos las cuales serán subidas.

## Introducción

En nuestro proyecto contemplamos la creación de una máquina que tome las fotos de manera automática para luego ser subidas a la plataforma. Para ello necesitamos un sistema de visión artificial que nos ayude con esta tarea. Unas de las posibles problemáticas será reconocer la placa de Petri y la población de bacterias que hay dentro. Otras cosas interesantes sería estimar  la cantidad de bacterias o el área que ocupa. 

En este repositorio proponemos un método para detectar de forma automática mediante técnicas de inteligencia artificial la placa de Petri y dar una estimación del área que ocupan las bacterias.


## Nuestro algoritmo

Nuestro algoritmo consiste primeramente en detectar la placa de Petri para ello usaremos la transformada de Hough. Como vemos en la siguiente imagen podemos detectar la placa de cada foto tomada de los experimentos:

[Imagen]

Una vez que nos quedamos con la placa de Petri optamos por una binarización de la imagen, de tal manera estableciendo un umbral podemos observar qué es bacteria y qué es fondo. En este algoritmo, optamos por una umbralización fija pero el algoritmo podría aprender un umbral en función de la luminosidad y condiciones de la fotografía de tal manera que obtuvieramos una representación más fina, la cual dejaremos para trabajos futuros.

Una vez que hemos detectado las bacterias contaremos los pixeles que se han activado y calcularemos el área que ocupan.

[Imagen]

## Transformada de Hough

En esta sección, explicaremos más detenidamente la herramienta de inteligencia artificial que hemos utilizado para
 detectar la placa de petri, la llamada transformada de Hough.
 
 
 ## Binarización

# Image-Processing
En este repositorio compartiremos el código para las imágenes obtenidas de los experimentos las cuales serán subidas.

## Introducción

En nuestro proyecto contemplamos la creación de una máquina que tome las fotos de manera automática para luego ser subidas a la plataforma. Para ello necesitamos un sistema de visión artificial que nos ayude con esta tarea. Unas de las posibles problemáticas será reconocer la placa de Petri y la población de bacterias que hay dentro. Otras cosas interesantes sería estimar  la cantidad de bacterias o el área que ocupa. 

En este repositorio proponemos un método para detectar de forma automática mediante técnicas de inteligencia artificial la placa de Petri y dar una estimación del área que ocupan las bacterias.


## Nuestro algoritmo

Nuestro algoritmo consiste primeramente en detectar la placa de Petri para ello usaremos la transformada de Hough. Como vemos en la siguiente imagen podemos detectar la placa de cada foto tomada de los experimentos:

!(https://github.com/TheOpenBacteriaProject/Image-Processing/blob/master/1.png)

Una vez que nos quedamos con la placa de Petri optamos por una binarización de la imagen, de tal manera estableciendo un umbral podemos observar qué es bacteria y qué es fondo. En este algoritmo, optamos por una umbralización fija pero el algoritmo podría aprender un umbral en función de la luminosidad y condiciones de la fotografía de tal manera que obtuvieramos una representación más fina, la cual dejaremos para trabajos futuros.

Una vez que hemos detectado las bacterias contaremos los pixeles que se han activado y calcularemos el área que ocupan.

[Imagen]

## Transformada de Hough

En esta sección, explicaremos más detenidamente la herramienta de inteligencia artificial que hemos utilizado para
 detectar la placa de petri, la llamada transformada de Hough. Este es un método de extracción de características de imágenes para detectar formas que sean expresables matemáticamente. En primer lugar, fue propuesto para rectas aunque puede ser extendido para cualquier forma arbitraria (solo necesitamos una parametrización de esta forma). Una vez tenemos la parametrización de la forma deseada y queremos aprender los parámetros de la forma. En este caso, queremos encontrar circunferencias, dada la imagen queremos como resultado el radio y centro de la circunferencia que representa a la placa de petri. 
 En nuestro caso la parametrización de una circunferencia sería: 
 
 !(https://latex.codecogs.com/gif.latex?(x-x_{0})^{2}&space;&plus;&space;(y-y_{0})^{2}&space;=&space;r^{2})
 
 De tal manera que nuestro espacio paramétrico sería https://latex.codecogs.com/gif.latex?(x_{0},y_{0},r). Tenemos que encontrar los valores de estos parámetros de tal manera que nos representara la placa de petri de las imágenes.
 
 La idea del algoritmo es binarizar la imagen detectando aristas de la siguiente manera:
 [aristas]
 Podemos usar para esto, por ejemplo, el detector de Canny. El cual sirve para revelar los bordes de una imagen.
 
 Una vez que tenemos una imagen binaria (blanco y negro) en la cual tenemos representadas las aristas, tenemos que ir "probando" con la figura que hemos elegido usando distintos valores de los parámetros. Se llama transformada, ya que buscaremos los posibles valores de los parámetros en el espacio paramétrico. Ahí buscaremos las figuras que se intersecan por lo tanto cuantas más intersecciones haya más votos hay para que por ahí pase nuestra figura. Un ejemplo ilustrativo de lo descrito es lo siguiente:

[Explicacion]

En nuestro caso, hemos usado la función de [OpenCV](https://opencv.org/) (una librería de software libre para visión por computador que está implementada entre otros lenguajes en python) para encontrar el círculo correspondiente a la placa de petri. Hemos elegido un rango entre el cual esperamos que se encuentre la placa y una distancia entre centros muy grande para que solo nos elija el círculo con más votos que será el de la placa.
 
 ## Binarización

Con la binarización lo que buscamos es poder distinguir entre bacterias y fondos. En primer lugar pasamos la imagen a escala de grises. Las bacterias tienen un color gris más claro que el fondo por lo que establecemos un umbral de tal manera que si el valor del pixel es mayor que ese umbral lo activamos al máximo de brillo, en otro caso, lo desactivamos dejándolo en negro. Con este procedimiento tenemos una imagen de tal manera que los colores blancos corresponden a las bacterias y el negro al fondo. Así podemos calcular el área que ocupa las bacterias y ver donde se distribuyen. Ya que sabemos que el diámetro de la placa de petri es (y suele ser) de 9cm.


## Probar el código

Hemos subido el [código desarrollado en Python](https://github.com/TheOpenBacteriaProject/Image-Processing/blob/master/main.py), para obtener nuestros resultados, sólamente tendrás que ejecutarlo sobre las imágenes subidas en la carpeta test.
## Bibliografía

– Ballard, D. H. *Generalizing the Hough Transform to Detect Arbitrary
Shapes*, Pattern Recognition 13:111-122, 1981.

– Illingworth, J. and J. Kittler, *Survey of the Hough Transform*, Computer
Vision, Graphics, and Image Processing, 44(1):87-116, 1988

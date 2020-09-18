# revivir-fotos
Dar color a imágenes en blanco y negro de épocas de antaño con ayuda de Deep Learning con la automatización de pyautogui. 

El objetivo del proyecto es utilizarla cuando tengas una cantidad relativamente pequeña de imágenes (considero superior a 100 imágenes) y tengas muy poca noción de variables de entorno, configuración de access_key, etc. Sí crees que tenes los conocimientos necesarios y tenés una alta carga de datos mejor implementa la librería.

# Resultados post-curado

![compara1](https://github.com/cabustillo13/Revivir-Imagenes/blob/master/Ejemplos/comparar1.png)

![compara0](https://github.com/cabustillo13/Revivir-imagenes/blob/master/Ejemplos/comparar0.png)

![compara2](https://github.com/cabustillo13/Revivir-imagenes/blob/master/Ejemplos/comparar2.png)

# Fuente de las imágenes

Todas las imágenes fueron obtenidas del respositorio [LILKAYA](https://lilkaya.unah.edu.hn/) de la Universidad Nacional Autónoma de Honduras. 

# Preguntas y respuestas

**¿Es lento este proceso?** 

No. Al ejecutar el programa tiene varios delays de 1 segundo para poder apreciar cada etapa, una vez que se apreció y entendió cómo funciona el programa se les puede quitar ese delay para que tenga su funcionamiento óptimo. También se puede alcanzar un mayor rendimiento utilizando acortadores de url como **bit.ly** para que ingrese más rápido el link. 

**¿Cuándo utilizar este programa?** 

Cuando tengas una cantidad relativamente pequeño de imágenes (unas 100 imágenes en adelante considero) y tengas muy ṕoca noción de variables de entorno, configuración de access_key, etc. Sí crees que tenes los conocimientos necesarios y tenés una alta carga de datos mejor implementa la librería.

Se puede correr estos programas desde una Raspberry u otro microprocesador para realizar acciones automáticas con la menor cantidad de recursos y energía.

**¿Puedo correr este programa directamente en mi computadora?**

No. Está configurado para las dimensiones físicas de mi equipo, por eso debe hacer un set up para su equipo.

**¿Qué otros usos puedo darle a funciones.py y polling.py?** 

* Puede ser un gran ejercicio para aprender pyautogui porque prácticamente involucra muchos de sus comandos.

* Detectar un reCAPTCHA y cargar los datos de un usuario.

* Detectar elementos de Tinder para hacer match! de manera automática.

* Responder a comentarios de venta en Facebook.

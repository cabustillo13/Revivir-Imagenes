import webbrowser
import pyautogui
import time
import funciones
import polling
import os

# Abrir una nueva ventana en el navegador
def urlNavegador():
    # Cargar url donde vamos a cargar la imagen
    webbrowser.open("<PATH TO DEMO>")

# Manejador de archivos
archivo = open("links.txt", "r")
lineas = archivo.readlines()
numeroLineas = len(lineas)
archivo.close()

for i in range(numeroLineas):

    # Abrir navegador
    urlNavegador()
    
    # Primer click
    polling.startPolling("./Recursos/photo3.png")           #Polling inicial
    pyautogui.moveTo(594, 306, 2, pyautogui.easeOutQuad)    #Da apariencia que arranca rapido el mouse y luego lento
    pyautogui.scroll(-10)
    
    # Encontrar primer casilla para hacer click
    polling.startPolling("./Recursos/photo4.png")
    funciones.encontrarBoton("./Recursos/photo8.png")
    
    # Segundo click
    polling.startPolling("./Recursos/photo5.png")
    funciones.localizarImagen("./Recursos/photo9.png")
    
    # Cargar URL en el rectangulo blanco de algorithmia
    pyautogui.typewrite("1")
    pyautogui.press("backspace")
    funciones.adaptarUrl(lineas[i])
    polling.startPolling("./Recursos/photo6.png")
    
    # Ahora nos movemos un poco hacia abajo, para encontrar el link y descargar la imagen
    funciones.localizarImagen("./Recursos/photo0.png")
    polling.startPolling("./Recursos/photo7.png")
    
    # Encontrar la imagen para guardar
    #funciones.localizarImagen("./Recursos/photo1.png")
    # Hay que cersiorarse que este la opcion de guardar
    funciones.localizarImagen("./Recursos/photo2.png")
    
    # Guardar imagen
    # Esto por defecto guardara las imagenes en descargas
    funciones.localizarImagen("./Recursos/photo11.png")
    
    # Cerrar ventana actual
    funciones.cerrarVentana()

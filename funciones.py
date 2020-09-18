import pyautogui
import time

# Determinar posicion del mouse para dar un click
# Sirve para asignas las posiciones de cada click, una vez cargadas a las demas funciones ya no lo volvemos a utilizar 
def posicionPuntero():
    time.sleep(10)                 #Esperar 10 segundos
    print(pyautogui.position())    #Capturar posicion del mouse

# Hacer click en las coordenadas encontradas
def asignarClick(valorx,valory):
    pyautogui.click(valorx, valory)

# Determinar la posicion de un boton entre muchos iguales
def encontrarBoton(pathImagen):
    for pos in pyautogui.locateAllOnScreen(pathImagen):
        
        #pos = [left,top,width,hight]
        valorx = pos[0] +pos[2]/2
        valory = pos[1] + pos[3]/2
        asignarClick(valorx,valory)
    
# Localizar imagen para darle click
def localizarImagen(pathImagen):
    # Ingresar imagen que debemos buscar
    buscarlocation = pyautogui.locateOnScreen(pathImagen)
    # Posiciones donde se encuentra el elemento buscado
    buscarpoint = pyautogui.center(buscarlocation)
    buscarx, buscary = buscarpoint
    # Hacer click en las coordenadas encontradas
    pyautogui.click(buscarx, buscary)


# Cerrar ventana actual al terminar el proceso
def cerrarVentana():
    # Para Google Chrome
    pyautogui.hotkey("ctrl","w") 

# Recordar que los comandos que usa autopygui son los de tu teclado,mause y pantalla fisica
#En mi teclado "/" es "shift+7" sino aplicara esta funcion pondria "7" en vez de "/"
def adaptarUrl(string):
    lista=list(string)   #Convertir string a lista
    cont = len(string)  #Contar cantidad de caracteres
    
    for i in range(cont):
        if (lista[i] == "/"):
            pyautogui.keyDown("shift")
            pyautogui.typewrite(lista[i])
            pyautogui.keyUp("shift")
        else:
            pyautogui.typewrite(lista[i])
    
    

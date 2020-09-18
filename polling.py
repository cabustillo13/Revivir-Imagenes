import cv2
import pyautogui
import time

# Hacer un polling hasta encontrar la imagen buscada
# Permite adaptar este programa a la velocidad de descarga de tu internet
def startPolling(pathImage):
    
    # Cargar plantilla o imagen de referencia
    plantilla = cv2.imread(pathImage,0)
    w, h = plantilla.shape[::-1]

    # Valores de inicializacion
    min_val = 1     #min_val ronda en valores menores a 1
    cont = 0
    contMax=60
    delay = 1       #1 segundos 

    while ((min_val > 0.015) or (cont==contMax)):      #Generelmente 0.015... es el valor que devuelve cuando no encuentra el objeto
    
        # Realizar screenshot de la pantalla para analizarla
        imagen = pyautogui.screenshot()
        # Para guardar cada screenshot
        imagen.save("./Recursos/screenshot.png")
    
        imagenCopy = cv2.imread("./Recursos/screenshot.png",0)
    
        metodo = eval('cv2.TM_SQDIFF_NORMED')
    
        # Aplicar coincidencia de plantillas
        res = cv2.matchTemplate(imagenCopy,plantilla,metodo)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
        top_left = min_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cont=cont+1
        time.sleep(delay)
        
        if (cont==contMax): print("Error archivo no encontrado en pantalla")

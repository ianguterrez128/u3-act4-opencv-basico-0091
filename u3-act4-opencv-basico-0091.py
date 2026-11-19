# ==============================================================================
# 0. IMPORTACIÓN DE LIBRERÍAS
# ==============================================================================
import cv2  # Importa la librería OpenCV para procesamiento de imágenes y visión artificial.
import numpy as np  # Importa NumPy para manejar las imágenes como arreglos/matrices matemáticas.
import sys  # Importa Sys para poder detener el programa de forma segura si ocurre un error.
import win32gui
import win32con 
import win32api
print("+-+-+  Ian Gutierrez NC 0091 +-+-+")
# ==============================================================================
# 1. LECTURA DE LA IMAGEN DESDE LA CARPETA
# ==============================================================================
print("\n1. LECTURA DE IMÁGENES")  # Imprime el título de la sección en la consola.
nombre_ventana = 'Gpo 3H img perro rojo ian gutierrez 0091' # linea nueva
imgperro_rojo = cv2.imread('perrorojo.png')  # Lee la imagen 'perrorojo.png' y la guarda como matriz en 'imgperro_rojo'.
# 3. crear ventana en OpenCV
cv2.namedWindow(nombre_ventana) # linea nueva


if imgperro_rojo is None:  # Verifica si la variable 'imgperro_rejo' está vacía (es decir, si no encontró el archivo).
    print("Error: No se pudo leer 'perrorojo.png'. Revisa el nombre y ubicación.")  # Muestra mensaje de error.
    sys.exit()  # Detiene inmediatamente la ejecución del programa para evitar fallos posteriores.
else:  # Si la imagen sí se cargó correctamente...
    print("Imagen cargada exitosamente.")  # Confirma en consola que la imagen está lista.
    # ==============================================================================
# 2. PROPIEDADES DE LA IMAGEN
# ==============================================================================
print("\n2. PROPIEDADES DE LA IMAGEN Ian gutierrez 0091")  # Imprime el título de la segunda sección.
height, width, channels = imgperro_rojo.shape  # Extrae el alto (filas), ancho (columnas) y canales de color de la matriz.
print(f"Dimensiones de la imagen: {width}x{height} píxeles")  # Muestra el ancho por el alto en consola.
print(f"Número de canales de color: {channels}")  # Muestra cuántos canales tiene (3 para BGR: Azul, Verde, Rojo).
print(f"Tipo de dato de la imagen: {imgperro_rojo.dtype}")  # Muestra el tipo de dato (uint8 = enteros de 0 a 255).
print(f"Total de datos/píxeles: {imgperro_rojo.size}")  # Muestra la cantidad total de valores numéricos en la matriz.
# ==============================================================================
# 3. VISUALIZACIÓN DE LA IMAGEN ORIGINAL
# ==============================================================================
print("\n3. MOSTRANDO IMAGEN ORIGINAL DEL PERRO ROJO")  # Imprime el título de la tercera sección.
print("Presiona cualquier tecla sobre la ventana de la imagen para continuar...")  # Instrucción para el usuario.
# 4. mostrar imagen 
cv2.imshow(nombre_ventana,imgperro_rojo) # linea nueva
# cv2.imshow('img perro rojo Original Ian gutierrez 0091', imgperro_rojo)  # Abre una ventana llamada 'Imagen Original' y muestra la imagen cargada.
cv2.waitKey(0)  # Pausa el programa infinitamente hasta que el usuario presione una tecla.
print("+-+-+-+ modificando pixeles 0091 +-+-+-+")
# ==============================================================================
# 4. ACCESO Y MODIFICACIÓN DE PÍXELES INDIVIDUALES
# ==============================================================================
print("\n4. ACCEDIENDO Y MODIFICANDO PÍXELES")  # Imprime el título de la cuarta sección.
pixel_img = imgperro_rojo.copy()  # Crea una copia exacta de la imagen original para no dañar la original.

y, x = 100, 150  # Define las coordenadas a analizar: fila (Y) = 100, columna (X) = 150.
pixel = pixel_img[y, x]  # Obtiene los 3 valores de color [Azul, Verde, Rojo] del píxel en esa posición.
print(f"Valor del píxel en ({x}, {y}): {pixel} (Formato BGR)")  # Imprime los valores BGR del píxel en consola.

pixel_img[y, x] = [0, 0, 255]  # Cambia el color de ese único píxel a Rojo puro (0 Azul, 0 Verde, 255 Rojo).
cv2.circle(pixel_img, (x, y), 15, (0, 255, 255), 2)  # Dibuja un círculo amarillo alrededor para poder verlo a simple vista.

cv2.imshow('Pixel Modificado ian gutierrez 0091', pixel_img)  # Muestra la imagen con el píxel alterado y señalado.
cv2.waitKey(0)  # Espera a que se presione una tecla para continuar.
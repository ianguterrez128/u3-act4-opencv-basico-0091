
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
print("\n1. LECTURA DE IMÁGENES")
nombre_ventana = 'Gpo 3H img amongus rojo ian gutierrez 0091'
imgamongus_rojo = cv2.imread('amongusrojo.png')

# 3. crear ventana en OpenCV
cv2.namedWindow(nombre_ventana)

if imgamongus_rojo is None:
    print("Error: No se pudo leer 'amongusrojo.png'. Revisa el nombre y ubicación.")
    sys.exit()
else:
    print("Imagen cargada exitosamente.")

# ==============================================================================
# 2. PROPIEDADES DE LA IMAGEN
# ==============================================================================
print("\n2. PROPIEDADES DE LA IMAGEN Ian gutierrez 0091")
height, width, channels = imgamongus_rojo.shape
print(f"Dimensiones de la imagen: {width}x{height} píxeles")
print(f"Número de canales de color: {channels}")
print(f"Tipo de dato de la imagen: {imgamongus_rojo.dtype}")
print(f"Total de datos/píxeles: {imgamongus_rojo.size}")

# ==============================================================================
# 3. VISUALIZACIÓN DE LA IMAGEN ORIGINAL
# ==============================================================================
print("\n3. MOSTRANDO IMAGEN ORIGINAL DEL AMONG US ROJO")
print("Presiona cualquier tecla sobre la ventana de la imagen para continuar...")

# 4. mostrar imagen
cv2.imshow(nombre_ventana, imgamongus_rojo)
cv2.waitKey(0)

print("+-+-+-+ modificando pixeles 0091 +-+-+-+")

# ==============================================================================
# 4. ACCESO Y MODIFICACIÓN DE PÍXELES INDIVIDUALES
# ==============================================================================
print("\n4. ACCEDIENDO Y MODIFICANDO PÍXELES")
pixel_img = imgamongus_rojo.copy()

y, x = 100, 150
pixel = pixel_img[y, x]
print(f"Valor del píxel en ({x}, {y}): {pixel} (Formato BGR)")

pixel_img[y, x] = [0, 0, 255]
cv2.circle(pixel_img, (x, y), 15, (0, 255, 255), 2)

cv2.imshow('Pixel Modificado ian gutierrez 0091', pixel_img)
cv2.waitKey(0)

# ==============================================================================
# 5. REGIÓN DE INTERÉS (ROI - REGION OF INTEREST)
# ==============================================================================
print("\n5. REGIÓN DE INTERÉS (ROI)")
roi_img = imgamongus_rojo.copy()

roi = roi_img[50:200, 100:300]
cv2.rectangle(roi_img, (100, 50), (300, 200), (0, 255, 0), 2)

cv2.imshow('Imagen con ROI marcada Ian gutierrez 0091', roi_img)
cv2.waitKey(0)

cv2.imshow('ROI Extraida (Recorte) Ian gutierrez 0091', roi)
cv2.waitKey(0)

# ==============================================================================
# 6. SEPARACIÓN Y FUSIÓN DE CANALES DE COLOR (BGR)
# ==============================================================================
print("\n6. SEPARANDO Y FUSIONANDO CANALES")
b, g, r = cv2.split(imgamongus_rojo)

cv2.imshow('Canal Azul (Escala de grises) Ian gutierrez 0091', b)
cv2.imshow('Canal Verde (Escala de grises) Ian gutierrez 0091', g)
cv2.imshow('Canal Rojo (Escala de grises) Ian gutierrez 0091', r)
cv2.waitKey(0)

zeros = np.zeros_like(b)
blue_img = cv2.merge([b, zeros, zeros])
green_img = cv2.merge([zeros, g, zeros])
red_img = cv2.merge([zeros, zeros, r])

cv2.imshow('Canal Azul (Coloreado) Ian gutierrez 0091', blue_img)
cv2.imshow('Canal Verde (Coloreado) Ian gutierrez 0091', green_img)
cv2.imshow('Canal Rojo (Coloreado) Ian gutierrez 0091', red_img)
cv2.waitKey(0)

# ==============================================================================
# 7. REDIMENSIONAMIENTO DE IMÁGENES (RESIZING)
# ==============================================================================
print("\n7. REDIMENSIONANDO IMÁGENES")
resized_img = cv2.resize(imgamongus_rojo, (400, 300))
cv2.imshow('Redimensionada a 400x300 Ian gutierrez 0091', resized_img)
cv2.waitKey(0)

half_size = cv2.resize(imgamongus_rojo, None, fx=0.5, fy=0.5)
double_size = cv2.resize(imgamongus_rojo, None, fx=1.5, fy=1.5)

cv2.imshow('Mitad de tamano (0.5x) Ian gutierrez 0091', half_size)
cv2.waitKey(0)
cv2.imshow('Ampliada (1.5x) Ian gutierrez 0091', double_size)
cv2.waitKey(0)

# ==============================================================================
# 8. ROTACIÓN DE IMÁGENES
# ==============================================================================
print("\n8. ROTANDO IMÁGENES")
height, width = imgamongus_rojo.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 1)
rotated_img = cv2.warpAffine(imgamongus_rojo, rotation_matrix, (width, height))

cv2.imshow('Imagen Rotada (45 grados) Ian gutierrez 0091', rotated_img)
cv2.waitKey(0)

# ==============================================================================
# 9. VOLTEO / ESPEJO DE IMÁGENES (FLIPPING)
# ==============================================================================
print("\n9. VOLTEANDO IMÁGENES")
horizontal_flip = cv2.flip(imgamongus_rojo, 1)
cv2.imshow('Volteo Horizontal (Espejo) Ian gutierrez 0091', horizontal_flip)
cv2.waitKey(0)

vertical_flip = cv2.flip(imgamongus_rojo, 0)
cv2.imshow('Volteo Vertical (De cabeza) Ian gutierrez 0091', vertical_flip)
cv2.waitKey(0)

both_flip = cv2.flip(imgamongus_rojo, -1)
cv2.imshow('Volteo en Ambos Ejes Ian gutierrez 0091', both_flip)
cv2.waitKey(0)

# ==============================================================================
# 10. GUARDADO DE RESULTADOS Y LIMPIEZA
# ==============================================================================
print("\n10. GUARDANDO IMAGEN RESULTANTE")
result = cv2.imwrite('rotated_image .jpg', rotated_img)

if result:
    print("Imagen rotada guardada exitosamente como 'rotated_image.jpg'")
else:
    print("Error: No se pudo guardar la imagen rotada.")

cv2.destroyAllWindows()
print("\n¡Todas las operaciones se completaron con éxito!")

import firebase_admin
from firebase_admin import credentials , db
import sys
import cv2
#Recuperamos la referencia de nuestro nuevo usuario
new_user_ref= sys.argv[4]

def abrir_camara():
    #Mostrar Datos de la interfaz
    nombre = sys.argv[1]
    direccion = sys.argv[2]
    codigo_acceso = sys.argv[3]
    print(nombre)
    print(direccion)
    print(codigo_acceso)
    # Inicializar la cámara
    cap = cv2.VideoCapture(0)  # 0 es la cámara predeterminada
    while True:
        # Capturar frame por frame
        ret, frame = cap.read()

        # Mostrar el frame en una ventana
        cv2.imshow('Camara', frame)

        # Detener la ejecución si se presiona 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            tomar_foto("fotos/foto.jpg")
            break

    # Liberar la cámara y cerrar la ventana
    cap.release()
    cv2.destroyAllWindows()


def tomar_foto(nombre_archivo):
    # Inicializar la cámara
    cap = cv2.VideoCapture(0)  # 0 es la cámara predeterminada
    # Capturar un solo fotograma
    ret, frame = cap.read()
    # Guardar la imagen
    cv2.imwrite(nombre_archivo, frame)
    # Liberar la cámara
    cap.release()
# Abrir la cámara
abrir_camara()
# Llamar al método para tomar una foto y guardarla como "foto.jpg"




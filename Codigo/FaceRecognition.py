#Importar librerias
#Face recognition: sirve para el reconocimiento facial

import cv2 
import numpy as np
import face_recognition as fr
import os 
import random
from datetime import datetime
import face_recognition_models


#Acceder a la carpeta en donde se tienen guardadas las imagenes (AQUI TENDRIA QUE SER DE LA BASE DE DATOS)
path = 'C:/Users/jocel/Documents/project_SCRUM/Codigo/imagenes_prueba'
images = [] #almacena todas las imagenes que tenga la base de datos
clases = [] #almacena los nombres de las imagenes para que estos se asignen como 'clases' (para la clasificacion de imagenes)
lista = os.listdir(path)

#Lee las imagenes de la carpeta (BD)
for lis in lista:
    #lee imagenes de los rostros
    imgdb = cv2.imread(f'{path}/{lis}')
    #se guarda imagen en arreglo de imagenes
    images.append(imgdb)
    #se guarda el nombre de la persona de la imagen
    clases.append(os.path.splitext(lis)[0])

#imprime todos los nombres de las personas encontradas
print(clases)

#Funcion para codificar los rostros
def codRostros(images):
    listacod = [] #imagenes codificadas

    #iterar sobre cada imagen que existe en la lista de todas las imagenes
    for img in images:
        #correccion de color
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #codificar la imagen
        cod = fr.face_encodings(img)[0]
        #almacenamos la imagen en la lista de imagenes codificadas
        listacod.append(cod)

    return listacod

#Registro de hora de ingreso
def horario(nombre):
    #extraer fecha y hora actual
    info = datetime.now()
    #extraer fecha
    fecha = info.strftime('%d:%m:%Y')
    #extraer la hora
    hora = info.strftime('%H:%M:%S')
    #imprimir la informacion
    print(nombre, fecha, hora)

#llamamos la funcion de codificar
rostroscod = codRostros(images)

#Realizar videocaptura, se conecta a la camara con el indice de la camara a utilizar.
cap = cv2.VideoCapture(0)

#empezar ciclo infinito
while True:
    #leer los fotogramas del video 
    ret, frame = cap.read()

    #reducir el tamaño de las imagenes para un mejor procesamiento
    frame2 = cv2.resize(frame, (0,0), None, 0.25, 0.25)

    #Conversion de color (los fotogramas son en BRG; se tienen que pasar en RGB para el face recognition)
    rgb = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)

    #buscar rostros dentro del video
    faces = fr.face_locations(rgb)
    facescod = fr.face_encodings(rgb, faces) #codifica rostros

    #iteramos sobre todos los rostros que se puedan detectar
    for facecod, faceloc in zip(facescod, faces):
        #comparar rostros de la bd con rostro del video
        comparacion = fr.compare_faces(rostroscod, facecod)

        #calcular la similitud
        simi = fr.face_distance(rostroscod, facecod)
        #buscar valor más bajo de similitudes, entre menor sea el valor, menos diferencia hay por lo que se detecta como dicha persona
        min = np.argmin(simi)

        if comparacion[min]:
            nombre = clases[min].upper()
            
            #se imprime el nombre y hora de acceso
            print (nombre)
            #extrae coordenadas
            horario(nombre)

    
    #mostrar frames
    cv2.imshow("Reconocimiento facial", frame)

    #leemos teclado
    t = cv2.waitKey(5)
    if t==27:
        break

cv2.destroyAllWindows()
cap.release()


    
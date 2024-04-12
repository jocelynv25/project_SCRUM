#Importar librerias
#Face recognition: sirve para el reconocimiento facial

import cv2 
import numpy as np
import face_recognition as fr
import os 
import random
from datetime import datetime

#Acceder a la carpeta en donde se tienen guardadas las imagenes (AQUI TENDRIA QUE SER DE LA BASE DE DATOS)
path = 'imagenes_prueba'
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
        img = cv2.cvtColor(img, cv2.COLORBGR2RGB)
        #codificar la imagen
        cod = fr.face_encodings(img)[0]
        #almacenamos la imagen en la lista de imagenes codificadas
        listacod.append(cod)

    return listacod

#Registro de hora de ingreso



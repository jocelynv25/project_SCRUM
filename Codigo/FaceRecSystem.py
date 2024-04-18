#Importar librerias
import cv2 
import numpy as np
import face_recognition as fr
import os, firebase_admin, requests
import random
from datetime import datetime
import time
from io import BytesIO
from tkinter import Image, messagebox
import subprocess, io
from firebase_admin import credentials, storage

from PIL import Image, ImageTk

cred = credentials.Certificate('Codigo/serviceAccount.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'proyectonoemi-449f2.appspot.com'
})

#path = "C:/Users/jocel/Documents/prueba"
images = [] #almacena todas las imagenes que tenga la base de datos
clases = [] #almacena los nombres de las imagenes para que estos se asignen como 'clases' (para la clasificacion de imagenes)
#lista = os.listdir(path)

def bajar_imagenes(directorio):
    #Accede a bucket de Firebase y lista archivos que contienen un prefijo, 'Intrusos\'    
    bucket = storage.bucket()
    blobs = bucket.list_blobs(prefix=directorio)

    #Itera los blobs (archivos)
    for blob in blobs:
        #Genera una URL temporal
        url = blob.generate_signed_url(version="v4", expiration=3600)
        
        #Solicitud para descargar la imagen con el URL generado
        respuesta = requests.get(url)
        imagen = Image.open(BytesIO(respuesta.content))

        #Almacenamos imágenes sin el prefijo en una lista y se retorna dicha.
        nombre_sin_directorio = blob.name[len(directorio):]
        
        images.append(np.array(imagen)) #convertir imagen a nparray
        clases.append(nombre_sin_directorio)

bajar_imagenes('Inquilinos/')


'''
#Lee las imagenes de la carpeta (local)
for lis in lista:
    #lee imagenes de los rostros
    imgdb = cv2.imread(f'{path}/{lis}')
    #se guarda imagen en arreglo de imagenes
    images.append(imgdb)
    #se guarda el nombre de la persona de la imagen
    clases.append(os.path.splitext(lis)[0])
'''

#imprime todos los nombres de las personas encontradas
print(clases)

#Funcion para codificar los rostros
def codRostros(images):
    listacod = [] #imagenes codificadas

    #iterar sobre cada imagen que existe en la lista de todas las imagenes
    for img in images:
        #correccion de color
        if img is None:
            continue
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
    fecha = info.strftime('%d/%m/%Y')
    #extraer la hora
    hora = info.strftime('%H:%M:%S')
    #imprimir la informacion
    print(nombre, fecha, hora)

def tomar_foto(carpeta, ret, frame, intruso):
    global fotoIntruso
    if ret:
        #Convierte el frame de BGR a RGB
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        #Se guarda en un buffer de bytes
        img_byte_arr = io.BytesIO()

        #Se guarda en formato PNG
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()    
    
        #Nos conectamos con Firebase, creando un bucket, y lo subimos con un blob (almacena datos binarios).
        bucket = storage.bucket()
        nombre = time.strftime("%Y_%m_%d - %H_%M_%S") + '.png'
        nombreFoto = carpeta + nombre
        blob = bucket.blob(nombreFoto)
        blob.upload_from_string(img_byte_arr, 'image/png')
        print("Foto subida con éxito!")
        if intruso:
            fotoIntruso = nombre
    else:   
        print("Fallo en la captura de la imagen.")
    
def showContra(mensaje):
    global fotoIntruso
    pathCONTRA = 'C:/Users/jocel/Documents/project_SCRUM/Codigo/Jonathan/Interfaz Contra.py'
    subprocess.Popen(['python', pathCONTRA, mensaje, fotoIntruso])
    cv2.destroyAllWindows()
    cap.release()

def showAccAut(inquilino):
    pathACC = 'C:/Users/jocel/Documents/project_SCRUM/Codigo/AccAutorizado.py'
    subprocess.Popen(['python', pathACC, inquilino])
    cv2.destroyAllWindows()
    cap.release()

def showMenuAdm():
    pathACC = 'C:/Users/jocel/Documents/project_SCRUM/Codigo/Zayra/MenuAdmin.py'
    subprocess.Popen(['python', pathACC])
    cv2.destroyAllWindows()
    cap.release()


#llamamos la funcion de codificar
rostroscod = codRostros(images)

#Realizar videocaptura, se conecta a la camara con el indice de la camara a utilizar.
cap = cv2.VideoCapture(0)

startTime = time.time()

flag = False
flagWhile = True
attempts = 0
nameFound = ""

while flagWhile:
    
    time.sleep(0.5) #cada segundo se ejecuta el ciclo
    if time.time() - startTime > 10:
        tomar_foto('Intrusos/', ret, frame, True)
        showContra("Se ha excedido el tiempo límite.")
        flagWhile = False
    
    #se detiene después de haber encontrado una similitud con un rostro.
    if flag:
        #time.sleep(3)
        flagWhile = False

        if nameFound == "ADMINISTRADOR":
            time.sleep(1)
            messagebox.showinfo("Acceso correcto", "Ha accedido como administrador.")
            showMenuAdm()
        else:
            #messagebox.showinfo("Acceso autorizado", "Bienvenid@ "+nameFound)
            #print("ACCESO EXITOSO COMO "+nameFound)
            #tomar_foto('Accesos/')
            showAccAut(nameFound)
    
    if attempts >= 4:
        tomar_foto('Intrusos/', ret, frame, True)
        showContra("Se ha excedido el límite de intentos para el reconocimiento.")
        flagWhile = False
    
    #leer los fotogramas del video 
    ret, frame = cap.read()
     #mostrar frames
    cv2.imshow("Reconocimiento facial", frame)

    # Verificar si se pudo leer correctamente el fotograma
    if not ret:
        continue

    #reducir el tamaño de las imagenes para un mejor procesamiento
    frame2 = cv2.resize(frame, (0,0), None, 0.25, 0.25)

    #Conversion de color (los fotogramas son en BRG; se tienen que pasar en RGB para el face recognition)
    rgb = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)

    #buscar rostros dentro del video
    faces = fr.face_locations(rgb)
    facescod = fr.face_encodings(rgb, faces) #codifica rostros

    if len(faces) > 0:
        attempts = attempts + 1
    print("# de intento: ", attempts)
    #iteramos sobre todos los rostros que se puedan detectar
    for facecod, faceloc in zip(facescod, faces):
        #comparar rostros de la bd con rostro del video
        #compara los rostros y devuelve una lista de booleanos que indica si los rostros son considerados como el mismo o no
        comparacion = fr.compare_faces(rostroscod, facecod) 

        #calcular la similitud
        simi = fr.face_distance(rostroscod, facecod) #lista con porcentajes de diferencia
        #buscar valor más bajo de similitudes, entre menor sea el valor, menos diferencia hay por lo que se detecta como dicha persona
        min = np.argmin(simi) #guarda la posicion en donde se almacena el menor porcentaje
        
        #guarda el porcentaje de la similitud
        porcentaje = (1 - np.min(simi))*100

        #si el valor que está como valor minimo de similitudes es true, se imprimen los datos de esta posicion
        if comparacion[min] and porcentaje > 50:
            nombre = clases[min].upper()
            nameFound = nombre[21:-4]
            #se imprime el nombre y hora de acceso
            print ("Persona: ", nombre ," Porcentaje de similitud:", porcentaje,"%")
            #extrae coordenadas
            horario(nombre)
            tomar_foto('Accesos/', ret, frame, False)
            flag = True

    #si se presiona letra scape se sale del ciclo
    t = cv2.waitKey(5)
    if t==27:
        break

cv2.destroyAllWindows()
cap.release()
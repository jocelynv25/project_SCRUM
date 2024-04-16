'''
Librerías externas (ejecutar en cmd):
pip install requests
pip install opencv-python
pip install Pillow
pip install firebase-admin
'''
import subprocess
import cv2, time, os, io, firebase_admin
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from firebase_admin import credentials, storage , db
import face_recognition as fr
import sys

'''
Dentro de este script, tenemos la parte donde, al tomar las fotos, se subirán
a nuestro Storage de Firebase en formato .png, la fecha y hora siendo el nombre 
de cada archivo. 
'''

cred = credentials.Certificate('Codigo/serviceAccount.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'proyectonoemi-449f2.appspot.com',
    'databaseURL': 'https://proyectonoemi-449f2-default-rtdb.firebaseio.com'
})

# Get a database reference to our blog.
ref = db.reference('/')
users_ref = ref.child('Inquilinos')
# Generar un ID único para el usuario
new_user_ref = users_ref.push()
# Obtener la clave generada por push()
idNuevoInquilino = new_user_ref.key

def guardar_datos(nombre , direccion , codigo, urlFoto):
    new_user_ref.set({
        'Fotografia': urlFoto,
        'Codigo': codigo,
        'Direccion': direccion,
        'Nombre' : nombre,
        'Id' : idNuevoInquilino
    })

nombre = sys.argv[1]
direccion = sys.argv[2]
codigo = sys.argv[3]

#Se crea la ventana principal
window = Tk()
window.title("Cámara")
#Ajustar ventana al centro de la pantalla
ancho_ventana = 600
alto_ventana = 520
ancho_pan = window.winfo_screenwidth()
alto_pan = window.winfo_screenheight()
x = (ancho_pan - ancho_ventana) // 2
y = (alto_pan - alto_ventana) // 2 - 50
window.geometry('{}x{}+{}+{}'.format(ancho_ventana, alto_ventana, x, y)) 
window.resizable(False, False)

#Se inicia la captura de video
cam = cv2.VideoCapture(0)

#Si la cámara no abre por cualquier razón, mostrará un mensaje de error.
if not cam.isOpened():
    messagebox.showerror("Error. La cámara no se puede abrir.")
    exit()

#Convierte los frames al formato adecuado.
def actualizar_frame():
    #Toma un frame de la cámara
    ret, frame = cam.read()
    if ret:
        #Convierte el frame de BGR a RGB
        cv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv_img)

        #Lo transforma a un formato de imagen Tkinter
        imgtk = ImageTk.PhotoImage(image=img)

        #Lo muestra en la ventana de nuestra GUI
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)

        #Actualiza el frame cada 10 milisegundos usando recursión.
        lmain.after(10, actualizar_frame)
    else:
        messagebox.showerror("Error: No frame") 

def showMenuAdm():
    #Al cerrar la ventana, se liberan los recursos de cámara y se destruyen las ventanas creadas.
    cam.release()
    cv2.destroyAllWindows()
    pathACC = 'C:/Users/jocel/Documents/project_SCRUM/Codigo/Zayra/MenuAdmin.py'
    subprocess.Popen(['python', pathACC])

#Captura una imagen desde la cámara
def tomar_foto():
    #Toma un frame de la cámara
    ret, frame = cam.read()

    #buscar rostros dentro del video
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = fr.face_locations(rgb)
    if len(faces) == 1: #valida que en la foto haya un solo rostro
        if ret:
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            #Se guarda en un buffer de bytes
            img_byte_arr = io.BytesIO()

            #Se guarda en formato PNG
            image.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            
            #Nos conectamos con Firebase, creando un bucket, y lo subimos con un blob (almacena datos binarios).
            bucket = storage.bucket()
            #La imagen se guarda en /Inquilinos/idusuario.png
            blob = bucket.blob('Inquilinos/'+ idNuevoInquilino + '_' +nombre+ '.png')
            blob.upload_from_string(img_byte_arr, 'image/png')

            urlFoto = idNuevoInquilino + '_' +nombre+ '.png'

            guardar_datos(nombre, direccion, codigo, urlFoto)
            messagebox.showinfo("Cambios guardados", "Nuevo registro añadido con éxito.")
            showMenuAdm()
        else:   
            messagebox.showerror("Fallo en la captura de la imagen.")
    else:
        messagebox.showerror("Error de imagen", "Asegúrese de que sólo se muestre un rostro en la foto e intente de nuevo")

#Se nos mostrará el video en un label
lmain = Label(window)
lmain.pack()

#Botón para poder tomar la foto (opcional)
btn_capturar = Button(window, text="Tomar foto y guardar cambios.", command=tomar_foto)
btn_capturar.pack()

print("Abriendo cámara para la toma de fotografía.")
#Bucle de Tkinter, mantiene ventana abierta y actualiza el contenido
actualizar_frame()
window.mainloop()

#Al cerrar la ventana, se liberan los recursos de cámara y se destruyen las ventanas creadas.
cam.release()
cv2.destroyAllWindows()
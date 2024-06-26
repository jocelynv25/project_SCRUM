import os
import subprocess
import firebase_admin, requests
import tkinter as tk
from tkinter import ttk
from firebase_admin import credentials, storage
from PIL import Image, ImageTk
from io import BytesIO

'''
Dentro de este script, tenemos la interfaz que tomará las fotos del intruso
y las mostrará dentro de una lista y, al dar clic sobre cada una de ellas,
nos mostrará la instatánea tomada
'''


#Inicializamos Firebase con las credenciales de nuestro proyecto
cred = credentials.Certificate('Codigo/serviceAccount.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'proyectonoemi-449f2.appspot.com'
})

print("\nCargando datos de accesos...")

#Almacena las imágenes del directorio dado
def bajar_imagenes(directorio):
    #Accede a bucket de Firebase y lista archivos que contienen un prefijo, 'Intrusos\'    
    bucket = storage.bucket()
    blobs = bucket.list_blobs(prefix=directorio)
    imagenes = []

    #Itera los blobs (archivos)
    for blob in blobs:
        #Genera una URL temporal
        url = blob.generate_signed_url(version="v4", expiration=3600)
        
        #Solicitud para descargar la imagen con el URL generado
        respuesta = requests.get(url)
        imagen = Image.open(BytesIO(respuesta.content))

        #Almacenamos imágenes sin el prefijo en una lista y se retorna dicha.
        nombre_sin_directorio = blob.name[len(directorio):]
        imagenes.append((nombre_sin_directorio, imagen))
    return imagenes

#Captura el evento de selección en la listbox
def seleccion(event):
    #Se obtiene el índice del elemento seleccionado
    index = listbox.curselection()
    
    #Si hay un index, se redimensiona la imagen y se muestra en un campo de Tkinter.
    if index:
        image = imagenes[index[0]][1].resize((400, 300), Image.BICUBIC)
        photo = ImageTk.PhotoImage(image)
        label.image = photo 
        label.config(image=photo)

#Función para cerrar ventana
def cerrar_ventana():
    root.destroy()


def volverMenu():
    pathACC = 'C:/Users/jocel/Documents/project_SCRUM/Codigo/Zayra/MenuAdmin.py'
    subprocess.Popen(['python', pathACC])
    root.destroy()

#Se muestra la ventana principal
root = tk.Tk()
root.title("Accesos")

#Encabezado de sección
header_label = tk.Label(root, text="Fotos de los accesos", font=('Arial', 24), bg='black', fg='white')
header_label.pack(fill=tk.X)

#Posiciona la ventana principal en el centro
height = 530
width = 630
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry('{}x{}+{}-{}'.format(width, height, x, y))

#Se crea y redimensiona un frame para trabajar en él
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

#Se crea una lista para mostrar los nombres de las imágenes
listbox = tk.Listbox(frame, width=50, height=5)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#Se crea un scroll para poder navegar a través de los elementos de la lista
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

#Label para mostrar imagen que se seleccione
label = tk.Label(root)
label.pack(fill=tk.BOTH, expand=True)

#Se usa el evento de selección <<ListboxSelect>> para que llame a la función al presionar un elemento
listbox.bind('<<ListboxSelect>>', seleccion)

#Se llama a la función bajar_imagenes para poder ser mostradas en la interfaz
imagenes = bajar_imagenes('Accesos/') 
for nombre_imagen, _ in imagenes:
    listbox.insert(tk.END, nombre_imagen)

#Botón para cerrar ventana
exit_button = tk.Button(root, text="Salir", command=cerrar_ventana)
exit_button.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

volverbt = tk.Button(root, text="Volver al menú",bg="#0844A4",fg="white",width=12, font=("Arial", 10), command=volverMenu)
volverbt.place(relx=1.0, rely=1.0, anchor='se', x=-520, y=-10)

#Mantiene abierta y en funcionamiento la app hasta cerrarla.
root.mainloop()
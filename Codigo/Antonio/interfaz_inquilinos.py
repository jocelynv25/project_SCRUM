import subprocess
import firebase_admin, requests
import tkinter as tk
from tkinter import ttk
from firebase_admin import credentials, storage, db
from PIL import Image, ImageTk
from io import BytesIO

'''
Dentro de este script, tenemos la interfaz que tomará las fotos del intruso
y las mostrará dentro de una lista y, al dar clic sobre cada una de ellas,
nos mostrará la instatánea tomada
'''

# Inicializamos Firebase con las credenciales de nuestro proyecto
cred = credentials.Certificate('Codigo/serviceAccount.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'proyectonoemi-449f2.appspot.com'
,'databaseURL': 'https://proyectonoemi-449f2-default-rtdb.firebaseio.com'})

print("\n Cargando datos de inquilinos...")

# Función para cargar los datos de la base de datos y mostrarlos en el Listbox
def cargar_datos():
    # Get a database reference to our blog.
    ref = db.reference('/')
    users_ref = ref.child('Inquilinos')
    # Obtener datos de la base de datos
    inquilinos = users_ref.get()
    # Limpiar el Listbox
    listbox.delete(0, tk.END)

    # Insertar los datos en el Listbox
    if inquilinos:
        for inquilino_key, inquilino_data in inquilinos.items():
            id= inquilino_data.get('Id','')
            nombre = inquilino_data.get('Nombre', '')
            direccion = inquilino_data.get('Direccion', '')
            codigo_acceso = inquilino_data.get('Codigo', '')
            listbox.insert(tk.END, f"NOMBRE: {nombre}  DIRECCIÓN:{direccion} CÓDIGO: {codigo_acceso}")
    else:
        listbox.insert(tk.END, "No hay inquilinos registrados")


# Almacena las imágenes de los intrusos
def bajar_imagenes(directorio):
    # Accede a bucket de Firebase y lista archivos que contienen un prefijo, 'Intrusos\'
    bucket = storage.bucket()
    blobs = bucket.list_blobs(prefix=directorio)
    imagenes = []

    # Itera los blobs (archivos)
    for blob in blobs:
        # Genera una URL temporal
        url = blob.generate_signed_url(version="v4", expiration=3600)

        # Solicitud para descargar la imagen con el URL generado
        respuesta = requests.get(url)
        imagen = Image.open(BytesIO(respuesta.content))

        # Almacenamos imágenes sin el prefijo en una lista y se retorna dicha.
        nombre_sin_directorio = blob.name[len(directorio):]
        imagenes.append((nombre_sin_directorio, imagen))
    return imagenes


# Captura el evento de selección en la listbox
def seleccion(event):
    # Se obtiene el índice del elemento seleccionado
    index = listbox.curselection()
    # Si hay un index, se redimensiona la imagen y se muestra en un campo de Tkinter.
    if index:
        image = imagenes[index[0]][1].resize((400, 300), Image.BICUBIC)
        photo = ImageTk.PhotoImage(image)
        label.image = photo
        label.config(image=photo)


# Función para cerrar ventana
def salir():
    root.destroy()

def volverMenu():
    pathACC = 'C:/Users/jocel/Documents/project_SCRUM/Codigo/Zayra/MenuAdmin.py'
    subprocess.Popen(['python', pathACC])
    root.destroy()

# Se muestra la ventana principal
root = tk.Tk()
root.title("Inquilinos.")

# Encabezado de sección
header_label = tk.Label(root, text="Inquilinos", font=('Arial', 24), bg='#7DD6FC', fg='white',bd=2, highlightbackground="black")
header_label.pack(fill=tk.X)

# Posiciona la ventana principal en el centro
height = 530
width = 630
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}-{}'.format(width, height, x, y))

# Se crea y redimensiona un frame para trabajar en él
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Se crea una lista para mostrar los nombres de las imágenes
listbox = tk.Listbox(frame, width=50, height=5,font=("Arial",12),bg="white",justify="center")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Se crea un scroll para poder navegar a través de los elementos de la lista
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

# Label para mostrar imagen que se seleccione
label = tk.Label(root)
label.pack(fill=tk.BOTH, expand=True)

# Se usa el evento de selección <<ListboxSelect>> para que llame a la función al presionar un elemento
listbox.bind('<<ListboxSelect>>', seleccion)

# Se llama a la función bajar_imagenes para poder ser mostradas en la interfaz
imagenes = bajar_imagenes('Inquilinos/')
cargar_datos()
#for nombre_imagen, _ in imagenes:
 #   listbox.insert(tk.END, nombre_imagen)

# Botón para cerrar ventana
exit_button = tk.Button(root, text="Salir",bg="red",fg="white",width=10, font=("Arial", 12), command=salir)
exit_button.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

volverbt = tk.Button(root, text="Volver al menú",bg="#0844A4",fg="white",width=12, font=("Arial", 10), command=volverMenu)
volverbt.place(relx=1.0, rely=1.0, anchor='se', x=-520, y=-10)
# Mantiene abierta y en funcionamiento la app hasta cerrarla.
root.mainloop()
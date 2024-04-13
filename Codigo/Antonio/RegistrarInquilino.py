import subprocess
import firebase_admin
from firebase_admin import credentials , db

import tkinter as tk

cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://proyectonoemi-449f2-default-rtdb.firebaseio.com'})

# Get a database reference to our blog.
ref = db.reference('/')
users_ref = ref.child('Inquilinos')

def guardar_datos(nombre , direccion , codigo):
    # Generar un ID único para el usuario
    new_user_ref = users_ref.push()
    # Obtener la clave generada por push()
    new_user_key = new_user_ref.key
    new_user_ref.set({
        'Fotografia': "",
        'Codigo de Acceso': codigo,
        'Direccion': direccion,
        'Nombre' : nombre,
        'Id' : new_user_key
    })
    ##Enviar los datos al otro programa
    subprocess.Popen(['python', 'reconocimiento.py', nombre, direccion, codigo, new_user_key])

def procesar_datos():
    nombre = entry_nombre.get()
    direccion = entry_direccion.get()
    codigo_acceso = entry_codigo.get()
    # Aquí puedes realizar cualquier función que desees con los datos
    guardar_datos(nombre,direccion,codigo_acceso)
    # Borra el contenido de los Entry después de guardar los datos
    entry_nombre.delete(0, 'end')
    entry_direccion.delete(0, 'end')
    entry_codigo.delete(0, 'end')
    # Llamar al programa que abre la cámara y pasar los datos como argumentos de línea de comandos

def cerrar_y_abrir():
    # Cierra la ventana actual
    ventana.destroy()
    # Abre la nueva ventana
    abrir_nueva_ventana()

# Crear ventana
Ventana = tk.Tk()
Ventana.title("Registrar Inquilino")
# Obtener dimensiones de la pantalla
screen_width = Ventana.winfo_screenwidth()
screen_height = Ventana.winfo_screenheight()
# Definir dimensiones y calcular posición para centrar la ventana
window_width = 400
window_height = 200
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
# Establecer la geometría de la ventana
Ventana.geometry(f"{window_width}x{window_height}+{x}+{y}")
# Etiqueta y entrada para Nombre
label_nombre = tk.Label(Ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(Ventana, width=40)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

# Etiqueta y entrada para Dirección
label_direccion = tk.Label(Ventana, text="Dirección:")
label_direccion.grid(row=1, column=0, padx=10, pady=5)
entry_direccion = tk.Entry(Ventana, width=40)
entry_direccion.grid(row=1, column=1, padx=10, pady=5)

# Etiqueta y entrada para Código de Acceso
label_codigo = tk.Label(Ventana, text="Código de Acceso:")
label_codigo.grid(row=2, column=0, padx=10, pady=5)
entry_codigo = tk.Entry(Ventana, width=40)
entry_codigo.grid(row=2, column=1, padx=10, pady=5)

# Botón para procesar los datos
boton_procesar = tk.Button(Ventana, text="Procesar DatOS", command=procesar_datos)
boton_procesar.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Iniciar la aplicación
Ventana.mainloop()

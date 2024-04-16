import os, cv2
import subprocess
import firebase_admin
from firebase_admin import credentials , db

import tkinter as tk

def btnSiguiente():
    nombre = entry_nombre.get()
    direccion = entry_direccion.get()
    codigo = entry_codigo.get()

    #Borrar contenido de los entry ???

    #Enviar los datos al programa de la toma de fotografía
    subprocess.Popen(['python', 'Codigo/Juan Angel/tomarFotoInquilinos.py', nombre, direccion, codigo])
    Ventana.withdraw()

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
boton_procesar = tk.Button(Ventana, text="Siguiente", command=btnSiguiente)
boton_procesar.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Iniciar la aplicación
Ventana.mainloop()
#cv2.destroyAllWindows()
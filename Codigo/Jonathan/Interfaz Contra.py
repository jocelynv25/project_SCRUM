import tkinter as tk
from tkinter import messagebox

import sys

# Función para verificar la contraseña
def verificar_contraseña():
    # Aquí se implementaría la lógica para comparar la contraseña con la base de datos
    # Por ahora, solo se muestra un mensaje de error
    messagebox.showerror("Error", "Error: contraseña incorrecta, ingresar su contraseña o contactar a su administrador")

# Función para salir de la aplicación
def salir():
    ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Acceso por código")
ventana.resizable(True, True)  # Permitir que la ventana sea redimensionable

#Obtener coordenadas de la pantalla del ordenador
ancho_ventana = 300
alto_ventana = 200
ancho_pan = ventana.winfo_screenwidth()
alto_pan = ventana.winfo_screenheight()
x = (ancho_pan - ancho_ventana) // 2
y = (alto_pan - alto_ventana) // 2
ventana.geometry('{}x{}+{}+{}'.format(ancho_ventana, alto_ventana, x, y)) 

# Crear un label para la contraseña
label_contraseña = tk.Label(ventana, text="Contraseña:")
label_contraseña.pack()

# Crear un textbox para ingresar la contraseña
textbox_contraseña = tk.Entry(ventana, show="*")
textbox_contraseña.pack()

# Crear un botón para verificar la contraseña
boton_verificar = tk.Button(ventana, text="Verificar", command=verificar_contraseña)
boton_verificar.pack()

# Crear un botón para salir de la aplicación
boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack()

# Ejecutar la aplicación
mensaje = sys.argv[1]
messagebox.showerror("Acceso denegado", mensaje +"\nIngrese su código de acceso.")
ventana.mainloop()

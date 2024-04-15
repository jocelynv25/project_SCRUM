import tkinter as tk
from tkinter import messagebox

import sys

# Función para salir de la aplicación
def salir():
    ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Acceso autorizado")
ventana.resizable(False, False)  # Permitir que la ventana sea redimensionable

#Obtener coordenadas de la pantalla del ordenador
ancho_ventana = 200
alto_ventana = 100
ancho_pan = ventana.winfo_screenwidth()
alto_pan = ventana.winfo_screenheight()
x = (ancho_pan - ancho_ventana) // 2
y = (alto_pan - alto_ventana) // 2
ventana.geometry('{}x{}+{}+{}'.format(ancho_ventana, alto_ventana, x, y)) 

# Crear un label para la contraseña
inquilino = sys.argv[1]
label = tk.Label(ventana, text="ACCESO AUTORIZADO \n Bienvenid@ "+inquilino)
label.pack()

# Crear un botón para salir de la aplicación
boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack()

# Ejecutar la aplicación
ventana.mainloop()

import tkinter as tk
from tkinter import messagebox

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
ventana.title("Acceso")
ventana.geometry("300x200")  # Tamaño inicial de la ventana
ventana.resizable(True, True)  # Permitir que la ventana sea redimensionable

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
ventana.mainloop()

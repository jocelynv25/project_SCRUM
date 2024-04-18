import os

import subprocess
import tkinter as tk
from tkinter import messagebox

import cv2
def salir():
    # Llamada llamar el método mainloop() para cambiar de ventana 
    ventana.destroy()

def showRegister():
    subprocess.Popen(['python', 'C:/Users/jocel/Documents/project_SCRUM/Codigo/Antonio/RegistrarInquilino.py'])
    ventana.withdraw()

def showBorrar():
    subprocess.Popen(['python', 'C:/Users/jocel/Documents/project_SCRUM/Codigo/Karla/sistema.py'])
    ventana.withdraw()

def showConsultarAcc():
    subprocess.Popen(['python', 'Codigo/Juan Angel/interfaz_accesos.py'])
    ventana.withdraw()

def showConsultarInt():
    subprocess.Popen(['python', 'Codigo/Juan Angel/interfaz_intrusos.py'])
    ventana.withdraw()

def showConsultarInq():
    subprocess.Popen(['python', 'Codigo/Antonio/interfaz_inquilinos.py'])
    ventana.withdraw()

def showConsulAccCod():
    subprocess.Popen(['python', 'Codigo/interfaz_accporcod.py'])
    ventana.withdraw()

    
ventana = tk.Tk()
ventana.title("Menú del administrador")

#Ajusta la ventana 
ancho_ventana = 300
alto_ventana = 480

ventana.minsize(width=ancho_ventana, height=alto_ventana)
ventana.maxsize(width=ancho_ventana, height=alto_ventana)
ventana.config(padx=35, pady=35)

ancho_pan = ventana.winfo_screenwidth()
alto_pan = ventana.winfo_screenheight()
x = (ancho_pan - ancho_ventana) // 2
y = (alto_pan - alto_ventana) // 2
ventana.geometry('{}x{}+{}+{}'.format(ancho_ventana, alto_ventana, x, y)) 

#Logotipo del menú
dir_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(dir_path, 'A.png')
img = tk.PhotoImage(file=path)
img = img.subsample(7, 7)  

# mostrar la imagen como icono
lbl_icono = tk.Label(ventana, image=img)
lbl_icono.grid(column=0, row=0, padx=1, pady=1, sticky="nsew") 

ventana.grid_rowconfigure(2, weight=1)
ventana.grid_columnconfigure(2, weight=1)

ventana.resizable(False, False)
 
titulo = tk.Label(ventana, text="Menu", font=("Arial", 20))
titulo.grid(column=0,row=1,padx=10, pady=10)


#Botones
boton1=tk.Button(ventana, text="Registrar nuevo inquilino", command = showRegister, fg="white", font=("Helvetica", 14),width=20, height=1, bg="#0844A4")
boton1.grid(column=0,row=3, padx=5, pady=5)

boton2=tk.Button(ventana, text="Consultar inquilinos", command = showConsultarInq, fg="white",  font=("Helvetica", 14),width=20, height=1,bg="#0844A4")
boton2.grid(column=0,row=4, padx=5, pady=5)

boton3=tk.Button(ventana, text="Consultar accesos", command = showConsultarAcc, fg="white", font=("Helvetica", 14),width=20, height=1,bg="#0844A4")
boton3.grid(column=0,row=5, padx=5, pady=5)

boton4=tk.Button(ventana, text="Consultar intrusos", command = showConsultarInt, fg="white", font=("Helvetica", 14),width=20, height=1,bg="#0844A4")
boton4.grid(column=0,row=6, padx=5, pady=5)

boton4=tk.Button(ventana, text="Ver accesos por código", command = showConsulAccCod, fg="white", font=("Helvetica", 14),width=20, height=1,bg="#0844A4")
boton4.grid(column=0,row=7, padx=5, pady=5)

boton5=tk.Button(ventana, text="Salir", command = salir, fg="white",  font=("Helvetican", 14),bg="#3D8AF7")
boton5.grid(column=0,row=8, padx=8, pady=8)

#messagebox.showinfo("Acceso correcto", "Ha accedido como administrador.")
ventana.mainloop()
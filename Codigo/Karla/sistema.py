import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def showFaceRec():
    messagebox.showinfo("Entrando al sistema", "Cargando el sistema de reconocimiento facial...")
    subprocess.Popen(['python', 'C:/Users/jocel/Documents/project_SCRUM/Codigo/FaceRecSystem.py'])
    ventana1.withdraw()


ventana1 = tk.Tk()
ventana1.title("Bienvenido al Sistema de Reconocimiento Facial")
ventana1.configure(bg='#FFFFFF')  
ventana1.resizable(False, False)

ancho_ventana = 500
alto_ventana = 350
ancho_pan = ventana1.winfo_screenwidth()
alto_pan = ventana1.winfo_screenheight()
x = (ancho_pan - ancho_ventana) // 2
y = (alto_pan - alto_ventana) // 2
ventana1.geometry('{}x{}+{}+{}'.format(ancho_ventana, alto_ventana, x, y)) 

marco_principal = tk.Frame(ventana1, bg="#0844A4", padx=10, pady=10)  #  margen azul
marco_principal.pack(expand=True, fill="both")

dir_path = os.path.dirname(os.path.realpath(__file__))
pathIMG = os.path.join(dir_path, 'casita.png')
imagen = Image.open(pathIMG)
imagen_tk = ImageTk.PhotoImage(imagen)

imagen_label = tk.Label(ventana1, image=imagen_tk, bg='#FFFFFF')
imagen_label.pack(pady=5) 

frame_contenedor = tk.Frame(ventana1, bg='#FFFFFF')
frame_contenedor.pack(expand=True)

cuadro_texto = tk.Label(frame_contenedor, text="SISTEMA DE RECONOCIMIENTO FACIAL", font=("Arial", 14), bg='#FFFFFF')
cuadro_texto.pack(pady=5) 

boton_entrar = tk.Button(frame_contenedor, text="ENTRAR AL SISTEMA", bg='#0844A4', fg="white", font=("Arial", 12), command=showFaceRec)
boton_entrar.pack(pady=5, padx=50, ipadx=10, ipady=3)  

ventana1.mainloop()
 
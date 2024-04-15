import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def abrir_ventana2():
    ventana1.withdraw()  
    
    ventana2 = tk.Toplevel()
    ventana2.title("Sistema de Reconocimiento Facial")
    ventana2.geometry("400x200")
    
    etiqueta = tk.Label(ventana2, text="¡Has entrado al sistema!", font=("Arial", 20))
    etiqueta.pack(pady=50)


ventana1 = tk.Tk()
ventana1.title("Bienvenido al Sistema de Reconocimiento Facial")
ventana1.geometry("400x400")
ventana1.configure(bg='#FFFFFF')  

marco_principal = tk.Frame(ventana1, bg='blue', padx=10, pady=10)  #  margen azul
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

boton_entrar = tk.Button(frame_contenedor, text="ENTRAR AL SISTEMA", bg='#000099', fg="white", font=("Arial", 12), command=abrir_ventana2)
boton_entrar.pack(pady=5, padx=50, ipadx=10, ipady=3)  

ventana1.mainloop()
 
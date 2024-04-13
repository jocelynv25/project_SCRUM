import tkinter as tk
def salir():
    # Llamada llamar el método mainloop() para cambiar de ventana 
    ventana.destroy()


def cambiar():
    # Llamada llamar el método mainloop() para cambiar de ventana 
    ventana1.deiconify()
    ventana.withdraw() 
    
ventana = tk.Tk()
ventana.title("Menu")

#Ajusta la ventana 
ventana.minsize(width=300, height=500)
ventana.maxsize(width=300, height=500)
ventana.config(padx=35, pady=35)

img = tk.PhotoImage(file="R.png")
img = img.subsample(7, 7)  

# mostrar la imagen como icono
lbl_icono = tk.Label(ventana, image=img)
lbl_icono.grid(column=0, row=0, padx=1, pady=1, sticky="nsew") 

ventana.grid_rowconfigure(2, weight=1)
ventana.grid_columnconfigure(2, weight=1)

ventana.resizable(False, False)

#Agrega un titulo 
 
titulo = tk.Label(ventana, text="Menu", font=("Arial", 14))
titulo.grid(column=0,row=1,padx=30, pady=30)


#Crean los botones 

boton1=tk.Button(ventana, text="Registrar nuevo inquilino", command = cambiar, font=("Times New Roman", 14),width=20, height=1, bg="blue")
boton1.grid(column=0,row=3, padx=5, pady=5)

boton2=tk.Button(ventana, text="Borrar inquilino",command = cambiar,  font=("Times New Roman", 14),width=20, height=1,bg="blue")
boton2.grid(column=0,row=4, padx=5, pady=5)
boton3=tk.Button(ventana, text="Consultar acceso",command = cambiar, font=("Times New Roman", 14),width=20, height=1,bg="blue")
boton3.grid(column=0,row=5, padx=5, pady=5)

boton4=tk.Button(ventana, text="Consultar intrusos",command = cambiar, font=("Times New Roman", 14),width=20, height=1,bg="blue")
boton4.grid(column=0,row=6, padx=5, pady=5)
boton5=tk.Button(ventana, text="Salir",command = salir,  font=("Times New Roman", 14),bg="red")
boton5.grid(column=0,row=10, padx=40, pady=40)

# cambia de ventana cerrando la actual 
ventana1 = tk.Toplevel()
ventana1.title("Ventana 1")
ventana1.withdraw()
ventana.mainloop()


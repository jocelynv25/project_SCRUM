import subprocess
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import firebase_admin
from firebase_admin import credentials , db

cred = credentials.Certificate("Codigo/serviceAccount.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://proyectonoemi-449f2-default-rtdb.firebaseio.com'})
# Get a database reference to our blog.
ref = db.reference('/')
users_ref = ref.child('Inquilinos')

global nameFound

def showAccAut(inquilino):
    pathACC = 'C:/Users/jocel/Documents/project_SCRUM/Codigo/AccAutorizado.py'
    subprocess.Popen(['python', pathACC, inquilino])
    cv2.destroyAllWindows()
    ventana.withdraw()

# Función para verificar la contraseña
def verificar_contraseña():
    valor_buscado = textbox_contraseña.get()
    # Aquí se implementaría la lógica para comparar la contraseña con la base de datos
    referencia = db.reference('/Inquilinos')# Referencia a la raíz de la base de datos
    data = referencia.get()# Obtener los datos de la base de datos
    # Llamar a la función buscar_valor con los datos de la base de datos y el valor buscado
    if not buscar_valor(data, valor_buscado):
        messagebox.showerror("Error","Error: Codigo de Acceso incorrecto"+"\n  Ingresar su Codigo de Acceso o Contactar a su Administrador")
    else:
        showAccAut(nameFound)



# Función para salir de la aplicación
def salir():
    ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Acceso por código")
ventana.resizable(False, False)  # Permitir que la ventana sea redimensionable

#Obtener coordenadas de la pantalla del ordenador
ancho_ventana = 300
alto_ventana = 300
ancho_pan = ventana.winfo_screenwidth()
alto_pan = ventana.winfo_screenheight()
x = (ancho_pan - ancho_ventana) // 2
y = (alto_pan - alto_ventana) // 2
ventana.geometry('{}x{}+{}+{}'.format(ancho_ventana, alto_ventana, x, y))
# Configurar el color de fondo de la ventana a blanco
ventana.configure(bg="white")

# Abrir la imagen
imagen_pillow = Image.open("Codigo/Jonathan/CodigoAcceso.jpg")
imagenRed=imagen_pillow.resize((120, 120)) #Redimensionar
# Convertir la imagen de Pillow a un formato compatible con Tkinter
imagen = ImageTk.PhotoImage(imagenRed)
# Crear un widget Label para mostrar la imagen
label_imagen = tk.Label(ventana, image=imagen,highlightthickness=0,bd=0)
label_imagen.pack()

# Crear un label para la contraseña
label_contraseña = tk.Label(ventana, text="Codigo de Acceso", font=("Helvetica", 24), bg="white")
label_contraseña.pack()

# Crear un textbox para ingresar la contraseña
textbox_contraseña = tk.Entry(ventana, show="*", width=10, bg="gray",fg="white", font=("Arial", 24), justify="center")
textbox_contraseña.pack()

# Crear un botón para verificar la contraseña
boton_verificar = tk.Button(ventana, text="Verificar",bg="#0844A4",fg="white",width=10, font=("Arial", 12), command=verificar_contraseña)
boton_verificar.pack()

# Crear un botón para salir de la aplicación
boton_salir = tk.Button(ventana, text="Salir",bg="#3D8AF7",fg="white",width=10, font=("Arial", 12), command=salir)
boton_salir.pack(side="bottom", anchor="se",padx=10, pady=10)
#Metodo para buscar el valor en la base de Datos
def buscar_valor(objeto, valor_buscado):
    global nameFound

    if isinstance(objeto, dict):
        if "Codigo" in objeto and objeto["Codigo"] == valor_buscado:
            print(f"El valor '{valor_buscado}' se encontró en la clave 'Codigo de Acceso'")
            nameFound = objeto.get("Nombre")
            print(objeto.get("Nombre")) #Recuperar el nombre del Inquilino con ese Codigo de Acceso
            return True  # Valor encontrado
        else:
            for value in objeto.values():
                if isinstance(value, (dict, list)):
                    if buscar_valor(value, valor_buscado):
                        print("encontrado")
                        return True  # Valor encontrado en la recursión
    elif isinstance(objeto, list):
        for item in objeto:
            if buscar_valor(item, valor_buscado):
                print("encontrado")
                return True  # Valor encontrado en la recursión
    return False  # Valor no encontrado

# Ejecutar la aplicación
#mensaje = sys.argv[1]
#messagebox.showerror("Acceso denegado", mensaje +"\nIngrese su código de acceso.")
#messagebox.showerror("Acceso denegado", "\nIngrese su código de acceso.")
ventana.mainloop()
